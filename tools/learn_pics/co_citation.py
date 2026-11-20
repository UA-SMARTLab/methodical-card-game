"""Co-citation analysis: the five steps' pictures, and the "count the links" exercise it shares with bibliographic
coupling (the two are mirror images on the same citation graph, so one exercise serves both pages)."""
import html
import json

from learn_pics._kit import INK, DIM, ACC, HOT, COOL, g, rect, text, arrow, line, doc, RNG_JS

e = html.escape

CITED = [(30, 22), (75, 22), (120, 22), (165, 22)]    # older works, top row
CITING = [(40, 104), (100, 104), (160, 104)]          # later papers, bottom row
# Which cited works each later paper cites (by index into CITED).
REFS = [(0, 1), (0, 1, 2), (1, 3)]


def _graph(hi_cited=(), hi_citing=(), c=ACC):
    out = ""
    for p, refs in enumerate(REFS):
        for r in refs:
            on = r in hi_cited and (not hi_citing or p in hi_citing) or (p in hi_citing and not hi_cited)
            out += arrow(CITING[p][0], CITING[p][1] - 4, CITED[r][0], CITED[r][1] + 30, c if on else DIM, 2 if on else 1.5, head=5)
    out += "".join(doc(x - 11, y, 22, 28, ACC if k in hi_cited else INK, 0, "#0f172a", 2) for k, (x, y) in enumerate(CITED))
    out += "".join(doc(x - 11, y, 22, 28, COOL if k in hi_citing else DIM, 2, "#0f172a44", 2) for k, (x, y) in enumerate(CITING))
    return out


def collect():
    # A field's later papers and the older works their reference lists point to.
    out = "".join(g("pop", doc(x - 11, y, 22, 28, DIM, 2, "#0f172a44", 2), k) for k, (x, y) in enumerate(CITING))
    out += "".join(g("draw", "".join(arrow(CITING[p][0], CITING[p][1] - 4, CITED[r][0], CITED[r][1] + 30, DIM, 1.5, head=5) for r in refs), 3 + p)
                   for p, refs in enumerate(REFS))
    out += "".join(g("pop", doc(x - 11, y, 22, 28, INK, 0, "#0f172a", 2), 6 + k) for k, (x, y) in enumerate(CITED))
    return out + text(100, 144, "later papers cite older works", 11, DIM)


def count():
    # Works A and B are cited together by two later papers: their co-citation count is 2.
    out = _graph()
    out += g("pop", _graph((0, 1), (0, 1)), 1)
    out += g("pop", text(52, 64, "A + B", 13, ACC), 2) + g("pop", text(146, 76, "cited together", 11, ACC), 3)
    return out + g("pop", text(100, 144, "co-citation = 2", 13, ACC), 4)


def cluster():
    # Count every pair, keep the strong links: works that are often cited together pull into a cluster.
    pts = [(40, 40), (70, 30), (58, 66), (140, 46), (166, 74), (132, 90)]
    out = ""
    for k, (a, b, w) in enumerate(((0, 1, 5), (0, 2, 4), (1, 2, 3), (3, 4, 4), (4, 5, 3), (3, 5, 5), (2, 5, 1))):
        out += g("draw", line([pts[a], pts[b]], ACC if w > 1 else DIM, w), k)
    for k, (x, y) in enumerate(pts):
        out += g("pop", doc(x - 9, y - 12, 18, 24, INK, 0, "#0f172a", 2), k)
    return out + g("pop", text(56, 112, "school 1", 12, ACC) + text(150, 122, "school 2", 12, ACC), 7)


def base():
    # The clusters are the field's intellectual base: the older works it builds on.
    out = rect(18, 92, 164, 34, "#0f172a66", ACC, 2.5, 4) + text(100, 114, "intellectual base", 13, ACC)
    for k, x in enumerate((44, 82, 120, 158)):
        out += g("grow", rect(x - 12, 56, 24, 34, "#0f172a", INK, 2, 2), k)
    out += g("pop", text(100, 34, "what the field stands on", 11, INK), 5)
    return out


def lag():
    # A paper published today has no citations yet, so it cannot be co-cited: it is invisible to the map.
    out = line([(18, 120), (182, 120)], DIM, 2) + text(100, 140, "time", 11, DIM)
    for k, (x, h) in enumerate(((36, 70), (78, 48), (120, 22))):
        out += g("grow", rect(x - 10, 120 - h, 20, h, ACC, "none", 0, 2), k)
    out += g("pop", doc(152, 70, 24, 32, INK, 0, "#0f172a", 2) + text(164, 62, "new", 12, HOT), 3)
    out += g("pop", text(164, 114, "0 links", 11, HOT), 4)
    return out + text(78, 30, "citations pile up", 11, ACC)


PICTURES = {"collect": collect, "count": count, "cluster": cluster, "base": base, "lag": lag}


def exercise(ex, quote):
    """Return (html, js). Example citation graph: pick two works (co-citation) or two papers (coupling) and count."""
    body = f"""
  <p>{e(ex["intro"])}</p>
  <div class="controls" role="group" aria-label="What to count">
    <button type="button" data-mode="co">Co-citation: two cited works</button>
    <button type="button" data-mode="bc">Coupling: two citing papers</button>
    <button type="button" id="today">Publish a paper today</button>
  </div>
  <div class="controls"><label>First <select id="a"></select></label> <label>Second <select id="b"></select></label></div>
  <svg id="graph" viewBox="0 0 400 230" role="img" aria-label="Citation graph" style="width:100%;max-width:640px;display:block"></svg>
  <p class="verdict" id="verdict" aria-live="polite"></p>
  <p class="note">{e(ex["data_label"])}</p>"""
    js = RNG_JS + "const X = " + json.dumps(ex) + ";\n" + r"""
let mode = X.mode, papers = X.papers.map(p => ({ ...p })), added = false;
const works = X.works;
function opts() {
  const list = mode === "co" ? works.map(w => w.id).concat(added ? ["NEW"] : []) : papers.map(p => p.id);
  for (const [k, def] of [["a", 0], ["b", 1]]) {
    const s = $(k), keep = s.value;
    s.innerHTML = list.map(v => `<option>${v}</option>`).join("");
    s.value = list.includes(keep) ? keep : list[def];
  }
}
function draw() {
  const a = $("a").value, b = $("b").value, svg = [];
  const wx = i => 40 + i * (320 / Math.max(1, works.length - 1 + (added ? 1 : 0)));
  const px = i => 40 + i * (320 / Math.max(1, papers.length - 1));
  const allWorks = works.map(w => w.id).concat(added ? ["NEW"] : []);
  let n = 0;
  papers.forEach((p, i) => p.refs.forEach(r => {
    const j = allWorks.indexOf(r);
    const on = mode === "co" ? (p.refs.includes(a) && p.refs.includes(b) && (r === a || r === b))
                             : ((p.id === a || p.id === b) && papers.find(q => q.id === (p.id === a ? b : a)).refs.includes(r));
    svg.push(`<line x1="${px(i)}" y1="180" x2="${wx(j)}" y2="50" stroke="${on ? "#B45309" : "currentColor"}" stroke-opacity="${on ? 1 : .25}" stroke-width="${on ? 3 : 1.5}"/>`);
  }));
  allWorks.forEach((w, j) => svg.push(`<rect x="${wx(j) - 18}" y="22" width="36" height="28" rx="4" fill="${mode === "co" && (w === a || w === b) ? "#B45309" : "#64748b"}"/><text x="${wx(j)}" y="41" text-anchor="middle" fill="#fff" font-size="13">${w}</text>`));
  papers.forEach((p, i) => svg.push(`<rect x="${px(i) - 22}" y="180" width="44" height="28" rx="4" fill="${mode === "bc" && (p.id === a || p.id === b) ? "#0369A1" : "#64748b"}"/><text x="${px(i)}" y="199" text-anchor="middle" fill="#fff" font-size="13">${p.id}</text><text x="${px(i)}" y="224" text-anchor="middle" fill="currentColor" font-size="11">${p.year}</text>`));
  svg.push(`<text x="4" y="14" fill="currentColor" font-size="11">cited works</text><text x="4" y="172" fill="currentColor" font-size="11">citing papers</text>`);
  $("graph").innerHTML = svg.join("");
  if (a === b) { $("verdict").textContent = "Pick two different ones."; return; }
  if (mode === "co") {
    n = papers.filter(p => p.refs.includes(a) && p.refs.includes(b)).length;
    $("verdict").textContent = `${a} and ${b} are cited together by ${n} later paper${n === 1 ? "" : "s"}: co-citation strength ${n}.` +
      (a === "NEW" || b === "NEW" ? " The new paper has not been cited by anyone yet, so co-citation cannot see it." : "");
  } else {
    const pa = papers.find(p => p.id === a), pb = papers.find(p => p.id === b);
    n = pa.refs.filter(r => pb.refs.includes(r)).length;
    $("verdict").textContent = `${a} and ${b} share ${n} reference${n === 1 ? "" : "s"}: coupling strength ${n}. This was fixed the day the later of the two appeared.`;
  }
  document.querySelectorAll("[data-mode]").forEach(x => x.setAttribute("aria-pressed", x.dataset.mode === mode));
  $("today").hidden = added;
}
document.querySelectorAll("[data-mode]").forEach(x => x.onclick = () => { mode = x.dataset.mode; opts(); draw(); });
$("today").onclick = () => { added = true; papers.push({ ...X.new_paper }); opts(); if (mode === "co") $("b").value = "NEW"; else $("b").value = X.new_paper.id; draw(); };
$("a").onchange = draw; $("b").onchange = draw;
opts(); draw();
"""
    return body, js
