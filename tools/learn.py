"""Learn pages: one page per Method that acts out how it works, step by step, with moving pictures.

Source: data/learn/<method-id>.json (steps, each with its source; an optional exercise; limits). The card's own
words, picture, threats and safeguards come from the decks, so nothing is written twice. Output:
app/learn/<method-id>/index.html. English only for now (see the data file's limits).

The pictures move with the CSS motions below (pop, draw, grow, fade, roll). Each plays three times on opening and
loops on hover or focus; the last frame is the whole picture, and reduced-motion users get that frame at once.

Each Method's pictures (and its exercise, if it has one) live in tools/learn_pics/<id with _ for ->.py: PICTURES maps
a step's "picture" name to a function that draws it; an optional exercise(ex, quote) returns (html, js). One file per
Method, so pages can be written side by side without touching each other.
"""
import html
import importlib
import json

import art
from art_threats import THREAT_ART
from art_safeguards import SAFEGUARD_ART

e = html.escape

def svg(inner, uid, color, label):
    s = art.frame(inner, uid, art.shade(color, .12), art.shade(color, -.45))
    return s.replace('role="img"', f'role="img" aria-label="{e(label)}"', 1)


# --------------------------------------------------------------------------- page
CSS = """
:root { --bg:#EEF1F4; --surface:#FFFFFF; --ink:#141922; --muted:#596273; --line:#D5DBE3; --accent:#2340A8; --fam:%(fam)s; color-scheme: light; }
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) { --bg:#0E131A; --surface:#161D27; --ink:#E5E9EF; --muted:#98A2B1; --line:#2A3441; --accent:#8AA6FF; color-scheme: dark; } }
:root[data-theme="dark"] { --bg:#0E131A; --surface:#161D27; --ink:#E5E9EF; --muted:#98A2B1; --line:#2A3441; --accent:#8AA6FF; color-scheme: dark; }
* { box-sizing: border-box; }
body { margin:0; background:var(--bg); color:var(--ink); font:16px/1.5 'IBM Plex Sans', system-ui, sans-serif; }
main { max-width: 980px; margin: 0 auto; padding: 16px 16px 64px; }
a { color: var(--accent); }
.top { display:flex; justify-content:space-between; gap:12px; flex-wrap:wrap; font-size:.95rem; }
h1, h2, h3 { font-family:'Bricolage Grotesque', system-ui, sans-serif; line-height:1.15; }
h1 { font-size: clamp(2rem, 6vw, 3.2rem); margin: 18px 0 6px; letter-spacing:-.02em; }
h2 { font-size: 1.5rem; margin: 40px 0 6px; }
.kicker { font-family:'Barlow Condensed', sans-serif; font-weight:700; text-transform:uppercase; letter-spacing:.06em; color:var(--muted); margin:0; }
.hero { display:grid; grid-template-columns: minmax(0,1fr) minmax(0,300px); gap:24px; align-items:center; }
.lead { font-size:1.15rem; max-width:52ch; }
.q { border-left:4px solid var(--fam); padding:4px 12px; font-weight:600; }
.pic svg { display:block; width:100%; height:auto; border-radius:12px; }
.steps { list-style:none; padding:0; margin:12px 0 0; display:grid; grid-template-columns:repeat(auto-fill, minmax(260px, 1fr)); gap:16px; counter-reset: s; }
.steps li { background:var(--surface); border:1px solid var(--line); border-radius:14px; padding:12px; counter-increment:s; }
.steps h3 { margin:10px 0 4px; font-size:1.15rem; }
.steps h3::before { content: counter(s) ". "; color:var(--muted); }
.steps p { margin:0 0 6px; }
.src { font-size:.85rem; color:var(--muted); }
blockquote { margin:8px 0; padding:6px 10px; border-left:3px solid var(--fam); background:color-mix(in srgb, var(--fam) 7%%, transparent); border-radius:0 8px 8px 0; }
blockquote p { margin:0; font-style:italic; font-size:.93rem; }
blockquote footer { font-size:.8rem; color:var(--muted); margin-top:2px; }
.sources li { margin-bottom:6px; }
.ex table { border-collapse:collapse; margin:8px 0; font-variant-numeric:tabular-nums; max-width:100%%; display:block; overflow-x:auto; }
.ex th, .ex td { border-bottom:1px solid var(--line); padding:4px 10px; text-align:left; }
.ex th { font-weight:600; color:var(--muted); font-size:.9rem; }
.ex input[type="range"] { accent-color:var(--fam); width:min(100%%, 320px); vertical-align:middle; min-height:32px; }
.ex input[type="checkbox"] { accent-color:var(--fam); width:20px; height:20px; vertical-align:middle; }
.ex output { font-weight:700; font-variant-numeric:tabular-nums; }
.ex label { display:inline-flex; gap:6px; align-items:center; flex-wrap:wrap; }
.ex svg { max-width:100%%; height:auto; }
.ex { background:var(--surface); border:1px solid var(--line); border-radius:14px; padding:16px; }
.ex .controls { display:flex; flex-wrap:wrap; gap:8px; align-items:center; margin:10px 0; }
.ex button, .ex select { font:inherit; padding:8px 14px; border-radius:999px; border:1px solid var(--line); background:transparent; color:inherit; cursor:pointer; min-height:44px; }
.ex button[aria-pressed="true"] { background:var(--ink); color:var(--bg); border-color:var(--ink); font-weight:700; }
.arms { display:grid; grid-template-columns:1fr 1fr; gap:16px; }
.arm h3 { margin:6px 0; font-size:1.05rem; }
.dots { display:flex; flex-wrap:wrap; gap:3px; min-height:24px; }
.dot { width:10px; height:10px; border-radius:50%%; background:var(--muted); opacity:.55; }
.dot.sev { background:#E11D48; opacity:1; }
.share { font-size:1.6rem; font-weight:800; font-family:'Bricolage Grotesque', sans-serif; }
.bar { height:10px; background:var(--line); border-radius:5px; overflow:hidden; }
.bar span { display:block; height:100%%; background:#E11D48; transition: width .4s; }
.verdict { font-weight:600; min-height:3em; }
.note { font-size:.85rem; color:var(--muted); }
.threats { display:grid; grid-template-columns:repeat(auto-fill, minmax(280px,1fr)); gap:16px; padding:0; list-style:none; }
.threats li { background:var(--surface); border:1px solid var(--line); border-radius:14px; padding:12px; }
.pair { display:grid; grid-template-columns:1fr 1fr; gap:8px; }
.pair figure { margin:0; }
.pair figcaption { font-size:.85rem; font-weight:600; margin-top:4px; }
.threats h3 { margin:0 0 2px; font-size:1.05rem; color:#BE123C; }
:root[data-theme="dark"] .threats h3 { color:#FB7185; }
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) .threats h3 { color:#FB7185; } }
.threats p { margin:0 0 8px; }
.fix { color:#047857; }
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) .fix { color:#34D399; } }
:root[data-theme="dark"] .fix { color:#34D399; }
@media (max-width: 640px) { .hero { grid-template-columns: 1fr; } .arms { grid-template-columns: 1fr; } }

/* Moving pictures: three plays on opening, a loop on hover or focus; the last frame is the whole picture. */
.mv .pop, .mv .draw, .mv .grow, .mv .fade, .mv .roll { animation-duration: 4.5s; animation-iteration-count: 3; animation-fill-mode: both;
  animation-delay: calc(var(--i, 0) * .32s); transform-box: fill-box; }
.mv .pop { animation-name: pop; transform-origin: center; }
.mv .draw { animation-name: draw; }
.mv .grow { animation-name: grow; transform-origin: bottom; }
.mv .fade { animation-name: fade; }
.mv .roll { animation-name: roll; transform-origin: center; }
.mv:hover .pop, .mv:hover .draw, .mv:hover .grow, .mv:hover .fade, .mv:hover .roll,
.mv:focus-within .pop, .mv:focus-within .draw, .mv:focus-within .grow, .mv:focus-within .fade, .mv:focus-within .roll { animation-iteration-count: infinite; }
@keyframes pop { 0%%, 8%% { opacity: 0; transform: scale(.4); } 18%%, 100%% { opacity: 1; transform: none; } }
@keyframes draw { 0%%, 6%% { opacity: 0; clip-path: inset(0 100%% 0 0); } 30%%, 100%% { opacity: 1; clip-path: inset(0 0 0 0); } }
@keyframes grow { 0%%, 8%% { transform: scaleY(0); } 40%%, 100%% { transform: none; } }
@keyframes fade { 0%%, 30%% { opacity: 1; } 55%%, 100%% { opacity: .18; } }
@keyframes roll { 0%% { transform: rotate(0) translateY(-6px); } 25%% { transform: rotate(360deg) translateY(0); } 100%% { transform: rotate(360deg); } }
@media (prefers-reduced-motion: reduce) { .mv * { animation: none !important; } }
"""

def fill(s, **kv):
    """Put values into CSS or JS written with %(name)s slots and %% for a literal per cent."""
    for k, v in kv.items():
        s = s.replace(f"%({k})s", v)
    return s.replace("%%", "%")


def build(d, method_id, out_root):
    """Write app/learn/<id>/index.html from data/learn/<id>.json and the decks in d. Returns the path."""
    from pathlib import Path
    root = Path(__file__).resolve().parent.parent
    L = json.loads((root / "data" / "learn" / f"{method_id}.json").read_text(encoding="utf-8"))
    m = next(x for x in d["designs"] if x["id"] == method_id)
    fam = next(f for f in d["meta"]["families"] if f["id"] == m["family"])
    threats = {t["id"]: t for t in d["threats"]}
    safeguards = {s["id"]: s for s in d["safeguards"]}
    color = fam["color"]
    card = svg(art.DESIGN_ART[method_id](), "card", color, m["name"])

    S = L["sources"]

    def quote(q):
        """A definition word for word, then who wrote it and where: the players are scientists and will want to check."""
        if q["source"] not in S:
            raise KeyError(f"data/learn/{method_id}.json quotes unknown source {q['source']!r}; add it under \"sources\"")
        s = S[q["source"]]
        return (f'<blockquote><p>“{e(q["text"])}”</p><footer><a href="{e(s["url"])}" target="_blank" rel="noopener">'
                f'{e(s["short"])}</a>, {e(q["where"])}</footer></blockquote>')

    def after(c):
        """Where a step cannot quote (the source could not be read word for word), it says whose account it follows."""
        s = S[c["source"]]
        return f'<p class="src">After <a href="{e(s["url"])}" target="_blank" rel="noopener">{e(s["short"])}</a>, {e(c["where"])}</p>'

    mod = importlib.import_module("learn_pics." + method_id.replace("-", "_"))
    for k in ("question", "sources", "steps"):
        if not L.get(k):
            raise ValueError(f"data/learn/{method_id}.json has no {k!r}")
    if not 3 <= len(L["steps"]) <= 7:
        raise ValueError(f"data/learn/{method_id}.json has {len(L['steps'])} steps; give it 3 to 7")
    if not any(s.get("quotes") for s in L["steps"]):
        raise ValueError(f"data/learn/{method_id}.json quotes no source word for word; at least one step must")
    steps = ""
    for i, s in enumerate(L["steps"]):
        if s["picture"] not in mod.PICTURES:
            raise KeyError(f"tools/learn_pics/{mod.__name__.split('.')[-1]}.py has no picture {s['picture']!r} for step {s['id']!r}")
        if not s.get("quotes") and not s.get("after"):
            raise ValueError(f"data/learn/{method_id}.json step {s['id']!r} has neither a quote nor an \"after\" source")
        steps += (f'<li><div class="pic mv" tabindex="0">{svg(mod.PICTURES[s["picture"]](), f"s{i}", color, s["title"])}</div>'
                  f'<h3>{e(s["title"])}</h3><p>{e(s["text"])}</p>{"".join(quote(q) for q in s.get("quotes", []))}'
                  + (after(s["after"]) if s.get("after") and not s.get("quotes") else "") + '</li>')

    ths = ""
    for i, tid in enumerate(m["weak_vs"]):
        t = threats[tid]
        fix = next((safeguards[c] for c in t["countered_by"] if m["family"] in safeguards[c].get("applies_to", [m["family"]])),
                   safeguards[t["countered_by"][0]])
        ths += (f'<li><h3>{e(t["name"])}</h3><p>{e(t["short"])}</p><div class="pair">'
                f'<figure>{svg(THREAT_ART[tid](), f"t{i}", "#9F1239", t["name"])}<figcaption>The threat</figcaption></figure>'
                f'<figure>{svg(SAFEGUARD_ART[fix["id"]](), f"g{i}", "#047857", fix["name"])}'
                f'<figcaption class="fix">Safeguard: {e(fix["name"])}</figcaption></figure></div>'
                f'<p class="src">{e(fix["short"])}</p>'
                + (quote(L["threat_quotes"][tid]) if tid in L.get("threat_quotes", {}) else "") + '</li>')

    # An exercise is optional: a Method argued in words gets pictures only.
    ex, exercise, ex_js = L.get("exercise"), "", ""
    if ex:
        if not hasattr(mod, "exercise"):
            raise KeyError(f"data/learn/{method_id}.json has an exercise but {mod.__name__} has no exercise()")
        body, ex_js = mod.exercise(ex, quote)
        exercise = (f'<h2>{e(ex["title"])}</h2><div class="ex">{quote(ex["quote"]) if ex.get("quote") else ""}{body}</div>')

    ref = m["ref"]
    page = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(m["name"])}: how it works</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,800&family=IBM+Plex+Sans:wght@400;600&family=Barlow+Condensed:wght@700&display=swap">
<style>{fill(CSS, fam=color)}</style></head>
<body><main>
<!-- Generated by tools/learn.py from data/learn/{e(method_id)}.json; do not edit. -->
<nav class="top"><a href="../../">&larr; Methodical</a></nav>
<div class="hero"><div>
  <p class="kicker">{e(fam["name"])} / Method</p>
  <h1>{e(m["name"])}</h1>
  <p class="q">{e(L["question"])}</p>
  <p class="lead">{e(m["gist"])}</p>
</div><div class="pic">{card}</div></div>

<h2>How it works</h2>
<ol class="steps">{steps}</ol>
{exercise}
<h2>Where it breaks, and what protects it</h2>
<ul class="threats">{ths}</ul>

<h2>A real example</h2>
<p>{e(m["example"])}</p>
<p class="src">Defining reference: <a href="{e(ref["url"])}" target="_blank" rel="noopener">{e(ref["cite"])}</a></p>

<h2>Sources</h2>
<ul class="sources">{"".join(f'<li><a href="{e(s["url"])}" target="_blank" rel="noopener">{e(s["cite"])}</a> <span class="note">Checked: {e(s["checked"])}.</span></li>' for s in S.values())}</ul>
</main>
{f"<script>{ex_js}</script>" if ex_js else ""}
</body></html>
"""
    out = out_root / "learn" / method_id / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page, encoding="utf-8", newline="\n")
    return out


def learn_ids(root):
    return sorted(p.stem for p in (root / "data" / "learn").glob("*.json"))


if __name__ == "__main__":
    # Build one page without the whole game: python tools/learn.py <method-id> [--out <folder>] (default app/).
    import sys
    from pathlib import Path
    root = Path(__file__).resolve().parent.parent
    load = lambda n: json.loads((root / "data" / f"{n}.json").read_text(encoding="utf-8"))
    d = {"meta": load("meta"), "designs": load("designs"), "threats": load("threats"), "safeguards": load("safeguards")}
    out = Path(sys.argv[sys.argv.index("--out") + 1]) if "--out" in sys.argv else root / "app"
    print(build(d, sys.argv[1], out))
