"""Randomized controlled trial: the five steps' pictures and the "chance or a doctor" exercise."""
import html
import json

from learn_pics._kit import (INK, DIM, ACC, HOT, TREAT, CONTROL, g, pill, person, rect, text, arrow, line, dice, RNG_JS)

e = html.escape


def enrol():
    out = rect(118, 30, 66, 92, "none", DIM, 2, 6) + text(151, 24, "ENROLLED", 12, INK)
    spots = [(130, 54), (150, 54), (170, 54), (130, 82), (150, 82), (170, 82), (140, 110), (160, 110)]
    # Eight fit and step into the box; four don't and stay outside, counted.
    out += "".join(g("pop", person(x, y, 0.8, INK), i) for i, (x, y) in enumerate(spots))
    out += "".join(g("pop", person(x, y, 0.8, DIM), 8 + i) for i, (x, y) in enumerate([(30, 50), (54, 50), (30, 96), (54, 96)]))
    out += text(42, 132, "not eligible", 11, DIM) + arrow(72, 76, 108, 76, INK, 2.5)
    return out


def allocate():
    out = g("roll", dice(44, 75, 38, 5))
    out += text(44, 124, "CHANCE", 12, INK)
    out += g("draw", arrow(70, 66, 112, 40, INK, 2.5), 1) + g("draw", arrow(70, 84, 112, 110, INK, 2.5), 1)
    for k in range(4):
        out += g("pop", person(126 + k * 18, 40, 0.75, TREAT), 2 + 2 * k)
        out += g("pop", person(126 + k * 18, 110, 0.75, CONTROL), 3 + 2 * k)
    out += text(153, 70, "intervention", 11, TREAT) + text(153, 140, "control", 11, CONTROL)
    return out


def treat():
    out = ""
    for k in range(3):
        out += person(30 + k * 20, 46, 0.75, TREAT) + person(30 + k * 20, 112, 0.75, CONTROL)
    out += g("pop", pill(120, 44, ACC), 1) + g("pop", pill(120, 110, INK), 2)
    out += g("pop", text(165, 49, "drug", 13, TREAT), 3) + g("pop", text(165, 115, "placebo", 13, CONTROL), 4)
    out += g("pop", text(100, 82, "look the same", 11, DIM), 5)
    return out


def follow():
    out = ""
    for row, c in ((40, TREAT), (106, CONTROL)):
        out += line([(20, row + 14), (186, row + 14)], DIM, 2)
        for k in range(4):
            out += person(30 + k * 16, row, 0.7, c)
        out += g("draw", arrow(100, row + 2, 176, row + 2, c, 2.5), 0)
    # One person per arm drops out: they fade, but stay in the count.
    out += g("fade", person(78, 40, 0.7, TREAT), 2) + g("fade", person(62, 106, 0.7, CONTROL), 3)
    out += text(140, 74, "time", 11, DIM) + text(140, 140, "who left, and why?", 11, HOT)
    return out


def compare():
    base = 126
    out = line([(30, base), (176, base)], DIM, 2)
    out += g("grow", rect(52, base - 38, 36, 38, TREAT, "none", 0, 3), 0)
    out += g("grow", rect(118, base - 82, 36, 82, CONTROL, "none", 0, 3), 1)
    out += text(70, base + 16, "intervention", 11, TREAT) + text(136, base + 16, "control", 11, CONTROL)
    out += g("pop", line([(92, base - 38), (162, base - 38)], INK, 1.5, dash="3 3")
             + arrow(170, base - 40, 170, base - 80, HOT, 2.5, head=6) + arrow(170, base - 80, 170, base - 40, HOT, 2.5, head=6), 2)
    out += g("pop", text(100, 22, "effect = difference", 13, HOT), 3)
    return out


PICTURES = {"enrol": enrol, "allocate": allocate, "treat": treat, "follow": follow, "compare": compare}


def exercise(ex, quote):
    """Return (html, js). Example patients: severity hidden; a doctor or chance splits them; the arms are compared."""
    size_opts = "".join(f'<option value="{s}"{" selected" if s == ex["sizes"][1] else ""}>{s} patients</option>' for s in ex["sizes"])
    body = f"""
  <p>{e(ex["intro"])}</p>
  <div class="controls" role="group" aria-label="Who decides">
    <button type="button" data-mode="doctor">A doctor chooses</button>
    <button type="button" data-mode="die">Chance chooses</button>
    <button type="button" id="roll">Roll again</button> <span id="seed" class="note"></span>
    <label class="note">Trial size <select id="size">{size_opts}</select></label>
  </div>
  <div class="arms" aria-live="polite">
    <div class="arm"><h3 style="color:#B45309">Intervention arm</h3><div class="dots" id="t-dots"></div>
      <p><span class="share" id="t-share"></span> <span id="t-n" class="note"></span></p><div class="bar"><span id="t-bar"></span></div></div>
    <div class="arm"><h3 style="color:#0369A1">Control arm</h3><div class="dots" id="c-dots"></div>
      <p><span class="share" id="c-share"></span> <span id="c-n" class="note"></span></p><div class="bar"><span id="c-bar"></span></div></div>
  </div>
  <p class="verdict" id="verdict"></p>
  <p class="note">{e(ex["data_label"])} {e(ex["doctor_rule"])}</p>"""
    js = RNG_JS + "const X = " + json.dumps(ex) + ";\n" + r"""
let mode = "die", n = X.sizes[1], seed = 1;
function patients() { const r = rng(1000 + n); return Array.from({ length: n }, () => r() < X.severe_share); }
function split(ps) {
  if (mode === "doctor") {
    // The doctor gives the new treatment to the patients who look most likely to recover. Severity shows only partly,
    // so the doctor's impression is severity plus seeded noise, not severity itself.
    const r = rng(7), look = ps.map(s => (s ? 1 : 0) + 2.5 * r());
    const order = ps.map((_, i) => [look[i], i]).sort((a, b) => a[0] - b[0] || a[1] - b[1]);
    const t = new Set(order.slice(0, n / 2).map(x => x[1]));
    return ps.map((_, i) => t.has(i));
  }
  const r = rng(seed), idx = ps.map((_, i) => i);
  for (let i = idx.length - 1; i > 0; i--) { const j = Math.floor(r() * (i + 1)); [idx[i], idx[j]] = [idx[j], idx[i]]; }
  const t = new Set(idx.slice(0, n / 2)); return ps.map((_, i) => t.has(i));
}
// One roll can be unlucky; the average gap over many seeded rolls shows the rule: it shrinks as the trial grows.
function typicalGap(ps) {
  let sum = 0; const keep = seed;
  for (seed = 1; seed <= 200; seed++) {
    const inT = split(ps), sev = want => ps.filter((s, i) => s && inT[i] === want).length / (n / 2);
    sum += Math.abs(sev(true) - sev(false));
  }
  seed = keep; return Math.round(100 * sum / 200);
}
function draw() {
  const ps = patients(), inT = split(ps);
  const arm = want => ps.filter((_, i) => inT[i] === want);
  for (const [key, list] of [["t", arm(true)], ["c", arm(false)]]) {
    const sev = list.filter(Boolean).length, pct = Math.round(100 * sev / list.length);
    $(key + "-dots").innerHTML = n <= 100 ? list.map(s => `<span class="dot${s ? " sev" : ""}"></span>`).join("") : "";
    $(key + "-share").textContent = pct + "%";
    $(key + "-bar").style.width = pct + "%";
    $(key + "-n").textContent = `${sev} of ${list.length} severely ill`;
  }
  const a = arm(true).filter(Boolean).length / (n / 2), b = arm(false).filter(Boolean).length / (n / 2);
  const gap = Math.round(100 * Math.abs(a - b));
  $("verdict").textContent = mode === "doctor"
    ? `The arms differ by ${gap} points before anyone is treated. Any difference at the end mixes the drug's effect with this one.`
    : `The arms differ by ${gap} points, by chance alone. Over 200 rolls of a trial this size they differ by ${typicalGap(ps)} points on average; make the trial bigger and that shrinks.`;
  $("seed").textContent = mode === "die" ? `Roll ${seed}` : "";
  $("roll").hidden = mode !== "die";
  document.querySelectorAll("[data-mode]").forEach(b => b.setAttribute("aria-pressed", b.dataset.mode === mode));
}
document.querySelectorAll("[data-mode]").forEach(b => b.onclick = () => { mode = b.dataset.mode; draw(); });
$("roll").onclick = () => { seed++; draw(); };
$("size").onchange = ev => { n = +ev.target.value; draw(); };
draw();
"""
    return body, js
