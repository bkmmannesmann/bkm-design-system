# AGENTS.md — BKM Mannesmann Design System v1.3

> Implementation instructions for AI coding agents. Read `DESIGN.md` for the full token reference and design philosophy. This file provides the code translation layer.

## The One Rule That Matters Most

> **The Keyvisual is a pre-rendered image asset. NEVER recreate it in code. No SVG generation, no CSS clip-paths, no procedural patterns. Place the provided image file, right-aligned, cropped.**

If you remember nothing else from this file, remember this. Every time an agent generates a "chevron pattern" in CSS or SVG, it produces visual garbage that damages the brand.

## Quick Rules

1. **Three typefaces only:** Unbounded (headlines/buttons, weight 900, uppercase), Inter (body/UI), Geist Mono (specs/code).
2. **No CSS `border` on cards.** Use `box-shadow` ring technique.
3. **Lime Green = interactive only.** Never decorative. Never on text. Never on large surfaces.
4. **Pro Line = angular** (0–4px radius). **Home Line = rounded** (12px–pill). Never mix.
5. **Dark surfaces = marketing.** Light surfaces = documentation. Hard cut between them.
6. **Max ONE primary button per viewport fold.**
7. **Keyvisual = image asset, right edge, cropped.** Not a pattern. Not generated. Not tiled.
8. **All interactive elements need states:** default, hover, active, disabled, loading, focus.
9. **Body text never below 16px** on any breakpoint.
10. **No pure black.** Darkest values: `#1c4b42` (surfaces), `#1a1a1a` (text).

## Keyvisual Implementation

### Correct Usage

```html
<!-- Hero section with Keyvisual -->
<section class="relative overflow-hidden bg-[#1c4b42]">
  <!-- Keyvisual: always as image, always right, always cropped -->
  <img
    src="/assets/brand/keyvisual.svg"
    alt=""
    aria-hidden="true"
    class="absolute top-0 right-0 h-full w-[20%] object-cover object-left pointer-events-none"
  />
  <!-- Content (left-aligned, never centered for heroes) -->
  <div class="relative z-10 max-w-[1280px] mx-auto px-8 py-40">
    <h1 class="font-['Unbounded'] text-7xl font-black uppercase text-white tracking-[-3px]">
      SCHUTZ DER HÄLT
    </h1>
  </div>
</section>
```

### What NOT to Do

```html
<!-- FORBIDDEN: Don't generate SVG patterns -->
<svg viewBox="0 0 100 100"><polygon points="50,0 100,100 0,100"/></svg>

<!-- FORBIDDEN: Don't use CSS shapes to approximate it -->
<div style="clip-path: polygon(50% 0%, 100% 100%, 0% 100%)"></div>

<!-- FORBIDDEN: Don't tile it as a background -->
<div class="bg-[url('chevron.svg')] bg-repeat opacity-5"></div>

<!-- FORBIDDEN: Don't use it on small components -->
<div class="card"><img src="keyvisual.svg" /></div>
```

### When to Skip the Keyvisual Entirely

- Instagram posts (too small)
- Email templates
- UI components (cards, modals, toasts)
- Technical data sheets (competes with data)
- Any surface smaller than a full-width hero band

## CSS Custom Properties

```css
:root {
  /* Brand Core */
  --bkm-deep-green: #1c4b42;
  --bkm-deep-green-light: #2a6b5e;
  --bkm-deep-green-90: rgba(28,75,66,0.90);
  --bkm-transition-green: #287d4b;
  --bkm-pure-green: #4daf46;
  --bkm-lime: #b4e717;
  --bkm-lime-soft: #d4f07a;
  --bkm-lime-muted: #e8f5b3;

  /* Surfaces */
  --bkm-canvas: #ffffff;
  --bkm-canvas-warm: #f6f5f2;
  --bkm-surface: #f0efec;
  --bkm-surface-soft: #fafaf8;

  /* Text */
  --bkm-ink: #1a1a1a;
  --bkm-charcoal: #2d2d2d;
  --bkm-stone-grey: #494949;
  --bkm-steel: #6b6b6b;
  --bkm-muted: #8a8a8a;
  --bkm-on-dark: #ffffff;
  --bkm-on-dark-muted: rgba(255,255,255,0.70);
  --bkm-on-dark-subtle: rgba(255,255,255,0.50);

  /* Hairlines */
  --bkm-hairline: #e8e6e1;
  --bkm-hairline-soft: #f0efec;
  --bkm-hairline-strong: #c8c5be;

  /* Semantic */
  --bkm-error: #dc2626;
  --bkm-warning: #d97706;
  --bkm-success: #4daf46;
  --bkm-info: #0284c7;

  /* Shadows (shadow-as-border technique) */
  --bkm-shadow-ring: rgba(0,0,0,0.08) 0px 0px 0px 1px;
  --bkm-shadow-subtle: rgba(0,0,0,0.08) 0px 0px 0px 1px, rgba(0,0,0,0.04) 0px 2px 4px;
  --bkm-shadow-card: rgba(0,0,0,0.08) 0px 0px 0px 1px, rgba(0,0,0,0.04) 0px 4px 8px;
  --bkm-shadow-featured: rgba(0,0,0,0.08) 0px 0px 0px 1px, rgba(0,0,0,0.06) 0px 8px 16px -4px;
  --bkm-shadow-elevated: rgba(0,0,0,0.08) 0px 0px 0px 1px, rgba(0,0,0,0.08) 0px 12px 24px -8px;
  --bkm-shadow-modal: rgba(0,0,0,0.12) 0px 0px 0px 1px, rgba(0,0,0,0.16) 0px 24px 48px -12px;
  --bkm-shadow-focus: 0 0 0 2px #ffffff, 0 0 0 4px #4daf46;
  --bkm-shadow-focus-dark: 0 0 0 2px #1c4b42, 0 0 0 4px #b4e717;

  /* Spacing */
  --bkm-space-xs: 8px;
  --bkm-space-sm: 12px;
  --bkm-space-md: 16px;
  --bkm-space-lg: 24px;
  --bkm-space-xl: 32px;
  --bkm-space-xxl: 48px;
  --bkm-space-section: 80px;
  --bkm-space-hero: 160px;

  /* Typography */
  --bkm-font-display: 'Unbounded', system-ui, sans-serif;
  --bkm-font-body: 'Inter', system-ui, sans-serif;
  --bkm-font-mono: 'Geist Mono', 'Source Code Pro', 'JetBrains Mono', monospace;

  /* Transitions */
  --bkm-transition-fast: all 150ms cubic-bezier(0.4, 0, 0.2, 1);
  --bkm-transition-normal: all 200ms cubic-bezier(0.4, 0, 0.2, 1);
  --bkm-transition-slow: all 300ms cubic-bezier(0.4, 0, 0.2, 1);
}
```

## Tailwind CSS v4 Theme

```css
@theme inline {
  --color-bkm-lime: oklch(0.87 0.22 115);
  --color-bkm-lime-soft: oklch(0.92 0.15 115);
  --color-bkm-deep-green: oklch(0.32 0.06 170);
  --color-bkm-deep-green-light: oklch(0.40 0.07 168);
  --color-bkm-pure-green: oklch(0.63 0.18 145);
  --color-bkm-transition-green: oklch(0.47 0.12 155);
  --color-bkm-canvas: oklch(1 0 0);
  --color-bkm-canvas-warm: oklch(0.97 0.005 80);
  --color-bkm-surface: oklch(0.95 0.005 80);
  --color-bkm-ink: oklch(0.15 0 0);
  --color-bkm-charcoal: oklch(0.23 0 0);
  --color-bkm-stone-grey: oklch(0.38 0 0);
  --color-bkm-steel: oklch(0.47 0 0);
  --color-bkm-muted: oklch(0.59 0 0);
  --color-bkm-hairline: oklch(0.92 0.005 80);

  --font-bkm-display: 'Unbounded', system-ui, sans-serif;
  --font-bkm-body: 'Inter', system-ui, sans-serif;
  --font-bkm-mono: 'Geist Mono', 'Source Code Pro', monospace;
}
```

## Google Fonts

```html
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Unbounded:wght@900&family=Inter:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap" rel="stylesheet" />
```

## Component Patterns

### Hero Band (Dark Marketing Surface)

```html
<section class="relative overflow-hidden bg-[#1c4b42] min-h-[560px]">
  <!-- Optional: Keyvisual as image asset, right-aligned -->
  <img
    src="/assets/brand/keyvisual.svg"
    alt="" aria-hidden="true"
    class="absolute top-0 right-0 h-full w-[20%] object-cover object-left pointer-events-none"
  />
  <div class="relative z-10 max-w-[1280px] mx-auto px-8 md:px-16 py-40">
    <p class="font-['Inter'] text-[13px] font-semibold uppercase tracking-[1.5px] text-white/50 mb-6">
      Bauwerksabdichtung seit 1928
    </p>
    <h1 class="font-['Unbounded'] text-5xl md:text-7xl font-black uppercase text-white tracking-[-3px] leading-none max-w-[800px]">
      SCHUTZ DER HÄLT
    </h1>
    <p class="font-['Inter'] text-xl text-white/70 mt-6 max-w-[640px] leading-relaxed">
      Professionelle Bauwerksabdichtung mit MicroPorex® Technologie.
    </p>
    <div class="flex flex-wrap gap-4 mt-10">
      <button class="bg-[#b4e717] text-[#1c4b42] font-['Unbounded'] text-sm font-black uppercase px-6 py-3 h-12 tracking-[0.5px] hover:bg-white transition-all duration-150 active:scale-[0.98]">
        PRODUKTE ENTDECKEN
      </button>
      <button class="border-2 border-white/30 text-white font-['Unbounded'] text-sm font-black uppercase px-6 py-3 h-12 tracking-[0.5px] hover:border-[#b4e717] hover:text-[#b4e717] transition-colors duration-150">
        FACHBETRIEB FINDEN
      </button>
    </div>
  </div>
</section>
```

### Card with Shadow-as-Border (Light Surface)

```html
<div class="
  bg-white p-8 rounded-[12px]
  shadow-[rgba(0,0,0,0.08)_0px_0px_0px_1px,rgba(0,0,0,0.04)_0px_2px_4px]
  transition-all duration-200
  hover:shadow-[rgba(0,0,0,0.08)_0px_0px_0px_1px,rgba(0,0,0,0.06)_0px_8px_16px_-4px]
  hover:-translate-y-0.5
">
  <h3 class="font-['Unbounded'] text-lg font-black uppercase tracking-[-0.3px] text-[#1a1a1a]">
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
<div class="divide-y divide-[#f0efec]">
  <div class="flex justify-between items-center py-3">
    <span class="font-['Inter'] text-sm text-[#6b6b6b]">Trocknungszeit</span>
    <span class="font-['Geist_Mono'] text-sm font-medium text-[#1c4b42]">24 h</span>
  </div>
  <div class="flex justify-between items-center py-3">
    <span class="font-['Inter'] text-sm text-[#6b6b6b]">Verbrauch</span>
    <span class="font-['Geist_Mono'] text-sm font-medium text-[#1c4b42]">1,2 kg/m²</span>
  </div>
  <div class="flex justify-between items-center py-3">
    <span class="font-['Inter'] text-sm text-[#6b6b6b]">pH-Wert</span>
    <span class="font-['Geist_Mono'] text-sm font-medium text-[#1c4b42]">12,5</span>
  </div>
</div>
```

### Button Pro Line (Angular)

```html
<button class="
  bg-[#b4e717] text-[#1c4b42]
  font-['Unbounded'] text-sm font-black uppercase tracking-[0.5px]
  px-6 py-3 h-12 min-w-[120px]
  rounded-none
  transition-all duration-150
  hover:bg-white active:scale-[0.98]
  disabled:bg-[#f0efec] disabled:text-[#8a8a8a] disabled:cursor-not-allowed disabled:opacity-40
  focus-visible:outline-none focus-visible:shadow-[0_0_0_2px_#ffffff,0_0_0_4px_#4daf46]
">
  JETZT KAUFEN
</button>
```

### Button Home Line (Pill)

```html
<button class="
  bg-[#4daf46] text-white
  font-['Unbounded'] text-sm font-black uppercase tracking-[0.5px]
  px-7 py-3 h-12
  rounded-full
  transition-all duration-150
  hover:bg-[#287d4b] active:scale-[0.98]
  disabled:bg-[#f0efec] disabled:text-[#8a8a8a] disabled:cursor-not-allowed disabled:opacity-40
  focus-visible:outline-none focus-visible:shadow-[0_0_0_2px_#ffffff,0_0_0_4px_#4daf46]
">
  In den Warenkorb
</button>
```

### Badge Pro / Badge Home

```html
<!-- Pro: angular, dark bg, lime text -->
<span class="inline-flex items-center bg-[#1c4b42] text-[#b4e717] font-['Inter'] text-xs font-bold uppercase tracking-[0.5px] px-2.5 py-1 rounded-[2px]">
  PRO
</span>

<!-- Home: pill, green bg, white text -->
<span class="inline-flex items-center bg-[#4daf46] text-white font-['Inter'] text-xs font-bold uppercase tracking-[0.5px] px-3 py-1 rounded-full">
  HOME
</span>

<!-- MicroPorex: monospace, ring shadow -->
<span class="inline-flex items-center bg-[#f0efec] text-[#494949] font-['Geist_Mono'] text-xs font-medium px-2.5 py-1 rounded-[4px] shadow-[rgba(0,0,0,0.08)_0px_0px_0px_1px]">
  MicroPorex®
</span>
```

## Page Structure Templates

### Landing Page

```
[DARK]  Navigation (sticky, 64px, deep green, lime CTA right)
[DARK]  Hero Band (160px padding, left-aligned headline, optional Keyvisual right)
[LIGHT] Features (3-up cards, shadow-as-border, canvas-warm background)
[LIGHT] Specs (stat cards with Geist Mono values)
[DARK]  Testimonial (deep green, white quote, lime accent mark)
[LIGHT] Products (3-up or 4-up card grid, hover-lift)
[DARK]  CTA Banner (centered headline + single lime button)
[DARK]  Footer (4-column links, deep green)
```

### Product Detail

```
[DARK]  Navigation
[LIGHT] Breadcrumb (body-sm, steel color)
[LIGHT] Product Hero (image 50% left, specs 50% right)
[LIGHT] Tabs (segmented, lime underline active)
[LIGHT] Tab Content (description / spec-table / downloads)
[LIGHT] Related Products (3-up cards)
[DARK]  CTA Banner
[DARK]  Footer
```

## Context

### What BKM Does
Building protection manufacturer (est. 1928). Products against rising damp and laterally penetrating water. Core technologies: horizontal barriers, surface barriers, resin injections. Proprietary MicroPorex® ingredient brand.

### Two Product Lines
- **Pro Line**: For certified specialist companies. Angular geometry. Deep Green + Lime.
- **Home Line**: For DIY homeowners. Rounded geometry. Pure Green. Warm tone.

### Two Audiences
- **Fachbetriebe** (specialists): Technical, results-focused. Du-Ansprache.
- **Hausbesitzer** (homeowners): Solution-seeking, quality-conscious. Du-Ansprache.

### Logo
- Light backgrounds: grey-green logo
- Dark backgrounds: white-green logo
- Clear space: 1× cap height of "BKM" in all directions
- Never rotate, stretch, recolor, or add effects

## Implementation Checklist

- [ ] Keyvisual placed as IMAGE (not generated in code)
- [ ] No CSS `border` on cards (shadow-as-border only)
- [ ] Lime Green used ONLY on interactive elements
- [ ] Maximum ONE primary button per viewport fold
- [ ] Unbounded only at weight 900, only uppercase, only ≥16px
- [ ] Geist Mono for all measurable/precise values
- [ ] Pro Line components use 0–4px radius
- [ ] Home Line components use 12px–pill radius
- [ ] Body text ≥16px on all breakpoints
- [ ] Focus rings visible on all interactive elements
- [ ] Touch targets ≥44px on mobile
- [ ] Dark/light surface transitions are hard cuts (no gradients)
- [ ] 3-level text opacity on dark surfaces (100%/70%/50%)
- [ ] MicroPorex® with ® on first mention per page
- [ ] `prefers-reduced-motion` respected (0ms when active)
- [ ] No pure black (#000000) anywhere
