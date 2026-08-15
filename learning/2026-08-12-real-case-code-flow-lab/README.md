# Real-Case Code-Flow Learning Lab

**Created:** 2026-08-12  
**Learning branch:** `learning/real-case-code-flows-2026-08-12`  
**Initial main baseline:** `7a177a585fb8dcf0ed4c6af295ca93d975b11c85`  
**Latest synchronized main baseline:** `54ce69082b0d74ec0412b05264dfae897f970d47`  
**Latest sync merge:** `4bedb554174a8300f6b39233b2446c9049fb87e5`

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
- what is waiting on implementation or live acceptance.

The TODO may reorder as `main` advances or Ali redirects the learning focus. Skipped work stays open.

### [`2026-08-14_MAIN_SYNC_AND_LEARNING_ORIENTATION.md`](2026-08-14_MAIN_SYNC_AND_LEARNING_ORIENTATION.md)

Historical checkpoint for the August 14 synchronization and the then-current Target Artifact Environment orientation. It remains valid for that source state and is not rewritten to pretend it described later Phase-E work.

### [`2026-08-15_PHASE_E_ONBOARDING_REALIGNMENT.md`](2026-08-15_PHASE_E_ONBOARDING_REALIGNMENT.md)

Current learning-orientation checkpoint recording:

- synchronization through the newest observed `main` source state;
- the completed Phase A-D architecture reconciliation and ADR-0008;
- Cluster-1 validated parser foundation;
- newly landed Cluster-2 typed static workflow-IR source/tests;
- the distinction between source/test implementation presence and live validated cluster completion;
- why the learning target moved from the older Target-only flow to the cross-responsibility Phase-E architecture/parser/IR path;
- the preserved return path for older unchecked learning work.

## Current orientation

The latest synchronized source state now contains the bounded typed GitHub Actions static workflow-definition IR and focused IR regressions. However, at this exact snapshot `MEMORY.md` still records the earlier deliberate pause after validated Cluster 1 and has not yet recorded Cluster 2 as completed/green.

Therefore our learning state distinguishes:

```text
source/tests for Cluster 2 are present
!= Cluster 2 live completion/validation has been recorded
```

The current learning target is:

```text
why duplicated CI/Target GitHub Actions readers became an architecture problem
        ↓
ADR-0008 shared bounded static workflow-definition architecture
        ↓
Cluster 1 PyYAML parser/traversal foundation
        ↓
new typed provider IR in workflow_definition.py
        ↓
focused IR tests and problem-localization behavior
        ↓
what is implemented now vs what remains unvalidated/unmigrated
```

Current source now includes provider types such as:

```text
WorkflowDefinition / WorkflowDefinitionProblem
StepsJobDefinition / ReusableWorkflowJobDefinition / JobProblem
RunStepDefinition / UsesStepDefinition / StepProblem
StaticScalarValue / StaticSequenceValue / StaticMappingValue
SourceSpan
```

The central proof boundary remains:

```text
static declaration
!= runtime execution
!= runtime success
!= environment formation
!= dependency exercise
```

CI and Target have **not** yet been migrated merely because the shared IR exists. Their current local readers remain valuable contrast specimens and later migration targets.

The older Target Artifact Environment lesson remains open and useful. It may be pulled in just in time rather than treated as a mandatory first lesson.

## Boundaries

- `main` owns active product implementation.
- current source/tests/runtime evidence own implemented truth.
- `MEMORY.md` owns live project position and validated continuation.
- source/test presence must not be mislabeled as completed/green plan state without the corresponding validation/live-state evidence.
- this branch may hold learning artifacts without authorizing production changes.
- learning artifacts may be historical snapshots and must not override newer implementation truth.
- a future implementation cluster appearing in a plan is not automatically selected or authorized for execution.
