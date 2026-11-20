"""Systematic review & meta-analysis: the six steps' pictures (after PRISMA 2020) and the "pool a forest plot" exercise."""
import html
import json

from learn_pics._kit import INK, DIM, ACC, HOT, COOL, g, rect, text, arrow, line, circle, path, doc, RNG_JS
from art import magnifier, check, cross

e = html.escape


def protocol():
    # The plan is written and registered before the search: a dated, numbered protocol.
    out = doc(52, 18, 70, 92, INK, 0, "#0f172a", 3)
    for k, lab in enumerate(("question", "criteria", "search", "analysis")):
        out += g("draw", text(64, 40 + k * 18, "•", 12, ACC, "start") + text(74, 40 + k * 18, lab, 11, INK, "start"), k)
    out += g("pop", rect(118, 92, 62, 26, "#0f172a", ACC, 2.5, 4) + text(149, 109, "registered", 11, ACC), 4)
    return out + text(87, 134, "before searching", 11, DIM)


def search():
    # Every database, register and other source, with its date.
    out = ""
    for k, (x, lab) in enumerate(((34, "database"), (100, "register"), (166, "lists"))):
        out += g("pop", path(f"M{x - 20},34 a20,7 0 0 0 40,0 a20,7 0 0 0 -40,0 V66 a20,7 0 0 0 40,0 V34", INK, 2.5, fill="#0f172a66")
                 + text(x, 90, lab, 11, INK), k)
        out += g("draw", arrow(x, 96, 100, 116, DIM, 1.5, head=5), 3)
    return out + g("pop", text(100, 134, "all of them, dated", 12, ACC), 4)


def screen():
    # A PRISMA-style flow: many records in, few studies out, each exclusion counted.
    out = ""
    for k, (w, n) in enumerate(((150, "1,240 records"), (110, "86 full texts"), (60, "12 studies"))):
        y = 18 + k * 44
        out += g("pop", rect(100 - w / 2 - 10, y, w, 26, "#0f172a66", ACC if k == 2 else INK, 2.5, 4) + text(100 - 10, y + 17, n, 12, ACC if k == 2 else INK), 2 * k)
        if k < 2:
            out += g("draw", arrow(90, y + 28, 90, y + 42, INK, 2, head=5) + arrow(120, y + 34, 160, y + 34, HOT, 2, head=5), 2 * k + 1)
    return out + text(178, 66, "out", 11, HOT) + text(178, 110, "out", 11, HOT)


def appraise():
    # Each study judged for risk of bias, domain by domain.
    out = text(30, 22, "study", 11, DIM)
    doms = ("D1", "D2", "D3", "D4")
    out += "".join(text(80 + k * 30, 22, d, 11, DIM) for k, d in enumerate(doms))
    grid = (("+", "+", "?", "+"), ("+", "-", "+", "+"), ("?", "+", "+", "-"), ("+", "+", "+", "+"))
    for r, row in enumerate(grid):
        y = 42 + r * 24
        out += text(30, y + 4, f"S{r + 1}", 12, INK)
        for k, v in enumerate(row):
            c = {"+": "#86EFAC", "-": HOT, "?": ACC}[v]
            out += g("pop", circle(80 + k * 30, y, 9, c) + text(80 + k * 30, y + 5, v, 13, "#0f172a"), r * 4 + k)
    return out + text(100, 144, "risk of bias", 11, ACC)


def pool():
    # A forest plot: each study's estimate and interval, and the pooled diamond.
    out = line([(110, 14), (110, 128)], DIM, 2, "3 3")
    for k, (c, lo, hi, s) in enumerate(((90, 64, 116, 5), (98, 80, 116, 6), (106, 94, 118, 8), (114, 98, 130, 7), (80, 44, 116, 4))):
        y = 22 + k * 18
        out += g("pop", line([(lo, y), (hi, y)], INK, 2) + rect(c - s / 2, y - s / 2, s, s, INK, INK, 0, 1), k)
    out += g("pop", path("M84,122 L100,114 L116,122 L100,130 Z", ACC, 2, fill=ACC), 5)
    return out + text(48, 126, "pooled", 12, ACC) + text(150, 40, "favours", 11, DIM) + text(150, 54, "control", 11, DIM)


def certainty():
    # Missing studies and certainty: a funnel plot with an empty corner.
    out = line([(100, 16), (40, 124)], DIM, 2, "4 3") + line([(100, 16), (160, 124)], DIM, 2, "4 3") + line([(100, 16), (100, 124)], DIM, 1.5)
    pts = [(96, 30), (104, 36), (92, 50), (110, 56), (86, 74), (114, 70), (78, 96), (70, 110), (90, 104)]
    out += "".join(g("pop", circle(x, y, 4, INK), k) for k, (x, y) in enumerate(pts))
    out += g("pop", circle(126, 98, 4, "none", HOT, 2, dash="2 2") + circle(136, 112, 4, "none", HOT, 2, dash="2 2"), 9)
    return out + g("pop", text(150, 142, "missing?", 12, HOT), 10) + text(46, 142, "small studies", 11, DIM)


PICTURES = {"protocol": protocol, "search": search, "screen": screen, "appraise": appraise, "pool": pool, "certainty": certainty}


def exercise(ex, quote):
    """Return (html, js). Example studies on a forest plot: pool them fixed or random, and hide the null ones."""
    body = f"""
  <p>{e(ex["intro"])}</p>
  <div class="controls" role="group" aria-label="Model">
    <button type="button" data-model="fixed">Fixed effect</button>
    <button type="button" data-model="random">Random effects</button>
    <button type="button" id="drawer" aria-pressed="false">Leave the null studies in the drawer</button>
  </div>
  <svg id="forest" viewBox="0 0 520 300" role="img" aria-label="Forest plot" style="width:100%;max-width:720px;display:block"></svg>
  <p class="verdict" id="verdict" aria-live="polite"></p>
  <p class="note">{e(ex["data_label"])} {e(ex["method_note"])}</p>"""
    js = RNG_JS + "const X = " + json.dumps(ex) + ";\n" + r"""
let model = "fixed", drawer = false;
function pooled(ss) {
  const w = ss.map(s => 1 / (s.se * s.se)), W = w.reduce((a, b) => a + b, 0);
  const fe = ss.reduce((a, s, i) => a + w[i] * s.y, 0) / W;
  const Q = ss.reduce((a, s, i) => a + w[i] * (s.y - fe) ** 2, 0), df = ss.length - 1;
  const C = W - w.reduce((a, b) => a + b * b, 0) / W, tau2 = Math.max(0, (Q - df) / C);
  const I2 = Q > 0 ? Math.max(0, (Q - df) / Q) : 0;
  if (model === "fixed") return { y: fe, se: Math.sqrt(1 / W), I2, tau2, w: w.map(x => x / W) };
  const ws = ss.map(s => 1 / (s.se * s.se + tau2)), Ws = ws.reduce((a, b) => a + b, 0);
  return { y: ss.reduce((a, s, i) => a + ws[i] * s.y, 0) / Ws, se: Math.sqrt(1 / Ws), I2, tau2, w: ws.map(x => x / Ws) };
}
const lo = Math.log(0.25), hi = Math.log(2.5), sx = v => 170 + (Math.min(hi, Math.max(lo, v)) - lo) / (hi - lo) * 330;
const f2 = v => Math.exp(v).toFixed(2);
function draw() {
  const ss = X.studies.filter(s => !drawer || Math.abs(s.y / s.se) >= 1.96), p = pooled(ss), svg = [];
  svg.push(`<line x1="${sx(0)}" y1="10" x2="${sx(0)}" y2="270" stroke="currentColor" stroke-opacity=".4" stroke-dasharray="4 3"/>`);
  for (const t of [0.25, 0.5, 1, 2]) svg.push(`<text x="${sx(Math.log(t))}" y="292" text-anchor="middle" font-size="12" fill="currentColor">${t}</text>`);
  X.studies.forEach((s, i) => {
    const y = 24 + i * 28, hidden = !ss.includes(s), k = ss.indexOf(s);
    const op = hidden ? .2 : 1, size = hidden ? 6 : 4 + 22 * p.w[k];
    svg.push(`<g opacity="${op}"><text x="4" y="${y + 4}" font-size="13" fill="currentColor">${s.name}</text>
      <text x="96" y="${y + 4}" font-size="12" fill="currentColor">${f2(s.y)} [${f2(s.y - 1.96 * s.se)}, ${f2(s.y + 1.96 * s.se)}]</text>
      <line x1="${sx(s.y - 1.96 * s.se)}" y1="${y}" x2="${sx(s.y + 1.96 * s.se)}" y2="${y}" stroke="currentColor" stroke-width="2"/>
      <rect x="${sx(s.y) - size / 2}" y="${y - size / 2}" width="${size}" height="${size}" fill="currentColor"/></g>`);
  });
  const y = 24 + X.studies.length * 28 + 6, a = sx(p.y - 1.96 * p.se), b = sx(p.y + 1.96 * p.se), c = sx(p.y);
  svg.push(`<text x="4" y="${y + 4}" font-size="13" font-weight="700" fill="currentColor">Pooled</text>
    <text x="96" y="${y + 4}" font-size="12" font-weight="700" fill="currentColor">${f2(p.y)} [${f2(p.y - 1.96 * p.se)}, ${f2(p.y + 1.96 * p.se)}]</text>
    <path d="M${a},${y} L${c},${y - 8} L${b},${y} L${c},${y + 8} Z" fill="#B45309"/>`);
  $("forest").innerHTML = svg.join("");
  $("verdict").textContent = `${ss.length} studies, ${model === "fixed" ? "fixed-effect" : "random-effects"} pooled risk ratio ${f2(p.y)} ` +
    `(95% CI ${f2(p.y - 1.96 * p.se)} to ${f2(p.y + 1.96 * p.se)}); I² = ${Math.round(100 * p.I2)}%.` +
    (drawer ? " Only the 'significant' studies were published: the pooled effect looks stronger than the full evidence." : "");
  document.querySelectorAll("[data-model]").forEach(x => x.setAttribute("aria-pressed", x.dataset.model === model));
  $("drawer").setAttribute("aria-pressed", drawer);
}
document.querySelectorAll("[data-model]").forEach(x => x.onclick = () => { model = x.dataset.model; draw(); });
$("drawer").onclick = () => { drawer = !drawer; draw(); };
draw();
"""
    return body, js
