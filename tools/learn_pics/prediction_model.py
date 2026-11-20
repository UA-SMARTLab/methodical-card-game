"""Prediction model: the five steps' pictures and the "add predictors, watch the gap" exercise."""
import html
import json

from learn_pics._kit import INK, DIM, ACC, HOT, COOL, g, person, rect, text, arrow, line, circle, RNG_JS
from art import clock

e = html.escape


def define():
    out = person(40, 80, 1.0, INK) + clock(150, 56, 18, ACC)
    out += g("draw", arrow(62, 76, 126, 62, DIM, 2.5), 0) + g("pop", text(134, 104, "event by 10 years?", 12, ACC), 1)
    out += text(100, 136, "outcome, how and when", 11, DIM)
    return out


def develop():
    out = ""
    for i, (lab, w) in enumerate((("age", 0.9), ("smoking", 0.6), ("blood pressure", 0.75))):
        y = 40 + i * 28
        out += text(52, y + 4, lab, 11, INK) + g("grow", rect(100, y - 8, 50 * w, 12, ACC, "none", 0, 2), i)
    out += g("draw", arrow(100, 116, 140, 116, INK, 2.5), 3) + g("pop", text(166, 121, "risk %", 13, HOT), 4)
    out += text(60, 121, "weights", 11, DIM)
    return out


def internal():
    out = line([(24, 120), (186, 120)], DIM, 2)
    out += g("grow", rect(50, 40, 36, 80, ACC, "none", 0, 3), 0) + text(68, 136, "apparent", 11, ACC)
    out += g("grow", rect(118, 66, 36, 54, COOL, "none", 0, 3), 1) + text(136, 136, "corrected", 11, COOL)
    out += g("pop", text(100, 28, "optimism", 13, HOT) + line([(88, 40), (164, 40)], HOT, 1.5, dash="3 3") + line([(160, 40), (160, 66)], HOT, 2), 2)
    return out


def measure():
    out = line([(20, 120), (96, 120)], DIM, 2) + line([(20, 120), (20, 40)], DIM, 2)
    out += g("draw", path_curve(), 0) + text(58, 136, "ranks well", 11, INK)
    out += line([(110, 120), (186, 120)], DIM, 2) + line([(110, 120), (110, 40)], DIM, 2)
    out += line([(110, 120), (186, 44)], DIM, 1.5, dash="3 3")
    out += "".join(g("pop", circle(110 + k * 15, 116 - k * 15 + (4 if k % 2 else -3), 3.5, ACC), 1 + k) for k in range(1, 5))
    out += text(148, 136, "risks match", 11, ACC)
    return out


def path_curve():
    return line([(20, 120), (26, 84), (36, 64), (52, 52), (72, 44), (96, 40)], INK, 2.5)


def external():
    out = rect(16, 44, 54, 50, "none", DIM, 2, 6) + text(43, 36, "built here", 11, DIM)
    out += g("draw", arrow(74, 69, 120, 69, ACC, 2.5), 0) + g("pop", text(97, 60, "same formula", 11, ACC), 1)
    for k in range(4):
        out += g("pop", person(136 + (k % 2) * 22, 54 + (k // 2) * 34, 0.6, COOL), 2 + k)
    out += text(158, 128, "new people", 11, COOL)
    return out


PICTURES = {"define": define, "develop": develop, "internal": internal, "measure": measure, "external": external}


def exercise(ex, quote):
    """Return (html, js). Least-squares fits on example data; apparent R² against R² in a new sample."""
    body = f"""
  <p>{e(ex["intro"])}</p>
  <label class="note" style="display:block">Noise predictors added: <output id="kv"></output><br>
    <input type="range" id="k" min="0" max="{ex["max_noise"]}" step="1" value="0" style="width:100%;max-width:420px"></label>
  <div class="arms" aria-live="polite">
    <div class="arm"><h3>On the 60 it was built on</h3><p><span class="share" id="app"></span> explained</p><div class="bar"><span id="app-bar"></span></div></div>
    <div class="arm"><h3>On 1000 new people</h3><p><span class="share" id="val"></span> explained</p><div class="bar"><span id="val-bar"></span></div></div>
  </div>
  <p class="verdict" id="verdict"></p>
  <p class="note">{e(ex["data_label"])}</p>"""
    js = RNG_JS + "const X = " + json.dumps(ex) + ";\n" + r"""
function gauss(r) { const u = 1 - r(), v = r(); return Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * v); }
function sample(seed, n) { const r = rng(seed), rows = [];
  for (let i = 0; i < n; i++) { const x = Array.from({ length: 2 + X.max_noise }, () => gauss(r));
    rows.push({ x, y: 0.6 * x[0] + 0.4 * x[1] + 0.8 * gauss(r) }); } return rows; }
const dev = sample(31, X.n_dev), fresh = sample(32, X.n_new);
function fit(k) { // least squares with an intercept and the first 2 + k predictors, by the normal equations
  const p = 3 + k, A = Array.from({ length: p }, () => new Array(p + 1).fill(0));
  dev.forEach(({ x, y }) => { const z = [1, ...x.slice(0, 2 + k)];
    for (let i = 0; i < p; i++) { for (let j = 0; j < p; j++) A[i][j] += z[i] * z[j]; A[i][p] += z[i] * y; } });
  for (let c = 0; c < p; c++) { let m = c; for (let r = c + 1; r < p; r++) if (Math.abs(A[r][c]) > Math.abs(A[m][c])) m = r;
    [A[c], A[m]] = [A[m], A[c]];
    for (let r = 0; r < p; r++) if (r !== c) { const f = A[r][c] / A[c][c]; for (let j = c; j <= p; j++) A[r][j] -= f * A[c][j]; } }
  return A.map((row, i) => row[p] / row[i]); }
function r2(b, data) { const k = b.length - 3, mean = data.reduce((s, d) => s + d.y, 0) / data.length; let ss = 0, st = 0;
  data.forEach(({ x, y }) => { const z = [1, ...x.slice(0, 2 + k)], yh = z.reduce((s, v, i) => s + v * b[i], 0); ss += (y - yh) ** 2; st += (y - mean) ** 2; });
  return 1 - ss / st; }
function draw() { const k = +$("k").value, b = fit(k), a = r2(b, dev), v = r2(b, fresh);
  $("kv").textContent = k;
  $("app").textContent = Math.round(100 * a) + "%"; $("val").textContent = Math.round(100 * Math.max(0, v)) + "%";
  $("app-bar").style.width = Math.round(100 * a) + "%"; $("val-bar").style.width = Math.round(100 * Math.max(0, v)) + "%";
  $("verdict").textContent = k === 0 ? "Only the two real predictors: the model does about as well on new people as on its own data."
    : `With ${k} noise predictors the model explains ${Math.round(100 * a)}% of its own data but ${Math.round(100 * Math.max(0, v))}% of new people's. The gap is optimism.`; }
$("k").oninput = draw;
draw();
"""
    return body, js
