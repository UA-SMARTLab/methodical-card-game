# Arabic glossary for Methodical (مسرد المصطلحات العربية)

This glossary explains the term choices in the Arabic edition (`i18n/ar/cards.json`, `i18n/ar/ui.json`) so that a native-speaking methodologist can check or contest them.

Principles:

- **The term Arabic scientific writing actually uses.** For medicine and epidemiology, the WHO Eastern Mediterranean Regional Office (EMRO) usage comes first: the Unified Medical Dictionary (المعجم الطبي الموحد) and the Arabic abstracts of the *Eastern Mediterranean Health Journal* (EMHJ). For economics, social science, information science and engineering, the usage of Arabic textbooks, theses and institutional documents in that field.
- **The most widely understood form** where usage differs between regions (Levant, Egypt, Gulf, Maghreb). Alternatives are listed in the notes.
- **One concept, one term**, in every field: card names, short texts, explanations, trap reasons, interface strings and art labels.
- Modern Standard Arabic, Arabic punctuation (، ؛ ؟), Western digits. Author, study and organisation names stay in Latin script.

Numbers in brackets refer to the sources at the end. "Usage" marks a choice based on common usage in Arabic textbooks and articles for which no authoritative online source could be checked during this review. **The UMD's online search (umd.emro.who.int) returned no results during this review**, so entries attributed to UMD-style usage were confirmed only through EMRO/EMHJ texts or Wikipedia; a reviewer with UMD access should spot-check them.

## Cross-cutting decisions

| English | Arabic used | Source | Note |
|---|---|---|---|
| exposure | **التعرض** | [1] | EMHJ abstracts use التعرُّض throughout. |
| outcome | **الحصيلة** (pl. الحصائل) | [2] usage | EMRO/UMD term ("الحصائل الصحية"). Kept distinct from النتيجة (= result, finding). Alternatives: النتيجة، المآل. The draft also used حصيلة in the sense "sum total" (P1 stage 5); that was rewritten to avoid the clash. |
| cohort; cohort study | **الأتراب / مجموعة أترابية; دراسة أترابية** | [1] [4] | EMHJ: "دراسة أترابية". Draft mixed أترابية (card names) with فوج/أفواج (running text, art); now أترابية everywhere. subcohort → **عينة فرعية من الأتراب** (art label: عينة فرعية). Alternatives: دراسة الأفواج / الفوجية (Levant), الدراسة الحشدية (Arabic Wikipedia). |
| prospective / retrospective | **استباقية / استعادية** | usage | Alternatives: مستقبلية / رجعية (تاريخية). |
| case–control; controls (non-cases) | **الحالات والشواهد; الشواهد** | [4] | Fixed epidemiological term (Arabic Wikipedia title "دراسة الحالات والشواهد"). |
| control group / control arm / control series | **المجموعة الضابطة / الذراع الضابطة / سلسلة ضابطة** | [4] [9] | Understood across medicine, psychology, education and economics. The draft used مجموعة الشاهد; UMD-style مجموعة الشاهد remains an acceptable alternative. شاهد is kept only where the case–control lineage is meant (case–control, case-crossover "each case is its own control", GWAS shared controls, art label CONTROL WINDOWS → فترات الشاهد) and in the fixed RCT name below. |
| randomized controlled trial | **تجربة معشاة ذات شواهد** | [2] [4] | EMRO/UMD fixed name (Arabic Wikipedia: "تجربة منضبطة معشاة"). Kept as a fixed name because it is the form researchers search for. |
| randomization; randomize | **التوزيع العشوائي; وزّع عشوائيًا** | [3] [4] | World Bank Arabic impact-evaluation material and the Arabic Wikipedia RCT article use التوزيع العشوائي. The draft's تعشية / imperative «عَشِّ» is a correct UMD coinage but opaque outside medicine, and the imperative is unreadable; it also clashed visually with تعشيش (nesting, Q22). معشّاة survives only inside fixed design names. |
| allocation; assign (to treatment) | **التخصيص; خصّص / وزّع** | [4] | Replaces تعيين (draft), which reads as "appointment". "Can't assign" → **تعذّر التخصيص**. |
| allocation concealment | **إخفاء التخصيص** | usage | Cochrane-style rendering. |
| blinding; blinded | **التعمية; معمّى / دون معرفة …** | [2] | UMD term. The draft's imperative «عَمِّ» was replaced by «طبّق التعمية». |
| confounding; confounder | **الإرباك; العامل المُربِك** | usage | The most common form in Arabic medical papers ("بعد ضبط العوامل المربكة"). Alternatives: التشويش، الالتباس، التأثير المخالِط / الدَّغم (Arabic Wikipedia [4]). |
| indication (clinical) | **الاستطباب** | [2] | UMD term (cf. مضاد استطباب). Draft's الدواعي alone was vague. Alternative: دواعي الاستعمال. |
| bias | **التحيز** | usage | UMD and Arabic Wikipedia often use الانحياز; التحيز is more common in Arabic research-methods writing. Either is understood. |
| prevalence | **الانتشار / معدل الانتشار** | [4] | |
| incidence | **معدل الحدوث** | usage, [4] | Arabic Wikipedia/UMD: الوقوع. معدل الحدوث is more transparent to non-epidemiologists. |
| odds | **الأرجحية** | [4] | As in نسبة الأرجحية (odds ratio). Used in P5 stage 3 ("change the odds"), where the draft had the vaguer الاحتمالات. |
| statistical power | **القوة الإحصائية** | usage | |
| effect size | **حجم الأثر** | [4] | |
| statistically significant; null result | **دالّ إحصائيًا; نتيجة غير دالّة** | [4] | Draft "النتائج الصفرية" (calque of "null results") → النتائج غير الدالّة. |
| population (epidemiology) / population (sampling frame) | **السكان، الفئة السكانية / المجتمع (الإحصائي)** | usage | Source population → السكان الذين نشأت منهم الحالات. Draft used المجتمع everywhere, which also means "community". |
| sampling; sample (verb) | **المعاينة; اختر العينة / عايِن** | usage | The draft's imperative «اعتَن» (from اعتيان) reads as "take care of" and was replaced in Q08 and Q55; اعتيان (UMD) replaced by معاينة in the grounded-theory gist for consistency. |
| purposive sampling | **عينة قصدية** | usage | Standard in Arabic qualitative-research teaching. |
| evidence | **البيّنات** | [2] | EMRO usage (الطب المسند بالبيّنات). Alternative: الأدلة. |
| (evidence) synthesis; synthesize | **التوليف; ولِّف** | usage | Replaces تجميع (draft), because the game must keep *synthesis* apart from *pooling*: a scoping review synthesizes "without pooling effects". Suit SYNTHESIZE → توليف; family → توليف البيّنات; realist synthesis → التوليف الواقعي. Alternative: تجميع البيّنات. |
| pool (results, effects) | **دمج; ادمج** | usage | Draft used تجميع for both. |
| aggregate data | **بيانات مجمّعة** | usage | Distinct from pooling. |
| reliability (measurement) | **الثبات** | usage | The entrenched Arabic psychometric pair is الصدق والثبات. Applied to the Measurement deck (reliability design, Q34, Q64, suit MEASURE). Alternative: الموثوقية (engineering, some medical writing; Arabic Wikipedia "موثوقية (إحصاء)"). General adverbs ("reliably predict") are rendered by sense (بدقة، بموثوقية). |
| validity; valid | **الصدق** | usage | الصدق الداخلي/الخارجي in Arabic research-methods textbooks. |
| construct | **المفهوم** | usage | Psychometric alternative: البناء / التكوين الفرضي (صدق البناء). "Wrong construct" → المفهوم الخطأ (clearer on a card). |
| regression to the mean | **الانحدار نحو المتوسط** | usage | Galton's "regression" = الانحدار, the standard statistics term. Draft: الارتداد نحو المتوسط. |
| manipulate (experimentally) | **تحكّم تجريبيًا** | usage | Draft "يُتلاعب / التلاعب" means tampering. التلاعب is kept only in "p-hacking" (التلاعب بقيمة p), where tampering is the meaning. |
| derive; derivation | **اشتقّ; اشتقاق** | usage | Draft mixed استنتج and اشتقاق. |
| universal (claim) | **كلّي / عام** | usage | Draft "كوني" means cosmic. |
| treatment (experimental factor) / treatment (medical) | **المعالجة / العلاج** | usage | |
| peek (at data) | **استراق النظر** | usage | Draft "التلصص" (spying). |
| mediator | **المتغير الوسيط** | usage | Draft "الوسائط" means media. |
| time zero | **الزمن الصفري** | usage | |
| washout (period) | **فترة إزالة الأثر** | usage | No settled Arabic term was found; alternatives seen: فترة الغسل، فترة الإزالة، فترة التصفية. The chosen form states the purpose and pairs with الأثر المتبقي (carryover). |
| burnout | **الاحتراق الوظيفي** | [4] | Arabic Wikipedia: احتراق نفسي مهني. "مقياس الاحتراق" alone reads as "combustion scale". |
| conservation (biology) | **صون الطبيعة** | usage | As in the Arabic name of IUCN (الاتحاد الدولي لصون الطبيعة). Draft mixed علم الحفظ and الحفاظ على الطبيعة. |
| repeatability / reproducibility | **التكرارية / قابلية إعادة الإنتاج** | [4] | Draft used قابلية التكرار for "reproducible" in the interlab card, conflating the two quantities that Q37 asks to separate. |
| replication (crisis) | **التكرار (أزمة التكرار)** | [4] | |

## Suits, families, constraints

| English | Arabic | Note |
|---|---|---|
| Describe / Explore / Associate / Cause / Predict / Measure / Explain / Build / Synthesize | وصف / استكشاف / ارتباط / سببية / تنبؤ / قياس / تفسير / بناء / **توليف** | Only Synthesize changed (was تجميع), see above. |
| Descriptive / Analytical observational | رصدية وصفية / رصدية تحليلية | "Observational" = رصدية (EMHJ usage); Arabic Wikipedia: دراسة بالملاحظة. |
| Quasi-experimental / Experimental | شبه تجريبية / تجريبية | Arabic Wikipedia: شبه تجربة. |
| Qualitative & mixed | نوعية ومختلطة | Arabic Wikipedia: بحث نوعي. Maghreb alternative: كيفي. |
| Evidence synthesis | **توليف البيّنات** | was تجميع البيّنات |
| Can't assign | **تعذّر التخصيص** | was لا تعيين |
| Rare outcome / Rare exposure / Long latency / Brief trigger | حصيلة نادرة / تعرض نادر / كمون طويل / محفز عابر | |
| Cutoff rule / Rollout | قاعدة حد فاصل / تعميم تدريجي | |

## Designs

| English | Arabic | Source | Note |
|---|---|---|---|
| Case report / case series | تقرير حالة / سلسلة حالات | [4] | |
| Cross-sectional survey | مسح مستعرض | [4] | Arabic Wikipedia: دراسة مستعرضة; alternative مقطعية. Because مسح is masculine, trap reasons that refer to this design now use masculine verbs (لا يستطيع، لا يفصل). |
| Ecological study / ecological fallacy | دراسة إيكولوجية / المغالطة الإيكولوجية | [4] | Arabic Wikipedia: دراسة بيئية / مغالطة بيئية. بيئية is ambiguous with "environmental" (Q06 is an environmental-health question), so the transliteration is kept. |
| Monitoring / surveillance | رصد / ترصّد | usage | WHO Arabic: الترصد. |
| Capture–recapture | الالتقاط وإعادة الالتقاط | usage | Ecology alternative: الصيد وإعادة الصيد، الوسم وإعادة الأسر. |
| Prospective / retrospective cohort | دراسة أترابية استباقية / استعادية | [1] | |
| Case–control study | دراسة الحالات والشواهد | [4] | |
| Case-crossover | تصميم الحالة التبادلي | usage | Pairs with تجربة تبادلية (crossover). Alternative: التصالبي. |
| Target trial emulation | محاكاة التجربة المستهدفة | usage | |
| Instrumental variable analysis | تحليل المتغير الأداتي | usage, [3] | World Bank slides: متغيرات مساعدة. الأداتي is the more common form in Arabic econometrics teaching. |
| Mendelian randomization | **التوزيع العشوائي المندلي** | usage | was التعشية المندلية; follows the randomization decision. No established Arabic form was found; the term is rare in Arabic. |
| Genome-wide association study | دراسة الارتباط على نطاق الجينوم | usage | Alternatives: على مستوى الجينوم؛ Arabic Wikipedia: دراسة الترابط الجينومي الكامل. |
| Case-cohort / nested case–control | **الحالات والأتراب / الحالات والشواهد المضمّنة** | usage | was الحالات والفوج / … المتداخلة; متداخلة means "overlapping". |
| Difference-in-differences | الفرق في الفروق | [3] [4] | World Bank and Arabic Wikipedia: الاختلاف في الاختلافات; also الفروق في الفروق. Kept the draft's shorter form. |
| Regression discontinuity | انقطاع الانحدار | [3] | World Bank Arabic slides. Arabic Wikipedia (تقييم الأثر): الانحدار المتقطع. |
| Interrupted time series | السلاسل الزمنية المتقطعة | usage | |
| Synthetic control | **الضبط التركيبي** | usage | was الشاهد التركيبي; follows the control-group decision. Explanations say "مجموعة ضابطة تركيبية" where needed. Alternative: التحكم التركيبي. |
| Randomized controlled trial | تجربة معشاة ذات شواهد | [2] [4] | |
| Cluster randomized trial | تجربة معشاة عنقودية | usage | |
| Crossover trial | تجربة تبادلية | usage | Arabic Wikipedia: دراسة العبور. |
| Factorial experiment (DoE) | تجربة عاملية (DoE) | [4] | |
| N-of-1 trial | تجربة الفرد الواحد | usage | |
| Stepped-wedge trial | تجربة الإسفين المتدرج | usage | |
| Online A/B test | اختبار A/B عبر الإنترنت | [4] | |
| Adaptive / platform trial | تجربة تكيفية / منصّية | usage | |
| Field experiment | تجربة ميدانية | usage | |
| Ethnography | الإثنوغرافيا | usage | Participant observation → الملاحظة بالمشاركة. |
| Grounded theory | النظرية المجذّرة | [4] [8] | Both المجذّرة and المتجذّرة are in use (Arabic Wikipedia gives both; Arabic research-methods teaching sites mostly use المجذّرة). Others: المؤسَّسة، نظرية التأسيس. |
| Interviews & thematic analysis | المقابلات والتحليل الموضوعاتي | usage | التحليل الموضوعي is also common but reads as "objective analysis". Themes → الموضوعات. |
| Case study | دراسة حالة (معمقة) | [4] | |
| Process tracing | تتبّع العمليات | usage | Hoop test → اختبار الطوق; smoking gun → الدليل الدامغ. |
| Delphi consensus | إجماع دلفي | [4] | |
| Mixed methods (sequential) | الأساليب المختلطة (المتتابعة) | usage | Alternatives: المناهج / البحوث المختلطة. |
| Systematic review & meta-analysis | مراجعة منهجية وتحليل تلوي | [2] [4] | |
| Scoping review | مراجعة نطاقية | usage | Alternative: المراجعة الاستكشافية (ambiguous with a general literature search). |
| Network meta-analysis / IPD meta-analysis | التحليل التلوي الشبكي / تحليل تلوي لبيانات المشاركين الفردية | usage | |
| Umbrella / rapid / realist review | مراجعة مظلية / سريعة / واقعية | [4] | |
| Prior art review | **مراجعة حالة التقنية السابقة** | [5] [6] | WIPO Arabic: حالة التقنية (الصناعية) السابقة; Saudi IP Authority guide titled "حالة التقنية السابقة". Draft lacked حالة. Novelty → الجِدّة. |
| Co-citation analysis | تحليل الاستشهاد المشترك | [7] usage | Older Arabic LIS term: المصاحبة الاستشهادية. الاستشهاد المشترك is transparent and appears in some recent Arabic bibliometric studies. |
| Bibliographic coupling | **المزاوجة الببليوجرافية** | [7] | was الاقتران الببليوغرافي; المزاوجة is the term in Arabic library-science writing. Alternative: الاقتران / الازدواج الببليوغرافي. |
| Multivocal literature review | مراجعة الأدبيات متعددة الأصوات | usage | Grey literature → الأدبيات الرمادية [4]. |
| Diagnostic accuracy study | دراسة الدقة التشخيصية | usage | Sensitivity / specificity → الحساسية / النوعية [4]. Reference standard → المعيار المرجعي. |
| Reliability & agreement study | **دراسة الثبات والاتفاق** | usage | was الموثوقية; see "reliability". |
| Instrument development & validation | تطوير الأداة والتحقق من صدقها | usage | Psychometrics → القياس النفسي [4]. |
| Nomological network study | دراسة الشبكة الناموسية | usage | ناموس = law, matching *nomo-* (law-like). Arabic Wikipedia's "شبكة اسمية" confuses it with *nomen* (name) and should not be followed. Alternative: الشبكة النوموثيتية / القانونية. |
| Discrete choice experiment | تجربة الاختيار المنفصل | usage | Willingness to pay → الاستعداد للدفع. |
| Interlaboratory comparison | المقارنة بين المختبرات | usage | Proficiency testing → اختبار الكفاءة. |
| Analytical / mathematical theory | نظرية تحليلية / رياضية | usage | |
| Computational simulation | المحاكاة الحاسوبية | [4] | Agent-based → قائم على الوكلاء [4]. |
| Prediction model | نموذج تنبؤي | [4] | Discrimination / calibration → القدرة التمييزية / المعايرة. |
| Cost-effectiveness analysis | تحليل فعالية التكلفة | [4] | QALY kept as QALY (سنة حياة معدلة بالجودة). |
| Design science | علم التصميم (بناء وتقييم) | usage | Artifact → مُنتَج (draft "أداة" clashed with measurement "instrument"). |
| Pilot / feasibility study | **دراسة استطلاعية / دراسة جدوى** | usage, [4] | was دراسة تجريبية أولية, where تجريبية reads as "experimental". Arabic Wikipedia: دراسة استرشادية. |
| Usability test (think-aloud) | اختبار قابلية الاستخدام (التفكير بصوت عالٍ) | [4] | |
| PDSA cycles | دورات خطِّط–نفِّذ–ادرُس–تصرَّف | usage | Run chart → مخطط التشغيل; control limits → حدود الضبط. |
| Benchmark evaluation | تقييم مرجعي مقارن | [4] | Ablation → الاستئصال (ablation) [4]. |

## Threats

| English | Arabic | Note |
|---|---|---|
| Confounding / by indication | الإرباك / **الإرباك بالاستطباب** | was الإرباك بالدواعي |
| Selection bias | تحيز الاختيار | [4] |
| Attrition & missing data | **الاستنزاف والبيانات المفقودة** | was الفقد; الاستنزاف follows Arabic usage around intention-to-treat ("الاستنزاف غير العشوائي للمشاركين" [4]). تسرّب is reserved for data leakage. |
| Recall bias | تحيز الاستدعاء | [4]; alternative: تحيز التذكر |
| Regression to the mean | **الانحدار نحو المتوسط** | was الارتداد |
| Contamination & spillover | **التلوث وانتقال الأثر** | was التلوث والانتشار (انتشار already means prevalence) |
| Immortal time bias | تحيز الزمن الخالد | literal rendering used in translated material; alternative: تحيز الوقت الخالد. Not found in an authoritative Arabic source. |
| Collider bias | تحيز المُصادِم | literal; text also names تحيز Berkson. Not found in an authoritative Arabic source. |
| Survivorship bias | تحيز النجاة | Arabic Wikipedia: انحياز البقاء |
| Publication bias | تحيز النشر | [4] |
| Forking paths & p-hacking | المسارات المتشعبة والتلاعب بقيمة p | |
| Overfitting & leakage | **فرط الملاءمة والتسرّب** | was فرط التلاؤم; Arabic Wikipedia: فرط الملاءمة. Leakage → تسرّب البيانات. |
| Spectrum bias | تحيز الطيف | [4] |
| History & secular trends | التاريخ والاتجاهات الزمنية | Campbell's "history" threat = عامل التاريخ |
| Carryover | الأثر المتبقي | |
| Limited generalizability | محدودية التعميم | |
| Apples & oranges | تفاح وبرتقال | idiom kept because the card art shows the fruit; the concept is عدم التجانس |
| Wrong construct | المفهوم الخطأ | see "construct" |

## Safeguards

| English | Arabic | Note |
|---|---|---|
| Randomization | **التوزيع العشوائي** | was التعشية |
| Allocation concealment / Blinding | إخفاء التخصيص / التعمية | |
| Placebo or sham control | **دواء وهمي أو إجراء زائف للمقارنة** | was شاهد بدواء وهمي … |
| Intention-to-treat | **تحليل النية للعلاج** | was التحليل بقصد المعالجة; Arabic Wikipedia title and common usage |
| Negative controls | **الضوابط السلبية** | was الشواهد السلبية; alternative (lab science): الشاهد السلبي |
| Concurrent control group | **مجموعة ضابطة متزامنة** | |
| Pre-trend check & control series | فحص الاتجاه المسبق و**سلسلة ضابطة** | |
| Washout period | **فترة إزالة الأثر** | was فترة الإزالة |
| Multiplicity correction | **تصحيح تعدد الاختبارات** | was تصحيح التعددية (التعددية = pluralism) |
| Matching / propensity scores | المطابقة / درجات الميل | |
| Sensitivity analysis | تحليل الحساسية | [4] |
| Active comparator, new users | مقارن فعّال، مستخدمون جدد | prevalent users → المستخدمون الحاليون |
| Reflexivity / Triangulation / Theoretical sampling to saturation | الانعكاسية / التثليث / المعاينة النظرية حتى التشبع | [4] |
| Verification & validation | التحقق والمصادقة | Arabic Wikipedia: التحقق والتثبت |
| Run charts & control limits | مخططات التشغيل وحدود الضبط | |

## Still open (for a native methodologist)

1. **Randomization**: this edition uses التوزيع العشوائي in running text and in the safeguard and Mendelian-randomization names, but keeps معشّاة inside the fixed RCT/cluster-RCT names. A purely medical audience might prefer التعشية throughout.
2. **Reliability**: الثبات (psychometrics) was chosen over الموثوقية. Medical and engineering readers may expect الموثوقية, especially for the reliability-and-agreement card.
3. **Collider bias, immortal time bias, nomological network, washout period**: no authoritative Arabic form was found; the renderings are literal or descriptive.
4. **Cohort**: أترابية is the EMRO form, but Levantine and North African readers often know الأفواج / الفوجية better.
5. **Synthesis**: توليف was preferred to keep synthesis distinct from pooling (دمج); check that this matches current Arabic evidence-synthesis teaching.

## Sources

1. WHO EMRO, *Eastern Mediterranean Health Journal*, Arabic abstract of Araban et al. (2012) "تلوث الهواء وانخفاض وزن الوليد: دراسة أترابية من طهران", EMHJ 18(6):556–560. https://applications.emro.who.int/emhj/v18/06/18_6_2012_0556_0560.pdf
2. WHO EMRO, Unified Medical Dictionary (المعجم الطبي الموحد). https://umd.emro.who.int/WHODictionary/ (online search returned no results during this review; see note above).
3. World Bank, P. Gertler, "تقييم الأثر: تحويل الوعود إلى إثباتات" (Arabic slides, Cairo workshop). https://thedocs.worldbank.org/en/doc/440141526059353339-0090022018/original/20OperationsGertlerCairoArabicEdited.pdf
4. Arabic Wikipedia article titles and texts, retrieved 30 October 2026 through the Wikipedia API (e.g. تجربة منضبطة معشاة، دراسة الحالات والشواهد، دراسة مستعرضة، تحليل تلوي، تحليل النية للعلاج، نظرية متجذرة، فرط الملاءمة، تقييم الأثر). Used as evidence of current usage, not as an authority.
5. WIPO, دليل الويبو لصياغة البراءات (2nd ed., Arabic). https://www.wipo.int/edocs/pubdocs/ar/wipo-pub-867-23-ar-wipo-patent-drafting-manual.pdf
6. Saudi Authority for Intellectual Property, "الدليل الخاص – حالة التقنية السابقة" (2023). https://externalportal-backend-production.saip.gov.sa/sites/default/files/2023-11/
7. Arabic thesis on the bibliometrics of Omani medical journals (sections 2.2.2–2.2.3: المزاوجة الببليوجرافية، المصاحبة الاستشهادية), VTechWorks. https://vtechworks.lib.vt.edu/bitstream/handle/10919/71487/417_1.doc.txt?sequence=2
8. "النظرية المجذرة طريق نحو أبحاث مبتكرة", Attaa. https://attaa.sa/library/view/1100
9. Arabic Wikipedia, "تقييم الأثر" (مجموعة المعالجة / المجموعة الضابطة). https://ar.wikipedia.org/wiki/تقييم_الأثر
