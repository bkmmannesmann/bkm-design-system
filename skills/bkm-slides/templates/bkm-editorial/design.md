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

- **Display:** Unbounded **900**, negatives Tracking (−0.04em), enge Zeilenhöhe (0.90–0.95).
  **Casing: UPPERCASE (Standard) oder Mixed-Case erlaubt** — beide markenkonform.
  **Nie kursiv, keine Fremd-Akzentschrift** (Entscheidung: Versionen A & B ja, C nein).
  Akzentwörter werden über **Farbe** (Lime/Pure Green) gesetzt, nicht über Kursivschrift.
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
- **Flächen-Elemente mit `border-radius: 8px`** abgerundet: Tags, Icon-Kacheln,
  Chart-Karte, CTA-Buttons. Balken nur oben gerundet (`8px 8px 0 0`).
  **Linien** (4px-Regelwerk, Trenner) bleiben Linien — nicht runden.

## Slide-Typen (in `demo.html`)

1. **Cover** — Linie, Eyebrow, große Headline (ein Wort Pure Green), Lead, Tag + Datum.
2. **Agenda** — nummerierte Zeilen, 4px-Linien oben/unten, Ordnungszahl in Pure Green.
3. **Content (3 Spalten)** — je Spalte 4px-Toplinie, Inverse-Icon-Kachel mit Lime-Icon, Titel, Text.
4. **Daten** — KPI-Liste links (4px-Linien) + Inverse-Chart-Karte rechts mit Lime/Paper-Balken.
5. **Statement** — Vollflächiges Deep Green, Doppellinien-Ornament in Lime, Riesen-Headline.
6. **Closing** — Linie, Headline, Kontaktblock + Inverse-CTA mit Lime-Pfeil.
7. **Referenzen** (nur Dunkel-Demo) — Typo-Karten: flacher Deep2-Block mit großer
   zweifarbiger Zahl, 4px-Paper-Linie als Trenner, darunter Case-Study-Text.
   (Energma-Muster in editorial-flacher Sprache — Gegenstück zur Glas-Variante.)

## Keyvisual (nur Deckblatt)

Das M-Pfeil-**Keyvisual** erscheint **ausschließlich auf der Titelfolie/dem Deckblatt** —
als ruhige Markensignatur an der rechten Kante.

- **Position:** rechte Außenkante **bündig** mit dem Folienrand (`right:0`), **vertikal
  zentriert**. **Vollständig sichtbar** — nicht angeschnitten, oben/unten frei.
- **Größe:** Höhe ~560px (≈52 % der Folie), bewusst zurückhaltend.
- **Variante je Hintergrund:** dunkel → **weiß** (`keyvisual-on-dark.png`), hell →
  **grün** (`keyvisual-on-light.png`). Opacity ~0.85.
- **Z-Ebene:** hinter Inhalts-Cards/Text, vor dem Hintergrund.
- **Asset:** kompakte PNGs in `assets/keyvisual/` (~50 KB; Voll-Vektor: `.svg` daneben).
  Im Prototyp als Data-URI eingebettet, im Skill per Pfad referenzieren.

```css
.keyvisual{position:absolute;right:0;top:50%;transform:translateY(-50%);
  height:560px;width:auto;opacity:.85;pointer-events:none;z-index:0;}
```

## Do / Don't

**Do:** große Typo statt mehr Elemente; 4px-Linien als Rhythmus; ein Headline-Wort in
Pure Green; Inverse-Kacheln für Hervorhebung; Statement-Folie auf Deep Green.

**Don't:** keine Glas-Cards/Schatten/Gradienten in dieser Familie; kein Lime als Fläche;
keine fremden Farben/Fonts; nicht überladen (Headline + 3–4 Stützelemente pro Slide).

## Varianten

| Variante | Datei | Canvas | Struktur-Linien | Eyebrow / Akzentwort | Logo |
|----------|-------|--------|-----------------|----------------------|------|
| **Hell** (Standard) | `demo.html` | Paper `#f5f0eb` | Deep-Green-Ink | Pure Green | Primärlogo (Stone-Grey + Pure-Green) |
| **Dunkel** | `demo-dark.html` | Deep Green `#1c4b42` | Paper-Weiß | Lime | Sekundärlogo (weiß + Pure-Green-Signet) |

**Regeln der dunklen Variante:**
- Headlines bewusst **kleiner** als hell (Cover 118px statt 142px, Section 76px statt 88px) —
  auf dunklem Grund wirkt große Typo schneller erdrückend.
- Struktur-Linien in **Paper-Weiß**; Lime bleibt punktuelles Signal (Ordnungszahlen, KPI-Einheit,
  Ornament, Pfeil, CTA-/Tag-Fläche als erlaubte „Mark/Button").
- **Statement-Folie invertiert** zu Paper (heller Beat) — gibt dem dunklen Deck Atemraum.
- **Chart-Karte** als heller Sand-Block (Kontrast-Beat) mit Deep-Green-Balken, höchster Balken Lime.
- **Logo** statt Wortmarke im Masthead: `assets/logos/bkm-logo-white-puregreen` (Sekundärlogo).
  Im Prototyp als Data-URI eingebettet, damit die Datei eigenständig bleibt; im Skill per Pfad referenzieren.
  Schriftzug nie umfärben/verzerren (siehe `docs/logo.md`).

## Fixed-Stage-Policy

Bei `frontend-slides`-Nutzung: 1920×1080, als Ganzes in den Viewport skaliert,
Letterbox statt Reflow. Nach dem Bau Screenshots auf Überlauf **und** Überlappung prüfen.
