# UpgradePilot Current Memory

**Last updated:** 2026-07-31 16:12 +03:30  
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
- **Validated product source revision:** `734c78e1b7754b14f2a8456fa415d3b714d24032`.
- **Step 2 validation-record revision:** `6bb668e319e6e707c7b236d05b4f6dc7560471b5`.

## Current phase

Step 1 is complete and behavior-validated.

Step 2 is complete and behavior-validated:

```text
move the existing exact-requirement extraction behavior
into a dedicated exact_requirement_change.py module
+ add the architecture-approved path-eligibility rule
+ produce file-level shared extraction results
+ preserve the legacy runtime API through a compatibility wrapper
```

Step 3 is the next bounded plan step, but implementation has not started:

```text
compare_extracted_dependency_changes
```

The next activity is a focused Step 3 discussion and source/test design review.

## Current behavior-validated product boundary

The validated product source revision is:

```text
734c78e1b7754b14f2a8456fa415d3b714d24032
```

Observed complete-suite result:

```text
Ran 86 tests in 0.021s
OK
```

The complete suite includes the 10 Step 2 exact-requirement tests, six legacy dependency tests, four Step 1 contract tests, and all other deterministic repository tests.

The installed anonymous public S004 control also passed:

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

The supplied Step 2 transcript did not repeat `python --version`, `git rev-parse HEAD`, or `git status --short`. The same active `.venv` previously reported Python 3.12.3, and repository `main` resolved to the validated source revision immediately after the run. Future validation records should capture those commands directly.

## Step 2 implementation now validated

The dedicated module is:

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

Path eligibility means only that a file may supply exact package/version evidence. It does not establish dependency role, installation, CI consumption, compatibility, safety, or maintainer action.

`extract_exact_requirement_changes` accepts one `ChangedFile` and returns:

```text
ExtractedDependencyVersionChange
or
DependencyChangeEvidenceProblem
```

Validated behavior includes:

- exact `package==version` grammar;
- complete-patch addition/deletion reconciliation;
- `modified` file-status requirement;
- package-name normalization;
- explicit ambiguity and stopping outcomes;
- `DependencyFileEvidence` preserving full path, `exact_requirement` format, and `changed_file_patch` method;
- translation from legacy outcomes to the shared ADR-0004 problem vocabulary.

## Legacy runtime compatibility

The current product runtime still calls:

```text
ChangedFile[]
→ extract_pinned_dependency_change
→ PinnedDependencyChange or UnsupportedDependencyChange
```

`extract_pinned_dependency_change` remains exported from `dependency_change.py` and delegates lazily to the moved exact-requirement implementation.

The lazy import avoids a module-initialization cycle because `exact_requirement_change.py` imports shared records from `dependency_change.py`.

The CLI, CI evaluator, workflow-command reader, and their output labels have not been migrated. `PinnedDependencyChange.source_file` still combines observed change evidence with the current requirements-install assumption.

`normalize_package_name` remains in `dependency_change.py` because exact-requirement extraction and `pypi_client.py` both use it.

## Learning state

Step 1 concepts remain at introductory explanatory depth, not mastered.

Step 2 introduced through concrete source:

- source-specific module ownership;
- path eligibility before syntax interpretation;
- file-level extracted evidence versus PR-wide trusted evidence;
- compatibility wrapper;
- lazy import for cycle avoidance;
- explicit legacy-to-shared problem translation.

Current Step 2 depth:

```text
introduced and explained through concrete source
+ validation observed
but
no independent implementation practice recorded
no user-owned explanation recorded
no formal assessment recorded
not mastered
```

Test execution and successful runtime behavior are product evidence, not mastery evidence.

## Exact continuation

Remain within the selected dependency-version-change plan.

Discuss Step 3 before modifying source. Review these cases in order:

1. no extracted changes;
2. one extracted change;
3. equivalent extracted changes with combined source evidence;
4. conflicting transitions;
5. several package transitions;
6. recognized dependency-file problems that must block trust.

The Step 3 implementation responsibility is limited to:

```text
all extracted changes and recognized file problems
→ compare_extracted_dependency_changes
→ DependencyVersionChange or DependencyChangeEvidenceProblem
```

Step 3 must not implement:

- generic exact PR base/head file acquisition;
- `uv.lock` parsing;
- duplicate-package-group comparison;
- CLI or CI migration;
- PEP 440 validation;
- Python-support relevance;
- recommendation or safety logic.

## Not established

- `compare_extracted_dependency_changes` runtime behavior;
- PR-wide trusted `DependencyVersionChange` production;
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
