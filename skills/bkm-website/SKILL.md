# BKM Website Skill — v2

> Generiert **Awwwards-Level** Websites im BKM Mannesmann Design System.  
> Vanilla HTML/CSS/JS · Selbst-enthalten · Motion Design · Kein Build-Toolchain nötig.

---

## Sofortstart

**Lies zuerst das fertige Template:**  
→ `../../examples/bkm-website-v2-template.html`

Das Template ist die **Single Source of Truth** für alle Website-Generierungen.  
Verwende es als Basis, adaptiere Inhalt und Struktur, behalte alle Motion-Design-Patterns.

---

## Architektur-Entscheidung

| Ansatz | Wann |
|--------|------|
| **Self-contained HTML** (diese Skill) | Landing Pages, Showrooms, Pitch-Seiten, Kampagnenseiten |
| React + Tailwind | Wenn interaktive App-Logik nötig (Auth, API, State) |

Self-contained HTML ist **vorzuziehen** — kein Build-Toolchain, keine Dependencies, sofort deploybar.

---

## Design Tokens — Quick Reference

```css
/* Farben — BKM AG Kontext */
--c-dg:   #1c4b42;   /* Deep Green — Hauptflächen, Nav */
--c-dg2:  #122e27;   /* Deep Green 2 — dunkelste Flächen */
--c-lime: #b4e717;   /* Lime — Akzent NUR BKM AG, nie Fachbetrieb */
--c-tg:   #287d4b;   /* Transition Green — Links, Steps */
--c-sand: #f6f5f2;   /* Sand White — helle Flächen */

/* Typografie */
--f-display: 'Unbounded', sans-serif;   /* Headlines: immer 900, UPPERCASE */
--f-body:    'TT Norms Pro', system-ui; /* Body, Labels */

/* Assets-Pfad */
../assets/fonts/Unbounded_900.woff2
../assets/fonts/TT_Norms_Pro_Compact_Regular.woff2
../assets/fonts/TT_Norms_Pro_Bold.woff2
../assets/backgrounds/bg-green-texture-1.jpg   /* bis bg-green-texture-4.jpg */
../assets/logos/bkm-logo-white.svg
../assets/logos/bkm-logo-black.svg
../assets/keyvisual/keyvisual-on-dark.png
```

---

## Seiten-Aufbau — Kanonische Sequenz

```
NAV          sticky, glassmorphism on scroll
HERO         100svh, Unbounded 900 in XL, cursor spotlight, word-reveal animation
MARQUEE      Infinite-scroll trust strip (lime background)
PROBLEM      Dark (--c-dg2), glassmorphism cards, diagonal top cut
SOLUTION     Split layout: visual panel + process steps
STATS        Bento Grid (12 col), lime accent cell, animated counters
PRODUCTS     Light (--c-sand), product cards mit Dark-Header / Light-Body
TESTIMONIALS Editorial: 1 dark featured + 2 light
CTA          Full-bleed dark, riesige Typo, magnetic buttons
FAQ          Accordion links + dark panel rechts
FOOTER       4-spaltig, --c-dg2 background
```

---

## Motion Design Patterns — Code

### 1. Word-Reveal (Hero Headline)

```css
.word { display: inline-block; overflow: hidden; }
.word-inner {
  display: inline-block;
  transform: translateY(110%);
  transition: transform 0.5s cubic-bezier(0.16, 1, 0.3, 1);
}
.word-inner.visible { transform: translateY(0); }
```
```js
const words = document.querySelectorAll('.word-inner');
words.forEach((w, i) => setTimeout(() => w.classList.add('visible'), 200 + i * 120));
```

### 2. Cursor Spotlight (auf Glasmorphismus-Cards)

```css
.glass-card {
  background-image: radial-gradient(
    600px circle at var(--cx, -9999px) var(--cy, -9999px),
    rgba(180,231,23,0.08), transparent 40%
  );
}
```
```js
card.addEventListener('mousemove', e => {
  const r = card.getBoundingClientRect();
  card.style.setProperty('--cx', (e.clientX - r.left) + 'px');
  card.style.setProperty('--cy', (e.clientY - r.top)  + 'px');
});
card.addEventListener('mouseleave', () => {
  card.style.setProperty('--cx', '-9999px');
  card.style.setProperty('--cy', '-9999px');
});
```

### 3. Scroll Reveal

```css
[data-reveal] {
  opacity: 0; transform: translateY(36px);
  transition: opacity .7s cubic-bezier(0.16, 1, 0.3, 1),
              transform .7s cubic-bezier(0.16, 1, 0.3, 1);
}
[data-reveal].in-view { opacity: 1; transform: translateY(0); }
[data-delay="1"] { transition-delay: .1s; }
[data-delay="2"] { transition-delay: .2s; }
```
```js
const io = new IntersectionObserver(entries => {
  entries.forEach(e => {
    if (e.isIntersecting) { e.target.classList.add('in-view'); io.unobserve(e.target); }
  });
}, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });
document.querySelectorAll('[data-reveal]').forEach(el => io.observe(el));
```

### 4. Animated Number Counter

```html
<div class="js-count" data-to="47" data-suffix="+">0</div>
```
```js
const io = new IntersectionObserver(entries => {
  entries.forEach(e => {
    if (!e.isIntersecting) return;
    const el = e.target;
    const to = parseInt(el.dataset.to);
    const suffix = el.dataset.suffix || '';
    const dur = 1800;
    const start = performance.now();
    function tick(now) {
      const t = Math.min((now - start) / dur, 1);
      const ease = 1 - Math.pow(1 - t, 3);  /* ease-out-cubic */
      el.textContent = Math.floor(ease * to) + suffix;
      if (t < 1) requestAnimationFrame(tick);
    }
    requestAnimationFrame(tick);
    io.unobserve(el);
  });
}, { threshold: 0.5 });
```

### 5. Magnetic Button

```html
<div class="btn-magnetic">
  <a href="#" class="btn btn-primary">Label</a>
</div>
```
```js
document.querySelectorAll('.btn-magnetic').forEach(wrap => {
  const btn = wrap.querySelector('.btn');
  wrap.addEventListener('mousemove', e => {
    const r = wrap.getBoundingClientRect();
    const dx = (e.clientX - (r.left + r.width/2))  * 0.35;
    const dy = (e.clientY - (r.top  + r.height/2)) * 0.35;
    btn.style.transform = `translate(${dx}px, ${dy}px)`;
  });
  wrap.addEventListener('mouseleave', () => btn.style.transform = '');
});
```

### 6. Parallax Hero Background Text

```js
const el = document.getElementById('heroBgWord');
window.addEventListener('scroll', () => {
  el.style.transform = `translate(-50%, calc(-50% + ${window.scrollY * 0.3}px))`;
}, { passive: true });
```

### 7. Diagonal Section Cut (CSS only)

```css
/* Oben abschneiden — weißer Keil bleibt oben */
.dark-section::before {
  content: ''; position: absolute; top: -1px; left: 0; right: 0;
  height: 90px; background: var(--c-white);    /* Farbe der DARÜBERLIEGENDEN Sektion */
  clip-path: polygon(0 0, 100% 0, 100% 100%);  /* Rechteck bleibt rechts stehen */
  pointer-events: none;
}

/* Unten abschneiden — Keil rechts */
.dark-section::after {
  content: ''; position: absolute; bottom: -1px; left: 0; right: 0;
  height: 90px; background: var(--c-sand);     /* Farbe der DARUNTER liegenden Sektion */
  clip-path: polygon(0 100%, 100% 100%, 100% 0);
  pointer-events: none;
}
```

### 8. Infinite Marquee Strip

```css
.marquee-track {
  display: flex;
  animation: marquee 28s linear infinite;
  will-change: transform;
}
.marquee-track:hover { animation-play-state: paused; }
@keyframes marquee {
  from { transform: translateX(0); }
  to   { transform: translateX(-50%); }  /* Content muss 2× wiederholt sein */
}
```

### 9. Glassmorphismus Card

```css
.glass-card {
  background: rgba(255,255,255,0.055);
  backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 24px;
  position: relative; overflow: hidden;
}
.glass-card::before {   /* Oberkante-Schimmer */
  content: ''; position: absolute; top: 0; left: 0; right: 0; height: 1px;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,.25), transparent);
}
.glass-card:hover {
  border-color: rgba(255,255,255,.14);
  transform: translateY(-4px);
}
```

### 10. Bento Grid (12-spaltig, responsive)

```css
.bento {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: 16px;
}
.bc-4 { grid-column: span 4; }
.bc-7 { grid-column: span 7; }
.bc-5 { grid-column: span 5; }

@media (max-width: 1024px) {
  .bento { grid-template-columns: repeat(6, 1fr); }
  .bc-4, .bc-5 { grid-column: span 3; }
  .bc-7, .bc-8 { grid-column: span 6; }
}
@media (max-width: 768px) {
  .bento { grid-template-columns: 1fr 1fr; }
  .bc-4, .bc-5, .bc-7, .bc-8 { grid-column: span 2; }
}
```

---

## Buttons — System

```html
<!-- Primary — Lime, für 1× pro Viewport -->
<a href="#" class="btn btn-primary btn-lg">CTA Text</a>

<!-- Ghost — auf Dark-Flächen -->
<a href="#" class="btn btn-ghost btn-lg">Sekundär</a>

<!-- Dark — auf hellen Flächen -->
<a href="#" class="btn btn-dark">Aktion</a>

<!-- Magnetic Wrapper — für CTAs -->
<div class="btn-magnetic">
  <a href="#" class="btn btn-primary btn-xl">Hauptaktion</a>
</div>
```

Größen: `.btn` (48px) · `.btn-lg` (56px) · `.btn-xl` (64px)

---

## Typografie-Regel

| Einsatz | Klasse / Property | Wert |
|---------|-------------------|------|
| Hero H1 | `font-size: clamp(52px, 9vw, 128px)` | Unbounded 900, UPPERCASE |
| Section H2 | `font-size: clamp(32px, 4vw, 56px)` | Unbounded 900, letter-spacing -0.03em |
| Card Title | `font-size: 19–22px` | Unbounded 900 |
| Body | `font-size: 14–18px` | TT Norms Pro 400, line-height 1.65–1.7 |
| Label/Eyebrow | `font-size: 11–12px` | TT Norms Pro 700, letter-spacing .10em, UPPERCASE |

**Niemals:** Italic, Font-Weight unter 700 für Headlines, Lime auf hellem Hintergrund als Text.

---

## Sektion-Farb-System

| Sektion | Background | Headline | Body | Akzent |
|---------|-----------|----------|------|--------|
| Hero | `--c-dg2` | `--c-white` | rgba(white,0.6) | `--c-lime` |
| Problem | `--c-dg2` | `--c-white` | rgba(white,0.55) | `--c-lime` |
| Solution | `--c-white` | `--c-black` | `--c-stone` | `--c-tg` |
| Stats | `--c-dg` | `--c-white` | rgba(white,0.35) | `--c-lime` |
| Products | `--c-sand` | `--c-black` | `--c-stone` | `--c-tg` |
| Testimonials | `--c-white` | — | `--c-stone` | `--c-lime` |
| CTA | `--c-dg` | `--c-white` | rgba(white,0.5) | `--c-lime` |
| FAQ | `--c-sand` | `--c-black` | `--c-stone` | `--c-tg` |
| Footer | `--c-dg2` | `--c-white` | rgba(white,0.4) | `--c-lime` |

---

## Kritische Regeln (Nicht brechen)

1. **Lime NUR BKM AG** — nie im Fachbetrieb-Kontext
2. **Unbounded immer 900** — nie dünner für Headlines
3. **Harte Schnitte zwischen Sektionen** — keine sanften Gradient-Übergänge
4. **Shadow-as-Border** — kein `border` auf Cards, stattdessen `box-shadow`
5. **Keyvisual** — nie in Code nachbauen, immer vorgerendertes `keyvisual-on-dark.png` verwenden
6. **Max. 1 Primary Button** (Lime) pro sichtbarem Viewport
7. **Fonts lokal einbinden** — kein Google Fonts CDN, woff2 aus `../assets/fonts/`
8. **Diagonal-Cuts immer in `::before`/`::after`** — nie als separates Element

---

## Fachbetrieb-Variante

Wenn Kontext = Fachbetrieb:

```css
/* Statt: */
--c-dg:   #1c4b42;
--c-lime: #b4e717;

/* Verwende: */
--c-primary:  #4daf46;   /* Pure Green */
--c-deep:     #287d4b;   /* Transition Green */
/* Kein Lime! Kein Deep Green! */

/* Logo: */
../assets/logos/bkm-logo-stonegrey-puregreen.svg
```

---

## Awwwards-Level Checkliste

Bevor die Website abgegeben wird, prüfen:

- [ ] Hero-Headline nutzt `clamp()` — nie fixe px auf mobil
- [ ] Word-Reveal Animation aktiv (JS)
- [ ] Cursor Spotlight auf Glasmorphismus-Cards
- [ ] Scroll Reveal auf allen Sektions-Headings + Cards (`data-reveal`)
- [ ] Number Counter auf Stats-Zellen (`js-count`, `data-to`)
- [ ] Magnetic Button auf Haupt-CTA
- [ ] Nav wird glassmorphisch beim Scrollen
- [ ] Marquee Strip vorhanden
- [ ] Diagonale Schnitte zwischen Dark/Light Sektionen
- [ ] Fonts lokal eingebunden (kein CDN)
- [ ] Mobile getestet (320px Minimum)
- [ ] Textur-Overlays auf Dark-Sektionen (`bg-green-texture-*.jpg`)
- [ ] Keyvisual eingebunden
- [ ] Logo mit `onerror`-Fallback auf Text

---

## Inspiration & Referenzlevel

Zielästhetik: **Awwwards · Brutalism meets Swiss** — große Typografie, starke Farbmomente,
präzise Motion, keine Spielereien ohne Funktion.

Konkrete Referenzprojekte die Orientierung geben:
- Stripe.com (Trust + Motion)
- Linear.app (Glassmorphism + Stats)
- Vercel.com (Dark + Lime-artiger Akzent)
- Loom.com (Bento Grid + Videos)
