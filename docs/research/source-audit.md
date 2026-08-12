# Source Intelligence Audit — BKM Website-Projekt

> Output 1. Bewertung aller bereitgestellten Quellen (Stand: 2026-08-12). Methode: drei unabhängige Research-Durchläufe (Design-Quellen, GitHub-Repos/Discovery, Video-Tools + Live-Site). Einige Domains waren über den Egress-Proxy blockiert; dort wurde über Suchindizes und GitHub-API verifiziert. GitHub-Metadaten (Stars, Lizenz, letzter Push) sind API-verifiziert.

## 1. Entscheidungsübersicht

| Quelle | Typ | Entscheidung | Kernbegründung |
|--------|-----|:---:|----------------|
| **impeccable.style** ([pbakaus/impeccable](https://github.com/pbakaus/impeccable), Apache-2.0) | Design-QA-Skill für Agents | **CORE** | Einzige Quelle mit deterministischen Anti-Slop-Checks (~60 Regeln), `/audit`→`/polish`-Loop gegen unser DESIGN.md; nur Dev-Time, null Runtime-Risiko |
| **emilkowalski/skills** (MIT, aktiv) | Motion-/UI-Craft-Skills (Markdown) | **CORE** | Best-in-class Easing-/Duration-/Restraint-Prinzipien; genau die Schicht, in der AI-Output am schwächsten ist. Nur die 3–4 relevanten Skills, nicht alle 9. A11y-Disziplin müssen wir selbst erzwingen |
| **DietrichGebert/ponytail** (MIT) | Code-Ökonomie-Regeln | **SUPPORTING** | „Kleinste robuste Lösung"-Leiter passt exakt zur Static-Site-Strategie. Nur passive Regel-/Skill-Variante; Lifecycle-Hooks (Fremdcode) nicht installieren |
| **Jitter** (jitter.video) | Content-Production-Tool (SaaS) | **SUPPORTING** | Motion-Assets (z. B. MicroPorex-3-Phasen-Animation) als MP4/WebM produzieren. Niemals Runtime-Dependency; Lottie nur sparsam |
| **tasteskill.dev** ([leonxlnx/taste-skill](https://github.com/leonxlnx/taste-skill), MIT) | Anti-Slop-Direction-Skill | **EXPERIMENTAL** | Legitim, aber redundant zu Impeccable + eigenem DESIGN.md; v2 selbsterklärt experimentell; GSAP-lastige Defaults kollidieren mit Lightweight-Ziel. Nie parallel zu Impeccable laden |
| **awwwards.com** | Award-Galerie | **REFERENCE ONLY** | Kalibriert „premium"; typischer Tech-Stack der Gewinner (WebGL/Scroll-Jacking) ist für BKM Anti-Pattern |
| **getdesign.md** | DESIGN.md-Sammlung fremder Marken | **REFERENCE ONLY** | Das **Format** validiert unser Vorgehen; der **Inhalt** (Stripe/Linear-Looks) ist für BKM wertlos bis schädlich (Trade-Dress-Risiko) |
| **bestfreefonts.com** | Font-Verzeichnis | **REFERENCE ONLY** | Typografie ist entschieden (Unbounded OFL + TT Norms Pro). Nur Notfall-Referenz für Fallbacks |
| **Agents365-ai/drawio-skill** (MIT) | Diagramm-Skill | **REFERENCE ONLY** | Gut für interne Doku-Diagramme; draw.io-Ästhetik gehört nicht auf eine Premium-Website. Kundengerichtete Diagramme = markeneigenes SVG-System (S1 Wandschnitt) |
| **skillsllm.com** | Skill-Verzeichnis | **REFERENCE ONLY** | Discovery-Hilfe; Metriken teils unplausibel — immer auf GitHub verifizieren |
| **horizonx.so** | Bezahlte UI-Kit-Subscription | **REJECT** | Falsches ästhetisches Register (Dark-SaaS/Fintech), React-lastig, Lizenz unverifiziert, kauft nichts, was das Projekt braucht |
| **aura.build** | AI-Page-Builder (SaaS) | **REJECT** | Redundant zur bestehenden Claude-Code-Pipeline; zieht Richtung generischem AI-Template-Look |
| **motionsites.ai** | Prompt-/Template-Shop für AI-Builder | **REJECT** | Falsche Zielgruppe/Toolchain; Animation-first widerspricht Performance- und Vertrauenszielen |
| **karpathy/llm-council** | Konzept-Hack (Multi-LLM-Review) | **REJECT** als Dependency | Tot (1 Commit-Tag, keine Lizenz!). Das **Prinzip** (unabhängige Reviewer-Perspektiven) übernehmen wir als Verfahren — siehe §4 |
| **Jeffallan/claude-skills** (MIT) | Full-Stack-Framework-Skills | **REJECT** | 66 Skills für React/Next/Vue/Angular — keine für CSS, A11y, SEO, Static Sites. Kontext-Verschmutzung ohne Nutzen |
| **oso95/scroll-world** (MIT) | Scroll-Video-Landingpage-Generator | **REJECT** | Scheitert an jeder harten Anforderung: zig MB Video, Scroll-Jacking, A11y-Desaster, SEO-unsichtbar, AI-Fantasiewelten vs. echtes Handwerk. Siehe §5 |
| **awesome-repositories.com** | Generisches Repo-Verzeichnis | **REJECT** | GitHub-Suche ist strikt besser |
| **reactvideoeditor.com** | React-Video-Editor-Komponente (ab $499 + Remotion-Firmenlizenz) | **REJECT** | Kein Use Case auf einer Marketing-Site; doppelte Lizenzkette; schwerer Runtime-Footprint |

Detaillierte 13-Faktor-Scores (0–5) für jede Quelle: siehe Anhang der drei Research-Reports; die Kernwerte sind oben in die Begründungen eingeflossen. Ausschlaggebend war nie ein Einzelscore, sondern: **Löst die Quelle ein echtes Problem dieses Projekts besser als vorhandene Mittel — ohne Runtime-, Lizenz- oder Ästhetik-Risiko?**

## 2. Kategorisierung der Quellen

- **Inspiration:** awwwards, getdesign.md (Format), horizonx, motionsites
- **Methodik / Design Governance:** impeccable, taste-skill, ponytail, llm-council-Prinzip
- **Dev-Tooling (Dev-Time only):** impeccable, emilkowalski/skills, ponytail, drawio-skill
- **Library / Runtime:** react-video-editor, scroll-world (beide abgelehnt) — **es verbleibt bewusst KEINE Runtime-Dependency**
- **Discovery-Service:** awesome-repositories, skillsllm
- **Content-Production:** jitter.video
- **Spezialwerkzeug:** drawio-skill, bestfreefonts

## 3. Overlap-Analyse (Design-Guidance-Cluster)

Die vermeintlich konkurrierenden Quellen zerlegen sich in vier Schichten:

| Schicht | Frage | Beste Quelle | Verlierer |
|---------|-------|--------------|-----------|
| **Spezifikation** | Wie sieht die Marke aus? | **Unser eigenes `DESIGN.md`** (Format à la getdesign.md, Inhalt 100 % BKM) | getdesign.md-Katalog |
| **Direction** | Welche Gestaltungsrichtung? | **Eigene Creative Direction** (`docs/design/creative-direction.md`) | taste-skill (redundant, sobald DESIGN.md existiert) |
| **Enforcement** | Verstößt der Output gegen System/wirkt AI-generiert? | **impeccable** (deterministische Regeln statt Vibes) | — |
| **Craft (Motion)** | Fühlt sich Interaktion gestaltet an? | **emilkowalski/skills** | motionsites |

**Regel:** Nie zwei Doktrinen gleichzeitig in den Agent-Kontext laden (Impeccable **oder** Taste Skill, nicht beide). Ponytail ist orthogonal (Code-Menge, nicht Gestalt) und kombinierbar.

## 4. LLM-Council-Prinzip → BKM-Review-Verfahren

Das Repo wird nicht installiert (unlizenziert, tot). Das Prinzip wird als **Qualitäts-Verfahren** übernommen: Nach jeder größeren Implementierungsstufe bewerten fünf simulierte, unabhängige Reviewer-Perspektiven (Creative Director, UX Lead, Frontend Architect, Conversion Specialist, A11y/Performance Engineer) die Screenshots. Konflikte werden nicht per Mehrheitsgeschmack, sondern am Projektziel entschieden. Dokumentiert in `docs/reviews/`.

## 5. Scroll World / 3D / Cinematic — Sonderprüfung

Geprüft gegen die vorgeschriebenen Fragen: Verständnis-Verbesserung? *Nein — erklärende Wandschnitt-SVGs erklären besser als Kamerafahrten.* Mobile? *Zig MB Video.* Reduced Motion? *Konzeptionell unmöglich, das Format IST die Bewegung.* LCP/CPU? *Disqualifizierend.* Ohne JS? *Leere Seite.* Einfacherer Weg mit 80 % Wirkung? *Ja: statisches SVG-Diagramm mit dezenter Trocknungs-Animation (S1).* → **REJECT** für die Corporate Site; allenfalls denkbar für ein separates Messe-Microsite-Experiment außerhalb des Performance-Budgets.

## 6. Video-Tools: Runtime vs. Production

- **Jitter = Content Production Tool.** Erzeugt Assets (MP4/WebM), die als normale Medien eingebunden werden. Kein Byte Jitter-Code im Bundle. SUPPORTING.
- **React Video Editor = Runtime-Produkt.** Kein Use Case, Lizenzkette (RVE + Remotion-Firmenlizenz), REJECT.
- **Regel:** Lottie nur für kleine UI-Animationen (<20 KB JSON) und nur, falls der Player-Kostenpunkt (~60 KB) je bewusst beschlossen wird; Standard ist `<video>` bzw. CSS/SVG-Animation.

## 7. Kritische Funde jenseits der Quellenliste

1. **TT-Norms-Pro-Webfont-Lizenz:** TT Norms Pro ist kommerziell (TypeType). Die woff2-Dateien liegen im Repo; **eine gültige Webfont-Lizenz für bkm-mannesmann.de muss vor Go-Live verifiziert werden** (Pageview-Tiers beachten). Unbounded ist SIL OFL — unkritisch.
2. **Tonalitäts-Konflikt:** Live-Site siezt („Finden Sie Ihren BKM Fachbetrieb"), `docs/brand-voice.md` schreibt Du vor. Der Relaunch ist damit auch ein bewusster Tonalitätswechsel → **Stakeholder-Freigabe nötig.** Dieses Projekt folgt dem normativen Brand-Dokument (Du).
3. **SEO-Bestand:** WordPress-Technical-Debt auf der Live-Site (indexierte `__trashed`-URLs, `-2`-Slugs, gemischte `.html`/Verzeichnis-Muster, `/about_us/`) und eine rankende TDS-PDF-Bibliothek → beim Go-Live vollständige 301-Redirect-Map erforderlich. Inventar: `docs/research/ist-zustand.md`.
4. **MicroPorex-Lücke:** Die Ingredient Brand ist im Design System definiert, auf der Live-Site aber nicht auffindbar — der Relaunch schließt diese Lücke.

## 8. Empfohlene Workflow-Reihenfolge

1. Eigenes DESIGN.md als Single Source of Truth (erweitert um Web-Systeme) ✅
2. Strategie → IA → Blueprints → statisches UI (ohne Effekte)
3. Impeccable-artiger Audit-Loop + Screenshot-Review je Stufe
4. Motion zuletzt, nach Emil-Kowalski-Prinzipien, System in DESIGN.md
5. Ponytail-Leiter vor jeder Dependency (Ziel: null Runtime-Dependencies)
6. Council-Review + finale Quality Gates (A11y/Perf/SEO)
