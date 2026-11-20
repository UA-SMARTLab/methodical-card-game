"""Case-control study: five steps' pictures and the "odds ratio from a 2 x 2 table" exercise."""
import html
import json

from learn_pics._kit import INK, DIM, ACC, HOT, g, person, rect, text, arrow, line

e = html.escape


def cases():
    out = text(100, 22, "people with the disease", 12, HOT)
    spots = [(40, 60), (70, 60), (100, 60), (130, 60), (160, 60), (55, 104), (85, 104), (115, 104), (145, 104)]
    out += "".join(g("pop", person(x, y, 0.9, HOT), i) for i, (x, y) in enumerate(spots))
    return out + g("pop", text(100, 140, "all or most cases", 11, DIM), 9)


def controls():
    # Many people without the disease; only a few are sampled, from the same population the cases came from.
    out = rect(10, 28, 120, 100, "none", DIM, 2, 8, dash="5 4") + text(70, 22, "source population", 11, DIM)
    for r in range(3):
        for c in range(5):
            picked = (r + c) % 4 == 0
            out += person(26 + c * 22, 52 + r * 30, 0.7, INK if picked else DIM)
    out += g("draw", arrow(132, 78, 160, 78, INK, 2.5), 1)
    out += "".join(g("pop", person(176, 52 + k * 30, 0.75, INK), 2 + k) for k in range(3))
    return out + text(172, 142, "controls", 11, INK)


def ask_past():
    out = text(150, 22, "CASES", 12, HOT) + text(150, 88, "CONTROLS", 12, INK)
    for k in range(3):
        out += person(126 + k * 24, 48, 0.75, HOT) + person(126 + k * 24, 114, 0.75, INK)
    out += g("draw", arrow(110, 46, 50, 46, ACC, 2.5), 1) + g("draw", arrow(110, 112, 50, 112, ACC, 2.5), 2)
    out += g("pop", text(30, 50, "past?", 13, ACC), 3) + g("pop", text(30, 116, "past?", 13, ACC), 4)
    return out + text(80, 140, "look back in time", 11, DIM)


def odds():
    # The 2 x 2 table, with the cross-product a*d / b*c.
    x0, y0, w, h = 52, 34, 64, 40
    out = text(84, 26, "exposed", 11, ACC) + text(148, 26, "not", 11, DIM)
    out += text(28, 58, "cases", 11, HOT) + text(28, 98, "controls", 11, INK)
    cells = [("a", 0, 0, ACC), ("b", 1, 0, DIM), ("c", 0, 1, ACC), ("d", 1, 1, DIM)]
    for i, (lab, cx, cy, c) in enumerate(cells):
        out += g("pop", rect(x0 + cx * w, y0 + cy * h, w, h, "none", c, 2.5, 4) + text(x0 + cx * w + w / 2, y0 + cy * h + 27, lab, 18, INK), i)
    out += g("pop", text(116, 138, "OR = (a·d) / (b·c)", 14, ACC), 4)
    return out


def matching():
    out = ""
    for k in range(3):
        y = 36 + k * 38
        out += g("pop", person(60, y, 0.8, HOT) + line([(72, y), (118, y)], DIM, 2, dash="3 3") + person(130, y, 0.8, INK), k)
    out += g("pop", text(60, 144, "case", 11, HOT) + text(130, 144, "matched control", 11, INK), 3)
    return out + g("pop", text(180, 76, "age", 12, DIM) + text(180, 92, "sex", 12, DIM), 4)


PICTURES = {"cases": cases, "controls": controls, "ask_past": ask_past, "odds": odds, "matching": matching}


def exercise(ex, quote):
    """Return (html, js). A 2 x 2 table the reader can change; the odds ratio follows the cross-product."""
    a, b, c, d = ex["table"]
    def cell(i, v):
        return f'<input type="number" min="0" step="1" value="{v}" id="cc{i}" aria-label="{e(ex["cells"][i])}" style="width:6em;font:inherit;padding:6px">'
    body = f"""
  <p>{e(ex["intro"])}</p>
  <table style="border-collapse:collapse;margin:8px 0">
    <tr><th></th><th style="padding:6px">Exposed</th><th style="padding:6px">Not exposed</th><th style="padding:6px">Odds of exposure</th></tr>
    <tr><th style="padding:6px;text-align:left">Cases</th><td>{cell(0, a)}</td><td>{cell(1, b)}</td><td id="oc" style="padding:6px"></td></tr>
    <tr><th style="padding:6px;text-align:left">Controls</th><td>{cell(2, c)}</td><td>{cell(3, d)}</td><td id="on" style="padding:6px"></td></tr>
  </table>
  <p class="verdict" id="verdict" aria-live="polite"></p>
  <div class="controls"><button type="button" id="reset">Back to the example</button></div>
  <p class="note">{e(ex["data_label"])}</p>"""
    js = "const X = " + json.dumps(ex) + r""";
const $ = id => document.getElementById(id);
const f = v => (Math.round(v * 100) / 100).toString();
function draw() {
  const [a, b, c, d] = [0, 1, 2, 3].map(i => Math.max(0, +$("cc" + i).value || 0));
  $("oc").textContent = b ? `${a} / ${b} = ${f(a / b)}` : "no unexposed cases";
  $("on").textContent = d ? `${c} / ${d} = ${f(c / d)}` : "no unexposed controls";
  if (!b || !c || !d) { $("verdict").textContent = "Put a number above zero in every cell to get an odds ratio."; return; }
  const or = (a * d) / (b * c);
  $("verdict").textContent = `Odds ratio = (${a} × ${d}) / (${b} × ${c}) = ${f(or)}. ` + (or > 1.05
    ? "Cases were more often exposed than controls."
    : or < 0.95 ? "Cases were less often exposed than controls." : "Cases and controls were exposed about equally often.");
}
for (let i = 0; i < 4; i++) $("cc" + i).oninput = draw;
$("reset").onclick = () => { X.table.forEach((v, i) => $("cc" + i).value = v); draw(); };
draw();
"""
    return body, js
