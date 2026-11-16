# Find your method: sources for the top of the tree

How published typologies name the purposes of research, checked on 2026-11-16 for the "Find your method" page. The game uses these in `data/method-tree.json`; the method-family and research-field sources are in `method-tree-taxonomies.md`.
Each entry says what was read and how. Nothing here is from memory.

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
