# Find your method: sources for the top of the tree

How published typologies name the purposes of research, checked on 2026-11-16 for the "Find your method" page. The game uses these in `data/method-tree.json`; the method-family and research-field sources are in `method-tree-taxonomies.md`.
Each entry says what was read and how. Nothing here is from memory.

**In use since 2026-11-17:** Gregor (2006) for the kinds of question, MeSH 2026 for the tools and the time terms
(Cross-Sectional D003430, Longitudinal D008137, Prospective D011446 and Retrospective Studies D012189; scope notes read
through the NLM MeSH API), and Timmermans & Tavory (2012) with Suddaby (2006) for the approach to theory. Saunders et
al. (2019) and Grimes & Schulz (2002) were dropped to keep the references few; their entries below stay as the record.

## Verified

| Source | What it classifies | Its categories (own words) | How checked |
|---|---|---|---|
| Saunders, Lewis & Thornhill (2019). *Research Methods for Business Students*, Pearson, §5.7, pp. 186–188 | Purposes of a research design | **Exploratory** ("ask open questions to discover what is happening"), **descriptive** ("gain an accurate profile of events, persons or situations"), **explanatory** ("establish causal relationships between variables"), **evaluative** ("find out how well something works"), and combinations | Read the chapter pages (PDF excerpt of ch. 5, pp. 172–200) |
| Saunders et al. (2019), Figure 5.1 (the research onion) | Time horizon, a later layer than purpose | **Cross-sectional**, **longitudinal** | Seen in the figure; §5.9 itself was not in the excerpt |
| Gregor (2006). The Nature of Theory in Information Systems. *MIS Quarterly* 30(3): 611–642. [doi:10.2307/25148742](https://doi.org/10.2307/25148742) | Goals of theory (what research is for) | Four goals (p. 619): **analysis and description**, **explanation**, **prediction**, **prescription**. Five types (Table 2, p. 620): I Analysis ("says what is"), II Explanation ("says what is, how, why, when, and where"), III Prediction ("says what is and what will be"), IV Explanation and prediction, V **Design and action** ("says how to do something") | Read pp. 611, 619, 620 of the published PDF (ANU repository); DOI checked with Crossref |
| Shmueli (2010). To Explain or to Predict? *Statistical Science* 25(3): 289–310. [doi:10.1214/10-STS330](https://doi.org/10.1214/10-STS330) | Goals of statistical modelling | **Causal explanation**, **prediction**, **description**; argues explanation and prediction must not be conflated | Abstract (arXiv 1101.0891); DOI checked with Crossref |
| Hernán, Hsu & Healy (2019). A Second Chance to Get Causal Inference Right: A Classification of Data Science Tasks. *CHANCE* 32(1). [doi:10.1080/09332480.2019.1579578](https://doi.org/10.1080/09332480.2019.1579578) | Data-science tasks | **Description**, **prediction**, **counterfactual prediction** (which "includes causal inference") | Abstract (arXiv 1804.10846); DOI checked with Crossref |
| Grimes & Schulz (2002). An overview of clinical research: the lay of the land. *Lancet* 359: 57–61. [doi:10.1016/S0140-6736(02)07283-5](https://doi.org/10.1016/S0140-6736(02)07283-5) | Study designs (not purposes) | **Experimental** vs **observational** (does the investigator assign the exposure?); observational splits into **analytical** (has a comparison group) and **descriptive** | DOI checked with Crossref; abstract wording from secondary copies of the abstract, not the article itself |
| Grant & Booth (2009). A typology of reviews. *Health Information and Libraries Journal* 26(2): 91–108. [doi:10.1111/j.1471-1842.2009.00848.x](https://doi.org/10.1111/j.1471-1842.2009.00848.x) | Review types (secondary research) | 14 review types | DOI checked with Crossref; abstract via secondary summaries |
| Euser et al. (2009). Cohort Studies: Prospective versus Retrospective. *Nephron Clinical Practice*. [doi:10.1159/000235241](https://doi.org/10.1159/000235241) | Direction in time | **Prospective**, **retrospective** | Abstract from Crossref |

## Not verified (searched, not read)

- SAGE Encyclopedia of Social Science Research Methods (Lewis-Beck, Bryman & Liao, 2004), browsed on SAGE Research Methods
  (full text needs an institutional sign-in): it is arranged by term and method, not by research purpose. There is an entry
  **Explanation** ([doi:10.4135/9781412950589.n314](https://doi.org/10.4135/9781412950589.n314)); its open preview defines a
  scientific explanation as an argument showing *why* an event or regularity came to pass (covering-law model). No entry
  "Exploratory Research" exists (its URL returns "does not exist"), and none for "Explanatory Research" (the entry after
  "Explanation" is "Explanatory Variable"). So it offers no typology of purposes to adopt.
- Selltiz, Jahoda, Deutsch & Cook (1959), *Research Methods in Social Relations*: could not read its classification of study purposes.

## What the sources agree on

- **Description, explanation, prediction** appear in every typology that covers them (Gregor, Shmueli, Hernán et al.; Saunders has description and explanation).
- **"Explanatory" means causal** in Saunders et al. ("causal relationships"), Shmueli ("causal explanation") and Hernán et al. ("causal inference"). Gregor's "explanation" is broader: how, why, when and where.
- **Exploratory** and **evaluative** come from the social-science purposes (Saunders et al.).
- **Design** is a goal of its own in Gregor ("design and action", "prescription"), not a kind of evaluation.
- **Review** (secondary research) sits outside these purpose typologies; Grant & Booth classify reviews.
- **Association** and **measurement** are not purposes in any of these typologies. Association is what epidemiology's *analytical* observational studies examine (Grimes & Schulz); measurement studies are a kind of study, not a goal of research in these schemes.

## Reasoning: deductive, inductive, abductive (checked 2026-11-17)

**Sources in use** (since 2026-11-17, at the user's request: peer-reviewed and few, in place of the textbook below):

| Source | Used for | Checked |
|---|---|---|
| Timmermans & Tavory (2012). Theory construction in qualitative research: from grounded theory to abductive analysis. *Sociological Theory* 30(3): 167–186. [doi:10.1177/0735275112457914](https://doi.org/10.1177/0735275112457914) | The three logics side by side (pp. 170–171): deduction "begins with a rule and proceeds through a case"; induction "starts with a collection of given cases"; abduction "starts with consequences and then constructs reasons". Abduction needs a finding surprising "in light of existing theories" (p. 169). How the three work together (p. 171). | Read pp. 169–171 ourselves, in a copy hosted by mackenzie.br (not the publisher's); DOI checked with Crossref |
| Suddaby (2006). From the editors: What grounded theory is not. *Academy of Management Journal* 49(4): 633–642. [doi:10.5465/amj.2006.22083020](https://doi.org/10.5465/amj.2006.22083020) | The deciding rule for the inductive answer: grounded theory "is best used when no explicit hypotheses exist to be tested" (p. 636, citing Martin & Turner 1986) | Read p. 636 ourselves, in a JSTOR copy hosted by uga.edu; DOI checked with Crossref |

Considered and not used: the SAGE Encyclopedia entries "Deduction", "Induction", "Abduction" (previews only, no author
shown; its "Abduction" is the interpretivist sense, not Peirce's); the Stanford Encyclopedia of Philosophy, "Abduction"
(Douven), which is open and authoritative but mainly about inference to the best explanation, not research design;
Ketokivi & Mantere (2010), Blaikie (2010) and Van Maanen et al. (2007), not read (no open copy). Checked by a research
subagent; the two in use were then read by us.

**Replaced** (2026-11-17), kept here as the record of what was checked: the approaches came from Saunders, Bristow, Thornhill & Lewis (2019), "Understanding research philosophy and approaches
to theory development", ch. 4 of *Research Methods for Business Students*, 8th ed., §4.5, pp. 152–158
([ORO record](https://oro.open.ac.uk/66370/)). Read in the authors' own copy (ResearchGate, an uncorrected proof dated
29/01/2019, so page numbers may differ slightly in print). Table 4.4 (p. 153) sets out deduction, induction and
abduction: their logic, how they generalise, how they use data, and what they do to theory. Pages 155–157 say a study
can combine them and that the choice "depends" on the researcher's philosophy and the topic. The chapter's learning
goals also name a fourth approach, retroduction, which p. 156 treats as another name for abduction among critical
realists. The chapter assigns no Methods, so each Method's mark rests on its own source:

| Method | Mark | Basis | Source, location | How read |
|---|---|---|---|---|
| Randomised trial | deductive | named | Moher et al. (2010), CONSORT 2010 E&E, item 2b, [doi:10.1136/bmj.c869](https://doi.org/10.1136/bmj.c869) | Full text (PMC2844943); quote rechecked by us |
| A/B test | deductive | named | Kohavi, Henne & Sommerfield (2007), §1, [doi:10.1145/1281192.1281295](https://doi.org/10.1145/1281192.1281295) | pp. 1–2 |
| Nomological network | deductive | named | Cronbach & Meehl (1955), "The nomological net", [doi:10.1037/h0040957](https://doi.org/10.1037/h0040957) | Full text (psychclassics) |
| Grounded theory | inductive | named | Chun Tie, Birks & Francis (2019), Background, [doi:10.1177/2050312118822927](https://doi.org/10.1177/2050312118822927) | Full text (Europe PMC); no open copy of Glaser & Strauss (1967) |
| Case study | deductive + inductive | named | Crowe et al. (2011), "Analysing, interpreting and reporting case studies", [doi:10.1186/1471-2288-11-100](https://doi.org/10.1186/1471-2288-11-100) | Full text (PMC3141799); quote rechecked by us |
| Process tracing | deductive + inductive | named | Collier (2011), p. 824, [doi:10.1017/S1049096511001429](https://doi.org/10.1017/S1049096511001429) | Full PDF |
| Thematic analysis | deductive + inductive | named | Braun & Clarke (2012), APA Handbook, p. 58, [doi:10.1037/13620-004](https://doi.org/10.1037/13620-004) | Chapter pages; the 2006 paper was not reached |
| Mixed methods (sequential) | all three | named | Johnson & Onwuegbuzie (2004), p. 17, [doi:10.3102/0013189X033007014](https://doi.org/10.3102/0013189X033007014) | Full PDF; said of mixed methods in general |
| Systematic review | deductive + inductive | definition | Page et al. (2021), PRISMA 2020, Introduction ("generate or evaluate theories"), [doi:10.1136/bmj.n71](https://doi.org/10.1136/bmj.n71) | Full text |
| Realist review | abductive | definition | Wong et al. (2013), RAMESES, Background and items 11, 14, [doi:10.1186/1741-7015-11-21](https://doi.org/10.1186/1741-7015-11-21) | Full text; says "theory-driven", "building and testing", not "abductive" |
| Design science | abductive | definition | Hevner et al. (2004), pp. 76, 78 (build-and-evaluate loop), [doi:10.2307/25148625](https://doi.org/10.2307/25148625) | pp. 75–78 |

Method-level sources were read by a research subagent through WebFetch. Two quotes (CONSORT item 2b, Crowe et al.) were
rechecked by us, and every DOI was checked with Crossref.

**Left unmarked**, because no source we read settles it: scoping review, prediction model and Delphi (their sources
state no reasoning); GWAS (neither Visscher et al. 2017 nor Bush & Moore 2012 calls it "hypothesis-free"); ethnography,
factorial experiment, field experiment, co-citation and case report (their sources could not be read). The other Methods
were not checked yet.
