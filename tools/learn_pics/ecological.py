"""Ecological study: the five steps' pictures and the "regions or people" exercise (the ecological fallacy)."""
import html
import json

from learn_pics._kit import INK, DIM, ACC, HOT, COOL, g, person, rect, text, arrow, line, circle, RNG_JS
from art import axes, globe

e = html.escape


def groups():
    out = ""
    for k, (x, y) in enumerate([(40, 44), (100, 44), (160, 44), (70, 104), (130, 104)]):
        out += g("pop", circle(x, y, 22, "none", INK, 2.5) + "".join(
            circle(x + dx, y + dy, 2.2, DIM) for dx, dy in ((-8, -6), (6, -8), (0, 2), (-6, 9), (8, 7))), k)
    out += text(100, 144, "regions, not people", 11, ACC)
    return out


def aggregate():
    out = circle(46, 72, 34, "none", INK, 2.5) + "".join(
        circle(46 + dx, 72 + dy, 2.6, DIM) for dx, dy in ((-14, -10), (10, -14), (0, 0), (-12, 14), (14, 10), (2, -22), (-20, 2)))
    out += g("draw", arrow(86, 72, 118, 72, ACC, 3), 0)
    out += g("pop", rect(124, 50, 66, 44, "none", ACC, 2.5, 6), 1)
    out += g("pop", text(157, 78, "rate 12%", 15, ACC), 2)
    out += text(46, 130, "many people", 11, DIM) + text(157, 116, "one number", 11, INK)
    return out


def place_time():
    out = globe(52, 66, 28) + text(52, 120, "by place", 12, INK)
    out += g("pop", axes(110, 40, 76, 60), 1)
    out += g("draw", line([(116, 90), (132, 82), (148, 84), (164, 66), (180, 58)], ACC, 3), 2)
    out += text(148, 120, "by time", 12, INK)
    return out


def correlate():
    out = axes(18, 14, 172, 118)
    pts = [(42, 112), (70, 100), (98, 82), (126, 72), (154, 54), (178, 38)]
    out += "".join(g("pop", circle(x, y, 7, "none", ACC, 2.5), k) for k, (x, y) in enumerate(pts))
    out += g("draw", line([(30, 120), (184, 32)], INK, 2.5, "6 5"), 6)
    out += text(110, 146, "group exposure", 11, DIM)
    return out


def leap():
    # The group line rises; inside each group the people's line falls.
    out = line([(24, 118), (182, 34)], DIM, 2.5, "6 5")
    for k, (cx, cy) in enumerate([(50, 104), (102, 76), (154, 48)]):
        out += circle(cx, cy, 20, "none", INK, 2)
        out += g("draw", arrow(cx - 16, cy - 10, cx + 16, cy + 10, HOT, 2.5, head=6), k)
    out += g("pop", text(100, 140, "people may differ", 12, HOT), 3)
    out += text(150, 22, "groups", 11, DIM)
    return out


PICTURES = {"groups": groups, "aggregate": aggregate, "place_time": place_time, "correlate": correlate, "leap": leap}


def exercise(ex, quote):
    """Return (html, js). Example regions whose averages rise together while, inside each region, people's values fall."""
    body = f"""
  <p>{e(ex["intro"])}</p>
  <div class="controls" role="group" aria-label="What to show">
    <button type="button" data-view="groups">Regions only</button>
    <button type="button" data-view="people">Show the people</button>
  </div>
  <svg id="eco" viewBox="0 0 400 260" style="width:100%;max-width:560px;height:auto" role="img" aria-label="Scatter plot of regions and people"></svg>
  <p class="verdict" id="eco-verdict" aria-live="polite"></p>
  <p class="note">{e(ex["data_label"])}</p>"""
    js = RNG_JS + "const X = " + json.dumps(ex) + ";\n" + r"""
let view = "groups";
// Each region: its own average exposure and outcome; inside it, people with more exposure have less outcome.
const r = rng(X.seed), regions = X.regions.map((g, k) => {
  const people = Array.from({ length: X.per_region }, () => {
    const dx = (r() - 0.5) * 2 * X.spread, noise = (r() - 0.5) * X.noise;
    return [g[0] + dx, g[1] + X.within_slope * dx + noise];
  });
  return { mx: g[0], my: g[1], people };
});
function slope(pts) {
  const n = pts.length, mx = pts.reduce((s, p) => s + p[0], 0) / n, my = pts.reduce((s, p) => s + p[1], 0) / n;
  let sxy = 0, sxx = 0; for (const [x, y] of pts) { sxy += (x - mx) * (y - my); sxx += (x - mx) ** 2; }
  return sxy / sxx;
}
const W = 400, H = 260, L = 44, B = 224, sx = x => L + (x / 100) * (W - L - 14), sy = y => B - (y / 100) * (B - 14);
function draw() {
  let s = `<line x1="${L}" y1="${B}" x2="${W - 10}" y2="${B}" stroke="currentColor" opacity=".5"/><line x1="${L}" y1="${B}" x2="${L}" y2="10" stroke="currentColor" opacity=".5"/>`;
  s += `<text x="${(W + L) / 2}" y="${H - 8}" font-size="13" text-anchor="middle" fill="currentColor">exposure</text>`;
  s += `<text x="14" y="${B / 2}" font-size="13" text-anchor="middle" fill="currentColor" transform="rotate(-90 14 ${B / 2})">outcome</text>`;
  const cols = ["#B45309", "#0369A1", "#7C3AED", "#BE123C", "#047857"];
  regions.forEach((g, k) => {
    if (view === "people") for (const [x, y] of g.people) s += `<circle cx="${sx(x)}" cy="${sy(y)}" r="3" fill="${cols[k]}" opacity=".6"/>`;
    s += `<circle cx="${sx(g.mx)}" cy="${sy(g.my)}" r="9" fill="none" stroke="${cols[k]}" stroke-width="3"/>`;
  });
  $("eco").innerHTML = s;
  const gs = slope(regions.map(g => [g.mx, g.my]));
  const ws = regions.map(g => slope(g.people)).reduce((a, b) => a + b, 0) / regions.length;
  $("eco-verdict").textContent = view === "groups"
    ? `Across the ${regions.length} regions, outcome rises by ${gs.toFixed(2)} for each unit of exposure. It is tempting to say the same of each person.`
    : `Inside the regions, outcome falls by ${Math.abs(ws).toFixed(2)} per unit of exposure, on average. The regions' line said the opposite: the data on regions alone could not tell.`;
  document.querySelectorAll("[data-view]").forEach(b => b.setAttribute("aria-pressed", b.dataset.view === view));
}
document.querySelectorAll("[data-view]").forEach(b => b.onclick = () => { view = b.dataset.view; draw(); });
draw();
"""
    return body, js
