# Referenzen & Inspiration

Dieses Design System wurde unter Berücksichtigung moderner Design-System-Ansätze erstellt. Die folgenden externen Ressourcen dienten als strukturelle Inspiration und können für die Weiterentwicklung herangezogen werden.

## DESIGN.md Konzept

Das `DESIGN.md`-Format wurde von [Google Stitch](https://stitch.withgoogle.com/) eingeführt und durch das [awesome-design-md](https://github.com/VoltAgent/awesome-design-md) Repository popularisiert. Es handelt sich um ein reines Markdown-Dokument, das AI-Agenten lesen können, um konsistente UI zu generieren.

| Datei | Leser | Definiert |
|-------|-------|-----------|
| `AGENTS.md` | Coding-Agenten | Wie das Projekt gebaut wird |
| `DESIGN.md` | Design-Agenten | Wie das Projekt aussehen und sich anfühlen soll |

## Empfohlene Referenz-Design-Systeme

Die folgenden Design-Systeme aus dem awesome-design-md Repository sind besonders relevant für die Weiterentwicklung des BKM Systems:

| Design System | Relevanz für BKM | Link |
|---------------|-----------------|------|
| **NVIDIA** | Industrielle Ästhetik, Grün-Akzent, technische Dokumentation | [DESIGN.md](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/nvidia) |
| **MongoDB** | Grüne Markenfarbe, duale Oberflächen (dunkel/hell), Produktdokumentation | [DESIGN.md](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/mongodb) |
| **Mintlify** | Dokumentations-Fokus, grüner Akzent, 3-Spalten-Layout | [DESIGN.md](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/mintlify) |
| **Vercel** | Minimalismus, Shadow-System, Typografie-Hierarchie | [DESIGN.md](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/vercel) |
| **Supabase** | Dark Emerald Theme, Code-First-Ansatz | [DESIGN.md](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/supabase) |

## Weiterentwicklung

Für die Weiterentwicklung des BKM Design Systems können folgende Bereiche aus den Referenzen übernommen werden:

| Bereich | Inspiration von | Anwendung bei BKM |
|---------|----------------|-------------------|
| Token-System (YAML) | MongoDB, Vercel | Maschinenlesbare Design-Tokens für Automatisierung |
| Komponentenbibliothek | Alle | Detaillierte Komponentendefinitionen mit States |
| Responsive Breakpoints | Vercel | Systematische Breakpoint-Definitionen |
| Shadow & Depth System | Vercel | Konsistentes Tiefensystem für Web-Anwendungen |
| Dark Mode | Supabase, NVIDIA | Erweiterung des BKM Dark Mode |
| Dokumentations-IA | Mintlify | Strukturierte Sidebar-Navigation für Docs |
