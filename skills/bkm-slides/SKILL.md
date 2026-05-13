# BKM Slides — Skill

> Generiert visuell ansprechende, brand-konforme HTML-Präsentationen im BKM Mannesmann Design System. Jede Slide ist eine einzelne HTML-Datei ohne externe Abhängigkeiten.

## Wann diesen Skill verwenden

- Wenn Slides, Präsentationen oder Pitch-Decks im BKM-Stil erstellt werden sollen
- Wenn visuell ansprechende ("vibe-coded") Slides benötigt werden, die trotzdem brand-konform sind
- Wenn Slides für BKM AG oder Fachbetrieb-Kontexte erstellt werden sollen

## Workflow

### 1. Kontext bestimmen

Vor dem Erstellen einer Slide: Welcher Farbkontext?

| Kontext | Wann | Farben |
|---------|------|--------|
| **BKM AG** | Corporate, Produkte, Shop, Marketing, Investor | Deep Green + Lime + Weiß |
| **Fachbetrieb** | Fachbetrieb-Seiten, Partner, Zertifizierung | Stone Grey + Pure Green + Weiß |

### 2. Style Preset laden

Lies die Datei `STYLE_PRESETS.md` in diesem Ordner für die vollständigen Farbdefinitionen, Typografie-Regeln und CSS-Variablen des gewählten Kontexts.

### 3. HTML-Template laden

Lies die Datei `html-template.md` in diesem Ordner für die HTML-Architektur. Jede Slide ist eine einzelne HTML-Datei mit:

- Viewport-basiertem CSS (vw/vh Einheiten für responsive Skalierung)
- Eingebetteten Google Fonts (Unbounded, Inter, Geist Mono)
- BKM-Farbvariablen als CSS Custom Properties
- Keine externen Abhängigkeiten

### 4. Animation Patterns laden (optional)

Lies die Datei `animation-patterns.md` für CSS-only Animationen, die in Slides verwendet werden können. Alle Animationen sind performant und funktionieren ohne JavaScript.

### 5. Pattern-Katalog konsultieren (optional)

Lies `PATTERN_CATALOG.md` für eine Übersicht, welche Patterns aus der `patterns/` Bibliothek in Slides adaptiert werden können (als statische CSS-Versionen ohne React/Framer Motion).

## Kritische Regeln (aus DESIGN.md)

1. **Keyvisual ist ein vorgerendertes Bild** — Nie in Code nachbauen.
2. **Lime Green nur im BKM AG Kontext** — Nie im Fachbetrieb.
3. **Unbounded: weight 900, uppercase, min. 18px** — Keine Ausnahmen.
4. **Harte Schnitte zwischen Flächen** — Keine Gradients, Wellen oder Diagonalen als Übergang.
5. **Shadow-as-Border** — Keine CSS `border` auf Cards.
6. **Max. 1 Primary Button pro Viewport** — Auch auf Slides.
7. **Technische Werte in Geist Mono** — Preise, Maße, Prozente.
8. **Pure Green nie als Text auf hellem Hintergrund** — Kontrast nur 2.79.

## Dateistruktur

```
skills/bkm-slides/
├── SKILL.md                  ← Diese Datei (Einstieg)
├── STYLE_PRESETS.md          ← BKM AG + Fachbetrieb Farbdefinitionen
├── html-template.md          ← HTML-Architektur für Slides
├── animation-patterns.md     ← CSS-only Animationen
└── PATTERN_CATALOG.md        ← Welche patterns/ in Slides nutzbar
```
