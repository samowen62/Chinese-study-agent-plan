# HSK4 Comprehensive Course — Course Manifest + Wave 1

Plan created 2026-11-05 (approved). Status: executing.
Build the full HSK4 course in `Z:\Chinese\courses\hsk4\` per
`planning/syllabuses/01-hsk-syllabus.md`. Total course ≈ 80+ units (P practice worksheets,
GT tests per cluster, VT batches covering 词汇大纲 #1001–2000), built in **staged waves**
tracked by a course manifest. Wave 1 (11 worksheets) generated immediately after approval.

## Todos

### 1. Directories + plan storage
- Create `Z:\Chinese\courses\hsk4\p\`, `...\gt\`, `...\vt\`
- Create `Z:\Chinese\planning\plans\`, save this plan there as
  `plans/2026-11-05-hsk4-course-build.md`, and add a `plans\` line to the directory map in
  `planning/README.md` (convention: all future plans saved there)

### 2. Course manifest — `courses/hsk4/course-manifest.md`
List EVERY unit in syllabus order (P…P→GT→VT interleaving), each row: unit id, type,
cluster/topic, anchor points or word batch, predecessor, status. Specifically:
- Unit 0: `hsk4-gt-entry` — level-entry placement mini-check (syllabus level-progression rule)
- GT per cluster for CL01–CL26; split `L4-CL02 Adverbs` (27 points) into three sub-units
  CL02a/CL02b/CL02c (~9 points each) so each GT stays in the 10–15 min format
- Comparison clusters CL27–CL30 folded into parent-cluster GTs (syllabus rule: no own P)
- P worksheets per syllabus rule of thumb: 1–2 per small cluster (≤4 pts), 2–4 per larger
- ~36 VT batches: 1000 L4 words grouped by HSK4 话题 topics (20–30 words, 70% L4 / 30% lower)
- Trivial clusters (e.g. CL06 其中, CL07 分之, CL10/CL11 single points) merged into nearest
  related cluster unit, noted in the manifest

### 3. Generate Wave 1 (11 worksheets, in order)
| # | File | Unit |
|---|---|---|
| 1 | `gt/hsk4-gt-entry.html` | Placement mini-check: 5-6 R4 items sampling CL01/CL06/CL23 + HSK3 core |
| 2 | `p/hsk4-ws-001.html` | P: CL01 Adjectives — anchor L4-CM-1 程度补语2 死了 (secondary: 全) |
| 3 | `gt/hsk4-gt-CL01.html` | GT: cluster L4-CL01 (语法讲解 cards → R4 → score-summary, `data-point`) |
| 4 | `vt/hsk4-vt-01.html` | VT: topic 1 日常生活·个人情况 batch (词语讲解 definitions → VM1-4, `data-word`) |
| 5 | `p/hsk4-ws-002.html` | P: CL02a — anchor L4-QT-1 反问句2 难道/究竟 |
| 6 | `p/hsk4-ws-003.html` | P: CL02a — anchor L4-SP-5 双重否定 不得不/只好 |
| 7 | `gt/hsk4-gt-CL02a.html` | GT: sub-cluster CL02a 语气/评价类副词 |
| 8 | `vt/hsk4-vt-02.html` | VT: topic 2 饮食 batch |
| 9 | `p/hsk4-ws-004.html` | P: CL02b — anchor L4-FX-1 一+量+比+一+量 + L4-FX-2 再也不 |
| 10 | `p/hsk4-ws-005.html` | P: CL02b — anchor time adverbs contrast 刚/原来/本来/差点 |
| 11 | `gt/hsk4-gt-CL02b.html` | GT: sub-cluster CL02b 时间/频率类副词 |

Rules per blueprint used by each type (`planning/blueprints/01-practice-worksheet-blueprint.md`,
`planning/blueprints/02-grammar-test-blueprint.md`,
`planning/blueprints/03-vocabulary-test-blueprint.md`) from
`planning/templates/worksheet-template.html`:
pinyin hidden; every item has answer + explanation; vocab within #1–2000 cumulative
(gloss anything above); topics rotate per level guide; GT coverage-symmetry (every tested
point explained in section A); VT batch words verified against 词汇大纲 序号; review
sections use earlier L4 points (no hsk4 log history yet — per blueprint fallback).

### 4. Browser verification
Serve `courses/hsk4` locally; spot-check one of each type: GT score-summary +
`data-point` collection, VT bank-fill reset + `data-word`, P interactions (MCQ marking,
pinyin toggle). Fix anything broken before finishing.

### 5. Update tracking
- Append 11 rows to `planning/progress-log.md`
- Mark the 11 units `generated` in `course-manifest.md`; note Wave 2 contents
  (CL02c + GT + next clusters + VT-03/04) for the next "continue the course" request
