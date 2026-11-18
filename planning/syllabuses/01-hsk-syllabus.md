# HSK Study Syllabus — Structured Introduction Sequence

This syllabus defines the order in which grammar clusters and vocabulary batches are
introduced and tested, so any agent can generate "the next worksheet" without asking Sam
what comes next. Progress state lives in `progress-log.md`.

## Worksheet types

| Code | Type | Blueprint | Unit | When |
|---|---|---|---|---|
| P | Practice | `blueprints/01-practice-worksheet-blueprint.md` | ONE official grammar point (appendix ID) | core learning step |
| GT | Grammar unit test | `blueprints/02-grammar-test-blueprint.md` | ONE cluster (`L{n}-CL{kk}`) | after a cluster's P worksheets |
| VT | Vocabulary test | `blueprints/03-vocabulary-test-blueprint.md` | ONE thematic word batch (20–30 words) | after every 1–2 clusters |

## The unit cycle

For each level, the syllabus walks two parallel tracks that share the topic rotation:

```
… → [P worksheet: point 1 of cluster] → [P worksheet: point 2] → … → [GT: cluster test]
→ (pass? → next cluster;  fail? → targeted P worksheet(s) on missed points → GT retake
   in `gt/retakes/`; generate that retake as soon as the fail is logged, unless Sam skips)
Vocabulary track runs alongside: [VT: topic batch 1] → [VT: topic batch 2] → …
```

**Interleaving rule**: after each cluster unit (P…→GT), do the next vocabulary unit (VT)
before starting the next cluster. If the GT failed, insert remediation first. This gives
roughly one VT per 1–2 clusters — enough batches to cover a level's cumulative new words
over the level (L1: 300 new words ≈ 11 batches of ~27; L2: 251 ≈ 9; L3: 449 ≈ 17;
L4: 1000 ≈ 36; L5: 1600 ≈ 57; L6: 1800 ≈ 64 — the syllabus does not need to finish all
batches before moving levels; see Level progression below).

## Level {n} — content sources

Per level, in order:

1. **Grammar clusters**: follow cluster order in `references/03-grammar-inventory.md`
   (## HSK {n} clusters). The wiki order is the textbook teaching order. For each cluster:
   - Cover its points with P worksheets. A point is worth its own P worksheet when it has
     an official appendix ID and is substantive (sentence patterns, complements, complex
     sentences, fixed formats). Small/support points (single particles, single adverbs
     from the support inventory) are bundled: one P worksheet can anchor one main point
     while drilling several cluster siblings as secondary content.
   - Rule of thumb: cluster with 1–4 points → 1–2 P worksheets; 5–15 points → 2–4 P
     worksheets, each anchoring a different point, siblings as distractor context.
   - **Comparison clusters** (Category 相似语法点辨析) need no P worksheets of their own —
     they are tested inside the GT of their parent cluster (e.g. 再 vs 又 items in the
     HSK3 Adverbs GT). Exception: a comparison cluster may anchor one P worksheet if Sam
     requests focused contrast practice.
   - **Skip or merge judgment**: some clusters are single trivial points (e.g. HSK2
     Conjunctions = filler 那个). Merge such clusters into the nearest related cluster's
     unit; note the merge in the log.
2. **Vocabulary topics**: follow that level's 话题大纲 list in `references/02-level-guide.md`
   (one topic per VT batch). Rotate topics for P worksheets' contexts in the same order.

## Level progression

- A level is "done" when every non-merged cluster has a logged pass. Vocabulary batches
  continue across levels cumulatively — unfinished batches of level n continue into n+1
  interleaved with new-level units (review sections will reinforce them).
- Before starting level n+1, generate one **level-entry GT-lite**: the next level's first
  cluster test doubles as a placement check. If it's a disaster (<50%), fall back one level
  for a refresher cycle.
- Sam may jump anywhere at any time; when he requests off-sequence content, generate it,
  but record it in the log so the sequence tracks remain accurate.

## Review protocol (all worksheet types)

- Every worksheet's 温故知新/review content comes from `progress-log.md`:
  the most recent unit, a unit from ~3 back, and a unit from ~7–10 back.
- Any word or point logged as "needs review" is REQUIRED content of the next worksheet's
  review section and of the next VT's section C / GT's section C respectively.
- GT/VT retakes live in `courses/hsk{L}/{gt|vt}/retakes/` (`…-r2.html`, then `-r3`…).
  Generate the retake file automatically when a <80% score is logged, unless Sam skips.
  A completed retake replaces (not appends to) the failed attempt's row; missed points
  from the failed attempt stay flagged until a subsequent pass-level mention. If Sam
  skips the retake, leave the fail row in place and advance.

## Unit numbering and logging

- Worksheet IDs: `hsk{L}-ws{NNN}` (P) · `hsk{L}-gt-CL{kk}[-rN]` (GT) · `hsk{L}-vt-{NN}` (VT).
- Every generated worksheet appends to `progress-log.md` (P: point + topic; GT: cluster +
  score + verdict + missed points; VT: topic + score + verdict + missed words).
- The "next unit" question is answered by: first unpassed cluster in current level order →
  its next uncovered point (P) or the GT if all points covered; if a cluster just passed →
  next vocabulary topic without a VT; if vocab is also done → next cluster; level done →
  next level's entry sequence.

## Placement (first run)

When Sam starts: ask for (or infer from a sample) his level. Default recommendation:
start at HSK 2 cluster order if HSK1 GT-lite (a quick 5-item R4 over L1-CL06 Particles +
L1-CL13 Question Forms) feels trivial; start at HSK 1 otherwise. Vocabulary track starts
at the current level's first topic regardless — VT batches reinforce lower-level words by
design (70/30 rule in the VT blueprint).
