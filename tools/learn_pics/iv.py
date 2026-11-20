"""Instrumental variable analysis: five steps' pictures and the "naive versus instrument" exercise."""
import html
import json

from learn_pics._kit import INK, DIM, ACC, HOT, g, rect, text, arrow, line, dice, RNG_JS
from art import node, cross, path

e = html.escape


def _zxy(z_glow=False):
    out = node(40, 100, "Z", 15, "none", ACC if z_glow else INK) + node(100, 100, "X", 15) + node(164, 100, "Y", 15)
    out += node(132, 34, "U", 14, "none", DIM)
    out += arrow(122, 45, 106, 84, DIM, 2, "5 4") + arrow(142, 45, 158, 84, DIM, 2, "5 4")
    return out


def instrument():
    out = g("roll", dice(40, 52, 30, 3, ACC)) + _zxy(True)
    out += arrow(56, 100, 83, 100, INK, 2.5) + arrow(117, 100, 147, 100, INK, 2.5)
    return out + text(132, 140, "U: unmeasured", 11, DIM)


def relevance():
    out = _zxy(True) + arrow(117, 100, 147, 100, DIM, 2)
    out += g("draw", arrow(56, 100, 83, 100, ACC, 4), 0)
    return out + g("pop", text(70, 136, "Z moves X", 13, ACC), 1)


def exclusion():
    out = _zxy(True) + arrow(56, 100, 83, 100, INK, 2.5) + arrow(117, 100, 147, 100, INK, 2.5)
    out += g("draw", path("M48,114 Q100,150 152,114", HOT, 2, dash="3 4"), 0) + g("pop", cross(100, 132, 7), 1)
    return out + g("pop", text(100, 24, "no Z → Y shortcut", 12, HOT), 2)


def exchangeable():
    out = _zxy(True) + arrow(56, 100, 83, 100, INK, 2.5) + arrow(117, 100, 147, 100, INK, 2.5)
    out += g("draw", line([(52, 88), (120, 40)], HOT, 2, dash="3 4"), 0) + g("pop", cross(86, 64, 7), 1)
    return out + g("pop", text(40, 30, "no Z ← U link", 12, HOT, "start"), 2)


def ratio():
    out = g("pop", text(100, 40, "effect of Z on Y", 14, INK), 0) + g("draw", line([(30, 56), (170, 56)], INK, 2.5), 1)
    out += g("pop", text(100, 80, "effect of Z on X", 14, ACC), 2)
    return out + g("pop", text(100, 118, "= effect of X on Y", 14, HOT), 3)


PICTURES = {"instrument": instrument, "relevance": relevance, "exclusion": exclusion, "exchangeable": exchangeable, "ratio": ratio}


def exercise(ex, quote):
    """Return (html, js). Simulated people with a hidden confounder U; compare the naive estimate with the Wald ratio."""
    sizes = "".join(f'<option value="{s}"{" selected" if s == ex["sizes"][1] else ""}>{s} people</option>' for s in ex["sizes"])
    body = f"""
  <p>{e(ex["intro"])}</p>
  <div class="controls">
    <label class="note">Instrument <select id="iv-str"><option value="strong" selected>strong (nudges many)</option><option value="weak">weak (nudges few)</option></select></label>
    <label class="note">Study size <select id="iv-n">{sizes}</select></label>
    <button type="button" id="iv-roll">Draw again</button> <span id="iv-seed" class="note"></span>
  </div>
  <table style="border-collapse:collapse;margin:8px 0" aria-live="polite">
    <tr><th style="text-align:left;padding:4px 10px 4px 0">True effect of X on Y (set by us)</th><td id="iv-true"></td></tr>
    <tr><th style="text-align:left;padding:4px 10px 4px 0">Naive: Y in exposed minus unexposed</th><td id="iv-naive"></td></tr>
    <tr><th style="text-align:left;padding:4px 10px 4px 0">Z on Y (numerator)</th><td id="iv-num"></td></tr>
    <tr><th style="text-align:left;padding:4px 10px 4px 0">Z on X (denominator)</th><td id="iv-den"></td></tr>
    <tr><th style="text-align:left;padding:4px 10px 4px 0">Instrument estimate (ratio)</th><td id="iv-wald"></td></tr>
  </table>
  <p class="verdict" id="iv-verdict"></p>
  <p class="note">{e(ex["data_label"])} {e(ex["model"])}</p>"""
    js = RNG_JS + "const X = " + json.dumps(ex) + ";\n" + r"""
let seed = 1;
const f = v => (Math.round(v * 100) / 100).toFixed(2);
function simulate() {
  const r = rng(seed * 7919 + (+$("iv-n").value)), n = +$("iv-n").value, nudge = X.nudge[$("iv-str").value];
  const gauss = () => { let s = 0; for (let k = 0; k < 6; k++) s += r(); return (s - 3) / Math.SQRT1_2; };
  let s = { y1: 0, n1: 0, y0: 0, n0: 0, yz1: 0, xz1: 0, nz1: 0, yz0: 0, xz0: 0, nz0: 0 };
  for (let i = 0; i < n; i++) {
    const u = gauss(), z = r() < 0.5 ? 1 : 0;
    // Healthier people (high U) take the exposure more often and also do better: confounding the naive comparison.
    const x = (X.u_on_x * u + nudge * z + gauss() > X.threshold) ? 1 : 0;
    const y = X.effect * x + X.u_on_y * u + gauss();
    if (x) { s.y1 += y; s.n1++; } else { s.y0 += y; s.n0++; }
    if (z) { s.yz1 += y; s.xz1 += x; s.nz1++; } else { s.yz0 += y; s.xz0 += x; s.nz0++; }
  }
  return s;
}
function draw() {
  const s = simulate();
  const naive = s.y1 / s.n1 - s.y0 / s.n0, num = s.yz1 / s.nz1 - s.yz0 / s.nz0, den = s.xz1 / s.nz1 - s.xz0 / s.nz0;
  const wald = num / den;
  $("iv-true").textContent = f(X.effect);
  $("iv-naive").textContent = f(naive);
  $("iv-num").textContent = f(num);
  $("iv-den").textContent = f(den) + ` (Z raises the share exposed by ${Math.round(100 * den)} points)`;
  $("iv-wald").textContent = f(wald);
  $("iv-verdict").textContent = `The naive comparison is off by ${f(Math.abs(naive - X.effect))}, because U drives both X and Y. `
    + `The instrument estimate is off by ${f(Math.abs(wald - X.effect))}. `
    + ($("iv-str").value === "weak" ? "With a weak instrument the denominator is small, so the ratio jumps around from draw to draw: draw again and see." : "Draw again: it varies around the true value.");
  $("iv-seed").textContent = `Draw ${seed}`;
}
$("iv-roll").onclick = () => { seed++; draw(); };
$("iv-str").onchange = draw; $("iv-n").onchange = draw;
draw();
"""
    return body, js

