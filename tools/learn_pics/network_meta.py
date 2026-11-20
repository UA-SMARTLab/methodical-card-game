"""Network meta-analysis: the five steps' pictures (after Ioannidis 2009) and the indirect-comparison exercise."""
import html
import json

from learn_pics._kit import INK, DIM, ACC, HOT, COOL, g, rect, text, arrow, line, circle, path, RNG_JS
from art import node, check, cross

e = html.escape

POS = {"P": (100, 118), "A": (40, 40), "B": (160, 40), "C": (34, 106), "D": (166, 106)}


def network():
    # Treatments as nodes, trials as links; thicker links have more trials.
    out = ""
    for k, (a, b, w) in enumerate((("A", "P", 5), ("B", "P", 4), ("C", "P", 3), ("D", "P", 2), ("A", "B", 2), ("A", "C", 2))):
        out += g("draw", line([POS[a], POS[b]], INK, w), k)
    for k, (lab, (x, y)) in enumerate(POS.items()):
        out += g("pop", node(x, y, lab, 13, "#0f172a", ACC if lab == "P" else INK, size=13), k)
    return out + text(100, 144, "P = placebo", 11, DIM)


def geometry():
    # Most trials go to placebo; some pairs were never compared (dashed).
    out = ""
    for a, b, w in (("A", "P", 6), ("B", "P", 5), ("C", "P", 5), ("D", "P", 4)):
        out += line([POS[a], POS[b]], INK, w)
    for k, (a, b) in enumerate((("B", "D"), ("C", "D"), ("B", "C"))):
        out += g("draw", line([POS[a], POS[b]], HOT, 2, "4 4"), k)
    out += "".join(node(x, y, lab, 13, "#0f172a", INK, size=13) for lab, (x, y) in POS.items())
    return out + g("pop", text(100, 22, "never compared", 12, HOT), 3)


def indirect():
    # A and B meet only through placebo: A vs B = (A vs P) - (B vs P).
    out = line([POS["A"], POS["P"]], INK, 4) + line([POS["B"], POS["P"]], INK, 4)
    out += g("draw", line([POS["A"], POS["B"]], ACC, 3, "6 4"), 1)
    out += "".join(node(*POS[k], k, 13, "#0f172a", INK, size=13) for k in ("A", "B", "P"))
    return out + g("pop", text(100, 30, "indirect", 13, ACC), 2) + text(100, 144, "through placebo", 11, DIM)


def incoherence():
    # A loop: the direct link and the indirect path give two answers to compare.
    out = line([POS["A"], POS["P"]], INK, 3) + line([POS["B"], POS["P"]], INK, 3)
    out += g("draw", line([POS["A"], POS["B"]], COOL, 4), 1)
    out += "".join(node(*POS[k], k, 13, "#0f172a", INK, size=13) for k in ("A", "B", "P"))
    out += g("pop", text(100, 30, "direct", 12, COOL), 2) + g("pop", text(100, 92, "indirect", 12, ACC), 3)
    return out + g("pop", text(100, 144, "agree?", 13, HOT), 4)


def rank():
    # The chance of being best, per treatment.
    base = 120
    out = line([(24, base), (184, base)], DIM, 2)
    for k, (lab, h) in enumerate((("A", 76), ("C", 40), ("B", 22), ("D", 10), ("P", 2))):
        x = 30 + k * 32
        out += g("grow", rect(x, base - h, 22, h, ACC if k == 0 else INK, "none", 0, 2), k) + text(x + 11, base + 16, lab, 12, INK)
    return out + text(110, 24, "chance of being best", 12, ACC)


PICTURES = {"network": network, "geometry": geometry, "indirect": indirect, "incoherence": incoherence, "rank": rank}


def exercise(ex, quote):
    """Return (html, js). Example odds ratios: an adjusted indirect comparison of A vs B through placebo."""
    body = f"""
  <p>{e(ex["intro"])}</p>
  <div class="controls"><label>A vs placebo, odds ratio <input type="range" id="a" min="0.3" max="1.5" step="0.05" value="{ex["a_vs_p"]["or"]}"></label> <output id="av"></output></div>
  <div class="controls"><label>B vs placebo, odds ratio <input type="range" id="b" min="0.3" max="1.5" step="0.05" value="{ex["b_vs_p"]["or"]}"></label> <output id="bv"></output></div>
  <p class="share" id="ind" aria-live="polite"></p>
  <p class="verdict" id="verdict"></p>
  <p class="note">{e(ex["data_label"])} {e(ex["method_note"])}</p>"""
    js = RNG_JS + "const X = " + json.dumps(ex) + ";\n" + r"""
const ci = (m, s) => `${Math.exp(m - 1.96 * s).toFixed(2)} to ${Math.exp(m + 1.96 * s).toFixed(2)}`;
function draw() {
  const a = Math.log(+$("a").value), b = Math.log(+$("b").value);
  $("av").textContent = (+$("a").value).toFixed(2); $("bv").textContent = (+$("b").value).toFixed(2);
  const m = a - b, s = Math.hypot(X.a_vs_p.se, X.b_vs_p.se);
  const d = Math.log(X.a_vs_b_direct.or), sd = X.a_vs_b_direct.se;
  const z = (m - d) / Math.hypot(s, sd);
  $("ind").textContent = `Indirect A vs B: OR ${Math.exp(m).toFixed(2)} (95% CI ${ci(m, s)})`;
  $("verdict").textContent = `Direct trial: OR ${X.a_vs_b_direct.or.toFixed(2)} (95% CI ${ci(d, sd)}). ` +
    (Math.abs(z) > 1.96 ? `Direct and indirect disagree (z = ${z.toFixed(1)}): incoherence. Look for why before combining them.`
                        : `They agree within chance (z = ${z.toFixed(1)}), so both can feed one network estimate. Note how wide the indirect interval is: it carries the uncertainty of two comparisons.`);
}
$("a").oninput = draw; $("b").oninput = draw;
draw();
"""
    return body, js
