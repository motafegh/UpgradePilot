# B2 Step 8 — Multi-Format Dependency Command Integration Plan

**Status:** Approved and controlling for Step 8  
**Recorded:** 2026-07-31 21:23 +03:30  
**Route:** B2 — Public PR vertical slice  
**Parent plan:** [`B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md`](B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md)  
**Architecture:** [`../docs/architecture/ADR-0004-dependency-version-change-evidence.md`](../docs/architecture/ADR-0004-dependency-version-change-evidence.md)

## Purpose

Replace the temporary requirements-only command ingress with one explicit multi-format dependency-analysis coordinator.

The coordinator must connect the already validated components:

```text
complete changed-file records
        │
        ├── exact requirements / constraints
        │     └── patch extraction
        │
        └── exact lowercase uv.lock path
              ├── unsupported status → explicit problem without file acquisition
              └── modified
                    └── exact base/head acquisition
                          └── uv.lock extraction
                                   │
                                   ▼
              compare_extracted_dependency_changes
                                   │
                    ┌──────────────┴──────────────┐
                    ▼                             ▼
        DependencyVersionChange     DependencyChangeEvidenceProblem
```

A trusted result then feeds the already validated target-Python, package, upstream, generic presentation, and CI dependency-exercise stages.

## Current problem

The installed command currently begins through:

```text
ChangedFile[]
→ extract_legacy_dependency_ingress
→ LegacyDependencyIngress
```

That temporary path can interpret only the legacy exact-requirements case. It cannot:

- recognize `uv.lock` during normal command execution;
- acquire exact base/head lockfiles;
- combine equivalent evidence across formats;
- stop on a recognized malformed or unavailable lockfile when another convenient source succeeds;
- produce S001 through `upgradepilot pydantic/pydantic 13432`.

All required source-specific parsers, exact-file acquisition methods, the shared comparator, canonical downstream identity, and shared CI exercise contract already exist and are behavior-validated independently.

## Selected architecture

### 1. One integration module

Create:

```text
src/upgradepilot/dependency_analysis.py
```

Public contracts:

```text
DependencyChangeAnalysis
DependencyChangeAnalysisResult
analyze_dependency_change
```

`DependencyChangeAnalysis` contains:

```text
dependency: DependencyVersionChange
direct_requirements_install_path: str | None
```

The canonical dependency record carries package/version identity and source evidence.

The optional direct-requirements path remains separate source-specific operational input for the current CI rule.

### 2. Static visible source coordination

The coordinator uses explicit source branches rather than a dynamic plugin framework:

```text
is_exact_requirement_file(path)
→ extract_exact_requirement_changes(changed_file)

is_uv_lock_file(changed_file)
→ status admission
→ exact base/head acquisition only when modified
→ extract_uv_lock_changes(changed_file, base, head)
```

A later same-meaning source format should add one explicit branch and focused tests. It must not require changes to package lookup, target acquisition, upstream resolution, generic presentation, or CI result semantics.

### 3. Requirements versus constraints CI input

`is_exact_requirement_file` intentionally admits both requirements and constraints as dependency evidence.

Add a narrower helper:

```text
is_admitted_requirements_file(path)
```

It identifies only admitted requirements-family paths, not constraints-family paths.

The coordinator may emit a direct-requirements install path only when:

1. file-level extraction succeeded;
2. the source is an admitted requirements-family file;
3. exactly one distinct requirements path supports the trusted PR-wide transition.

```text
one requirements path
→ expose that path to the current CI rule

zero requirements paths
→ None

several requirements paths
→ None
```

The coordinator must not choose one path by changed-file order, shortest path, filename preference, or known-case identity.

A constraints path never becomes direct-requirements CI input.

### 4. uv.lock recognition and acquisition

Add a path-only recognizer:

```text
is_uv_lock_file(changed_file)
```

It recognizes a normalized repository-relative path whose basename is exactly lowercase `uv.lock`, regardless of status.

Keep:

```text
is_modified_uv_lock_file(changed_file)
```

as the admitted exact-file extraction predicate.

Coordinator behavior:

```text
recognized uv.lock + status != modified
→ unsupported_dependency_file_status
→ no base/head acquisition

recognized modified uv.lock
→ acquire exact base
→ acquire exact head
→ extract
```

Added, deleted, and renamed lockfiles must therefore remain explicit recognized problems rather than being ignored as unsupported arbitrary files.

### 5. PR-wide comparison

Every source-specific success and every recognized source-specific problem is passed to:

```text
compare_extracted_dependency_changes
```

The coordinator must not:

- select the first successful parser;
- prefer requirements over `uv.lock`;
- prefer `uv.lock` over requirements;
- ignore a recognized problem because another file succeeded;
- choose one package from several transitions;
- collapse conflicting raw version transitions.

Equivalent source results combine source evidence.

### 6. Stopping behavior

A `DependencyChangeEvidenceProblem` is a normal evidence result, not an exception.

When returned by the coordinator, the CLI must:

```text
print dependency problem
skip target-Python acquisition
skip workflow acquisition and CI exercise
skip package acquisition
skip upstream resolution
```

GitHub transport failures and untyped malformed GitHub responses retain the existing CLI acquisition/response error handling.

Typed `UnavailableRepositoryFile` from exact base/head acquisition must become `dependency_file_unavailable` through the existing `uv.lock` extractor.

### 7. CLI boundary

Replace:

```text
extract_legacy_dependency_ingress
```

with:

```text
analyze_dependency_change(
    pull_request,
    changed_files,
    repository_client,
)
```

The command then narrows exactly once:

```text
DependencyChangeAnalysis
→ dependency_result = analysis.dependency
→ direct_requirements_install_path = analysis.direct_requirements_install_path

DependencyChangeEvidenceProblem
→ stop dependent stages
```

No direct exact-requirement or `uv.lock` parsing branch belongs in `cli.py`.

### 8. Legacy containment cleanup

After the command migrates:

- remove `LegacyDependencyIngress`;
- remove `LegacyDependencyIngressResult`;
- remove `extract_legacy_dependency_ingress`;
- remove `tests/test_legacy_dependency_ingress.py`.

Retain the older package-level `PinnedDependencyChange`, `UnsupportedDependencyChange`, and `extract_pinned_dependency_change` API for historical compatibility unless a separate deprecation/removal decision is selected.

The retained legacy parser must not be called by the active CLI.

## Required S004 behavior

Installed command:

```bash
upgradepilot googlefonts/glyphsLib 1145
```

must preserve:

```text
requirements-dev.txt
pytest 9.0.2 → 9.0.3
Dependency evidence format: exact_requirement
Target Python: project_table_absent
CI dependency exercise: proven
exact_head_dependency_exercised
published pytest==9.0.3
2 of 2 provenance
pytest-dev/pytest tag 9.0.3
unresolved_claim
```

The coordinator must not acquire exact base/head repository files for this requirements-only case.

## Required S001 behavior

Installed command:

```bash
upgradepilot pydantic/pydantic 13432
```

must establish:

```text
Dependency change: supported
Package: soupsieve
Old version: 2.6
Proposed version: 2.8.4
Dependency evidence: uv.lock
Format: uv_lock
Extraction method: exact_base_head_files
```

Exact provenance must remain:

```text
base revision: 652a61ce4f9d7d76eaada31535807a485ece0e21
base blob: b4a68ab725de337889d50d5374ac0f05db7fb484
base bytes: 606307

head revision: aa2dc024d33f61cdef50bf1973ab5adf0a974f5a
head blob: def33fe05d78ab851ce91a33db5bc55a439873a1
head bytes: 606313
```

No S001 repository, PR number, package, version, revision, blob, size, or expected answer may appear in product logic.

### S001 CI boundary

The coordinator must emit:

```text
direct_requirements_install_path = None
```

for a `uv.lock`-only transition.

If successful exact-head CI exists but no separately admitted consumption/exercise rule proves the lockfile path, the shared evaluator must report:

```text
CI dependency exercise: unresolved
```

The dependency, target, package, and upstream stages continue independently.

## Controlled tests before runtime source

### New coordinator tests

Create:

```text
tests/test_dependency_analysis.py
```

Prove at least:

1. one requirements transition produces canonical identity and one direct-requirements path;
2. one constraints transition produces canonical identity with no direct-requirements path;
3. one modified `uv.lock` acquires exact base/head files and preserves extracted provenance;
4. arbitrary files are ignored and produce `no_supported_dependency_file` when no admitted source exists;
5. non-modified recognized `uv.lock` produces `unsupported_dependency_file_status` without acquisition;
6. exact repository files are acquired only for admitted modified `uv.lock` records;
7. equivalent requirements and `uv.lock` transitions combine source evidence;
8. conflicting transitions remain `conflicting_dependency_version_changes`;
9. several package transitions remain `multiple_dependency_version_changes`;
10. a recognized exact-requirement problem blocks a convenient valid lockfile result;
11. an unavailable lockfile blocks a convenient valid requirements result;
12. several equivalent requirements paths do not cause one path to be guessed for CI.

### Source-recognition tests

Update exact-requirement tests to distinguish:

```text
is_exact_requirement_file
→ requirements or constraints evidence

is_admitted_requirements_file
→ requirements family only
```

Update `uv.lock` tests to distinguish path recognition from modified-file admission.

### CLI tests

Migrate CLI mocks from `LegacyDependencyIngress` to `DependencyChangeAnalysis`.

Prove:

- the coordinator receives pull-request identity, complete changed files, and the repository client;
- a coordinator problem stops all dependent stages;
- an S004-style analysis passes its explicit requirements path to CI;
- an S001-style analysis passes `None` to CI;
- S001 exact source provenance renders through the existing generic output;
- unresolved S001 CI does not block package/upstream work;
- the CLI contains no active legacy ingress call.

### Package-interface tests

Export:

```text
DependencyChangeAnalysis
DependencyChangeAnalysisResult
analyze_dependency_change
is_admitted_requirements_file
is_uv_lock_file
```

Do not export the retired temporary ingress names.

## Build order

1. commit this focused plan;
2. add source-recognition and coordinator tests;
3. migrate CLI and package-interface tests;
4. implement source-recognition helpers;
5. implement `dependency_analysis.py`;
6. migrate `cli.py`;
7. update package exports;
8. retire temporary legacy ingress code and tests;
9. audit active source/tests for temporary ingress references;
10. record implementation state as unvalidated;
11. run focused tests, complete suite, installed S004, and installed S001;
12. record validation and close the parent dependency-evidence plan only after all required behavior is observed.

## Explicit non-goals

Step 8 does not implement:

- `uv sync`, `uv run`, constraints, Poetry, Pipenv, or another new CI-consumption rule;
- dynamic plugin discovery or reflection;
- PEP 440 ordering;
- crossed-release acquisition;
- target-Python support-drop relevance;
- release-note semantic interpretation;
- compatibility, safety, recommendation, or maintainer action;
- broad YAML, shell, tox, nox, task-runner, or reusable-workflow tracing;
- multi-package upgrade support.

## Stop line

Step 8 is complete only when:

```text
one active multi-format coordinator
+
requirements and constraints use patch extraction
+
modified uv.lock uses exact base/head extraction
+
all recognized results/problems reach the shared comparator
+
LegacyDependencyIngress is absent from active command code
+
S004 remains materially intact and CI exercise is proven
+
S001 works through the installed one-line command
+
S001 exact provenance matches the validated base/head evidence
+
S001 CI exercise does not infer uv.lock consumption
+
focused tests pass
+
complete deterministic suite passes
```

Until those proofs are observed, Step 8 remains implemented or in progress—not behavior-validated.