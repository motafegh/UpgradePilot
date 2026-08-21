# Plan 04 — Mastery and Depth Map

**Companion to:** `PLAN_04_APPLICATION_BOUNDARY_AND_RETURN_TO_BUILDING.md`  
**Purpose:** define exactly what Ali must own at the ordinary-application seam and what remains navigation/deferred  
**Authority:** subordinate to the learning contract, live `MEMORY.md`, active source/tests, and Plan 04  
**Important rule:** Plan 04 is about **application-seam ownership and intelligent return to building**, not mastering the whole orchestration layer.

## 1. Depth labels

### OWN / MASTER
Ali can reconstruct the selected application responsibility with reduced assistance, explain the actual call/data flow and representative test, predict a legitimate change when authorized, and state proof limits.

### STRONG WORKING UNDERSTANDING
Ali can follow the source and explain the relevant transitional/compatibility path without owning unrelated application behavior.

### NAVIGATE / RECOGNIZE
Ali knows where the component lives and what role it plays but does not need to master its internals.

### DEFER
No learning/implementation depth until live project authority selects the responsibility.

## 2. Plan-04 end-state in one sentence

By the end of Plan 04, Ali should be able to identify and explain the exact seam between the ordinary public-PR application path and the newer typed Cluster-5 capability, reconstruct the current end-to-end proposition flow, understand one representative integration test, and re-enter authorized building without pretending to own every branch in `investigation.py` or every downstream subsystem.

## 3. Chunk 1 — Ordinary application path vs Cluster-5 path

### `src/upgradepilot/investigation.py`

**OWN / MASTER — selected orchestration seam, NOT the whole file.**

Own the specific public-PR CI evidence path centered on:

- `PublicPullRequestInvestigation` only for fields relevant to dependency/CI evidence;
- `investigate_public_pull_request(...)` only through the dependency-analysis → workflow evidence → CI evaluator seam;
- the current use of `DependencyChangeAnalysis.direct_requirements_install_path` where still present;
- construction of `WorkflowDependencyExerciseInput` for the legacy path;
- the current call to `evaluate_dependency_ci_exercise(...)`;
- the contrast with the newer typed Cluster-5 path that uses environment/source context + typed consumption/coverage capability.

Ali should be able to reconstruct:

```text
public PR
→ dependency analysis
→ workflow/runtime evidence acquisition
→ current legacy CI evaluation call

IN PARALLEL IN DOMAIN LAYER:
new typed environment/consumption/coverage capability exists
but ordinary orchestration has not yet been migrated at the inspected snapshot
```

**MASTER THE SEAM, NOT ALL ORCHESTRATION:** Ali does not need to master upstream release/changelog/LLM/target-Python branches merely because they live in the same large function. Those branches are navigation-only unless a different learning responsibility selects them.

### STRONG WORKING UNDERSTANDING

- conditionals/early returns only where they determine whether dependency/CI evaluation runs;
- typed object construction at the migration seam;
- why Cluster 5 deliberately retained the old path until separate application integration;
- which data shape the legacy path uses versus which richer typed evidence the new path can use.

### NAVIGATE / DEFER

- all upstream release/tag/changelog/support-drop logic;
- target-Python applicability logic;
- unrelated fields in `PublicPullRequestInvestigation`;
- CLI presentation/detail not needed to understand the seam;
- every dependency/CI helper called elsewhere in the function.

### Representative test target

`tests/test_investigation.py` — one test that protects current ordinary application CI behavior at the seam.

Ali should explain setup → orchestration action → asserted result/path → what integration invariant it protects → what it does not prove.

## 4. Supporting source at the seam

### `src/upgradepilot/dependency/analysis.py`

**STRONG WORKING UNDERSTANDING:** understand the difference between `source_contexts` as richer current truth and `direct_requirements_install_path` as a compatibility projection where still retained.

Do not re-master the whole analysis source from Plan 01.

### `src/upgradepilot/ci/dependency_exercise.py`

**OWN THE LEGACY-vs-NEW CONTRACT DIFFERENCE:**

Ali should understand at API/semantic level:

```text
evaluate_dependency_ci_exercise(...)
vs
evaluate_dependency_ci_coverage(...)
```

He should know which one ordinary orchestration currently calls at the inspected snapshot and what semantic limitations/differences matter for migration.

**NAVIGATE:** do not reread every internal branch already covered in Plan 02 unless needed to explain the seam.

### `src/upgradepilot/ci/workflow_commands.py`

**OWN THE OLD-vs-NEW INSPECTOR DIFFERENCE AT BOUNDARY LEVEL:**

```text
inspect_workflow_commands(...)
vs
inspect_workflow_dependency_evidence(...)
```

Ali should understand why the newer path preserves richer typed static evidence and multiple jobs while the retained legacy path exists for compatibility.

No whole-file re-mastery is required.

### CLI / presentation source

**NAVIGATE ONLY** unless a real integration test or user-visible contract depends on it. Plan 04 does not require broad CLI ownership.

## 5. Transitional architecture mastery

Ali should be able to answer:

- Why can a new domain capability be implemented and tested while the normal application still uses the legacy path?
- What migration risk/responsibility separation did that staged approach protect?
- Which compatibility projection/path is temporary by design?
- When does “deliberately transitional” become stale duplication that should be removed?
- What observations are implementation facts versus engineering recommendations?

Ali should **not** assume the transitional seam is permanently good architecture merely because it was intentional.

## 6. Chunk 2 — End-to-end reconstruction

### MASTER — proposition chain, not every helper

Ali should be able to reconstruct:

```text
S001 dependency update
→ exact dependency/source context
→ static workflow/environment selection
→ selected-environment membership witness
→ static CI consumption
→ separate direct exercise
→ separate runtime authority
→ supported_not_correlated
→ ordinary application integration seam
```

For each major rung, Ali should know:

- owning module/responsibility;
- central function/type at recognition level;
- input/output meaning;
- strongest established proposition;
- immediate stronger claim that remains unjustified.

This is **not** a requirement to remember every helper name or exact signature.

### TRANSFER CHECK

Ali should also predict:

```text
S011 → affected mlx + selected dev → not_established
S005 → tox-mediated lock use → current-support/architecture pressure, not invented support
```

## 7. Chunk 3 — Return to building / modification ownership

Plan 04 is the prime candidate for a Career-grade **ownership-bearing modification**, but only when live `MEMORY.md` selects a legitimate integration/refactor/change.

### BEFORE A LEGITIMATE CHANGE — MUST MASTER THE MODEL

Ali should be able to state:

```text
what behavior/data flow should change?
which layer/responsibility owns it?
what should remain unchanged?
what output/test should change or stay green?
what proof boundary remains after the change?
```

If Ali cannot yet form a useful model, teach the smallest blocking prerequisite first. Do not let AI implement the selected change before this model exists.

### AFTER AI-ASSISTED IMPLEMENTATION — MUST INSPECT

Ali must inspect the actual material diff/source/tests and explain:

- what changed;
- why it belongs there;
- what old path was removed/retained;
- what test/evidence protects the change;
- whether the observed result matched the pre-change prediction;
- what remains uncertain/non-owned.

Manual typing is not required. Understanding/control is required.

### REAL FAILURE DIAGNOSIS

If a genuine failure occurs during authorized work, Ali should first contribute:

```text
likely failure layer
current hypothesis
one discriminating check
```

before the assistant immediately supplies root cause/patch. If no real failure occurs, no debugging evidence is fabricated.

## 8. Tests to master

### PRIMARY

- `tests/test_investigation.py` — one representative application-seam test.

### SUPPORTING / RECOGNIZE AS NEEDED

- `tests/test_ci_dependency_exercise.py` — legacy behavior;
- `tests/test_ci_dependency_coverage.py` — new typed coverage contract;
- `tests/test_cli.py` only if user-visible integration behavior materially matters.

Ali does not need to master the entire test files. One or a few discriminating tests are sufficient when they expose the seam and behavior boundary.

## 9. What Plan 04 must NOT become

Do not turn Plan 04 into:

- mastery of the entire `investigation.py` function;
- reopening every upstream/LLM/target-Python responsibility;
- rereading all CI internals from Plan 02;
- a full CLI architecture course;
- implementing Cluster 6 merely because the learning plan reaches the seam;
- forcing a change to satisfy Career evidence;
- manufacturing a failure;
- delaying legitimate building until every earlier `[~]` item is perfect.

## 10. Plan-04 completion evidence

Plan 04 is complete enough when Ali can, with reduced assistance:

1. point to and explain the current legacy CI call in ordinary orchestration;
2. name and explain the newer typed Cluster-5 alternative at the correct semantic level;
3. distinguish `source_contexts` from the retained compatibility projection;
4. explain old vs new CI evaluator/inspector contracts without rereading every internal line;
5. explain one representative application-seam test;
6. reconstruct S001 end to end through the current Cluster-5 domain boundary;
7. use S011/S005 as short transfer checks;
8. explain why domain capability existence != application integration;
9. classify remaining gaps as blocking/non-blocking/deferred rather than requiring perfect recall;
10. re-read live `MEMORY.md` and follow the actual authorized next project action.

If a legitimate integration/refactor is authorized during or after this plan, a strong ownership candidate additionally includes Ali's pre-change model + inspected diff/test + post-change explanation. That is **additional evidence**, not a compulsory reason to mutate code.