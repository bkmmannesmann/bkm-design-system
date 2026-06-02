---
version: alpha
name: BKM Mannesmann AG
description: >
  Building protection manufacturer (est. 1928). Visual identity communicates
  protective authority through material contrast. One unified brand world with
  two color contexts: the BKM AG context (Deep Green, Lime, White) and the
  Fachbetrieb context (White, Sand White, Pure Green, Transition Green,
  with Stone Grey as text color only). The green tones tell
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
  # === H1 — Unbounded 900 UPPERCASE (only H1 uses uppercase) ===
  headline-display:
    fontFamily: Unbounded
    fontSize: 72px
    fontWeight: 900
    lineHeight: 1.0
    letterSpacing: -0.04em
    textTransform: uppercase
  headline-lg:
    fontFamily: Unbounded
    fontSize: 56px
    fontWeight: 900
    lineHeight: 1.05
    letterSpacing: -0.03em
    textTransform: uppercase
  # === H2–H6 — Unbounded 900, sentence case (NO uppercase) ===
  headline-md:
    fontFamily: Unbounded
    fontSize: 44px
    fontWeight: 900
    lineHeight: 1.08
    letterSpacing: -0.02em
    textTransform: none
  headline-sm:
    fontFamily: Unbounded
    fontSize: 36px
    fontWeight: 900
    lineHeight: 1.15
    letterSpacing: -0.02em
    textTransform: none
  title-lg:
    fontFamily: Unbounded
    fontSize: 28px
    fontWeight: 900
    lineHeight: 1.2
    letterSpacing: -0.01em
    textTransform: none
  title-md:
    fontFamily: Unbounded
    fontSize: 22px
    fontWeight: 900
    lineHeight: 1.25
    textTransform: none
  title-sm:
    fontFamily: Unbounded
    fontSize: 18px
    fontWeight: 900
    lineHeight: 1.3
    textTransform: none
  # === Body — TT Norms Pro Regular (400) ===
  body-lg:
    fontFamily: TT Norms Pro
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.7
  body-md:
    fontFamily: TT Norms Pro
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
  body-sm:
    fontFamily: TT Norms Pro
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
  # === Body Bold — TT Norms Pro Bold (700) for emphasis ===
  body-lg-bold:
    fontFamily: TT Norms Pro
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.7
  body-md-bold:
    fontFamily: TT Norms Pro
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.6
  # === Labels — TT Norms Pro Bold (700) ===
  label-lg:
    fontFamily: TT Norms Pro
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: 0.02em
  label-md:
    fontFamily: TT Norms Pro
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.0
  label-sm:
    fontFamily: TT Norms Pro
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: 0.05em
  # === Technical Values — TT Norms Pro Regular (400) ===
  code-md:
    fontFamily: TT Norms Pro
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
  code-sm:
    fontFamily: TT Norms Pro
    fontSize: 12px
    fontWeight: 400
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
    backgroundColor: "{colors.fachbetrieb-primary-deep}"
    textColor: "{colors.on-fachbetrieb-primary}"
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
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface}"
    padding: "{spacing.hero}"
    # NOTE: Fachbetrieb hero is light (White/Sand White), not dark.
    # Use Transition Green accent bands sparingly, never Stone Grey as surface.
---

## Overview

BKM Mannesmann AG is a building protection manufacturer established in 1928. The visual identity communicates one thing above all: **Schutz** (protection). Every design decision traces back to this core promise.

### One Brand, Two Color Contexts

The BKM world is unified — there are no separate "sub-brands" with different design languages. However, two color contexts exist within the same design system:

**BKM AG Context** — The primary brand world. Used for the corporate website, product pages, the online shop, marketing materials, and all content where BKM Mannesmann AG speaks as the manufacturer. Colors: Deep Green, Lime Green, White, Sand White.

**Fachbetrieb Context** — Used for landingpages, portals, and materials where certified specialist companies (Fachbetriebe) are the subject. These are independent craftsmen certified by BKM to apply Pro Line products at the customer's site. The design structure is identical, but the color palette shifts to lighter, more approachable tones: **White and Sand White dominate as surface colors**, Pure Green and Transition Green provide the identity accents, and Stone Grey serves as the primary text color. Unlike the BKM AG context (where Deep Green dominates as a heavy, dark surface), the Fachbetrieb context is deliberately light and open — Stone Grey is NEVER used as a dominant background surface because it makes designs feel heavy and oppressive. This lighter approach communicates approachability and solution-orientation: the Fachbetrieb delivers the dry, protected end state.

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

For the Fachbetrieb context: `fachbetrieb-primary` (#4daf46, Pure Green) is the identity and accent color. `fachbetrieb-primary-deep` (#287d4b, Transition Green) is used for headlines on light backgrounds, links, and header bands. `fachbetrieb-secondary` (#494949, Stone Grey) is the primary text color — it replaces Deep Green's role as text, NOT as surface. **Critical: Stone Grey must never be used as a dominant background surface in the Fachbetrieb context.** The dominant surfaces are White (#ffffff) and Sand White (#f6f5f2). If a dark accent band is needed, use Transition Green (#287d4b) sparingly — not Stone Grey. Lime Green does not appear.

## Typography

Two typefaces serve distinct communicative roles:

**Unbounded (weight 900)** — Headlines and buttons. Its extreme weight and geometric construction communicate mass and protection. Negative letter-spacing at display sizes creates visual density. Never used below 18px. Never at weights other than 900. **H1 headlines use uppercase. H2 and below use sentence case** — this creates a clear visual hierarchy where the primary headline dominates while sub-headlines feel more approachable. This font makes the brand feel load-bearing.

**TT Norms Pro (weights 400 + 700)** — Everything else. Body text, labels, UI elements, technical specifications, measurements, prices, and product data. TT Norms Pro is a proprietary font (not a Google Font) and must be self-hosted from `assets/fonts/`. Two weights are available: **Regular (400)** for body text, descriptions, and technical values; **Bold (700)** for emphasized information, important labels, and highlighted content. Its clean geometric construction provides excellent readability while maintaining a professional, engineered aesthetic.

**Font files:**
- `assets/fonts/TT_Norms_Pro_Compact_Regular.woff2` — Regular (400)
- `assets/fonts/TT_Norms_Pro_Bold.woff2` — Bold (700)

## Layout

The layout follows a fluid grid model with a strict 8px spacing scale. Content is contained within a maximum width of 1280px on desktop.

The page rhythm alternates between full-width dark bands (marketing/emotional) and contained light sections (technical/rational). Dark bands always span edge-to-edge. Light sections use the grid system with generous margins.

The transition between dark and light surfaces is always a **hard horizontal cut** — never a gradient, never a diagonal, never a wave. This is deliberate: the brand communicates through material contrast (moisture barrier vs. dry wall), and the hard cut is the visual metaphor for that barrier.

Spacing tokens scale from `xs` (4px) for micro-adjustments to `hero` (160px) for primary hero sections. The `section` token (80px) governs vertical rhythm between major content blocks.

## Elevation & Depth

Depth is achieved through two complementary techniques depending on context:

### Shadow-as-Border (Website/Digital UI)

For digital interfaces, cards and elevated surfaces use a composite box-shadow that combines a 1px ring (simulating a border) with a soft spread shadow (simulating physical lift).

- **Ring only** — `rgba(0,0,0,0.08) 0px 0px 0px 1px`. Hairline definition without lift. Inactive containers.
- **Subtle** — Ring + 2px blur. Default card state.
- **Featured** — Ring + 8px blur + inset highlight. Hover state and promoted content.
- **Elevated** — Ring + 12px blur. Dropdowns and popovers.
- **Modal** — Ring + 24px blur. Modals and overlays.

### Colored Border-Left (Slides/Print/Editorial)

For presentations, brochures, and editorial layouts, cards use a **4px solid left border** in a semantic color instead of shadow. This is the primary card differentiation technique in the real BKM corporate design (observed in all official PDFs and brochures).

- **Deep Green border-left** — Standard content card on Sand/White backgrounds.
- **Red border-left** — Warning or problem-state cards.
- **Lime border-left** — Highlight or success-state cards (BKM AG context only).
- **Pure Green border-left** — Fachbetrieb context cards.

Cards in editorial context have minimal rounded corners (8px), white background on Sand surfaces, and NO box-shadow. The colored border-left provides all necessary visual differentiation.

### Glasmorphismus (Both Contexts)

Glasmorphismus (frosted glass effect) is available as an optional technique for both BKM AG and Fachbetrieb contexts. It works particularly well for overlays on photo backgrounds, floating UI panels, and cards that need to feel lightweight against complex backgrounds.

```css
.glass {
  background: rgba(255, 255, 255, 0.12);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border: 1px solid rgba(255, 255, 255, 0.15);
  border-radius: 12px;
}
```

Use sparingly — maximum 1–2 glass elements per viewport. Never use glass on elements that contain critical text at small sizes (readability concern).

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

All buttons use Unbounded at weight 900, uppercase, with slight letter-spacing. Height is fixed at 48px for consistent touch targets. Button text is always uppercase regardless of heading level.

### Cards

**Website/Digital context:** Cards use the shadow-as-border technique. Cards lift on hover (translateY -2px + shadow escalation from subtle to featured). Dark cards (on light surfaces) use Deep Green background with white text and a Lime accent border-left (4px solid). In Fachbetrieb context, the accent is Pure Green instead.

**Slide/Print/Editorial context:** Cards use a **4px solid colored left border** as the primary visual differentiator — NO shadow, NO hover effects. White card on Sand/Beige background. Minimal rounded corners (8px). Icon + Title (TT Norms Pro Bold) + Body (TT Norms Pro Regular). The border color carries semantic meaning: Deep Green = standard, Red = warning/problem, Lime = highlight (BKM AG), Pure Green = highlight (Fachbetrieb).

### Navigation

The navigation bar uses Deep Green (`primary`) at 64px height. Links are white, transitioning to Lime on hover. The single CTA button in the navigation is Lime.

In Fachbetrieb context, the navigation uses Transition Green (`fachbetrieb-primary-deep`, #287d4b) with white text, and links transition to Pure Green on hover. Stone Grey may be used as a secondary navigation option (e.g., footer) but never as the primary navigation bar color — it makes the design feel too heavy.

### Technical Data (Spec Tables)

All measurable values are displayed in TT Norms Pro Regular. Labels in TT Norms Pro Bold. Rows are separated by hairline dividers (`outline-variant`). This pattern is identical in both BKM AG and Fachbetrieb contexts.

### The Keyvisual

The Keyvisual is a fixed branded composition (layered arrow shapes derived from the logo signet). It must NEVER be recreated in code — no SVG patterns, no CSS shapes, no procedural generation. It is always placed as a pre-rendered image file, with its **right edge flush against the right edge of the slide**, **vertically centered** and **fully visible (not cropped)**, at a restrained size (height ≈ 52% of the slide, opacity ≈ 0.85). It must not touch the top or bottom edge.

It appears on: title pages, hero bands (optional), print materials. It does NOT appear on: product cards, small components, Instagram posts, email templates, technical data sheets.

## Brand Assets

All brand assets live in the `assets/` directory. They are pre-rendered, color-correct files — never recreate them in code.

### Keyvisual Variants

The Keyvisual consists of three layered chevron shapes representing the drying process. Different background colors require different file variants:

| File | Colors | Use on background |
|------|--------|-------------------|
| `assets/keyvisual/keyvisual-on-light.svg` | Pure Green + Transition Green + Deep Green | White (#ffffff), Sand White (#f6f5f2) |
| `assets/keyvisual/keyvisual-on-dark.svg` | All White | Deep Green (#1c4b42), Transition Green (#287d4b), Stone Grey (#494949) |

Compact pre-rendered PNGs (`keyvisual-on-dark.png` / `keyvisual-on-light.png`, ~50 KB, transparent) are available for embedded decks; the `.svg` files remain the full-vector source.

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
- Do use Unbounded only at weight 900, only at 18px or larger. H1 in uppercase, H2+ in sentence case
- Don't use pure black (#000000) — darkest value is Deep Green (#1c4b42) for surfaces
- Do use TT Norms Pro Regular for all measurable values (prices, dimensions, percentages, specs)
- Do use TT Norms Pro Bold for emphasized information and important labels
- Don't use more than ONE primary button per viewport fold
- Do use shadow-as-border technique for cards in digital/website context
- Do use colored border-left (4px solid) for cards in slide/print/editorial context
- Don't use CSS `border` property on website cards (shadows provide depth; borders flatten)
- Don't use box-shadow on editorial/slide cards (colored border-left provides differentiation)
- Do keep the same design structure for Fachbetrieb pages — only swap the color context
- Don't create a visually separate "brand" for Fachbetriebe — it is the same system, different palette
- Do use White/Sand White as the dominant surface in Fachbetrieb context — it must feel light and open
- Don't use Stone Grey (#494949) as a dominant background surface in Fachbetrieb — it makes designs heavy and oppressive
- Do use Transition Green (#287d4b) for header bands and accent surfaces in Fachbetrieb when a dark element is needed
- Do use Stone Grey only as text color and for small structural elements (footer, dividers) in Fachbetrieb
- Do use `keyvisual-on-light.svg` on white/sand-white backgrounds and `keyvisual-on-dark.svg` on dark backgrounds
- Don't place the Keyvisual on Pure Green or Lime Green backgrounds (chevron disappears)
- Do use `bkm-logo-stonegrey-puregreen` (Stone Grey wordmark + Pure Green M-element) for Fachbetrieb on light backgrounds
- Do use `bkm-logo-white-puregreen` (White wordmark + Pure Green M-element) for BKM AG on dark backgrounds
- Do use `bkm-logo-white` (all white) for BKM AG on colored backgrounds (Pure Green, Deep Green)
- Don't use `bkm-logo-black` in digital media — it is reserved for single-color print
- Don't assume any logo variant has Deep Green or Transition Green coloring — only Pure Green exists as M-element color
- Don't use Pure Green (#4daf46) as text on light backgrounds — contrast is only 2.79 (FAIL)
- Don't use noise textures on slides — real BKM slides use clean, flat surfaces
- Don't use aurora gradients on slides — they are web-only decorative effects
- Do use Glasmorphismus sparingly for overlays on photo backgrounds (both contexts)
- Don't use bento grids, floating badges, or spotlight effects on slides — these are web UI patterns
- Do use a vertical Lime accent line (4px wide, ~60% height) on BKM AG title slides
- Do use a Deep Green full-width footer bar on editorial/slide content pages
- Do ensure at least 40% of slide surface is photography or visual content
- Do maintain at least 25% whitespace on every slide

## Editorial & Print Design (Slides / Brochures)

This section documents the design language observed in official BKM Mannesmann print materials, PDFs, and presentations. It differs significantly from the website/digital design language and must be followed when creating slides, brochures, pitch decks, or any print-adjacent output.

### Core Principle: Corporate Editorial, Not Web Design

BKM slides and brochures follow a **corporate editorial** aesthetic — closer to a premium magazine or annual report than to a SaaS landing page. The key differences from web design:

- **Clean, flat surfaces** — no noise textures, no animated gradients, no aurora effects
- **Photography-dominant** — large, emotional photos occupy 40–60% of the page
- **Generous whitespace** — at least 25% of the surface remains empty
- **Asymmetric, editorial layouts** — not symmetric dashboard grids
- **Minimal decoration** — no floating badges, no bento grids, no spotlight effects
- **Glasmorphismus** is permitted as an optional overlay technique on photo backgrounds

### The Two Background Types (Slides Only)

Every slide uses exactly ONE of these two background types:

| Type | Color | Use for | Text color |
|------|-------|---------|------------|
| **Dark** | Deep Green (#1c4b42) | Title slides, CTA slides, quote slides | White |
| **Light** | Sand/Beige (#f5f0eb – #f6f5f2) | Content slides, data slides | Deep Green or Black |

There is no third option. No Stone Grey backgrounds. No Transition Green full-surface backgrounds (except sparingly in Fachbetrieb context, max 1–2 per deck). No white-on-white.

### Title Slide Anatomy (BKM AG)

```
┌────────────────────────────────────────────────┐
│  [Logo white]                              │
│                                                │
│  │ (Lime vertical line, 4px, ~60% height)     │
│  │                                              │
│  │  HEADLINE                                    │
│  │  Unbounded Bold Italic, White, 72–100px      │
│  │                                              │
│  │  Subtitle                                    │
│  │  TT Norms Pro Regular Italic, White 70%      │
│  │                                              │
│     Meta: Lime icons + Lime text (author, date) │
│                                                │
└────────────────────────────────────────────────┘
Background: Deep Green (#1c4b42), completely flat
```

The **vertical Lime accent line** is a signature element of BKM AG title pages. It runs along the left side of the content area, 4px wide, approximately 60% of the slide height. It visually anchors the headline block.

### Content Slide Anatomy

```
┌────────────────────────────────────────────────┐
│                                                │
│  Headline: Unbounded Bold, Pure Green, 48px    │
│                                                │
│  ┌───────────────┐  ┌───────────────┐  │
│  │█ Card 1       │  │█ Card 2       │  │
│  │  Title (Bold) │  │  Title (Bold) │  │
│  │  Body (Reg.)  │  │  Body (Reg.)  │  │
│  └───────────────┘  └───────────────┘  │
│  (█ = 4px colored left border)                 │
│                                                │
│────────────────────────────────────────────────│
│  [Deep Green Footer Bar: Icon + Text, White]    │
└────────────────────────────────────────────────┘
Background: Sand/Beige (#f5f0eb)
```

### Content Slide Components

**Deep Green Footer Bar:** A full-width bar at the bottom of content slides. Deep Green background, 48–60px height, containing a Lime icon and white text (e.g., a key takeaway or navigation hint). This is a signature element of BKM editorial design.

**Cards with Colored Border-Left:** White cards on Sand background. 4px solid left border in Deep Green (standard), Red (warning), or Lime/Pure Green (highlight). No shadow. Minimal border-radius (8px). Content structure: Icon (optional) + Title (TT Norms Pro Bold) + Body (TT Norms Pro Regular).

**Accent Numbers:** Large numbers (Unbounded Bold, 48–96px) in Pure Green or Lime on light backgrounds. Used for statistics, KPIs, and proof points.

**Lime Checkmarks and Arrows:** Lime-colored checkmarks (✓) and directional arrows as visual indicators. Always paired with TT Norms Pro Bold titles in Deep Green.

### Photography Rules (Editorial)

Photography is the PRIMARY visual element in BKM editorial design — not text, not icons, not decorative patterns.

- At least 40% of slide/page surface should be photography or visual content
- Use real, emotional photos: people, buildings, construction sites, before/after
- Photos break out of the grid — they can bleed to edges, overlap with the Keyvisual
- The Keyvisual chevrons overlap photos at the right edge (signature BKM composition)
- Never use generic stock photos — prefer BKM-specific imagery or well-designed placeholders

### What Does NOT Belong in BKM Editorial Design

The following patterns are **web UI design** and must NOT appear in slides, brochures, or print materials:

- Noise textures (SVG fractal noise overlays)
- Aurora gradients (animated multi-color gradients)
- Bento grids (equal-sized tile layouts)
- Floating badges (positioned absolutely over content)
- Spotlight/glow effects
- Animated text effects
- Dashboard-style symmetric grids
- Multiple card shadows competing for attention

These patterns remain valid for the **website/digital context** (see `skills/bkm-website/`) but are explicitly forbidden in editorial output.
