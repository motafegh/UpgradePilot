# UpgradePilot Current Memory

**Last updated:** 2026-07-31 16:25 +03:30  
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
- **Last behavior-validated product source revision:** `734c78e1b7754b14f2a8456fa415d3b714d24032`.
- **Latest Step 3 implementation revision:** `fe3b1f7a07aeb2acbc0b76105ddc3cb09e131497`.

## Current phase

Step 1 is complete and behavior-validated.

Step 2 is complete and behavior-validated.

Step 3 source and focused tests are now implemented on `main`:

```text
compare_extracted_dependency_changes
```

Step 3 has **not** yet been behavior-validated in the real Python 3.12 checkout.

Do not begin Step 4.

## Last behavior-validated product boundary

The validated product source revision remains:

```text
734c78e1b7754b14f2a8456fa415d3b714d24032
```

Observed validation at that boundary:

```text
complete deterministic suite: 86 passed
installed anonymous S004 command: passed
```

The current Step 3 commits do not extend this boundary until focused comparison tests, prior dependency tests, the complete deterministic suite, and the installed S004 control pass.

## Step 3 implementation present on main

Added to:

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

Each item is already one of:

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

The comparator is format-independent. It does not parse patches, recognize dependency paths, acquire repository files, interpret `uv.lock`, perform PEP 440 validation, inspect CI, or decide compatibility or safety.

## Comparison rule now implemented

Decision order:

```text
1. any explicit evidence problem blocks PR-wide trust
2. no extracted changes
   → no_supported_dependency_file
3. several normalized packages
   → multiple_dependency_version_changes
4. one normalized package with different exact old/proposed pairs
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

The first extracted result supplies the readable package spelling. Every unique `DependencyFileEvidence` record is preserved once in caller-provided repository order.

When an evidence problem is present, the comparator preserves the first explicit problem in caller order and attaches all unique source evidence considered by the comparison. This prevents a convenient successful extraction from hiding malformed, unavailable, incomplete, oversized, or otherwise explicit admitted evidence problems.

## Step 3 focused tests present

Added:

```text
tests/test_dependency_change_comparison.py
```

The file defines six tests proving:

1. empty input produces `no_supported_dependency_file`;
2. one extracted change becomes one trusted PR-wide change;
3. equivalent evidence combines source records;
4. conflicting exact transitions for one normalized package remain explicit;
5. several package changes remain explicit;
6. a recognized malformed evidence problem blocks a convenient valid change.

Package-level export was added through:

```text
upgradepilot.compare_extracted_dependency_changes
```

## Relevant Step 3 revisions

```text
b507ed88f3544e23bac823bffac013fff057e31e
Compare extracted dependency changes

4a4652e79bad774d40505a94c1ef2fe30c58517f
Export dependency comparison API

fe3b1f7a07aeb2acbc0b76105ddc3cb09e131497
Test dependency change comparison
```

## Learning state

Step 3 introduced these concrete concepts:

- **comparison layer** — aggregates typed extraction results without reparsing source files;
- **comparison key** — normalized package plus exact raw old/proposed strings;
- **evidence aggregation** — agreeing file evidence is combined into one immutable tuple;
- **decision precedence** — blocking problems are handled before convenient success;
- **conflict classification** — several packages differ from conflicting transitions for one package;
- **representative display value** — the first equivalent extracted record supplies readable package spelling while normalized identity controls equivalence.

Current Step 3 learning depth:

```text
structured explanation completed
+ actual source ownership and decision order reviewed
+ focused tests defined
but
no local execution recorded
no independent implementation practice recorded
no formal assessment recorded
not mastered
```

Product validation and learning mastery remain separate claims. Do not treat generated implementation or passing tests alone as mastery.

## Exact continuation

Synchronize the local checkout to current `main` and capture the exact execution boundary:

```bash
git switch main
git pull --ff-only
git rev-parse HEAD
git status --short
python --version
```

Run the focused Step 3 comparison tests first:

```bash
python -m unittest tests.test_dependency_change_comparison -v
```

Then preserve the prior dependency boundaries:

```bash
python -m unittest tests.test_exact_requirement_change -v
python -m unittest tests.test_dependency_change -v
python -m unittest tests.test_dependency_change_contracts -v
```

Run the complete deterministic suite:

```bash
python -m unittest discover -s tests -v
```

Expected counts if no unrelated tests are added:

```text
Step 3 comparison tests: 6
Step 2 exact-requirement tests: 10
legacy dependency tests: 6
Step 1 contract tests: 4
complete deterministic suite: 92
```

Then run the installed public regression control:

```bash
unset GITHUB_TOKEN
upgradepilot googlefonts/glyphsLib 1145
```

The S004 evidence chain should remain unchanged.

If all checks pass:

1. create one dated Step 3 validation record;
2. update this file with exact revision, interpreter, working-tree state, and outputs;
3. mark Step 3 behavior-validated;
4. only then discuss Step 4: exact PR base/head dependency-file acquisition.

If any check fails, remain in Step 3, diagnose the comparison or regression failure, correct it, and rerun focused and complete tests.

## Not established

- Step 3 behavior validation;
- CLI orchestration through the new file-level extraction and comparison flow;
- constraints-file CI consumption semantics;
- generic exact PR base/head dependency-file acquisition;
- reported-versus-decoded byte-size validation;
- `uv.lock` parsing;
- duplicate-group comparison;
- S001 dependency identity through the product;
- CLI migration to `DependencyVersionChange`;
- `DependencyCIExerciseResult` runtime behavior;
- PEP 440 runtime validation;
- Python-support relevance;
- compatibility, safety, maintainer action, or production readiness;
- mastery of Step 1, Step 2, or Step 3 concepts.

## State-maintenance rule

When route, selected plan, verified behavior, blocker, learning state, or exact continuation changes, update this file only. Change another file only when its stable responsibility or dated evidence changes.
