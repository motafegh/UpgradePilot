# Real-Case Code-Flow Learning Lab

**Created:** 2026-08-12  
**Learning branch:** `learning/real-case-code-flows-2026-08-12`  
**Initial main baseline:** `7a177a585fb8dcf0ed4c6af295ca93d975b11c85`  
**Latest synchronized main baseline:** `89d2b845647a7159cb276cbb38c0cdea0608d8af`  
**Latest sync merge:** `6e53c7a6c50dfa42e7cb1a26bc083040bdf0f996`

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

Small operational checklist:

- what is covered;
- what is current;
- what is next;
- what is postponed;
- what is waiting on new implementation.

The TODO may reorder as `main` advances or Ali redirects the learning focus. Skipped work stays open.

### [`2026-08-14_MAIN_SYNC_AND_LEARNING_ORIENTATION.md`](2026-08-14_MAIN_SYNC_AND_LEARNING_ORIENTATION.md)

Historical checkpoint for the August 14 synchronization and the then-current Target Artifact Environment orientation. It remains valid for that source state and is not rewritten to pretend it described later Phase-E work.

### [`2026-08-15_PHASE_E_ONBOARDING_REALIGNMENT.md`](2026-08-15_PHASE_E_ONBOARDING_REALIGNMENT.md)

Current learning-orientation checkpoint recording:

- synchronization through current `main@89d2b845...`;
- the completed Phase A-D architecture reconciliation and ADR-0008;
- Phase-E Cluster 0/1 completion and deliberate onboarding pause;
- why the learning target moved from the older Target-only flow to the cross-responsibility Phase-E architecture/parser boundary;
- the preserved return path for older unchecked learning work.

## Current orientation

Current `MEMORY.md` deliberately pauses Phase-E implementation after Cluster 1 for onboarding and understanding. No Cluster-2 implementation has begun.

The current learning target is therefore:

```text
why duplicated CI/Target GitHub Actions readers became an architecture problem
        ↓
ADR-0008 shared bounded static workflow-definition architecture
        ↓
Cluster 1 PyYAML parser/traversal boundary
        ↓
what Cluster 1 proves and deliberately does not prove
        ↓
mental model for the future typed static workflow IR
```

Current implemented parser slice:

```text
untrusted GitHub Actions workflow YAML text
→ yaml.compose(..., Loader=yaml.BaseLoader)
→ PyYAML representation nodes
→ controlled malformed-YAML failure
→ bounded recursive-alias / depth / node traversal validation
```

The typed GitHub Actions static workflow-definition IR is **not implemented yet**. That is a later Phase-E cluster and is not authorized merely because we study its intended responsibility.

The central proof boundary to own is:

```text
static declaration
!= runtime execution
!= runtime success
!= environment formation
!= dependency exercise
```

The older Target Artifact Environment lesson remains open and useful. It is now a contrast/prerequisite source that may be pulled in just in time rather than the mandatory first lesson.

## Boundaries

- `main` owns active product implementation.
- current source/tests/runtime evidence own implemented truth.
- `MEMORY.md` owns live project position.
- this branch may hold learning artifacts without authorizing production changes.
- learning artifacts may be historical snapshots and must not override newer implementation truth.
- a future implementation cluster appearing in a plan is not automatically selected or authorized for execution.
