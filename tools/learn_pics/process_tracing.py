"""Process tracing: the five steps' pictures and the "Silver Blaze" exercise (Collier's own teaching example)."""
import html
import json

from art import check, cross, node
from learn_pics._kit import INK, DIM, ACC, HOT, g, rect, text, arrow, line, circle, path, doc, RNG_JS

e = html.escape
GREEN = "#86EFAC"


def rivals():
    # One outcome, several rival explanations, each a chain that could have led to it.
    out = g("pop", node(170, 75, "Y", 14, "#0f172a", ACC, size=14), 0)
    for k, (y, lab) in enumerate(((30, "H1"), (75, "H2"), (120, "H3"))):
        out += g("pop", node(36, y, lab, 14, "#0f172a", INK, size=12), 1 + k)
        out += g("draw", arrow(52, y, 152, 75 + (y - 75) * 0.2, DIM, 2.5, dash="5 4"), 4 + k)
    out += text(170, 108, "outcome", 11, ACC) + text(100, 142, "rival explanations", 11, INK)
    return out


def describe():
    # Good snapshots at each moment: a timeline with a document at every stop.
    out = line([(16, 110), (184, 110)], DIM, 2.5)
    for k, x in enumerate((36, 82, 128, 174)):
        out += g("pop", circle(x, 110, 5, ACC) + doc(x - 12, 54, 24, 32, INK, 3), k)
    out += text(100, 136, "snapshot each step", 12, ACC) + text(100, 30, "time", 11, DIM)
    out += arrow(80, 26, 120, 26, DIM, 2, head=5)
    return out


def hoop():
    # A hypothesis must jump through the hoop to stay in: one passes, one fails and is out.
    out = g("pop", circle(100, 64, 32, "none", ACC, 4), 0)
    out += g("draw", arrow(26, 64, 150, 64, INK, 3), 1) + node(26, 64, "H1", 13, "#0f172a", INK, size=12)
    out += g("pop", check(172, 64, 12), 2)
    out += node(40, 122, "H2", 13, "#0f172a", DIM, size=12) + g("draw", arrow(56, 122, 84, 108, DIM, 2.5), 3)
    out += g("pop", cross(98, 104, 8), 4) + text(150, 130, "fails: out", 12, HOT) + text(100, 20, "HOOP", 12, ACC)
    return out


def smoking():
    # Caught with the smoking gun: enough to confirm, but its absence clears no one.
    out = path_gun()
    out += g("pop", circle(132, 46, 6, "none", DIM, 2) + circle(142, 34, 8, "none", DIM, 2) + circle(156, 22, 10, "none", DIM, 2), 0)
    out += g("pop", node(56, 118, "H1", 13, "#0f172a", ACC, size=12) + check(84, 118, 12), 1)
    out += text(140, 122, "confirms", 12, GREEN) + text(140, 138, "if found", 11, DIM)
    return out


def path_gun():
    return path("M40,64 H120 V76 H74 L66,98 H50 L56,76 H40 Z", INK, 3, fill="#0f172a44")


def combine():
    # Several tests together: two rivals eliminated, one left standing.
    out = ""
    for k, (x, lab, ok) in enumerate(((40, "H1", False), (100, "H2", False), (160, "H3", True))):
        out += node(x, 56, lab, 16, "#0f172a", INK if ok else DIM, size=13)
        out += g("pop", check(x, 96, 13) if ok else cross(x, 96, 9), k)
    out += g("pop", rect(132, 30, 56, 52, "none", GREEN, 3, 10), 3)
    out += text(100, 134, "eliminate the rest", 12, ACC)
    return out


PICTURES = {"rivals": rivals, "describe": describe, "hoop": hoop, "smoking": smoking, "combine": combine}


def exercise(ex, quote):
    """Return (html, js). Collier's Silver Blaze clues, one at a time; each test moves the three suspects."""
    clue_buttons = "".join(f'<button type="button" data-clue="{i}">{e(c["label"])}</button>' for i, c in enumerate(ex["clues"]))
    body = f"""
  <p>{e(ex["intro"])}</p>
  <div class="controls" role="group" aria-label="Clues">{clue_buttons}
    <button type="button" id="reset">Start again</button></div>
  <label class="note"><input type="checkbox" id="strong"> Read the knife as exceptionally unusual (a smoking gun, not a straw in the wind)</label>
  <div id="suspects" aria-live="polite"></div>
  <p class="verdict" id="verdict"></p>
  <p class="note">{e(ex["data_label"])} {e(ex["weights_note"])}</p>"""
    js = RNG_JS + "const X = " + json.dumps(ex) + ";\n" + r"""
let used = new Set();
function weights() {
  const w = X.suspects.map(() => 1), out = X.suspects.map(() => false);
  for (const i of [...used].sort((a, b) => a - b)) {
    const c = X.clues[i];
    let test = c.test;
    if (c.alt && $("strong").checked) test = c.alt;
    const f = X.factor[test];
    if (test === "hoop-fail") out[c.target] = true;
    else w[c.target] *= f;
  }
  return w.map((v, i) => out[i] ? 0 : v);
}
function draw() {
  const w = weights(), sum = w.reduce((a, b) => a + b, 0) || 1;
  $("suspects").innerHTML = X.suspects.map((s, i) => {
    const pct = Math.round(100 * w[i] / sum);
    return `<p style="margin:10px 0 2px"><strong>${s}</strong> <span class="note">${w[i] === 0 ? "eliminated" : pct + "% of the weight"}</span></p>`
      + `<div class="bar"><span style="width:${pct}%;background:${w[i] === 0 ? "transparent" : "#6D28D9"}"></span></div>`;
  }).join("");
  const last = [...used].pop();
  $("verdict").textContent = last === undefined ? "Pick a clue." : X.clues[last].says;
  document.querySelectorAll("[data-clue]").forEach(b => b.setAttribute("aria-pressed", used.has(+b.dataset.clue)));
}
document.querySelectorAll("[data-clue]").forEach(b => b.onclick = () => { const i = +b.dataset.clue; used.has(i) ? used.delete(i) : used.add(i); draw(); });
$("reset").onclick = () => { used = new Set(); draw(); };
$("strong").onchange = draw;
draw();
"""
    return body, js
