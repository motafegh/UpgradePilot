# 05 — Code and Syntax You Must Own

## SMART objective

Within 30–40 minutes, classify current Python constructs by learning depth, explain the central constructs in plain language, and make one small safe test or rule modification with AI assistance.

## AI-era standard

You are not training to type every implementation from memory.

You are training to:

- specify correct behavior;
- understand the generated structure;
- challenge unsafe assumptions;
- inspect contracts and invariants;
- modify a central rule or test;
- diagnose failures;
- explain claims and limits.

Syntax matters when it enables those capabilities. Syntax memorization without reasoning is not the goal.

## Must master now

### Function contract

For a central function, know:

- what inputs it accepts;
- what output states it can return;
- what exceptions it can raise;
- what invariants it enforces;
- what it intentionally refuses to infer.

Examples:

- `get_pull_request(...)` returns exact proposal identity;
- `extract_pinned_dependency_change(...)` returns supported or unsupported interpretation;
- `evaluate_ci_authority(...)` returns sufficient, insufficient, or unresolved authority.

### Dataclass records

Pattern:

```python
@dataclass(frozen=True, slots=True)
class PullRequestIdentity:
    repository: str
    number: int
    head_sha: str
```

Practical meaning:

- `@dataclass` generates routine record behavior;
- `frozen=True` prevents normal field reassignment after construction;
- `slots=True` fixes the expected attribute set and avoids arbitrary new attributes;
- annotations describe the intended field types.

Why this matters:

The record is a validated handoff contract. Later modules should not mutate proposal identity.

You do not need to memorize every dataclass option.

### Union result types

Examples:

```python
type DependencyChangeResult = (
    PinnedDependencyChange | UnsupportedDependencyChange
)
```

Practical meaning:

A valid call can produce more than one normal result shape. The caller must handle both rather than assuming success.

You must understand why unsupported/unresolved is part of the contract.

### `isinstance` narrowing

Example:

```python
if isinstance(result, PinnedDependencyChange):
    ...
else:
    ...
```

Practical meaning:

The code identifies which result variant it received before accessing variant-specific fields.

This is central because later acquisition should activate only for a supported dependency identity.

### Immutable tuples

Validated collections are returned as tuples:

```python
return tuple(records)
```

Why:

- callers cannot append or remove evidence in place;
- the validated collection shape is more stable;
- the type signals that the function has completed collection.

Immutability does not make the evidence universally correct; it prevents accidental local mutation.

### Exceptions versus normal result states

Use exceptions for:

- rejected input;
- acquisition failure;
- malformed or contradictory successful response.

Use normal result objects for:

- unsupported dependency grammar;
- insufficient authority;
- unresolved authority.

You must be able to challenge code that throws an exception merely because evidence is unsupported.

### Loop and pagination invariants

Understand patterns such as:

```python
while expected_total is None or len(records) < expected_total:
    ...
```

The important skill is not reproducing the exact loop from memory. It is proving:

- what causes another page request;
- what proves completion;
- what stops an infinite or partial loop;
- what happens if totals disagree.

### Regular expressions at the rule level

You should understand:

- `fullmatch` requires the whole string to match;
- capturing groups recover package/version values;
- normalization regex collapses `.`, `_`, and `-` runs;
- command regexes recognize a narrow supported grammar.

You do not need to write the complex patterns without assistance.

Your ownership requirement is to test whether the pattern is too broad or too narrow.

## Operationally understand

### Imports

Know the difference between:

```python
from .github_api import GitHubResponseError
```

and importing an entire module. Understand relative import purpose inside the package.

### Type annotations

Recognize:

- `str | None` as nullable text;
- `tuple[WorkflowJob, ...]` as any-length immutable job tuple;
- `Sequence[T]` as read-oriented sequence input;
- `Mapping[str, Any]` as dictionary-like untrusted JSON object;
- `Literal[...]` as a bounded set of string states.

You do not need to master Python's entire typing system now.

### Static and private methods

- `@staticmethod` indicates behavior that does not use instance state;
- a leading underscore marks an internal implementation detail by convention.

These are design signals, not security boundaries.

### `try` / `except` with exception translation

Pattern:

```python
try:
    value = data["field"]
except KeyError as exc:
    raise GitHubResponseError(...) from exc
```

Practical meaning:

A low-level Python failure becomes a product-specific evidence error while preserving the original cause.

### Mocked collaborators

Recognize:

- `Mock()` creates a controlled substitute;
- `return_value` controls one call result;
- `side_effect` controls successive responses or raises an error;
- `call_args` and `call_args_list` inspect how the collaborator was used.

You should be able to modify a fixture and predict the resulting behavior.

## Introduced, not mastered

- base64 decoding details;
- shell command tokenization edge cases;
- YAML block syntax beyond current supported forms;
- Requests connection reuse;
- Python packaging build backend behavior.

Know where these appear and why, but do not spend the session studying internals.

## Deferred deliberately

- advanced metaprogramming;
- descriptors and custom object models;
- async I/O;
- complete typing theory;
- parser generators;
- full YAML specification;
- dependency-injection frameworks;
- performance micro-optimization.

## How to read AI-written code

Use this order:

1. Read the module docstring: what question does the file answer?
2. Read public records: what data crosses boundaries?
3. Read public functions/methods: what is the contract?
4. Read early returns: where does the function stop?
5. Read invariant checks: what unsafe state is rejected?
6. Read tests: what behavior is actually protected?
7. Only then inspect helpers and syntax details.

Do not begin by reading every line from top to bottom equally.

## Required ownership modification

Choose one bounded task tomorrow.

Recommended task:

```text
Add the deferred normalized-package identity test:
removed: demo.package==1.0.0
added:   demo_package==1.1.0
expected normalized package: demo-package
```

Before editing:

- predict supported or unsupported;
- identify the responsible module and test file;
- explain which rule protects the result.

After editing:

- run the complete suite;
- explain what a failure would localize;
- distinguish “test passes” from “I independently own the whole module.”

Alternative ownership task:

Add a focused CI-authority test where the install command uses:

```text
pip install --requirement=requirements-dev.txt
```

Predict whether the current command reader supports it before running.

## Red flags when reviewing AI output

Stop and challenge the change if it:

- uses branch name instead of exact SHA;
- treats missing evidence as success;
- combines commands across jobs without proving shared state;
- converts unresolved evidence into insufficient or sufficient without justification;
- places interpretation logic in transport code;
- catches every exception and returns a generic result;
- adds a framework before a concrete responsibility requires it;
- changes tests to match incorrect implementation rather than fixing the rule;
- prints a stronger claim than the result object establishes.

## Completion evidence

This file is mastered when you can explain the constructs above, review a generated change using the red flags, and complete one predicted central modification with a diagnosis explanation.