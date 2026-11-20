"""Cost-effectiveness analysis: the five steps' pictures and the "price of a QALY" exercise."""
import html
import json

from learn_pics._kit import INK, DIM, ACC, HOT, COOL, g, person, rect, text, arrow, line, circle, pill, RNG_JS
from art import clock

e = html.escape


def alternatives():
    out = rect(16, 38, 70, 60, "none", ACC, 2.5, 6) + text(51, 30, "new", 12, ACC) + pill(51, 68, ACC)
    out += text(100, 72, "vs", 14, INK)
    out += rect(114, 38, 70, 60, "none", COOL, 2.5, 6) + text(149, 30, "usual care", 12, COOL) + pill(149, 68, INK, False)
    out += g("pop", text(100, 124, "whose costs count?", 12, INK), 0)
    return out


def costs():
    out = ""
    for k in range(5):
        x = 30 + k * 34
        out += g("pop", circle(x, 60, 13 - k * 1.6, "none", ACC, 2.5) + text(x, 64, "€", 12, ACC), k)
        out += text(x, 96, f"yr {k + 1}", 11, DIM)
    out += g("draw", arrow(184, 116, 30, 116, INK, 2), 5) + text(100, 138, "worth less later", 11, INK)
    return out


def qalys():
    base = 120
    out = line([(20, base), (186, base)], DIM, 2) + line([(20, base), (20, 30)], DIM, 2) + text(12, 36, "1", 11, DIM) + text(12, base, "0", 11, DIM)
    for i, q in enumerate((0.9, 0.8, 0.8, 0.6, 0.4)):
        h = 86 * q
        out += g("grow", rect(28 + i * 32, base - h, 26, h, ACC, "none", 0, 2), i)
    out += text(100, 140, "years × quality", 11, INK)
    return out


def icer():
    out = text(100, 40, "Δ cost", 16, ACC) + g("draw", line([(52, 54), (148, 54)], INK, 3), 0)
    out += text(100, 78, "Δ QALYs", 16, COOL)
    out += g("pop", text(100, 116, "= cost per QALY", 14, HOT), 1)
    return out


def sensitivity():
    out = line([(100, 24), (100, 128)], DIM, 2)
    # A tornado: the widest bar is the input the answer is most sensitive to.
    for i, (lab, lo, hi) in enumerate((("price", 56, 186), ("effect", 70, 150), ("horizon", 84, 120))):
        y = 44 + i * 30
        out += g("grow", rect(lo, y - 9, hi - lo, 18, ACC if i == 0 else COOL, "none", 0, 3), i) + text(8, y + 4, lab, 11, INK, anchor="start")
    out += text(100, 140, "which input moves it most?", 11, INK)
    return out


PICTURES = {"alternatives": alternatives, "costs": costs, "qalys": qalys, "icer": icer, "sensitivity": sensitivity}


def exercise(ex, quote):
    """Return (html, js). Example costs and QALYs; the ratio and a chosen willingness to pay."""
    body = f"""
  <p>{e(ex["intro"])}</p>
  <label class="note" style="display:block">Cost of the new treatment per patient: <output id="cv"></output><br>
    <input type="range" id="cost" min="10000" max="60000" step="1000" value="30000" style="width:100%;max-width:420px"></label>
  <label class="note" style="display:block">QALYs with the new treatment: <output id="qv"></output><br>
    <input type="range" id="qaly" min="5.1" max="6.5" step="0.1" value="5.8" style="width:100%;max-width:420px"></label>
  <label class="note" style="display:block">Willingness to pay per QALY: <output id="wv"></output><br>
    <input type="range" id="wtp" min="5000" max="80000" step="1000" value="30000" style="width:100%;max-width:420px"></label>
  <p aria-live="polite"><span class="share" id="icer"></span> per QALY gained</p>
  <p class="verdict" id="verdict"></p>
  <p class="note">{e(ex["data_label"])}</p>"""
    js = RNG_JS + "const X = " + json.dumps(ex) + ";\n" + r"""
const fmt = v => Math.round(v).toLocaleString("en-GB");
function draw() {
  const c = +$("cost").value, q = +$("qaly").value, w = +$("wtp").value;
  const dc = c - X.usual_cost, dq = q - X.usual_qaly, r = dc / dq;
  $("cv").textContent = fmt(c); $("qv").textContent = q.toFixed(1); $("wv").textContent = fmt(w);
  $("icer").textContent = fmt(r);
  $("verdict").textContent = `It costs ${fmt(dc)} more for ${dq.toFixed(1)} more QALYs: ${fmt(r)} per QALY. `
    + (Math.round(r) <= w ? "Below your willingness to pay: cost-effective by your standard." : "Above your willingness to pay: not cost-effective by your standard.");
}
["cost", "qaly", "wtp"].forEach(id => $(id).oninput = draw);
draw();
"""
    return body, js
