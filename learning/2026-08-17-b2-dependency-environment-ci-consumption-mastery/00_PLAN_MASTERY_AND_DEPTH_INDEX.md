# Plan Mastery and Depth Index

**Created:** 2026-08-21  
**Revised:** 2026-08-22 — depth ownership clarified and aligned with the consolidated learning contract  
**Role:** navigation and depth-control index for the active B2 learning package  
**Live learning status owner:** `LEARNING_MEMORY.md`  
**Technical live-state owner:** `../../MEMORY.md`  
**Teaching/learning contract:** `00_LEARNING_SESSION_CONTRACT_AND_ROUTE.md`

## 1. Purpose

The learning plans reference several large UpgradePilot source files. A file may contain many helpers, compatibility branches, parser details, defensive checks, and responsibilities outside the active question.

The correct learning unit is therefore:

> **a meaningful engineering responsibility / mechanism, not raw file length.**

This index owns the package-wide depth vocabulary and navigation. It does **not** repeat the contract's teaching method or the execution plans' chunk routes.

## 2. How the files work together

For each plan use:

```text
EXECUTION PLAN
→ what route/chunks/cases/source/tests are followed

MASTERY / DEPTH MAP
→ how deeply each responsibility/concept must be understood

GLOBAL CONTRACT
→ how the learning is conducted

LEARNING_MEMORY.md
→ where we currently are and what has actually been demonstrated
```

If they appear to conflict:

- the contract owns global learning method;
- the execution plan owns local learning sequence/scope;
- the matching mastery map owns intended depth;
- current source/tests own implementation truth;
- `../../MEMORY.md` owns live project continuation.

Plans inherit the contract. A plan should specialize a global rule only when its local mechanism changes how that rule is applied.

## 3. Global depth vocabulary

### OWN / MASTER

Ali can reconstruct the selected responsibility with reduced assistance:

```text
real input/precondition
→ owning source/type/function
→ material executable control flow
→ important states/branches
→ output/problem
→ representative test
→ proof/non-proof boundary
```

When material to the responsibility, mastery also includes distinguishing:

```text
CURRENT IMPLEMENTATION FACT
vs PROPOSITION-ESSENTIAL REQUIREMENT
vs DEFENSIVE / BOUNDARY HARDENING
vs UNCERTAIN / AUDIT NEEDED
vs plausible alternative design
```

Mastery does not require memorizing exact lines or reproducing a large file from a blank editor.

### STRONG WORKING UNDERSTANDING

Ali can follow the supporting source/mechanism when it is open and explain why it exists, its important inputs/outputs, and the branches that affect the current proposition. Detailed internals are learned only when they carry the mechanism.

### NAVIGATE / RECOGNIZE

Ali knows where the component lives, what responsibility it contributes, and when to inspect it. No broad source ownership is required.

### OPERATIONAL BACKGROUND

Ali understands the external technology/tool/file format enough to reason correctly about UpgradePilot without mastering that technology's implementation.

### DEFER

No present learning investment unless later real work makes the detail causally necessary.

## 4. Important interpretation rule

A single large source file may contain several depth levels at once.

Example:

```text
uv_membership.py
OWN       → selected membership evaluator / traversal responsibility
WORKING   → parsing stages that determine the active proposition
NAVIGATE  → unrelated helpers
DEFER     → unsupported/resolver/marker detail not needed now
```

Do not assign one depth label to an entire file just because one function in it is important.

Similarly:

```text
master a responsibility/mechanism
!= master the whole module
```

## 5. Plan pairs

### Plan 01 — S001 Real Case → First UpgradePilot Evidence Models

Execution:
`PLAN_01_S001_REAL_CASE_TO_FIRST_UPGRADEPILOT_EVIDENCE_MODELS.md`

Depth:
`PLAN_01_MASTERY_AND_DEPTH_MAP.md`

Primary ownership targets:

```text
uv_lock.py exact file-level transition extraction
→ change.py canonical reconciliation
→ analysis.py source-context composition at working depth
→ environment_selection.py static selector interpretation
```

Primary rule: own the selected source responsibility, not every parser/provider/helper line.

### Plan 02 — S001 Membership → CI Consumption → Coverage

Execution:
`PLAN_02_S001_MEMBERSHIP_TO_CI_CONSUMPTION_AND_COVERAGE.md`

Depth:
`PLAN_02_MASTERY_AND_DEPTH_MAP.md`

Primary ownership targets:

```text
uv_membership.py selected-environment evidence boundary + membership/traversal
→ environment_membership.py source-vs-selected comparison
→ ci/consumption.py static consumption composition
→ workflow_commands.py exact rebinding at selected slices
→ dependency_exercise.py bounded coverage evaluation
```

Primary rule: this is the most code-heavy plan, but the target is mechanism ownership + representative tests, not whole-file mastery.

### Plan 03 — Generalization Pressure: S011 + S005

Execution:
`PLAN_03_GENERALIZATION_PRESSURE_S011_AND_S005.md`

Depth:
`PLAN_03_MASTERY_AND_DEPTH_MAP.md`

Primary ownership target:

```text
changed-case transfer / prediction / evidence-state reasoning
```

Primary rule: reuse previously learned source and inspect decisive branches only. Do not create new broad source mastery merely because a different technology appears.

### Plan 04 — Current Application Boundary → Return to Building

Execution:
`PLAN_04_APPLICATION_BOUNDARY_AND_RETURN_TO_BUILDING.md`

Depth:
`PLAN_04_MASTERY_AND_DEPTH_MAP.md`

Primary ownership targets:

```text
investigation.py dependency/CI orchestration seam only
→ legacy-vs-new CI contract distinction
→ representative integration test
→ pre/post reasoning for a legitimate future change when authorized
```

Primary rule: own the application seam, not all branches in the large orchestration function.

## 6. What mastery does not require

Mastery does not require:

- memorizing source line by line or remembering exact line numbers;
- remembering every helper/type/error message;
- reproducing large files from scratch;
- avoiding AI assistance;
- learning every external tool deeply;
- reading every test;
- understanding every compatibility branch before moving forward;
- accepting current implementation choices as inherently necessary.

The normal engineering standard is:

> With the repository open, Ali can locate the selected responsibility, read the material code, explain important control flow/evidence states, understand a representative test, predict meaningful changed behavior, and participate intelligently in a later change or diagnosis.

## 7. Per-chunk usage rule

At the start of a learning chunk:

1. read the current execution-plan chunk;
2. read its matching mastery/depth section;
3. identify the exact responsibility being learned;
4. identify which nearby material is working/navigation/deferred;
5. ignore raw file size as a learning metric;
6. stop deepening when the required responsibility, important branches, representative test meaning, and proof boundary are sufficiently understood;
7. deepen a helper only when the current responsibility cannot be explained without it or a real change/failure enters it.

## 8. Learning-memory recording rule

When a chunk closes, `LEARNING_MEMORY.md` should record the responsibility/depth actually demonstrated rather than vague statements such as `learned file X`.

Prefer:

```text
OWNED / demonstrated
- exact responsibility
- central source/functions
- representative test
- proof boundary
- material design/necessity distinction if demonstrated
- assistance level where relevant

WORKING / NAVIGATION ONLY
- supporting source or external mechanism

DEFERRED
- nearby internals intentionally not learned
```

This prevents source exposure from being misread as broad ownership.

This index does not change technical sequencing, product implementation authorization, Career capability claims, or live project continuation.
