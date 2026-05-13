# Digitale Medien

Richtlinien für alle digitalen Kommunikationsmittel der BKM Mannesmann AG.

## Webseiten & Online-Präsenz

| Bereich | Gestaltung |
|---------|-----------|
| Header | Weißer Hintergrund, grau-grünes Logo (Primärlogo), zentrierte Suchleiste |
| Top-Bar | Lime Green Hintergrund, schwarzer Text, wechselnde Botschaften |
| Hero-Banner | Großflächige Bilder, Keyvisual-Chevrons rechts, weiße Headline (Unbounded) |
| Footer | Deep Green Hintergrund, weißer Text, Adresse, Social Media |

## CTA-Buttons

| Zustand | Hintergrund | Schrift |
|---------|------------|---------|
| Standard | Deep Green (#1c4b42) | Lime Green (#b4e717) |
| Hover | Lime Green (#b4e717) | Deep Green (#1c4b42) |

Schrift: Unbounded Black, Versalien.

## Web-Banner

Großflächige Bilder mit Keyvisual-Chevrons rechts, weiße Headline in Unbounded Black. Subheadline in Lime Green. Produktbilder integriert.

## CSS-Variablen

```css
:root {
  --bkm-pure-green: #4daf46;
  --bkm-transition-green: #287d4b;
  --bkm-deep-green: #1c4b42;
  --bkm-lime-green: #b4e717;
  --bkm-sand-white: #f6f5f2;
  --bkm-stone-grey: #494949;
  --bkm-clean-white: #ffffff;
  --bkm-true-black: #000000;
}
```

## Tailwind CSS Konfiguration

```javascript
colors: {
  'bkm': {
    'pure-green': '#4daf46',
    'transition-green': '#287d4b',
    'deep-green': '#1c4b42',
    'lime-green': '#b4e717',
    'sand-white': '#f6f5f2',
    'stone-grey': '#494949',
  }
}
```

## Web-App Komponenten

| Komponente | Gestaltung |
|-----------|-----------|
| Primary Button | Lime Green (#b4e717) Hintergrund, Deep Green Text |
| Secondary Button | Pure Green (#4daf46) Hintergrund, White Text |
| Hover State | Transition Green (#287d4b) |
| Background | Sand White (#f6f5f2) |
| Cards | Clean White (#ffffff) mit leichtem Schatten |
| Header/Footer | Deep Green (#1c4b42) |

## Dark Mode

| Element | Farbe |
|---------|-------|
| Background | Deep Green (#1c4b42) |
| Text | Clean White (#ffffff) |
| Akzente | Lime Green (#b4e717) oder Pure Green (#4daf46) |

## Bildauflösungen

| Medium | Auflösung | Hinweis |
|--------|-----------|---------|
| Web (Standard) | 72 dpi | Optimiert für schnelle Ladezeiten |
| Web (Retina) | 144 dpi / @2x | Für hochauflösende Displays |

Bevorzugtes Bildformat: WebP (Fallback: JPEG).

## Google Fonts Import (Unbounded)

```html
<link href="https://fonts.googleapis.com/css2?family=Unbounded:wght@900&display=swap" rel="stylesheet">
```

TT Norms ist keine Google Font und muss lokal eingebunden werden. Fallback: `'TT Norms Pro', 'Roboto', sans-serif`.
