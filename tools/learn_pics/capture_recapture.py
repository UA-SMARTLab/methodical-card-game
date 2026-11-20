"""Capture–recapture: the five steps' pictures and the "two lists" exercise (real Rajasthan counts, then a seeded simulation)."""
import html
import json

from learn_pics._kit import INK, DIM, ACC, HOT, COOL, g, person, rect, text, arrow, line, circle, doc, RNG_JS

e = html.escape


def lists():
    out = g("pop", doc(24, 30, 50, 70, ACC, 5), 0) + g("pop", doc(126, 30, 50, 70, COOL, 5), 1)
    out += text(49, 120, "list A", 12, ACC) + text(151, 120, "list B", 12, COOL)
    out += text(100, 140, "two separate sources", 11, DIM)
    return out


def match():
    out = ""
    for k, (y, both) in enumerate([(38, True), (66, False), (94, True), (122, False)]):
        out += rect(14, y - 10, 60, 18, "none", ACC, 2, 3) + text(44, y + 4, f"case {k + 1}", 11, ACC)
        if both:
            out += rect(126, y - 10, 60, 18, "none", COOL, 2, 3) + text(156, y + 4, f"case {k + 1}", 11, COOL)
            out += g("draw", line([(76, y), (124, y)], INK, 2.5), k)
    out += g("pop", text(100, 22, "same person?", 12, INK), 4)
    return out


def overlap():
    out = circle(78, 74, 46, "#FCD34D22", ACC, 3) + circle(122, 74, 46, "#7DD3FC22", COOL, 3)
    out += g("pop", text(56, 80, "12", 18, ACC), 0) + g("pop", text(100, 80, "21", 20, INK), 1)
    out += g("pop", text(144, 80, "20", 18, COOL), 2)
    out += text(100, 140, "found by both", 11, INK)
    return out


def estimate():
    out = circle(78, 66, 36, "none", ACC, 2.5) + circle(122, 66, 36, "none", COOL, 2.5)
    out += g("pop", rect(18, 18, 164, 98, "none", DIM, 2, 8, dash="5 4"), 0)
    out += g("pop", text(166, 108, "?", 22, HOT), 1)
    out += g("pop", text(100, 136, "N ≈ A × B ÷ both", 14, INK), 2)
    return out


def assume():
    # Two lists that tend to catch the same people: the overlap is too big, so N comes out too small.
    out = circle(88, 70, 44, "none", ACC, 3) + g("pop", circle(110, 70, 44, "none", COOL, 3), 0)
    out += g("draw", arrow(60, 128, 140, 128, HOT, 3), 1)
    out += g("pop", text(100, 22, "lists linked?", 12, HOT), 2)
    out += text(100, 146, "estimate too low", 11, HOT)
    return out


PICTURES = {"lists": lists, "match": match, "overlap": overlap, "estimate": estimate, "assume": assume}


def exercise(ex, quote):
    """Return (html, js). Part 1: the published counts. Part 2: a hidden example population, two lists, an estimate."""
    r = ex["real"]
    body = f"""
  <p>{e(ex["intro"])}</p>
  <h3>The published counts</h3>
  <p>{e(r["label"])}: list A found <b>{r["a"]}</b>, list B found <b>{r["b"]}</b>, both found <b>{r["both"]}</b>.
     Together they saw {r["a"] + r["b"] - r["both"]} different deaths.</p>
  <p class="verdict" id="cr-real"></p>
  <h3>Try it on a population you can check</h3>
  <div class="controls" role="group" aria-label="How the lists catch people">
    <button type="button" data-dep="0">Lists independent</button>
    <button type="button" data-dep="1">List B follows list A</button>
    <button type="button" id="cr-roll">Draw again</button> <span id="cr-seed" class="note"></span>
  </div>
  <svg id="cr-svg" viewBox="0 0 400 128" style="width:100%;max-width:560px;height:auto" role="img" aria-label="People caught by list A, list B or both"></svg>
  <p class="verdict" id="cr-verdict" aria-live="polite"></p>
  <p class="note">{e(ex["data_label"])}</p>"""
    js = RNG_JS + "const X = " + json.dumps(ex) + ";\n" + r"""
// Lincoln-Petersen in the form the paper gives: N = (A+1)(B+1)/(both+1) - 1.
const lp = (a, b, m) => (a + 1) * (b + 1) / (m + 1) - 1;
$("cr-real").textContent = `Estimated total: (${X.real.a}+1) × (${X.real.b}+1) ÷ (${X.real.both}+1) − 1 = ${Math.round(lp(X.real.a, X.real.b, X.real.both))}. So about ${Math.round(lp(X.real.a, X.real.b, X.real.both)) - (X.real.a + X.real.b - X.real.both)} deaths were missed by both lists.`;
let dep = 0, seed = 1;
function draw() {
  const r = rng(seed), N = X.population;
  // Each person is caught by A with chance pA. B catches independently with pB, or, when linked, more often those A caught.
  const ppl = Array.from({ length: N }, () => {
    const a = r() < X.pA;
    const pb = dep ? (a ? X.pB_if_A : X.pB_if_not_A) : X.pB;
    return [a, r() < pb];
  });
  const A = ppl.filter(p => p[0]).length, B = ppl.filter(p => p[1]).length, M = ppl.filter(p => p[0] && p[1]).length;
  let s = "";
  ppl.forEach((p, i) => {
    const x = 10 + (i % 40) * 9.6, y = 12 + Math.floor(i / 40) * 12;
    const c = p[0] && p[1] ? "currentColor" : p[0] ? "#B45309" : p[1] ? "#0369A1" : "none";
    s += `<circle cx="${x}" cy="${y}" r="3.6" fill="${c}" stroke="currentColor" stroke-opacity=".35"/>`;
  });
  $("cr-svg").innerHTML = s;
  const est = Math.round(lp(A, B, M));
  $("cr-verdict").textContent = `Truth: ${N} people. List A caught ${A}, list B ${B}, both ${M}; they saw ${A + B - M}. Estimate: ${est}` +
    (dep ? ` — too low, because the lists catch the same people more often than chance.` : `, close to the truth.`);
  $("cr-seed").textContent = `Draw ${seed}`;
  document.querySelectorAll("[data-dep]").forEach(b => b.setAttribute("aria-pressed", +b.dataset.dep === dep));
}
document.querySelectorAll("[data-dep]").forEach(b => b.onclick = () => { dep = +b.dataset.dep; draw(); });
$("cr-roll").onclick = () => { seed++; draw(); };
draw();
"""
    return body, js
