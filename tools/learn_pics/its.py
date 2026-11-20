"""Interrupted time series: the six steps' pictures and the "fit the break" exercise on the tutorial's published excerpt."""
import html
import json

from learn_pics._kit import INK, DIM, ACC, HOT, COOL, g, rect, text, arrow, line, circle
from art import axes, scatter

e = html.escape

PRE = [(24 + i * 8, 52 + i * 3.2 + (2 if i % 2 else -2)) for i in range(10)]
POST = [(110 + i * 8, 96 + i * 2.5 + (2 if i % 2 else -2)) for i in range(10)]


def series():
    out = axes(16, 18, 174, 114)
    out += "".join(g("pop", circle(x, y, 3.2, INK), k) for k, (x, y) in enumerate(PRE + POST))
    out += text(100, 146, "equal steps in time", 11, DIM)
    return out


def date():
    out = axes(16, 18, 174, 114) + scatter(PRE, 3.2, DIM) + scatter(POST, 3.2, DIM)
    out += g("draw", line([(104, 18), (104, 128)], ACC, 3, "6 5"), 0)
    out += g("pop", rect(64, 20, 80, 18, "#0f172a", ACC, 2, 4) + text(104, 34, "ban starts", 12, ACC), 1)
    return out


def model():
    # Three shapes the effect could take, chosen before looking.
    out = ""
    for k, (x0, pts, lab) in enumerate([
            (10, [(14, 60), (34, 52), (34, 82), (54, 74)], "level"),
            (72, [(76, 60), (96, 52), (116, 66)], "slope"),
            (134, [(138, 60), (158, 52), (158, 74), (178, 86)], "both")]):
        out += g("pop", rect(x0, 34, 56, 66, "none", DIM, 2, 5) + line(pts, ACC, 3) + text(x0 + 28, 118, lab, 12, INK), k)
    out += text(100, 24, "decide in advance", 12, HOT)
    return out


def counterfactual():
    out = axes(16, 18, 174, 114) + line([(104, 18), (104, 128)], ACC, 2.5, "6 5")
    out += scatter(PRE, 3.2) + line([(24, 52), (96, 81)], INK, 2.5)
    out += g("draw", line([(104, 84), (186, 116)], COOL, 2.5, "5 4"), 0)
    out += g("pop", text(160, 140, "expected", 11, COOL), 1)
    return out


def segments():
    out = axes(16, 18, 174, 114) + line([(104, 18), (104, 128)], ACC, 2.5, "6 5")
    out += scatter(PRE, 3.2) + scatter(POST, 3.2, ACC) + line([(104, 84), (186, 116)], DIM, 2, "5 4")
    out += g("draw", line([(24, 52), (96, 81)], INK, 3), 0) + g("draw", line([(110, 96), (182, 118)], ACC, 3), 1)
    out += g("pop", line([(108, 84), (108, 96)], HOT, 4) + text(140, 74, "level change", 12, HOT), 2)
    return out


def checks():
    out = axes(16, 18, 174, 114)
    wave = [(24 + i * 8, 76 + 18 * (1 if (i // 3) % 2 else -1) * (0.5 + 0.5 * ((i % 3) == 1))) for i in range(21)]
    out += g("draw", line(wave, INK, 2.5), 0)
    out += g("pop", text(100, 36, "seasons?", 12, ACC), 1) + g("pop", text(100, 140, "other events?", 12, HOT), 2)
    return out


PICTURES = {"series": series, "date": date, "model": model, "counterfactual": counterfactual, "segments": segments, "checks": checks}


def exercise(ex, quote):
    """Return (html, js). The 24 published months; fit before/after, level, slope or both, and move the break."""
    body = f"""
  <p>{e(ex["intro"])}</p>
  <div class="controls" role="group" aria-label="Which model">
    <button type="button" data-m="ba">Before vs after means</button>
    <button type="button" data-m="level">Trend + level change</button>
    <button type="button" data-m="both">Trend + level + slope change</button>
  </div>
  <div class="controls"><label class="note">Break placed at <select id="its-k"></select></label></div>
  <svg id="its-svg" viewBox="0 0 400 240" style="width:100%;max-width:560px;height:auto" role="img" aria-label="Monthly admission rate with the fitted segments"></svg>
  <p class="verdict" id="its-verdict" aria-live="polite"></p>
  <p class="note">{e(ex["data_label"])}</p>"""
    js = "const X = " + json.dumps(ex) + ";\nconst $ = id => document.getElementById(id);\n" + r"""
// Rate per 100,000 person-years from the published counts and standardised populations.
const Y = X.rows.map(r => 1e5 * r[2] / r[3]), N = Y.length, labels = X.rows.map(r => r[0] + "-" + String(r[1]).padStart(2, "0"));
let m = "level", k = X.ban_index;
$("its-k").innerHTML = labels.map((l, i) => i >= 3 && i <= N - 3 ? `<option value="${i}"${i === k ? " selected" : ""}>${l}${i === X.ban_index ? " (the real ban)" : ""}</option>` : "").join("");
// Ordinary least squares by the normal equations (small, exact for these few columns).
function fit(cols) {
  const p = cols[0].length, A = Array.from({ length: p }, () => Array(p + 1).fill(0));
  cols.forEach((row, i) => { for (let a = 0; a < p; a++) { for (let b = 0; b < p; b++) A[a][b] += row[a] * row[b]; A[a][p] += row[a] * Y[i]; } });
  for (let c = 0; c < p; c++) { let piv = c; for (let r = c + 1; r < p; r++) if (Math.abs(A[r][c]) > Math.abs(A[piv][c])) piv = r;
    [A[c], A[piv]] = [A[piv], A[c]]; for (let r = 0; r < p; r++) if (r !== c) { const f = A[r][c] / A[c][c]; for (let q = c; q <= p; q++) A[r][q] -= f * A[c][q]; } }
  return A.map((row, i) => row[p] / row[i]);
}
function draw() {
  const lo = Math.min(...Y) - 10, hi = Math.max(...Y) + 10, sx = i => 44 + i * (340 / (N - 1)), sy = v => 205 - (v - lo) / (hi - lo) * 190;
  let s = `<line x1="${sx(k - 0.5)}" y1="10" x2="${sx(k - 0.5)}" y2="210" stroke="#B45309" stroke-dasharray="6 5"/>`;
  s += `<text x="${sx(k - 0.5) + 4}" y="22" font-size="12" fill="#B45309">break</text>`;
  s += `<text x="${sx(0)}" y="232" font-size="12" fill="currentColor">${labels[0]}</text><text x="${sx(N - 1)}" y="232" font-size="12" text-anchor="end" fill="currentColor">${labels[N - 1]}</text>`;
  Y.forEach((v, i) => s += `<circle cx="${sx(i)}" cy="${sy(v)}" r="3.5" fill="${i < k ? "currentColor" : "#B45309"}"/>`);
  let pred, msg;
  if (m === "ba") {
    const a = Y.slice(0, k).reduce((s, v) => s + v, 0) / k, b = Y.slice(k).reduce((s, v) => s + v, 0) / (N - k);
    pred = Y.map((_, i) => i < k ? a : b);
    msg = `Mean after − mean before = ${(b - a).toFixed(1)} per 100,000. This ignores any trend already under way.`;
  } else {
    const cols = Y.map((_, i) => m === "level" ? [1, i, i >= k ? 1 : 0] : [1, i, i >= k ? 1 : 0, i >= k ? i - k : 0]);
    const b = fit(cols); pred = cols.map(c => c.reduce((s, v, j) => s + v * b[j], 0));
    const cf = Y.map((_, i) => b[0] + b[1] * i);
    s += `<polyline fill="none" stroke="#0369A1" stroke-width="2" stroke-dasharray="5 4" points="${cf.map((v, i) => i >= k ? sx(i) + "," + sy(v) : "").filter(Boolean).join(" ")}"/>`;
    msg = `Level change at the break: ${b[2].toFixed(1)} per 100,000 (${(100 * b[2] / (b[0] + b[1] * k)).toFixed(0)}% of the expected level)` + (m === "both" ? `; slope change ${b[3].toFixed(2)} per month.` : ".");
  }
  s += `<polyline fill="none" stroke="currentColor" stroke-width="2.5" points="${pred.slice(0, k).map((v, i) => sx(i) + "," + sy(v)).join(" ")}"/>`;
  s += `<polyline fill="none" stroke="#B45309" stroke-width="2.5" points="${pred.slice(k).map((v, i) => sx(i + k) + "," + sy(v)).join(" ")}"/>`;
  $("its-svg").innerHTML = s;
  $("its-verdict").textContent = msg + (k !== X.ban_index ? " The break is not at the real ban: a 'change' here is noise or season, which is why the model and date are fixed in advance." : "");
  document.querySelectorAll("[data-m]").forEach(b => b.setAttribute("aria-pressed", b.dataset.m === m));
}
document.querySelectorAll("[data-m]").forEach(b => b.onclick = () => { m = b.dataset.m; draw(); });
$("its-k").onchange = ev => { k = +ev.target.value; draw(); };
draw();
"""
    return body, js
