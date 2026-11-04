import json

data = json.load(open(r'Z:\Chinese\planning\scripts\wiki-clusters.json', encoding='utf-8'))
out = []
for lvl in data:
    out.append(f"===== HSK {lvl['level']} =====")
    for i, c in enumerate(lvl['clusters'], 1):
        out.append(f"{i:02d}. [{c['part']}] {c['name']}")
        for p in c['points']:
            out.append(f"     - {p['title']} | {p['pattern']}")
open(r'Z:\Chinese\planning\scripts\cluster-dump.txt', 'w', encoding='utf-8').write('\n'.join(out))
print('lines:', len(out))
