"""Baut aus den erzeugten Seiten eigenstaendige HTML-Dateien.

Die normalen Seiten verweisen relativ auf style.css, fonts/ und assets/. Wer
eine einzelne Datei verschickt oder herunterlaedt, bekommt sie ohne Design zu
sehen. Diese Fassung traegt alles in sich: Stylesheet, Schriften und Grafiken
sind eingebettet, die Datei laeuft per Doppelklick und per E-Mail.

Die Schriften werden dabei auf die tatsaechlich vorkommenden Zeichen
reduziert, sonst wuerde jede Seite unnoetig schwer.

    python3 build.py && python3 bundle.py    ->    standalone/*.html

Benoetigt fonttools mit Brotli:  pip install "fonttools[woff]"
"""

import base64, pathlib, re, sys, unicodedata

HERE = pathlib.Path(__file__).parent
OUT = HERE / 'standalone'
PAGES = sorted(p for p in HERE.glob('*.html'))

try:
    from fontTools import subset
    from fontTools.ttLib import TTFont
except ImportError:
    sys.exit('fonttools fehlt:  pip install "fonttools[woff]"')


def text_of(html_source: str) -> str:
    """Sichtbarer Text einer Seite, ohne Markup und ohne Skripte."""
    s = re.sub(r'<(script|style)\b.*?</\1>', ' ', html_source, flags=re.S | re.I)
    s = re.sub(r'<[^>]+>', ' ', s)
    return s


def used_characters() -> str:
    chars = set()
    for p in PAGES:
        chars |= set(text_of(p.read_text(encoding='utf-8')))
    # Reserve: der Steckbrief eines anderen Betriebs bringt andere Namen mit.
    chars |= set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    chars |= set('0123456789 .,;:!?„“”‚‘’\'"()[]{}<>/\\|-–—_+*=%&#@€$§°~^`')
    chars |= set('äöüÄÖÜßáàâéèêíìîóòôúùûñçÁÀÂÉÈÊÍÌÎÓÒÔÚÙÛÑÇ')
    chars |= set('→←↑↓✓✔★☆·•…')
    # Zusammengesetzte Zeichen sicherheitshalber auch einzeln
    for c in list(chars):
        chars |= set(unicodedata.normalize('NFD', c))
    return ''.join(sorted(chars))


def subset_font(path: pathlib.Path, chars: str) -> bytes:
    font = TTFont(str(path))
    opts = subset.Options()
    opts.layout_features = ['*']       # Ligaturen und Kerning erhalten
    opts.name_IDs = ['*']
    opts.notdef_outline = True
    opts.desubroutinize = False
    opts.drop_tables = []
    # Variable Fonts: Achsen unangetastet lassen, sonst faellt 800 auf 400
    opts.retain_gids = False
    subsetter = subset.Subsetter(options=opts)
    subsetter.populate(text=chars)
    subsetter.subset(font)
    font.flavor = 'woff2'
    buf = __import__('io').BytesIO()
    font.save(buf)
    return buf.getvalue()


def data_uri(raw: bytes, mime: str) -> str:
    return f'data:{mime};base64,' + base64.b64encode(raw).decode('ascii')


def main():
    chars = used_characters()
    css = (HERE / 'style.css').read_text(encoding='utf-8')

    # --- Schriften einbetten -------------------------------------------------
    fonts = {
        'fonts/Unbounded.woff2': None,
        'fonts/TT_Norms_Pro_Compact_Regular.woff2': None,
        'fonts/TT_Norms_Pro_Bold.woff2': None,
    }
    total_before = total_after = 0
    for rel in fonts:
        src = HERE / rel
        raw = subset_font(src, chars)
        total_before += src.stat().st_size
        total_after += len(raw)
        fonts[rel] = data_uri(raw, 'font/woff2')
        print(f'  {pathlib.Path(rel).name}: {src.stat().st_size // 1024} KB -> {len(raw) // 1024} KB')
    print(f'  Schriften gesamt: {total_before // 1024} KB -> {total_after // 1024} KB')

    for rel, uri in fonts.items():
        css = css.replace(f'url("{rel}") format("woff2")', f'url({uri}) format("woff2")')

    # --- Grafiken einbetten --------------------------------------------------
    assets = {}
    for svg in sorted((HERE / 'assets').glob('*.svg')):
        assets[f'assets/{svg.name}'] = data_uri(svg.read_bytes(), 'image/svg+xml')

    OUT.mkdir(exist_ok=True)
    for page in PAGES:
        html_source = page.read_text(encoding='utf-8')

        # Stylesheet-Verweis durch den eingebetteten Block ersetzen
        style_block = '<style>\n' + css + '\n</style>'
        html_source = html_source.replace('<link rel="stylesheet" href="style.css">', style_block)

        # Die Schriften stehen jetzt im Dokument — Preload-Verweise ins Leere weg
        html_source = re.sub(r'<link rel="preload" href="fonts/[^"]+"[^>]*>', '', html_source)

        for rel, uri in assets.items():
            html_source = html_source.replace(f'src="{rel}"', f'src="{uri}"')

        # index.html hat im Original keinen <head>, weil die Artifact-Plattform
        # ihn ergaenzt. Eigenstaendig braucht die Datei einen.
        if not html_source.lstrip().startswith('<!doctype'):
            head_end = html_source.index('<div class="proto">')
            head, body = html_source[:head_end], html_source[head_end:]
            html_source = ('<!doctype html><html lang="de"><head><meta charset="utf-8">'
                           '<meta name="viewport" content="width=device-width,initial-scale=1">'
                           + head + '</head><body>' + body + '</body></html>')

        target = OUT / page.name
        target.write_text(html_source, encoding='utf-8')
        print(f'  {page.name}: {len(html_source.encode("utf-8")) // 1024} KB')

    print(f'\n{len(PAGES)} eigenstaendige Seiten in {OUT.relative_to(HERE.parent.parent)}/')


if __name__ == '__main__':
    main()
