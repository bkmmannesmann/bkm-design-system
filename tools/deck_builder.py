# -*- coding: utf-8 -*-
"""
BKM Deck Builder — deterministischer Daten->Deck-Generator.

Eingabe : JSON-Spec (family + slides[]).  Ausgabe: eigenstaendiges HTML-Deck.
Prinzip : Der Renderer (dieser Code) besitzt das Layout. Das LLM/der Autor liefert nur
          strukturierten Inhalt -> identisches Ergebnis ueber alle Agenten hinweg.
Marke   : nur BKM-Farben, Unbounded + TT Norms (aus glass-ag/demo.html eingebettet),
          texturierte Hintergruende (Auto-Rotation), Hybrid-Casing, Reveal, Zebra,
          Presenter-Modus ("S") + Notizen ("N").  Familien: bkm-glass-ag | bkm-bold-poster.

Aufruf  : python3 tools/deck_builder.py <spec.json> -o <out.html> [--strict]
"""
import re, json, sys, base64, html, argparse, os, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AGDEMO = os.path.join(ROOT, 'skills/bkm-slides/templates/bkm-glass-ag/demo.html')

# ---- Marken-Assets aus der Glas-AG-Familie ziehen (Schriften, Logo, Texturen) ----
FBDEMO = os.path.join(ROOT, 'skills/bkm-slides/templates/bkm-glass-fachbetrieb/demo.html')

def load_assets():
    s = open(AGDEMO, encoding='utf-8').read()
    fonts = re.search(r'<style id="bkm-fonts">.*?</style>', s, flags=re.S).group(0)
    logo  = re.search(r'<img class="brand"[^>]*>', s).group(0)   # weiß (dunkle Familien)
    # grau-grünes Logo aus der Fachbetrieb-Familie (helle Familien)
    logo_dark = logo
    try:
        fb = open(FBDEMO, encoding='utf-8').read()
        src = re.search(r'src="(data:[^"]+)"', re.search(r'<img class="logo"[^>]*>', fb).group(0)).group(1)
        logo_dark = '<img class="brand" src="%s" alt="BKM Mannesmann">' % src
    except Exception:
        pass
    # Hintergründe direkt aus assets/backgrounds/ laden (bg-ag-01..NN.jpg) — 16 Konzept-Varianten
    tex = {}
    files = sorted(glob.glob(os.path.join(ROOT, 'assets/backgrounds/bg-ag-*.jpg')))
    for i, f in enumerate(files, start=1):
        tex[i] = 'data:image/jpeg;base64,' + base64.b64encode(open(f, 'rb').read()).decode()
    if not tex:  # Fallback: alte Texturen aus der demo.html
        for m in re.finditer(r'\.bg\.t([1-4])\{background:#0f2620 url\((data:image/jpeg;base64,[^)]+)\)', s):
            tex[int(m.group(1))] = m.group(2)
    return fonts, logo, logo_dark, tex

FONTS, LOGO, LOGO_DARK, TEX = load_assets()

def esc(x): return html.escape(str(x), quote=True)

# ======================= Kanonische Layout-CSS (Renderer besitzt das Layout) =======================
GEN_CSS = r"""
:root{--deep-green:#1c4b42;--deep2:#0f2620;--lime:#b4e717;--pure-green:#4daf46;
--transition-green:#287d4b;--paper:#f5f0eb;--stone-grey:#494949;
--font-display:'Unbounded',sans-serif;--font-body:'TT Norms Pro',-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
--stage-bg:#0a1c17;--ease:cubic-bezier(0.16,1,0.3,1);}
*{margin:0;box-sizing:border-box;}
html,body{width:100%;height:100%;overflow:hidden;background:var(--stage-bg);font-family:var(--font-body);}
.deck-viewport{position:fixed;inset:0;overflow:hidden;background:var(--stage-bg);}
.deck-stage{position:absolute;left:0;top:0;width:1920px;height:1080px;transform-origin:0 0;}
.slide{position:absolute;inset:0;width:1920px;height:1080px;overflow:hidden;color:#fff;visibility:hidden;opacity:0;pointer-events:none;}
.slide.visible{visibility:visible;opacity:1;pointer-events:auto;z-index:1;}
.bg{position:absolute;inset:0;z-index:0;background-size:cover;background-position:center;}
.reveal{opacity:0;transform:translateY(28px);transition:opacity .7s var(--ease),transform .7s var(--ease);}
.slide.visible .reveal{opacity:1;transform:translateY(0);}
.d1{transition-delay:.08s;}.d2{transition-delay:.20s;}.d3{transition-delay:.32s;}.d4{transition-delay:.44s;}.d5{transition-delay:.56s;}
/* Chrome */
.brand{position:absolute;top:58px;left:140px;height:40px;width:auto;z-index:6;}
.tagtop{position:absolute;top:74px;right:140px;font-weight:700;font-size:16px;letter-spacing:0.12em;text-transform:uppercase;color:rgba(255,255,255,0.75);z-index:6;}
.pg{position:absolute;bottom:60px;right:140px;font-family:var(--font-display);font-weight:900;font-size:18px;color:var(--lime);z-index:6;}
.fam-bold .brand{left:auto;right:130px;top:74px;}
.fam-bold .tagtop{display:none;}
.gen-mark{position:absolute;top:74px;left:130px;display:inline-flex;align-items:center;gap:10px;background:var(--lime);color:var(--deep-green);font-weight:700;font-size:16px;letter-spacing:0.12em;text-transform:uppercase;padding:11px 20px;border-radius:8px;z-index:6;}
.gen-kicker{position:absolute;bottom:62px;left:130px;font-weight:700;font-size:15px;letter-spacing:0.16em;text-transform:uppercase;color:rgba(245,240,235,0.55);z-index:6;}
.fam-glass .gen-mark,.fam-glass .gen-kicker{display:none;}
/* Event-Chrome: Logo links, Event-Label rechts, Tagline unten links (Unbounded Black) */
.ev .brand{left:130px;right:auto;top:64px;}
.gen-event{position:absolute;top:74px;right:130px;font-weight:700;font-size:16px;letter-spacing:0.12em;text-transform:uppercase;color:rgba(245,240,235,0.78);z-index:6;}
.gen-tagline{position:absolute;bottom:56px;left:130px;font-family:var(--font-display);font-weight:900;font-size:21px;letter-spacing:0.005em;color:rgba(245,240,235,0.92);z-index:6;}
.gen-tagline .g{color:var(--lime);}
/* Headlines / Akzent */
.gen-h,.gen-h1{font-family:var(--font-display);font-weight:900;text-transform:uppercase;letter-spacing:-0.04em;line-height:0.94;color:#fff;}
.gen-h.mx,.gen-h1.mx{text-transform:none;}
.g{color:var(--lime);}
.gen-eyebrow{font-weight:700;letter-spacing:0.18em;text-transform:uppercase;font-size:18px;color:var(--lime);}
.gen-lead{font-size:24px;line-height:1.5;color:rgba(255,255,255,0.85);}
.gen-li{display:flex;gap:16px;align-items:flex-start;}
.gen-li .ic{flex:0 0 auto;width:38px;height:38px;border-radius:10px;background:var(--lime);color:var(--deep-green);display:flex;align-items:center;justify-content:center;font-size:15px;margin-top:2px;}
.gen-li p{font-size:19px;color:rgba(255,255,255,0.85);line-height:1.45;}
/* Panel/Card — glass vs flat (Familie) */
.gen-card,.gen-panel{position:relative;border-radius:18px;}
.fam-glass .gen-card,.fam-glass .gen-panel{background:rgba(255,255,255,0.10);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);border:1px solid rgba(255,255,255,0.18);box-shadow:0 8px 32px rgba(0,0,0,0.25);}
.fam-bold .gen-card,.fam-bold .gen-panel{background:rgba(255,255,255,0.045);border:1px solid rgba(255,255,255,0.10);}
/* zentrierter Section-Header */
.gen-head{position:absolute;left:140px;right:140px;top:118px;text-align:center;z-index:2;}
.gen-head .gen-eyebrow{margin-bottom:14px;}
.gen-head .gen-h{font-size:56px;}
.fam-bold .gen-head .gen-h{font-size:62px;}
.gen-sub{font-size:21px;color:rgba(255,255,255,0.72);margin-top:14px;}
/* Cover */
.g-cover .gen-left{position:absolute;left:140px;top:300px;right:520px;z-index:2;}
.g-cover .gen-eyebrow{margin-bottom:24px;}
.g-cover .gen-h1{font-size:92px;}
.fam-bold .g-cover .gen-h1{font-size:120px;}
.g-cover .gen-lead{margin-top:28px;max-width:760px;}
.g-cover .gen-meta{display:flex;gap:46px;margin-top:40px;}
.g-cover .gen-meta .m{display:flex;flex-direction:column;gap:6px;}
.g-cover .gen-meta .k{font-size:12px;letter-spacing:0.12em;text-transform:uppercase;color:rgba(255,255,255,0.55);}
.g-cover .gen-meta .v{font-family:var(--font-display);font-weight:700;font-size:23px;color:#fff;}
.gen-btn{display:inline-flex;align-items:center;gap:12px;background:var(--lime);color:var(--deep-green);font-weight:700;font-size:18px;padding:18px 30px;border-radius:12px;margin-top:38px;}
.gen-btn i{font-size:15px;}
/* Grids */
.gen-grid{position:absolute;left:140px;right:140px;top:330px;display:grid;gap:30px;z-index:2;}
.gen-grid.g2{grid-template-columns:1fr 1fr;}.gen-grid.g3{grid-template-columns:repeat(3,1fr);}.gen-grid.g4{grid-template-columns:repeat(4,1fr);}
.gen-card.c,.gen-grid .gen-card{padding:38px 34px;}
.gen-grid .gen-card .ic{width:60px;height:60px;border-radius:14px;background:var(--lime);color:var(--deep-green);display:flex;align-items:center;justify-content:center;font-size:24px;margin-bottom:22px;}
.gen-grid .gen-card h3{font-family:var(--font-display);font-weight:700;font-size:24px;color:#fff;letter-spacing:-0.01em;}
.gen-grid .gen-card p{font-size:17px;color:rgba(255,255,255,0.74);line-height:1.5;margin-top:12px;}
/* KPI */
.gen-grid.kpis .kpi{text-align:left;}
.gen-grid.kpis .n{font-family:var(--font-display);font-weight:900;font-size:92px;line-height:0.88;color:#fff;letter-spacing:-0.04em;}
.gen-grid.kpis .n .g{color:var(--lime);}
.gen-grid.kpis .c{font-size:19px;color:rgba(255,255,255,0.78);margin-top:16px;line-height:1.4;}
/* Split */
.g-split .gen-split-txt{position:absolute;left:140px;top:270px;width:760px;z-index:2;}
.g-split .gen-eyebrow{margin-bottom:18px;}
.g-split .gen-h{font-size:60px;margin-bottom:24px;}
.g-split .gen-li{margin-top:16px;}
.g-split .gen-figure{position:absolute;right:140px;top:230px;width:780px;height:620px;border-radius:20px;overflow:hidden;box-shadow:0 24px 60px rgba(0,0,0,0.4);z-index:2;}
.g-split .gen-figure img{width:100%;height:100%;object-fit:cover;display:block;}
.g-split .gen-figure figcaption{position:absolute;left:0;right:0;bottom:0;padding:16px 22px;font-size:14px;color:#fff;background:linear-gradient(transparent,rgba(15,38,32,0.85));}
/* Quote */
.g-quote .gen-quote-mark{position:absolute;left:108px;top:120px;font-family:var(--font-display);font-weight:900;font-size:440px;line-height:0.62;color:var(--transition-green);opacity:0.45;z-index:0;}
.g-quote .gen-quote-wrap{position:absolute;left:180px;right:200px;top:330px;z-index:2;}
.g-quote .gen-eyebrow{margin-bottom:28px;}
.g-quote blockquote{font-family:var(--font-display);font-weight:700;font-size:60px;line-height:1.12;color:#fff;letter-spacing:-0.02em;}
.fam-bold .g-quote blockquote{text-transform:uppercase;}
.g-quote .gen-who{margin-top:44px;display:flex;align-items:center;gap:18px;}
.g-quote .gen-who .ln{width:54px;height:3px;background:var(--lime);}
.g-quote .gen-who span{font-weight:700;font-size:20px;letter-spacing:0.04em;color:var(--lime);text-transform:uppercase;}
/* Tabelle + Zebra */
.gen-table{position:absolute;left:140px;right:140px;top:300px;padding:6px 44px;z-index:2;}
.gen-table .tr{display:grid;gap:24px;align-items:center;padding:18px 16px;border-bottom:1px solid rgba(255,255,255,0.1);border-radius:8px;}
.gen-table .tr.head{border-bottom:1px solid rgba(180,231,23,0.45);}
.gen-table .tr.head .c{font-weight:700;letter-spacing:0.1em;text-transform:uppercase;font-size:14px;color:var(--lime);}
.gen-table .tr .c{font-size:18px;color:rgba(255,255,255,0.82);font-variant-numeric:tabular-nums;}
.gen-table .tr .c:first-child{color:#fff;font-weight:600;}
.gen-table .tr .c.hi{color:var(--lime);font-weight:700;}
.gen-table .tr:not(.head):nth-of-type(2n){background:rgba(255,255,255,0.035);}
.gen-table .tr:not(.head):nth-of-type(2n+1){background:rgba(245,240,235,0.05);}
/* Vergleich */
.gen-grid.cmp{top:316px;}
.gen-grid.cmp .gen-card{padding:38px 42px;}
.gen-grid.cmp .gen-card.win{border-color:rgba(180,231,23,0.45);}
.gen-grid.cmp .badge{display:inline-block;border-radius:999px;padding:6px 16px;font-weight:700;font-size:12px;text-transform:uppercase;letter-spacing:0.08em;margin-bottom:16px;background:rgba(255,255,255,0.08);color:rgba(255,255,255,0.7);}
.gen-grid.cmp .win .badge{background:rgba(180,231,23,0.16);border:1px solid rgba(180,231,23,0.4);color:var(--lime);}
.gen-grid.cmp h3{font-family:var(--font-display);font-weight:800;font-size:26px;color:#fff;}
.gen-grid.cmp ul{list-style:none;margin-top:22px;display:flex;flex-direction:column;gap:15px;}
.gen-grid.cmp li{display:flex;gap:13px;font-size:18px;color:rgba(255,255,255,0.82);line-height:1.4;}
.gen-grid.cmp li i{margin-top:3px;flex:0 0 auto;}
.gen-grid.cmp li.yes i{color:var(--lime);}.gen-grid.cmp li.no i{color:rgba(255,255,255,0.4);}
.gen-foot{position:absolute;left:140px;right:140px;bottom:104px;text-align:center;font-size:18px;color:rgba(255,255,255,0.72);z-index:2;}
/* Diagramm */
.gen-chart-wrap{position:absolute;left:140px;right:140px;top:330px;display:grid;grid-template-columns:1.25fr 1fr;gap:60px;align-items:center;z-index:2;}
.gen-chart{height:430px;display:flex;align-items:flex-end;gap:28px;padding:0 8px 40px;position:relative;border-bottom:2px solid rgba(255,255,255,0.18);}
.gen-chart .bar{flex:1;height:100%;display:flex;flex-direction:column;justify-content:flex-end;align-items:center;gap:12px;position:relative;}
.gen-chart .col{width:100%;border-radius:10px 10px 0 0;background:rgba(255,255,255,0.16);}
.gen-chart .bar.hi .col{background:var(--lime);}
.gen-chart .val{font-family:var(--font-display);font-weight:900;font-size:22px;color:#fff;}
.gen-chart .bar.hi .val{color:var(--lime);}
.gen-chart .lbl{position:absolute;bottom:-32px;left:0;right:0;text-align:center;font-size:14px;color:rgba(255,255,255,0.6);}
.gen-note h3{font-family:var(--font-display);font-weight:700;font-size:30px;color:#fff;line-height:1.2;}
.gen-note h3 .g{color:var(--lime);}
.gen-note p{font-size:18px;color:rgba(255,255,255,0.72);margin-top:16px;line-height:1.5;}
.gen-note .cap{font-size:13px;color:rgba(255,255,255,0.5);margin-top:24px;text-transform:uppercase;letter-spacing:0.08em;}
/* Liniendiagramm (Trends-Kurve) */
.gen-line{position:relative;height:392px;border-bottom:2px solid rgba(255,255,255,0.18);}
.gen-line svg{position:absolute;inset:0;width:100%;height:100%;overflow:visible;}
.gen-line .dot{position:absolute;width:13px;height:13px;border-radius:50%;background:var(--lime);border:2px solid var(--deep2);transform:translate(-50%,-50%);z-index:2;}
.gen-line .dot.hi{width:18px;height:18px;box-shadow:0 0 0 6px rgba(180,231,23,0.16);}
.gen-line .dot .cv{position:absolute;bottom:18px;left:50%;transform:translateX(-50%);font-family:var(--font-display);font-weight:900;font-size:21px;color:var(--lime);white-space:nowrap;}
.gen-chart-wrap .lbls{position:relative;height:22px;margin-top:10px;}
.gen-chart-wrap .lbls span{position:absolute;transform:translateX(-50%);font-size:13px;color:rgba(255,255,255,0.6);white-space:nowrap;}
.fam-fachbetrieb .gen-line{border-bottom-color:rgba(28,75,66,0.18);}
.fam-fachbetrieb .gen-line polyline{stroke:var(--pure-green);}
.fam-fachbetrieb .gen-line .dot{background:var(--pure-green);border-color:#f1ede6;}
.fam-fachbetrieb .gen-line .dot .cv{color:var(--transition-green);}
.fam-fachbetrieb .gen-chart-wrap .lbls span{color:var(--stone-grey);}
/* Kapitel-Trenner */
.gen-chapter{position:absolute;left:140px;top:50%;transform:translateY(-50%);z-index:2;}
.gen-chapter .big{font-family:var(--font-display);font-weight:900;font-size:300px;line-height:0.78;color:rgba(255,255,255,0.12);letter-spacing:-0.04em;}
.gen-chapter .t{margin-top:-26px;}
.gen-chapter .t .gen-eyebrow{margin-bottom:18px;}
.gen-chapter .t .gen-h{font-size:90px;}
.fam-bold .gen-chapter .t .gen-h{font-size:118px;}
/* Unterthema / Statement / Closing (zentriert/links groß) */
.gen-subhead{position:absolute;left:140px;right:140px;top:50%;transform:translateY(-50%);text-align:center;z-index:2;}
.gen-subhead .gen-eyebrow{margin-bottom:18px;}.gen-subhead .gen-h{font-size:76px;}
.gen-subhead .gen-sub{margin:24px auto 0;max-width:1040px;}
.gen-statement,.gen-closing{position:absolute;left:140px;right:140px;top:50%;transform:translateY(-50%);z-index:2;}
.gen-statement .gen-eyebrow,.gen-closing .gen-eyebrow{margin-bottom:24px;}
.gen-statement .gen-h1{font-size:104px;max-width:1500px;}
.fam-bold .gen-statement .gen-h1{font-size:128px;}
.gen-statement .gen-lead{margin-top:34px;max-width:1100px;font-size:26px;}
.gen-closing .gen-h1{font-size:100px;max-width:1500px;}
.fam-bold .gen-closing .gen-h1{font-size:150px;}
.gen-chips{display:flex;gap:14px;margin-top:38px;flex-wrap:wrap;}
.gen-chips .v{border:1.5px solid rgba(180,231,23,0.5);color:var(--lime);border-radius:999px;padding:12px 26px;font-family:var(--font-display);font-weight:700;font-size:20px;}
.gen-punch{font-size:24px;color:rgba(255,255,255,0.9);margin-top:36px;max-width:1100px;line-height:1.5;}
.gen-punch .g{color:var(--lime);}
/* Prozess */
.gen-process{position:absolute;left:140px;right:140px;top:300px;padding:8px 46px;z-index:2;}
.gen-process .row{display:grid;grid-template-columns:92px 1fr;align-items:baseline;gap:30px;padding:22px 12px;border-bottom:1px solid rgba(255,255,255,0.1);border-radius:8px;}
.gen-process .row:last-child{border-bottom:0;}
.gen-process .row:nth-child(odd){background:rgba(245,240,235,0.05);}.gen-process .row:nth-child(even){background:rgba(255,255,255,0.035);}
.gen-process .no{font-family:var(--font-display);font-weight:900;font-size:38px;color:var(--lime);line-height:1;}
.gen-process h3{font-family:var(--font-display);font-weight:700;font-size:24px;color:#fff;}
.gen-process p{font-size:18px;color:rgba(255,255,255,0.72);margin-top:6px;line-height:1.45;}
/* Agenda */
.gen-agenda{position:absolute;left:140px;right:140px;top:296px;padding:10px 46px;z-index:2;}
.gen-agenda .row{display:grid;grid-template-columns:128px 1fr 300px 48px;align-items:center;gap:24px;padding:21px 14px;border-bottom:1px solid rgba(255,255,255,0.12);border-radius:8px;}
.gen-agenda .row:last-child{border-bottom:0;}
.gen-agenda .row:nth-child(odd){background:rgba(245,240,235,0.05);}.gen-agenda .row:nth-child(even){background:rgba(255,255,255,0.035);}
.gen-agenda .time{font-family:var(--font-display);font-weight:900;font-size:24px;color:var(--lime);}
.gen-agenda .topic{font-size:23px;font-weight:600;color:#fff;}
.gen-agenda .topic small{display:block;font-size:15px;font-weight:400;color:rgba(255,255,255,0.6);margin-top:5px;}
.gen-agenda .spk{font-size:17px;color:rgba(255,255,255,0.75);}
.gen-agenda .no{font-family:var(--font-display);font-weight:900;font-size:20px;color:rgba(255,255,255,0.3);text-align:right;}
/* Timeline */
.gen-tl-wrap{position:absolute;left:200px;right:200px;top:50%;transform:translateY(-50%);z-index:2;}
.gen-tl-wrap .line{position:relative;height:4px;background:rgba(255,255,255,0.16);border-radius:2px;}
.gen-tl-wrap .pt{position:absolute;top:50%;transform:translate(-50%,-50%);width:18px;height:18px;border-radius:50%;background:var(--lime);box-shadow:0 0 0 7px rgba(180,231,23,0.14);}
.gen-tl-wrap .item{position:absolute;width:260px;transform:translateX(-50%);text-align:center;}
.gen-tl-wrap .item.up{bottom:46px;}.gen-tl-wrap .item.down{top:46px;}
.gen-tl-wrap .yr{font-family:var(--font-display);font-weight:900;font-size:26px;color:var(--lime);}
.gen-tl-wrap .item h3{font-family:var(--font-display);font-weight:700;font-size:19px;color:#fff;margin-top:8px;}
.gen-tl-wrap .item p{font-size:14px;color:rgba(255,255,255,0.65);margin-top:7px;line-height:1.4;}
/* ===== Batch 1: neue Archetypen (Referenz-inspiriert, BKM-nativ) ===== */
/* funnel — TAM/SAM/SOM */
.gen-funnel{position:absolute;left:140px;right:140px;top:336px;display:flex;flex-direction:column;align-items:center;gap:20px;z-index:2;}
.gen-funnel .tier{background:rgba(255,255,255,0.08);border:1px solid rgba(255,255,255,0.14);border-radius:14px;padding:26px 40px;display:flex;justify-content:space-between;align-items:center;}
.gen-funnel .tier .v{font-family:var(--font-display);font-weight:900;font-size:44px;color:var(--lime);line-height:1;}
.gen-funnel .tier .l{font-size:18px;color:rgba(255,255,255,0.8);text-align:right;max-width:60%;}
/* donut */
.gen-donut-wrap{position:absolute;left:140px;right:140px;top:340px;display:grid;grid-template-columns:1fr 1fr;gap:80px;align-items:center;z-index:2;}
.gen-donut{width:420px;height:420px;border-radius:50%;position:relative;margin:0 auto;}
.gen-donut::after{content:'';position:absolute;inset:27%;border-radius:50%;background:#0f2620;}
.gen-donut .center{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;z-index:2;}
.gen-donut .center .v{font-family:var(--font-display);font-weight:900;font-size:58px;color:#fff;line-height:1;}
.gen-donut .center .l{font-size:13px;color:rgba(255,255,255,0.6);text-transform:uppercase;letter-spacing:0.12em;margin-top:6px;}
.gen-legend{display:flex;flex-direction:column;gap:18px;}
.gen-legend .row{display:flex;align-items:center;gap:14px;font-size:20px;color:rgba(255,255,255,0.85);}
.gen-legend .dot{width:16px;height:16px;border-radius:5px;flex:0 0 auto;}
.gen-legend .pct{margin-left:auto;font-family:var(--font-display);font-weight:900;color:#fff;}
/* bigstat — Mega-Kennzahl */
.gen-bigstat{position:absolute;left:140px;right:140px;top:300px;z-index:2;}
.gen-bigstat .gen-eyebrow{margin-bottom:22px;}
.gen-bigstat .huge{font-family:var(--font-display);font-weight:900;font-size:200px;line-height:0.84;color:#fff;letter-spacing:-0.05em;}
.gen-bigstat .huge .g{color:var(--lime);}
.gen-bigstat .sub{font-size:24px;color:rgba(255,255,255,0.8);margin-top:14px;}
.gen-bigstat .row{display:flex;gap:64px;margin-top:54px;}
.gen-bigstat .s .n{font-family:var(--font-display);font-weight:900;font-size:46px;color:var(--lime);}
.gen-bigstat .s .l{font-size:17px;color:rgba(255,255,255,0.7);margin-top:6px;}
/* bubbles — überlappende Metriken */
.gen-bubbles{position:absolute;left:140px;right:140px;top:320px;height:580px;z-index:2;}
.gen-bubble{position:absolute;border-radius:50%;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:14px;}
.gen-bubble .v{font-family:var(--font-display);font-weight:900;line-height:1;}
.gen-bubble .l{font-size:14px;margin-top:8px;opacity:0.85;}
/* team — Porträt-Raster */
.gen-team{position:absolute;left:140px;right:140px;top:340px;display:grid;grid-template-columns:repeat(3,1fr);gap:34px 40px;z-index:2;}
.gen-team .m{display:flex;flex-direction:column;align-items:center;text-align:center;}
.gen-team .av{width:140px;height:140px;border-radius:50%;overflow:hidden;display:flex;align-items:center;justify-content:center;font-family:var(--font-display);font-weight:900;font-size:44px;color:var(--lime);background:rgba(255,255,255,0.1);border:2px solid rgba(180,231,23,0.3);}
.gen-team .av img{width:100%;height:100%;object-fit:cover;}
.gen-team .nm{font-family:var(--font-display);font-weight:700;font-size:21px;color:#fff;margin-top:16px;}
.gen-team .ro{font-size:16px;color:rgba(255,255,255,0.65);margin-top:4px;}
/* twocol — Zwei-Spalten-Text */
.gen-twocol{position:absolute;left:140px;right:140px;top:330px;display:grid;grid-template-columns:1fr 1fr;gap:64px;z-index:2;}
.gen-twocol .col h3{font-family:var(--font-display);font-weight:700;font-size:25px;color:var(--lime);margin-bottom:16px;}
.gen-twocol .col p{font-size:20px;color:rgba(255,255,255,0.82);line-height:1.55;}
.gen-twocol .col ul{list-style:none;display:flex;flex-direction:column;gap:14px;margin-top:10px;}
.gen-twocol .col li{display:flex;gap:12px;font-size:18px;color:rgba(255,255,255,0.82);line-height:1.45;}
.gen-twocol .col li i{color:var(--lime);margin-top:4px;flex:0 0 auto;}
/* ===== Batch 2: weitere Archetypen ===== */
/* pricing */
.gen-pricing{position:absolute;left:140px;right:140px;top:332px;display:grid;gap:28px;z-index:2;}
.gen-pricing.g2{grid-template-columns:repeat(2,1fr);}.gen-pricing.g3{grid-template-columns:repeat(3,1fr);}.gen-pricing.g4{grid-template-columns:repeat(4,1fr);}
.gen-pricing .plan{padding:38px 34px;border-radius:18px;background:rgba(255,255,255,0.07);border:1px solid rgba(255,255,255,0.12);display:flex;flex-direction:column;}
.fam-bold .gen-pricing .plan{background:rgba(255,255,255,0.045);}
.gen-pricing .plan.hi{border-color:rgba(180,231,23,0.5);background:rgba(180,231,23,0.07);}
.gen-pricing .badge{align-self:flex-start;background:var(--lime);color:var(--deep-green);font-weight:700;font-size:12px;text-transform:uppercase;letter-spacing:0.06em;padding:6px 14px;border-radius:999px;margin-bottom:14px;}
.gen-pricing .nm{font-family:var(--font-display);font-weight:700;font-size:23px;color:#fff;}
.gen-pricing .price{font-family:var(--font-display);font-weight:900;font-size:50px;color:var(--lime);margin-top:12px;line-height:1;}
.gen-pricing .per{font-size:15px;color:rgba(255,255,255,0.6);margin-top:6px;}
.gen-pricing ul{list-style:none;margin-top:22px;display:flex;flex-direction:column;gap:12px;}
.gen-pricing li{display:flex;gap:11px;font-size:17px;color:rgba(255,255,255,0.82);}
.gen-pricing li i{color:var(--lime);margin-top:4px;font-size:14px;flex:0 0 auto;}
/* flow */
.gen-flow{position:absolute;left:140px;right:140px;top:360px;display:flex;align-items:stretch;z-index:2;}
.gen-flow .step{flex:1;padding:30px 26px;background:rgba(255,255,255,0.07);border:1px solid rgba(255,255,255,0.12);border-radius:16px;}
.fam-bold .gen-flow .step{background:rgba(255,255,255,0.045);}
.gen-flow .step .ic{width:50px;height:50px;border-radius:12px;background:var(--lime);color:var(--deep-green);display:flex;align-items:center;justify-content:center;font-size:20px;margin-bottom:16px;}
.gen-flow .step h3{font-family:var(--font-display);font-weight:700;font-size:20px;color:#fff;}
.gen-flow .step p{font-size:16px;color:rgba(255,255,255,0.72);line-height:1.45;margin-top:10px;}
.gen-flow .arr{flex:0 0 auto;width:56px;display:flex;align-items:center;justify-content:center;color:var(--lime);font-size:26px;}
/* gauge */
.gen-gauge-wrap{position:absolute;left:140px;right:140px;top:340px;display:grid;grid-template-columns:1fr 1fr;gap:80px;align-items:center;z-index:2;}
.gen-gauge{width:380px;height:380px;border-radius:50%;position:relative;margin:0 auto;}
.gen-gauge::after{content:'';position:absolute;inset:15%;border-radius:50%;background:#0f2620;}
.gen-gauge .center{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;z-index:2;}
.gen-gauge .center .v{font-family:var(--font-display);font-weight:900;font-size:64px;color:#fff;line-height:1;}
.gen-gauge .center .l{font-size:14px;color:rgba(255,255,255,0.6);text-transform:uppercase;letter-spacing:0.1em;margin-top:6px;}
.gen-gauge-note h3{font-family:var(--font-display);font-weight:700;font-size:32px;color:#fff;line-height:1.2;}
.gen-gauge-note h3 .g{color:var(--lime);}
.gen-gauge-note p{font-size:19px;color:rgba(255,255,255,0.75);margin-top:16px;line-height:1.5;}
/* pictograph */
.gen-picto{position:absolute;left:140px;right:140px;top:340px;display:grid;gap:50px;z-index:2;}
.gen-picto.g1{grid-template-columns:1fr;}.gen-picto.g2{grid-template-columns:repeat(2,1fr);}.gen-picto.g3{grid-template-columns:repeat(3,1fr);}
.gen-picto .grp .v{font-family:var(--font-display);font-weight:900;font-size:60px;color:var(--lime);line-height:1;}
.gen-picto .grp .icons{display:flex;flex-wrap:wrap;gap:9px;margin:18px 0;max-width:340px;}
.gen-picto .grp .icons i{font-size:26px;color:rgba(255,255,255,0.18);}
.gen-picto .grp .icons i.on{color:var(--lime);}
.gen-picto .grp .l{font-size:18px;color:rgba(255,255,255,0.78);}
/* imagecover */
.g-imagecover .photo{position:absolute;inset:0;z-index:1;}
.g-imagecover .photo img{width:100%;height:100%;object-fit:cover;display:block;}
.g-imagecover .ov{position:absolute;inset:0;z-index:1;background:linear-gradient(90deg,rgba(15,38,32,0.88),rgba(15,38,32,0.35) 70%,rgba(15,38,32,0.2));}
.g-imagecover .txt{position:absolute;left:140px;right:560px;bottom:150px;z-index:3;}
.g-imagecover .gen-eyebrow{margin-bottom:20px;}
.g-imagecover .gen-h1{font-size:104px;}
.g-imagecover .sub{font-size:24px;color:rgba(255,255,255,0.85);margin-top:24px;}
/* bento */
.gen-bento{position:absolute;left:140px;right:140px;top:330px;display:grid;grid-template-columns:repeat(4,1fr);grid-auto-rows:228px;gap:24px;z-index:2;}
.gen-bento .cell{background:rgba(255,255,255,0.07);border:1px solid rgba(255,255,255,0.12);border-radius:18px;padding:28px 30px;display:flex;flex-direction:column;justify-content:flex-end;}
.fam-bold .gen-bento .cell{background:rgba(255,255,255,0.045);}
.gen-bento .cell.wide{grid-column:span 2;}.gen-bento .cell.tall{grid-row:span 2;}
.gen-bento .cell.accent{background:rgba(180,231,23,0.12);border-color:rgba(180,231,23,0.4);}
.gen-bento .cell .ic{width:54px;height:54px;border-radius:13px;background:var(--lime);color:var(--deep-green);display:flex;align-items:center;justify-content:center;font-size:22px;margin-bottom:auto;}
.gen-bento .cell h3{font-family:var(--font-display);font-weight:700;font-size:22px;color:#fff;margin-top:14px;}
.gen-bento .cell p{font-size:16px;color:rgba(255,255,255,0.72);line-height:1.45;margin-top:8px;}
/* ===== Batch 3: Rest-Archetypen ===== */
/* statcluster */
.gen-cluster{position:absolute;left:140px;right:140px;top:316px;height:600px;z-index:2;}
.gen-cluster .node{position:absolute;display:flex;flex-direction:column;align-items:center;text-align:center;}
.gen-cluster .node .circle{border-radius:50%;overflow:hidden;background:rgba(180,231,23,0.14);border:2px solid rgba(180,231,23,0.35);}
.gen-cluster .node .circle img{width:100%;height:100%;object-fit:cover;}
.gen-cluster .node .v{font-family:var(--font-display);font-weight:900;font-size:40px;color:var(--lime);margin-top:14px;line-height:1;}
.gen-cluster .node .l{font-size:15px;color:rgba(255,255,255,0.75);margin-top:8px;max-width:230px;}
/* numlist */
.gen-numlist{position:absolute;left:140px;right:140px;top:316px;z-index:2;}
.gen-numlist .row{display:grid;grid-template-columns:96px 1fr auto;align-items:center;gap:30px;padding:24px 12px;border-bottom:1px solid rgba(255,255,255,0.12);}
.gen-numlist .row:last-child{border-bottom:0;}
.gen-numlist .no{font-family:var(--font-display);font-weight:900;font-size:42px;color:var(--lime);}
.gen-numlist .tx{font-size:21px;color:rgba(255,255,255,0.88);line-height:1.4;}
.gen-numlist .tg{font-size:14px;font-weight:700;text-transform:uppercase;letter-spacing:0.08em;color:var(--lime);border:1px solid rgba(180,231,23,0.4);border-radius:999px;padding:8px 16px;white-space:nowrap;}
/* gallery */
.gen-gallery{position:absolute;left:140px;right:140px;top:330px;display:grid;gap:22px;z-index:2;}
.gen-gallery.g2{grid-template-columns:repeat(2,1fr);}.gen-gallery.g3{grid-template-columns:repeat(3,1fr);}.gen-gallery.g4{grid-template-columns:repeat(4,1fr);}
.gen-gallery figure{position:relative;border-radius:16px;overflow:hidden;height:500px;}
.gen-gallery.g3 figure,.gen-gallery.g4 figure{height:460px;}
.gen-gallery img{width:100%;height:100%;object-fit:cover;display:block;}
.gen-gallery figcaption{position:absolute;left:0;right:0;bottom:0;padding:14px 18px;font-size:14px;color:#fff;background:linear-gradient(transparent,rgba(15,38,32,0.85));}
/* contact */
.gen-contact{position:absolute;left:140px;top:280px;width:1000px;z-index:2;}
.gen-contact .gen-eyebrow{margin-bottom:16px;}
.gen-contact .gen-h{font-size:60px;}
.gen-contact .blocks{display:grid;grid-template-columns:1fr 1fr;gap:32px 50px;margin-top:42px;}
.gen-contact .b .k{font-size:13px;letter-spacing:0.12em;text-transform:uppercase;color:var(--lime);font-weight:700;}
.gen-contact .b .v{font-size:23px;color:#fff;margin-top:8px;font-weight:600;}
.gen-contact-photo{position:absolute;right:140px;top:230px;width:540px;height:620px;border-radius:20px;overflow:hidden;z-index:2;}
.gen-contact-photo img{width:100%;height:100%;object-fit:cover;display:block;}
/* imagesplit (50/50) */
.gen-imgsplit{position:absolute;inset:0;}
.gen-imgsplit .photo{position:absolute;top:0;bottom:0;width:50%;z-index:1;}
.gen-imgsplit.right .photo{right:0;}.gen-imgsplit.left .photo{left:0;}
.gen-imgsplit .photo img{width:100%;height:100%;object-fit:cover;display:block;}
.gen-imgsplit .txt{position:absolute;top:50%;transform:translateY(-50%);width:46%;z-index:2;}
.gen-imgsplit.right .txt{left:140px;}.gen-imgsplit.left .txt{right:140px;}
.gen-imgsplit .gen-eyebrow{margin-bottom:18px;}
.gen-imgsplit .gen-h{font-size:58px;}
.gen-imgsplit p{font-size:21px;color:rgba(255,255,255,0.82);line-height:1.55;margin-top:24px;}
.gen-imgsplit .gen-li{margin-top:16px;}
/* Controls + Notes */
.deck-controls{position:fixed;left:50%;bottom:18px;transform:translateX(-50%);z-index:1000;display:flex;align-items:center;gap:6px;background:rgba(8,22,18,0.9);border:1px solid rgba(255,255,255,0.16);border-radius:999px;padding:8px 12px;color:#fff;font-size:13px;font-weight:600;}
.deck-controls button{all:unset;cursor:pointer;width:30px;height:30px;border-radius:50%;display:flex;align-items:center;justify-content:center;}
.deck-controls .count{min-width:60px;text-align:center;font-variant-numeric:tabular-nums;}
.notes{display:none;}
.notes-panel{position:fixed;left:0;right:0;bottom:0;z-index:2000;display:none;background:rgba(8,22,18,0.97);border-top:2px solid var(--lime);color:#fff;padding:20px 44px 26px;max-height:42vh;overflow:auto;}
.notes-panel.on{display:block;}
.notes-panel .nh{font-size:12px;letter-spacing:0.16em;text-transform:uppercase;color:var(--lime);font-weight:700;margin-bottom:10px;}
.notes-panel .nb{font-size:17px;line-height:1.6;white-space:pre-wrap;}
/* ===== Fachbetrieb-Theme (hell, Sand, kein Lime; additiv) ===== */
.fam-fachbetrieb{color:var(--stone-grey);}.fam-fachbetrieb .deck-viewport{background:#dad6cd;}
.fam-fachbetrieb .gen-h,.fam-fachbetrieb .gen-h1{color:var(--transition-green);}
.fam-fachbetrieb h3{color:var(--deep-green);}
.fam-fachbetrieb .gen-eyebrow,.fam-fachbetrieb .g{color:var(--pure-green);}
.fam-fachbetrieb .gen-lead,.fam-fachbetrieb p,.fam-fachbetrieb .gen-li p,.fam-fachbetrieb .gen-sub,.fam-fachbetrieb .gen-bigstat .sub,.fam-fachbetrieb .gen-note p,.fam-fachbetrieb .gen-foot,.fam-fachbetrieb .gen-punch{color:var(--stone-grey);}
.fam-fachbetrieb .tagtop{color:var(--transition-green);}.fam-fachbetrieb .pg{color:var(--pure-green);}
.fam-fachbetrieb .gen-event{color:var(--transition-green);}.fam-fachbetrieb .gen-tagline{color:var(--deep-green);}.fam-fachbetrieb .gen-tagline .g{color:var(--pure-green);}
.fam-fachbetrieb .gen-card,.fam-fachbetrieb .gen-panel,.fam-fachbetrieb .gen-pricing .plan,.fam-fachbetrieb .gen-flow .step,.fam-fachbetrieb .gen-bento .cell,.fam-fachbetrieb .gen-funnel .tier{background:rgba(255,255,255,0.55);border-color:rgba(28,75,66,0.12);backdrop-filter:none;-webkit-backdrop-filter:none;box-shadow:0 12px 40px rgba(28,75,66,0.08);}
.fam-fachbetrieb .ic,.fam-fachbetrieb .gen-li .ic{background:var(--pure-green);color:#fff;}
.fam-fachbetrieb .gen-btn,.fam-fachbetrieb .badge,.fam-fachbetrieb .gen-pricing .badge{background:var(--pure-green);color:#fff;}
.fam-fachbetrieb .gen-chips .v{border-color:rgba(77,175,70,0.5);color:var(--transition-green);}
.fam-fachbetrieb .gen-grid.kpis .n,.fam-fachbetrieb .gen-bigstat .huge,.fam-fachbetrieb .gen-donut .center .v,.fam-fachbetrieb .gen-gauge .center .v{color:var(--transition-green);}
.fam-fachbetrieb .gen-numlist .no,.fam-fachbetrieb .gen-process .no,.fam-fachbetrieb .gen-agenda .time,.fam-fachbetrieb .gen-funnel .tier .v,.fam-fachbetrieb .gen-cluster .node .v,.fam-fachbetrieb .gen-tl-wrap .yr,.fam-fachbetrieb .gen-picto .grp .v{color:var(--pure-green);}
.fam-fachbetrieb .gen-bigstat .huge .g{color:var(--pure-green);}
.fam-fachbetrieb .gen-table .tr.head .c,.fam-fachbetrieb .gen-table .tr .c.hi{color:var(--pure-green);}
.fam-fachbetrieb .gen-table .tr .c{color:var(--stone-grey);}.fam-fachbetrieb .gen-table .tr .c:first-child{color:var(--deep-green);}
.fam-fachbetrieb .gen-table .tr{border-bottom-color:rgba(28,75,66,0.1);}.fam-fachbetrieb .gen-table .tr.head{border-bottom-color:rgba(77,175,70,0.45);}
.fam-fachbetrieb .gen-table .tr:not(.head):nth-of-type(2n){background:rgba(255,255,255,0.55);}.fam-fachbetrieb .gen-table .tr:not(.head):nth-of-type(2n+1){background:rgba(232,229,227,0.6);}
.fam-fachbetrieb .gen-agenda .row,.fam-fachbetrieb .gen-process .row,.fam-fachbetrieb .gen-numlist .row{border-bottom-color:rgba(28,75,66,0.1);}
.fam-fachbetrieb .gen-agenda .row:nth-child(odd),.fam-fachbetrieb .gen-process .row:nth-child(odd){background:rgba(232,229,227,0.55);}.fam-fachbetrieb .gen-agenda .row:nth-child(even),.fam-fachbetrieb .gen-process .row:nth-child(even){background:rgba(255,255,255,0.55);}
.fam-fachbetrieb .gen-agenda .topic,.fam-fachbetrieb .gen-process h3,.fam-fachbetrieb .gen-grid .gen-card h3,.fam-fachbetrieb .gen-bento .cell h3,.fam-fachbetrieb .gen-flow .step h3,.fam-fachbetrieb .gen-pricing .nm,.fam-fachbetrieb .gen-tl-wrap .item h3,.fam-fachbetrieb .gen-team .nm,.fam-fachbetrieb .gen-grid.cmp h3,.fam-fachbetrieb .gen-contact .b .v,.fam-fachbetrieb .gen-numlist .tx{color:var(--deep-green);}
.fam-fachbetrieb .gen-agenda .topic small,.fam-fachbetrieb .gen-agenda .spk,.fam-fachbetrieb .gen-process p,.fam-fachbetrieb .gen-grid .gen-card p,.fam-fachbetrieb .gen-bento .cell p,.fam-fachbetrieb .gen-flow .step p,.fam-fachbetrieb .gen-pricing li,.fam-fachbetrieb .gen-pricing .per,.fam-fachbetrieb .gen-grid.cmp li,.fam-fachbetrieb .gen-tl-wrap .item p,.fam-fachbetrieb .gen-team .ro,.fam-fachbetrieb .gen-cluster .node .l,.fam-fachbetrieb .gen-picto .grp .l{color:var(--stone-grey);}
.fam-fachbetrieb .gen-agenda .no{color:rgba(28,75,66,0.3);}
.fam-fachbetrieb .gen-chart{border-bottom-color:rgba(28,75,66,0.18);}.fam-fachbetrieb .gen-chart .col{background:rgba(28,75,66,0.14);}.fam-fachbetrieb .gen-chart .bar.hi .col{background:var(--pure-green);}.fam-fachbetrieb .gen-chart .val{color:var(--transition-green);}.fam-fachbetrieb .gen-chart .bar.hi .val{color:var(--pure-green);}.fam-fachbetrieb .gen-chart .lbl{color:var(--stone-grey);}
.fam-fachbetrieb .gen-note h3,.fam-fachbetrieb .gen-gauge-note h3{color:var(--transition-green);}.fam-fachbetrieb .gen-note h3 .g,.fam-fachbetrieb .gen-gauge-note h3 .g{color:var(--pure-green);}.fam-fachbetrieb .gen-note .cap{color:var(--transition-green);}.fam-fachbetrieb .gen-gauge-note p{color:var(--stone-grey);}
.fam-fachbetrieb .gen-donut::after,.fam-fachbetrieb .gen-gauge::after{background:#f1ede6;}.fam-fachbetrieb .gen-donut .center .l,.fam-fachbetrieb .gen-gauge .center .l{color:var(--stone-grey);}.fam-fachbetrieb .gen-legend .row,.fam-fachbetrieb .gen-legend .pct{color:var(--deep-green);}
.fam-fachbetrieb .gen-grid.cmp .gen-card.win{border-color:rgba(77,175,70,0.45);}.fam-fachbetrieb .gen-grid.cmp .badge{background:rgba(28,75,66,0.08);color:var(--stone-grey);}.fam-fachbetrieb .gen-grid.cmp .win .badge{background:rgba(77,175,70,0.16);color:var(--transition-green);}.fam-fachbetrieb .gen-grid.cmp li.yes i{color:var(--pure-green);}.fam-fachbetrieb .gen-grid.cmp li.no i{color:rgba(73,73,73,0.4);}
.fam-fachbetrieb .g-quote .gen-quote-mark{color:var(--pure-green);opacity:0.2;}.fam-fachbetrieb .g-quote blockquote{color:var(--transition-green);}.fam-fachbetrieb .g-quote blockquote .g{color:var(--pure-green);}.fam-fachbetrieb .g-quote .gen-who .ln{background:var(--pure-green);}.fam-fachbetrieb .g-quote .gen-who span{color:var(--pure-green);}
.fam-fachbetrieb .gen-team .av{background:rgba(28,75,66,0.08);color:var(--pure-green);border-color:rgba(77,175,70,0.3);}
.fam-fachbetrieb .gen-cluster .node .circle{background:rgba(77,175,70,0.14);border-color:rgba(77,175,70,0.35);}
.fam-fachbetrieb .gen-numlist .tg{color:var(--pure-green);border-color:rgba(77,175,70,0.4);}
.fam-fachbetrieb .gen-tl-wrap .line{background:rgba(28,75,66,0.18);}.fam-fachbetrieb .gen-tl-wrap .pt{background:var(--pure-green);box-shadow:0 0 0 7px rgba(77,175,70,0.14);}
.fam-fachbetrieb .gen-pricing .plan.hi{border-color:rgba(77,175,70,0.5);background:rgba(77,175,70,0.07);}.fam-fachbetrieb .gen-pricing .price{color:var(--pure-green);}.fam-fachbetrieb .gen-pricing li i{color:var(--pure-green);}
.fam-fachbetrieb .gen-bento .cell.accent{background:rgba(77,175,70,0.12);border-color:rgba(77,175,70,0.4);}
.fam-fachbetrieb .gen-flow .arr{color:var(--pure-green);}.fam-fachbetrieb .gen-picto .grp .icons i{color:rgba(28,75,66,0.18);}.fam-fachbetrieb .gen-picto .grp .icons i.on{color:var(--pure-green);}
.fam-fachbetrieb .g-cover .gen-meta .k{color:rgba(73,73,73,0.6);}.fam-fachbetrieb .g-cover .gen-meta .v{color:var(--deep-green);}
.fam-fachbetrieb .gen-funnel .tier .l{color:var(--stone-grey);}

@media print{html,body{width:1920px;height:auto;overflow:visible;}.deck-viewport{position:static;}.deck-stage{position:static;width:auto;height:auto;transform:none!important;}.slide{position:relative;visibility:visible!important;opacity:1!important;break-after:page;}.slide .reveal{opacity:1!important;transform:none!important;}.deck-controls,.notes-panel{display:none!important;}}
"""

SHELL = r"""<!DOCTYPE html><html lang="de"><head><meta charset="UTF-8">
<title>@@TITLE@@</title>
<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" rel="stylesheet">
@@FONTS@@
<style>@@GENCSS@@
@@BGCSS@@</style></head>
<body class="@@FAMBODY@@">
<div class="deck-viewport"><main class="deck-stage" id="deckStage">
@@SECTIONS@@
</main></div>
<div class="deck-controls"><button id="prev" aria-label="Zurück">&#8249;</button><span class="count"><span id="cur">1</span> / @@TOTAL@@</span><button id="next" aria-label="Weiter">&#8250;</button></div>
<script>
(function(){var st=document.getElementById('deckStage'),sl=[].slice.call(st.querySelectorAll('.slide')),i=0;
function fit(){var s=Math.min(innerWidth/1920,innerHeight/1080);st.style.transform='translate('+(innerWidth-1920*s)/2+'px,'+(innerHeight-1080*s)/2+'px) scale('+s+')';}
function show(n){i=Math.max(0,Math.min(sl.length-1,n));sl.forEach(function(x,k){x.classList.toggle('visible',k===i);});var c=document.getElementById('cur');if(c)c.textContent=i+1;}
addEventListener('resize',fit);fit();show(0);
document.getElementById('next').onclick=function(){show(i+1);};
document.getElementById('prev').onclick=function(){show(i-1);};
addEventListener('keydown',function(e){if(['ArrowRight',' ','PageDown'].indexOf(e.key)>=0){show(i+1);e.preventDefault();}else if(['ArrowLeft','PageUp'].indexOf(e.key)>=0){show(i-1);e.preventDefault();}});
/* Notizen ("N") */
var panel=document.createElement('div');panel.className='notes-panel';panel.innerHTML='<div class="nh">Speaker Notes — Taste „N“</div><div class="nb"></div>';document.body.appendChild(panel);var nb=panel.querySelector('.nb');
function curN(){var s=sl[i];var n=s&&s.querySelector('.notes');return n?n.textContent.trim():'—';}
function updN(){nb.textContent=curN();}
addEventListener('keydown',function(e){if(e.key==='n'||e.key==='N'){panel.classList.toggle('on');updN();}});
})();
</script>
@@PRESENTER@@
</body></html>"""

# Presenter-Modus ("S") — Referentenansicht in zweitem Fenster
PRESENTER = r"""<script>
(function(){function openP(){var w=window.open('','bkmPresenter','width=1180,height=760');if(!w){alert('Bitte Pop-ups erlauben, dann erneut „S“.');return;}
var slides=[].slice.call(document.querySelectorAll('.slide'));
function cur(){var i=slides.findIndex(function(s){return s.classList.contains('visible');});return i<0?0:i;}
function notesOf(i){var s=slides[i];var n=s&&s.querySelector('.notes');return n?n.textContent.trim():'— keine Notizen —';}
function titleOf(i){var s=slides[i];if(!s)return '';var h=s.querySelector('.gen-h,.gen-h1,blockquote');return h?h.textContent.replace(/\s+/g,' ').trim():('Folie '+(i+1));}
function go(d){var b=document.getElementById(d>0?'next':'prev');if(b)b.click();setTimeout(render,60);}
var doc=w.document;doc.open();doc.write('<!doctype html><meta charset=utf-8><title>Referentenansicht — BKM</title><style>*{margin:0;box-sizing:border-box;font-family:-apple-system,Segoe UI,sans-serif}body{background:#0a1c17;color:#fff;height:100vh;display:flex;flex-direction:column;overflow:hidden}.bar{display:flex;align-items:center;justify-content:space-between;padding:14px 22px;border-bottom:2px solid #b4e717;background:rgba(28,75,66,.55)}.timer{font-size:30px;font-weight:800;color:#b4e717}.clock{font-size:14px;color:rgba(255,255,255,.65);margin-top:3px}.pos{font-size:15px;color:rgba(255,255,255,.7)}.bar button{all:unset;cursor:pointer;background:#b4e717;color:#0f2620;font-weight:700;border-radius:8px;padding:10px 16px;margin-left:8px;font-size:14px}.bar .ghost{background:rgba(255,255,255,.12);color:#fff}.main{flex:1;display:grid;grid-template-columns:1.6fr 1fr;overflow:hidden}.now{padding:24px 28px;overflow:auto;border-right:1px solid rgba(255,255,255,.12)}.lbl{font-size:12px;letter-spacing:.16em;text-transform:uppercase;color:#b4e717;font-weight:700;margin-bottom:12px}.now h2{font-size:27px;font-weight:800;margin-bottom:18px}#nown{font-size:20px;line-height:1.6;white-space:pre-wrap;color:rgba(255,255,255,.92)}.nxt{padding:24px 28px;overflow:auto;background:rgba(255,255,255,.03)}.nxt h3{font-size:21px;font-weight:800;margin-bottom:12px}#nextn{font-size:15px;line-height:1.5;color:rgba(255,255,255,.6);white-space:pre-wrap}</style><body><div class=bar><div><div class=timer id=t>00:00</div><div class=clock id=c></div></div><div class=pos id=p></div><div><button class=ghost id=pv>◀</button><button id=nx>▶ Weiter</button><button class=ghost id=rs>⟳ Timer</button></div></div><div class=main><div class=now><div class=lbl>Aktuelle Folie · Notizen</div><h2 id=nowt></h2><div id=nown></div></div><div class=nxt><div class=lbl>Als Nächstes</div><h3 id=nextt></h3><div id=nextn></div></div></div>');doc.close();
var start=Date.now();function tw(n){return(n<10?'0':'')+n;}
function tick(){var T=doc.getElementById('t');if(!T)return;var s=Math.floor((Date.now()-start)/1000);T.textContent=tw(Math.floor(s/60))+':'+tw(s%60);var d=new Date();doc.getElementById('c').textContent='Uhrzeit '+tw(d.getHours())+':'+tw(d.getMinutes());}
function render(){if(!doc.body)return;var i=cur(),n=slides.length;doc.getElementById('p').textContent='Folie '+(i+1)+' / '+n;doc.getElementById('nowt').textContent=titleOf(i);doc.getElementById('nown').textContent=notesOf(i);var h=i+1<n;doc.getElementById('nextt').textContent=h?titleOf(i+1):'— Ende —';doc.getElementById('nextn').textContent=h?notesOf(i+1):'';}
doc.getElementById('nx').onclick=function(){go(1);};doc.getElementById('pv').onclick=function(){go(-1);};doc.getElementById('rs').onclick=function(){start=Date.now();tick();};
doc.addEventListener('keydown',function(e){if(e.key==='ArrowRight'||e.key===' ')go(1);else if(e.key==='ArrowLeft')go(-1);});
render();tick();setInterval(tick,1000);setInterval(render,400);w.focus();}
document.addEventListener('keydown',function(e){if((e.key==='s'||e.key==='S')&&!e.metaKey&&!e.ctrlKey)openP();});})();
</script>"""

# Akzentwort-Markup: "Wort {{Akzent}} Wort" -> <span class=g>Akzent</span>
def acc(t):
    t = esc(t)
    # erlaubte Marken-Auszeichnung wieder zulassen: Zeilenumbruch + weiches Trennzeichen
    t = t.replace('&lt;br&gt;', '<br>').replace('&lt;br/&gt;', '<br>').replace('&lt;br /&gt;', '<br>')
    t = t.replace('&amp;shy;', '&shy;')
    t = t.replace('&amp;amp;', '&amp;')  # falls Autor/LLM bereits `&amp;` schrieb -> nicht doppelt escapen
    return re.sub(r'\{\{(.+?)\}\}', r'<span class="g">\1</span>', t)

def icon(name):
    name = (name or 'fa-check').strip()
    if not name.startswith('fa-'): name = 'fa-' + name
    return '<i class="fas %s"></i>' % esc(name)

# ======================= Familien-Konfiguration =======================
FAM = {
  'bkm-glass-ag':         {'caps_all': False, 'chrome': 'ag',   'body': 'fam-glass'},
  'bkm-bold-poster':      {'caps_all': True,  'chrome': 'bold', 'body': 'fam-bold'},
  'bkm-glass-fachbetrieb':{'caps_all': False, 'chrome': 'ag',   'body': 'fam-fachbetrieb'},
}
# Hintergrund-Set + Grundfarbe je Familie
BGSET = {'bkm-glass-ag':('bg-ag','#0f2620'), 'bkm-bold-poster':('bg-ag','#0f2620'),
         'bkm-glass-fachbetrieb':('bg-fb','#f1ede6')}

def load_bgs(prefix):
    d = {}
    if not prefix: return d
    for i, f in enumerate(sorted(glob.glob(os.path.join(ROOT, 'assets/backgrounds/%s-*.jpg' % prefix))), start=1):
        d[i] = 'data:image/jpeg;base64,' + base64.b64encode(open(f, 'rb').read()).decode()
    return d

# Welche Typen sind "laut" (immer UPPERCASE, auch bei Hybrid-Casing)?
CAPS_TYPES = {'cover', 'chapter', 'statement', 'closing'}

def headline(text, stype, fam):
    """Headline mit korrektem Casing (Hybrid bei glass-ag, durchgehend UPPERCASE bei bold)."""
    caps = FAM[fam]['caps_all'] or stype in CAPS_TYPES
    cls = 'gen-h' if caps else 'gen-h mx'
    return '<h2 class="%s reveal d2">%s</h2>' % (cls, acc(text))

# ======================= Slide-Renderer pro Typ =======================
def r_cover(d, fam):
    meta = ''.join('<div class="m"><span class="k">%s</span><span class="v">%s</span></div>' %
                   (esc(x.get('k','')), esc(x.get('v',''))) for x in d.get('meta', []))
    btn = ('<a class="gen-btn reveal d4">%s %s</a>' % (icon('arrow-right'), esc(d['button']))) if d.get('button') else ''
    return ('<div class="gen-left">'
            '<div class="gen-eyebrow reveal d1">%s</div>'
            '<h1 class="gen-h1 reveal d1">%s</h1>'
            '%s%s%s</div>' % (
            esc(d.get('eyebrow','')), acc(d.get('title','')),
            ('<p class="gen-lead reveal d3">%s</p>' % acc(d['lead'])) if d.get('lead') else '',
            ('<div class="gen-meta reveal d4">%s</div>' % meta) if meta else '', btn))

def head_block(d, stype, fam):
    sub = ('<div class="gen-sub reveal d2">%s</div>' % acc(d['sub'])) if d.get('sub') else ''
    return ('<div class="gen-head"><div class="gen-eyebrow reveal d1">%s</div>%s%s</div>' %
            (esc(d.get('eyebrow','')), headline(d.get('title',''), stype, fam), sub))

def r_cards(d, fam):
    cs = ''
    for i, it in enumerate(d.get('items', [])[:4]):
        cs += ('<div class="gen-card reveal d%d"><div class="ic">%s</div>'
               '<h3>%s</h3><p>%s</p></div>' % (min(i+1,5), icon(it.get('icon')), acc(it.get('h','')), acc(it.get('p',''))))
    n = len(d.get('items', [])[:4])
    return head_block(d,'cards',fam) + '<div class="gen-grid g%d">%s</div>' % (n, cs)

def r_kpi(d, fam):
    ks = ''
    for i, it in enumerate(d.get('items', [])[:3]):
        ks += ('<div class="gen-card kpi reveal d%d"><div class="n">%s</div><div class="c">%s</div></div>'
               % (i+1, acc(it.get('value','')), acc(it.get('label',''))))
    return head_block(d,'kpi',fam) + '<div class="gen-grid g3 kpis">%s</div>' % ks

def r_split(d, fam):
    pts = ''.join('<div class="gen-li reveal d%d"><div class="ic">%s</div><p>%s</p></div>' %
                  (min(i+2,5), icon('check'), acc(p)) for i, p in enumerate(d.get('points', [])))
    img = d.get('image', '')
    src = embed_img(img) if img else TEX[2]
    cap = ('<figcaption>%s</figcaption>' % esc(d['caption'])) if d.get('caption') else ''
    return ('<div class="gen-split-txt"><div class="gen-eyebrow reveal d1">%s</div>%s%s</div>'
            '<figure class="gen-figure reveal d2"><img src="%s" alt="">%s</figure>' % (
            esc(d.get('eyebrow','')), headline(d.get('title',''),'split',fam), pts, src, cap))

def r_quote(d, fam):
    return ('<div class="gen-quote-mark">&ldquo;</div>'
            '<div class="gen-quote-wrap"><div class="gen-eyebrow reveal d1">%s</div>'
            '<blockquote class="reveal d2">%s</blockquote>'
            '<div class="gen-who reveal d3"><span class="ln"></span><span>%s</span></div></div>' % (
            esc(d.get('eyebrow','Das sagen Kunden')), acc(d.get('text','')), esc(d.get('source',''))))

def r_table(d, fam):
    cols = d.get('columns', []); hi = d.get('highlight', None)
    def cell(v, j, head=False):
        c = 'c hi' if (hi is not None and j == hi) else 'c'
        return '<div class="%s">%s</div>' % (c, esc(v))
    th = '<div class="tr head">' + ''.join(cell(c, j, True) for j, c in enumerate(cols)) + '</div>'
    trs = ''
    for row in d.get('rows', []):
        trs += '<div class="tr">' + ''.join(cell(v, j) for j, v in enumerate(row)) + '</div>'
    cols_css = 'grid-template-columns:1.7fr' + ' 1fr'*(max(len(cols)-1,1)) + ';'
    return head_block(d,'table',fam) + '<div class="gen-panel gen-table reveal d3" style="%s">%s%s</div>' % (cols_css, th, trs)

def r_compare(d, fam):
    cards = ''
    for k, col in enumerate(d.get('columns', [])[:2]):
        win = ' win' if col.get('win') else ''
        items = ''.join('<li class="%s">%s<span>%s</span></li>' %
                        (('yes' if col.get('win') else 'no'),
                         icon('check' if col.get('win') else 'xmark'), acc(x))
                        for x in col.get('items', []))
        cards += ('<div class="gen-card cmp%s reveal d%d"><span class="badge">%s</span>'
                  '<h3>%s</h3><ul>%s</ul></div>' % (win, k+1, esc(col.get('badge','')), acc(col.get('title','')), items))
    foot = ('<div class="gen-foot reveal d3">%s</div>' % acc(d['foot'])) if d.get('foot') else ''
    return head_block(d,'compare',fam) + '<div class="gen-grid g2 cmp">%s</div>%s' % (cards, foot)

def r_chart(d, fam):
    note = d.get('note', {})
    nb = ('<div class="gen-note reveal d3"><h3>%s</h3>%s%s</div>' % (
          acc(note.get('h','')),
          ('<p>%s</p>' % acc(note['p'])) if note.get('p') else '',
          ('<div class="cap">%s</div>' % esc(note['cap'])) if note.get('cap') else '')) if note else ''
    line = d.get('line')
    if line:  # Liniendiagramm (z. B. Trends-Kurve)
        n = len(line); mx = max([float(p.get('value',0) or 0) for p in line] + [1])
        coords = [((i/(n-1)*100) if n > 1 else 0, 100 - float(p.get('value',0) or 0)/mx*100) for i, p in enumerate(line)]
        poly = ' '.join('%.2f,%.2f' % c for c in coords)
        area = 'M0,100 L ' + ' L '.join('%.2f,%.2f' % c for c in coords) + ' L 100,100 Z'
        dots = ''; labels = ''
        for i, p in enumerate(line):
            x, top = coords[i]
            cv = ('<span class="cv">%s</span>' % esc(p['display'])) if p.get('display') else ''
            dots += '<div class="dot%s" style="left:%.2f%%;top:%.2f%%">%s</div>' % (' hi' if p.get('hi') else '', x, top, cv)
            if p.get('label'): labels += '<span style="left:%.2f%%">%s</span>' % (x, esc(p['label']))
        svg = ('<svg viewBox="0 0 100 100" preserveAspectRatio="none"><defs>'
               '<linearGradient id="lg" x1="0" y1="0" x2="0" y2="1">'
               '<stop offset="0" stop-color="var(--lime)" stop-opacity="0.32"/>'
               '<stop offset="1" stop-color="var(--lime)" stop-opacity="0"/></linearGradient></defs>'
               '<path d="%s" fill="url(#lg)"/><polyline points="%s" fill="none" stroke="var(--lime)" '
               'stroke-width="2.5" vector-effect="non-scaling-stroke" stroke-linejoin="round" stroke-linecap="round"/></svg>' % (area, poly))
        cell = '<div class="reveal d2"><div class="gen-line">%s%s</div><div class="lbls">%s</div></div>' % (svg, dots, labels)
        return head_block(d,'chart',fam) + '<div class="gen-chart-wrap">%s%s</div>' % (cell, nb)
    bars = d.get('bars', []); mx = max([float(b.get('value',0) or 0) for b in bars] + [1])
    bs = ''
    for b in bars:
        v = float(b.get('value',0) or 0); h = max(4, round(v/mx*100))
        hi = ' hi' if b.get('hi') else ''
        bs += ('<div class="bar%s"><div class="val">%s</div><div class="col" style="height:%d%%"></div>'
               '<div class="lbl">%s</div></div>' % (hi, esc(b.get('display', b.get('value',''))), h, esc(b.get('label',''))))
    return head_block(d,'chart',fam) + '<div class="gen-chart-wrap"><div class="gen-chart reveal d2">%s</div>%s</div>' % (bs, nb)

def r_chapter(d, fam):
    return ('<div class="gen-chapter"><div class="big reveal d1">%s</div>'
            '<div class="t"><div class="gen-eyebrow reveal d2">%s</div>'
            '<h2 class="gen-h reveal d3">%s</h2></div></div>' % (
            esc(d.get('no','01')), esc(d.get('eyebrow','')), acc(d.get('title',''))))

def r_subhead(d, fam):
    sub = ('<div class="gen-sub reveal d3">%s</div>' % acc(d['sub'])) if d.get('sub') else ''
    return ('<div class="gen-subhead"><div class="gen-eyebrow reveal d1">%s</div>%s%s</div>' %
            (esc(d.get('eyebrow','')), headline(d.get('title',''),'subhead',fam), sub))

def r_statement(d, fam):
    return ('<div class="gen-statement"><div class="gen-eyebrow reveal d1">%s</div>'
            '<h1 class="gen-h1 reveal d2">%s</h1>%s</div>' % (
            esc(d.get('eyebrow','')), acc(d.get('title','')),
            ('<p class="gen-lead reveal d3">%s</p>' % acc(d['lead'])) if d.get('lead') else ''))

def r_process(d, fam):
    rows = ''
    for i, st in enumerate(d.get('steps', [])):
        rows += ('<div class="row reveal d%d"><div class="no">%02d</div><div><h3>%s</h3>%s</div></div>' %
                 (min(i+1,5), i+1, acc(st.get('h','')), ('<p>%s</p>' % acc(st['p'])) if st.get('p') else ''))
    return head_block(d,'process',fam) + '<div class="gen-panel gen-process reveal d2">%s</div>' % rows

def r_agenda(d, fam):
    rows = ''
    for i, r in enumerate(d.get('rows', [])):
        rows += ('<div class="row reveal d%d"><div class="time">%s</div>'
                 '<div class="topic">%s%s</div><div class="spk">%s</div><div class="no">%02d</div></div>' % (
                 min(i+1,5), esc(r.get('time','')), acc(r.get('topic','')),
                 ('<small>%s</small>' % acc(r['sub'])) if r.get('sub') else '', esc(r.get('spk','')), i+1))
    return head_block(d,'agenda',fam) + '<div class="gen-panel gen-agenda reveal d2">%s</div>' % rows

def r_timeline(d, fam):
    pts = d.get('points', []); n = max(len(pts),1)
    items = ''
    for i, p in enumerate(pts):
        left = round((i + 0.5) / n * 100, 2); ud = 'up' if i % 2 == 0 else 'down'
        items += ('<div class="pt" style="left:%s%%"></div>'
                  '<div class="item %s" style="left:%s%%"><div class="yr">%s</div><h3>%s</h3>%s</div>' % (
                  left, ud, left, esc(p.get('yr','')), acc(p.get('h','')),
                  ('<p>%s</p>' % acc(p['p'])) if p.get('p') else ''))
    return head_block(d,'timeline',fam) + '<div class="gen-tl-wrap reveal d2"><div class="line">%s</div></div>' % items

def r_closing(d, fam):
    chips = ''.join('<span class="v">%s</span>' % esc(v) for v in d.get('chips', []))
    return ('<div class="gen-closing"><div class="gen-eyebrow reveal d1">%s</div>'
            '<h1 class="gen-h1 reveal d2">%s</h1>%s%s</div>' % (
            esc(d.get('eyebrow','')), acc(d.get('title','')),
            ('<div class="gen-chips reveal d3">%s</div>' % chips) if chips else '',
            ('<p class="gen-punch reveal d3">%s</p>' % acc(d['punch'])) if d.get('punch') else ''))

def _initials(name):
    parts = [p for p in re.split(r'\s+', (name or '').strip()) if p]
    return esc(''.join(p[0] for p in parts[:2]).upper() or '·')

# ---- Batch 1: neue Archetypen ----
def r_funnel(d, fam):
    tiers = d.get('tiers', []); widths = [100, 74, 50, 34, 24]
    rows = ''
    for i, t in enumerate(tiers):
        w = t.get('width', widths[min(i, 4)])
        rows += ('<div class="tier reveal d%d" style="width:%s%%"><div class="v">%s</div>'
                 '<div class="l">%s</div></div>' % (min(i+1,5), w, acc(t.get('value','')), acc(t.get('label',''))))
    return head_block(d,'funnel',fam) + '<div class="gen-funnel">%s</div>' % rows

def r_donut(d, fam):
    segs = d.get('segments', []); total = sum(float(s.get('value',0) or 0) for s in segs) or 1
    cols = ['var(--lime)','var(--pure-green)','var(--transition-green)','rgba(255,255,255,0.25)']
    stops, leg, cum = [], '', 0.0
    for i, s in enumerate(segs):
        pct = float(s.get('value',0) or 0)/total*100; c = cols[i % len(cols)]
        stops.append('%s %.2f%% %.2f%%' % (c, cum, cum+pct))
        leg += ('<div class="row"><span class="dot" style="background:%s"></span>%s'
                '<span class="pct">%d%%</span></div>' % (c, esc(s.get('label','')), round(pct)))
        cum += pct
    ctr = d.get('center', {})
    return head_block(d,'donut',fam) + (
        '<div class="gen-donut-wrap"><div class="gen-donut reveal d2" style="background:conic-gradient(%s)">'
        '<div class="center"><div class="v">%s</div><div class="l">%s</div></div></div>'
        '<div class="gen-legend reveal d3">%s</div></div>' % (
        ','.join(stops), esc(ctr.get('value','')), esc(ctr.get('label','')), leg))

def r_bigstat(d, fam):
    ss = ''.join('<div class="s"><div class="n">%s</div><div class="l">%s</div></div>' %
                 (acc(x.get('value','')), acc(x.get('label',''))) for x in d.get('stats', []))
    return ('<div class="gen-bigstat"><div class="gen-eyebrow reveal d1">%s</div>'
            '<div class="huge reveal d2">%s</div>%s%s</div>' % (
            esc(d.get('eyebrow','')), acc(d.get('value','')),
            ('<div class="sub reveal d2">%s</div>' % acc(d['sub'])) if d.get('sub') else '',
            ('<div class="row reveal d3">%s</div>' % ss) if ss else ''))

def r_bubbles(d, fam):
    bs = d.get('bubbles', [])[:4]
    def _num(b):
        try: return float(b.get('size', 50))
        except (TypeError, ValueError): return 50.0
    mx = max([_num(b) for b in bs] + [1])
    pos = [(20,'top:120px'), (430,'top:280px'), (820,'top:70px'), (1190,'top:260px')]
    cols = ['rgba(180,231,23,0.92)','rgba(77,175,70,0.9)','rgba(40,125,75,0.92)','rgba(255,255,255,0.14)']
    txt = ['#0f2620','#0f2620','#fff','#fff']
    out = ''
    for i, b in enumerate(bs):
        sz = int(210 + _num(b)/mx*220)
        out += ('<div class="gen-bubble reveal d%d" style="width:%dpx;height:%dpx;left:%dpx;%s;background:%s;color:%s">'
                '<div class="v" style="font-size:%dpx">%s</div><div class="l">%s</div></div>' % (
                min(i+1,5), sz, sz, pos[i][0], pos[i][1], cols[i], txt[i], max(30, sz//6),
                acc(b.get('value','')), acc(b.get('label',''))))
    return head_block(d,'bubbles',fam) + '<div class="gen-bubbles">%s</div>' % out

def r_team(d, fam):
    ms = ''
    for m in d.get('members', []):
        img = m.get('image')
        av = ('<img src="%s" alt="">' % embed_img(img)) if img else _initials(m.get('name',''))
        ms += ('<div class="m reveal"><div class="av">%s</div><div class="nm">%s</div>'
               '<div class="ro">%s</div></div>' % (av, esc(m.get('name','')), esc(m.get('role',''))))
    return head_block(d,'team',fam) + '<div class="gen-team">%s</div>' % ms

def r_twocol(d, fam):
    cols = ''
    for c in d.get('columns', [])[:2]:
        items = ''.join('<li>%s<span>%s</span></li>' % (icon('arrow-right'), acc(x)) for x in c.get('items', []))
        cols += ('<div class="col reveal">%s%s%s</div>' % (
                 ('<h3>%s</h3>' % acc(c['h'])) if c.get('h') else '',
                 ('<p>%s</p>' % acc(c['p'])) if c.get('p') else '',
                 ('<ul>%s</ul>' % items) if items else ''))
    return head_block(d,'twocol',fam) + '<div class="gen-twocol">%s</div>' % cols

# ---- Batch 2: weitere Archetypen ----
def r_pricing(d, fam):
    plans = d.get('plans', [])
    cs = ''
    for p in plans:
        feats = ''.join('<li>%s<span>%s</span></li>' % (icon('check'), acc(x)) for x in p.get('features', []))
        cs += ('<div class="plan%s reveal">%s<div class="nm">%s</div><div class="price">%s</div>'
               '<div class="per">%s</div><ul>%s</ul></div>' % (
               ' hi' if p.get('highlight') else '',
               ('<span class="badge">%s</span>' % esc(p['badge'])) if p.get('badge') else '',
               esc(p.get('name','')), acc(p.get('price','')), esc(p.get('period','')), feats))
    return head_block(d,'pricing',fam) + '<div class="gen-pricing g%d">%s</div>' % (min(max(len(plans),2),4), cs)

def r_flow(d, fam):
    parts = []
    for i, s in enumerate(d.get('steps', [])):
        parts.append('<div class="step reveal d%d"><div class="ic">%s</div><h3>%s</h3>%s</div>' % (
            min(i+1,5), icon(s.get('icon','arrow-right')), acc(s.get('h','')),
            ('<p>%s</p>' % acc(s['p'])) if s.get('p') else ''))
    joined = ('<div class="arr">' + icon('arrow-right') + '</div>').join(parts)
    return head_block(d,'flow',fam) + '<div class="gen-flow">%s</div>' % joined

def r_gauge(d, fam):
    v = max(0.0, min(100.0, float(d.get('value',0) or 0))); note = d.get('note', {})
    ring = 'conic-gradient(var(--lime) 0 %.2f%%, rgba(255,255,255,0.12) %.2f%% 100%%)' % (v, v)
    return head_block(d,'gauge',fam) + (
        '<div class="gen-gauge-wrap"><div class="gen-gauge reveal d2" style="background:%s">'
        '<div class="center"><div class="v">%s</div><div class="l">%s</div></div></div>'
        '<div class="gen-gauge-note reveal d3"><h3>%s</h3>%s</div></div>' % (
        ring, esc(d.get('display', '%d%%' % round(v))), esc(d.get('label','')),
        acc(note.get('h','')), ('<p>%s</p>' % acc(note['p'])) if note.get('p') else ''))

def r_pictograph(d, fam):
    grps = d.get('groups', [])
    out = ''
    for g in grps:
        total = int(g.get('total', 10)); filled = int(g.get('filled', 0))
        ic = g.get('icon', 'user'); ic = ic if ic.startswith('fa-') else 'fa-' + ic
        icons = ''.join('<i class="fas %s%s"></i>' % (ic, (' on' if k < filled else '')) for k in range(total))
        out += ('<div class="grp reveal"><div class="v">%s</div><div class="icons">%s</div>'
                '<div class="l">%s</div></div>' % (acc(g.get('value','')), icons, acc(g.get('label',''))))
    return head_block(d,'pictograph',fam) + '<div class="gen-picto g%d">%s</div>' % (min(max(len(grps),1),3), out)

def r_imagecover(d, fam):
    img = d.get('image')
    photo = ('<div class="photo"><img src="%s" alt=""></div><div class="ov"></div>' % embed_img(img)) if img else ''
    return ('%s<div class="txt"><div class="gen-eyebrow reveal d1">%s</div>'
            '<h1 class="gen-h1 reveal d2">%s</h1>%s</div>' % (
            photo, esc(d.get('eyebrow','')), acc(d.get('title','')),
            ('<div class="sub reveal d3">%s</div>' % acc(d['sub'])) if d.get('sub') else ''))

def r_bento(d, fam):
    cs = ''
    for it in d.get('items', []):
        cls = 'cell' + (' wide' if it.get('wide') else '') + (' tall' if it.get('tall') else '') + (' accent' if it.get('accent') else '')
        ic = ('<div class="ic">%s</div>' % icon(it.get('icon'))) if it.get('icon') else ''
        cs += '<div class="%s reveal">%s<h3>%s</h3>%s</div>' % (
            cls, ic, acc(it.get('h','')), ('<p>%s</p>' % acc(it['p'])) if it.get('p') else '')
    return head_block(d,'bento',fam) + '<div class="gen-bento">%s</div>' % cs

# ---- Batch 3: Rest-Archetypen ----
def r_statcluster(d, fam):
    items = d.get('items', [])[:5]
    pos = [(20,20,240),(430,200,180),(770,30,270),(1150,210,190),(880,420,160)]
    out = ''
    for i, it in enumerate(items):
        l, t, sz = pos[i]; img = it.get('image')
        inner = ('<img src="%s" alt="">' % embed_img(img)) if img else ''
        out += ('<div class="node reveal" style="left:%dpx;top:%dpx"><div class="circle" style="width:%dpx;height:%dpx">%s</div>'
                '<div class="v">%s</div><div class="l">%s</div></div>' % (
                l, t, sz, sz, inner, acc(it.get('value','')), acc(it.get('label',''))))
    return head_block(d,'statcluster',fam) + '<div class="gen-cluster">%s</div>' % out

def r_numlist(d, fam):
    rows = ''
    for i, it in enumerate(d.get('items', [])):
        no = esc(it.get('no', '%02d' % (i+1)))
        tag = ('<div class="tg">%s</div>' % esc(it['tag'])) if it.get('tag') else '<div></div>'
        rows += '<div class="row reveal d%d"><div class="no">%s</div><div class="tx">%s</div>%s</div>' % (
                min(i+1,5), no, acc(it.get('text','')), tag)
    return head_block(d,'numlist',fam) + '<div class="gen-numlist">%s</div>' % rows

def r_gallery(d, fam):
    figs = ''
    for im in d.get('images', []):
        cap = ('<figcaption>%s</figcaption>' % esc(im['caption'])) if im.get('caption') else ''
        figs += '<figure><img src="%s" alt="">%s</figure>' % (embed_img(im.get('src')), cap)
    n = len(d.get('images', []))
    return head_block(d,'gallery',fam) + '<div class="gen-gallery g%d reveal d2">%s</div>' % (min(max(n,2),4), figs)

def r_contact(d, fam):
    blocks = ''.join('<div class="b"><div class="k">%s</div><div class="v">%s</div></div>' %
                     (esc(b.get('k','')), acc(b.get('v',''))) for b in d.get('blocks', []))
    img = d.get('image')
    photo = ('<figure class="gen-contact-photo"><img src="%s" alt=""></figure>' % embed_img(img)) if img else ''
    return ('<div class="gen-contact"><div class="gen-eyebrow reveal d1">%s</div>%s'
            '<div class="blocks reveal d2">%s</div></div>%s' % (
            esc(d.get('eyebrow','')), headline(d.get('title',''),'contact',fam), blocks, photo))

def r_imagesplit(d, fam):
    side = 'left' if d.get('side') == 'left' else 'right'
    img = d.get('image')
    photo = ('<div class="photo"><img src="%s" alt=""></div>' % embed_img(img)) if img else ''
    pts = ''.join('<div class="gen-li reveal d%d"><div class="ic">%s</div><p>%s</p></div>' %
                  (min(i+2,5), icon('check'), acc(p)) for i, p in enumerate(d.get('points', [])))
    body = ('<p class="reveal d3">%s</p>' % acc(d['lead'])) if d.get('lead') else ''
    txt = ('<div class="txt"><div class="gen-eyebrow reveal d1">%s</div>%s%s%s</div>' %
           (esc(d.get('eyebrow','')), headline(d.get('title',''),'imagesplit',fam), body, pts))
    return '<div class="gen-imgsplit %s">%s%s</div>' % (side, photo, txt)

RENDER = {'cover':r_cover,'cards':r_cards,'kpi':r_kpi,'split':r_split,'quote':r_quote,
          'table':r_table,'compare':r_compare,'chart':r_chart,'chapter':r_chapter,
          'subhead':r_subhead,'statement':r_statement,'process':r_process,'agenda':r_agenda,
          'timeline':r_timeline,'closing':r_closing,
          'funnel':r_funnel,'donut':r_donut,'bigstat':r_bigstat,'bubbles':r_bubbles,
          'team':r_team,'twocol':r_twocol,
          'pricing':r_pricing,'flow':r_flow,'gauge':r_gauge,'pictograph':r_pictograph,
          'imagecover':r_imagecover,'bento':r_bento,
          'statcluster':r_statcluster,'numlist':r_numlist,'gallery':r_gallery,
          'contact':r_contact,'imagesplit':r_imagesplit}

# Bild einbetten (Pfad relativ zum Spec) — fallback: Textur als Platzhalter
SPEC_DIR = '.'
_MIME = {'jpg':'jpeg','jpeg':'jpeg','png':'png','webp':'webp','gif':'gif','svg':'svg+xml','avif':'avif','bmp':'bmp'}
def embed_img(path):
    p = path if os.path.isabs(path) else os.path.join(SPEC_DIR, path)
    if os.path.exists(p):
        ext = p.lower().rsplit('.', 1)[-1]
        mime = _MIME.get(ext, 'png')
        return 'data:image/%s;base64,%s' % (mime, base64.b64encode(open(p, 'rb').read()).decode())
    return TEX[2]

# ======================= Komposition / Auto-Mix =======================
DIVIDERS = {'chapter','subhead'}
def lint(slides, strict=False):
    types = [s.get('type') for s in slides]
    warn = []
    run = 1
    for i in range(1, len(types)):
        if types[i] == types[i-1] and types[i] not in ('cover','closing'):
            run += 1
            if run >= 3: warn.append('Folie %d: %d× „%s“ in Folge — Typ variieren.' % (i+1, run, types[i]))
        else: run = 1
    since = 0
    for i, t in enumerate(types):
        since = 0 if t in DIVIDERS or t == 'cover' else since + 1
        if since > 8: warn.append('Folie %d: >8 Folien ohne Kapitel-Trenner/Unterthema — Gliederung einstreuen.' % (i+1))
    from collections import Counter
    dist = Counter(types)
    print('  Typen-Verteilung:', dict(dist))
    if warn:
        print('  ⚠ Mix-Hinweise:'); [print('   -', w) for w in warn]
        if strict: raise SystemExit('Strict: Mix-Regeln verletzt.')
    else:
        print('  ✓ Mix-Rhythmus ok.')
    return warn

# Hintergrund-Rotation (nie zweimal gleich nebeneinander) — chapter bevorzugt t4
def bg_rotation(slides, n):
    n = max(n, 1)
    order = []; prev = 0
    for s in slides:
        if s.get('type') == 'cover':
            t = 1
        else:
            t = prev % n + 1            # zyklisch 1..n -> nie zweimal gleich nebeneinander
            if t == prev: t = t % n + 1
        order.append(t); prev = t
    return order

# ======================= HTML-Shell =======================
def build(spec, strict=False):
    fam = spec.get('family', 'bkm-glass-ag')
    if fam not in FAM: raise SystemExit('Unbekannte family: %s' % fam)
    slides = spec.get('slides', [])
    print('Deck:', spec.get('meta',{}).get('title','(ohne Titel)'), '| family:', fam, '| Folien:', len(slides))
    lint(slides, strict)
    prefix, bgbase = BGSET.get(fam, ('bg-ag', '#0f2620'))
    BGS = load_bgs(prefix)
    bgs = bg_rotation(slides, len(BGS)) if BGS else [0] * len(slides)
    fambody = FAM[fam]['body']
    meta = spec.get('meta',{})
    tagtop = esc(meta.get('tagtop',''))
    event = esc(meta.get('event',''))
    tagline = acc(meta.get('tagline','')) if meta.get('tagline') else ''
    secs = []
    notes_js_data = []
    for i, sl in enumerate(slides):
        st = sl.get('type')
        if st not in RENDER:
            print('  ! Unbekannter Typ übersprungen:', st); continue
        inner = RENDER[st](sl, fam)
        vis = ' visible' if i == 0 else ''
        chrome = chrome_html(fam, st, sl, tagtop, event, tagline)
        notes = esc(sl.get('notes','')).replace('\n','&#10;')
        bgdiv = ('<div class="bg t%d"></div>' % bgs[i]) if BGS else ''
        secs.append(
          '<section class="slide gen g-%s%s">'
          '%s%s%s'
          '<div class="pg">%02d</div>'
          '<aside class="notes">%s</aside></section>' % (st, vis, bgdiv, chrome, inner, i+1, notes))
    bg_css = ''.join('.bg.t%d{background:%s url(%s) center/cover;}' % (k, bgbase, v) for k, v in BGS.items())
    title = esc(spec.get('meta',{}).get('title','BKM Deck'))
    total = str(len([s for s in slides if s.get('type') in RENDER]))
    out = (SHELL
           .replace('@@TITLE@@', title)
           .replace('@@FONTS@@', FONTS)
           .replace('@@GENCSS@@', GEN_CSS)
           .replace('@@BGCSS@@', bg_css)
           .replace('@@FAMBODY@@', fambody)
           .replace('@@SECTIONS@@', '\n'.join(secs))
           .replace('@@TOTAL@@', total)
           .replace('@@PRESENTER@@', PRESENTER))
    return out

def chrome_html(fam, st, sl, tagtop, event='', tagline=''):
    rub = esc(sl.get('rubric', tagtop))
    # helle Familien -> grau-grünes Logo; dunkle -> weißes Logo
    logo = LOGO_DARK if FAM[fam].get('body') == 'fam-fachbetrieb' else LOGO
    # Event-Chrome (familienübergreifend): Logo links, Event-Label rechts, Tagline unten links
    if event or tagline:
        ev = ('<div class="gen-event">%s</div>' % event) if event else ''
        tg = ('<div class="gen-tagline">%s</div>' % tagline) if tagline else ''
        return '<div class="ev">%s</div>%s%s' % (logo, ev, tg)
    if FAM[fam]['chrome'] == 'bold':
        mark = esc(sl.get('mark', tagtop or 'BKM'))
        return ('<div class="gen-mark">%s %s</div>%s'
                '<div class="gen-kicker">BKM Mannesmann · Bautenschutz</div>' % (icon('bolt'), mark, logo))
    # ag
    tt = ('<div class="tagtop">%s</div>' % rub) if rub else ''
    return logo + tt

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('spec'); ap.add_argument('-o','--out', required=True); ap.add_argument('--strict', action='store_true')
    a = ap.parse_args()
    SPEC_DIR = os.path.dirname(os.path.abspath(a.spec))
    spec = json.load(open(a.spec, encoding='utf-8'))
    html_out = build(spec, a.strict)
    open(a.out,'w',encoding='utf-8').write(html_out)
    print('→ geschrieben:', a.out, '(%d KB)' % (len(html_out)//1024))
