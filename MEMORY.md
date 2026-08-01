# UpgradePilot Current Memory

**Last updated:** 2026-08-02  
**Authority:** Sole repository owner of live project position, verified behavior, blockers, selected continuation, and current learning state.

Stable plans, specifications, ADRs, source, tests, and dated working records retain their own responsibilities. They must not mirror or compete with this file for live status.

## Single-live-state rule

`MEMORY.md` is the only repository file allowed to answer what is selected now, what behavior is verified, what remains open, what happens next, and what learning depth is established.

This file is replacement state, not append-only history. Remove superseded live statements when the project advances; Git history and dated evidence preserve history.

## Live position

- **Execution branch:** `main`. No separate implementation branch is selected.
- **Route:** B2 — Public PR vertical slice.
- **Selected parent plan:** [`plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`](plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md)
- **Completed and behavior-validated:** parent-plan Steps 1–4.
- **Selected Step 5 plan:** [`plans/B2_STEP_5_UPSTREAM_INTERVAL_ACQUISITION_PLAN.md`](plans/B2_STEP_5_UPSTREAM_INTERVAL_ACQUISITION_PLAN.md)
- **Current responsibility:** Step 5A — acquire a complete PyPI package release index and deterministically earn `CrossedReleaseIndexEvidence`.
- **Current Step 5A state:** implemented with controlled tests; **local validation is required before Step 5B tag resolution/peeling begins**.
- **Step 4 validation record:** [`working-memory/2026-08-02_B2-step-4-target-python-relevance-validation.md`](working-memory/2026-08-02_B2-step-4-target-python-relevance-validation.md)
- **Step 5A implementation record:** [`working-memory/2026-08-02_B2-step-5a-release-index-implementation.md`](working-memory/2026-08-02_B2-step-5a-release-index-implementation.md)

## Last behavior-validated executable boundary

The user pulled `main` through repository head:

```text
9d09a669fe8f7ba31fdd326baa119f6ec2e1559a
```

and reported the complete deterministic suite:

```text
Ran 263 tests in 0.058s

OK
```

That complete run contains the Step 4 target-Python relevance tests and package-interface test. A separate focused Step 4 rerun is not required solely to establish the same executable behavior.

The Step 4 product/test implementation boundary is:

```text
cceb8da55e5908f346141545eacdca4672f7d977
```

Later commits through the locally tested head changed only documentation/state records relative to that Step 4 product/test boundary.

## Step 4 closure

Step 4 is **closed and behavior-validated**.

Established pure mapping:

```text
UpstreamSupportDropClaimResult
+ conditional TargetPythonEvidence
→ TargetPythonRelevanceResult
```

with bounded states:

```text
declared_python_overlap
outside_declared_python_range
target_declaration_unresolved
upstream_claim_unresolved
comparison_unsupported
```

The result remains target-declaration relevance only. It is not compatibility, safety, merge readiness, or a maintainer action.

## Step 5 controlling purpose

Step 5 must earn the exact upstream interval evidence records already defined by Step 1 rather than manually constructing them.

The first S001-capable path is intentionally:

```text
DependencyReleaseInterval
+ trusted upstream repository
→ PyPI project release index
→ complete admitted crossed-release index

trusted upstream repository
+ proposed-version tag
→ resolved immutable tag commit
→ exact bounded changelog file
→ TaggedChangelogEvidence

crossed-release index
+ tagged changelog
→ assemble_upstream_interval_authority(...)
→ AuthoritativeUpstreamIntervalEvidence
```

A complete GitHub Release-body series remains an alternative Step 1 authority path, but it is not required merely to prove S001 when an exact tagged changelog establishes interval-wide authority.

## Step 5A implemented boundary awaiting validation

The current Step 5A product/test revision is:

```text
4ad56dabf6613f7ad46b096bcda7198ac1baff25
```

Later Step 5A implementation-record and `MEMORY.md` commits do not alter this executable boundary.

### PyPI release-index acquisition

`src/upgradepilot/pypi_client.py` now separates two source facts:

```text
PyPIReleaseClient
→ one exact package/version release

PyPIReleaseIndexClient
→ one package's complete raw project release-key set
```

New contracts:

```text
PackageReleaseIndexEvidence
PackageReleaseIndexProblem
PackageReleaseIndexResult
PyPIReleaseIndexClient
```

The release-index evidence preserves requested/normalized/published package identity, PyPI project URL, retrieval time, `last_serial`, and exact raw release keys.

Acquisition deliberately does **not** give the raw keys semantic version order.

### Crossed-release selection

Created:

```text
src/upgradepilot/upstream_interval_acquisition.py
```

Public flow:

```text
PackageReleaseIndexEvidence
+ DependencyReleaseInterval
+ upstream repository identity
→ select_crossed_release_index(...)
→ SelectedCrossedReleaseIndex
   or CrossedReleaseIndexSelectionProblem
```

The selector:

1. verifies package identity;
2. parses old/proposed bounds through the accepted Step 3 PEP 440 method;
3. uses `packaging.version.Version` to identify releases satisfying `old < release <= proposed`;
4. delegates exact proposed-version presence, equivalent selected identities, interval checking, and deterministic final ordering to `order_crossed_release_versions`;
5. constructs the existing trusted `CrossedReleaseIndexEvidence` contract.

### Legacy/non-PEP-440 release keys

A raw PyPI project key that cannot be parsed under PEP 440 is not silently dropped and is not guessed into the interval.

It is preserved in:

```text
SelectedCrossedReleaseIndex.ignored_non_pep440_versions
```

The successful Step 1 index therefore means the complete set of **admitted PEP 440 release identities** inside the selected dependency interval.

### New tests

Added:

```text
tests/test_pypi_release_index.py
tests/test_upstream_interval_acquisition.py
```

and extended the package-interface contract.

The controlled cases cover source identity, malformed/missing/acquisition failures, S001-shaped interval selection, old-exclusive/proposed-inclusive boundaries, exact source provenance, ignored non-PEP-440 keys, missing exact proposed release, PEP 440-equivalent duplicates, identity mismatch, invalid dependency bounds, and public argument validation.

No Step 5A test pass is claimed yet.

## Exact continuation

From the real checkout:

```bash
git pull --ff-only

python -m unittest \
  tests.test_pypi_client \
  tests.test_pypi_release_index \
  tests.test_upstream_interval_acquisition \
  tests.test_package_interface \
  -v

python -m unittest discover -s tests -v
```

Derived counts at the current Step 5A product/test boundary are:

```text
focused: 32 tests
complete: 281 tests
```

These are derived expectations only. Observed terminal output controls validation truth.

If validation fails, diagnose and repair only within the Step 5A source/integration boundary unless evidence proves an older regression.

If validation passes:

1. close Step 5A as behavior-validated;
2. activate Step 5B — exact proposed-version Git tag resolution and bounded annotated-tag peeling;
3. do not begin tagged changelog file acquisition until the tag-resolution increment itself is validated.

## Stop line

Until Step 5A validates, do not begin:

- Step 5B Git tag resolution/peeling;
- exact tagged-changelog file acquisition;
- semantic claim extraction/model integration;
- target-Python or CLI orchestration changes;
- S001 live end-to-end product execution;
- compatibility, safety, merge, defer, targeted-check, or recommendation logic.

## Explicitly not established

- a passing Step 5A focused suite;
- a passing complete suite containing Step 5A;
- live PyPI release-index acquisition against S001;
- exact Git tag-to-commit resolution;
- tagged-changelog acquisition;
- automated semantic extraction/model path;
- conditional target-Python activation in CLI runtime;
- S001 automated end-to-end relevance result;
- compatibility, safety, recommendation, maintainer action, or production readiness;
- user mastery of Steps 1–5A.

## Learning state

Steps 1–4 are behavior-validated at product level. Step 5A concepts are introduced and implemented but not yet behavior-validated.

Step 5A learning concepts include:

- **source evidence versus interpreted evidence:** PyPI raw release keys are acquired before version meaning is assigned;
- **PEP 440 (Python Enhancement Proposal 440):** the maintained Python package-version standard supplies ordering semantics rather than lexical string order;
- **old-exclusive/proposed-inclusive interval:** the old dependency release is excluded while the proposed release is included;
- **exact raw identity versus parsed equality:** two different strings may represent the same PEP 440 version and therefore cannot silently become two trusted releases;
- **out-of-scope preservation:** non-PEP-440 registry keys remain visible even though they do not enter the admitted standards-based index;
- **nested source preservation:** `SelectedCrossedReleaseIndex` retains the original PyPI index evidence alongside the derived trusted interval record.

Current depth:

```text
Step 4 behavior validated
+ Step 5 acquisition design introduced
+ Step 5A plan and educational source available
+ Step 5A controlled tests written
+ Step 5A implementation complete
but
Step 5A local execution not yet observed
no user-owned Step 5A technical explanation recorded
no independent implementation proof
no formal mastery assessment
not mastered
```

Product validation and learning mastery remain separate claims.

## State-maintenance rule

When route, selected responsibility, verified executable boundary, blocker, learning state, or exact continuation changes:

1. update `MEMORY.md` only for live state;
2. replace obsolete live statements instead of accumulating them;
3. change plans/specifications/ADRs only when their stable responsibility actually changes;
4. create dated working-memory only for material historical evidence or reasoning, never as another status owner;
5. keep navigation READMEs non-state-bearing.
