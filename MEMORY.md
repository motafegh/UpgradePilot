# UpgradePilot Current Memory

**Last updated:** 2026-07-31 22:58 +03:30  
**Authority:** Sole repository owner of live project position, verified behavior, blockers, and exact continuation.

Stable plans, ADRs, source, tests, and dated evidence retain their own responsibilities. This file records only the current state needed to continue.

## Live position

- **Route:** B2 — Public PR vertical slice.
- **Selected parent plan:** [`plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`](plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md)
- **Completed Step 1 plan:** [`plans/B2_STEP_1_UPSTREAM_INTERVAL_AUTHORITY_PLAN.md`](plans/B2_STEP_1_UPSTREAM_INTERVAL_AUTHORITY_PLAN.md)
- **Step 1 validation:** [`working-memory/2026-07-31_2238_B2-step-1-upstream-interval-authority-validation.md`](working-memory/2026-07-31_2238_B2-step-1-upstream-interval-authority-validation.md)
- **Completed Step 2 plan:** [`plans/B2_STEP_2_SUPPORT_DROP_CLAIM_CONTRACT_PLAN.md`](plans/B2_STEP_2_SUPPORT_DROP_CLAIM_CONTRACT_PLAN.md)
- **Step 2 validation:** [`working-memory/2026-07-31_2258_B2-step-2-support-drop-claim-contract-validation.md`](working-memory/2026-07-31_2258_B2-step-2-support-drop-claim-contract-validation.md)
- **Controlling Step 3 plan:** [`plans/B2_STEP_3_PACKAGING_METHOD_PLAN.md`](plans/B2_STEP_3_PACKAGING_METHOD_PLAN.md)
- **Step 3 architecture:** [`docs/architecture/ADR-0005-packaging-version-and-python-line-method.md`](docs/architecture/ADR-0005-packaging-version-and-python-line-method.md)
- **Step 3 implementation:** [`working-memory/2026-07-31_2258_B2-step-3-packaging-method-implementation.md`](working-memory/2026-07-31_2258_B2-step-3-packaging-method-implementation.md)
- **Behavior-validated Step 2 product/test revision:** `c023a3b09e5dc5d31e3bd0a55820b9d83a51f4db`.
- **Step 2 validation-record revision:** `2d6b42a1ee6867341e28c3d420557959eab104b3`.
- **Latest Step 3 product/test revision:** `52d56773342f5dfe31c41fb0e39e58cc745ef5bf`.
- **Step 3 implementation-record revision:** `ca388bc3ab6bab1b10e13136ae6e6f21fad4aa3e`.

Later validation, implementation-record, and memory commits do not alter the product/test revisions above.

## Current phase

The dependency-version-change foundation is complete and behavior-validated.

Target Python relevance Steps 1 and 2 are complete and behavior-validated.

Step 3 is fully implemented in source, dependency metadata, architecture, and controlled tests but remains **open and unvalidated**:

```text
Record and freeze the packaging method
```

Do not begin Step 4 deterministic relevance mapping until the focused and complete Step 3 suites pass.

## Last behavior-validated boundary

Step 2 validation established:

```text
AuthoritativeUpstreamIntervalEvidence
+ untrusted CandidateUpstreamClaimResult
→ GroundedPythonSupportDropClaim
   or explicit UpstreamSupportDropClaimProblem
```

The user reported both required Step 2 suites passed. Exact terminal summary lines and timings were not supplied and are not invented.

## Step 3 implemented boundary

### Runtime dependency

`pyproject.toml` now declares:

```text
packaging>=26.2,<27
```

The editable environment must refresh dependencies before Step 3 tests:

```bash
python -m pip install -e .
```

The runtime dependency test checks both the declared bound and the installed version.

### Pure standards method

Created:

```text
src/upgradepilot/packaging_method.py
```

It performs no network request, does not acquire target or upstream evidence, does not map final relevance states, and does not modify CLI behavior.

### Dependency release interval parsing

```text
DependencyReleaseInterval
→ parse_dependency_release_interval
→ ParsedDependencyReleaseInterval
   ├── exact raw interval
   ├── old_version: packaging.version.Version
   └── proposed_version: packaging.version.Version
```

Problems:

```text
invalid_python_package_version
equivalent_python_package_versions
dependency_version_not_forward
```

Raw evidence remains preserved even when PEP 440 parsing or ordering fails.

### Crossed-release ordering

```text
ParsedDependencyReleaseInterval
+ already selected exact raw release versions
→ order_crossed_release_versions
→ OrderedCrossedReleaseVersions
   ├── ordered_raw_versions[]
   └── ordered_versions[]
```

The method requires:

- old < release <= proposed;
- exact raw proposed version present;
- no PEP 440-equivalent duplicate raw identities;
- deterministic parsed order;
- raw and parsed identity correspondence.

Problems:

```text
invalid_crossed_release_version
crossed_release_outside_interval
equivalent_crossed_release_versions
proposed_release_missing
```

The method does not discover releases or assign source authority.

### Exact stable Python-line method

The selected product meaning is:

```text
Does requires-python admit at least one exact stable public PEP 440 version X.Y.Z?
```

where `Z` is a non-negative integer.

This is mathematical declaration evidence. It does not prove that the witness interpreter release was actually published or used.

Created:

```text
PythonLineSpecifierEvaluation
├── python_line
├── requires_python
├── normalized_requires_python
├── line_lower_bound
├── line_upper_bound
├── candidate_versions_checked[]
├── witness_version
└── contains_stable_release
```

Created:

```text
evaluate_python_line_specifier
```

### Boundary-complete witness derivation

The implementation does not enumerate patches to an arbitrary ceiling.

```text
patch candidates start with 0
+
for every admitted stable boundary in selected X.Y:
    derive Z - 1, Z, Z + 1
    discard negative patches
    sort and deduplicate

construct only Version("X.Y.Z")
→ evaluate with target.contains(candidate, prereleases=False)
```

A boundary such as `>=3.9.500000` directly derives and checks `3.9.500000`; it does not scan prior patches.

The initial broad interval-satisfiability design was reviewed and rejected because general PEP 440 satisfiability can use release tuples broader than exact `X.Y.Z`. The implementation and ADR were corrected before validation.

### Specifier boundary

Supported operators:

```text
< <= > >= == != ~=
```

Supported wildcard prefix forms:

```text
==X.Y.*
!=X.Y.*
```

Explicitly unsupported:

```text
=== arbitrary equality
epoch
local version
prerelease
development release
post release
more than three public release components
```

Problems:

```text
invalid_python_line
invalid_requires_python_specifier
unsupported_requires_python_specifier
unsatisfiable_requires_python_specifier
```

A globally contradictory target declaration is not ordinary line non-overlap.

### Public package interface

Exported:

```text
OrderedCrossedReleaseVersions
PackagingVersionProblem
ParsedDependencyReleaseInterval
PythonLineSpecifierEvaluation
PythonLineSpecifierProblem
order_crossed_release_versions
parse_dependency_release_interval
evaluate_python_line_specifier
```

Importing `upgradepilot` remains network-free.

## Controlled tests

Added:

```text
tests/test_packaging_version_method.py: 13 tests
tests/test_python_line_specifier_method.py: 34 tests
tests/test_runtime_dependency_contract.py: 2 tests
```

Updated:

```text
tests/test_package_interface.py: 1 new Step 3 test
```

Expected focused invocation total, including all package-interface tests:

```text
54 tests
```

Expected complete deterministic total:

```text
250 tests
```

These are derived counts, not observed passing results.

## Validation status

No Step 3 test pass is claimed.

The GitHub connector exposes no repository test runner and reported no combined status for `52d56773342f5dfe31c41fb0e39e58cc745ef5bf`.

No S001 or S004 repetition is required because Step 3 changes no active CLI, acquisition, dependency-analysis, CI, package-evidence, upstream-resolution, or target-Python path.

## Exact continuation

Run from the real checkout:

```bash
git switch main
git pull --ff-only
python -m pip install -e .

python -m unittest \
  tests.test_packaging_version_method \
  tests.test_python_line_specifier_method \
  tests.test_runtime_dependency_contract \
  tests.test_package_interface \
  -v

python -m unittest discover -s tests -v
```

Expected:

```text
focused: Ran 54 tests / OK
complete: Ran 250 tests / OK
```

After both pass:

1. create the dated Step 3 validation record;
2. close Step 3;
3. activate parent Step 4 — deterministic relevance with manual trusted inputs;
4. do not begin model integration, upstream network acquisition, conditional target acquisition, CLI orchestration, or S001 end-to-end integration during closure.

## Explicitly not established

- final target relevance result contracts;
- mapping a grounded support-drop claim and target declaration into overlap/non-overlap;
- interpreter release publication evidence;
- complete release-index network acquisition;
- exact tag peeling or tagged-changelog acquisition;
- model or Instructor integration;
- conditional target-Python activation;
- S001 `outside_declared_python_range` result;
- compatibility, safety, recommendation, maintainer action, or production readiness;
- user mastery.

## Learning state

Steps 1 and 2 concepts are behavior-validated at product level. Step 3 concepts are introduced and implemented:

- PEP 440;
- raw versus parsed version identity;
- equivalent and backwards version intervals;
- crossed-release ordering;
- `SpecifierSet` syntax and contradiction detection;
- exact stable `X.Y.Z` product meaning;
- symbolic boundary candidate derivation;
- witness evidence versus publication evidence;
- supported versus valid-but-out-of-scope specifier forms.

Current depth:

```text
structured explanations completed
+ focused plans and ADR created
+ tests written before implementation
+ Steps 1 and 2 suites reported passing
+ Step 3 implementation completed
+ broad satisfiability design reviewed and corrected
but
Step 3 repository execution not yet observed
no user-owned technical explanation recorded
no independent implementation practice recorded
no formal assessment recorded
not mastered
```

Product behavior validation and learning mastery remain separate claims.

## State-maintenance rule

When route, selected plan, verified behavior, blocker, learning state, or exact continuation changes, update this file only. Change another file only when its stable responsibility or dated evidence changes.
