# BKM Slides — Style Presets

> Vollständige Farbdefinitionen und Typografie-Regeln für beide BKM-Kontexte im **Editorial/Print-Stil**. Basierend auf der Analyse echter BKM-Broschüren, PDFs und Präsentationen.

---

## Preset 1: BKM AG (Editorial)

**Einsatz:** Corporate-Präsentationen, Produkt-Launches, Investor-Decks, Marketing-Slides, Messe-Präsentationen.

**Atmosphäre:** Autoritativ, schützend, materiell. Deep Green dominiert als Fläche auf Titel- und CTA-Slides. Sand/Beige für Content-Slides. Lime Green ist der einzige Akzent — sparsam, nur für vertikale Linien, Checkmarks, Icons und hervorgehobene Elemente.

### CSS-Variablen

```css
:root {
  /* Flächen — NUR ZWEI TYPEN */
  --slide-bg-dark: #1c4b42;           /* Deep Green — Titel, CTA, Zitate */
  --slide-bg-light: #f5f0eb;          /* Sand/Beige — Content-Slides */
  --slide-bg-card: #ffffff;           /* Weiß — Cards auf Sand-Hintergrund */

  /* Text */
  --slide-text-on-dark: #ffffff;       /* Weiß auf dunklen Flächen */
  --slide-text-on-dark-muted: rgba(255,255,255,0.7);
  --slide-text-on-light: #1a1a1a;     /* Fast-Schwarz auf hellen Flächen */
  --slide-text-on-light-muted: #494949;
  --slide-headline-on-light: #4daf46; /* Pure Green für Headlines auf Sand */

  /* Akzent */
  --slide-accent: #b4e717;            /* Lime — Vertikale Linie, Checkmarks, Icons */
  --slide-accent-line: #b4e717;       /* Lime — Vertikale Akzentlinie auf Titelseiten */

  /* Semantische Grüntöne */
  --slide-green-deep: #1c4b42;
  --slide-green-transition: #287d4b;
  --slide-green-pure: #4daf46;
  --slide-green-lime: #b4e717;

  /* Strukturelemente */
  --slide-card-border: #1c4b42;       /* Deep Green — Standard Card Border-Left */
  --slide-card-border-warning: #dc2626; /* Rot — Warnung Card Border-Left */
  --slide-card-border-highlight: #b4e717; /* Lime — Highlight Card Border-Left */
  --slide-footer-bg: #1c4b42;         /* Deep Green — Footer-Bar */
  --slide-footer-icon: #b4e717;       /* Lime — Footer-Bar Icon */
  --slide-footer-text: #ffffff;       /* Weiß — Footer-Bar Text */

  /* Formen */
  --slide-radius-card: 8px;
  --slide-radius-sm: 4px;

  /* Glasmorphismus (optional) */
  --slide-glass-bg: rgba(255, 255, 255, 0.12);
  --slide-glass-border: rgba(255, 255, 255, 0.15);
  --slide-glass-blur: 16px;
}
```

### Farbkombinationen

| Slide-Typ | Hintergrund | Headline | Body | Akzent-Elemente |
|-----------|-------------|----------|------|-----------------|
| Titel-Slide | Deep Green | Weiß (Unbounded Bold Italic) | Weiß 70% | Vertikale Lime-Linie, Lime Meta-Text |
| Content-Slide | Sand/Beige | Pure Green (Unbounded Bold) | Stone Grey | Cards mit Deep Green Border-Left |
| Daten-Slide | Sand/Beige | Pure Green | Stone Grey | Große Zahlen in Lime oder Pure Green |
| Zitat-Slide | Deep Green | Weiß | Weiß 70% | Lime Anführungszeichen |
| CTA-Slide | Deep Green | Weiß | Weiß 70% | Lime Kontakt-Infos |

### Slide-Rhythmus

```
1. Titel-Slide          → Deep Green + Vertikale Lime-Linie + Logo
2. Agenda/Überblick      → Sand/Beige + Cards mit Border-Left
3. Inhalt 1              → Sand/Beige + Foto (40%+) + Text
4. Inhalt 2              → Deep Green + Weiß Text (Abwechslung)
5. Daten/Zahlen          → Sand/Beige + Große Akzent-Zahlen
6. Inhalt 3              → Sand/Beige + Cards + Footer-Bar
7. Zitat/Testimonial     → Deep Green + Zitat zentriert
8. Zusammenfassung       → Sand/Beige + Checkmarks
9. CTA/Schluss           → Deep Green + Kontakt + Logo
```

Regel: **Nie zwei gleiche Hintergründe hintereinander.** Immer zwischen Deep Green und Sand/Beige alternieren.

### Signatur-Elemente (BKM AG)

1. **Vertikale Lime-Linie** — 4px breit, ~60% der Slide-Höhe, links vom Content-Block auf Titelseiten
2. **Deep Green Footer-Bar** — Volle Breite, 48–60px Höhe, Lime Icon + Weiß Text
3. **Cards mit Border-Left** — Weiß auf Sand, 4px Deep Green links, 8px Radius, kein Shadow
4. **Lime Checkmarks** — ✓ in Lime als visuelle Indikatoren
5. **Keyvisual-Überlappung** — Chevrons am rechten Rand über Fotos (auf Titelseiten)

---

## Preset 2: Fachbetrieb (Editorial)

**Einsatz:** Fachbetrieb-Präsentationen, Kunden-Pitches, Schulungen, Zertifizierungs-Unterlagen, lokale Marketing-Slides.

**Atmosphäre:** Kompetent, bodenständig, lösungsorientiert. Das Design ist bewusst **hell und offen** — Weiß und Sand White dominieren. Transition Green für Headlines und sparsame Akzent-Bänder. Pure Green für dekorative Akzente. Stone Grey ist **nur Textfarbe** — nie Hintergrund.

### CSS-Variablen

```css
:root {
  /* Flächen — HELL DOMINIERT */
  --slide-bg-primary: #ffffff;         /* Weiß — Dominante Hauptfläche */
  --slide-bg-warm: #f5f0eb;           /* Sand/Beige — Alternative Hauptfläche */
  --slide-bg-accent: #287d4b;         /* Transition Green — Sparsam! Max 1–2 Slides */
  --slide-bg-card: #ffffff;           /* Weiß — Cards auf Sand-Hintergrund */

  /* Text */
  --slide-text-primary: #494949;       /* Stone Grey — Primäre Textfarbe */
  --slide-text-headline: #287d4b;      /* Transition Green — Headlines auf hellen Flächen */
  --slide-text-on-accent: #ffffff;     /* Weiß — Text auf Transition Green */
  --slide-text-muted: rgba(73,73,73,0.6);

  /* Akzent */
  --slide-accent: #4daf46;            /* Pure Green — Dekorativer Akzent */
  --slide-accent-readable: #287d4b;   /* Transition Green — Lesbarer Akzent */
  /* KEIN Lime im Fachbetrieb-Kontext */

  /* Strukturelemente */
  --slide-card-border: #287d4b;       /* Transition Green — Standard Card Border-Left */
  --slide-card-border-highlight: #4daf46; /* Pure Green — Highlight Card Border-Left */
  --slide-footer-bg: #287d4b;         /* Transition Green — Footer-Bar */
  --slide-footer-icon: #4daf46;       /* Pure Green — Footer-Bar Icon */
  --slide-footer-text: #ffffff;       /* Weiß — Footer-Bar Text */

  /* Formen */
  --slide-radius-card: 8px;
  --slide-radius-sm: 4px;

  /* Glasmorphismus (optional) */
  --slide-glass-bg: rgba(255, 255, 255, 0.15);
  --slide-glass-border: rgba(255, 255, 255, 0.2);
  --slide-glass-blur: 16px;
}
```

### Farbkombinationen

| Slide-Typ | Hintergrund | Headline | Body | Akzent-Elemente |
|-----------|-------------|----------|------|-----------------|
| Titel-Slide | Weiß | Transition Green (Unbounded Bold) | Stone Grey | Pure Green Divider, Logo |
| Content-Slide | Sand/Beige | Transition Green | Stone Grey | Cards mit Transition Green Border-Left |
| Daten-Slide | Weiß | Transition Green | Stone Grey | Große Zahlen in Transition Green |
| Akzent-Slide | Transition Green (sparsam!) | Weiß | Weiß 70% | Pure Green Icons |
| CTA-Slide | Weiß | Transition Green | Stone Grey | Pure Green CTA-Button |

### Slide-Rhythmus

```
1. Titel-Slide          → Weiß + Logo + Transition Green Headline
2. Agenda/Überblick      → Sand/Beige + Cards
3. Leistung 1            → Weiß + Foto (40%+) + Text
4. Leistung 2            → Sand/Beige + Cards + Footer-Bar
5. Akzent-Slide          → Transition Green (EINZIGE dunkle Slide!)
6. Referenz/Zahlen       → Weiß + Große Zahlen
7. Kundenstimme          → Sand/Beige + Zitat
8. Zusammenfassung       → Weiß + Checkmarks
9. Kontakt/CTA           → Weiß + Kontakt-Infos + Logo
```

**Kritische Regel:** Maximal 1–2 Slides pro Deck dürfen Transition Green als Fläche nutzen. Der Rest ist Weiß oder Sand/Beige. Stone Grey erscheint NIE als Slide-Hintergrund.

---

## Gemeinsame Typografie-Regeln

Gelten für **beide** Presets identisch. Nur 3 typografische Stufen:

### Stufe 1: Headlines (Unbounded Bold 900)

```css
.slide-headline {
  font-family: 'Unbounded', system-ui, sans-serif;
  font-weight: 900;
  letter-spacing: -0.03em;
  line-height: 1.0;
}

/* H1 — UPPERCASE, optional Italic auf Titelseiten */
.slide-headline-h1 {
  font-size: clamp(48px, 6vw, 100px);
  text-transform: uppercase;
}

/* H2 — sentence case */
.slide-headline-h2 {
  font-size: clamp(32px, 4vw, 48px);
  text-transform: none;
}
```

### Stufe 2: Subtitles / Card-Titel (TT Norms Pro Bold 700)

```css
.slide-subtitle {
  font-family: 'TT Norms Pro', system-ui, sans-serif;
  font-weight: 700;
  line-height: 1.3;
  font-size: clamp(16px, 1.5vw, 20px);
}

/* Große Statistik-Zahlen */
.slide-stat-number {
  font-family: 'TT Norms Pro', system-ui, sans-serif;
  font-weight: 700;
  font-size: clamp(48px, 5vw, 96px);
  line-height: 1.0;
}
```

### Stufe 3: Body (TT Norms Pro Regular 400)

```css
.slide-body {
  font-family: 'TT Norms Pro', system-ui, sans-serif;
  font-weight: 400;
  line-height: 1.6;
  font-size: clamp(14px, 1.2vw, 16px);
}

.slide-body-lg {
  font-size: clamp(16px, 1.5vw, 20px);
}

/* Labels */
.slide-label {
  font-family: 'TT Norms Pro', system-ui, sans-serif;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  font-size: clamp(10px, 0.9vw, 13px);
}

/* Footer */
.slide-footer-text {
  font-family: 'TT Norms Pro', system-ui, sans-serif;
  font-weight: 400;
  font-size: clamp(11px, 0.8vw, 13px);
}
```

**Keine Monospace-Schrift.** Technische Werte und Zahlen werden in TT Norms Pro Bold (große Zahlen) oder TT Norms Pro Regular (inline) gesetzt.

---

## Logo-Verwendung auf Slides

| Slide-Hintergrund | BKM AG Logo | Fachbetrieb Logo |
|-------------------|-------------|------------------|
| Deep Green | `bkm-logo-white-puregreen` oder `bkm-logo-white` | — |
| Transition Green | `bkm-logo-white-puregreen` oder `bkm-logo-white` | `bkm-logo-white` oder `bkm-logo-white-puregreen` |
| Weiß / Sand/Beige | — | `bkm-logo-stonegrey-puregreen` (Standard) |

**Fachbetrieb-Hinweis:** Da Fachbetrieb-Slides überwiegend helle Hintergründe haben, ist `bkm-logo-stonegrey-puregreen` das Standard-Logo. Nur auf den seltenen Transition-Green-Akzent-Slides wird `bkm-logo-white` oder `bkm-logo-white-puregreen` verwendet.

**Regel:** Das Logo steht immer auf der Titel-Slide und der Schluss-Slide. Auf Inhalts-Slides optional in der Footer-Bar (klein, max. 3% der Slide-Höhe).
