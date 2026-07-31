# B2 Step 6 — Downstream dependency input implementation

**Recorded:** 2026-07-31 19:57 +03:30  
**Route:** B2 — Public PR vertical slice  
**Step:** 6 — Migrate downstream dependency input  
**Status:** Implemented; repository validation required

## Controlling authority

- Parent plan: [`../plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md`](../plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md)
- Focused Step 6 plan: [`../plans/B2_STEP_6_DOWNSTREAM_DEPENDENCY_INPUT_MIGRATION_PLAN.md`](../plans/B2_STEP_6_DOWNSTREAM_DEPENDENCY_INPUT_MIGRATION_PLAN.md)
- Architecture: [`../docs/architecture/ADR-0004-dependency-version-change-evidence.md`](../docs/architecture/ADR-0004-dependency-version-change-evidence.md)

## Implemented revision boundary

Planning/state base before Step 6 source work:

```text
75af7e9c9d344333360eabb320614852db71a274
```

Latest Step 6 product/test implementation revision:

```text
885d8aab5a3cfd187bf3fce179aabcbfccebeaac
```

No Step 7 result migration or Step 8 multi-format command integration was implemented.

## Commits

Tests first:

```text
9316bb60a81be03b6f15d47ec36929b8adc7eacd
Test legacy dependency ingress conversion

fcc4a4832a0ed62938c257fb1c3e7b4d7506b234
Test explicit CI requirements input

e4b610db968dacb439b40657be8876867f002646
Test canonical downstream CLI input
```

Runtime source:

```text
3f7a2d2e1f18a12b0020ce4d507c49aa132ed7c3
Add canonical legacy ingress boundary

40b9dae529ffa5390032fcaaa83bc7bf2d33827c
Separate CI path from dependency identity

885d8aab5a3cfd187bf3fce179aabcbfccebeaac
Migrate CLI to canonical dependency input
```

## Implemented architecture

### Legacy ingress containment

The temporary installed command path still begins with the validated exact-requirements extractor, but the legacy result is now contained behind:

```text
extract_legacy_dependency_ingress
```

Successful flow:

```text
ChangedFile[]
→ legacy exact-requirements extraction
→ PinnedDependencyChange
→ one compatibility conversion
→ LegacyDependencyIngress
   ├── dependency: DependencyVersionChange
   └── direct_requirements_install_path: str
```

`PinnedDependencyChange` is no longer passed to target, package, upstream, CI identity, or CLI presentation stages.

The compatibility conversion constructs one source record:

```text
DependencyFileEvidence
path = legacy source_file
file_format = exact_requirement
extraction_method = changed_file_patch
```

It does not invent base/head revisions, blob SHAs, or byte counts absent from legacy patch evidence.

Unsupported legacy outcomes remain unchanged and do not create canonical identity.

### Canonical downstream identity

The CLI now narrows the temporary ingress once and uses:

```text
DependencyVersionChange
```

for:

- target-Python stage gating;
- package/version lookup;
- upstream stage gating;
- CI package identity;
- generic dependency presentation.

Downstream identity reads only:

```text
package
normalized_package
old_version
proposed_version
source_evidence[]
limitations[]
```

No package, target, or upstream branch selects behavior from `exact_requirement` or `uv_lock`.

### Explicit CI input

`evaluate_ci_authority` now accepts:

```text
DependencyVersionChange
+ workflow evidence
+ keyword-only direct_requirements_install_path: str | None
```

The current result names and decision order remain unchanged:

```text
sufficient
insufficient
unresolved
```

A successful exact-head workflow can be sufficient only when the caller separately supplies an explicit direct-requirements path and the workflow visibly installs that path and directly invokes the package.

When the explicit path is absent, a successful workflow stops as:

```text
status: unresolved
reason: direct_requirements_install_path_unavailable
```

The evaluator does not inspect or select `DependencyFileEvidence.path` as installation proof.

This applies even when generic evidence contains a tempting path such as:

```text
uv.lock
constraints/base.txt
```

### Generic dependency presentation

The CLI now presents:

```text
Dependency change: supported
Package: ...
Old version: ...
Proposed version: ...
Dependency evidence records: N
```

It iterates every `source_evidence` record and prints:

- path;
- file format;
- extraction method;
- optional exact base/head revision, blob, and byte fields.

It also iterates `limitations` when present.

There is no separate success branch for exact requirements versus `uv.lock` presentation.

The former singular output:

```text
Source file: requirements-dev.txt
```

is intentionally replaced by the generic evidence block.

## Files changed

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

`workflow_commands.py` already accepts an explicit path and package identity. It remains a command-inspection helper and does not inspect dependency evidence.

`__init__.py` already exposes the canonical shared contracts. Legacy exports remain intentionally available until their removal is separately selected; the transitional ingress conversion is not promoted to the package-level public API.

## Added and migrated proof obligations

### New focused ingress tests

`tests/test_legacy_dependency_ingress.py` proves:

1. a generic fictional exact-requirements transition converts to canonical identity;
2. package-name normalization and exact raw versions are preserved;
3. one `exact_requirement`/`changed_file_patch` source record is created;
4. the direct-requirements path is separate from canonical identity;
5. unsupported legacy evidence remains unsupported;
6. no S004 repository, package, version, or expected-result condition is hardcoded.

### Migrated CI tests

`tests/test_ci_authority.py` now constructs `DependencyVersionChange` directly and proves:

- the explicit S004-style requirements path can preserve the sufficient rule;
- existing unresolved and insufficient decision paths remain represented;
- missing explicit path remains unresolved;
- `uv.lock` evidence is not automatic `pip -r` proof;
- constraints evidence is not automatic direct-requirements proof.

### Migrated CLI tests

`tests/test_cli.py` proves:

- target, package, upstream, and CI receive canonical identity after ingress;
- CI receives the direct-requirements path separately;
- package/upstream problem stopping remains intact;
- unsupported identity skips dependent stages;
- exact-requirement evidence renders generically;
- controlled `uv_lock` exact provenance renders through the same helper;
- several evidence records and limitations render without format-specific branches.

## Scope explicitly not implemented

Step 6 does not implement:

- normal CLI recognition or acquisition of `uv.lock`;
- `upgradepilot pydantic/pydantic 13432` as the S001 command path;
- PR-wide multi-format coordination in the CLI;
- `DependencyCIExerciseResult` or the `proven`/`no_successful_ci` vocabulary;
- `uv sync`, `uv run`, or constraints CI-consumption rules;
- PEP 440 interpretation;
- Python-support relevance;
- compatibility, safety, recommendation, or maintainer action;
- a dynamic plugin framework.

## Validation status

No repository test execution is claimed in this record.

The connector exposes no test runner and returned no commit status for `885d8aab...`. The local container could not resolve `github.com`, so it could not clone or execute the committed repository independently.

Expected test counts based on the validated Step 5 total and added test methods:

```text
focused Step 6 tests: 14
complete deterministic suite: 130
```

These are expectations, not observed passing results.

## Required validation

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

Then run the installed anonymous S004 regression:

```bash
unset GITHUB_TOKEN
upgradepilot googlefonts/glyphsLib 1145
```

Expected material behavior remains:

```text
pytest 9.0.2 → 9.0.3
target Python project_table_absent
exact-head CI authority sufficient
pytest==9.0.3
2 of 2 provenance
pytest-dev/pytest release tag 9.0.3
unresolved_claim
```

Expected intentional presentation change:

```text
Dependency evidence records: 1
Dependency evidence: requirements-dev.txt
  Format: exact_requirement
  Extraction method: changed_file_patch
```

The singular `Source file:` line should no longer appear.

## Stop line

Step 6 remains open until the focused suite, complete suite, and installed S004 regression are supplied and recorded.

Do not start Step 7 before that validation is complete.
