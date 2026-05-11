# AGENTS.md — BKM Mannesmann Design System v1.2

> This file provides AI coding agents with implementation-ready instructions for the BKM Mannesmann design system. Read `DESIGN.md` for the full token reference; this file provides the translation layer into code.

## Quick Rules

1. **Three typefaces only:** Unbounded (headlines/buttons, weight 900, uppercase), Inter (body/UI), Geist Mono (specs/code).
2. **No CSS `border` on cards.** Use `box-shadow` ring technique instead.
3. **Lime Green = interactive only.** Never decorative, never on body text, never on large surfaces.
4. **Pro Line = angular** (0–4px radius). **Home Line = rounded** (12px–pill).
5. **Dark surfaces = marketing.** Light surfaces = documentation/technical.
6. **Max ONE primary button per viewport fold.**
7. **Chevron pattern at 5% opacity on dark surfaces only.**
8. **All interactive elements need 6 states:** default, hover, active, disabled, loading, focus.
9. **Body text never below 16px** on any breakpoint.
10. **Focus rings use double-ring technique** (white inner + brand outer).

## Critical Rules (Never Break These)

### Typography
- **Unbounded** is the ONLY headline/button font. Weight 900. Always uppercase. Always negative letter-spacing at display sizes.
- **Inter** is the ONLY body font. Weights 400/500/600/700.
- **Geist Mono** is the ONLY monospace font. Used for technical data, article numbers, measurements, code.
- Never mix these roles. Never use Inter for headlines. Never use Unbounded for body text.
- Unbounded is NEVER used below 16px — it becomes illegible.
- Letter-spacing scales with size: -3px at 72px, -2px at 56px, -1.5px at 44px, -1px at 36px, -0.5px at 28px.

### Color
- **Lime Green (`#b4e717`)** is ONLY for interactive elements: buttons, active states, checkmarks, icons on dark, key data highlights.
- Never use Lime Green for text (contrast fails), backgrounds (too aggressive), or decoration.
- **One Lime CTA per viewport fold maximum.** Scarcity = urgency.
- **Deep Green (`#1c4b42`)** for dark surfaces. Never use pure black (`#000000`).
- **On dark surfaces:** 3-level text hierarchy: 100% white (headlines), 70% white (body), 50% white (captions). Never a 4th level.
- **Stone Grey (`#494949`)** for body text on light. Never pure black.

### Geometry
- **Pro Line** = angular (0–4px radius). Technical. Professional. Sharp line-cap icons.
- **Home Line** = rounded (12–9999px radius). Accessible. Friendly. Rounded line-cap icons.
- Never apply pill shapes to Pro Line. Never apply angular shapes to Home Line.
- Brand-neutral components (shared across lines) use `8–12px` radius.

### Shadows (Shadow-as-Border)
- Use `box-shadow` stacks instead of CSS `border` on cards and containers.
- Ring layer: `rgba(0,0,0,0.08) 0px 0px 0px 1px`
- 7 elevation levels: ring → subtle → card → featured → elevated → elevated-lg → modal
- On dark surfaces: shadows are invisible. Use surface-color ladder instead (deep → standard → elevated).

### Layout
- Hero copy is ALWAYS left-aligned, asymmetric (60/40 split).
- Never center hero headlines (center is reserved for CTA banners only).
- Dark bands alternate with light bands for section rhythm.
- Maximum content width: 1440px. Standard content: 1280px. Prose: 640px.
- Grid: 12 columns desktop, 8 tablet, 4 mobile.

## File Structure

```
DESIGN.md              → Complete design tokens + documentation (1680+ lines, primary source)
AGENTS.md              → This file (agent instructions + code templates)
README.md              → Project overview + usage guide
CONTRIBUTING.md        → Contribution guidelines
CHANGELOG.md           → Version history
docs/
  brand-voice.md       → Tone, claims, copy patterns
  digitale-medien.md   → Web/app implementation details
  print-anwendungen.md → Print specifications (CMYK, bleed, safe zones)
  microporex-und-technik.md → Ingredient brand rules
  keyvisual.md         → Chevron pattern specifications
  logo.md              → Logo variants + placement rules
  icon-system.md       → Icon specifications (Lucide, sizes, colors)
  referenzen.md        → External design system references
  verbesserungsvorschlaege.md → Improvement proposals + gap analysis
```

## CSS Custom Properties Template

```css
:root {
  /* === Brand Core === */
  --bkm-primary: #4daf46;
  --bkm-primary-deep: #287d4b;
  --bkm-primary-pressed: #1c5c36;
  --bkm-lime: #b4e717;
  --bkm-lime-soft: #d4f07a;
  --bkm-lime-muted: #e8f5b3;
  --bkm-lime-10: rgba(180,231,23,0.10);
  --bkm-lime-20: rgba(180,231,23,0.20);
  --bkm-deep-green: #1c4b42;
  --bkm-deep-green-light: #2a6b5e;
  --bkm-deep-green-90: rgba(28,75,66,0.90);
  --bkm-transition-green: #287d4b;
  --bkm-pure-green: #4daf46;

  /* === Surfaces === */
  --bkm-canvas: #ffffff;
  --bkm-canvas-warm: #f6f5f2;
  --bkm-canvas-cool: #f8faf9;
  --bkm-surface: #f0efec;
  --bkm-surface-soft: #fafaf8;
  --bkm-surface-dark: #1c4b42;
  --bkm-surface-dark-elevated: #2a6b5e;
  --bkm-surface-dark-deep: #132f2a;
  --bkm-surface-overlay: rgba(28,75,66,0.85);

  /* === Hairlines === */
  --bkm-hairline: #e8e6e1;
  --bkm-hairline-soft: #f0efec;
  --bkm-hairline-strong: #c8c5be;
  --bkm-hairline-dark: rgba(255,255,255,0.12);
  --bkm-divider-dark: rgba(255,255,255,0.16);

  /* === Text === */
  --bkm-ink: #1a1a1a;
  --bkm-charcoal: #2d2d2d;
  --bkm-stone-grey: #494949;
  --bkm-steel: #6b6b6b;
  --bkm-muted: #8a8a8a;
  --bkm-ash: #b0b0b0;
  --bkm-on-dark: #ffffff;
  --bkm-on-dark-muted: rgba(255,255,255,0.70);
  --bkm-on-dark-subtle: rgba(255,255,255,0.50);
  --bkm-on-dark-disabled: rgba(255,255,255,0.30);

  /* === Semantic === */
  --bkm-error: #dc2626;
  --bkm-error-deep: #991b1b;
  --bkm-error-soft: #fef2f2;
  --bkm-warning: #d97706;
  --bkm-warning-soft: #fffbeb;
  --bkm-success: #4daf46;
  --bkm-success-soft: #f0fdf4;
  --bkm-info: #0284c7;
  --bkm-info-soft: #f0f9ff;

  /* === Product Lines === */
  --bkm-pro-accent: #b4e717;
  --bkm-pro-surface: #1c4b42;
  --bkm-pro-badge-bg: #1c4b42;
  --bkm-pro-badge-text: #b4e717;
  --bkm-home-accent: #4daf46;
  --bkm-home-surface: #f6f5f2;
  --bkm-home-badge-bg: #4daf46;
  --bkm-home-badge-text: #ffffff;

  /* === Data Visualization === */
  --bkm-chart-1: #1c4b42;
  --bkm-chart-2: #287d4b;
  --bkm-chart-3: #4daf46;
  --bkm-chart-4: #b4e717;
  --bkm-chart-5: #d4f07a;
  --bkm-chart-6: #e8f5b3;

  /* === Spacing === */
  --bkm-space-xxs: 4px;
  --bkm-space-xs: 8px;
  --bkm-space-sm: 12px;
  --bkm-space-md: 16px;
  --bkm-space-lg: 24px;
  --bkm-space-xl: 32px;
  --bkm-space-xxl: 48px;
  --bkm-space-xxxl: 64px;
  --bkm-space-section: 80px;
  --bkm-space-section-lg: 120px;
  --bkm-space-hero: 160px;

  /* === Radius === */
  --bkm-radius-none: 0px;
  --bkm-radius-xs: 2px;
  --bkm-radius-sm: 4px;
  --bkm-radius-md: 8px;
  --bkm-radius-lg: 12px;
  --bkm-radius-xl: 16px;
  --bkm-radius-xxl: 24px;
  --bkm-radius-full: 9999px;

  /* === Shadows === */
  --bkm-shadow-ring: rgba(0,0,0,0.08) 0px 0px 0px 1px;
  --bkm-shadow-subtle: rgba(0,0,0,0.08) 0px 0px 0px 1px, rgba(0,0,0,0.04) 0px 2px 4px;
  --bkm-shadow-card: rgba(0,0,0,0.08) 0px 0px 0px 1px, rgba(0,0,0,0.04) 0px 4px 8px;
  --bkm-shadow-featured: rgba(0,0,0,0.08) 0px 0px 0px 1px, rgba(0,0,0,0.06) 0px 8px 16px -4px, rgba(255,255,255,1) 0px 0px 0px 1px inset;
  --bkm-shadow-elevated: rgba(0,0,0,0.08) 0px 0px 0px 1px, rgba(0,0,0,0.08) 0px 12px 24px -8px;
  --bkm-shadow-elevated-lg: rgba(0,0,0,0.10) 0px 0px 0px 1px, rgba(0,0,0,0.12) 0px 20px 40px -12px;
  --bkm-shadow-modal: rgba(0,0,0,0.12) 0px 0px 0px 1px, rgba(0,0,0,0.16) 0px 24px 48px -12px;
  --bkm-shadow-focus: 0 0 0 2px #ffffff, 0 0 0 4px #4daf46;
  --bkm-shadow-focus-dark: 0 0 0 2px #1c4b42, 0 0 0 4px #b4e717;
  --bkm-shadow-focus-error: 0 0 0 2px #ffffff, 0 0 0 4px #dc2626;
  --bkm-shadow-tooltip: rgba(0,0,0,0.12) 0px 4px 12px;
  --bkm-shadow-dropdown: rgba(0,0,0,0.08) 0px 0px 0px 1px, rgba(0,0,0,0.12) 0px 8px 24px -4px;

  /* === Transitions === */
  --bkm-transition-fast: all 150ms cubic-bezier(0.4, 0, 0.2, 1);
  --bkm-transition-normal: all 200ms cubic-bezier(0.4, 0, 0.2, 1);
  --bkm-transition-slow: all 300ms cubic-bezier(0.4, 0, 0.2, 1);
  --bkm-transition-entrance: all 500ms cubic-bezier(0, 0, 0.2, 1);
  --bkm-transition-exit: all 200ms cubic-bezier(0.4, 0, 1, 1);
  --bkm-transition-spring: all 400ms cubic-bezier(0.34, 1.56, 0.64, 1);
  --bkm-transition-color: color 150ms ease, background-color 150ms ease, border-color 150ms ease;

  /* === Z-Index === */
  --bkm-z-dropdown: 100;
  --bkm-z-sticky: 200;
  --bkm-z-nav: 300;
  --bkm-z-modal-backdrop: 400;
  --bkm-z-modal: 500;
  --bkm-z-popover: 600;
  --bkm-z-tooltip: 700;
  --bkm-z-toast: 800;
  --bkm-z-max: 9999;

  /* === Typography === */
  --bkm-font-display: 'Unbounded', system-ui, sans-serif;
  --bkm-font-body: 'Inter', system-ui, sans-serif;
  --bkm-font-mono: 'Geist Mono', 'Source Code Pro', 'JetBrains Mono', monospace;
}
```

## Tailwind CSS v4 Configuration

```css
/* In your index.css with Tailwind v4 */
@theme inline {
  --color-bkm-lime: oklch(0.87 0.22 115);
  --color-bkm-lime-soft: oklch(0.92 0.15 115);
  --color-bkm-lime-muted: oklch(0.95 0.08 115);
  --color-bkm-deep-green: oklch(0.32 0.06 170);
  --color-bkm-deep-green-light: oklch(0.40 0.07 168);
  --color-bkm-deep-green-90: oklch(0.32 0.06 170 / 0.90);
  --color-bkm-surface-dark-deep: oklch(0.22 0.04 170);
  --color-bkm-pure-green: oklch(0.63 0.18 145);
  --color-bkm-transition-green: oklch(0.47 0.12 155);
  --color-bkm-canvas: oklch(1 0 0);
  --color-bkm-canvas-warm: oklch(0.97 0.005 80);
  --color-bkm-canvas-cool: oklch(0.98 0.003 160);
  --color-bkm-surface: oklch(0.95 0.005 80);
  --color-bkm-surface-soft: oklch(0.98 0.003 80);
  --color-bkm-ink: oklch(0.15 0 0);
  --color-bkm-charcoal: oklch(0.23 0 0);
  --color-bkm-stone-grey: oklch(0.38 0 0);
  --color-bkm-steel: oklch(0.47 0 0);
  --color-bkm-muted: oklch(0.59 0 0);
  --color-bkm-ash: oklch(0.72 0 0);
  --color-bkm-hairline: oklch(0.92 0.005 80);
  --color-bkm-hairline-strong: oklch(0.82 0.005 80);
  --color-bkm-error: oklch(0.53 0.21 25);
  --color-bkm-warning: oklch(0.63 0.16 70);
  --color-bkm-success: oklch(0.63 0.18 145);
  --color-bkm-info: oklch(0.55 0.14 240);

  --radius-bkm-none: 0px;
  --radius-bkm-xs: 2px;
  --radius-bkm-sm: 4px;
  --radius-bkm-md: 8px;
  --radius-bkm-lg: 12px;
  --radius-bkm-xl: 16px;
  --radius-bkm-xxl: 24px;
  --radius-bkm-full: 9999px;

  --spacing-bkm-xxs: 4px;
  --spacing-bkm-xs: 8px;
  --spacing-bkm-sm: 12px;
  --spacing-bkm-md: 16px;
  --spacing-bkm-lg: 24px;
  --spacing-bkm-xl: 32px;
  --spacing-bkm-xxl: 48px;
  --spacing-bkm-xxxl: 64px;
  --spacing-bkm-section: 80px;
  --spacing-bkm-section-lg: 120px;
  --spacing-bkm-hero: 160px;

  --font-bkm-display: 'Unbounded', system-ui, sans-serif;
  --font-bkm-body: 'Inter', system-ui, sans-serif;
  --font-bkm-mono: 'Geist Mono', 'Source Code Pro', 'JetBrains Mono', monospace;
}
```

## Google Fonts Import

```html
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Unbounded:wght@900&family=Inter:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap" rel="stylesheet" />
```

## Component Implementation Patterns

### Button Primary (Pro Line — Angular)

```html
<button class="
  bg-[#b4e717] text-[#1c4b42]
  font-['Unbounded'] text-sm font-black uppercase tracking-[0.5px]
  px-6 py-3 h-12 min-w-[120px]
  rounded-none
  transition-all duration-150 ease-[cubic-bezier(0.4,0,0.2,1)]
  hover:bg-white
  active:scale-[0.98]
  disabled:bg-[#f0efec] disabled:text-[#8a8a8a] disabled:cursor-not-allowed disabled:opacity-40
  focus-visible:outline-none focus-visible:shadow-[0_0_0_2px_#ffffff,0_0_0_4px_#4daf46]
">
  JETZT KAUFEN
</button>
```

### Button Primary (Home Line — Pill)

```html
<button class="
  bg-[#4daf46] text-white
  font-['Unbounded'] text-sm font-black uppercase tracking-[0.5px]
  px-7 py-3 h-12
  rounded-full
  transition-all duration-150 ease-[cubic-bezier(0.4,0,0.2,1)]
  hover:bg-[#287d4b]
  active:scale-[0.98]
  disabled:bg-[#f0efec] disabled:text-[#8a8a8a] disabled:cursor-not-allowed disabled:opacity-40
  focus-visible:outline-none focus-visible:shadow-[0_0_0_2px_#ffffff,0_0_0_4px_#4daf46]
">
  In den Warenkorb
</button>
```

### Button Outline (Dark Surface)

```html
<button class="
  bg-transparent text-white
  font-['Unbounded'] text-sm font-black uppercase tracking-[0.5px]
  px-6 py-3 h-12
  rounded-none
  border-2 border-white/30
  transition-all duration-150
  hover:border-[#b4e717] hover:text-[#b4e717]
  active:scale-[0.98]
  focus-visible:outline-none focus-visible:shadow-[0_0_0_2px_#1c4b42,0_0_0_4px_#b4e717]
">
  FACHBETRIEB FINDEN
</button>
```

### Card (Shadow-as-Border with Hover Lift)

```html
<div class="
  bg-white rounded-[12px] p-8
  shadow-[rgba(0,0,0,0.08)_0px_0px_0px_1px,rgba(0,0,0,0.04)_0px_2px_4px]
  transition-all duration-200 ease-[cubic-bezier(0.4,0,0.2,1)]
  hover:shadow-[rgba(0,0,0,0.08)_0px_0px_0px_1px,rgba(0,0,0,0.06)_0px_8px_16px_-4px]
  hover:-translate-y-0.5
">
  <h3 class="font-['Unbounded'] text-lg font-black uppercase tracking-[-0.3px] text-[#1a1a1a]">
    KELLERSCHUTZ PRO
  </h3>
  <p class="font-['Inter'] text-base text-[#494949] mt-3 leading-relaxed">
    Professionelle Horizontalsperre mit MicroPorex® Technologie.
  </p>
</div>
```

### Card Pro (Angular + Left Border)

```html
<div class="
  bg-white rounded-[2px] p-8
  shadow-[rgba(0,0,0,0.08)_0px_0px_0px_1px,rgba(0,0,0,0.04)_0px_2px_4px]
  border-l-4 border-l-[#1c4b42]
">
  <!-- Pro Line content -->
</div>
```

### Card Dark (Info Box)

```html
<div class="
  bg-[#1c4b42] rounded-none p-8
  border-l-4 border-l-[#b4e717]
">
  <h4 class="font-['Unbounded'] text-base font-black uppercase text-white">
    TECHNISCHE DATEN
  </h4>
  <p class="font-['Inter'] text-base text-white/70 mt-3 leading-relaxed">
    Verbrauch: <span class="font-['Geist_Mono'] font-medium text-[#b4e717]">1,2 kg/m²</span>
  </p>
</div>
```

### Hero Band (Dark Marketing)

```html
<section class="bg-[#1c4b42] py-40 relative overflow-hidden">
  <!-- Chevron pattern at 5% opacity -->
  <div class="absolute inset-0 opacity-[0.05]" aria-hidden="true">
    <svg class="w-full h-full" viewBox="0 0 1440 800" fill="none">
      <path d="M720 200 L1440 600 L1440 800 L720 400 L0 800 L0 600 Z" fill="white"/>
    </svg>
  </div>
  <div class="max-w-[1280px] mx-auto px-8 md:px-16 relative z-10">
    <p class="font-['Inter'] text-[13px] font-semibold uppercase tracking-[1.5px] text-white/50 mb-6">
      Bauwerksabdichtung seit 1928
    </p>
    <h1 class="font-['Unbounded'] text-5xl md:text-7xl font-black uppercase text-white tracking-[-3px] leading-none max-w-[800px]">
      SCHUTZ DER HÄLT
    </h1>
    <p class="font-['Inter'] text-xl text-white/70 mt-6 max-w-[640px] leading-relaxed">
      Professionelle Bauwerksabdichtung mit MicroPorex® Technologie für dauerhafte Ergebnisse.
    </p>
    <div class="flex flex-wrap gap-4 mt-10">
      <button class="bg-[#b4e717] text-[#1c4b42] font-['Unbounded'] text-sm font-black uppercase px-6 py-3 h-12 tracking-[0.5px] hover:bg-white transition-all duration-150">
        PRODUKTE ENTDECKEN
      </button>
      <button class="border-2 border-white/30 text-white font-['Unbounded'] text-sm font-black uppercase px-6 py-3 h-12 tracking-[0.5px] hover:border-[#b4e717] hover:text-[#b4e717] transition-colors duration-150">
        FACHBETRIEB FINDEN
      </button>
    </div>
  </div>
</section>
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
  <div class="flex justify-between items-center py-3">
    <span class="font-['Inter'] text-sm text-[#6b6b6b]">Gebindegröße</span>
    <span class="font-['Geist_Mono'] text-sm font-medium text-[#1c4b42]">25 kg</span>
  </div>
</div>
```

### Badge Pro

```html
<span class="
  inline-flex items-center
  bg-[#1c4b42] text-[#b4e717]
  font-['Inter'] text-xs font-bold uppercase tracking-[0.5px]
  px-2.5 py-1 rounded-[2px]
">
  PRO
</span>
```

### Badge Home

```html
<span class="
  inline-flex items-center
  bg-[#4daf46] text-white
  font-['Inter'] text-xs font-bold uppercase tracking-[0.5px]
  px-3 py-1 rounded-full
">
  HOME
</span>
```

### Badge MicroPorex

```html
<span class="
  inline-flex items-center
  bg-[#f0efec] text-[#494949]
  font-['Geist_Mono'] text-xs font-medium
  px-2.5 py-1 rounded-[4px]
  shadow-[rgba(0,0,0,0.08)_0px_0px_0px_1px]
">
  MicroPorex®
</span>
```

### Navigation Bar

```html
<nav class="
  sticky top-0 z-[300]
  bg-[#1c4b42] h-16
  backdrop-blur-[12px]
  transition-all duration-200
" id="main-nav">
  <div class="max-w-[1280px] mx-auto px-8 h-full flex items-center justify-between">
    <!-- Logo -->
    <a href="/" class="flex items-center">
      <img src="/logo-white-green.svg" alt="BKM Mannesmann" class="h-8" />
    </a>
    <!-- Links -->
    <div class="hidden md:flex items-center gap-8">
      <a href="/produkte" class="font-['Inter'] text-sm font-medium text-white/70 hover:text-[#b4e717] transition-colors">Produkte</a>
      <a href="/technologie" class="font-['Inter'] text-sm font-medium text-white/70 hover:text-[#b4e717] transition-colors">Technologie</a>
      <a href="/fachbetriebe" class="font-['Inter'] text-sm font-medium text-white/70 hover:text-[#b4e717] transition-colors">Fachbetriebe</a>
      <a href="/kontakt" class="font-['Inter'] text-sm font-medium text-white/70 hover:text-[#b4e717] transition-colors">Kontakt</a>
    </div>
    <!-- CTA -->
    <button class="bg-[#b4e717] text-[#1c4b42] font-['Unbounded'] text-xs font-black uppercase px-4 py-2 tracking-[0.5px]">
      ANFRAGE
    </button>
  </div>
</nav>
```

### Toast Notification

```html
<div class="
  bg-white rounded-[12px] px-6 py-4
  shadow-[rgba(0,0,0,0.08)_0px_0px_0px_1px,rgba(0,0,0,0.08)_0px_12px_24px_-8px]
  border-l-4 border-l-[#4daf46]
  flex items-start gap-3
  animate-[slide-in-right_300ms_ease]
" role="alert">
  <svg class="w-5 h-5 text-[#4daf46] mt-0.5 shrink-0"><!-- check-circle icon --></svg>
  <div>
    <p class="font-['Inter'] text-sm font-medium text-[#1a1a1a]">Anfrage gesendet</p>
    <p class="font-['Inter'] text-sm text-[#6b6b6b] mt-1">Wir melden uns innerhalb von 24 Stunden.</p>
  </div>
</div>
```

### Empty State

```html
<div class="text-center py-20">
  <svg class="w-12 h-12 text-[#b0b0b0] mx-auto"><!-- inbox icon --></svg>
  <h3 class="font-['Unbounded'] text-lg font-black uppercase text-[#1a1a1a] mt-6 tracking-[-0.3px]">
    KEINE ERGEBNISSE
  </h3>
  <p class="font-['Inter'] text-base text-[#6b6b6b] mt-3 max-w-[400px] mx-auto">
    Versuche einen anderen Suchbegriff oder erweitere deine Filter.
  </p>
  <button class="mt-6 bg-[#1c4b42] text-[#b4e717] font-['Unbounded'] text-sm font-black uppercase px-6 py-3 tracking-[0.5px]">
    FILTER ZURÜCKSETZEN
  </button>
</div>
```

### Skeleton Loading

```html
<div class="animate-pulse">
  <div class="bg-[#f0efec] rounded-[12px] h-48 w-full"></div>
  <div class="mt-4 space-y-3">
    <div class="bg-[#f0efec] rounded-[4px] h-5 w-3/4"></div>
    <div class="bg-[#f0efec] rounded-[4px] h-4 w-full"></div>
    <div class="bg-[#f0efec] rounded-[4px] h-4 w-5/6"></div>
  </div>
</div>
```

## Page Template Structures

### Landing Page Flow

```
1. [DARK]  Nav Bar (sticky, 64px, deep green)
2. [DARK]  Hero Band (160px padding, chevron pattern, headline + CTA)
3. [LIGHT] Feature Section (3-up cards, shadow-as-border, canvas-warm bg)
4. [LIGHT] Spec Highlight (stat cards with Geist Mono values)
5. [DARK]  Testimonial Band (deep green, quote in white, lime accent)
6. [LIGHT] Product Grid (3-up or 4-up cards, hover-lift)
7. [DARK]  CTA Banner (centered headline + lime button)
8. [DARK]  Footer (4-column links, deep green)
```

### Product Detail Page Flow

```
1. [DARK]  Nav Bar
2. [LIGHT] Breadcrumb
3. [LIGHT] Product Hero (image left 50%, specs right 50%)
4. [LIGHT] Tab Navigation (segmented tabs with lime underline)
5. [LIGHT] Tab Content (description / spec-table / downloads)
6. [LIGHT] Related Products (3-up card grid)
7. [DARK]  CTA Banner
8. [DARK]  Footer
```

### Technical Data Sheet (TDS) Flow

```
1. [DARK]  Header (product name, badge-pro, badge-microporex)
2. [LIGHT] Spec Table (key-value pairs, Geist Mono values)
3. [LIGHT] Application Areas (icon grid, 3-up or 4-up)
4. [LIGHT] Processing Instructions (step cards with numbers)
5. [LIGHT] Downloads Section (PDF links with file-size badges)
6. [DARK]  Footer
```

## Context for AI Agents

### What BKM Mannesmann Does
BKM Mannesmann AG manufactures building protection products — specifically solutions against rising damp (aufsteigende Feuchtigkeit) and laterally penetrating water (seitlich drückendes Wasser). Their core technologies include horizontal barriers (Horizontalsperren), surface barriers (Flächensperren), and resin injections (Harzinjektionen). The proprietary MicroPorex® technology is the ingredient brand that differentiates their products. Founded 1928.

### Two Product Lines
- **BKM Pro Line**: Professional-grade products for certified specialist companies (Fachbetriebe). Angular design language (0–4px radius), Deep Green + Lime Green, technical documentation, Sie-Ansprache.
- **BKM Home Line**: DIY products for homeowners (Novu products). Rounded design language (12px–pill), Pure Green, warm and encouraging tone, Du-Ansprache.

### Two Target Audiences
- **Fachbetriebsunternehmer** (specialist company owners): Typically 50+, conservative, skeptical of change. Emphasize tangible differentiation and proven results. Use Sie-Ansprache.
- **Hausbesitzer** (homeowners): Quality-conscious, seeking reliable solutions. Dual CTA approach: DIY with Home Line OR professional solution through certified Fachbetrieb. Use Du-Ansprache.

### Logo Rules
- Light backgrounds: grey-green BKM Mannesmann logo
- Dark backgrounds: white-green BKM Mannesmann logo
- Minimum clear space: 1× the cap height of "BKM" text in all directions
- Never rotate, stretch, recolor, or add effects to the logo

### Fachbetrieb Portal Differentiation
- Use **Pure Green** (`#4daf46`) instead of Deep Green for Fachbetrieb-specific pages
- Use **Cool White** (`#f8faf9`) instead of Warm White for canvas
- Differentiate clearly: Fachbetrieb = independent certified craftsman, BKM = manufacturer/certifier
- Fachbetrieb pages use Stone Grey + Pure Green color scheme

## Output Formats

This design system supports generation of:

| Format | Key Adaptations |
|--------|----------------|
| **Websites** (React, HTML/CSS, Tailwind) | Full token system, all components, responsive breakpoints |
| **Presentations/Slides** | Dark title slides, light content slides, Unbounded headlines, Geist Mono data |
| **Instagram Carousel** | 1080×1080 or 1080×1350, 80px safe zone, max 40 words/slide, dark cover + light content |
| **Print** (Brochures, TDS, Labels) | CMYK equivalents, 3mm bleed, 5mm safe zone, 10–12pt body |
| **Email Templates** | Inline CSS with token values, max-width 600px, system font fallbacks |
| **Social Media Graphics** | Apply color + typography tokens, ensure text readability at small sizes |
| **Fahrzeugbeschriftung** | Oracal 751C foil colors, simplified logo, high-contrast combinations |

## Implementation Checklist

- [ ] Load Unbounded (900) + Inter (400, 500, 600, 700) + Geist Mono (400, 500) via Google Fonts
- [ ] Set page background to `#f6f5f2` (canvas-warm) for documentation, `#1c4b42` (deep green) for marketing
- [ ] Apply negative letter-spacing to Unbounded headlines (scale with size)
- [ ] Use shadow-as-border on all cards (no CSS `border`)
- [ ] Implement double-ring focus indicators on all interactive elements
- [ ] Set max content width to 1280px (1440px for hero bands)
- [ ] Use 48px minimum height for all buttons and inputs
- [ ] Implement hover-lift on cards: translateY(-2px) + shadow intensification
- [ ] Respect `prefers-reduced-motion: reduce` — collapse all animations to 0ms
- [ ] Use correct logo variant (white-green on dark, grey-green on light)
- [ ] Validate all text/background combinations against WCAG 2.1 AA (4.5:1 body, 3:1 large)
- [ ] Ensure touch targets ≥ 44px on mobile
- [ ] Implement skeleton loading states that match final content dimensions
- [ ] Use 3-level text opacity on dark surfaces (100%/70%/50%)
- [ ] Include MicroPorex® with ® on first mention per page
- [ ] Test responsive behavior at all 5 breakpoints (320, 480, 768, 1024, 1280, 1440)
