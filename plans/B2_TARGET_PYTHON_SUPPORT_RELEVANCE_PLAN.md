# B2 Target Python Support Relevance Plan

**Owner:** Ali Rajabi  
**Parent gate:** [`B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md`](B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md)  
**Parent decision plan:** [`B2_TRANSPARENT_DECISION_METHOD_PLAN.md`](B2_TRANSPARENT_DECISION_METHOD_PLAN.md)  
**Stable product authority:** [`../PROJECT_CHARTER.md`](../PROJECT_CHARTER.md)

## Purpose

Define the smallest product slice that connects one explicit upstream Python-version support-drop claim to one exact-revision target-repository declaration.

```text
upstream: support for Python X.Y was dropped
+ target: exact-head [project].requires-python
→ declared-range overlap, declared non-overlap, or honest unresolved result
```

This is a relevance result, not a compatibility, safety, or merge decision. This plan remains position-neutral; `../MEMORY.md` alone selects it and records continuation.

## Why this plan exists

The release-note experiment established that a local model can represent some bounded upstream claims, including the corrected v1.3 compatibility-assurance case. It did not establish whether any extracted claim matters to the target repository.

A support-drop claim is useful only when UpgradePilot can compare it with target-side evidence. For example:

```text
upstream: Python 3.9 support was dropped

target declaration: requires-python = ">=3.9"
→ Python 3.9 is inside the declared installation range

target declaration: requires-python = ">=3.11"
→ Python 3.9 is outside the declared installation range
```

The first result exposes a concrete declared-range conflict requiring later decision handling. The second establishes only absence of overlap with this declaration; it does not prove universal compatibility or safety.

## Owning question

For one supported exact pinned Python dependency update:

> When the upstream release explicitly states that support for Python `X.Y` was dropped, does the target repository's exact-head `[project].requires-python` declaration include that Python line?

## First bounded scope

### Upstream side

Only one grounded claim form is admitted initially:

```text
category: support_boundary_change
change_state: support_dropped
python_line: normalized X.Y
source_quote: exact contiguous upstream release span
```

`support_added`, generic behavior changes, compatibility assurances, deprecations, and removals remain outside this first relevance comparison.

### Target side

Only this source is admitted initially:

```text
pyproject.toml at PullRequestIdentity.head_sha
→ [project].requires-python
```

This source is selected because:

- `GitHubRepositoryClient.get_exact_head_text_file` already provides bounded UTF-8 acquisition at the immutable PR head;
- Python 3.12 provides `tomllib`, so TOML structure can be parsed without a new dependency;
- `[project].requires-python` is an explicit project declaration rather than an inference from file names or prose;
- missing, malformed, or unsupported evidence can remain explicit.

## Authority and claim limits

`[project].requires-python` establishes the project's declared Python installation-version specifier at one exact revision. It does **not** establish:

- which Python versions CI actually executed;
- production runtime versions;
- every Python version the maintainers actively test;
- dependency usage on the affected path;
- update safety or a maintainer action.

Therefore the comparator may say only whether Python `X.Y` is inside or outside the accepted meaning of that declaration.

Workflow matrices, tox environments, classifiers, documentation, and deployment files are not silently combined with this evidence. They require a later activated need and their own authority rules.

## Responsibility separation

```text
Target acquisition
→ fetch exact-head pyproject.toml

Target interpretation
→ parse only [project].requires-python

Upstream claim input
→ receive one separately validated grounded support_dropped claim

Range evaluation
→ determine whether X.Y is included by the accepted specifier method

Relevance result
→ declared overlap, declared non-overlap, or unresolved

Decision
→ remains outside this plan
```

## Target evidence states

The target parser must preserve at least:

- `available` — a non-empty textual `[project].requires-python` value was established;
- `file_unavailable` — exact-head `pyproject.toml` was absent or inaccessible;
- `malformed_toml` — the file existed but was not valid TOML;
- `project_table_absent` — TOML parsed but had no `[project]` table;
- `requires_python_absent` — `[project]` existed but did not declare `requires-python`;
- `invalid_requires_python` — the field existed but was not non-empty text.

No unavailable or malformed state may be converted into an inferred range.

## Known gaps before implementation

1. The current experimental LLM claim schema does not contain a dedicated normalized `python_line` field.
2. Gemma v1.3 passed only the exact compatibility claim-partition case; it has not yet proven reliable support-drop extraction.
3. The project has not selected a deterministic Python specifier evaluator.
4. No target-side Python declaration is currently acquired or exposed by the product command.
5. No relevance result is currently connected to evidence sufficiency or maintainer action.

These gaps are the reason prompt tuning is paused rather than treated as completed model adoption.

## Work sequence

### Step 1 — Acquire and expose the target declaration

Use `GitHubRepositoryClient.get_exact_head_text_file` for `pyproject.toml`, parse it with `tomllib`, and expose the typed target evidence through the CLI.

This step does not require an LLM or a version-range evaluator.

### Step 2 — Freeze the upstream support-drop input contract

Define and test the typed support-drop input independently of any model runtime. Controlled tests must be able to construct it directly.

Do not resume sentence-by-sentence prompt tuning merely to fill this contract. First determine whether the target-side evidence makes the claim useful.

### Step 3 — Select the deterministic range method

Compare:

1. a standards-based PEP 440 specifier implementation;
2. a deliberately narrower accepted grammar with explicit abstention;
3. no comparison when the declaration is outside the accepted method.

Do not implement a home-grown general PEP 440 parser. A new runtime dependency requires separate justification and Ali approval.

### Step 4 — Implement bounded relevance evaluation

The first comparator must distinguish:

- `declared_python_overlap` — target `requires-python` includes the dropped Python line;
- `outside_declared_python_range` — the declaration excludes that line;
- `target_declaration_unresolved` — target evidence is unavailable, malformed, missing, or unsupported;
- `upstream_claim_unresolved` — no valid grounded support-drop claim is available;
- `comparison_unsupported` — both inputs exist but the accepted range method cannot evaluate them responsibly.

These states must not contain `safe`, `compatible`, `merge`, or equivalent claims.

### Step 5 — Prove the narrow product value

After controlled tests, run one public read-only case only when both inputs are available. Record exactly what the result proves and does not prove.

If no suitable public case is available, preserve the controlled proof and the live evidence gap rather than manufacturing a case.

## Proof obligations

Controlled tests must prove:

1. the target file is requested at the exact PR head SHA;
2. a valid `requires-python` declaration becomes available evidence with path, revision, and blob identity;
3. missing file, malformed TOML, missing table, missing field, and invalid field remain distinct;
4. no target range is inferred from workflows, classifiers, documentation, or repository age;
5. comparison cannot run without one valid support-drop claim and one valid target declaration;
6. an included dropped Python line produces `declared_python_overlap`;
7. an excluded line produces only `outside_declared_python_range`, not a safety conclusion;
8. unsupported specifier syntax produces `comparison_unsupported`;
9. no package, repository, version, or release wording is hardcoded;
10. the ordinary product test suite remains green.

## Rejection conditions

Reframe or stop this slice if:

- `requires-python` cannot provide a useful distinction for realistic supported cases;
- useful comparison requires broad repository inference before the narrow declaration is tested;
- the upstream claim cannot expose a reliable normalized Python line without renewed disproportionate prompt tuning;
- the result would not affect any later bounded decision state;
- the work begins implying safety from declared-range non-overlap.

## Stop line

Stop this plan when UpgradePilot can expose, for one admitted case:

```text
one grounded Python support-drop claim
+ exact-head target requires-python evidence
→ deterministic declared-range relevance or honest unresolved result
```

Do not continue here into:

- support-added interpretation;
- broad repository usage analysis;
- workflow/tox/configuration aggregation without an activated gap;
- safety scoring or automatic merge/block action;
- target mutation;
- large semantic-corpus expansion;
- further model comparison unrelated to a demonstrated blocker.

## Maintenance

Change this plan only when its responsibility, admitted sources, authority limits, result states, proof obligations, rejection conditions, or stop line changes. Do not record progress, current status, latest commits, or immediate continuation here.