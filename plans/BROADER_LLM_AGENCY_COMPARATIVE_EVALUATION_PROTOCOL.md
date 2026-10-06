# Broader LLM agency — local comparative evaluation protocol

**Version:** 0.2, investigation-interface repair design added 2026-10-06

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

F's initial provisional schedule was upstream-change interpretation → consumer localization → conditional/environment/CI assessment → synthesis → challenge/revision, with 4/4/4/2/2 call allocations. Section 14 records the actual first prototype, including its differences from this intention. Section 16 defines the replacement qualification design with explicit stage artifacts and completion rules. A may investigate in any useful order. Freeze F's routing, pagination and unused-budget policy after development; do not tune them on protected outcomes. F's stage partition is an intentional policy difference, not evidence deprivation.

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
| `search_sources` | Explicit literal text, repository/path filters; bounded matches with pagination | Model invents its own searches and follows indirect usage; a regex extension needs separate qualification |
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

Initial version-0.1 limits are preserved below for provenance. Section 16.6 replaces their input/output allowances for version-0.2 qualification. Freeze the selected comparable configuration after development; neither table automatically selects a batch.

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

These ceilings represent equal available resources, not a target to exhaust. Under the initial limits, 4096 context and a 1536-token final reserve leave at most 2560 rendered input tokens, including all template/tool overhead. Reserve final calls/output according to the selected configuration; section 16 requires a report plus possible correction rather than the initial single-call reservation. Clamp each completion allowance to the aggregate remainder. The common evidence ledger must support cited findings without stuffing the full transcript into that request. Any model-driven compaction counts as inference; exact source evidence remains recoverable outside model context. Budget exhaustion returns explicit partial/failed evidence, never an unearned favorable answer.

Use three fresh repeat IDs per protected case/arm/model; record seeds only where demonstrably supported. Temperature zero is not a proof of deterministic provider execution. Reset notes, session history and outputs between trials. Use a balanced pre-generated case/arm order within model blocks; disclose model-block/hardware temporal effects. Cache frozen source acquisition consistently, isolate trial artifacts, and report cold versus warm inference policy.

| Stage | Cases × arms × repeats × models | F/A trial count with two feasible models |
|---|---|---:|
| Technical feasibility | Two development cases × 2 × 1 × 2 | 8 |
| Development/tuning | Six development cases × 2 × 2 × 2 | 48 |
| Protected measured pilot | Twelve cases × 2 × 3 × 2 | 144 |
| Core total | Sum above | 200 |

With one feasible model the core total is 100 and the protected count 72. R adds eighteen reference investigations, one per distinct development/protected case, with its own inference/time accounting. Provider contract probes, case acquisition/adjudication, optional diagnostics and human review are additional; this is not a 200-call estimate. At the initial version-0.1 ceilings, 200 F/A trials allowed at most 3200 inference calls, 9,830,400 input tokens, 3,276,800 generated tokens and 66 hours 40 minutes of trial wall time. At the replacement version-0.2 ceilings, the same hypothetical schedule allows 49,152,000 input and 6,553,600 generated tokens; calls/time are unchanged. Protected trials alone cap at 48 hours. These are upper bounds, not a selected batch or throughput forecast. Re-estimate actual occupancy after qualified development runs.

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

## 14. Historical first technical pilot configuration — version 0.1

This section preserves the original pilot/clarification brief and its limitations. Its execution instructions describe version 0.1; use section 16 for the replacement design. The dated evidence, rather than this position-neutral brief, records actual execution outcomes.

The two known-development cases are the HTTPX/framework/CI and glyphsLib/pytest cases identified above. Both arms receive the same pinned target base/head, upstream old/new text and bounded historical public CI observations. Selected framework source is included as a declared development clue in both arms. Historical interpretations, disposition reports and grader answers are excluded. These are deliberately known cases; this acquisition cannot establish unseen discovery performance.

Acquire immutable commit ZIPs without extracting or executing them. For binary-heavy repositories, a declared alternate transport obtains the complete recursive commit tree (8 MiB metadata/50,000 entries), selects the same text inventory and reads only those raw files, verifying each against its Git blob SHA1 and size. At most six public readers run concurrently; repeated verified blobs may be reused across base/head. Retain UTF-8 text in the declared source/doc/config suffix set, with 2 MiB per-file, 32 MiB per-repository text and 32 MiB compressed-archive ceilings. Record binary/unsupported/oversized omissions and acquisition hashes. Completed same-session captures may be reused with source/revision consistency checks and their original capture-file digest, explicitly labelled as reuse. Search supports arbitrary literal queries over all retained text; paged reads return exact source line IDs. Missing binary fixtures, full CI logs and installed environments remain explicit limitations, especially for negative claims.

Use ordinary Python and a common **text JSON-action interface** over LM Studio's native stateless chat endpoint. Native function-call support is not inferred or graded. `reasoning=off`, temperature 0.2, no stored chat or server integrations; actual total/reasoning token counts must be supplied. SDK-rendered request counts plus a declared 64-token allowance bound each request before inference and are checked against native input usage afterward. This allowance is conservative measurement evidence, not exact native template identity. Record the SDK version, GGUF file SHA256, model key/path/size, loaded instance and configuration. Load a separately named research instance only when the local server is available; unload only that owned instance. [Native chat request and statistics](https://lmstudio.ai/docs/developer/rest/chat).

For this prototype F follows 4/4/4/2/2 scheduled call slots for upstream interpretation, consumer localization, conditions/CI, synthesis and challenge/report. A selects its next tool and stopping time. Access, limits and report language are identical. F's early finish request is visibly refused until the report stage, except when the aggregate output reserve forces completion. This baseline has no conditional stage skipping yet; its efficiency is not a claim about the best possible fixed workflow. Reverse arm order on the second case; this pilot is formative and has no protected randomization.

Both arms keep a model-written cumulative notebook of at most 2400 characters plus the latest tool page. The full prior trace stays private and sources remain available to re-read. Reads return at most 20 lines/2400 source characters; lines above 1600 characters are explicitly omitted rather than shortened as exact quotes. Searches return six preview matches per page, with incompleteness flagged. The source-byte guard stops before another model request when the just-returned page exhausts the allowance; that terminal page is retained and its actual bytes counted. A finished report with existing references is labelled `completed_ungraded`; reference existence never establishes meaning.

A labelled development clarification may repeat the same eight assigned model/arm/case trials once after the initial interface feasibility pass: explain exact action nesting, exclude copied input fields, illustrate a generic search action, reinforce literal-search scope and terminal-report instructions. Keep sources, tools, limits, models and decoder unchanged; freeze the new prompt/code and preserve all earlier failures. This is known-case formative interface repair, not a protected repeat, semantic adoption or independent causal experiment. Count its probes/calls/trials separately from the core schedule.

The first run retains every assigned trial, harmless probe, provider receipt, terminal error and configuration under ignored `.tmp/broader-agency-pilot/`. The CLI refuses corpus/code/model drift and output-directory reuse. Each model gets four trials, plus two harmless interface probes. Development failures may motivate a versioned repair, but earlier failed outcomes remain evidence. The next protected comparison requires the broader corpus/reference preparation and independent semantic review specified above.

## 15. Interface and memory qualification before a broader comparison

A failed tool/report interface is evidence about that configuration, not an agency verdict. Resolve these experiment-design responsibilities before a larger comparison:

1. **Observation provenance:** every next-turn tool observation must retain its originating action, source/query scope and pagination. Private traces alone do not supply that information to the model. Test the path with an empty notebook and zero-hit searches.
2. **Usable memory:** compare the notebook/latest-page prototype with explicit action/observation history or measured context packing under shared budgets. Record memory cost and omissions. Do not silently replace the policy or assume a small model-written notebook preserves all findings.
3. **Verified action/report interface:** qualify client-dispatched typed/native tools where actually supported, including reasoning/usage and a real multi-step source-follow-up/report probe. A framework is not required. Reports may need a distinct terminal interface; typing should preserve provisional meaning rather than impose the product taxonomy.
4. **Visible recovery:** design model-visible tool/action errors inside the declared call/token/time budgets, identically for F/A. Every failed response and correction remains in the trace. This differs from hidden retries or stripping a selected malformed reply into an accepted result.
5. **Credible fixed workflow:** show that its concrete orchestration performs upstream interpretation, consumer localization, conditions/CI and synthesis. Prompt labels alone do not prove those responsibilities. Keep shared source access and explicit costs; qualify any change to supplied initial context.
6. **Reasoning configuration:** evaluate reasoning-off/on separately with measured completion capacity, or label a combined redesign as a new configuration. The first prototype cannot establish reasoning-enabled agent performance.

Use small known-development mechanics/diagnostic cases first, then re-enter the six-case development and protected-reference preparation when both interfaces perform their intended roles. Freeze each comparison before output and preserve earlier attempts. These are design/proof prerequisites, not adopted product architecture, a mandate to add dependencies, or automatic authorization for another full batch.

## 16. Replacement investigation-interface design — version 0.2

This is an experiment implementation design, grounded in the [reviewed sixteen-trial pilot](../working-memory/evidence/2026-10-06-broader-agency-feasibility/README.md) and the current workspace/trial/provider code. Its outcome is a usable, inspectable investigation interface for both policies. It makes no product architecture commitment. Implementation and local qualification are subsequent selected responsibilities; this section is sufficient to enter them without reopening routine design decisions.

The complete responsibility remains maintainer support through relevant changes, target exposure, conditions, check coverage, useful advice and justified stopping. Qualification includes source investigation and final reporting. Live discovery, unknown-code execution, external action, long-term resume and multi-agent arrangements remain the separately selectable extensions in section 12. Narrowing here is temporary: a working observation/history/report path is needed to measure the value of those capabilities honestly.

### 16.1 Responsibility owners and retained baseline

| Responsibility | Experiment owner / selected method |
|---|---|
| Frozen source access, normalized query scope and honest page completeness | `SourceWorkspace` in `experiments/broader_agency_workspace.py` |
| Trial events/history, fixed/agent control, reserves, recovery and finalization | `experiments/broader_agency_trial.py`; small private helpers are sufficient initially |
| Local client tools, terminal schema, rendered-fit and usage qualification | `experiments/broader_agency_local.py` |
| Case/configuration freeze, reset, assigned-run accounting and private artifacts | `experiments/broader_agency_pilot.py` |
| Mechanical/composition proof | `experiments/tests/test_broader_agency_trial.py`; split only if a distinct test responsibility warrants it |
| Semantic adjudication | Reviewer-only references and section 7; unavailable to the running model |

Use ordinary Python and the existing transport/session facilities. No framework, dependency, MCP service or new package layer is necessary for this responsibility. Retain exact corpus/model binding, no-proxy local transport, private raw receipts, reset, budget guards and the distinction between reference validity and meaning. Retain previous run evidence unchanged, but do not keep the mandatory per-action notebook or strict whole-trial termination on a correctable formatting error merely because tests currently assert them. Those are prototype choices, not required product semantics. The [minimum-useful-generality specification](../docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md) remains the product-adoption reference; this experiment may explore broader provisional advice without changing it.

### 16.2 Complete observations

Every tool result includes its normalized scope: source/revision or corpus identity, originating tool and arguments, effective search mode, offset/range, total within that scope, returned count, continuation and explicit omissions. Include these on zero matches, empty pages and tool errors. `SourceWorkspace` owns defaults and completeness because it actually applies them; the trial owner attaches the event ID and pairs the requested action with its result. Avoid reconstructing scope from prose later.

For example, zero hits for literal `starlette|fastapi` must preserve that exact phrase, source/path filters and literal mode. It cannot imply that neither library exists. Paging the CI capture must expose its continuation. Both arms receive identical behavior; no query expansion, answer-dependent prioritization or new semantic absence inference is added.

Keep current literal search and explicit preview/long-line omissions for initial qualification. Assess their usefulness on development evidence before adding regex, larger pages or AST tools. Source citations remain references to exact retained lines; omitted/preview text is never silently promoted into an exact read.

### 16.3 History and model notes

Replace the notebook/latest-result dependency with a measured action/observation history. Keep complete assistant tool-call messages and matching tool results together, including failures and corrections. Native transport must preserve tool-call IDs; the labelled JSON alternative preserves equivalent event pairs in its prompt. Model notes are optional candidate interpretations, retained when emitted, and never a prerequisite for seeing previous evidence. Provide the same trial-local `record_note(text, citations)` to both arms; it stores model-authored text without adjudicating it. Ordinary assistant content and F stage artifacts are also retained as model-authored material, not supplied reference truth.

Use full history while the fully rendered request fits. At pressure, use a deterministic common packing policy: retain the task/tool contract, neutral source catalog, latest whole event pair, latest nonempty model-written note, F's completed stage artifacts where applicable and a compact event directory, then include older whole event pairs from newest to oldest while they fit. An empty note does not erase an earlier note; superseded notes remain recoverable by event ID. The directory contains event IDs, tool/query/source/range scope and whether an event is omitted from this request; it contains no host-generated conclusions. Log the included/omitted event IDs and measured costs on every request. Do not silently crop lines or sever assistant/tool message pairs.

Provide the same trial-local `read_trial_event(event_id)` to F and A so omitted observations can be recovered, using the same paging/byte/operation limits as other observations. It can access only that trial's actions, results and errors; reviewer packets, other trials and private provider reasoning are inaccessible. Replayed evidence costs another operation and rendered input. Repeating older notes does not upgrade their truth. If the indispensable packet cannot fit, stop with explicit capacity evidence rather than erase a material condition.

The common baseline adds no model-driven compaction calls or automatic semantic summary. Those remain a later named memory alternative. A shared-budget development ablation may compare packed history with the old latest-page/notebook policy while holding tools, interface, reasoning and ceilings constant. This can investigate the memory contribution; the whole redesign alone cannot isolate it.

### 16.4 Client tools, terminal report and recovery

Preferred candidate: client-dispatched function tools through local `/v1/chat/completions`, followed by a separate terminal request using `response_format` JSON schema. Investigation tools carry their own arguments; the model no longer has to emit the unrelated outer `notes` field on every action. A tool-free assistant response may signal readiness to report; its prose is retained as provisional material, not accepted as the final report. F accepts that signal only at its scheduled completion boundary; A may signal it whenever justified. The terminal request contains no investigation tools and returns the common six-field report directly. Claim status and recommendation remain free text; no product action enum or exhaustive change taxonomy is imposed.

LM Studio documents client tool calls and returning both the assistant request and tool result in subsequent messages, with native/default template-parser differences. It separately documents schema-constrained terminal output. These are capability candidates, not evidence that either exact local GGUF deployment passes them. [Client tool documentation](https://lmstudio.ai/docs/developer/openai-compat/tools), [structured-output documentation](https://lmstudio.ai/docs/developer/openai-compat/structured-output).

Do not mix native `/api/v1/chat` request fields into the compatible endpoint. The native API documents reasoning settings and total/reasoning statistics, plus server integrations; this does not prove equivalent client-tool reasoning control or accounting on the compatible path. Qualify effective template/tool rendering, exact instance binding, completion reserve, reasoning control and usage before selecting it. All tools execute in our Python dispatcher over the frozen map, without server integrations. [Native request/statistics documentation](https://lmstudio.ai/docs/developer/rest/chat).

If the compatible path cannot satisfy these requirements, preserve its failure and qualify an explicitly named native text-JSON alternative. It uses tool/arguments for investigation, optional notes and a distinct direct terminal report request, with the same observations/history/recovery. Do not silently switch a method mid-trial, strip extra braces or infer unsupported parameters worked. A deployment failing both interfaces remains unqualified; do not rescue it with a hosted model or download.

Model-visible, recoverable errors include malformed action/report shape, unsupported names/arguments and nonexistent retained references. Return a structured error with the failed event ID, field/type issue and allowed contract, without a case answer or semantic grade. Allow at most two explicit format/citation corrections per trial, including at most one terminal-report correction. Each costs a normal inference call, input/output and elapsed time; keep the failed reply. Valid tool requests returning no results or a tool problem consume ordinary steps and remain visible. Recovered completion is labelled separately from first-attempt completion. A correct-looking citation or corrected JSON never establishes meaning.

Identity/accounting drift, unusable transport, irrecoverable truncation, exhausted resources or an indispensable packet that cannot fit stop the trial with their own outcomes. No automatic provider retries. Multiple native requests in a reply are dispatched sequentially and counted individually within the shared operation/byte budget; stop before dispatching an over-budget operation and retain which requests were not executed. Neither arm gets free hidden loops.

### 16.5 Fixed workflow with explicit work products

The source tools remain common. F additionally has deterministic sequencing with actual stage artifacts; A owns its investigative sequence. F's required artifacts record what it examined, candidate source-linked findings, conditions/unknowns and unexamined scope. Their existence proves orchestration; source adjudication separately determines their quality.

| Fixed stage | Maximum scheduled inference calls | Required work product |
|---|---:|---|
| Upstream change interpretation | 3 | Candidate changes with exact references, affected behavior and uncertainty |
| Consumer localization | 3 | Target use or conditional exposure linked to candidate changes; unsuccessful searches retain scope |
| Conditions, environment and CI | 4 | Activation/binding conditions, relevant check paths and decision-critical unknowns |
| Synthesis | 1 | Provisional recommendation connecting prior artifacts and their limits |
| Challenge | 1 | Contradictions/counterevidence and unsupported assumptions; revisions or explicit residual uncertainty |
| Terminal common report | 1 reserved | Report via the separate interface |

Total scheduled maximum is 13 calls, leaving three reserve calls under the 16-call ceiling. Hold one of those three for a possible terminal correction, leaving two flexible calls before reporting. In each retrieval stage, reserve its last scheduled call for a structured stage artifact, with tools disabled; preceding calls may select any relevant frozen source and may request multiple tools. Stage artifacts use a common lightweight schema for free-text findings with citations, conditions/unknowns and unexamined scope, through the qualified structured response path or the labelled direct-JSON alternative. Thus stage labels cannot substitute for preserved findings. Synthesis/challenge consume those artifacts plus the common packed history and recoverable source access; their single calls produce artifacts, not additional retrieval. A fixed artifact does not become accepted evidence merely because the model submitted it.

Early stage completion transfers unused slots to the reserve. To complete early, request the stage artifact on the next call after a tool-free readiness signal; count both calls, and transfer only the genuinely unused slots. Spend flexible reserve first on necessary corrections, then on an incomplete retrieval stage before advancing; allow at most two additional calls to that stage. Do not revisit earlier stages after advancement. A truly empty stage may be skipped only with a logged structural reason from the common case inventory; absence of a known expected issue is not a skip reason. Missing/malformed artifacts consume recovery or remain explicit incomplete work; never synthesize a substitute from reviewer knowledge. F may still produce an honest partial report, which remains in assigned denominators.

Both arms start from the same neutral update identities, proposed changed-path/declaration-diff packet and source inventory, derived generically from frozen base/head data with explicit omissions. Stage-specific instructions may refer to those source identities but may not supply historical conclusions or case-selected consumer paths. Freeze packet construction and artifact schemas before output. F's seven nominal retrieval responses and possible batching may be insufficient for some tasks: development must assess that limitation and revise shared budgets/routing under a new configuration if needed, rather than proclaim a weak F the strongest baseline.

### 16.6 Resource configuration and discriminating proof

Keep 16 calls, 48 tool operations, 8 MiB returned-observation bytes, 20 minutes and serial trials. Use a qualified 16,384-token deployment context, 1024 ordinary output reserve and 4096 terminal-report reserve. Replace cumulative input/output limits with 245,760 input and 32,768 generated tokens, including reported reasoning and all repairs. The input ceiling is 16 × (16,384 − 1024); request-level fit still applies, and report input can be at most 12,288 rendered tokens. Before further investigation, both arms reserve two calls and 8192 output tokens for the initial report and its possible correction. A therefore has at most fourteen investigative calls, with any earlier corrections included. A valid initial report releases the correction reserve without another call. If remaining input/time cannot support reporting, finalize early or retain the exact resource failure; reservations do not override actual accounting. The two-model 200-trial hypothetical caps in section 9 are arithmetic upper bounds only.

Reason: retaining ordinary history and providing tools should not be defeated by an inherited 3072-token average input allowance or a small final-report reserve. These are available ceilings, not consumption goals. Report actual costs; a completed result at higher cost cannot be called a version-0.1 efficiency improvement. The redesign is a combined configuration change. F/A within that configuration share all common mechanics and ceilings. Reasoning-off remains the continuity setting only if independently observed on the selected interface; unknown reasoning/accounting is a failed qualification, not assumed zero. A reasoning-enabled pair needs its own completion-fit/accounting qualification and predeclared limits, and remains separate from the control comparison.

Implementation proof must discriminate the actual pilot failures: empty notes with retained prior evidence; scoped zero-hit searches; paged CI continuation; preserved tool-call/result linkage; forced history packing and event recovery; no cross-trial state/reference leakage; stage artifact propagation and incomplete-stage handling; malformed action followed by visible correction; invalid final report followed by one correction; exhausted correction/call/input/output/operation/byte/time budgets; terminal reserve; provider identity/usage/truncation; identical common tool access and arbitrary provisional advice. Reuse the 39 focused checks as a historical baseline, adapting prototype-specific expectations deliberately. Run new focused proof and nearest composition tests before live qualification; passing them establishes mechanics only.

Qualification sequence, once implementation/runs are selected:

1. Controlled-provider mechanics and measured packet-fit checks, including tools, full/packed history and the terminal schema.
2. At most twelve harmless probe calls per model for preferred-interface qualification: two fresh multi-step source-follow-up/report sequences of at most six calls each. Include multiple source scopes, a zero-hit search and a report citation. Test malformed/omitted-reference recovery under controlled proof; preserve any naturally occurring live errors. Require both sequences to complete with bounded usage, verified identity and valid references. This is a readiness criterion, not a reliability estimate.
3. If needed, a separately selected named alternative-interface qualification with the same bound; no automatic second batch after failure.
4. Two known-case diagnostic trials per policy/model at most once (eight assigned trials with two models), balanced arm order, unchanged frozen case sources and fresh state. Inspect every final/partial outcome against source obligations. Passing format alone cannot advance to protected comparison; F must actually perform its stages and reviewers must find a usable investigative path.
5. Only after readiness/source review, re-enter six-case development and independent protected-reference preparation. Diagnostic ablations and reasoning changes receive separate identities and costs. Preserve all prior outcomes; no best-run selection.

The design is complete when ownership, wire-interface qualification, history packing, recovery, F routing and resource/proof rules are internally consistent and executable as a bounded implementation brief. Its stop line is before executable mutation, model loading or inference unless that next responsibility is separately selected. Product architecture, semantic acceptance, protected comparison and learner mastery remain distinct decisions/evidence.

### 16.7 Implementation and model-selection clarification

The selected v0.2 diagnostic implementation uses the same frozen two-case corpus, a 6000-character budget for whole generic base/head text diffs with omission records, five F artifacts using summary/claims/conditions/unexamined, and common trial event pairs. The labelled native alternative supplies those schemas as prompt contracts with visible validation/recovery; compatible requests use client tools and `response_format`. Rendered SDK counts include history/tools plus a 128-token allowance; actual server usage must stay within that measured upper estimate. This is qualified fit/accounting evidence, not a claim of byte-identical server templates. F does not silently skip stages or revisit completed stages. Flexible corrections are bounded by two trial-wide corrections; the nominal seven retrieval slots require adequacy review.

On 2026-10-06 Ali added the already local `mimo-v2.6-distill-qwen-9b` as a third diagnostic candidate alongside Gemma E4B and Qwen3.5 9B. The selected maximum is now twelve known-case diagnostic trials (two cases x two policies x three models), once per qualified deployment. Both wire candidates are explicitly selected in advance: preferred qualification first, and a separately identified native-json qualification only after retaining preferred failure. Each candidate remains <=12 probe calls/model; unqualified candidates do not enter case trials. The working-memory record owns the procedural adaptation rationale and actual receipts. These changes do not select the protected/full comparison or imply a reliability estimate.

### 16.8 Separately identified server-default reasoning diagnostic profile

Fresh compatible-wire receipts report total completion and reasoning token counts. Gemma and Qwen produced positive reasoning counts under the server default; the compatible path still has no established native-style off toggle. Thus those receipts do not qualify the reasoning-off continuity baseline. MiMo's first compatible receipt reports zero reasoning, without establishing a controllable setting.

Select a separate **compatible-tools / server-default-accounted** diagnostic profile for the same three local deployments and unchanged two-case sources. The provider sends no undocumented reasoning flag. Every response must report valid total/reasoning usage and exact instance identity; generated-token ceilings include reasoning. Keep section 16.6's 16 calls, 1024 ordinary output, 4096 terminal output, 32768 generated, 245760 cumulative input, 48 operations, 8 MiB observations, 1200 seconds and qualified 16384 context. Irrecoverable truncation still fails. This is measured server-default behavior, not a promised reasoning-on toggle. Both arms use the same profile within each model; no comparison to earlier reasoning-off/native results can isolate agency or memory.

Earlier preferred attempts used one actual inference call/model after the schema repair, then exposed the SDK's distinct tool-history input wrapper. After repairing that wrapper and preserving neutral intervening stage turns, allow at most eleven remaining preferred qualification calls/model across two fresh sequences, each at most six calls. This keeps total preferred qualification within the predeclared twelve-call bound, including failed implementation attempts. Previously failed native qualification is retained and is not rerun. Up to twelve known-case diagnostic trials remain selected only for deployments passing both fresh sequences. A failure remains a result; no protected batch or product promotion is selected.

### 16.9 MiMo diagnostic exception after instruction-following qualification failure

MiMo's first fresh preferred sequence produced a valid source-linked report with accounted usage and working multi-scope tools/follow-up, but omitted the exact requested zero-hit query. Both-sequence qualification therefore remains **failed**, and its second sequence is withheld. The ordinary readiness route in 16.7/16.8 would withhold all four cases.

Ali explicitly selected this model for testing. Under the Smart Situational Override, execute its four already-selected known-case assignments once as **unqualified diagnostic trials**. The canary failure concerns following the requested investigation, rather than an unresolved transport, identity, accounting or capacity boundary; observing case behavior can help diagnose that failure without admitting readiness. Preserve the failed probe unchanged. Use the same executable freeze, corpus, model-file identity, load configuration, server-default-accounted profile, per-trial budgets, arm order and fresh-state rules. A private driver records this exception and its own hash before execution; it invokes the existing trial owner without changing the ordinary qualification gate. No additional canary, prompt repair, best-run selection or broader batch is selected.

Include these outcomes and costs in all twelve assigned case denominators, explicitly distinguish them from the eight qualified Gemma/Qwen assignments, and inspect every final/partial candidate against source. A complete MiMo report cannot retroactively pass qualification. This exception establishes diagnostic evidence only; readiness, protected comparison, causal agency claims and product authority remain unestablished.

## 17. Larger-local-model diagnostic comparison before interface redesign

Ali selected this comparison on 2026-10-06 after the complete twelve-case repair review. Test the already-local **Gemma 4 12B Instruct Q4_K_M** (`google/gemma-4-12b`) and **Qwen3.6 35B-A3B UD IQ2_M** (`qwen3.6-35b-a3b-ud`). These are deployment comparisons, not isolated parameter-count experiments: architecture/training/quantization/template and load placement differ. No download, hosted model, third-party execution, protected batch or product adoption is selected.

Reuse the exact two known-case corpus maps, task text, generic packet, tool/report schemas, fixed stages, packing, visible corrections, case order and fresh state. Preserve 16384 context, temperature 0.2, 16 calls, 245760 input/32768 generated tokens, 1024 ordinary/4096 report reserve, 48 operations and 8 MiB observations. Retain compatible client tools with server-default-accounted reasoning. Text input only; hash the main GGUF and any local vision companion separately. Validate deployment path/key/size, echoed load configuration, measured fit and actual usage before claiming a working comparison.

Speed is a measured operating cost, not the initial research acceptance criterion. Select **1800 seconds maximum per HTTP response**, **5400 seconds per fresh canary sequence** and **14400 seconds per case trial**. The trial's remaining time still bounds each response; there are no hidden retries. Configuration is explicit and recorded by the existing provider/pilot owners; older defaults remain 60/180/1200 seconds. No source-navigation/reference/stage redesign enters this configuration. A token truncation remains a capacity result; preserve it before selecting any separately labelled token-reserve repair, rather than silently changing budgets during a trial.

Load serial owned instances with conservative partial GPU placement (initial ratios Gemma 0.55 / Qwen 0.45), strict VRAM cap, flash attention and GPU KV cache. Host memory/load feasibility is runtime evidence, not file-size inference. The earlier full-GPU configuration is not an efficiency control. Never unload another workstream's instance; idle-GPU availability is rechecked before each load, and unload only owned instances on closure.

Run at most twelve preferred canary calls/model, two fresh sequences up to six each. Keep every failed/rejected outcome. After qualification, execute the four known-case assignments/model once in F/A then A/F order. If a canary fails only the requested investigation/reference criterion while tools, source delivery, accounting, identity and capacity remain established, the same preselected diagnostic exception as section 16.9 permits four explicitly unqualified case assignments; it never retroactively passes qualification. An unusable tool/report path or unresolved transport/accounting/identity/capacity failure withholds case execution and becomes diagnostic evidence.

Inspect every final/partial candidate against the same source obligations, including mechanically rejected candidates. Compare release/version attribution, indirect consumer paths, exact citation support, CI activation/installation, stale claims, stopping and useful clues. Preserve costs and proof limits separately from the existing three-model batch. The question is whether these local deployments improve the investigation under the existing interface; no model winner, reliable delegated authority or causal size/agency conclusion follows from two known cases. Interface redesign and broader independent-case evaluation remain later responsibilities.

### 17.1 Explicitly selected larger output-capacity profile

Ali stopped the first larger-deployment run after three Gemma cases reached the 1024-token ordinary/stage ceiling and explicitly requested increasing the limits. Preserve those three saved outcomes, the interrupted fourth assignment and all receipts. The interrupted request has unknown response usage; Qwen's four assignments were not started. This overrides finishing the original eight assignments: continuing the demonstrated inadequate capacity profile would spend time without establishing the intended model comparison. The user's stop and repair instruction controls sequencing; the working-memory record preserves the interruption and reconciliation.

Select a separate **larger-local-v2-capacity** profile: **8192 ordinary/stage output**, **8192 final-report output**, **131072 total generated tokens per trial**, **524288 cumulative input tokens**, and **32768 loaded context**. Generated counts include reasoning. The total output allowance covers sixteen full 8192-token responses, including corrections. Both final-report calls remain reserved. Keep sixteen calls, two corrections (at most one terminal), 48 operations, 8 MiB observations, temperature 0.2, server-default-accounted reasoning, compatible tools, sources, tasks, schema validation, stage order, packet/history and stopping mechanics unchanged. The larger output reserve has sufficient per-request input space in the selected 32K context; the host still measures actual fit and preserves necessary history packing. No setting promises semantic correctness.

The existing `TrialLimits` object is the single resource-profile owner, passed through pilot execution into both case arms and fresh canaries. Canaries override only their selected sequence time and <=6-call limit, now also honoring the total qualification call allowance. CLI resource flags expose this object; earlier defaults remain available for historical-profile reproduction, but they are not used for the selected larger runs. Invalid profiles fail before model access. Retain 1800-second response, 5400-second canary and 14400-second trial ceilings and initially the same partial GPU ratios; actual 32K load feasibility is new proof, not presumed from the 16K run.

Before the new batch, perform **one explicitly labelled saved-packet capacity contrast** using the first truncated Gemma HTTPX F stage-correction request. Preserve its model-visible system/user/history/schema exactly; change only the selected output reserve, owned instance binding and context/load profile. Account its usage and truncation, and inspect any returned candidate against source. This is diagnostic replay of a known request, not an independent trial, semantic acceptance or repaired historical result. No hidden retry or reference answer is added.

Then execute two fresh canaries per model, <=12 calls/model under the new profile, followed by the eight already-selected case assignments once when eligible, including the preselected unqualified diagnostic exception only for completed investigation-criterion failures. Preserve every failure/withheld assignment separately. At most 153 new inference attempts are selected: one contrast, 24 canary calls and 128 case calls. Do not mix the interrupted 1024-token profile with this profile as if they were repeated equivalent trials or isolate size/agency from their difference. Further actual truncation remains a result requiring a new recorded decision, rather than automatic repeated budget escalation.
