# UpgradePilot B2 Evidence-Pipeline Learning Session Plan

**Purpose:** Position-neutral learning plan for understanding, practising, and progressively owning the implemented UpgradePilot B2 evidence pipeline  
**Learning branch:** `agent/learning-current-implementation`  
**Baseline captured:** 2026-07-31 22:49 +03:30  
**Baseline commit:** `1181a4305bbd2489188e5a9a027113ac8c4d9ae8` (`Activate Step 2 support-drop validation`)  
**Latest learning-plan intake snapshot:** 2026-08-02 against `main` revision `9d09a669fe8f7ba31fdd326baa119f6ec2e1559a`  
**Live-state authority:** [`../../MEMORY.md`](../../MEMORY.md) on the actively developed `main` branch

## 1. Boundary

This file controls only the structure of this learning package. It does not control the live product stage, authorize implementation work, replace source and tests, or claim Ali's mastery.

The implementation was already moving while this package was created. Therefore:

- `main` remains the production-development branch;
- this branch isolates learning artifacts and bounded ownership practice;
- the baseline and intake snapshots above are dated references, not permanent statements of project position;
- actual behavior comes from inspected source, tests, commands, outputs, and environment evidence;
- live continuation remains exclusively owned by `MEMORY.md` on `main`.

The 2026-08-02 intake snapshot records only why the learning sequence below was updated. At that snapshot, Steps 1–3 had product-level validation evidence and Step 4 had been planned, implemented, and covered by controlled tests but still awaited the local validation gate recorded in `MEMORY.md`. That status must not be treated as current after `main` advances.

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
→ PEP 440 dependency/version and Python-line method
→ deterministic target-Python relevance mapping
→ later acquisition / extraction / orchestration responsibilities as they actually land
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
- trusted authority versus untrusted semantic candidate;
- PEP 440 parsed meaning versus raw evidence identity;
- target-declaration evidence versus downstream relevance mapping.

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
- a new bounded unit or subsection;
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

## 5. Implementation map for this learning package

The original branch baseline captured three connected boundaries. Later synchronized implementation now adds two more concrete boundaries that must be learned without erasing the original sequence.

### A. Dependency foundation

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
- [`../../src/upgradepilot/github_repository.py`](../../src/upgradepilot/github_repository.py)
- [`../../src/upgradepilot/ci_dependency_exercise.py`](../../src/upgradepilot/ci_dependency_exercise.py)
- [`../../src/upgradepilot/workflow_commands.py`](../../src/upgradepilot/workflow_commands.py)
- [`../../src/upgradepilot/cli.py`](../../src/upgradepilot/cli.py)

### B. Upstream interval authority

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

### C. Support-drop candidate grounding

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

The 2026-08-02 intake also captured a validated regression correction around Python-line quote-token boundaries. It belongs inside the existing grounding unit rather than creating a new architectural unit.

### D. Step 3 packaging/version and exact Python-line method

```text
DependencyReleaseInterval
→ PEP 440 parsed forward interval

ParsedDependencyReleaseInterval
+ already selected raw crossed-release versions
→ deterministic crossed-release ordering

canonical Python line X.Y
+ requires-python declaration
→ exact stable X.Y.Z witness / non-overlap
   or explicit method problem
```

Important files include:

- [`../../src/upgradepilot/packaging_method.py`](../../src/upgradepilot/packaging_method.py)
- [`../../tests/test_packaging_version_method.py`](../../tests/test_packaging_version_method.py)
- [`../../tests/test_python_line_specifier_method.py`](../../tests/test_python_line_specifier_method.py)
- [`../../tests/test_runtime_dependency_contract.py`](../../tests/test_runtime_dependency_contract.py)
- [`../../docs/architecture/ADR-0005-packaging-version-and-python-line-method.md`](../../docs/architecture/ADR-0005-packaging-version-and-python-line-method.md)
- [`../../plans/B2_STEP_3_PACKAGING_METHOD_PLAN.md`](../../plans/B2_STEP_3_PACKAGING_METHOD_PLAN.md)

### E. Step 4 target-Python relevance mapping

```text
UpstreamSupportDropClaimResult
├── unresolved problem
│   → upstream_claim_unresolved
│
└── GroundedPythonSupportDropClaim
    + TargetPythonEvidence
      ├── target problem
      │   → target_declaration_unresolved
      │
      └── TargetPythonDeclaration
          → Step 3 Python-line method
             ├── overlap
             ├── non-overlap
             └── explicit unresolved / unsupported mapping
```

Important files include:

- [`../../src/upgradepilot/target_python_relevance.py`](../../src/upgradepilot/target_python_relevance.py)
- [`../../tests/test_target_python_relevance.py`](../../tests/test_target_python_relevance.py)
- [`../../plans/B2_STEP_4_TARGET_PYTHON_RELEVANCE_PLAN.md`](../../plans/B2_STEP_4_TARGET_PYTHON_RELEVANCE_PLAN.md)
- [`../../working-memory/2026-08-01_B2-step-4-target-python-relevance-implementation.md`](../../working-memory/2026-08-01_B2-step-4-target-python-relevance-implementation.md)

This mapping is still intentionally narrower than compatibility, safety, or recommendation.

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

- `src/upgradepilot/dependency_analysis.py`
- `src/upgradepilot/github_repository.py`
- `src/upgradepilot/uv_lock_change.py`
- `tests/test_dependency_analysis.py`
- `tests/test_pull_request_repository_files.py`
- `tests/test_step8_source_recognition.py`
- `tests/test_exact_requirement_change.py`
- relevant CLI and package-interface tests

**Design-review companion:**

- `audits/2026-08-01_AUDIT-001_exact-pr-file-acquisition-evidence-contract.md`

Use the audit only after the exact base/head acquisition mechanism is understood. It is a non-controlling review artifact that asks which provenance fields are required, merely useful during validation, derivable, or plausibly useful later. It must not be treated as an instruction to refactor the current contract.

**Ali-owned evidence:**

- trace why both cases produce a canonical dependency change but different CI conclusions;
- after the mechanism is understood, classify at least two Audit-001 findings as current defect, accepted complexity, simplification opportunity, or future reassessment and explain why.

**Exit condition:** Ali can separate orchestration, source-specific interpretation, reconciliation, downstream evidence semantics, and a non-controlling audit recommendation.

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
- deterministic grounding versus later semantic extraction reliability;
- token-boundary precision: terminal punctuation after `Python 3.8.` may still ground line `3.8`, while a patch version such as `Python 3.8.1` must not be misread as the major/minor token `3.8`;
- the relevant regular-expression lookaround only at the depth required to explain that regression and its corrected boundary.

**Current regression to inspect:**

```text
"Drop support for Python 3.8."
→ may ground canonical line 3.8

"Drop support for Python 3.8.1."
→ must not ground canonical line 3.8
```

This regression was added after the original learning baseline and belongs directly to this unit.

**Ali-owned evidence:** Diagnose a deliberately introduced quote-span, Python-line, source-selector, interval-membership, or token-boundary defect.

**Exit condition:** Ali can explain what deterministic grounding proves, why token boundaries matter, and why exact grounding still does not prove arbitrary natural-language interpretation reliability.

## Unit 11 — Concrete post-baseline implementation intake

**Responsibility:** Learn the material implementation added to `main` after the original learning baseline without restarting earlier units.

### Unit 11A — Step 3 packaging/version method

**Owning product questions:**

```text
Are the raw old/proposed dependency versions a valid forward PEP 440 interval?

How should already selected crossed-release identities be ordered without losing raw identity?

Does requires-python admit at least one exact stable X.Y.Z version in a selected Python X.Y line?
```

**Core files:**

- `src/upgradepilot/packaging_method.py`
- `tests/test_packaging_version_method.py`
- `tests/test_python_line_specifier_method.py`
- `tests/test_runtime_dependency_contract.py`
- `docs/architecture/ADR-0005-packaging-version-and-python-line-method.md`
- `plans/B2_STEP_3_PACKAGING_METHOD_PLAN.md`

**Core concepts:**

- PEP 440 at the minimum depth needed for `Version` and `SpecifierSet`;
- raw evidence identity versus parsed semantic value;
- invalid, equivalent, and non-forward version intervals;
- deterministic ordering of already selected crossed releases;
- bounded runtime dependency `packaging>=26.2,<27` and why a dependency bound is part of the method contract;
- exact stable `X.Y.Z` product meaning;
- boundary-derived finite witness candidates rather than arbitrary patch enumeration;
- `contains(..., prereleases=False)` as the admitted exact-witness check;
- witness evidence versus evidence that an interpreter release was actually published;
- valid-but-unsupported specifier semantics versus invalid or contradictory declarations.

**Ali-owned evidence:**

- predict the result of one invalid/equivalent/non-forward dependency-version case;
- explain why `>=3.9.500000` does not require scanning patches `0..499999`;
- classify one valid-but-unsupported specifier separately from an invalid one;
- explain why finding `3.8.0` as a witness proves declaration overlap but not CPython publication or runtime compatibility.

**Exit condition:** Ali can trace one dependency-version method case and one Python-line witness case through source and tests and state the exact nonclaims.

### Unit 11B — Step 4 target-Python relevance mapping

**Owning product question:**

> Given one Step 2 support-drop result and, only when activated, one target Python declaration result, what bounded relevance state follows through the accepted Step 3 method?

**Core files:**

- `src/upgradepilot/target_python_relevance.py`
- `tests/test_target_python_relevance.py`
- `plans/B2_STEP_4_TARGET_PYTHON_RELEVANCE_PLAN.md`
- `working-memory/2026-08-01_B2-step-4-target-python-relevance-implementation.md`

**Core states:**

```text
declared_python_overlap
outside_declared_python_range
target_declaration_unresolved
upstream_claim_unresolved
comparison_unsupported
```

**Core concepts:**

- discriminated state mapping;
- conditional activation of target evidence;
- early return as an authority boundary, not merely a performance optimization;
- caller sequencing misuse (`ValueError`) versus ordinary evidence/method product states;
- single-owner validation: Step 4 consumes trusted Step 2 and target-parser records instead of duplicating their validation;
- nested evidence preservation instead of copying provenance/witness fields into a second representation;
- invalid/contradictory target declaration versus valid-but-unsupported comparison semantics;
- Step 3 problem ownership mapping;
- `relevance` as declared-range intersection only, not compatibility, safety, merge readiness, or recommendation.

**Key transfer cases:**

```text
Python line 3.8 drop + requires-python >=3.10
→ outside_declared_python_range

Python line 3.8 drop + requires-python >=3.8
→ declared_python_overlap

unresolved upstream claim + target_evidence None
→ upstream_claim_unresolved

unresolved upstream claim + target evidence supplied
→ caller sequencing error

valid but unsupported specifier
→ comparison_unsupported
```

**Ali-owned evidence:** Predict at least three changed mappings, explain why target evidence must not be admitted before a grounded upstream claim, and distinguish a product evidence state from caller misuse.

**Exit condition:** Ali can trace the linear Step 4 mapping, explain every state owner, and preserve the narrow relevance claim without promoting it to compatibility.

### Unit 11C — Future implementation intake after the current snapshot

For each later material boundary:

1. identify the owning product question;
2. compare the new source/test path with the last learned boundary;
3. identify reused contracts and newly introduced contracts;
4. classify prerequisites as required core, supporting operational, deferred core, or optional exploration;
5. add only the minimum new learning unit needed;
6. require one transfer prediction using a changed case.

Likely later topics under the parent route include:

- authoritative upstream acquisition;
- bounded semantic extraction adapter evaluation;
- conditional CLI orchestration;
- S001 end-to-end target relevance;
- later replay/persistence implications when they actually become active responsibilities.

Do not treat a planned future responsibility as implemented until source/tests and live state establish it.

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

Current reusable session records include:

- `2026-07-31-11pm-Session1.md` — original Step 7 introduction and first complete proving-path explanation;
- `2026-08-02-Session1-continuation.md` — demonstrated state classification, precedence, existential aggregation, claim-boundary reasoning, and initial function-signature mechanics.

## 8. Learning-depth checkpoint

The original package began with only an introduced Step 7 mental model. The dated continuation now records additional demonstrated evidence, including correct classification of `unresolved` versus `no_successful_ci`, precedence reasoning, existential aggregation, and claim-boundary discipline.

Do not convert that progress into blanket mastery. In particular, the following remain incomplete or only introduced until later evidence is recorded:

- full Unit 2 source trace;
- tuple/generator/`next(..., None)` mechanics;
- frozen/slotted dataclass rationale;
- bounded workflow-command reader ownership;
- canonical dependency reverse trace;
- exact base/head acquisition mechanics and Audit-001 design review;
- upstream interval and support-drop grounding ownership;
- Step 3 PEP 440/witness method ownership;
- Step 4 relevance-mapping ownership;
- Ali-authored meaningful source/test modification;
- independent end-to-end explanation and defect diagnosis.

Continue from the exact unfinished Unit 2 point after each synchronization rather than replaying already demonstrated Unit 1 reasoning unless a regression shows it is needed.
