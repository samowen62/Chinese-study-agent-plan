# Practice Worksheet Blueprint (type P)

There are three worksheet types in this framework:

| Type | Blueprint | Unit | Test? |
|---|---|---|---|
| **P** practice | this file | ONE official grammar point (`L{n}-XXX-n`, appendix of `references/03-grammar-inventory.md`) | no |
| GT grammar test | `blueprints/02-grammar-test-blueprint.md` | ONE grammar cluster (`L{n}-CL{kk}`) | yes |
| VT vocabulary test | `blueprints/03-vocabulary-test-blueprint.md` | ONE thematic word batch | yes |

This document describes **P only**. Sequence of units comes from
`syllabuses/01-hsk-syllabus.md`.

---

## Anatomy of one worksheet

Every worksheet is a single self-contained HTML file. Structure, order, and rules below are
fixed. The example at `templates/example-worksheet-hsk3-ba.html` shows all of this applied.

## Metadata block

First thing in the HTML, as a comment — machine-readable, one line per field:

```html
<!--
worksheet_id: hsk3-ws-014
hsk_level: 3
grammar_point: L3-SP-1 把字句1
grammar_point_name: 把字句 (把-sentence, basic disposal construction)
topic_context: 日常生活-家庭生活 (moving house / tidying the room)
est_minutes: 13
review_sources: hsk3-ws-013 (L3-CP-2 比较句2), hsk3-ws-011 (L3-AS-3 越来越)
generated: 2026-11-02
-->
```

- `grammar_point` uses the IDs defined in `references/03-grammar-inventory.md`.
- `review_sources` lists worksheet IDs whose content feeds section F (see Review rules below).
- Also render the human-readable header at the top of the page: level, grammar point,
  topic context, estimated time.

## Learning objective (学习目标)

Directly under the header, 1–2 sentences, bilingual (Chinese + English), stating what the
learner will be able to DO by the end. Example: "能使用'把'字句说明对某事物处置的结果 —
Use 把-sentences to state what someone did to an object and the result."

## Section skeleton (fixed order)

| # | Section (Chinese / English) | Purpose | Time | Typical items |
|---|---|---|---|---|
| A | 模式感知 · Pattern warm-up | Meet the pattern in context before analyzing it | 2–3 min | 3–4 |
| B | 语法操练 · Grammar drills | Recognize → discriminate → produce under control | 4–5 min | 6–8 |
| C | 听力模拟 · Listening simulation | Dialogue transcript: read-aloud + comprehension | 3 min | 1 dialogue + 2–3 items |
| D | 考试题型 · Exam-style | Official HSK question formats adapted interactively | 3 min | 3–5 |
| E | 自由产出 · Free production | Open-ended use of the pattern | 3 min | 2–3 |
| F | 温故知新 · Review | Spaced recall of earlier worksheets' content | 2 min | 3–4 |

Total: ~13–15 min, 18–27 items. For HSK 1–2 use the lower end of every range.
Sections A–E all revolve around the ONE grammar point. Section F is the only section that
doesn't.

## Section specs

### A — 模式感知 (Pattern warm-up)
- 3–4 **flip cards** (`flip-card` component): front = natural sentence using the pattern in
  the topic context; back = the pattern highlighted + a one-line note on what it expresses.
  Optionally one card showing the pattern's formula (e.g. `主语 + 把 + 宾语 + 动词 + 结果`).
- No quizzing here. Input only. Pinyin behind click-reveal per policy.
- Include one **deliberate contrast card** when the pattern has a classic confusion partner
  (e.g. 把 vs 被, 了 vs 着, 二 vs 两).

### B — 语法操练 (Grammar drills)
- A graded ladder, always in this difficulty order:
  1. **Recognize**: which sentence uses the pattern correctly (R1/R2) — 2 items
  2. **Select**: MCQ fill-in of the pattern word/particle (R1) or choose correct sentence (R2) — 2–3 items
  3. **Order**: sentence scramble (P2) — 2 items
  4. **Correct**: find and fix the error (P3) — 1–2 items
  5. **Transform / produce**: rewrite or typed answer (P1/P4/P5) — 1–2 items
- Question types and their rules: see `references/01-question-type-catalog.md`.
- Rotate sentence subjects, registers, and situations; keep all items inside the topic context.

### C — 听力模拟 (Listening simulation)
- One short dialogue (6–10 turns at L1–2, 8–14 turns at L3–6) where the pattern occurs at
  least twice, set in the topic context, written as a natural conversation (fillers, 你说呢,
  好啊 etc. — but within level vocabulary).
- Render as a **read-aloud script**: each line numbered, speaker-labeled (男/女 or names),
  with an optional 🔊 TTS button per line (`tts` component) and a "reveal line by line"
  mode for shadowing practice.
- Then 2–3 comprehension items (L1/L2/L3 question types): at least one must require
  understanding an occurrence of the target pattern.
- Instruction tells Sam to read the dialogue aloud twice (once for meaning, once for flow)
  before answering.

### D — 考试题型 (Exam-style)
- Mirrors the official question formats for that level from the past papers
  (see `references/02-level-guide.md` → "Exam structure" for the format list per level).
- 3–5 items, interactive adaptation of paper formats (e.g. word-bank fill becomes click-to-
  place; word-order writing becomes drag/click ordering with the official instruction text).
- Use the official Chinese instruction phrasing from the past papers where sensible
  (e.g. 第51-54题：排列顺序), then add an English subtitle.

### E — 自由产出 (Free production)
- 2–3 open prompts requiring the learner to *write their own* sentences using the pattern:
  - F1 guided questions about Sam's real life (make them specific, not "write 5 sentences"),
  - F2 translation at L3+ (L1–2 uses F3 instead),
  - F4 mini-composition (80–150 字) at L5–6 only.
- Typed input (`typed` component). The answer key gives a **model answer + acceptable
  variants + what would make it wrong**, never a single "the answer".

### F — 温故知新 (Review)
- 3–4 quick items recycling grammar points and vocabulary from `review_sources`
  (earlier worksheets, listed in `progress-log.md`).
- Default spacing: most recent worksheet (≈1 day), one from ~3 worksheets ago, one from
  ~7–10 worksheets ago (weekly). If history is thin, pull the nearest *earlier* grammar
  points from `references/03-grammar-inventory.md` for the same level.
- Prefer quick formats: V1 mixed MCQ, V2 "say it with the old pattern" transformation,
  or one flip-card self-test. Mark each item with the source worksheet ID and its topic.
- Also include the **自评 self-check strip** at the very end: per-section confidence
  checkboxes (😊 / 🤔 / 😩) and a "词语收藏 words to revisit" text box. Whatever Sam notes
  there becomes required content for the next worksheet's review section (agent should ask).

## Answer key & explanation rules (apply to every item, all sections)

1. Reveal is **per item** (check button) — never a big answer-key dump at the bottom.
2. Every key states: correct answer → the rule in one sentence → (for MCQ) why the most
   tempting distractor is wrong.
3. Production items (P1/P4/F*): give model answer + 1–2 acceptable variants + a
   "this would be wrong" example with its reason.
4. Explanations in English, model sentences in Chinese. Chinese in an explanation may
   carry inline click-pinyin like any other content.
5. If an item uses a word above the target level, the key must gloss it
   (word + pinyin + English).

## Pinyin policy (all sections)

- Hidden by default, at every level (Sam's explicit preference; forces character reading).
- Implementation: `<span class="zh" data-py="nǐ hǎo">你好</span>` — click toggles ruby-style
  pinyin above the characters. A page-level "显示拼音 / Show pinyin" toggle also exists.
- Pinyin is written with tone marks; sandhi is NOT respelled (bù stays bù, yī stays yī).
- The only strings exempt from pinyin: section titles and long instruction paragraphs —
  still add pinyin to key pattern words inside instructions.

## Difficulty calibration (by level)

See `references/02-level-guide.md` for level-specific caps (sentence length, vocabulary range, English
gloss allowance, dialogue length). When in doubt, err one notch easier — frustration is worse
than mild ease.
