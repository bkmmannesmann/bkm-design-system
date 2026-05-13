# BKM Slides — HTML Template (Editorial)

> Architektur für einzelne HTML-Slide-Dateien im **Corporate Editorial**-Stil. Jede Slide ist eine eigenständige HTML-Datei ohne externe Abhängigkeiten (außer Google Fonts CDN für Unbounded). Basierend auf echten BKM-Broschüren und PDFs.

## Basis-Template

```html
<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{{SLIDE_TITLE}}</title>

  <!-- Google Fonts: Unbounded -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Unbounded:wght@900&display=swap" rel="stylesheet" />

  <style>
    /* ========================================
       BKM SLIDE SYSTEM — EDITORIAL
       Kontext: {{CONTEXT}} (BKM AG oder Fachbetrieb)
       ======================================== */

    /* Self-hosted TT Norms Pro */
    @font-face {
      font-family: 'TT Norms Pro';
      src: url('assets/fonts/TT_Norms_Pro_Compact_Regular.woff2') format('woff2');
      font-weight: 400;
      font-style: normal;
      font-display: swap;
    }
    @font-face {
      font-family: 'TT Norms Pro';
      src: url('assets/fonts/TT_Norms_Pro_Bold.woff2') format('woff2');
      font-weight: 700;
      font-style: normal;
      font-display: swap;
    }

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
       CSS VARIABLES
       ======================================== */
    :root {
      /* Hintergründe (nur 2 Typen!) */
      --slide-bg-dark: #1c4b42;
      --slide-bg-light: #f5f0eb;
      --slide-bg-card: #ffffff;

      /* Text */
      --slide-text-on-dark: #ffffff;
      --slide-text-on-dark-muted: rgba(255,255,255,0.7);
      --slide-text-on-light: #1a1a1a;
      --slide-text-on-light-muted: #494949;
      --slide-headline-on-light: #4daf46;

      /* Akzent */
      --slide-accent: #b4e717;
      --slide-card-border: #1c4b42;
      --slide-footer-bg: #1c4b42;

      /* Formen */
      --slide-radius-card: 8px;

      /* Fonts */
      --font-display: 'Unbounded', system-ui, sans-serif;
      --font-body: 'TT Norms Pro', system-ui, sans-serif;
    }

    /* ========================================
       SLIDE CONTAINER
       ======================================== */
    .slide {
      width: 100vw;
      height: 100vh;
      position: relative;
      overflow: hidden;
      display: flex;
      flex-direction: column;
    }

    /* Dark surface (Titel, CTA, Zitate) */
    .slide--dark {
      background-color: var(--slide-bg-dark);
      color: var(--slide-text-on-dark);
    }

    /* Light surface (Content, Daten) */
    .slide--light {
      background-color: var(--slide-bg-light);
      color: var(--slide-text-on-light);
    }

    /* ========================================
       CONTENT AREAS
       ======================================== */
    .slide__content {
      position: relative;
      z-index: 10;
      flex: 1;
      padding: 60px 80px;
      display: flex;
      flex-direction: column;
      justify-content: center;
    }

    .slide__content--top {
      justify-content: flex-start;
      padding-top: 80px;
    }

    .slide__content--split {
      flex-direction: row;
      align-items: center;
      gap: 60px;
    }

    .slide__half {
      flex: 1;
      min-width: 0;
    }

    /* ========================================
       SIGNATURE ELEMENTS
       ======================================== */

    /* Vertikale Lime-Akzentlinie (nur Titelseiten, BKM AG) */
    .accent-line {
      position: absolute;
      left: 7%;
      top: 20%;
      width: 4px;
      height: 60%;
      background-color: var(--slide-accent);
    }

    /* Deep Green Footer-Bar (Content-Slides) */
    .footer-bar {
      background-color: var(--slide-footer-bg);
      padding: 16px 80px;
      display: flex;
      align-items: center;
      gap: 12px;
      width: 100%;
    }

    .footer-bar__icon {
      color: var(--slide-accent);
      font-size: 18px;
    }

    .footer-bar__text {
      font-family: var(--font-body);
      font-weight: 400;
      color: #ffffff;
      font-size: 14px;
    }

    /* ========================================
       TYPOGRAPHY (3 Stufen)
       ======================================== */

    /* Stufe 1: Headlines — Unbounded Bold 900 */
    .headline-h1 {
      font-family: var(--font-display);
      font-weight: 900;
      text-transform: uppercase;
      letter-spacing: -0.04em;
      line-height: 1.0;
      font-size: clamp(48px, 6vw, 100px);
    }

    .headline-h2 {
      font-family: var(--font-display);
      font-weight: 900;
      text-transform: none;
      letter-spacing: -0.02em;
      line-height: 1.1;
      font-size: clamp(32px, 4vw, 48px);
    }

    /* Stufe 2: Subtitles / Card-Titel — TT Norms Pro Bold */
    .subtitle {
      font-family: var(--font-body);
      font-weight: 700;
      line-height: 1.3;
      font-size: clamp(16px, 1.5vw, 20px);
    }

    .stat-number {
      font-family: var(--font-body);
      font-weight: 700;
      line-height: 1.0;
      font-size: clamp(48px, 5vw, 96px);
    }

    /* Stufe 3: Body — TT Norms Pro Regular */
    .body {
      font-family: var(--font-body);
      font-weight: 400;
      line-height: 1.6;
      font-size: clamp(14px, 1.2vw, 16px);
    }

    .body-lg {
      font-family: var(--font-body);
      font-weight: 400;
      line-height: 1.7;
      font-size: clamp(16px, 1.5vw, 20px);
    }

    .label {
      font-family: var(--font-body);
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      font-size: clamp(10px, 0.9vw, 13px);
    }

    /* ========================================
       COMPONENTS
       ======================================== */

    /* Card mit Border-Left (Editorial) */
    .card {
      background: var(--slide-bg-card);
      border-left: 4px solid var(--slide-card-border);
      border-radius: var(--slide-radius-card);
      padding: 24px;
      /* KEIN box-shadow! */
    }

    .card--warning {
      border-left-color: #dc2626;
    }

    .card--highlight {
      border-left-color: var(--slide-accent);
    }

    .card__title {
      font-family: var(--font-body);
      font-weight: 700;
      color: var(--slide-text-on-light);
      font-size: 18px;
    }

    .card__body {
      font-family: var(--font-body);
      font-weight: 400;
      color: var(--slide-text-on-light-muted);
      font-size: 15px;
      margin-top: 8px;
      line-height: 1.5;
    }

    /* Glasmorphismus (optional, auf Foto-Hintergründen) */
    .glass {
      background: rgba(255, 255, 255, 0.12);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border: 1px solid rgba(255, 255, 255, 0.15);
      border-radius: 12px;
      padding: 40px;
    }

    /* Stat Block */
    .stat {
      display: flex;
      flex-direction: column;
      gap: 8px;
    }

    .stat__value {
      font-family: var(--font-body);
      font-weight: 700;
      font-size: clamp(48px, 5vw, 96px);
      line-height: 1.0;
      color: var(--slide-accent);
    }

    .stat__label {
      font-family: var(--font-body);
      font-weight: 400;
      font-size: clamp(12px, 1vw, 14px);
      opacity: 0.7;
    }

    /* Checkmark List */
    .checklist {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }

    .checklist__item {
      display: flex;
      align-items: flex-start;
      gap: 12px;
    }

    .checklist__icon {
      color: var(--slide-accent);
      font-size: 20px;
      flex-shrink: 0;
    }

    .checklist__text {
      font-family: var(--font-body);
      font-weight: 700;
      color: var(--slide-text-on-light);
      font-size: 16px;
    }

    /* Page number */
    .slide__page-number {
      position: absolute;
      bottom: 20px;
      right: 40px;
      font-family: var(--font-body);
      font-weight: 400;
      font-size: 12px;
      opacity: 0.4;
    }
  </style>
</head>
<body>
  <div class="slide slide--dark">
    <div class="slide__content">
      <!-- SLIDE CONTENT HERE -->
    </div>
  </div>
</body>
</html>
```

## Slide-Typen

### 1. Titel-Slide (BKM AG — Deep Green + Lime-Linie)

```html
<div class="slide slide--dark">
  <!-- Vertikale Lime-Akzentlinie -->
  <div class="accent-line"></div>
  
  <!-- Logo oben rechts -->
  <img src="assets/logos/bkm-logo-white-puregreen.svg" alt="BKM"
       style="position: absolute; top: 5%; right: 5%; height: 40px;" />
  
  <div class="slide__content" style="padding-left: 10%;">
    <h1 class="headline-h1" style="font-style: italic;">
      {{PRESENTATION_TITLE}}
    </h1>
    <p class="body-lg" style="color: var(--slide-text-on-dark-muted); margin-top: 24px; max-width: 60%;">
      {{SUBTITLE}}
    </p>
    <div style="margin-top: 32px; display: flex; align-items: center; gap: 12px;">
      <span style="color: var(--slide-accent);">●</span>
      <span class="label" style="color: var(--slide-accent);">{{AUTHOR}} • {{DATE}}</span>
    </div>
  </div>
</div>
```

### 2. Content-Slide (Sand/Beige + Cards + Footer-Bar)

```html
<div class="slide slide--light">
  <div class="slide__content slide__content--top">
    <h2 class="headline-h2" style="color: var(--slide-headline-on-light);">
      {{HEADLINE}}
    </h2>
    
    <!-- Card Grid -->
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 24px; margin-top: 40px;">
      <div class="card">
        <h3 class="card__title">{{CARD_TITLE_1}}</h3>
        <p class="card__body">{{CARD_BODY_1}}</p>
      </div>
      <div class="card">
        <h3 class="card__title">{{CARD_TITLE_2}}</h3>
        <p class="card__body">{{CARD_BODY_2}}</p>
      </div>
    </div>
  </div>
  
  <!-- Footer-Bar -->
  <div class="footer-bar">
    <span class="footer-bar__icon">✓</span>
    <span class="footer-bar__text">{{FOOTER_TEXT}}</span>
  </div>
  
  <span class="slide__page-number">{{PAGE_NUMBER}}</span>
</div>
```

### 3. Foto-Slide (Split Layout — 50/50)

```html
<div class="slide slide--light">
  <div class="slide__content slide__content--split">
    <!-- Text-Hälfte -->
    <div class="slide__half">
      <span class="label" style="color: var(--slide-headline-on-light);">{{SECTION_LABEL}}</span>
      <h2 class="headline-h2" style="color: var(--slide-headline-on-light); margin-top: 12px;">
        {{HEADLINE}}
      </h2>
      <p class="body" style="color: var(--slide-text-on-light-muted); margin-top: 16px;">
        {{BODY_TEXT}}
      </p>
    </div>
    
    <!-- Foto-Hälfte (mindestens 40% der Slide) -->
    <div class="slide__half" style="height: 100%; position: relative;">
      <img src="{{IMAGE_PATH}}" alt="{{IMAGE_ALT}}"
           style="width: 100%; height: 100%; object-fit: cover; border-radius: 8px;" />
    </div>
  </div>
  
  <span class="slide__page-number">{{PAGE_NUMBER}}</span>
</div>
```

### 4. Daten-Slide (Große Zahlen)

```html
<div class="slide slide--light">
  <div class="slide__content" style="align-items: center; text-align: center;">
    <span class="label" style="color: var(--slide-headline-on-light);">{{SECTION_LABEL}}</span>
    <h2 class="headline-h2" style="color: var(--slide-headline-on-light); margin-top: 12px;">
      {{HEADLINE}}
    </h2>
    
    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 60px; margin-top: 60px;">
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
  
  <!-- Footer-Bar -->
  <div class="footer-bar">
    <span class="footer-bar__icon">📊</span>
    <span class="footer-bar__text">{{DATA_SOURCE}}</span>
  </div>
</div>
```

### 5. Zitat-Slide (Deep Green + Zentriert)

```html
<div class="slide slide--dark">
  <div class="slide__content" style="align-items: center; text-align: center;">
    <span style="font-size: 64px; color: var(--slide-accent); line-height: 1;">„</span>
    <blockquote class="headline-h2" style="max-width: 70%; margin-top: 16px; font-style: italic;">
      {{QUOTE_TEXT}}
    </blockquote>
    <p class="subtitle" style="color: var(--slide-text-on-dark-muted); margin-top: 24px;">
      — {{AUTHOR_NAME}}, {{AUTHOR_ROLE}}
    </p>
  </div>
</div>
```

### 6. CTA/Schluss-Slide (Deep Green + Kontakt)

```html
<div class="slide slide--dark">
  <!-- Logo oben rechts -->
  <img src="assets/logos/bkm-logo-white-puregreen.svg" alt="BKM"
       style="position: absolute; top: 5%; right: 5%; height: 40px;" />
  
  <div class="slide__content" style="align-items: center; text-align: center;">
    <h2 class="headline-h1">{{CTA_HEADLINE}}</h2>
    <p class="body-lg" style="color: var(--slide-text-on-dark-muted); margin-top: 16px; max-width: 60%;">
      {{CTA_BODY}}
    </p>
    <div style="margin-top: 40px; display: flex; flex-direction: column; align-items: center; gap: 8px;">
      <span class="subtitle" style="color: var(--slide-accent);">{{CONTACT_EMAIL}}</span>
      <span class="body" style="color: var(--slide-text-on-dark-muted);">{{CONTACT_PHONE}}</span>
    </div>
  </div>
</div>
```

### 7. Glasmorphismus-Slide (Foto-Hintergrund + Glass Card)

```html
<div class="slide" style="position: relative;">
  <!-- Vollbild-Foto -->
  <img src="{{PHOTO_PATH}}" alt="" 
       style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover;" />
  
  <!-- Dunkles Overlay -->
  <div style="position: absolute; inset: 0; background: rgba(28, 75, 66, 0.55);"></div>
  
  <!-- Glass Card -->
  <div class="slide__content" style="align-items: flex-start;">
    <div class="glass" style="max-width: 500px;">
      <h2 class="headline-h2" style="color: #ffffff;">{{HEADLINE}}</h2>
      <p class="body-lg" style="color: rgba(255,255,255,0.85); margin-top: 16px;">
        {{BODY_TEXT}}
      </p>
    </div>
  </div>
</div>
```

## Platzhalter-Referenz

| Platzhalter | Beschreibung |
|-------------|-------------|
| `{{CONTEXT}}` | "BKM AG" oder "Fachbetrieb" |
| `{{SLIDE_TITLE}}` | HTML-Seitentitel |
| `{{PRESENTATION_TITLE}}` | Präsentations-Haupttitel |
| `{{SUBTITLE}}` | Untertitel |
| `{{AUTHOR}}` | Autor-Name |
| `{{DATE}}` | Datum |
| `{{SECTION_LABEL}}` | Sektions-Label (z.B. "01 — Produkte") |
| `{{HEADLINE}}` | Slide-Headline |
| `{{BODY_TEXT}}` | Fließtext |
| `{{CARD_TITLE_N}}` | Card-Titel |
| `{{CARD_BODY_N}}` | Card-Body |
| `{{FOOTER_TEXT}}` | Footer-Bar Text |
| `{{PAGE_NUMBER}}` | Seitenzahl (z.B. "03") |
| `{{IMAGE_PATH}}` | Pfad zum Bild |
| `{{VALUE_N}}` | Statistik-Wert |
| `{{LABEL_N}}` | Statistik-Label |
| `{{DATA_SOURCE}}` | Datenquelle |
