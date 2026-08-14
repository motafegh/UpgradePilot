# Real-Case Code-Flow Learning Lab

**Created:** 2026-08-12  
**Learning branch:** `learning/real-case-code-flows-2026-08-12`  
**Initial main baseline:** `7a177a585fb8dcf0ed4c6af295ca93d975b11c85`  
**Latest synchronized main baseline:** `8c1415e61aab4b16e80bb3f09ba7fb9a77b54ae1`  
**Latest sync merge:** `64971024740f8943533410c7d222606b7b4a97d5`

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

It is intentionally not the live project-state owner. `MEMORY.md` on current `main` remains authoritative for live product position.

### [`LEARNING_TODO.md`](LEARNING_TODO.md)

Small operational checklist:

- what is covered;
- what is current;
- what is next;
- what is postponed;
- what is waiting on new implementation.

The TODO may reorder as `main` advances or Ali redirects the learning focus. Skipped work stays open.

### [`2026-08-14_MAIN_SYNC_AND_LEARNING_ORIENTATION.md`](2026-08-14_MAIN_SYNC_AND_LEARNING_ORIENTATION.md)

Dated checkpoint recording:

- the preserved pre-sync learning state;
- synchronization from the original baseline to current `main`;
- material implementation changes now available to learn;
- why the current recommended checkpoint is the Target Artifact Environment positive flow.

## Current orientation

At the latest synchronization, the newest verified learning-relevant implementation is:

```text
RepositoryTextFile
+ dependency source path
→ interpret_target_artifact_environment(...)
→ TargetArtifactEnvironmentEvidence / explicit problem
```

Artifact Serviceability Increment 2 is also implemented and verified downstream given exact `TargetWheelCompatibilityEvidence`.

The recommended current learning checkpoint is therefore the concrete target artifact-environment flow, with older prerequisites pulled in only as needed. Ali may redirect this at any time under the learning-order override rule.

## Boundaries

- `main` owns active product implementation.
- current source/tests/runtime evidence own implemented truth.
- `MEMORY.md` owns live project position.
- this branch may hold learning artifacts without authorizing production changes.
- learning artifacts may be historical snapshots and must not override newer implementation truth.
