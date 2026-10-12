"""Render each Markdown source as a page, with shared chapter navigation."""
import html
import json
import os
import subprocess
from pathlib import Path
from urllib.parse import quote

def pandoc(*args, data=None):
    return subprocess.check_output(['pandoc', *args], input=data, text=True)

sources = [Path('pages/index.md')] + sorted(p for p in Path('pages').glob('*.md') if p.name != 'index.md')
docs = {p: json.loads(pandoc(str(p), '-f', 'markdown', '-t', 'json')) for p in sources}
metadata = docs[sources[0]]['meta']

def plain(inlines):
    return pandoc('-f', 'json', '-t', 'plain', data=json.dumps({'pandoc-api-version': docs[sources[0]]['pandoc-api-version'], 'meta': {}, 'blocks': [{'t': 'Plain', 'c': inlines}]})).strip()

def meta_text(key, default):
    value = metadata.get(key, {})
    return plain(value['c']) if value.get('t') == 'MetaInlines' else default

site_title = meta_text('title', 'Dokumentation')
lang = meta_text('lang', 'de')
base = 'https://github.com/' + os.environ.get('GITHUB_REPOSITORY', 'peevey/doc_as_code_template') + '/edit/' + quote(os.environ.get('DOCS_EDIT_BRANCH', 'main'), safe='/')
titles = {}
for p, doc in docs.items():
    headings = [b for b in doc['blocks'] if b['t'] == 'Header']
    titles[p] = plain(headings[0]['c'][2]) if headings else ('Startseite' if p.name == 'index.md' else p.stem)

def rewrite(node):
    if isinstance(node, dict):
        if node.get('t') == 'Link':
            url = node['c'][2][0]
            path, sep, anchor = url.partition('#')
            candidate = Path(path).name
            if candidate in {p.name for p in sources}:
                node['c'][2][0] = quote(Path(candidate).stem) + '.html' + (sep + anchor if sep else '')
        for value in node.values(): rewrite(value)
    elif isinstance(node, list):
        for value in node: rewrite(value)

for p, doc in docs.items():
    rewrite(doc['blocks'])
    nav = '<ul>' + ''.join('<li><a ' + ('aria-current="page" ' if other == p else '') + 'href="' + quote(other.stem) + '.html">' + html.escape(titles[other]) + '</a></li>' for other in sources) + '</ul>'
    title = site_title if p.name == 'index.md' else titles[p]
    # Keep the original heading and its anchor for incoming links.
    doc['meta'] = {}
    if not doc['blocks']:
        doc['blocks'] = [{'t': 'Para', 'c': [{'t': 'Str', 'c': 'Wählen Sie ein Kapitel in der Navigation.'}]}]
    result = pandoc('-f', 'json', '-t', 'html5', '--standalone', '--toc', '--toc-depth=3', '--template=scripts/page.html',
                    '-M', 'lang=' + lang, '-M', 'pagetitle=' + title + ' · ' + site_title,
                    '-V', 'site-title=' + site_title, '-V', 'navigation=' + nav,
                    '-V', 'edit-url=' + base + '/' + quote(str(p), safe='/'),
                    data=json.dumps(doc))
    Path('_site', p.stem + '.html').write_text(result)
