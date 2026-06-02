# BKM Slides — Skill (v5)

> Generiert visuell ansprechende, marken­konforme HTML-Präsentationen im BKM Mannesmann
> Design System. v5 ist **familien-basiert**: statt fünf starrer Templates wählst du
> (oder der Nutzer per „Show don't tell") aus **vier Stil-Familien** und baust das Deck
> auf einer gemeinsamen **Fixed-Stage-Engine**.

---

## Wann diesen Skill verwenden

- Slides, Präsentationen, Pitch-Decks, Showrooms im BKM-Stil
- Für **BKM AG** (corporate/dunkel) oder **Fachbetrieb** (nahbar/hell)
- Lese-Decks (dicht) ebenso wie Vortrags-Decks (plakativ)

---

## Source of Truth (zuerst lesen, wenn unklar)

| Datei | Inhalt |
|-------|--------|
| `../../DESIGN.md`, `../../AGENTS.md` | Verbindliche Marken-Token & -Regeln (Repo-Wurzel) |
| `ENGINE.md` | Fixed-Stage-Engine (Shell-CSS/JS, 1:1 kopieren) |
| `tokens.css` | **Kanonische Design-Tokens** (CSS-Variablen, Single Source of Truth) |
| `components.html` | Gerendertes Komponenten-Schaufenster (lebende Referenz) |
| `selection-index.json` | Kompakter Index aller Familien (Metadaten für die Auswahl) |
| `templates/<slug>/preview.md` | Leichte Stilkarte je Familie (für Titel-Vorschau) |
| `templates/<slug>/design.md` | **Vollständiges Design-Rezept** je Familie (vor dem Bau lesen) |
| `templates/<slug>/demo.html` | Golden-Reference-Deck der Familie |
| `STYLE_PRESETS.md` | Exakte CSS-Token (Referenz, v3) |
| `PATTERN_CATALOG.md` | Erlaubte vs. verbotene Patterns (Anti-Slop) |
| `SLIDE_TYPES.md` | **Folientyp-Taxonomie** (Rollen-Folien + Inhalts-Bausteine, Plan/Spec) |
| `QUICKSTART.md` | Verlässlicher Weg zu stimmigen Decks (Claude Code, Claude.ai, Manus) |
| `style-discovery.html` | Visuelle Auswahl-Galerie (4 Familien nebeneinander) |

---

## Die vier Familien

| Familie (`slug`) | Track | Look | Kontext |
|------------------|-------|------|---------|
| **`bkm-glass-ag`** | Standard | Glasmorphismus auf Deep Green, Lime-Signal | BKM AG |
| **`bkm-glass-fachbetrieb`** | Standard | helles Milchglas auf Sand, Pure/Transition Green, **kein Lime** | Fachbetrieb |
| **`bkm-editorial`** | Kreativ | flaches Ink, 4px-Linien-Regelwerk, Inverse-Kacheln (hell **und** dunkel) | beide |
| **`bkm-bold-poster`** | Kreativ | übergroße Statements auf Deep Green, Lime-Signal | BKM AG |

**Zwei Tracks:**
- **Standard** = Marken-Lock (sicherer Default für Kunden/Produkt/Print-nahe Decks).
- **Kreativ** = mehr Layout-Freiheit für intern/Pitch/Vision — **trotzdem ausschließlich
  BKM-Farben & Unbounded**.

---

## Workflow (in dieser Reihenfolge)

### 1 · Kurz-Brief einholen (Turn 1, **vor** dem Bauen)
Bevor ein Pixel entsteht: **ein** kompaktes Frageformular (≤ 7 Fragen), dann stoppen und
Antwort abwarten. Bereits Beantwortetes weglassen. Standard-Fragen:

1. **Zweck/Anlass?** (Pitch, Kundentermin, Investor, Messe, internes Update …)
2. **Kontext?** BKM AG (corporate) ODER Fachbetrieb (nahbar)
3. **Track?** Standard (Marken-Lock) ODER Kreativ
4. **Folienzahl?** (ungefähr)
5. **Dichte?** Vortrag (wenig Text, groß) ODER Lesen (strukturierte Grids)
6. **Speaker Notes?** ja/nein
7. **Inhalt/Quelle?** (Stichpunkte, Dokument, Thema)

> Ausnahme: Wenn der Nutzer „einfach bauen / keine Fragen" sagt, mit sinnvollen Defaults
> (BKM AG · Standard · Vortragsdichte) starten.

### 2 · Kandidaten finden — `selection-index.json` lesen
**Nur den Index** lesen und anhand der Metadaten (track, context, mood, best_for) 1–3
passende Familien eingrenzen. **Nie alle `design.md` gleichzeitig laden.**

### 3 · Stil wählen — „Show don't tell"
Für die engere Auswahl die `preview.md` lesen. Wenn ein Mensch entscheidet: die
`style-discovery.html` zeigen (Galerie der 4 Familien). Faustregel des Vorschlags:
1× sicher (Standard) + 1–2× Kreativ, je nach Anlass.

### 4 · Genau **eine** `design.md` lesen
Nach der Wahl das vollständige Rezept **der gewählten Familie** lesen — erst jetzt, nicht früher.

### 5 · Deck bauen
1. **Engine-Shell aus `ENGINE.md`** kopieren (deck-viewport / deck-stage / Deck-JS / Print-CSS).
2. `:root`-Token & Slide-Stile **aus der `design.md`** der Familie übernehmen.
3. Folien-Typen der Familie nutzen (jede `design.md` listet ihre Slide-Typen).
4. Inhalte einsetzen; Dichte-Modus bewusst wählen.
5. Logo/Keyvisual **per Pfad** referenzieren (siehe Tabelle in `ENGINE.md`).

### 6 · Self-Check + Selbstkritik (PFLICHT)
1. **`checklist.md` durchgehen** (Screenshot ansehen!). **Jedes P0 muss bestehen** —
   sonst nicht ausliefern, sondern korrigieren. P1 stark empfohlen.
2. **5-Dimensionen-Selbstkritik** (Marke · Hierarchie · Ausführung · Spezifität · Zurückhaltung),
   je 1–5. Alles < 3/5 nachbessern und neu bewerten. Zwei Durchläufe sind normal.

Erst wenn P0 vollständig grün **und** alle Kritik-Dimensionen ≥ 3/5 sind: ausliefern.

---

## Nicht verhandelbar (Marken-Leitplanken)

1. **Nur BKM-Farben** aus `DESIGN.md` — keine fremden Akzentfarben.
   Deep Green `#1c4b42` · Lime `#b4e717` · Pure Green `#4daf46` · Transition Green `#287d4b`
   · Sand/Paper `#f6f5f2`/`#f5f0eb` · Stone Grey `#494949`.
2. **Headlines Unbounded 900** — UPPERCASE (Standard) **oder** Mixed-Case erlaubt;
   **nie kursiv**, keine Fremd-Akzentschrift. Akzentwörter über **Farbe** (Lime/Pure/Transition Green).
3. **Lime nur als Signal** (Akzentwort, Zahl, Mark, Button, ein Highlight-Block) —
   nie als dekorative Vollfläche. **Lime erscheint nie im Fachbetrieb-Kontext.**
4. **Fachbetrieb-Text = Transition Green** (Deep Green dort nur für Flächen/Button).
5. **Fixed-Stage 1920×1080**, als Ganzes skaliert (`ENGINE.md`).
6. **8px-Rundung** für Flächen-Elemente (Tags, Kacheln, Karten, Buttons); Balken oben
   gerundet; Linien bleiben Linien. (Glas-Cards größer: 24px.)
7. **Logo** nie umfärben/verzerren (`../../docs/logo.md`).

---

## Dateistruktur

```
skills/bkm-slides/
├── SKILL.md                ← diese Datei (Einstieg + Workflow)
├── ENGINE.md               ← Fixed-Stage-Engine (Shell, PFLICHT-Basis)
├── tokens.css              ← kanonische Design-Tokens (Single Source of Truth)
├── components.html         ← gerendertes Komponenten-Schaufenster
├── selection-index.json    ← Familien-Index (Auswahl-Metadaten)
├── style-discovery.html    ← visuelle Auswahl-Galerie (4 Familien)
├── templates/
│   ├── bkm-glass-ag/        {preview.md, design.md, demo.html}
│   ├── bkm-glass-fachbetrieb/ {preview.md, design.md, demo.html}
│   ├── bkm-editorial/       {preview.md, design.md, demo.html, demo-dark.html}
│   └── bkm-bold-poster/     {preview.md, design.md, demo.html}
├── checklist.md            ← P0/P1/P2 Self-Check + 5-Dim-Selbstkritik (PFLICHT)
├── STYLE_PRESETS.md        ← exakte CSS-Token (Referenz)
├── PATTERN_CATALOG.md      ← Anti-Slop (verboten + Positiv-Regeln)
├── animation-patterns.md   ← Reveal-/Animations-Referenz
├── assets/                 ← Hintergrund-Asset(s)
└── legacy/                 ← v4-System (5-Templates) — abgelöst, nur Referenz
```

---

## Zusammenfassung für Agents

```
1. Kurz-Brief per Frageformular einholen (≤7 Fragen), dann bauen
2. selection-index.json lesen → 1–3 Familien eingrenzen (nur Metadaten)
3. preview.md der Finalisten lesen → Stil wählen (Mensch: style-discovery.html zeigen)
4. GENAU EINE design.md der gewählten Familie lesen
5. Engine-Shell aus ENGINE.md kopieren → Folien im Familien-Stil bauen
6. Logo/Keyvisual per Pfad; Marken-Leitplanken einhalten
7. checklist.md (P0 muss grün) + 5-Dim-Selbstkritik → erst dann ausliefern
```

> **Hinweis:** Das alte v4-System (fünf Copy-Paste-Templates, „kopieren, nicht
> interpretieren") liegt in `legacy/` und ist durch die Familien abgelöst. Token- und
> Anti-Slop-Wissen (`STYLE_PRESETS.md`, `PATTERN_CATALOG.md`) bleibt gültig.
