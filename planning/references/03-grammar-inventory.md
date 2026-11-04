# Grammar Inventory (HSK 1–6)

Two coordinated layers, both machine- and human-readable:

1. **Cluster spine (primary)** — grammar points grouped into **133 clusters of similar points**
   (502 points), extracted from the Chinese Grammar Wiki files in `Z:\Chinese\grammar\`
   (HSK 1–6, old wiki scheme). Each cluster has a stable ID `L{n}-CL{kk}`.
   - **Unit tests** (`blueprints/02-grammar-test-blueprint.md`) test an entire cluster.
   - **Scenario MCQs** (question type R4) ask "which grammar point in this cluster fits this
     scenario?" — the cluster's point list is the option pool.
   - **Comparison clusters** (Category: 相似语法点辨析) are the highest-value R4 sources.
2. **Official 2025 syllabus appendix** — the 语法大纲 (PDF pages 383–400) with stable IDs like
   `L3-SP-1 把字句1`. **Practice worksheets** (`blueprints/01-practice-worksheet-blueprint.md`)
   still anchor to ONE appendix point at a time. Each cluster header cross-references appendix IDs.

**Level caveat**: cluster levels follow the OLD wiki HSK scheme (matching the past papers in
`hsk1\`…`hsk6\`); the appendix follows the 2025-11 syllabus. Cross-reference lines note
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

## HSK 1 clusters

HSK 1 has **15 clusters / 54 points** (wiki old-HSK scheme). Cluster order below is the wiki's teaching order — the order the syllabus introduces them.

### L1-CL01 · Adverbs 副词
*Category: 词类 · 5 points · Official 2025 syllabus: L1-AS-3 进行态 · 否定/程度/范围/关联副词（support）*

| Point | Pattern | Example |
|---|---|---|
| Expressing actions in progress with "zai" | (正) 在 + Verb | 我们 正在 吃饭。 |
| Negation of "you" with "mei" | 没 + 有 | 我 没有 钱 。 |
| Standard negation with "bu" | 不 + Verb / Adj. | 他们 不 是 坏 孩子。 |
| The "all" adverb "dou" | 都 + Verb / Adj. | 我们 都 住 在 上海。 |
| The "also" adverb "ye" | 也 + Verb / Adj. | 昨天 很 冷，今天 也 很 冷。 |

### L1-CL02 · Adverbs with Adjectives 副词修饰形容词
*Category: 词类 · 2 points · Official 2025 syllabus: 程度副词 多/很/太/有（一）点儿（support）*

| Point | Pattern | Example |
|---|---|---|
| Asking about degree with "duo" | Subj. + 多 + Adj. ? | 他 多 高？ |
| Expressing "not very" with "bu tai" | 不太 + Adj. | 他 不太 高兴 。我 不太 喜欢。 |

### L1-CL03 · Conjunctions 连词
*Category: 词类 · 1 points · Official 2025 syllabus: 连词 和（support）*

| Point | Pattern | Example |
|---|---|---|
| Expressing "and" with "he" | Noun 1 + 和 + Noun 2 | 我 和 他 都 不 去。 |

### L1-CL04 · Nouns 名词
*Category: 词类 · 3 points · Official 2025 syllabus: 时间/方位名词（support）；注：以前/以后 在官方新大纲属三级 L3-FX-5*

| Point | Pattern | Example |
|---|---|---|
| After a specific time with "yihou" | Time / Verb + 以后 | 10点 以后 ，我 不 在 家。 |
| Before a specific time with "yiqian" | Time / Verb + 以前 | 十 点 以前，我 在 家。 |
| Time words and word order | Subj. + Time⋯⋯ / Time + Subj.⋯⋯ | 我 明天 有 空。/ 明天 我 有 空。 |

### L1-CL05 · Numbers 数词
*Category: 词类 · 7 points · Official 2025 syllabus: L1-WC-3 数量短语 · L1-WC-4 时间表示法 · L1-EX-1 序数/钱数*

| Point | Pattern | Example |
|---|---|---|
| Age with "sui" | Subj. + Number + 岁 | 我 20 岁 。 |
| Measure word "ge" | Number + 个 + Noun | 一 个 人 。 |
| Structure of dates | Number + 年 + Number + 月 + Number + 日 | 今天 是 2011年 11月 11日/号 。 |
| Structure of days of the week | 星期 + Number | 今天 星期三 。 |
| Structure of numbers | Number + Unit | 三 百 五 十 九。 |
| Structure of times (advanced) | Number 1 + 点(钟) + Number 2 + 分 | 现在 十一点十八分 。 |
| Structure of times (basic) | Number + 点(钟) | 现在 十一点 。 |

### L1-CL06 · Particles 助词
*Category: 词类 · 9 points · Official 2025 syllabus: L1-AS-1 了1 · L1-AS-2 了2 · 结构助词 的 · 语气助词 吗/呢/吧（support）*

| Point | Pattern | Example |
|---|---|---|
| Expressing close possession without "de" | Pronoun + Noun | 我 女朋友 |
| Expressing completion with "le" | Subj. + Verb + 了 + Obj. | 我 吃 了 两 个 苹果。 |
| Expressing "not anymore" with "le" | 不 / 没(有) + Verb Phrase + 了 | 我 不 想 吃 了 。 |
| Expressing "now" with "le" | New Situation + 了 | 吃饭 了！ |
| Expressing possession with "de" | Noun 1 + 的 + Noun 2 | 我 的 老师 |
| Questions with "ne" | ⋯⋯呢 ? | 我 很 好。你 呢 ? |
| Sentence-final interjection "a" | ⋯⋯啊 | 是 啊！谁 啊？ |
| Softening speech with "ba" | ⋯⋯吧 | 这样 不 太 好 吧。 |
| Suggestions with "ba" | Command + 吧 | 我们 走 吧 。 |

### L1-CL07 · Verbs 动词
*Category: 词类 · 7 points · Official 2025 syllabus: L1-SP-1 是字句 · L1-SP-2 有字句 · L1-SP-3 存现句 · 连动句（support）*

| Point | Pattern | Example |
|---|---|---|
| Directional verbs "lai" and "qu" | 来 / 去 + Place | 我 来 上海 一 年 了。 |
| Expressing existence in a place with "zai" | 在 + Place | 老师 在 上海 。 |
| Expressing existence with "you" | Place + 有 + Obj. | 我们 学校 有 很 多 学生。 |
| Expressing possession with "you" | Subj. + 有 + Obj. | 我 有 钱。 |
| Polite requests with "qing" | 请 + Verb | 请 坐 。 |
| Using the verb "jiao" | 叫 + Name | 你 叫 什么 名字 ？ |
| Using the verb "qu" | 去 + Place | 我 去 学校。 |

### L1-CL08 · Auxiliary verbs 能愿动词
*Category: 词类 · 4 points · Official 2025 syllabus: L1-WC-1 能愿动词 会/能/想/要/可以*

| Point | Pattern | Example |
|---|---|---|
| Expressing ability or possibility with "neng" | 能 + Verb | 中文 这么 难，你 能 学 好 吗？ |
| Expressing a learned skill with "hui" | 会 + Verb | 他 会 说 中文 。 |
| Expressing "will" with "hui" | 会 + Verb | 明天 你 会 来 吗？ |
| Expressing "would like to" with "xiang" | 想 + Verb | 我 想 去。 |

### L1-CL09 · Verb phrases 动词短语
*Category: 词类 · 3 points · Official 2025 syllabus: L1-QT-2 特指问（怎么）· 没有+V（support）· 在+处所+V*

| Point | Pattern | Example |
|---|---|---|
| How to do something with "zenme" | 怎么 + Verb ? | 怎么 走? |
| Indicating location with "zai" before verbs | Subj. + 在 + Place + Verb | 我 在 上海 工作。 |
| Negation of past actions with "meiyou" | 没有 + Verb | 我 没有 去 酒吧。 |

### L1-CL10 · Basics 基础句型
*Category: 句法结构 · 4 points · Official 2025 syllabus: L1-SP-1 是字句 · 动词/形容词谓语句（support）· 太+Adj+了*

| Point | Pattern | Example |
|---|---|---|
| Basic sentence order | Subj. + Verb (+ Obj.) | 我 爱 你 。 |
| Connecting nouns with "shi" | A + 是 + B | 我 是 学生 。 |
| Expressing "excessively" with "tai" | 太 + Adj. + 了 | 太 好 了 ! |
| Simple "noun + adjective" sentences | Noun + 很 + Adj. | 我 很 好。 |

### L1-CL11 · Noun Phrases 名词短语
*Category: 句法结构 · 1 points · Official 2025 syllabus: 数量短语 一些（support）*

| Point | Pattern | Example |
|---|---|---|
| Expressing "some" with "yixie" | 一些 + Noun | 这里 有 一些 咖啡。 |

### L1-CL12 · Numbers and Measure Words 数量表达
*Category: 句法结构 · 2 points · Official 2025 syllabus: L1-EX-1 钱数 · 几+量词*

| Point | Pattern | Example |
|---|---|---|
| Counting money | Number + 块 / 元 (+ Number + 毛 / 角) (+ 钱) | 给 你 五 块 三 毛。 |
| Measure words in quantity questions | 几 + Measure Word (+ Noun) ? | 几 个 人？ |

### L1-CL13 · Question Forms 疑问句式
*Category: 句法结构 · 4 points · Official 2025 syllabus: L1-QT-1 是非问 · L1-QT-2 特指问 · L1-QT-3 正反问 · 了吗*

| Point | Pattern | Example |
|---|---|---|
| Asking how something is with "zenmeyang" | ⋯⋯怎么样？ | 你 最近 怎么样 ？ |
| Placement of question words | 什么 / 什么时候 / 谁 / 哪儿 / 为什么 / 怎么 | 你 是 谁 ？你 在 哪儿 ？ |
| Questions with "le ma" | Verb + 了 + 吗？ | 你 吃饭 了 吗 ？ |
| Yes-no questions with "ma" | ⋯⋯吗？ | 他 是 老板 吗 ? |

### L1-CL14 · Sentence Patterns 句式
*Category: 句法结构 · 1 points · Official 2025 syllabus: 是…的 — 官方新大纲属二级 L2-SP-2*

| Point | Pattern | Example |
|---|---|---|
| The "shi... de" construction for emphasizing details | 是⋯⋯ 的 | 你 是 怎么 来 的？ |

### L1-CL15 · Adverbs 副词
*Category: 相似语法点辨析 · 1 points · Official 2025 syllabus: L1-AS-3 进行态 · 否定/程度/范围/关联副词（support）*

| Point | Pattern | Example |
|---|---|---|
| Comparing "bu" and "mei" | 不 vs 没 | 我 今天 晚上 不 吃饭。昨天 晚上 我 没 吃饭。 |


## HSK 2 clusters

HSK 2 has **22 clusters / 78 points** (wiki old-HSK scheme). Cluster order below is the wiki's teaching order — the order the syllabus introduces them.

### L2-CL01 · Adverbs 副词
*Category: 词类 · 11 points · Official 2025 syllabus: L2 副词（support）· L2-FX-1 要/快要/就要…了 · L2-FX-3 都…了 · 再2/就1/就2/还是1/别*

| Point | Pattern | Example |
|---|---|---|
| Continuation with "hai" | Subj. + 还 + Verb Phrase / Adj. | 你 还在 看 书 ？ |
| Emphasis with "jiushi" | 就是 + Verb | 我 父母 就是 不 让 我 一个人 去 。 |
| Emphasizing quantity with "dou" | 大家 / 很多人 + 都⋯⋯ | 很 多 地方 都 有 wifi。 |
| Expressing "about to" with "jiuyao" | 还有 + Time Period + 就要 + Verb Phrase + 了 | 还有 五 天 就要 放假 了 。 |
| Expressing "again" in the future with "zai" | 再 + Verb | 我 下 次 再 来。 |
| Expressing "already" with "dou" | 都 + Time + 了 | 都 九点 了 ，快点 起床 ！ |
| Expressing "already" with "yijing" | 已经⋯⋯了 | 他 已经 走 了 。 |
| Expressing "and also" with "hai" | 还 + Verb | 她 有 一个 弟弟，还 有 一个 妹妹。 |
| Expressing earliness with "jiu" | Subj. + Time + 就 + Verb + 了 | 我 昨晚 八 点 半 就 睡觉 了 。 |
| Expressing "then" with "jiu" | 就 + Verb Phrase | 我们 现在 有 时间，就 去吧。 |
| Negative commands with "bie" | 别 + Verb | 别走。 |

### L2-CL02 · Adverbs with Adjectives 副词修饰形容词
*Category: 词类 · 8 points · Official 2025 syllabus: L2 程度副词 多/好/最（support）· 有点儿 · 离（介词）· 更（官方属三级）*

| Point | Pattern | Example |
|---|---|---|
| Asking about degree with "duo" | Subj. + 多 + Adj. ? | 他 多 高？ |
| Expressing "a little too" with "you dian" | 有点(儿) + Adj. | 我 有点 饿 。 |
| Expressing distance with "li" | Place 1 + 离 + Place 2 + Adv. + 近 / 远 | 我 家 离 大学 很 近。 |
| Expressing "even more" with "geng" | 更 + Adj. | 我 想 找 一个 更 有钱 的 男朋友。 |
| Expressing "really" with "zhen" | 真 + Adj. | 你 女朋友 真 漂亮 。 |
| Moderating positive adjectives with "hai" | 还 + Adj. | 还 可以。还 好。 |
| Modifying nouns with phrase + "de" | Phrase + 的 + Noun | 去 北京 的 火车。今天 来 的 人。 |
| Superlative "zui" | 最 + Adj. (+ 了) | 谁 最 有钱 ？ |

### L2-CL03 · Conjunctions 连词
*Category: 词类 · 1 points · Official 2025 syllabus: 口语填充词 那个 — 无官方对应（生成时标注为口语）*

| Point | Pattern | Example |
|---|---|---|
| The filler word "neige" | ⋯⋯那个⋯⋯ | 那个⋯⋯你 可以 做 我 的 女 朋友 吗？ |

### L2-CL04 · Measure Words 量词
*Category: 词类 · 1 points · Official 2025 syllabus: 量词重叠 MW+MW（官方 L3-WC-3 量词重叠属三级）*

| Point | Pattern | Example |
|---|---|---|
| Reduplication of measure words | MW + MW | 个 个 都 很 好。 |

### L2-CL05 · Nouns 名词
*Category: 词类 · 1 points · Official 2025 syllabus: …的时候 — 官方时间表达（support，L3 范围）*

| Point | Pattern | Example |
|---|---|---|
| Expressing "when" with "de shihou" | ⋯⋯的时候 | 你 不在 的 时候，我 会 想 你。 |

### L2-CL06 · Numbers 数词
*Category: 词类 · 1 points · Official 2025 syllabus: 概数1 数词+多（L2-EX support）*

| Point | Pattern | Example |
|---|---|---|
| Indicating a number in excess | Number + 多 | 三 十 多 岁 |

### L2-CL07 · Numbers and Measure Words 数量表达
*Category: 词类 · 1 points · Official 2025 syllabus: 每+量词 · 第+数词 序数2 · 几+量+名 · 这/那+量词（support）*

| Point | Pattern | Example |
|---|---|---|
| Using "ji" to mean "several" | 几 + Measure Word + Noun | 桌子 上 有 几 本 书。 |

### L2-CL08 · Particles 助词
*Category: 词类 · 6 points · Official 2025 syllabus: L2-AS-1 着 · L2-AS-2 过 · 的2/呢4/吧2/啊1（support）*

| Point | Pattern | Example |
|---|---|---|
| Aspect particle "zhe" | Verb + 着 | 我 读 ，你 听 着 。 |
| Conceding with "ba" | ⋯⋯吧 | 那 好 吧。 |
| Expressing "already" with just "le" | Subj. + Verb Phrase + 了 | 你 应该 问 老师 。我 问 了 。 |
| Expressing experiences with "guo" | Verb + 过 | 我 去 过 中国 。 |
| Modal particle "ne" | ⋯⋯呢 ? | 我 不 要 回家 。还 早 呢 ！ |
| Using "guo" with "le" | Verb + 过 + 了 | 她 吃 过 了 。 |

### L2-CL09 · Prepositions 介词
*Category: 词类 · 5 points · Official 2025 syllabus: L2 介词 从/往/给/比/跟（support）· L2-SP-1 比较句1*

| Point | Pattern | Example |
|---|---|---|
| Basic comparisons with "bi" | Noun 1 + 比 + Noun 2 + Adj. | 你 比 我 胖 。 |
| Expressing "for" with "gei" | Subj. + 给 + Recipient + Verb Phrase | 妈妈 在 给 孩子 们 做饭 。 |
| Expressing "from… to…" with "cong… dao…" | 从⋯⋯到⋯⋯ | 从1 号 到 5 号 我 在 上海。 |
| Expressing "toward" with "wang" | 往 + Direction Word | 往 + Direction / Place + Verb |
| Using "dui" with verbs | Subj. + 对 + Person + Verb | 宝宝 对 我 笑 了。 |

### L2-CL10 · Verbs 动词
*Category: 词类 · 1 points · Official 2025 syllabus: 姓 — 称谓表达（support）*

| Point | Pattern | Example |
|---|---|---|
| Using the verb "xing" | 姓 + Surname | 你 姓 什么 ？ |

### L2-CL11 · Auxiliary verbs 能愿动词
*Category: 词类 · 4 points · Official 2025 syllabus: L1-WC-1 能愿动词延伸：要/可以（support）*

| Point | Pattern | Example |
|---|---|---|
| Auxiliary verb "yao" and its multiple meanings | 要 + Noun / 要 + Verb | 我 要 一 杯 水。 |
| Expressing "be going to" with "yao" | Subj. + 要 + Verb (+ 了) | 我 要 去 吃饭，你 去 吗？ |
| Expressing permission with "keyi" | 可以 + Verb | 这里 可以 吸烟 吗? |
| Wanting to do something with "yao" | 要 + Verb | 我 要 吃饭 。 |

### L2-CL12 · Verb phrases 动词短语
*Category: 词类 · 12 points · Official 2025 syllabus: L2-CM-1 结果补语 · V+给+O（L2-SP-6）· L2-WC-1 动词重叠 · 一下 · 动量词 · 连动句*

| Point | Pattern | Example |
|---|---|---|
| Actions in a row | (Verb Phrase 1) + (Verb Phrase 2) | 我们 去 咖啡店 喝 咖啡 吧。 |
| Expressing "together" with "yiqi" | 一起 + Verb | 我们 一起 去 吧！要 不 要 一起 吃饭？ |
| Measure words for verbs | Verb + Number + Measure Word | 做 三 次。读 两 遍 。 |
| Negative commands with "buyao" | 不要 + Verb | 不要 说 英文！ |
| Reduplication of verbs | Verb + Verb | 你 看看。 |
| Special cases of "zai" following verbs | Verb + 在 + Place | 我 住 在 北京。放 在 这里。 |
| Using "dao" to mean "to go to" | 到 + Place | 我 到 上海。 |
| Using "hao" to mean "easy" | 好 + Verb | 好 做。好 买。 |
| Verbing briefly with "yixia" | Verb + 一下 | 你 看 一下 。 |
| Verbs followed by "gei" | Subj. + Verb + 给 + Recipient + Obj. | 他 送给 我 一 束 花 。 |
| Verbs preceded by "gei" | Subj. + 给 + Target + Verb + Obj. | 现在 不要 给 他 打 电话 。 |
| Verbs that take double objects | Subj. + Verb + Indirect Obj. + Direct Obj. | 我 问 了 老师 一 个 问题。 |

### L2-CL13 · Complements 补语
*Category: 句法结构 · 5 points · Official 2025 syllabus: L2-CM-1 结果补语1 · L2-CM-2 趋向补语1 · L2-CM-3 状态补语1 · L2-CM-4 数量补语2*

| Point | Pattern | Example |
|---|---|---|
| Degree complement | Verb + 得⋯⋯ | 你 做 得 不错 。 |
| Potential complement "-bu dong" for not understanding | Verb + 不懂 | 我 听不懂 。 |
| Result complements | Verb + 好 / 完 / 错 | 我们 吃 好 了 。 |
| Result complements "-dao" and "-jian" | Verb + 到 / 见 | 听 到 了 吗 ？ |
| Result complement "-wan" for finishing | Verb + 完 (+ 了) | 我 说 完 了。 |

### L2-CL14 · Numbers and Measure Words 数量表达
*Category: 句法结构 · 4 points · Official 2025 syllabus: 每+量词 · 第+数词 序数2 · 几+量+名 · 这/那+量词（support）*

| Point | Pattern | Example |
|---|---|---|
| Expressing "every" with "mei" | 每 + Measure Word (+ Noun) | 每 个 人。每 天。 |
| Measure words for counting | Number + Measure Word + Noun | 一 个 人。一 杯 水。 |
| Measure words with "this" and "that" | 这 / 那 + Measure Word (+ Noun) | 那 个 人。这 杯 水。 |
| Ordinal numbers with "di" | 第 + Number (+ Measure Word) | 你 是 我 的 第 一 个 朋友。 |

### L2-CL15 · Question Forms 疑问句式
*Category: 句法结构 · 5 points · Official 2025 syllabus: L1-QT-3 正反问 · L2-QT-1 选择问 还是 · 反问 不是…吗（官方属三级 L3-QT-1）· tag questions*

| Point | Pattern | Example |
|---|---|---|
| Affirmative-negative question | Verb + 不 + Verb / Adj. + 不 + Adj. | 去 不 去？好 不 好 ? |
| Asking why with "zenme" | 怎么⋯⋯？ | 你 怎么 没 来？ |
| Simple rhetorical questions | 不 是…… 吗 ？ | 不 是 说好 了 吗 ？怎么 会 这样 ？ |
| Tag questions with "bu" | ⋯⋯是不是 / 对不对 / 好不好 ? | 你们 明天 来，好 不 好 ? |
| Tag questions with "ma" | ⋯⋯是吗 / 对吗 / 好吗 ? | 这样 做， 对 吗 ? |

### L2-CL16 · Sentence Patterns 句式
*Category: 句法结构 · 6 points · Official 2025 syllabus: L2-CP-2 因为…所以 · L2-SP-2 是…的 · 别+V+了 · 什么+都/也（官方属三级 L3-FX-3）*

| Point | Pattern | Example |
|---|---|---|
| Cause and effect with "yinwei" and "suoyi" | 因为⋯⋯ 所以⋯⋯ | 因为 饿 了，所以 吃饭。 |
| Expressing "about to happen" with "le" | 快 + Verb / Adj. + 了 | 快 下雨 了 。 |
| Expressing "everything" with "shenme dou" | 什么 + 都 / 也⋯⋯ | 爸爸 什么 都 知道。 |
| Expressing "stop doing" with "bie… le" | 别 + Verb + 了 | 别 哭 了，烦 死了 。 |
| The "shi... de" construction for indicating purpose | 是⋯⋯ 的 | 我 是 来 上海 旅游 的 。 |
| The "shi... de" patterns: an overview | 是⋯⋯ 的 | 你 是 哪个 学校 的 ？ |

### L2-CL17 · Basic/Simple Sentence Patterns 基本句式
*Category: 句法结构 · 1 points · Official 2025 syllabus: 每+量词+都（support）*

| Point | Pattern | Example |
|---|---|---|
| Expressing "every time" with "mei" and "dou" | 每次 + Event 1 + 都 + Event 2 | 为什么 每 次 我 来 他 都 不 在。 |

### L2-CL18 · Comparison Patterns 比较句式
*Category: 句法结构 · 1 points · Official 2025 syllabus: L2-SP-1 比较句1（…多了）*

| Point | Pattern | Example |
|---|---|---|
| Expressing "much more" in comparisons | Noun 1 + 比 + Noun 2 + Adj. + 多了 | 拼音 比 汉字 容易 多了 。 |

### L2-CL19 · Complex Sentence Patterns 复杂句式
*Category: 句法结构 · 1 points · Official 2025 syllabus: L2-CP-1 虽然…但是*

| Point | Pattern | Example |
|---|---|---|
| Expressing "although" with "suiran" and "danshi" | 虽然⋯⋯ ，但是 / 可是⋯⋯ | 虽然 渴 了，但是 不 想 喝 啤酒。 |

### L2-CL20 · Auxiliary verbs 能愿动词
*Category: 相似语法点辨析 · 1 points · Official 2025 syllabus: L1-WC-1 能愿动词延伸：要/可以（support）*

| Point | Pattern | Example |
|---|---|---|
| Comparing "yao" and "xiang" | 要 vs 想 | 我 要 一 杯 水 。 我 想 你 。 |

### L2-CL21 · Auxiliary Verbs 能愿动词辨析
*Category: 相似语法点辨析 · 1 points · Official 2025 syllabus: 相似语法点辨析 — 用作 R4 场景选择题的题源*

| Point | Pattern | Example |
|---|---|---|
| Comparing "hui," "neng," "keyi" | 会 vs. 能 vs. 可以 | 我 会 跳舞 。这里 不 能 跳舞 。我 可以 请 你 跳舞 吗 ？ |

### L2-CL22 · Numbers 数词
*Category: 相似语法点辨析 · 1 points · Official 2025 syllabus: 概数1 数词+多（L2-EX support）*

| Point | Pattern | Example |
|---|---|---|
| Comparing "er" and "liang" | 二 vs 两 | 两 个 人。二 十 二。 |


## HSK 3 clusters

HSK 3 has **22 clusters / 86 points** (wiki old-HSK scheme). Cluster order below is the wiki's teaching order — the order the syllabus introduces them.

### L3-CL01 · Adjectives 形容词
*Category: 词类 · 3 points · Official 2025 syllabus: L3-CM-4 程度补语1 极了 · 形容词重叠（L2-WC-2 延伸）· Adj+地 状语（support）*

| Point | Pattern | Example |
|---|---|---|
| Adjectives with "-ji le" | Adj. + 极了 | 这个 主意 好 极了 。 |
| Reduplication of adjectives | Adj. + Adj. | 你 应该 慢慢 地 走。 |
| Turning adjectives into adverbs | Adj. + 地 + Verb | 你 要 认真 地 学习。 |

### L3-CL02 · Adverbs 副词
*Category: 词类 · 12 points · Official 2025 syllabus: L3 副词（support）又/一直/总是/才/终于/只/几乎 · L3-CP-1 先…再 · L3-CP-5 一边…一边*

| Point | Pattern | Example |
|---|---|---|
| Expressing "again" in the past with "you" | 又 + Verb + 了 | 你 又 迟到 了 。 |
| Expressing "all along" with "yizhi" | Subj. + 一直 + Predicate | 我 一直 在 现在 的 公司 工作。 |
| Expressing "always" with "zongshi" | 总是 + Verb | 他 总是 迟到。 |
| Expressing duration of inaction | Duration + 没 + Verb + 了 | 他 已经 一 个 星期 没 洗澡 了 。 |
| Expressing "finally" with "zhongyu" | Subj. + 终于 + Predicate + 了 | 你 终于 到 了 。 |
| Expressing lateness with "cai" | Subj. + Time + 才 + Verb | 他 二十五 岁 才 上 大学 。 |
| Expressing "nearly" with "jihu" | Subj. + 几乎 + Verb | 他 的 头发 几乎 全 白 了 。 |
| Expressing "only" with "zhi" | 只 + Verb | 我 只 有 一个 妹妹。 |
| Sequencing with "xian" and "zai" | 先⋯⋯ ，再⋯⋯ | 先 洗 手 ，再 吃饭 。 |
| Simultaneous tasks with "yibian" | 一边 + Verb 1 (，) 一边 + Verb 2 | 不要 一边 说话 ，一边 吃 东西。 |
| Using "always" as a complaint with "laoshi" | Subj. + 老 (是 ) + Verb | 你 怎么 老是 加班 ？ |
| Using "cai" for small numbers | 才 + Number + Measure Word + Noun | 这 个 班 才 两 个 学生 。 |

### L3-CL03 · Adverbs with Adjectives 副词修饰形容词
*Category: 词类 · 6 points · Official 2025 syllabus: L3 程度副词 比较/更/特别/挺/多（support）· L3-SP-3 跟…一样 · 又…又（L3-CP-5）*

| Point | Pattern | Example |
|---|---|---|
| Adjectives with "name" and "zheme" | 那么 / 这么 + Adj. | 你 怎么 那么 忙 ？ |
| Basic comparisons with "yiyang" | Noun 1 + 跟 / 和 + Noun 2 + 一样 + Adj. | 你 跟 他 一样 高 。 |
| Expressing "both A and B" with "you" | 又⋯⋯ 又⋯⋯ | 他 又 高 又 帅。 |
| Expressing "rather" with "bijiao" | Subj. + 比较 + Adj. | 这个 问题 比较 简单 。 |
| Intensifying with "duo" | Subj. + 多 + Adj. | 多 好！外面 多 舒服！ |
| Modifying nouns with adjective + "de" | Adj. + 的 + Noun | 好喝 的 啤酒 / 可爱 的 宝宝 |

### L3-CL04 · Conjunctions 连词
*Category: 词类 · 4 points · Official 2025 syllabus: L3-CP-6 或者…或者 · L3-QT-1 还是 · 那么/跟（support）*

| Point | Pattern | Example |
|---|---|---|
| Expressing "or" in statements | ⋯⋯或者⋯⋯ | 我 想 去 青岛 或者 南京。 |
| Expressing "then…" with "name" | 那么⋯⋯ | 他 不 听 ，那 我 应该 怎么办 ？ |
| Expressing "with" with "gen" | 跟⋯⋯ + Verb | 你 要 跟 我 一起 去 吗？ |
| Offering choices with "haishi" | A + 还是 + B ? | 你 要 喝 茶 还是 咖啡 ? |

### L3-CL05 · Nouns 名词
*Category: 词类 · 6 points · Official 2025 syllabus: 时间词 以前/刚才/时/后来（support）*

| Point | Pattern | Example |
|---|---|---|
| Before a specific time with "yiqian" | Time / Verb + 以前 | 十 点 以前，我 在 家。 |
| Expressing "before" in general with "yiqian" | 以前，⋯⋯ | 以前，我 不 会 说 中文。 |
| Expressing "just now" with "gangcai" | 刚才 + Verb | 你 刚才 说 什么 了？ |
| Expressing "when" with "shi" | Time + 时 | 考试 时 不要 说话 。 |
| In the future in general with "yihou" | 以后，⋯⋯ | 以后，你 不要 问 我。 |
| Sequencing past events with "houlai" | ⋯⋯ ，后来 ⋯⋯ | 开始 他 不 同意， 但 后来 同意了。 |

### L3-CL06 · Numbers 数词
*Category: 词类 · 4 points · Official 2025 syllabus: L3-EX-1 概数2（相邻数词）· 万/亿*

| Point | Pattern | Example |
|---|---|---|
| Approximating with sequential numbers | Number 1 + Number 2 | 三 四个 人。一 两 天。 |
| Big numbers in Chinese | Number + 万 / 亿 | 五 万 |
| Structure of times (advanced) | Number 1 + 点(钟) + Number 2 + 分 | 现在 十一点十八分 。 |
| Structure of times (basic) | Number + 点(钟) | 现在 十一点 。 |

### L3-CL07 · Particles 助词
*Category: 词类 · 4 points · Official 2025 syllabus: 着/了/的/得/地/呢（support，承 L2）*

| Point | Pattern | Example |
|---|---|---|
| Aspect particle "zhe" | Verb + 着 | 我 读 ，你 听 着 。 |
| Change of state with "le" | ⋯⋯了 | 我 25 岁 了。 |
| Questions with "ne" | ⋯⋯呢 ? | 我 很 好。你 呢 ? |
| Structural particle "de" | 的 / 得 / 地 | 红色的车，跑得很快，慢慢地走 |

### L3-CL08 · Prepositions 介词
*Category: 词类 · 3 points · Official 2025 syllabus: L3 介词 关于/向/为了/根据/把/被（support）*

| Point | Pattern | Example |
|---|---|---|
| Expressing "about" with "guanyu" | 关于 + Obj. ，⋯⋯ | 关于 中国 历史 ，我 知道 的 不 多 。 |
| Expressing "all the way until" with "zhidao" | 直到 + Time / Event ，Subj. + 才 ⋯⋯ | 直到 十二 点 半 ，我 才 做 完 作业 。 |
| Expressing "towards" with "xiang" | 向 + Direction / Person + Verb | 你 必须 向 他 道歉！ |

### L3-CL09 · Verbs 动词
*Category: 词类 · 4 points · Official 2025 syllabus: 看起来 · 兼语句 让/叫/请/使（L2-SP-4 承接）· 经过 · L3-SP-3 没（有）+比较*

| Point | Pattern | Example |
|---|---|---|
| Appearance with "kanqilai" | 看起来⋯⋯ | 这 家 餐厅 看起来 不错 。 |
| Basic comparisons with "meiyou" | Noun 1 + 没(有) + Noun 2 + Adj. | 你 没有 我 胖 。 |
| Causative verbs | Subj. + 让 / 叫 / 请 / 使 + Person + Predicate | 你 为什么 不 让 我 去 ？ |
| Expressing "through" with "jingguo" | 经过 + Event / Time ，⋯⋯ | 经过 自己 的 努力 ，她 考上 了 北京 大学 。 |

### L3-CL10 · Auxiliary verbs 能愿动词
*Category: 词类 · 1 points · Official 2025 syllabus: L3 能愿动词 应该/该/得/需要（support）*

| Point | Pattern | Example |
|---|---|---|
| Expressing "should" with "yinggai" | 应该 / 该 + Verb | 你 应该 工作。 |

### L3-CL11 · Verb phrases 动词短语
*Category: 词类 · 6 points · Official 2025 syllabus: V+了+时量（L2-CM-4 承接）· 难+V · 没办法 · V+V 重叠（L2-WC-1）*

| Point | Pattern | Example |
|---|---|---|
| Expressing "difficult" with "nan" | 难 + Verb | 难 做。难 买。 |
| Expressing duration with "le" | Verb + 了 + Duration | 他 在 北京 住 了 两 年。 |
| Expressing ongoing duration with double "le" | Verb + 了 + Duration + 了 | 他 在 北京 住 了 两 年 了。 |
| Inability with "mei banfa" | 没办法 + Verb | 我 没 办法 帮 你。 |
| Reduplication of verbs | Verb + Verb | 你 看看。 |
| Special verbs with "hen" | 很 + Verb | 我 很 喜欢 他。 |

### L3-CL12 · Complements 补语
*Category: 句法结构 · 4 points · Official 2025 syllabus: L3-CM-1 结果补语2 · L3-CM-2 趋向补语2 引申 · L3-CM-3 可能补语1*

| Point | Pattern | Example |
|---|---|---|
| Direction complement | Verb (+ Direction) + 来 / 去 | 我们 走 过去 吧 。 |
| Potential complement | Verb + 得 / 不 + Complement | 做 得 完 / 做 不 完 |
| Result complements | Verb + 好 / 完 / 错 | 我们 吃 好 了 。 |
| Result complement "-xiaqu" | Verb + 下去 | 这个 故事 太 无聊 了 ，我 听 不 下去 了 。 |

### L3-CL13 · Conditional Statements 条件复句
*Category: 句法结构 · 3 points · Official 2025 syllabus: L3-CP-4 只要…就 / 只有…才 · 除非（官方属六级 L6-CP-4）*

| Point | Pattern | Example |
|---|---|---|
| Expressing "as long as" with "zhiyao" | 只要⋯⋯，就⋯⋯ | 只要 你 过来 ， 我们 就 很 开心 。 |
| Expressing "only after" with "cai" | ⋯⋯，才⋯⋯ | 那 本 书 我 看 了 两 遍 才 看 懂。 |
| Expressing "only if" with "zhiyou" | 只有⋯⋯，才⋯⋯ | 只有 你 帮忙 ， 我 才 能 完成 任务 。 |

### L3-CL14 · Noun Phrases 名词短语
*Category: 句法结构 · 1 points · Official 2025 syllabus: 有的（L1 指示代词 support）*

| Point | Pattern | Example |
|---|---|---|
| Using "youde" to mean "some" | 有的 + Noun | 派对的时候，有的人在喝酒，有的人在跳舞，还有的人在聊天。 |

### L3-CL15 · Numbers and Measure Words 数量表达
*Category: 句法结构 · 1 points · Official 2025 syllabus: 数+量+半+名（数量表达 support）*

| Point | Pattern | Example |
|---|---|---|
| Expressing "half" with "ban" | Number + Measure Word + 半 + Noun | 三 个 半 小时 |

### L3-CL16 · Sentence Patterns 句式
*Category: 句法结构 · 4 points · Official 2025 syllabus: L3-FX-3 一…也/都+不/没 · L3-FX-1 越…越 · L3-SP-1 把字句 · L3-SP-2 被动句*

| Point | Pattern | Example |
|---|---|---|
| Expressing "not even one" | 一 + Measure Word + (Noun) + 也 / 都 + 不 / 没 + Verb | 一 句 中文 都 不 会 说 。 |
| Expressing "the more... the more..." with "yue… yue…" | Subj.＋越＋Verb＋越 + Adj. / Verb | 她 越 想 越 生气 。 |
| Using "ba" sentences | Subj. + 把 + Obj.+ Verb Phrase | 我 把 书 看 完 了。 |
| Using "bei" sentences | Subj. + 被 + Doer + Verb Phrase | 我 被 他 骗 了 。 |

### L3-CL17 · Basic/Simple Sentence Patterns 基本句式
*Category: 句法结构 · 6 points · Official 2025 syllabus: L3-SP-3 存现句 · L3-WC-1 疑问代词非疑问用法 · L3-FX-1 越来越 · L3-CP-7 为了*

| Point | Pattern | Example |
|---|---|---|
| Alternative existential sentences | Place + Verb + 着 + Noun Phrase | 桌子 上 放 着 一 本 书 。 |
| Expressing "as one likes" with "jiu" | 想 + Question Word + 就 + Question Word | 想 去 哪儿 就 去 哪儿 。 |
| Expressing "every" with question words | Question Word + 都 + Predicate | 谁 都 可以 进 。 |
| Expressing "more and more" with "yuelaiyue" | Subj. + 越来越 + Adj. + 了 | 天气 越来越 冷 了。 |
| Expressing purpose with "weile" | 为了 + Purpose + Verb | 为了 钱 ，他 什么 都 愿意 做 。 |
| Expressing "some" with question words | 在哪儿 / 谁 / 什么 / 什么时候 | 这个 人 我 在 哪儿 见 过 。 |

### L3-CL18 · Comparison Patterns 比较句式
*Category: 句法结构 · 4 points · Official 2025 syllabus: L3-SP-3 比较句2（有…吗/跟…比/更/还/…多了）*

| Point | Pattern | Example |
|---|---|---|
| Expressing comparable degree with "you" | Noun 1 有 Noun 2 + Adj. + 吗？ | 他 有 我 帅 吗 ？ |
| Expressing "compared with" using "gen" | 跟 + Noun 1 + 比 (起来) ，Noun 2⋯⋯ | 跟 上海 比 ，北京 的 冬天 比较 干 。 |
| Expressing "even more" with "geng" or "hai" | Noun 1 + 比 + Noun 2 + 更 / 还 + Adj. | 他 比 姚明 还 高 。 |
| Expressing "much more" in comparisons | Noun 1 + 比 + Noun 2 + Adj. + 多了 | 拼音 比 汉字 容易 多了 。 |

### L3-CL19 · Complex Sentence Patterns 复杂句式
*Category: 句法结构 · 4 points · Official 2025 syllabus: L3-FX-2 除了…以外 · L3-CP-3 如果…（的话）就 · L3-CP-2 不但…而且*

| Point | Pattern | Example |
|---|---|---|
| Expressing "except" and "in addition" with "chule… yiwai" | 除了 ⋯⋯ (+ 以外) ，Subj. + 都 / 也 / 还 ⋯⋯ | 除了 他 ，我们 都 去 过 。 |
| Expressing "if... then..." with "ruguo... jiu..." | 如果 ⋯⋯ ，就 ⋯⋯ | 如果 有 困难 ，就 给 我 打 电话 。 |
| Expressing "if" with "ruguo... dehua" | 如果⋯⋯ (的话) ，(就) ⋯⋯ | 如果 明天 下雨 的话 ，我们 就 不 去 了 。 |
| Expressing "not only... but also" with "budan... erqie..." | 不但⋯⋯，而且⋯⋯ | 他 不但 聪明，而且 勤劳。 |

### L3-CL20 · Adverbs 副词
*Category: 相似语法点辨析 · 4 points · Official 2025 syllabus: L3 副词（support）又/一直/总是/才/终于/只/几乎 · L3-CP-1 先…再 · L3-CP-5 一边…一边*

| Point | Pattern | Example |
|---|---|---|
| Comparing "cai" and "jiu" | 才 vs 就 | 我 花 了 两 天 才修 好 ，你 一下子 就 弄 坏 了。 |
| Comparing "gang" and "gangcai" | 刚 vs. 刚才 | 你 刚才 去 哪儿 了？我 刚 回来 。 |
| Comparing "youdian" and "yidian" | 有点 vs. 一点 | 这 衣服 有点 贵 ，便宜 一点 吧。 |
| Comparing "zai" and "you" | 再 vs 又 | 我不能再喝了，你走后我又喝了两瓶 。 |

### L3-CL21 · Conjunctions 连词
*Category: 相似语法点辨析 · 1 points · Official 2025 syllabus: L3-CP-6 或者…或者 · L3-QT-1 还是 · 那么/跟（support）*

| Point | Pattern | Example |
|---|---|---|
| Comparing "haishi" and "huozhe" | 还是 vs. 或者 | 我们 明天 见 还是 后天 见 ？明天 或者 后天 都 可以 。 |

### L3-CL22 · Time Words 时间词辨析
*Category: 相似语法点辨析 · 1 points · Official 2025 syllabus: 相似语法点辨析 — 用作 R4 场景选择题的题源*

| Point | Pattern | Example |
|---|---|---|
| Comparing "yihou" "ranhou" "houlai" | 以后 vs. 然后 vs. 后来 | 我 以后 想 开 公司 。/ 后来 他 去 了 美国 ，然后 他 的 父母 也 搬 过去 了 。 |


## HSK 4 clusters

HSK 4 has **30 clusters / 113 points** (wiki old-HSK scheme). Cluster order below is the wiki's teaching order — the order the syllabus introduces them.

### L4-CL01 · Adjectives 形容词
*Category: 词类 · 2 points · Official 2025 syllabus: L4-CM-1 程度补语2 死了 · 全（范围 support）*

| Point | Pattern | Example |
|---|---|---|
| Indicating the whole with "quan" | 全 + Noun | 我们 全 家 都 去 旅游 了。 |
| Negative adjectives with "-si le" | Adj. + 死了 | 我 今天 累 死了 。 |

### L4-CL02 · Adverbs 副词
*Category: 词类 · 27 points · Official 2025 syllabus: L4 副词（support）· L4-QT-1 反问句2 难道/疑问代词反问 · L4-SP-5 双重否定 不得不 · L4-FX-1 一+量+比+一+量 · 千万/只好/差点儿/竟然/毕竟?（毕竟属五级）*

| Point | Pattern | Example |
|---|---|---|
| Approximations with "chabuduo" | Subj. + 差不多 | 我们 的 中文 水平 差不多。 |
| Assessing situations with "kanlai" | 看来 + Judgment to the Situation；在 + Person + 看来 | 看来他不来了，都这么晚了。 |
| Coincidence with "zhenghao" | Subj. + 正好 + Verb Phrase | 他 正好 问 了 我 想 问 的 问题 。 |
| Declaring the only option with "zhihao" | 只好 + Verb Phrase | 上 个 周末 下雨 了 ，我们 只好 待 在 家。 |
| Emphasizing negation with "you" | 又 + 不 / 没 + Verb | 又 没 下雨 ，带 伞 干吗 ？ |
| Emphatic adverb "ke" | 可 + Adj. (+ 了) | 这 件 事情 对 他 造成 的 影响 可 大 了 。 |
| Expressing "all along" with "yuanlai" | Subj. + 原来 + Predicate | 原来 昨天 那个 人 是 你 啊 。 |
| Expressing "almost" using "chadian" | Subj. + 差点 + Predicate | 我 今天 差点儿 迟到 了 。 |
| Expressing "always" with "conglai" | 从来 + 都 (是) + Predicate | 我 从来 都 是 一个人，已经 习惯了。 |
| Expressing "as a result" with "jieguo" | Reason / Condition ，结果 + Result | 他 没 好好 复习 ，结果 没 通过 考试。 |
| Expressing concern with "kongpa" | 恐怕 + Subj. ⋯⋯ | 恐怕 今天 做 不 完。 |
| Expressing "enough" with "gou" | Subj. + 够 + Predicate (+ 了) | 我们 买 了 很 多 菜 ，够 吃 了 。 |
| Expressing "even" with "shenzhi" | 甚至 | 他们 贡献 出 所有 的 精力 ， 甚至 最 宝贵 的 生命 。 |
| Expressing "had better" with "haishi" | 还是 + Verb | 我们 还是 先 吃饭 吧。 |
| Expressing "had better" with "zuihao" | Subj. + 最好 + Predicate | 你 最好 先 休息 一下 。 |
| Expressing "have to" with "budebu" | Subj. + 不得不 + Verb | 老板 很 讨厌 应酬，但是 她 不得不 去。 |
| Expressing "in the end" with "daodi" | 到底 | 事情 到底 是 办 成 了 。 |
| Expressing "in the end" with "jiujing" | 究竟 | 你 究竟 喜 不 喜欢 我？ |
| Expressing "just" with "gang" | Subj. + 刚 + Verb | 他 刚 走。 |
| Expressing "one by one" with "yi" | 一 + Measure Word + 一 + Measure Word | 宝宝 一 天 一 天 在 长大 。 |
| Expressing "originally" with "benlai" | 本来⋯⋯ | 搬家 本来 就 很 麻烦。 |
| Expressing "small quantity" with "jiu" | 就 + Subject + Predicate | 这 件 事 就 我 一 个 人 知道 。 |
| Expressing the unexpected with "jingran" | Subj. + 竟然 ⋯⋯ | 我们 要 出发 的 时候，他 竟然 说 不 去 了 。 |
| Expressing "to make certain" with "qianwan" | 千万 + Verb/Verb Phrase | 千万 别 泄露 出 去。 |
| Rhetorical questions with "nandao" | 难道⋯⋯？ | 这 都 是 你 引起 的 ， 难道 你 就 不 内疚 ？ |
| Sequencing with "xian" and "zai" | 先⋯⋯ ，再⋯⋯ | 先 洗 手 ，再 吃饭 。 |
| Using "ye" and "dou" together | 也都 + Verb / Adj. | 他们 也 都 是 法国 人 。 |

### L4-CL03 · Adverbs with Adjectives 副词修饰形容词
*Category: 词类 · 1 points · Official 2025 syllabus: 挺（官方属三级程度副词）*

| Point | Pattern | Example |
|---|---|---|
| Expressing "quite" with "ting" | 挺 + Adj. + 的 | 你 男朋友 挺 帅 的 。 |

### L4-CL04 · Auxiliary Words 虚词
*Category: 词类 · 2 points · Official 2025 syllabus: L2 什么的 · L4 其他助词 等2/等等*

| Point | Pattern | Example |
|---|---|---|
| Ending a non-exhaustive list with "shenme de" | Noun 1, Noun 2 + 什么的 | 明天 去 野餐 ，我们 要 不 要 买 一些 水果 ，零食 什么的 。 |
| Non-exhaustive lists with "dengdeng" | ⋯⋯ 等 / 等等 | 长城、故宫 等 地方 都 是 北京 有名 的 景点 。 |

### L4-CL05 · Conjunctions 连词
*Category: 词类 · 8 points · Official 2025 syllabus: L4 连词（support）不过/于是/另外/再说/而/还有 · L4-CP-* 系列*

| Point | Pattern | Example |
|---|---|---|
| A softer "but" with "buguo" | ⋯⋯ ，不过 ⋯⋯ | 他 的 汉语 口语 不错 ，不过 不 认识 汉字 。 |
| Expressing "and then" with "yushi" | ⋯⋯ ，于是 ⋯⋯ | 他 实在 太 懒 了 ，于是 老板 把 他 辞 了 。 |
| Expressing "in addition" with "haiyou" | ⋯⋯ ，还有 ，⋯⋯ | 你 需要 吃 药 。还有，要 多 休息 。 |
| Expressing "in addition" with "lingwai" | ⋯⋯ ，另外 ，⋯⋯ | 希望 你 不要 再 迟到 了。另外，你 应该 穿 得 正式 一点 。 |
| Expressing "in addition" with "zaishuo" | ⋯⋯ ，再说 ，⋯⋯ | 这么 晚 ，别 走 了 。再说 ，外面 还 在 下雨 。 |
| Two words for "but" | ……，可是 / 但是…… | 我 喜欢 他，可是/但是 他 不 喜欢 我。 |
| Using "er" to explain contrasting ideas | Sentence 1， + 而 + Sentence 2 | 以后 后悔 的 人 不 是 我，而 是 你 自己。 |
| Using "lai" to connect two verb phrases | 通过 / 用 + Method + 来 + Verb Phrase | 用 这 种 方法 来 赚钱 ，真 丢人 。 |

### L4-CL06 · Nouns 名词
*Category: 词类 · 1 points · Official 2025 syllabus: 其中（指示 support）*

| Point | Pattern | Example |
|---|---|---|
| Expressing "within (it/them)" with "qizhong" | 其中 | 有 五 个 人 报名 了 ， 其中 两 个 是 女生 。 |

### L4-CL07 · Numbers 数词
*Category: 词类 · 1 points · Official 2025 syllabus: L4-EX-2 分数 分之*

| Point | Pattern | Example |
|---|---|---|
| Expressing fractions with "fenzhi" | Denominator + 分之 + Numerator | 在 我们 班 ，外国 学生 占 三 分 之 一 。 |

### L4-CL08 · Particles 助词
*Category: 词类 · 3 points · Official 2025 syllabus: 吗（确认问）/吧（列举）/的2 语气（support）*

| Point | Pattern | Example |
|---|---|---|
| Advanced yes-no questions with "ma" | Confirmation + Question + 吗 ？ | 你 要 什么 吗 ? |
| Reviewing options with "ba" | Option 1吧 ，⋯⋯ ；Option 2 吧 ，⋯⋯ | 不 说 吧 ，他 还 会 做 错 ；说 吧，他 肯定 不 高兴 。 |
| Using "de" (modal particle) | ⋯⋯的 | 我 不 会 骗 你 的。 |

### L4-CL09 · Prepositions 介词
*Category: 词类 · 2 points · Official 2025 syllabus: L4 介词 随着/在…上（在…上/下/中 官方属三级 L3-FX-5）*

| Point | Pattern | Example |
|---|---|---|
| Expressing "along with…" with "suizhe" | 随着 A + 的 + Verb， Subj. + Predicate | 随着 经济 的 发展，人们 的 生活 越 来 越 好。 |
| Idiomatic phrases with "zai" | 在 + Topic + 上 ，Subj. ⋯⋯ | 在美国 历史 上 ，最重要 的 总统 是 谁 ？ |

### L4-CL10 · Sentence patterns 句式
*Category: 词类 · 1 points · Official 2025 syllabus: 以…为… — 书面结构，无直接官方对应（生成时按固定格式处理）*

| Point | Pattern | Example |
|---|---|---|
| Using "yi... wei..." | 以 + A + 为 + B | 我们 公司 是 以 亚洲 市场 为 主，以 欧美 市场 为 辅。 |

### L4-CL11 · Sentence Patterns 句式
*Category: 词类 · 1 points · Official 2025 syllabus: L4-FX-1 连…都/也 · 为…而（L4-FX-2）· 任何（指示）· 既…也/又（L4-CP-1）· 在…上/下/里（L3-FX-5）*

| Point | Pattern | Example |
|---|---|---|
| Emphasizing a negation with "bing" | Subj. + 并 + 不 + Verb / Adj. | 当 金融 分析 人员 并 不是 我 的 梦想。 |

### L4-CL12 · Verbs 动词
*Category: 词类 · 8 points · Official 2025 syllabus: L4-SP-3 兼语句2 让/叫/使 · 好像/以为/通过/来自/在于/要看（support）*

| Point | Pattern | Example |
|---|---|---|
| Causative verbs | Subj. + 让 / 叫 / 请 / 使 + Person + Predicate | 你 为什么 不 让 我 去 ？ |
| Expressing "it depends" with "kan" | 这 / 那 + 要看 / 得看 + Unclear Situation | 这 得 看 你 的 时间 。 |
| Expressing "it seems" with "haoxiang" | 好像⋯⋯ | 他 好像 是 英国 人 。 |
| Expressing "lies in" with "zaiyu" | ⋯⋯ 在于 ⋯⋯ | 我们 服务 的 特色 在于 个性化 。 |
| Expressing "mistakenly think that" with "yiwei" | Subj. + 以为⋯⋯ | 我 以为 你 不 是 我的 朋友。 |
| Expressing "through" with "tongguo" | 通过 + Agent / Method ，⋯⋯ | 我们 是 通过 他 的 朋友 找到 他 的 。 |
| Expressing "to come from" with "laizi" | Subj. + 来自 + Place | 我 来自 美国。 |
| Using "lai" as a dummy verb | (让 +) Subj. + 来 | 让 我 来 吧。 |

### L4-CL13 · Auxiliary verbs 能愿动词
*Category: 词类 · 2 points · Official 2025 syllabus: 不用 · 得（L3 能愿动词）*

| Point | Pattern | Example |
|---|---|---|
| Expressing "don't need to" with "buyong" | Subj. + 不用 + Verb Phrase | 不用 担心 。 |
| Expressing "must" with "dei" | 得 + Verb | 我们 得 走 了 。 |

### L4-CL14 · Verb phrases 动词短语
*Category: 词类 · 11 points · Official 2025 syllabus: 并/并且 · 少+V/多+V · 由（L4 介词 由1/由2）· 从来 · 值得 · V+到 · 害得 · L3-WC-2 离合词 · V着V着就…*

| Point | Pattern | Example |
|---|---|---|
| Combining verbs with "bing" | Verb Phrase 1 + 并 / 并且 + Verb Phrase 2 | 我 同意 并且 支持 你 的 决定 。 |
| Doing something less with "shao" | 少 + Verb | 请 少 放 点 盐 。 |
| Doing something more with "duo" | 多 + Verb | 多 吃 点 。 |
| Emphasizing the doer of an action with "you" | 由 + Person + Verb | 这个 项目 由 小李 来 完成 。 |
| Expressing "moreover" with "bingqie" | Verb Phrase 1 + 并 / 并且 + Verb Phrase 2 | 我 同意 并且 支持 你 的 决定 。 |
| Expressing "never" with "conglai" | 从来 + 不 / 没(有) + Verb | 她 从来 不 喝酒。我 从来 没有 去 过 美国。 |
| Expressing "to be worth" doing with "zhide" | 值得 + Verb | 这个 想法 不错 ， 值得 考虑 。 |
| Expressing "until" with "dao" | Verb + 到 + Time / Event | 我 昨天 晚上 工作 到 十二 点 半 。 |
| Indicating negative impact with "haide" | 害得 + Verb Phrase | 老师 给 的 作业 太 难 了 ， 害得 我 浪费 了 一 个 下午 学习 。 |
| Separable verb | Verb-Obj. | 我们 见 过 面 。 |
| Using "zhe" when "verbing away" | Verb + 着 + Verb + 着 + 就 + Comment + 了 | 走 着 走 着 ， 他们 到 家 了 。 |

### L4-CL15 · "But" Statements 转折复句
*Category: 句法结构 · 3 points · Official 2025 syllabus: L4-CP-5 转折复句 尽管…但是/然而/不过 · 倒 · 却（关联副词 support）*

| Point | Pattern | Example |
|---|---|---|
| Expressing "although" with "jinguan" | 尽管⋯⋯，但是⋯⋯ | 尽管 我 很 生气 ，但是 我 没 发脾气 。 |
| Expressing contrariness with "dao" | 倒⋯⋯ | 雨 没有 停 ， 倒 大 起来 了 。 |
| The "however" adverb "que" | ⋯⋯，却⋯⋯ | 他们 一见钟情 ， 却 没有 在 一起 。 |

### L4-CL16 · Cause/Effect Statements 因果复句
*Category: 句法结构 · 3 points · Official 2025 syllabus: L4-CP-8 既然…就 / （由于）…因此 · 由于/因此*

| Point | Pattern | Example |
|---|---|---|
| Expressing "due to…" with "youyu" | 由于⋯⋯，⋯⋯ | 由于 天气 原因， 我们 的 航班 取消了。 |
| Expressing "since" with "jiran" | 既然⋯⋯，就⋯⋯ | 既然 来 了 ， 就 留 下来 吃饭 吧 。 |
| Expressing "therefore" with "yinci" | ⋯⋯，因此⋯⋯ | 这 家 饭店 涨价 了 ， 因此 顾客 也 少 了 。 |

### L4-CL17 · Complements 补语
*Category: 句法结构 · 4 points · Official 2025 syllabus: L4-CM-2 可能补语2 得/不了 · 起来引申（L3-CM-2）· 趋向（L2-CM-2 承接）*

| Point | Pattern | Example |
|---|---|---|
| Advanced uses of direction complement "-qilai" | Verb + 起来 | 宝宝，你 应该 把 你 的 玩具 收 起来 。 |
| Direction complement | Verb (+ Direction) + 来 / 去 | 我们 走 过去 吧 。 |
| Direction complement "-qilai" | Verb / Adj.+ 起来 | 天气 热 起来 了 。 |
| Potential complement | Verb + 得 / 不 + Complement | 做 得 完 / 做 不 完 |

### L4-CL18 · Conditional Statements 条件复句
*Category: 句法结构 · 2 points · Official 2025 syllabus: L4-CP-7 只要…就 · 除非…才（官方属六级 L6-CP-4）*

| Point | Pattern | Example |
|---|---|---|
| Expressing "as long as" with "zhiyao" | 只要⋯⋯，就⋯⋯ | 只要 你 过来 ， 我们 就 很 开心 。 |
| Expressing "unless" with "chufei" | 除非⋯⋯ ，才⋯⋯ | 除非 你 求情 ，他 才 肯 帮忙 。 |

### L4-CL19 · "Even If" Statements 让步复句
*Category: 句法结构 · 1 points · Official 2025 syllabus: L4-CP-10 即使…也*

| Point | Pattern | Example |
|---|---|---|
| Expressing "even if…" with "jishi" | 即使⋯⋯，也⋯⋯ | 即使 你 没胃口 ， 也 要 吃 一点 。 |

### L4-CL20 · "If" Statements 假设复句
*Category: 句法结构 · 1 points · Official 2025 syllabus: L4-CP-6 要是…就*

| Point | Pattern | Example |
|---|---|---|
| Expressing "if… then…" with "yaoshi" | 要是⋯⋯，就⋯⋯ | 你 要是 真 想 我，就 给 我 打 电话 。 |

### L4-CL21 · "No Matter" Statements 无条件复句
*Category: 句法结构 · 2 points · Official 2025 syllabus: L4-CP-7 不管/无论…都*

| Point | Pattern | Example |
|---|---|---|
| Expressing "no matter" with "buguan" | 不管⋯⋯，都 / 也⋯⋯ | 不管 身体 好 坏 ， 他 都 工作 到 深夜 。 |
| Expressing "no matter" with "wulun" | 无论 / 不论⋯⋯，都 / 也⋯⋯ | 无论 天 多 热 ， 都 要 坚持 。 |

### L4-CL22 · Noun Phrases 名词短语
*Category: 句法结构 · 3 points · Official 2025 syllabus: 所有 · 之一 · 另外+数量（support）*

| Point | Pattern | Example |
|---|---|---|
| Expressing "all" with "suoyou" | 所有 (+ 的) + Noun | 我 喜欢 吃 所有 我 妈妈 做 的 菜 。 |
| Expressing "one of" with "zhiyi" | ⋯⋯之一 | 你 是 我 最 好 的 朋友 之一 。 |
| Expressing "the other" with "lingwai" | 另外 + Number + Measure Word + Noun | 我 有 两 个 手机 ，一 个 是 小米 ，另 一 个 是 iPhone 。 |

### L4-CL23 · Sentence Patterns 句式
*Category: 句法结构 · 5 points · Official 2025 syllabus: L4-FX-1 连…都/也 · 为…而（L4-FX-2）· 任何（指示）· 既…也/又（L4-CP-1）· 在…上/下/里（L3-FX-5）*

| Point | Pattern | Example |
|---|---|---|
| Advanced uses of "lian" | 连 + Verb + 都 + 不 / 没 + Verb (，就 ⋯⋯) | 朋友 ？这个 人 我 连 见 都 没 见 过 。 |
| Explaining purpose with "wei... er..." | 为⋯⋯ ，而⋯⋯ | 不 为 朋友圈 而 运动 |
| Expressing "any" with "renhe" | 任何 + Noun + 都 / 也 …… | 我 的 弟弟 特别 顽固，任何 的 人 都 不 能 说服 他。 |
| Expressing "both… and…" with "ji...you" | 既⋯⋯也 / 又⋯⋯ | 他 做 事情 既 快 又 好。 |
| Expressing location with "zai... shang / xia / li" | 在 + Place + 上 / 下 / 里 / 旁边 | 你 的 手机 在 桌子 上。 |

### L4-CL24 · Basic/Simple Sentence Patterns 基本句式
*Category: 句法结构 · 6 points · Official 2025 syllabus: L4-FX-2 一点儿也不 · 连+Subj+都（L4-FX-1）· 疑问代词+都（L3-WC-1）· L4-EX-2 倍数 · 对/一般来说（L3-FX-5）*

| Point | Pattern | Example |
|---|---|---|
| Expressing "even" with "lian" and "dou" | 连 + Subj. + 都 (+ 不 / 没) + Verb | 你 连 小狗 都 怕 ？ |
| Expressing "every" with question words | Question Word + 都 + Predicate | 谁 都 可以 进 。 |
| Expressing "multiples" with "bei" | Noun 1 + 是 + Noun 2 + 的 + Number + 倍 | 他 现在 的 工资 是 两 年 前 的 三 倍 。 |
| Expressing "not at all" with "yidianr ye bu" | Subj. + 一点 + 也 / 都 + 不 + Adj. | 你 一点 也 不 胖 。 |
| Expressing not knowing how to do something using "hao" | Subj. + 不知道 + Verb Phrase + 好 | 我 真的 不 知道 怎么办才 好 。 |
| Phrases using "laishuo" | 对 + Person + 来说 / 一般 来说 | 一般 来说 ，私立 学校 都 比较 贵 。 |

### L4-CL25 · Complex Sentence Patterns 复杂句式
*Category: 句法结构 · 3 points · Official 2025 syllabus: X是X concession（L4-FX-4）· 一…就（L2-CP-3 延伸）· 一方面…另一方面（L4-CP-1）*

| Point | Pattern | Example |
|---|---|---|
| Conceding a point with "shi" | Adj. + 是 + Adj.， 但是⋯⋯ | 这个 东西 好 是 好 ，就是 太 贵 了 。 |
| Events in quick succession with "yi... jiu..." | Subj. + 一 + Event 1，就 + Event 2 | 他 一 到 家 ，就 去 洗澡 了 。 |
| Expressing various aspects with "yi fangmian" | 一方面⋯⋯，一方面⋯⋯ | 一 方面 他 很 喜欢 这 份 工作 ， 一 方面 他 又 觉得 工资 太 低 。 |

### L4-CL26 · Not only… but also… 递进复句
*Category: 句法结构 · 1 points · Official 2025 syllabus: L4-CP-3 递进复句 不但/不仅…而且/还/也*

| Point | Pattern | Example |
|---|---|---|
| Many types of "not only... but also..." | 不但 / 不只 / 不仅⋯⋯，而且 / 还 / 也 ⋯⋯ | 他 不仅 喜欢 吃 中国 菜，而且 也 会 做 几 个 中国 菜！ |

### L4-CL27 · Adverbs 副词
*Category: 相似语法点辨析 · 3 points · Official 2025 syllabus: L4 副词（support）· L4-QT-1 反问句2 难道/疑问代词反问 · L4-SP-5 双重否定 不得不 · L4-FX-1 一+量+比+一+量 · 千万/只好/差点儿/竟然/毕竟?（毕竟属五级）*

| Point | Pattern | Example |
|---|---|---|
| Comparing "benlai" and "yuanlai" | 本来 vs 原来 | 他原来的 公司 本来 要 派 他 去 上海，但是 因为 家 里 有事，去 不了 了。 |
| Comparing "changchang" and "wangwang" | 常常 vs. 往往 | 我 不 常 运动 ，我 往往 呆在 家里 。 |
| Comparing "gang" and "gangcai" | 刚 vs. 刚才 | 你 刚才 去 哪儿 了？我 刚 回来 。 |

### L4-CL28 · Prepositions 介词
*Category: 相似语法点辨析 · 2 points · Official 2025 syllabus: L4 介词 随着/在…上（在…上/下/中 官方属三级 L3-FX-5）*

| Point | Pattern | Example |
|---|---|---|
| Comparing "guanyu" and "duiyu" | 关于 vs 对于 | 对于 那 个 人， 关于 我们 的 学习 方法 |
| Comparing "li" and "cong" | 离 vs. 从 | 从 明天 开始，我 不 抽烟 了。 |

### L4-CL29 · Separate Functions 功能辨析
*Category: 相似语法点辨析 · 3 points · Official 2025 syllabus: 相似语法点辨析 — 用作 R4 场景选择题的题源*

| Point | Pattern | Example |
|---|---|---|
| Comparing "fan'er" and “xiangfan" | 反而 vs 相反 | 吃 水果 不但 对 他 没 好处，反而 有 坏处。 老板 的 想法 跟 我 的 相反。 |
| Comparing "kending" "queding" and “yiding" | 肯定 vs 确定 vs 一定 | 老板 肯定 了 我们 团队 的 工作。你 确定 他 是 我们 要 找 的 人？一定 要 小心。 |
| Comparing "shihe" and "heshi" | 适合 vs 合适 | 这 个 颜色 不 适合 他 ， 黑色 才 是 最 合适 的。 |

### L4-CL30 · Time Words 时间词辨析
*Category: 相似语法点辨析 · 1 points · Official 2025 syllabus: 相似语法点辨析 — 用作 R4 场景选择题的题源*

| Point | Pattern | Example |
|---|---|---|
| Comparing "yihou" and "de shihou" | 以后 vs 的时候 | 打 篮球 的 时候 会 出 了 很 多 汗 ，所以 打 完 篮球 以后 我 要 洗澡 。 |


## HSK 5 clusters

HSK 5 has **29 clusters / 107 points** (wiki old-HSK scheme). Cluster order below is the wiki's teaching order — the order the syllabus introduces them.

### L5-CL01 · Adjectives 形容词
*Category: 词类 · 4 points · Official 2025 syllabus: L5-CM-4 得+不得了 · 得很 · Adj+了+（一）点儿 · 有的是（官方属四级固定短语）*

| Point | Pattern | Example |
|---|---|---|
| Adjectival complement "de budeliao" | Adj. + 得不得了 | 爸爸 气 得 不得了，你 要 倒霉 啦。 |
| Adjectival complement "de hen" | Adj. + 得 很 | 这个 题目 简单 得 很 。 |
| Expressing "a bit too" | Adj. + 了 + (一) 点儿 | 那个 地方 离 我家 远 了 点儿 。 |
| Saying "a lot" with "youdeshi" | Subj. + 有的是 + Noun | 川菜 上海 有的是。 |

### L5-CL02 · Adverbs 副词
*Category: 词类 · 20 points · Official 2025 syllabus: L5-WC-1 语气副词 毕竟/反正/干脆/简直/白 · L5 时间副词 曾经 · 再也不（L4-FX-2）· 差点没（L4 差点儿）· 好不容易/再三（官方属六级）· 顺便/互相（support）*

| Point | Pattern | Example |
|---|---|---|
| Advanced uses of "dou" | Subj. + 都 + Predicate | 我都能闻见面包的香味。 |
| Advanced uses of "hai" | Subj. + 还 + Predicate + 呢 | 还 好朋友 呢 ，天天 说 我 坏话 。 |
| Advanced uses of "zong" | 总 + Verb Phrase | 咱们 总 得 想 个 办法 啊。总 不 能 让 他 一个人 去 吧？ |
| Expressing "after all" with "bijing" | 毕竟 | 别 怪 他 了 ， 毕竟 他 还 小 。 |
| Expressing a last chance with "zaibu... jiu..." | 再不…… 就…… | 再不 抢 就 没 了 。 |
| Expressing "almost" using "chadian mei" | Subj. + 差点没 + Verb | 路 这么 滑，我 差点没 摔倒。 |
| Expressing "anyway" with "fanzheng" | 反正 | 随便 你 信 不 信 ， 反正 我 不 信 。 |
| Expressing "as much as possible" with "jinliang" | 尽量 + Verb | 我 会 尽量 想 办法 帮 你 的。 |
| Expressing difficulty with "hao (bu) rongyi" | 好(不)容易 | 我 好不容易 才 打通 了 银行 的 服务 热线。 |
| Expressing "each other" with "huxiang" | 互相 + Verb Phrase | 互相 帮助 |
| Expressing "feel free" with "jinguan" | 尽管 + Verb | 有 什么 事 ，尽管 找 我 。 |
| Expressing "just" do it with "gancui" | Subj. + 干脆 + Verb Phrase | 家里什么都没有，干脆出去吃吧。 |
| Expressing "never again" with "zai ye bu" | Subj. + 再也 + 不 + Verb Phrase + 了 | 我 再也 不 想 跟 你 说话 了 。 |
| Expressing "once" with "cengjing" | Subj. + 曾经 + Verb + 过 (+ Obj.) | 他 说 他 曾经 做 过 很多 傻事 。 |
| Expressing "over and over again" with "zaisan" | 再三 + Verb | 妈妈 再三 叮嘱 我 ， 要 注意 安全 。 |
| Expressing "simply" with "jianzhi" | 简直⋯⋯ | 她 简直 要 哭 出来 了 。 |
| Expressing wasted efforts with "bai" | 白 + Verb | 白 花 了 一 百 块 钱，这 件 衣服 不 能 穿。 |
| Expressing "while you're at it" with "shunbian" | Subj. ＋Verb Phrase 1，顺便 + Verb Phrase 2 | 你 出去 的 时候顺便 帮 我 买 杯 咖啡。 |
| Repeated actions in the past with "you" | Subj. + Verb + 了 + 又 + Verb | 他 找 了 又 找，还 是 没 找到 他 的 钱 包。 |
| The opposite of "chabuduo" is "cha hen duo" | Subj. + 差很多 | 中国 文化 和 西方 文化 差 很 多 。 |

### L5-CL03 · Auxiliary Words 虚词
*Category: 词类 · 1 points · Official 2025 syllabus: 啊（列举）— 官方叹词 啊（support）*

| Point | Pattern | Example |
|---|---|---|
| Listing things with "a" | ⋯⋯啊，⋯⋯啊 | 我们 店里 有 水饺 啊，盖浇饭 啊 ⋯⋯ |

### L5-CL04 · Conjunctions 连词
*Category: 词类 · 1 points · Official 2025 syllabus: 要不 — L5-CP-3 要不然 branch*

| Point | Pattern | Example |
|---|---|---|
| Expressing "how about" with "yaobu" | Reason / Situation，要不 + Suggestion + 吧 | 下雨 了，要不 明天 再 去 吧 。 |

### L5-CL05 · Nouns 名词
*Category: 词类 · 5 points · Official 2025 syllabus: L5 指示代词 彼此 · （自）…以来（L5-FX-1）· 当中 · 当…的时候 · N+这个（口语）*

| Point | Pattern | Example |
|---|---|---|
| Expressing "among" with "dangzhong" | 当中 | 他们 当中 有 温州 人 ， 有 宁波 人 。 |
| Expressing "each other" with "bici" | 彼此 + Verb | 太 吵 了，我们 都 听不到 对方 在 说 什么。 |
| Expressing "ever since" with "yilai" | Time / Event + 以来 ，⋯⋯ | 今年 八月 以来 ，这里 一直 没 下 过 雨 。 |
| Expressing "when" using "dang" | 当……的时候，…… | 当 我 见到 他 的 时候 ，我 完全 忘 了 要 问 他 什么 。 |
| Name-calling with "zhege" | Noun + 这个 + Category | 你 这个 坏蛋，就 没 做 过 一 件 好 事。 |

### L5-CL06 · Particles 助词
*Category: 词类 · 4 points · Official 2025 syllabus: 了+宾语/补语（advanced，承 L4 把字句2）· 嘛（官方属六级）· 呢（softening）*

| Point | Pattern | Example |
|---|---|---|
| Advanced "le" after an object | Verb + Obj. + 了 | 我 吃 了 早饭 。 |
| Advanced "le" with complements | Subj. + Verb + 了 + Complement | 走 了 上去 。 |
| Marking a topic with "ma" | Statement + 嘛 | 大家 有 话 就 说 嘛 。 |
| Softening the tone of questions with "ne" | ⋯⋯呢？ | 他 人 在 哪 呢 ？ |

### L5-CL07 · Prepositional Phrase 介宾结构
*Category: 词类 · 1 points · Official 2025 syllabus: 以上/以下（数目表达 support）*

| Point | Pattern | Example |
|---|---|---|
| Defining upper and lower limits | 级别 / 次序 / 数目 + 以上 / 以下 | 十 岁 以下 的 孩子 不用 买 票 。 |

### L5-CL08 · Prepositions 介词
*Category: 词类 · 9 points · Official 2025 syllabus: L5 介词 自从/凭/据/依据/替/同/朝/沿着（support）· 给+被动（L5-SP-5）· 至于（官方属六级 L6-WC-3）· 趁/就…而言*

| Point | Pattern | Example |
|---|---|---|
| Expressing "ever since" with "zicong" | (自)从⋯⋯ | 自从 来 了 上海 ， 他 就 习惯 了 繁忙 的 生活 。 |
| Expressing "for…" with "eryan" | 对 + Person / Group + 而言 ，⋯⋯ | 对 消费者 而言 ，促销 活动 很 有 吸引力 。 |
| Expressing "for" with "wei" | 为 + Person + Predicate | 为 人民 服务 ！ |
| Expressing "including" with "zainei" | (包括)⋯⋯ 在内 ，⋯⋯ | 包括 水 电 费 在内 ，我 每 个 月 的 房租 三千 五 。 |
| Expressing "on the basis of" with "ping" | 凭⋯⋯ | 他 凭 自己 的 努力 成功 。 |
| Expressing passive voice with "gei" | Receiver + 给 + The Doer + 给 + Verb Phrase | 事情 给 解决 了 吗？ |
| Expressing "with regards to" with "zhiyu" | 至于 + Topic， Comment | 你 先 看 产品 。 至于 价格 ， 我们 再 商量 。 |
| Limiting scope with "jiu" | 就⋯⋯ (来说 / 而言) | 就 我 而言 ， 兴趣 最 重要 。 |
| Opportune timing with "chen" | 趁 + Situation / Opportunity…… | 趁 老板 不 在，我们 出去 吃饭 吧。 |

### L5-CL09 · Sentence Patterns 句式
*Category: 词类 · 4 points · Official 2025 syllabus: L5-SP-2 把字句3 · 不比（L3-SP-3）· 少不了 · 等于 · 从…中 · V就V · 无…可… · 不但…甚至连（L5-CP-6）· 好（L4-CP-9 目的）· 有关的 · 一面…一面（L3-CP-5）· 所谓 · 不是…就是（L4-CP-4）· 在…内 · 宁可…也（官方属七—九级）*

| Point | Pattern | Example |
|---|---|---|
| Expressing "if it were not for" with "yaobushi" | 要不是 ⋯⋯ ( 的话 )，⋯⋯ | 要不是 你们 迟到 的话，我们 早就 到 了。 |
| Expressing "thanks to" with "duokui" | Good Outcome ，多亏 (了) + Lucky Incident | 我 没 迟到 ，多亏了 你 开车 送 我 。 |
| Expressing "that's all" with "eryi" | Subj. + (仅仅) + 是 + Obj. + 而已 | 他 只 是 开 个 玩笑 而已，不 要 当 真。 |
| Using "jiang" as a formal "ba" | Subj. + 将 + Obj. + Verb Phrase | 学校 将 那些 经常 逃学 的 学生 都 开除 了 。 |

### L5-CL10 · Verbs 动词
*Category: 词类 · 7 points · Official 2025 syllabus: V+什么（L5-WC-2 X什么X）· 不像/不如/比起（L4-SP-4 比较句3）· 化（官方属六级 L6-WC-1）· 算 · 难怪*

| Point | Pattern | Example |
|---|---|---|
| Challenging a verb with "shenme" | Verb + 什么 + Obj. | 没有 钱 看 什么 电影。 |
| Comparing specifically with "xiang" | Noun 1 + 不像 + Noun 2 + 这么 / 那么 + Adj. / Verb | 你 怎么 像 我 妈 一样 啰嗦！ |
| Comparisons with "biqi" | 比起 + B (+ 来) ，A ~ | 比起上海 ，我 老家 的 物价 便宜 多 了。 |
| Comparisons with "buru" | 不如⋯⋯ | 我的 汉语 不如 他的。 |
| Making "-ize" and "-ify" verbs with "hua" | Noun / Adj. + 化 | KFC 的 中国 本土化 经营 做 得 非常 成功。 |
| Making judgments with "suan" | Subj. + 算 + Adj. + 的 | 在 我们 公司 ，我 算 年轻 的 。 |
| Using "nanguai" as a verb | 难怪 + Specific Person / People …… | 难怪 他，他还是个孩子呢，什么都不懂。 |

### L5-CL11 · Auxiliary verbs 能愿动词
*Category: 词类 · 1 points · Official 2025 syllabus: 将/将要（L4 时间副词 将 support）*

| Point | Pattern | Example |
|---|---|---|
| Expressing future with "jiang" | Subj. + 将 / 将要 / 将会 + Verb Phrase | 比赛 结果 将 在 月底 公布 。 |

### L5-CL12 · Verb phrases 动词短语
*Category: 词类 · 2 points · Official 2025 syllabus: 难免（官方属七—九级）· 受（书面被动，关联 L5-SP-5）*

| Point | Pattern | Example |
|---|---|---|
| Expressing "hard to avoid" with "nanmian" | (Subj. +) 难免 + Verb Phrase | 第 一 次 尝试 ， 难免 失败 。 |
| Passive verbs with "shou" | 受 + Verb | 他 为 人 善良 ， 很 受 尊重 。 |

### L5-CL13 · Adverbs with Adjectives 副词修饰形容词
*Category: 句法结构 · 1 points · Official 2025 syllabus: 格外（L5 程度副词）*

| Point | Pattern | Example |
|---|---|---|
| Expressing "especially" with "gewai" | 格外 + verb | 他今天格外 忙. |

### L5-CL14 · "But" Statements 转折复句
*Category: 句法结构 · 1 points · Official 2025 syllabus: L5-CP-6 反而（不但不…反而）*

| Point | Pattern | Example |
|---|---|---|
| Expressing "on the contrary" with "fan'er" | ⋯⋯，反而 ⋯⋯ | 他 没有 放弃 ，反而 更加 努力 了 ！ |

### L5-CL15 · Cause/Effect Statements 因果复句
*Category: 句法结构 · 1 points · Official 2025 syllabus: 之所以…是因为（因果倒装，关联 L5-CP-4 …可见）*

| Point | Pattern | Example |
|---|---|---|
| Stating the effect before the cause | 之所以 ⋯⋯ ，是因为 / 是为了 / 是想 ⋯⋯ | 我 之 所以 来 晚 了 是 因为 路上 堵车 。 |

### L5-CL16 · Complements 补语
*Category: 句法结构 · 7 points · Official 2025 syllabus: L5-CM-1 状态补语2 · L5-CM-2 趋向补语3 引申 · L5-CM-3 得/不得 · L5-CM-4 不得了 · V来V去（L5-WC-2）· 坏了（L4-CM-1）*

| Point | Pattern | Example |
|---|---|---|
| Advanced degree complements | Adj. + 得 + 很 / 不得了 / 要命 / 不行 | 我 老婆 的 工作 轻松 得很 。 |
| Advanced potential complements | Verb + 得了 / 不了 | 今晚 我 有事 ，去 不 了 。 |
| Advanced result complements "zhu", "kai", and "chulai" | Verb + 住 / 开 / 出(来) | 抓住 那个 小偷 ！ |
| Complement "-huai le" | Verb + 坏了 | 坏 了。 |
| Complement "-zhao" | Verb + 着 | 宝宝 刚 睡 着。 |
| Tricky uses of "dao" | Verb + 到 | 他 做 到 了 吗 ？ |
| Using "lai" and "qu" when "verbing around" | Verb + 来 + Verb + 去 | 他 考虑 来 考虑 去 ， 最后 还是 决定 回 学校 。 |

### L5-CL17 · Conditional Statements 条件复句
*Category: 句法结构 · 1 points · Official 2025 syllabus: L5-CP-3 一旦…就*

| Point | Pattern | Example |
|---|---|---|
| Expressing "once...then..." with "yidan...jiu..." | 一旦⋯⋯，就⋯⋯ | 一旦 我 找 好 的 工作，我 就 会 安心。 |

### L5-CL18 · "Even If" Statements 让步复句
*Category: 句法结构 · 3 points · Official 2025 syllabus: L5-CP-5 哪怕…也 · 就是/就算…也（承 L4-CP-10）*

| Point | Pattern | Example |
|---|---|---|
| Expressing "even if…" with "jiushi" | 就是⋯⋯，也⋯⋯ | 就是 天气 不 好 ， 我 也 要 出去 玩 。 |
| Expressing "even if…" with "jiusuan" | 就算⋯⋯ ，也⋯⋯ | 就算 再 困难 ， 我们 也 要 坚持 到底 。 |
| Expressing "even if…" with "napa" | 哪怕⋯⋯，也⋯⋯ | 哪怕 第 一 次 失败 了 ， 也 要 继续 研究 。 |

### L5-CL19 · "If" Statements 假设复句
*Category: 句法结构 · 3 points · Official 2025 syllabus: L5-CP-3 假如/万一/不然 · 的话（L3 助词）*

| Point | Pattern | Example |
|---|---|---|
| Expressing "if… then…" with "jiaru" | 假如⋯⋯，就⋯⋯ | 假如 下雨 了 ， 就 收 衣服 。 |
| Expressing "what if" with "wanyi" | 万一 ⋯⋯ 怎么办 ？ | 万一 被 发现 了 怎么办 ？ |
| Marking a topic with "de hua" | Topic + 的话 ，Comment | 北京 的话 ，秋天 去 最好 。 |

### L5-CL20 · Sentence Patterns 句式
*Category: 句法结构 · 16 points · Official 2025 syllabus: L5-SP-2 把字句3 · 不比（L3-SP-3）· 少不了 · 等于 · 从…中 · V就V · 无…可… · 不但…甚至连（L5-CP-6）· 好（L4-CP-9 目的）· 有关的 · 一面…一面（L3-CP-5）· 所谓 · 不是…就是（L4-CP-4）· 在…内 · 宁可…也（官方属七—九级）*

| Point | Pattern | Example |
|---|---|---|
| Advanced uses of "ba" | 把 + Noun + Verb⋯⋯ | 我 没有 把 它 当回事。 |
| Basic comparisons with "bu bi" | Noun 1 + 不比 + Noun 2 + Adj. | 你 不 比 别人 笨 。 |
| Conditions with "yao" and "jiu" | 要 + Verb + 就 + Verb …… | 要 买 就 买 ，我们 快 关门 了 。 |
| Expressing "can't do without" with "shaobuliao" | Subj. + 少不了 + Noun / Verb Phrase | 春节 少不了 吃 饺子。 |
| Expressing "equal to" with "dengyu" | A, 等于 B | 今天吃了炸鸡等于白跑步了。 |
| Expressing "from" with "cong... zhong" | 从 + noun + 中 + result | 我从 书中学习了很多知识。 |
| Expressing indifference with "jiu" | Verb + 就 + Verb | 走 就 走 ，我 早就 不 想 干 了 ！ |
| Expressing "no" (noun) "to" (verb) with "wu... ke..." | 无 + Noun + 可 + Verb | 我 无 话 可 说。 |
| Expressing "not only..., even..." using "budan..., shenzhi lian" | Subj. + 不但 ⋯⋯ ，甚至连 + New Subject + 也 + Matching Situation | 不但，甚至连。 |
| Expressing purpose with "hao" | Action ，好 + Purpose | 她 睡前 常常 喝 牛奶 ，好 入睡 。 |
| Expressing "related to..." with "you guan de" | 跟 / 和 + Topic + 有关的 + Noun | 与 他有关的事情，我都不想知道。 |
| Expressing simultaneous actions with "yimian" | 一面⋯⋯，一面⋯⋯ | 他 喜欢 一面 吃 东西 ， 一面 看 电影。 |
| Expressing "so-called" with "suowei" | 所谓 + (的) Noun Phrase | 所谓 “小意思” 就 是 指 礼物。 |
| Expressing the only two possibilities | 不是⋯⋯，就是⋯⋯ | 不是 成功，就是 失败。 |
| Expressing "within" a period of time using "zai... nei" | 在 + Time + 内 | 你 必须 在 一周 内 完成。 |
| Expressing "would rather" with "ningke" | 宁可⋯⋯，也⋯⋯ | 他 宁可 输，也 不 放弃。 |

### L5-CL21 · Complex Sentence Patterns 复杂句式
*Category: 句法结构 · 1 points · Official 2025 syllabus: 怪不得/难怪（L5-WC-1）*

| Point | Pattern | Example |
|---|---|---|
| Expressing "no wonder" | Reason ，怪不得 / 难怪 + Observation | 小张 请假 了，难怪 今天 没有 看到 他。 |

### L5-CL22 · Either… or 选择复句
*Category: 句法结构 · 1 points · Official 2025 syllabus: 或者…或者 — 官方属三级 L3-CP-6（此为五级进阶用法）*

| Point | Pattern | Example |
|---|---|---|
| Providing two options with double "huozhe" | 或者⋯⋯，或者⋯⋯ | 只 有 一 块 蛋糕，或者 你 吃 或者 我 吃。 |

### L5-CL23 · Let alone 递进（更不用说）
*Category: 句法结构 · 2 points · Official 2025 syllabus: 别说…就是 · 更不用说（官方属七—九级）*

| Point | Pattern | Example |
|---|---|---|
| Expressing "let alone" with "bie shuo" | 别说⋯⋯，就是⋯⋯ | 别说 一百 ， 就是 一 块 钱 我 也 不 给 你 。 |
| Expressing "let alone" with "geng buyong shuo" | ⋯⋯，更不用说⋯⋯ | 她 会 说 法语 ， 更 不用 说 英语 了 。 |

### L5-CL24 · Adverbs 副词
*Category: 相似语法点辨析 · 1 points · Official 2025 syllabus: L5-WC-1 语气副词 毕竟/反正/干脆/简直/白 · L5 时间副词 曾经 · 再也不（L4-FX-2）· 差点没（L4 差点儿）· 好不容易/再三（官方属六级）· 顺便/互相（support）*

| Point | Pattern | Example |
|---|---|---|
| Comparing "changchang" and "jingchang" | 常常 vs. 经常 | 我 不 常 运动 ，我 需要 经常 运动 。 |

### L5-CL25 · Auxiliary Words 虚词
*Category: 相似语法点辨析 · 1 points · Official 2025 syllabus: 啊（列举）— 官方叹词 啊（support）*

| Point | Pattern | Example |
|---|---|---|
| Comparing "zongsuan" and “zhongyu" | 总算 vs 终于 | 今天 的 会 终于 开 完 了！你 总算 来 了。 |

### L5-CL26 · Conjunctions 连词
*Category: 相似语法点辨析 · 1 points · Official 2025 syllabus: 要不 — L5-CP-3 要不然 branch*

| Point | Pattern | Example |
|---|---|---|
| Comparing "gen" and "dui" | 跟 vs 对 | 那 个 帅哥 在 对 我 招手！那 你 要 跟 他 去 吗？ |

### L5-CL27 · Prepositions 介词
*Category: 相似语法点辨析 · 4 points · Official 2025 syllabus: L5 介词 自从/凭/据/依据/替/同/朝/沿着（support）· 给+被动（L5-SP-5）· 至于（官方属六级 L6-WC-3）· 趁/就…而言*

| Point | Pattern | Example |
|---|---|---|
| Comparing "chao" "xiang" and "wang" | 朝 vs 向 vs 往 | 往 前 走 十 分 钟。向 雷锋 同志 学习！他 朝 我 笑 了 笑。 |
| Comparing "dui" and "duiyu" | 对 vs. 对于 | 我 对 她 很 了解 ，她 不 会 这么 做 的 。 |
| Comparing "duiyu" and "zhiyu" | 关于 vs 对于 vs 至于 | 关于 放假， 对于 怎么解决，至于另外一份工作 。 |
| Comparing "gei" and "wei" | 给 vs. 为 | 为 你 准备 的 礼物 |

### L5-CL28 · Time Words 时间词辨析
*Category: 相似语法点辨析 · 2 points · Official 2025 syllabus: 相似语法点辨析 — 用作 R4 场景选择题的题源*

| Point | Pattern | Example |
|---|---|---|
| Comparing "pingshi" and "pingchang" | 平时 vs. 平常 | 你 平时 / 平常 做饭 吗 ？ |
| Comparing "yihou" and "zhihou" | 以后 vs. 之后 | 我 昨天 吃完 以后 去 了 超市 。之后 我 就 回家 了 。 |

### L5-CL29 · Verbs 动词
*Category: 相似语法点辨析 · 2 points · Official 2025 syllabus: V+什么（L5-WC-2 X什么X）· 不像/不如/比起（L4-SP-4 比较句3）· 化（官方属六级 L6-WC-1）· 算 · 难怪*

| Point | Pattern | Example |
|---|---|---|
| Comparing "kanqilai" and "kanlai" | 看起来 vs. 看来 | 这 家 餐厅 看起来 不错 。 看来 你 喜欢。 |
| Comparing "xiande" and "kanqilai" | 显得 vs 看起来 | 你 看起来 很 苗条 ，可能 是 这 件 衣服 显得 你 很 苗条 。 |


## HSK 6 clusters

HSK 6 has **15 clusters / 64 points** (wiki old-HSK scheme). Cluster order below is the wiki's teaching order — the order the syllabus introduces them.

### L6-CL01 · Adverbs 副词
*Category: 词类 · 15 points · Official 2025 syllabus: L6 副词（support）倒是/很是/足足/一再/向来/果然/似乎/偏偏/一律/无非/一向/何必/到时候 · 凡是（L6-CP-4）*

| Point | Pattern | Example |
|---|---|---|
| Advanced usages of the contrary "dao" | Subject + Verb + 得 + 倒 + Adjective | 你 说 得 倒 容易，那 你来！ |
| Emphasizing with "henshi" | Subj. + 很是 + Adj. | 这样做 很是 必要 。 |
| Expressing "a full" with "zuzu" | 足足 + Verb | 姚明 身高 足足 有 2.26米。 |
| Expressing "again and again" with "yizai" | Subj. + 一再 + Verb | 我 一再 跟 你 说 ，出门在外 要 小心 。 |
| Expressing "all" with "fanshi" | 凡是 + Noun 都 / 就 / 一律 + Predicate | 凡是 不 听话 的 孩子 都 没有 糖 吃 。 |
| Expressing "always previously" with "xianglai" | Subject + 向来（都） + Verb/Verb Phrase | 我 向来 努力，所以 我 每 一 次 考试 都 获得 满分。 |
| Expressing "as expected" with "guoran" | 果然 + Predicate | 第一名 果然 是 她 ！我 就 知道 。 |
| Expressing "as if" with "sihu" | Subj. + 似乎 ⋯⋯ | 你 说 得 似乎 很 有道理 。 |
| Expressing "contrary to expectations" with "pianpian" | A ,Subject + 偏偏 + B | 不 叫 他 去，他 偏偏 要 去。 |
| Expressing "even so" with "zaibu... ye..." | 再不…… 也…… | 再不 也。 |
| Expressing "no exception" with "yilu" | 一律 + Predicate | 明天 的 部门 会议 一律 都 要 参加 。 |
| Expressing "nothing but" with "wufei" | 无非 + 是 + Verb / Noun | 我 无非 是 想 要 一 台 电脑 ！ |
| Expressing "since the beginning" with "yixiang" | 一向 + Verb | 他 做 事情 一向 踏实 。 |
| Expressing "when the time comes" with "dao shihou" | A, 到时候 + B | 现在 不 好好 准备 考试，到时候 又 要 后悔 了。 |
| Expressing "why" with "hebi" | Subj. + 何必 + Predicate | 都是 一家人 ，你们 何必 这么 客气 ？ |

### L6-CL02 · Auxiliary Words 虚词
*Category: 词类 · 1 points · Official 2025 syllabus: 来着 — 口语语气词，无官方对应*

| Point | Pattern | Example |
|---|---|---|
| Expressing that something has already happened with "laizhe" | Sentence + 来着 | 刘老师 说 课本 在 桌子 上 来着。 |

### L6-CL03 · Conjunctions 连词
*Category: 词类 · 4 points · Official 2025 syllabus: 以及/总之（L5 连词）· 则（书面）· 以免（官方属七—九级）*

| Point | Pattern | Example |
|---|---|---|
| Expressing "as well as" with "yiji" | Subj. + 何必 + Predicate | A ，B + 以及 + C |
| Expressing "in short" with "zongzhi" | （⋯⋯ ，）总之 ，⋯⋯ | 不管 他 的 理由 是 什么 ，总之 ，我 不会 再 相信 他 了 。 |
| Indicating contrast with "ze" | Clause 1，+ 则 + Clause 2 | 南方 人 喜欢 吃 甜 的 东西，北方 人 则 喜欢 吃 咸 的 东西。 |
| "In order to avoid" with "yimian" | 以免 + Verb Phrase | 这儿 有 高压电线，请 不要 靠近，以免 发生 危险。 |

### L6-CL04 · Nouns 名词
*Category: 词类 · 2 points · Official 2025 syllabus: 本（L5 指示代词）· 性（L6-WC-1 类后缀 -性）*

| Point | Pattern | Example |
|---|---|---|
| Expressing "your side" with "ben" | 本 + Noun | 是 本 公司 的 商业 模式。 |
| Indicating a characteristic with "xing" | Word + 性 | 发生 地震 的 可能性 较 大。 |

### L6-CL05 · Particles 助词
*Category: 词类 · 5 points · Official 2025 syllabus: 是否 · 之（L4 助词 之）· 嘛 · 与否 · 呗（L6-WC-3 书面虚词）*

| Point | Pattern | Example |
|---|---|---|
| Expressing "is or is not" with "shifou" | 是否 + Verb/Adjective | 我 不 知道 如果 那 个 房间 是否 有 足够 空间。 |
| Expressing possession with "zhi" | Noun + 之 + Noun | 这些 解决 问题 的 方式 仍然 有 不足 之 处。 |
| Expressing the self-evident with "ma" | Statement + 嘛 | 大家 有 话 就 说 嘛 。 |
| Expressing "whether or not" with "yufou" | Verb/Adjective + 与否 | 成功 与否，都 靠 自己。 |
| Using the particle "bei" | Sentence + 呗 | 如果 你 不 想 去 就 不 去 呗。 |

### L6-CL06 · Prepositions 介词
*Category: 词类 · 1 points · Official 2025 syllabus: 鉴于（官方属七—九级）*

| Point | Pattern | Example |
|---|---|---|
| Expressing "in light of" with "jianyu" | 鉴于 + observation, conclusion/suggestion | 鉴于 是 紧急 情况，我们 应该 尽快 做出 决定。 |

### L6-CL07 · Sentence patterns 句式
*Category: 词类 · 12 points · Official 2025 syllabus: 非…不可（关联 L4-FX-4 X也得X）· 岂不是 · 兼 · 莫非 · 由此 · 非得（官方属七—九级）· 莫过于（七—九级）· 与其…不如（七—九级）· 似的（L5 助词）· 不愧是 · 由…做主 · 一来…二来（七—九级）*

| Point | Pattern | Example |
|---|---|---|
| Adding emphasis with "fei....buke" | Subj. + 非(要) + Verb Phrase (+ 不可) | 我 非 学 好 汉语 不可 。 |
| "Could it be that" with "qibushi" | 岂不是 + rhetorical question | 如果 他 要 来， 岂不是 一 件 好 事？ |
| Expressing "at the same time" with "jian" | Subject + 兼 + Verb + A + 和 + B | 这 首 歌 的 主唱 兼 词 作者 就 是 他 。 |
| Expressing "could it be possible that" with "mofei" | Subject + 莫非 + rhetorical question | 莫非 你 真的 相信 他？ |
| Expressing "from this" with "youci" | 由此 + Verb | 人们 滥 用 农药 和 其他 化学 原料，由此 产生 了 一系列 严重 的 食品 安全 问题。 |
| Expressing “must" with "feidei" | 非得 + Action + 不可/不行/不成 | 现在 是 紧急 情况，医生 非得 马上 开 刀 不可。 |
| Expressing "nothing is more...than" with "moguoyu" | Object 1 + 莫过于 + Object 2 | 美国 最 好 的 大学 莫过于 哈佛大学。 |
| Expressing "rather than..." with "yuqi... buru" | 与其 + A，宁可 / 宁愿 / 宁肯）+ B | 与其 这样 等着，不如 找点 事 做做。 |
| Expressing "similar to" with "gen... shide" | 跟 + Noun/Pronoun/Adjective + 似的 | 他们 俩 好 得 跟 亲 姐妹 似的。 |
| Expressing "to be worthy of" with "bukuishi" | 不愧是（不愧为）+ N | 他 不愧是 一名 光荣的 人民 教师。 |
| Expressing who is in charge with "you... zuozhu" | Area of responsibility + 由 + Person(s) + 做主 | 作为 商店 经理，所有 的 事情 都 由 你 做主，出 了 事情 也 由 你 负责。 |
| Stating two or more reasons with "yilai...erlai" | 一来 + Reason 1 ，二来 + Reason 2 | 一来 是那边 的 宾馆 很 贵，二来 也那边 没有 什么 好看 的 风景。 |

### L6-CL08 · Verbs 动词
*Category: 词类 · 1 points · Official 2025 syllabus: 谅 — 书面，无官方对应*

| Point | Pattern | Example |
|---|---|---|
| Expressing "I bet" using "liang" | 谅 + Subject + Verb phrase | 谅 他 也 不敢！ |

### L6-CL09 · Verb phrases 动词短语
*Category: 词类 · 2 points · Official 2025 syllabus: 不屑 · 以便（L6-CP-6 目的复句）*

| Point | Pattern | Example |
|---|---|---|
| Expressing something is "not worth doing" with "buxie" | Subject + 不屑(于) + Verb | 我 的 同事 是 一位 很 诚实 的 人 ，他 不屑 说谎。 |
| Facilitating an outcome with "yibian" | 以便 + Verb | 用 普通话 说 ， 以便 我 能 听懂 。 |

### L6-CL10 · Cause/Effect Statements 因果复句
*Category: 句法结构 · 1 points · Official 2025 syllabus: 因…而…（官方属七—九级；关联 L4 为了…而）*

| Point | Pattern | Example |
|---|---|---|
| Using "because" with "er" to indicate effect | 因为⋯⋯ ，而⋯⋯ | 饭店 因为 物价 上涨 而 涨价 。 |

### L6-CL11 · "If" Statements 假设复句
*Category: 句法结构 · 1 points · Official 2025 syllabus: 假使（官方属七—九级）*

| Point | Pattern | Example |
|---|---|---|
| Expressing "if… then…" with "jiashi" | 假使⋯⋯，就⋯⋯ | 假使 你 遇到 坏人 ， 就 报警 。 |

### L6-CL12 · Sentence Patterns 句式
*Category: 句法结构 · 6 points · Official 2025 syllabus: 以…名义 · 势必/倘若（七—九级）· 所 结构（L6-WC-3）· 通过…使（关联 L4-SP-3 致使）*

| Point | Pattern | Example |
|---|---|---|
| Additional way to express "in the name of" | Subj. + 借 + noun + 之名 + situation | 借之名。 |
| Express an action and its effect by using "tongguo… shi" | 通过 + verb (situation occurring)，使 resultative situation | 通过，使国。 |
| Expressing "inevitably" with "shibi" | 势必 | 势必。 |
| Expressing "in the name of" with "yi... de mingyi" | 以 + Subject + 名义 | 不要 以 我的 名义 给公司写信. |
| Use "tangruo" to express "if" | 倘若 + resultative situation | 倘若 有问题，可以给我打个电话。 |
| Using the "suo" structure | 所 + Verb + 的 | 他 所 说 的 话 |

### L6-CL13 · Let alone 递进（更不用说）
*Category: 句法结构 · 1 points · Official 2025 syllabus: 何况（官方属七—九级 …尚且…何况）*

| Point | Pattern | Example |
|---|---|---|
| Expressing "let alone" with "hekuang" | 连⋯⋯都（也）⋯⋯，何况⋯⋯ | 连 小李 都 同意 了 ， 何况 小张。 |

### L6-CL14 · Adverbs 副词
*Category: 相似语法点辨析 · 10 points · Official 2025 syllabus: L6 副词（support）倒是/很是/足足/一再/向来/果然/似乎/偏偏/一律/无非/一向/何必/到时候 · 凡是（L6-CP-4）*

| Point | Pattern | Example |
|---|---|---|
| Comparing "anzhao" and "genju" | 按照 vs 根据 | 按照，根据 |
| Comparing "budebu" and "zhihao" | 不得不 vs 只好 | 刚 下 飞机，还 没 找到 宾馆，行李 不得不/只好 寄存 在 朋友 那。 |
| Comparing "buduan" and "buting" | 不断 vs 不停 | 她 不断 地 找 我，每次 都 说 个 不停。 |
| Comparing "fan'er" and “que" | 反而 vs 却 | 她反而 有点不高兴。他 却 没 带 伞。 |
| Comparing "genben" and "daodi" | 根本 vs 到底 | 我 根本 不知道 女朋友 为什么 生气。我们 到底 什么时候 结束？ |
| Comparing "genju" and "ju" | 根据 vs 据 | 据 他 说，灾情 并 不是 很 严重。根据我的 看法，他 是 个 很 负 责任 的 人。 |
| Comparing "huifu" and "huanyuan" | 恢复 vs 还原 | 中国 1977年 恢复 了 高考。他 想 把 这个 应用程序 还原 成 代码。 |
| Comparing "juran" and "fan'er" | 居然 vs 反而 | 雨 不仅 没 停，反而 越 下 越 大 了 – 他 居然 就 住在 我们家 隔壁，真是 缘分 呐！ |
| Comparing "yishi" and "yidu" | 一度 vs 一时 | 他 过去 一度 想 自杀。这 雨 一时 半会儿 停 不 了。 |
| Comparing "yizhi" and "yixiang" | 一直 vs. 一向 | 我 一直 在 现在 的 公司 工作 。他 一向 不 迟到 。 |

### L6-CL15 · Nouns 名词
*Category: 相似语法点辨析 · 2 points · Official 2025 syllabus: 本（L5 指示代词）· 性（L6-WC-1 类后缀 -性）*

| Point | Pattern | Example |
|---|---|---|
| Comparing "bici" and "duifang" | 彼此 + Verb | 太 吵 了，我们 都 听不到 对方 在 说 什么。 |
| Comparing "renjia" and "bieren" | 人家 vs. 别人 | 因为 人家 喜欢 你 啊 。我 不 在乎 别人 怎么 说 。 |

---

# Appendix — Official 2025 语法大纲 (grammar syllabus)

The official syllabus content below is the source of truth for the official IDs (L{n}-XXX-n)
referenced by clusters above and used by practice worksheets. Levels here are the 2025
syllabus levels (词汇/语法/话题 boundaries per `references/02-level-guide.md`).

## HSK 1

### Primary patterns

| ID | Pattern | Official definition / notes | Example |
|---|---|---|---|
| L1-SP-1 | 是字句1 | 是 = equivalence or class membership | 我是美国人。 |
| L1-SP-2 | 有字句1 | 有 = possession | 我有一个妹妹。 |
| L1-SP-3 | 存现句1 | 处所＋是＋名词；处所＋有＋数量短语＋名词 | 桌子上有一本书。 |
| L1-SP-4 | 连动句1 | Serial verbs: ① second action is purpose ② first is manner | 我去商店买东西。 |
| L1-SP-5 | 双宾语句1 | 主语＋动词＋宾语1＋宾语2 | 老师教我们汉语。 |
| L1-AS-1 | 完成态 了1 | Dynamic 了 marking completed action | 我吃了早饭。 |
| L1-AS-2 | 变化态 了2 | Sentence-final 了 marking new state/change | 下雨了。 |
| L1-AS-3 | 进行态 | （正）在＋V；……呢 | 他在打电话呢。 |
| L1-QT-1 | 是非问句 | V/A＋吗？ | 你是学生吗？ |
| L1-QT-2 | 特指问句 | 谁／什么／哪儿／几／怎么＋…？ | 这是什么？ |
| L1-QT-3 | 正反问句 | V不V / A不A？ | 你去不去？ |
| L1-WC-1 | 能愿动词 | 会、能、想、要、可以 | 我会说汉语。 |
| L1-WC-2 | 离合词 | 看病、睡觉、说话、上课、下课、上班、下班、生病 | 我晚上十点睡觉。 |
| L1-WC-3 | 数量短语与专用量词 | 本、个、家、口、块、件、只、元、杯 ＋ 数字 | 三个苹果 |
| L1-WC-4 | 时间表示法 | 年月日星期；钟点 | 今天星期三。三点一刻。 |
| L1-EX-1 | 序数1／钱数 | 第＋数词；钱数表示法 | 第一次；二十块 |
| L1-CP-1 | 并列复句 | ……，也……；……，还…… | 他是老师，也是我朋友。 |

### Support inventory (secondary content)
- 前缀 小－、第－；后缀 －们、－边
- 方位名词 上、下、里、外、前、后
- 疑问代词 多少、几、哪、哪儿、哪里、哪些、什么、谁、怎么、怎么样
- 人称代词 full set incl. 您、它、大家；指示代词 这/那系列、有的、有些
- 数词 一～十、百、千、半、二/两
- 程度副词 非常、很、太、真、有（一）点儿；范围副词 都；时间副词 在、正在；频率 再；关联 还、也；否定 不、没（有）、不要
- 介词 在、和、对；连词 和；结构助词 的；语气助词 吧、吗、呢；叹词 喂
- 短语结构: 联合、偏正、动宾、主谓；数量、介宾、方位短语
- 句子成分 basics: 主/谓/宾/定/状 + 数量补语1（动词＋动量补语）
- 句型: 动词/形容词/名词谓语句、非主谓句；句类: 陈述、祈使、感叹

---

## HSK 2

### Primary patterns

| ID | Pattern | Official definition / notes | Example |
|---|---|---|---|
| L2-AS-1 | 持续态 着 | ① state continuation ② action continuation | 桌上放着一杯茶。 |
| L2-AS-2 | 经历态 过 | 过 marking past experience | 我去过北京。 |
| L2-SP-1 | 比较句1 | A比B＋形；A比B＋形＋数量/程度补语；A有/没有B（＋这么/那么）＋形；A比B＋V＋得＋形 | 姐姐比我高三厘米。 |
| L2-SP-2 | 是……的句1 | Emphasizes time/place/manner/agent of past event | 我是坐飞机来的。 |
| L2-SP-3 | 存现句2 | 处所＋动词＋着（＋数量短语）＋名词 | 门上写着两个字。 |
| L2-SP-4 | 兼语句1 | 表使令: 主语＋请/叫/让＋O1＋V＋O2 | 妈妈让我买东西。 |
| L2-SP-5 | 有字句2 | 有 = reaching/attaining | 他有一米八。 |
| L2-SP-6 | 双宾语句2 | 主语＋V＋给＋宾语1＋宾语2 | 我送给他一本书。 |
| L2-CP-1 | 转折复句 | 虽然……但是…… | 虽然很累，但是我很快�。 |
| L2-CP-2 | 因果复句 | 因为……所以…… | 因为下雨，所以我在家。 |
| L2-CP-3 | 紧缩复句 | 一……就…… | 他一到家就做作业。 |
| L2-QT-1 | 选择问句 | （是）……还是……？ | 你喝茶还是喝咖啡？ |
| L2-CM-1 | 结果补语1 | V＋错/懂/好/会/完 | 我听懂了。 |
| L2-CM-2 | 趋向补语1 | V＋来/去；V＋上/下/进/出/过/回；复合趋向 | 他拿出一个苹果。 |
| L2-CM-3 | 状态补语1 | V＋得＋形容词短语 | 她唱得很好。 |
| L2-CM-4 | 数量补语2 | 动作持续时量；形容词＋数量补语 | 我等了半个小时。 |
| L2-WC-1 | 动词重叠 | AA、A一A、A了A、ABAB | 我们试试吧。 |
| L2-WC-2 | 形容词重叠 | AA、AABB | 她的房间干干净净。 |
| L2-FX-1 | 要/快要/就要……了 | Imminent change | 火车就要开了。 |
| L2-FX-2 | 还是……吧 | Suggestion after weighing | 我们还是明天去吧。 |
| L2-FX-3 | 都……了 | "already" emphasis | 都十二点了，睡吧！ |

### Support inventory
- 后缀 面；方位名词 左、右；能愿动词 可能
- 疑问代词 为什么；人称代词 自己；指示代词 那么、那样、这么、这样、每
- 数词 万、好多、多；量词 条、位、间、名、包、次
- 副词: 程度 多、好、最；时间 已经、有时（候）、快、快要、正、还2；频率 常、经常；否定 别；关联 再2、就1；语气 都2、就2、还是1
- 介词 从1、往、从2、给、比、跟1、因为1；连词 跟2、但、但是、那、虽然、还是2、因为2、所以
- 结构助词 得、地；动态助词 过、着；语气助词 呢4、吧2、的2、啊1
- 短语: 动补短语1、"的"字短语、连谓短语、兼语短语、动宾离合词 帮忙、游泳、跳舞、跑步
- 句子成分: 受事主语；名词性短语作谓语；动词性/主谓短语作定语
- 句型: 主谓谓语句；祈使句 with 别
- 特殊表达法: 序数2（数词＋量词）；概数1（几；数词＋多＋量词；数词＋量词＋多）

---

## HSK 3

### Primary patterns

| ID | Pattern | Official definition / notes | Example |
|---|---|---|---|
| L3-SP-1 | 把字句1 | ① S＋把＋O＋V＋在/到＋处所 ② S＋把＋O1＋V（＋给）＋O2 ③ S＋把＋O＋V＋结果/趋向/状态补语 | 请把门关上。 |
| L3-SP-2 | 被动句1 | ① S＋被＋O＋V＋其他 ② S＋被＋V＋其他 | 作业被我做完了。 |
| L3-SP-3 | 比较句2 | A比B＋更/还＋形；A跟B一样（＋形）；A不比B＋形；A比B＋多/少/早/晚＋V＋数量短语 | 今天跟昨天一样冷。 |
| L3-SP-4 | 存现句3 | ① 出现: 处所＋V＋趋向/结果补语＋了＋数量＋人/物 ② 消失 | 前面开过来一辆车。 |
| L3-SP-5 | 是……的句2 | Emphasizes speaker's view/attitude | 我是不会去的。 |
| L3-SP-6 | 重动句 | S＋V＋O＋V＋补语 | 我看书看了一个小时。 |
| L3-SP-7 | 连动句2 | V1＋着＋V2 (accompanying action) | 我们坐着聊吧。 |
| L3-CP-1 | 承接复句 | 先……再/然后…… | 我先吃饭，然后写作业。 |
| L3-CP-2 | 递进复句 | 不但……而且…… | 他不但会说汉语，还会写。 |
| L3-CP-3 | 假设复句 | 如果……就……；……的话，就…… | 如果下雨，我们就不去了。 |
| L3-CP-4 | 条件复句 | 只有……才……；只要……就…… | 只有努力才能进步。 |
| L3-CP-5 | 并列复句 | 一会儿……一会儿……；又……又……；一边……一边…… | 他一边听音乐一边跑步。 |
| L3-CP-6 | 选择复句 | 或者……或者…… | 周末我们或者爬山，或者游泳。 |
| L3-CP-7 | 目的复句 | 为了……，…… | 为了健康，他每天走路。 |
| L3-CP-8 | 紧缩复句 | ……了……（就）…… | 下了课就去食堂。 |
| L3-CM-1 | 结果补语2 | V＋到/住/走/上 | 我赶上了早班车。 |
| L3-CM-2 | 趋向补语2 | 引申: 结果义 出/起/下；开始 上/起来；持续 下去/下来 | 大家都笑起来了。 |
| L3-CM-3 | 可能补语1 | V＋得/不＋V/A | 我听得懂。 |
| L3-CM-4 | 程度补语1 | A＋得很；A/V＋极了/坏了 | 今天热得很。 |
| L3-FX-1 | 越来越……；越……越…… | Gradual change | 汉语越来越难了。 |
| L3-FX-2 | 除了……（以外），……还/也/都…… | Additive exception | 除了他，我们都去了。 |
| L3-FX-3 | 一……也/都＋不/没…… | Total negation; 一点儿也不 | 我一个问题也没错。 |
| L3-FX-4 | 该……了 | Due time | 该吃饭了。 |
| L3-FX-5 | 对……来说；(在)……以前/以后；在……上/下/中 | Frame setters | 对我来说，这个考试很难。 |
| L3-QT-1 | 反问句1 | 不是……吗？ (rhetorical emphasis) | 这不是你的书吗？ |
| L3-QT-2 | 怎样＋动词 特指问句 | | 你怎样去学校？ |
| L3-WC-1 | 疑问代词非疑问用法 | 任指: 疑问代词＋都；疑＋疑；不定指 | 谁都认识他。 |
| L3-WC-2 | 离合词 | 动宾: 放假、见面、结婚、洗澡；动补: 离开、完成、分开 | 我跟她见过两次面。 |
| L3-WC-3 | 量词重叠 | 个个、张张 (each and every) | 张张纸都写满了。 |
| L3-EX-1 | 概数2 | 大概；相邻数词连用；(L2: 几/多) | 三四个人 |

### Support inventory
- 前缀 老－；后缀 －家、－子、－员；方位名词 东南西北＋方、中间
- 能愿动词 需要、该、应该、愿意、得；人称代词 别人、咱们；指示代词 别的、其他
- 量词 把、双、张、种、层、封、页、辆、节、所、班、段、头、句、公斤、斤、角、毛、刻、米、碗、盘、口、回、遍、声
- 副词: 程度 比较、还3、更、特别、挺、有些、越、极；范围 就3、一块儿、一共、只、到处、只是；时间 才1、马上、先、一会儿、刚(刚)、一直；频率 总(是)、又、常常；关联 一边；情态 大概、必须、差不多、一定、好像、几乎；语气 当然、其实、终于、才2、才3、就4；否定 不必、不用
- 介词 为、向、关于、为了、把、被、根据；连词 或(者)、只有、只要、不但、而且、如果、可(是)、然后；助词 的话
- 固定短语 不一会儿、看来、在……看来、看起来、看上去、一般来说、不怎么样；四字格 不A不B
- 数量重叠 数＋量＋数＋量；同位短语；多项定语
- 概数: 大概；相邻数词连用

---

## HSK 4

### Primary patterns

| ID | Pattern | Official definition / notes | Example |
|---|---|---|---|
| L4-SP-1 | 把字句2 | ① S＋把＋O＋V（＋一/了）＋V ② ＋V＋了 ③ ＋V＋动量/时量补语 ④ ＋状语＋V | 把地扫一扫。 |
| L4-SP-2 | 被动句2 | S＋叫/让＋O＋V＋其他 | 钱包让小偷偷走了。 |
| L4-SP-3 | 兼语句2 | ① 爱憎: 表扬/批评＋O1＋V＋O2 ② 称谓/认定: 收/选＋O1＋做/当/为＋O2 ③ 致使: 使/让＋代＋V短语 | 老师表扬他学习努力。 |
| L4-SP-4 | 比较句3 | ① A不如B（＋形） ② 跟……相比 | 跟去年相比，今年冷多了。 |
| L4-SP-5 | 双重否定句 | Double negation = emphasis | 他不可能不知道。 |
| L4-QT-1 | 反问句2 | 难道……吗？；疑问代词构成的反问句 | 难道你不同意吗？ |
| L4-CM-1 | 程度补语2 | A/心理V＋死了/厉害 | 昨天热死了。 |
| L4-CM-2 | 可能补语2 | V＋得/不＋了 | 今天我忙得很，去不了了。 |
| L4-CP-1 | 并列复句 | 不是……而是……；既……又/也……；一方面……另一方面…… | 我不是不想去，而是没时间。 |
| L4-CP-2 | 承接复句 | 首先……其次/然后……；……，于是…… | 他先道歉，于是我们又和好了。 |
| L4-CP-3 | 递进复句 | ……甚至……；不仅(不光)……还/而且……；……并且……；连……也/都……更…… | 他甚至半夜还在学习。 |
| L4-CP-4 | 选择复句 | 不是……就是…… | 他不是在图书馆，就是在教室。 |
| L4-CP-5 | 转折复句 | 尽管……但是/可是……；……然而……；……不过……；X是X，就是/不过…… | 尽管很贵，但我还是买了。 |
| L4-CP-6 | 假设复句 | ……，否则……；要是……，（就）……，否则…… | 快点儿，否则赶不上火车了。 |
| L4-CP-7 | 条件复句 | 不管/无论……都/也…… | 不管多忙，他都锻炼。 |
| L4-CP-8 | 因果复句 | 既然……就……；（由于）……因此…… | 既然累了，就休息一下。 |
| L4-CP-9 | 目的复句 | ……，好…… | 你慢点儿说，好让我记下来。 |
| L4-CP-10 | 让步复句 | 即使……也……；就是……也…… | 即使失败，我也不放弃。 |
| L4-CP-11 | 紧缩复句 | 不……也…… | 不看也知道结局。 |
| L4-FX-1 | 一＋量＋比＋一＋量 | Progressive increase | 天气一天比一天冷。 |
| L4-FX-2 | 再也不/没…… | Never again | 我再也不迟到了。 |
| L4-FX-3 | 在……方面；拿……来说；够……的 | Frame / degree | 在发音方面，他比我强。 |
| L4-FX-4 | 固定格式 (口语系) | X就是了；还X呢；你X你的吧；X就X（点儿）吧；说什么也得X；X是X | 需要帮忙说一声就是了。 |
| L4-EX-1 | 概数3 | 数词＋来＋量词；大约、左右、前后 | 十来个人；八点左右 |
| L4-EX-2 | 小数/分数/百分数/倍数 | | 增加了百分之二十。 |

### Support inventory
- 能愿动词 敢；指示代词 各、各位、各种、任何、此；量词 打、袋、棵、台、幅、脸、手、盒、屋子、桌子、场、顿、趟
- 副词: 程度 十分、更加、稍(微)、尤其、多么；范围 共、全、光、仅(仅)、至少；时间 按时、从来、赶紧、赶快、已、忽然、将(要)、从、本来；频率 重新、往往、偶尔、再次、老；方式 故意、互相、相互；关联 却；情态 也许、恐怕；语气 才4、就5、并、还4、竟然、究竟、正好、到底、难道、千万、确实、只好、差（一）点儿
- 介词 自、当、由1、随着、等1；将、由2、叫、让；由于1；对于、与1；作为、按(照)
- 连词 此外、而、既然、甚至、不过、并且、不光、不仅、另外、要是、因此、由于2、加上；助词 等2、者、之、就是；叹词 啊、嗯
- 四字格 一A一B、无A无B、有A有B；固定短语 来得及/来不及、有的是、说不定、不怎么、就是说

---

## HSK 5

### Primary patterns

| ID | Pattern | Official definition / notes | Example |
|---|---|---|---|
| L5-SP-1 | 有字句3 | ① 存在/具有: S＋有＋着＋O ② 附着: S＋V＋有＋O | 墙上刻着一行字。他身上带有一种正气。 |
| L5-SP-2 | 把字句3 | ① S＋把＋O＋一＋V ② S＋把＋O1＋V＋O2 | 他把眼一闭，不理我了。 |
| L5-SP-3 | 连动句3 | Two verb phrases in 因果/转折/条件 relation | 他有事没来开会。 |
| L5-SP-4 | 比较句4 | A＋形容词＋B＋数量补语 | 他高我一头。 |
| L5-SP-5 | 被动句3 | S＋被/叫/让＋O＋给＋V＋其他 | 手机被他给摔坏了。 |
| L5-CM-1 | 状态补语2 | V/A＋得＋动词短语 / 主谓短语 / 固定短语 | 他跑得上气不接下气。 |
| L5-CM-2 | 趋向补语3 | 引申, 状态意义: V/A＋下来/下去/起来/过来/过去 | 天色渐渐暗了下来。 |
| L5-CM-3 | 可能补语 | V＋得/不得 | 这种玩笑开不得。 |
| L5-CM-4 | 程度补语 | A/心理V＋得＋不得了 | 他急得不得了。 |
| L5-CP-1 | 承接复句 | ……，便…… | 想通了这一点，心里便轻松了。 |
| L5-CP-2 | 选择复句 | 或是……或是…… | 或是看书，或是散步，他总有安排。 |
| L5-CP-3 | 假设复句 | 一旦……就……；假如……，（就）；万一……，（就）；……要不然/不然 | 一旦决定了，就别犹豫。 |
| L5-CP-4 | 因果复句 | ……，因而……；……，可见…… | 他没来，可见还没收到消息。 |
| L5-CP-5 | 让步复句 | 哪怕……也…… | 哪怕只有一天，也要去看看。 |
| L5-CP-6 | 递进复句 | 不但(没有)……反而……；不是……还/还是…… | 他不但没道歉，反而怪我。 |
| L5-CP-7 | 目的复句 | ……，为的是…… | 他熬夜加班，为的是赶上进度。 |
| L5-CP-8 | 紧缩复句 | 没有……就没有……；不……不……；再……也…… | 再难也要坚持。 |
| L5-FX-1 | 从……来看；(自)……以来；由……组成 | Frame setters | 从长远来看，值得。 |
| L5-FX-2 | A的A，B的B；X着也是X着；不X白不X | Distribution / "might as well" | 不看白不看。 |
| L5-FX-3 | X什么X；什么X不X（的） | Dismissive echo | 什么周末不周末的，忙起来都一样。 |
| L5-WC-1 | 语气副词群 | 毕竟、居然、反正、根本、果然、简直、绝对、的确、反而、白、刚好 | 他居然没打招呼就走了。 |
| L5-WC-2 | 固定短语 | A来A去；A着A着；没A没B；说A就A；不得了；用不着 | 他说走就走。 |

### Support inventory
- 后缀 －头；指示代词 彼此、如此、本
- 量词 册、朵、届、颗、匹、行、架、群、支、根、批、束、副、集、周、眼
- 副词: 程度 过于、相当、较、可2、格外、极其；时间 时刻、曾经、立刻、连忙、始终、早已、即将、急忙、渐渐、尽快、早晚；频率 老是、通常、时常；方式 尽量、亲自；关联 便、一旦；情态 似乎、仿佛
- 介词 自从；朝、沿（着）；替、同1、较2；凭、据、依据；连词 以及、同2、从而、可见、假如、总之；助词 似的

---

## HSK 6

### Primary patterns

| ID | Pattern | Official definition / notes | Example |
|---|---|---|---|
| L6-SP-1 | 把字句4 | ① 非生物主语＋把＋O＋V＋其他 ② S＋把＋O（施事）＋V＋其他 | 这场雨把路都淹了。真把我气坏了。 |
| L6-CP-1 | 并列复句 | 一时……一时…… | 他一时想去，一时又不想去。 |
| L6-CP-2 | 选择复句 | 要么……要么…… | 要么现在，要么永远别来。 |
| L6-CP-3 | 转折复句 | 虽……但/可/却/也…… | 话虽不多，分量却很重。 |
| L6-CP-4 | 条件复句 | 凡是……都……；除非……才……；除非……否则/不然…… | 除非你亲自道歉，否则免谈。 |
| L6-CP-5 | 让步复句 | 就算……也…… | 就算输，也输得体面。 |
| L6-CP-6 | 目的复句 | ……，以便…… | 请提前报名，以便安排座位。 |
| L6-FX-1 | 放着X不Y | Have X but not use it | 放着现成的资料不用，真可惜。 |
| L6-FX-2 | X归X，Y归Y | Separate spheres | 朋友归朋友，生意归生意。 |
| L6-FX-3 | A一量，B一量；东一A，西一A | Scattered instances | 东一句西一句，谁也听不懂。 |
| L6-FX-4 | 早（也）不X，晚（也）不X；不X不……，一X…… | Bad timing / conditional twist | 早不来晚不来，偏偏这时候来。 |
| L6-FX-5 | 到……为止；看/瞧把＋宾语＋X得 | Extent / "look what you did to…" | 瞧把孩子急得直哭。 |
| L6-WC-1 | 类前缀/类后缀 | 超－、多－、反－、无－、亚－、准－；－化、－式、－型、－性 | 超市文化里的"绿色消费"观念。 |
| L6-WC-2 | 四字格 | A这A那；左A右B | 他一进门就指手画脚，东一句西一句。 |
| L6-WC-3 | 书面语虚词 | 于、因、至于、除、所、不料、未必 | 此事至今不明真相，未必属实。 |
| L6-WC-4 | 语气/方式副词群 | 恰好、倒是、干脆、明明、总算、不禁、一再、再三、偷偷 | 他再三强调安全第一。 |
| L6-CM-1 | 程度补语3 | V/A＋透＋了 | 他把话说透了。 |

### Support inventory
- 人称代词 人家；量词 串、滴、枝、扇、卷、番
- 副词: 程度 特、异常、较为；范围 净、一同、大都；时间 一时、不时、仍旧、依旧、一向；频率 一再、再三；方式 不禁、赶忙、特地、特意、偷偷；否定 未必；语气 恰好、倒是、干脆、明明、总算
- 介词 于（时间处所）；至于（对象）；因（目的原因）；除（排除）；连词 不料
- 助词 所（结构）；啦、嘛（语气）；也好；固定短语 好（不）容易、那倒（也）是、算了、得了

---

## Cross-level dependency notes (for sequencing)

- 了1/了2 (L1) must be solid before 是……的 (L2) and 把字句 (L3) worksheets.
- 趋向补语1 (L2) precedes 趋向补语2 引申 (L3) precedes 趋向补语3 状态引申 (L5).
- 比较句 sequence: L2 比 → L3 更/还/一样/不比 → L4 不如/相比 → L5 数量补语.
- 把字句 sequence: L3 basic three forms → L4 动量/时量/状语 forms → L5 一＋V → L6 施事宾语/非生物主语.
- 被动句 sequence: L3 被 → L4 叫/让 → L5 给.
- Before starting an L(n+1) pattern, the review section should confirm the L(n) prerequisite above still holds.
