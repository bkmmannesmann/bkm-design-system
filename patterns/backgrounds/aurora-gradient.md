# Aurora Gradient Background

> Animierter Farbverlauf-Hintergrund mit weichen, sich bewegenden Lichteffekten. Erzeugt eine atmosphärische Tiefe für Hero-Sektionen.

## Metadaten

| Eigenschaft | Wert |
|-------------|------|
| **Quelle** | [Aceternity UI — Aurora Background](https://ui.aceternity.com/components/aurora-background) |
| **Lizenz** | MIT |
| **Tech** | React, Framer Motion, Tailwind CSS |
| **Kontext** | BKM AG only |
| **Einsatz** | Hero-Sektionen, Landing Pages, Fullscreen-Hintergründe |

## BKM-Farbmapping

Die Aurora-Effekte nutzen die BKM AG Farbwelt. Der Hintergrund bleibt Deep Green, die Lichteffekte bewegen sich zwischen den BKM-Grüntönen und Lime.

| Aurora-Parameter | BKM-Wert | Token |
|-----------------|----------|-------|
| Basis-Hintergrund | `#1c4b42` | `colors.primary` (Deep Green) |
| Lichteffekt 1 | `#287d4b` | `colors.tertiary` (Transition Green) |
| Lichteffekt 2 | `#4daf46` | `colors.fachbetrieb-primary` (Pure Green) |
| Lichteffekt 3 | `#b4e717` | `colors.secondary` (Lime) |
| Lichteffekt 4 | `#2a6b5e` | `colors.primary-light` |
| Text auf Aurora | `#ffffff` | `colors.on-primary` |

## Installation

```bash
npx shadcn@latest add @aceternity/aurora-background
```

## BKM-angepasster Code

```tsx
import { AuroraBackground } from "@/components/ui/aurora-background";
import { motion } from "framer-motion";

export function BkmHeroAurora() {
  return (
    <AuroraBackground
      className="relative overflow-hidden"
      style={{
        // BKM Deep Green Basis
        background: "#1c4b42",
      }}
    >
      <motion.div
        initial={{ opacity: 0, y: 40 }}
        whileInView={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.3, duration: 0.8, ease: "easeInOut" }}
        className="relative z-10 flex flex-col items-start max-w-[1280px] mx-auto px-8 md:px-16 py-40"
      >
        <p className="font-['TT_Norms_Pro'] text-[13px] font-semibold uppercase tracking-[1.5px] text-white/50 mb-6">
          Bauwerksabdichtung seit 1928
        </p>
        <h1 className="font-['Unbounded'] text-5xl md:text-7xl font-black uppercase text-white tracking-[-0.04em] leading-none max-w-[800px]">
          SCHUTZ DER HÄLT
        </h1>
        <p className="font-['TT_Norms_Pro'] text-xl text-white/70 mt-6 max-w-[640px] leading-relaxed">
          Professionelle Bauwerksabdichtung mit MicroPorex® Technologie.
        </p>
        <button className="mt-10 bg-[#b4e717] text-[#1c4b42] font-['Unbounded'] text-sm font-black uppercase px-6 py-3 h-12 rounded-[4px] tracking-[0.02em] hover:bg-white transition-colors duration-150">
          PRODUKTE ENTDECKEN
        </button>
      </motion.div>
    </AuroraBackground>
  );
}
```

## CSS-Anpassung der Aurora-Farben

Die Aurora-Komponente nutzt CSS-Variablen für die Lichteffekte. Diese müssen auf BKM-Werte gesetzt werden:

```css
/* In der globalen CSS-Datei oder im Komponenten-Scope */
.aurora-background {
  --aurora-first-color: 40, 125, 75;    /* Transition Green RGB */
  --aurora-second-color: 77, 175, 70;   /* Pure Green RGB */
  --aurora-third-color: 180, 231, 23;   /* Lime RGB */
  --aurora-fourth-color: 42, 107, 94;   /* Deep Green Light RGB */
}
```

## Einschränkungen

- **Nicht im Fachbetrieb-Kontext verwenden** — Lime Green ist dort verboten.
- **Keyvisual nicht gleichzeitig platzieren** — Die Aurora-Animation ersetzt den Keyvisual als visuelles Element. Beide zusammen erzeugen visuelles Rauschen.
- **Performance:** Die Animation nutzt CSS `@keyframes` und ist GPU-beschleunigt. Auf älteren Geräten ggf. `prefers-reduced-motion` respektieren.
- **Text-Kontrast:** Alle Texte auf der Aurora müssen Weiß sein (Kontrast gegen Deep Green: 9.84 — PASS).

## Wann einsetzen

- Landing Pages mit emotionalem Einstieg
- Produkt-Launch-Seiten
- Event-Ankündigungen
- Über-uns-Seiten

## Wann NICHT einsetzen

- Technische Dokumentation (zu verspielt)
- Fachbetrieb-Kontext (Lime verboten)
- Produkt-Detailseiten (lenkt von Specs ab)
- Mobile-First-Layouts (Performance)
