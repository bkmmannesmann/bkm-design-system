# Fachbetrieb · Glas — Design-Rezept (design.md)

> Familie **Fachbetrieb · Glas** (Standard-Track, Marken-Lock). Helles Glassmorphism
> auf Sand. Die nahbare Schwester von `bkm-glass-ag`. Engine: `frontend-slides` Fixed-Stage.
> Demo: `demo.html`.
> **Leitplanke:** nur BKM-Farben; **niemals Lime** (Fachbetrieb-Kontext); Headlines Unbounded 900.

## Idee

Der **helle, zugängliche** Marken-Look für den Fachbetrieb vor Ort: warmer Sand-Raum,
in dem **helle Milchglas-Cards** schweben. Freundlich und vertrauensvoll statt
corporate-dunkel. Akzent ist **Pure Green** — kein Lime.

## Farben (nur BKM, kein Lime)

| Rolle | Token | Wert |
|------|-------|------|
| Hintergrund-Verlauf | Sand → Sand2 | `#f7f6f3` → `#e9e5de` |
| Blobs (Tiefe hinter Glas) | Pure Green / Transition / warmer Sand | `#4daf46` / `#287d4b` / `#d8cfbf` |
| **Text / Ink** (Headlines, KPI-Zahlen, Eyebrow) | `--transition-green` | `#287d4b` |
| Flächen/Tiefe (Button-Fill, Karten-Kopf-Verlauf, Schatten) | `--deep-green` | `#1c4b42` |
| Akzentwort / Icon / KPI-Einheit / Page | `--pure-green` | `#4daf46` |
| Body | `--stone-grey` | `#494949` |

**Regeln:** **Kein Lime.** Akzent ist Pure Green (Wort, Icon-Kachel, KPI-Einheit, Page-Nr.),
Transition Green für Sublabels. Button = Deep-Green-Fläche, weißer Text.

## Das helle Glas-Rezept

```css
.glass-card{
  background:rgba(255,255,255,0.55);
  backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);
  border-radius:24px;border:1px solid rgba(255,255,255,0.85);
  box-shadow:
    0 12px 40px rgba(28,75,66,0.10),
    inset 0 1px 0 rgba(255,255,255,0.9),
    inset 0 0 60px 10px rgba(255,255,255,0.25);
}
.glass-card::before{ /* Licht-Linie oben */
  content:'';position:absolute;top:0;left:0;right:0;height:1px;
  background:linear-gradient(90deg,transparent,rgba(255,255,255,.95),transparent);}
```

Gegenüber `bkm-glass-ag`: helleres Milchglas (höhere Weiß-Deckung), **dunkler Text**,
weicher **grüner** Schatten statt schwarzer. Damit Blur wirkt, immer Sand-Verlauf +
Blobs (oder Foto) dahinter.

## Typografie

- **Display:** Unbounded **900**, −0.04em, Zeilenhöhe ~0.94. Casing UPPERCASE oder
  Mixed-Case erlaubt, nie kursiv. **Textfarbe Transition Green** (`#287d4b`) —
  weicher/freundlicher als Deep Green; Akzentwort über **Pure-Green-Farbe**.
  Deep Green nur noch für Flächen (Button, Karten-Kopf).
- **Body:** System-Sans (Echtbetrieb: TT Norms Pro), Stone Grey.
- **Eyebrow/Labels:** UPPERCASE, ≥0.12em Tracking.

## Form & Struktur

- Canvas 1920×1080, Seitenabstand **140px**.
- Glas-Cards `border-radius: 24px`; Icon-Kachel/Button **12–16px** (8px-Regel-konform).
- **Primärlogo** (Stone-Grey + Pure-Green) oben links, Rubrik oben rechts, Seitenzahl
  unten rechts (Pure Green). Im Prototyp als Data-URI eingebettet; im Skill per Pfad.

## Slide-Typen (in `demo.html`)

1. **Titel** — große Milchglas-Card (Eyebrow/Headline/Text/Button); **Keyvisual rechts** (kein Chip).
2. **Drei Leistungen** — drei Glas-Cards mit Pure-Green-Icon-Kachel.
3. **Kennzahlen** — breite Glas-Panel mit 3 KPI-Spalten (dezente Trennlinien).
4. **Referenzen** — Typo-Bild-Karten: **Transition-Green-Kopf** (Verlauf
   Transition→Deep Green) mit **weißer Zahl** + Pure-Green-Einheit, darunter sauberer
   **weißer Body** mit Case-Study-Text; Überschrift in **Transition Green**.
   (Bewusst kräftiger Grün-Kopf statt heller Sand-Fläche — sauberer, nicht „schmutzig".)

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

**Do:** hell & luftig halten; Sand/Blobs hinter das Glas; Pure Green als einziger Akzent;
dunkler Text auf hellem Glas; freundlicher, partnerschaftlicher Ton.

**Don't:** **kein Lime**; keine dunklen Deep-Green-Vollflächen (das ist der AG-Look);
kein Glas ohne Hintergrund; keine fremden Farben/Fonts.

## Fixed-Stage-Policy

1920×1080, als Ganzes skaliert, Letterbox statt Reflow. `backdrop-filter` GPU-lastig —
beim PDF-Export Blur prüfen, zur Not auf flache Halbtransparenz zurückfallen.
