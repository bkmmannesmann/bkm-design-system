---
version: alpha
name: BKM Mannesmann AG
description: >
  Building protection manufacturer (est. 1928). Visual identity communicates
  protective authority through material contrast. One unified brand world with
  two color contexts: the BKM AG context (Deep Green, Lime, White) and the
  Fachbetrieb context (Stone Grey, Pure Green, White). The green tones tell
  the story of the drying process — Deep Green represents moisture/the problem,
  Pure Green represents the dry end state/the solution.
colors:
  # === BKM AG Context (Primary Brand World) ===
  primary: "#1c4b42"
  primary-light: "#2a6b5e"
  on-primary: "#ffffff"
  secondary: "#b4e717"
  on-secondary: "#1c4b42"
  tertiary: "#287d4b"
  on-tertiary: "#ffffff"
  neutral: "#f6f5f2"
  neutral-dim: "#f0efec"
  neutral-bright: "#ffffff"
  surface: "#ffffff"
  surface-container: "#fafaf8"
  on-surface: "#1a1a1a"
  on-surface-variant: "#494949"
  outline: "#c8c5be"
  outline-variant: "#e8e6e1"
  # === Fachbetrieb Context ===
  fachbetrieb-primary: "#4daf46"
  fachbetrieb-primary-deep: "#287d4b"
  on-fachbetrieb-primary: "#ffffff"
  fachbetrieb-secondary: "#494949"
  on-fachbetrieb-secondary: "#ffffff"
  fachbetrieb-surface: "#f6f5f2"
  # === Semantic ===
  error: "#dc2626"
  on-error: "#ffffff"
  error-container: "#fef2f2"
  on-error-container: "#991b1b"
typography:
  headline-display:
    fontFamily: Unbounded
    fontSize: 72px
    fontWeight: 900
    lineHeight: 1.0
    letterSpacing: -0.04em
  headline-lg:
    fontFamily: Unbounded
    fontSize: 56px
    fontWeight: 900
    lineHeight: 1.05
    letterSpacing: -0.03em
  headline-md:
    fontFamily: Unbounded
    fontSize: 44px
    fontWeight: 900
    lineHeight: 1.08
    letterSpacing: -0.02em
  headline-sm:
    fontFamily: Unbounded
    fontSize: 36px
    fontWeight: 900
    lineHeight: 1.15
    letterSpacing: -0.02em
  title-lg:
    fontFamily: Unbounded
    fontSize: 28px
    fontWeight: 900
    lineHeight: 1.2
    letterSpacing: -0.01em
  title-md:
    fontFamily: Unbounded
    fontSize: 22px
    fontWeight: 900
    lineHeight: 1.25
  title-sm:
    fontFamily: Unbounded
    fontSize: 18px
    fontWeight: 900
    lineHeight: 1.3
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.7
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
  label-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: 0.02em
  label-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.0
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: 0.05em
  code-md:
    fontFamily: Geist Mono
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
  code-sm:
    fontFamily: Geist Mono
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
rounded:
  none: 0px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 16px
  full: 9999px
spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  xxl: 48px
  section: 80px
  hero: 160px
components:
  # === BKM AG Buttons ===
  button-primary:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-secondary}"
    typography: "{typography.label-lg}"
    rounded: "{rounded.sm}"
    padding: 12px
    height: 48px
  button-primary-hover:
    backgroundColor: "{colors.neutral-bright}"
    textColor: "{colors.on-secondary}"
  button-primary-active:
    backgroundColor: "{colors.neutral-bright}"
    textColor: "{colors.primary}"
  button-secondary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-lg}"
    rounded: "{rounded.sm}"
    padding: 12px
    height: 48px
  button-secondary-hover:
    backgroundColor: "{colors.primary-light}"
  button-outline:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary}"
    typography: "{typography.label-lg}"
    rounded: "{rounded.sm}"
    padding: 12px
    height: 48px
  button-outline-hover:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
  button-outline-dark:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-lg}"
    rounded: "{rounded.sm}"
    padding: 12px
    height: 48px
  button-outline-dark-hover:
    textColor: "{colors.secondary}"
  # === Fachbetrieb Buttons ===
  button-fachbetrieb-primary:
    backgroundColor: "{colors.fachbetrieb-primary-deep}"
    textColor: "{colors.on-fachbetrieb-primary}"
    typography: "{typography.label-lg}"
    rounded: "{rounded.sm}"
    padding: 12px
    height: 48px
  button-fachbetrieb-primary-hover:
    backgroundColor: "{colors.fachbetrieb-secondary}"
  # === Cards ===
  card-base:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl}"
  card-base-hover:
    backgroundColor: "{colors.surface}"
  card-dark:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xl}"
  card-fachbetrieb:
    backgroundColor: "{colors.fachbetrieb-surface}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl}"
  # === Badges ===
  badge-product:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.secondary}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.sm}"
    padding: 4px
  badge-fachbetrieb:
    backgroundColor: "{colors.fachbetrieb-primary-deep}"
    textColor: "{colors.on-fachbetrieb-primary}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.sm}"
    padding: 4px
  badge-microporex:
    backgroundColor: "{colors.neutral-dim}"
    textColor: "{colors.on-surface-variant}"
    typography: "{typography.code-sm}"
    rounded: "{rounded.sm}"
    padding: 4px
  # === Form Elements ===
  input-field:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 12px
    height: 48px
  input-field-focus:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface}"
  input-field-error:
    backgroundColor: "{colors.error-container}"
    textColor: "{colors.on-error-container}"
  # === Navigation ===
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    height: 64px
  nav-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.label-md}"
  nav-link-hover:
    textColor: "{colors.secondary}"
  nav-bar-fachbetrieb:
    backgroundColor: "{colors.fachbetrieb-secondary}"
    textColor: "{colors.on-fachbetrieb-secondary}"
    height: 64px
  # === Technical Data ===
  spec-row:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface-variant}"
    padding: 12px
  # === Hero ===
  hero-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    padding: "{spacing.hero}"
  hero-fachbetrieb:
    backgroundColor: "{colors.fachbetrieb-surface}"
    textColor: "{colors.on-surface}"
    padding: "{spacing.hero}"
---

## Overview

BKM Mannesmann AG is a building protection manufacturer established in 1928. The visual identity communicates one thing above all: **Schutz** (protection). Every design decision traces back to this core promise.

### One Brand, Two Color Contexts

The BKM world is unified — there are no separate "sub-brands" with different design languages. However, two color contexts exist within the same design system:

**BKM AG Context** — The primary brand world. Used for the corporate website, product pages, the online shop, marketing materials, and all content where BKM Mannesmann AG speaks as the manufacturer. Colors: Deep Green, Lime Green, White, Sand White.

**Fachbetrieb Context** — Used for landingpages, portals, and materials where certified specialist companies (Fachbetriebe) are the subject. These are independent craftsmen certified by BKM to apply Pro Line products at the customer's site. The design structure is identical, but the color palette shifts to the original BKM logo colors: Stone Grey, Pure Green, White, Sand White. This differentiation ensures customers understand that the Fachbetrieb is an independent, certified entity performing craft services — while BKM Mannesmann AG is the product manufacturer and certifier.

### The Story of Green

The different green tones are not arbitrary — they visualize the drying process of walls, from problem to solution:

- **Deep Green (#1c4b42)** — Represents moisture, dampness, the problem state. A wall that is wet. This is the dominant brand color because BKM's entire business starts with the problem: rising damp, laterally penetrating water.
- **Transition Green (#287d4b)** — The process of drying. The barrier is working.
- **Pure Green (#4daf46)** — The dry end state. The solution achieved. The wall is protected. This color identifies the Fachbetrieb context because the Fachbetrieb delivers the solution at the customer's site.
- **Lime Green (#b4e717)** — An effect color added later to the system. It works exceptionally well with Deep Green as a high-contrast accent for interactive elements and key highlights. It is never used in the Fachbetrieb context.

### What This System Is NOT

This is not a generic SaaS interface. It is not a "clean modern website." It is a system that communicates the physical reality of building protection — heavy materials, precise measurements, protective barriers. If a design decision could belong to any brand, it is wrong for BKM.

## Colors

The palette communicates protection through depth and material contrast.

- **Primary (#1c4b42):** Deep Green — the protective, authoritative surface color. Represents moisture/the problem. Used for dark marketing surfaces, navigation, and the dominant brand presence.
- **Secondary (#b4e717):** Lime Green — the high-contrast interactive accent. Used ONLY for primary CTAs and active states on dark surfaces. Never decorative, never on large surfaces, never as body text. Not used in Fachbetrieb context.
- **Tertiary (#287d4b):** Transition Green — the process color. Used for links, secondary actions, and hover states on light surfaces.
- **Neutral (#f6f5f2):** Sand White — warm foundation for documentation and technical surfaces.

For the Fachbetrieb context: `fachbetrieb-primary` (#4daf46, Pure Green) replaces Deep Green as the identity color, and `fachbetrieb-secondary` (#494949, Stone Grey) provides the authoritative contrast. Lime Green does not appear.

## Typography

Three typefaces serve distinct communicative roles:

**Unbounded (weight 900, uppercase)** — Headlines and buttons only. Its extreme weight and geometric construction communicate mass and protection. Negative letter-spacing at display sizes creates visual density. Never used below 18px. Never at weights other than 900. Never in sentence case. This font makes the brand feel load-bearing.

**Inter (weights 400–700)** — Body text, labels, and UI elements. Chosen for its invisibility — it never competes with the message. The reader should focus on content, not letterforms.

**Geist Mono (weight 500)** — Technical specifications, measurements, prices, and product data. Its monospace grid communicates precision and measurability. Every value that could be verified with a measuring instrument is set in Geist Mono: layer thickness (2.5 mm), drying time (24 h), consumption rate (1.2 kg/m²), pH values, prices.

## Layout

The layout follows a fluid grid model with a strict 8px spacing scale. Content is contained within a maximum width of 1280px on desktop.

The page rhythm alternates between full-width dark bands (marketing/emotional) and contained light sections (technical/rational). Dark bands always span edge-to-edge. Light sections use the grid system with generous margins.

The transition between dark and light surfaces is always a **hard horizontal cut** — never a gradient, never a diagonal, never a wave. This is deliberate: the brand communicates through material contrast (moisture barrier vs. dry wall), and the hard cut is the visual metaphor for that barrier.

Spacing tokens scale from `xs` (4px) for micro-adjustments to `hero` (160px) for primary hero sections. The `section` token (80px) governs vertical rhythm between major content blocks.

## Elevation & Depth

Depth is achieved through the **shadow-as-border** technique rather than CSS borders. Every card and elevated surface uses a composite box-shadow that combines a 1px ring (simulating a border) with a soft spread shadow (simulating physical lift).

- **Ring only** — `rgba(0,0,0,0.08) 0px 0px 0px 1px`. Hairline definition without lift. Inactive containers.
- **Subtle** — Ring + 2px blur. Default card state.
- **Featured** — Ring + 8px blur + inset highlight. Hover state and promoted content.
- **Elevated** — Ring + 12px blur. Dropdowns and popovers.
- **Modal** — Ring + 24px blur. Modals and overlays.

Why shadows over borders: CSS borders add to element dimensions, create hard edges that feel flat, and cannot express physical depth. Shadows simulate the real-world behavior of elevated materials — consistent with a brand that deals in physical building materials.

## Shapes

The shape language uses a restrained radius scale. The default for most interactive elements is `sm` (4px) — just enough softness to feel modern while maintaining a rigid, engineered aesthetic that communicates precision.

- **Buttons:** `sm` (4px) for the industrial, precise feel of BKM AG. Never pill-shaped in the primary brand context.
- **Cards:** `lg` (12px) for content cards. Creates a contained, approachable surface without feeling overly rounded.
- **Inputs:** `md` (8px) for form fields. Neutral territory.
- **Badges:** `sm` (4px) for product and status badges.
- **Full radius** (`full`) is reserved only for avatar images and status indicators — never for buttons or cards in the BKM world.

## Components

### Buttons

Primary buttons use Lime Green (`secondary`) on dark surfaces — the single highest-contrast interactive signal. On light surfaces, buttons use Deep Green (`primary`) with white text. Only ONE primary button per viewport fold.

In the Fachbetrieb context, primary buttons use Pure Green (`fachbetrieb-primary`) instead of Lime. The button shape and typography remain identical.

All buttons use Unbounded at weight 900, uppercase, with slight letter-spacing. Height is fixed at 48px for consistent touch targets.

### Cards

Cards never use CSS borders. They use the shadow-as-border technique exclusively. Cards lift on hover (translateY -2px + shadow escalation from subtle to featured).

Dark cards (on light surfaces) use Deep Green background with white text and a Lime accent border-left (4px solid). In Fachbetrieb context, the accent is Pure Green instead.

### Navigation

The navigation bar uses Deep Green (`primary`) at 64px height. Links are white, transitioning to Lime on hover. The single CTA button in the navigation is Lime.

In Fachbetrieb context, the navigation uses Stone Grey (`fachbetrieb-secondary`) with white text, and links transition to Pure Green on hover.

### Technical Data (Spec Tables)

All measurable values are displayed in Geist Mono. Labels in Inter. Rows are separated by hairline dividers (`outline-variant`). This pattern is identical in both BKM AG and Fachbetrieb contexts.

### The Keyvisual

The Keyvisual is a fixed branded composition (layered arrow shapes derived from the logo signet). It must NEVER be recreated in code — no SVG patterns, no CSS shapes, no procedural generation. It is always placed as a pre-rendered image file, positioned on the right edge, cropped via overflow.

It appears on: title pages, hero bands (optional), print materials. It does NOT appear on: product cards, small components, Instagram posts, email templates, technical data sheets.

## Brand Assets

All brand assets live in the `assets/` directory. They are pre-rendered, color-correct files — never recreate them in code.

### Keyvisual Variants

The Keyvisual consists of three layered chevron shapes representing the drying process. Different background colors require different file variants:

| File | Colors | Use on background |
|------|--------|-------------------|
| `assets/keyvisual/keyvisual-on-light.svg` | Pure Green + Transition Green + Deep Green | White (#ffffff), Sand White (#f6f5f2) |
| `assets/keyvisual/keyvisual-on-dark.svg` | All White | Deep Green (#1c4b42), Transition Green (#287d4b), Stone Grey (#494949) |

**FORBIDDEN:** Never place the Keyvisual on Pure Green (#4daf46) or Lime Green (#b4e717) backgrounds — one chevron element would visually disappear due to identical color.

### Logo Variants

The BKM Mannesmann logo consists of the wordmark **BKM MANNESMANN** and a characteristic **second M-element** (two diagonal strokes on the right side). In the colored variants, this M-element is always **Pure Green (#4daf46)** — never Deep Green, Transition Green, or any other color.

| File | Wordmark + MANNESMANN | M-Element | Context | Use on background |
|------|----------------------|-----------|---------|-------------------|
| `assets/logos/bkm-logo-stonegrey-puregreen` | Stone Grey (#494949) | Pure Green (#4daf46) | **Fachbetrieb** | White, Sand White |
| `assets/logos/bkm-logo-white-puregreen` | White (#ffffff) | Pure Green (#4daf46) | **BKM AG** | Deep Green, Transition Green, Stone Grey |
| `assets/logos/bkm-logo-white` | White (#ffffff) | White (#ffffff) | **BKM AG** | Deep Green, Transition Green, Pure Green, Stone Grey |
| `assets/logos/bkm-logo-black` | Black (#000000) | Black (#000000) | **Reserve/Druck** | White, Sand White (selten verwenden) |

Each variant is available as `.svg` (vector) and `.png` (raster fallback).

**Context assignment:**
- Stone Grey + Pure Green M = **Fachbetrieb** on light backgrounds (primary logo for partner companies)
- White + Pure Green M = **BKM AG** on dark backgrounds (primary logo for manufacturer context)
- All White = **BKM AG** on colored backgrounds where Pure Green M would not be visible
- All Black = Reserve for single-color print only (avoid in digital media)

**Critical rule:** No logo variant exists with Deep Green or Transition Green coloring. The M-element is ALWAYS Pure Green in colored variants.

### SVG Export Rules

All SVGs must be exported from Adobe Illustrator with these settings:
- CSS-Eigenschaften: **Präsentationsattribute** (ensures `fill="#hex"` on each path)
- Responsiv: **Deaktiviert** (preserves width/height attributes)
- Text: In Pfade umwandeln (prevents font dependency)

If an SVG shows colors as CSS classes (`class="cls-1"`) instead of inline `fill` attributes, it was exported incorrectly and will render black in many contexts.

## Contrast Matrix

All color combinations used in this system have been validated against WCAG AA:

| Foreground | Background | Ratio | Status | Use |
|-----------|-----------|-------|--------|-----|
| White | Deep Green (#1c4b42) | 9.84 | PASS | Text + UI |
| White | Transition Green (#287d4b) | 5.09 | PASS | Text + UI |
| White | Stone Grey (#494949) | 9.00 | PASS | Text + UI |
| Lime (#b4e717) | Deep Green (#1c4b42) | 6.74 | PASS | Text + UI |
| Lime (#b4e717) | Stone Grey (#494949) | 6.17 | PASS | Text + UI |
| Lime (#b4e717) | Transition Green (#287d4b) | 3.49 | PASS | Large text only |
| Deep Green | White (#ffffff) | 9.84 | PASS | Text + UI |
| Deep Green | Sand White (#f6f5f2) | 9.02 | PASS | Text + UI |
| Transition Green | White (#ffffff) | 5.09 | PASS | Text + UI |
| Stone Grey | White (#ffffff) | 9.00 | PASS | Text + UI |
| Pure Green (#4daf46) | White (#ffffff) | 2.79 | FAIL | Decorative only |
| Lime (#b4e717) | White (#ffffff) | 1.46 | FAIL | Decorative only |

**Key rule:** Pure Green and Lime Green must NEVER be used as text on light backgrounds. They only work as text on dark backgrounds (Deep Green, Stone Grey).

## Do's and Don'ts

- Do use Lime Green (`secondary`) exclusively for interactive elements on dark surfaces
- Don't use Lime Green in the Fachbetrieb context — use Pure Green instead
- Do maintain hard horizontal cuts between dark and light surface bands
- Don't use gradients, waves, diagonals, or any soft transition between surfaces
- Do place the Keyvisual as a pre-rendered image asset (right edge, cropped)
- Don't recreate the Keyvisual in code (no SVG, no CSS clip-path, no procedural patterns)
- Do use Unbounded only at weight 900, only uppercase, only at 18px or larger
- Don't use pure black (#000000) — darkest value is Deep Green (#1c4b42) for surfaces
- Do use Geist Mono for all measurable values (prices, dimensions, percentages, specs)
- Don't use more than ONE primary button per viewport fold
- Do use shadow-as-border technique for all cards and elevated surfaces
- Don't use CSS `border` property on cards (shadows provide depth; borders flatten)
- Do keep the same design structure for Fachbetrieb pages — only swap the color context
- Don't create a visually separate "brand" for Fachbetriebe — it is the same system, different palette
- Do use `keyvisual-on-light.svg` on white/sand-white backgrounds and `keyvisual-on-dark.svg` on dark backgrounds
- Don't place the Keyvisual on Pure Green or Lime Green backgrounds (chevron disappears)
- Do use `bkm-logo-stonegrey-puregreen` (Stone Grey wordmark + Pure Green M-element) for Fachbetrieb on light backgrounds
- Do use `bkm-logo-white-puregreen` (White wordmark + Pure Green M-element) for BKM AG on dark backgrounds
- Do use `bkm-logo-white` (all white) for BKM AG on colored backgrounds (Pure Green, Deep Green)
- Don't use `bkm-logo-black` in digital media — it is reserved for single-color print
- Don't assume any logo variant has Deep Green or Transition Green coloring — only Pure Green exists as M-element color
- Don't use Pure Green (#4daf46) as text on light backgrounds — contrast is only 2.79 (FAIL)
