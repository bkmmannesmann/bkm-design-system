# BKM Slides — HTML Template

> Architektur für einzelne HTML-Slide-Dateien. Jede Slide ist eine eigenständige HTML-Datei ohne externe Abhängigkeiten (außer Google Fonts CDN).

## Basis-Template

```html
<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{{SLIDE_TITLE}}</title>

  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Unbounded:wght@900&display=swap" rel="stylesheet" />

  <style>
    /* ========================================
       BKM SLIDE SYSTEM — {{CONTEXT}} PRESET
       ======================================== */

    /* Reset */
    *, *::before, *::after {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    /* Viewport-Lock: 16:9 */
    html, body {
      width: 100vw;
      height: 100vh;
      overflow: hidden;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
    }

    /* ========================================
       CSS VARIABLES — {{CONTEXT}} PRESET
       (Ersetze mit Werten aus STYLE_PRESETS.md)
       ======================================== */
    :root {
      --slide-bg-dark: {{BG_DARK}};
      --slide-bg-dark-alt: {{BG_DARK_ALT}};
      --slide-bg-light: #ffffff;
      --slide-bg-warm: #f6f5f2;

      --slide-text-on-dark: #ffffff;
      --slide-text-on-dark-muted: rgba(255,255,255,0.5);
      --slide-text-on-light: #1a1a1a;
      --slide-text-on-light-muted: #494949;

      --slide-accent: {{ACCENT}};
      --slide-accent-on-dark: {{ACCENT_ON_DARK}};
      --slide-accent-on-light: {{ACCENT_ON_LIGHT}};

      --slide-divider: rgba(255,255,255,0.15);
      --slide-divider-light: #e8e6e1;

      --slide-radius-sm: 4px;
      --slide-radius-md: 8px;
      --slide-radius-lg: 12px;

      /* Fonts */
      --font-display: 'Unbounded', system-ui, sans-serif;
      --font-body: 'TT Norms Pro', system-ui, sans-serif;
      --font-mono: 'TT Norms Pro', monospace;
    }

    /* ========================================
       TYPOGRAPHY SYSTEM
       ======================================== */

    /* Headlines — Unbounded 900 UPPERCASE */
    .headline-xl {
      font-family: var(--font-display);
      font-weight: 900;
      text-transform: uppercase;
      letter-spacing: -0.04em;
      line-height: 1.0;
      font-size: clamp(48px, 6vw, 72px);
    }

    .headline-lg {
      font-family: var(--font-display);
      font-weight: 900;
      text-transform: uppercase;
      letter-spacing: -0.03em;
      line-height: 1.05;
      font-size: clamp(36px, 4.5vw, 56px);
    }

    .headline-md {
      font-family: var(--font-display);
      font-weight: 900;
      text-transform: uppercase;
      letter-spacing: -0.02em;
      line-height: 1.08;
      font-size: clamp(28px, 3.5vw, 44px);
    }

    .headline-sm {
      font-family: var(--font-display);
      font-weight: 900;
      text-transform: uppercase;
      letter-spacing: -0.02em;
      line-height: 1.15;
      font-size: clamp(22px, 2.8vw, 36px);
    }

    /* Body — TT Norms Pro */
    .body-lg {
      font-family: var(--font-body);
      font-weight: 400;
      line-height: 1.7;
      font-size: clamp(16px, 1.5vw, 20px);
    }

    .body-md {
      font-family: var(--font-body);
      font-weight: 400;
      line-height: 1.6;
      font-size: clamp(14px, 1.2vw, 16px);
    }

    /* Labels — TT Norms Pro Bold Uppercase */
    .label {
      font-family: var(--font-body);
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      font-size: clamp(10px, 0.9vw, 13px);
    }

    /* Mono — TT Norms Pro for specs */
    .mono {
      font-family: var(--font-mono);
      font-weight: 500;
      line-height: 1.4;
    }

    .mono-lg { font-size: clamp(18px, 1.8vw, 24px); }
    .mono-md { font-size: clamp(14px, 1.2vw, 16px); }

    /* ========================================
       SLIDE CONTAINER
       ======================================== */
    .slide {
      width: 100vw;
      height: 100vh;
      position: relative;
      overflow: hidden;
      display: flex;
    }

    /* Dark surface */
    .slide--dark {
      background-color: var(--slide-bg-dark);
      color: var(--slide-text-on-dark);
    }

    /* Light surface */
    .slide--light {
      background-color: var(--slide-bg-light);
      color: var(--slide-text-on-light);
    }

    /* Warm surface */
    .slide--warm {
      background-color: var(--slide-bg-warm);
      color: var(--slide-text-on-light);
    }

    /* ========================================
       CONTENT AREAS
       ======================================== */
    .slide__content {
      position: relative;
      z-index: 10;
      width: 100%;
      max-width: 1280px;
      margin: 0 auto;
      padding: 5vh 5vw;
      display: flex;
      flex-direction: column;
      justify-content: center;
    }

    .slide__content--left {
      align-items: flex-start;
      text-align: left;
    }

    .slide__content--center {
      align-items: center;
      text-align: center;
    }

    .slide__content--split {
      flex-direction: row;
      align-items: center;
      gap: 5vw;
    }

    .slide__half {
      flex: 1;
      min-width: 0;
    }

    /* ========================================
       COMPONENTS
       ======================================== */

    /* Badge */
    .badge {
      display: inline-flex;
      align-items: center;
      padding: 0.4em 0.8em;
      border-radius: var(--slide-radius-sm);
      font-family: var(--font-body);
      font-weight: 700;
      font-size: clamp(10px, 0.9vw, 13px);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .badge--accent {
      background-color: var(--slide-accent);
      color: var(--slide-bg-dark);
    }

    .badge--dark {
      background-color: var(--slide-bg-dark);
      color: var(--slide-accent);
    }

    /* Divider */
    .divider {
      width: 60px;
      height: 3px;
      background-color: var(--slide-accent);
      border: none;
      margin: 2vh 0;
    }

    /* Stat Block */
    .stat {
      display: flex;
      flex-direction: column;
      gap: 0.5vh;
    }

    .stat__value {
      font-family: var(--font-mono);
      font-weight: 500;
      font-size: clamp(32px, 4vw, 56px);
      line-height: 1.0;
      color: var(--slide-accent);
    }

    .stat__label {
      font-family: var(--font-body);
      font-weight: 400;
      font-size: clamp(12px, 1vw, 14px);
      opacity: 0.7;
    }

    /* Card (on light slides) */
    .card {
      background: var(--slide-bg-light);
      border-radius: var(--slide-radius-lg);
      padding: 2vw;
      box-shadow: rgba(0,0,0,0.08) 0px 0px 0px 1px, rgba(0,0,0,0.04) 0px 2px 4px;
    }

    /* Noise Texture Overlay */
    .noise::after {
      content: "";
      position: absolute;
      inset: 0;
      z-index: 1;
      pointer-events: none;
      opacity: 0.04;
      background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.65' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)'/%3E%3C/svg%3E");
      background-repeat: repeat;
      background-size: 256px 256px;
      mix-blend-mode: overlay;
    }

    /* Footer */
    .slide__footer {
      position: absolute;
      bottom: 3vh;
      left: 5vw;
      right: 5vw;
      display: flex;
      justify-content: space-between;
      align-items: center;
      z-index: 20;
    }

    .slide__footer-text {
      font-family: var(--font-body);
      font-weight: 400;
      font-size: clamp(10px, 0.8vw, 12px);
      opacity: 0.4;
    }

    .slide__page-number {
      font-family: var(--font-mono);
      font-weight: 500;
      font-size: clamp(10px, 0.8vw, 12px);
      opacity: 0.4;
    }
  </style>
</head>
<body>
  <div class="slide slide--dark noise">
    <div class="slide__content slide__content--left">
      <!-- SLIDE CONTENT HERE -->
    </div>
    <div class="slide__footer">
      <span class="slide__footer-text">BKM Mannesmann AG</span>
      <span class="slide__page-number">01</span>
    </div>
  </div>
</body>
</html>
```

## Slide-Typen

### Titel-Slide

```html
<div class="slide slide--dark noise">
  <div class="slide__content slide__content--left">
    <span class="label" style="color: var(--slide-text-on-dark-muted); margin-bottom: 3vh;">
      Bauwerksabdichtung seit 1928
    </span>
    <h1 class="headline-xl" style="max-width: 70%;">
      {{PRESENTATION_TITLE}}
    </h1>
    <hr class="divider" style="margin: 3vh 0;" />
    <p class="body-lg" style="color: var(--slide-text-on-dark-muted); max-width: 50%;">
      {{SUBTITLE}}
    </p>
  </div>
  <!-- Optional: Keyvisual rechts -->
</div>
```

### Inhalts-Slide (Dunkel, Text links)

```html
<div class="slide slide--dark noise">
  <div class="slide__content slide__content--left">
    <span class="label" style="color: var(--slide-accent);">{{SECTION_LABEL}}</span>
    <h2 class="headline-lg" style="margin-top: 1vh; max-width: 70%;">{{HEADLINE}}</h2>
    <p class="body-lg" style="margin-top: 2vh; max-width: 60%; opacity: 0.7;">
      {{BODY_TEXT}}
    </p>
  </div>
</div>
```

### Inhalts-Slide (Hell, Split Layout)

```html
<div class="slide slide--warm">
  <div class="slide__content slide__content--split">
    <div class="slide__half">
      <span class="label" style="color: var(--slide-accent-on-light);">{{SECTION_LABEL}}</span>
      <h2 class="headline-md" style="margin-top: 1vh; color: var(--slide-text-on-light);">{{HEADLINE}}</h2>
      <p class="body-md" style="margin-top: 2vh; color: var(--slide-text-on-light-muted);">
        {{BODY_TEXT}}
      </p>
    </div>
    <div class="slide__half">
      <!-- Bild, Chart, oder Daten -->
    </div>
  </div>
</div>
```

### Daten-Slide (Statistiken)

```html
<div class="slide slide--warm">
  <div class="slide__content slide__content--center">
    <span class="label" style="color: var(--slide-accent-on-light);">{{SECTION_LABEL}}</span>
    <h2 class="headline-md" style="margin-top: 1vh;">{{HEADLINE}}</h2>
    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 4vw; margin-top: 5vh;">
      <div class="stat">
        <span class="stat__value">{{VALUE_1}}</span>
        <span class="stat__label">{{LABEL_1}}</span>
      </div>
      <div class="stat">
        <span class="stat__value">{{VALUE_2}}</span>
        <span class="stat__label">{{LABEL_2}}</span>
      </div>
      <div class="stat">
        <span class="stat__value">{{VALUE_3}}</span>
        <span class="stat__label">{{LABEL_3}}</span>
      </div>
    </div>
  </div>
</div>
```

### Schluss-Slide (CTA)

```html
<div class="slide slide--dark noise">
  <div class="slide__content slide__content--center">
    <h2 class="headline-lg">{{CTA_HEADLINE}}</h2>
    <p class="body-lg" style="margin-top: 2vh; opacity: 0.7; max-width: 60%;">
      {{CTA_BODY}}
    </p>
    <div style="margin-top: 4vh; display: flex; gap: 1vw; align-items: center;">
      <span class="mono-md" style="color: var(--slide-accent);">{{CONTACT_INFO}}</span>
    </div>
  </div>
</div>
```

## Platzhalter-Referenz

| Platzhalter | Beschreibung |
|-------------|-------------|
| `{{CONTEXT}}` | "BKM AG" oder "Fachbetrieb" |
| `{{BG_DARK}}` | Dunkle Hintergrundfarbe (#1c4b42 oder #494949) |
| `{{BG_DARK_ALT}}` | Alternative dunkle Farbe (#2a6b5e oder #3a3a3a) |
| `{{ACCENT}}` | Akzentfarbe (#b4e717 oder #4daf46) |
| `{{ACCENT_ON_DARK}}` | Akzent auf dunklem Hintergrund |
| `{{ACCENT_ON_LIGHT}}` | Akzent auf hellem Hintergrund (#1c4b42 oder #287d4b) |
| `{{SLIDE_TITLE}}` | HTML-Seitentitel |
| `{{PRESENTATION_TITLE}}` | Präsentations-Haupttitel |
| `{{SUBTITLE}}` | Untertitel |
| `{{SECTION_LABEL}}` | Sektions-Label (z.B. "01 — Produkte") |
| `{{HEADLINE}}` | Slide-Headline |
| `{{BODY_TEXT}}` | Fließtext |
