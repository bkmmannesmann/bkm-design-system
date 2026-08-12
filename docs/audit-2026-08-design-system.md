# Design-System-Audit (August 2026)

> Systematische Prüfung des Repos auf **veraltete/falsche Daten** und **Regeln, die
> Qualität deckeln**. Anlass: wiederholtes Gefühl, dass Seiten trotz korrekter
> Marken-Tokens „nicht herausragend" werden. Ergebnis vorweg: Das Gefühl ist
> berechtigt — das Repo enthält mehrere konkurrierende Wahrheiten, tote Verweise,
> defekte Assets und Regel-Muster, die generische Ergebnisse erzwingen.
>
> Methode: manuelle Prüfung von DESIGN.md/AGENTS.md/Assets, zwei parallele
> Audit-Durchläufe über docs/ und patterns/+skills/, `@google/design.md lint`,
> Abgleich mit Anti-Slop-Regelwerken (Impeccable, Taste-Skill). Die echte Website
> (bkm-mannesmann.de) war aus der Sandbox nicht erreichbar — Fakten, die nur dort
> verifizierbar sind, stehen unten als **offene Fragen**.

---

## A. Falsche oder widersprüchliche Fakten

| # | Befund | Fundstellen |
|---|--------|-------------|
| A1 | **Gründungsjahr/Alter driftet:** „established in 1928" vs. „96 Jahre" (= Stand 2024) vs. „Seit 1976" im Feuchte-Check-Prototyp. „500+ Fachbetriebe" ist nirgends belegt. | DESIGN.md:300, AGENTS.md:84, bkm-slide-prompt.md:167, prototypes/feuchte-check |
| A2 | **Firmen-Schreibweise:** Design-System durchgehend „BKM Mannesmann AG" — die realen Produkt-PDFs im Repo schreiben „**BKM.MANNESMANN AG**" (mit Punkt). | presentations/bkm-sp-express-*.pdf vs. alle .md |
| A3 | **Erfundener Logo-Claim:** assets/README.md behauptet, das Logo enthalte den Claim „Für eine lebenswerte Zukunft" — nicht in der Claim-Freigabeliste, widerspricht docs/logo.md und assets/logos/README.md. | assets/README.md:29 vs. docs/brand-voice.md:29-37 |
| A4 | **assets/README.md beschreibt ein Logo-System, das nicht existiert:** 4-5 gelistete Dateien (`bkm-logo-on-light.svg` …) gibt es nicht; die echten Varianten heißen anders und sind anders zugeordnet. | assets/README.md:31-37 vs. assets/logos/ |
| A5 | **Font-Assets defekt:** `Unbounded_400.woff2`, `_700` und `_900` sind **byte-identisch** (gleiche MD5) — es existiert nur ein Schnitt in drei Dateinamen. Zudem ist die Regular-Datei die Subfamilie „TT Norms Pro **Compact**", die Bold-Datei normal breit — Breiten-Mismatch im Fließtext. | assets/fonts/ |
| A6 | **Unbounded Italic existiert nicht** (Google-Font ohne Italic-Achse). Trotzdem fordern DESIGN.md:582/585 und AGENTS.md:200/204 „Unbounded Bold Italic" auf Titelfolien; 6 andere Dateien verbieten Kursiv als P0 (Faux-Italic). Der Root-Widerspruch liegt in DESIGN.md. | DESIGN.md:582 vs. PATTERN_CATALOG.md:295 u. a. |
| A7 | **Keyvisual in 4 Versionen normiert:** angeschnitten vs. „fully visible (not cropped)"; Breite 20 % / 22 % / Höhe 52 %; Opacity 0.15 / 0.18 / 0.85. Sogar DESIGN.md widerspricht sich selbst (Zeile 435 vs. 513). | DESIGN.md:435/513, AGENTS.md:64, docs/keyvisual.md:31, docs/bkm-slide-prompt.md:58 |
| A8 | **Zwei Sand-Töne für dieselbe Rolle:** `#f5f0eb` vs. `#f6f5f2`; DESIGN.md:569 kaschiert es als Spanne „#f5f0eb – #f6f5f2". | mehrere Dateien |
| A9 | **Oracal-Folientabelle:** Lime Green und Pure Green haben dieselbe Foliennummer (064G) — mindestens eine Zeile falsch. | docs/print-anwendungen.md:142-143 |
| A10 | **Logo-Position widersprüchlich:** „oben rechts" vs. „auf allen Printmedien links oben". | docs/bkm-slide-design-erkenntnisse.md:11 vs. docs/logo.md:23 |
| A11 | **AGENTS.md Quick-Start lädt keine Schrift:** Google-Fonts-Preconnect + Kommentar „replaced by the @font-face block above" — der Block existiert nicht (Editier-Rest). | AGENTS.md:20-25 |
| A12 | **MicroPorex®-Schreibweise inkonsistent:** mal mit ®, mal ohne; docs/microporex-und-technik.md (die Regel-Quelle) kennt das ® gar nicht. Zusätzlicher Claim „Powered by BKM Mannesmann" ist nicht freigegeben. | diverse |
| A13 | **Produkt-PDFs im Design-Repo:** `presentations/bkm-sp-express-tds.pdf` + `-va.pdf` sind Produktdatenblatt und Verarbeitungsanleitung (BKM SP Express) — Produktdokumentation, keine Design-Referenz. Kandidaten für Entfernung oder Verschiebung in ein Produkt-Repo. | presentations/ |

## B. Der Kern des Problems: Drei-vier konkurrierende Wahrheiten pro Regel

Ein Agent bekommt je nachdem, **welche Datei er zuerst liest**, andere Vorgaben:

| Thema | Wahrheit 1 | Wahrheit 2 | Wahrheit 3+ |
|-------|-----------|-----------|-------------|
| **Button-Schrift** | DESIGN.md-YAML: TT Norms Pro Bold 16px (label-lg) | DESIGN.md-Prosa:415 + digitale-medien.md:21: „Unbounded 900, Versalien" | AGENTS.md:92: Unbounded 14px (verletzt eigene 18px-Regel) |
| **H2–H6 Casing/Font** | DESIGN.md:338: Unbounded 900, sentence case | website/social/patterns: „uppercase, keine Ausnahmen" | assets/fonts/README.md: H2–H6 in **TT Norms Pro** |
| **Body-Font auf Slides** | DESIGN.md/ENGINE.md: TT Norms Pro Pflicht, self-hosted | STYLE_PRESETS.md:239: „Kein TT Norms Pro nötig — system-ui reicht" | bkm-website/SKILL.md lädt nur Unbounded via CDN |
| **Slide-Bühne** | ENGINE.md/QUICKSTART (v5): 1920×1080 (P0) | STYLE_PRESETS.md:337: 1280×720 („gültig in v5"!) | AGENTS.md: 100vw×100vh |
| **Glas-Radius** | DESIGN.md/AGENTS.md: 12px | tokens.css: 24px | STYLE_PRESETS: 16px, glass-ag/design.md: eigene Werte |
| **Lime im Fachbetrieb** | verboten (DESIGN.md:317, P0 in checklist) | STYLE_PRESETS.md:231/437 + bkm-slide-prompt v3: erlaubt | icon-system.md kennt keinen Fachbetrieb-Fall |
| **Fachbetrieb-Primärfarbe** | DESIGN.md: Pure Green, Flächen Weiß/Sand | bkm-website + bkm-social: „Stone Grey" als Primärfarbe | — |
| **Pure Green als Text auf hell** | Kontrastmatrix: FAIL, „NEVER" (DESIGN.md:505) | DESIGN.md:601 + AGENTS.md:222 schreiben es in den Folien-Anatomien selbst vor | STYLE_PRESETS/bkm-slide-prompt ebenso |
| **Glasmorphismus auf Folien** | referenz-analyse/erkenntnisse: „kommt im echten CD nicht vor" | PATTERN_CATALOG: „zentrales Element ALLER Slides" | DESIGN.md: „sparsam, 1–2 pro Viewport" |
| **Border-Left-Karten** | DESIGN.md: primäre Karten-Technik Slides/Print + dunkle Web-Karten | PATTERN_CATALOG.md:296: „verboten" | Anti-Slop-Standard: #1-KI-Tell im Web |
| **H1-Titelgröße** | Token: 72px | STYLE_PRESETS: 56px | DESIGN.md:582: „72–100px", glass-ag: ~118px |

Dazu **zwei gleichnamige Legacy-Prompts** (`bkm-slide-prompt.md` v2 im Root — unreferenziert, „flach + Border-Left"; `docs/bkm-slide-prompt.md` v3 — „Glas auf jeder Folie") mit gegensätzlichem Paradigma, beide von v5 abgelöst, nur einer als Legacy markiert.

## C. Regeln, die Qualität systematisch deckeln

1. **Pflicht-Eyebrow überall:** bkm-website schreibt für *jede* Sektion `[Label] → [Headline] → [Body] → [Cards]` vor; alle 15 Folientypen und alle 3 Social-Templates haben ein Pflicht-Eyebrow-Feld. Das uppercase Mikro-Label über jeder Überschrift ist das meistgenannte KI-Slop-Signal — hier ist es Systempflicht.
2. **Erzwungene Effekt-Rezepte:** Aurora + Noise als Default-Hero-Rezept (patterns/), Noise als „kritische Regel" bei Social, Pulse-Glow/Noise-Shimmer in animation-patterns.md (obwohl an anderer Stelle verboten), Spotlight-Glow als offizielles Web-Pattern. Ergebnis: Jede Seite bekommt dieselbe Effekt-Schicht statt einer eigenen Komposition.
3. **Ein Akzentwort pro Headline erzwungen** (AUTHORING.md:81) und **Zeilen-Zebra für alle Listen** — mechanische Wiederholung statt bewusster Ausnahme.
4. **„Nur Inhalt ersetzen, nie Layout":** QUICKSTART verbietet Layout-Varianz komplett; es fehlt die Stufe „Engine + Tokens übernehmen, Komposition neu".
5. **Ein einziges Hero-Muster im ganzen Repo** (Eyebrow → uppercase H1 → Lead → Lime-Button), 1:1 in Patterns kopiert. Keine Alternativen (Split, Foto-Full-Bleed, typografisch, Zahl-dominant).
6. **Quoten ohne Strategie:** „40 % Fotofläche, nie Stock" — aber nirgends steht, woher Bilder kommen (keine Motivliste, keine Prompt-Vorlagen, keine Bildbehandlungs-Regeln). In der Praxis: Platzhalter-Gradients oder Stock-Slop.

## D. Lücken (was für „herausragend" fehlt)

- **Bild-Strategie** (größte Lücke): Motivwelt, Bildbehandlung (Grading Richtung Deep Green?), Generierungs-Prompts, Alt-Text-Standard.
- **Layout-Varianz-Kapitel:** asymmetrische Raster, Full-Bleed, Rhythmus, wann Karten und wann Liste/Editorial — „Asymmetric, editorial layouts" steht als Prinzip ohne ein einziges Beispiel in DESIGN.md.
- **Hero-Komposition:** 3–4 erlaubte Hero-Familien statt einer.
- **Motion-Tokens für Web:** Dauer/Easing, Scroll-Reveal-Konzept, `prefers-reduced-motion`-Standard (DESIGN.md hat null Motion-Token, README behauptet „+ animations, responsive").
- **Responsive:** keine Breakpoints, keine fluide Typo-Skala definiert.
- **Anti-Slop-Checkliste für Web/Social** (existiert nur für Slides).
- **Ikonografie:** docs/icon-system.md wird von keinem Skill referenziert; stattdessen schreibt STYLE_PRESETS Font Awesome 6.0.0-**beta3** mit generischen Icons (fa-rocket, fa-bolt) vor.

## E. Veraltetes / Aufräumkandidaten

- `bkm-slide-prompt.md` (Root, v2): unreferenziert, widersprüchlich → löschen oder als Historie markieren.
- `docs/bkm-slide-prompt.md` (v3): trägt selbst keinen Legacy-Hinweis → Banner rein oder löschen.
- `skills/bkm-slides/STYLE_PRESETS.md`: „gültig in v5" ist falsch (1280×720-Werte, uppercase H2, 17px-Unbounded, „kein TT Norms nötig", Lime im Fachbetrieb) → gefährlichste Einzeldatei, neu ableiten oder auf Historie zurückstufen.
- `docs/verbesserungsvorschlaege.md`: ~83 % erledigt/verworfen, liest sich aber als offene Roadmap → Statusspalte oder Archiv-Marker.
- `docs/bkm-referenz-analyse-final.md`: Mangel-Report, dessen Punkte teils umgesetzt sind → Status ergänzen.
- `CHANGELOG.md`: verweist auf nicht existierendes `legacy/`-Verzeichnis und falschen Beispiel-Pfad; README-Badge 1.1.0 ohne Changelog-Eintrag; CONTRIBUTING nennt „CD-Richtlinien V2.8" (nirgends verankert).
- `presentations/bkm-sp-express-*.pdf`: Produktdokumentation → raus aus dem Design-Repo (oder eigener `product-docs/`-Bereich mit klarer Abgrenzung).
- `AGENTS.md`: kaputter Font-Quick-Start, `text-[#6b6b6b]` außerhalb der Palette, `font-medium/semibold` (Gewichte existieren nicht), 100vw/vh-Folien.

## F. Empfohlene Reihenfolge der Sanierung

1. **Fakten-Fragen klären** (siehe unten) — ohne sie lässt sich A1–A3 nicht korrigieren.
2. **DESIGN.md entwidersprüchlichen** (eine Wahrheit je Regel): Button-Typo, H2-Casing, Italic-Verbot, Keyvisual-Spec, Pure-Green-Textverbot auch in den Folien-Anatomien, ein Sand-Wert.
3. **STYLE_PRESETS.md ersetzen** (aus tokens.css/ENGINE.md neu ableiten) und die beiden Legacy-Prompts entfernen/markieren.
4. **Fachbetrieb-Farbfehler in bkm-website/bkm-social fixen** (Stone Grey → Pure/Transition Green auf hellen Flächen).
5. **Qualitätsbremsen lockern:** Eyebrow von Pflicht auf „max. 1 pro 3 Sektionen", Aurora/Noise/Glow von Default auf Opt-in, Akzentwort-Zwang und Zebra-Zwang streichen, Layout-Varianz-Stufe im Slides-Skill ergänzen.
6. **Fehlende Kapitel schreiben:** Bild-Strategie, Hero-Familien, Layout-Varianz, Motion-Tokens, Web-Anti-Slop-Checkliste.
7. **Assets reparieren:** echte Unbounded-Schnitte 400/700 beschaffen oder Dateien/Doku auf „nur 900" reduzieren; assets/README.md gegen die echten Logo-Dateien neu schreiben; PDFs verschieben.

## Offene Fakten-Fragen (nur extern verifizierbar)

1. Gründungsjahr / „seit"-Angabe: **1928**, **1976** oder beides (Firma vs. Feuchtigkeitsschutz-Sparte)?
2. Offizielle Schreibweise: „BKM Mannesmann AG" oder „**BKM.MANNESMANN AG**" (so in den Produkt-PDFs)?
3. Gehört der Claim „Für eine lebenswerte Zukunft" wirklich zum Logo?
4. Buttons im echten CD: TT Norms Pro Bold oder Unbounded, Versalien ja/nein?
5. H2–H6 im echten CD: Unbounded oder TT Norms Pro?
6. Existieren echte Unbounded-Schnitte 400/700 als Lizenz/Datei?
