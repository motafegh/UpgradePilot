# UpgradePilot Current Memory

**Last updated:** 2026-07-30 16:44 +03:30  
**Authority:** Sole repository owner of live project position, verified behavior, blockers, and exact continuation.

Stable route definitions, specifications, ADRs, source, tests, plans, and dated evidence retain their own responsibilities. This file records only the current position needed to continue.

## Live position

- **Route:** B2 — Public PR vertical slice.
- **Controlling route:** [`plans/UPGRADEPILOT_90_DAY_PLAN.md`](plans/UPGRADEPILOT_90_DAY_PLAN.md)
- **B2 gate:** [`plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md`](plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md)
- **Selected plan:** [`plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md`](plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md)
- **Accepted architecture:** [`docs/architecture/ADR-0004-dependency-version-change-evidence.md`](docs/architecture/ADR-0004-dependency-version-change-evidence.md)
- **Latest implementation evidence:** [`working-memory/2026-07-30_1644_B2-step-1-dependency-contracts-partial-proof.md`](working-memory/2026-07-30_1644_B2-step-1-dependency-contracts-partial-proof.md)
- **Design closure evidence:** [`working-memory/2026-07-30_1631_B2-dependency-evidence-design-closure.md`](working-memory/2026-07-30_1631_B2-dependency-evidence-design-closure.md)
- **Latest relevant non-memory revision:** `121d70530c97a80cca83c648670c71d874a66930`.

Use local `HHMM` after the date for additional same-day working-memory records. Existing files are not renamed merely to retrofit the convention.

## Current phase

The dependency-version-change design phase is closed.

Implementation has begun through **Step 1 only**:

```text
freeze and test shared dependency-change records and problem states
```

Step 1 is currently:

```text
implemented
but
not behavior-validated
```

Do not begin Step 2 until the focused contract tests, legacy dependency-change tests, and complete deterministic suite pass in a real repository checkout.

## Behavior-validated product boundary

The latest behavior-validated product revision remains:

```text
75e1b5c55844c2e7b6f9f64d6ae1bd76c2dabd15
```

At that revision Ali ran:

```text
Ran 72 tests
OK
```

One installed public read-only S004 command preserved the existing evidence chain.

Current behavior-valid runtime remains:

```text
public repository + Dependabot PR
→ exact PR identity and complete changed files
→ one supported same-file package==version transition
→ exact-head target declaration evidence
→ exact-head workflow/job/step evidence
→ current bounded CI classification
→ exact PyPI package/version/file identity
→ matching upstream repository and release evidence
→ concise CLI evidence report
→ unresolved_claim
```

The commits made during Step 1 do not yet extend this behavior-validated boundary.

## Existing runtime contract inspected

The current implemented dependency path is still:

```text
ChangedFile[]
→ extract_pinned_dependency_change
→ PinnedDependencyChange or UnsupportedDependencyChange
```

`PinnedDependencyChange.source_file` currently combines:

1. the file where the version transition was observed;
2. the requirements file that the current CI rule expects to install.

Direct coupling exists in:

- `src/upgradepilot/cli.py`;
- `src/upgradepilot/ci_authority.py`;
- `src/upgradepilot/workflow_commands.py`;
- `tests/test_dependency_change.py`;
- the package exports in `src/upgradepilot/__init__.py`.

The legacy parser, CLI gating, CI evaluator, workflow-command interpretation, and output labels remain runtime truth.

## Step 1 contract implementation

Added to `src/upgradepilot/dependency_change.py`:

```text
DependencyFileEvidence
ExtractedDependencyVersionChange
DependencyVersionChange
DependencyChangeEvidenceProblem

DependencyChangeExtractionResult
DependencyChangeComparisonResult
```

### `DependencyFileEvidence`

Identifies one dependency file and how evidence was obtained. It can preserve:

```text
path
file format
extraction method
base revision/blob/byte count when available
head revision/blob/byte count when available
```

It does not prove dependency role, installation, CI consumption, compatibility, safety, or maintainer action.

### `ExtractedDependencyVersionChange`

Means one dependency file supplied one possible exact version transition.

It is not trusted across the complete pull request.

### `DependencyVersionChange`

Means all admitted dependency evidence was considered and exactly one trusted package transition remains.

It preserves all supporting `DependencyFileEvidence` records and explicit limitations as tuples.

### `DependencyChangeEvidenceProblem`

Preserves:

```text
stable machine-readable reason
human-readable detail
source evidence already identified
```

## Initial problem vocabulary

```text
no_supported_dependency_file
missing_dependency_patch
incomplete_dependency_patch
unsupported_requirement_format
unsupported_dependency_file_status
dependency_file_unavailable
dependency_file_too_large
malformed_dependency_file
invalid_dependency_record
unsupported_uv_lock_schema
unsupported_uv_lock_structural_change
ambiguous_uv_lock_package_records
version_unchanged
multiple_dependency_version_changes
conflicting_dependency_version_changes
```

No parser currently produces these new results. Existing legacy reasons remain unchanged until later migration.

## Focused tests added

Created:

```text
tests/test_dependency_change_contracts.py
```

The tests protect:

- file path, format, extraction method, revision, blob, and byte-count preservation;
- extracted file evidence versus trusted PR-wide evidence;
- frozen dataclass behavior;
- tuple collection immutability;
- exact problem vocabulary;
- problem source-evidence retention;
- case-neutral fixtures rather than S001-specific values.

`src/upgradepilot/__init__.py` now exports the shared contracts while preserving existing exports.

## Step 1 revisions

```text
Shared records and vocabulary:
81717384f7351dd018c2ba7c3a2bfc7db970dc63

Focused contract tests:
d9bf3c6c9317ecaee9a03c842e92d75a902d0394

Package-level exports:
e8447a9c8330e67df5bbcdd3ba832ad53a5cf745

Case-neutral contract fixtures:
121d70530c97a80cca83c648670c71d874a66930

Dated partial-proof evidence:
b90a87bedcbf44f18dffc858771d186771e9ec4e
```

## Proof state

Completed:

- repository source and direct-caller inspection;
- additive source implementation;
- focused test definition;
- package export update;
- case-neutral fixture review;
- commit comparison showing only the intended three files changed;
- local Python 3.13 smoke proof of frozen instances, tuple immutability, value preservation, and problem vocabulary.

Not completed:

- execution of the committed focused test module;
- execution of the existing dependency-change tests;
- execution of the complete deterministic suite;
- Python 3.12 execution;
- an installed command validation after the Step 1 changes.

Execution limitation:

- the available container has no UpgradePilot checkout;
- outbound GitHub cloning is unavailable from the container;
- Python 3.12 is not installed there;
- the current commit has no GitHub Actions workflow run.

The smoke check is not equivalent to repository test proof.

## Learning state

Introduced during this session:

- **dataclass** — a Python class designed mainly to hold structured values;
- **frozen dataclass** — field reassignment is blocked after construction;
- **slots** — the instance has a fixed declared field set and no arbitrary new attributes;
- **tuple immutability** — collection fields cannot be appended to or modified in place;
- **union-style result** — a function may return a success record or a typed problem, requiring callers to check which one they received;
- extracted file evidence versus trusted PR-wide evidence;
- stable machine-readable problem vocabulary.

Current depth:

```text
concepts introduced
+ practical purpose explained
+ contract shapes committed
+ equivalent smoke mechanics exercised
but
repository tests not yet run
and
Ali-owned understanding not yet assessed
```

Do not mark these concepts mastered.

## Exact continuation

Remain in **Step 1**.

In a real repository checkout with Python 3.12 or another admitted `>=3.12` interpreter, run:

```bash
python -m unittest tests.test_dependency_change_contracts -v
python -m unittest tests.test_dependency_change -v
python -m unittest discover -s tests -v
```

Then:

1. preserve the exact commands, interpreter version, test counts, and output;
2. diagnose and correct any failure without beginning Step 2;
3. review the four records and the focused tests with Ali;
4. ask Ali to explain, at the current introductory depth:
   - why `ExtractedDependencyVersionChange` is not yet trusted;
   - why `DependencyVersionChange.source_evidence` is a tuple;
   - why a problem is a normal result rather than necessarily an exception;
5. only if all tests pass and the review exposes no contract contradiction, record Step 1 as behavior-validated and authorize Step 2.

Do not begin:

- exact-requirement extraction migration;
- path-eligibility implementation;
- generic base/head file acquisition;
- `uv.lock` parsing;
- duplicate-record comparison;
- CI result migration;
- PEP 440 work;
- public S001 execution.

## Not established

- Step 1 behavior validation;
- any new parser using the shared records;
- `compare_extracted_dependency_changes` implementation;
- path eligibility enforcement;
- constraints-file product behavior;
- generic exact PR base/head acquisition;
- reported/decoded byte-size validation;
- `uv.lock` parsing;
- duplicate-group comparison;
- S001 dependency identity through the product;
- `DependencyCIExerciseResult` runtime behavior;
- `packaging` admission or PEP 440 runtime validation;
- Python-support relevance;
- compatibility, safety, maintainer action, or production readiness;
- Ali-owned mastery of the new contracts.

## State-maintenance rule

When route, selected plan, verified behavior, blocker, or exact continuation changes, update this file only. Change another file only when its stable responsibility or dated evidence changes.
