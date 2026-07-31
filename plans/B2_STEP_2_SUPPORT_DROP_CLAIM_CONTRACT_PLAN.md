# B2 Step 2 — Support-drop claim contract plan

**Owner:** Ali Rajabi  
**Parent:** [`B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`](B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md)  
**Required predecessor:** [`B2_STEP_1_UPSTREAM_INTERVAL_AUTHORITY_PLAN.md`](B2_STEP_1_UPSTREAM_INTERVAL_AUTHORITY_PLAN.md)  
**Status:** Approved and controlling for target-relevance Step 2

## Purpose

Freeze the smallest deterministic boundary between untrusted semantic extraction and trusted Python support-drop evidence.

```text
AuthoritativeUpstreamIntervalEvidence
+ untrusted CandidateUpstreamClaimResult
→ one GroundedPythonSupportDropClaim
   or one explicit UpstreamSupportDropClaimProblem
```

This step defines and validates the contracts only. It does not select or invoke an LLM, Instructor, an OpenAI-compatible client, or any other extraction adapter.

## Owning question

Given one already trusted upstream interval authority bundle and one untrusted structured candidate result:

> Can UpgradePilot deterministically prove that one exact admitted upstream source states that support for one normalized Python `X.Y` line was dropped in one release inside the trusted crossed-version interval?

## Trust boundary

Schema-shaped output is not trusted evidence.

```text
candidate object exists
≠
claim is grounded
```

The validator must independently establish:

- dependency and interval identity;
- admitted source kind;
- exact source resolution from the authority bundle;
- exact contiguous source span;
- allowed category;
- allowed direction;
- normalized Python major/minor line;
- introduced release membership in the trusted crossed-release index;
- one non-conflicting final claim.

No candidate-provided source text, repository, path, blob, tag, release body, or interval membership becomes authoritative merely because the structure contains it.

## Candidate result contract

Create:

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

Candidate result states:

```text
candidates_available
no_relevant_claim
unresolved
```

Rules:

```text
candidates_available
→ at least one candidate

no_relevant_claim
→ no candidates

unresolved
→ no candidates + non-empty detail
```

Every state preserves the exact dependency identity supplied to extraction so deterministic validation can reject context drift.

## Candidate claim contract

Create:

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

All candidate fields remain untrusted.

### Admitted semantic form

Only this meaning may become trusted during Step 2:

```text
category = support_boundary_change
change_state = support_dropped
python_line = normalized X.Y
```

Reject rather than reinterpret:

- support added;
- generic compatibility claims;
- deprecation or removal claims without the admitted support-drop meaning;
- implementation, security, performance, bug-fix, or platform claims;
- malformed or patch-level Python versions;
- prose-selected categories outside the contract.

## Candidate source selection

Only these source kinds may ground a claim:

```text
github_release_body
tagged_changelog
```

The candidate identifies a source; the validator resolves the exact source from `AuthoritativeUpstreamIntervalEvidence`.

### GitHub Release candidate

```text
source_kind = github_release_body
source_release_version = exact crossed release version
introduced_in_version = same exact release version
```

The validator must find exactly one matching `IntervalGitHubReleaseSource` in the trusted authority bundle.

### Tagged changelog candidate

```text
source_kind = tagged_changelog
source_release_version = null
introduced_in_version = exact crossed release section/version identity
```

The validator must use the one exact `TaggedChangelogEvidence` admitted by Step 1.

Package metadata, Dependabot-copied notes, arbitrary documentation, and model-selected text cannot ground semantic prose claims.

## Trusted crossed-interval membership

A candidate support-drop claim cannot be grounded without:

```text
CrossedReleaseIndexEvidence
```

The candidate's `introduced_in_version` must be one exact member of the trusted `ordered_versions` tuple.

Step 2 does not parse or order versions itself. It consumes the already trusted index identity.

Therefore:

```text
exact tagged changelog
+ no trusted crossed-release index
→ release_interval_unresolved
```

This is required for intermediate-release claims such as a support drop introduced in `2.8` inside a `2.6 → 2.8.4` update.

## Exact quote/span grounding

The candidate supplies:

```text
source_quote
quote_start
quote_end
```

The validator must prove:

```text
0 <= quote_start < quote_end <= len(source_text)
source_text[quote_start:quote_end] == source_quote
source_quote is non-empty exact text
```

The exact span is authoritative only because it is checked against the exact admitted source text already preserved by Step 1.

Do not normalize whitespace, punctuation, capitalization, Unicode, or line endings during grounding. Semantic normalization belongs only to explicitly named fields such as `python_line`.

## Python-line normalization

Admit only canonical decimal major/minor text:

```text
X.Y
```

Rules:

- exactly two non-negative integer components;
- no leading zero except the component `0` itself;
- no patch component;
- no wildcard;
- no prerelease, epoch, local version, comparator, or surrounding prose;
- trimmed exact text.

Examples:

```text
3.8    → admitted
3.10   → admitted
03.8   → invalid_python_line
3.8.1  → invalid_python_line
3.8.*  → invalid_python_line
Python 3.8 → invalid_python_line
```

## Trusted claim contract

Create:

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
├── source
├── source_quote
├── quote_start
└── quote_end
```

`source` is the exact trusted Step 1 object:

```text
IntervalGitHubReleaseSource
or
TaggedChangelogEvidence
```

Equivalent candidates for the same Python line and introduced release may combine exact source records.

Distinct claim identities are not silently selected:

```text
same Python line + same introduced release
→ one claim with combined source evidence

different Python lines
or
different introduced releases
→ multiple_support_drop_claims
```

## Problem contract

Create:

```text
UpstreamSupportDropClaimProblem
├── state
├── interval
└── detail
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

Every rejected or unresolved condition is a normal product result, not an exception, once the function receives supported contract object types.

## Validation precedence

The validator must not allow a valid candidate to hide an invalid candidate in the same result.

Required order:

1. validate authority/result object types;
2. validate echoed dependency identity;
3. validate candidate-result state invariants;
4. require a trusted crossed-release index for available candidates;
5. validate every candidate structurally;
6. validate category and direction;
7. validate Python-line normalization;
8. validate introduced-release membership;
9. resolve the exact admitted source;
10. verify exact source quote/span;
11. group only equivalent grounded candidates;
12. reject several distinct claim identities.

Any invalid candidate stops the aggregate result. Partial candidate success is not trusted.

## Modification surface

Expected product files:

```text
src/upgradepilot/upstream_claim.py
src/upgradepilot/__init__.py
```

Expected tests:

```text
tests/test_upstream_claim.py
tests/test_upstream_claim_edges.py
tests/test_package_interface.py
```

Do not modify during Step 2 unless a concrete contradiction appears:

```text
src/upgradepilot/upstream_interval.py
src/upgradepilot/upstream_source.py
src/upgradepilot/github_release.py
src/upgradepilot/cli.py
src/upgradepilot/target_python.py
pyproject.toml
```

## Test-first sequence

Before product source:

1. test candidate-result state invariants;
2. test exact dependency identity agreement;
3. test one valid release-body claim;
4. test one valid tagged-changelog claim;
5. test exact quote/span grounding;
6. test wrong category;
7. test wrong direction;
8. test malformed Python line;
9. test source-kind rejection;
10. test missing source identity;
11. test missing trusted crossed-release index;
12. test introduced version outside the interval;
13. test release-body version/source agreement;
14. test equivalent multi-source claim combination;
15. test duplicate candidate deduplication;
16. test conflicting Python lines;
17. test conflicting introduced releases;
18. test invalid candidate blocking valid candidate;
19. test package-level exports;
20. then implement the smallest pure validator.

## Proof obligations

Step 2 is complete only when controlled tests establish:

1. candidate structures do not become trusted automatically;
2. exact dependency context drift is rejected;
3. only `support_boundary_change / support_dropped` is admitted;
4. only normalized `X.Y` Python lines are admitted;
5. only release bodies and tagged changelogs can ground prose claims;
6. release candidates resolve to the exact matching release body;
7. changelog candidates resolve to the exact Step 1 tagged changelog;
8. exact quote offsets and text must match the authoritative source exactly;
9. candidate release identity must belong to the trusted crossed-release index;
10. an intermediate release may be grounded from a proposed-tag changelog;
11. no trusted release index produces an explicit unresolved result;
12. equivalent exact evidence may combine without losing provenance;
13. several distinct support-drop claims remain explicit rather than selected;
14. one malformed or unsupported candidate blocks partial success;
15. production logic contains no S001-specific repository, package, version, quote, path, tag, blob, Python line, or expected result;
16. the ordinary deterministic test suite remains green.

## Explicit exclusions

Step 2 does not:

- select or run a model;
- add Instructor, Pydantic, or an OpenAI-compatible client;
- define prompts or retries;
- acquire release indexes, tags, files, or metadata;
- add `packaging`;
- parse PEP 440 release ordering;
- compare target `requires-python`;
- move target acquisition behind conditional activation;
- alter the CLI;
- decide compatibility, safety, recommendation, or action.

## Stop line

Stop Step 2 when UpgradePilot can deterministically transform:

```text
AuthoritativeUpstreamIntervalEvidence
+ CandidateUpstreamClaimResult
```

into:

```text
one GroundedPythonSupportDropClaim
```

only when exact identity, source, interval, quote, category, direction, and Python-line requirements are all proven; otherwise it must return one explicit claim problem.

After behavior validation, proceed to parent Step 3 — record and freeze the `packaging` method.
