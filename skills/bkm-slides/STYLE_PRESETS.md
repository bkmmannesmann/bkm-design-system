# BKM Slides — Style Presets

> Vollständige Farbdefinitionen und Typografie-Regeln für beide BKM-Kontexte. Jedes Preset definiert alle CSS-Variablen, die in der HTML-Template verwendet werden.

---

## Preset 1: BKM AG

**Einsatz:** Corporate-Präsentationen, Produkt-Launches, Investor-Decks, Marketing-Slides, Messe-Präsentationen.

**Atmosphäre:** Autoritativ, schützend, materiell. Deep Green dominiert als Fläche. Lime Green ist der einzige Akzent — sparsam, nur für interaktive oder hervorgehobene Elemente.

### CSS-Variablen

```css
:root {
  /* Flächen */
  --slide-bg-dark: #1c4b42;           /* Deep Green — Hauptfläche dunkel */
  --slide-bg-dark-alt: #2a6b5e;       /* Deep Green Light — Alternative */
  --slide-bg-light: #ffffff;           /* Weiß — Hauptfläche hell */
  --slide-bg-warm: #f6f5f2;           /* Sand White — Warme Fläche */

  /* Text */
  --slide-text-on-dark: #ffffff;       /* Weiß auf dunklen Flächen */
  --slide-text-on-dark-muted: rgba(255,255,255,0.5);
  --slide-text-on-light: #1a1a1a;     /* Fast-Schwarz auf hellen Flächen */
  --slide-text-on-light-muted: #494949;

  /* Akzent */
  --slide-accent: #b4e717;            /* Lime — Primärer Akzent */
  --slide-accent-on-dark: #b4e717;    /* Lime auf Deep Green */
  --slide-accent-on-light: #1c4b42;   /* Deep Green auf Weiß */

  /* Semantische Grüntöne */
  --slide-green-deep: #1c4b42;
  --slide-green-transition: #287d4b;
  --slide-green-pure: #4daf46;
  --slide-green-lime: #b4e717;

  /* Strukturelemente */
  --slide-divider: rgba(255,255,255,0.15);
  --slide-divider-light: #e8e6e1;
  --slide-shadow: rgba(0,0,0,0.08) 0px 0px 0px 1px, rgba(0,0,0,0.04) 0px 2px 4px;

  /* Formen */
  --slide-radius-sm: 4px;
  --slide-radius-md: 8px;
  --slide-radius-lg: 12px;
}
```

### Farbkombinationen

| Slide-Typ | Hintergrund | Headline | Body | Akzent |
|-----------|-------------|----------|------|--------|
| Titel-Slide | Deep Green | Weiß | Weiß/50% | Lime |
| Inhalts-Slide (dunkel) | Deep Green | Weiß | Weiß/70% | Lime |
| Inhalts-Slide (hell) | Weiß/Sand White | #1a1a1a | #494949 | Deep Green |
| Daten-Slide | Sand White | #1a1a1a | #494949 | Lime auf Deep Green |
| Schluss-Slide | Deep Green | Weiß | Weiß/50% | Lime |

### Slide-Rhythmus

Der empfohlene Rhythmus für eine BKM AG Präsentation:

```
1. Titel-Slide          → Dunkel (Deep Green + Keyvisual)
2. Agenda/Überblick      → Hell (Sand White)
3. Inhalt 1              → Dunkel (Deep Green)
4. Inhalt 2              → Hell (Weiß)
5. Daten/Zahlen          → Hell (Sand White + Charts)
6. Inhalt 3              → Dunkel (Deep Green)
7. Zitat/Testimonial     → Dunkel (Deep Green)
8. Zusammenfassung       → Hell (Weiß)
9. CTA/Schluss           → Dunkel (Deep Green + Keyvisual)
```

Regel: **Nie zwei gleiche Hintergründe hintereinander.** Immer zwischen dunkel und hell alternieren.

---

## Preset 2: Fachbetrieb

**Einsatz:** Fachbetrieb-Präsentationen, Kunden-Pitches, Schulungen, Zertifizierungs-Unterlagen, lokale Marketing-Slides.

**Atmosphäre:** Kompetent, bodenständig, lösungsorientiert. Das Fachbetrieb-Preset ist bewusst **hell und offen** — Weiß und Sand White dominieren als Flächen. Transition Green dient als Identitätsfarbe für Header-Bänder und Headlines. Pure Green ist der Akzent. Stone Grey ist **nur Textfarbe und für kleine Strukturelemente** (Footer, Divider) — **nie als dominante Hintergrundfläche**, da es das Design schwer und erdrückend wirken lässt. Kein Lime.

### CSS-Variablen

```css
:root {
  /* Flächen — HELL DOMINIERT */
  --slide-bg-primary: #ffffff;         /* Weiß — Dominante Hauptfläche */
  --slide-bg-warm: #f6f5f2;           /* Sand White — Alternative Hauptfläche */
  --slide-bg-accent-band: #287d4b;    /* Transition Green — Für Header-Bänder (sparsam!) */
  --slide-bg-dark: #494949;           /* Stone Grey — NUR für Footer-Zeilen, NIE als Fläche */

  /* Text */
  --slide-text-primary: #494949;       /* Stone Grey — Primäre Textfarbe auf hellen Flächen */
  --slide-text-headline: #287d4b;      /* Transition Green — Headlines auf hellen Flächen */
  --slide-text-on-accent: #ffffff;     /* Weiß — Text auf Transition Green Bändern */
  --slide-text-muted: rgba(73,73,73,0.6); /* Stone Grey 60% — Sekundärtext */

  /* Akzent */
  --slide-accent: #4daf46;            /* Pure Green — Dekorativer Akzent (Icons, Dots, Badges) */
  --slide-accent-readable: #287d4b;   /* Transition Green — Lesbarer Akzent auf Weiß (5.09 Kontrast) */
  /* KEIN Lime im Fachbetrieb-Kontext */

  /* Semantische Grüntöne */
  --slide-green-transition: #287d4b;
  --slide-green-pure: #4daf46;

  /* Strukturelemente */
  --slide-divider-light: #e8e6e1;
  --slide-divider-accent: #4daf46;     /* Pure Green Trennlinien */
  --slide-shadow: rgba(0,0,0,0.08) 0px 0px 0px 1px, rgba(0,0,0,0.04) 0px 2px 4px;

  /* Formen */
  --slide-radius-sm: 4px;
  --slide-radius-md: 8px;
  --slide-radius-lg: 12px;
}
```

### Farbkombinationen

| Slide-Typ | Hintergrund | Headline | Body | Akzent |
|-----------|-------------|----------|------|--------|
| Titel-Slide | Weiß + Transition Green Header-Band | Transition Green | Stone Grey | Pure Green Divider |
| Inhalts-Slide (hell) | Weiß | Transition Green | Stone Grey | Pure Green Icons/Dots |
| Inhalts-Slide (warm) | Sand White | Transition Green | Stone Grey | Pure Green Badges |
| Daten-Slide | Sand White | Transition Green | Stone Grey | Pure Green Zahlen |
| Akzent-Slide | Transition Green (sparsam!) | Weiß | Weiß/70% | Pure Green |
| Schluss-Slide | Weiß + Transition Green Header-Band | Transition Green | Stone Grey | Pure Green CTA |

### Slide-Rhythmus

```
1. Titel-Slide          → Weiß + Transition Green Header-Band
2. Agenda/Überblick      → Sand White (komplett hell)
3. Leistung 1            → Weiß (hell, Cards mit Shadow)
4. Leistung 2            → Sand White (warm)
5. Akzent-Slide          → Transition Green (EINZIGE dunkle Slide — sparsam!)
6. Referenz/Zahlen       → Weiß (hell, große Zahlen in Pure Green)
7. Kundenstimme          → Sand White (warm, Zitat zentriert)
8. Zusammenfassung       → Weiß (hell)
9. Kontakt/CTA           → Weiß + Transition Green Header-Band
```

**Kritische Regel:** Maximal 1–2 Slides pro Deck dürfen Transition Green als Fläche nutzen. Der Rest ist Weiß oder Sand White. Stone Grey erscheint NIE als Slide-Hintergrund.

---

## Gemeinsame Typografie-Regeln

Gelten für **beide** Presets identisch:

### Headlines (Unbounded)

```css
.slide-headline-display {
  font-family: 'Unbounded', system-ui, sans-serif;
  font-weight: 900;
  text-transform: uppercase;
  letter-spacing: -0.04em;
  line-height: 1.0;
}

/* Größen (viewport-basiert für Slides) */
.slide-headline-xl { font-size: clamp(48px, 6vw, 72px); }
.slide-headline-lg { font-size: clamp(36px, 4.5vw, 56px); }
.slide-headline-md { font-size: clamp(28px, 3.5vw, 44px); }
.slide-headline-sm { font-size: clamp(22px, 2.8vw, 36px); }
```

### Body (TT Norms Pro)

```css
.slide-body {
  font-family: 'TT Norms Pro', system-ui, sans-serif;
  font-weight: 400;
  line-height: 1.6;
}

.slide-body-lg { font-size: clamp(16px, 1.5vw, 20px); }
.slide-body-md { font-size: clamp(14px, 1.2vw, 16px); }
.slide-body-sm { font-size: clamp(12px, 1vw, 14px); }
```

### Technische Werte (TT Norms Pro)

```css
.slide-mono {
  font-family: 'TT Norms Pro', monospace;
  font-weight: 500;
  line-height: 1.4;
}

.slide-mono-lg { font-size: clamp(18px, 1.8vw, 24px); }
.slide-mono-md { font-size: clamp(14px, 1.2vw, 16px); }
```

### Labels (TT Norms Pro, fett)

```css
.slide-label {
  font-family: 'TT Norms Pro', system-ui, sans-serif;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  font-size: clamp(10px, 0.9vw, 13px);
}
```

---

## Logo-Verwendung auf Slides

| Slide-Hintergrund | BKM AG Logo | Fachbetrieb Logo |
|-------------------|-------------|------------------|
| Deep Green | `bkm-logo-white-puregreen` oder `bkm-logo-white` | — |
| Transition Green | `bkm-logo-white-puregreen` oder `bkm-logo-white` | `bkm-logo-white` oder `bkm-logo-white-puregreen` |
| Weiß / Sand White | — | `bkm-logo-stonegrey-puregreen` (Standard-Logo für Fachbetrieb) |

**Fachbetrieb-Hinweis:** Da Fachbetrieb-Slides überwiegend helle Hintergründe haben, ist `bkm-logo-stonegrey-puregreen` das Standard-Logo. Nur auf den seltenen Transition-Green-Akzent-Slides wird `bkm-logo-white` oder `bkm-logo-white-puregreen` verwendet.

**Regel:** Das Logo steht immer auf der Titel-Slide und der Schluss-Slide. Auf Inhalts-Slides optional in der Fußzeile (klein, max. 3% der Slide-Höhe).
