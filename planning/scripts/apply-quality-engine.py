"""Inject tile-shuffle, gendered TTS, and P2 data-order scoring into listed worksheets."""
from __future__ import annotations
import re
from pathlib import Path

ROOT = Path(r"Z:\Chinese")
FILES = [
    ROOT / "planning" / "templates" / "example-worksheet-hsk3-ba.html",
    ROOT / "courses" / "hsk4" / "vt" / "hsk4-vt-02.html",
    ROOT / "courses" / "hsk4" / "p" / "hsk4-ws-004.html",
    ROOT / "courses" / "hsk4" / "p" / "hsk4-ws-005.html",
    ROOT / "courses" / "hsk4" / "gt" / "hsk4-gt-CL02b.html",
]

SHUFFLE_JS = r"""
function shuffleTiles(row) {
  if (!row) return;
  const tiles = [...row.children];
  for (let i = tiles.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [tiles[i], tiles[j]] = [tiles[j], tiles[i]];
  }
  tiles.forEach(t => row.appendChild(t));
}
function shuffleAllTiles() {
  document.querySelectorAll('.tiles').forEach(shuffleTiles);
}
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', shuffleAllTiles);
} else {
  shuffleAllTiles();
}
"""

TTS_JS = r"""
function lineGender(el) {
  const line = el.closest('.line') || el.parentElement;
  const g = ((line && line.dataset.gender) || '').toLowerCase();
  if (g === 'm' || g === 'male') return 'm';
  if (g === 'f' || g === 'female') return 'f';
  const sp = line && line.querySelector('.speaker');
  const t = sp ? sp.textContent : '';
  if (/男/.test(t)) return 'm';
  if (/女/.test(t)) return 'f';
  return 'f';
}
function pickZhVoice(gender) {
  const voices = speechSynthesis.getVoices().filter(v =>
    /zh(-|_|$)/i.test(v.lang) || /chinese|中文/i.test(v.name));
  const re = gender === 'm'
    ? /kangkang|yunyang|yunjian|yunxi|yunhao|male|男/i
    : /huihui|yaoyao|xiaoxiao|xiaoyi|xiaoxuan|female|女/i;
  const named = voices.find(v => re.test(v.name));
  if (named) return { voice: named, pitch: 1 };
  const zh = voices.find(v => /zh-CN/i.test(v.lang)) || voices[0] || null;
  return { voice: zh, pitch: gender === 'm' ? 0.85 : 1.15 };
}
function whenVoices(cb) {
  if (speechSynthesis.getVoices().length) { cb(); return; }
  let ran = false;
  const go = () => { if (ran) return; ran = true; cb(); };
  speechSynthesis.addEventListener('voiceschanged', go, { once: true });
  setTimeout(go, 500);
}
document.addEventListener('click', e => {
  if (!e.target.matches('.tts')) return;
  if (!('speechSynthesis' in window)) return;
  const line = e.target.closest('.line') || e.target.parentElement;
  const clone = line.cloneNode(true);
  clone.querySelectorAll('button').forEach(b => b.remove());
  const sp = clone.querySelector('.speaker');
  if (sp) sp.remove();
  const gender = lineGender(e.target);
  const text = clone.textContent.trim();
  whenVoices(() => {
    const { voice, pitch } = pickZhVoice(gender);
    const u = new SpeechSynthesisUtterance(text);
    u.lang = 'zh-CN';
    if (voice) u.voice = voice;
    u.pitch = pitch;
    speechSynthesis.cancel();
    speechSynthesis.speak(u);
  });
});
"""

P2_SCORE_JS = r"""
  document.querySelectorAll('.item[data-order]').forEach(it => {
    total++;
    const want = it.dataset.order.split('|');
    const got = [...it.querySelectorAll('.built > .tile')].map(t => t.textContent);
    const ok = want.length === got.length && want.every((w, i) => got[i] === w);
    if (ok) { right++; return; }
    const w = it.dataset.point || it.dataset.word || tag(it);
    if (w && !seen.has(w)) { seen.add(w); missed.push(String(w).trim()); }
  });
"""

TILE_HANDLERS = r"""
document.addEventListener('click', e => {
  if (!e.target.matches('.tiles > .tile')) return;
  const built = e.target.closest('.item').querySelector('.built');
  if (!built) return;
  const t = document.createElement('button');
  t.className = 'tile'; t.textContent = e.target.textContent;
  built.appendChild(t); e.target.classList.add('used');
});
document.addEventListener('click', e => {
  if (e.target.matches('.built > .tile')) e.target.remove();
});
document.addEventListener('click', e => {
  if (!e.target.matches('.reset')) return;
  const item = e.target.closest('.item');
  item.querySelectorAll('.tiles > .tile.used').forEach(t => t.classList.remove('used'));
  const built = item.querySelector('.built'); if (built) built.innerHTML = '';
  shuffleTiles(item.querySelector('.tiles'));
  if (item.querySelector('.bank')) {
    item.querySelectorAll('.bank .bword').forEach(b => { b.classList.remove('used'); b.style.outline = ''; });
    item.querySelectorAll('.slot').forEach(s => { s.textContent = ''; delete s.dataset.filled; });
    armedWord = null;
  }
});
"""

DLG_CSS = """  .dlg { margin:8px 0; }
  .dlg .line { display:flex; gap:10px; align-items:flex-start; padding:6px 0; }
  .dlg .speaker { flex:0 0 64px; font-weight:700; color:var(--accent); }
  .tts { border:none; background:none; font-size:1rem; padding:0 4px; }
"""


def patch(text: str) -> str:
    if "function shuffleTiles" not in text:
        text = text.replace("<script>", "<script>\n" + SHUFFLE_JS, 1)

    if "const built = item.querySelector('.built'); if (built) built.innerHTML = '';" in text \
            and "shuffleTiles(item.querySelector('.tiles'))" not in text:
        text = text.replace(
            "const built = item.querySelector('.built'); if (built) built.innerHTML = '';",
            "const built = item.querySelector('.built'); if (built) built.innerHTML = '';\n"
            "  shuffleTiles(item.querySelector('.tiles'));",
            1,
        )

    if ".tiles > .tile" not in text:
        # Insert tile handlers before paste-report / score-btn
        if "if (e.target.matches('.copy-report'))" in text:
            text = text.replace(
                "document.addEventListener('click', e => {\n  if (e.target.matches('.copy-report'))",
                TILE_HANDLERS + "\ndocument.addEventListener('click', e => {\n  if (e.target.matches('.copy-report'))",
                1,
            )

    tts_pat = re.compile(
        r"document\.addEventListener\('click', e => \{\s*"
        r"if \(!e\.target\.matches\('\.tts'\)\) return;[\s\S]*?speechSynthesis\.speak\(u\);\s*\}\);",
        re.M,
    )
    if tts_pat.search(text):
        text = tts_pat.sub(TTS_JS.strip(), text, count=1)
    elif "function lineGender" not in text:
        if "if (e.target.matches('.copy-report'))" in text:
            text = text.replace(
                "document.addEventListener('click', e => {\n  if (e.target.matches('.copy-report'))",
                TTS_JS + "\ndocument.addEventListener('click', e => {\n  if (e.target.matches('.copy-report'))",
                1,
            )
        else:
            text = text.replace("</script>", TTS_JS + "\n</script>", 1)

    if ".item[data-order]" not in text:
        text = text.replace(
            "    if (!seen.has(w)) { seen.add(w); missed.push(w); }\n  });\n  const pct =",
            "    if (!seen.has(w)) { seen.add(w); missed.push(w); }\n  });"
            + P2_SCORE_JS
            + "  const pct =",
            1,
        )

    if ".dlg .line" not in text and ".tts {" not in text:
        text = text.replace("</style>", DLG_CSS + "</style>", 1)

    return text


def main() -> None:
    for p in FILES:
        src = p.read_text(encoding="utf-8")
        dst = patch(src)
        if dst != src:
            p.write_text(dst, encoding="utf-8")
            print("patched", p.relative_to(ROOT))
        else:
            print("unchanged", p.relative_to(ROOT))


if __name__ == "__main__":
    main()
