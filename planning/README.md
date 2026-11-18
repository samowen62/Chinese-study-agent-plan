# HSK Worksheet Generation Framework

This framework lets AI agents generate consistent, high-quality, interactive Chinese study
worksheets for Sam. Read this README first, then follow the map below.

## What we're building

**Worksheets are**: short (10–15 min), interactive HTML pages running in a browser (not
printed), with pinyin hidden by default (hover a dashed word) and answers behind
click-to-reveal keys. There are **three worksheet types**:

| Type | What it is | Unit it covers | Blueprint |
|---|---|---|---|
| **P** practice | One grammar point, studied in depth (this is also the "generalized review" format) | ONE official 语法大纲 point | `blueprints/01-practice-worksheet-blueprint.md` |
| **GT** grammar test | Unit test with scoring — cluster-wide discrimination (which grammar point fits a scenario?) | ONE grammar cluster | `blueprints/02-grammar-test-blueprint.md` |
| **VT** vocabulary test | Thematic batch test: meaning, pinyin, collocation, production | ONE topic word batch (20–30 words) | `blueprints/03-vocabulary-test-blueprint.md` |

**Structured introduction**: the order of all units is defined by
`syllabuses/01-hsk-syllabus.md` — agents should always be able to answer "what comes next?"
from the syllabus plus `progress-log.md`.

**Source material** (in `Z:\Chinese\resources\`):
- `resources\新版HSK考试大纲1219.pdf` — official HSK syllabus (2025-11 edition, effective 2026-07).
  Content source of truth: vocabulary, grammar, topics, tasks, characters.
- `resources\hsk1\` … `resources\hsk6\` — official past papers (older generation). Question-format
  reference for exam-style sections.
- `resources\grammar\` — Chinese Grammar Wiki pages (old wiki HSK levels); source of the
  **grammar clusters** in `references/03-grammar-inventory.md`.

## Design decisions (fixed — do not deviate without asking Sam)

| Decision | Value |
|---|---|
| Levels covered | HSK 1–6 |
| Purpose | Mixed study practice **and** exam-style sections; tests gate progression |
| Organizing principle | P: one grammar point · GT: one cluster · VT: one thematic word batch |
| Length | 10–15 minutes, ~20–25 items (all types) |
| Listening skill | "Listening simulation": dialogue transcripts for read-aloud + comprehension (optional TTS button) |
| Pinyin | Hidden by default everywhere; hover a dashed `.zh` word to show ruby pinyin; no Show-all button; tone marks (ā á ǎ à) |
| Answer keys | Every item: answer + explanation (why right / why distractors wrong), click-to-reveal |
| Vocabulary | Cumulative vocab of target level; may slightly exceed (~≤5%) when it serves learning; gloss anything beyond. Prefer unused list words over recycling 忙/累/热/高兴/哥哥; rotate 话题 even inside one worksheet. |
| Interactivity | Hover pinyin, flip cards, click-to-order tiles, paste-report score box on every worksheet |
| Output | Self-contained HTML (one file, no external dependencies) |

## Directory map

```
planning\
├── README.md                        ← you are here
├── progress-log.md                  ← append-only unit record; drives review sections
├── blueprints\
│   ├── 01-practice-worksheet-blueprint.md   (P)
│   ├── 02-grammar-test-blueprint.md         (GT)
│   └── 03-vocabulary-test-blueprint.md       (VT)
├── references\
│   ├── 01-question-type-catalog.md  ← every allowed item format + HTML components
│   ├── 02-level-guide.md            ← per-level exam structure, vocab ranges, topics, scaffolding
│   └── 03-grammar-inventory.md      ← cluster spine (133 clusters/502 points) + official 2025 语法大纲 appendix
├── syllabuses\
│   └── 01-hsk-syllabus.md           ← unit order, test cadence, progression rules
├── plans\                           ← build plans (one .md per task; all future plans saved here)
├── templates\
│   ├── worksheet-template.html      ← copy as starting point (all components implemented)
│   └── example-worksheet-hsk3-ba.html  ← complete P example (HSK3 把字句)
└── scripts\                         ← extraction tooling + generated data (cluster JSON)
```

**Course storage**: worksheets built as part of a level course go in
`Z:\Chinese\courses\hsk{L}\{p,gt,vt}\` with a `course-manifest.md` tracking every unit's
status. Failed GT/VT retakes go in the adjacent `gt\retakes\` or `vt\retakes\` folder
(generated automatically when a <80% score is logged, unless Sam skips). Standalone
one-off worksheets still go in `Z:\Chinese\worksheets\{type}\`.

## Workflow: generating a worksheet

1. **Determine the next unit**: read `progress-log.md`, then apply "the next unit" rules in
   `syllabuses/01-hsk-syllabus.md`. (Or take Sam's explicit request — off-sequence is fine,
   but log it.)
2. Read the blueprint for that type (P / GT / VT).
3. Read the unit's content source: appendix of `references/03-grammar-inventory.md` (P:
   one point · GT: one cluster) or the vocabulary boundaries + topic list in
   `references/02-level-guide.md` (VT).
4. Read `references/01-question-type-catalog.md` for item formats and components.
5. Generate content per the blueprint, then render HTML by copying
   `templates/worksheet-template.html`. Every file has `body data-id` + `data-type`
   (P|GT|VT) and the paste-report score box. MCQ/bank items carry `data-point` / `data-word`.
6. Run the QA checklist below. Fix anything that fails.
7. Save as `Z:\Chinese\worksheets\{type}\hsk{L}-…` with these names:
   - P: `hsk{L}-ws{NNN}-{slug}.html`
   - GT: `hsk{L}-gt-CL{kk}.html` (retakes: `{gt}/retakes/hsk{L}-gt-CL{kk}-rN.html`)
   - VT: `hsk{L}-vt-{NN}-{topic-slug}.html` (retakes: `{vt}/retakes/hsk{L}-vt-{NN}-rN.html`)
8. Append a row to `progress-log.md` (see its header for the format). For tests, record
   score + verdict + missed points/words once Sam reports them.

## Global content rules

1. **Simplified characters only.** Neutral, standard, natural Mandarin.
2. **Grammar accuracy is non-negotiable.** Every sentence must be verified natural and
   unambiguous. If unsure of a pattern's exact usage, check the 语法大纲 pages of the PDF
   (levels 1–6: PDF pages 383–400) before writing items.
3. **Vocabulary**: cumulative list of the 2025 词汇大纲 through the target level
   (boundaries: L1 #1–300 · L2 →#551 · L3 →#1000 · L4 →#2000 · L5 →#3600 · L6 →#5400).
   Wiki cluster examples may use old-HSK vocab — rewrite, don't copy. Words above the
   target level (~≤5%) must be glossed in the key.
4. **One correct answer per item.** Distractors are plausible learner errors
   (`references/01-question-type-catalog.md`), never nonsense. GT scenario items follow R4:
   all options come from the same cluster.
5. **Explanations teach the rule**, not just the answer; English explanations, Chinese
   model sentences.
6. **Pinyin**: tone marks, never numbers; base tone for sandhi (不 bù, 一 yī).
7. **No external resources** in HTML: no CDN links, no images beyond inline SVG/emoji, system
   font stack (`"Microsoft YaHei", "Noto Sans SC", sans-serif`).

## QA checklist (run before delivering)

- [ ] Correct type (P/GT/VT), correct unit, per the syllabus sequence or Sam's request.
- [ ] Section skeleton and order match the type's blueprint.
- [ ] GT: every cluster point appears in ≥1 item; R4 options all from the cluster;
      `data-point` on every MCQ; paste-report present.
- [ ] VT: every batch word tested ≥1 time; `data-word` on every MCQ/bank item;
      paste-report present; batch words verified in 词汇大纲.
- [ ] P: one grammar point only, in every section B–D item; review section sources from log.
- [ ] Item counts and estimated time fit 10–15 minutes at the target level.
- [ ] Pinyin hidden by default (hover only; no Show-all button); production items always show characters.
- [ ] Every item has a working check/reveal control with answer + explanation.
- [ ] Distractors plausible; exactly one defensible answer per item.
- [ ] Vocabulary within cumulative level list; anything above is glossed.
- [ ] HTML opens standalone; all interactions work (hover pinyin, MCQ marking, tiles, flip,
      paste-report); mobile-readable (720px max width).
- [ ] Metadata block filled; filename matches convention; progress log updated.
