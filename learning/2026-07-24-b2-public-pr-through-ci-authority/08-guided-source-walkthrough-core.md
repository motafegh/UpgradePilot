# 08 — Guided Source Walkthrough: CLI, GitHub Trust Boundary, PR Evidence, and Dependency Extraction

## Purpose

This file is the missing bridge between the conceptual notes and the actual Python implementation.

Use it with these files open beside it:

```text
src/upgradepilot/cli.py
src/upgradepilot/github_api.py
src/upgradepilot/github_client.py
src/upgradepilot/dependency_change.py
```

Do not try to memorize all syntax. Your goal is to understand each public contract, follow the success path, identify stopping conditions, and know which test would expose a defect.

## Source-reading method

For every module, use this order:

```text
module docstring
→ public records and result types
→ public functions or methods
→ main success path
→ failure or abstention paths
→ helper syntax
→ matching tests
```

After each module, complete:

```text
This module owns:
Its main input is:
Its trusted output is:
It raises an exception when:
It returns a bounded result when:
A defect here would appear as:
```

# 1. `cli.py` — orchestration, not domain reasoning

## What this module owns

`cli.py` owns:

- command-line input;
- construction of the focused clients;
- execution order;
- conversion of exceptions into exit codes;
- terminal presentation.

It deliberately does not own GitHub JSON parsing, dependency interpretation, workflow parsing, or CI-authority rules.

## Start with the module docstring

The docstring states the architectural intent: the CLI connects focused stages while keeping each stage independently readable and testable.

That means a growing `main()` is acceptable only while it remains orchestration. A dependency regex, GitHub response parser, or CI-authority rule placed here would violate the boundary.

## `build_parser()`

Important shape:

```python
def build_parser() -> argparse.ArgumentParser:
```

Practical meaning:

- no network request occurs;
- the parser can be created and tested independently;
- the supported public input is explicit: `owner/repository` plus a PR number.

You only need operational understanding of `argparse`. You must master the input contract.

## `main(argv: Sequence[str] | None = None) -> int`

The signature communicates three useful facts:

- `argv` may be supplied by tests or omitted for normal shell use;
- `Sequence[str]` accepts list-like argument collections without requiring a mutable list;
- the integer return value is the shell exit status.

### Client construction

```python
token = os.getenv("GITHUB_TOKEN")
pull_client = GitHubReadClient(token=token)
actions_client = GitHubActionsClient(token=token)
repository_client = GitHubRepositoryClient(token=token)
```

Mental model:

```text
one optional credential
→ three focused read-only clients
→ shared HTTP behavior through GitHubApiClient
```

Why three clients instead of one giant GitHub client?

- PR and changed-file evidence have one responsibility;
- Actions runs/jobs have another;
- exact-revision repository files have another;
- each boundary can evolve and be tested separately.

### Main acquisition and interpretation sequence

Read these statements as the product pipeline:

```python
pull_request = pull_client.get_pull_request(...)
changed_files = pull_client.get_changed_files(pull_request)
dependency_result = extract_pinned_dependency_change(changed_files)
```

Then, only for a supported dependency:

```python
if isinstance(dependency_result, PinnedDependencyChange):
```

This branch is important. It prevents later CI work from using an unproven dependency identity.

`isinstance(...)` is not merely syntax here. It is runtime narrowing of a union result:

```text
PinnedDependencyChange
or
UnsupportedDependencyChange
```

### Workflow evidence construction

```python
workflow_evidence = tuple(
    (run, actions_client.get_workflow_jobs(pull_request, run))
    for run in workflow_runs
)
```

Read it as:

```text
for every validated run
→ acquire that run's jobs
→ preserve run and jobs together
→ freeze the final collection as a tuple
```

You do not need to reproduce this comprehension from memory. You must understand why jobs remain attached to their run.

### Authority input construction

```python
WorkflowAuthorityInput(
    run=run,
    jobs=jobs,
    definition=repository_client.get_exact_head_workflow_file(
        pull_request, run
    ),
)
```

This assembles three evidence domains for one workflow:

```text
runtime run record
+ runtime job records
+ exact-head workflow definition
```

The evaluator receives already acquired evidence and performs no network I/O. This is a key acquisition-versus-interpretation boundary.

### Exception mapping

The three categories are intentionally different:

```python
except UpgradePilotInputError:
    return 2
except GitHubAcquisitionError:
    return 3
except GitHubResponseError:
    return 4
```

You must master the meaning:

- exit `2`: local input is unsupported;
- exit `3`: no usable GitHub response was obtained or GitHub refused it;
- exit `4`: GitHub returned a success response, but the evidence was malformed or contradictory.

Do not collapse them into one generic error.

### `assert authority_result is not None`

The assertion documents an internal invariant:

```text
supported dependency branch
→ authority evaluation must have occurred
```

It is not input validation. It is a programmer-facing consistency check after control flow has already established the condition.

## What to master in `cli.py`

Must master:

- execution order;
- why CI acquisition is conditional;
- exception-to-exit-code mapping;
- why presentation comes after successful orchestration;
- which module owns each stage.

Operationally understand:

- `argparse` syntax;
- tuple comprehensions;
- `Sequence[str] | None`;
- `assert` as an internal invariant.

## Matching source exercise

Without notes, point to the exact statement where:

1. dependency interpretation begins;
2. unsupported dependency evidence stops CI acquisition;
3. workflow definition acquisition occurs;
4. CI authority is evaluated;
5. a malformed successful GitHub response becomes exit code `4`.

# 2. `github_api.py` — shared HTTP and JSON trust boundary

## What this module owns

This module knows how to:

```text
send one read-only GitHub request
→ classify transport and HTTP outcomes
→ decode JSON
→ require top-level and field-level runtime types
```

It intentionally does not know what a pull request, workflow, or changed file means.

## Two exception classes

### `GitHubAcquisitionError`

Used when UpgradePilot cannot obtain a usable response:

- timeout;
- transport failure;
- `404` absence/access ambiguity;
- `403` or `429` refusal/rate limit;
- other non-success HTTP status.

The stable `reason` field is part of the product contract. Human message text can evolve; downstream logic should rely on bounded reason categories.

### `GitHubResponseError`

Used when GitHub returned a success status but the payload cannot be trusted.

Examples:

- JSON has the wrong top-level shape;
- a required field is missing;
- a field has the wrong runtime type;
- later identity checks contradict the request.

Central rule:

```text
HTTP success does not equal evidence success.
```

## `GitHubApiClient.__init__`

```python
def __init__(
    self,
    *,
    token: str | None = None,
    session: Session | None = None,
    timeout: tuple[float, float] = DEFAULT_TIMEOUT,
) -> None:
```

Important syntax and meaning:

- `*` makes following arguments keyword-only, reducing accidental argument-order mistakes;
- optional `session` enables deterministic tests to inject a mock;
- optional `token` adds authorization without requiring it for public requests;
- timeout is stored once and shared by subclasses.

You should be able to explain dependency injection here. You do not need to memorize Requests' internal classes.

## `_get()`

The main mechanism is:

```python
response = self._session.get(url, **kwargs)
```

Before that, the code constructs headers, timeout, and optional query parameters.

Then it classifies failures:

```python
except Timeout:
    reason="timeout"
except RequestException:
    reason="transport_error"
```

After a response exists:

```python
self._raise_for_status(response, resource=resource)
```

The separation matters:

```text
exception before usable HTTP response
versus
HTTP response with non-success status
```

## `_raise_for_status()`

This method intentionally preserves GitHub's ambiguous `404` behavior:

```text
not found
or
not accessible
```

UpgradePilot does not invent which interpretation is true.

`403` and `429` share a bounded category because both prevent reliable acquisition at this stage.

## `_read_json()` and top-level shape helpers

```python
_get_json_object(...)
_get_json_array(...)
```

These helpers prevent focused modules from repeating the same top-level checks.

They do not validate domain meaning. For example, object-shaped PR JSON can still contain the wrong PR number or wrong field types.

## Field validators

Examples:

```python
required_str(data, "title")
required_positive_int(data, "id")
required_bool(data, "merged")
```

These perform runtime validation because type hints do not validate external JSON.

Important detail:

```python
if isinstance(value, bool) or not isinstance(value, int):
```

Python treats `bool` as a subclass of `int`. The explicit boolean rejection prevents `True` from being accepted as integer `1`.

## What to master in `github_api.py`

Must master:

- acquisition error versus response-evidence error;
- why external JSON needs runtime validation;
- why a mockable session is injected;
- why shared transport code is separated from domain parsing.

Operationally understand:

- Requests session syntax;
- `**kwargs`;
- static methods;
- `Mapping[str, Any]`;
- keyword-only arguments.

## Matching test reading

In `tests/test_github_client.py`, locate the mocked `404` behavior. Explain why its expected reason is `not_found_or_inaccessible`, not simply `not_found`.

# 3. `github_client.py` — exact proposal identity and complete changed files

## Public records

### `PullRequestIdentity`

This immutable record freezes:

- repository and PR number;
- base ref and base SHA;
- head ref and head SHA;
- changed-file count;
- basic PR metadata.

The most important fields are the SHAs. Branch names can move; a commit SHA identifies one exact revision.

### `ChangedFile`

`patch: str | None` is deliberately optional. A changed-file response may be structurally valid while patch text is absent. That absence is preserved for the interpretation layer.

## `get_pull_request()`

The method performs four conceptual steps:

```text
validate local locator
→ build GitHub API path
→ acquire object-shaped JSON
→ parse exact immutable identity
```

The returned PR number is compared with the requested number. A server response that points to a different PR is contradictory evidence, even if every field has a valid type.

## `get_changed_files()`

Central invariant:

```text
acquired record count == PullRequestIdentity.changed_files
```

The loop:

```python
while len(records) < identity.changed_files:
```

means the first successful page is not assumed complete.

The code stops when:

- expected records have been collected;
- GitHub returns an empty page;
- a page contains fewer than the maximum page size.

After stopping, exact count reconciliation decides whether evidence is complete.

Why not silently continue with fewer records?

Because dependency extraction over an incomplete file set could select a false single dependency change while hidden files contain additional changes.

## Parsing helpers

`_parse_pull_request()` and `_parse_changed_file()` convert untrusted dictionaries into immutable records.

They use the shared validators but still enforce domain-specific identity:

- returned PR number must match requested number;
- patch must be text or absent;
- numeric counts must be non-negative.

## Local input validation

`validate_repository()` supports one bounded `owner/repository` grammar.

`validate_pull_number()` explicitly rejects booleans and non-positive integers.

These errors occur before network acquisition and therefore use `UpgradePilotInputError`.

## What to master in `github_client.py`

Must master:

- why exact head SHA is the proposal identity;
- why pagination is correctness, not optimization;
- why acquired files must reconcile with PR metadata;
- why missing patch text remains a valid record;
- local input error versus remote acquisition failure.

Operationally understand:

- frozen dataclasses;
- regex-based locator validation;
- list accumulation and tuple return;
- static parsing methods.

## Matching tests

Read these tests beside the method:

```text
test_get_pull_request_builds_exact_identity
test_get_changed_files_acquires_all_pages
test_get_changed_files_rejects_count_disagreement
test_get_changed_files_rejects_non_array_success
```

For each test, state the one invariant it protects.

# 4. `dependency_change.py` — deterministic interpretation and abstention

## Why this module has no network code

It receives already validated `ChangedFile` records and answers:

```text
Does this evidence prove exactly one supported package==old → package==new update?
```

Keeping it pure makes tests deterministic and keeps network failures separate from interpretation results.

## Result union

```python
type DependencyChangeResult = (
    PinnedDependencyChange | UnsupportedDependencyChange
)
```

This is a design statement: valid GitHub evidence does not guarantee a supported dependency result.

`UnsupportedDependencyChange` is a normal abstention result, not a generic exception.

## Exact-pin grammar

The regex recognizes a complete line shaped like:

```text
package==version
```

`fullmatch` matters because it refuses a valid-looking fragment inside richer syntax.

You do not need to memorize the regex. You should be able to identify:

- package capture group;
- version capture group;
- why start/end anchoring exists;
- why `fullmatch` is stricter than `search`.

## Collection before interpretation

The function first collects all removed and added exact-pin candidates:

```python
removed: list[_PinnedRequirementLine] = []
added: list[_PinnedRequirementLine] = []
```

This avoids deciding too early. Only after scanning the complete evidence does it ask whether the result is unambiguous.

## Patch completeness check

The code counts visible `+` and `-` content lines and compares them with GitHub's per-file totals.

This protects against a truncated patch that appears simpler than the real file change.

Important distinction:

- malformed GitHub schema → exception in acquisition layer;
- structurally valid but incomplete patch → unsupported interpretation result.

## Ambiguity and pairing rules

The first supported boundary requires:

- exactly one removed exact pin;
- exactly one added exact pin;
- both in the same modified file;
- normalized package identity is the same;
- version actually changes.

Any violation returns a stable reason rather than selecting a candidate heuristically.

## Package normalization

```python
return _NORMALIZED_PACKAGE_SEPARATOR.sub("-", package).lower()
```

Practical meaning:

```text
demo.package
demo_package
demo-package
```

all compare as:

```text
demo-package
```

This supports identity comparison only. It does not contact a package registry or prove the package exists.

## What to master in `dependency_change.py`

Must master:

- supported result versus unsupported abstention;
- complete evidence before interpretation;
- why ambiguity is preserved;
- same-file and same-normalized-package invariants;
- why exact-pin support is intentionally narrow.

Operationally understand:

- regex mechanics;
- internal dataclass `_PinnedRequirementLine`;
- list collection;
- union type narrowing;
- normalization regex.

## Matching tests

Read:

```text
test_extracts_supported_exact_pinned_change
test_missing_patch_is_explicitly_unsupported
test_patch_count_disagreement_is_incomplete_evidence
test_multiple_pinned_changes_are_ambiguous
test_different_package_names_are_unsupported
test_range_change_is_outside_exact_pin_support
```

For each, answer:

```text
Why is this an exception or a result?
Which invariant would be unsafe to ignore?
```

# Core walkthrough completion check

You pass this file when, without notes, you can explain:

1. how `main()` sequences acquisition and interpretation;
2. why three GitHub clients share one HTTP superclass;
3. why `200 OK` may still fail evidence validation;
4. why head SHA is stronger than branch name;
5. why changed-file pagination is required for correctness;
6. why missing patch evidence becomes unsupported instead of acquisition failure;
7. why dependency ambiguity is never guessed away;
8. which four source modules you would inspect for a wrong dependency result.

Then proceed to `09-guided-source-walkthrough-ci.md`.