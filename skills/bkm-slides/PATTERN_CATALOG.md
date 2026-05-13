# BKM Slides — Pattern-Katalog

> Übersicht welche Patterns aus der `patterns/` Bibliothek in Slides adaptiert werden können. Da Slides einzelne HTML-Dateien ohne React/Framer Motion sind, werden die Patterns als **statische CSS-Versionen** implementiert.

## Adaptierbare Patterns

| Pattern | Original-Tech | Slide-Adaption | Aufwand |
|---------|--------------|----------------|---------|
| **Noise Texture** | CSS (SVG Filter) | Direkt nutzbar (bereits im Template) | Keiner |
| **Aurora Gradient** | Framer Motion | CSS `@keyframes` Gradient-Animation | Niedrig |
| **Wavy Background** | Canvas API | CSS `@keyframes` mit SVG-Wellen | Mittel |
| **Spotlight Card** | React + Mouse Events | Nicht adaptierbar (braucht JS) | — |
| **3D Card** | Framer Motion | Nicht adaptierbar (braucht JS) | — |
| **Focus Cards** | Framer Motion | Nicht adaptierbar (braucht JS) | — |
| **Text Hover** | SVG + Framer Motion | CSS `stroke-dasharray` Animation | Mittel |
| **Text Animate** | Framer Motion | CSS `@keyframes` per Buchstabe | Hoch |
| **Colourful Text** | CSS Gradient | Direkt nutzbar (CSS `background-clip`) | Niedrig |
| **Compare** | React + Drag | Nicht adaptierbar (braucht JS) | — |
| **Carousel** | Framer Motion | Nicht adaptierbar (braucht JS) | — |
| **Testimonials** | Framer Motion | Statisches Zitat (kein Karussell) | Niedrig |

## CSS-Adaptionen für Slides

### Aurora Gradient (CSS-only)

```css
@keyframes auroraShift {
  0% {
    background-position: 0% 50%;
  }
  50% {
    background-position: 100% 50%;
  }
  100% {
    background-position: 0% 50%;
  }
}

.slide--aurora {
  background: linear-gradient(
    135deg,
    var(--slide-bg-dark) 0%,
    #2a6b5e 25%,
    #287d4b 50%,
    var(--slide-bg-dark) 75%,
    #2a6b5e 100%
  );
  background-size: 400% 400%;
  animation: auroraShift 12s ease-in-out infinite;
}
```

### Colourful Text (CSS-only)

```css
@keyframes gradientFlow {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}

.text-gradient {
  background: linear-gradient(
    90deg,
    #1c4b42,
    #287d4b,
    #4daf46,
    #b4e717,
    #4daf46,
    #287d4b,
    #1c4b42
  );
  background-size: 300% 100%;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  animation: gradientFlow 6s ease-in-out infinite;
}
```

### Text Stroke Animation (CSS-only)

```css
@keyframes strokeDraw {
  from {
    stroke-dashoffset: 1000;
    fill-opacity: 0;
  }
  to {
    stroke-dashoffset: 0;
    fill-opacity: 1;
  }
}

.text-stroke svg text {
  stroke: var(--slide-accent);
  stroke-width: 1;
  stroke-dasharray: 1000;
  fill: var(--slide-text-on-dark);
  fill-opacity: 0;
  animation: strokeDraw 2s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}
```

## Nicht-adaptierbare Patterns

Die folgenden Patterns benötigen JavaScript (React, Framer Motion, Canvas API) und können **nicht** in statischen HTML-Slides verwendet werden:

- Spotlight Card (Cursor-Tracking)
- 3D Card Effect (Perspective Transform auf Mouse Move)
- Focus Cards (Hover-State-Management über mehrere Elemente)
- Compare Slider (Drag-Interaktion)
- Apple Cards Carousel (Scroll + Animation)
- Animated Testimonials (Auto-Play Karussell)

Diese Patterns sind für **React-basierte Websites** reserviert (siehe `skills/bkm-website/`).
