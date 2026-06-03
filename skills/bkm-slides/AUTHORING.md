# BKM Decks — Autoren-Anleitung (deterministisch, agenten-unabhängig)

> **Ziel:** identische, markenkonforme Decks — **egal welcher KI-Agent** (Opus, Sonnet,
> ein Kollegen-LLM …) den Inhalt erzeugt.

## Prinzip: Inhalt vom Rendering trennen

Visuelle Unterschiede zwischen Agenten entstehen, wenn ein LLM **Layout/CSS selbst erfindet**.
Lösung: Das LLM liefert **nur strukturierten Inhalt** (eine JSON-Folienliste). Das **Layout
besitzt der Generator** (`tools/deck_builder.py`, committeter Code). Damit ist das Ergebnis
**reproduzierbar und über alle Agenten hinweg identisch**.

```
Inhalt (LLM → JSON-Spec)  ─►  tools/deck_builder.py (Code)  ─►  fertiges HTML-Deck
```

## Generator ausführen

```bash
python3 tools/deck_builder.py meine-folien.json -o mein-deck.html [--strict]
```

- bringt **Schriften, Logo, texturierte Hintergründe** selbst mit (eingebettet),
- erzwingt **automatisch**: Hintergrund-Rotation über **16 Hintergründe** (4 Konzepte × 4 Spiegel/Dreh-Varianten) (nie 2× gleich nebeneinander),
  Hybrid-Casing, Zeilen-Zebra, Reveal-Motion, Presenter-Modus (Taste „S") + Notizen („N"),
- prüft den **Mix-Rhythmus** und meldet Monotonie (`--strict` = Build bricht ab).

## JSON-Spec

```json
{
  "family": "bkm-glass-ag", // bkm-glass-ag | bkm-bold-poster | bkm-glass-fachbetrieb
  "meta": { "title": "…", "tagtop": "BKM AG" },
  "slides": [ { "type": "cover", … }, … ]
}
```

**Konventionen in Texten:** `{{Wort}}` = Akzent in Lime · `<br>` = Zeilenumbruch ·
`&shy;` = weiches Trennzeichen. Ein normales Und-Zeichen einfach als `&` schreiben (nicht als HTML-Entity). Jede Folie kann `"notes": "…"` (Sprechernotizen) tragen.

### Folientypen & Felder
| `type` | Felder |
|---|---|
| `cover` | `eyebrow, title, lead, button, meta:[{k,v}]` |
| `agenda` | `eyebrow, title, rows:[{time,topic,sub,spk}]` |
| `chapter` | `no, eyebrow, title` (Kapitel-Trenner) |
| `subhead` | `eyebrow, title, sub` |
| `statement` | `eyebrow, title, lead` (große Aussage) |
| `cards` | `eyebrow, title, items:[{icon,h,p}]` (2–4) |
| `kpi` | `eyebrow, title, items:[{value,label}]` (1–3) |
| `split` | `eyebrow, title, points:[…], image, caption` (Bild rechts) |
| `quote` | `eyebrow, text, source` |
| `table` | `eyebrow, title, columns:[…], rows:[[…]], highlight:<spaltenindex>` |
| `compare` | `eyebrow, title, columns:[{badge,title,win,items:[…]}] (2), foot` |
| `chart` | `eyebrow, title, bars:[{label,value,display,hi}]` **oder** `line:[{label,value,display,hi}]` (Linien-/Kurvendiagramm), `note:{h,p,cap}` |
| `process` | `eyebrow, title, steps:[{h,p}]` |
| `timeline` | `eyebrow, title, points:[{yr,h,p}]` |
| `closing` | `eyebrow, title, chips:[…], punch` |
| `funnel` | `eyebrow, title, tiers:[{value,label,width}]` (TAM/SAM/SOM) |
| `donut` | `eyebrow, title, center:{value,label}, segments:[{label,value}]` |
| `bigstat` | `eyebrow, value, sub, stats:[{value,label}]` (Mega-Kennzahl) |
| `bubbles` | `eyebrow, title, bubbles:[{value,size,label}]` (`size`=Zahl fürs Skalieren) |
| `team` | `eyebrow, title, members:[{name,role,image}]` (Porträt-Raster) |
| `twocol` | `eyebrow, title, columns:[{h,p,items:[…]}] (2)` (Zwei-Spalten-Text) |
| `pricing` | `eyebrow, title, plans:[{name,price,period,badge,highlight,features:[…]}]` |
| `flow` | `eyebrow, title, steps:[{icon,h,p}]` (horizontaler Ablauf mit Pfeilen) |
| `gauge` | `eyebrow, value(0–100), display, label, note:{h,p}` (Kreis-Fortschritt) |
| `pictograph` | `eyebrow, title, groups:[{value,filled,total,icon,label}]` (Icon-Array) |
| `imagecover` | `eyebrow, title, sub, image` (Vollbild-Foto-Titel mit Overlay) |
| `bento` | `eyebrow, title, items:[{icon,h,p,wide,tall,accent}]` (gemischtes Raster) |
| `statcluster` | `eyebrow, title, items:[{value,label,image}]` (organischer Kennzahl-/Bild-Cluster) |
| `numlist` | `eyebrow, title, items:[{no,text,tag}]` (nummerierte Liste mit Tag) |
| `gallery` | `eyebrow, title, images:[{src,caption}]` (Bild-Raster) |
| `contact` | `eyebrow, title, blocks:[{k,v}], image` (Kontakt-Folie) |
| `imagesplit` | `eyebrow, title, lead, points:[…], image, side:"left"/"right"` (50/50 Bild) |

`icon` = Font-Awesome-Name (z. B. `shield-halved`). `image` = Pfad relativ zur Spec
(sonst Platzhalter-Textur). Vollständiges Beispiel: **`tools/sample-deck.json`**.

## Mix & Rhythmus über lange Decks (bis 50 Folien)

Automatisch erzwungen: Hintergrund-Rotation, Casing, Zebra. Der Linter **warnt** bei:
- **≥ 3 gleichen Inhaltstypen in Folge** → Typ variieren.
- **> 8 Folien ohne `chapter`/`subhead`** → Gliederung einstreuen.

**Empfohlene Komposition** (für BKM AG inkl. Fachbetriebs-Themen):
`cover → agenda → chapter → (cards/kpi/split/table/compare/chart/process im Wechsel)
→ quote/statement als Auflockerer → chapter → … → closing`.
**Topic→Typ-Mapping:** Leistungen→`cards` · Zahlen→`kpi`/`chart` · Daten/Specs→`table` ·
Gegenüberstellung→`compare` · Ablauf/Regulatorik→`process`/`timeline` · Produkt/Referenz→`split` ·
Kundenstimme→`quote` · Kernaussage→`statement`.

## Der Prompt für Kollegen-LLMs (Inhalt → Spec)

> Wandle die folgende Präsentation/den Inhalt in eine **BKM-Deck-Spec (JSON)** nach dem
> Schema in `skills/bkm-slides/AUTHORING.md` um. Wähle pro Folie den **passenden `type`**,
> sorge für **abwechslungsreiche Typen** (nicht 3× derselbe in Folge; alle ~6–8 Folien ein
> `chapter`/`subhead`), nutze `{{…}}` für **ein** Akzentwort je Headline. `family`:
> `bkm-glass-ag`/`bkm-bold-poster` (BKM AG) oder `bkm-glass-fachbetrieb` (hell). **Gib NUR gültiges
> JSON aus — kein HTML, kein CSS.** Das Rendering macht `tools/deck_builder.py`.

So bleibt das Ergebnis konsistent — der Agent trifft nur Inhalts-/Struktur-Entscheidungen,
nie Layout-Entscheidungen.
