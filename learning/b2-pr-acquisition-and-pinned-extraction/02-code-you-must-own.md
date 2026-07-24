# 02 — Code You Must Own in an AI-Assisted Workflow

## Learning target

You do not need to reproduce every line from memory. You do need to locate, explain, modify, test, and diagnose the central responsibility safely.

In an AI-heavy engineering workflow, code ownership means:

```text
understand the responsibility
→ trace inputs and outputs
→ recognize invariants and failure states
→ review generated implementation critically
→ make a central change
→ predict and interpret tests
→ diagnose a defect
→ explain limits
```

## Read the code in execution order

### 1. `cli.main`

File: `src/upgradepilot/cli.py`

Own this flow:

```text
parse repository and PR number
→ construct GitHubReadClient
→ acquire PullRequestIdentity
→ acquire ChangedFile records
→ extract dependency result
→ print supported or unsupported evidence
```

You should know which errors cause exit codes 2, 3, and 4, and why unsupported extraction is printed as a normal result rather than raised as an acquisition exception.

### 2. `GitHubReadClient.get_pull_request`

File: `src/upgradepilot/github_client.py`

Own these responsibilities:

- validate local input;
- build the public GitHub endpoint;
- perform a read-only request;
- validate successful JSON as an object;
- construct exact `PullRequestIdentity`.

Do not confuse this method with changed-file acquisition or dependency extraction.

### 3. `_get` and `_raise_for_status`

These functions separate network behavior from evidence parsing.

You should be able to explain:

- why timeout and broader transport errors are separate;
- why `404` remains `not_found_or_inaccessible`;
- why `403` and `429` share the current bounded reason;
- why status handling happens before JSON parsing;
- why the client uses explicit connect/read timeouts.

### 4. `_read_json_object`, `_read_json_array`, and required-field helpers

These functions treat external JSON as untrusted.

Own the invariant:

```text
successful HTTP response
≠
valid product evidence
```

A helper may look small, but it protects every later assumption about types and required fields.

### 5. `GitHubReadClient.get_changed_files`

This is the central acquisition loop for the current increment.

Trace these variables:

```text
identity.changed_files
records
page
items
```

The loop:

1. rejects a PR beyond the current complete-acquisition limit;
2. returns an empty tuple for zero reported changed files;
3. requests pages of 100;
4. validates the top-level array;
5. validates every item as an object and then as `ChangedFile`;
6. stops when evidence indicates the final page or enough records were acquired;
7. compares the acquired count with PR metadata;
8. returns an immutable tuple.

You must be able to change or test this loop without accidentally allowing partial evidence to reach extraction.

### 6. `extract_pinned_dependency_change`

File: `src/upgradepilot/dependency_change.py`

This is a deterministic, side-effect-free interpretation function. It receives already validated records and returns one of two result types.

```text
PinnedDependencyChange
or
UnsupportedDependencyChange
```

Own the order of checks:

- no changed files;
- missing or blank patch;
- count patch additions and deletions;
- collect exact pinned removed/added candidates;
- reject incomplete patch evidence;
- reject no candidates or ambiguous candidates;
- require same file and supported file status;
- normalize package names and compare them;
- require different versions;
- construct the supported result.

The order matters because it determines the most accurate explanation for why analysis stopped.

## Python syntax to master now

### `@dataclass(frozen=True, slots=True)`

Practical meaning:

- `@dataclass` generates routine initialization and comparison behavior;
- `frozen=True` prevents normal field reassignment after construction;
- `slots=True` restricts instances to declared fields and reduces accidental attribute creation.

Required ability: read, construct, compare, and explain these records. You do not need to reproduce dataclass internals.

### Union types: `str | None`

Practical meaning:

```python
patch: str | None
```

The patch may contain text or may be explicitly absent.

Required ability: preserve and branch on absence correctly. Do not convert absence into invented text.

### Python 3.12 type alias

```python
type DependencyChangeResult = PinnedDependencyChange | UnsupportedDependencyChange
```

This names the two valid result shapes. It helps readers and type-checking tools; runtime Python does not automatically validate every annotation.

Required ability: understand why callers must branch on the concrete result type.

### `Mapping[str, Any]`

`Mapping` means dictionary-like read access without requiring one concrete dictionary class. `Any` acknowledges that external JSON values are unknown until validated.

Required ability: understand why untrusted JSON begins broad and becomes specific through validation.

### Keyword-only parameters using `*`

Example:

```python
def _get(url: str, *, resource: str, params: Mapping[str, int] | None = None):
```

Arguments after `*` must be named by the caller. This makes consequential context such as `resource="changed-file"` explicit.

Required ability: read and correctly call such functions.

### `raise ... from exc`

This raises a product-specific error while preserving the original exception as its cause.

Required ability: explain the product error and inspect the underlying cause during debugging.

### `isinstance`

The code uses runtime type checks for untrusted data and result branching.

Required ability: distinguish:

```text
validation of external values
from
branching between accepted internal result types
```

### Regular-expression `fullmatch`

The pinned requirement pattern accepts only the entire current line grammar, not a matching substring.

Required ability: explain why a strict narrow grammar is safer than pretending to parse every valid Python requirement form.

You do not need to memorize the complete regular expression. You must know its accepted shape, rejected shapes, and where to change/test it.

## Syntax to understand operationally, not memorize

- `from __future__ import annotations`;
- comprehensions used to collect pages or test data;
- `dict[str, Any]`, `list[...]`, and `tuple[...]` annotations;
- `@staticmethod` placement;
- `requests.Session` internals;
- `argparse` construction details;
- exact regex metacharacter-by-metacharacter behavior.

You should be able to read and safely edit around these constructs with documentation or AI assistance.

## Design boundaries you must be able to defend

### I/O and interpretation are separate

`GitHubReadClient` performs acquisition and structural validation. `extract_pinned_dependency_change` interprets validated patch evidence.

This separation makes deterministic tests possible and prevents network failure semantics from being mixed with unsupported-analysis semantics.

### Exceptions and normal result states are separate

Use exceptions for invalid input, failed acquisition, malformed responses, or inconsistent evidence.

Use `UnsupportedDependencyChange` when valid acquired evidence is outside the current extraction boundary.

### Narrow grammar is intentional

The extractor does not claim to parse all requirement syntax. It recognizes one proven form and preserves all other forms as unsupported.

### No target mutation

The client issues read-only requests. No code path comments on, approves, edits, merges, or otherwise mutates the target repository.

## AI-era code review checklist

When AI proposes a change here, check:

1. Which responsibility owns the change?
2. What new input or state is being accepted?
3. Which invariant protects incomplete evidence?
4. Does a new exception replace a normal unsupported result incorrectly?
5. Could partial pagination reach extraction?
6. Is external data validated before use?
7. Is any known PR, package, version, or expected answer hardcoded?
8. Which deterministic test proves the new behavior?
9. What does the test still not prove?
10. Can the change be reversed without a broad rewrite?

## Trace action

Open the pinned source baseline and trace this case using function names only:

```text
googlefonts/glyphsLib + 1145
→ ?
→ ?
→ PullRequestIdentity
→ ?
→ tuple[ChangedFile, ...]
→ ?
→ PinnedDependencyChange
→ terminal output
```

Expected central names:

```text
cli.main
GitHubReadClient.get_pull_request
GitHubReadClient.get_changed_files
extract_pinned_dependency_change
```