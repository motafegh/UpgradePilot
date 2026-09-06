# Artifact Serviceability Public Investigation Integration — Working Memory

**Date:** 2026-09-06  
**Session state:** ACTIVE execution/reasoning record. `../MEMORY.md` remains the sole owner of live project position.  
**Selected bounded plan:** [`../plans/ARTIFACT_SERVICEABILITY_PUBLIC_INVESTIGATION_INTEGRATION_PLAN.md`](../plans/ARTIFACT_SERVICEABILITY_PUBLIC_INVESTIGATION_INTEGRATION_PLAN.md)

## Session objective

Continue UpgradePilot from the framework-experiment closure by completing the unfinished artifact-serviceability application-integration responsibility through the normal `PublicPullRequestInvestigation` path, using the repository Learning-by-Doing method and progressively preserving decisions/evidence as the work proceeds.

This session begins with planning/design only. Product implementation has not yet been changed.

## Verified starting state

Re-entry inspection established:

1. `main` was at the framework-experiment closure boundary before this planning update; the framework package is intentionally deferred rather than the next product target.
2. The broad historical impact/applicability foundation plan already names the unfinished second-mechanism application-path responsibility, but its coordinate-heavy identity is no longer appropriate for live navigation and its scope is wider than the exact continuation now needed.
3. A new semantic bounded continuation plan now owns only the artifact-serviceability public-investigation integration responsibility.
4. `src/upgradepilot/impact/artifact_serviceability.py` already owns:
   - exact old/proposed wheel-inventory interpretation;
   - published-wheel-serviceability candidate formation;
   - explicit target wheel-compatibility evidence/problem contracts;
   - candidate applicability evaluation.
5. `src/upgradepilot/target/artifact_environment.py` already owns bounded exact-workflow interpretation into target artifact-environment facts while explicitly preserving static-configuration versus runtime-execution proof limits.
6. `src/upgradepilot/investigation.py` currently coordinates the Python-support mechanism but does not yet expose or orchestrate the artifact-serviceability / target-artifact-environment path.
7. `src/upgradepilot/cli.py` currently renders dependency, CI, package/upstream, Python-support, and target-Python state, but no artifact-serviceability section.
8. `tests/test_investigation.py` protects important orchestration invariants: conditional target acquisition, early-stop behavior, independent evidence preservation, exact target identity, and unresolved-state preservation.
9. `tests/test_artifact_serviceability.py` and `tests/test_target_artifact_environment.py` are existing focused proof owners for the two already-built mechanism components.
10. Package-root API expansion is not wanted; internal contracts remain with their owning modules.

## Why a new bounded plan was justified

The existing broad foundation plan is still useful historical/parent provenance, but it is not a good live execution surface for this session because:

- current naming governance requires semantic responsibility identities for selected active work;
- most of the broad foundation responsibility is already implemented/proven;
- the remaining work is a coherent multi-file integration spanning result contract, orchestration, presentation, tests, and final reconciliation;
- this boundary contains real design decisions that should be made progressively from source/test evidence rather than guessed all at once.

Therefore the session uses:

`plans/ARTIFACT_SERVICEABILITY_PUBLIC_INVESTIGATION_INTEGRATION_PLAN.md`

as the bounded continuation plan.

## Learning-by-Doing cadence for this session

For each substantive slice:

```text
orient on the exact mechanism / owner / proof boundary
→ perform one bounded real change
→ inspect actual tests/evidence
→ preserve material decisions/results here
→ explain what happened and what it teaches us
→ make the next ownership/reasoning decision together when useful
```

Do not silently jump from contract design to orchestration to CLI to full validation in one batch.

## Initial architectural model

The desired ownership relation is currently:

```text
PyPI release evidence
→ impact.artifact_serviceability candidate/evaluation owner

exact workflow file
→ github workflow-definition owner
→ target.artifact_environment interpretation owner

normal application coordination
→ investigation.py

human-facing rendering
→ cli.py
```

Important separation:

```text
published artifact transition fact
!= target exposure
!= exact target wheel compatibility
!= runtime installation outcome
!= final maintainer recommendation
```

`investigation.py` should coordinate these owners, not recreate their semantics.

## Decisions already established

### Decision 1 — continue with semantic plan identity

Use the new semantic continuation plan rather than selecting the old coordinate-heavy foundation filename as the live execution surface.

Reason: current navigation/naming governance plus the much narrower remaining responsibility.

### Decision 2 — integration is additive

The artifact-serviceability path must be added without weakening or replacing existing Python-support/CI/upstream behavior.

Reason: the existing mechanism is already independently proven and the second mechanism is meant to create heterogeneous technical state, not a replacement architecture.

### Decision 3 — serviceability state is technical evidence, not overall recommendation

The new path may expose candidate/applicability/proof-strength state, but must not silently decide the dependency update or maintainer action.

Reason: overall synthesis remains a separate product responsibility.

### Decision 4 — static target evidence remains bounded

Runner/Python/install declarations from workflow configuration must not be treated as runtime execution or exact wheel compatibility unless an admitted deterministic transformation genuinely establishes that proposition.

Reason: current Target and artifact-serviceability owners explicitly preserve this proof boundary.

## Open design questions for the first implementation slice

These are deliberate checkpoints, not blockers to planning:

1. What is the smallest truthful additive field shape for `PublicPullRequestInvestigation`?
   - candidate result?
   - target artifact-environment result?
   - final artifact-serviceability assessment?
   - some bounded combination?
2. Is target artifact-environment state one selected workflow/job result or a collection tied to several exact workflow environments?
3. The current normal path acquires the proposed package release. Where should exact old-release acquisition occur so artifact candidate formation reuses provider responsibility without awkward duplication?
4. Can currently admitted static target artifact-environment evidence establish any exact `TargetWheelCompatibilityEvidence`, or must the first integrated applicability result honestly remain unresolved/insufficient?
5. Should the first human-facing section show only proposition-relevant/required artifact states, or also optional candidate/blocked context?
6. What CLI terminology most clearly distinguishes observed facts, candidate state, blocked/insufficient evidence, and established applicability?

## Next bounded action

Start **result-contract and evidence-flow decision** from the new plan:

- inspect the exact artifact-serviceability focused tests and target artifact-environment focused tests;
- inspect how package release evidence is acquired/reused in `investigation.py`;
- trace existing workflow-definition evidence available to the application path;
- decide the smallest truthful result shape before changing executable code.

No implementation should begin until that contract/evidence-flow decision is explicit enough that its tests can be named.

## Validation / evidence ledger

### Planning re-entry

Inspected:

- `AGENTS.md`
- `MEMORY.md`
- `OPERATING_GUIDE.md`
- `.agents/skills/upgradepilot-planning-design/SKILL.md`
- `.agents/skills/upgradepilot-learning-by-doing/SKILL.md`
- `.agents/skills/upgradepilot-working-memory/SKILL.md`
- `plans/README.md`
- `working-memory/README.md`
- historical impact/applicability foundation plan, including its unfinished second-mechanism application-path responsibility
- `src/upgradepilot/impact/artifact_serviceability.py`
- `src/upgradepilot/target/artifact_environment.py`
- `src/upgradepilot/investigation.py`
- `src/upgradepilot/cli.py`
- `tests/test_investigation.py`
- package-interface protection test

Planning conclusion:

```text
existing components are independently present
+
normal application path does not compose them
+
remaining responsibility is coherent and multi-file
→ semantic bounded continuation plan is justified
```

### Executable validation

No executable product changes were made in this planning slice. No tests were run because this slice only created/reconciled planning and session-state artifacts.

## Progressive session log

Add only material decisions, evidence, failures, proof results, and continuation changes here as later slices are completed. Avoid command-by-command diary noise.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-working-memory`  
`UP-SKILL:upgradepilot-planning-design`