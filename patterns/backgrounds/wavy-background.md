# Wavy Background

> Animierte Wellen-Hintergrund mit sanften, sich bewegenden Wellenlinien. Erzeugt organische Tiefe, ohne die BKM-Regel "harte Schnitte zwischen Oberflächen" zu verletzen — die Wellen sind ein **Hintergrund-Effekt innerhalb einer Fläche**, kein Übergang zwischen Flächen.

## Metadaten

| Eigenschaft | Wert |
|-------------|------|
| **Quelle** | [Aceternity UI — Wavy Background](https://ui.aceternity.com/components/wavy-background) |
| **Lizenz** | MIT |
| **Tech** | React, Canvas API, Tailwind CSS |
| **Kontext** | Beide (BKM AG + Fachbetrieb) |
| **Einsatz** | Sektions-Hintergründe, CTA-Bereiche, Testimonial-Sektionen |

## Wichtige Abgrenzung zur DESIGN.md

DESIGN.md verbietet "Gradients, waves, or diagonals" als **Übergänge zwischen Oberflächen-Modi** (dunkel → hell). Dieses Pattern ist kein Übergang — es ist ein animierter Hintergrund **innerhalb** einer einzelnen Fläche. Die harten Schnitte zwischen Sektionen bleiben erhalten.

```
✅ ERLAUBT:
┌──────────────────────────────┐
│  Deep Green Fläche           │  ← Harter Schnitt oben
│  ~~~~ Wavy Animation ~~~~    │  ← Wellen innerhalb der Fläche
│  ~~~~ Wavy Animation ~~~~    │
└──────────────────────────────┘  ← Harter Schnitt unten

❌ VERBOTEN:
┌──────────────────────────────┐
│  Deep Green Fläche           │
│  ~~~~~ Wellen-Übergang ~~~~~ │  ← Weicher Übergang zur nächsten Fläche
│  Sand White Fläche           │
└──────────────────────────────┘
```

## BKM-Farbmapping

| Parameter | BKM AG (dunkel) | BKM AG (hell) | Fachbetrieb |
|-----------|-----------------|---------------|-------------|
| Basis-Hintergrund | `#1c4b42` (Deep Green) | `#f6f5f2` (Sand White) | `#f6f5f2` (Sand White) |
| Wellen-Farbe 1 | `#2a6b5e` (Deep Green Light) | `#e8e6e1` (Outline Variant) | `#e8e6e1` |
| Wellen-Farbe 2 | `#287d4b` (Transition Green) | `#c8c5be` (Outline) | `#c8c5be` |
| Wellen-Opazität | 0.3 | 0.2 | 0.2 |
| Text | `#ffffff` | `#1a1a1a` | `#1a1a1a` |

## Installation

```bash
npx shadcn@latest add @aceternity/wavy-background
```

## BKM-angepasster Code

```tsx
import { WavyBackground } from "@/components/ui/wavy-background";

// BKM AG — Dunkle CTA-Sektion
export function BkmCtaWavy() {
  return (
    <WavyBackground
      className="min-h-[400px] flex items-center"
      colors={["#2a6b5e", "#287d4b", "#1c4b42", "#2a6b5e"]}
      waveOpacity={0.3}
      backgroundFill="#1c4b42"
      speed="slow"
    >
      <div className="max-w-[1280px] mx-auto px-8 md:px-16 text-center">
        <h2 className="font-['Unbounded'] text-3xl md:text-5xl font-black uppercase text-white tracking-tight">
          BERATUNG ANFORDERN
        </h2>
        <p className="font-['Inter'] text-lg text-white/70 mt-4 max-w-[600px] mx-auto">
          Unsere Experten analysieren Ihr Feuchtigkeitsproblem und empfehlen die passende Lösung.
        </p>
        <button className="mt-8 bg-[#b4e717] text-[#1c4b42] font-['Unbounded'] text-sm font-black uppercase px-6 py-3 h-12 rounded-[4px] hover:bg-white transition-colors">
          JETZT KONTAKT AUFNEHMEN
        </button>
      </div>
    </WavyBackground>
  );
}
```

## Einschränkungen

- **Kein Übergang zwischen Flächen** — Nur als Hintergrund innerhalb einer Sektion.
- **Wellen-Opazität max. 0.3** — Subtil halten, nicht dominant.
- **Speed: "slow"** — Schnelle Wellen wirken unruhig und widersprechen der BKM-Ästhetik.
- **Performance:** Canvas-basiert, GPU-beschleunigt. `prefers-reduced-motion` respektieren.
