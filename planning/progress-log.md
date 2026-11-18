# Progress Log

Append one line per generated unit. The 温故知新 (review) section of each new worksheet pulls
from the most recent line, one from ~3 lines back, and one from ~7–10 lines back
(see `syllabuses/01-hsk-syllabus.md` §Review protocol). "needs review" comes from the
paste-report Sam copies from the worksheet (`needs_review:` line) — that content is
REQUIRED in the next worksheet's review section and re-tested in the next GT/VT.

Format:
`date | worksheet_id | type | level | unit (points / cluster / batch topic) | score | verdict | needs_review`

- type: P (practice) · GT (grammar test) · VT (vocabulary test)
- score/verdict: P worksheets leave as `—`; GT/VT record `X/Y (Z%)` + pass/fail once Sam
  reports (80% pass guideline). On fail, generate a retake in `{gt|vt}/retakes/` unless
  Sam skips; a completed retake replaces the failed attempt's row.
- needs_review: missed points (`data-point`) or words (`data-word`) from the paste-report
  (P, GT, and VT all emit this field).

---

2026-11-02 | hsk3-ws-014 | P | 3 | L3-SP-1 把字句1 · 搬家与整理房间 | — | (example file — not completed by Sam yet) | —

2026-11-05 | hsk4-gt-entry | GT | 4 | Level-entry placement mini-check (CL01/CL06/CL23 preview + HSK3 core) | 4/6 (67%) | placed (50–79% band — start HSK4 with review) | 程度补语2 死了 (L4-CL01); 反问句 (HSK3 core)
2026-11-10 | hsk4-ws-001 | P | 4 | L4-CL01 · L4-CM-1 程度补语2 死了 / 全 | — | completed (2 items wrong; which items not reported) | (unspecified — send item numbers / 词语收藏 if you want them in the remediating P)
2026-11-10 | hsk4-gt-CL01 | GT | 4 | L4-CL01 Adjectives 形容词 (全, 死了) | 8/11 (73%) | fail (retake skipped — Sam advancing) | 3 auto-scored items missed (list not reported); still flag 死了 + 反问句 from entry
2026-11-16 | hsk4-vt-01-r2 | VT | 4 | 日常生活 · 个人情况 (retake of vt-01) | 10/12 (83%) | pass | 眼镜; 性格/脾气/耐心/诚实/细心配对
2026-11-05 | hsk4-ws-002 | P | 4 | L4-CL02a · L4-QT-1 反问句2 难道/究竟 | — | generated | —
2026-11-05 | hsk4-ws-003 | P | 4 | L4-CL02a · L4-SP-5 双重否定 不得不/只好 | — | generated | —
2026-11-05 | hsk4-gt-CL02a | GT | 4 | CL02a 语气/评价类副词 | — | generated (not yet taken) | —
2026-11-05 | hsk4-vt-02 | VT | 4 | 日常生活 · 饮食 · 27 words | — | generated (not yet taken) | —
2026-11-05 | hsk4-ws-004 | P | 4 | L4-CL02b · L4-FX-1 一+量+比+一+量 + L4-FX-2 再也不 | — | generated | —
2026-11-05 | hsk4-ws-005 | P | 4 | L4-CL02b · 时间副词 contrast 刚/原来/本来/差点/从来 | — | generated | —
2026-11-05 | hsk4-gt-CL02b | GT | 4 | CL02b 时间/频率副词 + CL27 + CL30 | — | generated (not yet taken) | —
