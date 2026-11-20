"""Difference-in-differences: the five steps' pictures and the "two subtractions" exercise."""
import html
import json

from learn_pics._kit import INK, DIM, ACC, HOT, COOL, TREAT, CONTROL, g, rect, text, arrow, line, circle, RNG_JS
from art import axes

e = html.escape


def groups():
    out = rect(20, 30, 70, 90, "none", TREAT, 2.5, 8) + rect(110, 30, 70, 90, "none", CONTROL, 2.5, 8)
    out += text(55, 22, "gets policy", 11, TREAT) + text(145, 22, "does not", 11, CONTROL)
    for k, x in enumerate((40, 70)):
        out += g("pop", circle(x, 75, 12, TREAT), k) + g("pop", circle(x + 90, 75, 12, CONTROL), k + 2)
    out += text(100, 140, "two groups", 11, DIM)
    return out


def periods():
    out = rect(18, 34, 164, 84, "none", DIM, 2, 6) + line([(100, 34), (100, 118)], DIM, 2)
    out += line([(18, 76), (182, 76)], DIM, 2)
    out += text(59, 28, "before", 11, INK) + text(141, 28, "after", 11, INK)
    cells = [(59, 60, CONTROL, "control"), (141, 60, CONTROL, "control"), (59, 102, TREAT, "control"), (141, 102, HOT, "policy")]
    for k, (x, y, c, lab) in enumerate(cells):
        out += g("pop", text(x, y, lab, 12, c), k)
    out += text(100, 140, "2 × 2", 12, ACC)
    return out


def change():
    out = axes(16, 18, 172, 112) + line([(100, 18), (100, 128)], DIM, 2, "4 4")
    out += g("draw", line([(30, 104), (170, 88)], CONTROL, 3), 0) + g("draw", line([(30, 80), (170, 40)], TREAT, 3), 1)
    out += g("pop", arrow(178, 104, 178, 88, CONTROL, 2.5, head=5), 2) + g("pop", arrow(186, 80, 186, 40, TREAT, 2.5, head=5), 3)
    out += text(60, 142, "change in each", 11, DIM)
    return out


def subtract():
    out = axes(16, 18, 172, 112) + line([(100, 18), (100, 128)], DIM, 2, "4 4")
    out += line([(30, 104), (100, 98), (170, 88)], CONTROL, 3) + line([(30, 80), (100, 74)], TREAT, 3)
    out += g("draw", line([(100, 74), (170, 64)], TREAT, 2.5, "5 4"), 0)
    out += g("draw", line([(100, 74), (170, 40)], TREAT, 3.5), 1)
    out += g("pop", line([(178, 64), (178, 40)], HOT, 3.5), 2) + g("pop", text(150, 30, "effect", 12, HOT), 3)
    return out


def trends():
    out = axes(16, 18, 172, 112) + line([(110, 18), (110, 128)], DIM, 2, "4 4")
    out += g("draw", line([(24, 108), (50, 102), (76, 97), (102, 90)], CONTROL, 3), 0)
    out += g("draw", line([(24, 82), (50, 76), (76, 71), (102, 64)], TREAT, 3), 1)
    out += g("pop", text(64, 50, "parallel before?", 12, ACC), 2)
    return out


PICTURES = {"groups": groups, "periods": periods, "change": change, "subtract": subtract, "trends": trends}


def exercise(ex, quote):
    """Return (html, js). Example yearly means for two groups; compare a before-after reading with the DiD reading."""
    body = f"""
  <p>{e(ex["intro"])}</p>
  <div class="controls" role="group" aria-label="Which comparison">
    <button type="button" data-how="ba">Before vs after, treated only</button>
    <button type="button" data-how="did">Difference in differences</button>
  </div>
  <div class="controls" role="group" aria-label="Trends before the policy">
    <button type="button" data-tr="0">Trends parallel before</button>
    <button type="button" data-tr="1">Treated group already rising faster</button>
  </div>
  <svg id="did-svg" viewBox="0 0 400 240" style="width:100%;max-width:560px;height:auto" role="img" aria-label="Outcome over time in the treated and control groups"></svg>
  <p class="verdict" id="did-verdict" aria-live="polite"></p>
  <p class="note">{e(ex["data_label"])}</p>"""
    js = RNG_JS + "const X = " + json.dumps(ex) + ";\n" + r"""
let how = "ba", tr = 0;
function series() {
  const r = rng(X.seed), T = X.years, k0 = X.policy_year;
  const ctl = [], trt = [];
  for (let t = 0; t < T; t++) {
    const common = X.common_slope * t + (r() - 0.5) * X.noise;
    ctl.push(X.control_level + common);
    const extra = tr ? X.diverging_slope * t : 0;
    trt.push(X.treated_level + common + extra + (t >= k0 ? X.true_effect : 0) + (r() - 0.5) * X.noise);
  }
  return [trt, ctl];
}
const mean = a => a.reduce((s, v) => s + v, 0) / a.length;
function draw() {
  const [trt, ctl] = series(), k0 = X.policy_year, T = X.years;
  const all = trt.concat(ctl), lo = Math.min(...all) - 2, hi = Math.max(...all) + 2;
  const sx = t => 40 + t * (340 / (T - 1)), sy = v => 210 - (v - lo) / (hi - lo) * 190;
  const pl = (a, c) => `<polyline fill="none" stroke="${c}" stroke-width="3" points="${a.map((v, t) => sx(t) + "," + sy(v)).join(" ")}"/>`;
  let s = `<line x1="${sx(k0 - 0.5)}" y1="10" x2="${sx(k0 - 0.5)}" y2="215" stroke="currentColor" stroke-dasharray="4 4" opacity=".5"/>`;
  s += `<text x="${sx(k0 - 0.5) + 4}" y="22" font-size="12" fill="currentColor">policy</text>`;
  s += pl(ctl, "#0369A1") + pl(trt, "#B45309");
  s += `<text x="${sx(T - 1)}" y="${sy(trt[T - 1]) - 8}" font-size="12" text-anchor="end" fill="#B45309">treated</text>`;
  s += `<text x="${sx(T - 1)}" y="${sy(ctl[T - 1]) + 18}" font-size="12" text-anchor="end" fill="#0369A1">control</text>`;
  $("did-svg").innerHTML = s;
  const tb = mean(trt.slice(0, k0)), ta = mean(trt.slice(k0)), cb = mean(ctl.slice(0, k0)), ca = mean(ctl.slice(k0));
  const ba = ta - tb, did = (ta - tb) - (ca - cb);
  $("did-verdict").textContent = (how === "ba"
    ? `Treated after − before = ${ba.toFixed(1)}. This mixes the policy with everything else that changed over those years.`
    : `(${ta.toFixed(1)} − ${tb.toFixed(1)}) − (${ca.toFixed(1)} − ${cb.toFixed(1)}) = ${did.toFixed(1)}.`)
    + ` The true effect built into these data is ${X.true_effect}.`
    + (tr ? " The treated group was already pulling away before the policy, so even the DiD estimate carries that drift." : "");
  document.querySelectorAll("[data-how]").forEach(b => b.setAttribute("aria-pressed", b.dataset.how === how));
  document.querySelectorAll("[data-tr]").forEach(b => b.setAttribute("aria-pressed", +b.dataset.tr === tr));
}
document.querySelectorAll("[data-how]").forEach(b => b.onclick = () => { how = b.dataset.how; draw(); });
document.querySelectorAll("[data-tr]").forEach(b => b.onclick = () => { tr = +b.dataset.tr; draw(); });
draw();
"""
    return body, js
