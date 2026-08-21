# Plan 01 — Mastery and Depth Map

**Companion to:** `PLAN_01_S001_REAL_CASE_TO_FIRST_UPGRADEPILOT_EVIDENCE_MODELS.md`  
**Purpose:** define exactly what Ali should own, understand, navigate, or deliberately defer while completing Plan 01  
**Authority:** subordinate to the learning contract, live `MEMORY.md`, active source/tests, and the Plan 01 execution map  
**Important rule:** source-file size is not the learning target. **Engineering responsibility is the learning target.**

## 1. Depth labels used in this file

### OWN / MASTER

Ali should eventually be able to reconstruct the responsibility with reduced assistance:

```text
real input / precondition
→ owning source/function/type
→ material control flow
→ important success/problem branches
→ output/result
→ why the responsibility exists
→ what it does NOT prove
→ representative test meaning
```

OWN does **not** mean memorizing every line, helper, annotation, error string, or implementation detail. It means Ali can reopen the source and reason through the mechanism as an engineer rather than depending on an AI summary.

### STRONG WORKING UNDERSTANDING

Ali should know why the component exists, its important inputs/outputs and relevant branches, and be able to follow it when reading current source. Detailed internals are learned only when they carry the active responsibility.

### NAVIGATE / RECOGNIZE

Ali should know where the component lives, what role it plays in the data flow, and when to inspect it. No broad source ownership is required.

### OPERATIONAL BACKGROUND

Ali should understand the external concept/tool well enough to reason correctly about the real case, without mastering its implementation internals.

### DEFER

Do not spend learning capacity here unless a later real source/change/failure makes the detail causally necessary.

## 2. Plan-01 end-state in one sentence

By the end of Plan 01, Ali should be able to follow the real S001 dependency update from exact repository evidence through **one canonical dependency change + source context + one static project-environment selection**, while reading the central executable code and at least one representative test without treating the whole involved files as memorization targets.

The Plan-01 proof boundary remains:

```text
exact dependency/source evidence
→ canonical dependency change + source context
→ static workflow/environment selection

NOT YET:
selected-environment membership
CI consumption
runtime execution
coverage
compatibility/safety
```

## 3. Chunk 1 — S001 / Soup Sieve background

### MASTER

Ali should be able to explain:

- what Soup Sieve does at practical depth;
- its immediate relationship to Beautiful Soup;
- why it can appear in Pydantic's documentation/tooling dependency graph without being a normal Pydantic runtime dependency;
- direct versus transitive dependency at the depth needed by S001;
- why repository dependency relevance is not the same as core-runtime dependency relevance.

### OPERATIONAL BACKGROUND ONLY

- CSS selector semantics beyond what is needed to understand Soup Sieve's role;
- Beautiful Soup APIs;
- Pydantic documentation internals.

### DEFER

- Soup Sieve parser/selector-engine implementation;
- Beautiful Soup internals;
- unrelated Pydantic architecture.

## 4. Chunk 2 — uv / uv.lock background

### MASTER

Ali should be able to explain:

- why lockfiles exist;
- what `uv.lock` represents in this project context;
- why a package appearing in a universal lock does **not** establish that a particular environment selected or installed it;
- the exact S001 dependency path visible in the relevant lock evidence.

### OPERATIONAL BACKGROUND ONLY

- `uv` as a Python project/package/dependency environment tool;
- package records and dependency edges;
- dependency resolution at conceptual depth.

### DEFER

- uv resolver algorithms;
- lockfile generation internals;
- universal package-manager theory;
- every field in `uv.lock`.

## 5. Chunk 3 — CI / GitHub Actions / docs CI background

### MASTER

Ali should be able to explain:

- CI = Continuous Integration and the practical purpose of automated repository checks;
- workflow → job → step;
- `run:` versus `uses:` / `with:` at the level used by S001;
- why Pydantic has a documentation CI job;
- which S001 static command selects the docs environment;
- the critical boundary `static workflow definition != runtime execution evidence`.

### OPERATIONAL BACKGROUND ONLY

- GitHub Actions as the workflow/CI platform;
- checkout/setup actions used by the S001 job;
- runner/OS/Python setup only as far as they affect interpretation.

### DEFER

- full GitHub Actions expression language;
- matrices/reusable-workflow execution internals unless encountered later;
- generic CI-provider architecture.

## 6. Chunk 4 — Exact dependency transition + source context

This is the first major **source-ownership** section.

### `src/upgradepilot/dependency/uv_lock.py`

**OWN / MASTER — selected responsibility:** the **file-level exact uv.lock dependency-transition extraction responsibility**, centered on `extract_uv_lock_changes(...)`, `_build_source_evidence(...)`, and only the material parse/compare helpers needed to explain one supported exact transition or explicit problem result.

Ali should be able to reconstruct:

```text
ChangedFile + exact base/head RepositoryTextFile
→ validate admitted shape / exact source facts
→ parse relevant package/version evidence
→ compare base/head evidence
→ build exact source provenance
→ ExtractedDependencyVersionChange
   OR explicit DependencyChangeProblem
```

Material Python to master in context: typed signatures/result unions, dataclass evidence objects where semantic, early returns, `isinstance(...)` narrowing, assertions after type-state checks, typed-result construction, and helper-call flow.

**STRONG WORKING UNDERSTANDING:** the parser branches needed by the S001 supported case and one important ambiguity/problem case; unsupported/ambiguous source must not be guessed through; package normalization where it affects the transition.

**NAVIGATE / DEFER:** every regex/parser helper, every error string, every unused branch, every dataclass/type, imports/constants, and the whole file line by line. A helper becomes deeper only if the selected responsibility cannot be explained without it or later work enters it.

**Representative test:** `tests/test_uv_lock_change.py` — one supported transition/provenance case and one useful problem/ambiguity contrast.

### `src/upgradepilot/dependency/change.py`

**OWN / MASTER — reconciliation responsibility:** `DependencyChangeSourceEvidence`, `ExtractedDependencyVersionChange`, `DependencyVersionChange`, and `compare_extracted_dependency_changes(...)`.

Ali should understand:

```text
file-level extracted candidates
→ normalize / compare identity and transition
→ detect ambiguity/conflict
→ one canonical DependencyVersionChange
   OR explicit problem
```

Important questions: why a textual line change is not automatically the canonical PR-wide change; which ambiguity/conflict cases fail closed; what evidence identity remains attached; what the canonical result still does not prove.

**STRONG WORKING UNDERSTANDING:** collections/comprehensions only where they implement comparison semantics; result/problem unions; normalization that affects identity.

**DEFER:** memorizing every model field/helper or unrelated compatibility detail.

**Representative test:** `tests/test_dependency_change.py` or nearest current comparison-contract test.

### `src/upgradepilot/dependency/analysis.py`

**STRONG WORKING UNDERSTANDING — orchestration:** understand `analyze_dependency_change(...)` as the coordinator producing canonical dependency result + source contexts + transitional compatibility projection where present. Focus on supported source extractor invocation, candidate reconciliation, and `_source_contexts(...)`.

**NAVIGATE:** source families unrelated to S001 and compatibility properties not needed for the current data flow.

**Representative test:** `tests/test_dependency_analysis.py` — one combined dependency-result + source-context case.

### `src/upgradepilot/dependency/environment.py`

**OWN THE TYPE MEANING, NOT THE FILE:** own `UvLockDependencyContext` semantics—what source fact/provenance it represents and why it is context for later reasoning, not membership proof. Other context variants are navigation-only until their cases matter.

### `src/upgradepilot/github/repository.py`

**STRONG WORKING UNDERSTANDING — provider boundary:** understand repository + path + immutable revision, returned-path validation, blob SHA as content/provenance identity, reported versus decoded byte count, bounded file-size protection, and why provider validation precedes semantic parsing.

**NAVIGATE, NOT MASTER WHOLE CLIENT:** no need to master every GitHub HTTP path, auth/rate-limit internals, all client methods, transport-library behavior, or unrelated API responses.

## 7. Chunk 5 — Static workflow IR + environment selection

### `src/upgradepilot/github/workflow_definition.py`

**STRONG WORKING UNDERSTANDING:** understand the bounded workflow Intermediate Representation (IR) needed by the active path: `WorkflowDefinition`, steps-style job representation, `RunStepDefinition`, `RunDefaults` where working-directory matters, and `parse_workflow_definition(...)` only to the depth required to know which static shapes are admitted/rejected.

**NAVIGATE / DEFER:** full YAML parser behavior and every unsupported GitHub Actions construct.

### `src/upgradepilot/dependency/environment_selection.py`

**OWN / MASTER — selected responsibility:** static project-environment selection interpretation centered on `observe_project_environment_selection(...)`, `ProjectEnvironmentSelectionObservation`, `ProjectEnvironmentSelectionDeclaration`, and relevant `DependencyGroupSelector` / `OptionalExtraSelector` forms.

Ali should be able to explain:

```text
bounded static workflow run command
+ effective project/working-directory context
→ recognized project-environment selector
→ typed static selection declaration
```

and why that still does not establish execution or membership.

**STRONG WORKING UNDERSTANDING:** selector parsing/normalization where it changes interpretation and unresolved behavior for dynamic/unsupported command shapes.

**DEFER:** generic shell parsing, every pip/uv CLI option, and selector forms not required by a real case.

**Representative test:** `tests/test_project_environment_selection.py` — one S001-shaped selector case plus one unsupported/ambiguous contrast when useful.

### `src/upgradepilot/dependency/workflow_context.py`

**NAVIGATE / STRONG WORKING UNDERSTANDING ONLY WHERE NEEDED:** understand working-directory/path precedence only when it changes which project/configuration a run step refers to. Do not master the whole file unless later real work selects it.

## 8. Plan-01 Python language mastery

### MASTER IN CONTEXT

- function signatures and return-type unions;
- dataclasses used as typed evidence/results;
- practical meaning of `frozen=True` / `slots=True`;
- `isinstance(...)` type narrowing;
- guard clauses and early returns;
- assertions after prior state/type checks;
- typed object construction;
- `**mapping` unpacking where materially assembling evidence;
- small comprehensions/sets used for canonical comparison.

### OPERATIONAL / JUST-IN-TIME

- less common typing syntax not central to the responsibility;
- parser-specific Python tricks;
- incidental collection transformations.

The standard is: **Ali can read and explain the material Python with the repository open.** It is not: **Ali can recreate these files from memory.**

## 9. What Plan 01 must NOT become

Do not turn Plan 01 into whole-file memorization, a GitHub API course, a uv internals course, a YAML/TOML course, a complete dependency-parser implementation exercise, or a requirement to independently rewrite `uv_lock.py`, `change.py`, or `environment_selection.py`.

When a source file is large, ask:

> **Which responsibility in this file are we here to own?**

Then stop once that responsibility, important branches, representative test, and proof boundary are understood sufficiently.

## 10. Plan-01 completion evidence

Plan 01 is strong enough to hand to Plan 02 when Ali can, with reduced assistance:

1. explain S001 dependency/tooling context;
2. explain why lock presence does not prove selected-environment membership;
3. explain static workflow definition versus runtime execution;
4. reconstruct the selected `uv_lock.py` exact-transition extraction responsibility from executable source;
5. reconstruct canonical-change reconciliation in `change.py`;
6. explain how `analysis.py` preserves source context;
7. explain `UvLockDependencyContext` without treating it as membership proof;
8. trace the S001 run command through bounded workflow IR into the typed static environment selector;
9. explain at least one representative source-focused test at setup → action → assertion → protected behavior → non-proof depth;
10. state which large-file internals remain navigation-only or deliberately deferred.

A useful first Career-grade source candidate remains `src/upgradepilot/dependency/uv_lock.py` → exact file-level dependency-transition extraction. Plan completion itself does not promote Career capability; Career reassesses independently.