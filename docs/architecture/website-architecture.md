# Website-Architektur — BKM Mannesmann AG

> Output 5. Verdichtet Strategie (`website-strategy.md`) und Design-Richtung (`creative-direction.md`) zu einer umsetzbaren Architektur: Zielgruppen → Problemsituationen → Informationsarchitektur → Seiten → Conversion Paths → Komponenten → technische Systeme.

## 1. Gesamtbild

```
BKM MANNESMANN AG
      │
      ├── ZIELGRUPPEN
      │     N1 Betroffene Hausbesitzer  N2 Heimwerker  N3 „Profi bitte"
      │     N4 Verarbeiter/Betriebe     N5 Planer/Verwalter
      │
      ├── PROBLEMSITUATIONEN (Einstiege)
      │     feuchte Kellerwand · nasser Sockel · Schimmelecke ·
      │     Salzausblühungen · abplatzender Putz · muffiger Geruch
      │
      ├── INFORMATIONSARCHITEKTUR
      │     Verstehen → Orientieren (Feuchte-Check) → Entscheiden (Zwei Wege)
      │
      ├── SEITEN (siehe Seitenbaum in website-strategy.md §7)
      │
      ├── CONVERSION PATHS
      │     C1 Diagnose→Fachbetrieb · C2 Diagnose→DIY-Kauf ·
      │     C3 Direkt zum Profi · C4 Pro-Produkte · C5 Partner werden
      │
      ├── KOMPONENTEN (siehe §3)
      │
      └── TECHNISCHE SYSTEME (siehe §4)
```

## 2. Seiten-Blueprints (Vertical Slice)

Für jede Seite: Nutzerziel / BKM-Ziel / primäre Frage / primärer CTA / sekundärer CTA.

### 2.1 Startseite `/`
- **Nutzerziel:** „Bin ich hier richtig mit meinem Feuchtigkeitsproblem?"
- **BKM-Ziel:** In den Feuchte-Check oder direkt in einen der zwei Wege leiten.
- **Primäre Frage:** Was macht BKM — und was ist mein nächster Schritt?
- **Primärer CTA:** Feuchte-Check starten. **Sekundär:** Fachbetrieb finden.
- **Sektionen:** 1) Hero (Dark Band, Klartext-Nutzenversprechen, Keyvisual) → 2) Symptom-Einstieg („Was siehst du?" — Schadensbild-Kacheln) → 3) Wandschnitt-Erklärung (S1: so entsteht aufsteigende Feuchte, so wirkt die Sperrschicht) → 4) Zwei-Wege-Weiche (S3) → 5) Vertrauen (seit 1928, MicroPorex, Fachbetriebsnetz — Messwert-Block S5) → 6) Ratgeber-Teaser → 7) Abschluss-CTA (Dark Band).

### 2.2 Feuchtigkeit verstehen `/feuchtigkeit-verstehen/`
Hub: Schadensbilder-Galerie (visuell erkennen), Ursachen-Erklärstrecke (Wandschnitte), Risiko-Sektion („was passiert bei Nichtstun"), Einstieg Feuchte-Check.

### 2.3 Feuchte-Check `/feuchtigkeit-verstehen/feuchte-check/`
- **Nutzerziel:** „Sag mir, was ich habe und was ich tun soll."
- 5 geführte Fragen (Wo? Was siehst du? Seit wann? Ausmaß? Gebäude?) → Ergebnis: wahrscheinliche Ursachenlage + ehrliche Empfehlung + Zwei-Wege-Weiche mit gewichteter Empfehlung. Kein Login, keine Pflichtfelder vor dem Ergebnis. Läuft vollständig clientseitig (kein Backend nötig); Antworten sind keine personenbezogenen Daten.

### 2.4 Selbst sanieren `/loesungen/selbst-sanieren/`
Weg 1. Ehrliche Eignungsklärung („Wann DIY funktioniert — wann nicht"), Systemübersicht nach Anwendungsfall, Schritt-für-Schritt-Logik, Home-Line-Produkte als Teil der Lösung, Übergabeoption zum Fachbetrieb.

### 2.5 Fachbetrieb `/loesungen/fachbetrieb/`
Weg 2. So läuft die Sanierung ab (Prozess-Komponente), warum zertifizierte BKM-Fachbetriebe (Beweise), PLZ-Suche/Anfrageformular, Kostenrahmen-Transparenz.

### 2.6 Folgeausbau
Produkte (Home/Pro/MicroPorex), Ratgeber-Hub (bestehende Inhalte, URLs unangetastet), Unternehmen, Fachbetrieb werden, Rechtliches.

## 3. Komponentensystem

Nur Komponenten mit echter Wiederverwendung. Basis-Anatomie und Tokens: `DESIGN.md`.

| Kategorie | Komponente | Verwendung |
|-----------|------------|------------|
| Navigation | Header (heller Grund, Logo stone/puregreen, Nav, Lime-CTA), Mobile-Drawer, Breadcrumb | global |
| Hero | Dark-Band-Hero (H1 + Lead + 1 CTA + Keyvisual), Sub-Hero hell für Unterseiten | alle Seiten |
| Diagnose | Feuchte-Check (S4): Fragekarte, Antwortkarte, Trocknungslinie-Progress, Ergebnispanel | Check, einbettbar als Teaser |
| Erklärung | Wandschnitt-Diagramm (S1), Erklärstrecke (Text + Diagramm 7/5-Split), Prozess-Schritte (nummeriert) | Verstehen, Lösungen |
| Entscheidung | Zwei-Wege-Weiche (S3) | Ende jeder Problemstrecke |
| Vertrauen | Messwert-Block (S5), Beweis-Leiste (Fakten seit 1928), Fachbetrieb-Karte | Start, Fachbetrieb, Unternehmen |
| Inhalt | Schadensbild-Kachel (Bild + Titel + „erkennen"-Link), Ratgeber-Teaser, FAQ (native `<details>`) | Hubs |
| Produkt | Produktkarte (Shadow-as-Border, Badge, Preis), Spec-Tabelle | Produkte, Systeme |
| Formulare | Input, Select, Radio-Karte, Anfrageformular (Fachbetrieb) | Kontakt/Anfrage |
| CTA | Abschluss-Band (dunkel, 1 Primary), Inline-CTA | alle Seiten |
| Footer | Deep-Green-Footer: Sitemap, Kontakt, Rechtliches, Social | global |

**Anti-Cardisierung:** Erklärinhalte laufen als editorialer Text mit Diagrammen, nicht als Card-Raster. Cards nur für echte Sammlungen (Produkte, Schadensbilder, Betriebe).

## 4. Technische Systeme

### Stack-Entscheidung (Ponytail-Prinzip)

**Statisches HTML + eine geteilte CSS-Datei (Design Tokens + Komponenten) + minimales Vanilla-JS (progressive enhancement). Kein Framework, kein Build-Schritt, null Runtime-Dependencies.**

Begründung:
1. Alle Anforderungen (Content-Seiten, ein clientseitiger Check, Formulare) sind mit Browser-Bordmitteln lösbar (`<details>`, `:focus-visible`, IntersectionObserver, CSS `clamp()`).
2. Das Repo arbeitet bereits mit self-contained HTML; kein Node-Toolchain-Bruch.
3. Beste erreichbare Performance (kein Hydration-Gewicht) und triviale Wartbarkeit.
4. Ein späterer Umzug auf ein SSG/CMS (z. B. Astro + Headless CMS) kann die Seiten 1:1 übernehmen — Struktur, CSS und JS sind framework-neutral. Diese Migration ist bewusst **nicht** Teil dieses Schritts.

Dependency-Dokumentation gem. Dependency Rule: **keine** Runtime-Dependencies. Dev-Tooling: Playwright (bereits in der Umgebung) für Screenshot-QA.

### Struktur

```
website/
├── index.html
├── feuchtigkeit-verstehen/
│   ├── index.html
│   └── feuchte-check/index.html
├── loesungen/
│   ├── selbst-sanieren/index.html
│   └── fachbetrieb/index.html
├── assets/            (symlink-frei: kopierte Font-/Logo-Subsets)
├── css/tokens.css     (Design Tokens aus DESIGN.md)
├── css/base.css       (Reset, Typo, Layout, Komponenten)
└── js/main.js         (Nav, Reveals, Feuchte-Check — <8 KB, defer)
```

### Qualitäts-Gates
- **Performance:** selbst gehostete woff2 mit `font-display: swap` + korrekte Fallback-Metriken, SVG-Diagramme statt Bilder, keine Third-Party-Scripts, JS <10 KB.
- **Accessibility:** WCAG 2.2 AA; semantische Landmarks, Skip-Link, sichtbarer Fokus, 44px-Touch-Targets, Kontrast gem. Matrix in `DESIGN.md`, `prefers-reduced-motion`.
- **SEO:** sprechende deutsche URLs, ein H1 pro Seite, Meta + Open Graph, Schema.org (`Organization`, `HowTo`/`FAQPage` wo zulässig), interne Verlinkung entlang der Journeys, `sitemap.xml`/`robots.txt` beim Go-Live.
- **Bestandsschutz:** bestehende Live-URLs werden nicht angerührt; Redirect-Plan ist Go-Live-Aufgabe.
