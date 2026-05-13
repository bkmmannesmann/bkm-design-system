# BKM Component Pattern Library

> Kuratierte Frontend-Patterns aus Open-Source-Bibliotheken, angepasst auf die BKM-Farbwelt. Diese Patterns **lesen** aus dem Design System (DESIGN.md) — sie verändern es nicht.

## Architektur

```
DESIGN.md (Source of Truth)
    ↓ liest Tokens
patterns/ (diese Bibliothek)
    ↓ liefert Bausteine an
skills/ (Generierungs-Workflows)
```

Jedes Pattern referenziert die BKM-Tokens aus DESIGN.md und zeigt, wie ein Open-Source-Effekt brand-konform eingesetzt wird. Die Originalkomponenten stammen aus:

- **Aceternity UI** — 200+ React-Komponenten, shadcn-kompatibel, Framer Motion
- **Componentry** — 40+ Effekte, WebGL, Partikel, Cursor-Tracking

## Kontext-Regel

Jedes Pattern ist für einen oder beide Farbkontexte freigegeben:

| Kontext | Primärfarbe | Akzent | Hintergrund |
|---------|-------------|--------|-------------|
| **BKM AG** | Deep Green (#1c4b42) | Lime (#b4e717) | Weiß / Sand White |
| **Fachbetrieb** | Stone Grey (#494949) | Pure Green (#4daf46) | Weiß / Sand White |

Lime Green erscheint **nie** im Fachbetrieb-Kontext. Pure Green erscheint **nie** als Text auf hellem Hintergrund (Kontrast 2.79 — FAIL).

## Pattern-Katalog

### Backgrounds

| Pattern | Quelle | BKM-Einsatz | Kontext |
|---------|--------|-------------|---------|
| [Aurora Gradient](backgrounds/aurora-gradient.md) | Aceternity UI | Hero-Sektionen mit Deep Green → Lime Farbverlauf | BKM AG |
| [Wavy Background](backgrounds/wavy-background.md) | Aceternity UI | Sektions-Hintergründe mit animierten Wellen | Beide |
| [Noise Texture](backgrounds/noise-texture.md) | Componentry | Subtile Textur auf Sand White Flächen | Beide |

### Cards

| Pattern | Quelle | BKM-Einsatz | Kontext |
|---------|--------|-------------|---------|
| [Spotlight Card](cards/spotlight-card.md) | Componentry | Produkt-Showcases mit Cursor-Tracking Glow | Beide |
| [3D Card Effect](cards/3d-card.md) | Aceternity UI | Feature-Präsentationen mit Tiefenwirkung | Beide |
| [Focus Cards](cards/focus-cards.md) | Aceternity UI | Bild-Galerien mit Fokus-Effekt | Beide |

### Text & Typography

| Pattern | Quelle | BKM-Einsatz | Kontext |
|---------|--------|-------------|---------|
| [Text Hover Effect](text/text-hover.md) | Aceternity UI | Headlines mit SVG-Masken-Effekt | Beide |
| [Text Animate](text/text-animate.md) | Componentry | Einblende-Animationen für Überschriften | Beide |
| [Colourful Text](text/colourful-text.md) | Aceternity UI | Farbverlauf-Text für Akzent-Headlines | BKM AG |

### Interactive

| Pattern | Quelle | BKM-Einsatz | Kontext |
|---------|--------|-------------|---------|
| [Compare](interactive/compare.md) | Aceternity UI | Vorher/Nachher bei Bauchemie-Anwendungen | Beide |
| [Apple Cards Carousel](interactive/carousel.md) | Aceternity UI | Referenz-Projekte, Testimonials | Beide |
| [Animated Testimonials](interactive/testimonials.md) | Aceternity UI | Kundenstimmen mit Übergangsanimation | Beide |

## Installation

Alle Patterns sind shadcn-kompatibel und können per CLI installiert werden:

```bash
# Aceternity UI Komponenten
npx shadcn@latest add @aceternity/<component-name>

# Componentry Komponenten
npx shadcn@latest add @componentry/<component-name>
```

Alternativ: Code manuell kopieren (siehe jeweilige Pattern-Datei).

## BKM-Anpassungsregel

Nach der Installation jeder Komponente müssen folgende Werte ersetzt werden:

| Original (Bibliothek) | BKM AG Kontext | Fachbetrieb Kontext |
|----------------------|----------------|---------------------|
| Primärfarbe (meist Blau/Lila) | `#1c4b42` (Deep Green) | `#494949` (Stone Grey) |
| Akzentfarbe | `#b4e717` (Lime) | `#4daf46` (Pure Green) |
| Hintergrund dunkel | `#1c4b42` (Deep Green) | `#494949` (Stone Grey) |
| Hintergrund hell | `#f6f5f2` (Sand White) | `#f6f5f2` (Sand White) |
| Body-Font | `TT Norms Pro` | `TT Norms Pro` |
| Headline-Font | `Unbounded` (900, uppercase) | `Unbounded` (900, uppercase) |
| Border-Radius Buttons | `4px` | `4px` |
| Border-Radius Cards | `12px` | `12px` |
