# Real-Case Code-Flow Learning Lab

**Created:** 2026-08-12  
**Learning branch:** `learning/real-case-code-flows-2026-08-12`  
**Initial main baseline:** `7a177a585fb8dcf0ed4c6af295ca93d975b11c85`  
**Latest synchronized main baseline:** `72eb291e6ffc9112956e37f34dc5c7f7e3c40154`  
**Latest sync merge:** `35bc756f02c6afd044d80ab545ae5b860ec87b2a`

## Purpose

This folder is the dedicated learning workspace for understanding UpgradePilot's actual implementation through real code/data flows, tests, failures, concepts, and bounded ownership exercises while product development continues independently on `main`.

Product-simulation cases may provide realistic inputs and transfer pressure. They are not the curriculum and do not replace source/tests as implementation truth.

## Files

### [`LEARNING_PLAN.md`](LEARNING_PLAN.md)

Stable learning method and guardrails:

- learning-branch synchronization model;
- real-case code/data-flow method;
- just-in-time concept teaching;
- source/test/failure-diagnosis method;
- demonstrated-depth rules;
- artifact policy;
- learning-order override and prerequisite recovery.

It is intentionally not the live project-state owner. `MEMORY.md` on synchronized current `main` remains authoritative for live product position.

### [`LEARNING_TODO.md`](LEARNING_TODO.md)

Small operational checklist for what is covered, current, next, postponed, or waiting on implementation. The TODO may reorder as `main` advances or Ali redirects the learning focus. Skipped work stays open.

### Historical / dated checkpoints

- [`2026-08-14_MAIN_SYNC_AND_LEARNING_ORIENTATION.md`](2026-08-14_MAIN_SYNC_AND_LEARNING_ORIENTATION.md) — historical August 14 Target-artifact orientation.
- [`2026-08-15_PHASE_E_ONBOARDING_REALIGNMENT.md`](2026-08-15_PHASE_E_ONBOARDING_REALIGNMENT.md) — transition into Phase-E architecture learning through the then-current Cluster-2 point.
- [`2026-08-15_CLUSTER_3_VALIDATED_LEARNING_FRONTIER.md`](2026-08-15_CLUSTER_3_VALIDATED_LEARNING_FRONTIER.md) — current checkpoint after validated Clusters 2 and 3 and the pause before Cluster 4.

## Current orientation

Current synchronized `MEMORY.md` states:

```text
✓ Cluster 0 — green baseline
✓ Cluster 1 — PyYAML parser boundary
✓ Cluster 2 — typed static GitHub Actions workflow IR
✓ Cluster 3 — shared direct-install declaration observation

PAUSE — discussion / decision checkpoint

[ ] Cluster 4 — Target migration
```

The current validated implementation foundation is:

```text
RepositoryTextFile
        ↓
PyYAML bounded parser boundary
        ↓
typed GitHub Actions static workflow IR
        ↓
dependency-owned direct-install declaration observation
```

The learning branch is intentionally close to this frontier. We move backward only enough to understand why these newest responsibilities exist and how they connect.

## Current learning target

```text
why CI and Target duplicated GitHub Actions source reading
        ↓
ADR-0008 provider/domain boundary
        ↓
Cluster 1 parser foundation
        ↓
Cluster 2 typed static workflow IR
        ↓
Cluster 3 dependency-owned direct-install declaration observation
        ↓
why Target migration is next, but not yet implemented
```

Cluster 3 is especially useful because it is the first implemented consumer of the new static IR outside the GitHub provider layer. It translates a static `RunStepDefinition` plus working-directory context plus an independently established dependency-source path into:

```text
observed | not_observed | unresolved
```

Effective `working-directory` precedence is:

```text
step
↓
job defaults.run
↓
workflow defaults.run
↓
repository root
```

Central proof boundary:

```text
direct install declaration observed
!= command executed
!= command succeeded
!= environment formed
!= exact proposed dependency version installed
!= general dependency consumption
!= package exercise
```

## Boundaries

- `main` owns active product implementation.
- current source/tests/runtime evidence own implemented truth.
- `MEMORY.md` owns main's live project position and selected continuation.
- this branch may continue learning without changing `main` execution.
- Cluster 4 remains unimplemented and paused until explicitly resumed on `main`.
- learning artifacts may preserve historical snapshots but never override newer source/tests or `MEMORY.md`.
