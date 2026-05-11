version: 1.0
name: BKM Mannesmann
description: BKM Mannesmann carries a strong, protective, and competent visual identity. The design system is built on a foundation of deep greens and stark whites, accented by a vibrant Lime Green for solutions and CTAs. The signature Keyvisual (Chevron pattern) represents the transition from problem (Deep Green) to solution (Lime Green). The system uses Unbounded Black for bold, geometric headlines and TT Norms Pro for clean, readable body text. Coverage spans across Home Line (emotional, warm) and Pro Line (technical, competent) products, including print brochures, technical data sheets, and digital web applications.

colors:
  primary: "#4daf46" # Pure Green
  primary-deep: "#1c4b42" # Deep Green
  primary-transition: "#287d4b" # Transition Green
  accent-lime: "#b4e717" # Lime Green
  on-primary: "#ffffff" # Clean White
  on-accent: "#1c4b42" # Deep Green
  canvas: "#f6f5f2" # Sand White
  canvas-dark: "#1c4b42" # Deep Green
  surface: "#ffffff" # Clean White
  ink: "#494949" # Stone Grey
  ink-dark: "#000000" # True Black
  on-dark: "#ffffff" # Clean White

typography:
  hero-display:
    fontFamily: Unbounded
    fontSize: 48px
    fontWeight: 900
    lineHeight: 1.25
    textTransform: uppercase
  heading-1:
    fontFamily: Unbounded
    fontSize: 36px
    fontWeight: 900
    lineHeight: 1.25
    textTransform: uppercase
  heading-2:
    fontFamily: Unbounded
    fontSize: 22.5px
    fontWeight: 900
    lineHeight: 1.25
    textTransform: uppercase
  heading-3:
    fontFamily: Unbounded
    fontSize: 18px
    fontWeight: 900
    lineHeight: 1.25
    textTransform: uppercase
  subtitle:
    fontFamily: TT Norms Pro
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.25
  body-md:
    fontFamily: TT Norms Pro
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.25
  body-md-bold:
    fontFamily: TT Norms Pro
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
  body-sm:
    fontFamily: TT Norms Pro
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.25
  caption:
    fontFamily: Unbounded
    fontSize: 12px
    fontWeight: 900
    lineHeight: 1.25
    textTransform: uppercase

rounded:
  none: 0px
  sm: 4px
  md: 8px
  lg: 12px
  full: 9999px

spacing:
  xs: 8px
  sm: 16px
  md: 24px
  lg: 32px
  xl: 48px
  xxl: 64px
  hero: 120px

components:
  button-primary:
    backgroundColor: "{colors.accent-lime}"
    textColor: "{colors.on-accent}"
    typography: "{typography.body-md-bold}"
    textTransform: uppercase
    fontFamily: Unbounded
    fontWeight: 900
    rounded: "{rounded.none}"
    padding: "12px 24px"
  button-primary-hover:
    backgroundColor: "{colors.primary-deep}"
    textColor: "{colors.accent-lime}"
  button-secondary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-md-bold}"
    textTransform: uppercase
    fontFamily: Unbounded
    fontWeight: 900
    rounded: "{rounded.none}"
    padding: "12px 24px"
  button-secondary-hover:
    backgroundColor: "{colors.primary-transition}"
    textColor: "{colors.on-primary}"
  card-base:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    boxShadow: "0 4px 6px rgba(0,0,0,0.1)"
  info-box:
    backgroundColor: "{colors.primary-deep}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg}"
    borderLeft: "4px solid {colors.accent-lime}"
  hero-band:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    padding: "{spacing.hero} {spacing.xl}"
  footer-band:
    backgroundColor: "{colors.primary-deep}"
    textColor: "{colors.on-dark}"
    padding: "{spacing.xxl} {spacing.xl}"

## 1. Visual Theme & Atmosphere

BKM Mannesmann's visual identity is rooted in protection, competence, and reliability. The design system contrasts deep, solid greens (`#1c4b42`) with bright, energetic Lime Green (`#b4e717`) to symbolize the transition from a problem (moisture, damage) to a solution (protection, value retention). The canvas is typically Sand White (`#f6f5f2`) or Clean White (`#ffffff`), providing a clean, professional backdrop.

The typography is highly distinctive. **Unbounded Black** is used exclusively for headlines and is always set in uppercase. Its geometric, modern forms convey strength and structure. For body text, **TT Norms Pro** provides neutral, highly legible reading experiences. A strict 125% line-height rule applies across almost all typography, ensuring a consistent vertical rhythm.

A core element of the visual identity is the **Keyvisual**—a chevron pattern derived from the BKM logo. It is always placed on the right edge, bleeding off the page, and uses a specific color semantic (Deep Green at the bottom, transitioning to Pure Green at the top) to represent building up protection.

## 2. Color Palette & Roles

### Primary Colors
- **Pure Green** (`#4daf46`): The core brand color, used for primary logos on light backgrounds and secondary accents.
- **Transition Green** (`#287d4b`): Used in gradients and hover states.
- **Deep Green** (`#1c4b42`): Represents the "problem" or foundation. Used for info-boxes, footers, chapter dividers, and text on light backgrounds.
- **Lime Green** (`#b4e717`): Represents the "solution". Used strictly for high-priority CTAs, highlights, and icons on dark backgrounds.

### Neutral Colors
- **Sand White** (`#f6f5f2`): The standard warm background for print and web.
- **Stone Grey** (`#494949`): The primary color for body text and standard logos.
- **Clean White** (`#ffffff`): Used for text on dark backgrounds and clean surfaces.
- **True Black** (`#000000`): Used sparingly for maximum contrast.

## 3. Typography Rules

- **Headlines (H1-H3)**: Always `Unbounded Black` (weight 900), always uppercase.
- **Body Text**: `TT Norms Pro Regular` (weight 400).
- **Emphasis**: `TT Norms Pro Bold` (weight 700) for highlighting words in body text.
- **Line Height**: Strictly 125% (1.25) of the font size across all text elements.
- **Alignment**: Body text is typically justified with hyphenation in print, left-aligned in digital.

## 4. Component Stylings

### Buttons (CTAs)
- **Primary**: Deep Green background with Lime Green text. On hover, colors invert (Lime Green background, Deep Green text). Font is Unbounded Black, uppercase.
- **Secondary**: Pure Green background with White text. Hover state is Transition Green.

### Info-Boxes
- Used for Pro-Tips and safety instructions.
- Background: Deep Green.
- Text: Clean White.
- Accents/Highlights: Lime Green.

### Keyvisual (Chevrons)
- Always positioned on the right edge, bleeding off the canvas.
- Width is exactly 1/5 of the total page/container width.
- Color transitions from Pure Green (top) to Deep Green (bottom).

## 5. Layout Principles

- **Print**: 3-column grid system.
- **Web**: 12-column responsive grid.
- **Logo Placement**: Top left. Distance from top and left edges equals 1x the cap height of the "BKM" text in the logo.
- **Whitespace**: Used actively as a design element to convey clarity and premium quality.

## 6. Imagery

- **Style**: Authentic, professional, natural light. No staged stock photos.
- **Format**: 16:9 ratio is mandatory for hero and title images.
- **Content**: Divided into Home Line (emotional, warm, DIY) and Pro Line (technical, competent, professional).

## 7. MicroPorex (Ingredient Brand)
- Used as a seal of quality ("Powered by BKM Mannesmann").
- Lime Green on dark backgrounds, Black on light backgrounds.
