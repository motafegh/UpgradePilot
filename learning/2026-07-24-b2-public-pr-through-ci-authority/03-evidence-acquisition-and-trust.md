# 03 — Evidence Acquisition and Trust

## SMART objective

Within 30–40 minutes, explain the request-to-trusted-record process, predict the correct failure category for eight scenarios, and justify the exact-head and pagination invariants.

## The core rule

All external data is untrusted until UpgradePilot validates it.

This includes data from GitHub even when:

- the repository is public;
- the request used HTTPS;
- GitHub returned `200 OK`;
- the JSON decoded successfully;
- the fields look plausible.

Trust is created in layers, not assumed from the source's reputation.

## Layered acquisition model

```text
user locator
→ local input validation
→ HTTP transport
→ HTTP status classification
→ JSON decoding
→ top-level shape validation
→ required-field type validation
→ semantic identity validation
→ completeness reconciliation
→ immutable internal record
```

Each arrow can fail for a different reason.

## Local input validation

Examples:

- repository must use the supported `owner/repository` grammar;
- PR number must be a positive integer;
- Python `bool` values must not accidentally pass as integers.

Why reject `True` as PR number `1`?

In Python, `bool` is a subclass of `int`. A naive `isinstance(True, int)` check succeeds. Domain validation must be stricter than language inheritance behavior.

## Transport and HTTP failure

### Timeout

No usable response arrived within the configured connect/read limits.

### Transport error

The request failed before a usable HTTP response existed.

### `404` not found or inaccessible

GitHub may use `404` for both absence and inaccessible private resources. UpgradePilot preserves the ambiguity instead of claiming which one occurred.

### `403` or `429`

The request was forbidden or rate-limited.

### Other non-success status

Classified as a general HTTP acquisition failure.

These are acquisition problems, not unsupported product evidence.

## Successful HTTP is only the beginning

A successful response can still fail because:

- body is not valid JSON;
- top level is an array when an object is required;
- required field is missing;
- field is the wrong type;
- integer is negative;
- string is empty;
- returned identity contradicts the request;
- pagination is incomplete.

This distinction is central:

```text
HTTP success
≠ evidence success
```

## Exact proposal identity

`PullRequestIdentity` freezes:

- repository;
- PR number;
- base branch and base SHA;
- head branch and head SHA;
- changed-file count;
- other presentation facts.

Branch names are mutable references. A branch named `dependabot/pip/pytest-9.0.3` can move to a different commit.

The head SHA is the stable revision identity used by the current analysis.

## Pagination as a correctness feature

Pagination is not merely about performance.

GitHub may return only the first page of results. If UpgradePilot uses that page without proving completeness, it might miss:

- another changed dependency;
- another workflow run;
- another job;
- contradictory evidence.

The pattern is:

```text
request page 1
→ validate every item
→ continue while expected records remain
→ reconcile acquired count with independent total
→ reject disagreement
```

### Changed files

The PR metadata `changed_files` count is the independent completeness target.

### Workflow runs and jobs

The response `total_count` is checked across pages. If it changes during pagination, the evidence set is unstable and the current slice rejects it.

## Why empty evidence is not green evidence

An empty tuple of exact-head workflow runs means:

```text
no matching workflow runs were acquired
```

It does not mean:

```text
all CI passed
```

Absence is an explicit evidence state.

## Identity chain for Actions

For a workflow run:

- event must be `pull_request`;
- run head SHA must equal the PR head SHA.

For a job:

- job run ID must equal the requested run ID;
- job head SHA must equal the PR head SHA.

For a workflow definition:

- workflow path comes from the exact run detail;
- file content is requested at the same head SHA;
- returned revision must match that exact revision.

This prevents “cross-revision evidence contamination.”

## Missing versus contradictory evidence

### Missing or unavailable

Examples:

- workflow definition returns ambiguous `404`;
- patch text is absent;
- no exact-head workflow runs exist.

The product should preserve absence and often return unsupported, insufficient, or unresolved.

### Contradictory

Examples:

- run SHA differs from PR head SHA;
- returned PR number differs from requested number;
- changed-file count says two but only one record is acquired;
- job run ID differs from requested run.

Contradiction is stronger than absence. The current evidence set cannot safely be used.

## Dependency injection for deterministic tests

A Requests `Session` can be injected into the client.

Practical meaning:

```text
production → real requests.Session()
tests      → Mock implementing session.get(...)
```

Why “dependency injection” makes sense:

The client receives its external dependency instead of creating an uncontrollable dependency in every test.

Current depth:

- understand the purpose;
- read a mocked response sequence;
- add or modify one focused test.

Deferred:

- dependency-injection frameworks;
- complex service containers;
- advanced mocking architecture.

## Failure prediction drill

Classify each scenario.

1. Repository locator is `github.com/owner/repo`.
2. Connection waits too long and raises `Timeout`.
3. GitHub returns `404`.
4. GitHub returns `200` with HTML instead of JSON.
5. JSON contains PR number `1146` after requesting `1145`.
6. PR says 101 changed files; only the first 100 are acquired.
7. Workflow run event is `push`.
8. Workflow file does not exist at the exact head SHA.

Expected classifications:

1. input rejection;
2. acquisition timeout;
3. not found or inaccessible acquisition failure;
4. malformed successful response;
5. semantic identity contradiction;
6. completeness failure;
7. Actions response contradiction;
8. explicit unavailable repository evidence, later interpreted as unresolved.

## What you must master

- the layered trust model;
- exact SHA identity;
- pagination completeness;
- absence versus contradiction;
- acquisition error versus unsupported/unresolved result;
- what deterministic mocks prove.

## Operationally understand

- HTTP status ranges;
- request headers and timeout tuple;
- JSON object/array validation;
- base64 workflow-file decoding;
- `Mock.side_effect` for multiple pages.

## Deferred

- retry/backoff policy;
- ETag and conditional requests;
- GraphQL;
- private-repository permissions;
- cryptographic internals of Git object IDs;
- async HTTP and connection-pool internals.

## Completion evidence

This file is mastered when you can classify the eight scenarios and explain why exact-head identity and pagination are correctness requirements, not implementation decoration.