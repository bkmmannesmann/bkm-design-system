# Prototyp: BKM Feuchte-Check (Landingpage + Diagnose-Wizard)

> **Status: in Arbeit.** Interaktive Lead-Gen-Landingpage, die 8 Schadensursachen
> systematisch prüft — „wie ein Gutachter". Ein-Frage-Wizard (Typeform-Stil),
> Regelwerk-basierte Auswertung, Lead-Gate vor dem vollständigen Ergebnis.

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
- **Lead-Endpoint:** `api/lead.php` (relativ; Backend nicht Teil dieses Prototyps).
  Es werden zwei Payloads gesendet: anonyme Auswertung + Protokoll mit Lead-Daten.
- **Design System:** BKM Tokens aus `DESIGN.md`/`AGENTS.md`, Noise-Textur, Aurora
  (BKM AG), Glasmorphismus auf dunklen Flächen, Scroll-Reveal, Reduced-Motion- und
  Print-Styles (Ergebnis-Protokoll).
