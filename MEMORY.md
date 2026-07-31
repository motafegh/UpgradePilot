# UpgradePilot Current Memory

**Last updated:** 2026-07-31 19:57 +03:30  
**Authority:** Sole repository owner of live project position, verified behavior, blockers, and exact continuation.

Stable plans, ADRs, source, tests, and dated evidence retain their own responsibilities. This file records only the current state needed to continue.

## Live position

- **Route:** B2 — Public PR vertical slice.
- **Parent plan:** [`plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md`](plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md)
- **Step 6 controlling plan:** [`plans/B2_STEP_6_DOWNSTREAM_DEPENDENCY_INPUT_MIGRATION_PLAN.md`](plans/B2_STEP_6_DOWNSTREAM_DEPENDENCY_INPUT_MIGRATION_PLAN.md)
- **Accepted architecture:** [`docs/architecture/ADR-0004-dependency-version-change-evidence.md`](docs/architecture/ADR-0004-dependency-version-change-evidence.md)
- **Step 5 validation:** [`working-memory/2026-07-31_1854_B2-step-5-uv-lock-extraction-validation.md`](working-memory/2026-07-31_1854_B2-step-5-uv-lock-extraction-validation.md)
- **Step 6 implementation:** [`working-memory/2026-07-31_1957_B2-step-6-downstream-dependency-input-implementation.md`](working-memory/2026-07-31_1957_B2-step-6-downstream-dependency-input-implementation.md)
- **Last behavior-validated repository state:** `0925b9e2bf146be920f50f584201f346094743f0`.
- **Behavior-validated Step 5 product/test revision:** `82237ee4b11b1df7182a58cf5913194d8b231eac`.
- **Latest Step 6 product/test implementation revision:** `885d8aab5a3cfd187bf3fce179aabcbfccebeaac`.
- **Step 6 implementation-record revision:** `6d752597b76182ed8590437b03f0f761259639f6`.

Later evidence or memory commits do not alter the Step 6 product/test implementation revision.

## Current phase

Steps 1–5 are complete and behavior-validated.

Step 6 is fully implemented in source and tests but remains **open and unvalidated**:

```text
migrate downstream dependency input
```

Do not begin Step 7 CI-result migration or Step 8 multi-format command integration before Step 6 validation is complete.

## Step 6 implemented boundary

### Temporary legacy ingress

The installed command still enters through the validated exact-requirements path, but legacy identity is now contained behind:

```text
extract_legacy_dependency_ingress
```

Successful conversion:

```text
ChangedFile[]
→ PinnedDependencyChange
→ LegacyDependencyIngress
   ├── dependency: DependencyVersionChange
   └── direct_requirements_install_path: str
```

The conversion creates one source record:

```text
path = legacy source_file
file_format = exact_requirement
extraction_method = changed_file_patch
```

It does not invent exact base/head revision, blob, or byte evidence.

Unsupported legacy results remain unsupported.

### Canonical downstream identity

After ingress narrowing, runtime stages use only:

```text
DependencyVersionChange
├── package
├── normalized_package
├── old_version
├── proposed_version
├── source_evidence[]
└── limitations[]
```

Canonical identity now gates or feeds:

- target-Python acquisition;
- package release acquisition;
- upstream resolution;
- CI package identity;
- CLI dependency presentation.

`PinnedDependencyChange` is no longer imported by `cli.py` or `ci_authority.py`.

### Explicit CI input split

`evaluate_ci_authority` now accepts:

```text
DependencyVersionChange
+ WorkflowAuthorityInput[]
+ direct_requirements_install_path: str | None
```

The requirements path is keyword-only and independently supplied.

When it is absent and successful CI exists, the current evaluator returns:

```text
status: unresolved
reason: direct_requirements_install_path_unavailable
```

It never selects `source_evidence[0].path` or another generic evidence path as installation proof.

Controlled tests cover tempting paths including:

```text
uv.lock
constraints/base.txt
```

### Generic evidence presentation

The CLI success presentation now iterates canonical evidence:

```text
Dependency evidence records: N
Dependency evidence: <path>
  Format: <format>
  Extraction method: <method>
```

Optional exact base/head revisions, blob SHAs, and byte counts are printed when present. Limitations are printed when present.

The former singular line:

```text
Source file: requirements-dev.txt
```

is intentionally replaced by the generic evidence block.

## Step 6 files

Changed:

```text
src/upgradepilot/dependency_change.py
src/upgradepilot/ci_authority.py
src/upgradepilot/cli.py
tests/test_legacy_dependency_ingress.py
tests/test_ci_authority.py
tests/test_cli.py
```

Reviewed and intentionally unchanged:

```text
src/upgradepilot/workflow_commands.py
src/upgradepilot/__init__.py
```

`workflow_commands.py` already receives an explicit path and package identity. It remains a command reader, not a dependency-evidence interpreter.

Legacy package-level exports remain available until removal is separately selected. The transitional ingress conversion is not promoted to the package-level public API.

## Step 6 commits

```text
9316bb60a81be03b6f15d47ec36929b8adc7eacd
Test legacy dependency ingress conversion

fcc4a4832a0ed62938c257fb1c3e7b4d7506b234
Test explicit CI requirements input

e4b610db968dacb439b40657be8876867f002646
Test canonical downstream CLI input

3f7a2d2e1f18a12b0020ce4d507c49aa132ed7c3
Add canonical legacy ingress boundary

40b9dae529ffa5390032fcaaa83bc7bf2d33827c
Separate CI path from dependency identity

885d8aab5a3cfd187bf3fce179aabcbfccebeaac
Migrate CLI to canonical dependency input
```

## Validation status

No repository test pass is claimed yet.

The GitHub connector exposes no test runner and no status was present for the implementation head. The available container could not resolve `github.com`, so it could not clone and independently execute the repository.

Expected counts:

```text
focused Step 6 tests: 14
complete deterministic suite: 130
```

These are expectations, not observed passing results.

## Exact continuation

From the real checkout:

```bash
git switch main
git pull --ff-only

git rev-parse HEAD
git status --short
python --version
```

The history must include:

```text
885d8aab5a3cfd187bf3fce179aabcbfccebeaac
```

Run focused Step 6 tests:

```bash
python -m unittest \
  tests.test_legacy_dependency_ingress \
  tests.test_ci_authority \
  tests.test_cli \
  -v
```

Expected:

```text
Ran 14 tests
OK
```

Run the complete suite:

```bash
python -m unittest discover -s tests -v
```

Expected:

```text
Ran 130 tests
OK
```

Run installed anonymous S004:

```bash
unset GITHUB_TOKEN
upgradepilot googlefonts/glyphsLib 1145
```

Required material behavior remains:

```text
pytest 9.0.2 → 9.0.3
project_table_absent
exact-head CI authority sufficient
pytest==9.0.3
2 of 2 provenance
pytest-dev/pytest release tag 9.0.3
unresolved_claim
```

Required intentional presentation change:

```text
Dependency evidence records: 1
Dependency evidence: requirements-dev.txt
  Format: exact_requirement
  Extraction method: changed_file_patch
```

The singular `Source file:` line should be absent.

After all three proofs are supplied, create the dated Step 6 validation record, update this memory, and only then advance to Step 7.

## Not established

- Step 6 focused-suite pass;
- Step 6 complete-suite pass;
- post-migration installed S004 behavior;
- one-line installed S001 command behavior;
- normal CLI `uv.lock` recognition or exact-file acquisition;
- PR-wide multi-format comparison during command execution;
- `DependencyCIExerciseResult` runtime behavior;
- `uv.lock` or constraints CI-consumption rules;
- PEP 440 semantics;
- Python-support relevance;
- compatibility, safety, recommendation, maintainer action, or production readiness;
- user mastery.

## Learning state

Step 6 concepts now implemented and ready for review include:

- canonical domain model;
- compatibility boundary;
- separation of identity from source-specific operational evidence;
- explicit dependency injection through a keyword-only CI path;
- generic evidence rendering;
- localized future extension versus legitimate model change.

Current depth:

```text
structured explanation completed
+ focused architecture approved
+ tests written before source
+ source migration implemented
+ implementation diff reviewed
but
repository execution not yet observed
no user-owned technical explanation recorded
no independent implementation practice recorded
no formal assessment recorded
not mastered
```

Product behavior validation and learning mastery remain separate claims.

## State-maintenance rule

When route, selected plan, verified behavior, blocker, learning state, or exact continuation changes, update this file only. Change another file only when its stable responsibility or dated evidence changes.
