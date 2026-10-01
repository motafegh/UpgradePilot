# Increment 5 — Runtime Dependency-State Application Integration — Learning-by-Doing Cycle

**Date:** 2026-09-30  
**Cycle status:** ACTIVE — A0/A1/A2 DONE; STOP before Build; B/Verification/D/E NOT STARTED; C CONTINUOUS  
**Primary responsibility:** carry the already-verified command-derived runtime dependency-state evidence through the normal public-PR investigation path as a separate typed application result, without changing CI-coverage, later-use, compatibility, or maintainer-action semantics  
**Controlling plan:** `plans/RUNTIME_DEPENDENCY_STATE_PROOF_COMPLETION_PLAN.md`  
**Accepted architecture:** `docs/architecture/ADR-0010-package-manager-semantic-facts-and-runtime-dependency-state-composition.md`  
**Previous cycle:** `working-memory/2026-09-29_2130_increment-4_command-derived-requirement-state-composition_lbd-cycle.md`  
**A0 start head:** `e956c6d7f1fb1887d47fdb68d0b0ea5c0969ffc4`

## Cycle progression

```text
A0 — DONE: current main/governance/source/test state reconciled and cycle initialized
A1 — DONE: continuity from Increments 1–4 and the current application seam onboarded
A2 — DONE: technical design prepared and learning/ownership gate cleared
STOP — CURRENT: do not enter Build until deliberately continued
B — NOT STARTED
Verification — NOT STARTED
D — NOT STARTED
E — NOT STARTED
C — CONTINUOUS: preserve meaningful engineering and learning progression across A0→E
```

## A0 — current-state reconciliation + cycle initialization — DONE

### Exact entry state

Current `main` at cycle start:

```text
e956c6d7f1fb1887d47fdb68d0b0ea5c0969ffc4
clarify historical A0 status in closed Increment 4 cycle
```

Increment 4 remains closed against Product verification #15:

```text
verified implementation head: c9edc76e8c3f4e9bb9d58e27ddac3cfbc291a8be
workflow run: 36717618416
focused investigation composition: 15/15
deterministic product regression: 708/708
```

Comparison from the verified implementation head `c9edc76e...` to the A0 start head `e956c6d...` shows 16 later commits changing only:

- `MEMORY.md`;
- `plans/RUNTIME_DEPENDENCY_STATE_PROOF_COMPLETION_PLAN.md`;
- `working-memory/2026-09-27_runtime-dependency-state-proof-implementation-and-verification-planning.md`;
- `working-memory/2026-09-29_2130_increment-4_command-derived-requirement-state-composition_lbd-cycle.md`.

No `src/` or `tests/` files changed after the hosted-verified Increment-4 implementation head. Therefore the application cycle begins from the exact verified Increment-4 implementation surface plus documentation/live-owner reconciliation.

### Live-owner agreement

The controlling owners agree on the next responsibility:

- `MEMORY.md`: Increment 5 application integration is next and had not started before this cycle;
- runtime dependency-state plan: the implementation sequence reaches application integration only after the command-derived state composer;
- ADR-0010: runtime dependency-state proof remains separate from `DependencyCICoverageResult` and application orchestration will eventually carry an additional typed dependency-state result;
- R4 implementation-sequence record: expected application owner is `src/upgradepilot/investigation.py`, with proof in `tests/test_investigation.py` and `tests/test_r6_investigation_ci_integration.py`; no maintainer-action expansion belongs in this increment.

No current evidence justifies a Smart Situational Override, broader re-plan, or reopening Increment 4.

### Current implementation seam

The relevant current normal path is:

```text
DependencyChangeAnalysis
→ exact workflow runs/jobs
→ exact workflow definitions + project-environment sources
→ WorkflowDependencyCoverageInput[]
→ evaluate_dependency_ci_coverage(...)
→ PublicPullRequestInvestigation.ci_coverage_result
```

Current `PublicPullRequestInvestigation` has `ci_coverage_result` but no runtime dependency-state field.

`src/upgradepilot/ci/dependency_state.py` already owns the verified per-command composition:

```text
DependencyVersionChange
+ exact RequirementsFileDependencyContext
+ supported StaticDependencyConsumptionEvidence
+ ScopedPackageManagerSemanticEvidence
+ ExactCommandExecutionAssessment
→ RequirementSatisfiedAtCommandCompletion
  OR RequirementStateProblem
```

Therefore Increment 5 begins as **application composition/integration**, not a new parser, package-manager semantic subsystem, runtime-correlation subsystem, or maintainer-action change.

### Existing proof seams

Primary application proof owners already exist:

- `tests/test_investigation.py` — application sequencing and typed investigation results;
- `tests/test_r6_investigation_ci_integration.py` — normal public-PR CI orchestration from acquired exact sources;
- `tests/test_ci_dependency_state.py` — focused composer and real-producer Route-A proof from Increment 4.

The current R6 case is uv/project-environment based and must not be silently converted into positive pip/direct-requirements Route-A state evidence. It remains useful as a close boundary case for preserving existing meaning.

### A0 boundary

A0 does **not** decide the detailed integration design. In particular it leaves these for A2:

1. exact application-level result/aggregate shape when several command/environment candidates exist;
2. the earliest sufficient integration owner/helper so `investigation.py` remains orchestration rather than duplicating parser/environment/pip semantics;
3. whether existing coverage/runtime-correlation outputs can be reused safely or whether a bounded parallel composition helper is required;
4. how unsupported families such as the current uv/project-environment path are represented without broadening Increment-4 semantics;
5. whether presentation/JSON should remain unchanged in this increment.

## A1 — continuity / recent-work onboarding — DONE

### What the previous increments established

```text
Increment 1
reusable exact command-execution evidence
        ↓
Increment 2
shared package-manager operation declaration
+ first dependency-owned semantic resolution
        ↓
Increment 3
bounded executable / process-env / config evidence
+ four independent effective semantic facts
        ↓
Increment 4
cross-layer per-command composition
→ RequirementSatisfiedAtCommandCompletion
        ↓
Increment 5
make the normal application path actually carry that result
```

The important distinction is that Increment 5 is **not proving a new proposition**. The proposition and its proof boundary already exist and are hosted-verified. Increment 5 makes that evidence reachable through the normal product orchestration.

### Existing meanings that must remain unchanged

`DependencyCICoverageResult` continues to mean bounded static dependency consumption/direct exercise plus runtime strengthening. It does **not** become package-state evidence.

`RequirementSatisfiedAtCommandCompletion` continues to establish only the exact proposed direct requirement in the resolved package-state scope at the exact successful command-completion boundary.

It still does **not** establish:

- fresh-install causality;
- artifact identity;
- persistence after command completion;
- later dependency use;
- affected-behavior exercise;
- behavioral compatibility;
- maintainer-action permission.

### Why application integration matters

Before Increment 5:

```text
normal investigation
→ can produce CI coverage
→ cannot yet return the new runtime dependency-state proof
```

After a successful Increment 5:

```text
normal investigation
→ retains existing CI coverage
→ also carries bounded runtime dependency-state evidence
→ downstream work may consume it later under its own responsibility
```

This is the missing bridge between the verified internal proof capability and the normal product flow.

### Learning focus for A2

Before Build, Ali should be able to reason about:

- why application orchestration should compose/reuse existing evidence rather than own pip semantics;
- why package-state evidence must remain separate from CI coverage;
- why multiple per-command results must not be collapsed into a stronger global claim without an explicit aggregation contract;
- why a uv/project-environment result cannot inherit the first pip/direct-requirements Route-A witness;
- what exact data is already available in `investigation.py` and what additional composition seam is genuinely needed.

## Research corpus integration at the A1 STOP — RECORDED

### Full research provenance now on main

The complete parallel architecture-research branch `analysis/ai-agentic-capability-map-2026-09-28` was deliberately merged into `main` through PR #33 at merge commit `d4b79bf1bb4ee779c2dfe9732086a126786af0f1`.

The merge preserved the full 55-commit branch history and all 17 branch-only research/proposal artifacts. The PR itself contained only research/planning/working-memory documentation: 17 files, 19,366 additions, 0 deletions, and no `src/` or `tests/` changes.

This deliberately overrides the dated research branch's earlier recommendation to integrate only a distilled subset. The reason is record preservation: the complete research corpus is useful as durable project evidence and future reference. This integration-mechanism override does **not** change product architecture, proof truth, the current Increment-5 responsibility, or any live owner.

All imported dated research documents remain **non-controlling research provenance**. Statements inside them such as "current main is Increment 4" or "do not merge this branch yet" describe the historical research-time state and must not override current `MEMORY.md`, the active cycle, accepted ADRs, or controlling plans.

### Research artifacts relevant to Increment-5 A2

A2 should use the following main-branch research records as explicit design evidence without importing their unrelated future scope:

- `proposals/2026-09-29_UPGRADEPILOT_EVIDENCE_AI_ARCHITECTURE_PROPOSAL.md`
  - Sections 8–9: keep CI/workflow/runtime evidence classes distinct and preserve the deterministic package-manager/runtime-state chain;
  - Section 27: keep Increment 4 → Increment 5 sequencing intact;
  - Sections 28–31: advanced methods remain experiment-gated and the proposal is synthesis/provenance rather than a live-plan replacement.
- `working-memory/2026-09-29_step3_whole-pipeline-architecture-map.md`
  - Stage 7: application integration carries the command-completion requirement-state result through the normal path;
  - current implementation overlay / responsibility map: package-state application integration is a distinct responsibility;
  - the witness must preserve exact identity, provenance, observation boundary, and claim limitations for later consumers.
- `working-memory/2026-09-29_step4_existing-ai-agent-work-reconciliation.md`
  - Increment 5 has no model requirement;
  - the package-state witness should first enter the ordinary application/evidence flow before any later AI responsibility is activated.
- `working-memory/2026-09-29_step5_architecture-decisions-experiment-queue-and-integration-strategy.md`
  - no change to Increment-4/5 sequencing;
  - advanced methods must be admitted responsibility-by-responsibility against a baseline and observed limitation;
  - AI responsibilities and authority remain separated.
- `working-memory/2026-09-29_step2c_adversarial-track-a-vs-track-b-comparison.md`
  - command-derived package state remains separate from CI coverage;
  - command-completion state remains separate from later use, compatibility, and action permission;
  - broader workflow/runtime/AI alternatives are experiment triggers, not automatic additions.

The Tier-1 reports, independent candidate architecture, external-research discovery, and technology/learning ledger are now also available on `main` as deeper provenance. They need not be read during A2 unless a concrete design question reaches their responsibility.

### Research-derived constraints carried into A2

The active cycle will use the research to constrain A2 as follows:

1. **Increment 5 remains deterministic application integration.** No AI/LLM/agent/framework is required for this responsibility.
2. **Runtime dependency-state evidence remains separate from `DependencyCICoverageResult`.** Integration must not strengthen or redefine CI coverage.
3. **Preserve exact command/environment identity, provenance, command-completion boundary, and claim limitations.**
4. **Preserve per-command cardinality.** Multiple witnesses/problems must not be collapsed into a stronger repository- or workflow-level claim without an explicit aggregation contract.
5. **Keep application orchestration above lower-layer semantics.** `investigation.py` should compose/reuse evidence rather than become a pip/environment semantic owner; A2 still decides the earliest sufficient integration helper/owner.
6. **Leave room for future independent evidence mechanisms without conflation.** A later direct target-owned package-state observation may coexist with command-derived inference, but the two must retain their evidence mechanism and strength rather than becoming a generic boolean.
7. **Unsupported families remain unsupported/unresolved according to current contracts.** The current uv/project-environment path does not inherit the first pip/direct-requirements Route-A witness.
8. **Do not add later meanings.** No later-use, behavior/exercise, compatibility, action-permission, CodeQL, runtime telemetry, graph, broad-discovery, or maintainer-synthesis scope enters this increment.

These are **A2 inputs**, not A2 decisions. Exact result type/cardinality container, helper ownership, reuse strategy, and proof cases remain to be worked through deliberately in A2.


## A2 — exact application integration responsibility orientation — DONE

**A2 orientation head:** `5ac1e15f670099434c43b4b200b7e36dcb86eea8`

A2 traced the current normal application path against the exact Increment-4 composer inputs and prepared the recommended Build contract below. The learning/ownership gate is now cleared after active reasoning through responsibility, evidence, ownership, failure, and proof boundaries. No source/test modification was made in A2.

### 1. Current data-flow truth

The normal investigation already acquires the evidence needed for this increment:

```text
investigate_public_pull_request(...)
        │
        ├─ DependencyVersionChange + source_contexts
        │
        ├─ WorkflowDependencyCoverageInput[]
        │      ├─ exact WorkflowRun
        │      ├─ exact WorkflowJob[]
        │      ├─ exact workflow definition
        │      └─ project-environment sources
        │
        └─ evaluate_dependency_ci_coverage(...)
               │
               └─ DependencyCICoverageResult
                      └─ per workflow
                           ├─ consumptions[]
                           ├─ runtime_correlation
                           └─ existing CI-coverage classification
```

Increment 5 does **not** need a new external evidence acquisition path.

For the first direct-requirements/pip Route-A family, the new application integration can reuse:

- exact dependency/source contexts from dependency analysis;
- exact workflow definitions from `WorkflowDependencyCoverageInput`;
- already-derived static dependency consumptions from `WorkflowDependencyCoverageResult.consumptions`;
- already-derived `WorkflowRuntimeCorrelationResult` from the same workflow result;
- existing workflow command parsing, package-manager operation parsing, exact-process environment/config producers, semantic resolvers, exact-command execution assessment, and the Increment-4 composer.

### 2. Do not recompute CI coverage evidence

A2 rejects a design that independently calls:

- `inspect_workflow_dependency_evidence(...)` again for dependency consumption; or
- `correlate_workflow_runtime(...)` again for runtime identity.

Those results already exist in `DependencyCICoverageResult`.

The integration should reuse them and only perform the additional command-local work that CI coverage does not currently retain: locate the exact existing command occurrence in the exact workflow definition and derive the package-manager semantic inputs needed by the Increment-4 composer.

Re-parsing the exact workflow definition as provider syntax for this command-local semantic derivation is acceptable in the first Build slice because the current coverage result does not expose a reusable parsed workflow object. A2 does **not** authorize a broader refactor merely to avoid that bounded parse.

### 3. Selected ownership

A2 selects the following owner split:

```text
src/upgradepilot/investigation.py
    application orchestration only
    → invokes the dependency-state evaluator
    → carries its typed result

src/upgradepilot/ci/dependency_state.py
    CI-level runtime dependency-state evaluation/composition
    → reuses existing CI coverage consumptions + runtime correlation
    → binds exact workflow/job/step/command identity
    → invokes dependency-owned package-manager semantic producers
    → invokes exact-command execution assessment
    → invokes Increment-4 composer

existing dependency/github/ci modules
    keep their current semantic/provider/runtime responsibilities
```

No pip, process-environment, persistent-config, shell-parser, or GitHub runtime semantics move into `investigation.py`.

A separate new module is not required unless Build exposes a concrete cohesion problem. The existing `ci/dependency_state.py` already owns this exact CI-level proposition and is the narrowest coherent home for the evaluator that produces it from admitted evidence.

### 4. Selected application result shape

A2 rejects a single aggregate boolean/state such as:

```text
runtime_dependency_state = established
```

because several distinct commands/environments may exist and Increment 4 explicitly proves that they must remain separate.

The selected Build shape is conceptually:

```python
CommandRequirementStateAssessment
    consumption: StaticDependencyConsumptionEvidence
    result:
        RequirementSatisfiedAtCommandCompletion
        | RequirementStateProblem

RuntimeDependencyStateResult
    evaluation_state:
        "evaluated"
        | "no_admitted_candidate"
    reason: str
    detail: str
    assessments: tuple[CommandRequirementStateAssessment, ...]
```

The exact spelling may change during Build only if implementation evidence shows a clearer equally bounded name; the semantic contract must not change silently.

Important meanings:

- `evaluation_state` describes whether the first admitted Route-A family produced command candidates; it is **not** an aggregate package-state conclusion.
- `assessments` preserves every admitted exact command separately.
- each assessment retains the original `StaticDependencyConsumptionEvidence`, so even a `RequirementStateProblem` remains tied to exact workflow/revision/job/step/command provenance.
- positive witnesses retain their existing observation boundary and limitations.
- `no_admitted_candidate` means no command entered this first proof family. It must **not** be interpreted as dependency absent, CI failure, unresolved compatibility, or success.

### 5. Selected PublicPullRequestInvestigation contract

Add one separate field conceptually equivalent to:

```python
runtime_dependency_state_result: RuntimeDependencyStateResult | None
```

Meaning:

- `None` — dependency transition/source analysis itself did not establish a `DependencyVersionChange`, so this downstream responsibility was inactive;
- `RuntimeDependencyStateResult(evaluation_state="no_admitted_candidate", ...)` — dependency analysis succeeded, but no command entered the first direct-requirements/pip Route-A state-proof family;
- `RuntimeDependencyStateResult(evaluation_state="evaluated", assessments=(...))` — one or more per-command state assessments exist.

This field sits **alongside** `ci_coverage_result`. Neither derives its semantic meaning from the other.

### 6. Candidate and composition policy

The first Build slice evaluates only existing static consumptions that are:

- `state == "supported"`;
- `mechanism == "direct_requirements"`;
- bound to one exact `RequirementsFileDependencyContext`;
- bound to the exact workflow definition/revision retained by the corresponding coverage input.

This is intentionally narrower than “all workflow commands”.

For each candidate, Build should:

1. verify coverage-result/input one-to-one workflow identity;
2. map the consumption to exactly one trusted requirements source context;
3. parse the exact workflow definition and locate the exact job, run step, and command occurrence by the already-retained command identity;
4. parse the existing package-manager operation declaration for that occurrence;
5. derive only the currently admitted semantic evidence sources required by the first Route-A family;
6. bind those facts using an independently supplied `ExactCICommandIdentity`;
7. reuse the existing workflow's `runtime_correlation` to call `assess_exact_command_execution(...)`;
8. call `compose_requirement_satisfied_at_command_completion(...)`;
9. retain the command assessment without collapsing it with other commands.

Internal contradictions in already-related application objects—such as mismatched workflow path/revision/order—are invariant failures and should fail loudly rather than be disguised as domain uncertainty.

Evidence limitations—dynamic command semantics, unresolved env/config, dry-run, retargeting, runtime non-success, unsupported command semantics—remain typed `RequirementStateProblem` outcomes where the existing contracts permit.

### 7. Reuse boundary

A2 explicitly chooses:

```text
REUSE
- DependencyCICoverageResult.workflows[*].consumptions
- WorkflowDependencyCoverageResult.runtime_correlation
- WorkflowDependencyCoverageInput.definition
- source_contexts
- existing semantic/runtime/composer functions

DO NOT RE-RUN
- dependency-consumption discovery
- CI coverage classification
- workflow/runtime correlation

DO NOT ADD
- new GitHub/log/runtime acquisition
- direct package-state telemetry
- broad uv package-state semantics
- AI/LLM/agent logic
```

This is the smallest architecture-preserving integration seam without making `investigation.py` a semantic engine or refactoring the already-verified CI-coverage subsystem.

### 8. Unsupported-family behavior

The current uv/project-environment R6 path remains a boundary/control case.

It may still produce its existing `ci_coverage_result`, but the first runtime dependency-state evaluator must return a non-claiming `no_admitted_candidate` result rather than manufacturing a pip/direct-requirements witness or reclassifying uv coverage as package state.

This preserves:

```text
project_environment consumption
!=
first direct_requirements/pip command-completion package-state proof
```

### 9. Presentation and action boundary

A2 selects **no presentation/JSON change by default** in this increment.

The typed application result is the required integration contract. Presentation should change only if Build discovers a current external contract that necessarily serializes every `PublicPullRequestInvestigation` field.

No maintainer-action code should consume the new result in this increment.

### 10. Focused Build proof matrix

Build must prove at least:

1. **positive Route-A normal application path**  
   exact requirements source + admitted pip semantics + exact successful command execution produces one carried `RequirementSatisfiedAtCommandCompletion`;

2. **semantic close-defeater**  
   dry-run / retargeting / unresolved ambient-config evidence produces the corresponding per-command `RequirementStateProblem`, not a positive witness;

3. **runtime close-defeater**  
   supported static consumption with exact-command execution not established/unresolved preserves the problem;

4. **multiple-command cardinality**  
   two admitted command candidates remain two distinct assessments with independent identities/environments;

5. **unsupported-family control**  
   current uv/project-environment integration keeps its existing CI result and receives `no_admitted_candidate`, with no pip-state inference;

6. **inactive dependency branch**  
   `DependencyChangeProblem` keeps runtime dependency-state integration inactive (`None`);

7. **existing semantics preserved**  
   current `ci_coverage_result`, artifact-environment behavior, upstream analysis, and maintainer-action meanings do not change.

Primary proof owners remain:

- `tests/test_investigation.py`;
- `tests/test_r6_investigation_ci_integration.py`;
- focused `tests/test_ci_dependency_state.py` additions only where the new evaluator itself needs unit proof.

### 11. A2 learning model

The key architecture to own before Build is:

```text
CI coverage asks:
"Did CI statically consume/exercise this dependency, and can that declaration be
strengthened by runtime correlation?"

Runtime dependency-state asks:
"For this exact admitted command, do source applicability + effective package-manager
semantics + exact successful execution establish the proposed requirement at command
completion?"

Application integration asks:
"Can the normal product path carry those per-command results without changing either
question's meaning?"
```

A2's answer is **yes**, by composing/reusing existing evidence through a dedicated typed evaluator/result rather than merging the responsibilities.


## A2 learning / ownership progression — CLEARED

### Ownership check 1 — per-command cardinality

Ali correctly reasoned that collapsing multiple command outcomes into one aggregate `"established"` state would hide command-specific problems and could incorrectly make the whole investigation look proven merely because one command established the proposition. Keeping separate assessments preserves the exact environment/command identity and allows one positive result to coexist truthfully with another unresolved/problem result.

### Ownership check 2 — reuse vs re-derivation

Ali correctly identified the architectural value of assigning responsibilities to their proper layers and exposing reusable evidence to downstream consumers instead of letting each consumer independently reconstruct its own version of the same fact. This reduces redundancy, improves debugging/traceability, and prevents divergent internal interpretations or identity mismatches.

Refinement: the governing idea is not limited to the provider layer. Each proposition should be produced at its **earliest sufficient owner**—provider, dependency, CI, or application as appropriate—and later layers should reuse or compose that result unless they have an independently justified stronger/different proposition to establish.

### Ownership check 3 — unsupported family vs unresolved evidence

Ali correctly distinguished a known scope boundary from genuine uncertainty. The current uv/project-environment path can be understood well enough to say that it is **outside the first admitted direct-requirements/pip Route-A package-state family**. Therefore representing it as a per-command `unresolved` problem would be misleading: `unresolved` is reserved for a candidate that entered the admitted proof family but whose required evidence could not be resolved. The aggregate-level `no_admitted_candidate` state truthfully says that no command entered this evaluator's current proof family.

### Ownership check 4 — evidence mechanism and provenance

Ali correctly identified that later direct runtime package observation must retain its provenance and must not overwrite or retroactively strengthen unrelated command-derived evidence. Refinement: two different mechanisms may eventually support a similar higher-level proposition such as package presence at a particular observation boundary, but they must remain distinguishable as evidence mechanisms with their own identity, provenance, timing/observation boundary, and limitations. A direct `importlib.metadata.version(...)` observation may establish package presence at its own observation point; it does not prove that a prior install command caused that state, nor does it turn the command-derived witness into direct observation.

### Ownership check 5 — application orchestration boundary

Ali correctly reasoned that `investigation.py` is the proper place to **carry/orchestrate** the runtime dependency-state result because it coordinates the product's normal investigation flow, while the detailed semantic derivation remains in the owner that defines that proposition. This preserves thin application orchestration and prevents pip/environment semantics from leaking upward.


### Ownership check 6 — final failure/proof-state gate — CLEARED

Ali correctly classified the final three cases:

- a definitely effective dry-run command that executes successfully yields `not_established`, because package-state mutation is positively defeated;
- an admitted pip/direct-requirements command whose effective dry-run state remains materially unknown yields `unresolved`, with the blocking reason/provenance preserved;
- a supported uv project-environment consumption remains valid CI-coverage evidence but is outside the first pip/direct-requirements package-state family, so the runtime dependency-state aggregate reports `no_admitted_candidate`.

This clears the pre-B understanding gate and demonstrates the required distinction:

```text
outside current proof family
!= unresolved inside the family
!= positively not established
!= positive witness
```

## Current STOP boundary

A0, A1, and A2 are complete. The A2 learning/ownership gate is cleared.

Do **not** start Build yet.

The next deliberate continuation is:

```text
B — implement the bounded application integration contract selected in A2
→ add typed dependency-state evaluation/result composition
→ carry it through PublicPullRequestInvestigation
→ add focused/integration close-defeater proof
→ stop at the Verification gate
```

No source/test modification was made by A2 itself.

## C — continuous preservation

C currently preserves:

- exact cycle start head and verified predecessor;
- source/test drift check;
- live-owner agreement;
- current application data-flow seam;
- existing semantic/proof boundaries;
- A2-recommended typed result/cardinality contract and integration ownership;
- reuse of existing CI consumptions/runtime correlation without semantic collapse;
- evidence that the A2 learning/ownership gate was actively cleared through reasoning checks;
- canonical STOP before Build;
- complete research provenance now present on `main` without becoming a live owner;
- explicit research-derived A2 constraints and references, without importing future-scope experiments.
