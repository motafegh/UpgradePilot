# UpgradePilot Current Memory

**Last updated:** 2026-07-31 16:35 +03:30  
**Authority:** Sole repository owner of live project position, verified behavior, blockers, and exact continuation.

Stable route definitions, specifications, ADRs, source, tests, plans, and dated evidence retain their own responsibilities. This file records only the current position needed to continue.

## Live position

- **Route:** B2 — Public PR vertical slice.
- **Controlling route:** [`plans/UPGRADEPILOT_90_DAY_PLAN.md`](plans/UPGRADEPILOT_90_DAY_PLAN.md)
- **B2 gate:** [`plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md`](plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md)
- **Selected plan:** [`plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md`](plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md)
- **Accepted architecture:** [`docs/architecture/ADR-0004-dependency-version-change-evidence.md`](docs/architecture/ADR-0004-dependency-version-change-evidence.md)
- **Step 1 validation:** [`working-memory/2026-07-30_2138_B2-step-1-dependency-contracts-validation.md`](working-memory/2026-07-30_2138_B2-step-1-dependency-contracts-validation.md)
- **Step 2 validation:** [`working-memory/2026-07-31_1612_B2-step-2-exact-requirement-validation.md`](working-memory/2026-07-31_1612_B2-step-2-exact-requirement-validation.md)
- **Step 3 validation:** [`working-memory/2026-07-31_1635_B2-step-3-dependency-comparison-validation.md`](working-memory/2026-07-31_1635_B2-step-3-dependency-comparison-validation.md)
- **Validated repository `main` state:** `0b1e045ad18915fed59c34318cf482f0132d9112`.
- **Validated product-source/test revision:** `fe3b1f7a07aeb2acbc0b76105ddc3cb09e131497`.
- **Step 3 validation-record revision:** `ff87f13bc9de4de4a376ed31616c21e35c996e56`.

## Current phase

Step 1 is complete and behavior-validated.

Step 2 is complete and behavior-validated.

Step 3 is complete and behavior-validated:

```text
compare_extracted_dependency_changes
```

Step 4 is the next bounded plan step, but implementation has not started:

```text
generalize exact pull-request dependency-file acquisition
```

The next activity is a focused Step 4 discussion and source/test design review.

## Current behavior-validated product boundary

Observed complete-suite result:

```text
Ran 92 tests in 0.021s
OK
```

The complete suite includes:

```text
Step 3 comparison tests: 6
Step 2 exact-requirement tests: 10
legacy dependency tests: 6
Step 1 shared-contract tests: 4
all other deterministic repository tests
```

The installed anonymous public S004 regression control also passed:

```bash
unset GITHUB_TOKEN
upgradepilot googlefonts/glyphsLib 1145
```

The control preserved:

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

The supplied Step 3 transcript did not repeat `python --version`, `git rev-parse HEAD`, or `git status --short`. The same active `.venv` previously reported Python 3.12.3, and remote `main` resolved to the validated repository state immediately after the run. Future validation records should capture those commands directly.

## Step 3 behavior now validated

The shared comparator lives in:

```text
src/upgradepilot/dependency_change.py
```

Public function:

```text
compare_extracted_dependency_changes
```

Input:

```text
Sequence[DependencyChangeExtractionResult]
```

Each input item is already one of:

```text
ExtractedDependencyVersionChange
or
DependencyChangeEvidenceProblem
```

Output:

```text
DependencyVersionChange
or
DependencyChangeEvidenceProblem
```

Validated decision order:

```text
1. any explicit evidence problem blocks PR-wide trust
2. no extracted changes
   → no_supported_dependency_file
3. several normalized packages
   → multiple_dependency_version_changes
4. one normalized package with different exact old/proposed transitions
   → conflicting_dependency_version_changes
5. equivalent extracted changes
   → one DependencyVersionChange with combined source evidence
```

Equivalent evidence requires:

```text
same normalized package
+ same exact raw old-version string
+ same exact raw proposed-version string
```

The comparator preserves every unique `DependencyFileEvidence` record once in caller-provided order. It remains format-independent and does not parse patches, recognize dependency paths, acquire repository files, interpret `uv.lock`, perform PEP 440 validation, inspect CI, or decide compatibility or safety.

## Runtime compatibility boundary

The installed CLI still follows the legacy runtime path:

```text
ChangedFile[]
→ extract_pinned_dependency_change
→ PinnedDependencyChange or UnsupportedDependencyChange
```

The new file-level extraction and PR-wide comparison functions are implemented and behavior-validated, but CLI orchestration has not yet migrated to them.

S004 therefore remains a regression control for the existing end-to-end product path rather than proof that the new shared comparison flow is already used by the installed CLI.

## Learning state

Step 3 introduced and reviewed:

- **comparison layer** — aggregates typed extraction results without reparsing source files;
- **comparison key** — normalized package plus exact raw old/proposed strings;
- **evidence aggregation** — equivalent evidence becomes one immutable source tuple;
- **decision precedence** — explicit evidence problems block convenient success;
- **conflict classification** — several packages differ from conflicting transitions for one package;
- **representative display value** — readable spelling comes from the first equivalent result while normalized identity controls comparison.

Current Step 3 depth:

```text
structured explanation completed
+ source ownership and decision order reviewed
+ focused tests defined
+ complete-suite and installed-control execution observed
but
no independent implementation practice recorded
no user-owned explanation recorded
no formal assessment recorded
not mastered
```

Product behavior validation and learning mastery remain separate claims.

## Exact continuation

Remain within the selected dependency-version-change plan.

Before modifying source, inspect Step 4 in this order:

1. `src/upgradepilot/github_repository.py` current records, limits, and acquisition helpers;
2. every direct caller of repository-file acquisition;
3. `tests/test_github_repository.py` and any target/workflow tests depending on current behavior;
4. the exact ADR and selected-plan requirements for immutable base/head file retrieval;
5. the compatibility boundary preserving existing exact-head workflow and target-Python acquisition;
6. the smallest new records and public functions needed for dependency files.

Step 4 must prove:

```text
only an exact immutable PR base or head SHA is accepted
requested and returned paths match
revision and blob SHA are preserved
reported size is validated before decoding
reported and decoded byte counts agree
1,000,000 decoded-byte limit is enforced
missing, inaccessible, oversized, malformed Base64,
and invalid UTF-8 remain distinct
existing workflow and target exact-head acquisition remains green
```

Step 4 must not implement:

- `uv.lock` parsing;
- duplicate-package-group comparison;
- CLI migration to the shared dependency flow;
- CI dependency-exercise migration;
- PEP 440 validation or ordering;
- Python-support relevance;
- compatibility, safety, recommendation, or maintainer-action logic.

## Not established

- CLI orchestration through file-level extraction and PR-wide comparison;
- generic exact PR base/head dependency-file acquisition;
- reported-versus-decoded byte-size validation;
- `uv.lock` extraction;
- duplicate-group comparison;
- S001 dependency identity through the product;
- constraints-file CI consumption semantics;
- CLI migration to `DependencyVersionChange`;
- `DependencyCIExerciseResult` runtime behavior;
- PEP 440 runtime validation;
- Python-support relevance;
- compatibility, safety, maintainer action, or production readiness;
- mastery of Step 1, Step 2, or Step 3 concepts.

## State-maintenance rule

When route, selected plan, verified behavior, blocker, learning state, or exact continuation changes, update this file only. Change another file only when its stable responsibility or dated evidence changes.
