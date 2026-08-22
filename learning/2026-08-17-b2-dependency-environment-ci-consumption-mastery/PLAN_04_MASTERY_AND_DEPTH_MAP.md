# Plan 04 — Mastery and Depth Map

**Companion to:** `PLAN_04_APPLICATION_BOUNDARY_AND_RETURN_TO_BUILDING.md`  
**Purpose:** define exactly what Ali must own at the ordinary-application seam and what remains navigation/deferred  
**Authority:** subordinate to the learning contract, live `MEMORY.md`, active source/tests, and Plan 04  
**Important rule:** Plan 04 is about **application-seam ownership and intelligent return to building**, not mastering the whole orchestration layer.  
**Revised:** 2026-08-22 — explicit depth rationale and evidence-driven transitional-architecture audit added

## 1. Depth labels

### OWN / MASTER
Ali can reconstruct the selected application responsibility with reduced assistance, explain the actual call/data flow and representative test, explain why the selected depth matters, predict a legitimate change when authorized, state proof limits, and critically evaluate the seam without assuming its design is correct.

### STRONG WORKING UNDERSTANDING
Ali can follow the relevant source path and explain the compatibility/transitional behavior where evidence establishes it, while keeping unsupported rationale explicitly uncertain.

### NAVIGATE / RECOGNIZE
Ali knows where the component lives and what role it plays but does not need to master its internals.

### DEFER
No learning/implementation depth until live project authority selects the responsibility.

## 2. Plan-04 end-state and why this depth matters

By the end of Plan 04, Ali should be able to identify and explain the exact seam between the ordinary public-PR application path and the newer typed Cluster-5 capability, reconstruct the current end-to-end proposition flow, understand one representative integration test, critically evaluate the seam's actual rationale/design quality, and re-enter authorized building without pretending to own every branch in `investigation.py` or every downstream subsystem.

Why the application seam deserves OWN/MASTER depth:

```text
Domain capability existing in source/tests does not prove the ordinary product invokes it.
The seam decides what data shape and evaluator the real application path actually uses.
A future authorized integration/refactor/diagnosis is likely to enter this boundary.
```

That makes the seam more valuable than broad orchestration memorization.

## 3. Chunk 1 — Ordinary application path vs Cluster-5 path

### `src/upgradepilot/investigation.py`

**OWN / MASTER — selected orchestration seam, NOT the whole file.**

Own the specific public-PR CI evidence path centered on:

- `PublicPullRequestInvestigation` only for fields relevant to dependency/CI evidence;
- `investigate_public_pull_request(...)` only through the dependency-analysis → workflow evidence → CI evaluator seam;
- the use of `DependencyChangeAnalysis.direct_requirements_install_path` at the inspected snapshot where still present;
- construction of `WorkflowDependencyExerciseInput` for the legacy path;
- the call to `evaluate_dependency_ci_exercise(...)` at the inspected snapshot;
- the contrast with the newer typed Cluster-5 path that uses environment/source context + typed consumption/coverage capability.

Ali should be able to reconstruct:

```text
public PR
→ dependency analysis
→ workflow/runtime evidence acquisition
→ ordinary legacy CI evaluation call at inspected snapshot

IN PARALLEL IN DOMAIN LAYER:
newer typed environment/consumption/coverage capability exists
but ordinary orchestration has not yet adopted it at that snapshot
```

**Why this depth:** this is the exact product-integration boundary. Understanding only the newer domain capability would create a false mental model of product behavior; understanding the seam prepares Ali for a future integration/refactor/diagnosis if live authority selects it.

**MASTER THE SEAM, NOT ALL ORCHESTRATION:** Ali does not need to master upstream release/changelog/LLM/target-Python branches merely because they live in the same large function. Those branches are navigation-only unless a different learning responsibility selects them.

### STRONG WORKING UNDERSTANDING

- conditionals/early returns only where they determine whether dependency/CI evaluation runs;
- typed object construction at the seam;
- evidence for whether the old/new split was deliberately staged, rather than presuming that history;
- data-shape differences between the legacy and newer typed paths;
- any documented migration rationale only to the depth required to evaluate whether it still applies.

**Why this depth:** these details affect seam behavior/rationale but do not require ownership of unrelated application orchestration.

### NAVIGATE / DEFER

- all upstream release/tag/changelog/support-drop logic;
- target-Python applicability logic;
- unrelated fields in `PublicPullRequestInvestigation`;
- CLI presentation/detail not needed to understand the seam;
- every dependency/CI helper called elsewhere in the function.

### Representative test target

`tests/test_investigation.py` — one test that protects ordinary application CI behavior at the seam.

Ali should explain setup → orchestration action → asserted result/path → protected integration invariant → what it does not prove.

### Parallel audit focus

- Does ordinary orchestration actually call the path the plan expects at the inspected snapshot?
- What evidence, if any, establishes that legacy/newer paths were intentionally separated for migration?
- If a rationale is documented, is it technically convincing and still applicable?
- Does the seam lose richer typed evidence, duplicate semantics, or create stale compatibility risk?
- Are tests protecting intended product behavior or merely freezing an old wiring pattern?
- If rationale is not established, classify it `UNCERTAIN / AUDIT NEEDED` rather than inventing one.

## 4. Supporting source at the seam

### `src/upgradepilot/dependency/analysis.py`

**STRONG WORKING UNDERSTANDING:** understand the difference between `source_contexts` as richer current domain evidence and `direct_requirements_install_path` as a compatibility projection where still retained.

**Why this depth:** Ali needs to understand the data-shape difference that reaches the application seam, but Plan 01 already covered the broader analysis responsibility.

Do not re-master the whole analysis source from Plan 01.

### `src/upgradepilot/ci/dependency_exercise.py`

**OWN THE LEGACY-vs-NEW CONTRACT DIFFERENCE:**

Ali should understand at API/semantic level:

```text
evaluate_dependency_ci_exercise(...)
vs
evaluate_dependency_ci_coverage(...)
```

He should know which one ordinary orchestration calls at the inspected snapshot and what semantic limitations/differences matter for any future migration.

**Why this depth:** the contract difference determines what evidence strength/product data shape an integration change would introduce. Ali does not need another full internal pass because Plan 02 already owns the new coverage evaluator.

**NAVIGATE:** do not reread every internal branch already covered in Plan 02 unless needed to explain or audit the seam.

### `src/upgradepilot/ci/workflow_commands.py`

**OWN THE OLD-vs-NEW INSPECTOR DIFFERENCE AT BOUNDARY LEVEL:**

```text
inspect_workflow_commands(...)
vs
inspect_workflow_dependency_evidence(...)
```

Ali should understand the observed semantic/data-shape difference and verify from source/tests what richer evidence the newer path preserves. Do not attribute a compatibility rationale unless evidence establishes it.

**Why this depth:** the inspector choice is part of the application migration boundary, but whole-file re-mastery would repeat Plan 02 without adding integration understanding.

### CLI / presentation source

**NAVIGATE ONLY** unless a real integration test or user-visible contract depends on it. Plan 04 does not require broad CLI ownership.

**Why not deeper:** presentation is not the selected seam unless a real visible contract/test makes it causally necessary.

## 5. Transitional architecture mastery

Ali should be able to answer without presuming the answer in advance:

- How can a new domain capability exist while the ordinary application still uses an older path?
- What source/plan/history evidence establishes whether this specific seam was deliberately staged?
- If it was deliberate, what concrete migration risk/responsibility separation was it intended to protect?
- Is that rationale technically convincing and still applicable at the inspected/live state?
- Which compatibility projection/path is actually documented as temporary, if any?
- When does a transitional seam become stale duplication that should be removed?
- What observations are implementation facts, grounded rationale, engineering recommendations, or still uncertain?

**Why this depth:** future integration decisions require more than knowing that two APIs coexist. Ali must be able to evaluate whether the seam is justified or simply historical debt.

Ali should **not** assume the transitional seam is good architecture merely because source/history used transitional language.

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
- immediate stronger claim that remains unjustified;
- material audit concern if one was established.

**Why this depth:** the reconstruction proves the individual mechanisms form a coherent product evidence chain and reveals where the application currently stops. Re-learning every helper would not improve that ownership test.

This is **not** a requirement to remember every helper name or exact signature.

### TRANSFER CHECK

Ali should also predict:

```text
S011 → affected mlx + selected dev → not_established
S005 → tox-mediated lock use → current-support/architecture pressure, not invented support
```

## 7. Chunk 3 — Return to building / modification ownership

This seam may become a strong Career-grade **ownership-bearing modification** only when live `MEMORY.md` selects a legitimate integration/refactor/change.

### BEFORE A LEGITIMATE CHANGE — MUST MASTER THE MODEL

Ali should be able to state:

```text
what behavior/data flow should change?
which layer/responsibility appears to own it, based on evidence?
what should remain unchanged?
what output/test should change or stay green?
what proof boundary remains after the change?
what known audit finding/rationale should influence the change?
```

If Ali cannot yet form a useful model, teach the smallest blocking prerequisite first. Do not let AI implement the selected change before this model exists.

### AFTER AI-ASSISTED IMPLEMENTATION — MUST INSPECT

Ali must inspect the actual material diff/source/tests and explain:

- what changed;
- why it belongs there based on actual ownership/evidence;
- what old path was removed/retained;
- what test/evidence protects the change;
- whether the observed result matched the pre-change prediction;
- whether any earlier design rationale/audit finding was confirmed or contradicted;
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

**Why this depth:** this test is the nearest proof of what ordinary orchestration currently does at the selected seam; it is more valuable than broad test-file coverage.

### SUPPORTING / RECOGNIZE AS NEEDED

- `tests/test_ci_dependency_exercise.py` — legacy behavior;
- `tests/test_ci_dependency_coverage.py` — newer typed coverage contract;
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
- delaying legitimate building until every earlier `[~]` item is perfect;
- inventing a clean migration rationale to make historical architecture appear intentional.

## 10. Plan-04 completion evidence

Plan 04 is complete enough when Ali can, with reduced assistance:

1. point to and explain the ordinary legacy CI call at the inspected snapshot;
2. name and explain the newer typed Cluster-5 alternative at the correct semantic level;
3. distinguish `source_contexts` from the retained compatibility projection;
4. explain old vs new CI evaluator/inspector contracts without rereading every internal line;
5. explain why the application seam deserves this depth while unrelated orchestration does not;
6. explain one representative application-seam test;
7. reconstruct S001 end to end through the current Cluster-5 domain boundary;
8. use S011/S005 as short transfer checks;
9. explain why domain capability existence != application integration;
10. classify the seam's rationale/design quality as grounded, questionable, or uncertain without inventing reasons;
11. preserve any material durable seam finding through the contract's audit route when warranted;
12. classify remaining gaps as blocking/non-blocking/deferred rather than requiring perfect recall;
13. re-read live `MEMORY.md` and follow the actual authorized next project action.

If a legitimate integration/refactor is authorized during or after this plan, a strong ownership candidate additionally includes Ali's pre-change model + inspected diff/test + post-change explanation. That is **additional evidence**, not a compulsory reason to mutate code.
