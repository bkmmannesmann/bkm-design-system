# BKM Slides — Self-Check-Checkliste

> **PFLICHT vor Auslieferung.** Nach dem Bauen eines Decks (Screenshot ansehen!) diese
> Liste durchgehen. **Jedes P0 muss bestehen** — solange ein P0 fehlschlägt, wird das
> Deck NICHT ausgeliefert, sondern erst korrigiert. P1 stark empfohlen, P2 Feinschliff.
>
> Idee adaptiert aus Open Design (nexu-io/open-design, Apache-2.0): P0/P1/P2-Self-Check.

## P0 — kritisch (muss bestehen)

- [ ] **Nur BKM-Farben** — keine fremden Hex-Werte (Deep Green `#1c4b42`, Lime `#b4e717`,
      Pure Green `#4daf46`, Transition Green `#287d4b`, Sand/Paper, Stone Grey).
- [ ] **Headlines Unbounded 900**, UPPERCASE **oder** Mixed-Case — **nie kursiv**, keine Fremd-Akzentschrift.
- [ ] **Lime nur als Signal** (Akzentwort/Zahl/Mark/Button/ein Highlight-Block) — **nie** als
      dekorative Vollfläche; **kein Lime im Fachbetrieb-Kontext**.
- [ ] **Fixed-Stage-Shell unverändert** (1920×1080, als Ganzes skaliert; `ENGINE.md`).
- [ ] **Kein Überlauf, keine Überlappung**, kein Text unter Lesegröße (Screenshot prüfen).
- [ ] **Richtiges Logo im Kontext** (dunkel = white-puregreen, hell = stonegrey-puregreen),
      nicht umgefärbt/verzerrt.

## P1 — wichtig (stark empfohlen)

- [ ] Genau **eine** `design.md` gelesen → Deck ist in **einer** Familie konsistent.
- [ ] **8px-Rundung** für Flächen-Elemente (Tags, Kacheln, Karten, Buttons); Glas-Cards 24px; Linien bleiben Linien.
- [ ] **Fachbetrieb-Text in Transition Green** (Deep Green dort nur für Flächen/Button).
- [ ] Eyebrow/Labels/Footlines **UPPERCASE**, ≥0.12em Tracking.
- [ ] **Großzügiger Weißraum** — mind. ~25 % der Fläche bleibt leer.
- [ ] **Eine dominante Sache pro Folie** (kein konkurrierender Doppel-Fokus).

## P2 — Feinschliff

- [ ] Reveal-Verzögerungen sinnvoll gestaffelt (`.d1`–`.d4`).
- [ ] Chrome (Logo, Rubrik, Seitenzahl) über alle Folien konsistent.
- [ ] Akzentwort bewusst auf das Schlüsselwort gesetzt (nicht beliebig).
- [ ] Dichte-Modus passt zum Anlass (Vortrag = wenig/groß, Lesen = strukturierte Grids).

---

## 5-Dimensionen-Selbstkritik (nach bestandener P0-Liste)

Bewerte das Deck still auf einer Skala 1–5 in fünf Dimensionen. **Alles unter 3/5 ist eine
Regression** → schwächste Dimension nachbessern, neu bewerten. Zwei Durchläufe sind normal.

1. **Marke/Philosophie** — Sieht es unverkennbar nach **BKM** aus (nicht generisch-„AI")?
2. **Hierarchie** — Klare Lesereihenfolge? Eine dominante Aussage pro Folie?
3. **Ausführung** — Sauber: Ausrichtung, Abstände, kein Überlauf/Überlappung?
4. **Spezifität** — Echte, konkrete Inhalte/Zahlen statt Platzhalter-/Stat-Slop?
5. **Zurückhaltung** — Ein Akzent sparsam (max. 2×/Folie)? Genug Weißraum? Nicht überladen?

Erst wenn alle Dimensionen ≥ 3/5 sind: ausliefern.
