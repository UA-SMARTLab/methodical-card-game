"""Diagnostic accuracy study: the five steps' pictures and the "move the cut-off" exercise."""
import html
import json

from learn_pics._kit import INK, DIM, ACC, HOT, COOL, g, person, rect, text, arrow, line, circle, RNG_JS
from art import eye, check, cross

e = html.escape


def recruit():
    # A queue of suspected patients walks in one by one; healthy volunteers stand aside, not recruited.
    out = text(100, 22, "suspected, in order", 12, INK)
    for k in range(6):
        out += g("pop", person(30 + k * 26, 70, 0.8, INK), k)
    out += g("draw", arrow(20, 98, 186, 98, DIM, 2), 6)
    out += "".join(g("fade", person(x, 128, 0.6, COOL), 7 + i) for i, x in enumerate((150, 168, 186)))
    out += text(84, 136, "not healthy volunteers", 11, DIM)
    return out


def index():
    out = rect(30, 40, 50, 70, "none", INK, 2.5, 6) + text(55, 30, "NEW TEST", 12, INK)
    out += g("grow", rect(44, 66, 22, 38, ACC, "none", 0, 3), 0)
    out += g("draw", line([(24, 78), (88, 78)], HOT, 2.5, dash="5 3"), 1) + g("pop", text(130, 82, "cut-off", 13, HOT), 2)
    out += g("pop", text(130, 52, "above: positive", 11, ACC), 3) + g("pop", text(130, 112, "below: negative", 11, DIM), 4)
    out += text(100, 138, "fixed in advance", 11, INK)
    return out


def reference():
    out = ""
    for k in range(5):
        out += person(28 + k * 22, 62, 0.75, INK)
    out += g("draw", arrow(28, 86, 120, 86, DIM, 2), 0)
    out += g("pop", rect(132, 40, 52, 56, "none", ACC, 3, 6) + text(158, 74, "BEST", 14, ACC), 1)
    out += g("pop", text(158, 114, "reference", 12, ACC), 2)
    out += g("pop", check(40, 122) + cross(62, 122) + check(84, 122) + cross(106, 122), 3)
    out += text(72, 144, "everyone", 11, INK)
    return out


def blind():
    out = rect(18, 42, 62, 48, "none", INK, 2.5, 6) + text(49, 34, "index", 12, INK)
    out += rect(120, 42, 62, 48, "none", ACC, 2.5, 6) + text(151, 34, "reference", 12, ACC)
    out += eye(49, 66, 1.0, INK) + eye(151, 66, 1.0, ACC)
    out += g("pop", rect(94, 30, 12, 76, DIM, "none", 0, 2), 1)
    out += g("pop", text(100, 126, "neither sees the other", 12, HOT), 2)
    return out


def table():
    x0, y0, w, h = 54, 34, 64, 46
    out = text(86, 26, "condition  /  none", 11, DIM) + text(30, 62, "test +", 11, INK) + text(30, 108, "test −", 11, INK)
    cells = [("TP", 0, 0, ACC), ("FP", 1, 0, HOT), ("FN", 0, 1, HOT), ("TN", 1, 1, COOL)]
    for i, (lab, cx, cy, c) in enumerate(cells):
        out += g("pop", rect(x0 + cx * w, y0 + cy * h, w - 4, h - 4, "none", c, 2.5, 4)
                 + text(x0 + cx * w + (w - 4) / 2, y0 + cy * h + 28, lab, 16, c), i)
    out += g("pop", text(86, 140, "sensitivity", 11, ACC), 4) + g("pop", text(150, 140, "specificity", 11, COOL), 5)
    return out


PICTURES = {"recruit": recruit, "index": index, "reference": reference, "blind": blind, "table": table}


def exercise(ex, quote):
    """Return (html, js). Example test values; a cut-off slider fills the 2 x 2 table; two kinds of 'without' group."""
    body = f"""
  <p>{e(ex["intro"])}</p>
  <div class="controls" role="group" aria-label="People without the condition">
    <button type="button" data-grp="clinic">Clinic patients</button>
    <button type="button" data-grp="healthy">Healthy volunteers</button>
  </div>
  <label class="note" style="display:block">Cut-off <output id="cutv"></output><br>
    <input type="range" id="cut" min="20" max="90" step="1" value="{ex["cut"]}" style="width:100%;max-width:420px"></label>
  <svg id="hist" viewBox="0 0 420 120" style="width:100%;max-width:520px;display:block" role="img" aria-label="Test values of both groups and the cut-off"></svg>
  <table style="border-collapse:collapse;margin:10px 0;font-variant-numeric:tabular-nums" aria-live="polite">
    <tr><th></th><th style="padding:4px 10px">Has the condition</th><th style="padding:4px 10px">Does not</th></tr>
    <tr><th style="padding:4px 10px;text-align:left">Test positive</th><td id="tp" style="padding:4px 10px;text-align:center"></td><td id="fp" style="padding:4px 10px;text-align:center"></td></tr>
    <tr><th style="padding:4px 10px;text-align:left">Test negative</th><td id="fn" style="padding:4px 10px;text-align:center"></td><td id="tn" style="padding:4px 10px;text-align:center"></td></tr>
  </table>
  <p><span class="share" id="sens"></span> sensitivity &nbsp; <span class="share" id="spec"></span> specificity</p>
  <p class="verdict" id="verdict"></p>
  <p class="note">{e(ex["data_label"])}</p>"""
    js = RNG_JS + "const X = " + json.dumps(ex) + ";\n" + r"""
function normals(seed, n, m, sd) { const r = rng(seed), out = [];
  for (let i = 0; i < n; i++) { const u = 1 - r(), v = r(); out.push(m + sd * Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * v)); } return out; }
const withC = normals(11, X.n_with, X.with_mean, X.with_sd);
const groups = { clinic: normals(12, X.n_without, X.clinic_mean, X.clinic_sd), healthy: normals(13, X.n_without, X.healthy_mean, X.healthy_sd) };
let grp = "clinic";
function hist(vals, lo, hi, bins) { const h = new Array(bins).fill(0); vals.forEach(v => { const b = Math.min(bins - 1, Math.max(0, Math.floor((v - lo) / (hi - lo) * bins))); h[b]++; }); return h; }
function draw() {
  const cut = +$("cut").value, wo = groups[grp];
  $("cutv").textContent = cut;
  const tp = withC.filter(v => v >= cut).length, fn = withC.length - tp, fp = wo.filter(v => v >= cut).length, tn = wo.length - fp;
  $("tp").textContent = tp; $("fn").textContent = fn; $("fp").textContent = fp; $("tn").textContent = tn;
  const se = Math.round(100 * tp / withC.length), sp = Math.round(100 * tn / wo.length);
  $("sens").textContent = se + "%"; $("spec").textContent = sp + "%";
  const lo = 0, hi = 100, bins = 40, a = hist(withC, lo, hi, bins), b = hist(wo, lo, hi, bins), bw = 420 / bins;
  const top = Math.max(...a, ...b), y = c => 100 - 90 * c / top;
  let s = "";
  for (let i = 0; i < bins; i++) {
    s += `<rect x="${i * bw + 1}" y="${y(b[i])}" width="${bw / 2 - 1}" height="${100 - y(b[i])}" fill="#0369A1"/>`;
    s += `<rect x="${i * bw + bw / 2}" y="${y(a[i])}" width="${bw / 2 - 1}" height="${100 - y(a[i])}" fill="#B45309"/>`;
  }
  const cx = cut / 100 * 420;
  s += `<line x1="${cx}" y1="0" x2="${cx}" y2="104" stroke="#E11D48" stroke-width="3"/>`;
  s += `<text x="4" y="116" font-size="11" fill="#B45309">orange: has the condition</text><text x="230" y="116" font-size="11" fill="#0369A1">blue: does not</text>`;
  $("hist").innerHTML = s;
  $("verdict").textContent = grp === "healthy"
    ? `Against healthy volunteers the same test looks better: specificity ${sp}%. In the clinic it will meet look-alike illnesses, not volunteers.`
    : `Raise the cut-off and specificity rises while sensitivity falls; lower it and the reverse. No cut-off gives both for free.`;
  document.querySelectorAll("[data-grp]").forEach(btn => btn.setAttribute("aria-pressed", btn.dataset.grp === grp));
}
document.querySelectorAll("[data-grp]").forEach(btn => btn.onclick = () => { grp = btn.dataset.grp; draw(); });
$("cut").oninput = draw;
draw();
"""
    return body, js
