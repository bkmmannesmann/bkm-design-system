# AGENTS.md — BKM Mannesmann AG

> Implementation guidance for AI agents. Read `DESIGN.md` first for normative token definitions. This file provides the code translation layer.

## Critical Rules

1. **The Keyvisual is a pre-rendered image asset. NEVER recreate it in code.** No SVG generation, no CSS clip-paths, no procedural patterns. Place the provided image file, right-aligned, cropped.
2. **One brand, two color contexts.** BKM AG uses Deep Green + Lime. Fachbetrieb uses Stone Grey + Pure Green. Same design structure, different palette.
3. **Lime Green = interactive only (BKM AG context).** Never decorative. Never on text. Never on large surfaces. Never in Fachbetrieb context.
4. **The greens tell a story.** Deep Green = moisture/problem. Pure Green = dry/solution. This is not arbitrary branding — it visualizes the drying process.
5. **Max ONE primary button per viewport fold.**
6. **No CSS `border` on cards.** Use shadow-as-border technique.
7. **Unbounded: weight 900, uppercase, 18px minimum.** No exceptions.
8. **Hard cuts between surface modes.** Never gradients, waves, or diagonals.

## Quick Start

```html
<!-- 1. Load fonts -->
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Unbounded:wght@900&family=Inter:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap" rel="stylesheet" />
```

```css
/* 2. Set CSS variables */
:root {
  --bkm-deep-green: #1c4b42;
  --bkm-deep-green-light: #2a6b5e;
  --bkm-transition-green: #287d4b;
  --bkm-pure-green: #4daf46;
  --bkm-lime: #b4e717;
  --bkm-stone-grey: #494949;
  --bkm-sand-white: #f6f5f2;
  --bkm-surface: #ffffff;
  --bkm-ink: #1a1a1a;
  --bkm-on-dark: #ffffff;

  --bkm-shadow-subtle: rgba(0,0,0,0.08) 0px 0px 0px 1px, rgba(0,0,0,0.04) 0px 2px 4px;
  --bkm-shadow-featured: rgba(0,0,0,0.08) 0px 0px 0px 1px, rgba(0,0,0,0.06) 0px 8px 16px -4px;
  --bkm-shadow-elevated: rgba(0,0,0,0.08) 0px 0px 0px 1px, rgba(0,0,0,0.08) 0px 12px 24px -8px;
}
```

## Determining Context

Before writing any code, determine which color context applies:

| Context | When | Primary Color | Accent Color | Nav Background |
|---------|------|---------------|--------------|----------------|
| **BKM AG** | Corporate site, products, shop, marketing | Deep Green (#1c4b42) | Lime (#b4e717) | Deep Green |
| **Fachbetrieb** | Specialist company pages, partner portal, certification | Pure Green (#4daf46) / Stone Grey (#494949) | Pure Green (#4daf46) | Stone Grey (#494949) |

The design structure (typography, spacing, shadows, layout) is identical. Only the color mapping changes.

## Keyvisual Implementation

```html
<!-- CORRECT: Image asset, right edge, cropped -->
<section class="relative overflow-hidden bg-[#1c4b42]">
  <img src="/assets/brand/keyvisual.svg" alt="" aria-hidden="true"
       class="absolute top-0 right-0 h-full w-[20%] object-cover object-left pointer-events-none" />
  <div class="relative z-10"><!-- content --></div>
</section>

<!-- WRONG — NEVER do any of these -->
<svg>...</svg>                              <!-- No SVG recreation -->
<div class="bg-[url('chevron.svg')]"></div>  <!-- No tiling -->
<div style="clip-path: polygon(...)"></div>  <!-- No CSS approximation -->
```

When to skip the Keyvisual: Instagram posts, email templates, UI components, technical data sheets, any surface smaller than a full-width hero.

## BKM AG Context — Component Patterns

### Hero Band (Dark Surface)

```html
<section class="relative overflow-hidden bg-[#1c4b42] min-h-[560px]">
  <div class="max-w-[1280px] mx-auto px-8 md:px-16 py-40">
    <p class="font-['Inter'] text-[13px] font-semibold uppercase tracking-[1.5px] text-white/50 mb-6">
      Bauwerksabdichtung seit 1928
    </p>
    <h1 class="font-['Unbounded'] text-5xl md:text-7xl font-black uppercase text-white tracking-[-0.04em] leading-none max-w-[800px]">
      SCHUTZ DER HÄLT
    </h1>
    <p class="font-['Inter'] text-xl text-white/70 mt-6 max-w-[640px] leading-relaxed">
      Professionelle Bauwerksabdichtung mit MicroPorex® Technologie.
    </p>
    <button class="mt-10 bg-[#b4e717] text-[#1c4b42] font-['Unbounded'] text-sm font-black uppercase
                   px-6 py-3 h-12 rounded-[4px] tracking-[0.02em]
                   hover:bg-white transition-colors duration-150">
      PRODUKTE ENTDECKEN
    </button>
  </div>
</section>
```

### Card (Light Surface, Shadow-as-Border)

```html
<div class="bg-white p-8 rounded-[12px]
            shadow-[rgba(0,0,0,0.08)_0px_0px_0px_1px,rgba(0,0,0,0.04)_0px_2px_4px]
            hover:shadow-[rgba(0,0,0,0.08)_0px_0px_0px_1px,rgba(0,0,0,0.06)_0px_8px_16px_-4px]
            hover:-translate-y-0.5 transition-all duration-200">
  <span class="inline-flex bg-[#1c4b42] text-[#b4e717] font-['Inter'] text-xs font-bold uppercase tracking-[0.05em] px-2.5 py-1 rounded-[4px]">
    PRO LINE
  </span>
  <h3 class="font-['Unbounded'] text-lg font-black uppercase tracking-tight text-[#1a1a1a] mt-4">
    KELLERSCHUTZ PRO
  </h3>
  <p class="font-['Inter'] text-base text-[#494949] mt-3 leading-relaxed">
    Professionelle Horizontalsperre mit MicroPorex® Technologie.
  </p>
  <span class="inline-block mt-4 font-['Geist_Mono'] text-sm font-medium text-[#1c4b42]">
    ab 89,90 €
  </span>
</div>
```

### Spec Table (Technical Data)

```html
<div class="divide-y divide-[#e8e6e1]">
  <div class="flex justify-between items-center py-3">
    <span class="font-['Inter'] text-sm text-[#6b6b6b]">Schichtdicke</span>
    <span class="font-['Geist_Mono'] text-sm font-medium text-[#1c4b42]">2,5 mm</span>
  </div>
  <div class="flex justify-between items-center py-3">
    <span class="font-['Inter'] text-sm text-[#6b6b6b]">Verbrauch</span>
    <span class="font-['Geist_Mono'] text-sm font-medium text-[#1c4b42]">1,2 kg/m²</span>
  </div>
  <div class="flex justify-between items-center py-3">
    <span class="font-['Inter'] text-sm text-[#6b6b6b]">Trocknungszeit</span>
    <span class="font-['Geist_Mono'] text-sm font-medium text-[#1c4b42]">24 h</span>
  </div>
</div>
```

## Fachbetrieb Context — Color Swap

Same structure, different palette:

```html
<!-- Fachbetrieb Navigation: Stone Grey instead of Deep Green -->
<nav class="bg-[#494949] h-16 sticky top-0">
  <a class="text-white hover:text-[#4daf46] transition-colors">...</a>
</nav>

<!-- Fachbetrieb Hero: Light surface with Pure Green accents -->
<section class="bg-[#f6f5f2] py-40">
  <h1 class="font-['Unbounded'] text-5xl font-black uppercase text-[#1a1a1a]">
    IHR ZERTIFIZIERTER FACHBETRIEB
  </h1>
  <button class="bg-[#287d4b] text-white font-['Unbounded'] text-sm font-black uppercase
                 px-6 py-3 h-12 rounded-[4px] hover:bg-[#494949] transition-colors">
    TERMIN VEREINBAREN
  </button>
</section>

<!-- Fachbetrieb Badge: Pure Green instead of Lime -->
<span class="inline-flex bg-[#287d4b] text-white font-['Inter'] text-xs font-bold uppercase px-2.5 py-1 rounded-[4px]">
  ZERTIFIZIERT
</span>
```

## Tailwind v4 Theme

```css
@theme {
  --color-bkm-deep-green: #1c4b42;
  --color-bkm-deep-green-light: #2a6b5e;
  --color-bkm-transition-green: #287d4b;
  --color-bkm-pure-green: #4daf46;
  --color-bkm-lime: #b4e717;
  --color-bkm-stone-grey: #494949;
  --color-bkm-sand-white: #f6f5f2;
  --color-bkm-surface: #ffffff;
  --color-bkm-ink: #1a1a1a;
  --color-bkm-outline: #c8c5be;
  --color-bkm-error: #dc2626;

  --font-display: 'Unbounded', system-ui, sans-serif;
  --font-body: 'Inter', system-ui, sans-serif;
  --font-mono: 'Geist Mono', monospace;

  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 12px;
  --radius-xl: 16px;
  --radius-full: 9999px;

  --spacing-xs: 4px;
  --spacing-sm: 8px;
  --spacing-md: 16px;
  --spacing-lg: 24px;
  --spacing-xl: 32px;
  --spacing-xxl: 48px;
  --spacing-section: 80px;
  --spacing-hero: 160px;
}
```

## Format Compliance

This design system follows the [Google design.md specification](https://github.com/google-labs-code/design.md). Validate with:

```bash
npx @google/design.md lint DESIGN.md
```

Export to Tailwind v4:

```bash
npx @google/design.md export --format css-tailwind DESIGN.md
```

## Checklist Before Delivery

- [ ] Determined context: BKM AG or Fachbetrieb?
- [ ] Keyvisual placed as image (if applicable) — not generated in code
- [ ] Surface modes alternate with hard cuts (no gradients)
- [ ] Lime used ONLY for interactive elements (BKM AG context only)
- [ ] Pure Green used for Fachbetrieb accents (not Lime)
- [ ] Unbounded: weight 900, uppercase, 18px minimum
- [ ] Cards use shadow-as-border (no CSS border property)
- [ ] Technical values in Geist Mono
- [ ] Only ONE primary button per viewport fold
- [ ] WCAG AA contrast ratios met (4.5:1 minimum)
