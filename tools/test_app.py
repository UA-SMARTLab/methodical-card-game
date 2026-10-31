#!/usr/bin/env python3
"""Test the built app (app/index.html) in headless Chrome or Edge, driving it like a player.

  python tools/test_app.py      (run python tools/build.py first)

The test page loads the app in a frame and plays every Question once: tap a Method card, press the green "Pick this
card" button in the full-screen viewer, then defend the best Method in the peer-review round. It also checks the home
page, the decks, the phone's back button, signed scores in right-to-left pages, and that a round in progress
survives leaving the game. Expected tiers come from the answer key in data/questions.json, by definition: a Method
listed under "best" is best, under "ok" defensible, under "traps" a trap, anything else unlisted. Exit status 1 on any
failure.
"""
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from check_cards import chrome  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent

DRIVER = r"""
const sleep = ms => new Promise(r => setTimeout(r, ms));
const out = { errors: [], fails: [], played: 0 };
const fr = document.getElementById("app");
let w = fr.contentWindow, d = fr.contentDocument;
const $ = s => d.querySelector(s), $$ = s => [...d.querySelectorAll(s)];
const fail = m => out.fails.push(m);
const watch = () => w.addEventListener("error", e => out.errors.push(String(e.message)));
const reload = async () => {
  await new Promise(r => { fr.addEventListener("load", r, { once: true }); w.location.reload(); });
  await sleep(400); w = fr.contentWindow; d = fr.contentDocument; watch();
};
async function run() {
  watch();
  // Home
  if ($$("#hero-fan .tcg").length !== 5) fail("home: the fan should show 5 cards");
  $("#quick-card").click(); await sleep(50);
  if ($$("#quick-panel .opt").length !== 4) fail("home: the quick question should offer 4 choices");
  $("#quick-panel .opt").click(); await sleep(50);
  if (!$("#quick-verdict p")) fail("home: the quick question gave no verdict");
  // Play: every Question once, choosing through the full-screen viewer and its green button.
  $('[data-go="play"]').click(); await sleep(50);
  const questions = w.eval("questions"), SC = w.eval("SC");
  const seen = new Set();
  w.eval("queue = []; stats = { score: 0, answered: 0, bestHits: 0, streak: 0, seen: {} }; nextQuestion()");
  for (let n = 0; n < questions.length; n++) {
    const q = w.eval("q"); seen.add(q.id);
    const picks = $$("#panel [data-pick]").map(b => b.dataset.pick);
    if (picks.length !== 4) fail(`${q.id}: ${picks.length} choices instead of 4`);
    if (!picks.includes(q.best[0])) fail(`${q.id}: the best Method is not among the choices`);
    if (new Set(picks).size !== 4) fail(`${q.id}: a choice is repeated`);
    // A wrong answer on every other Question, the best one on the rest.
    const choice = n % 2 ? picks.find(p => p !== q.best[0]) : q.best[0];
    const ref = window.EXPECT[q.id][choice] || "unlisted";
    const before = w.eval("stats.score");
    $$("#panel [data-pick]")[picks.indexOf(choice)].click(); await sleep(60);
    if (!$(".viewer.choosing")) { fail(`${q.id}: tapping a card did not open the viewer`); break; }
    await sleep(380);
    $(".viewer .v-pick").click(); await sleep(60);
    const head = $("#panel .result-head");
    if (!head || !head.classList.contains("r-" + ref)) fail(`${q.id}: result shows ${head && head.className}, the key says ${ref}`);
    if (w.eval("stats.score") - before !== SC[ref]) fail(`${q.id}: score changed by ${w.eval("stats.score") - before}, expected ${SC[ref]}`);
    if ($$("#panel .pick.res").length !== 4 || !$("#panel .pick.chosen")) fail(`${q.id}: the four cards don't show the result`);
    // On a right-to-left (Arabic) page a negative score must still read "-2", not "2-".
    if (SC[ref] < 0 && !out.rtlChecked) {
      out.rtlChecked = true; d.documentElement.dir = "rtl";
      for (const e of $$("#panel .pts, #s-score, #panel .badge bdi").filter(e => /^[-−]\d/.test(e.textContent))) {
        const t = e.firstChild, a = d.createRange(), b = d.createRange();
        a.setStart(t, 0); a.setEnd(t, 1); b.setStart(t, 1); b.setEnd(t, 2);
        if (a.getBoundingClientRect().left > b.getBoundingClientRect().left) fail(`rtl: ${e.className || e.id || e.tagName} shows "${e.textContent}" with its sign on the right`);
      }
      d.documentElement.dir = "ltr";
    }
    // Peer review: a Safeguard that counters the key Threat scores +1.
    const right = w.eval("review.t.countered_by");
    const opt = $$("#review [data-sg]").find(b => right.includes(b.dataset.sg));
    if (!opt) fail(`${q.id}: no Safeguard offered that counters ${q.key_threat}`); else {
      const b2 = w.eval("stats.score"); opt.click(); await sleep(20);
      if (w.eval("stats.score") - b2 !== 1) fail(`${q.id}: the right Safeguard did not score +1`);
    }
    out.played++;
    if (n < questions.length - 1) { $("#b-next").click(); await sleep(30); }
  }
  if (seen.size !== questions.length) fail(`dealt ${seen.size} different Questions in ${questions.length} deals; the queue should not repeat`);
  // Keyboard: Escape closes the viewer.
  w.eval("nextQuestion()"); await sleep(30);
  $("#panel [data-pick]").click(); await sleep(60);
  w.dispatchEvent(new KeyboardEvent("keydown", { key: "Escape" })); await sleep(300);
  if ($(".viewer")) fail("Escape did not close the viewer");
  // The phone's back button stays in the game: it closes a full-screen card first, then returns to the previous page.
  // Back is only pressed when the game has a step of its own to go back to; otherwise it would leave this test page.
  const goBack = async () => {
    if (!(w.history.state?.depth > 0)) return false;
    const p = new Promise(r => w.addEventListener("popstate", () => setTimeout(r, 50), { once: true }));
    w.history.back(); await Promise.race([p, sleep(800)]); return true;
  };
  w.eval('show("home")'); $("#tab-play").click(); await sleep(50);
  $("#panel [data-pick]").click(); await sleep(60);
  if (!$(".viewer:not(.out)")) fail("back: the full-screen card did not open");
  if (!(await goBack()) || $(".viewer:not(.out)") || $("#view-play").hidden) fail("back did not close the full-screen card on the Play page");
  if (!(await goBack()) || $("#view-home").hidden) fail("back from Play did not return to Home");
  // A round in progress survives leaving the game: the same Question and choices come back, on the Play page, and a
  // finished round is not scored twice.
  $("#tab-play").click(); await sleep(50);
  w.eval("nextQuestion()"); await sleep(30);
  const qid = w.eval("q.id"), ch = w.eval("choices.join()");
  await reload();
  if ($("#view-play").hidden || w.eval("q.id") !== qid || w.eval("choices.join()") !== ch || w.eval("phase") !== "choose")
    fail(`leaving mid-question: came back to ${w.eval("q.id")} (${w.eval("phase")}) on ${$("#view-play").hidden ? "another page" : "Play"}, expected ${qid}`);
  $("#panel [data-pick]").click(); await sleep(400); $(".viewer .v-pick").click(); await sleep(60);
  const pickedId = w.eval("picked"), score = w.eval("stats.score");
  const right = w.eval("review.t.countered_by"), sg = $$("#review [data-sg]").find(b => right.includes(b.dataset.sg));
  sg.click(); await sleep(20);
  const scoreAfter = w.eval("stats.score");
  await reload();
  if (w.eval("phase") !== "result" || w.eval("picked") !== pickedId || !$("#panel .result-head")) fail("leaving after answering: the result did not come back");
  if (w.eval("review && review.answer") !== sg.dataset.sg) fail("leaving after the peer review: its answer did not come back");
  if (w.eval("stats.score") !== scoreAfter) fail(`leaving after answering: the score changed from ${scoreAfter} to ${w.eval("stats.score")}`);
  out.round = scoreAfter - score === 1;
  // Decks
  $("#tab-decks").click(); await sleep(50);
  const counts = {};
  for (const k of ["designs", "questions", "threats", "safeguards", "twists", "programs"]) {
    $(`#deck-tabs [data-deck="${k}"]`).click(); await sleep(30);
    counts[k] = $$("#cards figure").length;
    if (counts[k] !== w.eval(`DATA.${k}.length`)) fail(`decks: ${k} shows ${counts[k]} cards, expected ${w.eval(`DATA.${k}.length`)}`);
  }
  out.counts = counts;
}
run().catch(e => out.fails.push("driver crashed: " + e)).finally(() => { document.body.dataset.result = JSON.stringify(out); });
"""


def expectations():
    """For every Question, the tier of each Method in the answer key (data/questions.json), by definition."""
    out = {}
    for q in json.loads((ROOT / "data" / "questions.json").read_text(encoding="utf-8")):
        tiers = {d: "trap" for d in q["traps"]}
        tiers.update({d: "ok" for d in q["ok"]})
        tiers.update({d: "best" for d in q["best"]})
        out[q["id"]] = tiers
    return out


def run_test(exe):
    app = (ROOT / "app" / "index.html").as_uri()
    with tempfile.TemporaryDirectory() as tmp:
        page = Path(tmp) / "harness.html"
        page.write_text(f"""<!doctype html><html><head><meta charset="utf-8"><style>html,body{{margin:0;height:100%}}
iframe{{border:0;width:100%;height:100%;display:block}}</style></head><body>
<iframe id="app" src="{app}"></iframe>
<script>window.EXPECT = {json.dumps(expectations())};
document.getElementById("app").addEventListener("load", () => setTimeout(() => {{ {DRIVER} }}, 400), {{ once: true }});</script></body></html>""",
                        encoding="utf-8")
        dom = subprocess.run([exe, "--headless=new", "--disable-gpu", "--no-first-run", "--allow-file-access-from-files",
                              f"--user-data-dir={Path(tmp) / 'profile'}", "--window-size=1280,900",
                              "--virtual-time-budget=120000", "--dump-dom", page.as_uri()],
                             capture_output=True, text=True, encoding="utf-8", timeout=600).stdout
    m = re.search(r'data-result="([^"]*)"', dom)
    if not m:
        print("FAIL: the test page produced no result (the app did not load, or the driver did not finish)")
        return False
    res = json.loads(m.group(1).replace("&quot;", '"').replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">"))
    for f in res["fails"] + [f"page error: {e}" for e in res["errors"]]:
        print("FAIL", f)
    ok = not res["fails"] and not res["errors"]
    print(f"{'ok  ' if ok else 'FAIL'} played {res['played']} Questions through the viewer and its green button; decks show {res.get('counts')}")
    return ok


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")  # failure details may quote any language, also on a Windows console
    sys.exit(0 if run_test(chrome()) else 1)
