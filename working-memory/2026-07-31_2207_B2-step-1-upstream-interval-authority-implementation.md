# B2 Target Python Relevance Step 1 — Upstream interval authority implementation

**Recorded:** 2026-07-31 22:07 +03:30  
**Route:** B2 — Public PR vertical slice  
**Selected plan:** [`../plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`](../plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md)  
**Focused Step 1 plan:** [`../plans/B2_STEP_1_UPSTREAM_INTERVAL_AUTHORITY_PLAN.md`](../plans/B2_STEP_1_UPSTREAM_INTERVAL_AUTHORITY_PLAN.md)  
**Status:** Implemented; deterministic repository validation required

## Previous validated boundary

The dependency-version-change evidence foundation is complete and behavior-validated.

Validated canonical input:

```text
DependencyVersionChange
├── package
├── normalized_package
├── old_version
├── proposed_version
├── source_evidence[]
└── limitations[]
```

S001 now establishes:

```text
soupsieve 2.6 → 2.8.4
```

through the installed multi-format command.

## Latest Step 1 product/test revision

```text
e059b09ccd53252deec2ce13b11726f30d353e3a
Harden upstream authority identity validation
```

The GitHub connector reported no combined commit statuses for this revision. No test pass is claimed in this record.

## Commits

Plan:

```text
b503e90d0c4dbc4686a43a09aa361a5dc8d6f304
Finalize Step 1 upstream interval authority plan
```

Tests first:

```text
cf1a374adfedb0390a5379e35f7e7b73e003129c
Test upstream interval authority contracts

f7220636c31d4e172c98b197459add89492b8360
Test upstream interval package exports
```

Initial implementation:

```text
9135cc39e9d43d1f12ac62795d044625072e6595
Add upstream interval authority contracts

fdbf7403d69fd0460c13b775e6757fc169f2ed58
Export upstream interval authority contracts
```

Review-found edge tests and correction:

```text
29c8ff65ff9fba5c1a882dbb506facc3ea046758
Test upstream authority identity edges

e059b09ccd53252deec2ce13b11726f30d353e3a
Harden upstream authority identity validation
```

## Added module

```text
src/upgradepilot/upstream_interval.py
```

This is a pure domain module. It performs no network request and does not parse or interpret release prose.

## Interval identity

Created:

```text
DependencyReleaseInterval
├── package
├── normalized_package
├── old_version
├── proposed_version
├── lower_bound_inclusive = false
└── upper_bound_inclusive = true
```

Created conversion:

```text
release_interval_from_dependency_change
```

The record preserves exact raw version strings. It does not establish PEP 440 validity or forward ordering.

## Source kinds and authority roles

Frozen order:

```text
UPSTREAM_SOURCE_AUTHORITY_ORDER = (
    github_release_body,
    tagged_changelog,
    package_metadata,
)
```

Frozen roles:

```text
github_release_body
→ release_authority

tagged_changelog
→ interval_authority

package_metadata
→ corroboration

dependabot_release_note_copy
arbitrary_documentation
model_selected_text
unknown source kind
→ unsupported
```

Copied or model-selected text cannot enter the trusted authority bundle.

## Complete crossed-release index contract

Created:

```text
CrossedReleaseIndexEvidence
├── repository
├── interval
├── ordered_versions[]
├── source_url
└── retrieved_at
```

Structural invariants enforced now:

- non-empty tuple;
- non-empty unique raw versions;
- old version excluded;
- proposed version final;
- repository and interval agreement;
- source identity preserved.

Standards-based version validity and ordering remain deferred to the parent plan's Step 3.

## GitHub Release authority

Created:

```text
IntervalGitHubReleaseSource
├── release_version
└── release: GitHubReleaseEvidence
```

Enforced:

- repository agreement;
- release version inside the trusted crossed-release index when supplied;
- requested tag equals the release version or `v` plus the release version;
- exact tag-reference agreement;
- supported tag-object identity;
- positive release identity;
- non-empty release body for usable prose authority;
- one non-conflicting exact record per release version.

A bodyless exact release becomes a preserved `source_unavailable` problem. It does not become empty evidence.

## Tagged changelog authority

Created:

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

Enforced:

- proposed-version tag form;
- exact tag-reference agreement;
- supported `commit` or `tag` object;
- non-empty tag and resolved-commit identities;
- a lightweight tag resolves to its direct commit;
- normalized repository-relative path;
- requested and returned path equality;
- non-empty blob identity;
- non-negative integer byte counts;
- reported/decoded/content-byte agreement;
- non-empty text;
- exactly one distinct tagged changelog identity.

Annotated tags preserve both tag-object SHA and resolved commit SHA for later tag peeling and exact-file acquisition.

## Package metadata corroboration

Created:

```text
PackageMetadataCorroboration
├── package
├── normalized_package
├── release_version
├── source_url
├── requires_python: str | None
└── retrieved_at
```

Package identity is compared through normalized distribution identity.

Metadata must belong to:

```text
old version
or
one release in the trusted crossed interval
```

It can corroborate resulting Python requirements but cannot establish interval prose authority.

## Source-level problem contract

Created:

```text
UpstreamAuthoritySourceProblem
├── source_kind
├── state
├── detail
├── release_version: str | None
└── path: str | None
```

States:

```text
source_unavailable
malformed_source
identity_mismatch
acquisition_failed
```

Rules:

```text
source_unavailable or acquisition_failed
+ independent complete authority path
→ preserve problem and continue

malformed_source or identity_mismatch
→ stop aggregate authority
```

A source problem referring to a release outside the bounded interval also stops as `identity_mismatch`.

## Aggregate result

Successful type:

```text
AuthoritativeUpstreamIntervalEvidence
├── interval
├── repository
├── crossed_releases
├── release_bodies[]
├── tagged_changelog
├── package_metadata[]
├── source_problems[]
└── authority_basis
```

Authority bases:

```text
complete_release_series
tagged_changelog
complete_release_series_and_tagged_changelog
```

Problem type:

```text
UpstreamIntervalAuthorityProblem
```

Aggregate problem states:

```text
no_interval_authority
interval_incomplete
identity_mismatch
ambiguous_source
conflicting_source_identity
malformed_source
unsupported_source_authority
```

## Coverage rules implemented

### Proposed release body alone

```text
proposed body
+ no trusted complete release index
+ no tagged changelog
→ interval_incomplete
```

### Complete release series

```text
trusted crossed-release index
+ usable exact body for every indexed release
→ complete_release_series
```

### Missing intermediate release

```text
2.7 body
+ missing 2.8 body
+ 2.8.4 body
+ no tagged changelog
→ interval_incomplete
```

The proposed release body cannot hide the intermediate gap.

### Tagged changelog

```text
exact proposed-tag changelog
→ tagged_changelog interval authority
```

This establishes source authority only. Later claim extraction must ground exact version sections and quotations.

### Independent coverage

```text
partial release bodies
+ exact tagged changelog
→ tagged_changelog authority
→ preserve exact bodies and source problems
```

### Combined complete sources

```text
complete exact release series
+ exact tagged changelog
→ preserve both
→ complete_release_series_and_tagged_changelog
```

### Metadata only

```text
package metadata only
→ no_interval_authority
```

## S001 oracle boundary

The completed product simulation preserves a bounded Soup Sieve changelog capture at tag `2.8.4` with sections:

```text
2.7
2.8
2.8.2
2.8.3
2.8.4
```

The support change appears in the intermediate `2.8` section.

The simulation does not preserve the production-required changelog path, resolved tag commit, or blob SHA. No S001 repository, package, versions, wording, path, tag, blob, or expected relevance result was added to product logic.

## Tests

Added:

```text
tests/test_upstream_interval.py: 17 tests
tests/test_upstream_interval_authority_edges.py: 5 tests
```

Updated:

```text
tests/test_package_interface.py: 1 new Step 1 export test
```

Focused Step 1 invocation includes:

```text
17 + 5 + 3 package-interface tests = 25 tests
```

Previously validated complete suite:

```text
153 tests
```

Net new tests:

```text
17 + 5 + 1 = 23
```

Expected complete suite:

```text
176 tests
```

These counts are derived from committed test methods. They are not observed results.

## Files changed

Added:

```text
plans/B2_STEP_1_UPSTREAM_INTERVAL_AUTHORITY_PLAN.md
src/upgradepilot/upstream_interval.py
tests/test_upstream_interval.py
tests/test_upstream_interval_authority_edges.py
working-memory/2026-07-31_2207_B2-step-1-upstream-interval-authority-implementation.md
```

Modified:

```text
src/upgradepilot/__init__.py
tests/test_package_interface.py
MEMORY.md
```

No existing runtime orchestration or acquisition module changed.

## Explicitly not implemented

Step 1 does not implement:

- PEP 440 version validation or ordering;
- GitHub release/tag enumeration;
- tag peeling network acquisition;
- exact tagged-file network acquisition;
- changelog-path discovery;
- semantic claim extraction;
- candidate or grounded support-drop contracts;
- LLM, Instructor, or model integration;
- target Python relevance comparison;
- conditional CLI activation;
- compatibility, safety, recommendation, or maintainer action.

## Validation commands

Run from the real checkout:

```bash
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

## Stop line

Step 1 remains open until both deterministic gates pass.

Do not begin parent Step 2 support-drop claim contracts before the focused and complete suites are observed and recorded.
