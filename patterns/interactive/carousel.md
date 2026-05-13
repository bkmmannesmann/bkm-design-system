# Apple Cards Carousel

> Horizontaler Karussell-Effekt inspiriert von Apple's Produktseiten. Karten gleiten mit Parallax-Effekt und expandieren bei Klick zu einer Detailansicht.

## Metadaten

| Eigenschaft | Wert |
|-------------|------|
| **Quelle** | [Aceternity UI — Apple Cards Carousel](https://ui.aceternity.com/components/apple-cards-carousel) |
| **Lizenz** | MIT |
| **Tech** | React, Framer Motion, Tailwind CSS |
| **Kontext** | Beide (BKM AG + Fachbetrieb) |
| **Einsatz** | Referenz-Projekte, Produkt-Linien, Testimonials, Leistungsübersichten |

## BKM-Farbmapping

| Parameter | BKM AG | Fachbetrieb |
|-----------|--------|-------------|
| Card-Hintergrund | `#ffffff` (Surface) | `#ffffff` (Surface) |
| Card-Shadow | `var(--bkm-shadow-subtle)` | `var(--bkm-shadow-subtle)` |
| Card-Shadow-Active | `var(--bkm-shadow-elevated)` | `var(--bkm-shadow-elevated)` |
| Kategorie-Badge | Deep Green + Lime | Transition Green + Weiß |
| Titel-Font | Unbounded 900 uppercase | Unbounded 900 uppercase |
| Body-Font | Inter 400 | Inter 400 |
| Overlay-Hintergrund | `#1c4b42` (Deep Green, 90%) | `#494949` (Stone Grey, 90%) |
| Close-Button | `#b4e717` (Lime) | `#4daf46` (Pure Green) |
| Card-Radius | `12px` (rounded.lg) | `12px` (rounded.lg) |
| Sektions-Hintergrund | `#f6f5f2` (Sand White) | `#f6f5f2` (Sand White) |

## Installation

```bash
npx shadcn@latest add @aceternity/apple-cards-carousel
```

## BKM-angepasster Code

```tsx
import { Carousel, CarouselCard } from "@/components/ui/apple-cards-carousel";

interface BkmProject {
  title: string;
  category: string;
  image: string;
  description: string;
  specs?: { label: string; value: string }[];
}

interface BkmProjectCarouselProps {
  projects: BkmProject[];
  context?: "ag" | "fachbetrieb";
}

export function BkmProjectCarousel({
  projects,
  context = "ag",
}: BkmProjectCarouselProps) {
  const badgeBg = context === "ag" ? "#1c4b42" : "#287d4b";
  const badgeText = context === "ag" ? "#b4e717" : "#ffffff";

  return (
    <section className="bg-[#f6f5f2] py-20">
      <div className="max-w-[1280px] mx-auto px-8 md:px-16 mb-12">
        <h2 className="font-['Unbounded'] text-3xl md:text-4xl font-black uppercase text-[#1a1a1a] tracking-tight">
          {context === "ag" ? "REFERENZEN" : "UNSERE PROJEKTE"}
        </h2>
      </div>
      <Carousel>
        {projects.map((project, i) => (
          <CarouselCard
            key={i}
            className="bg-white rounded-[12px]
              shadow-[rgba(0,0,0,0.08)_0px_0px_0px_1px,rgba(0,0,0,0.04)_0px_2px_4px]
              hover:shadow-[rgba(0,0,0,0.08)_0px_0px_0px_1px,rgba(0,0,0,0.06)_0px_8px_16px_-4px]
              hover:-translate-y-0.5 transition-all duration-200"
            expandedContent={
              <ProjectDetail project={project} context={context} />
            }
          >
            <img
              src={project.image}
              alt={project.title}
              className="w-full h-48 object-cover rounded-t-[12px]"
            />
            <div className="p-6">
              <span
                className="inline-flex font-['Inter'] text-xs font-bold uppercase tracking-[0.05em] px-2.5 py-1 rounded-[4px]"
                style={{ backgroundColor: badgeBg, color: badgeText }}
              >
                {project.category}
              </span>
              <h3 className="font-['Unbounded'] text-base font-black uppercase tracking-tight text-[#1a1a1a] mt-3">
                {project.title}
              </h3>
            </div>
          </CarouselCard>
        ))}
      </Carousel>
    </section>
  );
}

function ProjectDetail({
  project,
  context,
}: {
  project: BkmProject;
  context: "ag" | "fachbetrieb";
}) {
  return (
    <div className="p-8">
      <p className="font-['Inter'] text-base text-[#494949] leading-relaxed">
        {project.description}
      </p>
      {project.specs && (
        <div className="mt-6 divide-y divide-[#e8e6e1]">
          {project.specs.map((spec, i) => (
            <div key={i} className="flex justify-between items-center py-3">
              <span className="font-['Inter'] text-sm text-[#6b6b6b]">
                {spec.label}
              </span>
              <span className="font-['Geist_Mono'] text-sm font-medium text-[#1c4b42]">
                {spec.value}
              </span>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
```

## Anwendungsbeispiel

```tsx
const referenzen: BkmProject[] = [
  {
    title: "ALTBAUSANIERUNG DÜSSELDORF",
    category: "HORIZONTALSPERRE",
    image: "/images/referenz/duesseldorf.jpg",
    description: "Nachträgliche Horizontalsperre in einem Gründerzeit-Altbau...",
    specs: [
      { label: "Wandstärke", value: "42 cm" },
      { label: "Injektionsmenge", value: "3,2 l/m" },
      { label: "Trocknungszeit", value: "12 Wochen" },
    ],
  },
  // ...
];

<BkmProjectCarousel projects={referenzen} context="fachbetrieb" />
```

## Einschränkungen

- **Keine CSS `border` auf Cards** — Shadow-as-border Technik.
- **Mindestens 3 Karten** — Das Karussell wirkt erst ab 3 Elementen. Optimal: 4–8.
- **Bilder:** Einheitliches Seitenverhältnis (16:10 empfohlen). Professionelle Fotografie.
- **Expanded Content:** Die Detailansicht öffnet als Overlay. Auf Mobile wird sie fullscreen.
- **Technische Werte in Geist Mono** — Auch in der Detailansicht gelten die Spec-Table-Regeln.

## Wann einsetzen

- Referenz-Projekte mit Bildern und technischen Details
- Produkt-Linien-Übersicht (Home Line, Pro Line)
- Fachbetrieb-Leistungen
- Testimonials / Kundenstimmen

## Wann NICHT einsetzen

- Weniger als 3 Elemente
- Reine Text-Inhalte ohne Bilder
- Technische Dokumentation
- Innerhalb anderer Karussells (kein Nesting)
