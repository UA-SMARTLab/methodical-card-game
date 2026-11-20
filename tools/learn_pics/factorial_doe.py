"""Factorial experiment: the six steps' pictures and the "margins and interaction" exercise (a 2 x 2)."""
import html
import json

from learn_pics._kit import INK, DIM, FAINT, HOT, ACC, COOL, g, rect, text, line, dice, circle

e = html.escape
GX, GY, S = 64, 34, 46  # 2 x 2 grid: left edge, top edge, cell size


def _axes():
    return (text(GX + S, GY - 8, "factor A", 12, ACC) + text(GX - 6, GY + S + 4, "B", 12, COOL, anchor="end")
            + text(GX + S / 2, GY + 2 * S + 14, "off", 11, DIM) + text(GX + 1.5 * S, GY + 2 * S + 14, "on", 11, ACC)
            + text(GX - 6, GY + S / 2 + 4, "off", 11, DIM, anchor="end") + text(GX - 6, GY + 1.5 * S + 4, "on", 11, COOL, anchor="end"))


def _cell(c, r, fill="none", stroke=DIM, sw=1.5):
    return rect(GX + c * S, GY + r * S, S - 4, S - 4, fill, stroke, sw, 5)


def factors():
    out = g("pop", rect(18, 40, 70, 30, ACC, "none", 0, 6) + text(53, 60, "A: on / off", 12, "#0f172a"), 0)
    out += g("pop", rect(112, 40, 70, 30, COOL, "none", 0, 6) + text(147, 60, "B: on / off", 12, "#0f172a"), 1)
    out += g("pop", text(100, 104, "two factors,", 13, INK), 2) + g("pop", text(100, 122, "two levels each", 13, INK), 3)
    return out


def combine():
    out = _axes()
    for k, (c, r) in enumerate([(0, 0), (1, 0), (0, 1), (1, 1)]):
        out += g("pop", _cell(c, r, FAINT, INK), k)
    out += g("pop", text(GX + 2 * S + 16, GY + S + 4, "4 runs", 12, HOT), 4)
    return out


def randomise():
    out = _axes() + "".join(_cell(c, r) for c in range(2) for r in range(2))
    out += g("roll", dice(30, 120, 18, 4))
    spots = [(0, 0), (1, 1), (1, 0), (0, 1), (1, 1), (0, 0), (0, 1), (1, 0)]
    for k, (c, r) in enumerate(spots):
        dx = 12 + (k // 4) * 18
        out += g("pop", circle(GX + c * S + dx, GY + r * S + 20, 5, INK), 1 + k)
    return out


def margins():
    out = _axes() + "".join(_cell(c, r) for c in range(2) for r in range(2))
    # All of column "A on" against all of column "A off": every unit counts for A, and again for B.
    out += g("pop", rect(GX + S - 3, GY - 3, S + 2, 2 * S + 2, "none", ACC, 3, 6), 0)
    out += g("pop", rect(GX - 3, GY + S - 3, 2 * S + 2, S + 2, "none", COOL, 3, 6), 1)
    out += g("pop", text(GX + 2 * S + 16, GY + 30, "main", 12, INK) + text(GX + 2 * S + 16, GY + 46, "effects", 12, INK), 2)
    return out


def interaction():
    base, top = 124, 30
    out = line([(30, base), (176, base)], DIM, 2) + text(48, base + 14, "A off", 11, DIM) + text(158, base + 14, "A on", 11, ACC)
    # Without B, A helps a little; with B on, A helps a lot: the lines are not parallel.
    out += g("draw", line([(48, 104), (158, 84)], DIM, 3), 0) + text(176, 82, "B off", 11, DIM, anchor="end")
    out += g("draw", line([(48, 96), (158, top + 14)], COOL, 3), 1) + text(150, top + 4, "B on", 11, COOL, anchor="end")
    out += g("pop", text(80, top + 4, "not parallel", 12, HOT), 2)
    return out


def fraction():
    # A 2 x 2 x 2 has eight corners; a half fraction runs four of them, chosen so main effects stay estimable.
    pts = {(0, 0, 0): (50, 110), (1, 0, 0): (120, 110), (0, 1, 0): (50, 50), (1, 1, 0): (120, 50),
           (0, 0, 1): (80, 92), (1, 0, 1): (150, 92), (0, 1, 1): (80, 32), (1, 1, 1): (150, 32)}
    edges = [(a, b) for a in pts for b in pts if a < b and sum(x != y for x, y in zip(a, b)) == 1]
    out = "".join(line([pts[a], pts[b]], DIM, 1.5) for a, b in edges)
    for k, (key, (x, y)) in enumerate(sorted(pts.items())):
        run = sum(key) % 2 == 1
        out += g("pop", circle(x, y, 7 if run else 5, HOT if run else "none", DIM if not run else "none", 2), k)
    out += g("pop", text(100, 140, "half the runs", 12, HOT), 8)
    return out


PICTURES = {"factors": factors, "combine": combine, "randomise": randomise, "margins": margins,
            "interaction": interaction, "fraction": fraction}


def exercise(ex, quote):
    """Return (html, js). Set the true effects of A, B and their interaction; read what each analysis estimates."""
    body = f"""
  <p>{e(ex["intro"])}</p>
  <div class="controls" style="flex-direction:column;align-items:flex-start">
    <label>Effect of A alone: <input type="range" id="a" min="0" max="10" value="{ex["start"][0]}"> <output id="a-o"></output></label>
    <label>Effect of B alone: <input type="range" id="b" min="0" max="10" value="{ex["start"][1]}"> <output id="b-o"></output></label>
    <label>Extra when both are on (interaction): <input type="range" id="ab" min="-6" max="6" value="{ex["start"][2]}"> <output id="ab-o"></output></label>
  </div>
  <table aria-live="polite"><thead><tr><th></th><th>A off</th><th>A on</th></tr></thead>
    <tbody><tr><th>B off</th><td id="c00"></td><td id="c10"></td></tr><tr><th>B on</th><td id="c01"></td><td id="c11"></td></tr></tbody></table>
  <table><tbody>
    <tr><td>A at the margins (all A on minus all A off)</td><td><output id="ma"></output></td></tr>
    <tr><td>A without B (A alone minus neither)</td><td><output id="sa"></output></td></tr>
    <tr><td>A with B (both minus B alone)</td><td><output id="sab"></output></td></tr>
  </tbody></table>
  <p class="verdict" id="verdict"></p>
  <p class="note">{e(ex["data_label"])} Every cell starts from {ex["base"]} points; there is no noise, so the numbers show what each comparison estimates.</p>"""
    js = "const X = " + json.dumps(ex) + ";\nconst $ = id => document.getElementById(id);\n" + r"""
function draw() {
  const a = +$("a").value, b = +$("b").value, ab = +$("ab").value, y0 = X.base;
  $("a-o").textContent = a; $("b-o").textContent = b; $("ab-o").textContent = ab;
  const c = { "00": y0, "10": y0 + a, "01": y0 + b, "11": y0 + a + b + ab };
  for (const k in c) $("c" + k).textContent = c[k];
  const ma = ((c["10"] + c["11"]) - (c["00"] + c["01"])) / 2;
  $("ma").textContent = ma; $("sa").textContent = c["10"] - c["00"]; $("sab").textContent = c["11"] - c["01"];
  $("verdict").textContent = ab === 0
    ? `No interaction: A adds ${a} with or without B, and the margins use every unit to estimate it.`
    : `With an interaction, A adds ${a} without B but ${a + ab} with it. The margins give ${ma}, an average of the two, which describes neither situation.`;
}
["a", "b", "ab"].forEach(id => $(id).oninput = draw);
draw();
"""
    return body, js
