# Noise Texture

> Subtile Rausch-Textur als CSS-Overlay auf Hintergrundflächen. Verleiht flachen Farbflächen eine physische, materielle Qualität — passend zur BKM-Identität als Baustoff-Hersteller.

## Metadaten

| Eigenschaft | Wert |
|-------------|------|
| **Quelle** | [Componentry — Noise Background](https://www.componentry.fun/docs/hero-backgrounds/noise) |
| **Lizenz** | MIT |
| **Tech** | CSS (SVG Filter), kein JavaScript |
| **Kontext** | Beide (BKM AG + Fachbetrieb) |
| **Einsatz** | Hintergrundflächen, Hero-Sektionen, Cards auf dunklen Flächen |

## BKM-Relevanz

BKM handelt mit physischen Baustoffen — Mörtel, Injektionsharze, Abdichtungsmassen. Eine subtile Rausch-Textur auf Farbflächen vermittelt Materialität und Haptik. Die Fläche wirkt nicht mehr digital-flach, sondern wie eine gestrichene Wand oder eine Betonoberfläche.

## BKM-Farbmapping

| Fläche | Basis-Farbe | Noise-Opazität | Effekt |
|--------|-------------|----------------|--------|
| Deep Green Hero | `#1c4b42` | 0.03–0.05 | Subtile Wandtextur |
| Sand White Sektion | `#f6f5f2` | 0.02–0.03 | Papier-/Putzstruktur |
| Stone Grey Nav | `#494949` | 0.04 | Beton-Anmutung |
| Weiße Cards | `#ffffff` | 0.015 | Kaum sichtbar, aber fühlbar |

## CSS-Implementation (Zero Dependencies)

```css
/* Noise-Textur als CSS-only Lösung */
.bkm-noise {
  position: relative;
  isolation: isolate;
}

.bkm-noise::after {
  content: "";
  position: absolute;
  inset: 0;
  z-index: 1;
  pointer-events: none;
  opacity: 0.04;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.65' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)'/%3E%3C/svg%3E");
  background-repeat: repeat;
  background-size: 256px 256px;
  mix-blend-mode: overlay;
}

/* Varianten nach Opazität */
.bkm-noise--subtle::after { opacity: 0.02; }
.bkm-noise--medium::after { opacity: 0.04; }
.bkm-noise--strong::after { opacity: 0.06; }
```

## Tailwind-Integration

```tsx
// Als Utility-Klasse in tailwind.config
// Oder direkt als CSS-Klasse verwenden

// BKM AG Hero mit Noise
<section className="bkm-noise bkm-noise--medium bg-[#1c4b42] min-h-[560px]">
  <div className="relative z-10 max-w-[1280px] mx-auto px-8 md:px-16 py-40">
    {/* Content über der Noise-Textur */}
  </div>
</section>

// Sand White Sektion mit Noise
<section className="bkm-noise bkm-noise--subtle bg-[#f6f5f2] py-20">
  <div className="relative z-10">
    {/* Content */}
  </div>
</section>
```

## Einschränkungen

- **Opazität nie über 0.06** — Stärkere Werte wirken schmutzig statt materiell.
- **Content muss `z-10` haben** — Damit Text über der Noise-Schicht liegt.
- **Nicht auf Bildern** — Noise nur auf Farbflächen, nie über Fotografien.
- **Performance:** SVG-Filter sind leichtgewichtig, keine Bedenken.
- **Print:** Noise wird beim Drucken ignoriert (CSS `::after`).

## Wann einsetzen

- Jede größere Farbfläche (Hero, CTA, Footer)
- Dark-Mode-Sektionen (Deep Green, Stone Grey)
- Sand White Hintergründe für mehr Tiefe

## Wann NICHT einsetzen

- Über Fotografien oder Illustrationen
- Auf sehr kleinen Flächen (Buttons, Badges)
- In Kombination mit Aurora Background (doppelte Textur)
