# Broader LLM agency — local comparative evaluation protocol

**Version:** 0.1, designed 2026-10-05

**Responsibility:** compare investigation and experimental recommendation quality before choosing product architecture or delegated authority.

**Authorization:** Ali selected open research on a separate branch, then this concrete protocol-design step. Ali explicitly selected **local-only** model comparisons. This artifact designs future execution; it does not itself authorize implementation, model loading, inference batches or third-party execution. Live selection belongs to [MEMORY.md](../MEMORY.md).

**Research basis:** [broader-agency dossier](../proposals/2026-10-05_BROADER_LLM_AGENCY_RESEARCH_DOSSIER.md). Progression and procedural adaptation belong to the [single research working memory](../working-memory/2026-10-05_2052_broader-llm-agency-research.md). Dated feasibility observations belong to the [metadata/source snapshot](../working-memory/evidence/2026-10-05-broader-llm-agency-protocol/local-model-and-reference-snapshot.json).

## 1. Decision and complete responsibility

For a concrete dependency-update proposal, help a maintainer understand relevant changes, affected target paths and environments, what existing checks establish, important unknowns, and the most useful next decision or investigation. Wider agency might improve any of these responsibilities, including inventing a useful investigation beyond predefined product categories.

The first comparison asks: **does letting a local model direct evidence gathering, reasoning and stopping improve this support over a well-designed fixed LLM workflow using the same evidence access and resource ceiling?** Both may propose independent recommendations. Neither is restricted to the product's currently implemented abstention action.

This separates two freedoms: deciding **what to investigate and recommend**, and **executing consequential actions**. The first experiment gives broad freedom over the former. A later execution experiment addresses reproductions and repairs with its own causal observations and containment. Changing both together would leave the source of improvement unclear.

| Outcome of the broader program | Included in the first comparison | Deferred capability and reason | Expansion condition |
|---|---|---|---|
| Discover and explain target-relevant effects | Broad change hypotheses; arbitrary source queries; target/CI/environment analysis within frozen public evidence | Unrestricted live-web discovery: changing information would obscure a paired comparison | Separate acquisition trial with common decision-time availability and recorded sources |
| Choose useful investigation and stop | Agent-selected queries, revisits, hypothesis changes, uncertainty and stopping | Unknown-code execution: introduces environmental and causal-validation responsibilities | Select the execution extension in §12 |
| Help decide what to do | Independent experimental advice with facts, hypotheses and conditions | Product action admission and external repository writes: need a later product decision | Repeated capability evidence, usefulness review and explicit owner reconciliation |
| Preserve and recover the investigation | Exact source references, visible trace, final claim ledger and session reset | General resume and long-lived agent memory: separate experimental factor | Select interruption/memory comparisons after basic control is measurable |
| Obtain useful results economically | Local models, measured time/tokens/reviewer effort | Multi-agent topology, graphs and framework competitions: additional interacting factors | A concrete failure or opportunity from this comparison justifies that factor |

These exclusions are temporary experimental sequencing, except hosted inference, which is outside Ali's selected local-only scope. They do not redefine the eventual product horizon. A poor first result under limited context cannot establish that broader agents are intrinsically unsuitable.

## 2. Questions and possible outcomes

1. Does adaptive control find material effects a fixed workflow misses, particularly indirect use, conditional activation and missing CI observations?
2. Does it reduce irrelevant investigation, premature conclusions or unnecessary abstention?
3. Are any gains explained by evidence selection, a different deployment, more compute or a better tool interface rather than control itself?
4. Can reviewers recover the basis of a recommendation and identify its remaining conditions with reasonable effort?
5. Which decisions are promising delegation candidates: change interpretation, localization, investigation planning, stopping, synthesis or a combination?

Credible outcomes include a richer fixed workflow, an agent-led investigator, a hybrid with task-dependent routing, or an inconclusive comparison requiring better capacity/tools/cases. None is the preferred answer embedded in the scoring.

## 3. Comparators and fairness

| ID | Method | Model responsibility | Purpose and claim limit |
|---|---|---|---|
| R | Existing product investigation at a pinned committed revision | Existing configured semantic role; otherwise current owned producers | Current capability reference. Its narrow action vocabulary is scored as missing capability where relevant, never used as the answer key |
| F | Rich fixed LLM workflow | Interpret sources, generate search queries, assess exposure/coverage, synthesize and challenge advice within a scheduled workflow | Strong alternative to broader control; multiple model calls and substantial context, rather than a deliberately weak one-shot prompt |
| A | Agent-led investigator | Choose queries, files, tool arguments, order, revisits, hypothesis updates and stopping; independently recommend | Main agency comparison. Host owns tool safety, identities and budget accounting; model owns the investigative policy |

F and A use the same model deployment within each paired comparison, initial identity/diff packet, source corpus, tool implementations, citation representation, report requirements and resource ceiling. They begin without R's conclusions. They may obtain different evidence because selection is part of the policy being measured. They have equal **access**, not identical observed context or required token consumption. Report actual consumption alongside quality.

F's provisional schedule is: upstream-change interpretation → consumer localization → conditional/environment/CI assessment → synthesis → challenge/revision. Initial allocations are four inference calls, four, four, two and two respectively, under the total 16-call ceiling. The host deterministically skips empty stages and pages oversized material; the model chooses queries and relevant files within the stage. It cannot freely reorder/revisit stages. A may use the entire budget in any useful order. Freeze F's routing, pagination and unused-budget policy after development; do not tune them on protected outcomes. F's stage partition is an intentional policy difference, not evidence deprivation.

The new source-only API interpreter can inform F's rendering/citation boundary. Its current schema or change categories must not become the exhaustive discovery vocabulary for either arm. Any reuse/changed prompt is a separately identified experimental configuration, not the pinned interpreter's already-proved semantic performance.

R is a product reference, not the causal estimate of agency. Current product inference, if invoked by R, is recorded and counted separately; R is not described as cost-free or wholly deterministic. Run R once per development/protected case with exact configured identities. If unavailable or methodologically non-comparable, retain the reference failure without blocking a valid F–A comparison or inventing a reference answer.

Two predeclared development diagnostics help explain differences:

- **Shared-evidence replay:** for two development cases, give F and A the same neutral, source-linked evidence packet assembled from the union of their retrieved evidence, with conclusions removed. This probes whether differences persist after discovery; it does not fully isolate every reasoning factor.
- **Context/budget sensitivity:** on the same two cases, compare the core configuration with a larger feasible context or 32-call/40-minute ceiling, changing one factor at a time for both arms. This distinguishes an operational limit from a promising agency policy. Diagnostic trials are additional and are not included in the core totals or protected claims.

Do not relabel these diagnostics as independent protected evidence. Keep the old offered-action planner and LangGraph result as narrow historical clues; a further bounded-planner arm needs a common task/access definition before its score can be compared.

## 4. Local models and deployment feasibility

The dated native model-list GET returned HTTP 200 without inference. It showed the following available candidates; file size is a storage observation, not a GPU-fit measurement.

| Planned role | Local key | Reported quantization / file bytes | Qualification |
|---|---|---|---|
| Primary continuity candidate | `gemma-4-e4b-it-ud` | Q4_K_XL / 5,101,713,792 | Loaded instance reported context 4096 and parallel 4; exact comparative request fit/tool behavior unproved |
| Recommended second-family candidate | `qwen3.5-9b-ud` | Q4_K_XL / 5,966,095,584 | Available, unloaded. Family/tool capability metadata is promising; no claim of superiority or quantized deployment readiness |
| Smaller fallback candidate | `qwen3-4b-instruct-2507` | Q6_K / 3,306,260,928 | Available, unloaded; consider only if the second candidate cannot meet memory/latency/context requirements |
| Optional larger local capacity candidate | `google/gemma-4-12b` or `gemma-4-12b-it-qat` | Q4_K_M / 7,556,574,286 or Q4_0 / 6,975,878,560 | Available, unloaded; substantial runtime/KV overhead may require CPU offload. Not a required core arm |

The maintained environment records an 8-GiB RTX 3070 Laptop GPU; available VRAM/RAM, loaded weights and context costs require fresh measurement. The loaded parallelism observation differs from ENVIRONMENT's historically validated parallelism 1. Preserve this as dated drift, not a silent deployment change. The source snapshot also proves no `src/` or product `tests/` delta between the research fork and the inspected main reference.

Before inference, identify exact GGUF file/hash, upstream/quantizer lineage, backend/app version, tokenizer, effective chat template, offload, context, reasoning/sampling and tool parser. A familiar key is insufficient. Avoid loading/unloading a shared main-workstream model during its evaluation; arrange an idle window or an independent local instance with measured resources when execution is selected. Trial concurrency is one even if the server supports more.

**Capacity ladder:** test exact rendered fit at 4096 first; consider 8192 and 16384 only with explicit experimental deployment setup and measured stability. Prefer the largest useful verified common context, up to 16384, for both models. If only one model is feasible, execute a within-model F–A comparison and state its deployment-specific scope. If contexts differ, retain valid within-model comparisons and do not attribute cross-model differences to reasoning alone. Never silently truncate a request or drop a difficult case to improve results.

**Provider contract probes:** a harmless tool request/result/follow-up; citation/report decoding; truncated output; unsupported arguments; tool errors; exact prompt + tools + template token accounting; final output reserve; usage and reasoning-token reporting. These probes need fresh inference in the later execution step; metadata does not pass them. Native API tokenization of plain text alone does not establish fully rendered request fit.

LM Studio documents custom tool requests through its compatible endpoints, with model-template/parser support affecting the interface. Choose one verified transport for F and A, initially `/v1/chat/completions`; do not assume the native `/api/v1/chat` request fields apply to it. If native tool parsing fails, diagnose template/parser versus model response first. A common explicitly labelled text/JSON-action interface is a legitimate alternate experiment, not an unreported repair. [Tool-use documentation](https://lmstudio.ai/docs/developer/openai-compat/tools), [model metadata](https://lmstudio.ai/docs/developer/rest/list), [tokenization documentation](https://lmstudio.ai/docs/python/tokenization).

Qwen's official model card describes tool use and default thinking, but recommends substantially larger context/output allowances for complex work. The proposed small-context deployment therefore tests **our local operating configuration**, not the model's maximum capability. Prefer a verified non-thinking configuration for the core resource comparison; if disabling reasoning is unsupported, qualify that deployment or identify an alternate arm. Provisional Qwen non-thinking sampling is temperature 0.7, top-p 0.8, top-k 20, min-p 0, presence penalty 1.5; validate actual backend support. Gemma's exact sampling is frozen after development. Keep settings identical across F/A within each model; disclose model-specific settings rather than forcing inappropriate universal defaults. [Official Qwen3.5-9B model card](https://huggingface.co/Qwen/Qwen3.5-9B).

No model download, hosted option, paid inference, backend replacement or product deployment substitution is part of this protocol-design increment.

## 5. Evidence workspace and tools

Each case has a read-only decision-time evidence workspace: target base tree, proposed dependency/lock diff, identified upstream old/new release evidence, relevant adapter trees, public metadata and CI observations available at the chosen cutoff. Include manifests, lockfiles, configs, docs and source broadly, not just files an earlier investigator found useful. Freeze repository/revision/path/content identities. Missing observations are explicit.

Provide these generic tools through the same implementation for F and A:

| Tool | Permitted parameters and returned evidence | Why it belongs |
|---|---|---|
| `list_sources` / `list_paths` | Repository/source ID, path prefix; paged inventories with exact revisions | Discover relevant evidence without a case-specific action menu |
| `read_source` | Source ID, path, line range; exact text, offsets/hash and omission status | Progressive source access with recoverable citations |
| `search_sources` | Text/regex, repository/path filters; bounded matches with pagination | Model invents its own searches and follows indirect usage |
| `read_diff` | Frozen repository/revision pair and path | Distinguish proposed change from unrelated head source/history |
| `inspect_python_structure` | Frozen source/path/symbol; static imports/declarations/calls, with limitations | Optional reusable AST view; never claims installed binding or runtime reachability |
| `read_observation` | Frozen CI/run/job/attempt or package-metadata ID | Inspect exact observation scope, time and missingness |
| `record_note` / `finish_report` | Trial-local hypotheses, evidence references, next investigations and final report | Preserve visible investigation state and allow model-chosen stopping |

The source index reveals names and identities, not expected answers or labels. Both methods can read unfiltered bytes, structured static views and observations. No hidden oracle-derived prioritization. If the optional AST tool is not built, omit it from both arms and identify that configuration; textual discovery remains a complete simpler baseline. Freeze deterministic paging/order, search syntax and per-response limits after development, with continuation handles and explicit completeness/omission flags; do not make a tool silently return only an oracle-selected match.

Host limits govern paths/bytes/time, not the permissible hypotheses or investigation categories. No arbitrary shell, package installation, target-code imports, credential access, unrestricted network or writes to target/upstream/main are present in the first tool catalog. Treat externally supplied instructions as source data, including target `AGENTS.md`; source content cannot grant execution permission. Frozen-tool acquisition quality and breadth remain measured limitations.

## 6. Cases, sampling and leakage controls

### Development set: six known real cases

| Case | Exact existing clue | Development responsibility / oracle caution |
|---|---|---|
| D1 | [Pydantic / Soup Sieve (S001)](../product-simulation/scenarios/S001-pydantic-soupsieve-2.6-to-2.8.4/README.md) | Separate source support drop from target declaration/applicability; reconstructed history and unresolved trigger are not runtime proof |
| D2 | [Dashboard token API / HTTPX (S002)](../product-simulation/scenarios/S002-kubernetes-dashboard-token-api-httpx-0.27.2-to-0.28.1/README.md) | Indirect Starlette/FastAPI exposure and missing exact resolver/test evidence; do not convert a possible version path into observed breakage |
| D3 | [glyphsLib / pytest (S004)](../product-simulation/scenarios/S004-glyphslib-pytest-9.0.2-to-9.0.3/README.md) | Adequate public checks and justified stopping; repeated investigation may add no value |
| D4 | [ModelArrayIO / pytest (S005)](../product-simulation/scenarios/S005-modelarrayio-pytest-9.0.3-to-9.1.1/README.md) | Challenge an overly cautious baseline using exact target evidence; scenario conclusion is not an independent gold label |
| D5 | [CARLA / OpenCV (S008)](../product-simulation/scenarios/S008-carla-opencv-python36-artifact-fallback/README.md) | Wheel-to-source transition versus unsupported source-build-failure inference |
| D6 | [Dictare / MLX extra (S011)](../product-simulation/scenarios/S011-dictare-mlx-optional-extra-ci-coverage/README.md) | Conditional platform/extra activation and non-discriminating CI; no NumPy compatibility verdict |

These clues have already influenced prompts/design, so they are **development evidence**. Recover source identities from their records; independently re-adjudicate useful facts and unknowns. Their reports, decisions, working memories and historical action labels never enter model inputs. The prepared 19 API development cases on main can test the interpretation boundary separately; they are not 19 unseen whole-investigation cases.

### Protected pilot: twelve new cases

Select twelve cases before measured outputs, with four each in these reference strata:

- Material target-relevant concern supported by decision-time evidence.
- No material concern within an explicitly examined scope, with adequate evidence to avoid needless investigation.
- A decision-critical condition remains unresolved; useful next evidence exists or honest stopping is appropriate.

Require at least six consumer repositories, at most two cases per consumer and at most three per dependency family. Include direct API use, wrapper/transitive use, activation/markers, behavior/configuration, installation/artifact or runtime-state uncertainty, and CI coverage/stopping across the set. The strata describe a curated discriminating pilot, not natural prevalence. Record overlap across dimensions; do not promise a meaningful per-category rate from one case.

Candidate sources are fresh public update proposals plus exact source histories, and optionally independently reviewed dependency-migration benchmark instances. Select on structural fit and evidence availability before seeing method outputs. Do not select only cases where the current product fails or only reproducible known breakages. Record all screened candidates and exclusion reasons. An unavailable historical log can be a valid unresolved case, not an automatic exclusion.

Freeze an initial decision cutoff and distinguish source time from retrieval time. Later repaired commits, merged status, subsequent comments and gold patches belong only to the evaluator where needed for corroboration; models cannot read them. Existing model training contamination cannot be ruled out for public cases. New-to-this-research means protected from our prompt tuning, not guaranteed unseen during training.

Reviewer independence: an adjudicator who did not write the trial output builds/validates reference facts from sources before outputs. A human reviews material disputed claims and all consequential recommendation errors. If the same assistant develops the method and constructs/grades the cases without independent review, label the pilot internally reviewed and do not claim independent semantic acceptance. Ali's participation is not presumed, and a second LLM alone does not supply independent ground truth.

A protected case exposed during tuning/diagnosis becomes development material. Record the exposure, retain its result, and recruit a replacement through the same screening procedure before a new measured corpus version. Never quietly erase a hard case or run an adaptive prompt search on the protected set.

## 7. Independent reference and common output

For each case, freeze a reviewer-only reference packet before measured trials:

1. Exact target/update/upstream identities, cutoff and evidence availability.
2. Material source claims, target links and conditions, each with citations and proof class.
3. Which propositions are supported, disproved within scope, or unresolved; alternative valid interpretations.
4. Useful next investigations and acceptable recommendation conditions, without requiring a particular tool sequence or wording.
5. Known excluded surfaces, potential counterevidence and reviewer disagreement.

The current action evaluator, valid JSON, exact quotation, green CI, merged status, existing simulation answer and agreement among models are insufficient as sole correctness oracles. A legitimate novel finding absent from the reference receives blinded source review; do not automatically score it false. Amend a faulty reference with a versioned rationale and rescore all arms affected, preserving original grades.

Both F and A return a readable report plus a lightweight claim ledger: change/target question; exact cited sources/observations; supported interpretation versus hypothesis; activation/environment conditions; scope examined/unexamined; recommendation and conditions; next investigation and expected discriminator; stopping reason. Allow concerns outside predeclared categories and recommendations beyond current product action enums. Confidence wording is optional and not assumed calibrated.

A report can succeed by explaining a justified unknown. Unsupported certainty about compatibility or breakage cannot be rescued by good prose, an exact citation or a caveat elsewhere. Shape/citation checks grade preservation and grounding, not semantic truth. Judge outcomes, not imitation of a reference trajectory. This design follows primary guidance on repeated trials, separate transcript/outcome checks and calibrated grading, while the specific rubric here is our proposed engineering design. [Agent-evaluation guidance](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents).

## 8. Measures and failure analysis

Report separate dimensions rather than a single weighted score that hides errors:

| Measure | Definition / denominator |
|---|---|
| Satisfactory investigation | Per trial: covers reference material issues/conditions, contains no critical unsupported claim, preserves decision-critical unknowns and gives a useful scoped recommendation/stop. Report count over all assigned trials |
| Material issue recall | Supported material reference issues correctly identified / all such issues in the case. Partial and uncertain claims scored separately |
| Unsupported material claims | Count and severity of ungrounded or misinterpreted consequential claims per trial, plus affected-case count; include invented breakage and false reassurance |
| Conditional reasoning | Correct handling of activation, temporal state, binding and observation scope / relevant reference conditions |
| Appropriate stopping | Adequate-evidence cases stopped without unnecessary next work; unresolved cases request a discriminating observation or explain why none is proportionate |
| Failure/abstention | Transport, capacity, parser, tool, budget, semantic uncertainty and empty-output outcomes, each over all assigned trials; no survivor-only accuracy |
| Reviewability/usefulness | Reviewer can recover source basis and conditions; time to assess/correct; required follow-ups; material corrections and recommendation utility |
| Resource cost | Inference/tool calls, cumulative input/generated tokens, available reasoning-token counts, wall/service time, source bytes, timeout/OOM, CPU/GPU memory and storage |
| Repeatability | Successes and critical errors per case across three repeats; same-prompt seed/control limitations recorded |

Severity rule: critical means a claim or recommendation could materially change the maintainer decision in the wrong direction within the task scope. Both false reassurance and invented blockers qualify. Other material errors remain visible; formatting defects alone do not receive critical semantic severity. Reviewer severity/novel-finding disputes require rationale, not silent grade edits.

For grading, hide method IDs and randomize report order where practical; record imperfect blinding and evaluator familiarity. Repeated reports of the same case create learning/practice effects. Compare review times under balanced presentation and disclose those effects; one reviewer's timing is formative evidence, not a causal human-productivity result. Optional model grading can flag issues, but it cannot overrule source adjudication or replace human review of consequential disputes.

For each failure, trace evidence through acquisition → rendering/context → inference → tool interface → reasoning → report → evaluator. Assign supported primary cause and secondary contributors: missing source, wrong binding/identity, truncation, environment contention, unsupported parser, model interpretation, flawed stopping, inappropriate constraint, or faulty oracle. Do not blame agency merely because its deployment ran out of context, and do not excuse a real semantic error merely because the harness has limitations.

Inspect every critical error and every discordant case; sample matched successes for missed issues. Keep total-system reliability and diagnostic semantic performance among valid inferences separate. Infrastructure failures remain in the overall denominator. Any rerun is appended under a new run ID with a reason; no hidden retries or best-of-three selection.

## 9. Budgets, repetitions and local cost

Proposed core limits, frozen after development for each comparable configuration:

| Resource | Ceiling per F/A trial |
|---|---|
| Inference calls | 16 total, including compaction, challenge and format repairs |
| Generated tokens | 16,384 aggregate, including reasoning where reported/accountable |
| Input tokens | 49,152 cumulative tokens across calls, including repeated context/tools/template |
| Request fit | Exact effective context minus reserved completion; default output reserve 1024, final-report reserve 1536 |
| Tool operations | 48 total; batches count each underlying operation |
| Evidence output | 8 MiB total returned source bytes, paged rather than silently cut |
| Trial wall time | 20 minutes; record actual latency and timeout |
| Concurrency | One trial on the local inference deployment |

These ceilings represent equal available resources, not a target to exhaust. At 4096 context, a 1536-token final reserve leaves at most 2560 rendered input tokens, including all template/tool overhead. Hold back final-report tokens and one inference call before issuing further investigative calls; clamp each completion allowance to the aggregate remainder. The common evidence ledger must support cited findings without stuffing the full transcript into that request. Any model-driven compaction counts as inference; exact source evidence remains recoverable outside model context. Budget exhaustion returns explicit partial/failed evidence, never an unearned favorable answer.

Use three fresh repeat IDs per protected case/arm/model; record seeds only where demonstrably supported. Temperature zero is not a proof of deterministic provider execution. Reset notes, session history and outputs between trials. Use a balanced pre-generated case/arm order within model blocks; disclose model-block/hardware temporal effects. Cache frozen source acquisition consistently, isolate trial artifacts, and report cold versus warm inference policy.

| Stage | Cases × arms × repeats × models | F/A trial count with two feasible models |
|---|---|---:|
| Technical feasibility | Two development cases × 2 × 1 × 2 | 8 |
| Development/tuning | Six development cases × 2 × 2 × 2 | 48 |
| Protected measured pilot | Twelve cases × 2 × 3 × 2 | 144 |
| Core total | Sum above | 200 |

With one feasible model the core total is 100 and the protected count 72. R adds eighteen reference investigations, one per distinct development/protected case, with its own inference/time accounting. Provider contract probes, case acquisition/adjudication, optional diagnostics and human review are additional; this is not a 200-call estimate. The 200 F/A trials allow at most 3200 inference calls, 9,830,400 input tokens, 3,276,800 generated tokens and 66 hours 40 minutes of trial wall time at these ceilings. Protected trials alone cap at 48 hours. Actual requirements could be substantially lower; no throughput forecast is claimed from metadata.

Measure prefill/decode rate, end-to-end latency and review time during technical feasibility, then forecast the full run as sum of expected trial durations plus source/review/setup time. Report CPU-offload and contention explicitly. Local-only means no API bill; machine occupancy, electricity, storage and Ali's attention still cost resources. No electricity-price or hourly-cost estimate is invented. Development may adjust limits proportionately before protected freeze; a later limit change creates a new comparable configuration rather than silently rescuing selected failures.

## 10. Analysis and decision rules

The unit for paired comparative claims is the **case**, with repeats describing within-case variation. Seventy-two trials per model are not seventy-two independent cases. Show all twelve paired case results, repeat distributions, wins/regressions/ties, critical errors and measured costs. A case win means A succeeds on at least two of three repeats while F succeeds on at most one; a regression is the converse. Cluster uncertainty calculations by case if used; a tiny curated pilot does not establish deployment prevalence or precise rare-error rates.

Freeze these proposed engineering triage criteria before protected outputs, and report sensitivity rather than treating them as scientifically validated thresholds:

- **Candidate for broader control or a hybrid:** at least three of twelve case wins and at most one regression by the repeat rule above; A has zero observed critical errors; median reviewer assessment time is at most 1.25× F and median trial time at most 2× F. Review cross-model consistency where a second model is feasible. This qualifies further testing/design consideration, never automatic product authority.
- **Fixed workflow or selective agency:** F performs comparably with lower operational/review cost, or A's benefits concentrate in a traceable family. Preserve useful model responsibilities rather than rejecting LLM breadth as a whole.
- **Inconclusive / repair the experiment:** source/oracle/capacity/tool failures dominate, important protected strata cannot be adjudicated, or differences are smaller/unstable. Diagnose and version the next comparison instead of declaring a winner.
- **Promising but consequential-error-prone:** A finds additional issues but has critical recommendation errors. Consider investigative assistance with independent decision review, and evaluate the failure mechanism before expanding authority.

These criteria are one practical recommendation for deciding what to research next, not product safety policy. Zero observed critical errors in twelve curated cases cannot prove a low future error rate. For perspective, even twelve independent random cases with zero errors would have a one-sided 95% binomial upper error bound of about 22%; our stratified curated corpus does not satisfy that population-sampling assumption.

Apply the same semantic grading to F. A case where both arms fail may still expose useful partial capability, but is not an accepted full investigation. A best result at doubled budget is reported as a different efficiency point, not the equal-budget winner. Publication of a pilot report does not select architecture or change specifications/ADRs.

## 11. Execution sequence and proof obligations

1. **Select the bounded execution increment:** experiment-local F/A runner, generic read-only tools, preserved output and provider probes; no product integration/dependency/framework change by default. Consult exact source/tests and the Build procedure at that point.
2. **Reconcile main/reference and runtime:** pin immutable source revisions; preserve the currently building checkout; arrange local inference availability; identify capacity/model lineage and actual parser/template behavior.
3. **Build the simplest common harness:** ordinary Python is the baseline. Use existing pure source/identity mechanisms where suitable. A framework is justified only by a measured lifecycle/control need, not its name. Keep product dependency direction intact.
4. **Verify engineering mechanics before semantic trials:** controlled-provider tests for identical access, arbitrary valid queries, stage/free-control distinction, all budget counters, reset/isolation, pagination, truncation/tool/provider errors, missing observations, trace preservation and oracle non-exposure. A case with an intentionally wrong but well-cited meaning must remain semantically wrong. No passing engineering suite claims model quality.
5. **Run technical feasibility:** fresh harmless provider probes, then two development cases per arm/model; measure actual fit/resource behavior. Diagnose infeasible deployment before attributing agency failure.
6. **Develop and freeze:** complete six-case development; tune prompts/tools within declared scope; independently prepare protected corpus/reference. Freeze method/source/model identities, sampler, context/memory policy, budgets, rubric, screened-case ledger and randomized trial schedule. Publish a public-safe manifest digest before measured results.
7. **Run protected repeats:** preserve all assigned outcomes and counters. No grader/gold history is reachable by model tools. Stop the batch if isolation/privacy/source-integrity failures occur; keep incomplete results explicit. Ordinary semantic failures are results, not permission to erase cases.
8. **Adjudicate and analyze:** blinded reference review, novel finding/disagreement handling, all-case paired table, diagnostic causes, reviewer usefulness/time and residual limitations. Share source-backed examples before a design decision.
9. **Choose the next responsibility:** strengthen/retest a promising arm, select a hybrid, design the execution extension, or retain the simpler workflow. Any product adoption reconciles the accepted owners separately.

The first experiment implementation uses `experiments/broader_agency_pilot.py`, with source access in `broader_agency_workspace.py`, trial control in `broader_agency_trial.py` and local transport in `broader_agency_local.py`. Product behavior and semantic acceptance remain separate proof responsibilities.

## 12. Predefined expansion experiments

Execution/reproduction deserves its own comparison once source investigation is observable. It does not require a first-round agency victory: it can be selected earlier if a concrete task and admitted environment make execution the better discriminator.

- Use six source-adjudicated cases with independently reproducible old/new behavior, plus controls where no change should be asserted. Admit exact repositories/packages/commands and resources before running unknown code.
- Compare F and A with identical isolated build/test tools and budgets. The model may design tests/patches; test evaluation is separate from generated explanations.
- Require old-environment control, new-environment observation and a target-relevance check. If both old/new fail, setup is unresolved; if a repair is tested, new+repair should address the changed behavior without weakening tests, and broader unaffected checks should remain green.
- Keep evaluator tests and gold patches outside the working workspace. Generated tests passing alone prove only their exercised assertion. Record resolved dependencies/platform/runner identity and actual end state.
- No secrets, host-main mounts or target pushes; proportionate process/container isolation and resource limits are proved, not assumed from the word sandbox.

A separate live-discovery experiment compares broader source acquisition under common cutoff/access. Interruption/memory, equal-compute single-agent versus challenger/multiple agents, selective-confidence policies and maintainer interaction are independently named follow-ups. Confidence calibration needs a larger held-out population; twelve cases support failure exploration rather than deployment thresholds. A single reviewer can provide formative usefulness feedback, not a causal general human–AI benefit claim.

For trust robustness, add explicitly labelled perturbations to two development packets: hostile instructions inside retrieved source, and distracting/unrelated evidence. Compare original/perturbed utility and attempted instruction-following for both arms, with harmless canaries and no real credentials. Synthetic overlays remain separate from untouched real-case results and are additional diagnostic trials. Passing a few perturbations cannot establish prompt-injection resistance; forbidden host capabilities remain unavailable even if a model requests them.

Dependency-specific research reinforces retaining both structured workflows and agents as alternatives. DepRepair's selected methods use consumer/upstream evidence and post-generation executable tests; in-loop execution is absent, so its results do not answer the execution-feedback extension above. Its corpus selects reproducible breakages, while this protocol also needs negatives and unresolved conditions. Its reported oracle is limited by test coverage and it does not significantly beat the strongest agent comparison. These are inspected author results, not reproduced local evidence. [DepRepair benchmark, methods and limitations](https://arxiv.org/html/2607.17957v1).

## 13. Evidence retention, boundaries and completion

Future run artifacts record configuration/corpus hashes, public evidence identities, source omissions, model/tool outputs needed for evaluation, counters, failures, final claim ledgers, reference/grading versions and review rationale. Keep raw model requests/responses and sensitive/private captures local and excluded from Git; publish reviewed structured claims, public-safe manifests, aggregates and reproductions sufficient to inspect the evidence boundary. Review target text/output for secrets before publication. A digest detects identity drift; it does not prove authenticity or semantic correctness.

Each trial ID identifies method/model/case/repeat/corpus/configuration. Preserve visible planning notes/tool calls and failures needed for diagnosis; do not require private chain-of-thought to judge success. Record reasoning-token counts where available, and mark accounting gaps. If hidden generation cannot be bounded or accounted for comparably, qualify or reject the resource-efficiency contrast.

The design step is complete when the comparison, candidate deployments, corpus/reference method, tools, budgets, measures, failure analysis and execution dependencies are concrete and internally consistent. Runtime feasibility, independent labels and semantic success remain future proof. Final architecture/authority selection follows evidence and discussion with Ali; this plan cannot promote experimental proposals into product findings or external action permission.

Reassess/version the protocol when task responsibility, source availability, deployment/template/interface, corpus protection, budget or oracle changes materially. Preserve earlier manifests/results; position-neutral plans describe the agreed experiment, while dated working memory records evolution and MEMORY.md selects continuation.

## 14. First technical pilot configuration

The two known-development cases are the HTTPX/framework/CI and glyphsLib/pytest cases identified above. Both arms receive the same pinned target base/head, upstream old/new text and bounded historical public CI observations. Selected framework source is included as a declared development clue in both arms. Historical interpretations, disposition reports and grader answers are excluded. These are deliberately known cases; this acquisition cannot establish unseen discovery performance.

Acquire immutable commit ZIPs without extracting or executing them. Retain UTF-8 text in the declared source/doc/config suffix set, with 2 MiB per-file, 32 MiB per-repository text and 32 MiB compressed-archive ceilings. Record binary/unsupported/oversized omissions and acquisition hashes. Search supports arbitrary literal queries over all retained text; paged reads return exact source line IDs. Missing binary fixtures, full CI logs and installed environments remain explicit limitations, especially for negative claims.

Use ordinary Python and a common **text JSON-action interface** over LM Studio's native stateless chat endpoint. Native function-call support is not inferred or graded. `reasoning=off`, temperature 0.2, no stored chat or server integrations; actual total/reasoning token counts must be supplied. SDK-rendered request counts plus a declared 64-token allowance bound each request before inference and are checked against native input usage afterward. This allowance is conservative measurement evidence, not exact native template identity. Record the SDK version, GGUF file SHA256, model key/path/size, loaded instance and configuration. Load a separately named research instance only when the local server is available; unload only that owned instance. [Native chat request and statistics](https://lmstudio.ai/docs/developer/rest/chat).

For this prototype F follows 4/4/4/2/2 scheduled call slots for upstream interpretation, consumer localization, conditions/CI, synthesis and challenge/report. A selects its next tool and stopping time. Access, limits and report language are identical. F's early finish request is visibly refused until the report stage, except when the aggregate output reserve forces completion. This baseline has no conditional stage skipping yet; its efficiency is not a claim about the best possible fixed workflow. Reverse arm order on the second case; this pilot is formative and has no protected randomization.

Both arms keep a model-written cumulative notebook of at most 2400 characters plus the latest tool page. The full prior trace stays private and sources remain available to re-read. Reads return at most 20 lines/2400 source characters; lines above 1600 characters are explicitly omitted rather than shortened as exact quotes. Searches return six preview matches per page, with incompleteness flagged. The source-byte guard stops before another model request when the just-returned page exhausts the allowance; that terminal page is retained and its actual bytes counted. A finished report with existing references is labelled `completed_ungraded`; reference existence never establishes meaning.

The first run retains every assigned trial, harmless probe, provider receipt, terminal error and configuration under ignored `.tmp/broader-agency-pilot/`. The CLI refuses corpus/code/model drift and output-directory reuse. Each model gets four trials, plus two harmless interface probes. Development failures may motivate a versioned repair, but earlier failed outcomes remain evidence. The next protected comparison requires the broader corpus/reference preparation and independent semantic review specified above.
