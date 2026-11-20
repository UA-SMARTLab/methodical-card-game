"""IPD meta-analysis: the six steps' pictures (after Tierney et al. 2015) and the "one big table" exercise."""
import html
import json

from learn_pics._kit import INK, DIM, ACC, HOT, COOL, TREAT, CONTROL, g, rect, text, arrow, line, circle, path, doc, person, RNG_JS
from art import check, cross

e = html.escape


def collect():
    # Each trial team sends its participant-level file to the central team.
    out = ""
    for k, y in enumerate((20, 62, 104)):
        out += g("pop", doc(12, y, 24, 30, INK, 2, "#0f172a55") + text(24, y + 44, "", 1), k)
        out += g("pop", "".join(person(48 + i * 10, y + 18, .5, DIM) for i in range(3)), k)
        out += g("draw", arrow(82, y + 15, 120, 74, ACC, 2, head=6), 3 + k)
    out += g("pop", rect(124, 46, 64, 56, "#0f172a66", ACC, 2.5, 4) + text(156, 80, "central", 12, ACC), 6)
    return out + text(156, 120, "every participant", 11, ACC)


def plan():
    # The analysis plan is fixed before the data are opened.
    out = doc(22, 22, 66, 90, INK, 0, "#0f172a", 3)
    for k, lab in enumerate(("outcomes", "models", "subgroups")):
        out += g("draw", text(32, 46 + k * 22, "• " + lab, 11, INK, "start"), k)
    out += g("pop", rect(118, 52, 56, 46, "#0f172a", DIM, 2.5, 4) + path("M132,52 V42 a14,14 0 0 1 28,0 V52", DIM, 3), 3)
    return out + g("pop", text(146, 116, "data still shut", 11, DIM), 4)


def check_():
    # Rows of a data file, with the odd values flagged.
    out = text(100, 20, "trial 2 data", 12, INK)
    rows = (("54", "F", "12"), ("61", "M", "—"), ("47", "F", "9"), ("212", "M", "14"), ("58", "F", "11"))
    for r, row in enumerate(rows):
        y = 34 + r * 20
        for k, v in enumerate(row):
            bad = (r, k) in ((1, 2), (3, 0))
            out += g("pop" if bad else "draw", rect(40 + k * 40, y, 36, 16, "#0f172a66", HOT if bad else DIM, 1.5, 2)
                     + text(58 + k * 40, y + 12, v, 11, HOT if bad else INK), 5 if bad else r)
    return out + g("pop", text(172, 66, "missing", 11, HOT) + text(172, 106, "age 212?", 11, HOT), 6)


def harmonise():
    # Three trials with three outcome definitions become one shared definition.
    out = ""
    for k, lab in enumerate(("HbA1c < 7", "HbA1c < 6.5", "fasting < 7")):
        y = 24 + k * 36
        out += rect(10, y, 72, 24, "#0f172a66", DIM, 2, 4) + text(46, y + 16, lab, 11, DIM)
        out += g("draw", arrow(86, y + 12, 118, 72, INK, 2, head=5), k)
    out += g("pop", rect(120, 58, 70, 28, "#0f172a", ACC, 2.5, 4) + text(155, 76, "one definition", 11, ACC), 3)
    return out + text(100, 140, "same outcome everywhere", 11, DIM)


def stratify():
    # Compare arms inside each trial box, then combine the comparisons.
    out = ""
    for k, x in enumerate((14, 104)):
        out += rect(x, 20, 82, 70, "none", DIM, 2, 6) + text(x + 41, 16, f"trial {k + 1}", 11, DIM)
        out += person(x + 22, 50, .8, TREAT) + person(x + 60, 50, .8, CONTROL)
        out += g("draw", arrow(x + 32, 48, x + 50, 48, INK, 2, head=5) + arrow(x + 50, 56, x + 32, 56, INK, 2, head=5), k)
        out += g("draw", arrow(x + 41, 92, 100, 112, ACC, 2, head=5), 2 + k)
    return out + g("pop", path("M84,122 L100,114 L116,122 L100,130 Z", ACC, 2, fill=ACC), 4) + text(100, 146, "within, then combine", 11, ACC)


def who():
    # Effect by participant group: young and old get different benefits.
    base = 116
    out = line([(24, base), (180, base)], DIM, 2)
    for k, (lab, h) in enumerate((("< 50", 70), ("50–70", 46), ("> 70", 14))):
        x = 40 + k * 50
        out += g("grow", rect(x, base - h, 30, h, ACC, "none", 0, 2), k) + text(x + 15, base + 16, lab, 11, INK)
    return out + text(100, 24, "benefit by age", 12, ACC) + text(100, 144, "participant level", 11, DIM)


PICTURES = {"collect": collect, "plan": plan, "check": check_, "harmonise": harmonise, "stratify": stratify, "who": who}


def exercise(ex, quote):
    """Return (html, js). Two example trials: pool them as one mega trial, or compare within each trial (Mantel-Haenszel)."""
    rows = "".join(f'<tr><td>{e(t["name"])}</td><td>{t["t_events"]} / {t["t_n"]}</td><td>{t["c_events"]} / {t["c_n"]}</td>'
                   f'<td>{(t["t_events"] / t["t_n"]) / (t["c_events"] / t["c_n"]):.2f}</td></tr>' for t in ex["trials"])
    body = f"""
  <p>{e(ex["intro"])}</p>
  <table class="note" style="border-collapse:collapse;width:100%;max-width:560px">
    <thead><tr><th style="text-align:left">Trial</th><th>Treatment events</th><th>Control events</th><th>Risk ratio</th></tr></thead>
    <tbody>{rows}</tbody></table>
  <div class="controls" role="group" aria-label="How to pool">
    <button type="button" data-how="mega">One big table</button>
    <button type="button" data-how="strat">Trial by trial</button>
  </div>
  <p class="share" id="rr" aria-live="polite"></p>
  <p class="verdict" id="verdict"></p>
  <p class="note">{e(ex["data_label"])} {e(ex["method_note"])}</p>"""
    js = RNG_JS + "const X = " + json.dumps(ex) + ";\n" + r"""
let how = "mega";
function rr() {
  const T = X.trials;
  if (how === "mega") {
    const te = T.reduce((a, t) => a + t.t_events, 0), tn = T.reduce((a, t) => a + t.t_n, 0);
    const ce = T.reduce((a, t) => a + t.c_events, 0), cn = T.reduce((a, t) => a + t.c_n, 0);
    return { v: (te / tn) / (ce / cn), detail: `${te}/${tn} treated vs ${ce}/${cn} controls had the event` };
  }
  // Mantel-Haenszel: each trial's arms are compared with each other only, weighted by its size.
  let num = 0, den = 0;
  for (const t of T) { const N = t.t_n + t.c_n; num += t.t_events * t.c_n / N; den += t.c_events * t.t_n / N; }
  return { v: num / den, detail: "arms compared within each trial, then combined" };
}
function draw() {
  const r = rr();
  $("rr").textContent = `Risk ratio ${r.v.toFixed(2)}`;
  $("verdict").textContent = how === "mega"
    ? `${r.detail}. One big table says the treatment raises the risk, though it lowers it in both trials: the treated group is mostly high-risk trial 1 patients.`
    : `${r.detail}. The treatment lowers the risk, as it does in each trial.`;
  document.querySelectorAll("[data-how]").forEach(b => b.setAttribute("aria-pressed", b.dataset.how === how));
}
document.querySelectorAll("[data-how]").forEach(b => b.onclick = () => { how = b.dataset.how; draw(); });
draw();
"""
    return body, js
