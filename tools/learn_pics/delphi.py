"""Delphi consensus: the five steps' pictures and the "rounds converge" exercise (seeded example ratings)."""
import html
import json
import math

from learn_pics._kit import INK, DIM, ACC, HOT, COOL, g, rect, text, arrow, line, circle, doc, person, RNG_JS

e = html.escape
GREEN = "#86EFAC"


def panel():
    # Experts picked against criteria set beforehand: a checklist, and the ones who meet it.
    out = rect(14, 26, 50, 66, "none", INK, 2.5, 3)
    for k in range(3):
        out += line([(22, 40 + k * 18), (28, 46 + k * 18), (36, 34 + k * 18)], GREEN, 2.5) + line([(42, 40 + k * 18), (56, 40 + k * 18)], DIM, 2)
    out += text(39, 110, "criteria", 11, INK)
    for k in range(8):
        x, y = 92 + (k % 4) * 26, 50 + (k // 4) * 50
        chosen = k in (0, 2, 3, 5, 6)
        out += g("pop", person(x, y, 0.9, ACC if chosen else DIM), k)
    out += text(131, 140, "panel", 12, ACC)
    return out


def anonymous():
    # Each expert rates alone, behind a screen: nobody sees who said what.
    out = ""
    for k, x in enumerate((36, 100, 164)):
        out += person(x, 112, 1.1, INK) + rect(x - 22, 30, 44, 50, "#0f172a44", DIM, 2, 3)
        out += g("pop", text(x, 62, "?", 22, ACC), k)
        if k < 2:
            out += line([(x + 32, 26), (x + 32, 128)], DIM, 3, dash="4 4")
    out += text(100, 142, "rated alone", 11, INK)
    return out


def feedback():
    # The organisers send back the group's spread: a dot plot with the median marked.
    out = line([(20, 96), (180, 96)], DIM, 2)
    for k in range(1, 10):
        out += text(20 + (k - 1) * 20, 114, str(k), 11, DIM)
    stacks = {3: 1, 5: 2, 6: 2, 7: 3, 8: 2, 9: 1}
    i = 0
    for v, n in stacks.items():
        for j in range(n):
            out += g("pop", circle(20 + (v - 1) * 20, 86 - j * 12, 5, ACC), i)
            i += 1
    out += g("draw", line([(140, 40), (140, 100)], GREEN, 3), i) + g("pop", text(140, 34, "median", 11, GREEN), i + 1)
    out += text(100, 138, "group feedback", 12, INK)
    return out


def rounds():
    # Round after round the ratings close in on each other.
    out = ""
    spreads = ((10, 186), (50, 160), (80, 150))
    for k, (a, b) in enumerate(spreads):
        y = 36 + k * 40
        out += text(14, y + 4, f"R{k + 1}", 11, DIM, "start")
        out += g("draw", line([(a + 24, y), (b, y)], ACC, 6, o=.85), k)
        out += circle(118, y, 4, GREEN)
    out += text(118, 142, "spread narrows", 11, GREEN)
    return out


def stop():
    # Stop when the answers no longer change between rounds, by a rule set in advance.
    out = line([(30, 116), (176, 116)], DIM, 2) + line([(30, 30), (30, 116)], DIM, 2)
    pts = [(46, 40), (82, 76), (118, 92), (154, 94)]
    out += g("draw", line(pts, ACC, 3), 0) + "".join(g("pop", circle(x, y, 5, ACC), 1 + k) for k, (x, y) in enumerate(pts))
    out += g("pop", rect(106, 78, 62, 28, "none", GREEN, 2.5, 8), 5)
    out += text(137, 64, "stable", 12, GREEN) + text(100, 136, "rounds", 11, DIM) + text(60, 24, "spread", 11, DIM)
    return out


PICTURES = {"panel": panel, "anonymous": anonymous, "feedback": feedback, "rounds": rounds, "stop": stop}


def exercise(ex, quote):
    """Return (html, js). Seeded example panel: each round every expert sees the median and may move towards it."""
    body = f"""
  <p>{e(ex["intro"])}</p>
  <div class="controls" role="group" aria-label="Rounds">
    <button type="button" id="next">Run next round</button>
    <button type="button" id="restart">Start again</button>
    <button type="button" id="panel">New example panel</button> <span id="seed" class="note"></span>
    <label class="note">Consensus when at least <select id="cut">{"".join(f'<option value="{c}"{" selected" if c == ex["cutoff"] else ""}>{c}%</option>' for c in ex["cutoffs"])}</select> rate 7–9</label>
  </div>
  <svg id="plot" viewBox="0 0 360 {40 + 34 * ex["max_rounds"]}" role="img" aria-label="Ratings per round" style="width:100%;max-width:640px;display:block"></svg>
  <p class="verdict" id="verdict" aria-live="polite"></p>
  <p class="note">{e(ex["data_label"])} {e(ex["model_note"])}</p>"""
    js = RNG_JS + "const X = " + json.dumps(ex) + ";\n" + r"""
let seed = 1, rounds = [];
const median = a => { const s = [...a].sort((x, y) => x - y), m = s.length >> 1; return s.length % 2 ? s[m] : (s[m - 1] + s[m]) / 2; };
function first() {
  const r = rng(seed);
  // Example first-round ratings on a 1-9 scale, leaning to agreement but widely spread.
  return Array.from({ length: X.panel }, () => Math.max(1, Math.min(9, Math.round(2 + 7 * Math.sqrt(r())))));
}
function next(prev) {
  const r = rng(seed * 100 + rounds.length), med = median(prev);
  // After seeing the median, each expert moves part of the way towards it; a few hold their view.
  return prev.map(v => r() < X.stubborn ? v : Math.max(1, Math.min(9, Math.round(v + (med - v) * (0.3 + 0.5 * r())))));
}
function stats(a) {
  const s = [...a].sort((x, y) => x - y), q = p => s[Math.round(p * (s.length - 1))];
  return { med: median(a), iqr: q(0.75) - q(0.25), agree: Math.round(100 * a.filter(v => v >= 7).length / a.length) };
}
function draw() {
  const cut = +$("cut").value, W = 360, x = v => 30 + (v - 1) * 38;
  let svg = "";
  for (let v = 1; v <= 9; v++) svg += `<text x="${x(v)}" y="18" font-size="11" text-anchor="middle" fill="currentColor">${v}</text>`;
  svg += `<rect x="${x(7) - 16}" y="24" width="${x(9) - x(7) + 32}" height="${34 * X.max_rounds}" fill="#86EFAC" opacity=".15"/>`;
  rounds.forEach((a, k) => {
    const y = 44 + 34 * k, count = {};
    svg += `<text x="4" y="${y + 4}" font-size="11" fill="currentColor">R${k + 1}</text>`;
    a.forEach(v => { const j = count[v] = (count[v] || 0) + 1; svg += `<circle cx="${x(v) - 14 + 4 * ((j - 1) % 8)}" cy="${y + 3 * Math.floor((j - 1) / 8)}" r="3" fill="#6D28D9"/>`; });
    const m = stats(a).med; svg += `<line x1="${x(m)}" x2="${x(m)}" y1="${y - 10}" y2="${y + 10}" stroke="#047857" stroke-width="3"/>`;
  });
  $("plot").innerHTML = svg;
  const s = stats(rounds[rounds.length - 1]), prev = rounds.length > 1 ? stats(rounds[rounds.length - 2]) : null;
  // Two rounds cannot show stability (Nasa et al. 2021, "Closing criteria"), so it is judged from the third round on.
  const stable = rounds.length >= 3 && prev && Math.abs(prev.agree - s.agree) <= X.stable_points && prev.iqr === s.iqr;
  $("verdict").textContent = `Round ${rounds.length}: median ${s.med}, interquartile range ${s.iqr}, ${s.agree}% rate 7–9. `
    + (s.agree >= cut ? "Consensus by the rule you set. " : "No consensus yet by that rule. ")
    + (stable ? "Answers barely changed from the last round: stable, so stop." : rounds.length >= X.max_rounds ? "Last round reached." : "Not yet stable: run another round.");
  $("next").disabled = rounds.length >= X.max_rounds || stable;
  $("seed").textContent = `Panel ${seed}`;
}
function restart() { rounds = [first()]; draw(); }
$("next").onclick = () => { rounds.push(next(rounds[rounds.length - 1])); draw(); };
$("restart").onclick = restart;
$("panel").onclick = () => { seed++; restart(); };
$("cut").onchange = draw;
restart();
"""
    return body, js
