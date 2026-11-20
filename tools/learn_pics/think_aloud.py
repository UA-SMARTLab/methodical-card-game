"""Usability test (think-aloud): the five steps' pictures and the "how many users" exercise."""
import html
import json

from learn_pics._kit import INK, DIM, ACC, HOT, COOL, g, person, rect, text, arrow, line, circle, RNG_JS
from art import bubble, cross, doc

e = html.escape


def users():
    out = "".join(g("pop", person(36 + k * 32, 74, 0.85, INK), k) for k in range(5))
    out += g("fade", person(178, 116, 0.6, COOL), 5) + text(140, 140, "not the team", 11, COOL)
    out += text(100, 28, "like the real users", 12, INK)
    return out


def tasks():
    out = rect(70, 34, 110, 72, "none", INK, 2.5, 6) + rect(70, 34, 110, 14, DIM, "none", 0, 3)
    out += person(36, 90, 0.9, INK)
    out += g("pop", rect(82, 58, 44, 14, "none", ACC, 2, 3), 0) + g("pop", rect(82, 80, 70, 14, "none", ACC, 2, 3), 1)
    out += text(110, 128, "book a test slot", 12, ACC)
    return out


def aloud():
    out = person(40, 96, 1.0, INK) + g("pop", bubble(62, 24, 124, 50, ACC), 0)
    out += g("pop", text(124, 46, "where is the", 12, ACC), 1) + g("pop", text(124, 62, "save button…", 12, ACC), 2)
    return out


def prompt():
    out = person(40, 96, 0.9, INK) + person(160, 96, 0.9, COOL)
    out += g("pop", bubble(104, 26, 88, 30, COOL, tail="right"), 0) + g("pop", text(148, 46, "keep talking", 12, COOL), 1)
    out += g("fade", text(100, 132, "why did you…?", 12, HOT), 2) + g("pop", cross(160, 126, 7), 3)
    return out


def log():
    out = line([(24, 120), (186, 120)], DIM, 2) + line([(24, 120), (24, 26)], DIM, 2)
    pts = [(24, 120)] + [(24 + n * 30, 120 - 88 * (1 - (1 - 0.31) ** n)) for n in range(1, 6)]
    out += g("draw", line(pts, ACC, 2.5), 0)
    out += "".join(g("pop", circle(x, y, 3.5, ACC), 1 + i) for i, (x, y) in enumerate(pts[1:]))
    out += text(104, 140, "users tested", 11, DIM) + text(60, 22, "problems found", 11, INK, anchor="start")
    return out


PICTURES = {"users": users, "tasks": tasks, "aloud": aloud, "prompt": prompt, "log": log}


def exercise(ex, quote):
    """Return (html, js). Nielsen & Landauer's curve with their average lambda; seeded dots show which problems were found."""
    body = f"""
  <p>{e(ex["intro"])}</p>
  <label class="note" style="display:block">Users tested: <output id="nv"></output><br>
    <input type="range" id="n" min="1" max="15" step="1" value="5" style="width:100%;max-width:420px"></label>
  <label class="note" style="display:block">λ, the chance one user hits a given problem: <output id="lv"></output><br>
    <input type="range" id="lam" min="{ex["lambda_min"]}" max="{ex["lambda_max"]}" step="0.01" value="{ex["lambda"]}" style="width:100%;max-width:420px"></label>
  <div class="dots" id="dots" aria-hidden="true" style="max-width:420px"></div>
  <p aria-live="polite"><span class="share" id="share"></span> of the problems found</p>
  <p class="verdict" id="verdict"></p>
  <p class="note">{e(ex["data_label"])}</p>"""
    js = RNG_JS + "const X = " + json.dumps(ex) + ";\n" + r"""
function draw() {
  const n = +$("n").value, lam = +$("lam").value, share = 1 - Math.pow(1 - lam, n);
  $("nv").textContent = n; $("lv").textContent = lam.toFixed(2);
  $("share").textContent = Math.round(100 * share) + "%";
  // Each dot is a problem; each user finds each problem with chance lambda (seeded, the same on every visit).
  const r = rng(41); let html = "";
  for (let p = 0; p < X.problems; p++) { let found = false; for (let u = 0; u < 15; u++) { const hit = r() < lam; if (u < n && hit) found = true; }
    html += `<span class="dot${found ? " sev" : ""}"></span>`; }
  $("dots").innerHTML = html;
  const next = (1 - Math.pow(1 - lam, n + 1)) - share;
  $("verdict").textContent = `${n} users find about ${Math.round(100 * share)}% of the problems. One more user adds only ${Math.round(100 * next)} points: fix what you found, then test the new version.`;
}
$("n").oninput = draw; $("lam").oninput = draw;
draw();
"""
    return body, js
