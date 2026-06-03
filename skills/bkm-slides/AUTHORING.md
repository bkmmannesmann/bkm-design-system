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
- erzwingt **automatisch**: Hintergrund-Rotation (nie 2× gleich nebeneinander),
  Hybrid-Casing, Zeilen-Zebra, Reveal-Motion, Presenter-Modus (Taste „S") + Notizen („N"),
- prüft den **Mix-Rhythmus** und meldet Monotonie (`--strict` = Build bricht ab).

## JSON-Spec

```json
{
  "family": "bkm-glass-ag",          // oder "bkm-bold-poster" (beide = BKM AG)
  "meta": { "title": "…", "tagtop": "BKM AG" },
  "slides": [ { "type": "cover", … }, … ]
}
```

**Konventionen in Texten:** `{{Wort}}` = Akzent in Lime · `<br>` = Zeilenumbruch ·
`&shy;` = weiches Trennzeichen. Jede Folie kann `"notes": "…"` (Sprechernotizen) tragen.

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
| `chart` | `eyebrow, title, bars:[{label,value,display,hi}], note:{h,p,cap}` |
| `process` | `eyebrow, title, steps:[{h,p}]` |
| `timeline` | `eyebrow, title, points:[{yr,h,p}]` |
| `closing` | `eyebrow, title, chips:[…], punch` |

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
> `bkm-glass-ag` (Standard) oder `bkm-bold-poster` (laute Statements). **Gib NUR gültiges
> JSON aus — kein HTML, kein CSS.** Das Rendering macht `tools/deck_builder.py`.

So bleibt das Ergebnis konsistent — der Agent trifft nur Inhalts-/Struktur-Entscheidungen,
nie Layout-Entscheidungen.
