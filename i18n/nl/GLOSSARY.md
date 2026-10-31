# Dutch glossary for Methodical

Terms chosen for the Dutch translation (`cards.json`, `ui.json`), and the reasons for each choice. Written for a native methodologist reviewing or extending the translation.

## Principles

- **Audience.** Researchers and students in Flanders and the Netherlands. Where the two differ, the translation uses the form understood in both and gives the other in the Note column.
- **Keep the English term when Dutch researchers do.** Confounding, bias, power, follow-up, intention-to-treat, scoping review, grounded theory, difference-in-differences, overfitting and similar terms stay in English because Dutch journals and checklists use them that way. Everything else is in Dutch.
- **Trial vs. studie.** Randomized experimental designs are called *trial*, as in NTvG and the Cochrane Netherlands checklists. *Studie* and *onderzoek* are used for any study. In the draft, *studie* was used for RCTs, which blurred the difference between experiments and observational studies.
- **Random.** *Willekeurig* can mean "arbitrary" in Dutch. Where randomness is the methodological point, the translation uses *gerandomiseerd*, *door loting*, *gelote volgorde* or *aselect* (for samples and subcohorts), never *willekeurig*.
- **Methode and design.** The card type is *Methode* (deck *Methoden*), following the English *Method*: "design" on its own was ambiguous next to engineering design. In running text a study design stays *design* or *studiedesign*. *Ontwerp* is kept for engineering and product design and for a statistical *experimenteel ontwerp* (choice sets, screening designs). *Proefopzet* is used for agricultural factorial layouts.
- **Evidence status.** "Verified" means the term was seen in the cited source while preparing this glossary. "Convention" means standard usage known to the reviewer that was not checked online. A native reviewer should look at those first.

## Main sources

| Short name | Source |
|---|---|
| Cochrane-NL RCT | Cochrane Nederland, *Beoordelingscriteria voor een randomised controlled trial (RCT)*, checklist 4.4, from Scholten, Offringa & Assendelft (red.), *Inleiding in evidence-based medicine* (2018). https://netherlands.cochrane.org/sites/netherlands.cochrane.org/files/uploads/4.4_rct_checklist.pdf |
| Cochrane-NL etiologie | Same series, checklist 4.5, *Beoordelingscriteria voor een onderzoek over bijwerkingen of etiologie*. https://netherlands.cochrane.org/sites/netherlands.cochrane.org/files/uploads/4.5_bijwerkingen_en_etiologie_checklist.pdf |
| Cochrane-NL diagnostiek | Same series, checklist 4.2, *onderzoek naar het onderscheidend vermogen van een diagnostische test*. https://netherlands.cochrane.org/sites/netherlands.cochrane.org/files/uploads/4.2_diagnostische_test_checklist.pdf |
| Richtlijnendatabase | Kennisinstituut van de Federatie Medisch Specialisten, *Indeling van methodologische kwaliteit van individuele studies*. https://richtlijnendatabase.nl/application/notitie/32 |
| NTvG | Nederlands Tijdschrift voor Geneeskunde, articles cited per row |
| CBS | CBS achtergrondartikel on population size estimation (2025). https://www.cbs.nl/nl-nl/achtergrond/2025/04/een-toepassing-van-het-schatten-van-de-populatiegrootte-op-officiele-statistieken-gevoeligheid-van-modelaannames-en-het-effect-van-impliciete-dekking |
| Wikipedia-NL | Dutch Wikipedia article titles linked from the English articles (checked through the Wikipedia language links) |

## Core vocabulary in running text

| English | Dutch | Source / evidence | Note |
|---|---|---|---|
| study design | design, studiedesign | Convention; NTvG titles use *design* (e.g. "Het 'stepped wedge'-design", NTvG 2012;156:A4069, https://www.ntvg.nl/artikelen/het-stepped-wedge-design) | *Onderzoeksopzet* is also common (NTvG "De N = 1-trial, de meest ideale onderzoeksopzet"). |
| exposure | blootstelling | Verified: Cochrane-NL etiologie ("eenheid van blootstelling") | *Determinant* is also used in Dutch epidemiology. |
| outcome | uitkomst | Verified: Cochrane-NL RCT and etiologie | |
| confounder / confounding | confounder / confounding | Verified: Cochrane-NL etiologie ("prognostische factoren (confounders)"); NTvG 2012 "Verstoring in observationeel onderzoek: 'confounding'" (https://www.ntvg.nl/artikelen/verstoring-observationeel-onderzoek-confounding); Wikipedia-NL "Confounder" | The Dutch *verstoring* exists (NTvG) but researchers mostly say *confounding*. |
| bias (general) | bias | Convention; Cochrane-NL ("academic bias") | *Vertekening* is used in lay text. Compounds are written as one word where Dutch practice is settled: selectiebias, publicatiebias, spectrumbias, colliderbias. |
| trial | trial | Verified: Cochrane-NL RCT ("aan het begin van de trial"); NTvG 2016;160:D955 "een clustergerandomiseerde gecontroleerde trial" | Not *studie*; see Principles. |
| control group / controls | controlegroep (trials); controles (case–control) | Verified: Cochrane-NL RCT ("Controlegroep"); *cases en controles* is standard in Dutch case–control writing | The draft's "naar de controles lekken" (Q12) became *controlegroep*. |
| cases | cases | Convention | Bouter et al. use *patiënten en controlepersonen*. *Cases* is shorter and common in research. |
| blinding / blinded | blindering / geblindeerd | Verified: Cochrane-NL RCT ("Waren de patiënten en de behandelaars geblindeerd") | |
| outcome assessors | effectbeoordelaars | Verified: Cochrane-NL RCT | |
| enrol | insluiten / includeren | Verified: Cochrane-NL RCT ("degene die patiënten insluit") | |
| allocation / assign | toewijzing / toewijzen | Verified: Cochrane-NL RCT ("toewijzing van de interventie") | |
| randomize / random sample | randomiseren / aselecte steekproef | Convention (*aselecte steekproef* is the standard Dutch statistics term) | See Principles on *willekeurig*. |
| follow-up / loss to follow-up | follow-up / uitval | Verified: Cochrane-NL RCT ("loss-to-follow-up"), Cochrane-NL diagnostiek ("uitvallers", "uitval") | The draft's Flemish "volg ze op" became *volg ze (in de tijd)*. |
| prevalence / incidence | prevalentie / incidentie | Verified: Cochrane-NL etiologie ("incidente (nieuwe) ziektegevallen") | |
| odds ratio / relative risk / hazard ratio | oddsratio / relatieve risico / hazard ratio | Verified: Cochrane-NL etiologie | |
| statistical power | power | Verified usage: Maastricht University form "Informatie nodig voor steekproefgrootte- of powerberekening" (https://www.maastrichtuniversity.nl/file/informatie-nodig-voor-steekproefgrootte-powerberekening-20250829docx). A search snippet of a hospital nWMO protocol template (Catharina Ziekenhuis) also uses "poweranalyse" | Wikipedia-NL names the concept *onderscheidend vermogen* / *onderscheidingsvermogen* (https://nl.wikipedia.org/wiki/Onderscheidend_vermogen). Researchers say *power*. Because *onderscheidend vermogen* is also used for test and model discrimination, the cards avoid it for both meanings. |
| discrimination (prediction model) | discriminerend vermogen | Convention; Dutch prediction-model literature (Steyerberg, Moons) uses *discriminatie* and *kalibratie* | The draft used *onderscheidend vermogen*, which is also the Dutch term for statistical power. Cochrane-NL uses it for diagnostic accuracy. |
| calibration | kalibratie | Convention | |
| net benefit | net benefit | Convention (decision-curve analysis is cited in English in Dutch papers) | The draft had *netto voordeel*. |
| sample (lab) | monster | Convention (NL lab usage; ISO/NEN texts) | Flemish: *staal/stalen*. In the Netherlands *staal* means steel, so *monster* is used. |
| survey (questionnaire study) | enquête | Convention | Social scientists also say *survey(onderzoek)*; NTvG uses *vragenlijstonderzoek*. The draft mixed *survey* and *enquête*. |
| recruit / recruitment | werven / werving | Convention | Flemish usage favours *rekruteren/rekrutering*, which Dutch readers understand. |
| device (measurement) | apparaat | Convention | Flemish: *toestel*. |
| needs | behoeften | Convention | Flemish: *noden*. |
| quality of life | kwaliteit van leven | Convention (Zorginstituut usage) | KCE and Flemish usage: *levenskwaliteit*. |
| databases | databases | Convention | Flemish: *databanken*. |
| tax (Q13) | heffing (text), suikertaks (title, art label TAKS) | Convention: *suikertaks* is used in both Dutch and Flemish media | *Taks* on its own is Flemish. |
| greenhouse | kas | Convention | Flemish: *serre*. |
| prior art / novelty search | stand van de techniek / nieuwheidsonderzoek | Verified: Rijksoctrooiwet 1995 art. 32 ("onderzoek naar de stand van de techniek"); Octrooicentrum terminology (https://beijerterm.com/Nieuwheidsonderzoek) | |
| heat engine | warmtemachine | Verified: Wikipedia-NL "Warmtemachine" | The draft had *warmtemotor*. |
| civil engineering | civiele techniek | Convention (TU Delft faculty name) | Flemish: *(burgerlijke) bouwkunde*. In the Netherlands *bouwkunde* means building/architecture, so it was replaced. |
| marker / biomarker | marker / biomarker | Convention (NTvG usage) | The draft's *merker/biomerker* is rare. |
| ability (econometrics) | capaciteiten | Convention | The draft's *bekwaamheid* means competence, not innate ability. |
| first-principles simulation | ab-initiosimulatie | Convention | |
| closed-form solution | oplossing in gesloten vorm | Convention | |
| emergency department | spoedeisende hulp | Convention | Flemish: *spoed(gevallendienst)*. The draft's "triageprotocol voor spoed" became *spoedtriageprotocol*. |

## Suits, families and constraints (`meta`)

| English | Dutch | Source / evidence | Note |
|---|---|---|---|
| Describe / Explore / Cause / Predict / Measure / Explain / Build / Synthesize | Beschrijven / Verkennen / Oorzaak / Voorspellen / Meten / Verklaren / Bouwen / Synthetiseren | Draft kept | |
| Associate | Samenhang | Convention: *samenhangen met* is how the cards render "associated with" | The draft had *Verbanden*. |
| Descriptive / Analytical observational | Beschrijvend / Analytisch observationeel | Draft kept | |
| Quasi-experimental / Experimental | Quasi-experimenteel / Experimenteel | Draft kept | |
| Qualitative & mixed | Kwalitatief & gemengd | Draft kept | *Mixed methods* is used for the design card. |
| Evidence synthesis | Bewijssynthese | Convention (NL) | Flemish: *evidentiesynthese* (the draft's term). |
| Measurement (family) | Meetonderzoek | Avoids a clash with the suit *Meten* | The draft used *Meten* for both. |
| Theory & computation | Theorie & berekening | Draft kept | |
| Design & development | Ontwerp & ontwikkeling | Draft kept | |
| Cutoff rule | Afkapregel; *afkappunt* in running text | Convention | Same word as the RDD card, so the constraint and design match. |
| Can't assign, Rare outcome, Rare exposure, Long latency, Brief trigger, Existing data, One unit, Group-level, Rollout, Tight budget, Uncharted, Practice-led, Many studies | Niet toewijsbaar, Zeldzame uitkomst, Zeldzame blootstelling, Lange latentie, Korte trigger, Bestaande data, Eén eenheid, Groepsniveau, Uitrol, Krap budget, Onbekend terrein, Praktijkgedreven, Veel studies | Draft kept | |

## Design names

| English | Dutch | Source / evidence | Note |
|---|---|---|---|
| Case report / case series | Casusbeschrijving / -reeks | Draft kept | *Casuïstiek* is also used in NTvG. |
| Cross-sectional survey | Dwarsdoorsnedeonderzoek | Verified: NTvG, e.g. "Een dwarsdoorsnedeonderzoek naar declaraties binnen het basispakket" (https://www.ntvg.nl/artikelen/het-zorggebruik-van-minima-amsterdam) | The draft had *Cross-sectioneel onderzoek*, also in use but less established in NTvG. |
| Ecological study | Ecologische studie | Draft kept | |
| Monitoring / surveillance | Monitoring / surveillance | Draft kept | |
| Capture–recapture | Vangst–hervangst | Verified: CBS ("vangst-hervangst methode") | Ecologists also say *merk-terugvangst*. |
| Prospective / retrospective cohort | Prospectief / Retrospectief cohortonderzoek | Verified: Richtlijnendatabase ("Prospectief cohort onderzoek"); Wikipedia-NL "Cohortonderzoek" | |
| Case–control study | Patiënt-controleonderzoek | Verified: Cochrane-NL etiologie ("patiëntcontroleonderzoek"); Richtlijnendatabase ("patiëntcontrole onderzoek") | Spellings vary. The hyphenated form follows the Taalunie rule for coordinate compounds. *Case-controlonderzoek* is also heard, especially in Flanders. |
| Case-crossover | Case-crossover | Convention | |
| Target trial emulation | Target-trial-emulatie | Draft kept | |
| Instrumental variable analysis | Instrumentele variabelen (IV) | Convention | The draft's *Instrumentele-variabeleanalyse* is not attested. |
| Mendelian randomization | Mendeliaanse randomisatie | Convention | |
| Genome-wide association study | Genoombrede associatiestudie | Convention | *GWAS* is used everywhere. |
| Case-cohort / nested case–control | Case-cohort / genest patiënt-controle | Draft kept | |
| Difference-in-differences | Difference-in-differences | Convention (CPB and Dutch econometrics keep the English) | |
| Regression discontinuity | Regressiediscontinuïteit | Convention; spelled as one word (no vowel clash, so no hyphen) | Economists usually say *regression discontinuity (design)*. |
| Interrupted time series | Onderbroken tijdreeks | Convention | |
| Synthetic control | Synthetische controle | Convention | |
| Randomized controlled trial | Gerandomiseerde gecontroleerde trial | Verified: Cochrane-NL RCT; NTvG 2016;160:D955 | Wikipedia-NL: *gerandomiseerd onderzoek met controlegroep*. Richtlijnendatabase: *gerandomiseerd ... vergelijkend klinisch onderzoek*. |
| Cluster randomized trial | Clustergerandomiseerde trial | Verified: NTvG 2016;160:D955 | NTvG also uses *clusterstudie*. |
| Crossover trial | Cross-overtrial | Convention | |
| Factorial experiment (DoE) | Factorieel experiment (DoE) | Draft kept | In running text: *factoriële proefopzet* (agriculture). |
| N-of-1 trial | N-of-1-trial | Verified: NTvG "De N = 1-trial, de meest ideale onderzoeksopzet, die te weinig wordt gebruikt" (https://www.ntvg.nl/artikelen/de-n-1-trial-de-meest-ideale-onderzoeksopzet-die-te-weinig-wordt-gebruikt) | |
| Stepped-wedge trial | Stepped-wedge-trial | Verified: NTvG 2012 "Het 'stepped wedge'-design" | |
| Adaptive / platform trial | Adaptieve / platformtrial | Convention | |
| Online A/B test | Online A/B-test | Draft kept | |
| Field experiment | Veldexperiment | Draft kept | |
| Ethnography / Grounded theory / Interviews & thematic analysis / Case study / Process tracing | Etnografie / Grounded theory / Interviews & thematische analyse / Casestudy (diepgaand) / Process tracing | Convention (Dutch qualitative-methods texts keep *grounded theory* and *process tracing*) | Flemish also uses *gevalsstudie*. |
| hoop test / smoking gun | 'hoop test' / 'smoking gun' (English, in quotes); art label HOOP | Convention: no Dutch rendering found | The draft's calque *hoeptest* is not used in Dutch political science. |
| Delphi consensus | Delphi-consensus | Wikipedia-NL "Delphi-studie" | |
| Mixed methods (sequential) | Mixed methods (sequentieel) | Draft kept | *Verklarend sequentieel design* in running text. |
| Systematic review & meta-analysis | Systematische review & meta-analyse | Verified: Richtlijnendatabase ("Systematische review") | |
| Scoping / umbrella / rapid / realist review | Scoping review / Umbrella review / Rapid review / Realist review | Convention | *Realist synthesis* is also kept in English (*realistische synthese* would read as "realistic"). |
| Network meta-analysis / IPD meta-analysis | Netwerkmeta-analyse / IPD-meta-analyse (individuele data) | Draft kept | |
| Prior art review | Nieuwheidsonderzoek | Verified: Rijksoctrooiwet 1995 art. 32 / Octrooicentrum ("onderzoek naar de stand der techniek (ook wel nieuwheidsonderzoek genoemd)") | The draft's *Prior-art-review* is not Dutch usage. |
| Co-citation / bibliographic coupling | Co-citatieanalyse / Bibliografische koppeling | Convention (CWTS Leiden usage) | |
| Multivocal literature review | Multivocale literatuurreview | Draft kept | |
| Diagnostic accuracy study | Diagnostisch accuratesseonderzoek | Verified: Richtlijnendatabase ("Diagnostisch accuratesse onderzoek") | Cochrane-NL describes it as *onderzoek naar het onderscheidend vermogen van een diagnostische test*. |
| Reliability & agreement study | Betrouwbaarheid & overeenstemming | Draft kept | |
| Instrument development & validation | Ontwikkeling & validatie van instrumenten | Draft kept | |
| Nomological network study | Nomologisch-netwerkstudie | Draft kept | |
| Discrete choice experiment | Discrete keuze-experiment | Verified: Erasmus Universiteit ("discrete keuze-experimenten (DCE)", https://www.eur.nl/evenementen/promotie-vr-vikash-soekhai-2021-11-04) | The draft's *Discreet-keuze-experiment* is not attested. |
| Interlaboratory comparison / round robin | Interlaboratoriumvergelijking / ringonderzoek | Convention (Dutch accreditation and lab usage) | |
| repeatability / reproducibility | herhaalbaarheid / reproduceerbaarheid | Convention (Dutch title of NEN-ISO 5725) | |
| Analytical / mathematical theory, Computational simulation | Analytische / wiskundige theorie, Computersimulatie | Draft kept | FEM is *EEM* (eindige-elementenmethode). |
| Prediction model | Predictiemodel | Convention | *Voorspellingsmodel* is also used. |
| Cost-effectiveness analysis | Kosteneffectiviteitsanalyse | Convention (Zorginstituut) | |
| Design science | Design science | Convention | |
| Pilot / feasibility study | Pilot- / haalbaarheidsstudie | Draft kept | |
| Usability test (think-aloud) | Usabilitytest (hardop denken) | Draft kept | |
| PDSA cycles / run chart | Plan-Do-Study-Act-cycli / runchart | Convention (Dutch quality-improvement usage) | |
| Benchmark evaluation | Benchmarkevaluatie | Draft kept | |

## Threat names

| English | Dutch | Source / evidence | Note |
|---|---|---|---|
| Confounding | Confounding | See core vocabulary | |
| Confounding by indication | Confounding door indicatie | NTvG (Zielhuis 2000, "Randomisatie als middel tegen verstoring door indicatie", https://www.ntvg.nl/artikelen/dwalingen-de-methodologie-xx-randomisatie-als-middel-tegen-verstoring-door-indicatie) | Hybrid form, matching *Confounding*. Alternatives: *verstoring door indicatie* (NTvG) or the English *confounding by indication*. |
| Selection bias | Selectiebias | Convention | |
| Attrition & missing data | Uitval & ontbrekende data | Verified: Cochrane-NL diagnostiek ("uitval") | |
| Recall bias | Recall bias | Convention | *Herinneringsbias* is used in lay text. |
| Measurement error | Meetfout | Convention | In the text, "drifting" is rendered *verloopt* (metrology: *verloop* = drift). The draft's *ruizig* is not a standard word and became *onnauwkeurig*. |
| Reverse causation | Omgekeerde causaliteit | Convention | |
| Regression to the mean | Regressie naar het gemiddelde | Verified: Wikipedia-NL | |
| Expectation effects | Verwachtingseffecten | Convention | *Waarnemerseffect* instead of *observatoreffect*. *Hawthorne-effect* is on Wikipedia-NL. |
| Contamination & spillover | Contaminatie & spillover | Convention | The draft's *overloop* also means "landing" (of a staircase). Economists use *spillover* or *overloopeffect*. |
| Immortal time bias / Survivorship bias | Immortal time bias / Survivorship bias | Convention | |
| Collider bias | Colliderbias | Convention | |
| Ecological fallacy | Ecologische fout | Verified: Wikipedia-NL "Ecologische fout" (https://nl.wikipedia.org/wiki/Ecologische_fout) | Mackenbach: *ecologische valkuil*. That was not used because *Valkuil* is the game's "trap" tier. The draft's *ecologische drogreden* is understandable but less established. |
| Unit-of-analysis error | Verkeerde analyse-eenheid | Convention | |
| Publication bias | Publicatiebias | Convention | |
| Unvetted sources | Ongetoetste bronnen | Draft kept | |
| Forking paths & p-hacking | Forking paths & p-hacking | Convention | |
| Low power | Lage power | Convention | Also heard: *te weinig power*. |
| Overfitting & leakage | Overfitting & leakage | Convention | Flemish *vanbuiten leren* became *uit het hoofd leren*. |
| Spectrum bias | Spectrumbias | Convention | |
| History & secular trends | Historie & seculaire trends | Convention (Dutch epidemiology writes *seculaire trend*) | The draft had *seculiere* (secular as in non-religious). |
| Carryover | Carry-over | Convention | |
| Researcher bias | Onderzoekersbias | Draft kept | |
| Limited generalizability | Beperkte generaliseerbaarheid | Draft kept | |
| Apples & oranges | Appels & peren | Dutch idiom | |
| Unvalidated model / Wrong construct | Ongevalideerd model / Verkeerd construct | Draft kept | |
| Thin data | Magere data | Dutch idiom | The draft's *dunne data* is a calque. |

## Safeguard names

| English | Dutch | Source / evidence | Note |
|---|---|---|---|
| Randomization | Randomisatie | Convention | |
| Allocation concealment | Verborgen toewijzing | Cochrane-NL RCT describes it as "degene die patiënten insluit [is] niet op de hoogte van de randomisatievolgorde" | Older Dutch forms say *blindering van de randomisatie (concealment of allocation)*. That wording was avoided because it confuses concealment with blinding. |
| Blinding | Blindering | Verified: Cochrane-NL RCT | |
| Placebo or sham control | Placebo of schijnbehandeling | Convention (*schijnbehandeling*, *schijnoperatie*) | The draft's *schijncontrole* is not used. |
| Intention-to-treat / Preregistration | Intention-to-treat / Preregistratie | Convention; Cochrane-NL RCT describes ITT as "Zijn alle ingesloten patiënten geanalyseerd in de groep waarin ze waren gerandomiseerd?" | |
| Sample-size planning | Powerberekening | Verified usage (protocol templates, see *power*) | Alternative: *steekproefgrootteberekening*. The draft's *steekproefgrootteplanning* is a calque. |
| Causal diagram (DAG) | Causaal diagram (DAG) | Convention | |
| Matching / propensity scores | Matching / propensityscores | NTvG "'Propensity scores' in observationeel onderzoek" | |
| Negative controls | Negatieve controles | Convention | |
| Sensitivity analysis | Sensitiviteitsanalyse | Convention (Zorginstituut and KCE) | *Gevoeligheidsanalyse* is also used. |
| Active comparator, new users | Actieve comparator, nieuwe gebruikers | Convention (Dutch pharmacoepidemiology) | The draft's *actieve vergelijker, nieuwe starters* is a calque and pleonastic. The short text uses *starters*. |
| Time-zero alignment | Gelijk tijdstip nul | Draft kept | |
| Lag & early-event exclusion | Lag & vroege events uitsluiten | Convention | |
| Concurrent control group | Gelijktijdige controlegroep | Draft kept | |
| Pre-trend check & control series | Pretrendcheck & controlereeks | Draft kept | |
| Allocate by cluster | Toewijzen per cluster | Draft kept | |
| Washout period | Wash-outperiode | Convention (Dutch medical spelling) | |
| External validation / Multiplicity correction / Independent replication | Externe validatie / Correctie voor multipliciteit / Onafhankelijke replicatie | Draft kept | *Correctie voor meervoudig toetsen* is also common. |
| Comprehensive search | Uitputtende zoekactie | Convention (Dutch EBM and library usage: *zoekactie*) | |
| Grey-literature appraisal | Beoordeling grijze literatuur | Draft kept | |
| Pre-planned heterogeneity analysis | Geplande heterogeniteitsanalyse | Draft kept | |
| Representative sampling | Representatieve steekproef | Draft kept | The draft's text said "niet wie handig is", which reads as "not whoever is skilful". It now says *niet wie toevallig voorhanden is*. |
| Validated, objective measures | Gevalideerde, objectieve maten | Draft kept | |
| Reflexivity & double coding | Reflexiviteit & dubbel coderen | Draft kept | |
| Triangulation | Triangulatie | Convention | |
| Theoretical sampling to saturation | Theoretische sampling tot saturatie | Convention; Dutch qualitative-methods glossaries use *theoretische sampling* (e.g. https://webwoordenboek.nl/kenniscentrum/wat-is-theoretische-sampling, a weak source) | The draft's *theoretische steekproef* suggests a probability sample. Boeije also uses *(theoretische) verzadiging*. |
| Multilevel analysis | Multilevelanalyse | Convention | |
| Verification & validation | Verificatie & validatie | Draft kept | |
| Multi-site, diverse sample | Multicentrisch, divers | Draft kept | |
| Self or sibling comparison | Zelf- of broer-zusvergelijking | Draft kept | |
| Run charts & control limits | Runcharts & controlegrenzen | Convention (healthcare quality improvement) | Industrial SPC says *regelkaart* and *regelgrenzen*. |

## Interface labels

| English | Dutch | Note |
|---|---|---|
| suit | kleur | Card-game term (harten, ruiten, ...). |
| Weak vs | Kwetsbaar voor | The draft's *Zwak tegen* is a calque. |
| Counters / Countered by | Ondervangt / Ondervangen door | A safeguard *ondervangt* a threat; it does not *weerlegt* (refute) it. *Weerlegging* stays for the game's "rebuttal". |
| Play on a method | Speel tegen een methode | |
| Validity threat | Validiteitsbedreiging | |
| Intermediate / Advanced | Halfgevorderd / Gevorderd | The draft shifted the levels (Gevorderd / Expert). |
| Best / Defensible / Trap / Unlisted | Beste / Verdedigbaar / Valkuil / Niet vermeld | Card text that names a tier uses these words. Q39 said "'ok'-antwoord"; it now says *verdedigbare antwoord*. |

## Open questions for a native methodologist

1. **Patiënt-controleonderzoek or case-controlonderzoek?** The Dutch-medical term was kept, but several cards are non-medical (astronomy, engineering). A reviewer from Flanders or the social sciences may prefer *case-controlonderzoek*.
2. **Hybrid English–Dutch names.** *Confounding door indicatie*, *Target-trial-emulatie* and *Stepped-wedge-trial* mix English and Dutch. Each is attested, but a reviewer may prefer fully English or fully Dutch forms.
3. **Lage power.** Possible alternatives are *te weinig power* or *onvoldoende power*.
4. **Ecologische fout.** The alternatives are *ecologische drogreden*, which matches the *drogredenen*-stapel nickname, and Mackenbach's *ecologische valkuil*.
5. **Enquête or survey.** Social scientists may prefer *survey* in Q34, Q55, Q57, Q60, Q70 and the mixed-methods card.
6. **Art labels.** STRAKS (prediction output "NEXT"), RISICO (case-crossover "hazard" window), GEDATEERD (preregistration stamp "DATED") and TAKS (Q13 price tag) were chosen to fit the drawing widths. Check how they look on printed cards.
7. **Nieuwheidsonderzoek.** It is the patent term. The English card also covers checking novelty before publishing, which is slightly broader.
