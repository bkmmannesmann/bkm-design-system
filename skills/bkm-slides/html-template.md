# BKM Slides — HTML Templates (v3)

> Vollständige, kopierbare HTML-Templates für alle Slide-Typen. **Nicht interpretieren — 1:1 als Startpunkt verwenden** und nur Inhalte (Texte, Bilder, Icons) austauschen. Jede Slide ist eine eigenständige HTML-Datei.

---

## Pflicht-Abhängigkeiten (in jedem Slide-Head)

```html
<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" rel="stylesheet">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Unbounded:wght@900&display=swap" rel="stylesheet">
```

---

## Template 1: Titel-Slide — BKM AG (Glasmorphismus)

Vollständiges, kopierbares Template. Ersetze nur: Foto-URL, Logo-URL, Keyvisual-URL, Texte.

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
      .glass-meta {
        margin-top: 28px; display: flex; align-items: center; gap: 10px;
      }
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
      <!-- Optional: Trends-Bar am unteren Rand -->
      <div class="trends-bar">
        <div class="trend-item">
          <i class="fas fa-handshake trend-icon"></i>
          <div><div class="trend-text">{{TREND_1}}</div><div class="trend-sub">{{TREND_1_SUB}}</div></div>
        </div>
        <!-- Weitere Trend-Items nach Bedarf -->
      </div>
    </div>
</body>
</html>
```

---

## Template 2: Titel-Slide — Fachbetrieb (Glasmorphismus)

Gleiche Struktur, andere Farben. Ersetze nur: Foto-URL, Logo-URL, Keyvisual-URL, Texte.

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
        background: linear-gradient(140deg, rgba(246,245,242,0.88) 0%, rgba(246,245,242,0.75) 50%, rgba(246,245,242,0.85) 100%);
      }
      .accent-line {
        position: absolute; left: 7%; top: 18%; width: 4px; height: 60%;
        background: #4daf46; border-radius: 2px; z-index: 10;
      }
      .logo {
        position: absolute; top: 36px; right: 48px; height: 38px;
        z-index: 10; object-fit: contain;
      }
      .keyvisual {
        position: absolute; top: 0; right: 0; height: 100%; width: 22%;
        object-fit: cover; object-position: left center; opacity: 0.15; z-index: 5;
      }
      .glass-card {
        position: absolute; top: 50%; left: 10%; transform: translateY(-50%);
        z-index: 10; max-width: 600px;
        background: rgba(255,255,255,0.55); backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px); border: 1px solid rgba(255,255,255,0.7);
        border-radius: 16px; padding: 52px 48px;
      }
      .glass-card::before {
        content: ''; position: absolute; inset: 0; border-radius: 16px;
        background: linear-gradient(160deg, rgba(255,255,255,0.3) 0%, transparent 40%);
        pointer-events: none;
      }
      .glass-label {
        font-weight: 700; font-size: 11px; text-transform: uppercase;
        letter-spacing: 0.12em; color: #4daf46; margin-bottom: 16px;
      }
      .glass-headline {
        font-family: 'Unbounded', sans-serif; font-weight: 900; font-size: 56px;
        text-transform: uppercase; color: #1c4b42; line-height: 1.0; letter-spacing: -0.04em;
      }
      .glass-subtitle {
        font-weight: 400; font-size: 17px; color: #494949;
        line-height: 1.6; margin-top: 18px; max-width: 90%;
      }
      .glass-tagline {
        font-weight: 700; font-size: 13px; color: rgba(73,73,73,0.6); margin-top: 12px;
      }
      .glass-meta {
        margin-top: 28px; display: flex; align-items: center; gap: 10px;
      }
      .meta-dot { width: 8px; height: 8px; border-radius: 50%; background: #4daf46; }
      .meta-text {
        font-weight: 700; font-size: 11px; text-transform: uppercase;
        letter-spacing: 0.06em; color: #287d4b;
      }
      .trends-bar {
        position: absolute; bottom: 0; left: 0; right: 0;
        background: rgba(40,125,75,0.95); backdrop-filter: blur(10px);
        padding: 16px 48px; display: flex; align-items: center; gap: 40px; z-index: 10;
      }
      .trend-item { display: flex; align-items: center; gap: 10px; }
      .trend-icon { color: #b4e717; font-size: 16px; }
      .trend-text {
        font-weight: 700; font-size: 12px; color: #ffffff;
        text-transform: uppercase; letter-spacing: 0.03em;
      }
      .trend-sub {
        font-weight: 400; font-size: 11px; color: rgba(255,255,255,0.7);
        text-transform: none; letter-spacing: 0;
      }
    </style>
</head>
<body>
    <div class="slide-container">
      <img class="bg-photo" src="{{PHOTO_URL}}" alt="">
      <div class="bg-overlay"></div>
      <img class="keyvisual" src="{{KEYVISUAL_ON_LIGHT_URL}}" alt="">
      <div class="accent-line"></div>
      <img class="logo" src="{{LOGO_STONEGREY_PUREGREEN_URL}}" alt="BKM Mannesmann">
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
      </div>
    </div>
</body>
</html>
```

---

## Template 3: Content-Slide mit Checklist + Status-Card — BKM AG

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
      .check-text { font-weight: 400; font-size: 15px; color: rgba(255,255,255,0.85); line-height: 1.4; }
      .status-card {
        background: rgba(180,231,23,0.06); backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px); border: 1px solid rgba(180,231,23,0.15);
        border-radius: 14px; padding: 32px 36px; width: 280px; text-align: center;
      }
      .status-badge {
        display: inline-block; background: rgba(180,231,23,0.1);
        border: 1px solid rgba(180,231,23,0.25); border-radius: 20px;
        padding: 5px 14px; font-weight: 700; font-size: 10px;
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
            <div class="status-title">{{STATUS_TITLE}}</div>
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

## Template 4: Feature-Slide mit asymmetrischem Glass-Panel — BKM AG

```html
<!-- Gleiche Head-Struktur wie Template 3, nur der Body unterscheidet sich -->
<!-- Overlay: asymmetrisch — links stark, rechts Foto sichtbar -->
<!-- bg-overlay: linear-gradient(100deg, rgba(28,75,66,0.88) 0%, rgba(28,75,66,0.75) 55%, rgba(28,75,66,0.45) 100%) -->
<!-- glass-panel: max-width 580px, padding 44px 48px -->
<!-- Feature-Items: 32x32 icon-chips mit rgba(180,231,23,0.12) background -->
<!-- Siehe STYLE_PRESETS.md für exakte Token -->
```

## Template 5: Dual-Card-Slide — BKM AG

```html
<!-- Gleiche Head-Struktur wie Template 3 -->
<!-- Overlay: 150deg, rgba(28,75,66,0.85/0.68/0.80) -->
<!-- cards-area: flex, padding 24px 80px 20px 80px, gap 28px -->
<!-- Jede glass-card: flex: 1, padding 32px 32px 28px 32px -->
<!-- Card-Titel: Unbounded 900, 17px, uppercase -->
<!-- Siehe STYLE_PRESETS.md für exakte Token -->
```

## Template 6: CTA/Closing-Slide mit Prozess-Flow — BKM AG

```html
<!-- Gleiche Head-Struktur wie Template 3 -->
<!-- glass-panel: zentriert, max-width 900px, padding 44px 56px -->
<!-- Process-Flow: flex, gap 12px, step-circles 48x48 -->
<!-- Footer-Bar: mit Chevrons (») und Footer-Logo -->
<!-- Siehe STYLE_PRESETS.md für exakte Token -->
```

---

## Fachbetrieb-Varianten

Für alle Content-Templates (3–6) gelten folgende Farbänderungen gegenüber BKM AG:

| Element | BKM AG | Fachbetrieb |
|---------|--------|-------------|
| Overlay | `rgba(28,75,66, ...)` | `rgba(246,245,242, ...)` |
| Glass-Card bg | `rgba(255,255,255,0.07)` | `rgba(255,255,255,0.55)` |
| Glass-Card border | `rgba(255,255,255,0.12)` | `rgba(255,255,255,0.7)` |
| Headlines | `#ffffff` | `#1c4b42` |
| Body-Text | `rgba(255,255,255,0.85)` | `#494949` |
| Muted Text | `rgba(255,255,255,0.7)` | `rgba(73,73,73,0.7)` |
| Section-Label | `#b4e717` | `#4daf46` |
| Checkmarks | `#b4e717` | `#4daf46` |
| Status-Badge | Lime-getönt | Pure Green-getönt |
| Icon-Circles bg | `rgba(180,231,23,0.12)` | `rgba(77,175,70,0.1)` |
| Icon-Circles color | `#b4e717` | `#4daf46` |
| Footer-Bar bg | `rgba(28,75,66,0.95)` | `rgba(40,125,75,0.95)` |
| Footer-Icon | `#b4e717` | `#b4e717` (bleibt Lime!) |
| Page-Num | `rgba(255,255,255,0.3)` | `rgba(73,73,73,0.3)` |
| Logo | `bkm-logo-white-puregreen` | `bkm-logo-stonegrey-puregreen` |
| Keyvisual | `keyvisual-on-dark.svg`, opacity 0.18 | `keyvisual-on-light.svg`, opacity 0.15 |

---

## Platzhalter-Referenz

| Platzhalter | Beschreibung |
|-------------|-------------|
| `{{PHOTO_URL}}` | CDN-URL des generierten Hintergrund-Fotos |
| `{{LOGO_URL}}` | CDN-URL des BKM Logos (kontextabhängig) |
| `{{KEYVISUAL_URL}}` | CDN-URL des Keyvisuals (kontextabhängig) |
| `{{LABEL}}` | Oberer Label-Text (z.B. "Ein Blick hinter die Kulissen") |
| `{{HEADLINE_LINE1}}` | Erste Zeile der Headline |
| `{{HEADLINE_LINE2}}` | Zweite Zeile der Headline |
| `{{SUBTITLE}}` | Untertitel-Text |
| `{{TAGLINE}}` | Tagline unter dem Subtitle |
| `{{META_TEXT}}` | Meta-Info (z.B. "BKM Mannesmann AG • 2026") |
| `{{SECTION_NUM}}` | Sektionsnummer (z.B. "01") |
| `{{SECTION_NAME}}` | Sektionsname (z.B. "Vertrauen") |
| `{{ITEM_N}}` | Checklist-Item Text |
| `{{STATUS}}` | Status-Badge Text (z.B. "Beta / In Test") |
| `{{STATUS_ICON}}` | Font Awesome Icon-Klasse (z.B. "fa-handshake") |
| `{{STATUS_TITLE}}` | Status-Card Titel |
| `{{FOOTER_TEXT}}` | Footer-Bar Text |
| `{{PAGE_NUM}}` | Seitenzahl (z.B. "02") |
| `{{TREND_N}}` | Trend-Name |
| `{{TREND_N_SUB}}` | Trend-Untertitel |
