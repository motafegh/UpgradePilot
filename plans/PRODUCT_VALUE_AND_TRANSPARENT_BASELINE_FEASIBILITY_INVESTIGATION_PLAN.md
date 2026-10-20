# Product value and transparent-baseline feasibility investigation plan

**Artifact:** Prepared bounded investigation plan; acceptance/activation and results belong only in [MEMORY.md](../MEMORY.md).
**Responsibility:** Determine whether retained development cases support a fair automated-product versus transparent-baseline comparison, and recommend one justified next increment or an explicit narrow/stop/inconclusive disposition.
**Direction basis:** [Accepted product-direction proposal](../proposals/2026-10-19_INVESTIGATOR_RESPONSIBILITY_DECOMPOSITION_AND_PRODUCT_DIRECTION_PROPOSAL.md). Preparing this plan does not execute the investigation or authorize Build, inference or target execution.

## 1. Question, deliverable and proof boundary

For a maintainer reviewing a public Python Dependabot update, what useful, source-supported information can the implemented product add beyond the four-input transparent baseline, and which reachable improvement is worth the next engineering investment?

This investigation establishes **comparison readiness and a source-backed investment recommendation**. It does not itself run either comparison arm, measure product superiority, validate a new semantic method or establish independent maintainer usefulness.

On execution, keep detailed progression in one investigation cycle record and place the findings packet at `working-memory/evidence/<execution-date>-product-value-and-transparent-baseline-feasibility/FINDINGS.md`; do not precreate results during plan writing. Deliver that one dated packet containing:

- a lightweight S001–S016 screening matrix and detailed readiness for the smallest discriminating deep cohort, including exclusions, unavailable and uninspected material;
- a proposed fair comparison protocol with exact supported scope and review obligations;
- one concrete producer-to-consumer trace and a before/after benefit hypothesis;
- a comparison of credible next increments, with a preferred option and counterarguments;
- a complete bounded action contract for that option, or the exact missing premise and a narrow/stop/inconclusive disposition.

Do not create a general evaluation framework or a mandatory sequence of later plans. If the findings packet can specify the selected next action completely, it may serve as its reviewable handoff without another document. Even a complete contract requires Ali's explicit review and acceptance before any Build, source/test modification, benchmark execution, model/agent inference, network acquisition, target execution or product-action admission. The contract is not self-authorizing; MEMORY.md records the selected continuation after that decision. Material new product semantics or architecture still require their proper owner before Build.

## 2. Owners, entry and modification boundary

Read the [Charter](../PROJECT_CHARTER.md), accepted [Product Decision Model](../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md), [Core](../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md), [Minimum Useful Generality](../docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md), [Maintainer Action Synthesis](../docs/specifications/UPGRADEPILOT_MAINTAINER_ACTION_SYNTHESIS_SPECIFICATION.md) and [ADR-0012](../docs/architecture/ADR-0012-canonical-investigation-workspace-and-recovery-boundary.md) where their responsibilities matter. Reference their semantics; do not redefine them in this investigation.

At entry, reconcile current Git/source, the accepted proposal, live selection and the preceding dated handoff. Record source revision and inspection horizon. Preserve existing incomplete/negative Investigator outcomes, costs, unknown usage and learner debt; none is an automatic allowance to resume inference.

Read [simulation instructions](../product-simulation/AGENTS.md) before inspecting local cases. The historical cases remain immutable evidence; this plan does not restart simulations or admit a new case.

Related responsibilities remain separate:

| Existing owner | Relationship to this investigation |
| --- | --- |
| [Product direction and maintainer utility plan](PRODUCT_DIRECTION_AND_MAINTAINER_UTILITY_INVESTIGATION_PLAN.md) | Owns the broader action/advisor/hybrid direction comparison; do not reopen it merely to inspect baseline readiness. |
| [Report preservation and usefulness plan](MAINTAINER_REPORT_PRESERVATION_AND_USEFULNESS_EVALUATION_PLAN.md) | Owns report faithfulness/preservation and independent usefulness evaluation. This investigation may reuse its criteria without claiming to perform that study. |
| [Upstream API and target-exposure feasibility plan](UPSTREAM_API_CHANGE_AND_TARGET_EXPOSURE_FEASIBILITY_PLAN.md) | Owns a conditional executable API/exposure trial. Source-relation work remains an alternative here; this plan does not activate that trial. |
| [Historical instruction comparison plan](INVESTIGATOR_EVIDENCE_FIRST_INTERPRETATION_COMPARISON_PLAN.md) | Retains its own frozen trial scope and results; no retry or amendment follows from this investigation. |

Allowed investigation mutations: its single dated progression record, dated findings/evidence references and the necessary live handoff in MEMORY.md. Prefer one findings Markdown file; add a small machine-readable inventory only when it materially improves checking. Inspect local retained files, source and Git; local file listing, JSON inspection and hashing are permitted. Do not import or invoke product/experiment runners, execute target code, install dependencies, acquire new remote evidence or alter executable source/tests, accepted owners, frozen artifacts or historical case labels. A reproducible implementation defect may be documented with its responsible owner; a fix requires a selected change responsibility.

## 3. Effort and resource contract

The investigation has a **six-active-engineering-hour ceiling**, normally allocated as:

| Work | Budget |
| --- | --- |
| Lightweight sixteen-scenario screening, then selected deep readiness | Up to two hours; normally about 45 minutes screening and 75 minutes deep readiness, without a fixed deep-case count |
| Producer/consumer and representation trace | Up to two hours |
| Alternatives, comparison protocol and decision packet | Up to two hours |

These are investigation execution limits, not a retrospective measurement or budget for authoring this plan. Record actual active session start/end spans using a monotonic clock; count reasoning, inspection and writing, and disclose pauses. Do not invent precise historical effort. Allocation may be adjusted within the six-hour total with a recorded reason; extending the total needs an explicit new decision.

Hard resource limits: **zero product/experiment model predictions, zero model loading/GPU work, zero network acquisition, zero target commands/tests/reproductions and zero benchmark-arm executions**. There is no inference token, provider-operation or target-execution allowance. Ordinary local file inspection and document verification are not benchmark runs.

A missing asset or blocked case is a finding. After a bounded local lookup, preserve the exact gap and proceed with independent rows/work; do not spend the remaining budget repairing inputs or inventing labels. If the ceiling is reached, publish available findings, uninspected work and an inconclusive/narrow/stop consequence. Do not present budget exhaustion as evidence that the product or method cannot work.

## 4. Screen retained scenarios, then inspect selected case readiness

Use two levels: lightly screen S001–S016, then select the smallest deep-readiness cohort that discriminates the investment decision. Case IDs are provenance, not new product support promises. The table identifies questions to inspect, not current eligibility, retained-input availability or evaluation verdicts:

| Candidate evidence | Initial role to inspect, not a frozen evaluation verdict |
| --- | --- |
| [Pydantic / Soup Sieve update](../product-simulation/scenarios/S001-pydantic-soupsieve-2.6-to-2.8.4/README.md) (S001) | Dependency/upstream-support evidence and existing normal-product-path proofs |
| [Dashboard API / HTTPX update](../product-simulation/scenarios/S002-kubernetes-dashboard-token-api-httpx-0.27.2-to-0.28.1/README.md) (S002) | Adapter/exposure relation and incomplete CI |
| [event-handler-loader / TypeScript update](../product-simulation/scenarios/S003-event-handler-loader-typescript-5.9.3-to-7.0.2/README.md) (S003) | Historical install-failure/attribution pressure; TypeScript/npm is outside Python product coverage |
| [glyphsLib / pytest patch update](../product-simulation/scenarios/S004-glyphslib-pytest-9.0.2-to-9.0.3/README.md) (S004) | Baseline-sufficient stopping control |
| [modelarrayio / pytest update](../product-simulation/scenarios/S005-modelarrayio-pytest-9.0.3-to-9.1.1/README.md) (S005) | Historically misleading coarse action |
| [qldebugger / Pydantic validator case](../product-simulation/scenarios/S006-qldebugger-pydantic-validator-coverage-gap/README.md) (S006) | Discriminating check design, different artifact bundle and disclosed oracle exposure |
| [BiomedParse / Torch-CUDA family](../product-simulation/scenarios/S007-biomedparse-torch-cuda-family-resolution/README.md) (S007) | Coordinated package-family reasoning and investigation pruning |
| [CARLA / OpenCV artifact fallback](../product-simulation/scenarios/S008-carla-opencv-python36-artifact-fallback/README.md) (S008) | Artifact serviceability and source-fallback separation |
| [CGM / pandas publication](../product-simulation/scenarios/S009-cgm-pandas-publication-reproducibility-contract/README.md) (S009) | Publication, reproducibility and provenance contracts |
| [podcast-script / NumPy requirement](../product-simulation/scenarios/S010-podcast-script-numpy-discovery-breadth/README.md) (S010) | Multiple independently grounded mechanisms from one proposal |
| [Dictare / MLX optional extra](../product-simulation/scenarios/S011-dictare-mlx-optional-extra-ci-coverage/README.md) (S011) | Optional-environment activation and CI coverage |
| [Freqtrade / scikit-learn persisted artifact](../product-simulation/scenarios/S012-freqtrade-sklearn-persisted-artifact-version-boundary/README.md) (S012) | Persisted-artifact producer-version provenance |
| [LangChain / anyio prior sync](../product-simulation/scenarios/S013-langchain-anyio-uv-no-sync-prior-sync-state/README.md) (S013) | Prior state formation versus later no-sync exercise |
| [production-ready-cicd / pip command](../product-simulation/scenarios/S014-production-ready-cicd-pip-already-satisfied-vs-installed/README.md) (S014) | Command completion versus installation provenance |
| [charset-normalizer / pytest marker](../product-simulation/scenarios/S015-charset-normalizer-marker-scoped-pytest/README.md) (S015) | Marker applicability across runtime environments |
| [Thumbor / uv selector scope](../product-simulation/scenarios/S016-thumbor-uv-selector-scope-coverage/README.md) (S016) | Lock membership versus selected-environment reachability |

For each lightweight screening row capture only:

1. product-boundary eligibility and mechanism/responsibility exercised;
2. obvious retained-evidence availability/gaps and plausible evaluation mode;
3. distinct comparison responsibility versus duplication of another scenario;
4. material reviewer/oracle/exposure limits;
5. provisional deep-readiness value and inclusion/exclusion reason.

Use bounded local inspection; detailed identity/hash/producer work belongs to the selected deep cohort. Historical completion alone proves neither present replayability nor product support. S003 remains TypeScript/npm historical attribution pressure, outside supported Python runtime coverage. All sixteen are exposed development evidence; later scenario numbers do not make them protected holdouts. Do not admit S017+ or begin new case discovery here.

Select deep cases by responsibility coverage, retained-input reachability, discriminating value and cost, not scenario chronology or expected favorable answers. Seek, where retained material supports them: a baseline-sufficient/no-value control, misleading coarse reassurance, source/API relation, CI/runtime/environment coverage, dependency/package/environment state, multiple mechanisms, provenance/persisted state and justified unknown/stopping. These are contrasts to seek, not a mandatory case per category. No fixed deep-cohort size is required. Record overlaps, omitted responsibilities and the effect on conclusions; a larger cohort needs a reason within the unchanged six-hour ceiling. If none is useful/reachable, report non-selection.

For each selected deep-readiness row record:

1. **Eligibility and question:** actual ecosystem, automation author, dependency transition and mechanism within the admitted product boundary. Out-of-scope historical material may inform failure design but cannot count as supported Python runtime coverage.
2. **Identity and time:** repository/PR, base/head, dependency/environment identities, observations actually retained and historical information boundary. Later evidence cannot silently enter an earlier decision comparison.
3. **Retained inputs:** exact local path or Git object, hash where practical, content availability and missing/corrupt/private-only material. A reference to an absent file is not retained source content.
4. **Baseline readiness:** the four restricted inputs, provenance/derivation, literal keyword source text, rule/version identity and whether the result can be reproduced without injecting rich interpretation. Preserve absent inputs explicitly.
5. **Product route and dependencies:** normal entry/producer, consumed input form, semantic extraction, network/model requirements, missing adapters and unsupported mechanisms.
6. **Evaluation reference:** source-backed obligations, historical verdict and its qualifications, reviewer/oracle exposure, contradictions and manual semantic preparation. A historical report is not automatically ground truth.
7. **Disposition:** eligibility (`eligible`, `outside scope`, `unresolved`) and comparison readiness (`ready for declared mode`, `partly ready`, `unavailable`, `uninspected`), plus the exact mode, gap and consequence. These are investigation labels, not new product enums.

Distinguish these modes explicitly:

- a normal fresh end-to-end product run, including its actual acquisition and semantic dependencies;
- offline replay of retained observations and, where necessary, an explicitly frozen semantic intermediate;
- deterministic component evaluation that proves only its named bounded responsibility;
- manual simulation/report inspection, which cannot stand in for automated product output.

Current source hints: [investigate_public_pull_request](../src/upgradepilot/investigation.py) defaults to [evaluate_support_drop_runtime](../src/upgradepilot/upstream/support_drop.py), whose eligible source-window path uses `LocalSupportDropExtractor`. Therefore a no-new-model full product comparison is not established merely because downstream validation is deterministic. A supplied evaluator or retained extraction must be declared as a replay/component premise. Do not bypass a model and call the altered route the unchanged fresh product. Do not invoke the entry point to discover its dependencies; inspect source.

Account for all sixteen screening candidates, marking uninspected rows explicitly if the ceiling prevents completion. Separately report screening attempted/completed out of sixteen, deep-cohort selected/inspected and later comparison-ready counts in each declared mode. A candidate omitted from deep inspection is not thereby unsupported or unavailable. A runnable subset may be proposed only with its actual denominator, supported claim and explicit losses. Missing assets remain readiness findings; do not repair/reacquire them, expand the universe or substitute cases merely to improve counts.

## 5. Specify a fair comparison without running it

Use [simulation-transparent-baseline-v0.1](../product-simulation/TRANSPARENT_BASELINE_SPECIFICATION.md) exactly, including ordered rules and output limitations. Its coarse action labels are comparator behavior, not admitted product action permissions. Freeze its version/hash and any intended executable translation before a later run; do not tune keywords on known cases.

Specify for the proposed comparison:

- exact cases, input revisions, modes, product/comparator revisions and information-time boundary;
- restricted baseline inputs versus richer product inputs, with acquisition/preparation/replay differences and assistance disclosed;
- case-specific required/forbidden findings and source bases fixed before new output inspection, distinct from producer inputs;
- complete reporting of attempted/completed, unsupported, unavailable, operationally failed and semantically inadequate cases;
- source-aware development review versus independent maintainer usefulness and protected qualification;
- numeric execution/resource ceilings in the selected follow-up contract; no run is authorized by completing this protocol.

Compare action permission, material source-supported reasons, located uncertainty, specificity of justified next evidence/checks, evidence authority, failure handling, cost and user value. More detail/citations and blanket abstention do not establish benefit. An accurate, useful finding may show a narrower benefit while a non-abstain action remains unavailable; report both facts.

Use a source-backed supported positive, an unsupported reassurance/counterexample and justified unknown handling when the retained subset actually represents them. Retain the baseline-sufficient/no-added-value control where comparable. Missing controls limit the conclusion; they are not permission to manufacture case answers.

Any recommendation, reassurance, compatibility/risk conclusion or requested action is semantically inadequate when a material premise is unsupported, contradicted, stronger than admitted evidence, or a decision-critical unresolved premise is suppressed. Nonempty citations do not cure that failure. A scoped abstention, uncertainty statement or bounded next-evidence request may remain adequate when it explicitly names the missing/unresolved observation and does not promote that absence into a factual technical conclusion. No recommendation citation is not automatic inadequacy; an explicitly preserved missing observation is not negative evidence. Check claims of absence/completeness against the actual bounded evidence and decision-model owner. These criteria do not amend a frozen schema or regrade historical outputs. A model's agreement or an offline reviewer is not an admitted product Validation owner; semantic adequacy alone does not admit an action permission.

Readiness success means a specified, defensible comparison could be attempted under its declared mode and costs. It does not mean either arm wins, the comparison is independent, or all screened/deep cases are supported.

## 6. Trace one useful consumer and the cheapest sufficient owner

Choose one case/question after the inventory, on relevance, input reachability, discriminating value and likely engineering cost—not a favorable expected result. If no case supports a meaningful trace, preserve that gap instead of inventing a subsystem.

Trace source/observation → native facts/assessments → interpretation or conditional relation → evaluation/applicability → synthesis/report consumer. At each step name the actual owner, admitted input form, trustworthy strength, missing premise and responsible capability. Separate missing evidence, incorrect interpretation, absent evaluation and presentation loss; each suggests different work.

Start with [PropositionState and PropositionAssessment](../src/upgradepilot/impact/applicability.py), [Workspace lifecycle records](../src/upgradepilot/workspace/lifecycle_records.py), [proposal evaluation](../src/upgradepilot/workspace/lifecycle_host.py), [synthesis](../src/upgradepilot/maintainer_action.py) and [report projection](../src/upgradepilot/report_projection.py). Reuse their existing semantics where they fit; lifecycle processing outcome is not proposition truth. Native assessed facts do not require a redundant generic model validator. Internal callability or a fabricated fixture is not normal producer reachability.

Write one before/after benefit hypothesis. Specify what would materially change for the maintainer, which premises the product can actually establish, and what remains unresolved. A report finding is a real consumer; it does not establish positive action permission. A proposed targeted check must satisfy the synthesis specification's producer-grounded, discriminating, performable and stopping requirements, including whether UpgradePilot should investigate first. No new action is forced to make the trace look useful.

For a source-relation candidate, state capture completeness, parameter/argument kinds, keyword expansion, caller/callee binding and unknown dynamic dispatch before estimating its value. Human-paired excerpts cannot prove automated binding. Explain why that candidate addresses the chosen gap; do not assume it also repairs typed CI-state promotion or recommendation calibration.

## 7. Choose one next increment or a truthful non-selection

Compare only credible alternatives exposed by the evidence:

| Alternative | What would justify it |
| --- | --- |
| Finite offline product/baseline comparison | Retained inputs, explicit mode, a fair rubric and a plausible decision it can change |
| Repair/reuse an existing deterministic producer or projection | A demonstrated lost/incorrect fact and a reachable useful consumer |
| Bounded deterministic source relation | A mechanically expressible gap, real capture/binding inputs, generality and visible benefit |
| Single-pass semantic interpretation diagnostic/improvement | A residual meaning/calibration question that simpler deterministic work cannot answer; a new finite method decision rather than automatic exposed-fixture tuning |
| Bounded multi-role semantic interpretation/validation experiment | Available facts/relations are lost or conflated in one pass, and scoped responsibilities plus typed handoffs offer a discriminating hypothesis |
| Materially different deployment/model test | A specific residual capability question justifies the added qualification, runtime and inference cost |
| Positive action-permission work | Existing or justified narrow producer derivations can meet the accepted permission; no semantic weakening |
| Narrow, defer or stop | Missing premises, insufficient value, inadequate coverage or disproportionate cost |

For multi-role work, evaluate the hypothesis of the same bounded evidence with separated relation/proposition analysis, validation/challenge and synthesis responsibilities versus one response carrying them together. Evidence selection is another possible responsibility only when relevant. Roles are not mandatory agents, processes, model families or frameworks. A later comparison may use the same model in isolated calls to reduce deployment confounding. Specify any scoped-context differences, typed handoffs, resource differences and source-backed review obligations before proposing that experiment; this investigation runs none of it.

Record counterevidence: older Fixed work already used stages and still failed; additional calls create cost, handoff and failure modes; same-model or different-model agreement is not independent evidence; an always-reject/unresolved validator cannot establish useful discrimination. Compare preserved supported findings, false acceptance/rejection and justified unknowns, not agreement alone. Existing deterministic/native owners may solve the selected gap more cheaply. State whether multi-role work is worth selecting, deferred, rejected for this gap or unresolved. Give an evidence-based disposition for each named alternative without inventing a full design for an inapplicable option. No framework, parser, model topology or positive action is preselected.

For each credible option record evidence, expected information/benefit, remaining uncertainty, effort/resource estimate and maintenance/replacement cost. Estimates remain estimates. State why the preferred option beats the simpler alternative and the strongest counterargument. Do not turn a weighted score or known expected answer into the decision authority.

The chosen follow-up contract must name: exact responsibility and observable benefit; retained/normal input boundary; code home and integration seam; reused state/evidence owner; supported scope and excluded capabilities with re-entry conditions; proof and failure/unknown treatment; exact engineering ceiling and applicable call/token/operation/time/retention limits; prerequisites and success/narrow/reject/inconclusive consequences. For a no-call route, declare zero calls. For a model route, count qualification and unknown usage as well as semantic calls; no fresh prediction occurs in this investigation.

Settle product versus experiment responsibility before Build. An exploratory parser generally starts as disposable experiment work; an admitted existing product derivation may belong in product source. Justify the choice and adoption/disposal path. Product runtime cannot import experiments/tests/tools, and a directory alone does not prove product capability. New stable semantics or consequential architecture go to their proper owner; no generic proposition/evaluation framework is selected by default.

A material method change after development requires a new exact freeze and fresh protected qualification before general claims. Source-aware development success, runtime validation, positive permission, independent usefulness and adoption remain separate proof gates.

## 8. Verification, consequences and stop line

Before publishing the findings, check every material claim against its linked source/input and confirm:

- sixteen lightweight screening rows exist with honest eligibility, mode, exposure, selection reason or explicit uninspected state; deep-cohort selection, omitted responsibilities and separate screening/deep/runnable denominators are explicit;
- the protocol preserves comparator restrictions, source/time identities and useful-positive/false-positive/unknown distinctions;
- semantic review checks material premises and preserved uncertainty, not citation-list cardinality; historical frozen verdicts remain unchanged;
- the consumer trace identifies an actual producer and earliest sufficient owner or records its exact absence;
- named alternatives include bounded multi-role work with its counterevidence, cost and disposition; no inference occurs;
- the recommended contract is reviewable without inventing further architecture, or non-selection states the missing premise; explicit acceptance is still required before any follow-on execution;
- effort/resource accounting and skipped work are honest, local links/hashes cited are checkable, and no forbidden execution or frozen-evidence changes occurred.

This read-only responsibility needs document/data/source verification, not a product test-suite rerun. Record semantic uncertainty rather than promoting a link/hash check into semantic proof.

| Disposition | Required consequence |
| --- | --- |
| Ready and useful decision available | Recommend one finite next action with its complete contract; execution remains separately selected. |
| Partly ready | Name the narrower supported comparison/benefit and all exclusions; recommend it only if still materially useful. |
| Not ready / no justified value | Publish exact gaps and cost; reject/defer the affected direction rather than build generic infrastructure. |
| Budget/evidence insufficient | Publish an inconclusive decision with uninspected work and the smallest missing premise; no automatic extension. |

Preserve meaningful progress in one investigation cycle record and keep findings in one dated packet. Explain what the evidence established, failed to establish and changed from expectations; repair or explicitly defer important learner gaps without inferring mastery. MEMORY.md alone records the selected handoff. Stop after the investigation's decision packet and evidence-backed learning/handoff; no benchmark, implementation, action admission or model run follows automatically.
