# Question Type Catalog

Every item on a worksheet must use one of these types. Each entry: ID, where it may appear
(section + levels), the spec, generation rules, distractor rules, an example, and the HTML
component it uses. Component implementations live in `templates/worksheet-template.html`.

Legend: L1…L6 = HSK level suitability. ✔ = recommended, ○ = usable sparingly, — = don't use.

---

## W — Warm-up / input (Section A only)

### W1 Flip-card pattern demo
- **Levels**: all | **Component**: `flip-card`
- **Spec**: Front shows one natural sentence using the target pattern (in the topic
  context). Back shows the same sentence with the pattern highlighted, the pattern formula
  (e.g. `S + 把 + O + V + 结果补语`), and a one-line English note on what it expresses.
- **Rules**: Sentences must be at mid-level difficulty for the target level (the learner
  should parse them successfully). No pinyin on the front; hover a dashed word anywhere
  for ruby pinyin.
- **Example** (L3, 把): Front: 我把新的地图挂在墙上了。 Back: formula + note "把 marks that
  the action was applied to the object AND produced a result (挂在了墙上)."

### W2 Sentence-half matching (pattern focus)
- **Levels**: L2–L6 | **Component**: `match` (click left half → click right half)
- **Spec**: 3–4 sentence beginnings matched to endings; every complete sentence uses the
  target pattern.
- **Distractor rules**: every wrong pairing must still be grammatical-looking and use
  level vocabulary — ideally a classic wrong-scope error for the pattern
  (e.g. matching 把 with a bare verb with no result, at levels where that's ungrammatical).

---

## R — Recognition / selection

### R1 MCQ fill-in (particle / pattern word / function word)
- **Levels**: all | **Component**: `mcq`
- **Spec**: A sentence with a blank `( )`; 3–4 options; exactly one correct.
- **Generation rules**: The sentence tests the target pattern's *form* (which word/particle
  fits), not just meaning. At least one distractor must be a **classic learner error** for
  the pattern: 把/被, 了/着/过, 就/才, 二/两, 想/要, 会/能, A一AB vs ABAB reduplication, etc.
- **Example** (L2, 着-持续): 墙上挂（ ）一张地图。 A 着 ✔ B 了 C 过 D 的
- **Key must explain**: the rule + why the tempting distractor fails.

### MCQ stem variety (R1 / R2 / R4 / VM1 / L1 / L3)
- In any stretch of **4 consecutive MCQs**, do not repeat the same stem frame. Rotate among:
  blank fill, choose-the-correct-sentence, true/false, English scenario, reverse gloss (EN→ZH),
  "which is wrong", odd-one-out.
- Keep rotating the correct-answer letter (A/B/C/D).

### R2 Choose the correct sentence (form judgment)
- **Levels**: L2–L6 | **Component**: `mcq`
- **Spec**: 3–4 full sentences, one uses the pattern correctly, others violate one specific
  constraint of it (word order, required complement, semantic constraints like
  把 needing a definite/referential object).
- **Rules**: Each wrong sentence violates exactly ONE constraint and must be wrong for a
  reason nameable in the key. Never make an item where two sentences are both acceptable.
- **Example** (L3, 把): A 我把作业做完了。✔ B 我把作业做。C 我做了把作业完。D 我把想家了。

### R3 Usage-subtype discrimination
- **Levels**: L3–L6 (only for patterns with sub-uses) | **Component**: `mcq` or `classify`
- **Spec**: Given one sentence, choose which of 3–4 listed *uses/meanings* of the pattern it
  instantiates (e.g. 着: state-continuation vs action-continuation vs accompanying action;
  了1 completion vs 了2 change-of-state).
- **Rules**: Only for patterns the official 语法大纲 explicitly splits into sub-uses.

### R4 Cluster scenario MCQ (which grammar point fits?)
- **Levels**: all | **Component**: `mcq`
- **Usage**: Core of grammar unit tests (blueprints/02 section C); also usable inside
  practice worksheets' B section when the anchor point has close siblings.
- **Spec**: A mini-scenario (Chinese situation sentence with a blank, or an
  English-described situation) is presented; the options are 3–4 **grammar points from the
  same cluster** (`L{n}-CL{kk}` in `references/03-grammar-inventory.md`), labeled with key
  word + pattern (e.g. `A. 把+O+V+结果` `B. 被+doer+V`).
- **Generation rules**:
  - Options MUST all be members of the same cluster (borrow from the nearest cluster of
    the same level only if the cluster has <3 points, and say so in the key).
  - The scenario must contain a semantic cue that selects exactly one point (e.g. "object
    ends up somewhere" → 把; "speaker observes a change" → 了2); the key names the cue.
  - For **comparison clusters** (Category 相似语法点辨析), every item contrasts exactly two
    member points (e.g. 不 vs 没), the item sentences differing minimally.
  - Rotate correct-answer positions; each cluster member should be the correct answer
    somewhere in the section when item count allows.
- **Example** (L3-CL16 Sentence Patterns): Scenario: 这个句子想说"门现在是关着的，是我关的":
  门（　）我关上了。A. 被 ✔ B. 把 C. 给 D. 让 — key: the receiver 门 is the subject, so
  passive 被; 把 would need 我把门关上了; 让/叫 express causation, not realized result.


---

## P — Controlled production

### P1 Typed fill-in (open blank)
- **Levels**: all (character output) | **Component**: `typed`
- **Spec**: A sentence missing a word or short phrase the learner must type in characters.
  The key gives the expected word(s) + common acceptable alternatives + typical misspellings
  with corrections.
- **Rules**: Exactly one answer family is correct. Do NOT use for characters with tricky
  homophones unless context forces one answer.

### P2 Sentence scramble (word-order)
- **Levels**: all | **Component**: `order-tiles`
- **Spec**: The official exam format (HSK4/5 书写第一部分) made interactive: word/phrase tiles
  clicked in order rebuild the sentence. 5–10 tiles at L1–3, 6–12 at L4–6.
- **Rules**: Exactly one defensible order. Tiles must be genuinely reorderable-looking, not
  trivially linear (a bare 时间词 at the start every time is fine, but vary positions).
  Include the target pattern's fixed positions among the movable material. If a sentence has
  a particle that could attach two places with different meanings, don't use it.
- **Scramble (required)**: never write tiles in the correct sentence order in HTML — left-to-right
  clicking must not be the answer. Prefer **phrase chunks** (2–4 characters) mixed with single
  function words, not a 1-character chain. At least one chunk must be a tempting wrong grouping
  (e.g. offering `比一天` as a tile while the correct split is `一天` + `比`).
- **Scoring**: the `.item` carries `data-order="tile|tile|…"` (exact click sequence, `|`-joined).
  The engine shuffles `.tiles` on load and on 重来; paste-report auto-scores this item.

### P3 Error finding & correction
- **Levels**: L2–L6 | **Component**: `mcq` (find error) + optional `typed` (fix it)
- **Spec**: One sentence with exactly one error; learner picks the wrong segment (or types
  the fix). The error must be a real, common learner error of the target pattern
  (word order, missing complement, wrong aspect, over-generalized rule).
- **Rules**: The rest of the sentence must be impeccable. Never two errors. The key names
  the violated rule.

### P4 Sentence transformation (rewriting with the pattern)
- **Levels**: L2–L6 | **Component**: `typed`
- **Spec**: Given sentence A, rewrite it using the target pattern with (near-)identical
  meaning (e.g. 他关上了门 → 他把门关上了; 这个问题我不会回答 → 这个问题我回答不出来).
- **Rules**: The transformation must be truth-preserving and natural. Provide model answer
  + acceptable variants + one wrong version with its reason.

### P5 Substitution table drill
- **Levels**: L1–L2 mainly | **Component**: static table + `typed` (optional)
- **Spec**: A small grid (subjects × verbs/objects × complements) with instructions to
  build 2–3 sentences from it aloud, then type the best one. Key gives one model per row.
- **Rules**: Every cell combination must produce a grammatical sentence — verify the full
  cross product.

---

## L — Listening simulation (Section C)

The dialogue itself is generated content, not a question type. These are the item types
that hang off it.

### L1 Dialogue comprehension MCQ
- **Levels**: all | **Component**: `mcq`
- **Spec**: After reading (and reading aloud) the dialogue, answer 1–2 questions about
  content. At least one question's answer hinges on a use of the target pattern
  (e.g. "他最后把书怎么了？" → 挂在了墙上).
- **Distractors**: events from the dialogue but wrong roles/times, and one plausible
  misreading of the pattern itself.

### L2 Dialogue blank-fill (pattern harvesting)
- **Levels**: L2–L6 | **Component**: `typed` or `mcq`
- **Spec**: Show the dialogue again with the pattern occurrences blanked; learner restores
  them from memory + grammar knowledge. Key restores the exact line and notes the
  sub-pattern used.

### L3 True/false on statements (HSK4-style)
- **Levels**: L2–L6 | **Component**: `mcq` (二选一)
- **Spec**: 2–3 statements like the HSK4 听力第一部分 format (★ 他把礼物寄给妈妈了。
  （√/×）), each paraphrasing or mis-paraphrasing dialogue content. The wrong ones twist
  the target pattern's meaning (different result, different object, reversed roles).
- **Rules**: Statements must be decidable from the dialogue alone.

### TTS & read-aloud support (all listening sections)
- Every dialogue line gets an optional 🔊 button (`tts` component, `speechSynthesis`,
  `lang="zh-CN"`). Transcript is ALWAYS visible (Sam's design decision). Instruction tells
  Sam to read the dialogue aloud twice before answering. Line-by-line reveal mode
  (`reveal-lines` component) supports shadowing: read the next line yourself, then reveal.
- **Gendered voices**: 女 / 男 speakers must use different voices. Infer from `.speaker`
  (`女` → female, `男` → male); named speakers take `data-gender="f|m"` on the `.line`.
  Prefer named zh-CN voices (Huihui / Yaoyao / Xiaoxiao vs Kangkang / Yunyang). If the OS
  only has one zh voice, fall back to pitch `1.15` (female) vs `0.85` (male). Wait for
  `voiceschanged` before the first speak.

---

## E — Exam-style (Section D)

Formats mirror the level's official past-paper structure (see `references/02-level-guide.md`). These
are the adapted interactive versions of the paper formats Sam will face.

### E1 Word-bank fill (HSK1–2 阅读 P4 style)
- **Levels**: L1–L2 | **Component**: `bank-fill`
- **Spec**: 6 bank words (A–F), 4–5 sentences each missing one word. Official instruction:
  选词填空. Click a bank word to place it. Words may be reused... actually per official
  format each word is used at most once; keep 1–2 unused words as distractors.
- **Rules**: Two bank words must be same POS class to stay tricky (e.g. 量词 本/张/件).
  Every item includes a **重来 reset button** that clears all placed words and restores
  the bank, so the learner can retry before checking (per Sam's request).

### E2 Q–A matching (HSK1–3 阅读 P3 style)
- **Levels**: L1–L3 | **Component**: `match`
- **Spec**: 4–6 questions matched to 6–8 answers (official format: extra answers as
  distractors). At least one Q or A uses the target pattern.

### E3 Cloze passage (HSK4–6 阅读第二部分 style)
- **Levels**: L3–L6 | **Component**: `mcq` items inside one passage
- **Spec**: One short passage (L3: ~80字, L4: ~120字, L5: ~180字, L6: ~250字) with 3–4
  blanks, each blank a 4-option MCQ. Passage uses the target pattern at least once.
  Topic from 话题大纲. Blanks test the target pattern + function words.

### E4 Choose-the-summary / main-idea (HSK6 style)
- **Levels**: L5–L6 | **Component**: `mcq`
- **Spec**: Short passage (150–250字), choose the statement that best captures its main
  point. Wrong options are true-in-text but partial, or too broad. The passage should
  feature the target pattern prominently enough that pattern comprehension helps.

### E5 Picture-free sentence writing from given words (HSK4 书写 P2 / HSK5 书写 P2 style)
- **Levels**: L3–L5 | **Component**: `typed`
- **Spec**: Official-style: given 3–5 words (must all be used), write ONE sentence. Include
  the pattern's key word among the givens (e.g. 把, 或者, 不但…而且 pair). Key gives a model
  + acceptable variants.

### E6 Essay from given words (HSK6 书写 style, adapted)
- **Levels**: L6 | **Component**: `typed` (multiline)
- **Spec**: Given 5 words from the level list (all must appear), write a short coherent
  passage (~200字 worksheet version; the real exam wants 400+ — say so in the instructions).
  Key gives a model passage + the scoring logic the agent uses (structure, pattern use,
  word use), not just a sample.

---

## F — Free production (Section E)

### F1 Personal-guided writing
- **Levels**: all | **Component**: `typed`
- **Spec**: 2–3 specific questions about Sam's real life forcing pattern use
  ("你昨天到家后先把什么放下了？用'把'回答。"). Specific > generic. Key = model answers +
  variants + common mistake with reason.

### F2 Translation
- **Levels**: L3–L6 | **Component**: `typed`
- **Spec**: 1–2 English sentences whose natural translation REQUIRES the pattern. Key gives
  the model translation + notes on what an over-literal translation gets wrong.
- **Rules**: The English must be idiomatic (not itself translated-sounding). Only patterns
  with a genuine cross-language contrast make good F2 items.

### F3 Situation response
- **Levels**: L1–L2 (instead of F2) | **Component**: `typed`
- **Spec**: A mini-scene in Chinese (2–3 sentences), then a prompt: "你怎么说？用 …回答。
  Type what you would say." Key = model responses + variants.

### F4 Mini-composition
- **Levels**: L5–L6 | **Component**: `typed` (multiline)
- **Spec**: 80–150字 guided paragraph using the pattern at least twice; situation drawn
  from the topic syllabus. Key = model + variant opener/closer ideas.

---

## V — Review (Section F)

### V1 Mixed recall MCQ
- **Levels**: all | **Component**: `mcq`
- **Spec**: Quick items recycling grammar/vocab from `review_sources`. Each item labeled
  with source worksheet ID (e.g. "from hsk3-ws-011: 越来越"). 2–3 items.

### V2 Transform with old pattern
- **Levels**: L2–L6 | **Component**: `typed`
- **Spec**: One sentence (often using the CURRENT worksheet's pattern!) to rewrite with a
  PREVIOUS worksheet's pattern — interleaving old and new is the point
  (e.g. current 把: 我把房间打扫干净了 → rewrite with 越来越: 房间越来越干净).

### Paste-report (always last on P / GT / VT)
- **Component**: `scorebox` — **生成报告 / Copy report** auto-counts `.mcq` +
  `.item[data-answers]` bank-fill, then renders a paste-ready `<pre>` block
  (`worksheet_id`, `type`, `score`, `verdict`, `needs_review`, `notes`). P: `verdict: —`.
  GT/VT: `pass`/`fail` at 80%. Sam pastes the block into the course chat.

---

## VM — Vocabulary test items (blueprints/03 sections C–F)

Vocabulary tests are organized by thematic word batch, not by grammar. All VM items are
bound to the batch's words; see `blueprints/03-vocabulary-test-blueprint.md` for batch rules.

### VM1 Meaning recognition
- **Levels**: all | **Component**: `mcq`
- **Spec**: Two directions: ① word in characters → choose English gloss (4 gloss options);
  ② English meaning → choose the Chinese word (4 batch words as options).
- **Rules**: Distractors are glosses/words of OTHER batch words (same POS where possible)
  or classic confusables; never hinge an item on a dictionary nuance the gloss doesn't
  support. Item carries `data-word` (the word tested) for score-summary review collection.

### VM2 Pinyin ↔ character
- **Levels**: all | **Components**: `mcq` + `match`
- **Spec**: ① Select the correct tone-marked pinyin for a word — distractors are wrong-tone
  and tone-mark-placement variants of the same syllable; ② match 4–6 words to pinyin.
- **Rules**: Prioritize easily-confused pronunciations: tone pairs, 多音字, neutral tones
  (东西 dōngxi), look-alike characters (那/哪). Base tone written for sandhi (per HSK).

### VM3 Usage in context (collocation cloze)
- **Levels**: all | **Components**: `bank-fill` or `mcq`
- **Spec**: Sentence with a blank where exactly one batch word fits by collocation or
  context. Bank fill: 6–8 words with 1–2 extras; MCQ when the distinction is fine
  (见面 vs 看见). Bank-fill items include the 重来 reset button. Key states the
  collocation/context cue.
- **Rules**: Topic-context sentences, grammar within level only (no grammar surprises on
  a vocabulary test). Item carries `data-word`.

### VM4 Word production
- **Levels**: all | **Component**: `typed`
- **Spec**: "用『word』写一句话" or a situation prompt requiring the assigned word. Assign
  the trickiest batch words (prioritize words flagged in `progress-log.md`).
- **Rules**: Key = model sentence + variants + wrong-with-reason (bad collocation, wrong
  measure word, wrong valence like *见面你).

---

## Paste-report (every worksheet's final block)

- **Component**: `scorebox` — present on P, GT, and VT.
- **Behavior**: **生成报告 / Copy report** counts every `.mcq` marked right/wrong, every
  `.item[data-answers]` bank-fill, and every `.item[data-order]` P2 scramble; shows
  `correct / total`, the percentage, and a copy-ready report. Missed items contribute
  `data-point` (GT) or `data-word` (VT/P) to `needs_review`. Body must have `data-id` and
  `data-type`.
- **Rules**: percentage covers auto-scored items only. **Every worksheet must have ≥10
  auto-scored items** (MCQ + bank-fill + P2). P: `verdict: —`. GT/VT: ≥80% `pass`
  else `fail` (remediate then retake), matching `syllabuses/01-hsk-syllabus.md`.

---

## Component reference

All components are implemented once in `templates/worksheet-template.html` with class-based
behavior. Copy the file; don't re-implement.

| Component | Behavior |
|---|---|
| `.zh` + `data-py` | Chinese text; hover shows ruby pinyin. No Show-all button. Dashed underline + `cursor: help`. |
| `mcq` | Options as buttons; click selects; 对答案 button reveals ✓/✗ + explanation for the chosen one, and marks the correct option. |
| `typed` | Free text input; 对答案 reveals model answer(s) + explanation. No auto-grading (Chinese typing variants make exact match brittle). |
| `order-tiles` | Click tiles to append to the answer line; engine shuffles `.tiles` on load/重来; `data-order` auto-scores; 对答案 reveals correct order + explanation. |
| `bank-fill` | Click bank word → clicks blank slot to place; 对答案 checks; a 重来 reset button clears all placements and restores the bank. |
| `match` | Click left item then right item to link; lines/labels connect; 对答案 checks. |
| `flip-card` | Click flips front/back (CSS 3D). |
| `reveal-lines` | Dialogue lines revealed one at a time (显示下一句 button) for shadowing. |
| `tts` | 🔊 button reads its target text with `speechSynthesis` `zh-CN`; female vs male voice from 女/男 (or `data-gender`); pitch fallback if only one zh voice. |
| `scorebox` | Paste-report on every worksheet: counts MCQ + bank-fill, shows % + copy-ready block (`verdict` pass/fail on GT/VT, `—` on P). |
| `data-point` / `data-word` | Item metadata (on `.mcq` or `.item`) naming the cluster point / batch word tested; consumed by the paste-report. |
