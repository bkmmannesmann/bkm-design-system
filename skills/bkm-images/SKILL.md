# BKM Images — Skill

> Generiert **brand-konforme Bilder** im BKM Mannesmann Design System über die
> OpenAI Image-API (`gpt-image-1`, "OpenAI Images 2.0"). Output: editorial
> Fotografien und Hintergründe in der BKM-Bildsprache — gedämpfte Erdtöne,
> dramatisches natürliches Licht, grüne Akzente, kein Text, keine Logos im Bild.

---

## WICHTIGSTE REGEL

> **DIE BILDSPRACHE IST EDITORIAL, NICHT STOCK.** Jedes Bild folgt der
> BKM-Fotografie-Doktrin aus `DESIGN.md` (Abschnitt *Photography Rules*):
> echte, emotionale Motive (Architektur, Bau/Sanierung, Labor/Technik,
> Nachhaltigkeit, Business), gedämpfte Erdtöne mit grünen Akzenten, großzügiger
> Negativraum. **Niemals** Text, Wörter, Logos, Wasserzeichen oder UI-Elemente
> ins Bild generieren — Logo, Keyvisual und Typografie werden später als
> Overlay platziert (siehe `bkm-slides`, `bkm-social`).

---

## Wann diesen Skill verwenden

- Wenn Bild-**Hintergründe für Slides** (16:9) gebraucht werden → speist den
  `bkm-slides`-Workflow (Schritt 4: "Hintergrund-Fotos generieren").
- Wenn **Social-Media-Bilder** (1:1, 4:5, 9:16) erzeugt werden sollen → speist
  `bkm-social`.
- Wenn **Hero-/Section-Bilder für Websites** (16:9 / landscape) gebraucht werden
  → speist `bkm-website`.
- Wenn **Produkt- oder Architektur-Inszenierungen** im BKM-Stil benötigt werden.

---

## Voraussetzungen

| Was | Wert |
|-----|------|
| Modell | `gpt-image-1` (OpenAI Images) |
| Env-Variable | `OPENAI_API_KEY` (Pflicht) |
| Laufzeit | Node.js ≥ 18 (nutzt global `fetch`, **keine** npm-Dependencies) |
| API-Endpoint | `POST https://api.openai.com/v1/images/generations` |

```bash
export OPENAI_API_KEY="sk-..."
```

---

## PFLICHT-WORKFLOW

### Schritt 1: Kontext bestimmen

| Kontext | Wann | Farbstimmung im Bild |
|---------|------|----------------------|
| **BKM AG** (`ag`) | Corporate, Produkte, Marketing, Investor | Deep-Green-Dominanz (`#1c4b42`), gedämpfte Erdtöne, sparsamer **Lime-Akzent** (`#b4e717`) als einzelnes Licht-/Material-Highlight |
| **Fachbetrieb** (`fachbetrieb`) | Fachbetrieb-Seiten, Partner, Kunden-Pitches | Helle, sandfarbene Stimmung (`#f6f5f2`), **Pure-Green-Akzent** (`#4daf46`), Tageslicht. **Kein Lime.** |

> **Kritisch:** Lime Green (`#b4e717`) erscheint **niemals** im Fachbetrieb-Kontext.

### Schritt 2: Use Case + Format bestimmen

| Use Case | Flag | Default-Größe | Seitenverhältnis |
|----------|------|---------------|------------------|
| Slide-Hintergrund | `slide` | `1536x1024` | 3:2 (nächstes zu 16:9) |
| Website / Hero | `website` | `1536x1024` | landscape |
| Social Feed | `social` | `1024x1024` | 1:1 |
| Social Story | `social --ratio story` | `1024x1536` | Portrait (für 9:16) |
| Produkt / Architektur | `product` | `1024x1024` | 1:1 |

> `gpt-image-1` unterstützt nur `1024x1024`, `1536x1024`, `1024x1536`, `auto`.
> Echtes 16:9 / 9:16 wird durch leichten Beschnitt im Layout erreicht — der Skill
> reserviert dafür im Prompt **Negativraum oben/rechts**.

### Schritt 3: Motiv wählen

Erlaubte Motiv-Felder (aus der BKM-Fotografie-Doktrin):

- **Architektur** — Keller, Fundamente, Fassaden, Betonwände, Mauerwerk
- **Bau / Sanierung** — Baustellen, Werkzeuge, Materialien, Vorher/Nachher
- **Labor / Technik** — Materialprüfung, Mikroskop, Proben, Injektionstechnik
- **Nachhaltigkeit** — grüne Gebäude, Natur, moderne nachhaltige Architektur
- **Business** — Handshake, Tablet/Software, Teamwork, Beratung

### Schritt 4: Generieren

Nutze das Skript `generate.mjs` (baut automatisch den brand-konformen Prompt aus
`PROMPT_LIBRARY.md`):

```bash
node skills/bkm-images/generate.mjs \
  --usecase slide \
  --context ag \
  --motif "concrete basement wall with a horizontal moisture barrier line" \
  --count 1 \
  --out ./skills/bkm-images/output
```

Mehrere Bilder im Batch (z. B. ein Foto pro Slide):

```bash
node skills/bkm-images/generate.mjs --usecase slide --context fachbetrieb \
  --motif "renovated facade in daylight" --motif "laboratory sample testing" \
  --motif "construction team reviewing a tablet on site"
```

Der `--dry-run`-Modus gibt nur den finalen Prompt aus, ohne die API zu rufen
(zum Prüfen / für manuelle Nutzung in ChatGPT / DALL·E-UI):

```bash
node skills/bkm-images/generate.mjs --usecase social --context ag \
  --motif "drop of water on a treated mineral surface, macro" --dry-run
```

### Schritt 5: Einbinden + Overlay

1. Bild aus `output/` in das Ziel-Layout einbinden (`bkm-slides`, `bkm-social`,
   `bkm-website`).
2. **Overlay** gemäß Kontext darüberlegen (Deep Green rgba / Sand rgba) — siehe
   `skills/bkm-slides/STYLE_PRESETS.md`.
3. Logo + Keyvisual als separate Assets platzieren (rechter Rand, angeschnitten).
   **Nicht** ins generierte Bild brennen.

### Schritt 6: Qualitätskontrolle

- [ ] Kein Text / keine Wörter / keine Logos / kein Wasserzeichen im Bild?
- [ ] Gedämpfte Erdtöne, korrekte Kontext-Stimmung (AG dunkel / Fachbetrieb hell)?
- [ ] Lime-Akzent **nur** im AG-Kontext, sparsam?
- [ ] Negativraum vorhanden (für Glass-Card + Keyvisual rechts)?
- [ ] Editorial-Qualität, kein generisches Stock-Foto-Gefühl?
- [ ] Keine verbotenen Web-Patterns (Aurora-Gradient, Noise, Bento) als Bildmotiv?

---

## Brand-Bildsprache (Zusammenfassung)

**SO SIND BKM-Bilder:**
- Editorial, dokumentarisch, emotional — echte Räume, Materialien, Menschen
- Dramatisches **natürliches Licht**, hoher Kontrast, Medium-Format-Anmutung
- **Gedämpfte Erdtöne** mit grünen Akzenten (siehe Farbsemantik unten)
- Großzügiger Negativraum für Overlay + Keyvisual
- Materialität: Beton, Mauerwerk, Mineral, Wasser/Feuchtigkeit, Grün/Natur

**SO SIND BKM-Bilder NICHT (VERBOTEN):**
- ❌ Text, Wörter, Buchstaben, Zahlen im Bild
- ❌ Logos, Marken, Wasserzeichen, UI-/Browser-Chrome
- ❌ Generische, glatte Corporate-Stock-Fotos
- ❌ Aurora-Gradients, Noise-Texturen, Neon, 3D-Render-Look, Cartoon/Illustration
- ❌ Übersättigte Farben, HDR-Überzeichnung
- ❌ Lime Green im Fachbetrieb-Kontext

## Farbsemantik der Bildstimmung

| Farbe | Hex | Bedeutung | Bild-Einsatz |
|-------|-----|-----------|--------------|
| Deep Green | `#1c4b42` | Feuchtigkeit / Problem | Dominante Tonalität im AG-Kontext |
| Transition Green | `#287d4b` | Trocknung / Prozess | Übergänge, Vegetation |
| Pure Green | `#4daf46` | Trockene Lösung | Akzent im Fachbetrieb-Kontext |
| Lime Green | `#b4e717` | Effekt-Highlight | **Nur AG**, sparsam (Lichtkante, einzelnes Detail) |
| Sand White | `#f6f5f2` | Warme Basis | Helle, dokumentarische Stimmung (Fachbetrieb) |
| Stone Grey | `#494949` | Neutral / Text | Schatten, Beton, neutrale Materialität |

---

## Dateistruktur

```
skills/bkm-images/
├── SKILL.md            ← Diese Datei (Einstieg + Pflicht-Workflow)
├── PROMPT_LIBRARY.md   ← Brand-Prompt-Bausteine pro Use Case + Kontext
├── generate.mjs        ← Lauffähiges CLI (Node ≥ 18, kein npm install nötig)
└── output/             ← Generierte Bilder (gitignored)
```

## Abhängigkeiten

- Liest die Bildsprache aus `../../DESIGN.md` (*Photography Rules*) und den
  Farbkontext aus den Token-Definitionen.
- Speist die Skills `bkm-slides` (Hintergründe), `bkm-social` (Post-Bilder) und
  `bkm-website` (Hero-Bilder).
