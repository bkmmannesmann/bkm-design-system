# BKM Slides — Style Presets (v3)

> Exakte CSS-Token für beide BKM-Kontexte. Alle Werte sind **verbindlich** — nicht interpretieren, sondern 1:1 kopieren. Basierend auf getesteten, freigegebenen Slides.

---

## Glasmorphismus-Token (EXAKT kopieren)

Glasmorphismus ist das zentrale Gestaltungselement für BKM-Slides. Es funktioniert auf **zwei Hintergrund-Typen**: Foto mit Overlay ODER flache BKM-Farbe.

### BKM AG Kontext (dunkler Hintergrund)

```css
/* Glass Card auf dunklem Hintergrund (Deep Green oder Foto mit Deep Green Overlay) */
.glass-card {
  background: rgba(255, 255, 255, 0.07);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 16px;
  padding: 52px 48px;              /* Titel-Slide */
  /* padding: 36px 40px;           /* Content-Slide */
}

/* Innerer Glow (optional, nur auf Titel-Slides) */
.glass-card::before {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: 16px;
  background: linear-gradient(160deg, rgba(255,255,255,0.04) 0%, transparent 40%);
  pointer-events: none;
}

/* Status-Card (sekundäre Glass-Variante) */
.status-card {
  background: rgba(180, 231, 23, 0.06);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border: 1px solid rgba(180, 231, 23, 0.15);
  border-radius: 14px;
  padding: 32px 36px;
}

/* Status-Badge */
.status-badge {
  background: rgba(180, 231, 23, 0.1);
  border: 1px solid rgba(180, 231, 23, 0.25);
  border-radius: 20px;
  padding: 5px 14px;
  font-weight: 700;
  font-size: 10px;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: #b4e717;
}
```

### Fachbetrieb Kontext (heller Hintergrund)

```css
/* Glass Card auf hellem Hintergrund (Sand/Beige oder Foto mit Sand Overlay) */
.glass-card {
  background: rgba(255, 255, 255, 0.55);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.7);
  border-radius: 16px;
  padding: 52px 48px;              /* Titel-Slide */
  /* padding: 36px 40px;           /* Content-Slide */
  /* padding: 32px 32px 28px 32px; /* Kompakte Cards */
}

/* Innerer Glow (optional, nur auf Titel-Slides) */
.glass-card::before {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: 16px;
  background: linear-gradient(160deg, rgba(255,255,255,0.3) 0%, transparent 40%);
  pointer-events: none;
}

/* Status-Card (sekundäre Glass-Variante) */
.status-card {
  background: rgba(77, 175, 70, 0.08);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border: 1px solid rgba(77, 175, 70, 0.2);
  border-radius: 14px;
  padding: 32px 36px;
}

/* Status-Badge */
.status-badge {
  background: rgba(77, 175, 70, 0.12);
  border: 1px solid rgba(77, 175, 70, 0.35);
  border-radius: 20px;
  padding: 6px 16px;
  font-weight: 700;
  font-size: 11px;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: #287d4b;
}
```

---

## Hintergrund-Token (EXAKT kopieren)

### BKM AG — Foto-Hintergrund mit Deep Green Overlay

```css
/* Titel-Slide: Stärkerer Overlay, Foto subtil sichtbar */
.bg-overlay-title {
  background: linear-gradient(
    140deg,
    rgba(28, 75, 66, 0.80) 0%,
    rgba(28, 75, 66, 0.60) 50%,
    rgba(28, 75, 66, 0.75) 100%
  );
}

/* Content-Slide: Asymmetrischer Overlay, rechts mehr Foto */
.bg-overlay-content {
  background: linear-gradient(
    160deg,
    rgba(28, 75, 66, 0.82) 0%,
    rgba(28, 75, 66, 0.65) 60%,
    rgba(28, 75, 66, 0.78) 100%
  );
}

/* Content-Slide: Links stark, rechts Foto durchscheinen */
.bg-overlay-asymmetric {
  background: linear-gradient(
    100deg,
    rgba(28, 75, 66, 0.88) 0%,
    rgba(28, 75, 66, 0.75) 55%,
    rgba(28, 75, 66, 0.45) 100%
  );
}
```

### BKM AG — Flache Farbe (ohne Foto)

```css
/* Deep Green als Vollflächenhintergrund — Glass hebt sich trotzdem ab */
.slide-container {
  background: #1c4b42;
}
```

### Fachbetrieb — Foto-Hintergrund mit Sand/Beige Overlay

```css
/* Titel-Slide: Stärkerer Overlay */
.bg-overlay-title {
  background: linear-gradient(
    140deg,
    rgba(246, 245, 242, 0.88) 0%,
    rgba(246, 245, 242, 0.75) 50%,
    rgba(246, 245, 242, 0.85) 100%
  );
}

/* Content-Slide: Gleichmäßiger Overlay */
.bg-overlay-content {
  background: linear-gradient(
    160deg,
    rgba(246, 245, 242, 0.88) 0%,
    rgba(246, 245, 242, 0.78) 60%,
    rgba(246, 245, 242, 0.86) 100%
  );
}

/* Content-Slide: Links stark, rechts Foto durchscheinen */
.bg-overlay-asymmetric {
  background: linear-gradient(
    100deg,
    rgba(246, 245, 242, 0.92) 0%,
    rgba(246, 245, 242, 0.82) 55%,
    rgba(246, 245, 242, 0.55) 100%
  );
}
```

### Fachbetrieb — Flache Farbe (ohne Foto)

```css
/* Sand/Beige als Vollflächenhintergrund — Glass hebt sich trotzdem ab */
.slide-container {
  background: #f6f5f2;
}
```

---

## Farb-Token (EXAKT kopieren)

### BKM AG Kontext

| Token | Wert | Einsatz |
|-------|------|---------|
| `--deep-green` | `#1c4b42` | Overlay, Footer-Bar, Card-Border |
| `--lime` | `#b4e717` | Akzentlinie, Checkmarks, Icons, Footer-Icons, Status-Badges |
| `--white` | `#ffffff` | Headlines auf dunkel, Body auf dunkel |
| `--white-70` | `rgba(255,255,255,0.7)` | Subtitles auf dunkel, Muted Text |
| `--white-50` | `rgba(255,255,255,0.5)` | Taglines, sehr dezenter Text |
| `--white-30` | `rgba(255,255,255,0.3)` | Seitenzahlen |
| `--sand` | `#f5f0eb` | Helle Slide-Hintergründe |
| `--pure-green` | `#4daf46` | Headlines auf Sand-Hintergrund |
| `--transition-green` | `#287d4b` | Footer-Bar Hintergrund (Alternative) |

### Fachbetrieb Kontext

| Token | Wert | Einsatz |
|-------|------|---------|
| `--sand` | `#f6f5f2` | Overlay, Slide-Hintergrund |
| `--pure-green` | `#4daf46` | Akzente, Icons, Checkmarks, Section-Labels |
| `--transition-green` | `#287d4b` | Footer-Bar Hintergrund, Meta-Text, Status-Badges |
| `--deep-green` | `#1c4b42` | Headlines (Unbounded 900) |
| `--stone-grey` | `#494949` | Body-Text, Subtitles |
| `--stone-grey-70` | `rgba(73, 73, 73, 0.7)` | Card-Subtitles, Feature-Beschreibungen |
| `--stone-grey-60` | `rgba(73, 73, 73, 0.6)` | Taglines |
| `--stone-grey-30` | `rgba(73, 73, 73, 0.3)` | Seitenzahlen |
| `--lime` | `#b4e717` | Footer-Bar Icons (auch im Fachbetrieb erlaubt in Footer) |
| `--pure-green-10` | `rgba(77, 175, 70, 0.1)` | Icon-Circle-Hintergrund |
| `--pure-green-15` | `rgba(77, 175, 70, 0.15)` | Divider-Linien |

---

## Typografie-Token (EXAKT kopieren)

Nur 3 Stufen. Keine Ausnahmen. Kein TT Norms Pro im Repo nötig — `system-ui` als Fallback reicht.

### Stufe 1: Headlines — Unbounded 900

```css
/* Google Fonts CDN einbinden: */
/* https://fonts.googleapis.com/css2?family=Unbounded:wght@900&display=swap */

/* H1 — UPPERCASE, KEIN Italic */
.headline-h1 {
  font-family: 'Unbounded', sans-serif;
  font-weight: 900;
  font-size: 56px;           /* Titel-Slide */
  text-transform: uppercase;
  color: #ffffff;             /* BKM AG auf dunkel */
  /* color: #1c4b42;          /* Fachbetrieb auf hell */
  line-height: 1.0;
  letter-spacing: -0.04em;
}

/* H2 — Content-Slides, kleiner */
.headline-h2 {
  font-family: 'Unbounded', sans-serif;
  font-weight: 900;
  font-size: 48px;           /* Content-Slide */
  /* font-size: 38px;         /* Wenn Platz knapp */
  /* font-size: 36px;         /* Dual-Card-Slides */
  text-transform: uppercase;
  line-height: 1.05;
  letter-spacing: -0.03em;
}

/* Card-Titel in Unbounded (kleine Variante) */
.headline-card {
  font-family: 'Unbounded', sans-serif;
  font-weight: 900;
  font-size: 17px;
  text-transform: uppercase;
  line-height: 1.15;
  letter-spacing: -0.02em;
}
```

### Stufe 2: Subtitles — System Font Bold

```css
.subtitle {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  font-weight: 700;
  font-size: 18px;
  /* font-size: 17px;         /* Etwas kleiner */
  /* font-size: 16px;         /* Kompakt */
  /* font-size: 13px;         /* Card-Subtitles */
}

/* Section-Label */
.section-label {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  font-weight: 700;
  font-size: 11px;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: #b4e717;             /* BKM AG */
  /* color: #4daf46;           /* Fachbetrieb */
}

/* Status-Badge Text */
.status-badge-text {
  font-weight: 700;
  font-size: 10px;            /* BKM AG */
  /* font-size: 11px;          /* Fachbetrieb */
  text-transform: uppercase;
  letter-spacing: 0.08em;
}
```

### Stufe 3: Body — System Font Regular

```css
.body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  font-weight: 400;
  font-size: 17px;            /* Subtitle-Body */
  /* font-size: 15px;          /* Checklist-Text */
  /* font-size: 14px;          /* Feature-Beschreibung, Footer */
  /* font-size: 13px;          /* Card-Body, kompakt */
  line-height: 1.6;
}
```

---

## Struktur-Token (EXAKT kopieren)

### Slide-Container

```css
.slide-container {
  width: 1280px;
  min-height: 720px;
  position: relative;
  overflow: hidden;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
}
```

### Hintergrund-Foto

```css
.bg-photo {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}
```

### Overlay (über dem Foto)

```css
.bg-overlay {
  position: absolute;
  inset: 0;
  /* Gradient-Werte siehe Hintergrund-Token oben */
}
```

### Logo

```css
.logo {
  position: absolute;
  top: 36px;                  /* Titel-Slide */
  /* top: 32px;                /* Content-Slide */
  right: 48px;                /* Titel-Slide */
  /* right: 44px;              /* Content-Slide */
  height: 38px;               /* Titel-Slide */
  /* height: 32px;             /* Content-Slide */
  z-index: 10;
  object-fit: contain;
}
```

### Vertikale Akzentlinie (nur BKM AG Titelseiten)

```css
.accent-line {
  position: absolute;
  left: 7%;
  top: 18%;
  width: 4px;
  height: 60%;
  background: #b4e717;        /* BKM AG: Lime */
  /* background: #4daf46;      /* Fachbetrieb: Pure Green */
  border-radius: 2px;
  z-index: 10;
}
```

### Keyvisual

```css
.keyvisual {
  position: absolute;
  top: 0;
  right: 0;
  height: 100%;
  width: 22%;                 /* Exakt 1/5 der Breite + etwas Bleed */
  object-fit: cover;
  object-position: left center;
  opacity: 0.18;              /* BKM AG auf dunkel */
  /* opacity: 0.15;            /* Fachbetrieb auf hell */
  z-index: 5;
}
```

### Footer-Bar

```css
/* BKM AG */
.footer-bar {
  background: rgba(28, 75, 66, 0.95);  /* Deep Green, leicht transparent */
  padding: 16px 80px;
  display: flex;
  align-items: center;
  gap: 12px;
}

/* Fachbetrieb */
.footer-bar {
  background: rgba(40, 125, 75, 0.95);  /* Transition Green, leicht transparent */
  padding: 16px 80px;
  display: flex;
  align-items: center;
  gap: 12px;
}

.footer-icon {
  color: #b4e717;             /* Lime — in BEIDEN Kontexten */
  font-size: 16px;
}

.footer-text {
  font-weight: 400;
  font-size: 14px;
  color: #ffffff;
}
```

### Seitenzahl

```css
.page-num {
  position: absolute;
  bottom: 56px;
  right: 44px;
  font-size: 11px;
  color: rgba(255,255,255,0.3);   /* BKM AG auf dunkel */
  /* color: rgba(73,73,73,0.3);    /* Fachbetrieb auf hell */
  z-index: 10;
}
```

### Content-Wrapper (Flexbox-Layout)

```css
.content-wrapper {
  position: relative;
  z-index: 10;
  display: flex;
  flex-direction: column;
  height: 720px;
}

/* Top Section (Headline-Bereich) */
.top-section {
  padding: 56px 80px 0 80px;  /* Standard */
  /* padding: 48px 80px 0 80px; /* Kompakt */
}

/* Main Content Area */
.main-content {
  flex: 1;
  display: flex;
  align-items: center;
  padding: 30px 80px;
  gap: 40px;
}

/* Zentrierter Content (CTA-Slides) */
.main-area-centered {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 80px;
}
```

### Icon-Circle (Feature-Listen)

```css
/* BKM AG */
.feature-icon {
  width: 32px;
  height: 32px;
  border-radius: 8px;
  background: rgba(180, 231, 23, 0.12);
  display: flex;
  align-items: center;
  justify-content: center;
}
.feature-icon i { color: #b4e717; font-size: 14px; }

/* Fachbetrieb */
.feature-icon {
  width: 32px;
  height: 32px;
  border-radius: 8px;
  background: rgba(77, 175, 70, 0.1);
  display: flex;
  align-items: center;
  justify-content: center;
}
.feature-icon i { color: #4daf46; font-size: 14px; }
```

### Runde Icon-Circles (Status-Cards, Prozess-Steps)

```css
/* BKM AG */
.step-circle {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  background: rgba(180, 231, 23, 0.08);
  border: 1px solid rgba(180, 231, 23, 0.2);
  display: flex;
  align-items: center;
  justify-content: center;
}
.step-circle i { color: #b4e717; font-size: 18px; }

/* Fachbetrieb */
.step-circle {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  background: rgba(77, 175, 70, 0.1);
  border: 1px solid rgba(77, 175, 70, 0.25);
  display: flex;
  align-items: center;
  justify-content: center;
}
.step-circle i { color: #4daf46; font-size: 18px; }
```

---

## Spacing-Token

| Element | Wert | Kontext |
|---------|------|---------|
| Slide-Padding horizontal | `80px` | Alle Slides |
| Slide-Padding top (Titel) | `56px` | Titel-Slides |
| Slide-Padding top (Content) | `48px` | Content-Slides |
| Card-Padding (groß) | `52px 48px` | Titel-Glass-Card |
| Card-Padding (mittel) | `36px 40px` | Content-Glass-Card |
| Card-Padding (kompakt) | `32px 32px 28px 32px` | Dual-Card-Layout |
| Card-Gap | `28px` | Zwischen Cards |
| Content-Gap | `40px` | Zwischen Hauptelementen |
| Footer-Bar Padding | `16px 80px` | Alle Footer-Bars |
| Checklist-Gap | `16px` | Zwischen Checkmark-Items |
| Feature-List-Gap | `18px` | Zwischen Feature-Items |

---

## Logo-Verwendung

| Kontext | Hintergrund | Logo-Datei |
|---------|-------------|------------|
| BKM AG | Dunkel (Deep Green / Foto) | `bkm-logo-white-puregreen.png` |
| Fachbetrieb | Hell (Sand / Foto) | `bkm-logo-stonegrey-puregreen.png` |
| Fachbetrieb | Transition Green (selten) | `bkm-logo-white-puregreen.png` |

### Keyvisual-Verwendung

| Kontext | Hintergrund | Keyvisual-Datei |
|---------|-------------|-----------------|
| BKM AG | Dunkel | `keyvisual-on-dark.svg` |
| Fachbetrieb | Hell | `keyvisual-on-light.svg` |

**Keyvisual-Regeln:**
- Immer am **rechten Rand**, immer **angeschnitten**
- Breite: **22%** der Slide-Breite (≈ 1/5)
- Opacity: **0.18** (BKM AG) / **0.15** (Fachbetrieb)
- Nur auf **Titelseiten** verwenden
- Nie links, nie mittig, nie gedreht, nie gespiegelt

---

## Font Awesome CDN

```html
<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" rel="stylesheet">
```

Häufig verwendete Icons:
- `fa-check` — Checkmarks
- `fa-handshake` — Vertrauen
- `fa-laptop-code` — Digitalisierung
- `fa-user-shield` — Spezialisierung
- `fa-leaf` — Nachhaltigkeit
- `fa-atom` — Innovation
- `fa-certificate` — Zertifizierung
- `fa-users` — Gemeinschaft
- `fa-rocket` — Launch
- `fa-flask` — In Entwicklung
- `fa-check-circle` — Bestätigung
- `fa-arrow-right` — Prozess-Pfeile
- `fa-cogs` — Optimierung
- `fa-comments` — Feedback
- `fa-user-check` — Partner
- `fa-bolt` — Schnelligkeit
- `fa-plug` — Integration
- `fa-link` — Verbindung
- `fa-th-large` — Übersicht
