# BKM · Editorial — Design-Rezept (design.md)

> Vollständiges Design-System der Familie **BKM · Editorial** (Kreativ-Track).
> Engine: `frontend-slides` Fixed-Stage. Demo: `demo.html`.
> **Leitplanke:** ausschließlich BKM-Farben aus `DESIGN.md`, Headlines immer Unbounded 900.

## Idee

Ein **flaches, redaktionelles Ink-System** — „Geschäftsbericht trifft Magazin".
Keine Glasmorphismus-Cards, keine Schatten, keine Gradienten. Tiefe entsteht durch
**Farbblock-Inversion** (Deep-Green-Kachel auf Sand) und **4px-Linien**. Der Stil ist
der Kreativ-Gegenpol zum ruhigen Glas-Standard: größere Typo, mehr Struktur, mehr
Selbstbewusstsein — aber strikt in BKM-Farben.

## Farben (nur BKM)

| Rolle | Token | Wert |
|------|-------|------|
| Canvas / Paper | `--paper` | `#f5f0eb` |
| Ink (Text, Linien, Inverse-Kachel) | `--deep-green` | `#1c4b42` |
| Sekundär-Akzent (Eyebrow, ein Headline-Wort, KPI-Einheit) | `--pure-green` | `#4daf46` |
| Signal (Zahlen in Inverse-Kacheln, Marks, Pfeile) | `--lime` | `#b4e717` |
| Chrome unten / Meta | `--transition-green` | `#287d4b` |
| Body-Text | `--stone-grey` | `#494949` |

**Regeln:** Lime nur als Signal, nie als Fläche. Inverse-Kacheln sind immer Deep Green
mit Paper/Lime-Inhalt. Kein vierter Farbton.

## Typografie

- **Display:** Unbounded **900**, UPPERCASE, kein Italic, negatives Tracking
  (−0.04em), enge Zeilenhöhe (0.90–0.95).
- **Body/Chrome:** System-Sans (im Echtbetrieb TT Norms Pro). Labels/Eyebrows/Footlines
  immer **UPPERCASE** mit ≥0.10em Tracking.

| Token | Größe | Einsatz |
|-------|------:|---------|
| Cover-Headline | 142px | Titelfolie |
| Statement | 128px | Aussage-/Closing-Folie |
| Section-Headline | 88–96px | Agenda, Content, Daten |
| Agenda-Name | 46px | Listenzeile |
| Card-Titel | 30px | Spalten-Überschrift |
| KPI-Figur | 88px | Kennzahl (Einheit in Pure Green) |
| Eyebrow | 19px / 0.18em | über jeder Headline |
| Chrome (Mast/Foot) | 17px / 0.12em | Masthead, Footline |
| Body | 21–27px | Lead, Spaltentext |

## Struktur & Chrome

- **Canvas:** 1920×1080, Seitenabstand **140px**.
- **Masthead** (oben 64px): Wortmarke „BKM Mannesmann" + **Lime-Quadrat 12px** links,
  Rubrik rechts.
- **Footline** (unten 60px): Stil-/Sektionslabel links, Seitenzahl (Unbounded) rechts.
- **4px-Linie** (`--rule`): Struktur-Standard. Über jeder Spalte/Listenzeile, als
  Trenner, als Ornament-Balken. Niemals 1px/2px für Struktur.
- **Inverse-Kachel:** Deep-Green-Fläche mit Paper-Text und Lime-Zahl. Das „erhöhte" Element.
- Alle Formen **rechteckig** (kein Border-Radius), außer Lime-Quadrat-Mark.

## Slide-Typen (in `demo.html`)

1. **Cover** — Linie, Eyebrow, große Headline (ein Wort Pure Green), Lead, Tag + Datum.
2. **Agenda** — nummerierte Zeilen, 4px-Linien oben/unten, Ordnungszahl in Pure Green.
3. **Content (3 Spalten)** — je Spalte 4px-Toplinie, Inverse-Icon-Kachel mit Lime-Icon, Titel, Text.
4. **Daten** — KPI-Liste links (4px-Linien) + Inverse-Chart-Karte rechts mit Lime/Paper-Balken.
5. **Statement** — Vollflächiges Deep Green, Doppellinien-Ornament in Lime, Riesen-Headline.
6. **Closing** — Linie, Headline, Kontaktblock + Inverse-CTA mit Lime-Pfeil.

## Do / Don't

**Do:** große Typo statt mehr Elemente; 4px-Linien als Rhythmus; ein Headline-Wort in
Pure Green; Inverse-Kacheln für Hervorhebung; Statement-Folie auf Deep Green.

**Don't:** keine Glas-Cards/Schatten/Gradienten in dieser Familie; kein Lime als Fläche;
keine fremden Farben/Fonts; nicht überladen (Headline + 3–4 Stützelemente pro Slide).

## Fixed-Stage-Policy

Bei `frontend-slides`-Nutzung: 1920×1080, als Ganzes in den Viewport skaliert,
Letterbox statt Reflow. Nach dem Bau Screenshots auf Überlauf **und** Überlappung prüfen.
