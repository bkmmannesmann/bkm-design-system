# Changelog

Alle wesentlichen Änderungen am BKM Mannesmann Design System werden hier dokumentiert.

## [Unveröffentlicht]

### Geändert
- **`skills/bkm-slides` auf v5 (familien-basiert) umgestellt.** Statt fünf starrer
  Copy-Paste-Templates jetzt vier Stil-Familien (`bkm-glass-ag`, `bkm-glass-fachbetrieb`,
  `bkm-editorial`, `bkm-bold-poster`) auf gemeinsamer **Fixed-Stage-Engine** (1920×1080,
  skaliert), mit „Show don't tell"-Auswahl (`selection-index.json`, `style-discovery.html`).
- Neue `ENGINE.md` (Engine-Shell) und je Familie `preview.md`/`design.md`/`demo.html`.
- Headline-Casing: UPPERCASE **oder** Mixed-Case erlaubt (nie kursiv); 8px-Rundung für
  Flächen-Elemente; Fachbetrieb-Text in Transition Green.
- v4-System (5 Templates) nach `skills/bkm-slides/legacy/` archiviert.

### Hinzugefügt
- **Icon-Manifest um 41 Phosphor-Icons erweitert** (Bold; `circle`/`circle-half`/`diamond` zusätzlich als Fill für Statuspunkte), alle byteidentisch aus `@phosphor-icons/core@2.0.8`, mit Einsatzzweck im Manifest. Anlass: Design Stufe 3 des Support-Cockpits ersetzt Schriftzeichen- und handgezeichnete Icons durch das Manifest (Regel 11 `skills/bkm-app`).
- **Fester TDS-Abschnittsiconsatz.** Neun rendererfeste, nach Inhaltsblock benannte Phosphor-Bold-Dateien unter `assets/icons/tds/` mit Manifest, Quell- und Rendererprüfsummen. Die zusätzliche Lime-Füllung verhindert schwarze SVG-Glyphen in WeasyPrint-PDFs. Der Satz bleibt als freigegebene TDS-Version gepinnt und wird nicht durch abweichende allgemeine Phosphor-Assets ersetzt.
- Aus Open-Design-Analyse (Apache-2.0) übernommen: `skills/bkm-slides/checklist.md`
  (P0/P1/P2 + 5-Dim-Selbstkritik), Anti-Slop-**Positivregeln** in `PATTERN_CATALOG.md`,
  Engine-Härtung in `ENGINE.md` (Capture-Keydown, Autofokus, localStorage-Position),
  Turn-1-Kurzbrief in `SKILL.md`. Ideen-Sammlung: `docs/inspiration-open-design.md`.
- `skills/bkm-slides/tokens.css` — kanonische Design-Tokens (Single Source of Truth)
  und `components.html` — gerendertes Komponenten-Schaufenster. Erstes vollständiges
  v5-Beispiel-Deck `examples/bkm-ag-pitch.html`.

## [1.0.0] - 2026-05-11

### Hinzugefügt
- Initiale Veröffentlichung des Design Systems
- `DESIGN.md` mit maschinenlesbaren Tokens (Farben, Typografie, Spacing, Komponenten)
- Dokumentation für digitale Medien (`docs/digitale-medien.md`)
- Dokumentation für Print-Anwendungen (`docs/print-anwendungen.md`)
- Dokumentation für MicroPorex und Technik (`docs/microporex-und-technik.md`)
- README mit Nutzungshinweisen für AI-Agenten
- CONTRIBUTING-Richtlinien
