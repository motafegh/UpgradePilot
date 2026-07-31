# UpgradePilot Current Memory

**Last updated:** 2026-07-31 22:38 +03:30  
**Authority:** Sole repository owner of live project position, verified behavior, blockers, and exact continuation.

Stable plans, ADRs, source, tests, and dated evidence retain their own responsibilities. This file records only the current state needed to continue.

## Live position

- **Route:** B2 — Public PR vertical slice.
- **Selected parent plan:** [`plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`](plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md)
- **Completed Step 1 plan:** [`plans/B2_STEP_1_UPSTREAM_INTERVAL_AUTHORITY_PLAN.md`](plans/B2_STEP_1_UPSTREAM_INTERVAL_AUTHORITY_PLAN.md)
- **Step 1 validation:** [`working-memory/2026-07-31_2238_B2-step-1-upstream-interval-authority-validation.md`](working-memory/2026-07-31_2238_B2-step-1-upstream-interval-authority-validation.md)
- **Controlling Step 2 plan:** [`plans/B2_STEP_2_SUPPORT_DROP_CLAIM_CONTRACT_PLAN.md`](plans/B2_STEP_2_SUPPORT_DROP_CLAIM_CONTRACT_PLAN.md)
- **Step 2 implementation:** [`working-memory/2026-07-31_2238_B2-step-2-support-drop-claim-contract-implementation.md`](working-memory/2026-07-31_2238_B2-step-2-support-drop-claim-contract-implementation.md)
- **Behavior-validated Step 1 product/test revision:** `e059b09ccd53252deec2ce13b11726f30d353e3a`.
- **Latest Step 2 product/test revision:** `c023a3b09e5dc5d31e3bd0a55820b9d83a51f4db`.
- **Step 2 implementation-record revision:** `e04fc6117dc9bfec931fed9a7f1ca54c6d5d4f96`.

Later validation, implementation-record, and memory commits do not alter the product/test revisions above.

## Current phase

The dependency-version-change foundation is complete and behavior-validated.

Target Python relevance Step 1 is complete and behavior-validated:

```text
Freeze upstream interval and source authority
```

Target Python relevance Step 2 is fully implemented in source and controlled tests but remains **open and unvalidated**:

```text
Freeze the two-layer support-drop claim contract
```

Do not begin parent Step 3 `packaging` method work until the focused and complete Step 2 suites pass.

## Last behavior-validated boundary

Step 1 validation established:

```text
DependencyVersionChange
→ DependencyReleaseInterval
+ exact GitHub Release bodies
+ exact proposed-tag changelog
+ package metadata corroboration
+ trusted crossed-release index when available
→ AuthoritativeUpstreamIntervalEvidence
   or explicit UpstreamIntervalAuthorityProblem
```

Critical validated rule:

```text
proposed-version release body
+ no complete trusted release series
+ no exact proposed-tag changelog
→ interval_incomplete
```

The user reported both required Step 1 suites passed. Exact terminal counts and timings were not supplied and are not invented.

## Step 2 implemented boundary

### Pure candidate-grounding module

Created:

```text
src/upgradepilot/upstream_claim.py
```

It performs no network request and invokes no model or extraction adapter.

### Untrusted candidate result

```text
CandidateUpstreamClaimResult
├── state
├── package
├── normalized_package
├── old_version
├── proposed_version
├── candidates[]
└── detail
```

States:

```text
candidates_available
no_relevant_claim
unresolved
```

The result must echo the exact trusted dependency interval. Context drift returns `identity_mismatch`.

### Untrusted candidate claim

```text
CandidateUpstreamClaim
├── category
├── change_state
├── python_line
├── introduced_in_version
├── source_kind
├── source_release_version
├── source_quote
├── quote_start
└── quote_end
```

Candidate fields remain untrusted even when structurally valid.

### Admitted semantic identity

Only:

```text
category = support_boundary_change
change_state = support_dropped
python_line = canonical X.Y
```

Canonical Python-line text contains exactly two non-negative decimal components with no leading zero except `0`, no patch component, wildcard, comparator, prerelease, epoch, local version, or prose.

### Groundable sources

```text
github_release_body
tagged_changelog
```

Not admitted to ground prose claims:

```text
package metadata
Dependabot copied text
arbitrary documentation
model-selected text
unknown source kinds
```

Release-body candidates must identify and resolve one exact matching `IntervalGitHubReleaseSource`.

Tagged-changelog candidates must resolve the one exact `TaggedChangelogEvidence` already trusted by Step 1.

### Trusted interval membership

Available candidates require one trusted:

```text
CrossedReleaseIndexEvidence
```

The exact `introduced_in_version` must be a member of its `ordered_versions` tuple.

```text
exact tagged changelog
+ no trusted crossed-release index
→ release_interval_unresolved
```

Step 2 does not parse or order versions.

### Exact quote grounding

The validator proves:

```text
0 <= quote_start < quote_end <= len(exact_source_text)
exact_source_text[quote_start:quote_end] == source_quote
```

It performs no whitespace, punctuation, capitalization, Unicode, or line-ending normalization.

The normalized `python_line` must also occur inside the exact quote as a standalone major/minor token. A quote about `3.8` cannot ground a candidate claiming `3.9`, and `3.8` inside `3.8.1` is not accepted as the same line token.

### Trusted output

```text
GroundedPythonSupportDropClaim
├── category = support_boundary_change
├── change_state = support_dropped
├── python_line
├── introduced_in_version
├── interval
└── source_evidence[]
```

Each exact source record is:

```text
GroundedUpstreamClaimSource
├── source_kind
├── introduced_in_version
├── exact Step 1 source object
├── exact quote
├── quote_start
└── quote_end
```

Equivalent candidates for the same Python line and introduced release combine exact evidence. Duplicate exact records are deduplicated.

Different Python lines or different introduced releases return:

```text
multiple_support_drop_claims
```

One invalid candidate blocks partial success from another candidate in the same result.

### Problem states

```text
no_support_drop_claim
candidate_unresolved
identity_mismatch
malformed_candidate
unsupported_claim_category
unsupported_change_state
invalid_python_line
source_not_admitted
source_identity_unresolved
source_quote_not_grounded
release_interval_unresolved
claim_outside_interval
multiple_support_drop_claims
```

### Semantic honesty boundary

Deterministic grounding proves identity, source, interval, quote/span, normalized Python-line correspondence, allowed field values, and single-claim aggregation.

It does not independently reinterpret arbitrary prose to prove that every sentence semantically means support was dropped. Later bounded extraction evaluation owns semantic reliability. Exact source quotation and provenance keep that judgment auditable and prevent detached model assertions.

## Controlled tests

Added:

```text
tests/test_upstream_claim.py: 15 tests
tests/test_upstream_claim_edges.py: 8 tests
```

Updated:

```text
tests/test_package_interface.py: 1 new Step 2 test
```

Expected focused total:

```text
24 tests
```

Expected complete deterministic total:

```text
200 tests
```

These are derived counts, not observed passing results.

## Validation status

No Step 2 test pass is claimed.

The GitHub connector exposes no repository test runner and reported no combined status for `c023a3b09e5dc5d31e3bd0a55820b9d83a51f4db`.

No S001 or S004 repetition is required because Step 2 changes no active CLI, acquisition, dependency, CI, package, upstream resolver, or target-Python path.

## Exact continuation

Run from the real checkout:

```bash
git switch main
git pull --ff-only

python -m unittest \
  tests.test_upstream_claim \
  tests.test_upstream_claim_edges \
  tests.test_package_interface \
  -v

python -m unittest discover -s tests -v
```

Expected:

```text
focused: Ran 24 tests / OK
complete: Ran 200 tests / OK
```

After both pass:

1. create the dated Step 2 validation record;
2. close Step 2;
3. activate parent Step 3 — record and freeze the `packaging` method;
4. do not begin model integration, upstream acquisition, target comparison, or CLI orchestration during closure.

## Explicitly not established

- a model or Instructor adapter;
- prompt, retry, or model-selection behavior;
- PEP 440 release validity or ordering;
- complete release-index network acquisition;
- exact tag peeling or changelog-file acquisition;
- semantic extraction reliability across varied prose;
- target Python line overlap comparison;
- conditional target-Python activation;
- S001 `outside_declared_python_range` result;
- compatibility, safety, recommendation, maintainer action, or production readiness;
- user mastery.

## Learning state

Step 1 concepts are behavior-validated. Step 2 concepts are introduced and implemented:

- candidate schema versus trusted domain evidence;
- deterministic echoed-context validation;
- source resolution rather than candidate-provided authority;
- exact quote/span grounding;
- normalized fields versus unchanged source text;
- quote-to-Python-line correspondence;
- trusted crossed-release membership;
- equivalent evidence aggregation;
- invalid-candidate and ambiguity precedence;
- auditable grounding versus semantic-extraction reliability.

Current depth:

```text
structured explanations completed
+ focused plans created
+ tests written before implementation
+ Step 1 suites reported passing
+ Step 2 implementation completed
+ review-found quote-to-line drift corrected
but
Step 2 repository execution not yet observed
no user-owned technical explanation recorded
no independent implementation practice recorded
no formal assessment recorded
not mastered
```

Product behavior validation and learning mastery remain separate claims.

## State-maintenance rule

When route, selected plan, verified behavior, blocker, learning state, or exact continuation changes, update this file only. Change another file only when its stable responsibility or dated evidence changes.
