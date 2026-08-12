# IST-Zustand — BKM Mannesmann Digital (Phase 0)

> Stand: August 2026. Dieses Dokument hält den vorgefundenen Zustand fest, **bevor** Designentscheidungen für die Website getroffen wurden. Es ist die Referenz dafür, was bereits existiert, was verbindlich ist und was nicht stillschweigend verändert werden darf.

## 1. Dieses Repository (`bkm-design-system`)

Das Repository ist ein **Design-System- und Asset-Repository** — kein Website-Codebase. Es enthält keinen Anwendungscode, kein `package.json`, keinen Build-Prozess. Alle bisherigen HTML-Artefakte (Präsentationen, Prototypen, Showrooms) sind self-contained.

### Verbindliche Grundlagen (bereits vorhanden, gelten weiter)

| Quelle | Inhalt | Status |
|--------|--------|--------|
| `DESIGN.md` (v1.1.0) | Vollständige Token-Definition: Farben, Typografie, Radius, Spacing, Komponenten, Kontrastmatrix, Logo-/Keyvisual-Regeln | **Normativ.** Wird für die Website erweitert, nicht ersetzt. |
| `AGENTS.md` | Code-Übersetzungsschicht: CSS-Variablen, Tailwind-Theme, Komponenten-Patterns, Checklisten | Normativ für Implementierung |
| `docs/brand-voice.md` | Tonalität (kompetent / nahbar / motivierend), Du-Ansprache auf Website, freigegebene Claims | Normativ für Copy |
| `docs/digitale-medien.md` | Web-Richtlinien: Header hell, Top-Bar Lime, Footer Deep Green, CTA-Regeln, WebP | Normativ |
| `docs/logo.md`, `docs/keyvisual.md`, `docs/icon-system.md` | Asset-Verwendungsregeln | Normativ |
| `docs/microporex-und-technik.md` | Ingredient Brand MicroPorex, 3-Phasen-Wirkung, Naming, Firmenname-Schreibweisen | Normativ |
| `assets/` | Logos (4 Varianten, SVG+PNG), Keyvisual (hell/dunkel), Fonts (Unbounded 400/700/900, TT Norms Pro Regular/Bold, woff2), Hintergrund-Texturen | Produktionsfertig, selbst gehostet |

### Zentrale, bereits entschiedene Designprinzipien

1. **Ein System, zwei Farbkontexte:** BKM AG (Deep Green + Lime auf dunklen Flächen) und Fachbetrieb (Weiß/Sand White mit Transition/Pure Green; Stone Grey nur als Textfarbe).
2. **Die Grün-Geschichte:** Deep Green = Feuchtigkeit/Problem → Transition Green = Trocknungsprozess → Pure Green = trockener Endzustand. Die Palette visualisiert den Trocknungsprozess — das ist Markensubstanz, kein Styling.
3. **Lime (#b4e717) = ausschließlich interaktiv** (BKM-AG-Kontext), nie dekorativ, nie als Text auf hellen Flächen.
4. **Harte Schnitte** zwischen dunklen und hellen Flächenbändern — nie Verläufe, Wellen oder Diagonalen. Der harte Schnitt ist die visuelle Metapher der Sperrschicht.
5. **Shadow-as-Border** für Cards im Web (keine CSS-Border), Border-Left-Technik nur editorial/Print.
6. **Unbounded 900** nur ≥18px; H1 uppercase, H2+ sentence case. TT Norms Pro für alles andere.
7. **Keyvisual ist ein Bild-Asset** — wird niemals in Code nachgebaut.
8. **Max. ein Primary Button pro Viewport-Fold.**
9. Kontrastmatrix WCAG-AA-geprüft; Pure Green und Lime sind auf hellen Flächen als Text verboten.

### Was im Repository fehlt (Lücken, die dieses Projekt schließt)

- Kein Website-Code, keine Informationsarchitektur, keine Seiten-Blueprints.
- Kein responsiver Type-Scale (nur Desktop-Pixelwerte in `DESIGN.md`).
- Kein Layout-/Grid-/Breakpoint-System für Web.
- Keine Motion-Language (nur Slide-Animationspatterns im Slide-Skill).
- Keine Bildsprache-Definition für Web (nur Editorial-Fotoregeln für Slides).
- `skills/bkm-website/SKILL.md` existiert, empfiehlt aber einen React/shadcn/Aceternity-Stack und Patterns (Aurora Gradient, Spotlight Cards, 3D Cards), die mit den Anti-Slop-Zielen dieses Projekts teilweise kollidieren — siehe `source-audit.md`.

## 2. Bestehende Live-Präsenz

Siehe Abschnitt „Live-Site-Audit" unten (Ergebnis des Research-Agents). Verbindliche Regel dieses Projekts: **Bestehende URLs, SEO-Strukturen, Formulare und Businesslogik werden niemals stillschweigend verändert.** Die neue Website in diesem Repository ist ein Prototyp/Neubau auf eigener Struktur; eine Migrations-/Redirect-Strategie ist vor einem Go-Live separat zu beschließen.

## 3. Produkt- und Markenlogik (aus Bestandsdokumenten)

- **Hersteller seit 1928**, Bauwerksabdichtung: aufsteigende/seitlich eindringende Feuchtigkeit, Horizontalsperre, Injektionstechnik, Sanierputz, Schimmelschutz, Hydrophobierung.
- **Zwei Produktlinien:** Home Line (privater Anwender, emotional-warm, Marke „Novu") und Pro Line (Profi-Handwerker, technisch-fokussiert).
- **Fachbetriebs-Netzwerk:** unabhängige, von BKM zertifizierte Betriebe, die Pro-Line-Produkte beim Kunden verarbeiten.
- **MicroPorex®:** Ingredient Brand („Powered by BKM Mannesmann"), 3-Phasen-Wirkung: Eindringen → Reagieren → Schützen.
- **Freigegebene Claims:** „Build. Keep. Maintain.", „Feuchtigkeit hat Hausverbot.", „Endlich Klarheit. Die richtige Diagnose ist der Anfang der Lösung.", „Werterhalt & Sicherheit."
- **Ansprache:** Du (Website, Shop, Social), Sie nur in Rechtstexten.

Daraus folgt die Grundlogik der Website: **Zwei Wege. Ein Ziel.** — Selbst sanieren (Home Line) oder Sanierung durch den Fachbetrieb (Pro Line), beide führen zum trockenen, geschützten Zuhause.

## 4. Live-Site-Audit (Stand 2026-08-12, index-basiert)

> Methode: Die BKM-Domains waren aus dieser Umgebung nicht direkt abrufbar; die Inventur basiert auf Suchindex-Daten (bestätigte indexierte URLs, Titel, Snippets). Vor Go-Live einmal direkt gegenprüfen.

### Domain-Landschaft (Multi-Domain-Ökosystem)

| Domain | Rolle |
|--------|-------|
| `www.bkm-mannesmann.de` | Haupt-Corporate-Site („BKM MANNESMANN AG – Feuchtigkeit hat Hausverbot.") — WordPress |
| `www.bkm-mannesmann.shop` | Separater Online-Shop (eigene TLD, eigenes Shop-System, großgeschriebene Kategorie-Slugs) |
| `www.bkm-mannesmann.com` / `us.bkm-mannesmann.com` / `www.bkm-mannesmann.es` | International/US/Spanien |
| `bkm-wuppertal.de`, `bkm-eberswalde.de`, `bkm-brandenburg.de` | Regionale Fachbetriebs-Sites mit BKM-Branding |
| Extern | Amazon Brand Store, Facebook, YouTube |

### Bestätigte indexierte URLs der Hauptdomain (für Redirect-Map erhalten)

Kern: `/`, `/produkte/`, `/produkte-gewerbekunden/`, `/leistungen-uebersicht/`, `/fachbetriebe/`, `/bkm-partner-netzwerk/`, `/schulung/`, `/team/`, `/historie/`, `/about_us/`, `/kontakt/`, `/impressum/`, `/datenschutz/`.
Themen-/SEO-Seiten: `/leistungen-uebersicht/keller-abdichten/`, `/leistungen-uebersicht/feuchte-waende-im-keller/`, `/leistungen-uebersicht/sanierputzarbeiten/`, `/leistungen-uebersicht/innendaemmung-klimasysteme/`, `/leistungen-uebersicht/mauerwerksverfestigung/`, `/leistungen-uebersicht/bodenanschluss-2/`, `/nachtraegliche-horizontalsperre/`, `/flachensperre-querdurchfeuchtung/`, `/schimmel-im-keller/`, `/wta-zertifikat-fuer-die-bkm-mannesmann-abdichtung-2/`.
Conversion-Tools: `/bedarfsrechner/` (NOVUSAN-Rechner), `/kostenlose-schadensanalyse.html` (Lead-Formular).
Außerdem: rankende TDS-PDF-Bibliothek unter `/pdf/Produkte/...`.

### Technical Debt (Warnzeichen für Relaunch)

Indexierte WordPress-`__trashed`-URLs (`/leistungen-uebersicht__trashed/fassadenschutz/`, `.../rissverpressung/`), `-2`-Duplikat-Slugs, gemischte URL-Muster (`.html` vs. Verzeichnis), englischer Slug `/about_us/`, fehlerhafte Umlaut-Transliteration (`flachensperre`). → Beim Go-Live vollständige 301-Redirect-Map inkl. PDFs.

### Inhalte & Beweise (verifiziert live)

- Positionierung: Hersteller („direkt vom Hersteller"), Injektionssysteme gegen aufsteigende/Querfeuchte, Kellerabdichtung, Sanierputz, Schimmelschutz, Mauerwerksverfestigung, Innendämmung, Rissverpressung, Fassadenschutz.
- Produktlinien live: **Home Line** (Novusan, Novusticks, Bio-Schimmelschutz; auch Amazon) und **Pro Line** (HZ-C Injektionscreme, DS-1K, SEF 2K, SG Silikatgrund, PG/IG Grundierungen, BRM/FBM Mörtel, NOVUprotect, NovuTop).
- Vertrauenssignale live: **WTA-Zertifikat**, Gewährleistung **bis 15 Jahre** (über Fachbetriebe), Forschungs-Claims.
- HQ: Wideystr. 23, 59174 Kamen; +49 (0)2307 990 340; info@bkm-mannesmann.de.
- Drei Zielgruppen-Funnels bereits in URL-Struktur kodiert: Privat/DIY, Gewerbe/Profi, Fachbetriebe/Partner.

### Festgestellte Abweichungen IST vs. Markendokumente

1. **Tonalität:** Live „Sie" — `docs/brand-voice.md` schreibt „Du" für die Website vor. Der Relaunch vollzieht den Wechsel bewusst; Stakeholder-Freigabe erforderlich (dokumentiert in `source-audit.md` §7).
2. **MicroPorex:** Im Design System als Ingredient Brand definiert, live nicht auffindbar — Lücke, die der Relaunch schließt.
3. **Feuchte-Check:** Live existiert „Kostenlose Schadensanalyse" (Formular) und ein Bedarfsrechner — aber keine geführte Selbstdiagnose. Der neue Feuchte-Check ersetzt kein bestehendes Formular, sondern ergänzt es vorgelagert.
