# Increment 5 — Runtime Dependency-State Application Integration — Learning-by-Doing Cycle

**Date:** 2026-09-30  
**Cycle status:** ACTIVE — A0/A1 DONE; STOP before A2; B/Verification/D/E NOT STARTED; C CONTINUOUS  
**Primary responsibility:** carry the already-verified command-derived runtime dependency-state evidence through the normal public-PR investigation path as a separate typed application result, without changing CI-coverage, later-use, compatibility, or maintainer-action semantics  
**Controlling plan:** `plans/RUNTIME_DEPENDENCY_STATE_PROOF_COMPLETION_PLAN.md`  
**Accepted architecture:** `docs/architecture/ADR-0010-package-manager-semantic-facts-and-runtime-dependency-state-composition.md`  
**Previous cycle:** `working-memory/2026-09-29_2130_increment-4_command-derived-requirement-state-composition_lbd-cycle.md`  
**A0 start head:** `e956c6d7f1fb1887d47fdb68d0b0ea5c0969ffc4`

## Cycle progression

```text
A0 — DONE: current main/governance/source/test state reconciled and cycle initialized
A1 — DONE: continuity from Increments 1–4 and the current application seam onboarded
STOP — CURRENT: do not enter A2 until deliberately continued
A2 — NOT STARTED: orient and decide the exact application-level integration/result shape
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


## Current STOP boundary

A0 and A1 are complete.

Do **not** start A2 design or Build yet.

The next deliberate continuation is:

```text
A2 — orient the exact application integration responsibility
→ trace current investigation data flow against the Increment-4 composer inputs
→ decide result cardinality/aggregation and integration ownership
→ define focused proof/close-defeater cases
→ STOP before Build
```

No source/test modification is authorized by this A0/A1 closure.

## C — continuous preservation

C currently preserves:

- exact cycle start head and verified predecessor;
- source/test drift check;
- live-owner agreement;
- current application data-flow seam;
- existing semantic/proof boundaries;
- explicit A2 questions rather than premature implementation decisions;
- canonical STOP before A2;
- complete research provenance now present on `main` without becoming a live owner;
- explicit research-derived A2 constraints and references, without importing future-scope experiments.
