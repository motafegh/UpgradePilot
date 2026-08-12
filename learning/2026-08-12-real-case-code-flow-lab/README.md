# Real-Case Code-Flow Learning Lab

**Created:** 2026-08-12  
**Learning branch:** `learning/real-case-code-flows-2026-08-12`  
**Initial main baseline:** `7a177a585fb8dcf0ed4c6af295ca93d975b11c85`

## Purpose

This folder is a dedicated learning workspace for understanding UpgradePilot's real implementation through concrete end-to-end data flows, code paths, tests, failures, and concepts.

Product-simulation cases may be used as realistic example inputs and contrast evidence, but this workspace does **not** study the simulation program itself and does not treat simulation artifacts as product implementation truth.

## Boundaries

- `main` remains the active implementation branch.
- This learning branch may contain learning plans, flow traces, exercises, diagrams/notes, and other learning artifacts without disturbing ongoing implementation.
- Source/tests on `main` remain implementation truth; this branch should be synchronized with `main` frequently enough that learning does not drift onto stale code.
- `MEMORY.md` on the current project state remains the live-state authority; this folder does not replace it.
- No learning artifact here authorizes product implementation or changes controlling project scope.

## Learning plan

[`LEARNING_PLAN.md`](LEARNING_PLAN.md) defines the learning method and journey for this workspace, including:

- the long-lived learning-branch and `main` synchronization model;
- how real product-simulation cases are used only as concrete practical examples/pressure evidence;
- end-to-end real-code/data-flow tracing;
- just-in-time concept teaching and depth labels;
- source/test/failure-diagnosis methods;
- prediction, transfer, modification, and ownership exercises;
- artifact creation and source-baseline rules;
- the staged journey through current UpgradePilot implementation and future synchronized additions.

The plan controls this learning workspace only. It does not replace repository governance, `MEMORY.md`, product plans, source, tests, or runtime evidence.
