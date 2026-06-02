# Prototyp: Fixed-Stage-Engine + 3 Design-Stufen

> Entscheidungs-Prototyp. Zeigt, wie das BKM-Slide-System aussehen könnte, wenn wir
> die **Engine** des Repos [`zarazhangrui/frontend-slides`](https://github.com/zarazhangrui/frontend-slides)
> übernehmen — **ohne** die Marke zu verlassen.

## Was du hier siehst

Öffne **`bkm-3-design-levels.html`** im Browser (Doppelklick reicht, keine Installation).
Navigation: Pfeiltasten ← →, Leertaste, Ziffern 1–7, Wischen auf dem Handy, oder die
Buttons unten.

Dieselbe BKM-Botschaft („Dichtungstechnik") wird in **drei Design-Stufen** gezeigt —
alle 100 % in BKM-Farben (Deep Green, Lime, Sand, Pure Green) und der Marken-Schrift
Unbounded:

| Stufe | Charakter | Wofür |
|-------|-----------|-------|
| **01 · Glas** | Heutiger BKM-Stil. Frosted-Glass auf Deep Green, ruhig & seriös. | Produkt-/Kunden-Decks, Datenblätter, Standard |
| **02 · Editorial** | Mehr Design: große Typo, Regelwerk-Linien, Kennzahlen-Kacheln. | Strategie, Investor-Updates, Magazin-Charakter |
| **03 · Bold Poster** | Maximale Signalwirkung: Übergröße + Lime-Akzent. | Pitches, Messen, Vision & Manifest |

**Sinn des Prototyps:** Du warst unsicher, wie streng die Marke bleiben soll.
Statt das abstrakt zu diskutieren, kannst du jetzt *sehen*, wie weit „mehr Design"
gehen kann, ohne die BKM-Identität zu verlieren — und dann entscheiden, welche
Stufen wir ins System aufnehmen.

## Was die neue Engine technisch bringt

Übernommen aus `frontend-slides` (markenneutral, reines Plus):

- **Fixed-Stage 1920×1080** — die Folie wird als Ganzes in den Bildschirm skaliert
  (Letterbox). Sieht auf Beamer, Laptop und Handy **identisch** aus; nichts „verrutscht".
- **Druck/PDF** — `@media print` legt eine Folie pro Seite an → sauberer PDF-Export.
- **Navigation** — Tastatur, Touch-Swipe, Klick-Steuerung, Sprungziffern.
- **`prefers-reduced-motion`** — Barrierefreiheit out of the box.

Im vollen Skill kommen später dazu (siehe Fahrplan): **PPTX-Import**, **1-Klick-Deploy
auf eine Live-URL** und **screenshot-basierte Qualitätsprüfung** (Overflow/Overlap
automatisch erkennen statt nur Checkliste).

## Herkunft & Lizenz

- Engine-Konzept (Fixed-Stage, viewport-base.css, deck-stage.js, Workflow-Philosophie):
  [`zarazhangrui/frontend-slides`](https://github.com/zarazhangrui/frontend-slides) (MIT).
- „Editorial"-Stufe ist inspiriert von der grün-basierten `emerald-editorial`-Vorlage
  des Bold-Template-Packs, **neu interpretiert in BKM-Farben** — kein Code 1:1 kopiert.
- Alle Farben/Schriften/Logos: BKM Mannesmann `DESIGN.md`.

## Vorgeschlagener Fahrplan (zur Abstimmung)

1. **Prototyp abnehmen** → entscheiden, welche Stufen (01/02/03) ins System kommen.
2. **`viewport-base.css` + Stage-Controller** als gemeinsame Basis in `skills/bkm-slides/` aufnehmen.
3. **`html-template.md` erweitern**: die gewählten Stufen als kopierbare 1920×1080-Templates.
4. **Skript-Ebene** übernehmen: `export-pdf.sh`, `deploy.sh`, `extract-pptx.py`.
5. **Skill als Plugin** verpacken (`.claude-plugin/`) — parallel zur GitHub-URL-Nutzung.
6. **Auto-QA** (Screenshot-Check) in den Pflicht-Workflow aufnehmen.

> Dieser Ordner ist ein Prototyp/Sandbox — noch nicht der produktive Skill.
