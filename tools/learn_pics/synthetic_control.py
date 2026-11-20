"""Synthetic control: the five steps' pictures and the "build the twin" exercise."""
import html
import json

from learn_pics._kit import INK, DIM, FAINT, ACC, HOT, COOL, g, rect, text, arrow, line, circle
from art import axes

e = html.escape


def donors():
    out = g("pop", circle(40, 74, 20, ACC) + text(40, 116, "treated", 12, ACC), 0)
    for k, (x, y, ok) in enumerate([(110, 40, True), (150, 40, True), (130, 76, True), (110, 112, False), (170, 100, True)]):
        out += g("pop", circle(x, y, 13, "none", COOL if ok else DIM, 2.5), k + 1)
        if not ok:
            out += g("pop", line([(100, 102), (120, 122)], HOT, 3) + line([(120, 102), (100, 122)], HOT, 3), 6)
    out += text(140, 140, "similar donors only", 11, COOL)
    return out


def weights():
    out = ""
    for k, (x, w) in enumerate([(30, .5), (70, .3), (110, .2), (150, 0)]):
        out += circle(x, 40, 12, "none", COOL, 2.5)
        out += g("grow", rect(x - 8, 120 - w * 90, 16, max(w * 90, 1), COOL, "none", 0, 2), k)
        out += text(x, 136, f"{w:.1f}", 11, INK)
    out += g("draw", arrow(160, 86, 184, 86, ACC, 3), 4) + text(172, 30, "twin", 12, ACC)
    return out


def prefit():
    out = axes(16, 18, 174, 114) + line([(120, 18), (120, 128)], DIM, 2, "4 4")
    out += g("draw", line([(24, 100), (60, 90), (90, 82), (120, 72)], ACC, 3.5), 0)
    out += g("draw", line([(24, 102), (60, 89), (90, 83), (120, 71)], COOL, 3, "6 4"), 1)
    out += g("pop", text(72, 50, "close fit before", 12, INK), 2)
    return out


def gap():
    out = axes(16, 18, 174, 114) + line([(110, 18), (110, 128)], DIM, 2, "4 4")
    for dy in (-18, 14, 26, -30):
        out += line([(24, 96 + dy * .6), (110, 70 + dy), (182, 60 + dy * 1.2)], FAINT, 2)
    out += line([(24, 96), (60, 86), (110, 70), (150, 64), (182, 58)], COOL, 3, "6 4")
    out += g("draw", line([(24, 97), (60, 85), (110, 70), (150, 86), (182, 98)], ACC, 3.5), 0)
    out += g("pop", line([(186, 60), (186, 96)], HOT, 3.5) + text(150, 120, "effect", 12, HOT), 1)
    return out


def placebo():
    out = axes(16, 18, 174, 114) + line([(110, 18), (110, 128)], DIM, 2, "4 4") + line([(18, 74), (188, 74)], DIM, 1.5)
    for k, d in enumerate((-8, 6, -4, 10, -12, 3)):
        out += g("draw", line([(24, 74 + d * .3), (110, 74 - d * .2), (182, 74 + d)], FAINT, 2), k)
    out += g("draw", line([(24, 74), (110, 75), (182, 116)], ACC, 3.5), 6)
    out += text(60, 36, "pretend each donor", 11, INK) + text(150, 136, "real one stands out", 11, ACC)
    return out


PICTURES = {"donors": donors, "weights": weights, "prefit": prefit, "gap": gap, "placebo": placebo}


def exercise(ex, quote):
    """Return (html, js). Example yearly series for one treated unit and four donors; weights by hand or by best fit."""
    sliders = "".join(
        f'<label class="note" style="display:inline-flex;gap:6px;align-items:center">{e(d["name"])} '
        f'<input type="range" min="0" max="100" value="{d["start"]}" data-w="{i}" aria-label="Weight of {e(d["name"])}"></label>'
        for i, d in enumerate(ex["donors"]))
    body = f"""
  <p>{e(ex["intro"])}</p>
  <div class="controls">{sliders}</div>
  <div class="controls">
    <button type="button" id="sc-best">Find the best fit</button>
    <button type="button" id="sc-reveal" aria-pressed="false">Show the years after</button>
  </div>
  <svg id="sc-svg" viewBox="0 0 400 240" style="width:100%;max-width:560px;height:auto" role="img" aria-label="Treated unit and its synthetic twin over time"></svg>
  <p class="verdict" id="sc-verdict" aria-live="polite"></p>
  <p class="note">{e(ex["data_label"])}</p>"""
    js = "const X = " + json.dumps(ex) + ";\nconst $ = id => document.getElementById(id);\n" + r"""
let w = X.donors.map(d => d.start), show = false;
const T = X.treated.length, k = X.start_index;
const norm = () => { const s = w.reduce((a, b) => a + b, 0) || 1; return w.map(v => v / s); };
const twin = ww => X.treated.map((_, t) => X.donors.reduce((s, d, i) => s + ww[i] * d.series[t], 0));
const rmspe = ww => { const tw = twin(ww); let s = 0; for (let t = 0; t < k; t++) s += (X.treated[t] - tw[t]) ** 2; return Math.sqrt(s / k); };
// Best fit: weights between 0 and 1 that sum to 1, searched on a 5% grid (deterministic, small enough to be instant).
function best() {
  let bw = null, be = Infinity; const n = X.donors.length, step = 5;
  (function rec(i, left, acc) {
    if (i === n - 1) { const ww = acc.concat(left).map(v => v / 100), er = rmspe(ww); if (er < be) { be = er; bw = ww; } return; }
    for (let v = 0; v <= left; v += step) rec(i + 1, left - v, acc.concat(v));
  })(0, 100, []);
  return bw;
}
function draw() {
  const ww = norm(), tw = twin(ww), all = X.treated.concat(tw, ...X.donors.map(d => d.series));
  const lo = Math.min(...all) - 2, hi = Math.max(...all) + 2, last = show ? T - 1 : k - 1;
  const sx = t => 44 + t * (340 / (T - 1)), sy = v => 210 - (v - lo) / (hi - lo) * 195;
  const pl = (a, attrs) => `<polyline fill="none" ${attrs} points="${a.slice(0, last + 1).map((v, t) => sx(t) + "," + sy(v)).join(" ")}"/>`;
  let s = `<line x1="${sx(k - 0.5)}" y1="8" x2="${sx(k - 0.5)}" y2="212" stroke="currentColor" stroke-dasharray="4 4" opacity=".5"/>`;
  s += `<text x="${sx(k - 0.5) + 4}" y="20" font-size="12" fill="currentColor">programme</text>`;
  X.donors.forEach(d => s += pl(d.series, `stroke="currentColor" stroke-width="1.5" opacity=".25"`));
  s += pl(tw, `stroke="#0369A1" stroke-width="3" stroke-dasharray="6 4"`) + pl(X.treated, `stroke="#B45309" stroke-width="3.5"`);
  $("sc-svg").innerHTML = s;
  const pre = rmspe(ww), gapNow = X.treated[T - 1] - tw[T - 1];
  $("sc-verdict").textContent = `Weights: ${X.donors.map((d, i) => d.name + " " + Math.round(100 * ww[i]) + "%").join(", ")}. Fit before the programme (RMSPE): ${pre.toFixed(2)}.`
    + (show ? ` Gap in the last year: ${gapNow.toFixed(1)}. Trust it only if the fit before was close.` : " Get the fit close, then show the years after.");
  $("sc-reveal").setAttribute("aria-pressed", show);
}
document.querySelectorAll("[data-w]").forEach(el => el.oninput = () => { w[+el.dataset.w] = +el.value; draw(); });
$("sc-best").onclick = () => { w = best().map(v => Math.round(v * 100)); document.querySelectorAll("[data-w]").forEach(el => el.value = w[+el.dataset.w]); draw(); };
$("sc-reveal").onclick = () => { show = !show; draw(); };
draw();
"""
    return body, js
