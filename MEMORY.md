# UpgradePilot Current Memory

**Last updated:** 2026-07-30 22:01 +03:30  
**Authority:** Sole repository owner of live project position, verified behavior, blockers, and exact continuation.

Stable route definitions, specifications, ADRs, source, tests, plans, and dated evidence retain their own responsibilities. This file records only the current position needed to continue.

## Live position

- **Route:** B2 — Public PR vertical slice.
- **Controlling route:** [`plans/UPGRADEPILOT_90_DAY_PLAN.md`](plans/UPGRADEPILOT_90_DAY_PLAN.md)
- **B2 gate:** [`plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md`](plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md)
- **Selected plan:** [`plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md`](plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md)
- **Accepted architecture:** [`docs/architecture/ADR-0004-dependency-version-change-evidence.md`](docs/architecture/ADR-0004-dependency-version-change-evidence.md)
- **Step 1 validation:** [`working-memory/2026-07-30_2138_B2-step-1-dependency-contracts-validation.md`](working-memory/2026-07-30_2138_B2-step-1-dependency-contracts-validation.md)
- **Latest relevant non-memory revision:** `423fe29aca26a7969556f97eb4ddae77cf85aa0f`.

## Current phase

Step 1 is complete and behavior-validated.

Step 2 source and tests are now implemented on `main`:

```text
move the existing exact-requirement extraction behavior
into a dedicated exact_requirement_change.py module
+ add the architecture-approved path-eligibility rule
+ produce file-level shared extraction results
+ preserve the legacy runtime API through a compatibility wrapper
```

Step 2 has **not** yet been behavior-validated in the real Python 3.12 checkout.

Do not begin Step 3.

## Last behavior-validated product boundary

The latest behavior-validated source revision remains:

```text
60837a65883e1d21229e383ee47225839d49e951
```

Validation at that revision used:

```text
Python 3.12.3
focused Step 1 contracts: 4 passed
legacy dependency behavior: 6 passed
complete deterministic suite: 76 passed
installed anonymous S004 command: passed
```

The current Step 2 commits do not extend this behavior-validated boundary until their focused, legacy, complete-suite, and installed-command checks pass.

## Step 2 implementation present on main

Added:

```text
src/upgradepilot/exact_requirement_change.py
```

Public functions:

```text
is_exact_requirement_file
extract_exact_requirement_changes
```

`is_exact_requirement_file` admits:

- conventional lowercase `requirements...txt/.in` and `constraints...txt/.in` final filenames;
- `.txt` or `.in` files beneath an exact lowercase `requirements` or `constraints` directory component;
- the same rules at any repository depth while preserving the complete relative path.

Path eligibility establishes only that a file may supply exact package/version evidence. It does not establish dependency role, installation, CI consumption, compatibility, safety, or maintainer action.

`extract_exact_requirement_changes` accepts one `ChangedFile` and returns:

```text
ExtractedDependencyVersionChange
or
DependencyChangeEvidenceProblem
```

It preserves:

- exact `package==version` grammar;
- complete-patch addition/deletion reconciliation;
- `modified` file-status requirement;
- package-name normalization;
- explicit ambiguity and stopping outcomes;
- `DependencyFileEvidence` with the full path, `exact_requirement` format, and `changed_file_patch` method.

The implementation translates legacy parser outcomes into the shared ADR-0004 problem vocabulary.

## Legacy runtime compatibility

The current product runtime still calls:

```text
ChangedFile[]
→ extract_pinned_dependency_change
→ PinnedDependencyChange or UnsupportedDependencyChange
```

`extract_pinned_dependency_change` remains exported from `dependency_change.py` and now delegates lazily to the moved exact-requirement implementation.

The lazy import avoids a module-initialization cycle because `exact_requirement_change.py` imports shared records from `dependency_change.py`.

The CLI, CI evaluator, workflow-command reader, and their output labels have not been migrated. `PinnedDependencyChange.source_file` still combines observed change evidence with the current requirements-install assumption.

`normalize_package_name` remains in `dependency_change.py` because it is shared by exact-requirement extraction and `pypi_client.py`.

## Step 2 tests present

Added:

```text
tests/test_exact_requirement_change.py
```

The module defines 10 tests covering:

- accepted conventional root and nested requirements/constraints paths;
- rejection of arbitrary or invalid relative paths;
- one file-level extracted change with source evidence;
- ineligible-path rejection before patch interpretation;
- missing patch;
- incomplete patch;
- unsupported requirement range syntax;
- unsupported file status;
- multiple exact transitions;
- mismatched package identities.

The six legacy dependency tests and four Step 1 contract tests remain unchanged.

## Relevant Step 2 revisions

```text
ee4c4450dfa97f5b4e53e2a243fa37ff83d72b92
Add exact requirement change module

5ce3a7a849ffce2d6f8fe969ea52d4b249885a14
Delegate legacy dependency extraction

2e8d2f69ba764de66a4c080b200ac8da29b3257d
Export exact requirement APIs

e9c6bd81efa4c960be22e4b9e80ff3473c3fb583
Test exact requirement extraction

423fe29aca26a7969556f97eb4ddae77cf85aa0f
Restore dependency contract documentation
```

These commits were fast-forwarded onto `main` without force and without a pull request.

## Learning state

Step 1 concepts remain at introductory explanatory depth, not mastered.

Step 2 has introduced in concrete source:

- **source-specific module ownership** — shared records stay separate from format-specific parsing;
- **path eligibility** — file identity is checked before interpreting requirement-like text;
- **compatibility wrapper** — an old public API delegates to moved implementation while callers remain stable;
- **lazy import** — an import performed inside a function to avoid module-initialization cycles;
- **problem translation** — legacy outcome strings are mapped to one shared result vocabulary.

Current Step 2 learning depth:

```text
implementation structure reviewed and explained
but
no local execution recorded
no independent implementation practice recorded
no formal assessment recorded
not mastered
```

## Exact continuation

Synchronize the local checkout to current `main`, then capture exact revision and working-tree state:

```bash
git switch main
git pull --ff-only
git rev-parse HEAD
git status --short
```

The expected revision before further changes is:

```text
423fe29aca26a7969556f97eb4ddae77cf85aa0f
```

Run with the admitted interpreter:

```bash
python --version
python -m unittest tests.test_exact_requirement_change -v
python -m unittest tests.test_dependency_change -v
python -m unittest tests.test_dependency_change_contracts -v
python -m unittest discover -s tests -v
```

Expected test counts if no unrelated tests are added:

```text
exact-requirement Step 2 tests: 10
legacy dependency tests: 6
Step 1 contract tests: 4
complete deterministic suite: 86
```

Then run the installed public control:

```bash
unset GITHUB_TOKEN
upgradepilot googlefonts/glyphsLib 1145
```

The S004 evidence chain should remain unchanged.

If all checks pass:

1. create one dated Step 2 validation record;
2. update this file with the exact validated revision and outputs;
3. mark Step 2 behavior-validated;
4. only then discuss Step 3: `compare_extracted_dependency_changes`.

If any check fails, remain in Step 2, diagnose the failure, correct it, and rerun the focused and complete suites.

## Not established

- Step 2 behavior validation;
- PR-wide `compare_extracted_dependency_changes` behavior;
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
- mastery of Step 1 or Step 2 concepts.

## State-maintenance rule

When route, selected plan, verified behavior, blocker, learning state, or exact continuation changes, update this file only. Change another file only when its stable responsibility or dated evidence changes.
