# B2 Target Python Relevance Step 2 — Support-drop claim contract implementation

**Recorded:** 2026-07-31 22:38 +03:30  
**Route:** B2 — Public PR vertical slice  
**Selected plan:** [`../plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`](../plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md)  
**Focused Step 2 plan:** [`../plans/B2_STEP_2_SUPPORT_DROP_CLAIM_CONTRACT_PLAN.md`](../plans/B2_STEP_2_SUPPORT_DROP_CLAIM_CONTRACT_PLAN.md)  
**Status:** Implemented; deterministic repository validation required

## Previous validated boundary

Step 1 upstream interval and source authority is complete and behavior-validated.

Validation record:

```text
working-memory/2026-07-31_2238_B2-step-1-upstream-interval-authority-validation.md
```

Validated input boundary:

```text
AuthoritativeUpstreamIntervalEvidence
```

with one exact release interval, trusted crossed-release index when available, exact GitHub Release bodies, exact proposed-tag changelog evidence, package metadata corroboration, and preserved source problems.

## Latest Step 2 product/test revision

```text
c023a3b09e5dc5d31e3bd0a55820b9d83a51f4db
Ground candidate Python line in exact quote
```

The GitHub connector reported no combined commit statuses for this revision. No Step 2 test pass is claimed in this record.

## Commits

Step 1 closure:

```text
a2321c5842a8ec023a82d19d02aef3c51eb85ec5
Validate Step 1 upstream interval authority
```

Step 2 plan:

```text
e692c4aed36992ce2b69e4ec8a5bc9d990f673f7
Finalize Step 2 support-drop claim plan
```

Tests first:

```text
ab619a501cb7d12062e45cc0516d5e2f5fcb190f
Test Step 2 support-drop grounding

3089e5900261210347ec96ceed3516091bb5ab6f
Test Step 2 support-drop edge behavior

3e5068a2706f8863bd5fc657cb4dcd6ee3cb4f90
Test Step 2 package exports
```

Initial implementation:

```text
ebfff823f512cd55862bdcb681a9459540623308
Add Step 2 support-drop claim contracts

ee746fa79fe3db890b987ca52861abdf7b897a5a
Export Step 2 support-drop contracts
```

Review-found evidence-link correction:

```text
ee7566c84e68aa718db12a0b5ab20690552ead60
Test quoted Python line grounding

c023a3b09e5dc5d31e3bd0a55820b9d83a51f4db
Ground candidate Python line in exact quote
```

## Added module

```text
src/upgradepilot/upstream_claim.py
```

The module is pure. It performs no network request and invokes no model or extraction adapter.

## Candidate layer

Created:

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

State invariants are validated deterministically. Candidate availability requires at least one candidate; non-available states reject attached candidates; unresolved requires a non-empty detail.

Created:

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

Every field remains untrusted until validation completes.

## Trusted semantic boundary

Only this semantic identity is admitted:

```text
category = support_boundary_change
change_state = support_dropped
python_line = canonical X.Y
```

Canonical Python-line rules:

- exactly two decimal integer components;
- no leading zero except `0`;
- no patch component;
- no wildcard;
- no comparator, prerelease, epoch, local version, or surrounding prose;
- exact trimmed text.

## Source grounding

Groundable sources:

```text
github_release_body
tagged_changelog
```

Rejected as prose authority:

```text
package_metadata
Dependabot copied notes
arbitrary documentation
model-selected text
unknown source kinds
```

GitHub Release candidates must identify the exact same release as `introduced_in_version` and resolve uniquely from the trusted Step 1 release-body records.

Tagged-changelog candidates must resolve to the one exact trusted `TaggedChangelogEvidence` record and cannot invent a release-body selector.

## Trusted interval membership

Available candidates require:

```text
CrossedReleaseIndexEvidence
```

The exact `introduced_in_version` must be one member of the trusted ordered release tuple.

```text
exact tagged changelog
+ no trusted crossed-release index
→ release_interval_unresolved
```

Step 2 does not parse or order versions itself.

## Exact quote and Python-line grounding

The validator proves:

```text
0 <= quote_start < quote_end <= len(exact_source_text)
exact_source_text[quote_start:quote_end] == source_quote
```

No whitespace, punctuation, capitalization, Unicode, or line-ending normalization occurs.

Review added an additional deterministic link:

```text
candidate python_line
must appear in source_quote
as one exact standalone major/minor token
```

This blocks a candidate from quoting Python `3.8` while separately claiming Python `3.9`, and blocks patch-token confusion such as treating `3.8` inside `3.8.1` as equivalent evidence.

## Trusted output

Created:

```text
GroundedPythonSupportDropClaim
├── category = support_boundary_change
├── change_state = support_dropped
├── python_line
├── introduced_in_version
├── interval
└── source_evidence[]
```

Each source record preserves:

```text
GroundedUpstreamClaimSource
├── source_kind
├── introduced_in_version
├── exact Step 1 source object
├── exact quote
├── quote_start
└── quote_end
```

The exact source object is:

```text
IntervalGitHubReleaseSource
or
TaggedChangelogEvidence
```

Equivalent candidates for the same Python line and introduced release combine exact source records. Duplicate exact records are deduplicated. Release-body evidence is ordered before tagged-changelog evidence for deterministic output.

Several distinct claim identities are not silently selected:

```text
different Python lines
or
different introduced releases
→ multiple_support_drop_claims
```

One invalid candidate blocks partial success from another candidate in the same result.

## Problem contract

Created:

```text
UpstreamSupportDropClaimProblem
```

States:

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

## Public package interface

Exported:

```text
CandidateUpstreamClaim
CandidateUpstreamClaimResult
GroundedPythonSupportDropClaim
GroundedUpstreamClaimSource
UpstreamSupportDropClaimProblem
UpstreamSupportDropClaimResult
validate_support_drop_candidates
```

Importing `upgradepilot` still performs no network request.

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

Expected focused invocation:

```text
24 tests
```

Expected complete deterministic suite:

```text
200 tests
```

These are derived counts, not observed passing results.

## Review boundary and remaining semantic limit

Deterministic grounding establishes:

- exact dependency context;
- admitted source identity;
- exact source quote and span;
- exact normalized Python-line token in the quote;
- allowed candidate category and direction values;
- trusted crossed-release membership;
- one non-conflicting claim identity.

It does not independently reinterpret arbitrary natural-language prose to prove that every varied sentence semantically means support was dropped. Candidate extraction reliability remains a later bounded evaluation responsibility under parent Step 6. Exact quotation and provenance keep that semantic judgment auditable and prevent detached model assertions.

## Explicit exclusions preserved

Step 2 does not:

- run an LLM or Instructor;
- define prompts, retries, or model settings;
- acquire release indexes, tags, files, releases, or metadata;
- add `packaging`;
- parse PEP 440 ordering;
- compare target `requires-python`;
- change target acquisition order;
- modify the CLI;
- infer compatibility, safety, merge, or recommendation outcomes.

Unchanged active modules include:

```text
src/upgradepilot/upstream_interval.py
src/upgradepilot/upstream_source.py
src/upgradepilot/github_release.py
src/upgradepilot/cli.py
src/upgradepilot/target_python.py
pyproject.toml
```

## Validation required

Run from the real checkout:

```bash
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

## Stop line

Step 2 remains open until both deterministic suites pass.

After validation, proceed to parent Step 3:

```text
Record and freeze the packaging method
```

Do not begin model integration, upstream network acquisition, target comparison, or CLI orchestration during Step 2 closure.

## Learning state

Concepts introduced and implemented:

- candidate schema versus trusted domain evidence;
- deterministic context echo validation;
- source resolution rather than candidate-provided authority;
- exact quote/span grounding;
- normalized semantic fields versus unchanged source text;
- trusted crossed-release membership;
- equivalent evidence combination;
- aggregate ambiguity and invalid-candidate precedence;
- auditable grounding versus later semantic-extraction reliability evaluation.

Current depth:

```text
structured explanation completed
+ focused plan created
+ tests written before implementation
+ implementation completed
+ review-found quote-to-line drift corrected
but
repository execution not yet observed
no user-owned technical explanation recorded
no independent implementation practice recorded
no formal assessment recorded
not mastered
```

Product behavior validation and learning mastery remain separate claims.
