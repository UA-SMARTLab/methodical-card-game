"""Trading-card renderer for Methodical.

Each card is plain HTML + inline SVG art. Every size is a multiple of the CSS variable --u, which is 1mm in
print (cards are 63 x 88 u, standard poker size) and can be set to any pixel size on screen.
"""
import html

import art

try:
    from art_threats import THREAT_ART
except ImportError:
    THREAT_ART = {}
try:
    from art_safeguards import SAFEGUARD_ART
except ImportError:
    SAFEGUARD_ART = {}
try:
    from art_questions import QUESTION_ART
except ImportError:
    QUESTION_ART = {}
try:
    from art_misc import TWIST_ART, PROGRAM_ART
except ImportError:
    TWIST_ART, PROGRAM_ART = {}, {}

e = html.escape

THREAT_COLOR = "#9F1239"
SAFEGUARD_COLOR = "#047857"
TWIST_COLOR = "#6D28D9"
PROGRAM_COLOR = "#0C4A6E"
BACK_COLOR = "#0F172A"

FONTS_URL = ("https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,800"
             "&family=Barlow+Condensed:wght@600;700&family=IBM+Plex+Sans+Condensed:ital,wght@0,400;0,600;1,400&display=swap")

CARD_CSS = """
.tcg { --u: var(--card-u, 1mm); --hi: color-mix(in srgb, var(--c) 72%, #fff); --lo: color-mix(in srgb, var(--c) 55%, #000);
  box-sizing: border-box; width: calc(var(--u) * 63); height: calc(var(--u) * 88); flex: none;
  border-radius: calc(var(--u) * 3.2); padding: calc(var(--u) * 2.3); position: relative; overflow: hidden;
  display: flex; flex-direction: column; gap: calc(var(--u) * 1.2); color: #16181d; text-align: left;
  background: linear-gradient(160deg, var(--hi), var(--c) 42%, var(--lo));
  box-shadow: inset 0 0 0 calc(var(--u) * .45) rgba(0,0,0,.45), inset 0 0 0 calc(var(--u) * 1) rgba(255,255,255,.14);
  font-family: "IBM Plex Sans Condensed", "Arial Narrow", sans-serif; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
.tcg *, .tcg *::before { box-sizing: border-box; }
.tcg::before { content: ""; position: absolute; inset: 0; pointer-events: none; opacity: .5;
  background: repeating-linear-gradient(135deg, rgba(255,255,255,.07) 0 calc(var(--u) * .5), transparent calc(var(--u) * .5) calc(var(--u) * 1.6)); }
.tcg > * { position: relative; }
.tcg .nm { height: calc(var(--u) * 8.4); flex: none; display: flex; align-items: center; justify-content: space-between; gap: calc(var(--u) * 1.4);
  padding: 0 calc(var(--u) * 1.4) 0 calc(var(--u) * 2.2); border-radius: calc(var(--u) * 1.4);
  background: linear-gradient(#ffffff, #e4e8ee); box-shadow: inset 0 calc(var(--u) * -.45) 0 rgba(0,0,0,.14), 0 calc(var(--u) * .35) calc(var(--u) * .8) rgba(0,0,0,.35); }
.tcg .nm b { font: 800 calc(var(--u) * 4.4)/1 "Bricolage Grotesque", "Arial Narrow", sans-serif; letter-spacing: -.02em; overflow: hidden; }
.tcg .nm b.s1 { font-size: calc(var(--u) * 3.95); } .tcg .nm b.s2 { font-size: calc(var(--u) * 3.45); } .tcg .nm b.s3 { font-size: calc(var(--u) * 3.0); line-height: 1.05; }
.tcg .attr { flex: none; width: calc(var(--u) * 5.8); height: calc(var(--u) * 5.8); border-radius: 50%; display: grid; place-items: center;
  background: radial-gradient(circle at 35% 30%, var(--hi), var(--lo)); color: #fff; box-shadow: 0 0 0 calc(var(--u) * .4) #fff, 0 0 0 calc(var(--u) * .7) rgba(0,0,0,.35); }
.tcg .attr .ic, .tcg .sb .ic { width: 62%; height: 62%; }
.tcg .lv { height: calc(var(--u) * 4.6); flex: none; display: flex; align-items: center; justify-content: space-between; gap: calc(var(--u) * 1); color: #fff;
  font: 700 calc(var(--u) * 2.5)/1 "Barlow Condensed", "Arial Narrow", sans-serif; letter-spacing: .08em; text-transform: uppercase; }
.tcg .lv > span { display: flex; align-items: center; gap: calc(var(--u) * .8); }
.tcg .sb { width: calc(var(--u) * 4.4); height: calc(var(--u) * 4.4); border-radius: 50%; display: grid; place-items: center; color: #fff;
  background: var(--s); box-shadow: 0 0 0 calc(var(--u) * .35) #fff; }
.tcg .coin { width: calc(var(--u) * 2.8); height: calc(var(--u) * 2.8); border-radius: 50%; background: radial-gradient(circle at 35% 30%, #fff3b0, #e0a800);
  box-shadow: 0 0 0 calc(var(--u) * .25) rgba(0,0,0,.45); }
.tcg .tick { width: calc(var(--u) * 2.2); height: calc(var(--u) * 2.2); transform: rotate(45deg); background: #fff; box-shadow: 0 0 0 calc(var(--u) * .25) rgba(0,0,0,.45); }
.tcg .off { opacity: .28; }
.tcg .star { color: #fde047; font-size: calc(var(--u) * 3.6); line-height: 1; text-shadow: 0 0 calc(var(--u) * .5) rgba(0,0,0,.6); }
.tcg .art { flex: none; height: calc(var(--u) * 37.5); border-radius: calc(var(--u) * .7); overflow: hidden; background: #0f172a;
  box-shadow: 0 0 0 calc(var(--u) * .55) rgba(255,255,255,.9), 0 0 0 calc(var(--u) * .9) rgba(0,0,0,.45); margin: calc(var(--u) * .5) calc(var(--u) * .9); }
.tcg .art svg { width: 100%; height: 100%; display: block; }
.tcg.tcg-q .art { height: calc(var(--u) * 31); }
.tcg.tcg-t .art { height: calc(var(--u) * 43); }
.tcg.tcg-s .art { height: calc(var(--u) * 40.5); }
.tcg.tcg-x .art { height: calc(var(--u) * 41); }
.tcg .tb { flex: 1; min-height: 0; display: flex; flex-direction: column; gap: calc(var(--u) * .7); padding: calc(var(--u) * 1.1) calc(var(--u) * 1.7) calc(var(--u) * 1);
  border-radius: calc(var(--u) * 1); background: linear-gradient(#f8f9f6, #eceee8); box-shadow: inset 0 0 0 calc(var(--u) * .3) rgba(0,0,0,.28); }
.tcg .ty { font: 700 calc(var(--u) * 2.45)/1.1 "Barlow Condensed", "Arial Narrow", sans-serif; letter-spacing: .05em; text-transform: uppercase; color: #3b3f47; }
.tcg .fx { margin: 0; font-size: calc(var(--u) * 2.95); line-height: 1.24; }
.tcg.tcg-q .fx { font-size: calc(var(--u) * 2.75); line-height: 1.25; }
.tcg .row { display: flex; flex-wrap: wrap; align-items: center; gap: calc(var(--u) * .6) calc(var(--u) * 1.2);
  font: 700 calc(var(--u) * 2.3)/1.15 "Barlow Condensed", "Arial Narrow", sans-serif; letter-spacing: .04em; text-transform: uppercase; color: #4b5059; }
.tcg .row .ic { width: calc(var(--u) * 3.5); height: calc(var(--u) * 3.5); }
.tcg .row .yes { color: #0f7a3c; display: inline-flex; gap: calc(var(--u) * .5); align-items: center; }
.tcg .row .no { color: #b42318; display: inline-flex; gap: calc(var(--u) * .5); align-items: center; }
.tcg .row .k { color: #8a8f98; }
.tcg .chip { display: inline-flex; align-items: center; gap: calc(var(--u) * .5); padding: calc(var(--u) * .3) calc(var(--u) * 1.1) calc(var(--u) * .3) calc(var(--u) * .6);
  border-radius: calc(var(--u) * 3); background: #1f2937; color: #fff; font: 600 calc(var(--u) * 2.4)/1 "Barlow Condensed", "Arial Narrow", sans-serif; letter-spacing: .03em; text-transform: uppercase; }
.tcg .chip .ic { width: calc(var(--u) * 3); height: calc(var(--u) * 3); color: #fcd34d; }
.tcg .dot { display: inline-block; width: calc(var(--u) * 2.6); height: calc(var(--u) * 2.6); border-radius: 50%; box-shadow: 0 0 0 calc(var(--u) * .25) rgba(0,0,0,.35); }
.tcg .ft { margin-top: auto; display: flex; justify-content: space-between; gap: calc(var(--u) * 1); padding-top: calc(var(--u) * .5);
  border-top: calc(var(--u) * .25) solid rgba(0,0,0,.18); font: 600 calc(var(--u) * 2.1)/1 "Barlow Condensed", "Arial Narrow", sans-serif; letter-spacing: .06em; color: #6b7079; text-transform: uppercase; }
.tcg .ref { margin: 0; padding: 0; list-style: none; display: flex; flex-direction: column; gap: calc(var(--u) * .7); font-size: calc(var(--u) * 2.45); line-height: 1.2; }
.tcg .ref li { display: flex; gap: calc(var(--u) * 1); align-items: flex-start; }
.tcg .ref .ic { flex: none; width: calc(var(--u) * 3.4); height: calc(var(--u) * 3.4); }
/* card back */
.tcg.back { padding: calc(var(--u) * 3); background: radial-gradient(circle at 50% 42%, #24345a, #0f172a 70%); }
.tcg.back .bk { flex: 1; border-radius: calc(var(--u) * 2); border: calc(var(--u) * .5) solid rgba(252,211,77,.75); display: grid; place-items: center; overflow: hidden;
  background: repeating-conic-gradient(from 0deg at 50% 45%, rgba(255,255,255,.035) 0 10deg, transparent 10deg 20deg); }
.tcg.back svg { width: 86%; }
/* programme mat (A6 landscape) */
.mat { --u: var(--card-u, 1mm); box-sizing: border-box; width: calc(var(--u) * 148); height: calc(var(--u) * 105); border-radius: calc(var(--u) * 4); padding: calc(var(--u) * 4);
  display: grid; grid-template-columns: calc(var(--u) * 62) 1fr; gap: calc(var(--u) * 4); color: #16181d; --c: #0C4A6E;
  background: linear-gradient(160deg, color-mix(in srgb, var(--c) 72%, #fff), var(--c) 42%, color-mix(in srgb, var(--c) 55%, #000));
  font-family: "IBM Plex Sans Condensed", "Arial Narrow", sans-serif; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
.mat .side { display: flex; flex-direction: column; gap: calc(var(--u) * 2.5); min-width: 0; }
.mat h3 { margin: 0; color: #fff; font: 800 calc(var(--u) * 6)/1.02 "Bricolage Grotesque", sans-serif; letter-spacing: -.02em; }
.mat .k { color: #bae6fd; font: 700 calc(var(--u) * 2.8)/1 "Barlow Condensed", sans-serif; letter-spacing: .1em; text-transform: uppercase; }
.mat .art { border-radius: calc(var(--u) * 1); overflow: hidden; box-shadow: 0 0 0 calc(var(--u) * .6) rgba(255,255,255,.9); }
.mat .art svg { display: block; width: 100%; }
.mat .brief { margin: 0; color: #e0f2fe; font-size: calc(var(--u) * 3.4); line-height: 1.3; font-style: italic; }
.mat ol { margin: 0; padding: calc(var(--u) * 3); list-style: none; background: linear-gradient(#f8f9f6, #eceee8); border-radius: calc(var(--u) * 2);
  display: flex; flex-direction: column; gap: calc(var(--u) * 2.4); counter-reset: st; }
.mat li { display: grid; grid-template-columns: calc(var(--u) * 8) 1fr; gap: calc(var(--u) * 2); align-items: center; font-size: calc(var(--u) * 3.2); line-height: 1.25; counter-increment: st; }
.mat li .sb { width: calc(var(--u) * 8); height: calc(var(--u) * 8); border-radius: 50%; display: grid; place-items: center; color: #fff; background: var(--s); position: relative; }
.mat li .sb .ic { width: 60%; height: 60%; }
.mat li .sb::after { content: counter(st); position: absolute; right: calc(var(--u) * -1); top: calc(var(--u) * -1); width: calc(var(--u) * 3.6); height: calc(var(--u) * 3.6);
  border-radius: 50%; background: #fcd34d; color: #111; display: grid; place-items: center; font: 700 calc(var(--u) * 2.4)/1 "Barlow Condensed", sans-serif; }
.mat li small { display: block; font: 700 calc(var(--u) * 2.4)/1.2 "Barlow Condensed", sans-serif; letter-spacing: .06em; text-transform: uppercase; color: #6b7079; }
"""


class Ctx:
    """Lookup tables the renderers need (built once from the card data)."""

    def __init__(self, meta, designs, threats, safeguards):
        self.meta = meta
        self.D = {d["id"]: d for d in designs}
        self.T = {t["id"]: t for t in threats}
        self.S = {s["id"]: s for s in safeguards}
        self.SUIT = {s["id"]: s for s in meta["suits"]}
        self.FAM = {f["id"]: f for f in meta["families"]}
        self.CON = {c["id"]: c for c in meta["constraints"]}
        self.dnum = {d["id"]: i + 1 for i, d in enumerate(designs)}


def _name(s):
    n = len(s)
    cls = "s3" if n > 30 else "s2" if n > 24 else "s1" if n > 18 else ""
    return f'<b class="{cls}">{e(s)}</b>'


def _art(fn, uid, color, kind):
    if fn is None:
        inner = art.text(100, 82, kind.upper() + " ART", 16, art.DIM)
    else:
        inner = fn()
    return f'<div class="art">{art.frame(inner, uid, art.shade(color, .12), art.shade(color, -.45))}</div>'


def _suit_badge(cx, sid, big=False):
    s = cx.SUIT[sid]
    return f'<span class="sb" style="--s:{s["color"]}" title="{e(s["name"])}">{art.SUIT_ICONS[sid]}</span>'


def _con_icons(cx, ids):
    return "".join(f'<span title="{e(cx.CON[c]["name"])}">{art.CONSTRAINT_ICONS[c]}</span>' for c in ids)


def design_card(cx, d):
    f = cx.FAM[d["family"]]
    serves = "".join(_suit_badge(cx, s) for s in d["serves"])
    cost = "".join(f'<i class="coin{"" if k < d["cost"] else " off"}"></i>' for k in range(3))
    time = "".join(f'<i class="tick{"" if k < d["time"] else " off"}"></i>' for k in range(3))
    fits = f'<span class="yes">✔ {_con_icons(cx, d["fits"])}</span>' if d["fits"] else ""
    strug = f'<span class="no">✘ {_con_icons(cx, d["struggles"])}</span>' if d["struggles"] else ""
    weak = " · ".join(e(cx.T[t]["name"]) for t in d["weak_vs"][:2])
    return f'''<div class="tcg tcg-d" style="--c:{f["color"]}">
  <div class="nm">{_name(d["name"])}<span class="attr">{art.SUIT_ICONS[d["serves"][0]]}</span></div>
  <div class="lv"><span>{serves}</span><span>{cost}&nbsp;{time}</span></div>
  {_art(art.DESIGN_ART.get(d["id"]), "d-" + d["id"], f["color"], "design")}
  <div class="tb">
    <div class="ty">[ {e(f["name"])} / Design ]</div>
    <p class="fx">{e(d["short"])}</p>
    <div class="row">{fits}{strug}</div>
    <div class="row"><span class="k">Weak vs</span> {weak}</div>
    <div class="ft"><span>MTH-D{cx.dnum[d["id"]]:02d}</span><span>● cost &nbsp;◆ time</span></div>
  </div>
</div>'''


def question_card(cx, q):
    s = cx.SUIT[q["suit"]]
    chips = "".join(f'<span class="chip">{art.CONSTRAINT_ICONS[c]}{e(cx.CON[c]["name"])}</span>' for c in q["constraints"])
    stars = "".join(f'<span class="star{"" if k < q["difficulty"] else " off"}">★</span>' for k in range(3))
    return f'''<div class="tcg tcg-q" style="--c:{s["color"]}">
  <div class="nm">{_name(q["title"])}<span class="attr">{art.SUIT_ICONS[q["suit"]]}</span></div>
  <div class="lv"><span>{e(s["name"])} question</span><span>{stars}</span></div>
  {_art(QUESTION_ART.get(q["id"]), "q-" + q["id"], s["color"], "question")}
  <div class="tb">
    <div class="ty">[ {e(q["field"])} ]</div>
    <p class="fx">{e(q["text"])}</p>
    <div class="row">{chips}</div>
    <div class="ft"><span>MTH-{q["id"]}</span><span>Which design answers it?</span></div>
  </div>
</div>'''


def threat_card(cx, t, n):
    by = " · ".join(e(cx.S[s]["name"]) for s in t["countered_by"][:2])
    return f'''<div class="tcg tcg-t" style="--c:{THREAT_COLOR}">
  <div class="nm">{_name(t["name"])}<span class="attr">{_warn_icon()}</span></div>
  <div class="lv"><span>Threat</span><span>Play on a design</span></div>
  {_art(THREAT_ART.get(t["id"]), "t-" + t["id"], THREAT_COLOR, "threat")}
  <div class="tb">
    <div class="ty">[ Threat / Bias ]</div>
    <p class="fx">{e(t["short"])}</p>
    <div class="row"><span class="k">Countered by</span> {by}</div>
    <div class="ft"><span>MTH-B{n:02d}</span><span>Validity threat</span></div>
  </div>
</div>'''


def safeguard_card(cx, s, n):
    counters = " · ".join(e(cx.T[t]["name"]) for t in s["counters"][:2])
    if "any" in s["applies_to"]:
        fams = '<span class="k">Any design</span>'
    else:
        fams = "".join(f'<span class="dot" style="background:{cx.FAM[f]["color"]}" title="{e(cx.FAM[f]["name"])}"></span>' for f in s["applies_to"])
    return f'''<div class="tcg tcg-s" style="--c:{SAFEGUARD_COLOR}">
  <div class="nm">{_name(s["name"])}<span class="attr">{_shield_icon()}</span></div>
  <div class="lv"><span>Safeguard</span><span>Answer a threat</span></div>
  {_art(SAFEGUARD_ART.get(s["id"]), "s-" + s["id"], SAFEGUARD_COLOR, "safeguard")}
  <div class="tb">
    <div class="ty">[ Safeguard ]</div>
    <p class="fx">{e(s["short"])}</p>
    <div class="row"><span class="k">Counters</span> {counters}</div>
    <div class="row"><span class="k">Usable with</span> {fams}</div>
    <div class="ft"><span>MTH-S{n:02d}</span><span>Defence</span></div>
  </div>
</div>'''


def twist_card(cx, x):
    if x["adds"]:
        c = cx.CON[x["adds"]]
        add = f'<div class="row"><span class="k">Adds</span> <span class="chip">{art.CONSTRAINT_ICONS[c["id"]]}{e(c["name"])}</span></div>'
        kind = "Constraint"
    else:
        add, kind = "", "Event"
    return f'''<div class="tcg tcg-x" style="--c:{TWIST_COLOR}">
  <div class="nm">{_name(x["name"])}<span class="attr">{_twist_icon()}</span></div>
  <div class="lv"><span>Twist</span><span>{kind}</span></div>
  {_art(TWIST_ART.get(x["id"]), "x-" + x["id"], TWIST_COLOR, "twist")}
  <div class="tb">
    <div class="ty">[ Twist / {kind} ]</div>
    <p class="fx">{e(x["text"])}</p>
    {add}
    <div class="ft"><span>MTH-{x["id"]}</span><span>Flip after designs are revealed</span></div>
  </div>
</div>'''


def program_mat(cx, p):
    stages = "".join(f'<li><span class="sb" style="--s:{cx.SUIT[s["suit"]]["color"]}">{art.SUIT_ICONS[s["suit"]]}</span>'
                     f'<span><small>{e(cx.SUIT[s["suit"]]["name"])}</small>{e(s["ask"])}</span></li>' for s in p["stages"])
    fn = PROGRAM_ART.get(p["id"])
    inner = fn() if fn else art.text(100, 82, "PROGRAMME ART", 16, art.DIM)
    return f'''<div class="mat">
  <div class="side"><span class="k">Research programme · {e(p["id"])}</span><h3>{e(p["name"])}</h3>
    <div class="art">{art.frame(inner, "p-" + p["id"], art.shade(PROGRAM_COLOR, .12), art.shade(PROGRAM_COLOR, -.45))}</div>
    <p class="brief">{e(p["brief"])}</p></div>
  <ol>{stages}</ol>
</div>'''


def reference_cards(cx):
    m = cx.meta
    suits = "".join(f'<li><span class="sb" style="--s:{s["color"]}">{art.SUIT_ICONS[s["id"]]}</span><span><b>{e(s["name"])}</b> {e(s["ask"])}</span></li>' for s in m["suits"])
    cons = [f'<li>{art.CONSTRAINT_ICONS[c["id"]]}<span><b>{e(c["name"])}</b> {e(c["text"])}</span></li>' for c in m["constraints"]]
    fams = "".join(f'<li><span class="dot" style="background:{f["color"]}"></span><span>{e(f["name"])}</span></li>' for f in m["families"])
    sc = m["scoring"]
    half = (len(cons) + 1) // 2

    def card(title, body, color="#334155"):
        return f'''<div class="tcg tcg-r" style="--c:{color}"><div class="nm"><b class="s1">{e(title)}</b></div>
  <div class="tb">{body}</div></div>'''
    score = (f'<ul class="ref"><li>🥇 <span><b>Best</b> +{sc["best"]}</span></li><li>🥈 <span><b>Defensible</b> +{sc["ok"]}</span></li>'
             f'<li>⚠️ <span><b>Trap</b> {sc["trap"]}</span></li><li>⚖️ <span><b>Unlisted</b> {sc["unlisted"]}, or +{sc["appeal_win"]} if the table upholds your appeal</span></li></ul>')
    return [card("Suits: the question", f'<ul class="ref">{suits}</ul>'),
            card("Constraints 1/2", f'<ul class="ref">{"".join(cons[:half])}</ul>'),
            card("Constraints 2/2", f'<ul class="ref">{"".join(cons[half:])}</ul>'),
            card("Families & scoring", f'<ul class="ref">{fams}</ul>{score}')]


def card_back():
    logo = ('<svg viewBox="0 0 120 150" xmlns="http://www.w3.org/2000/svg">'
            '<rect x="20" y="16" width="80" height="92" rx="6" fill="#0f172a" stroke="#FCD34D" stroke-width="3"/>'
            '<text x="28" y="34" font-size="11" fill="#FCD34D" font-family="Barlow Condensed, sans-serif" font-weight="700">46</text>'
            '<text x="60" y="80" font-size="44" fill="#F8FAFC" text-anchor="middle" font-family="Bricolage Grotesque, sans-serif" font-weight="800">Me</text>'
            '<text x="60" y="98" font-size="9" fill="#94A3B8" text-anchor="middle" font-family="Barlow Condensed, sans-serif" font-weight="700" letter-spacing="2">METHOD</text>'
            '<text x="60" y="134" font-size="17" fill="#F8FAFC" text-anchor="middle" font-family="Bricolage Grotesque, sans-serif" font-weight="800" letter-spacing="1">METHODICAL</text>'
            '<text x="60" y="146" font-size="7" fill="#FCD34D" text-anchor="middle" font-family="Barlow Condensed, sans-serif" font-weight="700" letter-spacing="1.5">THE RESEARCH DESIGN CARD GAME</text></svg>')
    return f'<div class="tcg back" style="--c:{BACK_COLOR}"><div class="bk">{logo}</div></div>'


def _warn_icon():
    return art._icon('<path d="M12 3 2 20h20z"/><path d="M12 10v4"/><circle cx="12" cy="17" r=".7" fill="currentColor"/>')


def _shield_icon():
    return art._icon('<path d="M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6z"/><path d="m9 12 2 2 4-4"/>')


def _twist_icon():
    return art._icon('<path d="M4 12a8 8 0 0 1 14-5.3L20 9"/><path d="M20 4v5h-5"/><path d="M20 12a8 8 0 0 1-14 5.3L4 15"/><path d="M4 20v-5h5"/>')
