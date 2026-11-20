"""Regression discontinuity: the six steps' pictures and the "how wide a window" exercise."""
import html
import json

from learn_pics._kit import INK, DIM, ACC, HOT, COOL, TREAT, CONTROL, g, person, rect, text, arrow, line, circle, RNG_JS
from art import axes, scatter, lcg

e = html.escape


def rule():
    out = line([(16, 100), (184, 100)], INK, 3)
    for k in range(9):
        x = 24 + k * 19
        out += line([(x, 95), (x, 105)], DIM, 2)
    out += g("pop", line([(110, 70), (110, 120)], ACC, 3.5) + text(110, 64, "10% risk", 12, ACC), 0)
    out += g("pop", text(62, 130, "no statin", 12, CONTROL), 1) + g("pop", text(152, 130, "statin", 12, TREAT), 2)
    out += text(100, 30, "the rule decides", 12, INK)
    return out


def jump():
    out = axes(16, 16, 172, 112) + line([(104, 20), (104, 128)], ACC, 2.5, "6 5")
    out += g("draw", line([(24, 118), (100, 112)], CONTROL, 3.5), 0)
    out += g("draw", line([(108, 40), (184, 34)], TREAT, 3.5), 1)
    out += g("pop", arrow(112, 108, 112, 46, HOT, 2.5, head=6), 2)
    out += text(56, 100, "share treated", 11, DIM)
    return out


def no_cheat():
    # Scores piling up just past the line would mean people moved themselves across.
    out = line([(16, 120), (184, 120)], DIM, 2) + line([(104, 30), (104, 124)], ACC, 2.5, "6 5")
    hs = [20, 24, 27, 30, 31, 33, 34, 33, 32, 30, 28, 25, 22, 19]
    for k, h in enumerate(hs):
        x = 22 + k * 11.5
        out += g("grow", rect(x, 120 - h * 2, 9, h * 2, DIM if x < 104 else INK, "none", 0, 1), k)
    out += g("pop", text(100, 22, "smooth across?", 12, INK), 14)
    return out


def window():
    r = lcg(3)
    pts = [(22 + k * 5, 70 + (r() - .5) * 60) for k in range(33)]
    out = scatter(pts, 2.3, DIM)
    out += g("pop", rect(80, 30, 48, 84, "#FCD34D22", ACC, 2.5, 4), 0)
    for k, (x, y) in enumerate([(92, 56), (92, 88), (116, 56), (116, 88)]):
        out += g("pop", person(x, y, 0.7, CONTROL if x < 104 else TREAT), 1 + k)
    out += text(104, 132, "alike near the line", 11, ACC)
    return out


def fit():
    r = lcg(9)
    out = axes(16, 16, 172, 116) + line([(104, 30), (104, 130)], ACC, 2.5, "6 5")
    pts = []
    for k in range(34):
        x = 24 + k * 4.8
        pts.append((x, 112 - (x - 24) * 0.32 - (26 if x > 104 else 0) + (r() - .5) * 18))
    out += scatter(pts, 2.4, DIM)
    out += g("draw", line([(24, 112), (104, 86.4)], CONTROL, 3.5), 0) + g("draw", line([(104, 60.4), (184, 34.8)], TREAT, 3.5), 1)
    out += text(60, 26, "a line each side", 11, INK)
    return out


def read_jump():
    out = axes(16, 16, 172, 116) + line([(104, 30), (104, 130)], ACC, 2.5, "6 5")
    out += line([(24, 112), (104, 86.4)], CONTROL, 3.5) + line([(104, 60.4), (184, 34.8)], TREAT, 3.5)
    out += g("pop", line([(110, 86), (110, 61)], HOT, 4), 0) + g("pop", text(150, 84, "effect here", 12, HOT), 1)
    out += g("fade", text(56, 40, "not far away", 11, DIM), 2)
    return out


PICTURES = {"rule": rule, "jump": jump, "no_cheat": no_cheat, "window": window, "fit": fit, "read_jump": read_jump}


def exercise(ex, quote):
    """Return (html, js). Example patients scored 0–20%; statins from 10%. Naive comparison vs a local fit in a window."""
    wins = "".join(f'<option value="{w}"{" selected" if w == ex["windows"][1] else ""}>±{w} points</option>' for w in ex["windows"])
    body = f"""
  <p>{e(ex["intro"])}</p>
  <div class="controls" role="group" aria-label="Which comparison">
    <button type="button" data-rd="naive">Everyone treated vs everyone not</button>
    <button type="button" data-rd="local">A line each side, near the cutoff</button>
    <label class="note">Window <select id="rd-win">{wins}</select></label>
  </div>
  <svg id="rd-svg" viewBox="0 0 400 240" style="width:100%;max-width:560px;height:auto" role="img" aria-label="Outcome by risk score, with the cutoff"></svg>
  <p class="verdict" id="rd-verdict" aria-live="polite"></p>
  <p class="note">{e(ex["data_label"])}</p>"""
    js = RNG_JS + "const X = " + json.dumps(ex) + ";\n" + r"""
let mode = "naive", w = X.windows[1];
const r = rng(X.seed), c = X.cutoff;
// Outcome rises with risk score (sicker people), and statins lower it by X.effect for those at or above the cutoff.
const P = Array.from({ length: X.n }, () => {
  const x = r() * 20, t = x >= c;
  return [x, t, X.base + X.slope * x + X.curve * (x - 10) ** 2 + (t ? X.effect : 0) + (r() - 0.5) * X.noise];
});
function ols(pts) {
  const n = pts.length, mx = pts.reduce((s, p) => s + p[0], 0) / n, my = pts.reduce((s, p) => s + p[1], 0) / n;
  let sxy = 0, sxx = 0; for (const [x, y] of pts) { sxy += (x - mx) * (y - my); sxx += (x - mx) ** 2; }
  const b = sxy / sxx; return [my - b * mx, b];
}
const mean = a => a.reduce((s, v) => s + v, 0) / a.length;
function draw() {
  const ys = P.map(p => p[2]), lo = Math.min(...ys) - 0.2, hi = Math.max(...ys) + 0.2;
  const sx = x => 40 + x / 20 * 345, sy = y => 210 - (y - lo) / (hi - lo) * 195;
  let s = `<line x1="${sx(c)}" y1="8" x2="${sx(c)}" y2="215" stroke="#B45309" stroke-dasharray="6 5"/>`;
  s += `<text x="${sx(c) + 4}" y="20" font-size="12" fill="#B45309">cutoff ${c}%</text>`;
  s += `<text x="212" y="236" font-size="12" text-anchor="middle" fill="currentColor">risk score (%)</text>`;
  if (mode === "local") s += `<rect x="${sx(c - w)}" y="8" width="${sx(c + w) - sx(c - w)}" height="207" fill="#FCD34D" opacity=".15"/>`;
  for (const [x, t, y] of P) s += `<circle cx="${sx(x)}" cy="${sy(y)}" r="2.6" fill="${t ? "#B45309" : "#0369A1"}" opacity=".55"/>`;
  let msg;
  if (mode === "naive") {
    const d = mean(P.filter(p => p[1]).map(p => p[2])) - mean(P.filter(p => !p[1]).map(p => p[2]));
    msg = `Treated minus untreated, everyone: ${d.toFixed(2)}. The treated were sicker to begin with, so this mixes the drug with risk.`;
  } else {
    const L = P.filter(p => !p[1] && p[0] >= c - w).map(p => [p[0] - c, p[2]]), R = P.filter(p => p[1] && p[0] <= c + w).map(p => [p[0] - c, p[2]]);
    const [a0, b0] = ols(L), [a1, b1] = ols(R);
    s += `<line x1="${sx(c - w)}" y1="${sy(a0 - b0 * w)}" x2="${sx(c)}" y2="${sy(a0)}" stroke="#0369A1" stroke-width="3.5"/>`;
    s += `<line x1="${sx(c)}" y1="${sy(a1)}" x2="${sx(c + w)}" y2="${sy(a1 + b1 * w)}" stroke="#B45309" stroke-width="3.5"/>`;
    msg = `Jump at the cutoff, using ${L.length + R.length} patients within ±${w} points: ${(a1 - a0).toFixed(2)}. A narrow window is less biased by the curve but noisier.`;
  }
  $("rd-svg").innerHTML = s;
  $("rd-verdict").textContent = msg + ` The true effect built into these data is ${X.effect}.`;
  document.querySelectorAll("[data-rd]").forEach(b => b.setAttribute("aria-pressed", b.dataset.rd === mode));
}
document.querySelectorAll("[data-rd]").forEach(b => b.onclick = () => { mode = b.dataset.rd; draw(); });
$("rd-win").onchange = ev => { w = +ev.target.value; draw(); };
draw();
"""
    return body, js
