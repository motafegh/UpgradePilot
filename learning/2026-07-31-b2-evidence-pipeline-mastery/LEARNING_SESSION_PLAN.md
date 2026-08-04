# UpgradePilot B2 Evidence-Pipeline Learning Session Plan

**Purpose:** Position-neutral learning plan for understanding, practising, reviewing, and progressively owning the implemented UpgradePilot B2 evidence pipeline  
**Learning branch:** `agent/learning-current-implementation`  
**Original baseline:** `1181a4305bbd2489188e5a9a027113ac8c4d9ae8` — original early B2 learning baseline  
**Latest architecture intake:** 2026-08-04 against `main` revision `f0096c5547304e4bb2e75c3f5a5ba175b4ca7e0a`  
**Major architecture sync:** PR #20, merge commit `b0451f3cf797aa50d907f9b335f0c8fc31c6658a`  
**Latest documentation follow-up sync:** PR #21, merge commit `87067ccd912087f8d04b6f06f30ea7d9ad5e1127`, through `main` revision `523360e85fd7541bbf91fd013e9f48f2c68703c8`  
**Current durable checkpoint:** `2026-08-04-main-architecture-reconciliation-intake.md`  
**Live product-state authority:** [`../../MEMORY.md`](../../MEMORY.md) on `main`

## 1. Boundary

This file controls only the structure and progress of this learning package.

It does **not**:

- control live product continuation;
- authorize implementation work on `main`;
- replace source/tests as behavior truth;
- replace formal audits, specifications, or ADRs;
- imply mastery because product code is behavior-validated;
- require restarting completed learning whenever `main` advances.

The learning branch isolates educational artifacts, source review, bounded design debate, and later ownership practice while `main` continues product development.

Dated learning notes are historical snapshots. Do not rewrite their old module paths merely because ADR-0007 later moved active source.

## 2. Latest architecture intake

The 2026-08-04 synchronized intake records a major repository evolution:

```text
accepted ADR-0007 responsibility-based subpackages
source reconciliation completed and behavior-validated
Step 6 bounded semantic extractor adopted for its narrow role
Step 7A exact-commit changelog discovery behavior-validated
Step 7B selected in live product state at the intake snapshot
```

Follow-up architecture documentation clarifies that executable repository areas have distinct responsibilities:

```text
src/upgradepilot/  → installable product runtime only
tests/             → active deterministic product regression
experiments/       → non-product research/evaluation/calibration
experiments/tests/ → experiment machinery regression, not product coverage
tools/             → developer-operated diagnostics/live proofs/maintenance
```

This delta changes **where responsibilities live** and the later learning map.

It does **not** invalidate the CI mechanics already learned because inspection of the reconciled source shows the same material CI decision algorithm remains in:

```text
src/upgradepilot/ci/dependency_exercise.py
src/upgradepilot/ci/workflow_commands.py
```

Therefore Units 1–4 continue rather than restart.

## 3. Responsibility-based architecture mental model

The accepted active source organization is:

```text
upgradepilot/
├── ci/          → workflow-command reading and dependency-exercise interpretation
├── dependency/  → dependency-change contracts, extraction, coordination, version ordering
├── github/      → GitHub acquisition and exact GitHub identity
├── pypi/        → PyPI release/index/provenance acquisition
├── upstream/    → upstream repository, interval authority, evidence composition, claim grounding
├── target/      → target Python declaration, specifier semantics, relevance
├── investigation.py → application orchestration
└── cli.py            → interface/presentation/exit policy
```

Cross-domain source-neutral primitives remain precisely named at package root:

```text
package_identity.py
repository_path.py
json_contract.py
```

The architecture deliberately rejects generic buckets such as `services/`, `managers/`, `helpers/`, or `common/` without demonstrated responsibility.

### Architecture-orientation checklist

These items are covered only at **introduced** depth unless later units demonstrate ownership:

- [x] responsibility-based subpackages versus flat module layout
- [x] module location communicates ownership
- [x] provider responsibility versus domain interpretation
- [x] precise internal imports rather than giant root re-export façade
- [x] `upgradepilot.__init__` intentionally minimal
- [x] architecture/topology invariants can be protected by tests
- [x] `investigation.py` separates application orchestration from CLI presentation
- [x] active product tests versus completed experiment/harness tests are separate proof sets
- [x] `src/upgradepilot/`, `experiments/`, and `tools/` are different executable trust/lifecycle boundaries
- [x] product runtime must not depend on experiments/tests/tools
- [x] shared implementation library does not imply shared domain responsibility (`packaging_method.py` split)
- [ ] independently reconstruct the full responsibility map without prompts
- [ ] independently explain one migration trade-off and its proof requirement

Reinforce these ideas just-in-time as later units visit each owner. Do not create a separate architecture lecture before finishing the active CI responsibility.

## 4. Learning objective

Build transferable ownership of the B2 request-to-evidence path rather than memorize files chronologically.

The learning path is:

```text
exact-head CI dependency-exercise evidence
→ canonical dependency identity
→ multi-format dependency coordination
→ application/request-to-output orchestration
→ authoritative upstream crossed-release interval
→ untrusted semantic candidate
→ deterministic support-drop grounding
→ dependency-version / target-Python specifier methods
→ deterministic target-Python relevance
→ live upstream acquisition
→ bounded semantic extraction
→ Step 7 deterministic/runtime bridges
→ ownership assessment
```

For central responsibilities, progressively demonstrate the ability to:

1. state the exact product question;
2. identify authority and identity boundaries;
3. predict changed-case outcomes;
4. trace inputs through source/tests to outputs;
5. distinguish evidence absence, unresolved proof, contradiction, and internal defect;
6. challenge a design without confusing a bounded rule with an implementation bug;
7. add or materially alter one meaningful test;
8. make/review one bounded implementation change when appropriate;
9. diagnose a deliberately introduced defect;
10. state exactly what the result proves and does not prove.

## 5. Learning method

### 5.1 Learn from the active responsibility

The first deep anchor remains CI dependency exercise because it connects:

```text
domain identity
GitHub Actions evidence
exact revision identity
workflow text interpretation
aggregation
abstention
public diagnostics
```

Do not replay the project from Step 0 before finishing this responsibility.

### 5.2 Repair prerequisites just in time

```text
identify exact missing prerequisite
→ inspect only its owner
→ learn minimum accurate mechanism
→ make one transfer prediction
→ return to active responsibility
```

### 5.3 Use tests as executable claims

```text
product question
→ fixture/evidence
→ expected state
→ public contract
→ implementation path
→ negative/abstention branch
→ caller/output effect
```

### 5.4 Keep learning and review coupled

```text
understand mechanism
→ predict behavior
→ challenge design
→ classify observation
→ preserve material review item
→ continue learning
```

Use `LIVE_LEARNING_AND_REVIEW_NOTES.md` for provisional material observations.

Do not create a formal audit until consequence, contract, source/test boundary, and proof requirement are established.

### 5.5 Product validation is not learning mastery

Depth labels remain:

```text
introduced
operationally understood with guidance
implementation-adjacent
ownership practice
independently demonstrated
```

A passing product suite or live proof establishes product behavior, not personal mastery.

## 6. Progress-marking rule

```text
[x] = covered to the intended current learning depth for that item
[ ] = not yet covered enough to treat as complete
```

A checked concept does not automatically mean mastery.

A unit closes only when its exit condition and user-owned evidence are satisfied.

---

# 7. Current learning position

Current active source:

```text
src/upgradepilot/ci/workflow_commands.py
```

Exact continuation:

```text
_extract_job_definitions(...)
→ continue after locating plain `jobs:` and recording `jobs_index` / `jobs_indent`
→ direct child-job discovery
→ sibling job-body slicing
→ _extract_run_commands(...)
```

Current unit status:

```text
Unit 1 — complete at operational depth
Unit 2 — evaluator mechanics mostly covered; independent full-trace ownership gate open
Unit 3 — core precedence/aggregation covered; independent decision-table gate open
Unit 4 — active; command matchers covered, YAML/job extraction mechanics remain
Units 5+ — not yet learned in this package
```

Do not jump to the live product's later Step 7 responsibility merely because implementation is ahead of learning.

---

# 8. Learning sequence

## Unit 1 — CI dependency-exercise product question

**Status:** complete at current operational depth.

**Current owners:**

```text
src/upgradepilot/ci/dependency_exercise.py
tests/test_ci_dependency_exercise.py
```

### Concept checklist

- [x] Continuous Integration (CI) practical meaning in this path
- [x] exact-head workflow evidence
- [x] dependency consumption versus package exercise
- [x] admitted deterministic rule versus generic green CI
- [x] `proven`
- [x] `no_successful_ci`
- [x] `unresolved`
- [x] successful CI can still be unresolved
- [x] no-successful-CI does not mean dependency exercise was disproved
- [x] narrow dependency-exercise proof versus compatibility/safety/merge claims

**Ali-owned evidence already observed:** changed-state predictions, execution-absence versus proof-insufficiency distinction, and refusal to promote CI proof into compatibility.

**Exit condition:** satisfied at current operational depth.

---

## Unit 2 — One complete `proven` path

**Status:** in progress.

### Product path

```text
DependencyVersionChange
+ WorkflowDependencyExerciseInput
+ explicit direct-requirements install path
→ per-workflow gates
→ inspect_workflow_commands(...)
→ WorkflowDependencyExerciseResult
→ aggregate DependencyCIExerciseResult
```

### Concept/Python checklist

- [ ] `Literal` as type-level state vocabulary independently explained
- [ ] frozen dataclass rationale
- [ ] `slots=True` rationale
- [ ] keyword-only `*` independently demonstrated
- [ ] `Sequence[...]` interface contract independently demonstrated
- [x] tuple materialization
- [x] generator expression mechanics at current use sites
- [x] `next(..., None)` as first-witness selection
- [x] `any(...)` as Boolean existence check
- [x] `None` as expected absence marker
- [x] per-workflow versus aggregate result responsibility
- [x] all workflows evaluated before first-witness search
- [x] one existential witness can determine aggregate `proven`
- [x] all per-workflow results remain preserved
- [x] internal invariant `assert` versus ordinary unresolved evidence
- [x] `state` / `reason` / `detail` / evidence payload roles

### Ownership gate

- [ ] trace a complete proving test through the evaluator without line-by-line prompting
- [ ] explain each major input's authority from memory

**Exit condition:** not yet satisfied.

---

## Unit 3 — Decision order, precedence, and aggregation

**Status:** core cases covered; ownership gate open.

### Case checklist

- [x] no workflow inputs
- [x] no completed-successful job
- [x] successful child job with unsuccessful parent run
- [x] unavailable workflow definition
- [x] workflow-definition revision mismatch
- [x] missing explicit direct-requirements install path
- [x] successful CI but no admitted dependency-exercise proof
- [x] one proven workflow plus weaker workflows
- [x] per-workflow versus aggregate no-success reasons
- [x] `AND` success condition versus `OR` rejection condition
- [x] earlier `return` prevents later gates from executing

### Ownership gate

- [ ] independently reconstruct the decision table
- [ ] predict at least two new mixed-workflow cases without prompting
- [ ] explain aggregate precedence and nonclaims end to end

---

## Unit 4 — Bounded workflow-command reader

**Status:** active.

**Current owner:**

```text
src/upgradepilot/ci/workflow_commands.py
```

**Relevant tests:**

```text
tests/test_workflow_commands.py
tests/test_ci_dependency_exercise.py
```

### Reader architecture checklist

- [x] shallow indentation reader versus complete YAML parser
- [x] `_WorkflowJobDefinition` preserves only job key + visible command tuple
- [x] `jobs is None` versus zero readable jobs distinction
- [x] exactly-one-job current restriction
- [x] why install in Job A + execution in Job B must not be combined automatically
- [x] design challenge: one self-contained proving job inside a multi-job workflow could be evaluated without cross-job inference
- [x] `splitlines()` keeps indentation signal while removing newline characters
- [x] `jobs_index` and `jobs_indent` roles
- [x] blank/comment skipping during `jobs:` search
- [x] exact plain `jobs:` recognition
- [x] indentation calculation using `len(line) - len(line.lstrip())`
- [x] missing readable `jobs:` mapping returns `None`
- [ ] direct child-job scan after `jobs:`
- [ ] first child establishes sibling `job_indent`
- [ ] nested keys ignored as jobs
- [ ] sibling job-body slicing
- [ ] inline `run:` extraction mechanics
- [ ] block `run: |` / `run: >` extraction mechanics
- [ ] `_RUN_PATTERN` named groups
- [ ] `_JOB_KEY_PATTERN` named groups

### Command-evidence checklist

- [x] one-job command tuple at conceptual level
- [x] separate install witness and execution witness searches
- [x] partial evidence preserved on unresolved result
- [x] success requires both install + invocation witnesses
- [x] direct `pip install -r` / `--requirement` concept
- [x] exact admitted requirements path comparison
- [x] superficial path normalization (`./`, backslash→slash)
- [x] path normalization applies to extracted path identity, not the whole command
- [ ] `_PIP_INSTALL_PATTERN` regex mechanics
- [ ] `_REQUIREMENT_PATTERN` regex mechanics
- [x] shell segmentation practical meaning
- [x] `_command_invokes_package(...)` responsibility
- [x] package + normalized-package candidate set
- [x] set comprehension lowercase/deduplication role
- [x] candidate token grammar via `re.fullmatch(...)`
- [x] supported prefixes/wrappers (`python -m`, `uv run`, `poetry run`, `pipenv run`, `coverage run -m`)
- [x] leading shell environment-variable assignment stripping
- [x] invocation must begin at shell-segment start
- [x] whitespace/end token boundary behavior
- [x] `re.escape(expected)` literalizes dynamic expected invocation
- [x] `re.IGNORECASE` case-insensitive matching
- [x] tox/script/alias/function/custom-action/reusable-workflow non-inference at conceptual level
- [x] current reader checks install existence + execution existence independently
- [x] current reader does **not** enforce install-before-execution order

### Design-review companions

Already formalized:

```text
audits/2026-08-02_AUDIT-002_ci-dependency-exercise-proof-boundary.md
```

Open provisional review items:

```text
LR-001 — aggregate detail names first proof witness only
LR-002 — exactly-one-job restriction is stricter than same-job existential proposition
```

These remain relevant after ADR-0007 because the reconciled CI algorithm preserves those behaviors.

### Ownership gate

- [ ] design one new supported reader case
- [ ] design one new unresolved reader case
- [ ] explain which inference would become unsafe if the reader guessed
- [ ] optionally implement one focused test after full mechanics are understood

**Exit condition:** not yet satisfied.

---

## Unit 5 — Canonical dependency identity

**Status:** not started.

**Current owners:**

```text
src/upgradepilot/dependency/change.py
src/upgradepilot/dependency/requirements.py
src/upgradepilot/dependency/uv_lock.py
src/upgradepilot/dependency/analysis.py
```

### Checklist

- [ ] `DependencyVersionChange`
- [ ] extracted source-specific change versus PR-wide canonical result
- [ ] package normalization and PEP 503 identity owner
- [ ] exact old/proposed version identity
- [ ] requirements/constraints extraction
- [ ] uv.lock extraction
- [ ] trusted change versus explicit problem
- [ ] dependency evidence path versus operational CI-install path
- [ ] why transition-era `PinnedDependencyChange` runtime compatibility was removed

**Ali-owned evidence:** explain why a dependency source can establish canonical change identity without automatically proving CI consumption.

---

## Unit 6 — Multi-format dependency coordination and S004/S001 contrast

**Status:** not started.

**Primary owner:** `src/upgradepilot/dependency/analysis.py`.

### Path

```text
changed files
→ source recognition
→ source-specific extraction
→ ExtractedDependencyVersionChange | problem
→ PR-wide comparison/reconciliation
→ DependencyVersionChange | problem
```

### Checklist

- [ ] source recognition
- [ ] requirements/constraints path
- [ ] exact base/head uv.lock path
- [ ] reconciliation
- [ ] conflict/multiple/incomplete states
- [ ] representation-neutral downstream contract
- [ ] S004 versus S001 transfer explanation

**Design-review companion:** AUDIT-001 only after exact-file mechanics are understood.

---

## Unit 7 — Application request-to-output integration

**Status:** not started.

This unit changed materially under ADR-0007.

### Current application split

```text
CLI locator/input
→ investigate_public_pull_request(...)
→ PublicPullRequestInvestigation
→ CLI rendering / exit policy
```

### Current owners

```text
src/upgradepilot/investigation.py
src/upgradepilot/cli.py
src/upgradepilot/github/*
src/upgradepilot/dependency/*
src/upgradepilot/ci/*
src/upgradepilot/pypi/*
src/upgradepilot/upstream/*
src/upgradepilot/target/*
```

### Checklist

- [ ] application orchestration versus interface/presentation
- [ ] client construction/dependency injection
- [ ] acquisition versus interpretation boundaries
- [ ] exact identity/provenance joins
- [ ] independent unresolved subsystems
- [ ] typed investigation result
- [ ] CLI labels/output as public contract
- [ ] package root intentionally not used as internal façade
- [ ] request-to-output authority map

---

## Unit 8 — Upstream release-interval authority

**Status:** not started.

### Current owners

```text
src/upgradepilot/upstream/interval.py
src/upgradepilot/upstream/interval_evidence.py
src/upgradepilot/github/release.py
src/upgradepilot/github/tag.py
src/upgradepilot/github/repository.py
src/upgradepilot/pypi/release.py
```

### Checklist

- [ ] old-exclusive / proposed-inclusive interval
- [ ] raw identity versus semantic version ordering
- [ ] trusted crossed-release index
- [ ] release-body authority
- [ ] exact proposed-tag changelog authority
- [ ] package metadata corroboration only
- [ ] authority basis
- [ ] interval incomplete versus unavailable versus contradiction

---

## Unit 9 — Untrusted candidate versus trusted support-drop claim

**Status:** not started.

**Owner:** `src/upgradepilot/upstream/claim.py`.

### Checklist

- [ ] `CandidateUpstreamClaimResult` is untrusted
- [ ] dependency-context identity validation
- [ ] category/direction admission
- [ ] canonical Python X.Y
- [ ] introduced-release membership
- [ ] trusted source selector
- [ ] exact quote/span grounding
- [ ] grounded claim versus explicit claim problem
- [ ] schema-valid output does not mean semantically trusted

---

## Unit 10 — Quote grounding, ambiguity, and evidence aggregation

**Status:** not started.

### Checklist

- [ ] quote offsets
- [ ] unchanged source text
- [ ] Python X.Y token grounding
- [ ] release-body versus tagged-changelog selector
- [ ] equivalent evidence deduplication
- [ ] invalid candidate aggregate behavior
- [ ] multiple distinct claim ambiguity
- [ ] `3.8` versus `3.8.1` token-boundary regression
- [ ] exact grounding versus semantic-truth nonclaim

---

## Unit 11 — Dependency versioning and target Python methods

Product validation is ahead of learning. Do not check learning items merely because implementation/tests are complete.

### Unit 11A — Dependency versioning

**Owner:** `src/upgradepilot/dependency/versioning.py`.

- [ ] minimum PEP 440 mental model
- [ ] `Version`
- [ ] raw identity versus parsed semantic value
- [ ] invalid/equivalent/non-forward intervals
- [ ] deterministic crossed-release ordering
- [ ] bounded `packaging` dependency contract

### Unit 11B — Target Python specifier semantics

**Owner:** `src/upgradepilot/target/python_specifier.py`.

- [ ] `SpecifierSet`
- [ ] stable X.Y.Z witness meaning
- [ ] boundary-derived witness candidates
- [ ] valid-but-unsupported specifier semantics
- [ ] declaration-overlap witness nonclaims

### Unit 11C — Target Python relevance

**Owner:** `src/upgradepilot/target/relevance.py`.

- [ ] relevance-state vocabulary
- [ ] conditional target activation concept
- [ ] early return as authority boundary
- [ ] caller misuse versus product unresolved state
- [ ] nested evidence preservation
- [ ] declared overlap/non-overlap only
- [ ] compatibility/safety/recommendation nonclaims

Learning point to preserve:

```text
one third-party implementation library (`packaging`)
≠
one product responsibility
```

The source reconciliation deliberately split dependency versioning from target-Python specifier semantics.

---

## Unit 12 — Authoritative upstream acquisition

**Status:** not started.

### Current owner map

```text
PyPI release/index        → pypi/release.py
tag→commit               → github/tag.py
exact repository file    → github/repository.py
changelog discovery      → github/changelog.py
interval evidence        → upstream/interval_evidence.py
interval authority       → upstream/interval.py
```

### Checklist

- [ ] PyPI release-index acquisition
- [ ] PEP 440 selection versus raw release identity
- [ ] ignored non-PEP-440 visibility
- [ ] lightweight versus annotated Git tag
- [ ] tag object versus resolved commit
- [ ] bounded tag peeling
- [ ] immutable commit text-file acquisition
- [ ] path/blob/byte/UTF-8 evidence
- [ ] commit/file identity join
- [ ] authority composition
- [ ] interval identity mismatch rejection
- [ ] deterministic controlled proof versus live public-source proof
- [ ] generic exact-commit changelog discovery versus package-specific path constant

---

## Unit 13 — Bounded semantic extraction and Step 7 runtime bridges

**Status:** not started in this learning package.

At the 2026-08-04 intake snapshot, product implementation had already established more than the previous plan captured. This does not imply learning completion.

### Step 6 retained product architecture to learn later

```text
bounded authoritative source text
→ local structured candidate extraction
→ CandidateUpstreamClaimResult
→ deterministic validate_support_drop_candidates(...)
→ grounded claim or explicit problem
```

Relevant references:

```text
docs/architecture/ADR-0006-bounded-local-support-drop-semantic-extractor.md
learning/bounded-llm-semantic-extraction.md
experiments/
experiments/tests/
```

### Step 6 checklist

- [ ] semantic oracle
- [ ] transport versus structured generation
- [ ] structured output versus semantic correctness
- [ ] deterministic source reconstruction
- [ ] grounding versus trust admission
- [ ] false-positive/false-negative evaluation
- [ ] repeated critical controls
- [ ] bounded local model/provider identity
- [ ] adoption gate and `adopt_bounded_extractor` disposition
- [ ] why this is narrow model trust, not general model trust

### Step 7A — exact-commit changelog discovery

**Current owner:** `src/upgradepilot/github/changelog.py`.

- [ ] exact commit → root tree → bounded recursive tree listing
- [ ] admitted Markdown changelog basename grammar
- [ ] truncated tree handling
- [ ] zero versus multiple candidate paths
- [ ] discovery heuristic versus evidence authority

### Step 7B — deterministic crossed-release Markdown source windows

Planned owner when implementation exists: `src/upgradepilot/upstream/changelog.py`.

- [ ] Markdown ATX heading grammar
- [ ] trusted raw crossed-release identity
- [ ] exact section boundaries
- [ ] original line IDs and character offsets
- [ ] every crossed release maps exactly once
- [ ] source-order consistency
- [ ] deterministic/semantic-neutral source window
- [ ] explicit prompt-size bound without silent truncation

### Later Step 7 runtime path

Learn only after implementation exists:

```text
bounded source window
→ product local semantic adapter
→ deterministic claim grounding
→ conditional target-Python activation
→ relevance result
```

Do not scaffold future learning as if unimplemented files already exist.

---

## Unit 14 — Ownership assessment and eventual branch integration

**Status:** not started.

Minimum evidence before any mastery claim:

- [ ] explain the learned request-to-evidence path
- [ ] predict a changed case not copied from tests
- [ ] add/materially modify one meaningful test
- [ ] make or review one bounded implementation change
- [ ] diagnose one deliberate defect
- [ ] identify permission/evidence/stopping/claim boundaries
- [ ] separate validated product behavior from personal learning depth
- [ ] reconstruct the responsibility-based source map at useful depth

Before eventual branch integration classify each learning-branch change as:

```text
reusable learning artifact
merge-eligible product improvement
practice-only change to revert
stale/conflicting material to revise
```

Do not merge the learning branch back merely because notes are useful. Final scope requires explicit review and user approval.

---

# 9. Current review inventory

## Open provisional observations

```text
LR-001
aggregate CI detail names only the first proof witness
→ possible diagnostic/presentation limitation
→ current source: src/upgradepilot/ci/dependency_exercise.py

LR-002
exactly-one-workflow-job rule rejects richer workflows even when one job is independently sufficient
→ possible capability limitation / prototype boundary
→ current source: src/upgradepilot/ci/workflow_commands.py
```

## Already formalized

```text
AUDIT-001
exact PR file-acquisition evidence contract/proportionality

AUDIT-002
CI dependency-exercise proof boundary
```

Formal findings should not be duplicated into new live observations.

---

# 10. Reusable session/delta records

```text
2026-07-31-11pm-Session1.md
→ original CI responsibility introduction

2026-08-02-Session1-continuation.md
→ state classification, precedence, existential aggregation, early mechanics

2026-08-02-main-delta-intake.md
→ early synchronized implementation delta

2026-08-03-main-delta-intake.md
→ Step 5 acquisition intake

2026-08-03-Session1-continuation-2.md
→ evaluator mechanics, command-reader entry, install matcher

2026-08-03-main-delta-intake-step6.md
→ Step 5 live closure and early Step 6 intake

2026-08-04-main-architecture-reconciliation-intake.md
→ responsibility-based source reconciliation, Step 6/7 progression, old→new owner map

LIVE_LEARNING_AND_REVIEW_NOTES.md
→ provisional learning/review observations between durable checkpoints
```

---

# 11. Synchronization discipline

At a material learning-session boundary:

1. inspect current `main` `MEMORY.md`;
2. compare `main` and learning branch;
3. inspect only relevant changed files/plans;
4. classify the delta as unrelated, locally relevant, or architecture-changing;
5. merge `main` normally into the learning branch when current-source truth would otherwise be stale;
6. update this plan only when sequence/ownership/proof requirements materially change;
7. preserve dated historical learning snapshots;
8. never rebase/force-push published learning history merely to simplify it.

Do not sync after every explanation.

---

# 12. Exact continuation

Continue directly in:

```text
src/upgradepilot/ci/workflow_commands.py
```

Resume `_extract_job_definitions(...)` after the already-covered first stage:

```text
text.splitlines()
→ locate first plain jobs:
→ record jobs_index + jobs_indent
→ missing mapping returns None
```

Next learning chunk:

```text
scan lines below jobs:
→ determine direct child indentation
→ collect sibling job starts
→ distinguish nested mapping keys from jobs
→ slice each job body
→ _extract_run_commands(...)
```

Then finish Unit 4 with:

```text
inline/block run extraction
useful regex/named-group mechanics
supported/unresolved test design
one ownership exercise
```

Do not restart tuple/`next`/aggregate/per-workflow material unless a transfer prediction reveals a gap.

Do not detour into later Step 6/7 model work before the current CI-reader unit reaches its ownership checkpoint.
