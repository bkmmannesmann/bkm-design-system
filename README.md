# BKM Mannesmann Design System

> The single source of truth for all visual and communicative guidelines of BKM Mannesmann AG — optimized for AI agents, developers, and designers.

[![Version](https://img.shields.io/badge/version-1.1.0-brightgreen)]()
[![Format](https://img.shields.io/badge/format-DESIGN.md-blue)]()
[![awesome-design-md](https://img.shields.io/badge/awesome--design--md-compatible-orange)](https://github.com/VoltAgent/awesome-design-md)

## Overview

This repository contains the complete design system for BKM Mannesmann AG, a manufacturer of building protection products specializing in moisture barriers and injection technologies. The system is structured in the [awesome-design-md](https://github.com/VoltAgent/awesome-design-md) format — machine-readable YAML tokens + human-readable prose documentation.

### What's Inside

| File | Purpose | Lines |
|------|---------|-------|
| `DESIGN.md` | Complete design tokens (colors, typography, spacing, shadows, components, animations, responsive) + documentation | 700+ |
| `AGENTS.md` | Instructions for AI coding agents + CSS variables template + Tailwind v4 config | 200+ |
| `docs/brand-voice.md` | Tone, claims, copy patterns, UI text guidelines | |
| `docs/digitale-medien.md` | Web/app implementation details, CSS variables, Dark Mode | |
| `docs/print-anwendungen.md` | Print specifications (brochures, TDS, labels, vehicles) | |
| `docs/microporex-und-technik.md` | Ingredient brand rules, naming, file formats | |
| `docs/keyvisual.md` | Chevron pattern specifications and placement | |
| `docs/logo.md` | Logo variants, clear space, positioning | |
| `docs/icon-system.md` | Icon specifications | |
| `docs/referenzen.md` | External design system references (Vercel, MongoDB, NVIDIA, Mintlify, Supabase) | |
| `docs/verbesserungsvorschlaege.md` | Improvement proposals based on reference analysis | |
| `docs/bkm-slide-prompt.md` | Reusable slide prompt with exact CSS tokens (v3) | |
| `skills/bkm-slides/SKILL.md` | Slide skill entry point — mandatory workflow for slide creation | |
| `skills/bkm-slides/STYLE_PRESETS.md` | Exact CSS tokens for glassmorphism slides (both contexts) | |
| `skills/bkm-slides/html-template.md` | Complete copy-paste HTML templates for all slide types | |
| `skills/bkm-slides/PATTERN_CATALOG.md` | Allowed and forbidden patterns with exact CSS values | |
| `skills/bkm-images/SKILL.md` | Brand-conform image generation via OpenAI Images (`gpt-image-1`) | |
| `skills/bkm-images/PROMPT_LIBRARY.md` | Brand prompt building blocks per use case + context | |
| `skills/bkm-images/generate.mjs` | Runnable CLI that builds the brand prompt and calls the OpenAI Image API | |

## Quick Start

### For AI Agents (Cursor, Copilot, Manus, etc.)

**For Websites, Landing Pages, Web Apps:**

```
Read the DESIGN.md and AGENTS.md from https://github.com/bkmmannesmann/bkm-design-system
and create [a landing page / web app / etc.] following the BKM Mannesmann design.
```

**For Slide Presentations (Glasmorphism Style):**

```
Read the following files from https://github.com/bkmmannesmann/bkm-design-system:
1. skills/bkm-slides/SKILL.md (mandatory workflow)
2. skills/bkm-slides/STYLE_PRESETS.md (exact CSS tokens)
3. skills/bkm-slides/html-template.md (copy-paste HTML templates)
Then create a presentation about [topic] in the [BKM AG / Fachbetrieb] context.
```

The slide skill includes a mandatory workflow: determine context → read exact CSS tokens → read HTML templates → generate background photos → upload assets → build slides → quality check.

**For Brand-Conform Images (OpenAI Images / `gpt-image-1`):**

```bash
export OPENAI_API_KEY="sk-..."
node skills/bkm-images/generate.mjs \
  --usecase slide --context ag \
  --motif "concrete basement wall with a horizontal moisture barrier line"
```

The `bkm-images` skill builds a BKM-brand-conform prompt (editorial photography,
muted earth tones, green accents, no text/logos in the image) for slide
backgrounds, social media, website heroes and product shots. Use `--dry-run` to
print the prompt without calling the API. No npm install required (Node ≥ 18).
See `skills/bkm-images/SKILL.md`.

**For Other Formats (Instagram, Print, Social Media):**

```
Read the DESIGN.md from https://github.com/bkmmannesmann/bkm-design-system
and create [Instagram posts / print materials / etc.] following the BKM Mannesmann design.
```

The agent will parse the YAML tokens and prose documentation to produce brand-consistent output.

### For Developers

1. Clone the repository
2. Copy the CSS Custom Properties from `AGENTS.md` into your project's root CSS
3. Or use the Tailwind v4 configuration block from `AGENTS.md`
4. Reference `DESIGN.md` for component specifications

### For Designers

Read the prose sections of `DESIGN.md` for visual guidelines, then reference the specific `docs/` files for your medium (digital, print, social).

## Design Philosophy

The BKM system is built on five pillars:

1. **Dual-Mode Architecture** — Deep Green marketing surfaces alternate with Sand White documentation surfaces
2. **Shadow-as-Border** — Multi-layer box-shadow stacks replace traditional CSS borders (inspired by Vercel)
3. **Product-Line Geometry** — Angular (0–4px) for Pro Line, Rounded (pill) for Home Line
4. **Single-Accent Strategy** — Lime Green (`#b4e717`) exclusively for interactive elements
5. **Two-Voice Typography** — Unbounded (announce), TT Norms Pro Regular + Bold (read + specify)

## Supported Output Formats

This design system can be applied to generate:

- Websites (React, HTML/CSS, Tailwind, Next.js)
- Slide presentations (PowerPoint, Google Slides, image-based)
- Instagram Carousel Posts (4:5 or 1:1)
- Print documents (brochures, technical data sheets, labels)
- Email templates
- Social media graphics
- Video title cards

## Compatibility

This design system follows the [awesome-design-md](https://github.com/VoltAgent/awesome-design-md) specification and is compatible with:

- **Cursor** — Add as project context
- **GitHub Copilot** — Reference in workspace
- **Manus** — Share as project file or reference via GitHub URL
- **Claude** — Paste DESIGN.md content as context
- **ChatGPT** — Upload DESIGN.md as file
- **Any AI agent** that can read Markdown with YAML frontmatter

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to propose changes to the design system.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history and updates.

## License

Proprietary — BKM Mannesmann AG. Internal use only.
