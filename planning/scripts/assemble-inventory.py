#!/usr/bin/env python3
"""Assemble the new references/03-grammar-inventory.md:
new intro + generated cluster spine + official-syllabus appendix (from the old doc)."""
from pathlib import Path

OLD = Path(r'Z:\Chinese\planning\references\03-grammar-inventory.md')
SPINE = Path(r'Z:\Chinese\planning\scripts\inventory-spine.md')

INTRO = """# Grammar Inventory (HSK 1–6)

Two coordinated layers, both machine- and human-readable:

1. **Cluster spine (primary)** — grammar points grouped into **133 clusters of similar points**
   (502 points), extracted from the Chinese Grammar Wiki files in `Z:\\Chinese\\resources\\grammar\\`
   (HSK 1–6, old wiki scheme). Each cluster has a stable ID `L{n}-CL{kk}`.
   - **Unit tests** (`blueprints/02-grammar-test-blueprint.md`) test an entire cluster.
   - **Scenario MCQs** (question type R4) ask "which grammar point in this cluster fits this
     scenario?" — the cluster's point list is the option pool.
   - **Comparison clusters** (Category: 相似语法点辨析) are the highest-value R4 sources.
2. **Official 2025 syllabus appendix** — the 语法大纲 (PDF pages 383–400) with stable IDs like
   `L3-SP-1 把字句1`. **Practice worksheets** (`blueprints/01-practice-worksheet-blueprint.md`)
   still anchor to ONE appendix point at a time. Each cluster header cross-references appendix IDs.

**Level caveat**: cluster levels follow the OLD wiki HSK scheme (matching the past papers in
`resources\\hsk1\\`…`resources\\hsk6\\`); the appendix follows the 2025-11 syllabus. Cross-reference lines note
placement mismatches (e.g. a wiki-HSK1 point that the 2025 syllabus teaches at level 3).
Vocabulary in worksheet items always follows the 2025 syllabus cumulative list
(`references/02-level-guide.md`), regardless of which layer a grammar point comes from.

## Choosing worksheet content

- **Practice worksheet**: pick ONE appendix point (official ID) as anchor; its cluster is
  context for distractors and warm-up cards.
- **Grammar unit test**: pick ONE cluster; cover all its points across sections; draw R4
  options from the cluster's point list; comparison clusters make ideal standalone tests.
- **Vocabulary test**: see `blueprints/03-vocabulary-test-blueprint.md` (thematic batches,
  not grammar-anchored).

**Progression**: follow `syllabuses/01-hsk-syllabus.md`. Mark completed clusters/points in
`progress-log.md`.
"""

old_text = OLD.read_text(encoding='utf-8')
idx = old_text.find('## HSK 1')
if idx == -1:
    raise SystemExit('could not find appendix start (## HSK 1) in old inventory')
appendix = old_text[idx:]
spine = SPINE.read_text(encoding='utf-8').strip()

APPENDIX_HDR = "\n---\n\n# Appendix — Official 2025 语法大纲 (grammar syllabus)\n\nThe official syllabus content below is the source of truth for the official IDs (L{n}-XXX-n)\nreferenced by clusters above and used by practice worksheets. Levels here are the 2025\nsyllabus levels (词汇/语法/话题 boundaries per `references/02-level-guide.md`).\n"

out = INTRO + '\n' + spine + '\n' + APPENDIX_HDR + '\n' + appendix
OLD.write_text(out, encoding='utf-8')
print('written lines:', out.count('\n') + 1)
