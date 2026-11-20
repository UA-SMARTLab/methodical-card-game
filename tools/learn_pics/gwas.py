"""Genome-wide association study: five steps' pictures and the "how many false hits" exercise."""
import html
import json

from learn_pics._kit import INK, DIM, ACC, HOT, g, person, rect, text, line, RNG_JS
from art import helix, magnifier

e = html.escape


def samples():
    # Thousands of people in the study; the first row arrives one by one, the rest stand for the many more.
    out = ""
    for r in range(3):
        for c in range(7):
            p = person(22 + c * 26, 40 + r * 34, 0.65, HOT if c < 3 else INK)
            out += g("pop", p, c) if r == 0 else p
    return out + text(48, 142, "cases", 11, HOT) + text(140, 142, "controls", 11, INK)


def test_each():
    out = g("draw", helix(14, 46, 186, 14, 5), 0)
    for k in range(9):
        x = 22 + k * 20
        out += g("pop", line([(x, 70), (x, 88)], ACC, 2) + text(x, 104, "p", 11, ACC), 1 + k)
    return out + text(100, 132, "one test per variant", 12, INK)


def manhattan():
    # A Manhattan plot: millions of tests, almost all under the dashed genome-wide line.
    out = line([(18, 130), (188, 130)], DIM, 2) + line([(18, 130), (18, 16)], DIM, 2)
    heights = [12, 20, 9, 28, 15, 18, 10, 24, 14, 92, 19, 11, 26, 16, 13, 21, 8, 30, 17, 12, 22, 14, 74, 18, 10, 25]
    for i, h in enumerate(heights):
        x = 24 + i * 6.3
        c = HOT if h > 60 else (INK if i % 2 else DIM)
        out += g("grow", rect(x, 130 - h, 3.4, h, c, "none", 0, 1), i % 8)
    out += g("pop", line([(18, 66), (188, 66)], ACC, 2, dash="5 4"), 8) + text(186, 60, "5 × 10⁻⁸", 11, ACC, "end")
    return out + text(104, 143, "position on the genome", 11, DIM)


def replicate():
    out = rect(14, 34, 76, 74, "none", INK, 2, 6) + rect(110, 34, 76, 74, "none", INK, 2, 6)
    out += text(52, 28, "discovery", 11, INK) + text(148, 28, "new sample", 11, INK)
    out += g("grow", rect(44, 52, 16, 46, HOT, "none", 0, 2), 0) + g("grow", rect(140, 58, 16, 40, HOT, "none", 0, 2), 1)
    return out + g("pop", text(100, 130, "same variant again", 12, ACC), 2)


def biology():
    out = g("draw", helix(14, 40, 186, 12, 4), 0)
    out += g("pop", rect(70, 24, 60, 32, "none", HOT, 2.5, 4) + text(100, 70, "locus", 12, HOT), 1)
    out += g("pop", magnifier(100, 106, 16, INK), 2)
    return out + g("pop", text(160, 112, "which gene?", 12, ACC) + text(160, 128, "how?", 12, ACC), 3)


PICTURES = {"samples": samples, "test_each": test_each, "manhattan": manhattan, "replicate": replicate, "biology": biology}


def exercise(ex, quote):
    """Return (html, js). Variants with no true effect give uniform p values; count how many pass each threshold."""
    counts = "".join(f'<option value="{n}"{" selected" if n == ex["counts"][1] else ""}>{n:,} variants</option>' for n in ex["counts"])
    body = f"""
  <p>{e(ex["intro"])}</p>
  <div class="controls">
    <label class="note">Variants tested <select id="gw-n">{counts}</select></label>
    <button type="button" id="gw-roll">Run again</button> <span id="gw-seed" class="note"></span>
  </div>
  <div class="arms" aria-live="polite">
    <div class="arm"><h3>Usual threshold, p &lt; 0.05</h3><p><span class="share" id="gw-loose"></span> <span class="note">false hits</span></p></div>
    <div class="arm"><h3>Genome-wide threshold, p &lt; 5 × 10⁻⁸</h3><p><span class="share" id="gw-strict"></span> <span class="note">false hits</span></p></div>
  </div>
  <p class="verdict" id="gw-verdict"></p>
  <p class="note">{e(ex["data_label"])}</p>"""
    js = RNG_JS + "const X = " + json.dumps(ex) + ";\n" + r"""
let seed = 1;
function draw() {
  const n = +$("gw-n").value, r = rng(seed * 104729 + n);
  let loose = 0, strict = 0;
  // No variant has any effect here, so every p value is uniform on (0, 1): every hit is a false one.
  for (let i = 0; i < n; i++) { const p = r(); if (p < 0.05) loose++; if (p < 5e-8) strict++; }
  $("gw-loose").textContent = loose.toLocaleString("en-GB");
  $("gw-strict").textContent = strict.toLocaleString("en-GB");
  $("gw-verdict").textContent = `None of the ${n.toLocaleString("en-GB")} variants does anything, yet p < 0.05 flags ${loose.toLocaleString("en-GB")} of them (about 1 in 20). `
    + `At 5 × 10⁻⁸ you expect ${(n * 5e-8).toPrecision(2)} false hits across the whole scan.`;
  $("gw-seed").textContent = `Run ${seed}`;
}
$("gw-roll").onclick = () => { seed++; draw(); };
$("gw-n").onchange = draw;
draw();
"""
    return body, js
