"""Replace （　） with clickable .slot spans inside bank-fill items only."""
from pathlib import Path
import re

ROOT = Path(r"Z:\Chinese\courses\hsk4")
BLANK = "（　）"
SLOT = '<span class="slot"></span>'


def fix_html(text: str) -> str:
    parts = re.split(r'(<div class="item"[^>]*>)', text)
    out = [parts[0]]
    i = 1
    while i < len(parts):
        opener = parts[i]
        body = parts[i + 1] if i + 1 < len(parts) else ""
        # only rewrite blanks that sit before the check/reset buttons of a bank item
        if '<div class="bank">' in body:
            # split at first check button so later MCQ/typed blanks stay as-is
            m = re.search(r'<button class="btn check">', body)
            if m:
                head, tail = body[: m.start()], body[m.start() :]
                head = head.replace(BLANK, SLOT)
                body = head + tail
            else:
                body = body.replace(BLANK, SLOT)
        out.append(opener)
        out.append(body)
        i += 2
    return "".join(out)


def main():
    n_files = 0
    n_slots = 0
    for p in ROOT.rglob("*.html"):
        src = p.read_text(encoding="utf-8")
        dst = fix_html(src)
        if dst != src:
            added = dst.count(SLOT) - src.count(SLOT)
            p.write_text(dst, encoding="utf-8")
            n_files += 1
            n_slots += added
            print(f"{p.name}: +{added} slots")
    print(f"updated {n_files} files, {n_slots} slots")


if __name__ == "__main__":
    main()
