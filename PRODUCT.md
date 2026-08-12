# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

Privatpersonen (Hausbesitzer, Wohnungseigentümer, Heimwerker) mit einem akuten oder
vermuteten Feuchtigkeitsschaden — beunruhigt, ohne Fachwissen, oft unter Zeit- und
Kostendruck. Sekundär: professionelle Handwerker/Fachbetriebe als Partner der BKM
Mannesmann AG. Ansprache laut Brand Voice: Du (Website-Kontext).

## Product Purpose

Der **BKM Feuchte-Check** (prototypes/feuchte-check/) ist ein interaktiver
Diagnose-Wizard, der 8 mögliche Schadensursachen systematisch prüft — mit derselben
Systematik wie ein Gutachter. **Erfolg heißt: Der Nutzer weiß am Ende, welche
nächste Handlung für ihn sinnvoll ist** (selbst beheben, beheben lassen oder erst
prüfen) — bestätigtes primäres Geschäftsziel: Orientierung und Klarheit für den
Kunden, nicht Lead-Maximierung. Lead-Erfassung (Protokoll per E-Mail, optionaler
Experten-Rückruf) ist Mittel, nicht Zweck.

## Positioning

„Endlich Klarheit. Die richtige Diagnose ist der Anfang der Lösung." (freigegebener
Claim). Kein Verkaufsgespräch, sondern ein Messverfahren: transparentes Regelwerk,
ehrliche Empfehlung inklusive „Du brauchst uns nicht"-Ausgang. BKM Mannesmann AG
(gegr. 1928) ist Hersteller von Bauwerksabdichtung (MicroPorex-Injektionstechnik)
— die Diagnose-Neutralität ist glaubwürdig, weil beide Wege (DIY-Produkt und
Fachbetrieb) im eigenen Haus liegen.

## Operating Context

- Wird als Unterseite von **bkm-mannesmann.de** integriert (bestätigt); relative
  Pfade wie `api/lead.php` gelten relativ zu diesem Einbau-Ort.
- Nutzungsszene: mobil oder Desktop, häufig abends/am Wochenende nach Entdeckung
  eines Flecks; emotionaler Zustand: Sorge → gewünschtes Endgefühl: Erleichterung
  und Handlungssicherheit.
- Ergebnis-Protokoll ist druckbar (Print-Styles) und wird per E-Mail versendet.

## Capabilities and Constraints

- Regelwerk v2.1 im Inline-Script: Fragen, Bedingungen, Gewichtung, Ausschlüsse,
  Plausibilitätsprüfung, Routing (`auswerten()`, `routing()`).
- Self-contained HTML ohne Build-Schritt; Fonts und Bilder als Data-URIs.
- Lead-Endpoint `api/lead.php` (Backend nicht Teil dieses Repos).
- Keine Diagnose-Garantie: Disclaimer erforderlich, Check ersetzt keinen Gutachter
  vor Ort.

## Brand Commitments

- BKM Design System ist bindend: `DESIGN.md` (Root), Kontext **BKM AG**
  (Deep Green `#1c4b42`, Lime `#b4e717`, Aurora + Noise nur BKM AG-Kontext).
- Typografie: Unbounded 900 für Headlines (nur H1 uppercase), TT Norms Pro für
  Fließtext (im Prototyp aktuell per Fallback gelöst).
- Brand Voice: kompetent, nahbar, motivierend; Du-Ansprache; freigegebene Claims
  siehe `docs/brand-voice.md`.

## Evidence on Hand

- Design-Tokens und Muster: `DESIGN.md`, `AGENTS.md`, `patterns/`, `assets/`.
- Brand Voice und Claims: `docs/brand-voice.md`.
- Keine echten Kundenstimmen/Fallzahlen für den Feuchte-Check vorhanden —
  **nicht erfinden**; Zahlen im Prototyp (z. B. Kosten von Fehlsanierungen) nur
  verwenden, wenn belegbar.

## Product Principles

1. Klarheit vor Konversion: Der Nutzer soll seinen nächsten Schritt kennen, auch
   wenn er BKM dafür nicht braucht.
2. Gutachter-Systematik statt Verkaufsrhetorik: transparent zeigen, *warum* eine
   Ursache wahrscheinlich ist (Pro/Contra-Befunde, Evidenz).
3. Beruhigen, dann befähigen: Empathie zuerst, dann konkrete Handlung.
4. Ehrlichkeit als Differenzierung: Grenzen des Checks offen benennen.

## Accessibility & Inclusion

Zielgruppe umfasst ältere Hausbesitzer: gute Lesbarkeit, ausreichende Kontraste,
Tastatur-Bedienbarkeit des Wizards, `prefers-reduced-motion` wird respektiert.
