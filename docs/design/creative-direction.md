# Creative Direction — BKM Mannesmann Website

> Output 3. Baut auf `DESIGN.md` (verbindliche Tokens) und `website-strategy.md` auf.
> Aufgabe dieses Dokuments: die Markenwelt in eine **unverwechselbare digitale Gestaltungssprache** übersetzen — jenseits von „grüne SaaS-Website".

## 1. Design Principles

Fünf Prinzipien, gegen die jede Gestaltungsentscheidung geprüft wird:

### P1 — Bauphysik als Bildsprache
BKM verkauft keine Software, sondern Schutz für Mauerwerk. Die Gestaltung nutzt daher die Rohstoffe der Bauphysik: Wandschnitte, Feuchtigkeitsverläufe, Kapillarität, Schichtaufbauten, Materialoberflächen. **Diagramme sind bei BKM keine Dekoration, sondern Inhalt.**

### P2 — Die Sperrschicht als Formprinzip
Der harte horizontale Schnitt zwischen dunklen und hellen Flächen (bereits in `DESIGN.md` verankert) ist die visuelle Metapher der Horizontalsperre: unten Deep Green (feucht), oben hell (trocken). Sektionen wechseln hart, nie mit Verläufen. Dieses Prinzip trägt die gesamte Seitenrhythmik.

### P3 — Ruhige Autorität statt Lautstärke
Ein Hersteller mit Geschichte seit 1928 muss nicht schreien. Große, sichere Typografie (Unbounded 900), viel Weißraum, wenige, präzise Akzente. Kein Element existiert, um zu beeindrucken — jedes, um zu erklären oder zu führen.

### P4 — Ehrliche Führung
Das Zwei-Wege-Prinzip ist auch ein Gestaltungsprinzip: Die Seite bevormundet nicht, sie legt beide Wege offen — inklusive der ehrlichen Aussage, wann DIY nicht reicht. Vertrauen entsteht durch nachvollziehbare Empfehlungen, echte Prüfsiegel, echte Betriebe. **Keine erfundenen Zahlen, Testimonials oder Awards — nirgends.**

### P5 — Präzision ohne Sterilität
Technische Kompetenz (Spec-Tabellen, Maße, exakte Werte in TT Norms Pro) trifft auf warme Materialität (Sand White, Fotografie von echten Wänden, Händen, Baustellen). Das Sand-Weiß und die Du-Ansprache halten die Präzision menschlich.

## 2. Referenz-Extraktion (aus dem Source-Audit)

Aus den Inspirationsquellen werden **Prinzipien** extrahiert, keine Layouts kopiert:

- **Editorial-/Awwwards-Ebene:** asymmetrische Kompositionen, typografischer Mut, ein starkes Bild statt drei mittelmäßiger Cards.
- **Vercel/Technik-Referenzen (bereits in `docs/referenzen.md`):** Shadow-as-Border, klare Spec-Tabellen, ruhige Interaktionen.
- **Emil-Kowalski-Schule (Motion):** wenige, kurze, physikalisch plausible Bewegungen; Animation als Feedback, nicht als Show; `prefers-reduced-motion` immer respektiert.
- **Ponytail-Prinzip (Engineering):** kleinste robuste Lösung; Browser-native Mittel vor Libraries.

## 3. Drei Creative Directions

### Direction A — „Material Intelligence"
**These:** Die Website fühlt sich an wie das Material, das sie schützt.
Makrofotografie von Mauerwerk, Putz, Beton als große Flächen; Texturen aus `assets/backgrounds/` als subtile Oberflächen; Sektionen wie geschichtete Bauteile. Typografie sitzt auf „Material", nicht auf Weiß.
- Stärken: maximale Differenzierung von SaaS-Ästhetik, sinnlich, premium.
- Schwächen: fotografieabhängig (Beschaffungsrisiko), Gefahr visueller Schwere, Lesbarkeit auf Textur erfordert Disziplin, mobil schwer zu verdichten.

### Direction B — „Building Science Editorial"
**These:** Die Website ist ein präzise gestaltetes Fachmagazin über das eigene Haus.
Editoriale Layouts mit starker Typo-Hierarchie, große erklärende **Informationsgrafiken** (Wandschnitt, Feuchtigkeitsverlauf, Systemaufbau) als Hero-Elemente, Zahlen und Fakten als gestaltete Elemente, viel Sand White, Fotografie dokumentarisch statt werblich.
- Stärken: erklärt am besten (Kernjob J1/J2), baut Autorität auf, funktioniert exzellent mit SEO-/Ratgeber-Strategie, wenig fotografieabhängig (Diagramme sind selbst erzeugbar und markeneigen), skaliert auf alle Seitentypen, sehr performant (SVG statt WebGL).
- Schwächen: erfordert wirklich gute Diagramme; bei schwacher Umsetzung droht Lehrbuch-Trockenheit.

### Direction C — „Engineered Protection"
**These:** Industrielle Reduktion — die Website als Präzisionswerkzeug.
Strenges Raster, harte Kanten (Radius 0–4px), monochrome Deep-Green-Welt mit Lime als einzigem Signal, technische Labels, fast keine Fotografie.
- Stärken: unverwechselbar hart, sehr konsistent, schnell.
- Schwächen: emotional kalt für verunsicherte Hausbesitzer (N1!), Home-Line-Wärme („Novu", Du-Ansprache) passt schlecht, Distanz statt Reassurance.

### Bewertung

| Kriterium | A Material | B Editorial | C Engineered |
|-----------|:---:|:---:|:---:|
| BKM Fit (Marke + beide Linien) | 4 | **5** | 3 |
| Differenzierung | 5 | **5** | 4 |
| Vertrauen | 4 | **5** | 3 |
| Verständlichkeit | 3 | **5** | 3 |
| Premiumwirkung | 5 | **4** | 4 |
| Skalierbarkeit auf alle Seiten | 3 | **5** | 4 |
| Mobile | 3 | **5** | 4 |
| Performance | 3 | **5** | 5 |

## 4. Finale Direction: „Building Science Editorial" mit Material-Akzenten

**B als Fundament, geschärft mit dem stärksten Element aus A:** An wenigen, hochwirksamen Stellen (Hero, Sektionsübergänge, Kapitel-Openings) tragen Flächen echte Materialtextur (vorhandene Assets) — dosiert, nie unter Fließtext. C liefert die Disziplin: strenges Raster, Radius-Zurückhaltung, technische Labels.

**Kurzformel:** *Ein präzises Fachmagazin über dein Haus — gedruckt auf dem Material, um das es geht.*

Die Entscheidung folgt dem Projektziel, nicht dem Geschmack: Die wichtigste Aufgabe der Website ist **Verstehen und Vertrauen bei verunsicherten Laien** (J1, J2, J6). Direction B bedient genau das, differenziert maximal von SaaS-Ästhetik (Informationsgrafiken statt Feature-Cards) und ist zugleich die performanteste und am besten skalierbare Richtung.

## 5. Signature Elements

Fünf reproduzierbare, BKM-eigene Muster — Bestandteil des Design Systems (Definition in `DESIGN.md`):

### S1 — Der Wandschnitt (Sektionsdiagramm)
Ein markeneigenes SVG-Diagrammsystem: stilisierter Querschnitt durch Mauerwerk/Boden mit Feuchtigkeitszone (Deep Green), Sperrschicht (Lime-Linie) und trockener Zone (Sand/Pure Green). Wird für Ursachen, Systemaufbauten und den Feuchte-Check wiederverwendet. Feste Farbcodierung = die Grün-Geschichte der Marke.

### S2 — Die Sperrschicht-Kante (Section Transition)
Der harte Dunkel-/Hell-Schnitt zwischen Sektionen, markiert durch eine 4px-Lime-Linie an ausgewählten Übergängen (max. 1–2 pro Seite). Digitale Übersetzung der Horizontalsperre und der vertikalen Lime-Linie aus dem Editorial-Design.

### S3 — Die Zwei-Wege-Weiche
Das wiederkehrende Entscheidungsmodul am Ende jeder Problem-/Ratgeberstrecke: zwei gleichwertige Panels (Selbst sanieren / Fachbetrieb), getrennt durch eine vertikale Linie, überschrieben mit „Zwei Wege. Ein Ziel." Identische Anatomie überall — die Nutzer lernen das Muster.

### S4 — Das Diagnose-Interface (Feuchte-Check)
Geführte Selbstdiagnose in BKM-Formsprache: große Antwortkarten mit Schadensbild-Piktogrammen (Icon-System: Kreis, Deep Green, Lime-Linie), Fortschritt als horizontale „Trocknungslinie" von Deep Green zu Pure Green.

### S5 — Der Messwert-Block (Technical Label System)
Technische Beweise als gestaltetes Element: Label in TT Norms Pro Bold uppercase 13px, Wert groß in Unbounded, Einheit in TT Norms Pro — immer mit Hairline-Divider. Ersetzt generische „Stat-Cards" und zieht sich durch Produkt-, System- und Unternehmensseiten.

## 6. Bildsprache (Image Direction)

- **Motive:** echte Gebäude (Altbau, Keller, Fassade), Hände bei der Verarbeitung, Materialoberflächen im Makro, dokumentarische Vorher/Nachher-Paare. Menschen: konzentriert arbeitend oder erleichtert im trockenen Raum — nie gestellte Stock-Lächel-Szenen.
- **Perspektive:** frontal und ruhig (Architektur), nah und haptisch (Material/Verarbeitung). Keine Drohnen-Spektakel.
- **Licht/Grade:** natürlich, leicht warm; Schatten dürfen existieren (Materialehrlichkeit). Kein HDR, keine Neonfarben, keine violetten AI-Looks.
- **Technische Visuals:** das Wandschnitt-System (S1) in fester Farbcodierung; Datenvisualisierung nur mit echten Werten.
- **Platzhalter-Regel:** Solange echte Fotografie fehlt, werden neutrale Material-/Diagramm-Platzhalter genutzt — niemals generische Stock-SaaS-Illustrationen.

## 7. Motion-Haltung (Kurzfassung — System in `DESIGN.md`)

Die Seite muss ohne jede Animation hervorragend aussehen. Motion dient Orientierung, Hierarchie, Feedback, Erklärung — insbesondere: das langsame „Trocknen" des Wandschnitts (S1) als erklärende Animation, sanfte Reveals bei Sektionseintritt (einmalig, kurz, ≤600ms), Feedback auf Interaktion (≤200ms). Kein Scroll-Hijacking, kein Parallax als Deko, keine Marquees. `prefers-reduced-motion` schaltet alle nicht-essenziellen Bewegungen ab.
