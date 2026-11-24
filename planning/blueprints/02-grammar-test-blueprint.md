# Grammar Test Blueprint — Cluster Unit Test (GT)

A **grammar unit test** is taken after finishing the practice worksheets for one grammar
cluster (`L{n}-CL{kk}` from `references/03-grammar-inventory.md`). It checks mastery of the
whole cluster before the syllabus (`syllabuses/01-hsk-syllabus.md`) moves on.

Same global rules as all worksheets: 10–15 min, self-contained interactive HTML, pinyin
hidden by default, per-item answer keys with explanations, simplified characters only,
2025-syllabus cumulative vocabulary (see `references/02-level-guide.md`). Start from
`templates/worksheet-template.html`. Body needs `data-id` + `data-type="GT"`; the paste-report
score box is already in the template.

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
est_minutes: 15   (study pass A≈2-3 + test B-G)
scoring: auto (MCQ) + self-grade (production)
generated: 2026-11-04
-->
```

Filename: `hsk{L}-gt-CL{kk}.html`.

**Retakes (automatic):** when Sam reports a score **<80%**, generate the retake immediately
into the adjacent `retakes\` folder — do not wait to be asked, unless he explicitly skips.
Path: `courses/hsk{L}/gt/retakes/hsk{L}-gt-CL{kk}-r2.html` (later attempts `-r3`, …).
Write fresh items; overweight missed `data-point`s from the failed attempt. Also generate
the targeted remediation P on those points. A passing retake replaces the fail row in
`progress-log.md`.

## Section skeleton (fixed order)

| # | Section | Purpose | Time | Items |
|---|---|---|---|---|
| A | 语法讲解 · Grammar explanations | Non-graded: every grammar point being tested, explained | 2–3 min | one card per point |
| B | 集群速览 · Cluster reference | Non-graded collapsed compact reference card | 1 min | — |
| C | 场景选择 · Scenario MCQ (R4) | "Which grammar point fits this scenario?" — the heart of the test | 4–5 min | 5–6 |
| D | 形式判断 · Form check | Form-focused MCQ/error items per point (R1/R2/P3) | 2–3 min | 4–5 |
| E | 综合运用 · Production | Typed items: transform / produce with cluster points (P4/P1, self-graded) | 2–3 min | 2–3 |
| F | 语篇理解 · Cluster in context | One dialogue or passage using ≥3 cluster points + comprehension items | 2 min | 1 + 2–3 |
| G | 报告 · Report | paste-report: auto-score + copy-ready block (pass/fail at 80%) | 1 min | — |

Section A is a **study pass**, not part of the scored test — keep the test proper (C–G)
inside the 10–15 minute envelope and keep A tight (2–3 min max).

### A — 语法讲解 (Grammar explanations) — REQUIRED, one card per cluster point
- For **every point in the cluster** (the exact set that will be tested), render one
  explanation card, in cluster order:
  - **Name**: English point name + the key Chinese word(s) (e.g. 被 passive — "bei sentences").
  - **Formula**: the pattern, from the inventory row (e.g. `S + 被 + doer + V + 其他`).
  - **What it expresses**: 1–2 plain-English sentences on meaning/function — when a speaker
    reaches for this point (e.g. "the receiver of the action is the topic; the doer may be
    omitted when it's unknown or obvious").
  - **Worked examples**: **2–3** natural sentences (not one), each a different situation,
    with hover pinyin and an English gloss, the pattern keywords highlighted. Prefer unused
    HSK4 cumulative words; do not recycle 忙/累/热/高兴. These A sentences must not reappear
    in C–F.
  - **Pitfall**: one line naming the classic learner error for this point (e.g. "negation
    goes before 把: 我没把…" not 我把…没…").
- For **comparison clusters** (Category 相似语法点辨析), each card must state *what
  distinguishes this point from its partner* (e.g. 不 = subjective/habitual/future negation,
  没 = objective/past) — that contrast IS the card's "what it expresses".
- Cards use the `flip-card` component (front: name + key word + formula; back: explanation
  + example + pitfall) or plain `.item` cards — but ALL points of the cluster must appear,
  and every point that appears in a C–F item must have been explained here. No surprises.
- Pinyin stays hover-only per global policy (no Show-all button).

### B — 集群速览 (Cluster reference)
- Collapsed card (visible by clicking) listing every cluster point compactly: English name +
  pattern + one example, taken from the inventory's cluster table. This is the during-test
  lookup card, so keep it to one line per point.
- If the cluster has a sibling comparison cluster in the same level, include its rows here.
- The C-section instruction should say "try to answer before peeking at B".

### C — 场景选择 (Scenario MCQ, question type R4)
- 5–6 items. Each presents a mini-scenario (situation sentence in Chinese with a blank, or
  an English-described situation) and asks which of the cluster's grammar points fits.
- **Options** = 3–4 grammar points from the cluster, labeled with the point's key word +
  pattern (e.g. `A. 把+O+V+结果` `B. 被+doer+V` `C. 越来越…` `D. 一…也/都+不/没`).
  Never invent options outside the cluster unless the cluster has <3 points (then borrow
  from the nearest cluster in the same level and say so in the key).
- Rotate the correct answer across positions; every cluster point must be the correct
  answer at least once across the section (for clusters with more points than items,
  prioritize points NOT yet tested in sections D/F).
- The key explains the scenario's semantic cue (e.g. "the object ends up somewhere → 把
  pattern ①", "new situation unfolding → 了2").
- **Comparison clusters** (e.g. 不 vs 没, 再 vs 又, 才 vs 就): make this the dominant
  section — every item contrasts exactly two member points.

### D — 形式判断 (Form check)
- 4–5 MCQ items testing form, not choice of point: choose the correct sentence (R2),
  pick the error segment (P3), or fill the particle (R1) — all within cluster points.
- Exactly one defensible answer each; distractors = classic learner errors of these points.

### E — 综合运用 (Production, self-graded)
- 2–3 typed items: rewrite with a specified cluster point (P4), or answer a personal
  question forcing a specific point (F1-style). Keys give model + variants + wrong-with-reason.

### F — 语篇理解 (Cluster in context)
- One dialogue (6–10 turns) or short passage where ≥3 cluster points occur naturally,
  in the topic context; then 2–3 comprehension items (L1/L3 or R2).
  At least one item asks the learner to identify WHICH cluster point a highlighted
  sentence uses and what it contributes to meaning.

### G — 报告 (Report)
- Paste-report box: auto-counts MCQ in C/D/F, bank-fill, and P2 `data-order` (≥10 total);
  **生成报告 / Copy report**
  writes a `<pre>` block Sam pastes into the course chat:

```
worksheet_id: hsk4-gt-CL01
type: GT
score: 8/11 (73%)
verdict: fail
needs_review: 死了, 反问句
notes:
```

- `verdict` is `pass` / `fail` at 80% of auto-scored items. `needs_review` lists missed
  `data-point` values. No emoji self-grade row.
- ≥80%: unit passed — log `pass` in `progress-log.md`.
- <80%: generate a targeted mini-practice worksheet for the missed points (type P) **and**
  the retake file in `gt/retakes/` (see Filename above), then point Sam at those. Skip
  generation only if he says to skip.

## Scoring rules
- Auto-scored: all MCQ (C, D, F comprehension) plus bank-fill plus P2 `.item[data-order]`.
  The paste-report counts these. **≥10 auto-scored items** on every GT.
- Production (E) is not auto-scored; Sam can add notes in the report's `notes:` line.
- The pass threshold (80% of auto-scored items) is a guideline recorded in the log, not a
  hard gate — Sam decides whether to advance or remediate.

## Generation rules specific to GT
1. **Coverage symmetry**: every cluster point must appear in at least one C–F item AND have
   an explanation card in section A — the test never quizzes an unexplained point.
2. Items must NOT reuse example sentences from the inventory or from section A verbatim;
   write fresh sentences in the topic context, with level-appropriate vocabulary.
3. Cluster points whose official 2025-syllabus placement is higher than the test level
   (see cluster cross-ref notes) may be included (they're in the wiki cluster) but their
   vocabulary must stay in the 2025 cumulative list; gloss anything above.
4. Log the result in `progress-log.md` with score, verdict, and missed points.
