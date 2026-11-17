# Reasoning overlay: findings waiting to be entered

Working log, 2026-11-17. Two research subagents checked the Methods not yet marked in
`data/classifications.json` (`reasoning`). Nothing below is in the data yet. You asked to add new marks tonight. Before
each mark goes in, its quote is rechecked against the source and its DOI against Crossref. Quotes marked (s) came
through a summariser and must be read in the source itself. Delete this file once its findings are entered or rejected.

Already rechecked by us (2026-11-17): STROBE E&E "from discovery to refutation or confirmation" (section "The scope of
observational research"); Frazier-Wood (2015) Table 1, GWAS: "Is a hypothesis-free or hypothesis-generating approach".

## Candidate marks

| Method | Candidate | Basis | Source, location | Quote (≤15 words) | Caveat |
|---|---|---|---|---|---|
| cross-sectional | deductive + inductive | named | Vandenbroucke et al. (2007), STROBE E&E, Introduction, 10.1371/journal.pmed.0040297 | "from discovery to refutation or confirmation" | STROBE covers cohort, case-control, cross-sectional together |
| cohort-prospective, cohort-retrospective | deductive + inductive | named | STROBE E&E (as above); Euser et al. (2009), 10.1159/000235241, Strengths and weaknesses | "Hypothesis generation is another advantage that has been associated with cohort studies." | Euser alone suggests inductive; cite both |
| case-control | deductive + inductive | named | STROBE E&E (as above) | as above | Doll & Hill (1950) not read |
| gwas | inductive | named | Frazier-Wood (2015), 10.1007/s13668-014-0110-6, Table 1; Kingsmore et al. (2007), PMC2717811 | "Is a hypothesis-free or hypothesis-generating approach" | Not dedicated GWAS methods reviews |
| case-report | inductive | named | Gagnier et al. (2013), CARE, 10.1186/1752-1947-7-223, Introduction | "Case reports may generate hypotheses for future clinical studies" | Riley (2017), the card's own ref, not read |
| its | deductive | definition | Lopez Bernal et al. (2016), 10.1093/ije/dyw098, step 2 | "this decision is made a priori based on existing literature" | Recheck (fetch was aborted) |
| mendelian | deductive | definition | Davey Smith & Ebrahim (2003), 10.1093/ije/dyg070, "Fibrinogen and CHD" | "genotype–disease associations can provide an unconfounded test of the association" | Says "test", not "hypothesis" |
| field-experiment | deductive | named | Harrison & List (2004), 10.1257/0022051043004577, p. 11 fn 14 (working paper) | "the objective is to assess how well theory matches behavior" | Weak: "often"; working-paper version |
| adaptive-platform | deductive + inductive | named | Dimairo et al. (2020), ACE, 10.1136/bmj.m115, Table 1 | "addressing learning … and confirmatory objectives in one trial" | Tentative |
| ethnography | inductive | named | Cubellis, Schmid & von Peter (2021), 10.1177/10497323211022312 | "characterizes a profoundly inductive and relational scientific endeavor" | Also describes iteration between theory and data |
| delphi | deductive + inductive | named | Jünger et al. (2017), CREDES, 10.1177/0269216317690685, Background | "ranging from open and exploratory to standardised confirmatory approaches" | Submitted manuscript; check print wording |
| prediction-model | deductive + inductive | named | Shmueli (2010), 10.1214/10-STS330, §1.4 items 1 and 5 | "for the purpose of developing and testing theories" | — |
| pdsa | abductive | named? | Taylor et al. (2013), 10.1136/bmjqs-2013-001862, Introduction | "making inferences to iterate the hypothesis" | "Abductive" not used: probably basis definition |
| validation | abductive | definition | Clark & Watson (2019), 10.1037/pas0000626 | "empirical tests of hypothesized relations" (s) | Update of own ref (1995); recheck wording |
| diagnostic-accuracy | deductive | named | Bossuyt et al. (2015), STARD, 10.1136/bmj.h5527, item 4 | "Not having a specific study hypothesis may invite generous interpretation" | The hypothesis is about accuracy, not theory: probably leave unmarked |

## Settled as unmarked (the source states no reasoning)

pilot (CONSORT pilot extension: "Pilot trials are exploratory", about the trial's methods, not theory), crossover,
stepped-wedge (checklist item 2b only), target-trial, synthetic-control, reliability (Bland & Altman set testing aside),
scoping-review (Munn et al. 2018: mapping, clarifying concepts), umbrella-review, rapid-review, multivocal-review,
benchmark (Sim: "Usually no hypothesis testing", slides only), discrete-choice, prior-art.

## Not read (paywalled, blocked or no open copy)

cluster-rct, n-of-1, factorial-doe, did, rdd, iv, case-crossover, case-cohort, ecological, surveillance,
capture-recapture, think-aloud, network-meta, ipd-meta, co-citation, bibliographic-coupling, interlab, analytical-model,
simulation, economic-evaluation. Next places to try: the UAntwerp library login (Chest, Annual Reviews, BMJ PDFs),
Europe PMC's HTML pages for Collins et al. (2009), and STROBE-MR for Mendelian randomisation.
