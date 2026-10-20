# AUDIT-017 — Investigator experiment methodology and machinery lifecycle

**Audit date:** 2026-10-20  
**Branch:** `audit/project-wide-system-audit-2026-10-20`  
**Main revision last reconciled:** `a1c291c6cf9238493eeb666b184192ed178b90f1`  
**Mode:** cross-responsibility experiment-methodology and retention audit  
**Authority:** non-controlling audit evidence. No model call, experiment rerun, product adoption or experiment-file deletion is authorized by this record.

## 1. Question

After the October Investigator research, qualification, Raw/Structured/Fixed/Agent comparisons, supplied-evidence diagnostics and instruction-only comparison:

> Which experiment mechanisms still have a justified reusable responsibility, which runners/protocols now belong to historical evidence, and what exact residual question would justify another model call?

## 2. Executive assessment

The Investigator programme produced substantial useful negative evidence and several reusable laboratory controls, but its **live question has moved**.

AUDIT-011 correctly identified that the broad autonomous comparison mixed controller economics, interface usability, discovery, interpretation, stopping and reporting. Its recommended supplied-evidence localization was then executed on main. The r4 supplied-evidence cohort completed cleanly with **5/5 operational roles and 0/4 semantically adequate cases**. The r5 instruction-only candidate also completed cleanly and left **0/4 adequate cases**, despite some partial corrections.

Therefore the immediate bottleneck is no longer “can this exact supplied-evidence runner finish?” or “should autonomous navigation be optimized first?” It is **whether a useful product gap remains that actually requires semantic interpretation, and if so which isolated interpretation/validation responsibility is worth another experiment**.

The correct lifecycle decision is not to delete all experiment infrastructure. It is to separate:

1. **reusable laboratory substrate**;
2. **conditional research baselines that may inform a named future question**;
3. **completed cohort/freeze runners that are historical and should not be treated as current defaults**;
4. **accepted product architecture that has already superseded prototype experiment routes**.

`experiments/` currently has no README/lifecycle index making those distinctions, which creates avoidable maintenance and selection risk.

## 3. What later evidence changed from AUDIT-011

### Run-control/completion question

AUDIT-011 found real deadline/cancellation, completion-affordability, navigation and pagination problems in the broad autonomous experiment. Those remain valid evidence about that protocol.

Later main work repaired the local run-control path sufficiently for the selected supplied-evidence diagnostic:

- all five r4 roles completed;
- known usage was complete;
- all reports published;
- resource/deadline ceilings passed;
- owned model/client cleanup passed.

The r5 instruction-only comparison also completed all five predictions under the same bounded supplied-evidence responsibility.

**Consequence:** do not continue treating controller completion as the default blocker for the report-only path. If a future autonomous-discovery protocol is selected, completion affordability still needs a prospective invariant; that is a different question.

### Semantic question

r4 removed autonomous discovery as the immediate cause by delivering the relevant evidence directly. All four cases remained semantically inadequate, including contradicted forwarded-argument claims, omitted material relations and overclaimed CI coverage.

r5 changed only the model-facing task goal within the existing report shape. It produced real partial improvements—e.g. withdrawing earlier low-risk reassurance and noticing some forwarding facts—but all four cases still failed the frozen semantic obligations and new false relations appeared.

**Consequence:** another prompt/instruction variant on the same exposed fixtures is not justified without a newly isolated hypothesis.

### Broader Fixed/Agent research

The completed contract2 branch result produced **8/8 mechanically valid final reports and 0/8 advice-ready reports**. Discovery advantages were mixed: Agent sometimes found useful material that Fixed missed, while Fixed sometimes covered sources better. Agent used less observed input and elapsed time in all four descriptive pairs, but one sample per arm/deployment and different policy overhead do not establish a general efficiency or quality ranking.

**Consequence:** autonomous agency remains an empirical candidate, not a winner and not the current prerequisite. Semantic recommendation failures persisted across both policies.

## 4. Cost/information-value interpretation

Do not pool incompatible experiment lineages as one statistical sample. Their accounting remains separate.

Within the AUDIT-011 main lineage, historical accounting recorded **460 qualification attempts versus 45 semantic attempts** (~91.1% qualification). This does not make qualification useless; runtime, rendering and reference failures were real. It does show that full-matrix qualification became disproportionate to the number of product questions resolved.

The broader Fixed/Agent branch separately recorded 135 attempts and ~3h17m summed trial time for the final selected comparison, with 0/8 advice-ready reports.

Main r4/r5 then spent another finite pair of completed five-role cohorts and still obtained 0/4 adequate cases in each.

**Decision principle:** future inference should maximize **information gained per product decision**, not number of models/arms/qualifications completed.

## 5. Experiment machinery lifecycle

### 5.1 RETAIN — reusable laboratory substrate

These mechanisms still serve a plausible future bounded semantic experiment:

#### `experiments/investigator_run_control.py`

Retain as experiment-only process-control infrastructure for the current LM Studio SDK path:

- monotonic deadline ownership;
- cancellation/drain/release handling;
- signal handoff discipline;
- explicit unknown-usage treatment.

It is platform/runtime specific and must be requalified when SDK/backend/transport changes. It is not product runtime infrastructure.

#### `experiments/investigator_model_interface.py`

Retain the strict stateless request/measurement/receipt/configuration/cleanup mechanisms as a reusable lab boundary. Do not treat current request presentations, SDK version assumptions or deployment identity as universal.

Future use requires a new source-bound freeze when prompt/schema/tool/configuration/runtime changes materially.

#### `experiments/investigator_workspace_adapter.py`

Retain as an experiment-owned bridge into product Workspace/source authority. Its separation of delivered references, lifecycle records and model-authored interpretation is valuable.

However its native-family/tool menu is a snapshot of the current experiment boundary. Any future use must reconcile it against the then-current product Workspace; it cannot become a competing product contract.

#### `experiments/investigator_workspace_trial.py`

Retain model-free packing/reference/publication and scripted-feasibility mechanisms. They are useful for proving an experiment protocol mechanically before paying for inference.

Do **not** reuse the old 48-operation economics as a default future budget. AUDIT-011 already showed that its terminal reserve was insufficient for some natural autonomous paths.

#### `experiments/investigator_supplied_evidence.py`

Retain the generic report-only supplied-evidence composition as a useful simpler semantic baseline. It cleanly separates trusted preparation from consumer interpretation and can support a future single-pass or role-decomposition comparison if a product trace justifies one.

The existing PR/source-pair briefs are exposed development instructions, not a protected qualification method.

### 5.2 NARROW / REQUALIFY — useful mechanisms wrapped in question-specific policy

#### `experiments/qualify_investigator_model_interface.py`

The underlying identity/backend/render/token/receipt checks are valuable. The current qualifier, however, hardcodes a six-candidate universe and a Raw/Structured × sequence matrix built for the concluded comparison lineage.

Do not make another full matrix the standing admission tax for every future semantic question. A new experiment should qualify only the changed deployment/interface claims at risk, with a small wire/runtime smoke plus representative capacity/fit evidence.

Retain the mechanism; narrow the future contract.

#### `experiments/api_python_bindings.py` and related deterministic API/source research

This research remains potentially relevant to AUDIT-014's deterministic source-fact/relation candidate. It already preserves lexical binding uncertainty rather than promoting source observations into execution truth.

Do not port it into product source by inheritance. If Stage-2/architecture tracing selects a deterministic relation responsibility, compare its admitted grammar/producer/consumer needs with this research and either reuse/port the justified subset or reject it.

### 5.3 HISTORICAL / DORMANT — completed cohort runners

These should remain reproducible evidence but must not look like the default route for the next experiment:

#### `experiments/run_investigator_semantic_comparison.py`

Encodes the completed/incomplete three-deployment × two-case × Raw/Structured question, its qualification dependency and old freeze semantics. That exact comparison is closed/inconclusive and explicitly must not be resumed merely to finish the denominator.

Status: **historical runner**. A future comparison should create a new bounded protocol rather than silently relaunch this one.

#### `experiments/run_investigator_supplied_evidence.py`

Contains exact Gemma12 operating-point inheritance, fixed context/GPU layer assumptions, packet roles A–D, current cohort ceilings and source-bound freeze logic used for r4/r5. The selected exposed-case diagnostic has produced its negative result.

Status: **historical cohort runner / useful implementation reference**. Do not use it as the default launcher for a multi-role or new-model experiment; those require a new finite question and freeze.

#### `experiments/prepare_investigator_supplied_evidence.py` and fixed packet recipes

Retain for provenance/reproduction of r4/r5. The exact packet selection is exposed development material. A future semantic experiment may reuse source material only at the claim strength allowed by its new protocol; it should not inherit the old packet set as a qualification corpus by default.

### 5.4 SUPERSEDED AS ACTIVE ARCHITECTURE — Workspace prototype/migration experiments

Files such as:

- `experiments/workspace_replacement_migration.py`;
- `experiments/workspace_revision_representation.py`;
- `experiments/workspace_seam_*`;
- `experiments/run_workspace_migration_trial.py`;
- related checkpoint/public-grounding/revision-comparison runners;

remain valuable historical architecture/research evidence. But accepted ADR-0012/0013 plus `src/upgradepilot/workspace/` and active product tests now own the real Workspace implementation.

`run_workspace_migration_trial.py` itself describes a bounded migration proof with **no product cutover** and runs over experiment-owned prototype representations.

Status: **historical architecture experiment**, not an alternate active Workspace implementation path. Future product migration should use product source/tests and accepted ADR/plan owners rather than extending prototype modules unless a new research question explicitly requires them.

## 6. Findings

### AUDIT-017-F1 — P1: future model calls require a named residual product question

After r4/r5, no further inference is justified by the generic goal “improve Investigator.” A future model call must name the exact unresolved responsibility and simpler alternative.

Examples of valid residual hypotheses:

- supplied native/source facts are correct and reachable, but one-pass semantic relation selection remains inadequate;
- a validator role can reject false premises without collapsing into blanket unresolved output;
- a smaller/scoped role context materially improves proposition handling versus one combined response;
- a deployment/model difference is still plausible after task/input/interface confounders are controlled;
- autonomous discovery is worth revisiting only after the chosen interpretation method is adequate on supplied evidence.

If the product-value/source trace instead identifies a deterministic producer/projection gap, do that cheaper work first.

### AUDIT-017-F2 — P1: do not resume autonomous discovery optimization before semantic adequacy earns it

AUDIT-011 already defined this stopping rule; r4 activated it. Decisive evidence was delivered and the reports still made decision-critical semantic errors.

Autonomous discovery remains useful research, but it is not the immediate dependency for the observed supplied-evidence failures.

### AUDIT-017-F3 — P1: full qualification matrices must be proportional to the changed claim

Qualification should protect interface/runtime claims at risk, not become the dominant research output. The recorded main lineage's ~91.1% qualification-attempt share is strong evidence that standing full-matrix requalification can overwhelm semantic learning.

For future experiments distinguish:

```text
deterministic code-only change
→ deterministic tests / no model requalification unless wire semantics changed

prompt/schema/tool/render/configuration change
→ small representative real-model interface smoke + exact fit/config proof

deployment/model operating-point change
→ point-specific identity/backend/render/capacity qualification

new semantic method claim
→ semantic development diagnostic + later protected qualification
```

The exact future matrix must be justified prospectively.

### AUDIT-017-F4 — P2: experiment lifecycle/state is not discoverable from repository structure

`experiments/` has no README/index distinguishing active reusable substrate from historical cohort runners, superseded Workspace prototypes and conditional deterministic research.

This matters because many files are executable and heavily tested. A new session can reasonably mistake historical machinery for the current selected method.

**Correction:** add one compact `experiments/README.md` lifecycle/ownership map. It should classify files/families as reusable infrastructure, conditional research, historical/dormant runners or superseded prototypes; point to canonical evidence/owners; and state that `MEMORY.md`/selected plans alone activate new experiment execution.

Do not physically move/delete historical files until references/imports are audited.

### AUDIT-017-F5 — P2: broad model/arm runners are over-specialized for reuse

The current comparison/supplied-evidence runners bind exact candidate sets, cases, roles, model profiles, GPU placement/context and freeze formats. That is good for reproducibility of their original studies and bad as an implicit general experimentation framework.

Do not “generalize” them preemptively into a large framework. Future selected experiments should reuse the smallest lower-level substrate and author a thin new bounded runner around the new hypothesis.

### AUDIT-017-F6 — RETAIN: strict evidence/reference/accounting boundaries earned real value

Typed delivered references, original response retention, exact request/render/configuration receipts, usage accounting, unknown-usage preservation, owned model cleanup and immutable freeze/evidence publication materially improved auditability and prevented false semantic acceptance.

These controls should survive future experiments, proportionately. They are not evidence the semantic method works, but they are high-value research infrastructure.

### AUDIT-017-F7 — RETAIN: negative/inconclusive outputs are useful and should remain immutable

The old Raw/Structured matrix, Fixed/Agent research, r4 and r5 are not “failed files to clean up.” They establish specific negative knowledge:

- interface qualification is weaker than real semantic adequacy;
- autonomous discovery and supplied-evidence interpretation fail in different ways;
- Agent policy can reduce observed cost and discover useful evidence without producing advice-ready output;
- strict citations do not imply entailment;
- instruction-only changes can improve some observations while creating/preserving other false premises.

Preserve these results and do not rerun them merely for prettier denominators.

### AUDIT-017-F8 — P2: multi-role decomposition deserves only a discriminating, same-evidence experiment if selected

Stage 2 correctly added bounded multi-role interpretation/validation as an option. If selected, the experiment should primarily test **responsibility decomposition**, not simultaneously change model family, retrieval universe, framework, memory system and reviewer protocol.

A credible first design would use the same frozen supplied evidence and preferably the same underlying qualified model across isolated roles, with typed handoffs and a separately judged validator contribution. Same-model agreement is not independent evidence; the value is failure localization and proposition rejection/retention behavior.

### AUDIT-017-F9 — P2: future semantic acceptance must move beyond exposed development cases

HTTPX/glyphsLib and related supplied packets have been repeatedly inspected, prompted, reviewed and used for design. They remain useful development regressions.

A materially tuned semantic method requires a frozen exact method and newly protected cases before broader transfer/reliability claims. Do not create “unseen” status by selecting another already-known S001–S016 case after reading its expected reasoning during this audit programme.

## 7. Recommended current experiment stance

Until the product-value/deep producer-consumer trace selects a residual semantic responsibility:

```text
NO NEW MODEL CALLS
NO NEW MODEL SWEEP
NO AUTONOMOUS-DISCOVERY OPTIMIZATION
NO AGENT FRAMEWORK ADOPTION
NO QUALIFICATION MATRIX FOR ITS OWN SAKE
```

Keep the reusable lab substrate and historical evidence intact.

If a semantic experiment later earns selection, use this sequence:

```text
named product question
→ simpler deterministic/native alternative rejected or insufficient
→ smallest reusable lab substrate
→ point-specific interface/deployment qualification
→ bounded exposed-case development diagnostic
→ reject/narrow/adopt-decision
→ only after material tuning: newly protected qualification
```

## 8. Immediate non-inference correction

The highest-value immediate experiment-area change is **documentation/lifecycle clarity**, not code generalization:

Create `experiments/README.md` with:

- product/experiment authority boundary;
- reusable substrate list;
- current conditional research candidates;
- historical/dormant cohort runners;
- Workspace prototype status;
- activation/requalification rules;
- links to AUDIT-011, AUDIT-014, this audit and main evidence records.

That correction can be performed without model calls or changing historical results.

## 9. Stop line

No experiment rerun or deletion follows automatically. Stage 6 should consolidate all cross-domain findings and choose the remediation order. The lifecycle index is a strong low-risk correction candidate; broader experiment code cleanup should wait until reference/import impact is checked.

## References

- `audits/2026-10-18_AUDIT-011_investigator-experiment-validity-and-progress.md`
- `audits/2026-10-20_AUDIT-014_product-value-and-evaluation-sequencing.md`
- `working-memory/evidence/2026-10-19-investigator-capability-diagnostic/README.md`
- `working-memory/evidence/2026-10-19-investigator-evidence-first-build/COMPARISON_REVIEW.md`
- research commit `cde0ea9906fa37e4184962d0ba65577e4d62396e`
- `working-memory/evidence/2026-10-07-broader-agency-contract2-comparison/README.md` at that research commit
- `experiments/investigator_run_control.py`
- `experiments/investigator_model_interface.py`
- `experiments/investigator_workspace_adapter.py`
- `experiments/investigator_workspace_trial.py`
- `experiments/investigator_supplied_evidence.py`
- `experiments/qualify_investigator_model_interface.py`
- `experiments/run_investigator_semantic_comparison.py`
- `experiments/run_investigator_supplied_evidence.py`
- `experiments/api_python_bindings.py`
- `experiments/run_workspace_migration_trial.py`

`UP-SKILL:upgradepilot-repository-audit`
