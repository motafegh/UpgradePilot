# B2 Target Python Relevance Step 1 — Upstream interval authority validation

**Recorded:** 2026-07-31 22:38 +03:30  
**Route:** B2 — Public PR vertical slice  
**Selected plan:** [`../plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`](../plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md)  
**Focused Step 1 plan:** [`../plans/B2_STEP_1_UPSTREAM_INTERVAL_AUTHORITY_PLAN.md`](../plans/B2_STEP_1_UPSTREAM_INTERVAL_AUTHORITY_PLAN.md)  
**Status:** Complete and behavior-validated

## Validated product/test revision

```text
e059b09ccd53252deec2ce13b11726f30d353e3a
```

Later implementation-record, validation-record, and memory commits do not alter that product/test revision.

## Deterministic validation

The user reported that all required Step 1 tests passed:

```text
focused Step 1 suite: passed
complete deterministic suite: passed
```

The focused invocation covered:

```text
tests.test_upstream_interval
tests.test_upstream_interval_authority_edges
tests.test_package_interface
```

The exact terminal summary lines and elapsed times were not supplied in the validation message, so this record does not invent them.

## Behavior-validated Step 1 boundary

Validated contracts:

```text
DependencyVersionChange
→ DependencyReleaseInterval
   ├── old version exclusive
   └── proposed version inclusive
```

Validated interval source roles:

```text
exact GitHub Release body
→ exact-release authority
→ interval authority only with a complete trusted release series

exact proposed-tag changelog
→ interval-wide authority

exact package metadata
→ corroboration only

Dependabot copied notes, arbitrary documentation, model-selected text, and unknown sources
→ unsupported authority
```

Validated exact source records:

```text
CrossedReleaseIndexEvidence
IntervalGitHubReleaseSource
TaggedChangelogEvidence
PackageMetadataCorroboration
UpstreamAuthoritySourceProblem
```

Validated aggregate result:

```text
AuthoritativeUpstreamIntervalEvidence
or
UpstreamIntervalAuthorityProblem
```

Validated authority bases:

```text
complete_release_series
tagged_changelog
complete_release_series_and_tagged_changelog
```

Validated stopping states:

```text
no_interval_authority
interval_incomplete
identity_mismatch
ambiguous_source
conflicting_source_identity
malformed_source
unsupported_source_authority
```

## Critical interval protection

Behavior-validated:

```text
proposed-version release body
+ no trusted complete crossed-release index
+ no exact proposed-tag changelog
→ interval_incomplete
```

A final release body cannot silently hide a material change introduced in an intermediate crossed release.

## Provenance protection

Behavior-validated for tagged changelog evidence:

- proposed-version tag form;
- exact tag-reference identity;
- lightweight-tag direct commit agreement;
- annotated-tag object and resolved-commit separation;
- requested/returned path equality;
- exact blob identity;
- reported/decoded/actual UTF-8 byte agreement;
- non-empty exact source text;
- rejection of ambiguous distinct changelog identities.

Behavior-validated for GitHub Release evidence:

- repository identity agreement;
- release version belongs to the trusted interval index when present;
- requested tag identifies the declared release version;
- exact tag-reference agreement;
- supported tag-object identity;
- positive release identity;
- bodyless releases preserved as source-unavailable rather than empty authority;
- conflicting exact records rejected.

## Source-problem severity

Behavior-validated:

```text
source_unavailable or acquisition_failed
+ independent complete interval authority
→ preserve the problem and continue

identity_mismatch or malformed_source
→ stop aggregate authority
```

A valid alternative source cannot hide contradictory or malformed recognized evidence.

## Scope preserved

Step 1 remains a pure authority layer.

It does not:

- perform network acquisition;
- parse PEP 440 versions;
- extract semantic support-drop claims;
- use an LLM or Instructor;
- compare target Python declarations;
- reorder CLI orchestration;
- make compatibility, safety, merge, or recommendation claims.

No active CLI or acquisition path changed during Step 1, so S001 and S004 did not require repetition.

## Step 1 stop-line result

Step 1 is complete and behavior-validated.

The next authorized responsibility is:

```text
Step 2 — Freeze the two-layer support-drop claim contract
```

Step 2 must separate:

```text
untrusted CandidateUpstreamClaimResult
from
deterministically grounded GroundedPythonSupportDropClaim
```

It must validate exact authority identity, exact quote/span grounding, allowed category and direction, normalized Python line, and trusted crossed-interval membership. It must not add a model adapter, PEP 440 runtime dependency, network acquisition, target comparison, or CLI integration.

## Learning state

Concepts introduced, implemented, and behavior-validated:

- release identity versus release ordering;
- exact-release authority versus interval authority;
- complete release series versus proposed-tag changelog;
- corroboration versus authority;
- lightweight and annotated Git tag identity;
- immutable commit, path, blob, byte, and text provenance;
- recoverable source unavailability versus severe evidence contradiction.

Current depth:

```text
structured explanation completed
+ focused plan created
+ tests written before implementation
+ implementation and review-found edge cases completed
+ focused and complete suites reported passing
but
no user-owned technical explanation recorded
no independent implementation practice recorded
no formal assessment recorded
not mastered
```

Product behavior validation and learning mastery remain separate claims.
