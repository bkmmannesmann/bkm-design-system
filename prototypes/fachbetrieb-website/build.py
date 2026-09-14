import re, html, pathlib

DOC = pathlib.Path('Fachbetriebs-Websites_Baukasten_v1.md').read_text(encoding='utf-8')
OUT = pathlib.Path('.')

V = {
 'BETRIEB':'BKM Abdichtungstechnik GmbH','BETRIEB_KURZ':'BKM Abdichtungstechnik','ORT':'Düsseldorf',
 'PLZ':'40789','ADRESSE':'Rheinpromenade 13','SITZ_ORT':'Monheim am Rhein','REGION':'im Rheinland',
 'EINSATZGEBIET':'Düsseldorf, Kreis Mettmann (Monheim, Langenfeld, Hilden, Erkrath, Mettmann, Ratingen, Haan, Velbert) und Umgebung',
 'EINSATZGEBIET_KURZ':'in Düsseldorf und im Kreis Mettmann','TELEFON':'0211 90986205','TELEFON_LINK':'+4921190986205',
 'EMAIL':'info@bkm-duesseldorf.de','ANSPRECHPARTNER':'Philipp Pannen','FUNKTION':'Dein Ansprechpartner für die Schadensaufnahme',
 'JAHRE_PARTNER':'5',
 'BAUSUBSTANZ_SATZ':'In Düsseldorf und im Kreis Mettmann stehen Gründerzeithäuser, Nachkriegsbauten der 50er- und 60er-Jahre und Einfamilienhäuser aus den 70ern dicht beieinander – viele davon ohne Sperrschicht gegen aufsteigende Feuchtigkeit, und in Rheinnähe mit wechselndem Grundwasserstand.',
 'VORSTELLUNG':'Unser Betrieb sitzt in Monheim am Rhein und ist seit fünf Jahren zertifizierter BKM-Fachbetrieb für Düsseldorf und den Kreis Mettmann. Uns ist aufgefallen, wie viele Eigentümer mit widersprüchlichen Empfehlungen alleingelassen werden. Deshalb beginnt bei uns jede Sanierung mit einem Termin vor Ort – und mit der Frage, woher die Feuchtigkeit kommt.',
}
def sub(t):
    for k,v in V.items(): t=t.replace('['+k+']',v)
    return t

PAGES = [
 ('horizontalsperre','Horizontalsperre','F.1'),
 ('flaechensperre','Flächensperre','F.2'),
 ('innenabdichtung','Innenabdichtung','F.3'),
 ('wand-boden-anschluss','Wand-Boden-Anschluss','F.4'),
 ('rissverpressung','Rissverpressung','F.5'),
 ('sanierputz','Sanierputz','F.6'),
]
SLUG_BY_NAME = {n:s for s,n,_ in PAGES}
TITLES = {
 'horizontalsperre':('Horizontalsperre in Düsseldorf – nachträglich, ohne Aufgraben','Feuchte Wand von unten? Nachträgliche Horizontalsperre im Injektionsverfahren in Düsseldorf und im Rheinland. Kostenlose Diagnose vor Ort.'),
 'flaechensperre':('Flächensperre in Düsseldorf – Mauerwerk in der Tiefe abdichten','Wand von der Seite feucht und nicht freilegbar? Flächensperre durch Rasterinjektion in Düsseldorf. Wann sie passt, wann nicht.'),
 'innenabdichtung':('Kellerabdichtung von innen in Düsseldorf – Innenabdichtung','Kellerwand großflächig feucht? Innenabdichtung nach WTA in Düsseldorf und im Rheinland – ohne Baugrube, auch bei Reihenhäusern.'),
 'wand-boden-anschluss':('Wasser im Keller nach Regen? Wand-Boden-Anschluss in Düsseldorf','Pfützen am Übergang von Wand und Boden: Abdichtung der Aufstandsfuge von innen in Düsseldorf. Kostenlose Diagnose.'),
 'rissverpressung':('Rissverpressung in Düsseldorf – Risse und Fugen dauerhaft dicht','Wasser tritt aus einem Riss? Zweistufige Rissverpressung in Düsseldorf und im Rheinland: erst stoppen, dann dauerhaft schließen.'),
 'sanierputz':('Sanierputz in Düsseldorf – wenn Putz trotz trockener Wand abplatzt','Salzausblühungen und abplatzender Putz? Sanierputz nach WTA in Düsseldorf. Was er leistet – und was nicht.'),
}
SYMPTOM = {
 'horizontalsperre':'Die Wand ist unten feucht, der Fleck wird nach oben schwächer, weiße Ränder.',
 'innenabdichtung':'Die Kellerwand ist großflächig feucht, nach Regen deutlicher, muffiger Geruch.',
 'flaechensperre':'Die Wand ist von der Seite feucht, aber von außen nicht erreichbar.',
 'wand-boden-anschluss':'Nach Regen steht Wasser dort, wo Wand und Boden zusammentreffen.',
 'rissverpressung':'Wasser tritt an einem Riss, einer Fuge oder einem Rohr aus.',
 'sanierputz':'Putz und Farbe platzen ab, weiße Ablagerungen kommen wieder – obwohl die Wand trocken ist.',
}
TEASER = {
 'horizontalsperre':'Neue Sperrschicht per Injektion, ohne Aufgraben.',
 'innenabdichtung':'Abdichtung von innen nach WTA, auch bei Reihenhäusern.',
 'flaechensperre':'Mauerwerk in der Tiefe wasserabweisend machen.',
 'wand-boden-anschluss':'Fuge verpressen, Dichtkehle einbauen.',
 'rissverpressung':'Erst stoppen, dann dauerhaft schließen.',
 'sanierputz':'Salze aufnehmen, Oberfläche trocken halten.',
}
ORDER_HOME = ['horizontalsperre','innenabdichtung','flaechensperre','wand-boden-anschluss','rissverpressung','sanierputz']

# ---------- icons (schematic wall sections) ----------
BRICK = '<rect x="10" y="8" width="44" height="48" rx="2" fill="none" stroke="currentColor" stroke-width="2"/>' \
        '<path d="M10 20h44M10 32h44M10 44h44M32 8v12M21 20v12M43 20v12M32 32v12M21 44v12M43 44v12" stroke="currentColor" stroke-width="1" opacity=".45"/>'
ICONS = {
 'horizontalsperre': BRICK + '<path d="M8 40h48" stroke="currentColor" stroke-width="4" stroke-dasharray="5 3"/><path d="M32 60V46M27 51l5-5 5 5" fill="none" stroke="currentColor" stroke-width="2.5"/>',
 'flaechensperre': BRICK + ''.join(f'<circle cx="{x}" cy="{y}" r="2.6" fill="currentColor"/>' for y in (18,30,42) for x in ((16,26,36,46) if y!=30 else (21,31,41))),
 'innenabdichtung': BRICK + '<rect x="50" y="6" width="6" height="52" fill="currentColor"/><path d="M2 22h8M2 32h8M2 42h8" stroke="currentColor" stroke-width="2.5"/><path d="M6 18l4 4-4 4M6 28l4 4-4 4M6 38l4 4-4 4" fill="none" stroke="currentColor" stroke-width="2"/>',
 'wand-boden-anschluss': '<path d="M14 6v34H58" fill="none" stroke="currentColor" stroke-width="2"/><path d="M8 40h50v16H8z" fill="none" stroke="currentColor" stroke-width="2"/><path d="M14 20h12M14 30h12M20 6v14M20 30v10" stroke="currentColor" stroke-width="1" opacity=".45"/><path d="M26 40a12 12 0 0 1 12-12h-12z" fill="currentColor"/><path d="M4 48h6M4 36l6 4" stroke="currentColor" stroke-width="2.5"/>',
 'rissverpressung': BRICK + '<path d="M40 8l-6 12 6 10-8 12 6 14" fill="none" stroke="currentColor" stroke-width="3"/><circle cx="24" cy="18" r="3" fill="currentColor"/><circle cx="22" cy="34" r="3" fill="currentColor"/><circle cx="26" cy="50" r="3" fill="currentColor"/><path d="M27 19l6 1M25 34l6 0M29 49l4-2" stroke="currentColor" stroke-width="1.5"/>',
 'sanierputz': BRICK + '<rect x="44" y="6" width="14" height="52" fill="currentColor" opacity=".18"/><rect x="44" y="6" width="14" height="52" fill="none" stroke="currentColor" stroke-width="2"/>' + ''.join(f'<circle cx="{x}" cy="{y}" r="1.6" fill="currentColor"/>' for (x,y) in ((48,14),(53,20),(49,28),(54,36),(48,44),(53,52))),
}
def icon(slug, cls='ico'):
    return f'<svg class="{cls}" viewBox="0 0 64 64" aria-hidden="true">{ICONS[slug]}</svg>'

# ---------- markdown block parser ----------
def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'\*(.+?)\*', r'<em>\1</em>', t)
    return t

def section(label):
    m = re.search(r'^## '+re.escape(label)+r' .*?$(.*?)(?=^## )', DOC, re.S|re.M)
    return m.group(1)

def blocks(text):
    parts = re.split(r'^### Block (\d) – (.+)$', text, flags=re.M)
    out = []
    for i in range(1, len(parts), 3):
        out.append((int(parts[i]), parts[i+1].strip(), parts[i+2].strip()))
    return out

def render_body(body):
    body = sub(body)
    out = []; ul=[]; ol=[]; faq=[]
    def flush():
        nonlocal ul, ol, faq
        if ul: out.append('<ul>'+''.join(f'<li>{inline(x)}</li>' for x in ul)+'</ul>'); ul=[]
        if ol: out.append('<ol>'+''.join(f'<li>{inline(x)}</li>' for x in ol)+'</ol>'); ol=[]
        if faq:
            out.append('<div class="faq">'+''.join(f'<details><summary>{inline(q)}</summary><p>{inline(a)}</p></details>' for q,a in faq)+'</div>'); faq=[]
    for line in body.split('\n'):
        s=line.strip()
        if not s: continue
        if s.startswith('- '): ul.append(s[2:]); continue
        m=re.match(r'^\d+\. (.*)$', s)
        if m: ol.append(m.group(1)); continue
        m=re.match(r'^\*(.+?\?)\* – (.*)$', s)
        if m: faq.append((m.group(1), m.group(2))); continue
        flush()
        if s.startswith('Verwandte Leistungen:'):
            names=re.findall(r'→ ([^·]+)', s)
            links=''.join(f'<a href="{SLUG_BY_NAME[n.strip()]}.html">{n.strip()} →</a>' for n in names)
            out.append(f'<div class="related"><span style="align-self:center;color:var(--muted)">Verwandte Leistungen:</span>{links}</div>'); continue
        if s.startswith('**H1:**') or s.startswith('**Button:**'): continue
        if s.startswith('**Text:**'): out.append(f'<p class="lead">{inline(s[9:].strip())}</p>'); continue
        if s.startswith('Das sind Hinweise') or s.startswith('Hinweise, keine Diagnose'):
            out.append(f'<p class="note">{inline(s)}</p>'); continue
        out.append(f'<p>{inline(s)}</p>')
    flush()
    return '\n'.join(out)

# ---------- shared chrome ----------
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700&family=Source+Sans+3:ital,wght@0,400;0,600;0,700;1,400&display=swap">'

def header(active=''):
    menu=''.join(f'<a href="{s}.html">{n}</a>' for s,n,_ in PAGES)
    return f'''<div class="proto"><b>Prototyp</b> · bkm-duesseldorf.de · Texte Baukasten v1.1 · Bilder sind Platzhalter · Vorlage für den Aufbau in Astra + Elementor</div>
<header class="hdr"><div class="wrap">
 <a class="brand" href="index.html"><span class="mark">BKM</span><span><span class="t1">BKM Abdichtungstechnik</span><br><span class="t2">Zertifizierter BKM-Fachbetrieb · Düsseldorf</span></span></a>
 <nav class="nav" aria-label="Hauptmenü">
  <div class="dd"><a href="leistungen.html">Leistungen</a><div class="menu">{menu}</div></div>
  <a href="index.html#ablauf">Ablauf</a><a href="index.html#faq">Häufige Fragen</a><a href="diagnose.html">Kontakt</a>
 </nav>
 <a class="phone" href="tel:{V['TELEFON_LINK']}">{V['TELEFON']}</a>
 <a class="btn btn-primary" href="diagnose.html">Kostenlose Diagnose</a>
</div></header>'''

def footer():
    links=''.join(f'<li><a href="{s}.html">{n}</a></li>' for s,n,_ in PAGES)
    return f'''<footer class="ftr"><div class="wrap">
 <div><h4>{V['BETRIEB']}</h4><p>{V['ADRESSE']}<br>{V['PLZ']} {V['SITZ_ORT']}</p><p style="margin-top:10px"><a href="tel:{V['TELEFON_LINK']}">{V['TELEFON']}</a><br><a href="mailto:{V['EMAIL']}">{V['EMAIL']}</a></p></div>
 <div><h4>Leistungen</h4><ul>{links}</ul></div>
 <div><h4>Einsatzgebiet</h4><p>{V['EINSATZGEBIET']}</p><p style="margin-top:12px"><a href="https://www.bkm-mannesmann.de/">Zertifizierter BKM-Fachbetrieb – mehr über das System →</a></p></div>
 <div class="bottom"><span class="seal"><b>BKM</b> Systempartner</span><a href="#">Impressum</a><a href="#">Datenschutz</a><span>Abgestimmte Sanierungssysteme von BKM Mannesmann AG</span></div>
</div></footer>'''

def page(title, desc, body, full=True):
    head=f'<title>{html.escape(title)}</title><meta name="description" content="{html.escape(desc)}">{FONTS}<link rel="stylesheet" href="style.css">'
    if full:
        return f'<!doctype html><html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">{head}</head><body>{body}</body></html>'
    return head+body

def closing():
    return f'''<section class="closing sec"><div class="wrap">
 <div class="stack"><h2>Du musst heute noch nicht wissen, welche Sanierung Du brauchst.</h2>
 <p class="lead">Der erste Schritt ist, die Ursache zu verstehen. Beim Termin in {V['ORT']} oder {V['REGION']} sehen wir uns Deine Wand an, messen die Feuchtigkeit und erklären Dir, was wir sehen – in Ruhe und in verständlichen Worten. Manchmal ist das Ergebnis eine Sanierung. Manchmal eine Beobachtung über einige Wochen oder ein Hinweis zum Lüften. Was es nicht ist: ein Verkaufsgespräch.</p>
 <div class="ctas"><a class="btn btn-primary" href="diagnose.html">Kostenlose Diagnose anfragen</a><a class="btn btn-secondary" href="tel:{V['TELEFON_LINK']}">{V['TELEFON']} anrufen</a></div></div>
 <div class="contact"><b>{V['BETRIEB']}</b><span>{V['ADRESSE']}, {V['PLZ']} {V['SITZ_ORT']}</span><a href="tel:{V['TELEFON_LINK']}">{V['TELEFON']}</a><a href="mailto:{V['EMAIL']}">{V['EMAIL']}</a><span>Einsatzgebiet: {V['EINSATZGEBIET_KURZ']}</span></div>
</div></section>'''

# ---------- service pages ----------
for slug, name, label in PAGES:
    sec = section(label)
    bl = blocks(sec)
    h1 = sub(re.search(r'\*\*H1:\*\* (.+)', bl[0][2]).group(1))
    lead = sub(re.search(r'\*\*Text:\*\* (.+)', bl[0][2]).group(1))
    body = header() + f'''<div class="wrap crumb"><a href="index.html">Start</a> › <a href="leistungen.html">Leistungen</a> › {name}</div>
<section class="svc-hero sec-paper" style="padding-block:24px 56px"><div class="wrap">
 <div class="stack">{icon(slug)}<span class="eyebrow">{name} · {V['EINSATZGEBIET_KURZ'][0].upper()+V['EINSATZGEBIET_KURZ'][1:]}</span><h1>{html.escape(h1)}</h1><p class="lead">{inline(lead)}</p>
 <div><a class="btn btn-primary" href="diagnose.html">Kostenlose Diagnose in {V['ORT']}</a></div></div>
 <div class="ph"><span>Bild: Schadensbild {name}</span></div>
</div></section>'''
    for n, title, content in bl[1:]:
        body += f'<section class="block"><div class="wrap"><h2>{html.escape(title)}</h2><div class="body">{render_body(content)}</div></div></section>'
    body += closing() + footer()
    t, d = TITLES[slug]
    (OUT/f'{slug}.html').write_text(page(t, d, body), encoding='utf-8')

# ---------- overview ----------
cards=''.join(f'<a href="{s}.html">{icon(s)}<div><span class="sym">{SYMPTOM[s]}</span><b>{n}</b><span>{TEASER[s]}</span></div></a>' for s in ORDER_HOME for (ss,n,_) in PAGES if ss==s)
ov = header() + f'''<section class="sec-paper sec"><div class="wrap sec-head"><span class="eyebrow">Leistungen</span><h1>Leistungen gegen Feuchtigkeit in {V['ORT']} und {V['REGION']}</h1>
<p class="lead">Feuchtigkeit hat mehr als einen Weg ins Haus: von unten, von der Seite, mit Druck, durch Schwachstellen oder aus der Raumluft. Jede Leistung auf dieser Seite unterbricht einen dieser Wege. Welche zu Deinem Haus passt, zeigt der Befund vor Ort – nicht die Ferndiagnose. Wenn Du Dein Schadensbild wiedererkennst, findest Du hier den Einstieg.</p></div>
<div class="wrap"><div class="ov">{cards}</div>
<p class="note" style="margin-top:26px;background:var(--clay-soft);border-left:4px solid var(--clay);padding:12px 16px;max-width:var(--measure)"><strong>Was Du wissen solltest:</strong> In vielen Häusern kommen mehrere Wege zusammen – eine Wand, in der Feuchtigkeit aufsteigt, kann zugleich seitlich Erdfeuchte aufnehmen. Deshalb kombinieren wir Leistungen, wenn der Befund es verlangt, und lassen weg, was nicht nötig ist. Beides steht im Angebot.</p>
<p style="margin-top:18px;color:var(--ink-2);max-width:var(--measure)">Weitere Themen rund um Feuchtigkeitsschutz erklärt BKM Mannesmann zentral im <a href="https://www.bkm-mannesmann.de/">Ratgeber</a>.</p></div></section>
''' + closing() + footer()
(OUT/'leistungen.html').write_text(page(f'Leistungen gegen Feuchtigkeit in {V["ORT"]} – {V["BETRIEB_KURZ"]}','Horizontalsperre, Innenabdichtung, Rissverpressung, Sanierputz und mehr – welche Lösung zu welchem Schaden passt. Fachbetrieb in Düsseldorf.', ov), encoding='utf-8')

# ---------- form ----------
def form(idp):
    return f'''<form class="form" onsubmit="event.preventDefault();this.querySelector('.done').hidden=false;">
 <div class="row"><label>Name*<input id="{idp}-name" required autocomplete="name"></label><label>E-Mail*<input id="{idp}-email" type="email" required autocomplete="email"></label></div>
 <div class="row"><label>Telefon*<input id="{idp}-tel" type="tel" required autocomplete="tel"></label><label>Postleitzahl*<input id="{idp}-plz" inputmode="numeric" pattern="[0-9]{{5}}" required></label></div>
 <label>Was hast Du beobachtet? (optional)<textarea id="{idp}-msg" placeholder="Seit wann, wo, bei welchem Wetter …"></textarea></label>
 <label class="consent"><input id="{idp}-consent" type="checkbox" required><span>Ich habe die Datenschutzerklärung gelesen und bin einverstanden, dass meine Angaben zur Bearbeitung meiner Anfrage gespeichert werden.*</span></label>
 <button class="btn btn-primary" type="submit">Termin anfragen</button>
 <p class="done" hidden style="color:var(--ok);font-weight:600">Danke – wir melden uns innerhalb von 24 Stunden bei Dir. (Prototyp: es wurde nichts gesendet.)</p>
 <div class="promise"><span>✓ Unverbindlich</span><span>✓ Antwort in 24 Stunden</span><span>✓ Fachbetrieb vor Ort</span><span>✓ Kein Kaufzwang</span></div>
</form>'''

# ---------- diagnose ----------
dg = header() + f'''<section class="diag sec-paper sec"><div class="wrap">
 <div class="stack" style="gap:18px"><span class="eyebrow">Diagnose vor Ort</span><h1>Kostenlose Feuchtigkeitsdiagnose in {V['ORT']} und {V['REGION']}</h1>
 <p class="lead">Du hast eine feuchte Wand, einen nassen Keller oder einen Fleck, den Du nicht einordnen kannst? Hinterlasse hier Deine Kontaktdaten und, wenn Du möchtest, ein oder zwei Fotos. Wir melden uns innerhalb von 24 Stunden bei Dir, um einen Termin zu vereinbaren. Der Termin ist eine Schadensaufnahme, kein Verkaufsgespräch.</p>
 <div class="contact" style="margin-top:8px"><b>{V['BETRIEB']}</b><span>{V['ADRESSE']}, {V['PLZ']} {V['SITZ_ORT']}</span><a href="tel:{V['TELEFON_LINK']}">{V['TELEFON']}</a><a href="mailto:{V['EMAIL']}">{V['EMAIL']}</a></div>
 <p class="note" style="background:var(--clay-soft);border-left:4px solid var(--clay);padding:12px 16px;border-radius:0 4px 4px 0"><strong>Muss ich etwas vorbereiten?</strong> Nein. Hilfreich ist, wenn die betroffene Wand zugänglich ist und Du sagen kannst, seit wann es feucht ist, bei welchem Wetter es schlimmer wird und was schon versucht wurde. Wenn Du schon Angebote hast: Bring sie mit. Wir erklären Dir, von welcher Ursache jedes ausgeht.</p></div>
 {form('dg')}
</div></section>
<section class="sec"><div class="wrap"><div class="sec-head"><h2>Was beim Termin passiert</h2></div><div class="cards3">
 <div><h3>Ansehen</h3><p>Nicht nur der Fleck: Wandaufbau, Anschlüsse, Rohrdurchführungen, Geländehöhe, Nutzung des Raums. Und Deine Beobachtungen: seit wann, bei welchem Wetter, was schon versucht wurde.</p></div>
 <div><h3>Messen</h3><p>Feuchtigkeit an mehreren Stellen mit kalibrierter Messtechnik, damit die Verteilung erkennbar wird: waagerecht, flächig oder punktförmig. Salze, Risse und Anschlüsse werden beurteilt.</p></div>
 <div><h3>Erklären</h3><p>Du bekommst eine nachvollziehbare Einschätzung, woher die Feuchtigkeit wahrscheinlich kommt, und eine Empfehlung, wie es weitergehen kann. Wenn eine Sanierung sinnvoll ist, folgt ein Festpreisangebot – schriftlich, mit erklärten Positionen.</p></div>
</div></div></section>''' + footer()
(OUT/'diagnose.html').write_text(page(f'Kostenlose Feuchtigkeitsdiagnose in {V["ORT"]} – Termin anfragen','Ein Termin, ein Blick auf die Wand, eine ehrliche Einschätzung. Diagnose vor Ort in Düsseldorf und im Kreis Mettmann – unverbindlich.', dg), encoding='utf-8')

# ---------- home ----------
svc_cards=''.join(f'<a href="{s}.html">{icon(s)}<span class="sym">{"Wenn " + SYMPTOM[s][0].lower()+SYMPTOM[s][1:]}</span><h3>{n}</h3><p>{TEASER[s]}</p><span class="more">Mehr erfahren →</span></a>' for s in ORDER_HOME for (ss,n,_) in PAGES if ss==s)
faq_home = [
 ('Ist die erste Schadensanalyse wirklich kostenfrei?','Ja. Der Termin vor Ort mit Messung und Einschätzung kostet Dich nichts und verpflichtet Dich zu nichts. Ein Angebot bekommst Du nur, wenn eine Sanierung aus unserer Sicht sinnvoll ist.'),
 ('Warum ein spezialisierter Fachbetrieb und nicht der Maler oder Maurer?','Weil die Diagnose entscheidet. Ein Betrieb, der auf Bauwerksabdichtung spezialisiert und für die Systeme geschult ist, unterscheidet aufsteigende, seitliche, drückende und Kondensationsfeuchte – und wählt danach die Maßnahme. Sonst wird oft das Symptom behandelt und die Ursache bleibt.'),
 ('Welche Gewährleistung gilt?','Für die Ausführung gilt die gesetzliche Gewährleistung. Was darüber hinaus zugesagt wird, steht schriftlich im Angebot. Dazu bekommst Du eine Dokumentation mit Messwerten, Fotos und den eingesetzten Materialien.'),
 (f'Wie lange dauert eine Mauertrockenlegung {V["REGION"]}?','Die Arbeiten selbst meist 1–3 Tage, je nach Umfang auch länger. Danach braucht die Wand Zeit zum Trocknen: Wochen, bei dicken, stark durchfeuchteten Wänden Monate. Putz und Anstrich kommen nach der Trocknung. Der konkrete Zeitplan steht im Angebot.'),
 ('Muss für die Abdichtung der Garten aufgegraben werden?','In den meisten Fällen nicht. Im Bestand wird heute von innen abgedichtet: über Bohrlöcher, Abdichtungsschichten und Detailarbeiten an der Wandoberfläche. Aufgraben von außen ist die Ausnahme – bei Neubau, offener Baugrube oder auf ausdrücklichen Wunsch.'),
 ('Kommt die Feuchtigkeit wieder?','Wenn die Ursache richtig erkannt und die passende Maßnahme fachgerecht ausgeführt wurde, nach heutigem Kenntnisstand nicht aus dieser Quelle. Was passieren kann: Eine zweite, bisher unauffällige Ursache tritt hervor – zum Beispiel Kondensat in einem nun besser genutzten Keller. Deshalb steht im Angebot, was abgedichtet wird und was nicht.'),
]
faq_html=''.join(f'<details><summary>{html.escape(q)}</summary><p>{html.escape(a)}</p></details>' for q,a in faq_home)
home = header() + f'''
<section class="hero"><div class="wrap">
 <div class="stack"><span class="eyebrow">Zertifizierter BKM-Fachbetrieb · {V['ORT']} und Kreis Mettmann</span>
  <h1>Feuchte Wände {V['REGION']}? Dein BKM-Fachbetrieb für Mauertrockenlegung und Kellersanierung in {V['ORT']}</h1>
  <p class="sub">Feuchtigkeit hat Hausverbot.</p>
  <p class="lead">{V['BETRIEB']} ist zertifizierter BKM-Fachbetrieb für Bauwerksabdichtung – mit Sitz in {V['SITZ_ORT']} und Einsatzgebiet {V['EINSATZGEBIET_KURZ']}. Der erste Schritt ist nicht die Sanierung, sondern herauszufinden, woher die Feuchtigkeit kommt. Genau damit fangen wir an.</p>
  <div class="ctas"><a class="btn btn-primary" href="diagnose.html">Kostenlose Diagnose</a><a class="btn btn-secondary" href="tel:{V['TELEFON_LINK']}">{V['TELEFON']} anrufen</a></div></div>
 <div class="ph"><span>Bild: Fachberater bei der Feuchtemessung an einer Kellerwand</span></div>
</div></section>
<div class="trust"><div class="wrap">
 <div class="item"><svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 20h18M6 20V9l6-5 6 5v11"/><path d="M9 20v-5h6v5"/></svg>Kein Aufgraben in den meisten Fällen</div>
 <div class="item"><svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="9"/><path d="M8 12.5l3 3 5-6"/></svg>{V['JAHRE_PARTNER']} Jahre BKM-Systempartner</div>
 <div class="item"><svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/></svg>Sanierung meist in 1–3 Arbeitstagen</div>
 <span class="seal"><b>BKM</b> Systempartner</span>
</div></div>

<section class="sec"><div class="wrap">
 <div class="sec-head"><span class="eyebrow">Das Problem</span><h2>Feuchtigkeit wird nicht von allein besser</h2>
 <p class="lead">{V['BAUSUBSTANZ_SATZ']} Eine feuchte Wand zeigt immer nur das Ende einer Geschichte – nicht ihren Anfang. Dieselbe dunkle Stelle kann von unten aufsteigen, von der Seite durch die Wand drücken, durch einen Riss eindringen oder aus der Raumluft kommen. Behandelt wird jede dieser Ursachen anders. Deshalb lohnt sich der genaue Blick, bevor irgendjemand etwas verkauft.</p></div>
 <div class="grid-3">
  <div class="risk"><div class="ph"><span>Bild: Schimmelansatz in Kellerecke</span></div><h3>Gesundheit</h3><p>Feuchte Wände können Bedingungen schaffen, unter denen Schimmel entsteht. Das Risiko steigt mit der Dauer, nicht über Nacht.</p></div>
  <div class="risk"><div class="ph"><span>Bild: Wärmebild feuchte Außenwand</span></div><h3>Energie</h3><p>Feuchtes Mauerwerk dämmt schlechter. Der Raum kühlt aus, die Heizung arbeitet gegen die Wand.</p></div>
  <div class="risk"><div class="ph"><span>Bild: Salzränder und abplatzender Putz</span></div><h3>Wert</h3><p>Sichtbare Feuchteschäden fallen jedem Käufer und jedem Gutachter auf. Dokumentierte Sanierung ist das Gegenteil davon.</p></div>
 </div></div></section>

<section class="sec sec-paper" id="ablauf"><div class="wrap">
 <div class="sec-head"><span class="eyebrow">Ablauf</span><h2>Drei Schritte, die Klarheit schaffen</h2><p class="lead">Du schilderst uns Dein Anliegen. Wir sehen uns die Situation vor Ort an, messen und erklären Dir, was wir sehen. Erst dann geht es um eine Lösung.</p></div>
 <div class="steps">
  <div class="step"><span class="n">1</span><h3>Feuchtigkeitsbefund</h3><p>Vor-Ort-Analyse mit kalibrierter Messtechnik. Nicht nur der Fleck wird betrachtet, sondern Wandaufbau, Anschlüsse, Rohrdurchführungen und die Frage, wann es feuchter wird.</p><span class="tag">kostenlos und unverbindlich</span></div>
  <div class="step"><span class="n">2</span><h3>Planbare Sanierung</h3><p>Auf Grundlage des Befunds bekommst Du einen Sanierungsplan mit Festpreis, in dem steht, was gemacht wird, warum – und was nicht nötig ist.</p><span class="tag">schriftlich und nachvollziehbar</span></div>
  <div class="step"><span class="n">3</span><h3>Fachgerechte Ausführung</h3><p>Wir sanieren mit abgestimmten BKM-Systemen, in der Regel von innen und ohne Aufgraben. Was gemacht wird, dokumentieren wir mit Fotos und Messwerten.</p><span class="tag">DIN 18533 und WTA konform</span></div>
 </div></div></section>

<section class="sec"><div class="wrap">
 <div class="sec-head"><span class="eyebrow">Ansprechpartner</span><h2>Ein Ansprechpartner {V['EINSATZGEBIET_KURZ']}.</h2></div>
 <div class="person">
  <div class="card"><div class="ph portrait"><span>Foto: {V['ANSPRECHPARTNER']} bei einer Schadensaufnahme</span></div><span class="name">{V['ANSPRECHPARTNER']}</span><span class="role">{V['FUNKTION']}</span>
   <dl class="kv"><dt>Telefon</dt><dd><a href="tel:{V['TELEFON_LINK']}">{V['TELEFON']}</a></dd><dt>E-Mail</dt><dd><a href="mailto:{V['EMAIL']}">{V['EMAIL']}</a></dd></dl></div>
  <div class="stack" style="gap:18px"><p class="lead">{V['VORSTELLUNG']}</p>
   <div><span class="eyebrow" style="color:var(--petrol)">Unser Einsatzgebiet</span><p style="margin-top:6px">{V['EINSATZGEBIET']}</p></div>
   <div class="ph wide"><span>Grafik: Einsatzgebiet Düsseldorf und Kreis Mettmann</span></div></div>
 </div></div></section>

<section class="sec sec-paper"><div class="wrap">
 <div class="sec-head"><span class="eyebrow">Leistungen</span><h2>Es gibt nicht die eine Lösung. Es gibt die passende.</h2><p class="lead">Jede Sanierung unterbricht einen bestimmten Weg des Wassers. Welche zu Deinem Haus passt, entscheidet der Befund. Das sind die sechs Leistungen, mit denen wir {V['REGION']} am häufigsten arbeiten:</p></div>
 <div class="svc">{svc_cards}</div>
 <p style="margin-top:22px"><a href="leistungen.html" style="font-weight:700">Alle Leistungen im Überblick →</a></p></div></section>

<section class="sec sec-petrol result"><div class="wrap">
 <div class="stack" style="gap:18px"><span class="eyebrow">Das Ergebnis</span><h2>Ein Keller, der wieder Platz bieten kann</h2>
  <ul class="checks"><li>Trockener, nutzbarer Raum</li><li>Schimmelprävention durch behobene Ursache</li><li>Weniger Wärmeverlust über feuchte Wände</li><li>Dokumentation, die auch beim Verkauf zählt</li></ul>
  <div><a class="btn btn-primary" href="diagnose.html">Jetzt sanieren lassen</a></div></div>
 <div class="ph" style="border-color:rgba(255,255,255,.4);background:rgba(255,255,255,.08)"><span>Bild: Sanierter Keller nach der Trocknung</span></div>
</div></section>

<section class="sec diag" id="diagnose"><div class="wrap">
 <div class="stack" style="gap:16px"><span class="eyebrow">Dein erster Schritt</span><h2>Dein erster Schritt: Befund vor Ort</h2>
  <p class="lead">Ein geschulter Fachberater besucht Dich in {V['ORT']} und {V['REGION']}, misst die Feuchtigkeit und erklärt Dir, was er sieht. Das ist eine Untersuchung, kein Verkaufsgespräch.</p>
  <ul class="checks"><li>Feuchtemessung mit kalibrierter Messtechnik</li><li>Dokumentierter Befund mit Ursachenanalyse</li><li>Festpreisangebot, wenn eine Sanierung sinnvoll ist</li><li>Kein Kaufzwang</li></ul></div>
 {form('hm')}
</div></section>

<section class="sec sec-paper"><div class="wrap">
 <div class="tg">
  <div><b>BKM-Systempartner</b><span>Geschult auf abgestimmte Sanierungssysteme</span></div>
  <div><b>Fachgerecht</b><span>Ursache vor Maßnahme, Details im Angebot</span></div>
  <div><b>Persönlich</b><span>Regional. Klar. Erreichbar.</span></div>
  <div><b>Nachvollziehbar</b><span>Dokumentation mit Messwerten und Fotos</span></div>
 </div>
 <a class="rating" href="#"><span class="stars">★★★★★</span><b>4,9</b><span style="color:var(--muted)">· 47 Google-Rezensionen</span></a>
 <div class="contact" style="margin-top:26px"><b>{V['BETRIEB']}</b><span>{V['ADRESSE']}, {V['PLZ']} {V['SITZ_ORT']}</span><a href="tel:{V['TELEFON_LINK']}">{V['TELEFON']}</a><a href="mailto:{V['EMAIL']}">{V['EMAIL']}</a></div>
</div></section>

<section class="sec" id="faq"><div class="wrap">
 <div class="sec-head"><span class="eyebrow">Häufige Fragen</span><h2>Häufige Fragen – klare Antworten</h2></div>
 <div class="faq">{faq_html}</div></div></section>

<section class="closing sec"><div class="wrap">
 <div class="stack"><h2>Feuchtigkeit nicht aufschieben</h2><p class="lead">Feuchtigkeit im Mauerwerk verschwindet nicht von allein, solange ihre Quelle weiter liefert. Nichts davon passiert über Nacht – aber je früher Ursache und Umfang klar sind, desto kleiner fällt die Maßnahme meist aus. Du musst heute nicht wissen, welche Sanierung Du brauchst. Du musst nur den ersten Schritt gehen.</p>
 <div class="ctas"><a class="btn btn-primary" href="diagnose.html">Diagnose sichern</a><a class="btn btn-secondary" href="tel:{V['TELEFON_LINK']}">Direkt anrufen</a></div></div>
 <div class="ph"><span>Bild: Kellerabgang bei Tageslicht</span></div>
</div></section>
''' + footer()
(OUT/'index.html').write_text(page(f'Mauertrockenlegung & Kellersanierung in {V["ORT"]} – {V["BETRIEB_KURZ"]}','Feuchte Wände oder nasser Keller in Düsseldorf und im Rheinland? Zertifizierter BKM-Fachbetrieb: kostenlose Diagnose vor Ort, Sanierung von innen, meist ohne Aufgraben.', home, full=False), encoding='utf-8')
print('built', [p.name for p in OUT.glob('*.html')])
