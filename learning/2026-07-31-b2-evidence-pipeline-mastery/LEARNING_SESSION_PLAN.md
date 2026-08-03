# UpgradePilot B2 Evidence-Pipeline Learning Session Plan

**Purpose:** Position-neutral learning plan for understanding, practising, reviewing, and progressively owning the implemented UpgradePilot B2 evidence pipeline  
**Learning branch:** `agent/learning-current-implementation`  
**Original baseline:** `1181a4305bbd2489188e5a9a027113ac8c4d9ae8` — Activate Step 2 support-drop validation  
**Latest implementation intake:** 2026-08-03 against `main` revision `7db6a6b6f0f6c261d98c6df66d51e14eb99359cd`  
**Latest main→learning sync:** PR #19, merge commit `3be4ff047493697218ba451f1b2797823c2ae750`  
**Current learning checkpoint:** `2026-08-03-Session1-continuation-2.md`  
**Latest delta intake:** `2026-08-03-main-delta-intake-step6.md`  
**Live product-state authority:** [`../../MEMORY.md`](../../MEMORY.md) on `main`

## 1. Boundary

This file controls only this learning package.

It does **not**:

- control live product continuation;
- authorize implementation work on `main`;
- replace source/tests as behavior truth;
- replace formal audits or ADRs;
- imply mastery because product code is behavior-validated;
- require restarting completed learning whenever `main` advances.

The learning branch isolates educational artifacts, source review, bounded design debate, and later ownership practice while `main` continues production development.

Current product position at the latest intake is:

```text
parent Steps 1–5 behavior-validated
Step 6A semantic corpus/oracle behavior-validated
Step 6B environment observation active
```

That product position changes the **forward learning map**, but it does not invalidate the current CI/workflow-reader lesson because the observed main delta did not modify:

```text
src/upgradepilot/ci_dependency_exercise.py
src/upgradepilot/workflow_commands.py
```

## 2. Learning objective

Build transferable ownership of the B2 request-to-evidence pipeline rather than memorize files chronologically.

The learning path is:

```text
canonical dependency identity
→ exact-head CI dependency-exercise evidence
→ multi-format dependency coordination
→ exact request-to-output orchestration
→ authoritative upstream crossed-release interval
→ untrusted semantic candidate
→ deterministic support-drop grounding
→ PEP 440 dependency/Python-line method
→ deterministic target-Python relevance
→ live upstream acquisition
→ bounded semantic-extractor evaluation
→ later conditional CLI orchestration / S001 end-to-end path when implemented
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
10. state exactly what the result proves and what it does not prove.

## 3. Learning method

### 3.1 Learn from a real responsibility

The first deep anchor remains the CI dependency-exercise responsibility because it connects:

```text
domain identity
GitHub Actions evidence
exact revision identity
workflow text interpretation
aggregation
abstention
public diagnostics
```

Do not replay the entire project from Step 0 before finishing this responsibility.

### 3.2 Repair prerequisites just in time

When a missing earlier concept blocks the active code:

```text
identify exact missing prerequisite
→ inspect only its owner
→ learn minimum accurate mechanism
→ make one transfer prediction
→ return to active responsibility
```

### 3.3 Use tests as executable claims

For each major behavior:

```text
product question
→ fixture/evidence
→ expected state
→ public contract
→ implementation path
→ negative/abstention branch
→ caller/output effect
```

### 3.4 Keep learning and review coupled

While studying source:

```text
understand mechanism
→ predict behavior
→ challenge design
→ classify observation
→ preserve only material review items
→ continue learning
```

Use `LIVE_LEARNING_AND_REVIEW_NOTES.md` for provisional material observations.

Do not create a formal audit until consequence, contract, source/test boundary, and proof requirement are established.

### 3.5 Product validation is not learning mastery

A passing product test suite or live proof establishes product behavior only.

Learning depth labels remain:

```text
introduced
operationally understood with guidance
implementation-adjacent
ownership practice
independently demonstrated
```

## 4. Progress-marking rules

Use Markdown checkboxes conservatively:

```text
[x] = covered to the intended current learning depth for that item
[ ] = not yet covered enough to treat as complete
```

A checked concept does **not** automatically mean mastery.

A unit is complete only when its exit condition and Ali-owned evidence are satisfied, even if many individual concepts are checked.

---

# 5. Current learning position

Current source position:

```text
src/upgradepilot/workflow_commands.py
→ _command_invokes_package(...)
```

Current unit status:

```text
Unit 1  — complete at operational depth
Unit 2  — in progress; most evaluator mechanics covered, ownership gate still open
Unit 3  — core precedence cases covered, independent decision-table gate still open
Unit 4  — active; install matcher covered, package-invocation matcher next
Units 5+ — not yet learned in this package
```

Do **not** jump to current product Step 6 merely because `main` is there. Finish the current bounded CI-reader responsibility first.

---

# 6. Learning sequence

## Unit 1 — CI dependency-exercise product question

**Status:** complete at current operational depth.

**Responsibility:** Understand exactly what the CI dependency-exercise evaluator claims.

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

**Core files:**

```text
src/upgradepilot/ci_dependency_exercise.py
tests/test_ci_dependency_exercise.py
```

**Ali-owned evidence already observed:**

- multiple changed-state predictions;
- correct distinction between green CI and dependency-exercise proof;
- correct distinction between execution absence and proof insufficiency;
- correct refusal to promote the result into compatibility.

**Exit condition:** satisfied for current operational depth.

---

## Unit 2 — One complete `proven` path

**Status:** in progress.

**Responsibility:** Trace one proving workflow from inputs through per-workflow interpretation and aggregate result.

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

- [ ] `Literal` as a type-level state vocabulary mechanism
- [ ] frozen dataclass rationale
- [ ] `slots=True` rationale
- [ ] keyword-only `*` independently demonstrated
- [ ] `Sequence[...]` collection-interface contract independently demonstrated
- [x] tuple materialization
- [x] generator expression mechanics at current use sites
- [x] `next(..., None)` as first-witness selection
- [x] `any(...)` as Boolean existence check
- [x] `None` as expected absence marker
- [x] per-workflow result versus aggregate result responsibility
- [x] all workflows evaluated before later first-witness search
- [x] one existential witness can determine aggregate `proven`
- [x] all per-workflow results remain preserved in `workflows=results`
- [x] internal invariant `assert` versus ordinary unresolved evidence
- [x] `state` / `reason` / `detail` / evidence payload roles

### Ali-owned evidence still required

- [ ] trace the complete proving test through the evaluator without line-by-line prompting
- [ ] explain each major input's authority from memory

**Exit condition:** not yet satisfied.

---

## Unit 3 — Decision order, precedence, and aggregation

**Status:** core cases covered; ownership gate open.

**Responsibility:** Understand why branch order is product semantics rather than incidental control flow.

### Case checklist

- [x] no workflow inputs
- [x] no completed-successful job
- [x] successful child job with unsuccessful parent run
- [x] unavailable workflow definition
- [x] workflow-definition revision mismatch
- [x] missing explicit direct-requirements install path
- [x] successful CI but no admitted dependency-exercise proof
- [x] one proven workflow plus weaker workflows
- [x] per-workflow `no_successful_jobs` versus aggregate `no_successful_exact_head_jobs`
- [x] `AND` success condition versus `OR` rejection condition
- [x] earlier `return` prevents later gates from executing

### Ownership checklist

- [ ] Ali independently writes/reconstructs the decision table
- [ ] Ali predicts at least two new mixed-workflow cases without prompting
- [ ] Ali explains aggregate precedence and nonclaims end to end

**Exit condition:** not yet satisfied.

---

## Unit 4 — Bounded workflow-command reader

**Status:** active.

**Current exact position:** `_command_invokes_package(...)` is next.

**Responsibility:** Understand the deliberately narrow visible-YAML/visible-shell grammar and its abstention boundary.

**Core files:**

```text
src/upgradepilot/workflow_commands.py
tests/test_workflow_commands.py
relevant tests/test_ci_dependency_exercise.py cases
```

### Reader architecture checklist

- [x] shallow indentation reader versus complete YAML parser
- [x] `_WorkflowJobDefinition` keeps only key + visible command tuple
- [x] `jobs is None` versus zero readable jobs distinction
- [x] exactly-one-job current restriction
- [x] why install in Job A + execution in Job B must not be combined automatically
- [x] design challenge: one self-contained proving job inside a multi-job workflow could be conservatively evaluated without cross-job inference
- [ ] direct job-key scanner mechanics in `_extract_job_definitions(...)`
- [ ] indentation boundaries in detail
- [ ] inline `run:` extraction mechanics
- [ ] block `run: |` / `run: >` extraction mechanics
- [ ] `_RUN_PATTERN` named groups
- [ ] `_JOB_KEY_PATTERN` named groups

### Command evidence checklist

- [x] one-job command tuple extraction at conceptual level
- [x] separate install witness and execution witness searches
- [x] partial evidence preserved on unresolved result
- [x] success requires both install + invocation witnesses
- [x] direct `pip install -r` / `--requirement` concept
- [x] exact admitted requirements path comparison
- [x] superficial path normalization (`./`, backslash→slash)
- [x] path normalization applies to extracted path identity, not whole shell command
- [ ] `_PIP_INSTALL_PATTERN` regex mechanics
- [ ] `_REQUIREMENT_PATTERN` regex mechanics
- [ ] shell segmentation independently demonstrated
- [ ] `_command_invokes_package(...)`
- [ ] package versus normalized-package candidate set
- [ ] supported prefixes/wrappers (`python -m`, `uv run`, etc.)
- [ ] leading environment-variable assignment stripping
- [ ] invocation must begin at shell-segment start
- [ ] token boundary (`whitespace or end`) behavior
- [ ] tox/script/alias/function/custom-action/reusable-workflow non-inference in detail

### Design-review companions

Already formalized:

```text
audits/2026-08-02_AUDIT-002_ci-dependency-exercise-proof-boundary.md
```

Do not recreate its findings while learning. Use it after understanding source mechanics to connect:

```text
static recognized command
≠
matched runtime step success
≠
exact proposed version observed
≠
that exact version successfully exercised
```

Open live review items:

```text
LR-001 — aggregate detail names first proof witness only
LR-002 — exactly-one-job restriction is stricter than same-job existential proposition
```

### Ali-owned evidence still required

- [ ] design one new supported reader case
- [ ] design one new unresolved reader case
- [ ] explain which inference would become unsafe if the reader guessed
- [ ] optionally implement one focused test once the reader is fully understood

**Exit condition:** not yet satisfied.

---

## Unit 5 — Reverse trace to canonical dependency identity

**Status:** not started in this package.

**Responsibility:** Learn the exact trusted object consumed by the CI evaluator.

### Checklist

- [ ] canonical `DependencyVersionChange`
- [ ] package normalization
- [ ] exact old/proposed version identity
- [ ] `DependencyFileEvidence`
- [ ] source-specific extraction
- [ ] trusted change versus explicit evidence problem
- [ ] dependency evidence path versus operational CI-install path

**Core files:**

```text
src/upgradepilot/dependency_change.py
src/upgradepilot/exact_requirement_change.py
src/upgradepilot/uv_lock_change.py
focused tests
```

**Ali-owned evidence:** Explain why `uv.lock` or constraints evidence may establish dependency identity without proving CI consumption.

---

## Unit 6 — Multi-format dependency coordinator and S004/S001 contrast

**Status:** not started.

**Responsibility:** Understand how materially different dependency formats become one canonical downstream contract.

### Path

```text
changed files
→ source recognition
→ requirements/constraints patch interpretation
   OR exact base/head uv.lock acquisition + comparison
→ PR-wide reconciliation
→ DependencyVersionChange or explicit problem
```

### Key contrast

```text
S004
requirements-dev.txt
pytest 9.0.2 → 9.0.3
CI dependency exercise proven

S001
uv.lock
soupsieve 2.6 → 2.8.4
CI dependency exercise unresolved unless lock consumption is independently established
```

### Checklist

- [ ] source recognition
- [ ] requirements/constraints path
- [ ] exact base/head uv.lock path
- [ ] reconciliation
- [ ] conflict/multiple-change states
- [ ] downstream representation neutrality
- [ ] S004 vs S001 transfer explanation

**Design-review companion:** `AUDIT-001` only after exact-file mechanics are understood.

---

## Unit 7 — Request-to-output integration

**Status:** not started.

**Responsibility:** Trace the public command through the implemented pipeline.

### Checklist

- [ ] CLI acquisition order
- [ ] acquisition versus interpretation boundaries
- [ ] exact identity/provenance joins
- [ ] independent unresolved subsystems
- [ ] CLI labels as public contracts
- [ ] package exports as API surface
- [ ] request-to-output authority map

**Core files:**

```text
src/upgradepilot/cli.py
src/upgradepilot/__init__.py
GitHub acquisition modules
package/upstream/target modules
tests/test_cli.py
tests/test_package_interface.py
```

---

## Unit 8 — Upstream release-interval authority

**Status:** not started.

**Responsibility:** Understand why the complete crossed-version interval matters.

### Checklist

- [ ] old exclusive / proposed inclusive interval
- [ ] raw identity versus semantic version ordering
- [ ] trusted crossed-release index
- [ ] release body authority
- [ ] exact proposed-tag changelog authority
- [ ] package metadata corroboration only
- [ ] authority basis
- [ ] interval incomplete versus unavailable versus contradiction

**Core:** `upstream_interval.py` + focused tests.

---

## Unit 9 — Untrusted candidate versus trusted support-drop claim

**Status:** not started.

**Responsibility:** Understand the semantic trust boundary implemented before any model adoption.

### Checklist

- [ ] `CandidateUpstreamClaimResult` is untrusted
- [ ] echoed dependency identity validation
- [ ] category/direction admission
- [ ] canonical Python X.Y
- [ ] introduced-release membership
- [ ] source identity resolved from trusted evidence
- [ ] exact grounding requirement
- [ ] grounded claim versus explicit claim problem
- [ ] schema-valid does not mean semantically trusted

**Core:** `upstream_claim.py` + focused/edge tests.

---

## Unit 10 — Quote grounding, ambiguity, and aggregation

**Status:** not started.

**Responsibility:** Understand the strongest deterministic links around semantic candidates.

### Checklist

- [ ] quote offsets
- [ ] unchanged source text
- [ ] Python X.Y token grounding
- [ ] release-body versus tagged-changelog selector
- [ ] equivalent evidence deduplication
- [ ] invalid candidate poisoning/aggregate behavior
- [ ] multiple distinct claim ambiguity
- [ ] `3.8` versus `3.8.1` token boundary regression
- [ ] exact grounding versus semantic truth nonclaim

---

## Unit 11 — Concrete implementation intake after the original baseline

Product validation for these boundaries is already ahead of learning. Do not check learning items merely because implementation/tests are complete.

### Unit 11A — Step 3 packaging/version method

**Learning status:** not started.

**Product status at latest intake:** behavior-validated.

### Checklist

- [ ] minimum PEP 440 mental model
- [ ] `Version`
- [ ] `SpecifierSet`
- [ ] raw identity versus parsed semantic value
- [ ] invalid/equivalent/non-forward intervals
- [ ] crossed-release ordering
- [ ] bounded `packaging>=26.2,<27` contract
- [ ] stable X.Y.Z witness meaning
- [ ] boundary-derived witness candidates
- [ ] valid-but-unsupported specifier semantics
- [ ] declaration-overlap witness nonclaims

---

### Unit 11B — Step 4 target-Python relevance

**Learning status:** not started.

**Product status at latest intake:** behavior-validated.

### Checklist

- [ ] relevance-state vocabulary
- [ ] conditional target activation
- [ ] early return as authority boundary
- [ ] caller misuse versus product unresolved state
- [ ] Step 3 problem mapping
- [ ] nested evidence preservation
- [ ] declared overlap/non-overlap only
- [ ] compatibility/safety/recommendation nonclaims

---

### Unit 11C — Step 5 authoritative upstream acquisition

**Learning status:** not started.

**Product status at latest intake:** Steps 5A–5D and live S001 proof behavior-validated.

This is now a concrete unit, not “future implementation.”

### Acquisition chain

```text
PyPI project JSON
→ release index evidence
→ crossed-release selection

exact tag ref
→ tag object
→ immutable commit

resolved commit + explicit changelog path
→ exact text-file evidence
→ TaggedChangelogEvidence

crossed releases + tagged changelog
→ AuthoritativeUpstreamIntervalEvidence
```

### Checklist

- [ ] 5A PyPI project release-index acquisition
- [ ] PEP 440 selection versus raw release identity
- [ ] ignored non-PEP-440 visibility
- [ ] 5B lightweight versus annotated Git tag
- [ ] tag object versus resolved commit
- [ ] bounded tag peeling
- [ ] 5C immutable commit file acquisition
- [ ] path/blob/byte/UTF-8 evidence
- [ ] commit/file identity join
- [ ] 5D reuse of Step 1 authority assembler
- [ ] interval identity mismatch rejection
- [ ] deterministic proof versus live public-source proof
- [ ] S001 live evidence explanation

Reference: `2026-08-03-main-delta-intake.md` and `2026-08-03-main-delta-intake-step6.md`.

---

### Unit 11D — Step 6 semantic extraction/evaluation

**Learning status:** not started.

**Product status at latest intake:** 6A behavior-validated; 6B active; no model/adapter adopted.

### Core architecture

```text
AuthoritativeUpstreamIntervalEvidence
→ untrusted semantic candidate extraction
→ CandidateUpstreamClaimResult
→ deterministic Step 2 validation
→ GroundedPythonSupportDropClaim or explicit problem
```

### Step 6A — frozen corpus/oracle

Product implemented/validated; learning not yet covered.

- [ ] semantic oracle meaning
- [ ] frozen expected meaning versus extraction algorithm
- [ ] positive support-drop classes
- [ ] added/continued controls
- [ ] negation/future controls
- [ ] raised-minimum-only ungroundable control
- [ ] ambiguity/multiple-drop cases
- [ ] instruction-shaped source text as inert data
- [ ] exact S001 oracle case

### Step 6B — environment observation

Current product responsibility; learning not yet covered.

- [ ] LM Studio server/model identity
- [ ] GPU deployment evidence
- [ ] WSL2→server reachability
- [ ] environment identity versus semantic evidence

### Step 6C — smallest adapter smoke

Not yet established at latest intake.

- [ ] direct HTTP boundary
- [ ] JSON Schema output shape versus semantic truth
- [ ] transport success versus structured-generation success
- [ ] retries disabled in first-pass evaluation

### Step 6D — scored semantic evaluation

Not yet established at latest intake.

- [ ] semantic oracle scoring
- [ ] grounding result separately recorded
- [ ] false positive / false negative
- [ ] wrong direction / wrong Python line / wrong release
- [ ] invented quote/span
- [ ] repeated critical controls
- [ ] adoption disposition

### Layer-separation ownership target

Ali should eventually explain independently:

```text
transport
≠
structured generation
≠
semantic correctness
≠
grounding
≠
trust admission
≠
product adoption
```

---

## Unit 12 — Ownership assessment and eventual branch integration

**Status:** not started.

Minimum evidence before any mastery claim:

- [ ] explain the learned request-to-evidence path
- [ ] predict a changed case not copied from tests
- [ ] add/materially modify one meaningful test
- [ ] make or review one bounded implementation change
- [ ] diagnose one deliberate defect
- [ ] identify permission/evidence/stopping/claim boundaries
- [ ] separate validated product behavior from personal learning depth

Before eventual branch integration classify each branch change as:

```text
reusable learning artifact
merge-eligible product improvement
practice-only change to revert
stale/conflicting material to revise
```

Do not merge the learning branch back merely because notes are useful. Final scope requires explicit review and user approval.

---

# 7. Current review inventory

## Open provisional observations

```text
LR-001
aggregate CI detail names only the first proof witness
→ possible diagnostic/presentation limitation

LR-002
exactly-one-workflow-job rule rejects richer workflows even when one job is independently sufficient
→ possible capability limitation / prototype boundary
```

## Already formalized

```text
AUDIT-001
exact PR file-acquisition evidence contract/proportionality

AUDIT-002
CI dependency-exercise proof boundary
```

Formal audit findings should not be duplicated into new live observations.

---

# 8. Reusable session records

Current session/delta artifacts:

```text
2026-07-31-11pm-Session1.md
→ original CI responsibility introduction and first proving-path explanation

2026-08-02-Session1-continuation.md
→ state classification, precedence, existential aggregation, first signature mechanics

2026-08-02-main-delta-intake.md
→ first synchronized implementation delta

2026-08-03-main-delta-intake.md
→ Step 5A–5D intake before later live closure

2026-08-03-Session1-continuation-2.md
→ tuple/generator/next, aggregate fallback, per-workflow gates, workflow-reader entry, install matcher, current exact source position

2026-08-03-main-delta-intake-step6.md
→ Step 5 live closure, Step 6A validation, Step 6B activation

LIVE_LEARNING_AND_REVIEW_NOTES.md
→ provisional learning/review observations between durable checkpoints
```

---

# 9. Synchronization discipline

At a material learning-session boundary:

1. inspect current `main` `MEMORY.md`;
2. compare `main` and learning branch;
3. inspect only relevant changed files/plans;
4. classify the delta:
   - unrelated to current lesson;
   - locally relevant;
   - architecture-changing;
5. merge `main` normally into the learning branch when needed;
6. update this plan only when sequence/proof requirements materially change;
7. never rebase/force-push published learning history merely to simplify it.

Do not sync after every explanation. Sync when current-source truth or forward learning alignment would otherwise become stale.

---

# 10. Exact continuation

Continue directly from:

```python
_command_invokes_package(...)
```

Next learning chunk:

```text
package + normalized_package candidate set
→ supported prefixes/wrappers
→ visible leading environment assignment removal
→ segment-start requirement
→ whitespace/end token boundary
→ supported/unresolved examples
```

Then complete only the remaining workflow-reader mechanics required for Unit 4:

```text
_extract_run_commands(...)
_extract_job_definitions(...)
regex/named-group details at useful depth
supported/unresolved test design
```

Do not restart tuple/`next`/aggregate/per-workflow gate material unless a transfer prediction reveals a gap.

Do not detour into Step 6 model work before the current CI-reader unit reaches its ownership checkpoint.