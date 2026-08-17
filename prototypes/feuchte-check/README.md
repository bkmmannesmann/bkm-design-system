# Prototyp: BKM Feuchte-Check (Landingpage + Diagnose-Wizard)

> **Status: in Arbeit.** Interaktive Landingpage, die 8 Schadensursachen
> systematisch prüft — „wie ein Gutachter". Ein-Frage-Wizard (Typeform-Stil),
> Regelwerk-basierte Auswertung, Lead-Gate vor dem vollständigen Ergebnis.
> Primäres Ziel laut PRODUCT.md: Orientierung und Klarheit für den Kunden.

## Qualitäts-Pass (Impeccable, 2026-08)

Anti-Slop-Überarbeitung mit `npx impeccable detect` (70 → 11 Findings):
Eyebrows/Kicker entfernt, farbige Kantenbalken (side-tabs) ersetzt, Emoji-Icons
durch gezeichnete SVG-Icons ersetzt, Kontraste auf WCAG AA angehoben,
Schriftgrößen/Radien auf die DESIGN.md-Ramp gerastert, `width`-Transitions durch
`transform:scaleX` ersetzt, Headings-Hierarchie repariert, Buttons ohne Uppercase
(nur H1 ist laut DESIGN.md uppercase).

Bewusste Ausnahmen (Detector-Restmeldungen): `cramped-padding`-Meldungen auf
Sektionen sind False Positives des statischen Parsers (clamp()-Padding);
`flat-type-hierarchy` entspricht exakt der dokumentierten DESIGN.md-Ramp
(12/14/16/18); neutrale Schatten-Alpha `rgba(0,0,0,.35)` auf dem Lime-Button ist
beabsichtigt (neutrale Elevation statt Farb-Glow).

## Datei

- `index.html` — komplett self-contained (~1,5 MB): eingebettete Fonts (Unbounded,
  Inter als WOFF2-Data-URIs), Bilder als Base64, kein Build-Schritt. Direkt im
  Browser öffnen.

## Aufbau der Seite

1. **Hero** — Rotations-Claim („selbst beheben / beheben lassen / erst prüfen")
2. **Beruhigung** (`#beruhigung`) — Empathie-Sektion
3. **Fehldiagnose** (`#fehldiagnose`) — Kosten der falschen Sanierung
4. **So funktioniert's** (`#funktion`) — dunkles Band, Glas-Karten
5. **Prinzipien** (`#prinzipien`) — Spotlight-Cards
6. **Ablauf** (`#ablauf`) + **Acht Ursachen** (`#ursachen`)
7. **Der Check** (`#check`) — Wizard mit Phasen-Label, Fortschritts-Thread,
   Zurück/Weiter/Überspringen
8. **Ergebnis** — Teaser (Ursache verdeckt) → Lead-Gate (E-Mail + Consent +
   optionaler Rückruf-Opt-in) → freigeschaltetes Protokoll mit Evidenz-Gauge,
   Pro/Contra-Befunden, Handlungsempfehlung (Routing), Print-Protokoll
9. **FAQ**, CTA-Band, Footer

## Technik

- **Regelwerk** v2.1 (`RULES` im Inline-Script): Fragen, Bedingungen, Gewichtung,
  Ausschlüsse; Auswertung in `auswerten()`, Plausibilitätsprüfung, `routing()`
- **Feuchte-Check 2.0** (seit 2026-08): Trennung in Diagnose und Lösung.
  Phase A = 7 Kern-Screens in 3 Etappen (Ort / Schadensbild / Verlauf), der
  Verlaufs-Screen (`F0_verlauf`) übersetzt eine Laienantwort in mehrere
  Engine-Antworten. Danach entscheidet die Engine: Konfidenz hoch → Ergebnis,
  sonst max. 3 **Smart Questions** (`smartFrage()`: die offene Frage mit dem
  größten Punkte-Abstand zwischen den Top-2-Hypothesen; Pool = alle übrigen
  Regelwerk-Fragen inkl. `sichtbar_wenn`-Gating). „Weiß ich nicht" ist bei den
  Kernfragen Pflichtoption und zählt nicht als Evidenz (`effektiveAntworten()`).
  Ergebnis sofort und ohne Gate: Einordnung, qualitative Sicherheit
  (Punkte statt Prozent), Warum-Befunde, Bedeutung, Weg-Routing, aufklappbares
  „Was wir geprüft haben". Lead-Gate erst danach als „Persönlicher Lösungsplan".
  Modul C (DIY-Konfigurator, Fachbetriebs-Übergabe mit PLZ/Protokoll) ist
  konzipiert, aber noch nicht gebaut — braucht Produktdaten bzw. Backend.
- **SB7-Aufbau** (StoryBrand): Hero (Held + Ziel + Ergebnis-Versprechen) →
  Problem/Villain (Fehldiagnose) → Guide-Empathie (Beruhigung) → Autorität
  (Systematik/Prinzipien) → Plan (3 Schritte) → Call-to-Action (Check) →
  Erfolg (Protokoll) → FAQ
- **Lead-Endpoint:** `api/lead.php` (relativ; Backend nicht Teil dieses Prototyps).
  Es werden zwei Payloads gesendet: anonyme Auswertung + Protokoll mit Lead-Daten.
- **Design System:** BKM Tokens aus `DESIGN.md`/`AGENTS.md`, Noise-Textur, Aurora
  (BKM AG), Glasmorphismus auf dunklen Flächen, Scroll-Reveal, Reduced-Motion- und
  Print-Styles (Ergebnis-Protokoll).
