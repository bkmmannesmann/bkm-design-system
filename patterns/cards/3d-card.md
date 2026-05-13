# 3D Card Effect

> Card-Komponente mit perspektivischer Kipp-Animation bei Hover. Die Karte reagiert auf die Mausposition und kippt dreidimensional, was Tiefe und Interaktivität erzeugt.

## Metadaten

| Eigenschaft | Wert |
|-------------|------|
| **Quelle** | [Aceternity UI — 3D Card Effect](https://ui.aceternity.com/components/3d-card-effect) |
| **Lizenz** | MIT |
| **Tech** | React, Framer Motion, CSS Transforms |
| **Kontext** | Beide (BKM AG + Fachbetrieb) |
| **Einsatz** | Feature-Präsentationen, Produkt-Highlights, Team-Karten |

## BKM-Farbmapping

| Parameter | BKM AG | Fachbetrieb |
|-----------|--------|-------------|
| Card-Hintergrund | `#ffffff` (Surface) | `#ffffff` (Surface) |
| Card-Shadow | `var(--bkm-shadow-subtle)` | `var(--bkm-shadow-subtle)` |
| Card-Shadow-Hover | `var(--bkm-shadow-elevated)` | `var(--bkm-shadow-elevated)` |
| Akzent-Element | `#b4e717` (Lime) | `#4daf46` (Pure Green) |
| Card-Radius | `12px` (rounded.lg) | `12px` (rounded.lg) |
| Max. Rotation | 10° | 10° |

## Installation

```bash
npx shadcn@latest add @aceternity/3d-card
```

## BKM-angepasster Code

```tsx
import { CardContainer, CardBody, CardItem } from "@/components/ui/3d-card";

interface Bkm3DCardProps {
  image: string;
  badge: string;
  title: string;
  description: string;
  context?: "ag" | "fachbetrieb";
}

export function Bkm3DCard({
  image,
  badge,
  title,
  description,
  context = "ag",
}: Bkm3DCardProps) {
  const badgeBg = context === "ag" ? "#1c4b42" : "#287d4b";
  const badgeText = context === "ag" ? "#b4e717" : "#ffffff";

  return (
    <CardContainer className="inter-var">
      <CardBody
        className="bg-white rounded-[12px] p-6 w-full
          shadow-[rgba(0,0,0,0.08)_0px_0px_0px_1px,rgba(0,0,0,0.04)_0px_2px_4px]
          hover:shadow-[rgba(0,0,0,0.08)_0px_0px_0px_1px,rgba(0,0,0,0.08)_0px_12px_24px_-8px]"
      >
        <CardItem translateZ="50" className="w-full">
          <img
            src={image}
            alt={title}
            className="w-full h-48 object-cover rounded-[8px]"
          />
        </CardItem>
        <CardItem translateZ="30" className="mt-4">
          <span
            className="inline-flex font-['Inter'] text-xs font-bold uppercase tracking-[0.05em] px-2.5 py-1 rounded-[4px]"
            style={{ backgroundColor: badgeBg, color: badgeText }}
          >
            {badge}
          </span>
        </CardItem>
        <CardItem translateZ="40" className="mt-3">
          <h3 className="font-['Unbounded'] text-lg font-black uppercase tracking-tight text-[#1a1a1a]">
            {title}
          </h3>
        </CardItem>
        <CardItem translateZ="20" className="mt-2">
          <p className="font-['Inter'] text-sm text-[#494949] leading-relaxed">
            {description}
          </p>
        </CardItem>
      </CardBody>
    </CardContainer>
  );
}
```

## Einschränkungen

- **Keine CSS `border`** — Shadow-as-border.
- **Max. Rotation 10°** — Stärkere Kippung wirkt verspielt und widerspricht der BKM-Ästhetik.
- **`translateZ` Werte moderat halten** — 20–50px für subtile Tiefe. Keine extremen Parallax-Effekte.
- **Touch-Geräte:** Kein Kipp-Effekt auf Touch. Fällt auf Standard-Shadow-Hover zurück.
- **Nicht in Karussells verschachteln** — 3D-Effekt + Karussell-Scroll erzeugt Motion Sickness.
