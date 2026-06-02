# Prototyp: BKM Template-Pack + Style-Discovery

> Zweiter Entscheidungs-Prototyp. Zeigt zwei Konzepte aus `frontend-slides`,
> übersetzt auf BKM: das **auswählbare Template-Pack** und den
> **„Show don't tell"-Workflow**. Entscheidung: **Marke + Kreativ-Track**.

## Dateien

| Datei | Was |
|-------|-----|
| `style-discovery.html` | **Im Browser öffnen.** Die Stil-Auswahl-Galerie: 4 markenkonforme Vorschauen, auswählbar. |
| `selection-index.json` | Das Template-Pack-Manifest im `frontend-slides`-kompatiblen Metadaten-Format. |
| `templates/` | (folgt) Pro Familie eine `preview.md` (Stilkarte) + `design.md` (Design-Rezept). |

## Die zwei Tracks (deine Entscheidung)

- **Standard** — Marken-Lock. `BKM AG · Glas`, `Fachbetrieb · Glas`. Default für
  Kunden-/Produkt-/Print-nahe Decks.
- **Kreativ** — mehr Design für interne/Pitch/Vision-Decks: `BKM · Editorial`,
  `BKM · Bold Poster`. **Weiterhin ausschließlich BKM-Farben & Unbounded** —
  nur die Layout-Freiheit ist größer.

## So funktioniert der Workflow

1. **Inhalt & Anlass** abfragen (Zweck, Länge, Dichte: Lese- vs. Vortrags-Deck).
2. **Stil wählen** — Agent legt je nach Anlass 3 passende Vorschauen vor
   (1× sicher/Standard, 1–2× Kreativ), der Mensch wählt visuell. → `style-discovery.html`
3. **Deck generieren** — genau in der gewählten Familie, Fixed-Stage 1920×1080.
4. **Export/Deploy** — PDF, teilbarer Link, PPTX-Import.

## Anti-Slop-Regeln (BKM-Variante)

Aus `frontend-slides` übernommen, an BKM angepasst — kommen in den Skill:

- **Dichte-Modus** bewusst wählen (Vortrag = wenig Text/groß; Lesen = strukturierte Grids).
- Kein Überlauf, keine Überlappung, kein Text unter Lesegröße → sonst Slide teilen.
- Starke Hierarchie statt gleichförmiger Bento-Grids.
- **BKM-Leitplanken bleiben hart:** nur BKM-Farben, Unbounded 900 für Headlines,
  Lime nur als Signal und nie im Fachbetrieb-Kontext.

## Nächste Schritte

- `templates/*/preview.md` und `design.md` je Familie ausschreiben (wie im Upstream).
- Pack + Engine in den produktiven `skills/bkm-slides/` überführen.
- Skill zusätzlich als Claude-Code-Plugin verpacken (`.claude-plugin/`).

> Prototyp/Sandbox — noch nicht der produktive Skill.
