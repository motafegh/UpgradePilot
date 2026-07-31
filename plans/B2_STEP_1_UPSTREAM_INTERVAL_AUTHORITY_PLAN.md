# B2 Step 1 — Upstream Interval and Source Authority Plan

**Status:** Approved and controlling for Step 1  
**Route:** B2 — Public PR vertical slice  
**Parent plan:** [`B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`](B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md)  
**Prerequisite:** The dependency-version-change evidence foundation is complete and behavior-validated  
**Selected proof case:** S001 — `soupsieve` `2.6 → 2.8.4`

## Purpose

Freeze the domain contracts that determine which upstream texts may become bounded evidence for the complete dependency-release interval:

```text
old_version < relevant release <= proposed_version
```

This step establishes interval identity, admitted authority kinds, interval-coverage requirements, provenance, identity conflict handling, and explicit authority problems.

It does **not** extract a Python support-drop claim, add a model or Instructor, parse PEP 440, compare target Python ranges, reorder the CLI, or decide compatibility, safety, or maintainer action.

## Why a focused Step 1 plan is required

The parent plan correctly requires exact GitHub Release bodies, an exact proposed-tag changelog, package metadata corroboration, and an old-exclusive/proposed-inclusive interval. It does not yet freeze:

- the trusted interval and source records;
- the difference between one release body and interval-capable authority;
- how a complete release series is represented;
- what happens when an intermediate release body is missing;
- how tagged changelog provenance is represented for lightweight and annotated tags;
- how exact path, returned path, resolved commit, blob, and byte evidence are reconciled;
- how unavailable sources interact with an alternative complete authority path;
- which identity conflicts stop the bundle;
- how copied Dependabot notes, arbitrary documentation, or model-selected text are explicitly rejected;
- what is intentionally deferred to later semantic-claim validation.

Without those decisions, a proposed-version release body could accidentally hide a material change introduced in an intermediate release.

## Controlling distinction

```text
exact source identity
≠
interval coverage
≠
semantic claim
≠
target relevance
```

Step 1 owns the first two responsibilities only.

## Interval identity

Create one representation-neutral interval record from the trusted canonical dependency change:

```text
DependencyReleaseInterval
├── package
├── normalized_package
├── old_version
├── proposed_version
├── lower_bound_inclusive = false
└── upper_bound_inclusive = true
```

The record preserves exact raw version strings.

Step 1 does not decide whether the strings are valid PEP 440 versions or whether the proposed value is greater. The accepted `packaging` method and version-order failure states belong to Step 3 of the parent plan.

## Complete crossed-release index

Define a trusted input contract for the complete ordered release set inside the interval:

```text
CrossedReleaseIndexEvidence
├── repository
├── interval
├── ordered_versions[]
├── source_url
└── retrieved_at
```

Its semantic meaning is:

```text
all admitted releases after old_version
and no later than proposed_version
in deterministic standards-based order
```

Step 1 validates structural invariants that do not require a version parser:

- the list is non-empty;
- values are non-empty and unique;
- `old_version` is absent;
- `proposed_version` is the final value;
- repository and interval identity agree.

The future acquisition and Step 3 version method must earn this trusted record. Product code must not construct it from a title, copied notes, alphabetical ordering, or model choice.

## Admitted source kinds and roles

Freeze this order and role table:

| Source kind | Role | Can establish interval authority? |
|---|---|---|
| exact GitHub Release body | exact release authority | yes, only as a complete series covering every indexed release |
| exact proposed-tag changelog | interval-wide authority | yes |
| exact package metadata | corroboration | no |
| Dependabot release-note copy | locator/copied text only | no |
| arbitrary documentation | unsupported | no |
| model-selected text | unsupported | no |

The source-role mapping must be deterministic and testable.

## Exact GitHub Release body record

Reuse the validated `GitHubReleaseEvidence` contract and wrap it with the exact release version it represents:

```text
IntervalGitHubReleaseSource
├── release_version
└── release: GitHubReleaseEvidence
```

A usable release-body source requires:

- repository identity agreement;
- a non-empty exact body;
- exact requested tag and tag reference agreement already established by `GitHubReleaseEvidence`;
- supported tag object identity;
- release version inside the trusted crossed-release index when that index is supplied.

A release with no usable body remains exact release identity, but it cannot satisfy interval prose coverage. Preserve that state as a source problem rather than treating empty prose as evidence.

## Exact tagged changelog record

Define one exact file record at the proposed tag:

```text
TaggedChangelogEvidence
├── repository
├── interval
├── requested_tag
├── tag_ref
├── tag_object_type
├── tag_object_sha
├── resolved_commit_sha
├── path
├── returned_path
├── blob_sha
├── reported_byte_count
├── decoded_byte_count
├── content
└── retrieved_at
```

Why both tag object and resolved commit are required:

```text
lightweight tag
→ tag ref points directly to commit

annotated tag
→ tag ref points to tag object
→ tag object must be peeled to an exact commit
```

The changelog file must then be acquired at that exact resolved commit.

Admission requires:

- repository and interval agreement;
- accepted proposed-version tag form;
- exact tag-ref agreement;
- tag object type `commit` or `tag`;
- non-empty tag object SHA and resolved commit SHA;
- normalized repository-relative path;
- requested and returned path equality;
- non-empty blob SHA;
- non-negative integer byte counts;
- reported and decoded byte agreement;
- non-empty UTF-8 text.

Step 1 defines this record. Exact tag peeling and file acquisition belong to later upstream interval acquisition.

## Package metadata corroboration

Define a bounded corroboration record:

```text
PackageMetadataCorroboration
├── package
├── normalized_package
├── release_version
├── source_url
├── requires_python: str | None
└── retrieved_at
```

Package metadata may corroborate resulting Python requirements. It cannot establish what the changelog said, which intermediate release introduced a change, or complete interval coverage.

## Source problems

Preserve recognized acquisition or source failures:

```text
UpstreamAuthoritySourceProblem
├── source_kind
├── state
├── detail
├── release_version: str | None
└── path: str | None
```

Initial source-problem states:

```text
source_unavailable
malformed_source
identity_mismatch
acquisition_failed
```

A source problem may coexist with accepted authority when an independent complete authority path remains available. Example:

```text
one intermediate GitHub Release body unavailable
+
exact proposed-tag changelog available
→ accept tagged-changelog interval authority
→ preserve release-body source problem
```

## Aggregate authority result

Successful result:

```text
AuthoritativeUpstreamIntervalEvidence
├── interval
├── repository
├── crossed_releases: CrossedReleaseIndexEvidence | None
├── release_bodies[]
├── tagged_changelog: TaggedChangelogEvidence | None
├── package_metadata[]
├── source_problems[]
└── authority_basis
```

Authority basis:

```text
complete_release_series
tagged_changelog
complete_release_series_and_tagged_changelog
```

Problem result:

```text
UpstreamIntervalAuthorityProblem
├── state
├── interval
├── repository
├── detail
└── source_problems[]
```

Initial aggregate problem states:

```text
no_interval_authority
interval_incomplete
identity_mismatch
ambiguous_source
conflicting_source_identity
malformed_source
unsupported_source_authority
```

## Deterministic assembly rules

### Rule 1 — Proposed release body alone is not enough by default

```text
proposed-version release body
+ no complete crossed-release index
+ no tagged changelog
→ interval_incomplete
```

The absence of an index means the system has not established that no intermediate release exists.

### Rule 2 — Complete release series can establish authority

```text
trusted crossed-release index
+ exactly one usable exact GitHub Release body for every indexed version
→ complete_release_series
```

Missing an intermediate body produces `interval_incomplete` unless an exact tagged changelog provides independent interval coverage.

### Rule 3 — Tagged changelog can establish interval authority

```text
exact proposed-tag changelog with full immutable provenance
→ tagged_changelog
```

Step 1 does not claim that every section is semantically relevant. Later extraction and deterministic validation must establish exact quote, version section, and interval relevance.

### Rule 4 — Preserve both complete authorities

```text
complete release series
+ exact tagged changelog
→ complete_release_series_and_tagged_changelog
```

Do not discard one source or silently overwrite text from the other.

### Rule 5 — Package metadata never upgrades itself

```text
package metadata only
→ no_interval_authority
```

### Rule 6 — Identity conflicts stop

Stop on:

- repository mismatch;
- interval mismatch;
- release version outside the supplied crossed-release index;
- conflicting exact release records for the same release version;
- more than one distinct tagged changelog record;
- tag/path/blob/byte inconsistency;
- package metadata identity outside the bounded interval.

### Rule 7 — Semantic prose conflict is deferred

Step 1 does not compare the meaning of release-body and changelog prose. It preserves exact texts and identities.

A later Step 2 claim validator owns:

- exact quote grounding;
- support-drop category and direction;
- normalized Python line;
- release-section identity;
- interval relevance;
- conflicting grounded claims.

Do not label two exact source texts semantically conflicting before claim extraction establishes comparable claims.

## S001 design oracle

The completed simulation preserves a bounded changelog capture at Soup Sieve tag `2.8.4` containing sections:

```text
2.7
2.8
2.8.2
2.8.3
2.8.4
```

The Python support change appears in the intermediate section:

```text
2.8
Drop Python 3.8 support.
```

The simulation capture is an oracle only. It does not preserve the production-required upstream changelog path, resolved tag commit, or blob SHA. Later acquisition must reacquire those identities from `facelessuser/soupsieve`.

## Test-first proof obligations

Before source implementation, controlled tests must prove:

1. canonical dependency identity becomes an old-exclusive/proposed-inclusive interval;
2. exact raw versions are preserved;
3. source-role order is fixed;
4. copied Dependabot notes, arbitrary docs, and model-selected text are unsupported authority;
5. proposed release body without complete interval proof is rejected;
6. a one-release complete index plus its exact body is accepted;
7. a multi-release complete index requires every release body;
8. a missing intermediate release body cannot be hidden by the proposed body;
9. an exact tagged changelog independently establishes interval authority;
10. partial release bodies plus a tagged changelog remain accepted with both evidence and problems preserved;
11. package metadata alone cannot establish authority;
12. complete release series and changelog are both preserved;
13. conflicting duplicate release identity stops;
14. distinct tagged changelog identities are ambiguous;
15. repository and interval mismatch stop;
16. tag/path/blob/byte inconsistency is malformed;
17. crossed-release index excludes old, includes proposed last, and is unique;
18. package corroboration remains bounded to the old/crossed release set;
19. no product logic contains S001 repository, package, versions, wording, tag, path, blob, or expected answer;
20. the complete existing test suite remains green.

## Modification surface

Expected additions:

```text
src/upgradepilot/upstream_interval.py
tests/test_upstream_interval.py
```

Expected updates:

```text
src/upgradepilot/__init__.py
tests/test_package_interface.py
MEMORY.md
```

Do not modify during Step 1:

```text
src/upgradepilot/cli.py
src/upgradepilot/target_python.py
src/upgradepilot/upstream_source.py
src/upgradepilot/github_release.py
src/upgradepilot/github_repository.py
pyproject.toml
```

Those modules remain inputs or later acquisition/integration surfaces.

## Build order

1. commit this focused plan;
2. commit controlled interval/source-authority tests;
3. implement the pure domain contracts and deterministic assembly;
4. export the intended package-level contracts;
5. run focused and complete deterministic suites;
6. record behavior validation and activate parent Step 2 only after tests pass.

## Stop line

Step 1 is complete when the repository behavior-validly provides:

```text
trusted DependencyVersionChange
→ exact raw old-exclusive/proposed-inclusive interval
+ admitted exact upstream source records
→ authoritative interval bundle
   or explicit authority problem
```

Do not proceed during Step 1 into:

- PEP 440 parsing or ordering;
- release/tag listing acquisition;
- tag peeling or tagged-file network acquisition;
- support-drop claim extraction;
- LLM or Instructor integration;
- target Python comparison;
- conditional CLI orchestration;
- compatibility, safety, recommendation, or maintainer action.
