# BKM Slides — Quickstart (für Kollegen & KI-Tools)

> **Ziel:** stimmige, markenkonforme BKM-Präsentationen — egal ob in Claude Code,
> Claude.ai oder Manus AI.

---

## Das eine Prinzip, das alles entscheidet

Der markengetreue Look hängt an **eingebetteten Binär-Assets**, die **in den Vorlagedateien
stecken**:

- echtes **Logo** (als Data-URI),
- eingebettete Marken-Schriften **Unbounded + TT Norms Pro** (woff2),
- **texturierte Hintergründe** (Fensterlicht auf Deep Green),
- die **Fixed-Stage-Engine** (1920×1080) + Reveal-Motion.

**Diese Assets lassen sich NICHT aus den Markdown-Dokumenten rekonstruieren.** Wer eine KI
nur „lies die Doku und bau eine Präsentation" auffordert, bekommt einen **generischen,
veralteten** Look: nachgebautes Text-Logo, nur Google-Fonts-Unbounded (kein TT Norms),
flache Flächen statt Texturen.

> ✅ **Richtig:** immer von einer **fertigen, self-contained Vorlage ausgehen und nur den
> Inhalt ersetzen.**
> ❌ **Falsch:** „aus dem Nichts" anhand der Doku neu generieren.

Die Vorlagen sind die **Golden-Reference-Decks**:
`skills/bkm-slides/templates/<family>/demo.html` — jede Datei ist **vollständig
eigenständig** (Assets eingebettet, einfach im Browser öffnen).

---

## Welche Familie?

| Familie (`slug`) | Look | Kontext |
|---|---|---|
| **`bkm-glass-ag`** | Glasmorphismus auf Deep Green, Lime-Signal | **BKM AG** (corporate) — Default |
| **`bkm-glass-fachbetrieb`** | helles Milchglas auf Sand, **kein Lime** | Fachbetrieb (nahbar) |
| **`bkm-editorial`** | flaches Ink, 4px-Linien | beide / kreativ |
| **`bkm-bold-poster`** | übergroße Statements | BKM AG / Pitch |

Im Zweifel: **`bkm-glass-ag`**.

---

## Weg A — Claude Code mit dem Repo (empfohlen, beste Qualität)

Repo geöffnet/geklont, dann einfach:

```
Erstelle ein BKM-Deck zu [Thema] für [BKM AG / Fachbetrieb].
Nutze die bkm-slides-Skill, baue auf templates/bkm-glass-ag/demo.html auf,
ersetze nur den Inhalt und rendere zur Kontrolle (1920×1080).
```

Claude liest die Skill, kopiert `demo.html`, tauscht den Inhalt aus und prüft per Render.
Schriften, Logo, Texturen, Motion bleiben automatisch erhalten.

---

## Weg B — Claude.ai oder Manus AI (ohne Repo): Vorlage ANHÄNGEN

1. Lade die Vorlage herunter:
   `skills/bkm-slides/templates/bkm-glass-ag/demo.html`
   (eine Datei, ~0,9 MB, alles eingebettet).
2. **Hänge die Datei an** den Chat an (nicht nur verlinken!).
3. Prompt:

```
Anbei die BKM-Folienvorlage (self-contained: eingebettete Schriften, Logo,
texturierte Hintergründe, Engine). Bitte:
- Dupliziere die vorhandenen Folien und ersetze NUR Text/Inhalt mit [Thema].
- Lass CSS, Schriften (Unbounded + TT Norms), Logo, Hintergründe (.bg.t1..t4)
  und die Engine 1:1 unverändert.
- Hintergründe über die Folien rotieren (t1,t2,t3,t4,…), nicht zweimal gleich nebeneinander.
- Headline-Casing: Cover & Kapitel-Trenner UPPERCASE, Inhalts-Headlines Mixed-Case (.mixed).
- Akzentwort über Lime-Farbe, nie kursiv. Nur BKM-Farben.
Gib eine vollständige, eigenständige HTML-Datei zurück.
```

So bleibt der Marken-Look erhalten, weil die Assets in der Datei bleiben.

---

## Marken-Leitplanken (Kurzfassung)

- **Farben:** nur BKM (`#1c4b42` Deep Green, `#b4e717` Lime, `#4daf46`/`#287d4b` Grüns,
  Sand `#f5f0eb`). Lime **nur** als Akzent. Fachbetrieb: **kein** Lime.
- **Schrift:** Unbounded (Headlines) + TT Norms Pro (Fließtext). Keine Fremdschriften.
- **Casing:** Hybrid — Cover/Trenner UPPERCASE, Sections Mixed-Case (`.mixed`). Nie kursiv.
- **Hintergründe:** texturierte `.bg.t1…t4`, rotierend. Keine fremden Fotos als Vollfläche.
- **Logo/Keyvisual:** echtes eingebettetes Logo; Keyvisual (Chevrons) **nur** auf dem Deckblatt.
- Details: `PATTERN_CATALOG.md` (erlaubt/verboten), `templates/<family>/design.md` (Rezept).

---

## Schnell prüfen, ob es „stimmt"

- Schrift der Headlines = **Unbounded** (geometrisch), Fließtext = **TT Norms** (nicht Arial/Segoe)?
- Logo = echtes BKM-Signet (nicht nachgebauter Text)?
- Hintergrund **texturiert** (weiches Licht), nicht flaches Grün?
- Canvas **1920×1080**, Seitenzahl unten rechts in Lime?
- Beim Folienwechsel **Reveal-Motion** (Inhalte gleiten ein)?

Fehlt davon etwas → es wurde „from scratch" generiert statt aus der Vorlage. Weg A oder B nutzen.
