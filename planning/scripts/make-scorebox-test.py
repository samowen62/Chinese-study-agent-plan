#!/usr/bin/env python3
"""Create a score-summary test page from the template (un-comment the scorebox)."""
import re
from pathlib import Path

TPL = Path(r'Z:\Chinese\planning\templates\worksheet-template.html')
OUT = Path(r'Z:\Chinese\planning\scripts\test-scorebox.html')

src = TPL.read_text(encoding='utf-8')

# Extract the commented scorebox block
m = re.search(r'============ Score summary.*?============\s*\n(.*?)\n\s*NOTE for agents.*?-->', src, re.S)
if not m:
    raise SystemExit('scorebox block not found')
block = m.group(1)

# Replace the selfcheck div with the active scorebox
src2 = re.sub(r'<div class="selfcheck">.*?</div>\n', block + '\n', src, count=1, flags=re.S)
# Tag the demo MCQ so missed-point collection has data
src2 = src2.replace('<div class="mcq" data-answer="C">', '<div class="mcq" data-answer="C" data-point="把+O1+V+给+O2">', 1)

OUT.write_text(src2, encoding='utf-8')
print('written', OUT)
