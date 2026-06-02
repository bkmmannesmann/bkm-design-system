# BKM Slides — Slide-Type-Library (Plan / Spec)

> **Status:** Planungsdokument. Definiert die verbindliche Folientyp-Taxonomie als Bauauftrag.
> Implementierung erfolgt phasenweise (siehe unten) — **in die Familie-`demo.html`**, damit
> jeder Typ Engine, eingebettete Assets, texturierte Hintergründe, Casing & Motion automatisch erbt.

## Prinzip

> **Galerie:** `templates/bkm-glass-ag/type-gallery.png` zeigt alle 14 Typen gerendert.

- Jeder Typ = ein `<section class="slide s-<name>">`-Archetyp im `demo.html` der Familie.
- Kanonische Klassennamen (unten) sind ein **Vertrag** — Decks und KI-Tools referenzieren sie.
- Bausteine sind **frei kombinierbar**, keine Pflichtreihenfolge. Hybrid-Casing & bg-Rotation
  (`t1…t4`) gelten überall (siehe `PATTERN_CATALOG.md` 13–14).
- Status-Legende: ✅ in `bkm-glass-ag/demo.html` · 🔶 existiert in einem Deck (zu formalisieren) · ⬜ neu (Lücke).
- **Zeilen-Zebra:** Auflistungen & Tabellen alternieren pro Zeile in leichter Nuance White ↔ Sand-White
  (`rgba(255,255,255,.035)` / `rgba(245,240,235,.05)`) — gilt für `s-table`, `s-agenda`, `s-process`.

---

## Ebene A · Rollen-Folien (Gerüst eines Decks)

### A1 · Deckblatt — `.s-cover` ✅
- **Zweck:** Einstieg. **Slots:** Eyebrow, Headline, Lead, Meta (Datum/Ort/…), optional Button, Keyvisual.
- **Layout:** Glas-Card links, Keyvisual rechts (nur hier!). **Casing:** UPPERCASE. **bg:** t1.

### A2 · Agenda / Inhalt — `.s-agenda` ✅
- **Zweck:** Programm/Überblick. **Slots:** Eyebrow, Headline, 3–6 Zeilen (Zeit · Thema · Sprecher/No),
  optional Status-Card („39 Fachbetriebe").
- **Layout:** Glas-Panel, ggf. 2-spaltig mit Status-Card. **Casing:** Mixed. **bg:** t2.

### A3 · Kapitel-Trenner — `.s-chapter` ✅
- **Zweck:** neues Kapitel. **Slots:** große Geister-Nummer (01/02), Eyebrow, kurze Headline.
- **Layout:** links, große Nummer hinterlegt. **Casing:** UPPERCASE. **bg:** t4/t3.

### A4 · Unterthema-Header — `.s-subhead` ✅
- **Zweck:** Section innerhalb eines Kapitels. **Slots:** Eyebrow, Headline, optional Subline.
- **Layout:** zentriert oder links oben. **Casing:** Mixed. **bg:** rotierend.

### A5 · Abschluss / CTA / Kontakt — `.s-closing` ✅
- **Zweck:** Wrap-Up, Handlungsaufruf, Kontakt. **Slots:** Icon, Headline, Subline, Fließtext,
  optional Prozess-Flow oder Checkliste, Footer (Kontakt/Termin).
- **Layout:** zentriertes Glas-Panel. **Casing:** Mixed. **bg:** t1.

---

## Ebene B · Inhalts-Bausteine

### B6 · Großes Zitat — `.s-quote` ✅
- **Zweck:** Testimonial/Kernaussage. **Slots:** Eyebrow, Blockquote (Akzentwort Lime), Quelle (Name · Rolle · Ort).
- **Layout:** großes „"-Zeichen (transition-green, niedrige Opacity) hinter dem Zitat, Quelle mit Lime-Strich.
- **Casing:** Mixed (Zitat in Satzform). **bg:** t3.

### B7 · Statistik / KPI — `.s-stat` ✅/🔶
- **Zweck:** 1–3 große Zahlen. **Slots:** Eyebrow, Headline, 1–3 KPI (Zahl + Einheit-Lime + Bildunterschrift),
  optional Fußzeile.
- **Layout:** KPI-Reihe (Glas-Cards). **Casing:** Mixed. **bg:** t2.

### B8 · Tabelle — `.s-table` ✅
- **Zweck:** Daten/Specs/Preise/Matrix. **Slots:** Eyebrow, Headline, Header-Zeile, 3–8 Datenzeilen,
  optional Highlight-Spalte/Zeile (Lime-getönt).
- **Layout:** Zebra über `rgba`-Trennlinien (kein harter Rahmen — Shadow-as-Border), Header in Unbounded 700,
  Zahlen tabellarisch (`font-variant-numeric:tabular-nums`). Max ~8 Zeilen × 5 Spalten lesbar.
- **Casing:** Header-Labels UPPERCASE-Eyebrow-Stil, Headline Mixed. **bg:** t1 (dunkel-links für Lesbarkeit).

### B9 · Vergleich — `.s-compare` ✅
- **Zweck:** 2-Spalten / Vorher-Nachher / Wir-vs-Markt. **Slots:** Headline, 2 Spalten je
  (Titel, Badge, Liste mit ✓/✗), optional Mittel-Divider „vs".
- **Layout:** zwei Glas-Cards; „eigene" Seite Lime-akzentuiert, Gegenseite neutral. ✓ = Lime, ✗ = gedämpft.
- **Casing:** Headline Mixed, Spaltentitel Display 700. **bg:** t4.

### B10 · Diagramm / Chart — `.s-chart` ✅ (CSS/SVG · Chart.js-Variante offen)
- **Zweck:** Balken/Linie/Donut + Aussage. **Slots:** Eyebrow, Headline, Chart, Legende, Caption/Quelle.
- **Layout:** Chart links/zentriert, Kernaussage als kurzer Text daneben. **Casing:** Mixed. **bg:** t3.

### B11 · Prozess / Schritte — `.s-process` ✅
- **Zweck:** nummerierte Schritte / Ablauf / Flow. **Slots:** Eyebrow, Headline, 3–5 Schritte
  (Nummer/Icon + Titel + Text), optional Pfeile zwischen Schritten.
- **Layout:** Liste (vertikal, Lime-Nummern) **oder** horizontaler Flow (Kreise + Pfeile). **Casing:** Mixed. **bg:** t2.

### B12 · Karten-Raster — `.s-cards` ✅
- **Zweck:** 2–4 Features/Leistungen. **Slots:** Eyebrow, Headline, 2–4 Karten (Icon, Titel, Text).
- **Layout:** Glas-Cards-Grid. **Casing:** Mixed. **bg:** rotierend.

### B13 · Bild + Text — `.s-split` ✅/🔶
- **Zweck:** Foto/Diagramm mit Erläuterung, Vorher/Nachher-Beleg. **Slots:** Eyebrow, Headline,
  Text/Bulletpoints, Figure (Bild + Caption).
- **Layout:** Text eine Hälfte, `figure` die andere. **Casing:** Mixed. **bg:** t1 (Text-Seite dunkel).

### B14 · Timeline / Roadmap — `.s-timeline` ✅
- **Zweck:** zeitlicher Verlauf / Meilensteine / Phasen. **Slots:** Eyebrow, Headline, 3–6 Punkte
  (Zeit/Phase + Titel + kurzer Text) entlang einer Achse.
- **Layout:** horizontale Achse mit Lime-Knoten, abwechselnd ober-/unterhalb. **Casing:** Mixed. **bg:** t4.

---

## Diagramme — beide Wege (Entscheidung: beides anbieten)

**Default · reines CSS/SVG** (keine Abhängigkeit, print-stabil, voll markenkonform, im HTML editierbar):
- **Balken:** Flex-/Grid-Säulen, Höhe in %, Füllung Lime bzw. Grün-Abstufungen, Achse als `rgba`-Linie.
- **Linie/Fläche:** Inline-`<svg>` `<polyline>`/`<path>`, Lime-Stroke, weicher Flächen-Gradient darunter.
- **Donut/Progress:** `<svg>` `<circle>` mit `stroke-dasharray` (Lime auf Deep-Green-Track).
- Farbregel: **Lime = Hauptserie/Highlight**, Grüntöne (`pure/transition`) für Nebenserien; Gitter dezent `rgba(255,255,255,.12)`; Labels TT Norms.

**Option · Chart.js** (für interaktive/komplexe Datensätze) — dokumentierte Alternative:
- Per CDN einbinden; Marken-Theme setzen: Datasets in Lime/Grüns, `gridColor rgba(255,255,255,0.12)`,
  Ticks `rgba(255,255,255,0.7)`, Font Unbounded/TT Norms, Tooltips Deep-Green.
- **Trade-off:** externe Abhängigkeit + weniger print-/PDF-stabil → nur wenn CSS/SVG nicht reicht.

---

## Umsetzungsplan (phasenweise, später)

- **Phase 1 — Lücken zuerst** ✅ **erledigt** (in `bkm-glass-ag/demo.html`): `s-quote`, `s-table`, `s-compare`, `s-chart` (CSS/SVG), `s-agenda`.
- **Phase 2 — Vervollständigen in `bkm-glass-ag`:** ✅ **erledigt** — `s-chapter`, `s-subhead`, `s-closing`,
  `s-process`, `s-timeline`. `demo.html` deckt jetzt alle 14 Typen ab (= vollständige Vorlage).
- **Phase 3 — Galerie & Doku:** ✅ **erledigt** — `templates/bkm-glass-ag/type-gallery.png` + Verweise in `SKILL.md`.
- **Phase 4 — Portierung:** Typen in `bkm-glass-fachbetrieb`, `bkm-editorial`, `bkm-bold-poster`
  (familienspezifische Tokens, kein Lime im Fachbetrieb).

**Akzeptanzkriterien je Typ:** rendert sauber auf 1920×1080, kein Überlauf; erbt Schriften/Logo/Textur;
Hybrid-Casing korrekt; nur BKM-Farben; in `PATTERN_CATALOG` als erlaubt geführt.
