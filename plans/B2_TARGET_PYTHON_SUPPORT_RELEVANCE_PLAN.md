# B2 Target Python Support Relevance Plan

**Owner:** Ali Rajabi  
**Parent gate:** [`B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md`](B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md)  
**Selected decision plan:** [`B2_TRANSPARENT_DECISION_METHOD_PLAN.md`](B2_TRANSPARENT_DECISION_METHOD_PLAN.md)  
**Stable product authority:** [`../PROJECT_CHARTER.md`](../PROJECT_CHARTER.md)

## Purpose

Define the smallest product slice that connects one explicit upstream Python-support claim to exact-revision target-repository evidence without turning the LLM into a decision maker.

```text
attributed upstream support claim
+ exact-head target Python-support evidence
→ deterministic overlap or honest unresolved result
```

This plan defines position-neutral scope, sequence, proof, and stop conditions. `../MEMORY.md` alone selects it and records continuation.

## Owning question

For one supported exact pinned Python dependency update:

> When the upstream release explicitly adds or drops support for a Python version, does the target repository contain explicit exact-head evidence that the same Python version belongs to its declared or exercised support boundary?

## First bounded slice

The first target-side source is:

```text
pyproject.toml at the exact pull-request head SHA
→ [project].requires-python
```

This source is selected first because:

- the existing `GitHubRepositoryClient` already acquires bounded UTF-8 files at the immutable PR head;
- Python 3.12 includes `tomllib`, so TOML parsing requires no new dependency;
- `[project].requires-python` is an explicit project declaration rather than inferred repository usage;
- absent, malformed, or unsupported declarations can remain typed unresolved evidence.

The first slice does not yet treat workflow matrices, tox environments, classifiers, documentation, or runtime deployment files as equivalent evidence. Those may be added only after a concrete unresolved case demonstrates the need.

## Responsibility separation

```text
Target acquisition
→ fetch pyproject.toml at the exact PR head

Target interpretation
→ parse [project].requires-python without evaluating release prose

Upstream interpretation
→ separately admitted attributed support-added or support-dropped claim

Relevance evaluation
→ deterministic comparison between the two bounded inputs

Decision
→ remains outside this slice
```

## Target evidence states

The target parser must preserve at least:

- `available` — a non-empty textual `[project].requires-python` value was established;
- `file_unavailable` — the exact-head `pyproject.toml` was absent or inaccessible;
- `malformed_toml` — the file existed but could not be parsed as TOML;
- `project_table_absent` — TOML parsed but had no `[project]` table;
- `requires_python_absent` — `[project]` existed but did not declare `requires-python`;
- `invalid_requires_python` — the field existed but was not non-empty text.

None of these states may be converted into an inferred support range.

## Work sequence

### Step 1 — Acquire and expose target declaration

Use `GitHubRepositoryClient.get_exact_head_text_file` with:

```text
path: pyproject.toml
ref: PullRequestIdentity.head_sha
```

Parse only the explicit `[project].requires-python` value with `tomllib` and expose the typed result in the CLI evidence report.

### Step 2 — Freeze the support-claim input

Define the smallest attributed upstream support claim needed by the comparator:

```text
category: support_boundary_change
change_state: support_added | support_dropped
python_version: normalized major.minor line
source_quote: exact contiguous release-note span
```

The model may propose this claim only after grounding and category/change-state validation. The comparator must accept the same typed claim from controlled tests without requiring an LLM.

### Step 3 — Select deterministic version-range evaluation

Compare the simplest credible approaches for evaluating whether a Python major/minor line intersects a `requires-python` declaration:

1. a standards-based PEP 440 implementation;
2. a deliberately narrower supported grammar;
3. abstention for declarations outside the supported grammar.

Do not implement a home-grown general PEP 440 parser. Any new runtime dependency must be separately justified and approved under repository dependency-admission rules.

### Step 4 — Produce bounded relevance states

The comparator must distinguish at least:

- `declared_support_overlap` — target declaration explicitly includes the upstream-changed Python line;
- `outside_declared_support` — target declaration explicitly excludes that line under the accepted evaluator;
- `target_support_unresolved` — target evidence is absent, malformed, or outside the accepted comparison grammar;
- `upstream_claim_unresolved` — no valid grounded support-boundary claim exists;
- `conflicting_upstream_claims` — opposing grounded support claims cannot be collapsed.

These are relevance results, not merge recommendations.

## Proof obligations

Controlled tests must prove:

1. exact-head `pyproject.toml` acquisition is used;
2. valid `requires-python` text becomes available evidence;
3. missing file, malformed TOML, missing table, missing field, and invalid field remain distinct;
4. no target support range is invented;
5. comparison does not run without both valid inputs;
6. a support drop that overlaps target-declared support is not mislabeled safe;
7. a non-overlap result does not claim universal compatibility;
8. unsupported range syntax produces unresolved behavior rather than guessing;
9. no package, repository, version, or fixture wording is hardcoded;
10. the ordinary product test suite remains green.

## Stop line

Stop this plan when one public PR can expose:

```text
exact upstream support-boundary claim
+ exact-head target requires-python evidence
→ deterministic bounded relevance result
```

Do not continue here into:

- repository-wide dependency usage analysis;
- arbitrary build-system or ecosystem support;
- broad workflow/tox/configuration aggregation without an activated need;
- safety scoring or automatic merge/block action;
- target mutation;
- large evaluation-corpus expansion;
- further model comparison unrelated to a demonstrated extraction blocker.

## Maintenance

Change this plan only when its responsibility, admitted sources, result states, proof obligations, or stop line changes. Do not record progress, current status, latest commits, or immediate continuation here.
