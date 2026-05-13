# Compare (Vorher/Nachher Slider)

> Interaktiver Bild-Vergleich mit Slider. Zeigt zwei übereinanderliegende Bilder, die per Drag getrennt werden. Ideal für Bauchemie-Anwendungen: feuchte Wand → trockene Wand.

## Metadaten

| Eigenschaft | Wert |
|-------------|------|
| **Quelle** | [Aceternity UI — Compare](https://ui.aceternity.com/components/compare) |
| **Lizenz** | MIT |
| **Tech** | React, Framer Motion, Tailwind CSS |
| **Kontext** | Beide (BKM AG + Fachbetrieb) |
| **Einsatz** | Referenz-Projekte, Produkt-Demos, Schadensanalyse-Ergebnisse |

## BKM-Relevanz

Dieses Pattern ist besonders wertvoll für BKM, weil es die **Kerngeschichte der Marke** visuell erzählt: von Feuchtigkeit (Problem) zu Trockenheit (Lösung). Der Slider-Mechanismus ist die perfekte Metapher für die Barriere, die BKM-Produkte bilden.

| Seite | Bedeutung | Visuelle Sprache |
|-------|-----------|-----------------|
| Links (vorher) | Feuchte Wand, Schaden, Problem | Dunkle Töne, sichtbare Feuchtigkeit |
| Rechts (nachher) | Trockene Wand, Schutz, Lösung | Helle Töne, saubere Oberfläche |
| Slider-Linie | Die Barriere (Horizontalsperre) | BKM-Akzentfarbe |

## BKM-Farbmapping

| Parameter | BKM AG | Fachbetrieb |
|-----------|--------|-------------|
| Slider-Linie | `#b4e717` (Lime) | `#4daf46` (Pure Green) |
| Slider-Handle | `#1c4b42` (Deep Green) | `#494949` (Stone Grey) |
| Label "Vorher" | `#ffffff` auf halbtransparentem Deep Green | `#ffffff` auf halbtransparentem Stone Grey |
| Label "Nachher" | `#b4e717` auf halbtransparentem Deep Green | `#4daf46` auf halbtransparentem Stone Grey |
| Container-Shadow | `var(--bkm-shadow-featured)` | `var(--bkm-shadow-featured)` |
| Container-Radius | `12px` (rounded.lg) | `12px` (rounded.lg) |

## Installation

```bash
npx shadcn@latest add @aceternity/compare
```

## BKM-angepasster Code

```tsx
import { Compare } from "@/components/ui/compare";

interface BkmCompareProps {
  beforeImage: string;
  afterImage: string;
  beforeLabel?: string;
  afterLabel?: string;
  context?: "ag" | "fachbetrieb";
  className?: string;
}

export function BkmCompare({
  beforeImage,
  afterImage,
  beforeLabel = "VORHER",
  afterLabel = "NACHHER",
  context = "ag",
  className = "",
}: BkmCompareProps) {
  const accentColor = context === "ag" ? "#b4e717" : "#4daf46";
  const handleColor = context === "ag" ? "#1c4b42" : "#494949";

  return (
    <div
      className={`relative rounded-[12px] overflow-hidden
        shadow-[rgba(0,0,0,0.08)_0px_0px_0px_1px,rgba(0,0,0,0.06)_0px_8px_16px_-4px]
        ${className}`}
    >
      <Compare
        firstImage={beforeImage}
        secondImage={afterImage}
        className="w-full aspect-[16/10]"
        slideMode="hover"
        sliderLineColor={accentColor}
        sliderHandleColor={handleColor}
      />
      {/* Labels */}
      <div className="absolute top-4 left-4 z-10">
        <span
          className="font-['Unbounded'] text-xs font-black uppercase tracking-[0.05em] px-3 py-1.5 rounded-[4px]"
          style={{
            backgroundColor: `${handleColor}cc`,
            color: "#ffffff",
          }}
        >
          {beforeLabel}
        </span>
      </div>
      <div className="absolute top-4 right-4 z-10">
        <span
          className="font-['Unbounded'] text-xs font-black uppercase tracking-[0.05em] px-3 py-1.5 rounded-[4px]"
          style={{
            backgroundColor: `${handleColor}cc`,
            color: accentColor,
          }}
        >
          {afterLabel}
        </span>
      </div>
    </div>
  );
}
```

## Anwendungsbeispiel

```tsx
// Referenz-Projekt: Horizontalsperre
<BkmCompare
  beforeImage="/images/referenz/keller-feucht.jpg"
  afterImage="/images/referenz/keller-trocken.jpg"
  beforeLabel="FEUCHT"
  afterLabel="TROCKEN"
  context="fachbetrieb"
/>

// Produkt-Demo: Fassadenschutz
<BkmCompare
  beforeImage="/images/produkt/fassade-vorher.jpg"
  afterImage="/images/produkt/fassade-nachher.jpg"
  context="ag"
/>
```

## Einschränkungen

- **Bilder müssen identische Dimensionen haben** — Beide Bilder müssen exakt gleich groß sein, sonst verschiebt sich der Vergleich.
- **Keine CSS `border`** — Container nutzt shadow-as-border.
- **Labels in Unbounded** — Auch die kleinen Labels folgen der Unbounded-Regel (900, uppercase).
- **Touch-Support:** Der Slider funktioniert auch auf Touch-Geräten (Drag statt Hover).
- **Bildqualität:** Vorher/Nachher-Bilder sollten professionell fotografiert sein. Schlechte Bildqualität zerstört den Effekt.

## Wann einsetzen

- Referenz-Projekte (feuchte → trockene Wand)
- Produkt-Demos (unbehandelt → behandelt)
- Schadensanalyse-Berichte
- Landing Pages für Fachbetriebe

## Wann NICHT einsetzen

- Ohne echte Vorher/Nachher-Bilder (keine Stockfotos)
- Für rein dekorative Zwecke
- In technischen Datenblättern
- Mehr als 2 Compare-Elemente pro Seite
