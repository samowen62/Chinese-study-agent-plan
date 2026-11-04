#!/usr/bin/env python3
"""Build the cluster-spine section of references/03-grammar-inventory.md
from scripts/wiki-clusters.json. Prints markdown to stdout."""
import json
import sys

DATA = r'Z:\Chinese\planning\scripts\wiki-clusters.json'

# Chinese names for the three wiki "part" sections
PART_ZH = {
    'Parts of Speech': '词类',
    'Grammatical Structures': '句法结构',
    'Comparisons of Similar Grammar Points': '相似语法点辨析',
}

# Chinese names for cluster (section) headings
CLUSTER_ZH = {
    'Adverbs': '副词', 'Adverbs with Adjectives': '副词修饰形容词',
    'Conjunctions': '连词', 'Nouns': '名词', 'Numbers': '数词',
    'Particles': '助词', 'Prepositions': '介词', 'Verbs': '动词',
    'Auxiliary verbs': '能愿动词', 'Auxiliary Verbs': '能愿动词辨析', 'Verb phrases': '动词短语',
    'Adjectives': '形容词', 'Auxiliary Words': '虚词',
    'Measure Words': '量词', 'Prepositional Phrase': '介宾结构',
    'Sentence patterns': '句式', 'Sentence Patterns': '句式',
    'Basics': '基础句型', 'Noun Phrases': '名词短语',
    'Numbers and Measure Words': '数量表达', 'Question Forms': '疑问句式',
    'Basic/Simple Sentence Patterns': '基本句式',
    'Comparison Patterns': '比较句式',
    'Complex Sentence Patterns': '复杂句式', 'Complements': '补语',
    'Conditional Statements': '条件复句', 'Cause/Effect Statements': '因果复句',
    '"But" Statements': '转折复句', '"Even If" Statements': '让步复句',
    '"If" Statements': '假设复句', '"No Matter" Statements': '无条件复句',
    'Not only… but also…': '递进复句', 'Either… or': '选择复句',
    'Let alone': '递进（更不用说）', 'Separate Functions': '功能辨析',
    'Time Words': '时间词辨析',
}

# Official 2025-syllabus cross-references, keyed by (level, cluster name).
# "support" = covered by the level's official support inventory (see appendix).
XREF = {
 (1,'Adverbs'): 'L1-AS-3 进行态 · 否定/程度/范围/关联副词（support）',
 (1,'Adverbs with Adjectives'): '程度副词 多/很/太/有（一）点儿（support）',
 (1,'Conjunctions'): '连词 和（support）',
 (1,'Nouns'): '时间/方位名词（support）；注：以前/以后 在官方新大纲属三级 L3-FX-5',
 (1,'Numbers'): 'L1-WC-3 数量短语 · L1-WC-4 时间表示法 · L1-EX-1 序数/钱数',
 (1,'Particles'): 'L1-AS-1 了1 · L1-AS-2 了2 · 结构助词 的 · 语气助词 吗/呢/吧（support）',
 (1,'Verbs'): 'L1-SP-1 是字句 · L1-SP-2 有字句 · L1-SP-3 存现句 · 连动句（support）',
 (1,'Auxiliary verbs'): 'L1-WC-1 能愿动词 会/能/想/要/可以',
 (1,'Verb phrases'): 'L1-QT-2 特指问（怎么）· 没有+V（support）· 在+处所+V',
 (1,'Basics'): 'L1-SP-1 是字句 · 动词/形容词谓语句（support）· 太+Adj+了',
 (1,'Noun Phrases'): '数量短语 一些（support）',
 (1,'Numbers and Measure Words'): 'L1-EX-1 钱数 · 几+量词',
 (1,'Question Forms'): 'L1-QT-1 是非问 · L1-QT-2 特指问 · L1-QT-3 正反问 · 了吗',
 (1,'Sentence Patterns'): '是…的 — 官方新大纲属二级 L2-SP-2',
 (2,'Adverbs'): 'L2 副词（support）· L2-FX-1 要/快要/就要…了 · L2-FX-3 都…了 · 再2/就1/就2/还是1/别',
 (2,'Adverbs with Adjectives'): 'L2 程度副词 多/好/最（support）· 有点儿 · 离（介词）· 更（官方属三级）',
 (2,'Conjunctions'): '口语填充词 那个 — 无官方对应（生成时标注为口语）',
 (2,'Measure Words'): '量词重叠 MW+MW（官方 L3-WC-3 量词重叠属三级）',
 (2,'Nouns'): '…的时候 — 官方时间表达（support，L3 范围）',
 (2,'Numbers'): '概数1 数词+多（L2-EX support）',
 (2,'Numbers and Measure Words'): '每+量词 · 第+数词 序数2 · 几+量+名 · 这/那+量词（support）',
 (2,'Particles'): 'L2-AS-1 着 · L2-AS-2 过 · 的2/呢4/吧2/啊1（support）',
 (2,'Prepositions'): 'L2 介词 从/往/给/比/跟（support）· L2-SP-1 比较句1',
 (2,'Verbs'): '姓 — 称谓表达（support）',
 (2,'Auxiliary verbs'): 'L1-WC-1 能愿动词延伸：要/可以（support）',
 (2,'Verb phrases'): 'L2-CM-1 结果补语 · V+给+O（L2-SP-6）· L2-WC-1 动词重叠 · 一下 · 动量词 · 连动句',
 (2,'Complements'): 'L2-CM-1 结果补语1 · L2-CM-2 趋向补语1 · L2-CM-3 状态补语1 · L2-CM-4 数量补语2',
 (2,'Question Forms'): 'L1-QT-3 正反问 · L2-QT-1 选择问 还是 · 反问 不是…吗（官方属三级 L3-QT-1）· tag questions',
 (2,'Sentence Patterns'): 'L2-CP-2 因为…所以 · L2-SP-2 是…的 · 别+V+了 · 什么+都/也（官方属三级 L3-FX-3）',
 (2,'Basic/Simple Sentence Patterns'): '每+量词+都（support）',
 (2,'Comparison Patterns'): 'L2-SP-1 比较句1（…多了）',
 (2,'Complex Sentence Patterns'): 'L2-CP-1 虽然…但是',
 (3,'Adjectives'): 'L3-CM-4 程度补语1 极了 · 形容词重叠（L2-WC-2 延伸）· Adj+地 状语（support）',
 (3,'Adverbs'): 'L3 副词（support）又/一直/总是/才/终于/只/几乎 · L3-CP-1 先…再 · L3-CP-5 一边…一边',
 (3,'Adverbs with Adjectives'): 'L3 程度副词 比较/更/特别/挺/多（support）· L3-SP-3 跟…一样 · 又…又（L3-CP-5）',
 (3,'Conjunctions'): 'L3-CP-6 或者…或者 · L3-QT-1 还是 · 那么/跟（support）',
 (3,'Nouns'): '时间词 以前/刚才/时/后来（support）',
 (3,'Numbers'): 'L3-EX-1 概数2（相邻数词）· 万/亿',
 (3,'Particles'): '着/了/的/得/地/呢（support，承 L2）',
 (3,'Prepositions'): 'L3 介词 关于/向/为了/根据/把/被（support）',
 (3,'Verbs'): '看起来 · 兼语句 让/叫/请/使（L2-SP-4 承接）· 经过 · L3-SP-3 没（有）+比较',
 (3,'Auxiliary verbs'): 'L3 能愿动词 应该/该/得/需要（support）',
 (3,'Verb phrases'): 'V+了+时量（L2-CM-4 承接）· 难+V · 没办法 · V+V 重叠（L2-WC-1）',
 (3,'Complements'): 'L3-CM-1 结果补语2 · L3-CM-2 趋向补语2 引申 · L3-CM-3 可能补语1',
 (3,'Conditional Statements'): 'L3-CP-4 只要…就 / 只有…才 · 除非（官方属六级 L6-CP-4）',
 (3,'Noun Phrases'): '有的（L1 指示代词 support）',
 (3,'Numbers and Measure Words'): '数+量+半+名（数量表达 support）',
 (3,'Sentence Patterns'): 'L3-FX-3 一…也/都+不/没 · L3-FX-1 越…越 · L3-SP-1 把字句 · L3-SP-2 被动句',
 (3,'Basic/Simple Sentence Patterns'): 'L3-SP-3 存现句 · L3-WC-1 疑问代词非疑问用法 · L3-FX-1 越来越 · L3-CP-7 为了',
 (3,'Comparison Patterns'): 'L3-SP-3 比较句2（有…吗/跟…比/更/还/…多了）',
 (3,'Complex Sentence Patterns'): 'L3-FX-2 除了…以外 · L3-CP-3 如果…（的话）就 · L3-CP-2 不但…而且',
 (4,'Adjectives'): 'L4-CM-1 程度补语2 死了 · 全（范围 support）',
 (4,'Adverbs'): 'L4 副词（support）· L4-QT-1 反问句2 难道/疑问代词反问 · L4-SP-5 双重否定 不得不 · L4-FX-1 一+量+比+一+量 · 千万/只好/差点儿/竟然/毕竟?（毕竟属五级）',
 (4,'Adverbs with Adjectives'): '挺（官方属三级程度副词）',
 (4,'Auxiliary Words'): 'L2 什么的 · L4 其他助词 等2/等等',
 (4,'Conjunctions'): 'L4 连词（support）不过/于是/另外/再说/而/还有 · L4-CP-* 系列',
 (4,'Nouns'): '其中（指示 support）',
 (4,'Numbers'): 'L4-EX-2 分数 分之',
 (4,'Particles'): '吗（确认问）/吧（列举）/的2 语气（support）',
 (4,'Prepositions'): 'L4 介词 随着/在…上（在…上/下/中 官方属三级 L3-FX-5）',
 (4,'Sentence patterns'): '以…为… — 书面结构，无直接官方对应（生成时按固定格式处理）',
 (4,'Sentence Patterns'): '并+不 — 语气副词 并（L4 support）',
 (4,'Verbs'): 'L4-SP-3 兼语句2 让/叫/使 · 好像/以为/通过/来自/在于/要看（support）',
 (4,'Auxiliary verbs'): '不用 · 得（L3 能愿动词）',
 (4,'Verb phrases'): '并/并且 · 少+V/多+V · 由（L4 介词 由1/由2）· 从来 · 值得 · V+到 · 害得 · L3-WC-2 离合词 · V着V着就…',
 (4,'"But" Statements'): 'L4-CP-5 转折复句 尽管…但是/然而/不过 · 倒 · 却（关联副词 support）',
 (4,'Cause/Effect Statements'): 'L4-CP-8 既然…就 / （由于）…因此 · 由于/因此',
 (4,'Complements'): 'L4-CM-2 可能补语2 得/不了 · 起来引申（L3-CM-2）· 趋向（L2-CM-2 承接）',
 (4,'Conditional Statements'): 'L4-CP-7 只要…就 · 除非…才（官方属六级 L6-CP-4）',
 (4,'"Even If" Statements'): 'L4-CP-10 即使…也',
 (4,'"If" Statements'): 'L4-CP-6 要是…就',
 (4,'"No Matter" Statements'): 'L4-CP-7 不管/无论…都',
 (4,'Noun Phrases'): '所有 · 之一 · 另外+数量（support）',
 (4,'Sentence Patterns'): 'L4-FX-1 连…都/也 · 为…而（L4-FX-2）· 任何（指示）· 既…也/又（L4-CP-1）· 在…上/下/里（L3-FX-5）',
 (4,'Basic/Simple Sentence Patterns'): 'L4-FX-2 一点儿也不 · 连+Subj+都（L4-FX-1）· 疑问代词+都（L3-WC-1）· L4-EX-2 倍数 · 对/一般来说（L3-FX-5）',
 (4,'Complex Sentence Patterns'): 'X是X concession（L4-FX-4）· 一…就（L2-CP-3 延伸）· 一方面…另一方面（L4-CP-1）',
 (4,'Not only… but also…'): 'L4-CP-3 递进复句 不但/不仅…而且/还/也',
 (5,'Adjectives'): 'L5-CM-4 得+不得了 · 得很 · Adj+了+（一）点儿 · 有的是（官方属四级固定短语）',
 (5,'Adverbs'): 'L5-WC-1 语气副词 毕竟/反正/干脆/简直/白 · L5 时间副词 曾经 · 再也不（L4-FX-2）· 差点没（L4 差点儿）· 好不容易/再三（官方属六级）· 顺便/互相（support）',
 (5,'Auxiliary Words'): '啊（列举）— 官方叹词 啊（support）',
 (5,'Conjunctions'): '要不 — L5-CP-3 要不然 branch',
 (5,'Nouns'): 'L5 指示代词 彼此 · （自）…以来（L5-FX-1）· 当中 · 当…的时候 · N+这个（口语）',
 (5,'Particles'): '了+宾语/补语（advanced，承 L4 把字句2）· 嘛（官方属六级）· 呢（softening）',
 (5,'Prepositional Phrase'): '以上/以下（数目表达 support）',
 (5,'Prepositions'): 'L5 介词 自从/凭/据/依据/替/同/朝/沿着（support）· 给+被动（L5-SP-5）· 至于（官方属六级 L6-WC-3）· 趁/就…而言',
 (5,'Sentence Patterns'): '要不是 · 多亏 · 而已 · 将（formal 把，关联 L5-SP-2）',
 (5,'Verbs'): 'V+什么（L5-WC-2 X什么X）· 不像/不如/比起（L4-SP-4 比较句3）· 化（官方属六级 L6-WC-1）· 算 · 难怪',
 (5,'Auxiliary verbs'): '将/将要（L4 时间副词 将 support）',
 (5,'Verb phrases'): '难免（官方属七—九级）· 受（书面被动，关联 L5-SP-5）',
 (5,'Adverbs with Adjectives'): '格外（L5 程度副词）',
 (5,'"But" Statements'): 'L5-CP-6 反而（不但不…反而）',
 (5,'Cause/Effect Statements'): '之所以…是因为（因果倒装，关联 L5-CP-4 …可见）',
 (5,'Complements'): 'L5-CM-1 状态补语2 · L5-CM-2 趋向补语3 引申 · L5-CM-3 得/不得 · L5-CM-4 不得了 · V来V去（L5-WC-2）· 坏了（L4-CM-1）',
 (5,'Conditional Statements'): 'L5-CP-3 一旦…就',
 (5,'"Even If" Statements'): 'L5-CP-5 哪怕…也 · 就是/就算…也（承 L4-CP-10）',
 (5,'"If" Statements'): 'L5-CP-3 假如/万一/不然 · 的话（L3 助词）',
 (5,'Sentence Patterns'): 'L5-SP-2 把字句3 · 不比（L3-SP-3）· 少不了 · 等于 · 从…中 · V就V · 无…可… · 不但…甚至连（L5-CP-6）· 好（L4-CP-9 目的）· 有关的 · 一面…一面（L3-CP-5）· 所谓 · 不是…就是（L4-CP-4）· 在…内 · 宁可…也（官方属七—九级）',
 (5,'Complex Sentence Patterns'): '怪不得/难怪（L5-WC-1）',
 (5,'Either… or'): '或者…或者 — 官方属三级 L3-CP-6（此为五级进阶用法）',
 (5,'Let alone'): '别说…就是 · 更不用说（官方属七—九级）',
 (6,'Adverbs'): 'L6 副词（support）倒是/很是/足足/一再/向来/果然/似乎/偏偏/一律/无非/一向/何必/到时候 · 凡是（L6-CP-4）',
 (6,'Auxiliary Words'): '来着 — 口语语气词，无官方对应',
 (6,'Conjunctions'): '以及/总之（L5 连词）· 则（书面）· 以免（官方属七—九级）',
 (6,'Nouns'): '本（L5 指示代词）· 性（L6-WC-1 类后缀 -性）',
 (6,'Particles'): '是否 · 之（L4 助词 之）· 嘛 · 与否 · 呗（L6-WC-3 书面虚词）',
 (6,'Prepositions'): '鉴于（官方属七—九级）',
 (6,'Sentence patterns'): '非…不可（关联 L4-FX-4 X也得X）· 岂不是 · 兼 · 莫非 · 由此 · 非得（官方属七—九级）· 莫过于（七—九级）· 与其…不如（七—九级）· 似的（L5 助词）· 不愧是 · 由…做主 · 一来…二来（七—九级）',
 (6,'Verbs'): '谅 — 书面，无官方对应',
 (6,'Verb phrases'): '不屑 · 以便（L6-CP-6 目的复句）',
 (6,'Cause/Effect Statements'): '因…而…（官方属七—九级；关联 L4 为了…而）',
 (6,'"If" Statements'): '假使（官方属七—九级）',
 (6,'Sentence Patterns'): '以…名义 · 势必/倘若（七—九级）· 所 结构（L6-WC-3）· 通过…使（关联 L4-SP-3 致使）',
 (6,'Let alone'): '何况（官方属七—九级 …尚且…何况）',
}

# Comparison clusters: cross-ref pattern is "<wordA> vs <wordB> 辨析" — build automatically
for lvl in (1, 2, 3, 4, 5, 6):
    pass


def main():
    data = json.load(open(DATA, encoding='utf-8'))
    out = []
    for lvlobj in data:
        lvl = lvlobj['level']
        out.append(f"\n## HSK {lvl} clusters\n")
        out.append(f"HSK {lvl} has **{len(lvlobj['clusters'])} clusters / {lvlobj['total_points']} points** "
                   f"(wiki old-HSK scheme). Cluster order below is the wiki's teaching order — "
                   f"the order the syllabus introduces them.\n")
        k = 0
        for c in lvlobj['clusters']:
            k += 1
            cid = f"L{lvl}-CL{k:02d}"
            name = c['name']
            zh = CLUSTER_ZH.get(name)
            if zh is None:
                print(f"WARNING: no ZH name for {name!r}", file=sys.stderr)
                zh = ''
            part = PART_ZH.get(c['part'], c['part'])
            xref = XREF.get((lvl, name))
            if xref is None and c['part'] == 'Comparisons of Similar Grammar Points':
                xref = '相似语法点辨析 — 用作 R4 场景选择题的题源'
            if xref is None:
                print(f"WARNING: no XREF for HSK{lvl} {name!r}", file=sys.stderr)
                xref = '（待补）'
            out.append(f"### {cid} · {name} {zh}")
            out.append(f"*Category: {part} · {len(c['points'])} points · Official 2025 syllabus: {xref}*\n")
            out.append("| Point | Pattern | Example |")
            out.append("|---|---|---|")
            for p in c['points']:
                t = p['title'].replace('|', '\\|')
                pat = p['pattern'].replace('|', '\\|')
                ex = p['example'].replace('|', '\\|')
                out.append(f"| {t} | {pat} | {ex} |")
            out.append("")
    sys.stdout.write('\n'.join(out))
    with open(r'Z:\Chinese\planning\scripts\inventory-spine.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(out))


if __name__ == '__main__':
    main()
