# Increment 4 — Command-Derived Requirement-State Composition — Learning-by-Doing Cycle

**Date:** 2026-09-29  
**Cycle status:** ACTIVE — A0 DONE; A1 CURRENT; A2/B/Verification/D/E PENDING; C CONTINUOUS  
**Primary responsibility:** compose already-established dependency/source applicability, package-manager semantic facts, and exact successful command execution into one bounded per-command requirement-state witness without changing CI-coverage, later-use, compatibility, or maintainer-action meaning  
**Controlling plan:** `plans/RUNTIME_DEPENDENCY_STATE_PROOF_COMPLETION_PLAN.md`  
**Accepted architecture:** `docs/architecture/ADR-0010-package-manager-semantic-facts-and-runtime-dependency-state-composition.md`  
**Broader R4 sequence:** `working-memory/2026-09-27_runtime-dependency-state-proof-implementation-and-verification-planning.md`

## Cycle status

```text
A0 — DONE: current main/live owners/source/test seams reconciled; no route contradiction
A1 — CURRENT: continuity/recent-work onboarding; awaiting Ali's challenge/question/confirmation at the onboarding gate
A2 — PENDING
B — PENDING
Verification gate — PENDING
D — PENDING
E — PENDING
C — CONTINUOUS: preserve meaningful engineering + learning progression across A0→E
```

## A0 — current-state reconciliation + cycle initialization — DONE

### Exact repository state

A0 started from canonical `main` at:

```text
0148b057dfe09a6b1792062a0e38e7a19aefc397
reconcile completed R4 increment ownership
```

The last hosted Increment-3 implementation proof remains Product verification #14 on exact implementation head:

```text
29247346d1c1e3ea7074ffd7daf9c53d8c3beeda
focused investigation composition: 15/15
full deterministic product regression: 699/699
conclusion: GREEN
```

Comparison from that verified head to current `main` shows 15 later commits changing only:

- `MEMORY.md`;
- `README.md`;
- `plans/RUNTIME_DEPENDENCY_STATE_PROOF_COMPLETION_PLAN.md`;
- the R4 implementation-sequence working memory;
- the closed Increment-3 cycle record.

No `src/` or `tests/` file changed after the verified Increment-3 implementation head. Therefore the current implementation surface remains the hosted-verified Increment-3 source/test state while the later commits reconcile documentation and ownership.

### Live-owner reconciliation

The relevant owners agree:

- `MEMORY.md`: Increment 3 is closed; Increment 4 is selected next.
- runtime dependency-state plan: Increments 1–3 are implemented/verified/learned/closed; Increment 4 is command-derived requirement-state composition; application integration is later Increment 5.
- ADR-0010: runtime dependency-state proof must remain separate from existing CI coverage/exercise evidence and must preserve explicit unresolved/not-established problems.
- R4 sequence: execution evidence → package-manager declaration → effective semantic facts → requirement-state composer → later application integration.

No current evidence invalidates or changes the selected Increment-4 responsibility.

### Current source seams available to Increment 4

The required upstream evidence already exists as separate owners:

1. **Exact dependency transition/source provenance**
   - `dependency/change.py`
   - `DependencyVersionChange`
   - `DependencyChangeSourceEvidence`

2. **Supported exact static dependency consumption**
   - `ci/consumption.py`
   - `StaticDependencyConsumptionEvidence`
   - direct-requirements and project-environment mechanisms remain separately represented.

3. **Static package-manager operation identity**
   - `dependency/package_manager_operation.py`
   - `PackageManagerOperationDeclaration`
   - one parsed operation preserves exact `StaticCommandLocation`.

4. **Independent effective semantic facts**
   - `dependency/package_manager_semantics.py`
   - `ManagerEnvironmentSelectionFact`
   - `InstallationDestinationFact`
   - `PackageMutationModeFact`
   - `DirectRequirementHandlingFact`
   - each fact preserves the same exact command location plus bounded provenance.

5. **Exact successful command execution**
   - `ci/runtime_execution.py`
   - `ExactCommandExecutionAssessment`
   - exact command execution remains distinct from successful user-step execution.

The intended Increment-4 module `src/upgradepilot/ci/dependency_state.py` does not exist yet. That is expected and confirms the selected composer responsibility has not been implemented prematurely.

### Existing proof seams

Current tests already protect the ingredients independently:

- `tests/test_package_manager_semantics.py` — package-manager operation identity and semantic facts;
- `tests/test_package_manager_route_a_semantic_fixture.py` — one controlled Route-A fixture closes all four semantic facts while an ordinary-looking command remains unresolved;
- `tests/test_ci_runtime_execution.py` — exact command execution versus step execution and structural/continue-on-error/non-success boundaries;
- existing direct-install/CI-consumption tests protect static source-consumption meaning.

The plan's mention of `tests/test_runtime_dependency_contract.py` is only appropriate if an Increment-4 assertion genuinely belongs to that file's current dependency-version-bound responsibility. A dedicated focused dependency-state composer test module is likely the cleaner default; A2/B must decide from responsibility rather than filename convenience.

### A0 architectural observation

Increment 4 should begin as **composition of already-owned evidence**, not as another parser/environment/config subsystem.

The important join key already exists across the relevant command-scoped inputs: exact static command identity via `StaticCommandLocation`, with workflow/job/step identity carried by CI consumption/execution evidence.

The first design question is therefore not “what more environment state should we reconstruct?” but:

```text
when do these already-established propositions refer to the same exact dependency/source/command/runtime scope,
and when is their combined evidence sufficient to emit the bounded command-completion witness?
```

No new Increment-3-style environment producer is justified by A0 evidence.

### A0 non-goals preserved

Increment 4 must not silently establish:

- fresh-install causality;
- wheel/sdist or artifact identity;
- state persistence after command completion;
- later behavior/package exercise;
- compatibility;
- maintainer-action permission;
- generic job-log/stdout/artifact acquisition;
- application-level investigation integration (later Increment 5).

### A-phase orientation / learning map

#### A1 continuity topics
- what Increment 1 established: reusable exact-command execution evidence;
- what Increment 2 established: shared package-manager declaration + independent semantic dimensions;
- what Increment 3 added: enough bounded environment/config/executable evidence to close those semantic facts for one Route-A family;
- why none of those facts alone yet means the proposed dependency requirement is satisfied;
- why Increment 4 is the missing proof-composition edge rather than another evidence-producer increment.

#### A2 upcoming-responsibility topics
- exact proposition represented by `RequirementSatisfiedAtCommandCompletion`;
- distinction between **supported witness**, **not established**, and **unresolved**;
- identity alignment across dependency source, static consumption, semantic facts, and runtime execution;
- required positive premises for the first requirements-file/pip family;
- close-defeaters: dry-run, retargeting/exclusion, unresolved semantic source, non-success, command identity mismatch, multiple command candidates;
- witness provenance and limitations;
- likely focused source/test ownership;
- acceptance boundary and explicit non-goals.

#### Ownership depth
A2 should emphasize two engineering ownership points:
1. deciding when heterogeneous evidence may be joined as one proposition;
2. preserving the difference between absence/not-established and unresolved evidence when a join premise fails.

### A0 conclusion

A0 is complete.

No contradiction, stale live owner, implementation drift, or proof result requires replanning Increment 4. The cycle proceeds to A1 and must stop at the continuity/onboarding gate before A2.
