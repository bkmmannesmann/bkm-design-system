# BKM Slides — Fixed-Stage-Engine

> Die gemeinsame technische Grundlage **aller** Familien. Jede `demo.html` im Pack
> nutzt exakt diese Engine. Beim Bauen eines neuen Decks: diese Shell kopieren, dann
> Folien im Stil der gewählten Familie (`templates/<slug>/design.md`) füllen.

Inspiriert von `frontend-slides` (zarazhangrui/frontend-slides): **eine 1920×1080-Bühne,
die als Ganzes in den Viewport skaliert** — kein Reflow, kein responsives Umbrechen.
Was im Editor passt, passt überall (Beamer, PDF, Handy als Letterbox).

## Warum Fixed-Stage

- **Pixelgenau & vorhersehbar:** Position/Größe sind absolut auf 1920×1080. Keine
  Layout-Überraschungen auf anderen Bildschirmen.
- **Export-sicher:** PDF/Screenshot rendert identisch zur Ansicht.
- **Mobil:** Bühne wird letterboxed, statt Inhalt zu zerbrechen.

## Die Shell (1:1 kopieren)

```html
<div class="deck-viewport">
  <main class="deck-stage" id="deckStage">
    <section class="slide visible"> … Folie 1 … </section>
    <section class="slide">          … Folie 2 … </section>
    <!-- weitere Folien -->
  </main>
</div>
<div class="deck-controls">
  <button id="prev" aria-label="Zurück"><i class="fas fa-chevron-left"></i></button>
  <span class="count"><span id="cur">1</span> / <span id="tot">1</span></span>
  <button id="next" aria-label="Weiter"><i class="fas fa-chevron-right"></i></button>
</div>
```

```css
*{margin:0;padding:0;box-sizing:border-box;}
html,body{width:100%;height:100%;overflow:hidden;background:var(--stage-bg);}
.deck-viewport{position:fixed;inset:0;overflow:hidden;background:var(--stage-bg);}
.deck-stage{position:absolute;left:0;top:0;width:1920px;height:1080px;transform-origin:0 0;overflow:hidden;}
.slide{position:absolute;inset:0;width:1920px;height:1080px;overflow:hidden;
  visibility:hidden;opacity:0;pointer-events:none;}
.slide.visible{visibility:visible;opacity:1;pointer-events:auto;z-index:1;}

/* Reveal-Animation für Elemente mit .reveal */
.reveal{opacity:0;transform:translateY(28px);transition:opacity .7s var(--ease),transform .7s var(--ease);}
.slide.visible .reveal{opacity:1;transform:translateY(0);}
.d1{transition-delay:.08s;} .d2{transition-delay:.20s;} .d3{transition-delay:.32s;} .d4{transition-delay:.44s;}

/* Navigations-Leiste */
.deck-controls{position:fixed;left:50%;bottom:18px;transform:translateX(-50%);z-index:1000;
  display:flex;align-items:center;gap:6px;background:rgba(10,28,23,0.9);
  border:1px solid rgba(255,255,255,0.16);border-radius:999px;padding:8px 10px;color:#fff;font-size:13px;font-weight:600;}
.deck-controls button{all:unset;cursor:pointer;width:30px;height:30px;border-radius:50%;
  display:flex;align-items:center;justify-content:center;}
.deck-controls button:hover{background:rgba(255,255,255,0.16);}
.deck-controls .count{min-width:52px;text-align:center;font-variant-numeric:tabular-nums;}

/* PDF/Print: alle Folien untereinander, je eine Seite */
@media print{
  html,body{width:1920px;height:auto;overflow:visible;background:#fff;}
  .deck-viewport{position:static;overflow:visible;}
  .deck-stage{position:static;width:auto;height:auto;transform:none!important;}
  .slide{position:relative;visibility:visible!important;opacity:1!important;break-after:page;page-break-after:always;}
  .slide .reveal{opacity:1!important;transform:none!important;}
  .deck-controls{display:none!important;}
}
@media (prefers-reduced-motion:reduce){*,*::before,*::after{transition-duration:.2s!important;}}
```

```js
class Deck{
  constructor(){
    this.stage=document.getElementById('deckStage');
    this.slides=[...this.stage.querySelectorAll('.slide')];
    this.key='bkm-deck:'+location.pathname;            // Positions-Merker je Deck
    document.getElementById('tot').textContent=this.slides.length;
    const saved=parseInt(localStorage.getItem(this.key),10);
    this.i=Number.isInteger(saved)?Math.min(Math.max(saved,0),this.slides.length-1):0;
    document.body.tabIndex=-1;                          // Body fokussierbar machen
    this.fit(); this.show(this.i);
    addEventListener('resize',()=>this.fit());
    // Tasten zuverlaessig: Capture-Phase auf window UND document (iframe-Fokus-Quirks
    // koennen sonst Pfeiltasten schlucken)
    const onKey=e=>{
      if(['ArrowRight',' ','PageDown'].includes(e.key)){this.go(this.i+1);e.preventDefault();}
      else if(['ArrowLeft','PageUp'].includes(e.key)){this.go(this.i-1);e.preventDefault();}
      else if(e.key==='Home')this.go(0); else if(e.key==='End')this.go(this.slides.length-1);
      else if(/^[1-9]$/.test(e.key))this.go(+e.key-1);
    };
    window.addEventListener('keydown',onKey,true);
    document.addEventListener('keydown',onKey,true);
    // Body-Autofokus bei Load und Klick, damit Tasten ankommen
    const focus=()=>document.body.focus&&document.body.focus();
    addEventListener('load',focus); addEventListener('click',focus); focus();
    let x0=null;
    addEventListener('touchstart',e=>x0=e.touches[0].clientX,{passive:true});
    addEventListener('touchend',e=>{if(x0===null)return;const dx=e.changedTouches[0].clientX-x0;
      if(Math.abs(dx)>50)this.go(this.i+(dx<0?1:-1));x0=null;},{passive:true});
    document.getElementById('next').onclick=()=>this.go(this.i+1);
    document.getElementById('prev').onclick=()=>this.go(this.i-1);
  }
  fit(){const s=Math.min(innerWidth/1920,innerHeight/1080);
    this.stage.style.transform=`translate(${(innerWidth-1920*s)/2}px,${(innerHeight-1080*s)/2}px) scale(${s})`;}
  show(n){this.slides.forEach((sl,k)=>sl.classList.toggle('visible',k===n));
    document.getElementById('cur').textContent=n+1;
    try{localStorage.setItem(this.key,n);}catch(e){}}   // Position merken (Reload bleibt)
  go(n){this.i=Math.max(0,Math.min(this.slides.length-1,n));this.show(this.i);}
}
new Deck();
```

> **Härtung gegenüber der Basis (aus Open Design adaptiert):** Capture-Phase-Keydown auf
> `window` **und** `document`, Body-Autofokus bei Load/Klick, und `localStorage`-Positions-
> Merker (beim Reload landet man auf derselben Folie). Die mitgelieferten `demo.html`
> nutzen noch die schlanke Basis-Variante — neue Decks bekommen diese gehärtete Version.

## Regeln

- **Canvas immer 1920×1080**, Seitenabstand der Inhalte i. d. R. **130–140px**.
- Elemente **absolut** positionieren (px), nicht per Flow umbrechen lassen.
- `tot` (Folienzahl) liest die Engine automatisch aus der Anzahl `.slide`.
- Navigation: Pfeile, Leertaste, PageUp/Down, Home/End, Ziffern 1–9, Touch-Swipe.
- `:root`-Token kommen aus der kanonischen **`tokens.css`** (Single Source of Truth) —
  bei Deploy verlinken (`<link rel="stylesheet" href="../tokens.css">`), in eigenständigen
  Decks den `:root`-Block inlinen. `--stage-bg` und `--ease` müssen gesetzt sein.

## Assets im Echtbetrieb

Im Generierungs-Fall Logos/Keyvisual **per Pfad** referenzieren (nicht einbetten):

| Asset | dunkel (Deep Green) | hell (Sand) |
|-------|---------------------|-------------|
| Logo | `assets/logos/bkm-logo-white-puregreen.png` | `assets/logos/bkm-logo-stonegrey-puregreen.png` |
| Keyvisual | `assets/keyvisual/keyvisual-on-dark.svg` | `assets/keyvisual/keyvisual-on-light.svg` |

> In den mitgelieferten `demo.html` ist das Logo als Data-URI eingebettet, damit die
> Referenz-Dateien eigenständig im Browser laufen. Generierte Decks nutzen Pfade.

## Qualitätskontrolle (nach dem Bauen)

Immer einen Screenshot prüfen auf: **kein Überlauf**, **keine Überlappung**, Text nicht
unter Lesegröße. Sonst Folie teilen oder Typo verkleinern (siehe Anti-Slop in `PATTERN_CATALOG.md`).
