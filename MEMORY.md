# UpgradePilot Current Memory

**Last updated:** 2026-07-30 21:38 +03:30  
**Authority:** Sole repository owner of live project position, verified behavior, blockers, and exact continuation.

Stable route definitions, specifications, ADRs, source, tests, plans, and dated evidence retain their own responsibilities. This file records only the current position needed to continue.

## Live position

- **Route:** B2 — Public PR vertical slice.
- **Controlling route:** [`plans/UPGRADEPILOT_90_DAY_PLAN.md`](plans/UPGRADEPILOT_90_DAY_PLAN.md)
- **B2 gate:** [`plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md`](plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md)
- **Selected plan:** [`plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md`](plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md)
- **Accepted architecture:** [`docs/architecture/ADR-0004-dependency-version-change-evidence.md`](docs/architecture/ADR-0004-dependency-version-change-evidence.md)
- **Partial implementation evidence:** [`working-memory/2026-07-30_1644_B2-step-1-dependency-contracts-partial-proof.md`](working-memory/2026-07-30_1644_B2-step-1-dependency-contracts-partial-proof.md)
- **Learning correction:** [`working-memory/2026-07-30_1701_B2-learning-record-correction.md`](working-memory/2026-07-30_1701_B2-learning-record-correction.md)
- **Step 1 validation:** [`working-memory/2026-07-30_2138_B2-step-1-dependency-contracts-validation.md`](working-memory/2026-07-30_2138_B2-step-1-dependency-contracts-validation.md)
- **Latest relevant non-memory revision:** `c4e1bd3961b969120704f325396c03d079feadec`.

## Current phase

The dependency-version-change design phase is closed.

Step 1 is complete and behavior-validated:

```text
freeze and test shared dependency-change records and problem states
```

Validated Step 1 state:

```text
source records and focused tests committed
+ structured introductory teaching completed
+ Python 3.12 repository tests passed
+ installed public S004 control passed
```

Step 2 is the next bounded plan step, but implementation has not started:

```text
move the existing exact-requirement extraction behavior
into a dedicated exact_requirement_change.py module
without changing validated behavior
```

The next session should discuss and inspect Step 2 before modifying source.

## Behavior-validated product boundary

The current behavior-validated source revision is:

```text
60837a65883e1d21229e383ee47225839d49e951
```

The local validation used:

```text
Python 3.12.3
```

Required repository results:

```text
focused Step 1 contracts
→ 4 tests passed

legacy dependency-change behavior
→ 6 tests passed

complete deterministic suite
→ 76 tests passed
```

The complete 76-test count includes the focused and legacy tests; it is the unique complete-suite total.

The installed anonymous public control also passed:

```text
unset GITHUB_TOKEN
upgradepilot googlefonts/glyphsLib 1145
```

The S004 control preserved:

```text
exact public PR identity
→ complete changed-file evidence
→ requirements-dev.txt
→ pytest 9.0.2 → 9.0.3
→ exact-head target declaration: project_table_absent
→ two exact-head workflow runs
→ CI authority: sufficient
→ pytest==9.0.3 package evidence
→ 2/2 provenance coverage
→ pytest-dev/pytest release tag 9.0.3
→ unresolved_claim
```

The anonymous success applies to this execution only. GitHub anonymous rate limits still exist.

## Runtime boundary after Step 1

The current runtime still uses:

```text
ChangedFile[]
→ extract_pinned_dependency_change
→ PinnedDependencyChange or UnsupportedDependencyChange
```

`PinnedDependencyChange.source_file` still combines the file where the change was observed with the requirements file expected by the current CI rule. The legacy parser, CLI, CI evaluator, workflow-command reader, and output labels remain runtime truth.

No new parser produces the Step 1 shared contracts yet.

## Step 1 implementation present

The following additive contracts are committed in `src/upgradepilot/dependency_change.py`:

```text
DependencyFileEvidence
ExtractedDependencyVersionChange
DependencyVersionChange
DependencyChangeEvidenceProblem
DependencyChangeExtractionResult
DependencyChangeComparisonResult
```

Focused tests are committed in:

```text
tests/test_dependency_change_contracts.py
```

Package-level exports were added without migrating existing runtime callers.

Relevant implementation revisions:

```text
81717384f7351dd018c2ba7c3a2bfc7db970dc63
Add shared records and vocabulary

d9bf3c6c9317ecaee9a03c842e92d75a902d0394
Add focused contract tests

e8447a9c8330e67df5bbcdd3ba832ad53a5cf745
Expose package-level contracts

121d70530c97a80cca83c648670c71d874a66930
Use case-neutral contract fixtures
```

## Learning state

A structured introductory teaching and guided source/test walkthrough has now occurred. It covered:

```text
record and value-object meaning
@dataclass generated behavior
frozen=True and shallow immutability
slots=True and fixed instance shape
list versus tuple behavior
Literal static vocabulary limits
success-or-problem unions and type narrowing
extracted file evidence versus trusted PR-wide evidence
focused contract-test meaning and limits
```

Current depth:

```text
structured introductory explanation completed
+ actual source and focused tests reviewed
but
no independent implementation practice recorded
no user-owned explanation recorded
no formal assessment recorded
not mastered
```

The user requested continuation without comprehension-check questions. Product behavior validation and learning mastery remain separate claims.

Do not count generated code, architecture approval, test execution, or assistant explanation alone as mastery.

## Step 1 proof state

Completed:

- repository source and direct-caller inspection;
- additive source implementation;
- focused contract-test definition;
- package export update;
- case-neutral fixture review;
- structured introductory teaching and guided source/test review;
- Python 3.12.3 focused contract execution: 4 passed;
- Python 3.12.3 legacy dependency execution: 6 passed;
- Python 3.12.3 complete deterministic suite: 76 passed;
- installed anonymous S004 public command validation;
- dated Step 1 validation evidence;
- Step 1 behavior-validation closure.

Execution-record limitation:

- the local shell showed branch `main`, while the exact local `git rev-parse HEAD` and `git status --short` outputs were not separately captured;
- the validated source revision was resolved from repository `main` immediately after the supplied run.

This limitation does not change the observed passing command results, but future validation records should capture local revision and working-tree status directly.

## Exact continuation

Remain within the selected dependency-version-change plan.

The next activity is a focused Step 2 discussion and source review, not immediate feature implementation.

Review in order:

1. identify the current exact-requirement parser function and every private helper it owns;
2. map direct imports, package exports, CLI callers, CI callers, and workflow-command assumptions;
3. use the six existing dependency tests as the behavior-preservation boundary;
4. decide the exact Step 2 return contract and which legacy compatibility surface remains temporarily exported;
5. define the module-move sequence into `exact_requirement_change.py`;
6. keep focused, legacy, and complete tests green after each bounded change.

Step 2 must remain behavior-preserving. Do not add during Step 2:

- `uv.lock` parsing;
- generic exact base/head dependency-file acquisition;
- PR-wide comparison;
- path-eligibility expansion beyond the selected Step 2 scope;
- CLI or CI migration beyond what the plan explicitly requires;
- PEP 440 runtime validation;
- Python-support relevance;
- recommendation or safety logic.

## Not established

- an exact-requirement parser producing the new extracted shared record;
- `compare_extracted_dependency_changes` implementation;
- path-eligibility enforcement;
- constraints-file product behavior;
- generic exact PR base/head dependency-file acquisition;
- reported-versus-decoded byte-size validation;
- `uv.lock` parsing;
- duplicate-group comparison;
- S001 dependency identity through the product;
- `DependencyCIExerciseResult` runtime behavior;
- `packaging` admission or PEP 440 runtime validation;
- Python-support relevance;
- compatibility, safety, maintainer action, or production readiness;
- mastery of the Step 1 Python concepts.

## State-maintenance rule

When route, selected plan, verified behavior, blocker, learning state, or exact continuation changes, update this file only. Change another file only when its stable responsibility or dated evidence changes.
