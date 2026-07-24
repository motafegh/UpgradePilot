# 05 — AI-Era Code Ownership

## SMART objective

In 30–35 minutes, classify current Python constructs by required depth, review one AI-generated change using the red flags below, and prepare one predicted ownership modification.

## What ownership means now

You do not need to type the whole implementation from memory.

You must be able to:

- define the product behavior;
- explain a function's input/output contract;
- identify invariants and stopping conditions;
- challenge unsafe AI assumptions;
- modify one meaningful rule or test;
- run validation and localize a failure;
- state evidence limits accurately.

## Must master now

### Function contracts

For each central function, know:

- accepted input;
- normal result variants;
- exception categories;
- enforced invariant;
- intentionally unsupported meaning.

Examples:

- PR acquisition returns exact proposal identity;
- dependency interpretation returns supported or unsupported;
- CI authority returns sufficient, insufficient, or unresolved.

### Dataclass records

```python
@dataclass(frozen=True, slots=True)
```

Practical meaning:

- `@dataclass` generates routine record behavior;
- `frozen=True` prevents normal field reassignment;
- `slots=True` fixes expected attributes;
- annotations document field types.

These records are validated handoff contracts.

### Union results and narrowing

```python
PinnedDependencyChange | UnsupportedDependencyChange
```

A valid function call may produce more than one normal result shape. Callers must inspect the variant, commonly with `isinstance`, before activating later stages.

### Exceptions versus normal states

Use exceptions for:

- rejected input;
- transport/HTTP acquisition failure;
- malformed or contradictory response.

Use result objects for:

- unsupported dependency evidence;
- insufficient authority;
- unresolved authority.

### Pagination and identity invariants

You need not reproduce loops from memory. You must explain:

- what triggers another page;
- what proves completion;
- what independent count is reconciled;
- what happens when identity or count disagrees.

### Test-backed regular expressions

Know why:

- `fullmatch` requires the whole supported expression;
- capture groups recover values;
- package normalization collapses `.`, `_`, and `-`;
- command patterns intentionally recognize a narrow grammar.

Do not memorize complex regex syntax. Own whether tests show the pattern is too broad or too narrow.

## Operationally understand

- relative imports;
- `str | None`, `tuple[T, ...]`, `Sequence[T]`, `Mapping[str, Any]`, `Literal[...]`;
- `@staticmethod` and underscore-prefixed helpers;
- `try`/`except` exception translation;
- `Mock.return_value`, `Mock.side_effect`, and call inspection;
- base64 decoding and shallow YAML command reading.

## Deferred

Async I/O, complete typing theory, full YAML parsing, parser generators, advanced metaprogramming, dependency-injection frameworks, and performance optimization.

## How to read AI-written code

Use this order:

1. module docstring — which question does this file answer?
2. public records — what crosses the boundary?
3. public functions — what is the contract?
4. early returns — where does processing stop?
5. invariant checks — what unsafe state is rejected?
6. tests — which behavior is protected?
7. helpers — only where needed for understanding or diagnosis.

Do not begin by reading every line equally.

## Review red flags

Challenge an AI change if it:

- uses a branch name instead of exact SHA;
- treats missing evidence as success;
- combines installation and execution across jobs without linkage proof;
- converts unresolved evidence into sufficient/insufficient without justification;
- puts domain interpretation inside transport code;
- catches every exception and hides its category;
- adds a framework before a concrete responsibility requires it;
- changes tests to accommodate a broken invariant;
- prints a stronger claim than the result establishes.

## Recommended ownership task

Before editing, write:

```text
Change:
Expected result:
Responsible test/module:
Protected invariant:
Failure would localize to:
```

Then add the deferred normalized-package test:

```text
-demo.package==1.0.0
+demo_package==1.1.0
```

Expected:

```text
supported change
normalized package: demo-package
```

You may use AI to find the neighboring fixture and review syntax. You must personally decide the expected behavior and assertions.

Run the focused test, then full suite. A pass establishes that this rule is protected; it does not prove independent ownership of every module.

## Alternative task

Test whether this installation form is recognized:

```text
pip install --requirement=requirements-dev.txt
```

Predict the result before running.

## Pass condition

Explain the central constructs, identify all red flags in a proposed change, and complete one predicted meaningful test modification with a failure-localization explanation.