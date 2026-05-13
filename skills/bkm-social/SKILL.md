# BKM Social Media — Skill

> Generiert brand-konforme Social-Media-Grafiken, Stories und Carousel-Posts im BKM Mannesmann Design System. Output: einzelne Bild-Dateien (PNG/JPG) oder HTML-Vorlagen.

## Wann diesen Skill verwenden

- Wenn Social-Media-Posts (Instagram, LinkedIn, Facebook) im BKM-Stil erstellt werden sollen
- Wenn Story-Grafiken oder Carousel-Posts benötigt werden
- Wenn Social-Media-Vorlagen für Fachbetriebe erstellt werden sollen

## Workflow

### 1. Format bestimmen

| Format | Seitenverhältnis | Pixel | Einsatz |
|--------|-----------------|-------|---------|
| **Instagram Post** | 1:1 | 1080 × 1080 | Feed-Posts |
| **Instagram Story** | 9:16 | 1080 × 1920 | Stories, Reels-Cover |
| **LinkedIn Post** | 1.91:1 | 1200 × 628 | Feed-Posts |
| **LinkedIn Carousel** | 1:1 | 1080 × 1080 | Carousel-Slides |
| **Facebook Post** | 1.91:1 | 1200 × 628 | Feed-Posts |
| **Facebook Cover** | 2.7:1 | 1640 × 624 | Seiten-Cover |

### 2. Kontext bestimmen

| Kontext | Wann | Farben |
|---------|------|--------|
| **BKM AG** | Corporate-Kanäle, Produkt-Marketing | Deep Green + Lime |
| **Fachbetrieb** | Lokale Fachbetrieb-Kanäle, Partner-Content | Stone Grey + Pure Green |

### 3. Design System laden

Lies `../../DESIGN.md` für die vollständige Token-Referenz.

### 4. Post-Typen

#### Typ A: Produkt-Post (BKM AG)

```
┌──────────────────────────┐
│  Deep Green Hintergrund  │
│  + Noise Texture         │
│                          │
│  [Label] TT Norms Pro 700 13px  │
│  [Headline] Unbounded    │
│  900 UPPERCASE           │
│                          │
│  ─── Lime Divider ───    │
│                          │
│  [Produktbild]           │
│                          │
│  [CTA Badge] Lime        │
│                          │
│  ── Logo: White ──       │
└──────────────────────────┘
```

#### Typ B: Referenz-Post (Fachbetrieb)

```
┌──────────────────────────┐
│  [Vorher/Nachher Bild]   │
│  (obere Hälfte)          │
│                          │
│  Stone Grey Band         │
│  [Headline] Unbounded    │
│  [Body] TT Norms Pro            │
│                          │
│  [Badge] Transition      │
│  Green + Weiß            │
│                          │
│  Logo: StoneGrey+        │
│  PureGreen               │
└──────────────────────────┘
```

#### Typ C: Statistik-Post (Beide)

```
┌──────────────────────────┐
│  Hintergrund (Kontext)   │
│  + Noise Texture         │
│                          │
│  [Große Zahl]            │
│  TT Norms Pro 500          │
│  Akzentfarbe             │
│                          │
│  [Erklärung]             │
│  TT Norms Pro 400               │
│                          │
│  ── Logo ──              │
└──────────────────────────┘
```

#### Typ D: Carousel-Post (Beide)

Jede Slide folgt dem gleichen Layout-Schema, aber mit wechselnden Hintergründen (dunkel/hell alternierend):

```
Slide 1: Titel (dunkel)
Slide 2: Inhalt (hell)
Slide 3: Inhalt (dunkel)
Slide 4: Daten (hell)
Slide 5: CTA (dunkel)
```

### 5. Typografie auf Social Media

Aufgrund der kleineren Bildschirmgrößen gelten angepasste Mindestgrößen:

| Element | Mindestgröße (1080px Breite) |
|---------|------------------------------|
| Headline (Unbounded 900 UPPERCASE) | 36px |
| Body (TT Norms Pro 400) | 24px |
| Label (TT Norms Pro 700 UPPERCASE) | 16px |
| Technische Werte (TT Norms Pro 500) | 28px |
| Logo | Min. 80px Breite |

### 6. Safe Zones

Social-Media-Plattformen beschneiden Bilder unterschiedlich. Halte kritische Inhalte innerhalb der Safe Zone:

```
┌─────────────────────────────┐
│  ┌─────────────────────┐    │
│  │                     │    │
│  │    SAFE ZONE        │    │
│  │    (80% der Fläche) │    │
│  │                     │    │
│  └─────────────────────┘    │
│  10% Rand auf allen Seiten  │
└─────────────────────────────┘
```

## Kritische Regeln

1. **Lime Green nur im BKM AG Kontext** — Nie im Fachbetrieb.
2. **Unbounded: weight 900, uppercase** — Auch auf Social Media.
3. **Technische Werte in TT Norms Pro** — Preise, Maße, Prozente.
4. **Pure Green nie als Text auf hellem Hintergrund.**
5. **Logo immer sichtbar** — Auf jeder Grafik, in der korrekten Variante.
6. **Noise Texture auf dunklen Flächen** — Für Materialität.
7. **Keine Gradients als Übergang** — Harte Schnitte zwischen Farbflächen.
8. **Hashtags:** Nie auf der Grafik selbst. Nur im Post-Text.

## Abhängigkeiten

Keine. Social-Media-Grafiken werden als einzelne HTML-Dateien generiert und per Screenshot exportiert, oder direkt als Bild-Dateien über Bildgenerierung erstellt.
