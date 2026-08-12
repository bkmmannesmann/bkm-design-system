# Implementation Roadmap — BKM Website

> Output 6. Vertikale Milestones statt Ticket-Konfetti. Jeder Milestone endet mit Screenshot-Review (Mobile/Tablet/Desktop/Large) und Council-Check.

## M0 — Fundament *(Voraussetzung für alles)*
Dokumentierte Basis: IST-Zustand, Source-Audit, Strategie, Creative Direction, DESIGN.md-Web-Erweiterung, Architektur. **Definition of Done:** Alle Outputs 1–6 im Repo. ✅

## M1 — Design-System-Implementierung
`website/css/tokens.css` (1:1 aus DESIGN.md) + `base.css` (Reset, Typo-Scale, Grid, Buttons, Cards, Formulare, Focus-States) + Font-Setup (self-hosted woff2, `font-display: swap`, Fallback-Metriken) + `js/main.js` (Nav, Reveals; <10 KB, defer).
**DoD:** Komponenten-Testseite rendert korrekt in 4 Viewports; Kontrast- und Fokus-Check bestanden.

## M2 — Vertical Slice (Kern des Projekts)
Reihenfolge innerhalb des Slice:
1. **Header/Navigation + Footer** (global, mobile-first)
2. **Startseite** (7 Sektionen gem. Blueprint §2.1)
3. **Problem-Flow:** `/feuchtigkeit-verstehen/` (Hub) + **Feuchte-Check** (S4, clientseitig)
4. **Conversion-Flows:** `/loesungen/fachbetrieb/` (Anfrage) + `/loesungen/selbst-sanieren/` (Home-Line-Weg)
5. **Signature Elements:** Wandschnitt-SVG (S1), Zwei-Wege-Weiche (S3), Messwert-Block (S5), Sperrschicht-Kante (S2)

Abhängigkeiten: 1 vor 2–4; S1/S3/S5 entstehen mit der Startseite und werden wiederverwendet.
**DoD:** Alle 5 Seiten statisch exzellent (noch ohne Motion), Screenshot-Review bestanden.

## M3 — Interaction & Motion
Hover-/Fokus-Feedback, Mobile-Drawer, Reveals (einmalig, ≤600ms), Feuchte-Check-Übergänge, Wandschnitt-Trocknungsanimation. Alles hinter `prefers-reduced-motion`-Guard.
**DoD:** Seite ohne JS/Motion vollständig nutzbar; Motion-Review nach Emil-Kowalski-Kriterien.

## M4 — Quality Gates
A11y-Pass (Keyboard, Screenreader-Semantik, Touch-Targets, Kontrast), Performance-Pass (Font-Subsetting-Check, Bildgewichte, JS-Budget), SEO-Pass (Meta, Schema.org, interne Links, H-Struktur), Council-Review, `final-design-audit.md`. Kategorien <9 → Nacharbeit.
**DoD:** Audit dokumentiert, Nacharbeiten erledigt.

## M5 — Skalierung *(Folgephase, nicht Teil des Slice)*
Produkte (Home/Pro/MicroPorex), Systeme nach Anwendungsfall, Ratgeber-Hub, Unternehmen, Fachbetrieb werden, Rechtliches. Danach: CMS-/SSG-Migrationsentscheidung, Redirect-Map, Formular-Backend, Go-Live-Plan.

## Offene Entscheidungen (Stakeholder)
1. Tonalitätswechsel Sie→Du auf der Website (Brand-Doc vs. Live-Site) — hier gem. Brand-Doc umgesetzt.
2. TT-Norms-Pro-Webfont-Lizenz für die Domain verifizieren.
3. Zukunft der regionalen Fachbetriebs-Domains (SEO-/Governance-Frage).
4. Shop-Integration (`.shop`-Domain) in die neue IA.
