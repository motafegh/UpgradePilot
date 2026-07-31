# UpgradePilot Current Memory

**Last updated:** 2026-07-31 22:07 +03:30  
**Authority:** Sole repository owner of live project position, verified behavior, blockers, and exact continuation.

Stable plans, ADRs, source, tests, and dated evidence retain their own responsibilities. This file records only the current state needed to continue.

## Live position

- **Route:** B2 — Public PR vertical slice.
- **Selected parent plan:** [`plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`](plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md)
- **Controlling Step 1 plan:** [`plans/B2_STEP_1_UPSTREAM_INTERVAL_AUTHORITY_PLAN.md`](plans/B2_STEP_1_UPSTREAM_INTERVAL_AUTHORITY_PLAN.md)
- **Completed prerequisite:** [`plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md`](plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md)
- **Final prerequisite validation:** [`working-memory/2026-07-31_2157_B2-step-8-multi-format-command-integration-validation.md`](working-memory/2026-07-31_2157_B2-step-8-multi-format-command-integration-validation.md)
- **Step 1 implementation record:** [`working-memory/2026-07-31_2207_B2-step-1-upstream-interval-authority-implementation.md`](working-memory/2026-07-31_2207_B2-step-1-upstream-interval-authority-implementation.md)
- **Latest Step 1 product/test revision:** `e059b09ccd53252deec2ce13b11726f30d353e3a`.
- **Step 1 implementation-record revision:** `192aa2bf6acfe998960baa774f0b3c3231f1edb3`.

Later implementation-record and memory commits do not alter the Step 1 product/test revision.

## Current phase

The dependency-version-change foundation is complete and behavior-validated.

The target Python support relevance plan is active.

Step 1 is fully implemented in source and controlled tests but remains **open and unvalidated**:

```text
Freeze upstream interval and source authority
```

Do not begin Step 2 support-drop claim contracts until the focused and complete Step 1 suites pass.

## Last behavior-validated product boundary

Validated dependency foundation:

```text
requirements / constraints / uv.lock
→ one canonical DependencyVersionChange
   or explicit evidence problem
```

Observed public controls:

```text
S001
soupsieve 2.6 → 2.8.4
uv.lock exact base/head provenance
CI dependency exercise unresolved without inferred lockfile consumption

S004
pytest 9.0.2 → 9.0.3
requirements-dev.txt
CI dependency exercise proven
```

Those public commands do not need repetition during Step 1 because Step 1 changes no active CLI or acquisition module.

## Step 1 implemented boundary

### Pure authority module

Created:

```text
src/upgradepilot/upstream_interval.py
```

It performs no network requests and does not interpret release prose.

### Interval identity

```text
DependencyVersionChange
→ DependencyReleaseInterval
   ├── exact raw old_version
   ├── exact raw proposed_version
   ├── lower bound exclusive
   └── upper bound inclusive
```

No PEP 440 validity or ordering is claimed yet.

### Trusted crossed-release index

```text
CrossedReleaseIndexEvidence
├── repository
├── interval
├── ordered_versions[]
├── source_url
└── retrieved_at
```

Step 1 validates only structural invariants:

- non-empty unique values;
- old version absent;
- proposed version final;
- repository and interval agreement;
- source identity preserved.

A later acquisition/version step must earn this trusted record.

### Admitted source roles

```text
exact GitHub Release body
→ exact release authority
→ interval authority only when every indexed release has a usable body

exact proposed-tag changelog
→ interval-wide authority

exact package metadata
→ corroboration only

Dependabot copied notes
arbitrary documentation
model-selected text
unknown source kind
→ unsupported authority
```

### Exact tagged changelog provenance

```text
TaggedChangelogEvidence
├── repository and interval
├── requested tag and tag ref
├── tag object type and SHA
├── resolved commit SHA
├── requested and returned path
├── blob SHA
├── reported and decoded bytes
├── exact text
└── retrieval time
```

A lightweight tag must resolve directly to its tag-object commit. An annotated tag preserves its tag object and resolved commit separately.

### Aggregate authority

Successful result:

```text
AuthoritativeUpstreamIntervalEvidence
```

Authority bases:

```text
complete_release_series
tagged_changelog
complete_release_series_and_tagged_changelog
```

Problem result:

```text
UpstreamIntervalAuthorityProblem
```

States:

```text
no_interval_authority
interval_incomplete
identity_mismatch
ambiguous_source
conflicting_source_identity
malformed_source
unsupported_source_authority
```

### Critical coverage rule

```text
proposed-version release body
+ no trusted complete crossed-release index
+ no exact tagged changelog
→ interval_incomplete
```

A final release body cannot hide a change introduced in an intermediate release.

### Source-problem severity

```text
source_unavailable or acquisition_failed
+ independent complete authority path
→ preserve and continue

identity_mismatch or malformed_source
→ stop aggregate authority
```

## S001 oracle boundary

The completed simulation preserves a bounded Soup Sieve changelog capture at tag `2.8.4` containing sections for:

```text
2.7
2.8
2.8.2
2.8.3
2.8.4
```

The Python 3.8 support drop appears in the intermediate `2.8` section.

The simulation does not preserve the production-required upstream changelog path, resolved tag commit, or blob SHA. Product logic contains no S001 repository, package, versions, wording, path, tag, blob, or expected answer.

## Controlled tests

Added:

```text
tests/test_upstream_interval.py: 17 tests
tests/test_upstream_interval_authority_edges.py: 5 tests
```

Updated:

```text
tests/test_package_interface.py: 1 new Step 1 test
```

Expected focused invocation:

```text
25 tests
```

Expected complete suite:

```text
176 tests
```

These are derived counts, not observed passing results.

## Validation status

No Step 1 test pass is claimed.

The GitHub connector exposes no repository test runner and reported no combined status for `e059b09ccd53252deec2ce13b11726f30d353e3a`.

The available container could not resolve `github.com`, so it could not clone and run the repository independently.

## Exact continuation

Run from the real checkout:

```bash
git switch main
git pull --ff-only

python -m unittest \
  tests.test_upstream_interval \
  tests.test_upstream_interval_authority_edges \
  tests.test_package_interface \
  -v

python -m unittest discover -s tests -v
```

Expected:

```text
focused: Ran 25 tests / OK
complete: Ran 176 tests / OK
```

After both pass:

1. create the dated Step 1 validation record;
2. close Step 1;
3. activate parent Step 2 — freeze the two-layer support-drop claim contract;
4. do not begin PEP 440 ordering, network acquisition, LLM integration, target comparison, or CLI reordering during closure.

## Explicitly not established

- PEP 440 release validity or ordering;
- complete GitHub release/tag index acquisition;
- tag peeling network acquisition;
- exact tagged-changelog file acquisition;
- changelog-path discovery;
- candidate or grounded support-drop claims;
- semantic quote validation;
- LLM or Instructor integration;
- target Python range comparison;
- conditional target acquisition;
- S001 `outside_declared_python_range` result;
- compatibility, safety, recommendation, maintainer action, or production readiness;
- user mastery.

## Learning state

Step 1 concepts introduced and implemented:

- exact interval identity versus version ordering;
- exact release authority versus interval coverage;
- complete release series versus tagged changelog authority;
- corroboration versus authority;
- lightweight versus annotated tag identity;
- resolved commit and blob provenance;
- severe evidence contradictions versus recoverable source unavailability;
- semantic claim extraction as a later responsibility.

Current depth:

```text
structured explanation completed
+ focused plan created
+ tests written before source
+ source implementation reviewed
+ review-found edge cases added and corrected
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
