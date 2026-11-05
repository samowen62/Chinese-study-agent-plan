# Vocabulary Test Blueprint — Thematic Batch Test (VT)

A **vocabulary test** checks one thematic batch of words (20–30 words related to one
话题大纲 topic) and is taken after encountering them in practice worksheets / reading.
It is organized by TOPIC, not by grammar.

Same global rules: 10–15 min, self-contained interactive HTML, pinyin hidden by default,
per-item answer keys with explanations, 2025-syllabus cumulative vocabulary
(`references/02-level-guide.md`), simplified characters. Start from
`templates/worksheet-template.html` and add `score-summary`.

## The word batch

- **Source of truth**: the 词汇大纲 cumulative list (level boundaries in
  `references/02-level-guide.md`; 词汇大纲 PDF pages 77–212).
- **Theme**: one topic from the level's 话题大纲 list. The agent selects 20–30 words from
  the cumulative list whose meanings relate to the topic. Prefer nouns/verbs/adjectives
  that make concrete, testable items; skip pure function words unless thematically central.
- **Batch composition**: ~70% words at the target level, ~30% from lower levels (cumulative
  reinforcement). Never exceed the target level — this is a batch test, not enrichment.
- **Sequence** across batches: follow the level's topic order in `syllabuses/01-hsk-syllabus.md`;
  every cumulative word should eventually land in some batch.

## Metadata block

```html
<!--
worksheet_id: hsk3-vt-07
type: vocabulary-test
hsk_level: 3
topic: 自然 · 季节与天气
batch: [春天, 夏天, 秋天, 冬天, 阴, 晴, 雾, ...]   (20–30 words, 词汇大纲 序号 noted)
est_minutes: 15   (definitions pass A≈2-3 + test B-G)
scoring: auto (MCQ/match) + self-grade (production)
generated: 2026-11-04
-->
```

Filename: `hsk{L}-vt-{NN}-{topic-slug}.html`.

## Section skeleton (fixed order)

| # | Section | Purpose | Time | Items |
|---|---|---|---|---|
| A | 词语讲解 · Word definitions | Non-graded: every batch word defined upfront | 2–3 min | one entry per word |
| B | 词语表 · Batch reference | Non-graded collapsed compact word list for during-test lookup | 1 min | — |
| C | 认词 · Meaning recognition (VM1) | Chinese → English meaning MCQ + reverse | 4 min | 6–8 |
| D | 读音 · Pinyin ↔ character (VM2) | Select/match correct pronunciation | 2–3 min | 4–5 |
| E | 用法 · Usage in context (VM3) | Cloze sentences where only one batch word fits | 2–3 min | 5–6 |
| F | 造句 · Production (VM4) | Write sentences with assigned batch words (self-graded) | 2 min | 2–3 |
| G | 得分总结 · Score summary | `score-summary`: verdict + auto-collected review list | 1 min | — |

Section A is a **study pass**, not part of the scored test — keep the test proper (C–G)
inside the 10–15 minute envelope and keep A tight (2–3 min max).

### A — 词语讲解 (Word definitions) — REQUIRED, every batch word defined
- For **every word in the batch** (the exact set that will be tested), render one
  definition entry, in 词汇大纲 list order, containing:
  - **词** the word in characters (click-to-reveal pinyin with tone marks) + 词性 POS
    (from the 词汇大纲 词性 column: 名/动/形/副/量/…).
  - **定义**: a plain-English definition — a real dictionary sense for this word's POS,
    not a vague "about"-phrase.
  - **搭配/用法**: one usage note — a natural collocation, common measure word, or
    valence fact (e.g. 见面 needs 和/跟: 我跟她见过面).
  - **例句**: one natural example sentence in the topic context, English glossed.
- Entries are plain `.item` cards or a definition list — visible by default (this is the
  learning input), each word's pinyin behind click. NO word may appear in a C–F item
  without being defined here first. No surprises.
- Keep one entry tight (3–4 lines); the full pass must stay ≤3 minutes.

### B — 词语表 (Batch reference)
- Collapsed card: one compact row per batch word — `序号 | 词 | 词性 | English gloss |
  (pinyin by click)`. This is the during-test lookup; instruction says try without it first.

### C — 认词 (Meaning recognition, VM1)
- ~Half items: "这个词是什么意思？" — word shown in characters, 4 English gloss options.
  Distractors = glosses of OTHER batch words (same POS where possible) or of common
  confusables (e.g. 天气 vs 气候).
- ~Half items: reverse direction — English meaning → choose the Chinese word (options are
  Chinese words from the batch, visually distinct characters).
- One item per word; spread across C–E so every batch word is directly tested ≥ once
  (batch words too abstract for E cloze can appear twice in C).

### D — 读音 (Pinyin, VM2)
- 4–5 items in two flavors: select the correct tone-marked pinyin for a given word
  (distractors = same syllable wrong tone, or tone-mark placement errors), and match
  4–6 words to their pinyin (`match` component).
- Prioritize words with 容易错的 pronunciation: tone pairs, 多音字, neutral-tone syllables
  (e.g. 东西 dōngxi), and words whose characters look alike.

### E — 用法 (Usage in context, VM3)
- 5–6 cloze sentences; exactly one batch word fits per blank (collocation or context
  decided). Use `bank-fill` (6–8 word bank with 1–2 extra batch words as distractors) or
  MCQ when the distinction is fine (e.g. 见面 vs 看见). Every bank-fill item includes a
  重来 reset button.
- Sentences live in the topic context, use level grammar only, and must be decidable
  without the missing word being guessable from character components alone.
- The key states the collocation/context cue ("天气 takes 晴, not 晴天's 晴 alone…").

### F — 造句 (Production, VM4)
- 2–3 typed items: "用『春天』写一句话" / a situation prompt requiring one assigned word
  ("你想约朋友周末去公园赏花 — 用『晴』说一句话"). Assign the trickiest words (the ones that
  failed most often in earlier reviews, if known from `progress-log.md`).
- Keys give a model sentence + acceptable variants + a "this would be wrong" example
  (wrong collocation, wrong measure word, wrong valence: e.g. 见面 needs 和/跟 object).

### G — 得分总结 (Score summary)
- `score-summary` auto-counts C/D/E; self-grade buttons cover F; percentage over
  auto-scored items with the 80% pass guideline (same rules as the grammar test).
- The review list is **word-level**: missed words are listed (from item `data-word`) for
  Sam's 词语收藏; the agent must include them in the next worksheet's review section and
  re-test them in the next VT's section C.

## Generation rules specific to VT

1. Verify every batch word against the 词汇大纲 (correct pinyin, POS, level 序号). Tone
   sandhi is written as base tone per HSK convention.
2. Definitions must match standard dictionary senses for the word's POS; beware
   near-synonyms across definitions (test items must not hinge on a nuance the
   dictionary doesn't support).
3. Word-identification questions (C reverse, D match) must not put two visually
   near-identical character words in the same option set unless the key explains the
   distinguishing component (那/哪 style pairs are fair game — they ARE the point).
4. No grammar above the target level in any sentence (this is a vocabulary test;
   grammar surprise invalidates the item).
5. Log results in `progress-log.md`: score, verdict, missed words.
