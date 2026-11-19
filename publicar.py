#!/usr/bin/env python3
"""Turn the reviewed drafts into the published pages.

    python3 publicar.py 2026-12-01

Removes the "BROUILLON / DRAFT" line of both privacy policies and writes the
date, in French and in English, where the placeholder is. Refuses if a draft
line or a "[...]" placeholder would be left behind, so a half-finished policy
never reaches GitHub Pages. Nothing else in the text changes.
"""
import datetime
import pathlib
import re
import sys

MONTHS_FR = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet',
             'août', 'septembre', 'octobre', 'novembre', 'décembre']
PAGES = {
    'fr/confidentialite.html': ('[date de publication]', lambda d: f'{d.day} {MONTHS_FR[d.month - 1]} {d.year}'),
    'en/privacy.html': ('[publication date]', lambda d: d.strftime('%-d %B %Y')),
}


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit('usage: publicar.py AAAA-MM-DD')
    day = datetime.date.fromisoformat(sys.argv[1])
    root = pathlib.Path(__file__).resolve().parent
    for name, (placeholder, fmt) in PAGES.items():
        path = root / name
        lines = [l for l in path.read_text(encoding='utf-8').split('\n') if 'class="meta draft"' not in l]
        text = '\n'.join(lines)
        if text.count(placeholder) != 1:
            raise SystemExit(f'{name}: expected exactly one {placeholder}')
        text = text.replace(placeholder, fmt(day))
        if re.search(r'BROUILLON|DRAFT|\[[a-z ]+\]', text):
            raise SystemExit(f'{name}: a draft line or a [placeholder] is still there')
        path.write_text(text, encoding='utf-8')
        print(f'{name}: published, dated {fmt(day)}')


if __name__ == '__main__':
    main()
