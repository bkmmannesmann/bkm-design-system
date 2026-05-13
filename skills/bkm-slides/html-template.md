# BKM Slides — Baukasten (v4)

> **PFLICHT-REGEL:** Jede Slide MUSS aus einem der 5 Templates unten kopiert werden. Eigene CSS-Erfindungen sind VERBOTEN. Nur Inhalte (Texte, Bild-URLs, Icons) dürfen angepasst werden.

> **Golden References:** Siehe `examples/bkm-ag-showroom-glasmorphismus.html` und `examples/fachbetrieb-showroom-glasmorphismus.html` für das fertige Ergebnis aller 5 Slide-Typen in einer navigierbaren Präsentation.

---

## Kontext-Umschaltung (BKM AG ↔ Fachbetrieb)

Alle Templates unten sind im **BKM AG** Kontext (dunkel). Für **Fachbetrieb** (hell) ersetze diese Werte:

| Element | BKM AG (dunkel) | Fachbetrieb (hell) |
|---------|--------|-------------|
| Overlay-Basis | `rgba(28,75,66, ...)` | `rgba(246,245,242, ...)` |
| Glass-Card bg | `rgba(255,255,255,0.07)` | `rgba(255,255,255,0.55)` |
| Glass-Card border | `rgba(255,255,255,0.12)` | `rgba(255,255,255,0.7)` |
| Glass-Card ::before | `rgba(255,255,255,0.04)` | `rgba(255,255,255,0.3)` |
| Headlines | `#ffffff` | `#1c4b42` |
| Body-Text | `rgba(255,255,255,0.7)` | `#494949` |
| Check-Text | `rgba(255,255,255,0.85)` | `#494949` |
| Muted Text | `rgba(255,255,255,0.5)` | `rgba(73,73,73,0.6)` |
| Section-Label | `#b4e717` | `#4daf46` |
| Checkmarks/Icons | `#b4e717` | `#4daf46` |
| Accent-Line | `#b4e717` | `#4daf46` |
| Status-Badge bg | `rgba(180,231,23,0.1)` | `rgba(77,175,70,0.08)` |
| Status-Badge border | `rgba(180,231,23,0.25)` | `rgba(77,175,70,0.25)` |
| Status-Badge color | `#b4e717` | `#4daf46` |
| Icon-Circles bg | `rgba(180,231,23,0.12)` | `rgba(77,175,70,0.1)` |
| Icon-Circles color | `#b4e717` | `#4daf46` |
| Footer-Bar bg | `rgba(28,75,66,0.95)` | `rgba(40,125,75,0.95)` |
| Footer-Icon | `#b4e717` | `#b4e717` (bleibt Lime!) |
| Footer-Text | `#ffffff` | `#ffffff` |
| Page-Num | `rgba(255,255,255,0.3)` | `rgba(73,73,73,0.3)` |
| Logo | white-puregreen | stonegrey-puregreen |
| Keyvisual | on-dark.svg, opacity 0.18 | on-light.svg, opacity 0.15 |
| Trends-Bar bg | `rgba(28,75,66,0.9)` | `rgba(40,125,75,0.95)` |

---

## Pflicht-Abhängigkeiten (in jedem Slide-Head)

```html
<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" rel="stylesheet">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Unbounded:wght@900&display=swap" rel="stylesheet">
```

---

## SLIDE-TYP 1: Titel-Slide (mit Keyvisual + Trends-Bar)

**Wann verwenden:** Erste Folie jeder Präsentation. Enthält Headline, Subtitle, Meta-Info, optionale Trends-Bar unten.

```html
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" rel="stylesheet">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Unbounded:wght@900&display=swap" rel="stylesheet">
    <style>
      * { margin: 0; padding: 0; box-sizing: border-box; }
      .slide-container {
        width: 1280px; min-height: 720px; position: relative;
        overflow: hidden; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
      }
      .bg-photo { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; }
      .bg-overlay {
        position: absolute; inset: 0;
        background: linear-gradient(140deg, rgba(28,75,66,0.80) 0%, rgba(28,75,66,0.60) 50%, rgba(28,75,66,0.75) 100%);
      }
      .accent-line {
        position: absolute; left: 7%; top: 18%; width: 4px; height: 60%;
        background: #b4e717; border-radius: 2px; z-index: 10;
      }
      .logo {
        position: absolute; top: 36px; right: 48px; height: 38px;
        z-index: 10; object-fit: contain;
      }
      .keyvisual {
        position: absolute; top: 0; right: 0; height: 100%; width: 22%;
        object-fit: cover; object-position: left center; opacity: 0.18; z-index: 5;
      }
      .glass-card {
        position: absolute; top: 50%; left: 10%; transform: translateY(-50%);
        z-index: 10; max-width: 600px;
        background: rgba(255,255,255,0.07); backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px); border: 1px solid rgba(255,255,255,0.12);
        border-radius: 16px; padding: 52px 48px;
      }
      .glass-card::before {
        content: ''; position: absolute; inset: 0; border-radius: 16px;
        background: linear-gradient(160deg, rgba(255,255,255,0.04) 0%, transparent 40%);
        pointer-events: none;
      }
      .glass-label {
        font-weight: 700; font-size: 11px; text-transform: uppercase;
        letter-spacing: 0.12em; color: #b4e717; margin-bottom: 16px;
      }
      .glass-headline {
        font-family: 'Unbounded', sans-serif; font-weight: 900; font-size: 56px;
        text-transform: uppercase; color: #ffffff; line-height: 1.0; letter-spacing: -0.04em;
      }
      .glass-subtitle {
        font-weight: 400; font-size: 17px; color: rgba(255,255,255,0.7);
        line-height: 1.6; margin-top: 18px; max-width: 90%;
      }
      .glass-tagline {
        font-weight: 700; font-size: 13px; color: rgba(255,255,255,0.5); margin-top: 12px;
      }
      .glass-meta { margin-top: 28px; display: flex; align-items: center; gap: 10px; }
      .meta-dot { width: 8px; height: 8px; border-radius: 50%; background: #b4e717; }
      .meta-text {
        font-weight: 700; font-size: 11px; text-transform: uppercase;
        letter-spacing: 0.06em; color: #b4e717;
      }
      .trends-bar {
        position: absolute; bottom: 0; left: 0; right: 0;
        background: rgba(28,75,66,0.9); backdrop-filter: blur(10px);
        padding: 16px 48px; display: flex; align-items: center; gap: 40px; z-index: 10;
      }
      .trend-item { display: flex; align-items: center; gap: 10px; }
      .trend-icon { color: #b4e717; font-size: 16px; }
      .trend-text {
        font-weight: 700; font-size: 12px; color: #ffffff;
        text-transform: uppercase; letter-spacing: 0.03em;
      }
      .trend-sub {
        font-weight: 400; font-size: 11px; color: rgba(255,255,255,0.6);
        text-transform: none; letter-spacing: 0;
      }
    </style>
</head>
<body>
    <div class="slide-container">
      <img class="bg-photo" src="{{PHOTO_URL}}" alt="">
      <div class="bg-overlay"></div>
      <img class="keyvisual" src="{{KEYVISUAL_URL}}" alt="">
      <div class="accent-line"></div>
      <img class="logo" src="{{LOGO_URL}}" alt="BKM Mannesmann">
      <div class="glass-card">
        <div class="glass-label">{{LABEL}}</div>
        <h1 class="glass-headline">{{HEADLINE_LINE1}}<br>{{HEADLINE_LINE2}}</h1>
        <p class="glass-subtitle">{{SUBTITLE}}</p>
        <p class="glass-tagline">{{TAGLINE}}</p>
        <div class="glass-meta">
          <div class="meta-dot"></div>
          <span class="meta-text">{{META_TEXT}}</span>
        </div>
      </div>
      <div class="trends-bar">
        <div class="trend-item">
          <i class="fas fa-handshake trend-icon"></i>
          <div><div class="trend-text">{{TREND_1}}</div><div class="trend-sub">{{TREND_1_SUB}}</div></div>
        </div>
        <div class="trend-item">
          <i class="fas fa-laptop-code trend-icon"></i>
          <div><div class="trend-text">{{TREND_2}}</div><div class="trend-sub">{{TREND_2_SUB}}</div></div>
        </div>
        <div class="trend-item">
          <i class="fas fa-user-shield trend-icon"></i>
          <div><div class="trend-text">{{TREND_3}}</div><div class="trend-sub">{{TREND_3_SUB}}</div></div>
        </div>
        <div class="trend-item">
          <i class="fas fa-leaf trend-icon"></i>
          <div><div class="trend-text">{{TREND_4}}</div><div class="trend-sub">{{TREND_4_SUB}}</div></div>
        </div>
      </div>
    </div>
</body>
</html>
```

---

## SLIDE-TYP 2: Checklist + Status-Card

**Wann verwenden:** Wenn eine Liste von Vorteilen/Features mit einem Status-Badge gezeigt werden soll.

```html
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" rel="stylesheet">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Unbounded:wght@900&display=swap" rel="stylesheet">
    <style>
      * { margin: 0; padding: 0; box-sizing: border-box; }
      .slide-container {
        width: 1280px; min-height: 720px; position: relative;
        overflow: hidden; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
      }
      .bg-photo { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; }
      .bg-overlay {
        position: absolute; inset: 0;
        background: linear-gradient(160deg, rgba(28,75,66,0.82) 0%, rgba(28,75,66,0.65) 60%, rgba(28,75,66,0.78) 100%);
      }
      .logo { position: absolute; top: 32px; right: 44px; height: 32px; z-index: 10; object-fit: contain; }
      .content-wrapper { position: relative; z-index: 10; display: flex; flex-direction: column; height: 720px; }
      .top-section { padding: 56px 80px 0 80px; }
      .section-label {
        font-weight: 700; font-size: 11px; text-transform: uppercase;
        letter-spacing: 0.12em; color: #b4e717; margin-bottom: 12px;
      }
      .headline {
        font-family: 'Unbounded', sans-serif; font-weight: 900; font-size: 48px;
        text-transform: uppercase; color: #ffffff; line-height: 1.0; letter-spacing: -0.03em;
      }
      .subtitle { font-weight: 700; font-size: 18px; color: rgba(255,255,255,0.7); margin-top: 10px; }
      .main-content { flex: 1; display: flex; align-items: center; padding: 30px 80px; gap: 40px; }
      .glass-card {
        background: rgba(255,255,255,0.07); backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px); border: 1px solid rgba(255,255,255,0.12);
        border-radius: 14px; padding: 36px 40px; flex: 1;
      }
      .checklist { list-style: none; display: flex; flex-direction: column; gap: 16px; }
      .checklist li { display: flex; align-items: center; gap: 14px; }
      .check-icon { color: #b4e717; font-size: 16px; flex-shrink: 0; }
      .check-text { font-weight: 400; font-size: 15px; color: #ffffff; line-height: 1.4; }
      .status-card {
        background: rgba(180,231,23,0.1); backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px); border: 1px solid rgba(180,231,23,0.25);
        border-radius: 14px; padding: 32px 36px; width: 280px; text-align: center;
      }
      .status-badge {
        display: inline-block; background: rgba(180,231,23,0.15);
        border: 1px solid rgba(180,231,23,0.4); border-radius: 20px;
        padding: 6px 16px; font-weight: 700; font-size: 11px;
        text-transform: uppercase; letter-spacing: 0.08em; color: #b4e717; margin-bottom: 20px;
      }
      .status-icon { font-size: 48px; color: #b4e717; margin-bottom: 16px; }
      .status-title {
        font-family: 'Unbounded', sans-serif; font-weight: 900; font-size: 16px;
        color: #ffffff; text-transform: uppercase; letter-spacing: -0.02em;
      }
      .footer-bar {
        background: rgba(28,75,66,0.95); padding: 16px 80px;
        display: flex; align-items: center; gap: 12px;
      }
      .footer-icon { color: #b4e717; font-size: 16px; }
      .footer-text { font-weight: 400; font-size: 14px; color: #ffffff; }
      .page-num {
        position: absolute; bottom: 56px; right: 44px;
        font-size: 11px; color: rgba(255,255,255,0.3); z-index: 10;
      }
    </style>
</head>
<body>
    <div class="slide-container">
      <img class="bg-photo" src="{{PHOTO_URL}}" alt="">
      <div class="bg-overlay"></div>
      <img class="logo" src="{{LOGO_URL}}" alt="BKM">
      <div class="content-wrapper">
        <div class="top-section">
          <div class="section-label">{{SECTION_NUM}} — {{SECTION_NAME}}</div>
          <h1 class="headline">{{HEADLINE}}</h1>
          <p class="subtitle">{{SUBTITLE}}</p>
        </div>
        <div class="main-content">
          <div class="glass-card">
            <ul class="checklist">
              <li><i class="fas fa-check check-icon"></i><span class="check-text">{{ITEM_1}}</span></li>
              <li><i class="fas fa-check check-icon"></i><span class="check-text">{{ITEM_2}}</span></li>
              <li><i class="fas fa-check check-icon"></i><span class="check-text">{{ITEM_3}}</span></li>
              <li><i class="fas fa-check check-icon"></i><span class="check-text">{{ITEM_4}}</span></li>
              <li><i class="fas fa-check check-icon"></i><span class="check-text">{{ITEM_5}}</span></li>
            </ul>
          </div>
          <div class="status-card">
            <div class="status-badge">{{STATUS}}</div>
            <div class="status-icon"><i class="fas {{STATUS_ICON}}"></i></div>
            <div class="status-title">{{STATUS_TITLE_LINE1}}<br>{{STATUS_TITLE_LINE2}}</div>
          </div>
        </div>
        <div class="footer-bar">
          <i class="fas fa-check-circle footer-icon"></i>
          <span class="footer-text">{{FOOTER_TEXT}}</span>
        </div>
      </div>
      <span class="page-num">{{PAGE_NUM}}</span>
    </div>
</body>
</html>
```

---

## SLIDE-TYP 3: Feature-Liste mit Icon-Chips (asymmetrisch)

**Wann verwenden:** Wenn Features/Funktionen mit Icons und Beschreibungen gezeigt werden sollen. Glass-Panel links, Foto rechts sichtbar.

```html
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" rel="stylesheet">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Unbounded:wght@900&display=swap" rel="stylesheet">
    <style>
      * { margin: 0; padding: 0; box-sizing: border-box; }
      .slide-container {
        width: 1280px; min-height: 720px; position: relative;
        overflow: hidden; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
      }
      .bg-photo { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; }
      .bg-overlay {
        position: absolute; inset: 0;
        background: linear-gradient(100deg, rgba(28,75,66,0.88) 0%, rgba(28,75,66,0.75) 55%, rgba(28,75,66,0.45) 100%);
      }
      .logo { position: absolute; top: 32px; right: 44px; height: 32px; z-index: 10; object-fit: contain; }
      .content-wrapper { position: relative; z-index: 10; display: flex; flex-direction: column; height: 720px; }
      .main-area { flex: 1; display: flex; align-items: center; padding: 56px 80px; }
      .glass-panel {
        background: rgba(255,255,255,0.07); backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px); border: 1px solid rgba(255,255,255,0.12);
        border-radius: 16px; padding: 44px 48px; max-width: 580px;
      }
      .status-badge {
        display: inline-block; background: rgba(180,231,23,0.12);
        border: 1px solid rgba(180,231,23,0.35); border-radius: 20px;
        padding: 5px 14px; font-weight: 700; font-size: 10px;
        text-transform: uppercase; letter-spacing: 0.08em; color: #b4e717; margin-bottom: 16px;
      }
      .section-label {
        font-weight: 700; font-size: 11px; text-transform: uppercase;
        letter-spacing: 0.12em; color: #b4e717; margin-bottom: 10px;
      }
      .headline {
        font-family: 'Unbounded', sans-serif; font-weight: 900; font-size: 38px;
        text-transform: uppercase; color: #ffffff; line-height: 1.05; letter-spacing: -0.03em;
      }
      .subtitle { font-weight: 700; font-size: 16px; color: rgba(255,255,255,0.7); margin-top: 8px; }
      .feature-list { margin-top: 28px; display: flex; flex-direction: column; gap: 18px; }
      .feature-item { display: flex; align-items: flex-start; gap: 14px; }
      .feature-icon {
        width: 32px; height: 32px; border-radius: 8px;
        background: rgba(180,231,23,0.12); display: flex;
        align-items: center; justify-content: center; flex-shrink: 0;
      }
      .feature-icon i { color: #b4e717; font-size: 14px; }
      .feature-content { display: flex; flex-direction: column; gap: 2px; }
      .feature-title { font-weight: 700; font-size: 14px; color: #ffffff; }
      .feature-desc { font-weight: 400; font-size: 13px; color: rgba(255,255,255,0.6); line-height: 1.4; }
      .footer-bar {
        background: rgba(28,75,66,0.95); padding: 16px 80px;
        display: flex; align-items: center; gap: 12px;
      }
      .footer-icon { color: #b4e717; font-size: 16px; }
      .footer-text { font-weight: 400; font-size: 14px; color: #ffffff; }
      .page-num {
        position: absolute; bottom: 56px; right: 44px;
        font-size: 11px; color: rgba(255,255,255,0.3); z-index: 10;
      }
    </style>
</head>
<body>
    <div class="slide-container">
      <img class="bg-photo" src="{{PHOTO_URL}}" alt="">
      <div class="bg-overlay"></div>
      <img class="logo" src="{{LOGO_URL}}" alt="BKM">
      <div class="content-wrapper">
        <div class="main-area">
          <div class="glass-panel">
            <div class="status-badge">{{STATUS}}</div>
            <div class="section-label">{{SECTION_NUM}} — {{SECTION_NAME}}</div>
            <h1 class="headline">{{HEADLINE_LINE1}}<br>{{HEADLINE_LINE2}}</h1>
            <p class="subtitle">{{SUBTITLE}}</p>
            <div class="feature-list">
              <div class="feature-item">
                <div class="feature-icon"><i class="fas {{ICON_1}}"></i></div>
                <div class="feature-content">
                  <span class="feature-title">{{FEATURE_1_TITLE}}</span>
                  <span class="feature-desc">{{FEATURE_1_DESC}}</span>
                </div>
              </div>
              <div class="feature-item">
                <div class="feature-icon"><i class="fas {{ICON_2}}"></i></div>
                <div class="feature-content">
                  <span class="feature-title">{{FEATURE_2_TITLE}}</span>
                  <span class="feature-desc">{{FEATURE_2_DESC}}</span>
                </div>
              </div>
              <div class="feature-item">
                <div class="feature-icon"><i class="fas {{ICON_3}}"></i></div>
                <div class="feature-content">
                  <span class="feature-title">{{FEATURE_3_TITLE}}</span>
                  <span class="feature-desc">{{FEATURE_3_DESC}}</span>
                </div>
              </div>
              <div class="feature-item">
                <div class="feature-icon"><i class="fas {{ICON_4}}"></i></div>
                <div class="feature-content">
                  <span class="feature-title">{{FEATURE_4_TITLE}}</span>
                  <span class="feature-desc">{{FEATURE_4_DESC}}</span>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="footer-bar">
          <i class="fas fa-flask footer-icon"></i>
          <span class="footer-text">{{FOOTER_TEXT}}</span>
        </div>
      </div>
      <span class="page-num">{{PAGE_NUM}}</span>
    </div>
</body>
</html>
```

---

## SLIDE-TYP 4: Dual-Card (zwei gleichgroße Glass-Cards nebeneinander)

**Wann verwenden:** Wenn zwei Themen/Produkte/Konzepte verglichen oder nebeneinander präsentiert werden sollen.

```html
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" rel="stylesheet">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Unbounded:wght@900&display=swap" rel="stylesheet">
    <style>
      * { margin: 0; padding: 0; box-sizing: border-box; }
      .slide-container {
        width: 1280px; min-height: 720px; position: relative;
        overflow: hidden; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
      }
      .bg-photo { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; }
      .bg-overlay {
        position: absolute; inset: 0;
        background: linear-gradient(150deg, rgba(28,75,66,0.85) 0%, rgba(28,75,66,0.68) 50%, rgba(28,75,66,0.80) 100%);
      }
      .logo { position: absolute; top: 32px; right: 44px; height: 32px; z-index: 10; object-fit: contain; }
      .content-wrapper { position: relative; z-index: 10; display: flex; flex-direction: column; height: 720px; }
      .top-section { padding: 48px 80px 0 80px; }
      .section-label {
        font-weight: 700; font-size: 11px; text-transform: uppercase;
        letter-spacing: 0.12em; color: #b4e717; margin-bottom: 10px;
      }
      .headline {
        font-family: 'Unbounded', sans-serif; font-weight: 900; font-size: 36px;
        text-transform: uppercase; color: #ffffff; line-height: 1.05; letter-spacing: -0.03em;
      }
      .cards-area {
        flex: 1; display: flex; align-items: stretch;
        padding: 24px 80px 20px 80px; gap: 28px;
      }
      .glass-card {
        flex: 1; background: rgba(255,255,255,0.07); backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px); border: 1px solid rgba(255,255,255,0.12);
        border-radius: 14px; padding: 32px 32px 28px 32px;
        display: flex; flex-direction: column;
      }
      .card-status {
        display: inline-block; background: rgba(180,231,23,0.12);
        border: 1px solid rgba(180,231,23,0.35); border-radius: 20px;
        padding: 4px 14px; font-weight: 700; font-size: 10px;
        text-transform: uppercase; letter-spacing: 0.08em;
        color: #b4e717; align-self: flex-start; margin-bottom: 14px;
      }
      .card-icon-row { display: flex; align-items: center; gap: 12px; margin-bottom: 10px; }
      .card-icon-circle {
        width: 40px; height: 40px; border-radius: 50%;
        background: rgba(180,231,23,0.12); display: flex;
        align-items: center; justify-content: center; flex-shrink: 0;
      }
      .card-icon-circle i { color: #b4e717; font-size: 18px; }
      .card-title {
        font-family: 'Unbounded', sans-serif; font-weight: 900; font-size: 17px;
        text-transform: uppercase; color: #ffffff; line-height: 1.15; letter-spacing: -0.02em;
      }
      .card-subtitle {
        font-weight: 700; font-size: 13px; color: rgba(255,255,255,0.6);
        margin-top: 4px; margin-bottom: 16px;
      }
      .card-list { list-style: none; display: flex; flex-direction: column; gap: 10px; flex: 1; }
      .card-list li {
        display: flex; align-items: flex-start; gap: 10px;
        font-size: 13px; color: rgba(255,255,255,0.85); line-height: 1.4;
      }
      .card-list li i { color: #b4e717; font-size: 11px; margin-top: 3px; flex-shrink: 0; }
      .footer-bar {
        background: rgba(28,75,66,0.95); padding: 16px 80px;
        display: flex; align-items: center; gap: 12px;
      }
      .footer-icon { color: #b4e717; font-size: 16px; }
      .footer-text { font-weight: 400; font-size: 14px; color: #ffffff; }
      .page-num {
        position: absolute; bottom: 56px; right: 44px;
        font-size: 11px; color: rgba(255,255,255,0.3); z-index: 10;
      }
    </style>
</head>
<body>
    <div class="slide-container">
      <img class="bg-photo" src="{{PHOTO_URL}}" alt="">
      <div class="bg-overlay"></div>
      <img class="logo" src="{{LOGO_URL}}" alt="BKM">
      <div class="content-wrapper">
        <div class="top-section">
          <div class="section-label">{{SECTION_NUM}} — {{SECTION_NAME}}</div>
          <h1 class="headline">{{HEADLINE}}</h1>
        </div>
        <div class="cards-area">
          <!-- Card 1 -->
          <div class="glass-card">
            <div class="card-status">{{CARD1_STATUS}}</div>
            <div class="card-icon-row">
              <div class="card-icon-circle"><i class="fas {{CARD1_ICON}}"></i></div>
              <div class="card-title">{{CARD1_TITLE_LINE1}}<br>{{CARD1_TITLE_LINE2}}</div>
            </div>
            <div class="card-subtitle">{{CARD1_SUBTITLE}}</div>
            <ul class="card-list">
              <li><i class="fas fa-check"></i>{{CARD1_ITEM_1}}</li>
              <li><i class="fas fa-check"></i>{{CARD1_ITEM_2}}</li>
              <li><i class="fas fa-check"></i>{{CARD1_ITEM_3}}</li>
              <li><i class="fas fa-check"></i>{{CARD1_ITEM_4}}</li>
            </ul>
          </div>
          <!-- Card 2 -->
          <div class="glass-card">
            <div class="card-status">{{CARD2_STATUS}}</div>
            <div class="card-icon-row">
              <div class="card-icon-circle"><i class="fas {{CARD2_ICON}}"></i></div>
              <div class="card-title">{{CARD2_TITLE_LINE1}}<br>{{CARD2_TITLE_LINE2}}</div>
            </div>
            <div class="card-subtitle">{{CARD2_SUBTITLE}}</div>
            <ul class="card-list">
              <li><i class="fas fa-check"></i>{{CARD2_ITEM_1}}</li>
              <li><i class="fas fa-check"></i>{{CARD2_ITEM_2}}</li>
              <li><i class="fas fa-check"></i>{{CARD2_ITEM_3}}</li>
              <li><i class="fas fa-check"></i>{{CARD2_ITEM_4}}</li>
            </ul>
          </div>
        </div>
        <div class="footer-bar">
          <i class="fas fa-flask footer-icon"></i>
          <span class="footer-text">{{FOOTER_TEXT}}</span>
        </div>
      </div>
      <span class="page-num">{{PAGE_NUM}}</span>
    </div>
</body>
</html>
```

---

## SLIDE-TYP 5: CTA / Closing mit Prozess-Flow

**Wann verwenden:** Letzte Folie. Zentriertes Glass-Panel mit Call-to-Action, optionalem Prozess-Flow, und Closing-Statement in der Footer-Bar.

```html
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" rel="stylesheet">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Unbounded:wght@900&display=swap" rel="stylesheet">
    <style>
      * { margin: 0; padding: 0; box-sizing: border-box; }
      .slide-container {
        width: 1280px; min-height: 720px; position: relative;
        overflow: hidden; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
      }
      .bg-photo { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; }
      .bg-overlay {
        position: absolute; inset: 0;
        background: linear-gradient(160deg, rgba(28,75,66,0.82) 0%, rgba(28,75,66,0.68) 50%, rgba(28,75,66,0.80) 100%);
      }
      .logo { position: absolute; top: 32px; right: 44px; height: 32px; z-index: 10; object-fit: contain; }
      .content-wrapper { position: relative; z-index: 10; display: flex; flex-direction: column; height: 720px; }
      .main-area {
        flex: 1; display: flex; align-items: center; justify-content: center; padding: 40px 80px;
      }
      .glass-panel {
        background: rgba(255,255,255,0.07); backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px); border: 1px solid rgba(255,255,255,0.12);
        border-radius: 16px; padding: 44px 56px; max-width: 900px; width: 100%; text-align: center;
      }
      .cta-icon { font-size: 36px; color: #b4e717; margin-bottom: 0; }
      .headline {
        font-family: 'Unbounded', sans-serif; font-weight: 900; font-size: 42px;
        text-transform: uppercase; color: #ffffff; line-height: 1.05;
        letter-spacing: -0.03em; margin-top: 14px;
      }
      .subtitle {
        font-weight: 700; font-size: 17px; color: #b4e717; margin-top: 10px;
        text-transform: uppercase; letter-spacing: 0.04em;
      }
      .body-text {
        font-weight: 400; font-size: 15px; color: rgba(255,255,255,0.7);
        line-height: 1.6; margin-top: 14px; max-width: 600px; margin-left: auto; margin-right: auto;
      }
      .divider { width: 60px; height: 2px; background: rgba(180,231,23,0.4); margin: 28px auto 0 auto; }
      .process-flow {
        display: flex; align-items: center; justify-content: center; gap: 12px; margin-top: 28px;
      }
      .process-step { display: flex; flex-direction: column; align-items: center; gap: 8px; width: 150px; }
      .step-circle {
        width: 48px; height: 48px; border-radius: 50%;
        background: rgba(180,231,23,0.12); border: 1px solid rgba(180,231,23,0.3);
        display: flex; align-items: center; justify-content: center;
      }
      .step-circle i { color: #b4e717; font-size: 18px; }
      .step-label {
        font-weight: 700; font-size: 11px; color: #ffffff;
        text-transform: uppercase; letter-spacing: 0.04em; text-align: center; line-height: 1.3;
      }
      .process-arrow { color: rgba(180,231,23,0.5); font-size: 18px; margin-top: -20px; }
      .footer-bar {
        background: rgba(28,75,66,0.95); padding: 16px 80px;
        display: flex; align-items: center; gap: 10px;
      }
      .footer-chevrons { color: #b4e717; font-size: 18px; font-weight: 900; letter-spacing: -2px; }
      .footer-text {
        font-weight: 400; font-size: 13px; color: rgba(255,255,255,0.85); line-height: 1.5;
      }
      .footer-text strong { color: #b4e717; font-weight: 700; }
      .footer-logo { margin-left: auto; height: 24px; object-fit: contain; }
      .page-num {
        position: absolute; bottom: 56px; right: 44px;
        font-size: 11px; color: rgba(255,255,255,0.3); z-index: 10;
      }
    </style>
</head>
<body>
    <div class="slide-container">
      <img class="bg-photo" src="{{PHOTO_URL}}" alt="">
      <div class="bg-overlay"></div>
      <img class="logo" src="{{LOGO_URL}}" alt="BKM">
      <div class="content-wrapper">
        <div class="main-area">
          <div class="glass-panel">
            <div class="cta-icon"><i class="fas {{CTA_ICON}}"></i></div>
            <h1 class="headline">{{HEADLINE_LINE1}}<br>{{HEADLINE_LINE2}}</h1>
            <p class="subtitle">{{SUBTITLE}}</p>
            <p class="body-text">{{BODY_TEXT}}</p>
            <div class="divider"></div>
            <div class="process-flow">
              <div class="process-step">
                <div class="step-circle"><i class="fas {{STEP1_ICON}}"></i></div>
                <span class="step-label">{{STEP1_LABEL}}</span>
              </div>
              <i class="fas fa-arrow-right process-arrow"></i>
              <div class="process-step">
                <div class="step-circle"><i class="fas {{STEP2_ICON}}"></i></div>
                <span class="step-label">{{STEP2_LABEL}}</span>
              </div>
              <i class="fas fa-arrow-right process-arrow"></i>
              <div class="process-step">
                <div class="step-circle"><i class="fas {{STEP3_ICON}}"></i></div>
                <span class="step-label">{{STEP3_LABEL}}</span>
              </div>
              <i class="fas fa-arrow-right process-arrow"></i>
              <div class="process-step">
                <div class="step-circle"><i class="fas {{STEP4_ICON}}"></i></div>
                <span class="step-label">{{STEP4_LABEL}}</span>
              </div>
            </div>
          </div>
        </div>
        <div class="footer-bar">
          <span class="footer-chevrons">&raquo;</span>
          <span class="footer-text">{{CLOSING_STATEMENT}}</span>
          <img class="footer-logo" src="{{LOGO_URL}}" alt="BKM">
        </div>
      </div>
      <span class="page-num">{{PAGE_NUM}}</span>
    </div>
</body>
</html>
```

---

## Platzhalter-Referenz

| Platzhalter | Beschreibung |
|-------------|-------------|
| `{{PHOTO_URL}}` | CDN-URL des generierten Hintergrund-Fotos |
| `{{LOGO_URL}}` | CDN-URL des BKM Logos (kontextabhängig) |
| `{{KEYVISUAL_URL}}` | CDN-URL des Keyvisuals (nur Titel-Slide) |
| `{{LABEL}}` | Oberer Label-Text (z.B. "Ein Blick hinter die Kulissen") |
| `{{HEADLINE_LINE1/2}}` | Headline-Zeilen |
| `{{SUBTITLE}}` | Untertitel-Text |
| `{{TAGLINE}}` | Tagline unter dem Subtitle |
| `{{META_TEXT}}` | Meta-Info (z.B. "BKM Mannesmann AG • 2026") |
| `{{SECTION_NUM}}` | Sektionsnummer (z.B. "01") |
| `{{SECTION_NAME}}` | Sektionsname (z.B. "Vertrauen") |
| `{{ITEM_N}}` | Checklist-Item Text |
| `{{STATUS}}` | Status-Badge Text (z.B. "Beta / In Test") |
| `{{STATUS_ICON}}` | Font Awesome Icon-Klasse (z.B. "fa-handshake") |
| `{{FEATURE_N_TITLE/DESC}}` | Feature Titel und Beschreibung |
| `{{ICON_N}}` | Font Awesome Icon-Klasse für Features |
| `{{CARD1/2_...}}` | Dual-Card Inhalte |
| `{{STEP1-4_ICON/LABEL}}` | Prozess-Flow Schritte |
| `{{FOOTER_TEXT}}` | Footer-Bar Text |
| `{{CLOSING_STATEMENT}}` | Abschluss-Statement (mit `<strong>` für Lime-Highlights) |
| `{{PAGE_NUM}}` | Seitenzahl (z.B. "02") |
| `{{TREND_N/TREND_N_SUB}}` | Trend-Name und Untertitel |
| `{{CTA_ICON}}` | Font Awesome Icon für CTA (z.B. "fa-users") |

---

## Regeln für die Verwendung

1. **KOPIEREN, NICHT INTERPRETIEREN** — Wähle den passenden Slide-Typ und kopiere das komplette HTML
2. **Nur Platzhalter ersetzen** — Keine CSS-Werte ändern, keine neuen Klassen erfinden
3. **Checklist-Items anpassen** — Mehr oder weniger `<li>` Elemente sind erlaubt (3–6 Items)
4. **Feature-Items anpassen** — 3–5 Feature-Items sind erlaubt
5. **Prozess-Schritte anpassen** — 3–5 Schritte sind erlaubt
6. **Trends-Bar ist optional** — Kann bei Titel-Slides weggelassen werden
7. **Status-Card ist optional** — Kann bei Checklist-Slides weggelassen werden (dann `flex: 1` auf glass-card reicht)
8. **Footer-Bar ist PFLICHT** — Jede Content-Slide (Typ 2–5) MUSS eine Footer-Bar haben
