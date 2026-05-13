# BKM Referenz-Analyse — Was das echte BKM-Design ausmacht

## Was ich aus den Referenzbildern sehe

### 1. Website-Hero ("DEIN WEG ZUR TROCKENEN WAND")
- Deep Green Vollflächenhintergrund
- Headline in Unbounded BOLD UPPERCASE — Weiß + Lime für Akzentwörter
- Body in heller Schrift, zentriert
- Subtiler Lime-Chevron als Scroll-Indikator
- KEIN Noise, KEIN Gradient, KEIN Pattern — purer Deep Green, sauber, selbstbewusst

### 2. A4-Broschüre Deckblatt (3 Varianten)
- Logo oben links (Stone Grey + Pure Green Variante auf Weiß)
- Headline: Unbounded BOLD UPPERCASE, Schwarz auf Weiß
- Akzent-Subline: "Schimmel | Nasse Wände | Feuchte Keller" in BOLD Pure Green
- Body: TT Norms Pro Regular, Schwarz
- GROSSES FOTO: Haus/Architektur, nimmt 50-60% der Seite ein
- KEYVISUAL: Die drei Chevrons (Pure Green + Deep Green) rechts am Bildrand, überlappend
- Logo unten links (bei einer Variante)
- VIEL WEISSRAUM — die Seite atmet

### 3. Newsletter-Sektion ("FEUCHTE WÄNDE? WIR HABEN DIE LÖSUNG")
- Deep Green Hintergrund
- Headline: Unbounded BOLD UPPERCASE, Weiß + Lime für Akzentzeile
- Body: TT Norms Pro Regular, helles Grün/Weiß
- Rechts: Weißes Formular-Card (Newsletter)
- Button: Deep Green Hintergrund, Unbounded BOLD UPPERCASE

### 4. Broschüre Innenseiten (Look & Feel)
- Weißer Hintergrund dominant
- Headlines: Unbounded BOLD UPPERCASE, Schwarz/Deep Green
- Subheadlines: TT Norms Pro Bold, Pure Green
- Body: TT Norms Pro Regular, Schwarz, Mehrspaltiger Satz (Zeitungs-Layout)
- GROSSE FOTOS: Echte Menschen, echte Situationen (Paar vor feuchter Wand, Handwerker, Frau mit grünen Haaren)
- Keyvisual-Chevrons: Am rechten Rand, überlappend über Bilder
- Seitenzahlen unten

## Was im Design System FEHLT oder FALSCH ist

### A. Das Keyvisual als Designelement
- Im Design System wird das Keyvisual als "dekoratives Element" beschrieben
- In der REALITÄT ist es ein ZENTRALES Layoutelement — es überlappt Bilder, definiert den rechten Rand, schafft Dynamik
- Es ist NICHT optional, es ist IDENTITÄTSSTIFTEND
- Die Chevrons brechen bewusst aus dem Grid aus — das gibt dem Design Spannung

### B. Fotografie als Hauptelement
- Meine bisherigen Slides: Text-dominant mit dekorativen Elementen
- BKM-Realität: FOTOS sind das Hauptelement, Text ist sekundär
- Große, emotionale, ganzseitige oder halbseitige Fotos
- Echte Menschen, echte Situationen — nicht abstrakt

### C. Weißraum-Philosophie
- Meine Slides: Jeder Quadratzentimeter gefüllt (Cards, Grids, Badges)
- BKM-Realität: MASSIVER Weißraum, die Seite atmet
- Wenige Elemente, aber jedes hat Gewicht
- Kein Noise, kein Aurora, keine Texturen — SAUBERE Flächen

### D. Typografie-Hierarchie
- Meine Slides: Zu viele Größenstufen, zu viele Gewichte
- BKM-Realität: Nur 3 klare Stufen:
  1. Unbounded BOLD UPPERCASE — riesig, dominant (Headlines)
  2. TT Norms Pro Bold — mittelgroß, Pure Green (Subheadlines/Akzente)
  3. TT Norms Pro Regular — klein, Schwarz/Weiß (Body)
- KEINE Geist Mono, KEINE Monospace-Zahlen
- Zahlen werden in Unbounded oder TT Norms Pro Bold gesetzt

### E. Farbverwendung
- Meine Slides: Zu viele Farben gleichzeitig, Noise-Texturen, Gradients
- BKM-Realität: 
  - Helle Slides: Weiß + Schwarz + Pure Green Akzente
  - Dunkle Slides: Deep Green + Weiß + Lime Akzente
  - KEIN Gradient, KEIN Noise, KEIN Aurora
  - Farbe wird SPARSAM eingesetzt — nur für Akzente

### F. Layout-Prinzip
- Meine Slides: Symmetrische Grids, gleichmäßig verteilt
- BKM-Realität: Asymmetrisch, editorial, magazinartig
  - Große Flächen vs. kleine Details
  - Bilder brechen aus dem Raster
  - Keyvisual überlappt
  - Mehrspaltige Texte wie in einem Magazin

## Was sich im Design System ändern muss

1. **Keyvisual-Regeln**: Von "optional dekorativ" zu "zentrales Layoutelement mit Überlappungsregeln"
2. **Fotografie-Regeln**: Mindestens 40% der Slide-Fläche muss Bild sein
3. **Weißraum**: Mindestens 25% der Fläche muss leer bleiben
4. **Noise/Aurora/Gradient ENTFERNEN**: Nicht BKM. Saubere Flächen.
5. **Typografie vereinfachen**: Nur 3 Stufen, keine Monospace
6. **Farbregeln verschärfen**: Max. 3 Farben pro Slide
7. **Layout-Regeln**: Editorial/Magazin-Stil statt Dashboard-Stil
8. **Chevron-Überlappung**: Als CSS-Pattern dokumentieren
