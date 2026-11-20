"""Stepped-wedge trial: the five steps' pictures and the "time hides in the comparison" exercise."""
import html
import json

from learn_pics._kit import INK, DIM, HOT, TREAT, CONTROL, g, rect, text, arrow, line, dice, RNG_JS

e = html.escape
ROWS, COLS = 4, 5  # four groups of clusters, five measurement periods (the shape of Hemming et al.'s fig 1)
X0, Y0, W, H = 44, 34, 28, 22


def _grid(upto_col=COLS, i0=0, anim=True):
    """Row r switches at period r + 1: control (blue) before, intervention (amber) from then on."""
    out = ""
    for r in range(ROWS):
        out += text(X0 - 10, Y0 + r * H + 15, f"G{r + 1}", 11, DIM, anchor="end")
        for c in range(upto_col):
            col = TREAT if c > r else CONTROL
            cell = rect(X0 + c * W, Y0 + r * H, W - 3, H - 3, col, "none", 0, 3)
            out += g("pop", cell, i0 + c) if anim else cell
    return out


def start():
    out = ""
    for r in range(ROWS):
        out += text(X0 - 10, Y0 + r * H + 15, f"G{r + 1}", 11, DIM, anchor="end")
        out += g("pop", rect(X0, Y0 + r * H, W - 3, H - 3, CONTROL, "none", 0, 3), r)
        for c in range(1, COLS):
            out += rect(X0 + c * W, Y0 + r * H, W - 3, H - 3, "none", DIM, 1, 3, dash="2 3")
    out += g("pop", text(100, 22, "everyone starts as control", 12, INK), 4)
    out += text(100, 140, "period 1", 11, CONTROL)
    return out


def order():
    out = g("roll", dice(22, 24, 18, 6))
    # Chance decides which group steps first; each group's whole row of cells arrives in the drawn order.
    for r in range(ROWS):
        out += text(X0 - 10, Y0 + r * H + 15, f"G{r + 1}", 11, DIM, anchor="end")
        out += g("draw", "".join(rect(X0 + c * W, Y0 + r * H, W - 3, H - 3, TREAT if c > r else CONTROL, "none", 0, 3)
                                 for c in range(COLS)), r + 1)
    out += text(110, 140, "order of switching: by chance", 11, INK)
    return out


def step():
    out = _grid(COLS, 0)
    # The wedge: one staircase line where each group crosses over.
    pts = [(X0 + W, Y0 - 2)]
    for r in range(ROWS):
        x = X0 + (r + 1) * W - 1.5
        pts += [(x, Y0 + r * H - 2), (x, Y0 + (r + 1) * H - 2)]
    out += g("draw", line(pts, HOT, 2.5), 6)
    out += g("pop", text(100, 140, "one step per period", 11, HOT), 7)
    return out


def measure():
    out = _grid(COLS, 0, anim=False)
    for c in range(COLS):
        for r in range(ROWS):
            out += g("pop", f'<circle cx="{X0 + c * W + 12.5}" cy="{Y0 + r * H + 9.5}" r="3" fill="#0f172a"/>', c)
    out += text(100, 22, "measure every cell", 12, INK)
    out += g("draw", arrow(X0, 136, X0 + COLS * W - 3, 136, DIM, 2, head=6), 5)
    out += text(186, 140, "time", 11, DIM, anchor="end")
    return out


def adjust():
    out = _grid(COLS, 0, anim=False)
    # Compare inside each period (column), never early blue against late amber.
    for c in range(1, ROWS):
        out += g("pop", rect(X0 + c * W - 2, Y0 - 3, W + 1, ROWS * H + 3, "none", HOT, 2, 4), c)
    out += g("pop", text(100, 22, "compare within periods", 12, HOT), 5)
    out += text(100, 140, "time is adjusted for", 11, INK)
    return out


PICTURES = {"start": start, "order": order, "step": step, "measure": measure, "adjust": adjust}


def exercise(ex, quote):
    """Return (html, js). Example clusters improve over time anyway; compare the naive and the period-by-period estimate."""
    body = f"""
  <p>{e(ex["intro"])}</p>
  <div class="controls">
    <label>Things get better anyway, per period: <input type="range" id="trend" min="0" max="6" step="1" value="{ex["trend_start"]}"> <output id="trend-o"></output> points</label>
    <button type="button" id="roll">New sample</button> <span id="seed" class="note"></span>
  </div>
  <div id="grid" aria-hidden="true"></div>
  <table aria-live="polite"><thead><tr><th>Estimate</th><th>Points</th></tr></thead><tbody>
    <tr><td>True effect of the intervention</td><td>{ex["true_effect"]}</td></tr>
    <tr><td>All intervention cells minus all control cells</td><td><output id="naive"></output></td></tr>
    <tr><td>Within each period, then averaged</td><td><output id="within"></output></td></tr>
  </tbody></table>
  <p class="verdict" id="verdict"></p>
  <p class="note">{e(ex["data_label"])} {e(ex["model"])}</p>"""
    js = RNG_JS + "const X = " + json.dumps(ex) + ";\n" + r"""
let seed = 1;
function cells(trend) {
  // Group g (0..3) switches at period g+1; outcome = base + trend*period + effect if switched + seeded noise.
  const r = rng(seed), out = [];
  for (let g = 0; g < 4; g++) for (let p = 0; p < 5; p++) {
    const on = p > g, noise = (r() + r() + r() - 1.5) * X.noise;
    out.push({ g, p, on, y: X.base + trend * p + (on ? X.true_effect : 0) + noise });
  }
  return out;
}
const mean = a => a.reduce((s, v) => s + v, 0) / a.length;
function draw() {
  const trend = +$("trend").value, cs = cells(trend);
  $("trend-o").textContent = trend;
  const naive = mean(cs.filter(c => c.on).map(c => c.y)) - mean(cs.filter(c => !c.on).map(c => c.y));
  const per = [];
  for (let p = 1; p < 4; p++) {
    const a = cs.filter(c => c.p === p && c.on).map(c => c.y), b = cs.filter(c => c.p === p && !c.on).map(c => c.y);
    per.push(mean(a) - mean(b));
  }
  const within = mean(per);
  $("naive").textContent = naive.toFixed(1);
  $("within").textContent = within.toFixed(1);
  $("grid").innerHTML = '<table><tr><th></th>' + [1, 2, 3, 4, 5].map(p => `<th>Period ${p}</th>`).join("") + '</tr>' +
    [0, 1, 2, 3].map(g => `<tr><th>Group ${g + 1}</th>` + cs.filter(c => c.g === g).map(c =>
      `<td style="background:${c.on ? "#FCD34D55" : "#7DD3FC55"}">${c.y.toFixed(0)}</td>`).join("") + '</tr>').join("") + '</table>';
  $("verdict").textContent = trend === 0
    ? "With no trend, both estimates land near the true effect (apart from noise)."
    : `The naive estimate is off by ${(naive - X.true_effect).toFixed(1)} points: intervention cells are later, and later is better anyway. Comparing within periods removes most of that.`;
  $("seed").textContent = `Sample ${seed}`;
}
$("trend").oninput = draw;
$("roll").onclick = () => { seed++; draw(); };
draw();
"""
    return body, js
