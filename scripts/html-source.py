"""Assemble Markdown with HTML-only links to each chapter's GitHub source."""
import html
import sys
from pathlib import Path
from urllib.parse import quote

base = sys.argv[1].rstrip('/')
for filename in sys.argv[2:]:
    source = Path(filename)
    if filename != 'pages/index.md':
        url = base + '/' + quote(filename, safe='/')
        label = html.escape(source.stem)
        print('\n```{=html}\n<p class="chapter-edit"><a href="' +
              html.escape(url, quote=True) + '">Kapitel bearbeiten <span class="chapter-file">(' +
              label + ')</span></a></p>\n```\n')
    print(source.read_text(encoding='utf-8'))
    print()
