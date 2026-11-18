# HSK 4 Course Manifest

Comprehensive HSK4 course per `planning/syllabuses/01-hsk-syllabus.md`. Build order = the
unit order below. Status values: `pending` → `generated` → `passed` / `retake` (per Sam's
reported scores). This file + `planning/progress-log.md` answer "what comes next?".

**Sources**: clusters + points from `planning/references/03-grammar-inventory.md` §HSK 4
(official anchors from its appendix) · vocab batches from 词汇大纲 #1001–2000 · topics from
`planning/references/02-level-guide.md`. Worksheet types per
`planning/blueprints/0{1,2,3}-*.md`.

**Merges & splits applied** (per syllabus merge/split rules):
- `L4-CL02 Adverbs` (27 pts) split into CL02a/CL02b/CL02c GT units.
- Trivial clusters merged: CL03 (挺) → CL02c unit · CL04 (什么的/等等) → CL05 unit ·
  CL06 (其中) → CL22 unit · CL07 (分之) → CL24 unit · CL09 (随着/在…上) + CL10 (以…为…)
  → CL23 unit · CL11 (并+不) → CL02c unit · CL13 (不用/得) → CL12 unit ·
  CL19 (即使) → CL20 unit · CL26 (不但…而且) → CL25 unit.
- Comparison clusters folded into parent GTs: CL27 + CL30 → CL02b GT · CL28 → CL23 GT ·
  CL29 → CL15 GT (肯定/确定/一定 → CL02a GT).
- Official 2025 appendix points without an L4 wiki cluster (L4-SP-1 把字句2, L4-SP-2
  被动句2, L4-SP-4 比较句3) get their own P worksheets + a combined GT-SP unit
  (把 vs 被 is the built-in R4 discrimination).

## Grammar track

| Unit | Type | File | Content | Predecessor | Status |
|---|---|---|---|---|---|
| 0 | GT | `gt/hsk4-gt-entry.html` | Level-entry placement mini-check (5–6 R4 over CL01/CL06/CL23 samples + HSK3 core) | — | placed (4/6, 67%) |
| 1 | P | `p/hsk4-ws-001.html` | CL01 · anchor L4-CM-1 程度补语2 死了/厉害 (secondary: 全, 可+Adj) | 0 | completed (2 wrong) |
| 2 | GT | `gt/hsk4-gt-CL01.html` | CL01 Adjectives 形容词 (全, 死了) | 1 | fail (8/11, 73%; retake skipped) |
| 3 | VT | `vt/hsk4-vt-01.html` | Topic 个人情况 · 27 words | 2 | passed (r2 10/12, 83%) |
| 4 | P | `p/hsk4-ws-002.html` | CL02a · anchor L4-QT-1 反问句2 难道/究竟 | 3 | generated |
| 5 | P | `p/hsk4-ws-003.html` | CL02a · anchor L4-SP-5 双重否定 不得不/只好 | 4 | generated |
| 6 | GT | `gt/hsk4-gt-CL02a.html` | CL02a 语气/评价类副词 (看来 恐怕 甚至 还是 最好 不得不 只好 竟然 千万 难道 到底 究竟) | 5 | generated |
| 7 | VT | `vt/hsk4-vt-02.html` | Topic 饮食 · 27 words | 6 | generated |
| 8 | P | `p/hsk4-ws-004.html` | CL02b · anchor L4-FX-1 一+量+比+一+量 + L4-FX-2 再也不 | 7 | generated |
| 9 | P | `p/hsk4-ws-005.html` | CL02b · anchor 时间副词 contrast 刚/原来/本来/差点/从来 | 8 | generated |
| 10 | GT | `gt/hsk4-gt-CL02b.html` | CL02b 时间/频率副词 (刚 原来 本来 差点 从来 结果 正好 先…再) + CL27 + CL30 comparisons | 9 | generated |
| 11 | P | `p/hsk4-ws-006.html` | CL02c · anchor 程度/范围 十分/更加/稍微/尤其/挺 + 又+不/可不/差不多 | 10 | pending |
| 12 | GT | `gt/hsk4-gt-CL02c.html` | CL02c 数量/范围/程度 (差不多 又+不 没 可 够 一+量+比+一+量 也都 就) + CL03 挺 + CL11 并不 | 11 | pending |
| 13 | VT | `vt/hsk4-vt-03.html` | Topic 交通出行 · ~27 words | 12 | pending |
| 14 | P | `p/hsk4-ws-007.html` | CL05 · anchor 追加/递进连词 此外/另外/还有/再说/加上 + 什么的/等等 | 12 | pending |
| 15 | P | `p/hsk4-ws-008.html` | CL05 · anchor 顺承/对比连词 于是/而/不过 | 14 | pending |
| 16 | GT | `gt/hsk4-gt-CL05.html` | CL05 Conjunctions 连词 (8 pts) + CL04 | 15 | pending |
| 17 | VT | `vt/hsk4-vt-04.html` | Topic 购物 · ~27 words | 16 | pending |
| 18 | P | `p/hsk4-ws-009.html` | CL08 · anchor 语气助词 的/吧/啊 + 确认问 吗 | 16 | pending |
| 19 | GT | `gt/hsk4-gt-CL08.html` | CL08 Particles 助词 (吗 确认 / 吧 列举 / 的 语气) | 18 | pending |
| 20 | P | `p/hsk4-ws-010.html` | CL12 · anchor L4-SP-3 兼语句2 让/叫/请/使 | 19 | pending |
| 21 | P | `p/hsk4-ws-011.html` | CL12 · anchor 认知动词 以为/好像/通过/在于/要看 + 不用/得 | 20 | pending |
| 22 | GT | `gt/hsk4-gt-CL12.html` | CL12 Verbs 动词 (8 pts) + CL13 | 21 | pending |
| 23 | VT | `vt/hsk4-vt-05.html` | Topic 休闲 · ~27 words | 22 | pending |
| 24 | P | `p/hsk4-ws-012.html` | CL14 · anchor 离合词 advanced + V着V着就 | 22 | pending |
| 25 | P | `p/hsk4-ws-013.html` | CL14 · anchor V+到 结果/时段 + 值得/害得 | 24 | pending |
| 26 | GT | `gt/hsk4-gt-CL14.html` | CL14 Verb phrases 动词短语 (11 pts) | 25 | pending |
| 27 | P | `p/hsk4-ws-014.html` | 官方补点 · anchor L4-SP-1 把字句2 (动量/时量/状语 forms) | 26 | pending |
| 28 | P | `p/hsk4-ws-015.html` | 官方补点 · anchor L4-SP-2 被动句2 叫/让 | 27 | pending |
| 29 | P | `p/hsk4-ws-016.html` | 官方补点 · anchor L4-SP-4 比较句3 不如/跟…相比 | 28 | pending |
| 30 | GT | `gt/hsk4-gt-SP.html` | 官方核心句式: 把字句2 vs 被动句2 vs 比较句3 (R4 discrimination) | 29 | pending |
| 31 | VT | `vt/hsk4-vt-06.html` | Topic 医疗健康 · ~27 words | 30 | pending |
| 32 | P | `p/hsk4-ws-017.html` | CL15 · anchor L4-CP-5 转折复句 尽管…但是/然而/却/不过 (secondary 倒/反而) | 30 | pending |
| 33 | GT | `gt/hsk4-gt-CL15.html` | CL15 "But" 转折 (尽管…但是 倒 却) + CL29 comparisons | 32 | pending |
| 34 | P | `p/hsk4-ws-018.html` | CL16 · anchor L4-CP-8 既然…就 / 由于…因此 | 33 | pending |
| 35 | GT | `gt/hsk4-gt-CL16.html` | CL16 Cause/Effect 因果 (由于 既然…就 因此) | 34 | pending |
| 36 | VT | `vt/hsk4-vt-07.html` | Topic 家庭生活 · ~27 words | 35 | pending |
| 37 | P | `p/hsk4-ws-019.html` | CL17 · anchor L4-CM-2 可能补语2 得/不了 (secondary 起来引申) | 35 | pending |
| 38 | GT | `gt/hsk4-gt-CL17.html` | CL17 Complements 补语 (起来引申 趋向 可能补语) | 37 | pending |
| 39 | P | `p/hsk4-ws-020.html` | CL18 · anchor 条件复句 只要…就/只有…才 (secondary 除非) | 38 | pending |
| 40 | GT | `gt/hsk4-gt-CL18.html` | CL18 Conditional 条件 (只要…就 除非…才) | 39 | pending |
| 41 | P | `p/hsk4-ws-021.html` | CL20 · anchor L4-CP-6 要是…就 + L4-CP-10 即使/就是…也 (CL19 merged) | 40 | pending |
| 42 | GT | `gt/hsk4-gt-CL20.html` | CL20 If/CL19 Even If 假设+让步 (要是 即使 就是…也) | 41 | pending |
| 43 | VT | `vt/hsk4-vt-08.html` | Topic 学习与校园 · ~27 words | 42 | pending |
| 44 | P | `p/hsk4-ws-022.html` | CL21 · anchor L4-CP-7 不管/无论…都 | 42 | pending |
| 45 | GT | `gt/hsk4-gt-CL21.html` | CL21 No Matter 无条件 (不管 无论) | 44 | pending |
| 46 | P | `p/hsk4-ws-023.html` | CL22 · anchor 范围 所有/任何/各 + 之一/其中/另外+数量 | 45 | pending |
| 47 | GT | `gt/hsk4-gt-CL22.html` | CL22 Noun Phrases 名词短语 (所有 之一 另外) + CL06 其中 | 46 | pending |
| 48 | P | `p/hsk4-ws-024.html` | CL23 · anchor L4-CP-3 连…也/都…更 + 连+V+都 | 47 | pending |
| 49 | P | `p/hsk4-ws-025.html` | CL23 · anchor L4-CP-1 既…又/一方面…另一方面 + 为…而/以…为/随着/在…上 | 48 | pending |
| 50 | GT | `gt/hsk4-gt-CL23.html` | CL23 Sentence Patterns 句式 (连…都 为…而 任何 既…也 在…上) + CL09 + CL10 + CL28 | 49 | pending |
| 51 | VT | `vt/hsk4-vt-09.html` | Topic 职场生活 · ~27 words | 50 | pending |
| 52 | P | `p/hsk4-ws-026.html` | CL24 · anchor L4-EX-1 概数 + L4-EX-2 分数/百分数/倍数 (secondary 一点儿也不/一般来说) | 50 | pending |
| 53 | GT | `gt/hsk4-gt-CL24.html` | CL24 Basic/Simple 基本句式 (连+Subj+都 疑问代词+都 倍数 一点儿也不 不知道…好 一般来说) + CL07 分之 | 52 | pending |
| 54 | P | `p/hsk4-ws-027.html` | CL25 · anchor L4-CP-3 递进复句 不但/不仅…而且/还/也 | 53 | pending |
| 55 | P | `p/hsk4-ws-028.html` | CL25 · anchor L4-FX-4 X是X 让步格式 + 一…就 承接 (CL26 merged) | 54 | pending |
| 56 | GT | `gt/hsk4-gt-CL25.html` | CL25 Complex 复杂句式 (X是X 一…就 一方面…另一方面) + CL26 不但…而且 | 55 | pending |
| 57 | VT | `vt/hsk4-vt-10.html` | Topic 自然与环境 · ~27 words | 56 | pending |
| 58 | VT | `vt/hsk4-vt-11.html` | Topic 科技与网络 · ~27 words | 57 | pending |
| 59 | VT | `vt/hsk4-vt-12.html` | Topic 当代社会 · 概况 · ~27 words | 58 | pending |
| 60 | VT | `vt/hsk4-vt-13.html` | Topic 当代社会 · 经济 · ~27 words | 59 | pending |
| 61 | VT | `vt/hsk4-vt-14.html` | Topic 当代社会 · 社会现象 · ~27 words | 60 | pending |
| 62 | VT | `vt/hsk4-vt-15.html` | Topic 文艺 · ~27 words | 61 | pending |
| 63 | VT | `vt/hsk4-vt-16.html` | Topic 体育 · ~27 words | 62 | pending |
| 64 | VT | `vt/hsk4-vt-17.html` | Topic 中外交流 · 旅游 · ~27 words | 63 | pending |
| 65 | VT | `vt/hsk4-vt-18.html` | Topic 文化 · 饮食文化 · ~27 words | 64 | pending |
| 66 | VT | `vt/hsk4-vt-19.html` | Topic 文化 · 民俗传统 · ~27 words | 65 | pending |
| 67 | VT | `vt/hsk4-vt-20.html` | Topic 文化 · 语言文字 · ~27 words | 66 | pending |
| 68 | VT | `vt/hsk4-vt-21.html` | Topic 文化 · 人文景观与历史 · ~27 words | 67 | pending |
| 69 | VT | `vt/hsk4-vt-22.html` | Topic 网络生活 · ~27 words | 68 | pending |
| 70 | VT | `vt/hsk4-vt-23.html` | Topic 居住与社区 · 房屋租赁 · ~27 words | 69 | pending |
| 71 | VT | `vt/hsk4-vt-24.html` | Topic 成长过程 · ~27 words | 70 | pending |
| 72 | VT | `vt/hsk4-vt-25.html` | Topic 教育问题 · ~27 words | 71 | pending |
| 73 | VT | `vt/hsk4-vt-26.html` | Topic 科普知识 · ~27 words | 72 | pending |
| 74 | VT | `vt/hsk4-vt-27.html` | Topic 人生感悟 · ~27 words | 73 | pending |
| 75 | VT | `vt/hsk4-vt-28.html` | Topic 人际交往礼仪 · ~27 words | 74 | pending |
| 76 | VT | `vt/hsk4-vt-29.html` | Topic 职场交往 · ~27 words | 75 | pending |
| 77 | VT | `vt/hsk4-vt-30.html` | Topic 少数民族 · ~27 words | 76 | pending |
| 78 | VT | `vt/hsk4-vt-31.html` | Topic 国粹 · ~27 words | 77 | pending |
| 79 | VT | `vt/hsk4-vt-32.html` | Topic 名胜古迹 · ~27 words | 78 | pending |
| 80 | VT | `vt/hsk4-vt-33.html` | 综合复习 1 · leftover L4 words + earlier misses | 79 | pending |
| 81 | VT | `vt/hsk4-vt-34.html` | 综合复习 2 · leftover L4 words + earlier misses | 80 | pending |
| 82 | VT | `vt/hsk4-vt-35.html` | 综合复习 3 · leftover L4 words + earlier misses | 81 | pending |
| 83 | VT | `vt/hsk4-vt-36.html` | 综合复习 4 · leftover L4 words + earlier misses | 82 | pending |

**Wave 2** = units 11–13 (`p/hsk4-ws-006.html`, `gt/hsk4-gt-CL02c.html`, `vt/hsk4-vt-03.html`).

## Vocabulary track (36 batches, 词汇大纲 #1001–2000, ~70% L4 / 30% lower)

| VT | Topic | Anchor words noted at generation | Status |
|---|---|---|---|
| 01 | 日常生活 · 个人情况 | 年龄 性别 性格 脾气 帅 美 笨 诚实 粗心 细心 活泼 幽默 害羞 骄傲 耐心 自信 懒 眼镜 皮肤 印象 (+高 漂亮 聪明 忙 岁 哥哥 女儿) | passed (r2; still review 眼镜 + 性格搭配) |
| 02 | 日常生活 · 饮食 | 餐厅 厨房 厨师 味道 酸 辣 咸 香 汽水 酸奶 快餐 馒头 月饼 葡萄 巧克力 西红柿 汤 烤 聚餐 (+米饭 面条儿 茶 牛奶 饺子 好吃 苹果) | generated |
| 03 | 日常生活 · 交通出行 | 机场/交通 words: 大巴 动车 电动车 出租车?(L1) 交警 航班 乘客 乘坐 出行 交通 堵车 加油站 车位 车速 十字路口 出口 入口 导游 旅行 旅客 旅馆 景点 景区 (+自行车 L3 火车 L1 飞机 L1 出租车 L1) | pending |
| 04 | 日常生活 · 购物 | 商品 购买 购物 价格 价钱 打折 降价 便宜?(L1) 费用 付 支付 现金 零钱 红包 快递 网购 牌子 质量 顾客 纸巾 袋子 (+买 L1 卖 L1 贵 L1 商店 L1 超市 L1) | pending |
| 05 | 日常生活 · 休闲 | 健身 健身房 散步 电视剧 小说 话剧 演出 演唱 演员 歌手 排球 乒乓球 球迷 球队 聚会 聚 旅游? 钢琴 琴 弹 跳舞?(L2) 度假 晚? (+电视 L1 电影 L1 唱 L1 看书? L2 休息 L1) | pending |
| 06 | 日常生活 · 医疗健康 | 打针 医生?(L1) 护士 大夫 病人?(L2 病) 咳嗽 头痛 体检 体温 体重 血 身体?(L2) 受伤 危险 严重 健康?(L3) 恢复?(L5) 药?(L2) 酸? no — final list at generation | pending |
| 07 | 家庭生活 | 家庭 家乡 家具 家长 父母 父亲 母亲 父女 父子 母女 母子 孙女 孙子 兄弟 亲戚 老家 童年 成长?(L5) 红包 零花钱 房东 房租 (+家 L1 妈妈 L1 哥哥 L1 儿子 L1) | pending |
| 08 | 教育 · 学习与校园 | 课程 课堂 课堂 教师 教授 教学 学生?(L1) 高考 考生 笔试 口语 听力 预习 自习 自学 学费 学院 研究生 硕士 博士 本科 毕业生 教育 表扬 批评 (+学习 L1 学校 L1 大学 L1 作业 L3) | pending |
| 09 | 职场生活 | 办公 办事 加班 打工 工资 奖金 工人 经理?(L3) 部门 单位 负责 负责人 负担? 任务 职业 专业 面试 应聘 招聘 出差 团队? 合作?(L5) 队长 竞争 生意 (+工作 L1 公司 L1 上班 L1 老板 L1) | pending |
| 10 | 自然与环境 | 森林 树林 植物 叶子 云 雨?(L1) 气候 气温 温度 零下 寒冷 暖和 大自然 地球 污染 环保 垃圾 火 高温 低温 海洋 江 桥 (+天气 L1 热 L1 冷 L1 春天 L3 雪 L1) | pending |
| 11 | 科技与网络 | 科技 技术 科学 互联网 网址 网页 网友 视频 信号 信息 消息 短信 手机?(L1) 电脑?(L1) 打印 打印机 发送 回复 转发 扫码 密码 人工智能? no — L4 only; final at generation | pending |
| 12 | 当代社会 · 概况 | 城市?(L3) 农村 郊区 街道 社会 人口?(L2) 民族 国家?(L1) 国籍 国际 亚洲 首都 东部/南部/西部/北部 中年 老年 青年 儿童 少年 姑娘 小伙子 (+中国 L1 人 L1 名字 L1) | pending |
| 13 | 当代社会 · 经济 | 价格 市场 生意 经济 增加 增长 减价?(降价) 降低 减少 上升?下降 赚 钱?(L1) 银行?(L1) 现金 付费? 成功 失败 竞争 (+买 L1 贵 L1 便宜 L1) | pending |
| 14 | 当代社会 · 社会现象 | 日常 日常? — 乱 危险 规定 禁止 法律 允许 误会 抱歉 道歉 误会 批评 表扬 帮助?(L1) 机会?(L2) 人员 人数 大众? final at generation | pending |
| 15 | 文艺 | 艺术 文章 文字 小说 杂志 新闻?(L3) 话剧 京剧 演出 演员 演唱 歌声 观众 听众 读者 作者?(L5? no—作家 L4 #1993) 琴 弹 举 举办 举行 精彩 (+歌 L1 电影 L1 唱 L1) | pending |
| 16 | 体育 | 比赛?(L3) 参赛 大赛 打败 赢 输 球队 球迷 排球 乒乓球 教练 运动员? no—L4 list check at generation; 竞争 成功 失败 观众 举办 举行 加油 (+锻炼 L3 篮球? L2? verified at generation) | pending |
| 17 | 中外交流 · 旅游 | 签证 护照?no 机场?no—L3? 航班 登机 乘客 乘坐 出租 导游 景点 景区 景色 风景 美景 旅行 旅客 旅馆 度假 假日 节假日 暑假 寒假 参观 (+飞机 L1 火车 L1 出租车 L1) | pending |
| 18 | 文化 · 饮食文化 | 中餐 白酒 茶叶 厨师 味道 干杯 聚餐 月饼 饺子?(L1) 包子?(L1) 葡萄酒 小吃 香辣咸酸 + related L4 (餐 食品 食物) (+米饭 L1 茶 L1) | pending |
| 19 | 文化 · 民俗传统 | 传统?(L4? not in list — 民俗 at L5) 红包 节假日 假日 拜年?(L6) 亲戚 童年 饺子 月饼 中秋? final at generation from verified L4 words | pending |
| 20 | 文化 · 语言文字 | 词语 语法 普通话 文字 文章 阅读 例子 例如 翻译 解释 说明 表达?(L4 表达? #1035 表现) 知识 学问?(L3) 理解 意见 意思?(L2) (+汉语 L1 汉字 L1 字 L1 词典 L3) | pending |
| 21 | 文化 · 人文景观与历史 | 著名 京剧 名胜? 景点 古代?(L5) 历史人物? — final at generation (L4: 著名 景区 景色 参观 传统?…) | pending |
| 22 | 网络生活 | 网页 网址 网友 视频 信号 信息 消息 短信 发送 回复 转发 密码 打印 打印机 扫码 下载? 上传? 在线? — final L4 list at generation (+手机 L1 电脑 L1) | pending |
| 23 | 居住与社区 · 房屋租赁 | 房东 房租 家具 社区 邻居 地址 搬 搬家 房间 客厅 厨房 卫生间 钥匙 安静 吵 环境 (+家 L1 房子 L1 住 L1) | pending |
| 24 | 成长过程 | 童年 成长 回忆 经历 经验 梦想 理想 希望 努力 成功 失败 改变 原来 本来 当时 后来 (+小时候 L3 现在 L1) | pending |
| 25 | 教育问题 | 教育 高考 考生 研究生 硕士 博士 本科 毕业生 学费 预习 自习 自学 表扬 批评 压力 态度 (+学习 L1 学校 L1 老师 L1) | pending |
| 26 | 科普知识 | 科学 技术 研究 发现 实验 地球 海洋 植物 动物 温度 气候 原因 结果 证明 知识 (+知道 L1 为什么 L1) | pending |
| 27 | 人生感悟 | 幸福 烦恼 心情 印象 感情 感觉 理解 意见 态度 信心 勇气 失望 满意 后悔 将来 (+想 L1 觉得 L2) | pending |
| 28 | 人际交往礼仪 | 礼貌 客气 互相 友好 友谊 感谢 邀请 拒绝 道歉 误会 介绍 联系 打扰 欢迎 (+朋友 L1 认识 L1) | pending |
| 29 | 职场交往 | 同事 经理 部门 负责 任务 会议 出差 加班 通知 安排 合作 团队 汇报 材料 客户 (+工作 L1 公司 L1) | pending |
| 30 | 少数民族 | 民族 文化 传统 节日 风俗 语言 服装 特色 地区 西部 南部 保护 尊重 多样 (+中国 L1 人 L1) | pending |
| 31 | 国粹 | 京剧 功夫 茶叶 书法 武术 艺术 表演 演员 观众 传统 著名 代表 特色 欣赏 (+中国 L1 文化 L3) | pending |
| 32 | 名胜古迹 | 景点 景区 景色 风景 参观 著名 历史 建筑 博物馆 导游 旅行 旅客 门票 拍照 (+去 L1 旅游 L3) | pending |
| 33 | 综合复习 1 | Mixed leftovers + re-tests of words flagged "needs review" in earlier VTs | pending |
| 34 | 综合复习 2 | Mixed leftovers + re-tests of words flagged "needs review" in earlier VTs | pending |
| 35 | 综合复习 3 | Mixed leftovers + re-tests of words flagged "needs review" in earlier VTs | pending |
| 36 | 综合复习 4 | Mixed leftovers + re-tests of words flagged "needs review" in earlier VTs | pending |

**Word coverage rule**: every 词汇大纲 L4 word (#1001–2000) lands in ≥1 batch. After
batch 32, audit the manifest word lists against #1001–2000 and sweep leftovers into the
综合复习 batches.

## Progress notes

- Wave 1 (units 0–10): generated 2026-11-05. Browser-verified P (MCQ + pinyin), GT
  (score-summary + `data-point`), VT (bank-fill reset + `data-word`).
- Unit 0 taken 2026-11-05: **4/6 (67%)**, placed in the 50–79% band. Missed
  `程度补语2 死了` (item 3) and `反问句` (item 6).
- Unit 1 taken 2026-11-10: ws-001 completed, 2 items wrong (which items not reported).
- Unit 2 taken 2026-11-10: **hsk4-gt-CL01 8/11 (73%) — fail**. Sam skipped the retake
  (browser closed) and is advancing. Next unit: `vt/hsk4-vt-01.html`. Carry 死了 and
  反问句 in later review sections. Do **not** backfill `gt/retakes/hsk4-gt-CL01-r2.html`.
- Unit 3 taken 2026-11-12 / retake 2026-11-16: **hsk4-vt-01-r2 10/12 (83%) — pass**.
  Still review: 眼镜, 性格/脾气/耐心/诚实/细心配对. Next: `p/hsk4-ws-002.html` (反问句).
- Wave 2: units 11–13 (`p/hsk4-ws-006.html` CL02c 程度/范围, `gt/hsk4-gt-CL02c.html`,
  `vt/hsk4-vt-03.html` 交通出行). Next "continue the course" request starts here.
- When Sam reports a test score: update unit status, append progress-log row. If a
  cluster GT/VT is <80%, generate the remediation P (grammar) **and** the retake HTML in
  `{gt|vt}/retakes/` immediately, unless he skips. Entry placement is not a cluster gate.
