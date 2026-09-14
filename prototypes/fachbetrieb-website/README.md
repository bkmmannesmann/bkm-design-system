# Prototyp bkm-duesseldorf.de – Fachbetriebs-Website

Pilot für die rund 40 Fachbetriebs-Websites aus `Fachbetriebs-Websites_Baukasten_v1.md`.
Produktionsziel ist WordPress mit Astra und Elementor Standard; dieser Prototyp ist die
gestalterische Vorlage, aus der die Astra-Customizer-Vorgaben abgeleitet werden.

## Dateien

| Datei | Zweck |
|-------|-------|
| `style.css` | Das gesamte Design. Ganz oben der `:root`-Block mit allen Tokens. |
| `fonts/` | Unbounded (Variable Font) und TT Norms Pro, selbst gehostet. |
| `assets/` | Keyvisual, BKM-Logo und Phosphor-Icons aus dem Designsystem. |
| `index.html` | Startseite. Ohne eigenen `<head>` — den ergänzt die Artifact-Plattform. |
| `leistungen.html`, `diagnose.html`, sechs Leistungsseiten | Vollständige HTML-Dateien. |
| `build.py` | Erzeugt alle Seiten neu. `python3 build.py`, keine Abhängigkeiten. |
| `Fachbetriebs-Websites_Baukasten_v1.md` | Textquelle für die Leistungsseiten (Teil F.1–F.6). |

Nur am Design arbeiten: `style.css` ändern, Seite neu laden. Texte oder Struktur ändern:
`build.py` bzw. den Baukasten anfassen und neu bauen.

## Bildsprache

Die Gestaltung folgt dem BKM Feuchte-Check und dem Support-Cockpit: dunkle
Bänder mit Noise-Textur, Verlaufswäsche und angeschnittenem Keyvisual am
rechten Rand; Karten mit Schatten-als-Rahmen, die beim Hover anheben; Buttons
mit mitwanderndem Pfeil; der Ablauf als bebilderte Schrittfolge mit
Nummernplakette und Verbindungslinie; FAQ als Karten, deren Plus zum Kreuz
dreht; Einblenden beim Scrollen.

Beide Vorlagen stehen in Deep Green, weil sie die BKM Mannesmann AG betreffen.
Hier ist der Fachbetrieb der Absender, deshalb Transition Green. Drei Stellen
ließen sich dabei **nicht** eins zu eins übernehmen — Transition Green ist
heller als Deep Green:

| Vorlage (Deep Green) | Hier (Transition Green) | Grund |
|---|---|---|
| Fließtext `rgba(255,255,255,.72)` | `#edf5f0` | .72 Weiß ergibt auf Transition Green nur 3.47:1 |
| Eyebrow und Zwischentitel in Lime | Weiß | Lime auf Transition Green sind 3.49:1 — als Text zu wenig |
| Glas-Karten auf dem dunklen Band | massive helle Karten | Weiß auf Glas über Transition Green sind 4.39:1 |

Lime bleibt, wo es trägt: als CTA-Fläche mit Deep-Green-Beschriftung (6.74:1),
als Häkchen auf dem dunklen Band und als Fokusring auf Grün. Als Textfarbe
funktioniert es nur auf Deep Green (6.74:1) — also im Footer.

Die animierten Aurora-Blobs der Vorlage sind dort ausdrücklich als „nur BKM AG"
gekennzeichnet. Hier steht stattdessen dieselbe Lichtführung als ruhende
Verlaufswäsche (`.wash`): gleiche Wirkung, kein Dauerlauf auf der GPU.

## Farbkontext: Fachbetrieb

Die Tokens folgen dem Fachbetriebs-Kontext aus `DESIGN.md` des Designsystems — nicht dem
BKM-AG-Kontext. Die Rollenverteilung ist dort verbindlich festgelegt:

| Farbe | Rolle |
|-------|-------|
| Weiß + Sand White `#f6f5f2` | Die dominierenden Flächen. Der Kontext ist bewusst hell und offen. |
| Transition Green `#287d4b` | Headlines, Links, Buttons, Header-Band. Alles, was Text trägt. |
| Pure Green `#4daf46` | Identitätsakzent: Kanten, Marker, Icons, Hover. **Nie als Text** (2.79:1 auf Weiß). |
| Stone Grey `#494949` | Fließtext. Nie als dominante Fläche. |
| Deep Green `#1c4b42` | Nur im Footer, als Rückbezug auf BKM Mannesmann. |
| Lime `#b4e717` | Nur auf Deep Green (6.74:1). Auf Weiß und Transition Green zu kontrastarm. |

Jeder Farbwert im `:root` trägt den geprüften Kontrastwert als Kommentar. Wer einen Wert
ändert, sollte den Kontrast neu rechnen — besonders bei allem, was Text trägt.

## Schriften

Unbounded (Display) und TT Norms Pro (Body) liegen als woff2 in `fonts/` und werden per
`@font-face` eingebunden. Kein CDN: `assets/fonts/README.md` im Designsystem verlangt
ausdrücklich Selbsthosting für Unbounded.

Zwei Punkte, die vor dem Rollout zu klären sind:

- **TT Norms Pro ist proprietär** („Nur für interne Nutzung und BKM-Projekte"). Ob die
  Lizenz 40 öffentliche Websites deckt, deren Anbieter jeweils der Fachbetrieb ist,
  muss geprüft werden. Unbounded ist Google Fonts (OFL) und unkritisch.
- **Der Body-Schnitt mischt zwei Breiten:** `TT_Norms_Pro_Compact_Regular.woff2` ist der
  Compact-Schnitt, `TT_Norms_Pro_Bold.woff2` der normal breite. Fetter Text läuft dadurch
  etwas breiter als der Grundtext. Beide Dateien kommen so aus dem Designsystem.

### Beim Veröffentlichen als Artifact beachten

`index.html` referenziert die Schriften relativ (`fonts/*.woff2`). Lokal und in WordPress
funktioniert das. Auf der Artifact-Plattform werden nur mitveröffentlichte Dateien
ausgeliefert — die drei woff2 aus `fonts/` müssen also als Begleitdateien mitgegeben
werden, sonst fällt die Seite dort auf Systemschriften zurück und sieht nicht aus wie
dieser Prototyp.

## H1 und lange SEO-Headlines

Die H1 aus dem Baukasten sind lange lokale SEO-Headlines („Feuchte Wände im Rheinland?
Dein BKM-Fachbetrieb für Mauertrockenlegung und Kellersanierung in Düsseldorf" — 105
Zeichen). `DESIGN.md` sieht für H1 Unbounded 900 in Versalien vor. In dieser Länge ist das
nicht lesbar. Der Prototyp setzt H1 deshalb in Unbounded 800, gemischt, bei
`clamp(1.55rem, 2.7vw, 2.15rem)`.

Der saubere Weg wäre, die H1 im Baukasten zu kürzen und den SEO-Teil in die Unterzeile zu
nehmen. Das ist eine Textentscheidung und steht in Teil B.4 des Baukastens an.

## Geprüft

- Kontrast: alle Text-Hintergrund-Paare auf allen neun Seiten erfüllen WCAG AA
  (4.5:1, große Schrift 3:1) — automatisch gegen den gerenderten DOM gemessen,
  bei 1280 px und bei 390 px.
- Kein horizontaler Überlauf: 99 Kombinationen aus neun Seiten und elf Breiten
  von 320 bis 1600 px. Ohne `overflow-x:hidden` — die Ursachen sind behoben,
  nicht verdeckt.
- Ohne JavaScript bleibt nichts unsichtbar: das Einblenden beim Scrollen greift
  erst, wenn das Skript die Klasse `js` gesetzt hat. Fällt es aus, steht alles
  da. Dasselbe gilt bei `prefers-reduced-motion` und im Druck.
- Mobile Navigation: `<details>`-Menü ohne JavaScript, ab 1080 px abwärts.
  In der Produktion übernimmt das der Astra-Header.
- Der Build ist reproduzierbar: `python3 build.py` erzeugt neunmal dieselben
  Dateien.

## Assets

Keyvisual, Logo und Icons kommen aus dem Designsystem. Die vier SVG aus
`assets/keyvisual/` und `assets/logos/` tragen dort je rund eine halbe
Megabyte Illustrator-Rohdaten in einem `<metadata>`-Block mit sich (ein
base64-CDATA für `i:aipgf`). Für die Website sind sie entfernt: 1,8 MB werden
zu 36 KB, das Rendering ist identisch. Das lohnt sich auch im Designsystem
selbst.
