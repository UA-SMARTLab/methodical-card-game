# Learn pages: the brief (20 Nov 2026)

Every Method card gets a page that shows how the Method works, step by step, with moving pictures, so a player who
doesn't know it can open the card and learn. The finished example is the randomized controlled trial:
`data/learn/rct.json`, `tools/learn_pics/rct.py`, built to `app/learn/rct/index.html`. Copy its shape, not its
words.

**The readers are scientists** (the user, 20 Nov 2026): explanations must be citation-based. Quote the defining
sentence word for word wherever you can, and say which paper and which place in it (page, section, item, box) it
comes from.

## What you write, per Method (and nothing else)

1. `data/learn/<id>.json`, in this shape:
   - `method`: the card id.
   - `question`: the question the Method answers, in a few plain words.
   - `sources`: keyed by a short name. Each has `cite` (Author (Year). Title. Journal volume: pages), `short`
     ("Author (Year)" or "Author et al. (Year)"), `url` (https, preferably a DOI), and `checked` (what you read,
     where, and the date, e.g. "read in the PMC full text (PMC1234567) on 20 Nov 2026").
   - `steps`: 3 to 7 steps. Each has:
     - `id`, `title` (one to three words), and `text` (one or two short sentences in our own words);
     - `picture`, a key into your module's PICTURES;
     - `quotes`: a list of `{text, source, where}`, word for word, at most about 40 words each. In-text reference
       numbers may be left out (say so in the source's `checked`); trimmed ends are fine, but never change a word
       inside;
     - only when no source could be read word for word for this step: `after` (`{source, where}`) instead of
       `quotes`. It shows as "After Author (Year), place". At least one step on every page must quote.
   - optional `threat_quotes`: a defining quote for one of the card's `weak_vs` threats, keyed by threat id.
   - optional `exercise`: `title`, `intro`, an optional `quote`, `data_label`, and whatever your module needs. Add one
     only where acting it out teaches more than the pictures do. Methods argued in words get none.
   - `limits`: what the page leaves out or could not check, honestly.
2. `tools/learn_pics/<id with - replaced by _>.py`:
   - `PICTURES`: name → function returning SVG inner markup for a 200 × 150 frame.
   - Optional `exercise(ex, quote) -> (html, js)`. The JS must be plain, with no libraries. Randomness comes from the
     seeded `rng` in `RNG_JS`. Data is real, or labelled as example data on the page.
   - Import helpers from `learn_pics._kit` (`g`, `person`, `rect`, `text`, `arrow`, `line`, `circle`, `path`, `dice`,
     `doc`, `crowd`, `carrow`, colours `INK DIM FAINT ACC HOT COOL TREAT CONTROL`). Read `tools/art.py` for the
     primitives' signatures, and the card's own picture function there (`art_<id>` in `DESIGN_ART`) to stay
     consistent with the card.

Do not edit any other file: not `learn.py`, `build.py`, the decks, the app, or another Method's files. If you need
something shared, say so in your report.

## Pictures

- Each picture shows that step's concrete thing, never a generic symbol, and no two steps share a picture.
- Make it move: wrap shapes in `g("pop"|"draw"|"grow"|"fade"|"roll", inner, i)`. The last frame must be the whole
  picture.
- Labels are one to three words, at least 11 px, and stay inside the frame (x 6–194, y 14–144). The frame is dark,
  so use the art colours.

## Sources: what counts, and how to read them

- Prefer the paper that defines the Method (the card's `ref` in `data/designs.json`), its reporting guideline
  (EQUATOR: CONSORT, STROBE, STARD, TRIPOD, PRISMA, PRISMA-ScR, RAMESES, COREQ, SRQR, CHEERS…) or a standard
  textbook chapter whose text you can read.
- Read the text before quoting it. Never quote from memory.
- Routes that work from here:
  - The Europe PMC REST API: `https://www.ebi.ac.uk/europepmc/webservices/rest/<PMCID>/fullTextXML`. Find a PMCID
    with `https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:<doi>&format=json&resultType=core`.
  - Publishers' open-access HTML.
  - The user's research library, read-only: `C:\Users\A-Bag\Desktop\Obsidian Research Library\00 - Library\PDF text`
    (text copies of PDFs, numbered).
  - PMC article pages (`https://pmc.ncbi.nlm.nih.gov/articles/<PMCID>/`) read well in Claude in Chrome
    (`mcp__claude-in-chrome__*`; load those tools with ToolSearch). Open your own tab, extract passages with
    `javascript_tool` (search `document.querySelector('article').innerText` for a phrase and return about 600
    characters at a time, because long results get cut off), and close your tab when you are done. Other helpers
    use the same Chrome, so never touch tabs you didn't open.
- pmc.ncbi.nlm.nih.gov shows a bot check to plain fetchers (WebFetch, curl). Do not download files, and do not get past bot checks or
  CAPTCHAs.
- If you cannot read a defining source, use `after` with a source you did read, and say so in `limits`. Never invent
  a page number.

## Check before you report

- `python tools/learn.py <id> --out <your scratch folder>` builds without error for each of your Methods.
- Python standard library only. UTF-8, LF line endings. Write files with your file tools.
