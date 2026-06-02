# BKM AG · Glas — Design-Rezept (design.md)

> Familie **BKM AG · Glas** (Standard-Track, Marken-Lock). Glassmorphism auf
> Deep-Green-Grund. Engine: `frontend-slides` Fixed-Stage. Demo: `demo.html`.
> **Leitplanke:** nur BKM-Farben aus `DESIGN.md`, Headlines Unbounded 900.

## Idee

Der **sichere, premium Marken-Look** der BKM AG: ruhiger Deep-Green-Raum, in dem
**Frosted-Glass-Cards** schweben. Tiefe entsteht durch Licht (Highlight-Kanten,
Inner-Glow) statt durch laute Farbe. Lime ist nur das Signal.

## Farben (nur BKM)

| Rolle | Token | Wert |
|------|-------|------|
| Hintergrund-Verlauf | `--deep-green` → `--deep2` | `#1c4b42` → `#0f2620` |
| Blobs (Tiefe hinter Glas) | `--pure-green`, `--transition-green` | `#4daf46`, `#287d4b` |
| Signal / Akzentwort / Button | `--lime` | `#b4e717` |
| Text auf Glas | Weiß / `rgba(255,255,255,.85)` | — |
| Milchglas-Text (frost-Card) | `--deep-green` | `#1c4b42` |

**Regeln:** Lime nur als Signal (Akzentwort, Button, kleiner Blob-Schimmer). Nie als
großflächiger Fond. Kein Lime im Fachbetrieb-Kontext (dafür `bkm-glass-fachbetrieb`).

## Das Glas-Rezept

Basis: hype4academy Glassmorphism-Generator (https://hype4.academy/tools/glassmorphism-generator),
auf BKM angepasst. **Hinweis:** das Original nutzt `inset 0 0 60px 30px rgba(255,255,255,3)` —
Alpha `3` ist ungültig und wird vom Browser auf `1` geklemmt (extrem heller Glow).
Hier auf einen lesbaren Wert reduziert.

```css
.glass-card{
  background:rgba(255,255,255,0.12);
  backdrop-filter:blur(22px);-webkit-backdrop-filter:blur(22px);
  border-radius:24px;
  border:1px solid rgba(255,255,255,0.28);
  box-shadow:
    0 8px 32px rgba(0,0,0,0.28),
    inset 0 1px 0 rgba(255,255,255,0.5),
    inset 0 -1px 0 rgba(255,255,255,0.08),
    inset 0 0 60px 12px rgba(255,255,255,0.10);
  position:relative;overflow:hidden;
}
.glass-card::before{ /* Licht-Linie oben */
  content:'';position:absolute;top:0;left:0;right:0;height:1px;
  background:linear-gradient(90deg,transparent,rgba(255,255,255,.85),transparent);}
.glass-card::after{ /* Licht-Linie links */
  content:'';position:absolute;top:0;left:0;width:1px;height:100%;
  background:linear-gradient(180deg,rgba(255,255,255,.85),transparent,rgba(255,255,255,.25));}

/* Helle Milchglas-Variante (für Akzent-/Foto-Flächen, dunkler Text) */
.glass-card.frost{background:rgba(255,255,255,0.4);backdrop-filter:blur(14px);}
```

**Zwei Glas-Stufen:**
- **Standard** (`rgba(255,255,255,.12)`) — dezentes dunkles Glas, **weißer Text**.
- **Frost** (`rgba(255,255,255,.4)`) — helles Milchglas, **Deep-Green-Text**; für
  Chips/Akzente oder über Fotos.

**Damit Blur wirkt, muss etwas dahinter liegen.** Immer Brand-Blobs (geblurrte
Farbkreise) oder ein Foto hinter die Cards legen — sonst ist der Effekt unsichtbar.

## Typografie

- **Display:** Unbounded **900**, −0.04em, Zeilenhöhe ~0.94. Casing UPPERCASE (Standard)
  oder Mixed-Case erlaubt; **nie kursiv**. Akzentwort über Lime-Farbe, nicht kursiv.
  Titel ~118px, Section ~78px.
- **Body:** System-Sans (Echtbetrieb: TT Norms Pro), `rgba(255,255,255,.85)`.
- **Eyebrow / Labels:** UPPERCASE, ≥0.12em Tracking; Eyebrow in Lime.

## Form & Struktur

- Canvas 1920×1080, Seitenabstand **140px**.
- Glas-Cards `border-radius: 24px`; kleine UI-Elemente (Icon-Kachel, Button) **8–16px**
  — im Einklang mit der 8px-Rundungsregel des Systems.
- **Logo** (weißes Sekundärlogo, white+pure-green-Signet) oben links, Rubrik oben rechts, Seitenzahl unten rechts (Lime).
  Im Prototyp als Data-URI eingebettet; im Skill per Pfad referenzieren.

## Slide-Typen (in `demo.html`)

1. **Titel** — große Glas-Card mit Eyebrow/Headline/Text/Button; **Keyvisual rechts** (kein Chip).
2. **Drei Karten** — drei Glas-Cards mit Lime-Icon-Kachel, Titel, Text.
3. **Kennzahlen** — eine breite Glas-Panel mit 3 KPI-Spalten (Trennlinien aus Licht).
4. **Referenzen** — Typo-Bild-Karten: Glas-Card mit Gradient-Bildfläche + großer
   zweifarbiger Zahl (weiß + Lime), darunter Case-Study-Text. (Muster aus der
   Energma-Studie, hier in Glas-Sprache.)
5. **Bild & Grafik** — Text-Block links, **gerahmtes Foto** rechts (`.figure`:
   `object-fit:cover`, Glas-Kante, Bildunterschrift). Zeigt, wie Fotos/Diagramme
   eingesetzt werden — siehe Pattern 12 in `PATTERN_CATALOG.md`.

## Bilder & Grafiken

Nicht jede Folie ist nur Text. Bilder per `.figure` (gerahmt, `object-fit:cover`,
optionale `figcaption`), als vollflächiges Foto mit Overlay, oder im `.img`-Bereich
einer Card. **Foto austauschen = nur `src` ersetzen** (im Skill per Pfad, im Demo als
Data-URI). Fotos als **JPEG**, Grafiken mit Transparenz als **PNG**. Details: Pattern 12.

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

**Do:** Blobs/Foto hinter das Glas; Licht-Kanten beibehalten; Lime sparsam als Signal;
weißer Text auf dunklem Glas, Deep-Green-Text auf Milchglas.

**Don't:** kein Glas ohne Hintergrund (Effekt verpufft); Lime nicht als Card-Fond;
keine fremden Farben/Fonts; Text auf Glas immer auf Kontrast prüfen (Screenshot).

## Fixed-Stage-Policy

1920×1080, als Ganzes skaliert, Letterbox statt Reflow. `backdrop-filter` ist
GPU-lastig — beim PDF-Export prüfen (manche Renderer rastern Blur unterschiedlich;
zur Not Glas-Cards für den Export auf eine flache Halbtransparenz zurückfallen lassen).
