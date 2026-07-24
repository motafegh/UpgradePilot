# 03 — Evidence Trust and Identity

## SMART objective

In 30–35 minutes, explain the layered trust process, classify eight failure scenarios, and justify exact-head identity and pagination as correctness rules.

## External data starts untrusted

GitHub data remains untrusted even when the repository is public and GitHub returns `200 OK`.

```text
user locator
→ local validation
→ HTTP transport
→ HTTP status
→ JSON decoding
→ shape/type validation
→ semantic identity validation
→ completeness reconciliation
→ internal record
```

Each layer answers a different question.

## Error and result categories

### Input rejection

The local locator is unsupported, for example malformed `owner/repository` or non-positive PR number.

### Acquisition failure

No usable successful response exists:

- timeout;
- transport error;
- `404` not found or inaccessible;
- `403`/`429` forbidden or rate-limited;
- other HTTP error.

GitHub's `404` ambiguity is preserved; the product must not invent whether the resource is absent or private.

### Malformed or contradictory successful response

HTTP succeeded, but evidence is unsafe:

- invalid JSON;
- wrong top-level shape;
- missing or wrongly typed field;
- returned PR number differs from requested number;
- run/job SHA differs from frozen head;
- pagination totals disagree.

### Valid but unsupported/unresolved evidence

The system worked, but current product rules cannot establish the target meaning:

- missing patch text;
- unsupported dependency syntax;
- unavailable workflow definition;
- tox or multi-job indirection.

These are normally explicit result states, not generic exceptions.

## Exact proposal identity

`PullRequestIdentity` freezes the proposal revision:

- repository and PR number;
- base branch/SHA;
- head branch/SHA;
- changed-file count.

Branch names move. The head SHA identifies the exact revision analyzed.

Identity chain:

```text
PullRequestIdentity.head_sha
→ WorkflowRun.head_sha
→ WorkflowJob.head_sha
→ workflow-definition revision
```

This prevents mixing evidence from old CI runs or the current default branch with a different PR revision.

## Pagination is evidence completeness

A valid first page may omit contradictory or additional evidence.

Current pattern:

```text
request page
→ validate every item
→ continue until expected total
→ reconcile final count
→ reject disagreement
```

- Changed files reconcile against PR metadata `changed_files`.
- Workflow runs/jobs preserve a stable `total_count` across pages.
- Explicit upper bounds reject cases the current slice cannot acquire completely.

Partial evidence is not silently accepted.

## Empty is not green

```text
no exact-head workflow runs
```

means absence of matching CI evidence. It does not mean all checks passed.

## Missing versus contradictory

**Missing/unavailable:** no patch, no workflow file, no runs. Preserve absence and stop honestly.

**Contradictory:** wrong SHA, wrong PR number, count mismatch. Reject the evidence set because combining it would be unsafe.

## Dependency injection in tests

The clients accept an optional Requests `Session`:

```text
production → real Session
tests → controlled Mock with the same get interaction
```

This makes network behavior deterministic in tests. Current required depth: understand the purpose, read `return_value`/`side_effect`, and modify one focused test. Framework-level dependency injection is deferred.

## Classification drill

1. `github.com/owner/repo` supplied as repository locator.
2. Requests raises `Timeout`.
3. GitHub returns `404`.
4. GitHub returns `200` with invalid JSON.
5. Requested PR 1145, response says 1146.
6. Metadata says 101 files; only 100 acquired.
7. Workflow event is `push`.
8. Workflow file is absent at exact head SHA.

Expected:

1. input rejection;
2. acquisition timeout;
3. not found or inaccessible;
4. malformed successful response;
5. semantic contradiction;
6. completeness failure;
7. Actions identity contradiction;
8. unavailable repository evidence, later unresolved.

## Must master

- layered trust;
- exact SHA chain;
- pagination completeness;
- absence versus contradiction;
- exception versus normal unresolved result;
- deterministic test versus live-network proof.

## Operationally understand

- timeout tuple and common headers;
- JSON object/array validation;
- base64 workflow-file decoding;
- mocked page sequences.

## Deferred

Retry/backoff, ETags, GraphQL, private-repository permissions, async HTTP, and Git cryptographic internals.

## Pass condition

Classify all eight scenarios and explain why SHA binding and pagination are product correctness—not optional implementation detail.