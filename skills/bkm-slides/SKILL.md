# BKM Slides — Skill

> Generiert visuell ansprechende, brand-konforme HTML-Präsentationen im BKM Mannesmann Design System. Jede Slide ist eine einzelne HTML-Datei ohne externe Abhängigkeiten. Das Design folgt dem **Corporate Editorial**-Ansatz (Magazin/Jahresbericht), NICHT dem Web-Design-Ansatz.

## Wann diesen Skill verwenden

- Wenn Slides, Präsentationen oder Pitch-Decks im BKM-Stil erstellt werden sollen
- Wenn Broschüren-Layouts oder Print-nahe HTML-Dateien benötigt werden
- Wenn Slides für BKM AG oder Fachbetrieb-Kontexte erstellt werden sollen

## Workflow

### 1. Kontext bestimmen

Vor dem Erstellen einer Slide: Welcher Farbkontext?

| Kontext | Wann | Dominante Fläche | Akzent | Headlines auf hell |
|---------|------|------------------|--------|-------------------|
| **BKM AG** | Corporate, Produkte, Shop, Marketing, Investor | Deep Green (#1c4b42) | Lime (#b4e717) | Deep Green oder Schwarz |
| **Fachbetrieb** | Fachbetrieb-Seiten, Partner, Zertifizierung, Kunden-Pitches | Weiß / Sand White | Pure Green (#4daf46) | Transition Green (#287d4b) |

### 2. Style Preset laden

Lies die Datei `STYLE_PRESETS.md` in diesem Ordner für die vollständigen Farbdefinitionen, Typografie-Regeln und CSS-Variablen des gewählten Kontexts.

### 3. HTML-Template laden

Lies die Datei `html-template.md` in diesem Ordner für die HTML-Architektur. Jede Slide ist eine einzelne HTML-Datei mit:

- Viewport-basiertem CSS (vw/vh Einheiten für responsive Skalierung)
- Google Fonts CDN für Unbounded
- Selbst-gehostete TT Norms Pro (WOFF2 aus `assets/fonts/`)
- BKM-Farbvariablen als CSS Custom Properties
- Keine externen Abhängigkeiten

### 4. Animation Patterns laden (optional)

Lies die Datei `animation-patterns.md` für CSS-only Animationen. **Achtung:** Nur subtile Entrance-Animationen (fadeIn, slideIn) sind für Editorial-Slides geeignet. Noise-Shimmer und Aurora-Animationen sind NICHT für Slides geeignet.

## Kritische Regeln — Editorial Design

Diese Regeln basieren auf der Analyse echter BKM-Broschüren, PDFs und Präsentationen:

### Was BKM-Slides SIND:

1. **Corporate Editorial** — Magazin-Ästhetik, nicht Web-Design
2. **Fotografie-dominant** — Mindestens 40% der Fläche ist Bild/Foto
3. **Großzügiger Weißraum** — Mindestens 25% der Fläche bleibt leer
4. **Saubere, flache Flächen** — Kein Noise, kein Aurora, keine animierten Hintergründe
5. **Nur 2 Hintergrund-Typen:** Deep Green ODER Sand/Beige — kein dritter Typ
6. **Asymmetrische, editorial Layouts** — Nicht symmetrische Dashboard-Grids
7. **Vertikale Lime-Linie** auf BKM AG Titelseiten (4px breit, ~60% Höhe)
8. **Deep Green Footer-Bar** auf Content-Slides (volle Breite, Lime Icon + Weiß Text)
9. **Cards mit farbiger Border-Left** (4px solid) statt Shadow
10. **Glasmorphismus** erlaubt als optionales Overlay auf Foto-Hintergründen

### Was BKM-Slides NICHT sind:

- ❌ Noise-Texturen (SVG fractal noise)
- ❌ Aurora-Gradients (animierte Farbverläufe)
- ❌ Bento-Grids (gleichförmige Kachel-Layouts)
- ❌ Floating Badges (absolut positionierte Labels)
- ❌ Spotlight/Glow-Effekte
- ❌ Animierte Text-Effekte
- ❌ Dashboard-artige symmetrische Grids
- ❌ Mehrere Card-Shadows die um Aufmerksamkeit konkurrieren
- ❌ Box-Shadows auf Cards (nur colored border-left)

### Typografie (nur 3 Stufen):

| Stufe | Schrift | Einsatz |
|-------|---------|---------|
| **Headline** | Unbounded Bold 900 (teilweise Italic) | H1 UPPERCASE, H2+ sentence case |
| **Subtitle/Card-Titel** | TT Norms Pro Bold 700 | Subheadlines, Card-Titel, hervorgehobene Infos |
| **Body** | TT Norms Pro Regular 400 | Fließtext, Beschreibungen, technische Werte |

Keine Monospace-Schrift. Keine dritte Schriftfamilie. Zahlen in Unbounded Bold oder TT Norms Pro Bold.

### Card-Design (Editorial):

```css
.card-editorial {
  background: #ffffff;
  border-left: 4px solid #1c4b42; /* oder #dc2626 für Warnung, #b4e717 für Highlight */
  border-radius: 8px;
  padding: 24px;
  /* KEIN box-shadow */
}
```

### Footer-Bar:

```css
.footer-bar {
  background: #1c4b42;
  padding: 16px 80px;
  display: flex;
  align-items: center;
  gap: 12px;
  width: 100%;
  position: absolute;
  bottom: 0;
}
```

## Dateistruktur

```
skills/bkm-slides/
├── SKILL.md                  ← Diese Datei (Einstieg)
├── STYLE_PRESETS.md          ← BKM AG + Fachbetrieb Farbdefinitionen
├── html-template.md          ← HTML-Architektur für Slides
├── animation-patterns.md     ← CSS-only Animationen (nur subtile Entrance-Effekte)
└── PATTERN_CATALOG.md        ← Erlaubte und verbotene Patterns
```
