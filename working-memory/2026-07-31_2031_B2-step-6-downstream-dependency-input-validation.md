# B2 Step 6 — Downstream dependency input validation

**Recorded:** 2026-07-31 20:31 +03:30  
**Route:** B2 — Public PR vertical slice  
**Step:** 6 — Migrate downstream dependency input  
**Status:** Complete and behavior-validated

## Controlling authority

- Parent plan: [`../plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md`](../plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md)
- Focused Step 6 plan: [`../plans/B2_STEP_6_DOWNSTREAM_DEPENDENCY_INPUT_MIGRATION_PLAN.md`](../plans/B2_STEP_6_DOWNSTREAM_DEPENDENCY_INPUT_MIGRATION_PLAN.md)
- Architecture: [`../docs/architecture/ADR-0004-dependency-version-change-evidence.md`](../docs/architecture/ADR-0004-dependency-version-change-evidence.md)
- Implementation record: [`2026-07-31_1957_B2-step-6-downstream-dependency-input-implementation.md`](2026-07-31_1957_B2-step-6-downstream-dependency-input-implementation.md)

## Validated product/test revision

The Step 6 product and test implementation under validation is:

```text
885d8aab5a3cfd187bf3fce179aabcbfccebeaac
```

Later implementation-record and memory commits do not alter that product/test revision.

The supplied transcript showed a shell prompt on branch `main`, but did not include the output of:

```text
git rev-parse HEAD
git status --short
python --version
```

Therefore the exact local checkout SHA, clean-tree state, and interpreter version are not independently recorded here. This limitation does not change the observed behavioral results below.

## Deterministic suite

Observed user-supplied result:

```text
----------------------------------------------------------------------
Ran 130 tests in 0.036s

OK
```

This establishes that the complete deterministic suite passed after the Step 6 migration.

A separate focused-suite summary such as `Ran 14 tests` was not supplied. The focused tests are part of the complete suite, but their independent invocation is not claimed.

## Installed anonymous S004 regression

Command observed:

```bash
unset GITHUB_TOKEN
upgradepilot googlefonts/glyphsLib 1145
```

The installed public command preserved the validated S004 identity and evidence chain:

```text
Repository: googlefonts/glyphsLib
PR: 1145
Changed file: requirements-dev.txt (modified)
Package: pytest
Old version: 9.0.2
Proposed version: 9.0.3
Target Python declaration: project_table_absent
Exact-head workflow runs: 2
CI authority: sufficient
CI authority reason: exact_head_dependency_exercised
Published package: pytest==9.0.3
Distribution files: 2
Upstream repository: pytest-dev/pytest
Provenance coverage: 2 of 2 files
Accepted tag: 9.0.3
Tag object SHA: 24ec4b54c06a74721a285dcc317825b1735f4717
Claim state: unresolved_claim
```

The sufficient CI detail still established that the `Regression Tests` workflow visibly installed `requirements-dev.txt` and directly invoked `pytest` in successful exact-head CI.

The second `Test + Deploy` workflow remained unresolved under the existing multiple-job boundary. Step 6 therefore preserved the prior CI decision order and did not weaken the direct-requirements rule.

## Validated intentional presentation change

The installed CLI now rendered canonical dependency evidence:

```text
Dependency evidence records: 1
Dependency evidence: requirements-dev.txt
  Format: exact_requirement
  Extraction method: changed_file_patch
```

The former singular presentation:

```text
Source file: requirements-dev.txt
```

was absent.

This validates that the CLI now presents the canonical `DependencyVersionChange.source_evidence` collection rather than reading the legacy `PinnedDependencyChange.source_file` field.

## Step 6 stop-line result

Validated:

```text
all downstream identity consumers use DependencyVersionChange
+
PinnedDependencyChange is contained at the legacy ingress boundary
+
CI package identity and direct-requirements install path are separate inputs
+
generic source-evidence paths do not become installation proof
+
generic dependency-evidence presentation is active
+
S004 behavior remains materially intact
+
complete deterministic suite passes
```

Step 6 is therefore complete and behavior-validated.

## What Step 6 established

The active exact-requirements command path now performs one temporary compatibility conversion:

```text
ChangedFile[]
→ PinnedDependencyChange
→ LegacyDependencyIngress
   ├── dependency: DependencyVersionChange
   └── direct_requirements_install_path
```

After that boundary:

- target-Python gating uses canonical dependency identity;
- package acquisition uses canonical package/version identity;
- upstream resolution remains dependent on package evidence rather than source syntax;
- CI receives canonical identity plus an independently supplied direct-requirements path;
- CLI presentation iterates generic source evidence.

## What Step 6 did not establish

This validation does not establish:

- one-line installed S001 behavior;
- normal CLI recognition or exact-file acquisition for `uv.lock`;
- PR-wide multi-format coordination during command execution;
- final `DependencyCIExerciseResult` names and states;
- `uv.lock`, constraints, or other source-specific CI-consumption rules;
- PEP 440 ordering;
- Python-support relevance;
- compatibility, safety, recommendation, maintainer action, or production readiness;
- user mastery.

## Next bounded step

Step 7 is now authorized:

```text
migrate CI result names and semantics
```

Step 7 must introduce the shared `DependencyCIExerciseResult` boundary while preserving the validated direct-requirements behavior and the distinction among:

```text
proven
no_successful_ci
unresolved
```

Step 8 multi-format command integration remains blocked until Step 7 is behavior-validated.
