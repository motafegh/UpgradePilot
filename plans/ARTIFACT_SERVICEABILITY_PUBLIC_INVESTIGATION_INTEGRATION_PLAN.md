# Artifact Serviceability Public Investigation Integration Plan

**Status:** admitted continuation plan for the unfinished artifact-serviceability application-integration responsibility. Live selection remains owned only by `../MEMORY.md`.  
**Owner:** Ali Rajabi  
**Historical parent / provenance:** [`B2_IMPACT_APPLICABILITY_INVESTIGATION_FOUNDATION_PLAN.md`](B2_IMPACT_APPLICABILITY_INVESTIGATION_FOUNDATION_PLAN.md), especially its unfinished second-mechanism application-path responsibility.  
**Stable product authority:** [`../PROJECT_CHARTER.md`](../PROJECT_CHARTER.md)  
**Decision semantics:** [`../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md`](../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md)  
**Trust/evidence invariants:** [`../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md`](../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md)

## Responsibility

Connect the already-implemented artifact-serviceability and target artifact-environment responsibilities through the normal read-only `PublicPullRequestInvestigation` application path and human-facing output without weakening evidence boundaries or turning mechanism-specific technical state into an overall maintainer recommendation.

The intended application flow is:

```text
admitted dependency transition
+
exact old/proposed package artifact evidence
+
exact target workflow/configuration evidence where justified
↓
artifact-serviceability candidate
↓
target artifact-environment / compatibility evidence or explicit insufficiency
↓
artifact-serviceability applicability assessment
↓
PublicPullRequestInvestigation typed result
↓
human-facing explanation with proof strength preserved
```

This plan specializes the remaining application-integration work from the broad historical foundation plan. It does not reopen completed Python-support, applicability-composition, workflow-IR, target-artifact-environment, or architecture-reconciliation work unless new concrete evidence demonstrates a defect in those owners.

## Verified entry boundary

Repository evidence already establishes:

- `src/upgradepilot/impact/artifact_serviceability.py` owns target-agnostic published-wheel-loss candidate formation and target-specific applicability evaluation;
- `src/upgradepilot/target/artifact_environment.py` owns bounded interpretation of exact workflow definitions into partial target artifact-environment evidence while explicitly preserving static-configuration versus runtime-execution limits;
- focused tests exist for both responsibilities;
- `src/upgradepilot/investigation.py` currently composes the Python-support mechanism but does not yet return or orchestrate the artifact-serviceability / target-artifact-environment mechanism;
- `src/upgradepilot/cli.py` currently renders the Python-support-oriented result and does not yet explain artifact-serviceability state;
- `tests/test_investigation.py` protects sequencing, early-stop behavior, exact target identity, and unresolved-state preservation.

Therefore the next work is composition and proof, not invention of another artifact model or another orchestration framework.

## Learning-by-Doing operating loop

Every substantive slice follows the repository Learning-by-Doing method:

```text
PRE-ACTION ORIENTATION
→ understand the exact responsibility, data flow, and proof boundary needed now

REAL BOUNDED WORK
→ make the smallest coherent design / implementation / test change

ACTUAL EVIDENCE
→ inspect targeted tests, concrete result shapes, and failures

PRESERVE MATERIAL STATE
→ update the active working memory with decisions/evidence worth retaining

POST-ACTION LEARNING CLOSURE
→ explain what changed, why, what the evidence proves, and what remains unresolved

OWNERSHIP / REASONING STEP
→ Ali predicts, critiques, chooses, or explains the next important boundary when useful
```

Do not silently batch several architectural or semantic decisions into one implementation step.

## Scope and non-goals

In scope:

- additive typed result contract for artifact-serviceability-related application state;
- normal application orchestration using already-admitted provider/domain owners;
- exact evidence sequencing and explicit absent/unresolved/problem states;
- human-facing CLI/explanation of the new technical state;
- focused integration tests, nearest regressions, and final full-suite proof;
- small source-clarity refinements only where the new flow would otherwise be materially hard to understand.

Out of scope unless new evidence earns a separate responsibility:

- LangGraph/LangChain product adoption or new framework machinery;
- new planner actions added for framework richness;
- final maintainer recommendation or overall-sufficiency synthesis;
- pretending static workflow declarations prove runtime environment formation;
- inferring exact wheel tags from broad runner/Python labels without admitted evidence;
- matrix/reusable-workflow/container expansion merely to increase coverage;
- package-root facade expansion;
- redesign of already-accepted applicability semantics without a demonstrated contradiction.

## Initial design constraints

These constraints are already justified by current owners and tests:

1. **Additive integration.** Existing Python-support results and sequencing remain valid while the second mechanism is added.
2. **Mechanism-specific truth stays with its owner.** `investigation.py` coordinates; it does not reimplement wheel interpretation, workflow parsing, target-environment interpretation, or applicability semantics.
3. **Observation is not recommendation.** Artifact serviceability describes a technical candidate/assessment and its evidence strength; it must not silently change the overall dependency decision.
4. **Static evidence remains static.** A visible runner, Python setup, or installation declaration does not establish runtime execution or exact wheel compatibility.
5. **Exact identity survives composition.** Repository, pull-request head revision, dependency identity, release versions, workflow source, and target evidence must remain aligned.
6. **Absence and insufficiency stay explicit.** No candidate, unavailable evidence, insufficient evidence, and established non-applicability must not collapse into one state.
7. **No accidental facade.** Internal contracts continue to be imported from owning modules rather than expanded through the package root.

## Execution slices

### Slice 1 — result-contract and evidence-flow decision

**Know / inspect**

- `PublicPullRequestInvestigation` fields and return construction;
- artifact-serviceability candidate/assessment/result types;
- target artifact-environment result types;
- exact workflow/provider evidence already available in the normal investigation path;
- existing investigation and package-interface tests.

**Understand / decide**

- which application-level fields are required;
- which fields may legitimately be `None` and why;
- whether the application result should expose candidate state, final assessment state, target artifact-environment state, or a deliberately small combination;
- how one artifact/environment observation is associated with the exact workflow/dependency source that produced it;
- whether the first integration should surface only proposition-relevant/required artifacts or also optional states.

**Do**

- make only the smallest additive typed-contract change needed for the agreed flow;
- add contract-focused tests before broader orchestration work when they improve failure localization.

**Evidence / stop rule**

Proceed only when the result shape preserves existing callers and makes unavailable/unresolved states unambiguous. If the type shape requires a new cross-module abstraction that current owners do not justify, stop and return to design instead of inventing it in `investigation.py`.

### Slice 2 — artifact-serviceability candidate composition

**Know / inspect**

Trace the exact producer path for both old and proposed release evidence and verify which evidence is already acquired by the normal application flow.

**Understand / decide**

Determine the earliest sufficient orchestration point for building the artifact-serviceability candidate without duplicating provider acquisition or coupling it to the Python-support branch.

**Do**

- acquire/reuse the exact old/proposed release evidence required by the existing candidate builder;
- invoke the artifact-serviceability owner only when its prerequisites are established;
- preserve independent CI and Python-support branches;
- return explicit candidate/problem/no-candidate state according to the existing contract.

**Evidence / stop rule**

Focused tests must demonstrate positive candidate formation, no-candidate behavior, evidence-problem behavior, and that unrelated branch stops do not erase already-earned independent evidence.

### Slice 3 — target artifact-environment and applicability composition

**Know / inspect**

Trace exact workflow-definition acquisition, dependency source context, target artifact-environment interpretation, and the current exact target wheel-compatibility evidence boundary.

**Understand / decide**

Identify what static evidence can actually establish now and what must remain unresolved. Do not equate target artifact-environment facts with exact wheel compatibility unless an admitted owner provides that transformation.

**Adopted first-integration selection policy**

The initial application composition is intentionally evidence-gated rather than exhaustive:

```text
real ArtifactServiceabilityImpactCandidate
+
already-earned StaticDependencyConsumptionEvidence
  state == "supported"
  mechanism == "direct_requirements"
  exact source_path preserved
+
matching exact workflow definition already acquired for CI
+
matching exact DependencySourceContext
→ interpret_target_artifact_environment(...)
```

Do **not** create a workflow × dependency-source cross-product. Do **not** promote unresolved/plausible CI-consumption relationships into selected Target associations. Their uncertainty remains visible in `ci_coverage_result` instead of being strengthened by application composition.

Project-environment mechanisms such as uv/project selection also remain outside this first Target-composition gate even when CI has supported static consumption. The current Target interpreter owns direct requirements-style installation declarations, not general project-environment formation; feeding broader mechanisms into it would risk producing misleading `not_observed` Target states without establishing exact wheel compatibility.

Reuse the exact workflow definition already acquired for CI rather than re-fetching the same provider evidence. CI job identity may justify workflow/source relevance, but it does not silently extend the Target API: multi-job/reusable/otherwise unsupported Target forms remain explicit `TargetArtifactEnvironmentProblem` results under the current Target owner.

**Do**

- activate Target composition only for a real artifact-serviceability candidate;
- select only supported `direct_requirements` consumption relationships with exact source identity;
- match each selected consumption to the exact dependency source context and already-acquired workflow definition;
- deduplicate identical workflow-revision/workflow-path/dependency-source relationships before Target interpretation;
- connect exact target workflow evidence only where that candidate + supported CI relationship justifies it;
- preserve workflow/job ambiguity and unsupported forms as explicit target problems;
- preserve each result through `DependencySourceArtifactEnvironmentResult` without strengthening its proof level;
- do not synthesize `TargetWheelCompatibilityEvidence` from static Target facts;
- keep the existing artifact-serviceability applicability assessment unresolved unless a separately admitted exact target-compatibility owner supplies evidence.

**Evidence / stop rule**

Proceed only if focused tests show that: unsupported/unresolved CI relationships cannot accidentally enter Target composition; exact source/workflow/revision identity survives the join; multi-job/unsupported Target forms remain explicit problems rather than ad-hoc selections; static Target evidence cannot become runtime/exact-compatibility proof; and the existing unresolved artifact assessment is not silently strengthened.

### Slice 4 — human-facing explanation

**Know / inspect**

Trace `_print_investigation` and the existing CLI tests before changing presentation.

**Understand / decide**

Choose concise labels that distinguish at minimum:

```text
observed / established fact
candidate / proposition to evaluate
blocked / unavailable / insufficient evidence
established applicable or established not applicable
```

without inventing an overall recommendation.

**Do**

Add an additive artifact-serviceability section to the normal human-facing result, including provenance/limitations where they materially explain proof strength.

**Evidence / stop rule**

CLI tests must show that a user can tell what was observed, what remains only a candidate, what evidence is missing, and what conclusion is or is not justified.

### Slice 5 — cross-responsibility and end-to-end proof

Run validation from narrow to broad:

1. focused tests for changed contract/orchestration/presentation;
2. `tests/test_artifact_serviceability.py`;
3. `tests/test_target_artifact_environment.py`;
4. `tests/test_investigation.py`;
5. relevant CLI/package-interface and nearby integration/end-to-end tests selected from the actual diff;
6. full deterministic suite required by repository governance;
7. safe live read-only proof only if a product claim depends on network evidence and the environment permits it.

After proof, reconcile the broad historical foundation plan and `MEMORY.md` only for responsibilities whose durable/live state actually changed.

## Progressive decision checkpoints

The following are intentionally not guessed in advance and should be decided from the real source/tests during the corresponding slice:

- exact additive result field names/cardinality;
- whether target artifact-environment evidence is one selected result or a collection tied to several workflows/environments;
- how/when the old release evidence should be acquired without duplicating package-provider responsibility;
- whether current static target artifact evidence can support any exact wheel-compatibility transformation or must leave applicability unresolved;
- whether required/proposition-relevant artifacts alone are the correct first presentation boundary;
- exact CLI placement and wording.

Each decision should be recorded in the active working memory when it materially affects later implementation or proof.

## Proof obligations

The continuation is not complete unless evidence demonstrates:

- existing Python-support investigation behavior remains intact;
- artifact-serviceability candidate creation uses exact old/proposed release evidence and preserves dependency/revision identity;
- no-candidate, evidence-problem, unresolved, applicable, and not-applicable states remain distinguishable where their owners support them;
- target workflow interpretation does not manufacture runtime execution or exact wheel compatibility;
- application orchestration does not duplicate domain/provider logic;
- independent evidence branches remain independently preserved across later stops;
- human-facing output communicates proof strength without manufacturing a maintainer recommendation;
- focused and full deterministic regression suites pass after executable changes.

## Completion / stop line

Stop this plan when:

```text
artifact-serviceability + target-artifact-environment existing owners
→ coherently composed through PublicPullRequestInvestigation
→ additive typed state exposed
→ human-facing explanation exposes proof strength
→ focused + nearest + full deterministic proof passes
→ no unresolved architecture contradiction remains inside this integration responsibility
```

Then identify the concrete next product question. Do not automatically deepen artifact-serviceability, add more mechanisms, or restart framework experimentation merely because this integration is complete.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-planning-design`