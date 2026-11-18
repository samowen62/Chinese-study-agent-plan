"""Patch HSK worksheet HTML: hover pinyin, no Show-all, paste-report instead of emojis."""
from __future__ import annotations
import re
from pathlib import Path

ROOT = Path(r"Z:\Chinese")
FILES = list((ROOT / "courses" / "hsk4").rglob("*.html"))
FILES += [
    ROOT / "planning" / "templates" / "example-worksheet-hsk3-ba.html",
    ROOT / "planning" / "scripts" / "test-scorebox.html",
]

PINYIN_CSS = """  .zh { position:relative; cursor:help; border-bottom:1px dashed #d8d2c4; padding-top:1.05em; }
  .zh:hover::before {
    content:attr(data-py); position:absolute; top:0; left:0; right:0;
    font-size:.62em; color:var(--accent); text-align:center; white-space:nowrap;
    font-family:Arial,sans-serif; pointer-events:none; }"""

REPORT_CSS_LINE = (
    '  .scorebox pre.report { background:#f6f4ef; border:1px solid var(--line);'
    ' border-radius:8px; padding:12px; font-size:.85rem; white-space:pre-wrap;'
    ' font-family:Consolas,"Courier New",monospace; }\n'
)

REPORT_CSS_BLOCK = """  .scorebox { background:var(--card); border:2px solid var(--accent); border-radius:12px; padding:16px; margin-top:36px; }
  .scorebox .result { font-size:1.1rem; font-weight:700; margin:8px 0; }
  .scorebox .verdict-pass { color:var(--ok); }
  .scorebox .verdict-fail { color:var(--bad); }
  .scorebox pre.report { background:#f6f4ef; border:1px solid var(--line); border-radius:8px; padding:12px; font-size:.85rem; white-space:pre-wrap; font-family:Consolas,"Courier New",monospace; }
  .score-result { display:none; } .score-result.show { display:block; }
"""

SCOREBOX_HTML = """<div class="scorebox">
  <p><b>报告 Report</b> — 做完选择题后点按钮，把生成的文字贴到课程对话里。</p>
  <button class="btn score-btn">生成报告 / Copy report</button>
  <div class="score-result"></div>
</div>"""

REPORT_JS = r"""
document.addEventListener('click', e => {
  if (e.target.matches('.copy-report')) {
    const pre = e.target.closest('.scorebox').querySelector('pre.report');
    if (pre) navigator.clipboard.writeText(pre.textContent);
    return;
  }
  if (!e.target.matches('.score-btn')) return;
  const box = e.target.closest('.scorebox');
  const result = box.querySelector('.score-result');
  if (!result) return;
  let total = 0, right = 0;
  const missed = []; const seen = new Set();
  const tag = (el) => el.dataset.point || el.dataset.word
    || (el.closest('.item') && (el.closest('.item').dataset.point || el.closest('.item').dataset.word))
    || ((el.closest('.item') || el).querySelector('.qno') || {}).textContent
    || 'item';
  document.querySelectorAll('.mcq').forEach(mcq => {
    total++;
    const ok = mcq.dataset.done && !mcq.querySelector('.opt.incorrect');
    if (ok) { right++; return; }
    const w = tag(mcq);
    if (w && !seen.has(w)) { seen.add(w); missed.push(String(w).trim()); }
  });
  document.querySelectorAll('.item[data-answers]').forEach(it => {
    total++;
    const want = it.dataset.answers.split(/\s+/);
    const got = [...it.querySelectorAll('.slot')].map(s => s.dataset.filled || '_');
    const ok = want.length === got.length && want.every((w, i) => got[i] === w);
    if (ok) { right++; return; }
    const w = it.dataset.word || it.dataset.point || '选词填空';
    if (!seen.has(w)) { seen.add(w); missed.push(w); }
  });
  const pct = total ? Math.round((right / total) * 100) : 0;
  const type = document.body.dataset.type || 'P';
  const id = document.body.dataset.id || '';
  let verdict = '—';
  if (type === 'GT' || type === 'VT') verdict = pct >= 80 ? 'pass' : 'fail';
  const report =
`worksheet_id: ${id}
type: ${type}
score: ${right}/${total} (${pct}%)
verdict: ${verdict}
needs_review: ${missed.length ? missed.join(', ') : '—'}
notes:`;
  const cls = (type !== 'P' && pct >= 80) ? 'verdict-pass' : 'verdict-fail';
  result.innerHTML =
    `<p class="result">得分 Score: <span class="${cls}">${right} / ${total} (${pct}%)</span></p>` +
    `<pre class="report">${report}</pre>` +
    `<button type="button" class="btn copy-report">复制 Copy</button>` +
    `<p style="font-size:.85rem;color:#6b6558;margin-top:8px">把上面的报告整段粘贴到课程对话里，我会记进 progress-log 并安排下一课。</p>`;
  result.classList.add('show');
  navigator.clipboard.writeText(report).catch(() => {});
});
"""


def infer_meta(text: str, path: Path) -> tuple[str, str]:
    m = re.search(r"worksheet_id:\s*(\S+)", text)
    wid = m.group(1) if m else path.stem
    if "-vt-" in wid:
        typ = "VT"
    elif "-gt-" in wid:
        typ = "GT"
    else:
        typ = "P"
    return wid, typ


def inject_body(attrs: str, wid: str, typ: str) -> str:
    attrs = re.sub(r'\sdata-id="[^"]*"', "", attrs)
    attrs = re.sub(r'\sdata-type="[^"]*"', "", attrs)
    return f'<body{attrs} data-id="{wid}" data-type="{typ}">'


def patch(text: str, path: Path) -> str:
    wid, typ = infer_meta(text, path)

    # --- pinyin CSS ---
    text = re.sub(
        r"  \.zh \{ position:relative; cursor:pointer; border-bottom:1px dashed #d8d2c4; \}\s*"
        r"(?:  \.zh\.show::before, body\.py-all \.zh::before \{[^}]+\}\s*"
        r"|  \.zh\.show::before \{[^}]+\}\s*  body\.py-all \.zh::before \{[^}]+\}\s*)",
        PINYIN_CSS + "\n",
        text,
    )
    # leftover show/py-all rules if CSS split differently
    text = re.sub(
        r"  \.zh\.show::before, body\.py-all \.zh::before \{[^}]+\}\s*",
        "",
        text,
    )
    text = text.replace(
        "  .zh { position:relative; cursor:pointer; border-bottom:1px dashed #d8d2c4; }",
        PINYIN_CSS.split("\n")[0],
    )
    if ".zh:hover::before" not in text and ".zh {" in text:
        text = text.replace(
            ".zh { position:relative; cursor:help; border-bottom:1px dashed #d8d2c4; }",
            PINYIN_CSS.replace("\n", "\n").split("\n")[0]
            + "\n"
            + "\n".join(PINYIN_CSS.split("\n")[1:]),
            1,
        )

    # --- Show-all button ---
    text = re.sub(
        r'\s*<span><button class="btn" id="pyAll">显示拼音 / Show pinyin</button></span>\s*',
        "\n",
        text,
    )

    # --- emoji CSS ---
    text = re.sub(
        r"  \.selfcheck \{[^}]+\}\s*",
        "",
        text,
    )
    text = re.sub(r"  \.conf \{[^}]+\}\s*", "", text)
    text = re.sub(r"  \.conf\.sel \{[^}]+\}\s*", "", text)

    # --- report CSS ---
    if ".scorebox pre.report" not in text:
        if "  .scorebox {" in text:
            text = text.replace("  .scorebox {", REPORT_CSS_LINE + "  .scorebox {", 1)
        else:
            text = text.replace("</style>", REPORT_CSS_BLOCK + "</style>", 1)

    # --- body data-id / data-type ---
    text = re.sub(
        r"<body([^>]*)>",
        lambda m: inject_body(m.group(1), wid, typ),
        text,
        count=1,
    )

    # --- selfcheck / emoji rows → scorebox ---
    text = re.sub(
        r"<!-- ============ Self-check strip ============ -->\s*<div class=\"selfcheck\">.*?</div>",
        "<!-- ============ Report ============ -->\n" + SCOREBOX_HTML,
        text,
        count=1,
        flags=re.S,
    )
    text = re.sub(
        r'<div class="selfcheck">.*?</div>',
        SCOREBOX_HTML,
        text,
        count=1,
        flags=re.S,
    )
    text = re.sub(
        r'<p><b>自评打分[^<]*</b>.*?</p>\s*',
        "",
        text,
        flags=re.S,
    )
    text = re.sub(r'<p><b>自评 F</b>:[^<]*</p>\s*', "", text)
    text = text.replace("计算得分", "生成报告 / Copy report")
    text = re.sub(
        r"<p><b>得分总结 Score summary</b>[^<]*</p>",
        "<p><b>报告 Report</b> — 做完选择题后点按钮，把生成的文字贴到课程对话里。</p>",
        text,
    )
    text = re.sub(
        r"<p><b>得分总结</b>[^<]*</p>",
        "<p><b>报告 Report</b> — 做完选择题后点按钮，把生成的文字贴到课程对话里。</p>",
        text,
    )

    # --- pinyin JS ---
    text = re.sub(
        r"document\.getElementById\('pyAll'\)\.onclick = \(\) =>\s*document\.body\.classList\.toggle\('py-all'\);\s*",
        "",
        text,
    )
    text = re.sub(
        r"document\.addEventListener\('click', e => \{ const zh = e\.target\.closest\('\.zh'\); if \(zh(?: && !e\.target\.closest\('\.flip'\))?\) zh\.classList\.toggle\('show'\); \}\);\s*",
        "",
        text,
    )

    # --- conf JS ---
    text = re.sub(
        r"document\.addEventListener\('click', e => \{\s*if \(!e\.target\.matches\('\.conf'\)\) return;[\s\S]*?e\.target\.classList\.add\('sel'\);\s*\}\);\s*",
        "",
        text,
    )

    # --- score-btn handler ---
    text, n = re.subn(
        r"document\.addEventListener\('click', e => \{\s*if \(!e\.target\.matches\('\.score-btn'\)\) return;[\s\S]*?result\.classList\.add\('show'\);\s*\}\);",
        lambda _m: REPORT_JS.strip(),
        text,
        count=1,
    )
    if n == 0 and "matches('.score-btn')" not in text and "matches(\".score-btn\")" not in text:
        text = text.replace("</script>", REPORT_JS + "\n</script>", 1)

    text = text.replace("Click any Chinese to show its pinyin.", "Hover a dashed word to see pinyin.")
    text = text.replace("点开卡片，大声读句子", "点开卡片；虚线汉字悬停显示拼音")
    return text


def main():
    for p in FILES:
        if not p.exists():
            print("missing", p)
            continue
        src = p.read_text(encoding="utf-8")
        dst = patch(src, p)
        if dst != src:
            p.write_text(dst, encoding="utf-8")
            print("patched", p.relative_to(ROOT))
        else:
            print("unchanged", p.relative_to(ROOT))


if __name__ == "__main__":
    main()
