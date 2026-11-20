"""Online A/B test: the five steps' pictures and the "A/A tests and many metrics" exercise."""
import html
import json

from learn_pics._kit import INK, DIM, FAINT, HOT, TREAT, CONTROL, g, rect, text, arrow, line, circle, crowd, RNG_JS

e = html.escape


def _screen(x, y, c, label, button_y):
    return (rect(x, y, 56, 72, "none", c, 2.5, 6) + rect(x + 8, y + 10, 40, 6, FAINT, "none", 0, 2)
            + rect(x + 8, y + 22, 30, 6, FAINT, "none", 0, 2) + rect(x + 10, y + button_y, 36, 12, c, "none", 0, 6)
            + text(x + 28, y + 88, label, 12, c))


def variants():
    out = g("pop", _screen(24, 26, CONTROL, "A: current", 46), 0)
    out += g("pop", _screen(120, 26, TREAT, "B: new", 34), 1)
    out += g("pop", text(100, 72, "vs", 13, DIM), 2)
    return out


def oec():
    # Many metrics on the scorecard; one, chosen beforehand, decides.
    out = ""
    for k in range(6):
        y = 26 + k * 18
        main = k == 1
        out += g("pop", rect(30, y, 120 if main else 60 + (k * 37) % 70, 10, HOT if main else DIM, "none", 0, 3), k)
    out += g("pop", text(164, 46, "OEC", 13, HOT), 6) + text(100, 140, "agreed before the test", 11, INK)
    return out


def split():
    out = g("pop", crowd(22, 30, 4, 3, 14, 22, 0.55, lambda i, j: INK), 0)
    out += g("draw", arrow(86, 52, 120, 38, INK, 2.5), 1) + g("draw", arrow(86, 76, 120, 98, INK, 2.5), 1)
    out += g("pop", text(156, 42, "A: 50%", 13, CONTROL), 2) + g("pop", text(156, 104, "B: 50%", 13, TREAT), 3)
    out += text(100, 140, "millions of users, by hash", 11, DIM)
    return out


def check():
    out = g("grow", rect(52, 44, 36, 80, CONTROL, "none", 0, 3), 0) + g("grow", rect(112, 52, 36, 72, TREAT, "none", 0, 3), 1)
    out += line([(40, 124), (160, 124)], DIM, 2) + line([(46, 44), (154, 44)], INK, 1.5, dash="3 3")
    out += g("pop", text(100, 30, "ratio not 1.00?", 13, HOT), 2) + g("pop", text(100, 140, "find the bug first", 11, HOT), 3)
    return out


def decide():
    out = _screen(16, 30, TREAT, "B wins", 34)
    out += g("draw", arrow(80, 66, 116, 66, INK, 2.5), 0)
    out += g("pop", text(150, 58, "ship it", 14, TREAT), 1)
    out += g("pop", text(150, 82, "or drop it", 12, DIM), 2)
    out += g("pop", text(100, 22, "then the next idea", 12, INK), 3)
    return out


PICTURES = {"variants": variants, "oec": oec, "split": split, "check": check, "decide": decide}


def exercise(ex, quote):
    """Return (html, js). Seeded A/A tests: both arms identical, so every 'significant' metric is chance."""
    opts = "".join(f'<option value="{k}"{" selected" if k == ex["metrics"][0] else ""}>{k} metric{"s" if k > 1 else ""}</option>'
                   for k in ex["metrics"])
    body = f"""
  <p>{e(ex["intro"])}</p>
  <div class="controls">
    <label>Each test looks at <select id="k">{opts}</select></label>
    <button type="button" id="run">Run 100 A/A tests</button> <span id="seed" class="note"></span>
  </div>
  <div class="dots" id="dots" aria-hidden="true" style="max-width:340px"></div>
  <p class="verdict" id="verdict" aria-live="polite"></p>
  <p class="note">{e(ex["data_label"])} {e(ex["model"])}</p>"""
    js = RNG_JS + "const X = " + json.dumps(ex) + ";\n" + r"""
let seed = 1;
function test(r, k) {
  // One A/A test: both arms convert at the same rate; a metric "wins" when |z| > 1.96 (p < 0.05, two-sided).
  for (let m = 0; m < k; m++) {
    let a = 0, b = 0;
    for (let i = 0; i < X.users; i++) { if (r() < X.rate) a++; if (r() < X.rate) b++; }
    const p = (a + b) / (2 * X.users), se = Math.sqrt(2 * p * (1 - p) / X.users);
    if (se > 0 && Math.abs(a - b) / X.users / se > 1.96) return true;
  }
  return false;
}
function run() {
  const k = +$("k").value, r = rng(seed * 997 + k), hits = [];
  for (let t = 0; t < 100; t++) hits.push(test(r, k));
  const n = hits.filter(Boolean).length;
  $("dots").innerHTML = hits.map(h => `<span class="dot${h ? " sev" : ""}"></span>`).join("");
  $("verdict").textContent = `${n} of 100 identical comparisons showed at least one "significant" difference.` +
    (k === 1 ? " About 5 is what chance gives with one metric." : " With more metrics to look at, a chance 'winner' becomes likely: agree on one OEC beforehand.");
  $("seed").textContent = `Batch ${seed}`;
}
$("run").onclick = () => { seed++; run(); };
$("k").onchange = run;
run();
"""
    return body, js
