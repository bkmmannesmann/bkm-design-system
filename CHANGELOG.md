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
- **`skills/bkm-technical-drawings`** — neues Technical Drawing System für originale BKM-Prinzipzeichnungen als HTML + Inline-SVG. Enthält eine Vier-Grün-Systematik, semantische Layer, A4/A3-Vorlagen, Metadaten, Standards-Registry, strukturellen Validator und 18 schematische Referenzzeichnungen für Außen-/Innenabdichtung, Fugen, Durchdringungen, Bodenanschlüsse und Prüfdetails. Die Beispiele bleiben `DRAFT`, `NOT_TO_SCALE` und `NORMATIVE_VERIFICATION_REQUIRED`; sie ersetzen keine Fach- oder Normenprüfung.
- **Technical Drawings – Referenzangleichung** — Linien-, Schraffur-, Systemband-, Achs-/Verdeckt-, Komponentenlisten- und Detailbezuglogik anhand einer visuellen Analyse der intern bereitgestellten WTA- und BKM-Referenzen überarbeitet. Die BKM-Dateien bleiben eigenständig; es wurden keine Referenzgrafiken, Originalmaße, -texte oder -layouts übernommen.
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
