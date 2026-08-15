# Real-Case Code-Flow Learning Lab

**Created:** 2026-08-12  
**Learning branch:** `learning/real-case-code-flows-2026-08-12`  
**Initial main baseline:** `7a177a585fb8dcf0ed4c6af295ca93d975b11c85`  
**Latest synchronized main baseline:** `1e3027f87fa5b187c7d333472fe849aa6a49b049`  
**Latest sync merge:** `f6b433aa00b4d91d0542632bd4af632fb8b0a786`

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
- what is current for this learning lab;
- what is next;
- what is postponed;
- what is waiting on implementation or validation.

The TODO may reorder as `main` advances or Ali redirects the learning focus. Skipped work stays open.

### [`2026-08-14_MAIN_SYNC_AND_LEARNING_ORIENTATION.md`](2026-08-14_MAIN_SYNC_AND_LEARNING_ORIENTATION.md)

Historical checkpoint for the August 14 synchronization and the then-current Target Artifact Environment orientation. It remains valid for that source state and is not rewritten to pretend it described later Phase-E work.

### [`2026-08-15_PHASE_E_ONBOARDING_REALIGNMENT.md`](2026-08-15_PHASE_E_ONBOARDING_REALIGNMENT.md)

Current learning-orientation checkpoint recording:

- synchronization through the newest observed `main` source/live-state snapshot;
- the completed Phase A-D architecture reconciliation and ADR-0008;
- validated Cluster-1 parser foundation;
- Cluster-2 typed static workflow-IR source/tests written with WSL validation still pending;
- the distinction between main's implementation continuation and this explicitly requested separate learning-lab work;
- why the learning target moved from the older Target-only flow to the cross-responsibility Phase-E architecture/parser/IR path;
- the preserved return path for older unchecked learning work.

## Current orientation

Current synchronized `MEMORY.md` states:

```text
✓ Cluster 0 — green baseline
✓ Cluster 1 — PyYAML parser boundary
→ Cluster 2 — typed static workflow IR written; real WSL validation pending
```

The prior onboarding pause on `main` has ended. Main implementation is allowed to continue learning-by-doing after Cluster-2 validation, and its default deep walkthrough is deferred to a later meaningful milestone.

This learning branch is different: Ali has explicitly requested that this separate conversation continue the learning lab now. That current instruction authorizes learning here; it does **not** alter `main`, validate Cluster 2, or authorize later Phase-E source implementation from the learning branch.

The current learning target is therefore:

```text
why duplicated CI/Target GitHub Actions readers became an architecture problem
        ↓
ADR-0008 shared bounded static workflow-definition architecture
        ↓
Cluster 1 PyYAML parser/traversal foundation
        ↓
current typed provider IR in workflow_definition.py
        ↓
focused IR tests and problem-localization behavior
        ↓
what is written now vs what still awaits WSL validation / consumer migration
```

Current provider source includes:

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

## Boundaries

- `main` owns active product implementation.
- current source/tests/runtime evidence own implemented truth.
- `MEMORY.md` owns main's live project position and selected continuation.
- current explicit user instruction may choose a separate learning-lab focus without silently changing main's implementation continuation.
- Cluster-2 code/tests being written is not the same as successful WSL validation or completed/green classification.
- this branch may hold learning artifacts without authorizing production changes.
- learning artifacts may be historical snapshots and must not override newer implementation truth.
