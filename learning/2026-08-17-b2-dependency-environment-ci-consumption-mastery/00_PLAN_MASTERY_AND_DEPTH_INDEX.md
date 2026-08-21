# Plan Mastery and Depth Index

**Created:** 2026-08-21  
**Role:** navigation and depth-control index for the active B2 learning package  
**Live learning status owner:** `LEARNING_MEMORY.md`  
**Technical live-state owner:** `../../MEMORY.md`  
**Teaching/learning contract:** `00_LEARNING_SESSION_CONTRACT_AND_ROUTE.md`

## 1. Why this index exists

The learning plans reference several large UpgradePilot source files. A file may contain hundreds of lines, many helpers, multiple result types, compatibility branches, defensive validation, or responsibilities outside the active learning question.

The correct learning unit is therefore:

> **a meaningful engineering responsibility / mechanism, not raw file length.**

The mastery companions make the required depth explicit so Ali does not interpret “this file is in the plan” as “master every line in this file.”

## 2. How to use the plan pair

For each plan, use two files together:

```text
EXECUTION MAP
What route/chunks/cases/source/tests are we following?

+

MASTERY / DEPTH MAP
How deeply must Ali understand each responsibility/file/concept?
What can remain navigation-only, operational, or deferred?
```

If they appear to conflict:

- the execution plan owns the learning sequence and technical scope;
- the mastery companion owns the intended learning depth;
- the learning contract wins over both for teaching method;
- source/tests win for current implementation truth;
- `MEMORY.md` wins for live project continuation.

## 3. Plan pairs

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

---

### Plan 02 — S001 Membership → CI Consumption → Coverage

Execution:
`PLAN_02_S001_MEMBERSHIP_TO_CI_CONSUMPTION_AND_COVERAGE.md`

Depth:
`PLAN_02_MASTERY_AND_DEPTH_MAP.md`

Primary ownership targets:

```text
uv_membership.py selected-environment membership/traversal
→ environment_membership.py source-vs-selected comparison
→ ci/consumption.py static consumption composition
→ workflow_commands.py exact rebinding at selected slices
→ dependency_exercise.py bounded coverage evaluation
```

Primary rule: this is the most code-heavy plan, but even here the goal is mechanism ownership + representative tests, not whole-file mastery.

---

### Plan 03 — Generalization Pressure: S011 + S005

Execution:
`PLAN_03_GENERALIZATION_PRESSURE_S011_AND_S005.md`

Depth:
`PLAN_03_MASTERY_AND_DEPTH_MAP.md`

Primary ownership target:

```text
changed-case transfer / prediction / evidence-state reasoning
```

Primary rule: reuse previously learned source and inspect decisive branches only. Do not create new whole-file mastery obligations merely because S011/S005 touch another technology.

---

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
→ pre/post reasoning for a legitimate future integration change when authorized
```

Primary rule: own the application seam, not all branches in the large orchestration function.

## 4. Global depth rule

For any source file encountered, classify the current relationship as one of:

```text
OWN / MASTER
selected responsibility can be reconstructed from executable code + test + proof boundary

STRONG WORKING UNDERSTANDING
important supporting component can be followed and explained when source is open

NAVIGATE / RECOGNIZE
know role/location/when to inspect; no broad ownership target

OPERATIONAL BACKGROUND
understand external technology enough for the real case

DEFER
no present learning investment unless later work makes it causally necessary
```

A source file may contain **more than one depth level at once**. Example:

```text
uv_membership.py
OWN: selected membership evaluator + traversal
WORKING: exact parsing stages relevant to S001
NAVIGATE: unrelated private helpers
DEFER: unsupported/resolver/marker detail not needed by the current proposition
```

Do not assign one depth label to an entire large file when only one responsibility is being learned.

## 5. What “mastery” does not require

Mastery does not mean:

- memorizing source line by line;
- remembering exact line numbers;
- remembering every helper/type/error message;
- reproducing large files from a blank editor;
- avoiding AI assistance;
- learning every external tool deeply;
- reading every test;
- understanding every historical compatibility branch before moving forward.

The normal engineering standard is:

> With the repository open, Ali can locate the responsibility, read the material code, explain the important control flow and evidence states, understand a representative test, predict meaningful changed behavior, and participate intelligently in a later change or diagnosis.

## 6. Learning-memory recording rule

When a chunk closes, `LEARNING_MEMORY.md` should record the **responsibility/depth actually demonstrated**, not vague statements such as “learned file X.” Prefer:

```text
OWNED / demonstrated:
- exact responsibility
- central source/functions
- representative test
- proof boundary
- assistance level

WORKING / navigation only:
- supporting source or external mechanism

DEFERRED:
- exact nearby internals deliberately not learned
```

This avoids future Career or project sessions misreading source exposure as broad source ownership.

## 7. Current-use rule

At the start of a learning chunk:

1. read the current plan chunk;
2. read its matching mastery/depth section;
3. identify the exact responsibility being learned;
4. ignore raw file length as a learning metric;
5. stop deepening when the responsibility, important branches, test meaning, and proof boundary are sufficiently understood;
6. deepen a helper only when the current responsibility cannot be explained without it or a real change/failure enters it.

This index does not change technical sequencing, implementation authorization, or Career capability claims.