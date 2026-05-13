# Spotlight Card

> Card-Komponente mit Cursor-Tracking Glow-Effekt. Der Spotlight folgt der Mausbewegung und erzeugt einen subtilen Lichtschein auf der Kartenoberfläche.

## Metadaten

| Eigenschaft | Wert |
|-------------|------|
| **Quelle** | [Componentry — Spotlight Card](https://www.componentry.fun/docs/components/spotlight-card) |
| **Lizenz** | MIT |
| **Tech** | React, Tailwind CSS, CSS Radial Gradient |
| **Kontext** | Beide (BKM AG + Fachbetrieb) |
| **Einsatz** | Produkt-Showcases, Feature-Grids, Service-Übersichten |

## BKM-Farbmapping

| Parameter | BKM AG | Fachbetrieb |
|-----------|--------|-------------|
| Card-Hintergrund | `#ffffff` (Surface) | `#ffffff` (Surface) |
| Spotlight-Farbe | `rgba(180, 231, 23, 0.15)` (Lime, 15% Opazität) | `rgba(77, 175, 70, 0.15)` (Pure Green, 15% Opazität) |
| Card-Shadow | `var(--bkm-shadow-subtle)` | `var(--bkm-shadow-subtle)` |
| Card-Shadow-Hover | `var(--bkm-shadow-featured)` | `var(--bkm-shadow-featured)` |
| Badge-Farbe | Deep Green + Lime | Transition Green + Weiß |
| Headline-Font | Unbounded 900 uppercase | Unbounded 900 uppercase |
| Body-Font | TT Norms Pro 400 | TT Norms Pro 400 |
| Border-Radius | `12px` (rounded.lg) | `12px` (rounded.lg) |

## BKM-angepasster Code

```tsx
import { useRef, useState } from "react";

interface SpotlightCardProps {
  children: React.ReactNode;
  className?: string;
  context?: "ag" | "fachbetrieb";
}

export function BkmSpotlightCard({
  children,
  className = "",
  context = "ag",
}: SpotlightCardProps) {
  const divRef = useRef<HTMLDivElement>(null);
  const [position, setPosition] = useState({ x: 0, y: 0 });
  const [opacity, setOpacity] = useState(0);

  const spotlightColor =
    context === "ag"
      ? "rgba(180, 231, 23, 0.15)"  // Lime 15%
      : "rgba(77, 175, 70, 0.15)";  // Pure Green 15%

  const handleMouseMove = (e: React.MouseEvent<HTMLDivElement>) => {
    if (!divRef.current) return;
    const rect = divRef.current.getBoundingClientRect();
    setPosition({ x: e.clientX - rect.left, y: e.clientY - rect.top });
  };

  return (
    <div
      ref={divRef}
      onMouseMove={handleMouseMove}
      onMouseEnter={() => setOpacity(1)}
      onMouseLeave={() => setOpacity(0)}
      className={`relative overflow-hidden bg-white rounded-[12px]
        shadow-[rgba(0,0,0,0.08)_0px_0px_0px_1px,rgba(0,0,0,0.04)_0px_2px_4px]
        hover:shadow-[rgba(0,0,0,0.08)_0px_0px_0px_1px,rgba(0,0,0,0.06)_0px_8px_16px_-4px]
        hover:-translate-y-0.5 transition-all duration-200 ${className}`}
    >
      {/* Spotlight-Overlay */}
      <div
        className="pointer-events-none absolute inset-0 transition-opacity duration-300"
        style={{
          opacity,
          background: `radial-gradient(600px circle at ${position.x}px ${position.y}px, ${spotlightColor}, transparent 40%)`,
        }}
      />
      {/* Content */}
      <div className="relative z-10 p-8">{children}</div>
    </div>
  );
}
```

## Anwendungsbeispiel

```tsx
// BKM AG Kontext — Produkt-Showcase
<div className="grid grid-cols-1 md:grid-cols-3 gap-6">
  <BkmSpotlightCard context="ag">
    <span className="inline-flex bg-[#1c4b42] text-[#b4e717] font-['TT_Norms_Pro'] text-xs font-bold uppercase tracking-[0.05em] px-2.5 py-1 rounded-[4px]">
      PRO LINE
    </span>
    <h3 className="font-['Unbounded'] text-lg font-black uppercase tracking-tight text-[#1a1a1a] mt-4">
      KELLERSCHUTZ PRO
    </h3>
    <p className="font-['TT_Norms_Pro'] text-base text-[#494949] mt-3 leading-relaxed">
      Professionelle Horizontalsperre mit MicroPorex® Technologie.
    </p>
    <span className="inline-block mt-4 font-['TT_Norms_Pro'] text-sm font-medium text-[#1c4b42]">
      ab 89,90 €
    </span>
  </BkmSpotlightCard>
</div>

// Fachbetrieb Kontext — Service-Übersicht
<BkmSpotlightCard context="fachbetrieb">
  <span className="inline-flex bg-[#287d4b] text-white font-['TT_Norms_Pro'] text-xs font-bold uppercase tracking-[0.05em] px-2.5 py-1 rounded-[4px]">
    ZERTIFIZIERT
  </span>
  <h3 className="font-['Unbounded'] text-lg font-black uppercase tracking-tight text-[#1a1a1a] mt-4">
    HORIZONTALSPERRE
  </h3>
  <p className="font-['TT_Norms_Pro'] text-base text-[#494949] mt-3 leading-relaxed">
    Nachträgliche Horizontalsperre gegen aufsteigende Feuchtigkeit.
  </p>
</BkmSpotlightCard>
```

## Einschränkungen

- **Keine CSS `border` verwenden** — Die Card nutzt ausschließlich shadow-as-border (DESIGN.md Regel).
- **Spotlight-Opazität max. 15%** — Höhere Werte erzeugen zu starken Kontrast und lenken vom Inhalt ab.
- **Nur auf hellen Hintergründen** — Auf dunklen Flächen (Deep Green, Stone Grey) ist der Spotlight-Effekt nicht sichtbar genug.
- **Touch-Geräte:** Der Cursor-Tracking-Effekt funktioniert nicht auf Touch-Geräten. Die Card fällt dann auf den Standard-Hover-Effekt (Shadow-Escalation + translateY) zurück.
