#!/usr/bin/env python3
"""Parse Chinese Grammar Wiki HSK grammar-points HTML files into structured clusters.

Each h3/h4 section + its table (tbody) = one cluster of similar grammar points.
Outputs planning/scripts/wiki-clusters.json with levels -> parts -> clusters -> points.
"""
import json
import re
import html as htmllib
from pathlib import Path

GRAMMAR_DIR = Path(r"Z:\Chinese\resources\grammar")
OUT = Path(r"Z:\Chinese\planning\scripts\wiki-clusters.json")

HEADING_RE = re.compile(r'<h([234])[^>]*>.*?class="mw-headline"[^>]*>(.*?)</span>.*?</h\1>', re.S)
TABLE_RE = re.compile(r'<table[^>]*class="wikitable"[^>]*>.*?<tbody>(.*?)</tbody>', re.S)
ROW_RE = re.compile(r'<tr>(.*?)</tr>', re.S)
CELL_RE = re.compile(r'<td[^>]*>(.*?)</td>', re.S)
TAG_RE = re.compile(r'<[^>]+>')


def clean(text: str) -> str:
    text = htmllib.unescape(text)
    text = text.replace('\xa0', ' ')
    text = TAG_RE.sub('', text)
    return re.sub(r'\s+', ' ', text).strip()


def parse_rows(tbody: str):
    points = []
    for row in ROW_RE.findall(tbody):
        cells = CELL_RE.findall(row)
        if len(cells) < 3 or 'Grammar Point' in clean(cells[0]):
            continue
        title = clean(cells[0])
        pattern = clean(cells[1])
        example = clean(cells[2])
        if title and pattern:
            points.append({'title': title, 'pattern': pattern, 'example': example})
    return points


def parse_file(path: Path):
    src = path.read_text(encoding='utf-8')
    level = int(re.search(r'HSK (\d) grammar points', path.name).group(1))
    # Walk headings and tables in document order
    events = []
    for m in HEADING_RE.finditer(src):
        events.append((m.start(), m.end(), 'h' + m.group(1), clean(m.group(2))))
    for m in TABLE_RE.finditer(src):
        events.append((m.start(), m.end(), 'table', m.group(1)))
    events.sort(key=lambda e: e[0])

    part = None
    cluster = None
    parts, clusters = [], []
    for _, end, kind, val in events:
        if kind in ('h2', 'h3', 'h4'):
            name = clean(val)
            if kind == 'h2':
                part = name
                parts.append(name)
            elif kind in ('h3', 'h4'):
                cluster = {'part': part, 'name': name, 'depth': kind, 'points': []}
                clusters.append(cluster)
        elif kind == 'table' and cluster is not None:
            pts = parse_rows(val)
            if pts:
                cluster['points'].extend(pts)

    total = sum(len(c['points']) for c in clusters)
    return {'level': level, 'parts': parts,
            'clusters': [c for c in clusters if c['points']], 'total_points': total}


def main():
    data = []
    for f in sorted(GRAMMAR_DIR.glob('HSK *.html')):
        data.append(parse_file(f))
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding='utf-8')
    for lvl in data:
        print(f"HSK {lvl['level']}: {len(lvl['clusters'])} clusters, {lvl['total_points']} points")
        for c in lvl['clusters']:
            print(f"  [{c['part'][:30]:<32}] {c['name']:<40} {len(c['points'])} pts")


if __name__ == '__main__':
    main()
