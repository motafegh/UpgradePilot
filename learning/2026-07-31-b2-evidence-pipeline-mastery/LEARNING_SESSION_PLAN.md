# UpgradePilot B2 Evidence-Pipeline Learning Session Plan

**Purpose:** Position-neutral learning plan for understanding, practising, and progressively owning the implemented UpgradePilot B2 evidence pipeline  
**Learning branch:** `agent/learning-current-implementation`  
**Baseline captured:** 2026-07-31 22:49 +03:30  
**Baseline commit:** `1181a4305bbd2489188e5a9a027113ac8c4d9ae8` (`Activate Step 2 support-drop validation`)  
**Live-state authority:** [`../../MEMORY.md`](../../MEMORY.md) on the actively developed `main` branch

## 1. Boundary

This file controls only the structure of this learning package. It does not control the live product stage, authorize implementation work, replace source and tests, or claim Ali's mastery.

The implementation was already moving while this package was created. Therefore:

- `main` remains the production-development branch;
- this branch isolates learning artifacts and bounded ownership practice;
- the baseline above is a dated snapshot, not a permanent statement of project position;
- actual behavior comes from inspected source, tests, commands, outputs, and environment evidence;
- live continuation remains exclusively owned by `MEMORY.md` on `main`.

## 2. Learning objective

Build an accurate, transferable understanding of the active B2 request-to-evidence path, starting from the recently implemented CI dependency-exercise responsibility and tracing prerequisites backward only when they become necessary.

The learning path then follows the implementation forward into:

```text
canonical dependency change
→ exact-head CI dependency exercise
→ multi-format dependency coordination
→ authoritative upstream release interval
→ untrusted support-drop candidate
→ deterministically grounded support-drop claim
→ later target-Python relevance work
```

The goal is not passive familiarity. For central responsibilities, Ali should progressively become able to:

1. explain the product question and claim boundary;
2. predict results for changed evidence cases;
3. trace inputs through source and tests to outputs;
4. modify or add one meaningful test;
5. make one bounded implementation change when appropriate;
6. diagnose a deliberately introduced evidence, precedence, identity, or grounding defect;
7. explain what the result proves and explicitly does not prove.

## 3. SMARTLY operating method

### 3.1 Start from active responsibility

Begin with Step 7 CI dependency exercise because it is a compact, real product responsibility that connects domain evidence, GitHub Actions evidence, command inspection, aggregation, tests, package exports, and CLI presentation.

Do not replay all earlier steps chronologically before touching the active code.

### 3.2 Repair prerequisites just in time

When the selected code depends on an unfamiliar earlier concept:

```text
identify the exact missing link
→ explain why it blocks the selected responsibility
→ inspect only the owning source and tests
→ learn and practise the minimum complete mechanism
→ return explicitly to the selected responsibility
```

Examples include:

- `DependencyVersionChange`;
- base SHA versus head SHA;
- exact-revision repository evidence;
- requirements evidence versus CI installation proof;
- source-specific extraction behind one canonical model;
- trusted authority versus untrusted semantic candidate.

### 3.3 Use tests as executable claims

For each central behavior:

```text
product question
→ test fixture and expected result
→ public contract
→ implementation decision path
→ failure or abstention case
→ integration presentation
```

Do not read every source line equally. Prioritize state meanings, invariants, precedence, evidence authority, failure modes, and integration boundaries.

### 3.4 Require ownership evidence

An explanation, AI-written code, or passing test does not establish mastery. Each major unit must include at least one Ali-owned action: prediction, explanation, test design, modification, or diagnosis.

### 3.5 Stay synchronized without restarting

At the beginning of a material learning session:

1. inspect `main` branch `MEMORY.md`;
2. inspect commits and relevant source/test changes since the last learning sync;
3. classify the delta as unrelated, locally relevant, or architecture-changing;
4. incorporate locally relevant changes into the selected unit;
5. revise this plan only when the learning sequence or ownership proof materially changes.

A new implementation does not automatically restart the course. It becomes either:

- a small delta inside an existing unit;
- a new bounded unit;
- or a reason to replace a no-longer-accurate learning exercise.

## 4. Branch discipline

### Default change boundary

Keep routine learning records under:

```text
learning/2026-07-31-b2-evidence-pipeline-mastery/
```

Do not update root `MEMORY.md` from this branch merely to record learning progress.

### Code practice

Use the least disruptive mechanism that still proves ownership:

1. prediction or explanation without a repository change;
2. a focused exercise or test design inside this learning package;
3. a real test modification on the learning branch when integration behavior matters;
4. an active source modification only when the learning objective requires real implementation practice.

Practice-only active source or test changes must be committed separately and identified as practice. Before merging the branch, either:

- revert them with ordinary commits; or
- retain them only when they independently improve the product, match the then-current controlling plan, and pass the required tests.

Do not force-push or rewrite history to hide practice.

### Synchronizing from `main`

When relevant production changes accumulate, bring `main` into the learning branch before continuing implementation-adjacent work. Prefer a normal merge from `main`; do not rebase published learning history or force-update the branch.

Before eventual merge back:

- compare the branch against the latest `main`;
- separate reusable learning artifacts from practice-only code;
- resolve stale references and conflicts;
- run applicable checks for any retained source or test changes;
- review the complete diff;
- merge only after Ali explicitly approves the final scope.

## 5. Baseline implementation map

The branch baseline contains three connected implementation boundaries that must be covered.

### A. Behavior-validated dependency foundation

```text
requirements / constraints / uv.lock
→ source-specific extraction
→ PR-wide reconciliation
→ canonical DependencyVersionChange
   or explicit evidence problem
→ CI, package, upstream, and target consumers
```

Important files include:

- [`../../src/upgradepilot/dependency_change.py`](../../src/upgradepilot/dependency_change.py)
- [`../../src/upgradepilot/dependency_analysis.py`](../../src/upgradepilot/dependency_analysis.py)
- [`../../src/upgradepilot/exact_requirement_change.py`](../../src/upgradepilot/exact_requirement_change.py)
- [`../../src/upgradepilot/uv_lock_change.py`](../../src/upgradepilot/uv_lock_change.py)
- [`../../src/upgradepilot/ci_dependency_exercise.py`](../../src/upgradepilot/ci_dependency_exercise.py)
- [`../../src/upgradepilot/workflow_commands.py`](../../src/upgradepilot/workflow_commands.py)
- [`../../src/upgradepilot/cli.py`](../../src/upgradepilot/cli.py)

### B. Behavior-validated upstream interval authority

```text
DependencyVersionChange
→ old-exclusive / proposed-inclusive DependencyReleaseInterval
+ exact trusted upstream source records
→ AuthoritativeUpstreamIntervalEvidence
   or UpstreamIntervalAuthorityProblem
```

Important files include:

- [`../../src/upgradepilot/upstream_interval.py`](../../src/upgradepilot/upstream_interval.py)
- [`../../tests/test_upstream_interval.py`](../../tests/test_upstream_interval.py)
- [`../../tests/test_upstream_interval_authority_edges.py`](../../tests/test_upstream_interval_authority_edges.py)

### C. Implemented support-drop candidate grounding

```text
AuthoritativeUpstreamIntervalEvidence
+ untrusted CandidateUpstreamClaimResult
→ GroundedPythonSupportDropClaim
   or UpstreamSupportDropClaimProblem
```

Important files include:

- [`../../src/upgradepilot/upstream_claim.py`](../../src/upgradepilot/upstream_claim.py)
- [`../../tests/test_upstream_claim.py`](../../tests/test_upstream_claim.py)
- [`../../tests/test_upstream_claim_edges.py`](../../tests/test_upstream_claim_edges.py)

At the captured baseline, this responsibility had been implemented and its validation step activated. That statement is historical to the baseline; consult `main` for later results.

## 6. Learning sequence

A numbered unit is not necessarily one calendar session. Combine small units or split a dense unit according to demonstrated comprehension and concentration.

## Unit 1 — CI dependency-exercise product question

**Responsibility:** Understand exactly what Step 7 classifies.

**Core concepts:**

- Continuous Integration (CI);
- exact-head workflow evidence;
- dependency consumption versus package exercise;
- admitted deterministic rule;
- `proven`, `no_successful_ci`, and `unresolved`;
- narrow proof versus compatibility, safety, or merge claims.

**Core files:**

- `src/upgradepilot/ci_dependency_exercise.py`
- `tests/test_ci_dependency_exercise.py`

**Ali-owned evidence:**

- classify several changed scenarios without reading expected assertions;
- explain why green CI can still be `unresolved`;
- explain why `no_successful_ci` is not a generic failure state.

**Exit condition:** Ali can state the exact product question, distinguish all three states, and identify the prohibited conclusions.

## Unit 2 — One complete `proven` path

**Responsibility:** Trace one successful case from fixture to result.

**Path:**

```text
DependencyVersionChange
+ WorkflowDependencyExerciseInput
+ explicit requirements path
→ per-workflow evaluation
→ command inspection
→ WorkflowDependencyExerciseResult
→ overall DependencyCIExerciseResult
```

**Concepts and Python mechanisms:**

- `Literal` state vocabularies;
- frozen slotted dataclasses;
- keyword-only arguments;
- tuples and `Sequence`;
- generator expressions and `next(..., None)`;
- separation between per-workflow and aggregate results.

**Ali-owned evidence:** Explain each input's authority and predict which condition fails when one item is changed.

**Exit condition:** Ali can trace the proving test through the evaluator without relying on line-by-line prompting.

## Unit 3 — Decision order, precedence, and aggregation

**Responsibility:** Understand why condition order is part of product meaning.

**Cases:**

- no workflow inputs;
- no completed successful job;
- successful job with unsuccessful run;
- unavailable workflow definition;
- revision mismatch;
- missing explicit requirements path;
- unsupported command structure;
- one proven workflow plus weaker workflows.

**Ali-owned evidence:** Design a decision table and predict results for at least two mixed-workflow cases.

**Exit condition:** Ali can explain execution absence versus proof insufficiency and existential overall proof while retaining all workflow evidence.

## Unit 4 — The bounded workflow-command reader

**Responsibility:** Understand the intentionally narrow YAML/shell text reader and its abstention boundary.

**Core files:**

- `src/upgradepilot/workflow_commands.py`
- `tests/test_workflow_commands.py`
- relevant negative cases in `tests/test_ci_dependency_exercise.py`

**Concepts:**

- shallow indentation-based reading versus complete YAML parsing;
- regular expressions and named groups;
- block and inline `run:` extraction;
- shell segmentation;
- direct `pip install -r` recognition;
- direct package invocation and supported wrappers;
- why multiple jobs, tox indirection, scripts, variables, and reusable workflows remain unresolved.

**Ali-owned evidence:** Add or design one supported case and one unresolved case, then explain which claim would become unsafe if the reader guessed.

**Exit condition:** Ali can explain the supported grammar, implementation mechanics, and replacement cliff without calling the module a general parser.

## Unit 5 — Reverse trace to canonical dependency identity

**Responsibility:** Learn the prerequisite that Step 7 consumes without restarting from project history.

**Core concepts:**

- canonical `DependencyVersionChange`;
- package normalization;
- exact old and proposed version identity;
- `DependencyFileEvidence`;
- source-specific extraction;
- trusted result versus explicit evidence problem;
- dependency evidence path versus operational CI installation path.

**Core files and tests:**

- `dependency_change.py`
- `exact_requirement_change.py`
- `uv_lock_change.py`
- their focused tests

**Ali-owned evidence:** Explain why `uv.lock` or a constraints path may establish dependency identity without automatically establishing CI consumption.

**Exit condition:** Ali can state where the canonical model comes from, what it guarantees, and what it intentionally does not guarantee.

## Unit 6 — Step 8 multi-format coordinator and public-case contrast

**Responsibility:** Understand how materially different dependency formats enter one downstream pipeline.

**Core path:**

```text
changed-file evidence
→ source recognition
→ patch-based requirements/constraints extraction
   or exact base/head uv.lock acquisition and comparison
→ PR-wide reconciliation
→ canonical result/problem
→ downstream consumers
```

**Cases:**

- S004: `requirements-dev.txt`, `pytest 9.0.2 → 9.0.3`, CI exercise `proven`;
- S001: `uv.lock`, `soupsieve 2.6 → 2.8.4`, CI exercise `unresolved` without inferred lockfile consumption.

**Core files and tests:**

- `dependency_analysis.py`
- `tests/test_dependency_analysis.py`
- `tests/test_step8_source_recognition.py`
- `tests/test_exact_requirement_change.py`
- relevant CLI and package-interface tests

**Ali-owned evidence:** Trace why both cases produce a canonical dependency change but different CI conclusions.

**Exit condition:** Ali can separate orchestration, source-specific interpretation, reconciliation, and downstream evidence semantics.

## Unit 7 — Request-to-output integration

**Responsibility:** Trace the public command through the active pipeline.

**Core files:**

- `cli.py`
- `__init__.py`
- GitHub acquisition modules used by the path
- package, upstream, target, and provenance modules reached by the CLI
- `tests/test_cli.py`
- `tests/test_package_interface.py`

**Concepts:**

- acquisition versus interpretation;
- exact identity and provenance;
- independent evidence boundaries;
- why one unresolved subsystem does not erase independently established evidence;
- CLI labels as public contracts;
- package exports as supported API surface.

**Ali-owned evidence:** Produce a request-to-output map and identify where each visible line obtains its authority.

**Exit condition:** Ali can explain the complete current command path at implementation-adjacent depth, including major stop and abstention points.

## Unit 8 — Upstream release-interval authority

**Responsibility:** Understand why one final release body may not cover the complete crossed-version interval.

**Core files:**

- `upstream_interval.py`
- `tests/test_upstream_interval.py`
- `tests/test_upstream_interval_authority_edges.py`

**Concepts:**

- old-version-exclusive and proposed-version-inclusive interval;
- raw interval identity versus PEP 440 ordering;
- trusted crossed-release index;
- exact GitHub Release body;
- exact proposed-tag changelog provenance;
- package metadata as corroboration only;
- authority basis;
- complete coverage, recoverable unavailability, and severe contradiction.

**Ali-owned evidence:** Explain why a proposed-version release body alone can produce `interval_incomplete`, and classify several source combinations.

**Exit condition:** Ali can distinguish source identity, interval coverage, corroboration, and semantic interpretation.

## Unit 9 — Candidate output versus trusted support-drop evidence

**Responsibility:** Understand the two-layer semantic boundary.

**Core files:**

- `upstream_claim.py`
- `tests/test_upstream_claim.py`
- `tests/test_upstream_claim_edges.py`

**Concepts:**

- untrusted `CandidateUpstreamClaimResult`;
- echoed dependency-context validation;
- candidate state invariants;
- admitted category and direction;
- canonical Python major/minor text;
- source resolution rather than candidate-provided authority;
- trusted crossed-release membership;
- grounded output versus explicit problem.

**Ali-owned evidence:** Explain why schema-valid structured output remains untrusted and predict which validation boundary rejects several malformed candidates.

**Exit condition:** Ali can trace an untrusted candidate into either a grounded claim or an exact stopping state.

## Unit 10 — Exact quote grounding, ambiguity, and evidence aggregation

**Responsibility:** Understand the strongest deterministic links around semantic candidates.

**Concepts:**

- exact quote offsets;
- unchanged source text;
- quote-to-Python-line token grounding;
- release-body versus tagged-changelog source identity;
- equivalent evidence combination and deduplication;
- one invalid candidate blocking partial success;
- several distinct claim identities producing ambiguity;
- deterministic grounding versus later semantic extraction reliability.

**Ali-owned evidence:** Diagnose a deliberately introduced quote-span, Python-line, source-selector, or interval-membership defect.

**Exit condition:** Ali can explain what deterministic grounding proves and why it still does not prove arbitrary natural-language interpretation reliability.

## Unit 11 — Intake of later implementation

**Responsibility:** Incorporate implementation added to `main` after the branch baseline without losing the established mental model.

For each material new boundary:

1. identify the owning product question;
2. compare the new source/test path with the last learned boundary;
3. identify reused contracts and newly introduced contracts;
4. classify prerequisites as required core, supporting operational, deferred core, or optional exploration;
5. add only the minimum new learning unit needed;
6. require one transfer prediction using a changed case.

Likely future topics under the captured parent plan include:

- accepted `packaging` and PEP 440 method;
- deterministic target-Python line overlap;
- authoritative upstream acquisition;
- bounded semantic extraction adapter evaluation;
- conditional CLI orchestration;
- S001 end-to-end target relevance.

These topics are not treated as implemented merely because the parent plan names them.

## Unit 12 — Ownership assessment and branch integration

**Responsibility:** Demonstrate transferable control rather than immediate recall.

Minimum assessment evidence:

- explain the complete learned request-to-evidence path;
- predict a changed case not copied from existing tests;
- add or materially change one meaningful test;
- make or review one bounded implementation change;
- diagnose one deliberate defect;
- identify permission, evidence-authority, stopping, and claim boundaries;
- distinguish validated product behavior from personal learning depth.

Depth labels must remain accurate:

- introduced;
- operationally understood with guidance;
- implementation-adjacent;
- ownership practice;
- independently demonstrated.

Before branch integration, classify every branch change as:

```text
reusable learning artifact
merge-eligible product improvement
practice-only change to revert
stale or conflicting material to revise
```

The branch is merge-ready only when the final diff is intentional, public-safe, consistent with the then-current controlling project state, and any retained code changes have the required validation evidence.

## 7. Session record format

Create a dated session artifact only when reusable understanding or material ownership evidence would otherwise be lost. A concise record should contain:

```text
responsibility
baseline commit or compared delta
minimum mental model
source and tests inspected
Ali prediction, explanation, modification, or diagnosis
observed evidence
correction or remaining uncertainty
demonstrated depth
explicitly deferred depth
```

Do not turn every conversation into a document. Do not duplicate live continuation from `MEMORY.md`.

## 8. Initial depth statement

At package creation, the CI dependency-exercise responsibility had received one structured introductory explanation in conversation. That establishes only an introduced mental model. It does not establish code ownership, independent prediction, test modification, diagnosis, or mastery.

The learning sequence therefore begins from the Step 7 product question but will re-check understanding through prediction before advancing into source-level ownership.
