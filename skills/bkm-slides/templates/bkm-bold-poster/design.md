# BKM · Bold Poster — Design-Rezept (design.md)

> Familie **BKM · Bold Poster** (Kreativ-Track). Übergroße Statements auf Deep Green.
> Engine: `frontend-slides` Fixed-Stage. Demo: `demo.html`.
> **Leitplanke:** nur BKM-Farben, Unbounded 900; Lime nur als Signal (kein Vollflächen-Lime).

## Idee

Der **lauteste** BKM-Look: eine Aussage, maximal groß. Für Pitches, Messen, Titel- und
Manifest-Momente. Tiefe entsteht durch **Typo-Größe und Leere**, nicht durch Elemente.
Lime ist der scharfe Akzent, der die Botschaft setzt.

## Farben (nur BKM)

| Rolle | Token | Wert |
|------|-------|------|
| Hintergrund-Radialverlauf | `#235a4f → --deep-green → --deep2` | `#235a4f → #1c4b42 → #0f2620` |
| Headline-Text | `--paper` | `#f5f0eb` |
| Signal: Akzentwort / Zahl / Mark / Block / CTA | `--lime` | `#b4e717` |
| Eyebrow | `--lime` | `#b4e717` |
| Kicker / Sublines | `rgba(245,240,235,.55–.82)` | — |

**Regeln:** Lime als Signal — Akzentwort, große Zahl, Mark-Pill, **ein** Highlight-Block
hinter genau einem Wort, CTA-Button. **Kein** vollflächiger Lime-Hintergrund. Kein Lime
im Fachbetrieb-Kontext (Bold Poster ist AG-only).

## Typografie

- **Display:** Unbounded **900**, UPPERCASE, Zeilenhöhe **0.78–0.90**, Tracking **−0.05em**.
  - Manifest/CTA-Headline: 150–172px
  - Riesen-Zahl: bis ~500px
  - „Zahl + Wort": Zahl ~360px, Wort ~150px
- **Eyebrow:** Lime, 20px, 0.2em Tracking, UPPERCASE.
- **Kicker/Sublines:** System-Sans; Kicker 15px/0.16em.
- **Casing:** UPPERCASE ist hier Default (plakativ). Mixed-Case (Version B) wäre erlaubt,
  passt aber selten zum lauten Ton. **Nie kursiv.**

## Form & Struktur

- Canvas 1920×1080, Seitenabstand **130px**.
- **Lime-Mark-Pill** oben links, **Logo** (weißes Sekundärlogo, auf Deep Green) oben rechts, **Kicker** unten links,
  **Seitenzahl** (Lime) unten rechts.
- Rundungen **8–12px** (Mark, Highlight-Block, CTA) — im Einklang mit der 8px-Regel.

## Slide-Typen (in `demo.html`)

1. **Manifest** — übergroße 3-Zeilen-Headline, eine Zeile Lime, Lime-Mark + Subline-Linie.
2. **Riesen-Zahl** — zentrierte Mega-Zahl (`0%`), Einheit Lime, Label + Subline.
3. **Zahl + Wort** — große Lime-Zahl (`30+`) über einer Headline-Zeile.
4. **Highlight-Statement** — 3 Zeilen, das mittlere Wort in einem **Lime-Block** (Deep-Green-Text).
5. **Closing-CTA** — Headline (Akzentwort Lime) + Lime-CTA-Button + Kontaktblock.

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

**Do:** eine Idee pro Folie; riesig + viel Luft; Lime gezielt auf das Schlüsselwort;
kurze, harte Aussagen.

**Don't:** kein Fließtext/Listen/Tabellen (dafür Glas-AG/Fachbetrieb); kein vollflächiges Lime;
keine fremden Farben/Fonts; nicht zwei Lime-Signale konkurrieren lassen (ein Fokus pro Folie).

## Fixed-Stage-Policy

1920×1080, als Ganzes skaliert, Letterbox statt Reflow. Sehr große Typo nach dem Bau auf
Überlauf prüfen (Screenshot); zu lange Wörter ggf. umbrechen oder Größe reduzieren.
