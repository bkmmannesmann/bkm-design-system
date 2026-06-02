#!/usr/bin/env node
/**
 * BKM Images — brand-conform image generation via the OpenAI Image API.
 *
 * Builds a BKM Mannesmann brand-conform prompt (see PROMPT_LIBRARY.md) and
 * generates images with `gpt-image-1` ("OpenAI Images 2.0").
 *
 * Requirements:
 *   - Node.js >= 18 (uses global fetch; NO npm install needed)
 *   - env OPENAI_API_KEY
 *
 * Usage:
 *   node generate.mjs --usecase slide --context ag \
 *     --motif "concrete basement wall with a horizontal moisture barrier line"
 *
 *   node generate.mjs --usecase social --context fachbetrieb --ratio story \
 *     --motif "renovated facade in daylight" --dry-run
 *
 * Flags:
 *   --usecase   slide | website | social | product        (default: slide)
 *   --context   ag | fachbetrieb                           (default: ag)
 *   --motif     subject in English (repeatable for a batch) (required unless --dry-run defaults)
 *   --ratio     square | story | landscape  (mainly for social; overrides size)
 *   --size      1024x1024 | 1536x1024 | 1024x1536 | auto   (overrides usecase default)
 *   --quality   low | medium | high | auto                 (default: high)
 *   --count     N copies per motif                         (default: 1)
 *   --out       output directory                           (default: ./output)
 *   --dry-run   print the assembled prompt(s), do not call the API
 */

import { writeFile, mkdir } from "node:fs/promises";
import { join, resolve } from "node:path";

// ---------------------------------------------------------------------------
// Brand prompt building blocks (mirror of PROMPT_LIBRARY.md — keep in sync)
// ---------------------------------------------------------------------------

const BASE_STYLE =
  "Editorial documentary photograph in the BKM Mannesmann visual language. " +
  "Shot on a medium format camera, dramatic natural lighting, high contrast, " +
  "shallow depth of field, muted earth-tone color grade, realistic materials " +
  "and textures (concrete, masonry, mineral surfaces, water, greenery). " +
  "Authentic and emotional, never generic stock photography. Generous negative " +
  "space for a later text overlay. Photorealistic.";

const CONTEXT = {
  ag:
    "Mood: deep, protective, authoritative. Dominant deep teal-green tonality " +
    "(#1c4b42) in shadows and atmosphere, cool muted palette, dramatic low-key " +
    "lighting. A single subtle lime-green highlight accent (#b4e717) as a light " +
    "edge or one small material detail — used sparingly, never covering large areas.",
  fachbetrieb:
    "Mood: clean, trustworthy, hands-on. Bright warm daylight, sand-white " +
    "ambience (#f6f5f2), airy and documentary. Fresh pure-green accents " +
    "(#4daf46) from vegetation, signage edges or treated surfaces. Absolutely " +
    "no lime-green.",
};

const USE_CASE = {
  slide:
    "Composition for a 16:9 presentation background. Keep the right third and " +
    "the upper area calm and uncluttered for a glassmorphism card and a chevron " +
    "keyvisual overlay. Cinematic wide framing.",
  website:
    "Wide hero composition for a website header. Strong focal subject on the " +
    "left, clean negative space on the right for headline text. Cinematic, " +
    "premium, landscape framing.",
  social:
    "Square social-media composition. Centered, bold focal subject with " +
    "breathing room around it (10% safe margin on every side). Scroll-stopping " +
    "but editorial.",
  "social:story":
    "Vertical 9:16 story composition. Strong subject in the central safe zone, " +
    "calm space at the top and bottom thirds for overlaid text and a logo.",
  product:
    "Product-and-architecture hero. Clean, deliberate staging of the material, " +
    "detail or building element as the hero. Studio-grade natural light, precise " +
    "focus on texture and surface. Premium, technical, trustworthy.",
};

const NEGATIVE =
  "No text, no words, no letters, no numbers, no captions, no logos, no brand " +
  "marks, no watermarks, no signatures, no UI elements or browser chrome. No " +
  "aurora gradients, no neon, no noise overlay, no 3D render look, no cartoon " +
  "or illustration style, no oversaturated HDR. Not a flat graphic — a real " +
  "photograph.";

const DEFAULT_SIZE = {
  slide: "1536x1024",
  website: "1536x1024",
  social: "1024x1024",
  product: "1024x1024",
};

const RATIO_SIZE = {
  square: "1024x1024",
  landscape: "1536x1024",
  story: "1024x1536",
};

const VALID_SIZES = ["1024x1024", "1536x1024", "1024x1536", "auto"];
const API_URL = "https://api.openai.com/v1/images/generations";

// ---------------------------------------------------------------------------
// Arg parsing (supports repeated --motif)
// ---------------------------------------------------------------------------

function parseArgs(argv) {
  const opts = {
    usecase: "slide",
    context: "ag",
    motifs: [],
    ratio: null,
    size: null,
    quality: "high",
    count: 1,
    out: "./output",
    dryRun: false,
  };
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    const next = () => argv[++i];
    switch (a) {
      case "--usecase": opts.usecase = next(); break;
      case "--context": opts.context = next(); break;
      case "--motif": opts.motifs.push(next()); break;
      case "--ratio": opts.ratio = next(); break;
      case "--size": opts.size = next(); break;
      case "--quality": opts.quality = next(); break;
      case "--count": opts.count = parseInt(next(), 10); break;
      case "--out": opts.out = next(); break;
      case "--dry-run": opts.dryRun = true; break;
      case "--help": case "-h": printHelp(); process.exit(0); break;
      default:
        console.error(`Unknown flag: ${a}`);
        process.exit(1);
    }
  }
  return opts;
}

function printHelp() {
  console.log(`BKM Images — generate brand-conform images via gpt-image-1

  --usecase  slide | website | social | product   (default: slide)
  --context  ag | fachbetrieb                      (default: ag)
  --motif    subject in English (repeat for batch)
  --ratio    square | story | landscape            (mainly for social)
  --size     ${VALID_SIZES.join(" | ")}
  --quality  low | medium | high | auto            (default: high)
  --count    copies per motif                      (default: 1)
  --out      output directory                      (default: ./output)
  --dry-run  print prompt(s) only, no API call

Requires env OPENAI_API_KEY (unless --dry-run).`);
}

// ---------------------------------------------------------------------------
// Prompt assembly
// ---------------------------------------------------------------------------

function buildPrompt({ usecase, context, ratio, motif }) {
  if (!CONTEXT[context]) {
    throw new Error(`Invalid --context "${context}". Use: ag | fachbetrieb.`);
  }
  let useKey = usecase;
  if (usecase === "social" && ratio === "story") useKey = "social:story";
  if (!USE_CASE[useKey]) {
    throw new Error(
      `Invalid --usecase "${usecase}". Use: slide | website | social | product.`
    );
  }
  return [
    BASE_STYLE,
    CONTEXT[context],
    USE_CASE[useKey],
    `Subject: ${motif}.`,
    NEGATIVE,
  ].join(" ");
}

function resolveSize({ usecase, ratio, size }) {
  if (size) {
    if (!VALID_SIZES.includes(size)) {
      throw new Error(`Invalid --size "${size}". Use: ${VALID_SIZES.join(" | ")}.`);
    }
    return size;
  }
  if (ratio) {
    if (!RATIO_SIZE[ratio]) {
      throw new Error(`Invalid --ratio "${ratio}". Use: square | story | landscape.`);
    }
    return RATIO_SIZE[ratio];
  }
  return DEFAULT_SIZE[usecase] || "1024x1024";
}

function slug(s) {
  return s.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "").slice(0, 40);
}

// ---------------------------------------------------------------------------
// OpenAI API call
// ---------------------------------------------------------------------------

async function generate({ prompt, size, quality, apiKey }) {
  const res = await fetch(API_URL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${apiKey}`,
    },
    body: JSON.stringify({ model: "gpt-image-1", prompt, n: 1, size, quality }),
  });
  if (!res.ok) {
    const body = await res.text();
    throw new Error(`OpenAI API ${res.status}: ${body}`);
  }
  const data = await res.json();
  const b64 = data?.data?.[0]?.b64_json;
  if (!b64) throw new Error("API returned no image data.");
  return Buffer.from(b64, "base64");
}

// ---------------------------------------------------------------------------
// Main
// ---------------------------------------------------------------------------

async function main() {
  const opts = parseArgs(process.argv.slice(2));
  if (opts.motifs.length === 0) {
    console.error("Error: at least one --motif is required.\n");
    printHelp();
    process.exit(1);
  }

  const size = resolveSize(opts);
  const jobs = [];
  for (const motif of opts.motifs) {
    const prompt = buildPrompt({ ...opts, motif });
    for (let c = 0; c < opts.count; c++) {
      jobs.push({ motif, prompt, copy: c });
    }
  }

  if (opts.dryRun) {
    console.log(`# DRY RUN — ${jobs.length} prompt(s), size ${size}, quality ${opts.quality}\n`);
    for (const j of jobs) {
      console.log(`## ${j.motif}${opts.count > 1 ? ` (copy ${j.copy + 1})` : ""}`);
      console.log(j.prompt + "\n");
    }
    return;
  }

  const apiKey = process.env.OPENAI_API_KEY;
  if (!apiKey) {
    console.error("Error: OPENAI_API_KEY is not set.");
    process.exit(1);
  }

  const outDir = resolve(opts.out);
  await mkdir(outDir, { recursive: true });

  console.log(`Generating ${jobs.length} image(s) → ${outDir} (size ${size}, quality ${opts.quality})`);
  let n = 0;
  for (const j of jobs) {
    n++;
    const label = `[${n}/${jobs.length}] ${j.motif}`;
    try {
      console.log(`${label} — requesting…`);
      const buf = await generate({ prompt: j.prompt, size, quality: opts.quality, apiKey });
      const stamp = Date.now();
      const file = join(
        outDir,
        `bkm-${opts.context}-${opts.usecase}-${slug(j.motif)}-${stamp}.png`
      );
      await writeFile(file, buf);
      console.log(`${label} — saved ${file}`);
    } catch (err) {
      console.error(`${label} — FAILED: ${err.message}`);
    }
  }
  console.log("Done.");
}

main().catch((err) => {
  console.error(err.message || err);
  process.exit(1);
});
