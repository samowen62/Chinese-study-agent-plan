# Grammar Test Blueprint — Cluster Unit Test (GT)

A **grammar unit test** is taken after finishing the practice worksheets for one grammar
cluster (`L{n}-CL{kk}` from `references/03-grammar-inventory.md`). It checks mastery of the
whole cluster before the syllabus (`syllabuses/01-hsk-syllabus.md`) moves on.

Same global rules as all worksheets: 10–15 min, self-contained interactive HTML, pinyin
hidden by default, per-item answer keys with explanations, simplified characters only,
2025-syllabus cumulative vocabulary (see `references/02-level-guide.md`). Start from
`templates/worksheet-template.html` and add the `score-summary` component.

## Metadata block

```html
<!--
worksheet_id: hsk3-gt-CL07
type: grammar-test
hsk_level: 3
cluster: L3-CL07 Sentence Patterns 句式
cluster_points: [把字句, 被动句, 越…越…, 一…也/都+不/没]
practice_units_covered: hsk3-ws-014, hsk3-ws-015, hsk3-ws-016
topic_context: 日常生活 · 出行
est_minutes: 14
scoring: auto (MCQ) + self-grade (production)
generated: 2026-11-03
-->
```

Filename: `hsk{L}-gt-CL{kk}.html` (retakes: `hsk{L}-gt-CL{kk}-r2.html`).

## Section skeleton (fixed order)

| # | Section | Purpose | Time | Items |
|---|---|---|---|---|
| A | 集群速览 · Cluster reference | Non-graded collapsed reference card of the cluster's points + patterns | 1 min | — |
| B | 场景选择 · Scenario MCQ (R4) | "Which grammar point fits this scenario?" — the heart of the test | 4–5 min | 5–6 |
| C | 形式判断 · Form check | Form-focused MCQ/error items per point (R1/R2/P3) | 3–4 min | 4–5 |
| D | 综合运用 · Production | Typed items: transform / produce with cluster points (P4/P1, self-graded) | 3 min | 2–3 |
| E | 语篇理解 · Cluster in context | One dialogue or passage using ≥3 cluster points + comprehension items | 2–3 min | 1 + 2–3 |
| F | 得分总结 · Score summary | `score-summary` component: verdict + what-to-review advice | 1 min | — |

### A — 集群速览 (Cluster reference)
- Collapsible card (visible by clicking) listing every cluster point: English name + pattern
  + one example, from the inventory's cluster table. Learners may consult it during the test
  (this is a learning tool, not a proctored exam) — but section B instruction should say
  "try to answer before peeking".
- If the cluster has a sibling **comparison cluster** in the same level (Category:
  相似语法点辨析), include its rows here too.

### B — 场景选择 (Scenario MCQ, question type R4)
- 5–6 items. Each presents a mini-scenario (situation sentence in Chinese with a blank, or
  an English-described situation) and asks which of the cluster's grammar points fits.
- **Options** = 3–4 grammar points from the cluster, labeled with the point's key word +
  pattern (e.g. `A. 把+O+V+结果` `B. 被+doer+V` `C. 越来越…` `D. 一…也/都+不/没`).
  Never invent options outside the cluster unless the cluster has <3 points (then borrow
  from the nearest cluster in the same level and say so in the key).
- Rotate the correct answer across positions; every cluster point must be the correct
  answer at least once across the section (for clusters with more points than items,
  prioritize points NOT yet tested in section C/E).
- The key explains the scenario's semantic cue (e.g. "the object ends up somewhere → 把
  pattern ①", "new situation unfolding → 了2").
- **Comparison clusters** (e.g. 不 vs 没, 再 vs 又, 才 vs 就): make this the dominant
  section — every item contrasts exactly two member points.

### C — 形式判断 (Form check)
- 4–5 MCQ items testing form, not choice of point: choose the correct sentence (R2),
  pick the error segment (P3), or fill the particle (R1) — all within cluster points.
- Exactly one defensible answer each; distractors = classic learner errors of these points.

### D — 综合运用 (Production, self-graded)
- 2–3 typed items: rewrite with a specified cluster point (P4), or answer a personal
  question forcing a specific point (F1-style). Keys give model + variants + wrong-with-reason.

### E — 语篇理解 (Cluster in context)
- One dialogue (6–10 turns) or short passage where ≥3 cluster points occur naturally,
  in the topic context; then 2–3 comprehension items (L1/L3 or R2).
  At least one item asks the learner to identify WHICH cluster point a highlighted
  sentence uses and what it contributes to meaning.

### F — 得分总结 (Score summary)
- `score-summary` component: auto-counts correct MCQ selections in B/C/E; shows
  self-grade buttons (😊/🤔/😩) for section D items; computes a percentage over
  auto-scored items.
- **Advice text is generated from results**: list the cluster points missed (from item
  metadata `data-point`) as the "review these" list, plus a verdict:
  - ≥80% auto-score: unit passed — tell the syllabus to advance (log `pass` in
    `progress-log.md`).
  - <80%: unit not passed — recommend a targeted mini-practice worksheet for the missed
    points (type P) before retaking the test.

## Scoring rules
- Auto-scored: all MCQ (B, C, E comprehension). The template's MCQ marking provides the count.
- Self-graded: D items — the key asks the learner to honestly mark 😊 (correct) / 🤔
  (almost) / 😩 (wrong); these feed advice but not the percentage.
- The pass threshold (80% of auto-scored items) is a guideline recorded in the log, not a
  hard gate — Sam decides whether to advance or remediate.

## Generation rules specific to GT
1. Every cluster point must appear in at least one item across B–E (cover the whole
   cluster — that's what makes it a unit test).
2. Items must NOT reuse example sentences from the inventory verbatim; write fresh
   sentences in the topic context, with level-appropriate vocabulary.
3. Cluster points whose official 2025-syllabus placement is higher than the test level
   (see cluster cross-ref notes) may be included (they're in the wiki cluster) but their
   vocabulary must stay in the 2025 cumulative list; gloss anything above.
4. Log the result in `progress-log.md` with score, verdict, and missed points.
