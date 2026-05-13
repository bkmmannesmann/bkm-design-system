# BKM Website — Skill

> Generiert brand-konforme Websites und Web-Applikationen im BKM Mannesmann Design System. Nutzt React + Tailwind CSS + shadcn/ui und die BKM Pattern Library.

## Wann diesen Skill verwenden

- Wenn Websites, Landing Pages oder Web-Apps im BKM-Stil erstellt werden sollen
- Wenn React-Komponenten mit BKM-Tokens gebaut werden sollen
- Wenn interaktive Patterns (Spotlight Card, Compare, Carousel) eingesetzt werden sollen

## Workflow

### 1. Kontext bestimmen

| Kontext | Wann | Primärfarbe | Akzent |
|---------|------|-------------|--------|
| **BKM AG** | Corporate, Shop, Marketing | Deep Green (#1c4b42) | Lime (#b4e717) |
| **Fachbetrieb** | Fachbetrieb-Seiten, Partner | Stone Grey (#494949) | Pure Green (#4daf46) |

### 2. Design System laden

Lies `../../DESIGN.md` für die vollständige Token-Referenz:

- Farben, Typografie, Spacing, Schatten
- Do's & Don'ts
- Kontrastmatrix
- Logo-Verwendungsregeln

### 3. AGENTS.md konsultieren

Lies `../../AGENTS.md` für die KI-spezifischen Regeln:

- Farbkontext-Entscheidungsbaum
- Typografie-Hierarchie
- Komponentenregeln
- Sektions-Aufbau

### 4. Pattern Library nutzen

Lies `../../patterns/README.md` für verfügbare Patterns. Alle Patterns sind React + Tailwind-kompatibel:

**Backgrounds:**
- Aurora Gradient (BKM AG only)
- Wavy Background (beide Kontexte)
- Noise Texture (beide Kontexte)

**Cards:**
- Spotlight Card (Cursor-Tracking Glow)
- 3D Card Effect (Perspektive)
- Focus Cards (Fokus-Galerie)

**Text:**
- Text Hover Effect (SVG-Masken)
- Text Animate (Buchstaben-Animation)
- Colourful Text (Gradient, BKM AG only)

**Interactive:**
- Compare (Vorher/Nachher Slider)
- Apple Cards Carousel (Referenzen)
- Animated Testimonials (Kundenstimmen)

### 5. Tailwind-Konfiguration

Die BKM-Tokens müssen in die Tailwind-Konfiguration eingetragen werden:

```css
/* client/src/index.css — BKM Theme Layer */
@layer base {
  :root {
    /* BKM AG Kontext */
    --bkm-deep-green: #1c4b42;
    --bkm-deep-green-light: #2a6b5e;
    --bkm-transition-green: #287d4b;
    --bkm-pure-green: #4daf46;
    --bkm-lime: #b4e717;
    --bkm-sand-white: #f6f5f2;
    --bkm-stone-grey: #494949;
    --bkm-charcoal: #1a1a1a;

    /* Surfaces */
    --bkm-surface: #ffffff;
    --bkm-surface-warm: #f6f5f2;
    --bkm-outline: #c8c5be;
    --bkm-outline-variant: #e8e6e1;

    /* Shadows (no CSS border!) */
    --bkm-shadow-subtle: rgba(0,0,0,0.08) 0px 0px 0px 1px, rgba(0,0,0,0.04) 0px 2px 4px;
    --bkm-shadow-featured: rgba(0,0,0,0.08) 0px 0px 0px 1px, rgba(0,0,0,0.06) 0px 8px 16px -4px;
    --bkm-shadow-elevated: rgba(0,0,0,0.08) 0px 0px 0px 1px, rgba(0,0,0,0.08) 0px 12px 24px -8px;
  }
}
```

### 6. Font-Einbindung

```html
<!-- client/index.html -->
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Unbounded:wght@900&display=swap" rel="stylesheet" />
```

## Kritische Regeln

1. **Keyvisual ist ein vorgerendertes Bild** — Nie in Code nachbauen.
2. **Lime Green nur im BKM AG Kontext** — Nie im Fachbetrieb.
3. **Unbounded: weight 900, uppercase, min. 18px** — Keine Ausnahmen.
4. **Harte Schnitte zwischen Flächen** — Keine Gradients als Übergang.
5. **Shadow-as-Border** — Keine CSS `border` auf Cards.
6. **Max. 1 Primary Button pro Viewport.**
7. **Technische Werte in TT Norms Pro.**
8. **Pure Green nie als Text auf hellem Hintergrund** (Kontrast 2.79).

## Sektions-Aufbau

Jede Sektion folgt dem Schema:

```
┌─────────────────────────────────────────────┐
│  max-width: 1280px, mx-auto, px-8 md:px-16 │
│                                             │
│  [Label] TT Norms Pro 700 uppercase 13px           │
│  [Headline] Unbounded 900 UPPERCASE         │
│  [Body] TT Norms Pro 400 16–20px                   │
│  [Content: Cards, Grid, etc.]               │
│                                             │
└─────────────────────────────────────────────┘
```

## Abhängigkeiten

```bash
# Basis
pnpm add framer-motion

# Aceternity UI Patterns (nach Bedarf)
npx shadcn@latest add @aceternity/<component>

# Componentry Patterns (nach Bedarf)
npx shadcn@latest add @componentry/<component>
```
