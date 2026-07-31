# B2 Step 8 — Multi-format command integration implementation

**Recorded:** 2026-07-31 21:23 +03:30  
**Route:** B2 — Public PR vertical slice  
**Step:** 8 — Integrate the multi-format dependency command path  
**Status:** Implemented; repository and public-case validation required

## Controlling authority

- Parent plan: [`../plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md`](../plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md)
- Focused Step 8 plan: [`../plans/B2_STEP_8_MULTI_FORMAT_COMMAND_INTEGRATION_PLAN.md`](../plans/B2_STEP_8_MULTI_FORMAT_COMMAND_INTEGRATION_PLAN.md)
- Architecture: [`../docs/architecture/ADR-0004-dependency-version-change-evidence.md`](../docs/architecture/ADR-0004-dependency-version-change-evidence.md)
- Previous validation: [`2026-07-31_2112_B2-step-7-ci-dependency-exercise-validation.md`](2026-07-31_2112_B2-step-7-ci-dependency-exercise-validation.md)

## Implemented revision boundary

Step 7 validated state before Step 8:

```text
1e10f0c2e5b9201bb40e1c62d1ac16dfcdb876a3
```

Latest Step 8 product/test implementation revision:

```text
16c74f887d960a5e2dede56d05d7a55c16395a08
```

The GitHub connector reported no combined commit statuses for this implementation revision. No repository execution is claimed in this record.

## Commits

Plan:

```text
ee2478cc6b16823721a17a12edc251ec73381dda
Finalize Step 8 multi-format command integration plan
```

Tests first:

```text
3d798e7e43c3e959f46efa5a4f1542377ac7c0b1
Test requirements and constraints source roles

2063168ae77bffc9693a9e08961dc90e5bca6260
Test Step 8 dependency source recognition

c9176d9a5a0e01d7d132ff80897df27bed36f3f0
Test Step 8 multi-format dependency analysis

4bf0ff33d8ce54f16e98e5b40b316094d0610caa
Test Step 8 coordinator CLI integration

6e4e5b310718882bfd4a5b37327a4eff468abf2b
Test Step 8 package integration exports

43b7c3da479d14a2f5651a1d1fe39d81ffb39e39
Locate uv lock recognition at coordinator boundary
```

Runtime source:

```text
e54217b7ccf165b7db29d3f764d1fe81592a0ae2
Separate requirements and constraints source roles

956fcf9dab4e0429a9458eac20e9638774420845
Add multi-format dependency analysis coordinator

3207ef0dec8a46cd14e62fc35b07b245fb001359
Integrate multi-format dependency command path

0d396cd435f9adefb379dabdb7c8152b86849a97
Export multi-format dependency analysis contracts

99de221f43563e9a522afee5f4024da88b1f4d71
Retire temporary legacy dependency ingress

16c74f887d960a5e2dede56d05d7a55c16395a08
Retire temporary legacy ingress tests
```

## Implemented coordinator

Created:

```text
src/upgradepilot/dependency_analysis.py
```

Public contracts:

```text
DependencyChangeAnalysis
DependencyChangeAnalysisResult
analyze_dependency_change
is_uv_lock_file
```

Successful result:

```text
DependencyChangeAnalysis
├── dependency: DependencyVersionChange
└── direct_requirements_install_path: str | None
```

The coordinator is the only active PR-wide source integration boundary.

## Source discovery and extraction

### Requirements and constraints

```text
is_exact_requirement_file(path)
→ requirements or constraints dependency evidence
→ extract_exact_requirement_changes(changed_file)
```

A new narrower helper now distinguishes:

```text
is_admitted_requirements_file(path)
→ requirements-family paths only
```

This helper does not prove installation. It only controls whether one successful source path may be offered separately to the current CI rule.

### uv.lock

```text
is_uv_lock_file(changed_file)
→ path-only exact lowercase basename recognition

is_modified_uv_lock_file(changed_file)
→ extraction status admission
```

Coordinator behavior:

```text
recognized non-modified uv.lock
→ unsupported_dependency_file_status
→ no exact base/head acquisition

recognized modified uv.lock
→ get_pull_request_base_file
→ get_pull_request_head_file
→ extract_uv_lock_changes
```

Arbitrary files are ignored.

## PR-wide trust

Every recognized source success and problem reaches:

```text
compare_extracted_dependency_changes
```

The coordinator does not prefer one source format.

Implemented outcomes include:

- one trusted transition;
- equivalent cross-format evidence with combined source records;
- conflicting raw transitions;
- several changed packages;
- recognized exact-requirement problems blocking convenient lockfile success;
- unavailable lockfile evidence blocking convenient requirements success;
- no supported dependency source.

## Direct-requirements CI input

A path is emitted only when exactly one distinct successful requirements-family source supports the trusted transition.

```text
one requirements path
→ that path

zero requirements paths
→ None

several requirements paths
→ None
```

Constraints and `uv.lock` never populate the field.

The coordinator does not infer installation. The Step 7 evaluator still must prove visible installation of the supplied exact path and direct changed-package invocation in successful exact-head CI.

## CLI migration

The active CLI now calls:

```text
analyze_dependency_change(
    pull_request,
    changed_files,
    repository_client,
)
```

It no longer imports or calls:

```text
LegacyDependencyIngress
extract_legacy_dependency_ingress
```

After one result narrowing, target, package, upstream, presentation, and CI dependency exercise use the previously validated shared contracts.

No direct requirements/constraints/`uv.lock` parser branch exists in `cli.py`.

## Legacy cleanup

Removed active temporary contracts:

```text
LegacyDependencyIngress
LegacyDependencyIngressResult
extract_legacy_dependency_ingress
```

Removed temporary tests:

```text
tests/test_legacy_dependency_ingress.py
```

Retained historical compatibility API:

```text
PinnedDependencyChange
UnsupportedDependencyChange
extract_pinned_dependency_change
```

The retained API is no longer used by the active command path.

## Package interface

New package-level exports:

```text
DependencyChangeAnalysis
DependencyChangeAnalysisResult
analyze_dependency_change
is_admitted_requirements_file
is_uv_lock_file
```

Temporary ingress names are not package-level exports.

## Changed files

Added:

```text
plans/B2_STEP_8_MULTI_FORMAT_COMMAND_INTEGRATION_PLAN.md
src/upgradepilot/dependency_analysis.py
tests/test_dependency_analysis.py
tests/test_step8_source_recognition.py
working-memory/2026-07-31_2123_B2-step-8-multi-format-command-integration-implementation.md
```

Modified:

```text
src/upgradepilot/__init__.py
src/upgradepilot/cli.py
src/upgradepilot/dependency_change.py
src/upgradepilot/exact_requirement_change.py
tests/test_cli.py
tests/test_exact_requirement_change.py
tests/test_package_interface.py
```

Removed:

```text
tests/test_legacy_dependency_ingress.py
```

The existing `uv.lock` parser, exact repository-file acquisition implementation, comparator, CI dependency-exercise module, package client, target interpreter, and upstream resolver were not broadened.

## Controlled proof obligations

### Coordinator tests

`tests/test_dependency_analysis.py` contains 12 tests covering:

1. requirements-only canonical identity and explicit path;
2. constraints-only identity without a requirements path;
3. modified `uv.lock` exact acquisition and provenance;
4. arbitrary-file ignoring;
5. recognized non-modified `uv.lock` stopping without acquisition;
6. exact-file acquisition scoping;
7. equivalent requirements plus `uv.lock` evidence;
8. conflicting transitions;
9. several packages;
10. recognized requirements problem precedence;
11. unavailable lockfile precedence;
12. no path guessing across several requirements sources.

### Source-recognition tests

`tests/test_step8_source_recognition.py` contains 2 tests separating `uv.lock` path recognition from modified-file admission.

`tests/test_exact_requirement_change.py` now contains 11 tests, including requirements-versus-constraints role separation.

### CLI tests

`tests/test_cli.py` now contains 9 tests, including:

- one coordinator call with PR identity, complete changed files, and repository client;
- S004-style explicit requirements input;
- S001-style `uv.lock` provenance and `None` CI path;
- unresolved CI independence from package/upstream work;
- dependency-problem stopping;
- generic evidence presentation.

### Package interface

`tests/test_package_interface.py` contains 2 tests covering Step 7 and Step 8 public contracts.

## Expected deterministic counts

Previously observed complete suite:

```text
138 tests
```

Net Step 8 change:

```text
+1 exact-requirement role test
-2 temporary legacy-ingress tests
+2 source-recognition tests
+12 coordinator tests
+1 CLI integration test
+1 package-interface test
= +15
```

Expected complete suite:

```text
153 tests
```

Focused Step 8 files contain:

```text
12 + 2 + 11 + 9 + 2 = 36 tests
```

These counts are derived from committed test methods. They are not observed results.

## Required validation

From the real checkout:

```bash
git switch main
git pull --ff-only

python -m unittest \
  tests.test_dependency_analysis \
  tests.test_step8_source_recognition \
  tests.test_exact_requirement_change \
  tests.test_cli \
  tests.test_package_interface \
  -v

python -m unittest discover -s tests -v
```

Expected:

```text
focused: 36 tests / OK
complete: 153 tests / OK
```

### Installed S004

```bash
unset GITHUB_TOKEN
upgradepilot googlefonts/glyphsLib 1145
```

Required material behavior:

```text
pytest 9.0.2 → 9.0.3
requirements-dev.txt exact_requirement evidence
CI dependency exercise: proven
exact_head_dependency_exercised
published pytest==9.0.3
2 of 2 provenance
pytest-dev/pytest release tag 9.0.3
unresolved_claim
```

### Installed S001

```bash
unset GITHUB_TOKEN
upgradepilot pydantic/pydantic 13432
```

Required dependency result:

```text
Package: soupsieve
Old version: 2.6
Proposed version: 2.8.4
Dependency evidence: uv.lock
Format: uv_lock
Extraction method: exact_base_head_files
```

Required exact provenance:

```text
base revision: 652a61ce4f9d7d76eaada31535807a485ece0e21
base blob: b4a68ab725de337889d50d5374ac0f05db7fb484
base bytes: 606307
head revision: aa2dc024d33f61cdef50bf1973ab5adf0a974f5a
head blob: def33fe05d78ab851ce91a33db5bc55a439873a1
head bytes: 606313
```

Required CI boundary when successful exact-head CI exists without an admitted lockfile-consumption rule:

```text
CI dependency exercise: unresolved
CI dependency exercise reason: dependency_exercise_not_proven
```

Package, upstream, and target stages must continue independently and report their own available/problem states.

## Scope explicitly not implemented

Step 8 does not implement:

- `uv.lock` CI-consumption proof;
- constraints CI-consumption proof;
- another dependency-file format;
- dynamic plugin discovery;
- PEP 440 ordering;
- crossed-release acquisition;
- target-Python support relevance;
- semantic release-note extraction;
- compatibility, safety, recommendation, or maintainer action;
- multi-package upgrade support.

## Stop line

Step 8 remains open until:

```text
focused Step 8 tests pass
+
complete deterministic suite passes
+
installed S004 remains proven
+
installed S001 establishes soupsieve 2.6 → 2.8.4 with exact provenance
+
installed S001 does not infer uv.lock CI consumption
```

Do not close the parent dependency-evidence plan or return to Python-support relevance before those proofs are observed and recorded.
