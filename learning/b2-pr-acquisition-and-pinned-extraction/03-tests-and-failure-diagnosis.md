# 03 — Tests and Failure Diagnosis

## Learning target

After this note, you should be able to explain what each current test category protects, what mocked evidence cannot prove, and which source boundary to inspect first when a test fails.

## The current proof has two parts

### Deterministic test suite

```text
12 tests
→ controlled inputs
→ no live-network dependency
→ repeatable behavior checks
```

### Live smoke command

```text
real public GitHub API
→ real PR and changed-file responses
→ current environment and network
→ one observed end-to-end case
```

Neither proof replaces the other.

## The six GitHub client tests

### 1. Exact PR identity construction

Protects:

- required PR fields become `PullRequestIdentity`;
- requested and returned identity are connected;
- explicit timeout is supplied;
- authorization is not invented when no token exists.

Does not prove GitHub is reachable or the live response still has this shape.

### 2. Ambiguous `404`

Protects the claim boundary:

```text
404
→ not found or inaccessible
```

It prevents the program from overstating that a PR definitely does not exist.

### 3. Valid changed-file construction

Protects:

- a successful JSON array becomes validated `ChangedFile` records;
- the request uses `per_page=100` and starts at page 1.

### 4. Multi-page acquisition

The mocked first page has 100 records and the second has one.

Protects:

```text
101 expected files
→ request page 1
→ request page 2
→ return all 101 records
```

This is a boundary test, not a performance test.

### 5. Count disagreement rejection

Protects the strongest completeness invariant:

```text
expected changed-file count
==
acquired validated record count
```

Without this check, partial evidence could be analyzed as though it were complete.

### 6. Non-array successful response rejection

Protects the changed-files endpoint representation boundary. HTTP success with the wrong JSON shape must not become product evidence.

## The six dependency extraction tests

### 1. Supported exact pinned change

Uses the real S004 patch shape:

```diff
-pytest==9.0.2
+pytest==9.0.3
```

Protects the supported output fields: source file, package, old version, and proposed version.

### 2. Missing patch

Protects explicit absence:

```text
patch=None
→ UnsupportedDependencyChange(reason="missing_patch_evidence")
```

It prevents absence from being treated as an empty but complete patch.

### 3. Range requirement remains unsupported

```diff
-pytest>=9.0.2
+pytest>=9.0.3
```

Protects the narrow grammar. Similar-looking syntax is not silently interpreted as an exact version replacement.

### 4. Different packages remain unsupported

```diff
-pytest==9.0.2
+pluggy==1.6.0
```

Protects package identity rather than treating any removed/added pin pair as one update.

### 5. Multiple candidate changes are ambiguous

Protects the “exactly one supported dependency change” boundary.

### 6. Patch count disagreement is incomplete evidence

If GitHub reports more additions or deletions than the patch exposes, the patch may be truncated or incomplete. The extractor must not claim complete interpretation.

## How the mocks work

### `Mock()` response

The tests create a controlled object with:

```python
response.status_code = 200
response.json.return_value = ...
```

This supplies the smallest behavior the client needs from an HTTP response.

### Injected session

```python
client = GitHubReadClient(session=session)
```

The production client normally uses `requests.Session`. Tests inject a mock session so they can inspect calls and avoid network dependence.

This is dependency injection: an external collaborator is supplied from outside rather than fixed inside every method.

### `side_effect`

```python
session.get.side_effect = [first, second]
```

The first call returns page 1 and the second call returns page 2. This lets one test model a sequence of external responses.

### `assertRaises`

```python
with self.assertRaises(GitHubResponseError):
    ...
```

The test passes only when the expected failure boundary is activated.

## Why the tests use helper builders

`_identity`, `_changed_file`, and `_record` remove irrelevant setup repetition.

A good helper should make the tested difference clearer. It should not hide the behavior being tested or encode the product answer secretly.

## What the 12 tests prove

They support that, for the represented controlled cases:

- PR identity is built correctly;
- important acquisition failures remain distinct;
- changed-file pages are combined;
- malformed or incomplete evidence is rejected;
- the exact pinned update grammar works;
- major unsupported states remain explicit.

## What the 12 tests do not prove

They do not establish:

- live GitHub availability;
- compatibility with every GitHub response variation;
- all pagination edge cases;
- all Python requirement syntax;
- package version ordering or resolver correctness;
- CI relevance or authority;
- upgrade safety or a recommendation;
- production load, security hardening, or independent ownership.

## What the live smoke run adds

The live run establishes that the current installed package, Requests dependency, network path, GitHub endpoint, real response shape, pagination path, and extractor worked together for S004 at the observed time.

It still represents one case and one environment.

## Failure localization map

| Symptom | Inspect first | Likely boundary |
|---|---|---|
| No response or timeout | `_get` | transport/acquisition |
| Unexpected status reason | `_raise_for_status` | HTTP classification |
| Object returned where array expected | `_read_json_array` | representation |
| Missing or mistyped file field | `_parse_changed_file` | schema validation |
| Acquired count differs from metadata | `get_changed_files` loop and stop conditions | evidence completeness |
| Exact pin produces no candidate | requirement regex and line filtering | grammar extraction |
| Equivalent package spellings mismatch | `normalize_package_name` | package identity |
| Two changes accepted as one | candidate counting | ambiguity control |
| Supported result has wrong versions | result construction | extraction output |
| CLI reports acquisition failure for unsupported grammar | CLI/result branching | exception versus normal result state |

## Debugging method for this stage

Use this order:

```text
failing test name
→ expected protected boundary
→ actual result or exception
→ earliest source function that owns that boundary
→ smallest discriminating inspection
→ root cause
→ smallest repair
→ rerun failing test
→ rerun all 12 tests
→ run live smoke only when the changed behavior reaches the live path
```

Do not edit acquisition, extraction, and CLI simultaneously before locating the defect.

## Ownership transfer test

The next test should protect package normalization:

```diff
-demo.package==1.0.0
+demo_package==1.1.0
```

Prediction:

```text
demo.package
and
demo_package
→ normalize to demo-package
→ supported PinnedDependencyChange
```

A failure localizes differently depending on its result:

- `package_mismatch` → normalization comparison;
- `no_supported_pinned_change` → requirement grammar;
- supported result with wrong fields → result construction;
- unrelated acquisition error → test arrangement or responsibility mixing.

## Recall action

Choose four existing tests and say, in one sentence each:

1. the invariant protected;
2. the source function most directly exercised;
3. one important behavior the test does not prove.

Pass when your answers identify boundaries, not merely test inputs.