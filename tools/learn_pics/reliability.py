"""Reliability and agreement study: the six steps' pictures and the "correlation fools you" exercise."""
import html
import json

from learn_pics._kit import INK, DIM, ACC, HOT, COOL, g, person, rect, text, arrow, line, circle, RNG_JS

e = html.escape

PTS = [(40, 112), (58, 100), (70, 96), (86, 82), (100, 80), (114, 64), (128, 62), (142, 48), (156, 44), (170, 30)]


def measure():
    out = ""
    for k in range(3):
        out += person(40 + k * 60, 96, 0.8, INK)
        out += g("pop", rect(28 + k * 60, 40, 22, 16, "none", ACC, 2, 3), 2 * k) + g("pop", rect(28 + k * 60, 60, 22, 16, "none", COOL, 2, 3), 2 * k + 1)
    out += text(60, 30, "method A", 11, ACC) + text(150, 30, "method B", 11, COOL)
    out += text(100, 138, "same people, both", 12, INK)
    return out


def equality():
    out = line([(30, 126), (184, 126)], DIM, 2) + line([(30, 126), (30, 18)], DIM, 2)
    out += g("draw", line([(30, 126), (180, 22)], ACC, 2, dash="4 3"), 0) + g("pop", text(150, 22, "equality", 11, ACC), 1)
    out += "".join(g("pop", circle(x, y + 6, 3.2, INK), 2 + i // 3) for i, (x, y) in enumerate(PTS))
    out += text(108, 142, "method A", 11, DIM) + text(14, 70, "B", 11, DIM)
    return out


def not_r():
    out = line([(30, 126), (184, 126)], DIM, 2) + line([(30, 126), (30, 18)], DIM, 2)
    out += line([(30, 126), (180, 51)], ACC, 2, dash="4 3") + text(166, 66, "equality", 11, ACC)
    # B reads twice A: a perfect straight line, r = 1, yet no agreement at all.
    out += "".join(g("pop", circle(30 + k * 16, 126 - k * 16, 3.2, HOT), k) for k in range(1, 7))
    out += g("pop", text(140, 30, "r = 1, B = 2 × A", 12, HOT), 7)
    out += text(108, 142, "perfect r, poor agreement", 11, INK)
    return out


def difference():
    out = line([(24, 76), (186, 76)], DIM, 1.5, dash="3 3") + text(176, 70, "0", 11, DIM)
    out += g("draw", line([(24, 66), (186, 66)], ACC, 2.5), 0) + g("pop", text(42, 60, "bias", 11, ACC), 1)
    out += g("draw", line([(24, 32), (186, 32)], HOT, 2, dash="5 3") + line([(24, 100), (186, 100)], HOT, 2, dash="5 3"), 2)
    out += g("pop", text(100, 26, "limits of agreement", 11, HOT), 3)
    ds = [52, 80, 60, 44, 74, 90, 58, 70, 40, 64]
    out += "".join(g("pop", circle(36 + i * 15, d, 3.2, INK), 4 + i // 4) for i, d in enumerate(ds))
    out += text(100, 128, "mean of the pair", 11, DIM) + text(100, 142, "difference vs mean", 12, INK)
    return out


def judge():
    out = line([(20, 70), (180, 70)], DIM, 2)
    out += g("grow", rect(52, 58, 96, 24, "none", HOT, 2.5, 4), 0) + text(100, 52, "limits", 11, HOT)
    out += g("pop", rect(76, 92, 48, 18, "none", "#86EFAC", 2.5, 4), 1) + g("pop", text(100, 126, "what matters clinically", 11, "#86EFAC"), 2)
    out += g("pop", text(100, 28, "wider than this?", 13, INK), 3)
    return out


def repeat():
    out = person(40, 80, 0.9, INK)
    for k, (y, c) in enumerate(((44, ACC), (66, ACC), (96, COOL), (118, COOL))):
        out += g("draw", arrow(56, 80, 96, y, c, 2), k) + g("pop", circle(110, y, 5, c), k)
    out += text(150, 58, "A again", 12, ACC) + text(150, 112, "B again", 12, COOL)
    out += text(100, 142, "self-agreement first", 11, INK)
    return out


PICTURES = {"measure": measure, "equality": equality, "not_r": not_r, "difference": difference, "judge": judge, "repeat": repeat}


def exercise(ex, quote):
    """Return (html, js). Example pairs; the range of true values changes; r and the limits of agreement are shown."""
    opts = "".join(f'<button type="button" data-range="{r}">Range {r}</button>' for r in ex["ranges"])
    body = f"""
  <p>{e(ex["intro"])}</p>
  <div class="controls" role="group" aria-label="Range of true values">{opts}</div>
  <div class="arms">
    <div class="arm"><h3>Method B against A</h3><svg id="sc" viewBox="0 0 220 220" style="width:100%;max-width:300px" role="img" aria-label="Scatter of B against A with the line of equality"></svg>
      <p><span class="share" id="r"></span> correlation</p></div>
    <div class="arm"><h3>Difference against mean</h3><svg id="ba" viewBox="0 0 220 220" style="width:100%;max-width:300px" role="img" aria-label="Differences against means with bias and limits of agreement"></svg>
      <p><span class="share" id="loa"></span> limits of agreement</p></div>
  </div>
  <p class="verdict" id="verdict"></p>
  <p class="note">{e(ex["data_label"])}</p>"""
    js = RNG_JS + "const X = " + json.dumps(ex) + ";\n" + r"""
let range = X.ranges[1];
function data() { const r = rng(21), out = [];
  for (let i = 0; i < X.n; i++) { const t = X.centre - range / 2 + range * r();
    const u = 1 - r(), v = r(), z = Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * v);
    out.push([t, t + X.bias + X.sd * z]); } return out; }
function draw() {
  const d = data(), n = d.length, ma = d.reduce((s, p) => s + p[0], 0) / n, mb = d.reduce((s, p) => s + p[1], 0) / n;
  let sab = 0, saa = 0, sbb = 0; d.forEach(([a, b]) => { sab += (a - ma) * (b - mb); saa += (a - ma) ** 2; sbb += (b - mb) ** 2; });
  const r = sab / Math.sqrt(saa * sbb), diffs = d.map(([a, b]) => b - a), md = diffs.reduce((s, x) => s + x, 0) / n;
  const sd = Math.sqrt(diffs.reduce((s, x) => s + (x - md) ** 2, 0) / (n - 1)), lo = md - 2 * sd, hi = md + 2 * sd;
  const lo0 = X.centre - 260, hi0 = X.centre + 260, sx = v => 10 + 200 * (v - lo0) / (hi0 - lo0), sy = v => 210 - 200 * (v - lo0) / (hi0 - lo0);
  let s = `<line x1="${sx(lo0)}" y1="${sy(lo0)}" x2="${sx(hi0)}" y2="${sy(hi0)}" stroke="#B45309" stroke-dasharray="4 3"/>`;
  d.forEach(([a, b]) => s += `<circle cx="${sx(a)}" cy="${sy(b)}" r="3" fill="currentColor"/>`);
  $("sc").innerHTML = s;
  const dy = v => 110 - 200 * v / 260;
  let t = `<line x1="10" y1="${dy(0)}" x2="210" y2="${dy(0)}" stroke="currentColor" opacity=".3"/>`;
  t += `<line x1="10" y1="${dy(md)}" x2="210" y2="${dy(md)}" stroke="#B45309" stroke-width="2"/>`;
  for (const v of [lo, hi]) t += `<line x1="10" y1="${dy(v)}" x2="210" y2="${dy(v)}" stroke="#E11D48" stroke-dasharray="5 3" stroke-width="2"/>`;
  d.forEach(([a, b]) => t += `<circle cx="${sx((a + b) / 2)}" cy="${dy(b - a)}" r="3" fill="currentColor"/>`);
  $("ba").innerHTML = t;
  $("r").textContent = r.toFixed(2);
  $("loa").textContent = `${Math.round(lo)} to ${Math.round(hi)}`;
  $("verdict").textContent = `Range ${range}: r = ${r.toFixed(2)}. The meters disagree by the same amount at every range; only the correlation changed.`;
  document.querySelectorAll("[data-range]").forEach(b => b.setAttribute("aria-pressed", +b.dataset.range === range));
}
document.querySelectorAll("[data-range]").forEach(b => b.onclick = () => { range = +b.dataset.range; draw(); });
draw();
"""
    return body, js
