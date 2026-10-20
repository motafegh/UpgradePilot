# Product value and transparent-baseline feasibility investigation plan

**Artifact:** Prepared bounded investigation plan; acceptance/activation and results belong only in [MEMORY.md](../MEMORY.md).  
**Responsibility:** Determine whether exposed retained development evidence supports a fair automated-product versus transparent-baseline comparison, identify what useful product information is actually reachable beyond that baseline, and recommend one justified next increment or an explicit narrow/stop/inconclusive disposition.  
**Direction basis:** [Accepted product-direction proposal](../proposals/2026-10-19_INVESTIGATOR_RESPONSIBILITY_DECOMPOSITION_AND_PRODUCT_DIRECTION_PROPOSAL.md), [AUDIT-014](../audits/2026-10-20_AUDIT-014_product-value-and-evaluation-sequencing.md), and the October 20 review corrections. Preparing or revising this plan does not execute the investigation or authorize Build, inference, benchmark execution, acquisition or target execution.

## 1. Question, deliverable and proof boundary

For a maintainer reviewing a public Python Dependabot update:

> What useful, source-supported information can the implemented product add beyond the four-input transparent baseline, and which reachable improvement is worth the next engineering investment?

This investigation establishes **comparison readiness and a source-backed investment recommendation**. It does not itself run either comparison arm, measure product superiority, validate a new semantic method, establish independent maintainer usefulness, qualify a protected method, or admit a new maintainer action.

On execution, keep detailed progression in one investigation cycle record and place the findings packet at:

`working-memory/evidence/<execution-date>-product-value-and-transparent-baseline-feasibility/FINDINGS.md`

Do not precreate results during plan writing. Deliver one dated packet containing:

- a lightweight S001–S016 screening table, including out-of-scope, unavailable and uninspected cases;
- the **smallest discriminating deep-readiness cohort** selected from that screen, with exact reasons for inclusion/exclusion;
- a proposed fair comparison protocol with exact evidence modes, supported scope and review obligations;
- one concrete producer-to-consumer trace and a before/after maintainer-benefit hypothesis;
- a comparison of credible next increments, with a preferred option and counterarguments;
- a complete bounded action contract for that option, or the exact missing premise and a narrow/stop/inconclusive disposition.

Do not create a general evaluation framework or a mandatory sequence of later plans. A complete findings contract may be sufficient as the artifact presented for decision, but it is **not self-authorizing**. Explicit review/acceptance is required before any Build, product/source/test modification, benchmark execution, model/agent inference, network acquisition, target execution or product-action admission begins. Material new product semantics or architecture still require their proper owner.

## 2. Owners, entry and modification boundary

Read the [Charter](../PROJECT_CHARTER.md), accepted [Product Decision Model](../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md), [Core](../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md), [Minimum Useful Generality](../docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md), [Maintainer Action Synthesis](../docs/specifications/UPGRADEPILOT_MAINTAINER_ACTION_SYNTHESIS_SPECIFICATION.md) and [ADR-0012](../docs/architecture/ADR-0012-canonical-investigation-workspace-and-recovery-boundary.md) where their responsibilities matter. Reference their semantics; do not redefine them here.

At entry, reconcile current Git/source, the accepted proposal, live selection, this plan's revision and the preceding dated handoff. Record source revision and inspection horizon. Preserve existing incomplete/negative Investigator outcomes, costs, unknown usage and learning debt; none is an automatic allowance to resume inference.

Read [simulation instructions](../product-simulation/AGENTS.md) before inspecting local cases. S001–S016 remain immutable **exposed development evidence**. This plan does not restart simulations, admit a new case, or reclassify any existing case as protected validation.

Related responsibilities remain separate:

| Existing owner | Relationship to this investigation |
| --- | --- |
| [Product direction and maintainer utility plan](PRODUCT_DIRECTION_AND_MAINTAINER_UTILITY_INVESTIGATION_PLAN.md) | Owns the broader action/advisor/hybrid direction comparison; do not reopen it merely to inspect baseline readiness. |
| [Report preservation and usefulness plan](MAINTAINER_REPORT_PRESERVATION_AND_USEFULNESS_EVALUATION_PLAN.md) | Owns report faithfulness/preservation and independent usefulness evaluation. This investigation may reuse criteria without claiming to perform that study. |
| [Upstream API and target-exposure feasibility plan](UPSTREAM_API_CHANGE_AND_TARGET_EXPOSURE_FEASIBILITY_PLAN.md) | Owns a conditional executable API/exposure trial. Source-relation work remains an alternative here; this plan does not activate that trial. |
| [Historical instruction comparison plan](INVESTIGATOR_EVIDENCE_FIRST_INTERPRETATION_COMPARISON_PLAN.md) | Retains its own frozen scope/results; no retry, regrading or amendment follows from this investigation. |

Allowed investigation mutations: its dated progression record, dated findings/evidence references, an optional small machine-readable screen when that materially improves checking, and the necessary live handoff in `MEMORY.md`. Inspect local retained files, source and Git; local file listing, JSON inspection and hashing are permitted.

Do not import or invoke product/experiment runners, execute target code, install dependencies, acquire new remote evidence, alter executable source/tests, mutate accepted owners, repair frozen artifacts, change historical case labels, or fill missing comparison inputs during this investigation. A reproducible implementation defect may be documented with its responsible owner; a fix requires a separately selected change responsibility.

## 3. Effort and resource contract

The investigation has a **six-active-engineering-hour ceiling**, normally allocated as:

| Work | Budget |
| --- | --- |
| S001–S016 light screen + selected deep-cohort readiness | Up to two hours total |
| Producer/consumer and representation trace | Up to two hours |
| Alternatives, comparison protocol and decision packet | Up to two hours |

Within the first two-hour block, perform the S001–S016 screen first and spend the remaining time only on the smallest discriminating deep cohort. Do not deeply analyze all sixteen merely because they were screened. There is no required deep-case count.

These are execution limits, not retrospective measurements or budgets for authoring this plan. Record actual active session spans honestly; disclose pauses. Allocation may be adjusted within the six-hour total with a recorded reason. Extending the total requires an explicit new decision.

Hard resource limits: **zero product/experiment model predictions, zero model loading/GPU work, zero network acquisition, zero target commands/tests/reproductions and zero benchmark-arm executions**. There is no inference-token, provider-operation or target-execution allowance. Ordinary local file/source/document inspection and hashing are not benchmark runs.

A missing asset or blocked case is a finding. After a bounded local lookup, preserve the exact gap and continue with independent rows/work. Do not spend the remaining budget repairing inputs or inventing labels. If the ceiling is reached, publish available findings, uninspected work and an inconclusive/narrow/stop consequence. Budget exhaustion is not evidence that the product or method cannot work.

## 4. Screen S001–S016, then select a deep cohort

### 4.1 Lightweight screening universe

Screen these exact historical candidates; case IDs are provenance, not product-support promises:

| Case | Initial responsibility/value pressure to inspect |
| --- | --- |
| [S001 — Pydantic / Soup Sieve](../product-simulation/scenarios/S001-pydantic-soupsieve-2.6-to-2.8.4/README.md) | upstream Python-support evidence + target applicability |
| [S002 — Dashboard / HTTPX](../product-simulation/scenarios/S002-kubernetes-dashboard-token-api-httpx-0.27.2-to-0.28.1/README.md) | source/API relation, consumer forwarding, incomplete CI |
| [S003 — event-handler-loader / TypeScript](../product-simulation/scenarios/S003-event-handler-loader-typescript-5.9.3-to-7.0.2/README.md) | historical install-failure/attribution pressure; outside supported Python coverage |
| [S004 — glyphsLib / pytest](../product-simulation/scenarios/S004-glyphslib-pytest-9.0.2-to-9.0.3/README.md) | baseline-sufficient / no-added-value stopping control |
| [S005 — modelarrayio / pytest](../product-simulation/scenarios/S005-modelarrayio-pytest-9.0.3-to-9.1.1/README.md) | coarse favorable baseline versus coverage/target uncertainty |
| [S006 — qldebugger / Pydantic](../product-simulation/scenarios/S006-qldebugger-pydantic-validator-coverage-gap/README.md) | targeted-check design; distinct bundle and disclosed oracle exposure |
| [S007 — BiomedParse / torch CUDA family](../product-simulation/scenarios/S007-biomedparse-torch-cuda-family-resolution/README.md) | coordinated package-family reasoning and static-evidence pruning |
| [S008 — CARLA / OpenCV](../product-simulation/scenarios/S008-carla-opencv-python36-artifact-fallback/README.md) | binary artifact availability versus source fallback and CI coverage |
| [S009 — CGM / pandas](../product-simulation/scenarios/S009-cgm-pandas-publication-reproducibility-contract/README.md) | repository-purpose/provenance consistency independent of runtime compatibility |
| [S010 — podcast-script / NumPy](../product-simulation/scenarios/S010-podcast-script-numpy-discovery-breadth/README.md) | multi-mechanism discovery breadth and stopping |
| [S011 — dictare / mlx optional extra](../product-simulation/scenarios/S011-dictare-mlx-optional-extra-ci-coverage/README.md) | optional environment activation and proposition-specific CI coverage |
| [S012 — freqtrade / scikit-learn](../product-simulation/scenarios/S012-freqtrade-sklearn-persisted-artifact-version-boundary/README.md) | persisted-artifact producer-version/history applicability |
| [S013 — langchain / anyio](../product-simulation/scenarios/S013-langchain-anyio-uv-no-sync-prior-sync-state/README.md) | prior state formation versus later no-sync exercise |
| [S014 — production-ready-cicd / pip](../product-simulation/scenarios/S014-production-ready-cicd-pip-already-satisfied-vs-installed/README.md) | current requirement state versus install provenance |
| [S015 — charset-normalizer / pytest marker](../product-simulation/scenarios/S015-charset-normalizer-marker-scoped-pytest/README.md) | marker-scoped requirement applicability across runtime rows; current extractor boundary |
| [S016 — thumbor / uv scope](../product-simulation/scenarios/S016-thumbor-uv-selector-scope-coverage/README.md) | lock membership versus selected-root/environment reachability |

For each lightweight row record only what is needed to decide deep-readiness value:

1. current product-boundary eligibility;
2. distinct mechanism/responsibility exercised;
3. retained evidence availability and obvious material gaps;
4. plausible evidence/evaluation mode;
5. whether it adds a distinct comparison responsibility or duplicates another case;
6. material reviewer/oracle/exposure limitation;
7. provisional deep-readiness value.

S003 may remain useful failure/attribution pressure, but TypeScript/npm cannot count as supported Python product coverage. Do not add S017+ or perform new case discovery merely to improve coverage counts.

### 4.2 Evidence/evaluation modes are first-class

Do not pool these modes:

- **fresh end-to-end product** — current normal entry path, actual acquisition and conditional semantic dependencies;
- **offline replay** — retained observations plus any explicitly frozen semantic intermediate required by the declared replay boundary;
- **deterministic component evaluation** — proves only the named bounded product responsibility;
- **current-source projection** — source-backed prediction of current behavior/unsupported boundary, not a product execution;
- **historical manual/AI-assisted simulation/report inspection** — development evidence that cannot stand in for current automated product output.

A historical `BASELINE_RESULT.json` may preserve the old simulation comparison; it does not make the paired historical full-investigation result a current-product run. Likewise a current-source projection is not fresh execution.

For every deep row record:

1. **Eligibility and question** — ecosystem, automation author, transition and mechanism inside/outside admitted scope.
2. **Identity and time** — repository/PR, base/head, dependency/environment identities, retained observation time boundary.
3. **Retained inputs** — exact path/Git object/hash where practical; missing/corrupt/private-only material.
4. **Baseline readiness** — four restricted inputs, their provenance, literal keyword source, baseline version/rule and whether reproducible without rich interpretation.
5. **Product route/dependencies** — actual producer/entry, consumed form, semantic/network/model dependencies, missing adapters and unsupported mechanisms.
6. **Evaluation reference** — source-backed obligations, historical verdict qualifications, contradictions, assistance and oracle exposure.
7. **Mode/disposition** — exact evidence mode plus `ready for declared mode`, `partly ready`, `unavailable` or `uninspected`, with gap and consequence.

Current source matters: `investigate_public_pull_request` normally reaches a support-drop path that can use `LocalSupportDropExtractor`. Therefore a no-new-model altered path is not automatically the unchanged fresh product. A supplied evaluator or retained extraction must be declared as a replay/component premise.

### 4.3 Select the smallest discriminating deep cohort

Select deep cases by **responsibility coverage + evidence mode + current producer/consumer reachability + decision value**, not case number or favorable expected answer.

Where actually supported by retained evidence, seek useful contrasts such as:

- baseline-sufficient/no-added-value control;
- misleading coarse baseline or unsupported reassurance;
- supported positive finding;
- source/API relation;
- CI/runtime/environment coverage;
- dependency/package/environment state;
- multi-mechanism reasoning;
- provenance/persisted-state boundary;
- justified unknown/stopping behavior;
- current deterministic transfer/unsupported boundary.

A smaller cohort is preferred when it answers the decision. A somewhat larger cohort is acceptable only within the unchanged six-hour ceiling and with a recorded reason. Report the full 16-case screening denominator even if only a subset receives deep readiness analysis.

## 5. Specify a fair comparison without running it

Use [simulation-transparent-baseline-v0.1](../product-simulation/TRANSPARENT_BASELINE_SPECIFICATION.md) exactly, including ordered rules and input restrictions. Its coarse action labels are comparator behavior, **not** maintainer-action permissions automatically available to the current product. Freeze its version/hash and any intended executable translation before a later run; do not tune keywords on known cases.

Specify:

- exact cases, input revisions, evidence modes, product/comparator revisions and information-time boundary;
- restricted baseline inputs versus richer product inputs, with acquisition/preparation/replay differences and assistance disclosed;
- case-specific required/forbidden findings and source bases fixed before new output inspection, distinct from producer inputs;
- complete reporting of attempted/completed, unsupported, unavailable, operationally failed and semantically inadequate cases;
- source-aware development review versus independent maintainer usefulness versus future protected qualification;
- numeric execution/resource ceilings in any selected follow-up contract; completing this protocol authorizes no run.

### 5.1 Separate information value from action permission

Current deterministic synthesis admits only explained `abstain`. Therefore evaluate separately:

**Information value**
- material source-supported findings/reasons added;
- unsupported reasons/reassurance removed;
- uncertainty narrowed, broadened correctly or better located;
- evidence authority corrected;
- more specific discriminating next evidence/check identified;
- unnecessary investigation correctly stopped/pruned;
- missing/conflicting/irrelevant evidence handled honestly;
- additional cost.

**Action permission**
- whether an admitted maintainer action changes;
- which positive prerequisites establish it;
- whether that permission comes from the normal producer path.

A useful report finding can demonstrate narrower product value while final action remains `abstain`. Report both facts. Blanket abstention is not product superiority by itself, and inability to emit a positive action must not erase genuine information gain.

More prose, citations, roles or calls are not value metrics.

### 5.2 Semantic adequacy is material-premise based

Any recommendation, reassurance, compatibility/risk conclusion or requested action is inadequate when a material premise is unsupported, contradicted, stronger than admitted evidence, or when a decision-critical unresolved premise is suppressed.

```text
citation exists
!= cited source entails the material premise
```

and:

```text
no recommendation citation
!= automatically inadequate
```

A scoped abstention, uncertainty statement or bounded next-evidence request may be adequate when it explicitly names the unresolved/missing observation and does not promote absence into a negative technical fact.

Use a source-backed supported positive, unsupported reassurance/counterexample and justified-unknown handling when the selected cohort genuinely provides them. Retain a baseline-sufficient/no-added-value control where comparable. Missing controls constrain the claim; they do not permit manufactured answers. Model agreement or offline review is not an admitted product Validation owner.

Readiness means a specified, defensible comparison could later be attempted under its declared mode and cost. It does not mean either arm wins, the study is independent, or all screened cases are supported.

## 6. Trace one useful consumer and the cheapest sufficient owner

Choose one deep case/question on relevance, current input reachability, discriminating value and likely engineering cost—not a favorable expected result. If no case supports a meaningful current trace, preserve that gap rather than inventing a subsystem.

Trace:

`source/observation → native facts/assessments → interpretation/conditional relation → evaluation/applicability → synthesis/report consumer`

At each step name the actual owner, admitted input form, evidence strength, missing premise and responsible capability. Separate:

- missing/acquisition evidence;
- incorrect relation/binding;
- incorrect semantic interpretation;
- absent evaluation/applicability;
- action-permission gap;
- projection/presentation loss.

Start with [PropositionState and PropositionAssessment](../src/upgradepilot/impact/applicability.py), [Workspace lifecycle records](../src/upgradepilot/workspace/lifecycle_records.py), [proposal evaluation](../src/upgradepilot/workspace/lifecycle_host.py), [synthesis](../src/upgradepilot/maintainer_action.py) and [report projection](../src/upgradepilot/report_projection.py). Reuse their semantics where they fit; lifecycle processing outcome is not proposition truth. Native assessed facts do not require a redundant generic model validator.

Write one before/after benefit hypothesis: what changes for the maintainer, which premises the product can establish, which remain unresolved, and what cheaper owner could satisfy the same responsibility.

A report finding is a real consumer; it does not establish positive action permission. A proposed targeted check must meet the synthesis specification's producer-grounded, discriminating, performable and stopping requirements, including whether UpgradePilot itself should investigate first.

For a source-relation candidate, state capture completeness, parameter/argument kinds, keyword expansion, caller/callee binding and unknown dynamic dispatch before estimating value. Human-paired excerpts do not prove automated binding. Do not assume a source relation also fixes CI-state promotion, applicability completeness or recommendation calibration.

## 7. Choose one next increment or a truthful non-selection

Compare only credible alternatives exposed by the trace:

| Alternative | What would justify it |
| --- | --- |
| Repair/reuse an existing deterministic producer or projection | Demonstrated lost/incorrect fact and reachable useful consumer |
| Bounded deterministic source-fact/relation derivation | Mechanically expressible gap, real capture/binding inputs, honest scope and visible benefit |
| Finite product/baseline comparison | Exact retained/current modes, fair protocol and a decision that the comparison can change |
| Positive action-permission/synthesis work | Existing or justified narrow producer facts can meet accepted permission without semantic weakening |
| Single-pass semantic diagnostic/improvement | Residual interpretation/calibration uncertainty that simpler deterministic work cannot answer |
| **Bounded multi-role semantic interpretation/validation experiment** | Facts are available but responsibility conflation/scoped-context/validation failure is a plausible residual and role isolation can be tested distinctly |
| Materially different deployment/model test | A named deployment-quality residual remains after evidence/task-shape issues are controlled |
| Narrow, defer or stop | Missing premises, inadequate value/coverage or disproportionate cost |

For the multi-role option, preserve the empirical hypothesis rather than preselecting an architecture:

```text
same bounded evidence
+ explicit responsibility separation
+ scoped role contexts
+ typed proposition/evaluation handoffs
+ challenge/validation responsibility

versus

one response carrying relation building,
interpretation, uncertainty handling and reporting together
```

Potential roles are responsibilities, not mandatory processes, models, agents or frameworks. A first role-decomposition test may intentionally reuse one model in isolated calls to avoid immediately confounding role shape with model family. Earlier staged Fixed work is important counterevidence: more stages alone are not a demonstrated cure.

For each credible option record evidence, expected decision information/benefit, remaining uncertainty, effort/resource estimate, maintenance/replacement cost and what work the result would allow the project to stop. State why the preferred option beats the simpler alternative and its strongest counterargument.

The chosen follow-up contract must name: exact responsibility and observable benefit; retained/normal input boundary; code home/integration seam; reused evidence owner; supported scope and re-entry conditions; proof and failure/unknown treatment; engineering ceiling and applicable call/token/operation/time/retention limits; prerequisites; success/narrow/reject/inconclusive consequences. For a no-call route declare zero calls. For a model route count qualification and unknown usage as well as semantic calls.

No fresh prediction occurs in this feasibility investigation.

Settle product versus experiment responsibility before Build. An exploratory parser generally starts as disposable experiment work; an admitted existing product derivation may belong in product source. Justify adoption/disposal. Product runtime cannot import experiments/tests/tools. New stable semantics or consequential architecture go to their proper owner; no generic proposition framework, source parser, validator model, agent framework, model sweep or positive action is selected by default.

A material method change after exposed development work requires a new exact freeze and future protected qualification before general claims. Source-aware development success, runtime validation, positive action permission, independent usefulness and adoption remain separate proof gates.

## 8. Verification, consequences and stop line

Before publishing findings, confirm:

- all S001–S016 have lightweight screening rows with honest eligibility, distinct responsibility, evidence availability/mode, exposure and deep-readiness value;
- the selected deep cohort is the smallest one that can discriminate the decision, with no fixed-count pressure;
- S003 does not count as supported Python coverage;
- every deep row identifies exact evaluation mode and does not promote historical/manual/source-projection evidence into fresh product output;
- the comparison protocol preserves comparator restrictions, source/time identities, useful-positive/false-reassurance/unknown/no-added-value distinctions and information-value/action-permission separation;
- semantic adequacy is judged by material-premise support rather than citation-list cardinality;
- the consumer trace identifies an actual current producer and earliest sufficient owner or records the exact absence;
- deterministic repair, single-pass semantic work, bounded multi-role decomposition and deployment/model change are distinct alternatives rather than a preselected sequence;
- any complete findings/action contract still requires explicit acceptance before execution;
- effort/resource accounting and skipped work are honest and no forbidden execution/frozen-evidence change occurred.

This read-only responsibility needs document/data/source verification, not a product test-suite rerun. Record semantic uncertainty rather than promoting a link/hash check into semantic proof.

| Disposition | Required consequence |
| --- | --- |
| Ready and useful decision available | Recommend one finite next action with a complete contract; execution remains separately selected. |
| Partly ready | Name the narrower supported comparison/benefit and all exclusions; recommend it only if still materially useful. |
| Not ready / no justified value | Publish exact gaps/cost and reject/defer the affected direction rather than build generic infrastructure. |
| Budget/evidence insufficient | Publish an inconclusive decision with uninspected work and the smallest missing premise; no automatic extension. |

Preserve meaningful progress in one investigation record and one dated findings packet. `MEMORY.md` alone records any selected handoff after explicit review.

**STOP:** no benchmark, implementation, action admission, model/agent run, network acquisition or target execution follows automatically from the findings.