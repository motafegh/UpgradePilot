# B2 Step 8 — Public-case partial validation

**Recorded:** 2026-07-31 21:53 +03:30  
**Route:** B2 — Public PR vertical slice  
**Step:** 8 — Integrate the multi-format dependency command path  
**Status:** Public S001 and S004 gates passed; deterministic test gates still required

## Controlling authority

- Parent plan: [`../plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md`](../plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md)
- Focused Step 8 plan: [`../plans/B2_STEP_8_MULTI_FORMAT_COMMAND_INTEGRATION_PLAN.md`](../plans/B2_STEP_8_MULTI_FORMAT_COMMAND_INTEGRATION_PLAN.md)
- Architecture: [`../docs/architecture/ADR-0004-dependency-version-change-evidence.md`](../docs/architecture/ADR-0004-dependency-version-change-evidence.md)
- Implementation record: [`2026-07-31_2123_B2-step-8-multi-format-command-integration-implementation.md`](2026-07-31_2123_B2-step-8-multi-format-command-integration-implementation.md)

## Validation boundary

The user supplied installed anonymous command output for both public control cases:

```bash
unset GITHUB_TOKEN
upgradepilot pydantic/pydantic 13432

unset GITHUB_TOKEN
upgradepilot googlefonts/glyphsLib 1145
```

This record establishes live public-command behavior. It does not claim the focused Step 8 suite or complete deterministic suite, because those outputs were not supplied in this validation message.

## S001 installed integration passed

Observed identity:

```text
Repository: pydantic/pydantic
PR: 13432
Title: Bump soupsieve from 2.6 to 2.8.4
Merged: true
Base: main @ 652a61ce4f9d7d76eaada31535807a485ece0e21
Head: dependabot/uv/soupsieve-2.8.4 @ aa2dc024d33f61cdef50bf1973ab5adf0a974f5a
Changed-file records: 1
Changed file: uv.lock (modified)
```

Observed canonical dependency result:

```text
Dependency change: supported
Package: soupsieve
Old version: 2.6
Proposed version: 2.8.4
Dependency evidence records: 1
Dependency evidence: uv.lock
  Format: uv_lock
  Extraction method: exact_base_head_files
```

Observed exact source provenance:

```text
Base revision: 652a61ce4f9d7d76eaada31535807a485ece0e21
Base blob SHA: b4a68ab725de337889d50d5374ac0f05db7fb484
Base bytes: 606307
Head revision: aa2dc024d33f61cdef50bf1973ab5adf0a974f5a
Head blob SHA: def33fe05d78ab851ce91a33db5bc55a439873a1
Head bytes: 606313
```

These values exactly match the previously validated Step 4 acquisition and Step 5 extraction evidence.

## S001 downstream continuation passed

Observed target evidence:

```text
Target Python declaration: available
Target Python source: pyproject.toml @ aa2dc024d33f61cdef50bf1973ab5adf0a974f5a
Target Python blob SHA: 8271997ab85caa1af522954812a2749784432dc7
Target requires-python: >=3.10
```

Observed exact-head workflow acquisition:

```text
Exact-head workflow runs: 3
CI: completed / success / 59 jobs
Third party tests: completed / skipped / 17 jobs
codspeed: completed / success / 1 job
```

Observed CI dependency-exercise boundary:

```text
CI dependency exercise: unresolved
CI dependency exercise reason: dependency_exercise_not_proven
CI dependency exercise detail: Successful exact-head CI exists, but no admitted rule proved that it consumed and exercised the changed dependency.
```

Per-workflow transparency was preserved:

```text
CI
→ unresolved / direct_requirements_install_path_unavailable

Third party tests
→ no_successful_ci / no_successful_jobs

codspeed
→ unresolved / direct_requirements_install_path_unavailable
```

This is the required result. UpgradePilot established dependency identity but did not infer `uv.lock` consumption from the dependency-evidence path.

Observed package evidence:

```text
Package evidence: available
Published package: soupsieve==2.8.4
Distribution files: 2
```

Observed upstream boundary:

```text
Upstream source: unsupported_source
Upstream detail: PyPI metadata contains no well-known Source candidate.
```

This is a valid independent downstream stopping result. It does not weaken the established dependency, target, CI, or package evidence and is not a Step 8 integration failure.

## S004 installed regression passed

Observed canonical exact-requirements result:

```text
Repository: googlefonts/glyphsLib
PR: 1145
Changed file: requirements-dev.txt (modified)
Package: pytest
Old version: 9.0.2
Proposed version: 9.0.3
Dependency evidence: requirements-dev.txt
  Format: exact_requirement
  Extraction method: changed_file_patch
```

Observed preserved CI exercise:

```text
CI dependency exercise: proven
CI dependency exercise reason: exact_head_dependency_exercised
```

The proving workflow remained:

```text
Regression Tests
→ proven / source_installed_and_dependency_invoked
```

with visible evidence that it installed `requirements-dev.txt` and directly invoked `pytest`.

The multi-job workflow remained transparent non-proof:

```text
Test + Deploy
→ unresolved / multiple_or_zero_workflow_jobs
```

Observed preserved package and upstream evidence:

```text
Published package: pytest==9.0.3
Distribution files: 2
Upstream repository: pytest-dev/pytest
Provenance coverage: 2 of 2 files
Accepted tag: 9.0.3
Tag object SHA: 24ec4b54c06a74721a285dcc317825b1735f4717
Claim state: unresolved_claim
```

## What is now behavior-observed

```text
installed CLI uses the Step 8 coordinator for uv.lock
+
S001 exact base/head acquisition runs through the normal command
+
S001 uv.lock extraction establishes soupsieve 2.6 → 2.8.4
+
exact revision/blob/byte provenance is preserved
+
canonical downstream target and package stages continue
+
S001 does not infer uv.lock CI consumption
+
S004 exact-requirements behavior remains proven
+
requirements and uv.lock use the same generic dependency presentation
```

## Remaining Step 8 gates

The following outputs remain required before Step 8 and the parent dependency-evidence plan can be formally closed:

```text
focused Step 8 suite: expected 36 tests / OK
complete deterministic suite: expected 153 tests / OK
```

Required commands:

```bash
python -m unittest \
  tests.test_dependency_analysis \
  tests.test_step8_source_recognition \
  tests.test_exact_requirement_change \
  tests.test_cli \
  tests.test_package_interface \
  -v

python -m unittest discover -s tests -v
```

## Stop line

Step 8 remains open only because deterministic repository execution has not yet been supplied in this validation step.

Do not modify product source or begin the next route before the focused and complete suites pass. The two live public-case gates do not need to be repeated unless later product-source changes touch their path.
