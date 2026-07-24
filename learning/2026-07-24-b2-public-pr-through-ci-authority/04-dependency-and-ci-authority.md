# 04 — Dependency and CI Authority

## SMART objective

In 30–40 minutes, explain the supported dependency rule, distinguish sufficient/insufficient/unresolved authority, and reconstruct S004 without overclaiming safety.

## Supported dependency question

After complete changed-file acquisition:

> Do the visible patches prove exactly one `package==old` to `package==new` Python dependency update?

Supported example:

```text
-pytest==9.0.2
+pytest==9.0.3
```

The rule checks:

1. usable patch exists;
2. visible additions/deletions match GitHub totals;
3. exactly one removed exact pin and one added exact pin exist;
4. both come from the same supported modified file;
5. normalized package identities match;
6. versions differ.

Otherwise it returns an explicit unsupported result.

## Why the grammar is narrow

Real dependency syntax includes ranges, extras, markers, URLs, editable installs, VCS references, lockfiles, and generated constraints. Guessing across these would contaminate every later evidence lookup.

Current principle:

```text
support one complete form
→ abstain elsewhere
→ expand only from demonstrated product need
```

## Python package normalization

Under the current PEP 503 comparison rule:

```text
demo.package
demo_package
demo-package
```

all normalize to `demo-package`.

Raw spelling is retained for presentation; normalized spelling is used for identity comparison.

## CI-authority question

After exact-head runs, jobs, and workflow definitions:

> Does at least one successful exact-head workflow directly prove that the changed dependency source was installed and the dependency was invoked?

## First sufficient rule

A workflow is sufficient only when:

1. exact-head run completed successfully;
2. at least one job completed successfully;
3. exact-head workflow text is available;
4. one job is statically identifiable;
5. a command installs the changed requirements file via pip `-r` or `--requirement`;
6. a command directly invokes the changed package or Python module.

S004 direct evidence:

```text
pip install -r requirements.txt -r requirements-dev.txt
pytest --run-regression-tests tests/regression_test.py -n auto
```

## Authority states

### Sufficient

The current rule proves the bounded exercise claim.

### Insufficient

Evidence establishes that the required condition was not met, for example no completed successful exact-head job.

### Unresolved

Relevant evidence exists, but current rules cannot safely prove or disprove exercise:

- tox without configuration tracing;
- multiple jobs;
- reusable workflows;
- script indirection;
- richer YAML;
- unavailable exact-head workflow text.

Unresolved means “not proven by the current method,” not “CI did not exercise it.”

## Why commands are not combined across jobs

Separate jobs normally run in separate environments. If one installs the dependency and another runs tests, authority requires proof of environment/artifact linkage. Combining them automatically would manufacture evidence.

## Why S004 overall is sufficient

```text
Regression Tests → sufficient
Test + Deploy → unresolved
overall → sufficient
```

The overall claim is existential: at least one CI path exercised the dependency. Per-workflow uncertainty remains visible.

## Why tox tracing is not next

`Test + Deploy` uses tox/multiple jobs, but it is no longer a material blocker because `Regression Tests` already establishes the current authority claim.

Extend indirect tracing only when unresolved evidence blocks a required decision or exposes material risk.

## Authority is not safety

Sufficient CI authority does not establish:

- complete coverage;
- compatibility in all environments;
- package/release legitimacy;
- upstream change risk;
- absence of regressions;
- a merge recommendation.

Next evidence domain: minimum public package and upstream evidence.

## Classification drill

1. `pytest>=9` → `pytest>=9.0.3`.
2. Two exact package updates in one patch.
3. Patch line counts disagree.
4. Green workflow runs only `tox -e py`.
5. Single successful job installs the changed file and runs pytest.
6. No successful exact-head job.

Expected:

1. unsupported grammar;
2. ambiguous change;
3. incomplete patch evidence;
4. unresolved authority;
5. sufficient authority;
6. insufficient authority.

## Must master

- completeness before interpretation;
- narrow support and honest abstention;
- package normalization purpose;
- sufficient versus insufficient versus unresolved;
- existential overall authority;
- authority versus recommendation.

## Operationally understand

`fullmatch`, diff markers, pip requirement flags, direct command invocation, and shallow workflow command extraction.

## Deferred

Complete requirements/YAML parsing, lockfiles, tox/script/reusable-workflow tracing, package/upstream evidence, and decision policy.

## Pass condition

Explain exactly why S004 is sufficient, why `Test + Deploy` remains unresolved, and why neither result authorizes merge.