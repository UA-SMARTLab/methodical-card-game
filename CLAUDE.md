# Methodical: working notes for Claude

Methodical is the first game of the **SMART-Lab Science Game Kit**: card games that help researchers refresh their
research-methods knowledge. Its siblings (Red Flag, Major Revisions) copy the conventions below, so all kit games look
and work alike. My general rules are in `~/.claude/CLAUDE.md`; this file adds what is specific to the kit.

## The kit: what every game shares

### Front door
- The kit homepage is its own repo, github.com/UA-SMARTLab/science-game-kit (Pages: ua-smartlab.github.io/science-game-kit/),
  one hand-written `index.html`. Each game keeps its own repo and Pages site; its app header links back to the
  homepage (`kit.link` in `ui.json`). After a game's cards change, rebuild the game, then re-render the homepage's card
  pictures with that repo's `tools/card_images.py`. A new game gets a tile there and a line in the UA-SMARTLab profile README.

### Architecture
- Static site, no server, no dependencies. Python standard library only for tooling.
- `data/*.json` holds every deck; the code never contains card text. `tools/build.py` validates the data (fails on
  errors, warns on weak spots: every answer used, every weakness answerable, ids resolve) and generates:
  `app/index.html` (from `app/template.html`), `app/<code>/index.html` per language, `print/` sheets and the answer key.
  Generated files are never edited by hand.
- `tools/cards.py` draws cards as HTML; `tools/art*.py` draws each card's picture as inline SVG (viewBox 200×150,
  `preserveAspectRatio="xMidYMid slice"`). The picture box's shape differs by card type, so how much of the top and
  bottom is cut off differs too: in Methodical only y 20–130 shows on Questions, 9–141 on Methods, 3–147 on Twists and
  Safeguards, all of it on Threats. Measure, don't assume: `tools/check_cards.py` flags any picture label cut off.
- `tools/i18n.py`: English is the source. `i18n/en/ui.json` holds interface strings under stable keys;
  `i18n/en/cards.json` is generated from `data/`. Each language has `i18n/<code>/{ui.json, cards.json, GLOSSARY.md}`;
  anything missing falls back to English. `i18n/languages.json` lists languages (en, fr, nl, de, ar; ar is RTL).
- Feature flags (`FEATURES` in the template) hide unfinished modes without deleting their code.
- Launchers for Windows, Mac and Ubuntu; `.claude/launch.json` serves `app/` on 127.0.0.1.

### Card look (identical across the kit)
- Size 63×88 mm. Everything scales with `--u` (1 mm in print, `--card-u` on screen).
- Top to bottom: name bar (Bricolage Grotesque 800) with an attribute badge; level row; picture box; text box with a
  type line `[ FAMILY / TYPE ]` (Barlow Condensed, upper case), one sentence of effect text (IBM Plex Sans Condensed),
  labelled rows (grey upper-case label, then content: e.g. "Good for", "Struggles with", "Weak vs"), footer with the
  card code (MTH-D01) and a legend.
- Text that runs long shrinks to fit (`fitCards`, never below 72%). After `build.py`, run `tools/check_cards.py`
  (headless Chrome or Edge, all print sheets): no text box, name or picture label overflows in any language. Every kit
  game has the same file. A long single-word name (Dutch and German compounds) gets a soft hyphen (U+00AD) where it
  may break.
- Colour language: concept cards take their family's colour; prompt cards (Questions) are one neutral colour
  (#40402C) so colour never gives the answer away; Threats crimson #9F1239, Safeguards emerald #047857, Twists violet
  #6D28D9, Programmes #0C4A6E, backs #0F172A.
- Pictures are diagrams of the idea itself, drawn by us, never copied.
- Each game keeps the same frame and fonts but has its own accent colour and card back, with the kit mark
  "SMART-Lab Science Game Kit", so a stray card can be sorted back into its game.

### App
- Pages: Home (lively: fanned cards, live counts, a quick question), Play, Browse the decks, language picker.
- Play: one prompt card, four answer choices shown as whole cards. Tapping a card opens it full screen; only the big
  green "Pick this card" button answers. The result reacts on the cards themselves (badges, "Your pick", confetti for
  the best answer), then explains, then links the key reference. "Deal another question" is highlighted afterwards.
- Every concept card has a "?" that opens the paper or standard that defines it (`ref: {cite, url}`, https only,
  checked against Crossref). Hover enlarges cards on desktop; the full-screen viewer serves phones.
- Light and dark themes through CSS tokens; WCAG 2.2 AA; works at 320 px wide and sideways on phones.

### Content
- Three-tier answer keys: best, defensible, trap (each trap states why it fails). Unlisted answers can be appealed at
  the table.
- Real historical examples, never invented ones presented as real. Every factual claim and reference is verified, not
  written from memory.
- Terminology: the cards you pick are **Methods** (not "designs"); "study design" only where it is the precise term.
  One term per concept across cards, interface, rules and every language (see each GLOSSARY.md).
- Translations by meaning, with the field's established terms, reviewed by an independent pass.

### Licence (all kit games)
- Content (cards, art, rules, print sheets): CC BY-NC-SA 4.0. Software: PolyForm Noncommercial 1.0.0.
  Copyright Abdulhamid Baghdadi; developed at SMART-Lab, Universiteit Antwerpen. Commercial use only with written
  permission. See LICENSE.md and LICENSES/.

## Methodical specifics
- Decks: Questions, Methods (`data/designs.json`, id kept for compatibility), Threats, Safeguards, Twists, Programmes.
- Repo: github.com/UA-SMARTLab/methodical-card-game (public); Pages serves `/app/`. A private playable copy lives at
  claude.ai/artifact/5jwbrfQKQgZPq9nB8i91Zu; rebuild it with `python tools/build.py --artifact <file>` and republish
  after app changes.
- Next steps: DESIGN.md §7.
