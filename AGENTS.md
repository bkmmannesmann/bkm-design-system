# AGENTS.md — BKM Mannesmann Design System

> Instructions for AI coding agents working with BKM Mannesmann projects.

## Quick Start

1. Read `DESIGN.md` — it contains all design tokens (colors, typography, spacing, shadows, components, animations) in YAML frontmatter + prose documentation.
2. Use token references (`{colors.brand-deep-green}`, `{typography.heading-1}`, `{shadows.subtle}`) in your implementation.
3. Follow the **Do's and Don'ts** in Section 11 strictly — they are non-negotiable brand rules.
4. Reference the **Agent Prompt Guide** (Section 13) for quick copy-paste values.

## Critical Rules (Never Break These)

### Typography
- **Unbounded** is the ONLY headline/button font. Weight 900. Always uppercase. Always negative letter-spacing at display sizes.
- **Inter** is the ONLY body font. Weights 400/500/700.
- **Geist Mono** is the ONLY monospace font. Used for technical data, article numbers, measurements.
- Never mix these roles. Never use Inter for headlines. Never use Unbounded for body text.

### Color
- **Lime Green (`#b4e717`)** is ONLY for interactive elements: buttons, active states, checkmarks, icons on dark.
- Never use Lime Green for text (contrast fails), backgrounds (too aggressive), or decoration.
- **One Lime CTA per viewport fold maximum.** Scarcity = urgency.
- **Deep Green (`#1c4b42`)** for dark surfaces. Never use pure black (`#000000`).
- **Stone Grey (`#494949`)** for body text on light. Never pure black.

### Geometry
- **Pro Line** = angular (0–4px radius). Technical. Professional.
- **Home Line** = rounded (8–9999px radius). Accessible. Friendly.
- Never apply pill shapes to Pro Line. Never apply angular shapes to Home Line.

### Shadows
- Use `box-shadow` stacks instead of CSS `border` on cards.
- Ring layer: `rgba(0,0,0,0.08) 0px 0px 0px 1px`
- Featured cards include inner white ring: `rgba(255,255,255,1) 0px 0px 0px 1px inset`

### Layout
- Hero copy is ALWAYS left-aligned, asymmetric (60/40 split).
- Never center hero headlines.
- Dark bands alternate with light bands for section rhythm.

## File Structure

```
DESIGN.md              → Complete design tokens + documentation (primary source)
AGENTS.md              → This file (agent instructions)
README.md              → Project overview + usage guide
CONTRIBUTING.md        → Contribution guidelines
CHANGELOG.md           → Version history
docs/
  brand-voice.md       → Tone, claims, copy patterns
  digitale-medien.md   → Web/app implementation details
  print-anwendungen.md → Print specifications
  microporex-und-technik.md → Ingredient brand rules
  keyvisual.md         → Chevron pattern specifications
  logo.md              → Logo variants + placement rules
  icon-system.md       → Icon specifications
  referenzen.md        → External design system references
  verbesserungsvorschlaege.md → Improvement proposals
```

## Implementation Checklist

When building any BKM Mannesmann UI:

- [ ] Load Unbounded (900) + Inter (400, 500, 700) + Geist Mono (400, 500) via Google Fonts
- [ ] Set page background to `#f6f5f2` (Sand White) for documentation, `#1c4b42` (Deep Green) for marketing heroes
- [ ] Apply negative letter-spacing to Unbounded headlines (-2.5px at 64px, -1.5px at 48px, -1px at 36px)
- [ ] Use shadow-as-border on all cards: `rgba(0,0,0,0.08) 0px 0px 0px 1px`
- [ ] Implement focus rings: `0 0 0 2px #ffffff, 0 0 0 4px #4daf46` (light) or `0 0 0 2px #1c4b42, 0 0 0 4px #b4e717` (dark)
- [ ] Set max content width to 1280px
- [ ] Use 48px minimum height for all buttons and inputs
- [ ] Implement hover-lift on cards: translateY(-2px) + shadow intensification
- [ ] Respect `prefers-reduced-motion: reduce`
- [ ] Use BKM white-green logo on dark backgrounds, grey-green logo on light backgrounds

## CSS Custom Properties Template

```css
:root {
  /* Brand Greens */
  --bkm-deep-green: #1c4b42;
  --bkm-deep-green-light: #2a6b5e;
  --bkm-transition-green: #287d4b;
  --bkm-pure-green: #4daf46;
  --bkm-lime: #b4e717;
  --bkm-lime-soft: #d4f07a;
  --bkm-lime-muted: #e8f5b3;

  /* Neutrals */
  --bkm-ink: #1a1a1a;
  --bkm-charcoal: #2d2d2d;
  --bkm-stone-grey: #494949;
  --bkm-steel: #6b6b6b;
  --bkm-muted: #8a8a8a;
  --bkm-ash: #b0b0b0;

  /* Surfaces */
  --bkm-canvas: #ffffff;
  --bkm-canvas-warm: #f6f5f2;
  --bkm-surface: #f0efec;
  --bkm-surface-soft: #fafaf8;

  /* Borders */
  --bkm-hairline: #e8e6e1;
  --bkm-hairline-soft: #f0efec;
  --bkm-hairline-strong: #c8c5be;

  /* Semantic */
  --bkm-error: #dc2626;
  --bkm-warning: #d97706;
  --bkm-success: #4daf46;
  --bkm-info: #0284c7;

  /* Shadows */
  --bkm-shadow-ring: rgba(0,0,0,0.08) 0px 0px 0px 1px;
  --bkm-shadow-subtle: rgba(0,0,0,0.08) 0px 0px 0px 1px, rgba(0,0,0,0.04) 0px 2px 4px;
  --bkm-shadow-card: rgba(0,0,0,0.08) 0px 0px 0px 1px, rgba(0,0,0,0.04) 0px 4px 8px;
  --bkm-shadow-featured: rgba(0,0,0,0.08) 0px 0px 0px 1px, rgba(0,0,0,0.06) 0px 8px 16px -4px, rgba(255,255,255,1) 0px 0px 0px 1px inset;
  --bkm-shadow-elevated: rgba(0,0,0,0.08) 0px 0px 0px 1px, rgba(0,0,0,0.08) 0px 12px 24px -8px;
  --bkm-shadow-focus: 0 0 0 2px #ffffff, 0 0 0 4px #4daf46;
  --bkm-shadow-focus-dark: 0 0 0 2px #1c4b42, 0 0 0 4px #b4e717;

  /* Spacing */
  --bkm-space-xxs: 4px;
  --bkm-space-xs: 8px;
  --bkm-space-sm: 12px;
  --bkm-space-md: 16px;
  --bkm-space-lg: 24px;
  --bkm-space-xl: 32px;
  --bkm-space-xxl: 48px;
  --bkm-space-section: 64px;
  --bkm-space-section-lg: 96px;
  --bkm-space-hero: 120px;

  /* Radius */
  --bkm-radius-none: 0px;
  --bkm-radius-xs: 2px;
  --bkm-radius-sm: 4px;
  --bkm-radius-md: 8px;
  --bkm-radius-lg: 12px;
  --bkm-radius-xl: 16px;
  --bkm-radius-xxl: 24px;
  --bkm-radius-full: 9999px;

  /* Typography */
  --bkm-font-display: 'Unbounded', system-ui, sans-serif;
  --bkm-font-body: 'Inter', system-ui, -apple-system, sans-serif;
  --bkm-font-mono: 'Geist Mono', 'Source Code Pro', ui-monospace, monospace;

  /* Animation */
  --bkm-duration-fast: 150ms;
  --bkm-duration-normal: 200ms;
  --bkm-duration-slow: 300ms;
  --bkm-duration-entrance: 500ms;
  --bkm-ease-default: cubic-bezier(0.4, 0, 0.2, 1);
  --bkm-ease-entrance: cubic-bezier(0, 0, 0.2, 1);
  --bkm-ease-exit: cubic-bezier(0.4, 0, 1, 1);
  --bkm-ease-spring: cubic-bezier(0.34, 1.56, 0.64, 1);
}
```

## Tailwind CSS v4 Configuration

```css
@theme inline {
  --color-bkm-deep-green: oklch(0.35 0.06 165);
  --color-bkm-deep-green-light: oklch(0.43 0.06 165);
  --color-bkm-transition-green: oklch(0.48 0.10 155);
  --color-bkm-pure-green: oklch(0.62 0.15 140);
  --color-bkm-lime: oklch(0.87 0.20 115);
  --color-bkm-lime-soft: oklch(0.91 0.14 115);
  --color-bkm-lime-muted: oklch(0.94 0.08 115);
  --color-bkm-canvas-warm: oklch(0.97 0.005 80);
  --color-bkm-surface: oklch(0.95 0.005 80);
  --color-bkm-ink: oklch(0.15 0 0);
  --color-bkm-stone-grey: oklch(0.38 0 0);
  --color-bkm-steel: oklch(0.48 0 0);
  --color-bkm-muted: oklch(0.60 0 0);
  --color-bkm-hairline: oklch(0.92 0.005 80);
  --radius-bkm-none: 0px;
  --radius-bkm-xs: 2px;
  --radius-bkm-sm: 4px;
  --radius-bkm-md: 8px;
  --radius-bkm-lg: 12px;
  --radius-bkm-full: 9999px;
}
```

## Context for AI Agents

### What BKM Mannesmann Does
BKM Mannesmann AG manufactures building protection products — specifically solutions against rising damp (aufsteigende Feuchtigkeit) and laterally penetrating water (seitlich drückendes Wasser). Their core technologies include horizontal barriers (Horizontalsperren), surface barriers (Flächensperren), and resin injections (Harzinjektionen). The proprietary MicroPorex technology is the ingredient brand that differentiates their products.

### Two Product Lines
- **BKM Pro Line**: Professional-grade products for certified specialist companies (Fachbetriebe). Angular design language, Deep Green + Lime Green, technical documentation.
- **BKM Home Line**: DIY products for homeowners (Novu products). Rounded design language, Pure Green, warm and encouraging tone.

### Two Target Audiences
- **Fachbetriebsunternehmer** (specialist company owners): Typically 50+, conservative, skeptical of change. Emphasize tangible differentiation and proven results.
- **Hausbesitzer** (homeowners): Quality-conscious, seeking reliable solutions. Dual CTA approach: DIY with Home Line OR professional solution through certified Fachbetrieb.

### Logo Rules
- Light backgrounds: grey-green BKM Mannesmann logo
- Dark backgrounds: white-green BKM Mannesmann logo
- Minimum clear space: 1x the cap height of "BKM" text in all directions

### Fachbetrieb Branding
- Use **Pure Green** (`#4daf46`) instead of Deep Green for Fachbetrieb-specific pages
- Differentiate clearly: Fachbetrieb = independent certified craftsman, BKM = manufacturer/certifier
- Fachbetrieb pages use Stone Grey + Pure Green color scheme

## Output Formats

This design system supports generation of:
- **Websites** (React, HTML/CSS, Tailwind)
- **Presentations/Slides** (apply tokens to slide design)
- **Instagram Carousel Posts** (4:5 or 1:1 format, apply tokens)
- **Print Documents** (brochures, TDS, labels — see `docs/print-anwendungen.md`)
- **Email Templates** (inline CSS with token values)
- **Social Media Graphics** (apply color + typography tokens)

For each format, reference the appropriate tokens from `DESIGN.md` and adapt spacing/sizing to the medium's constraints.
