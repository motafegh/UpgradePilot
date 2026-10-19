# Investigator responsibility decomposition and evidence-to-decision product direction

**Created:** October 19, 2026. **Final revision:** October 20, 2026.

**Status:** Finalized direction accepted by Ali on October 20 for the bounded investigation/planning gate. This remains a non-controlling rationale; no implementation architecture, model topology or product method is admitted by it.

**Decision owner:** Ali Rajabi.

**Scope:** Reconcile experiment evidence with accepted product responsibilities; propose a bounded product-value and feasibility decision before further implementation or inference.

**Live position:** [MEMORY.md](../MEMORY.md) alone owns selected continuation. The [investigation plan](../plans/PRODUCT_VALUE_AND_TRANSPARENT_BASELINE_FEASIBILITY_INVESTIGATION_PLAN.md) coordinates the bounded gate; acceptance of the direction and plan writing does not execute it.

## 1. Recommended decision

Keep UpgradePilot's accepted hybrid evidence and decision architecture. Stop treating repeated tuning on the same exposed Investigator fixtures as the default route to progress. Before building another interpretation subsystem, establish what the current automated product can contribute beyond the transparent baseline and identify one useful downstream responsibility worth improving.

The immediate recommendation is **one bounded planning/feasibility gate**, with product comparison readiness first. It can select a small deterministic improvement, a source-relation baseline, a discriminating interpretation diagnostic, or no further investment in a candidate. It does not commit the project to a parser, proposition framework, validator model, multi-agent system or seven-stage programme.

The proposed priorities are:

1. Check whether a fair automated-product versus transparent-baseline comparison can be run from retained inputs. Specify its consumer, comparison dimensions, costs and missing prerequisites before execution.
2. Identify the earliest sufficient owner of one material product gap. Prefer existing deterministic facts and narrow derivations where they suffice.
3. If source relations remain the best next investment, design a small general source-fact/relation capability with explicit capture, binding, uncertainty and consumer contracts.
4. Consider additional semantic roles, deployments or autonomous discovery only when a named residual uncertainty makes that experiment worth its cost.

Useful interpretation, evidence evaluation and action permission remain distinct responsibilities. This is already accepted architecture; the proposal addresses missing capability within it. Whether decomposing model tasks improves performance remains an empirical question.

## 2. What is established, and what remains hypothetical

The recent experiments bought important negative evidence: the tested methods did not produce adequate complete advice on the exposed cases despite substantial control, acquisition and review work. They also earned reusable run-control, accounting, provenance and source-delivery mechanisms. Neither fact establishes that another layer is useful.

| Evidence | Observed result | Limit on interpretation |
| --- | --- | --- |
| Broader Fixed/Agent research at `cde0ea9906fa37e4184962d0ba65577e4d62396e` | Eight mechanically complete reports; zero advice-ready in the recorded known-case source review. Agent used less input and elapsed time in all four paired assignments and acquired relevant consumer source. | Two exposed cases, single samples, different policy/stage overhead; no general ranking, causal efficiency claim or product acceptance. |
| Separate broader interpretation-only diagnostic | Two completed calls, zero advice-ready results with supplied evidence. | Different diagnostic and inputs; no pooled controlled treatment estimate. |
| Main supplied-evidence reference, diagnostic-r4 | Five completed predictions: one canary and four cases; all four semantically inadequate. | Four related development fixtures, not four independent product domains. |
| Main instruction-only candidate, diagnostic-r5 | Five completed predictions; all four cases inadequate, with some accurate partial corrections and new/persistent errors. | Single historical/new cohort comparison, exposed cases and AI-assisted, source-aware review. |
| Original 12-assignment Raw/Structured comparison | Three completed assignments, one interrupted assignment, eight unattempted. | Incomplete/inconclusive comparison; no ranking or successful-subset result. It is preserved development evidence, not a suspended batch to finish. |

Main r4 used **66,920 input / 4,373 generated tokens**, **1,028.439 prediction seconds** and **180 operation units**. Main r5 used **67,590 / 5,833 tokens**, **1,262.634 prediction seconds** and **180 units**, with zero unknown usage in either completed cohort. The candidate generated 33.39% more tokens and took 22.77% more prediction time. These are descriptive costs, not estimates of a general method effect.

The broader comparison recorded **135 known provider attempts** including qualification, **1,085,940 input / 85,327 generated tokens** and **11,803.070 summed trial seconds**. It is a separate lineage; do not add its denominators to main's outcomes or silently exclude qualification, interruptions or unknown costs. The separate broader interpretation diagnostic used 39,357 input / 12,126 generated tokens.

The main candidate's only intentional model-facing method change was `task.goal`; fresh reference identities and measured timing fields also differed honestly. Its smaller source-pair requests were about 8k input tokens. They show that failure was not restricted to the largest packets; they are not minimal-context controls that eliminate context pressure, protocol, deployment, task composition or stochastic effects.

The older Fixed method already separated upstream, consumer/applicability, CI/environment and challenge stages. Its failures are counterevidence to assuming additional stages alone will solve the problem. They do not disprove every possible bounded validator or role decomposition.

**Working hypotheses:** some relations may be cheaper and more dependable to derive mechanically; task decomposition may improve attention or verification; a narrower context may help; model/deployment quality may still be limiting. None has been isolated as the general cause or cure.

**Rejected inference:** these results do not prove that one model cannot perform discovery, extraction, interpretation and review. Nor do they show that model quality is no longer a risk. Product authority separation is justified independently of that empirical question.

## 3. Accepted architecture versus implemented capability

The [Charter](../PROJECT_CHARTER.md), [Core specification](../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md), [Product Decision Model](../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md), [Maintainer Action Synthesis specification](../docs/specifications/UPGRADEPILOT_MAINTAINER_ACTION_SYNTHESIS_SPECIFICATION.md) and [ADR-0012](../docs/architecture/ADR-0012-canonical-investigation-workspace-and-recovery-boundary.md) control their respective responsibilities. This proposal does not replace them.

| Responsibility | Existing implementation | Gap relevant to this proposal |
| --- | --- | --- |
| Exact observations and native assessments | Product acquisition/investigation and canonical Workspace retain scoped evidence and native results. | Coverage and correctness remain mechanism-specific; missing or uncorrelated evidence cannot be promoted. |
| Proposition state and applicability | [impact/applicability.py](../src/upgradepilot/impact/applicability.py) defines `PropositionState`: established, refuted, unresolved, conflicted; `PropositionAssessment` also preserves coverage and owner. | This is bounded applicability composition, not a generic semantic evaluator. |
| Attributed proposals, citations and lifecycle evaluation records | [lifecycle_records.py](../src/upgradepilot/workspace/lifecycle_records.py) already owns these records. | Record availability does not establish semantic truth or adequacy. |
| Model-proposed semantic evaluation | [WorkspaceHost.evaluate_proposal](../src/upgradepilot/workspace/lifecycle_host.py) records unsupported when no semantic/conflict/adequacy evaluator is admitted; the experiment adapter uses this boundary. | An admitted domain-level evaluation method remains missing. |
| Maintainer-action synthesis | [maintainer_action.py](../src/upgradepilot/maintainer_action.py) admits explained `abstain` only. | No non-abstention permission is currently implemented there. |
| Product consumer | [report_projection.py](../src/upgradepilot/report_projection.py) consumes synthesis and projects findings/uncertainty into reports. | Incremental maintainer usefulness and additional action permissions require proof. |

Therefore “there is no product consumer” is too broad. Reports already consume product state. The material concern is building a new abstraction without a justified consumer requirement, or mistaking report detail for useful support.

Likewise, the product has not granted an experimental LLM unilateral action authority. Missing interpretation capability and missing admitted evaluation are separate from already enforced trust guards.

Start representation design from `PropositionState`, `PropositionAssessment` and existing evidence owners. Reuse their semantics where applicable; justify any adaptation at the actual owner. Do not create a second truth-state enumeration or silently broaden applicability into a generic rule engine. Lifecycle `EvaluationOutcome` values (`evaluated`, `unsupported`, `failed`, `stale`) describe processing disposition, not the four proposition truth states.

## 4. Product value must be tested before a long interpretation programme

The Charter's thesis concerns better supported, more useful decisions from richer evidence compared with a transparent baseline. The [simulation baseline v0.1](../product-simulation/TRANSPARENT_BASELINE_SPECIFICATION.md) uses version category, current CI conclusion, dependency directness and literal release-note keyword signals. Preserve its exact rule order and input restrictions. Its coarse action names are comparator outputs, not permissions automatically available to the current product.

Historical simulations compare full investigations with that baseline. There are also post-implementation transfer evaluations and real product-path proofs. Neither substitutes for a declared automated end-to-end product-versus-baseline evaluation. The inspected records do not establish the proposed complete six-case benchmark; do not describe all previous product evaluation as nonexistent.

### 4.1 Comparison-readiness check comes first

Use exposed S001–S006 as **candidate development material**, not a newly protected validation set. Check eligibility against the admitted Python Dependabot/product mechanism boundary; historical scenario inclusion does not automatically establish runtime support or authorize a new simulation. Inspect each case rather than assuming uniform frozen replayability:

- identify exact PR/head/dependency/environment identities and the case's admitted question;
- inventory retained machine inputs, source bytes, timestamps and provenance, including missing historical CI or external artifacts;
- locate the normal product producer/entry path that can consume them;
- determine whether any adapter merely translates retained observations or injects a human-derived conclusion the product is supposed to establish;
- recover the four baseline inputs and their provenance without exposing rich evidence to the restricted comparator;
- name the product capability and output that can fairly be evaluated, and explicitly mark unsupported or unavailable cases.

S006 [documents](../product-simulation/scenarios/S006-qldebugger-pydantic-validator-coverage-gap/README.md) that it does not reproduce the full earlier manual artifact bundle. Its [synthesis](../product-simulation/S006_POST_CASE_SYNTHESIS.md) also preserves an oracle-exposure limitation. These are concrete reasons why “six frozen cases, already implementable” requires qualification.

A deterministic offline comparison **can be CPU-only and require zero model calls** if the needed retained inputs and product route exist. Live acquisition may require network access; missing adapters, missing sources, unsupported mechanisms and execution permissions are separate costs. Do not promise a turnkey CPU replay before this inventory. No target test or reproduction runs merely because the comparison has no LLM.

### 4.2 Design the fair comparison before running it

Predeclare:

1. Product source revision, comparator version, selected cases and exclusions, exact input identities and a common information-time boundary.
2. Separate restricted baseline inputs from richer product inputs, as intended by the thesis; neither arm may receive hidden oracle conclusions. Disclose unequal acquisition and preparation costs.
3. Normal product path versus controlled replay, adapter behavior and any manual preparation. They support different claims.
4. Case-specific source-backed obligations and review rules fixed before viewing new outputs. Historical expected decisions are evidence to inspect, not unquestionable ground truth.
5. Full denominator: completed, unsupported, unavailable, operationally failed and semantically inadequate cases. Publish readiness for all six candidates even if only a subset is runnable; never present that subset as six-case product coverage.
6. Resource ceilings, reviewer independence/assistance, exposure, uncertainty and stopping consequences.

Use the existing baseline comparison dimensions: action, reasoning, uncertainty, targeted action, evidence authority, failure behavior, cost and user value. An abstain-only product cannot demonstrate superiority in actionable recommendation merely by avoiding all positive recommendations. It can demonstrate narrower, source-supported uncertainty or a useful finding; measure and label that narrower outcome separately.

Retain a baseline-sufficient/no-added-value control, supported positive findings, misleading favorable CI, and missing/contradictory evidence where represented. More prose, more citations or more conservative labels do not score as value by themselves. Compare preservation of useful supported conclusions and rejection of unsupported ones. At this development stage, source-aware review can establish traceability; it cannot substitute for independent maintainer usefulness or protected qualification.

### 4.3 Decision consequences

- **Ready:** propose a finite CPU-only offline comparison in the next authorized plan, with a fixed cohort and cost ceiling. Run it before investing in a general new interpretation subsystem when it can discriminate the investment decision.
- **Partly ready:** report the full readiness denominator and limitations; select a justified subset only if its narrower question is useful. Decide whether missing input/adapter work is worth doing.
- **Not ready:** produce the exact prerequisite/gap and its cost. Do not start a benchmark framework or manually fill semantics until the case “works.”
- **Baseline sufficient / product adds no material value:** preserve that finding; redirect, narrow or stop the proposed capability rather than expand the architecture.
- **Useful product difference:** identify the producer/consumer responsible and test the cheapest improvement there. It does not establish overall product superiority or authorize all later stages.

## 5. Require a concrete consumer; qualify any new action separately

Every proposed new capability must name a downstream product question, existing integration owner and observable benefit before implementation. Prefer one thin end-to-end development result over a generic proposition framework with hypothetical consumers.

A useful development example is a conditional source finding: a captured older caller passes `app`, a captured newer callee does not declare it and has no applicable keyword acceptance, while the newer captured caller omits it. If caller/callee correspondence is established and the input scope is adequate, this can explain a specific compatibility concern. If dispatch or actual installed version is unresolved, preserve that condition and identify the discriminating missing evidence. This example is not an admission of automated PR-to-call binding or global runtime incompatibility.

A first non-abstain action is a serious product option, not a fixture requirement. `run targeted checks` is attractive only if its accepted positive permission can be established from normal producers:

- one or a small stable set of exact decision-critical unresolved propositions;
- concrete bounded maintainer-performable checks that discriminate those propositions;
- plausible outcomes and explicit interpretation/stopping logic;
- no justified UpgradePilot-executable investigation that should do the work first;
- no concern requiring broader adaptive inquiry;
- no independently established block condition.

A useful check alone is insufficient. Do not invent source metadata downstream, outsource work the product can justifiably perform, or weaken permission to make a non-abstain result reachable. Existing facts may support a narrow synthesis derivation without a new generic “check producer”; trace that possibility first.

The first design must decide whether the reachable consumer is an informative report finding, an existing investigation transition or a separately planned positive action. If no permission is established, retain explained abstention. Do not count that alone as achieving the non-abstention product goal. Adding a new action requires its own owner changes, producer-to-synthesis-to-report proof and authorization before Build.

## 6. Candidate deterministic source-fact/relation baseline

This is a candidate to earn selection at the first gate, not the predetermined implementation.

### 6.1 Responsibility and non-goals

Derive mechanically justified facts from captured Python source, with exact provenance and supported grammar. Reuse existing parsers/facts where sufficient. Python's standard `ast` is a plausible dependency-free baseline; do not choose a new parser dependency without a concrete need. No full static analyzer, universal import resolver, knowledge graph or semantic migration oracle is proposed.

The contract must distinguish:

- syntactic observations, such as a declared parameter or explicit keyword at a call site;
- conditional relations given a stated caller/callee binding premise;
- an established binding justified by an admitted producer;
- execution/applicability conclusions requiring environment, installation or runtime evidence.

### 6.2 Input and binding proof

Specify the actual capture form supplied by the normal producer: full file or fragment, exact revision/blob, encoding, line mapping and completeness. A fragment must not silently become a complete module or complete function. Record parse failure and incomplete capture explicitly.

Identify who establishes caller/callee correspondence. Human-selected paired snippets may be a valid interpretation diagnostic, but they do not prove automated discovery or binding. `super()` alone does not establish the effective callee under arbitrary MRO, monkey-patching, decorators or dynamic dispatch. Preserve an unproved correspondence as a premise; do not report its consequence as unconditional fact.

### 6.3 Grammar and output obligations

Before Build, enumerate admitted constructs and honest non-results. Relevant distinctions include positional-only, positional-or-keyword and keyword-only parameters, defaults, receivers/bound methods, `*args`, `**kwargs`, literal versus unknown argument expansion, aliases, wrappers and multiple definitions. A raw parameter-name set difference is not Python call compatibility.

Outputs need source identity/spans, derivation/method identity, observed values, supported scope, correspondence premises, missing evidence and failure/unresolved states. Preserve positive and negative observations only within complete admitted scope; absence from a truncated excerpt is not absence from the function or program.

Fixture-specific package names, symbol paths or expected answers cannot define the algorithm. Under [Minimum Useful Generality](../docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md), vary irrelevant names/layout, include supported and counterexample constructs, exercise real producer inputs and show honest unsupported cases. A disposable experiment may have a narrow grammar; its generality claim must match that grammar and responsibility.

### 6.4 Expected benefit and residual failures

The demonstrated HTTPX signature/forwarding error is a credible target. Correct extraction could remove that mechanical burden. It does not by itself repair citation entailment, native CI-state promotion, applicability completeness, recommendation calibration or synthesis.

The glyphsLib packet already contained native typed uncertainty that the model overstated. Its repair may belong at a narrower interpretation/evaluation boundary; adding another source extractor is not automatically relevant. Preserve that alternative at the first decision gate.

Reject or narrow the baseline if source/binding inputs are unavailable, it needs fixture answers, duplicates an existing owner, cannot preserve unknowns, exceeds cost, or produces no useful consumer difference. Consulting original source for audit or independent checks is legitimate; needing a competing downstream extractor to recover essential lost semantics is a design failure.

## 7. Validation must discriminate truth and preserve useful information

Start with the earliest sufficient deterministic owner. Native assessed facts do not require a generic model revalidation ritual. Exact source-bound derivations, explicit assumptions, invariants and focused counterexamples can support mechanical facts without another model call.

“By construction” must mean a stated derivation whose premises and source mapping are checkable. Running the same extraction algorithm twice is not independent validation; a shared bug can agree with itself. Use independently specified expectations, source inspection and discriminating cases appropriate to the claim. Rechecking a source span is useful where it detects misattribution; it need not become a second competing parser.

For irreducibly semantic propositions, the next design must identify the evaluator, admissible evidence/counterevidence, evidence-coverage semantics, unsupported behavior and exact authority of its result. Existing lifecycle records do not supply the missing semantics by themselves.

If a model validator is later studied, give it the proposition it must evaluate and relevant evidence. Blind it, where feasible, to proposer identity, confidence, preferred verdict, persuasive rationale and prior appraisal. A validator cannot be blind to the proposition itself while evaluating it. Record any information it must receive that limits independence.

Measure false acceptance, false rejection, appropriate unresolved/conflicted handling, retained supported findings, coverage and cost against a source-backed adjudicated reference. Agreement/contradiction rates are descriptive diagnostics, not truth. Same-model or different-model agreement does not become independent evidential corroboration merely by using another call. An always-reject, always-unresolved or generic-abstain policy must not win.

The existing comparison reviews are AI-assisted and source-aware. Reviewer/implementer overlap limits independent corroboration. Do not confuse that limitation with proof that the deployed model acted as its own runtime validator. A future reviewer plan should separate implementation, rubric freezing and adjudication where feasible, and disclose overlap where not.

For review, an `asserted` or `inferred` recommendation with zero supporting recommendation evidence is semantically inadequate. Nonempty citations still require actual support for each material premise; source identity alone is not entailment. Preserve this distinction without silently changing a frozen experiment schema or regrading its original outcomes.

An experiment's offline reviewer remains its evaluator. Passing that review does **not** establish an admitted product Validation owner. Before recommendation/product adoption, separately design and qualify the required evaluation boundary and action permissions. No report schema, nonempty citation list or accurate worksheet can replace that proof.

## 8. First bounded decision gate and cost contract

The accepted gate is coordinated by **one bounded investigation plan**, rather than expanding the old experiment plan or opening a family of framework plans. Its output is a defensible next-investment decision.

**Proposed ceiling for that future planning gate:** one coherent cycle, at most six active engineering hours: up to two for comparison-input readiness, two for producer/consumer and representation tracing, two for alternatives and the decision packet. These are proposed ceilings, not retrospective measurements of this proposal revision. Record actual effort honestly; reaching the ceiling returns an incomplete/inconclusive design with a named gap, not an automatic extension.

**Resource boundary:** zero model predictions, zero GPU/model loading, zero target code/check execution and no new acquisition campaign in this design gate. Use retained evidence and local source. An unavailable item remains unavailable. Any later CPU evaluation, acquisition, build or inference requires its own finite scope and authorization; “CPU-only” does not waive those responsibilities.

The plan must settle, before Build:

| Required decision | Minimum answer |
| --- | --- |
| Product question and value | Exact supported maintainer question, normal consumer and observable improvement over the simple comparator. |
| Comparison readiness | Per-case input/producer/oracle/exposure inventory; runnable denominator, missing prerequisites and fair metrics. |
| Alternatives | Existing deterministic owner repair; bounded source relation; useful action-permission work if premises exist; discriminating semantic diagnostic; stop/defer. Compare likely information/value and cost without pretending an unmeasured estimate is fact. |
| Representation | Reuse current proposition/applicability/lifecycle owners where semantics fit; name the missing responsibility rather than invent generic types. |
| Code home | Decide experiment versus product responsibility, integration seam, adoption/disposal path and applicable tests. Do not defer this decision into Build. |
| Proof and boundaries | Supported input/capture/grammar/binding, negative controls, unknowns, actual producer path, consumer evidence and authority limits. |
| Future resource contract | Fixed engineering effort, calls including qualification, tokens, operations, monotonic time, retention and unknown-usage policy, as applicable to the selected action. No unspecified tuning allowance. |
| Consequences | Select one justified increment; narrow with explicit product exclusions; reject/stop; or remain inconclusive with the exact missing premise. No automatic follow-on programme. |

The recommended default for an unqualified parser feasibility probe is disposable `experiments/` work using product APIs. If the selected responsibility is an already admitted product derivation, implementation may belong in `src/upgradepilot/` with product tests. The plan must justify the choice. Directory placement does not prove capability or adoption. Product runtime must never import experiments/tests/tools; no permanent parallel truth path is authorized.

A narrow slice must name excluded product capabilities, why they are deferred rather than conveniently ignored, and what evidence permits re-entry. A helpful source fact is a step toward the product responsibility, not a substitute for the full maintainer decision.

## 9. Conditional later decisions, not a committed sequence

Only the first gate is recommended for selection. The following branches describe possible consequences:

- If comparison is ready and informative, run a finite authorized offline development comparison and use its gaps to select work.
- If a deterministic derivation is the cheapest valuable increment, implement and verify that bounded responsibility before a new model method.
- If semantically interpreting native state remains decisive, design the smallest control that distinguishes the proposed mechanism. Any model change or extra role needs an explicit hypothesis and full cost ceiling.
- If a prompt/envelope method becomes promising, isolate instruction changes from representation changes before claiming a mechanism. Do not automatically add an isolation arm to a frozen run.
- If a role-based method earns a test, a role need not mean a new agent, process, framework or model. Compare with the simpler deterministic and single-pass alternatives, preserving useful findings as well as safety.
- Autonomous discovery may be reconsidered when a useful downstream interpretation/evaluation/consumer path exists and acquisition is the remaining bottleneck. Earlier navigation/cost failures still need their own proof; interpreter success cannot qualify discovery.

Before protected qualification: freeze the complete method, input policy, prompts/schema, deployment/settings, evaluator/rubric and relevant consumer contract. Select new unexposed material with disclosed reviewer exposure. Do not tune between selecting and running it. Any material method change resets qualification: develop the changed method openly and qualify it on fresh protected material. Changing only a label cannot restore a leaked holdout.

Protected success is separate from independent usefulness, runtime validation, action permission and adoption. Failure, resource truncation or unavailable evidence must retain their declared semantic/operational/inconclusive classifications. A failed gate must not become an open-ended repair loop.

### 9.1 Working state and context, if another semantic method is selected

Canonical evidence remains in its existing owner. A model working set is a scoped projection with exact source identities, relevant native assessments, stated hypotheses, counterevidence, unknowns and remaining budget. It must preserve enough context to interpret source scope and uncertainty while avoiding repeated whole-trace accumulation. A summary cannot gain authority above its sources or erase a contradiction. Stateful transport, response chaining or another session is a transport choice, not durable product memory or proof that the model retained the right evidence. No new memory framework is selected.

### 9.2 Risks that can stop the direction

| Risk | Required response |
| --- | --- |
| Architecture grows before value is measured | First gate requires consumer, simple comparator, effort ceiling and a reject/no-value outcome. |
| Narrow parser becomes a fixture oracle or static-analysis project | Explicit grammar, producer/binding premises, generality controls, honest unsupported cases and disposal option. |
| Existing typed facts are still misinterpreted | Test calibration and evaluation at the responsible owner; do not assume more extraction fixes it. |
| Validator agrees ceremonially or rejects everything | Source-backed reference, false acceptance/rejection, retained true findings, justified unknowns and disclosed reviewer overlap. |
| Exposed scenarios masquerade as qualification | Preserve development labels, freeze exact methods and use fresh protected material after changes. |
| New action outruns its evidence | Enforce existing positive permission and normal producer-to-consumer proof; no forced action result. |
| Cost/control debt disappears in a new programme | Preserve all lineage costs/unknowns, finite gate budgets and explicit operational/inconclusive outcomes. |

## 10. Experiment disposition, maintenance and learning debt

Preserve completed r4/r5 outcomes, source reviews, original outputs, costs and unknown attempts without retry, regrading or completion. Closing repetitive tuning means stopping this exposed method line as the default next step, not proving prompt engineering never helps elsewhere.

The original 12-assignment batch has a terminal **incomplete/inconclusive execution disposition**: three completed, one externally interrupted, eight unattempted; 45 semantic attempts, 44 known usage calls and one unknown. Its known semantic usage is 563,812 input / 3,580 generated tokens. The incorrect file-age interruption rationale remains recorded; 1,740.47 measured seconds did not establish an 1,800-second overrun. Existing audit direction already treats the batch as immutable development evidence, not something to resume because eight assignments remain.

Reconcile stale “open at B” live wording to distinguish completed evidence publication/discontinued execution from pending learner D/E. Do not fabricate a complete matrix, erase partial traces, discharge unknown cost, or declare learner mastery. Original frozen artifacts and their retention index remain unchanged. A future run needs a new decision/freeze, not an alleged leftover allowance.

Maintain the existing controls without speculative infrastructure growth. Fix a reproducible integrity defect at its owning boundary when necessary for selected work; more profiles, dashboards, load sweeps or retention machinery require a named evidence need. Keep acquisition, interpretation, evaluation, synthesis and learner ownership proof separate.

## 11. Resolution of the additional review suggestions

| Suggestion | Resolution in this revision |
| --- | --- |
| (a) Put product versus transparent-baseline evaluation first | **Accept priority; qualify readiness and proof.** Add the comparison-readiness gate and an early conditional offline comparison. Do not assert turnkey six-case support, zero prior product evaluation, or overall superiority from a partial/abstain-only result. |
| (b) Add a non-abstain consumer | **Accept the concrete-consumer requirement; condition the action.** Reports already consume product state. A first positive action is a candidate only with existing producer-grounded permission; never force it to validate a framework. |
| (c) Anchor in `PropositionState` | **Accept with semantic scope.** Reuse existing applicability and lifecycle owners; avoid duplicate vocabularies or confusing processing outcome with proposition truth. |
| (d) Deterministic-first validation and blinded semantic review | **Accept with proof qualifications.** Source-bound derivation is useful; self-repetition is not independence. Blind irrelevant proposer/verdict cues, not the proposition/evidence. Measure correctness and retained value, not agreement alone. |
| (e) Close the old comparison | **Accept execution reconciliation; preserve learning debt.** Record incomplete/inconclusive discontinued execution and no resume, while D/E ownership remains pending and artifacts stay immutable. |
| (f) Decide code home before Build | **Accept.** First plan must settle responsibility, seam, evidence class and adoption/disposal, without equating a directory with product qualification. |
| (g) Negative result proves one-model impossibility; only architecture/value risks remain | **Reject that inference.** Keep the observed negative outcomes and authority principle. Overload, model quality, context and decomposition remain unresolved hypotheses; cost and “cheap fixes” need measurement. |

This revision also incorporates the [prior strategic review](../working-memory/2026-10-20_investigator-product-direction-proposal-review_lbd-cycle.md): correct causal overreach; reuse owners; tighten grammar/binding; distinguish CI calibration from source extraction; move value/cost earlier; replace mandatory stages with a discriminating gate; preserve sampling, review and qualification limits.

## 12. Accepted direction and its limited consequence

Ali accepted the bounded direction after the October 20 finalization and subsequently authorized writing its investigation plan. The decision text below records that limited direction; it does not authorize investigation execution, Build or the conditional later methods:

> Retain UpgradePilot's accepted hybrid evidence/authority architecture and current experiment infrastructure. Preserve the completed negative results and discontinue automatic tuning/resumption on the exposed Investigator line. Select one bounded planning/feasibility gate with product-versus-transparent-baseline readiness first, a concrete consumer, reuse of existing state/evidence owners, explicit engineering and resource ceilings, and honest stop/reject/inconclusive outcomes. A deterministic source-relation capability is one candidate, not a predetermined subsystem. Additional positive actions, semantic validators, models, agents, protected evaluations and autonomous discovery each require their own justified scope and proof. Finalizing this proposal does not authorize those actions.

Unresolved decisions belong in that gate: exact runnable cohort, earliest valuable owner, input/binding contract, code home, evaluator method, consumer permission and the cost of the selected increment. The gate may conclude that no new interpretation architecture is warranted.

## 13. References and verification horizon

All implementation statements describe the inspected main source at `e1192f39` before this documentation revision. Historical results are inspected records, not fresh inference or an independent rerun. Prior evidence review inspected the broader research through local Git; the branch is not merged or adopted by this proposal.

Accepted owners and relevant existing product source are linked in §§3–8. Additional evidence:

- [AUDIT-011](../audits/2026-10-18_AUDIT-011_investigator-experiment-validity-and-progress.md).
- [Original 12-assignment disposition](../working-memory/evidence/2026-10-18-investigator-reference-interface-v2/final-results.json) and [analysis](../working-memory/evidence/2026-10-18-investigator-reference-interface-v2/ANALYSIS.md).
- [Supplied-evidence diagnostic](../working-memory/evidence/2026-10-19-investigator-capability-diagnostic/README.md) and [review adjudication](../working-memory/evidence/2026-10-19-investigator-capability-diagnostic/review-adjudication.json).
- [Instruction-only comparison/source audit](../working-memory/evidence/2026-10-19-investigator-evidence-first-build/COMPARISON_REVIEW.md) and [Build evidence](../working-memory/evidence/2026-10-19-investigator-evidence-first-build/README.md).
- [Existing comparison plan](../plans/INVESTIGATOR_EVIDENCE_FIRST_INTERPRETATION_COMPARISON_PLAN.md), retained as its own execution owner rather than rewritten into this strategy.
- [Simulation authority](../product-simulation/AGENTS.md), [simulation navigation](../product-simulation/README.md), [historical D1 synthesis](../product-simulation/D1_FINAL_SYNTHESIS_AND_B1_ENTRY.md) and [bounded implemented-foundation transfer evaluation](../product-simulation/IMPLEMENTED_FOUNDATION_TRANSFER_EVALUATION_2026-08-11.md).
- Broader comparison evidence: Git object `cde0ea9906fa37e4184962d0ba65577e4d62396e:working-memory/evidence/2026-10-07-broader-agency-contract2-comparison/`; interpretation diagnostic inspected through `253b48de20b475eada48810d193bd420c51aa7d4:working-memory/evidence/2026-10-07-broader-agency-evidence-interface/`.

The revision changes a proposal and dated/live-state reconciliation only. It does not establish a runnable six-case benchmark, admit a source extractor/evaluator/action, perform target execution, or select a model topology. The accepted direction authorizes preparation of the linked investigation plan; performing that plan or its recommended next action requires the corresponding selection.
