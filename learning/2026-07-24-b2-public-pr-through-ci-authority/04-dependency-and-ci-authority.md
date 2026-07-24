# 04 — Dependency Interpretation and CI Authority

## SMART objective

Within 35–45 minutes, explain the supported dependency grammar, classify six dependency/CI examples, and reconstruct why S004 is sufficient without claiming upgrade safety.

## Dependency interpretation question

After changed-file acquisition succeeds, UpgradePilot asks:

> Do the complete visible patches prove exactly one supported exact pinned Python dependency update?

Current supported form:

```text
package==old_version
→ package==new_version
```

Example:

```text
-pytest==9.0.2
+pytest==9.0.3
```

## Why support is deliberately narrow

Dependency syntax can include:

- compatible-release ranges;
- minimum/maximum ranges;
- extras;
- environment markers;
- direct URLs;
- editable installs;
- VCS references;
- lockfile structures;
- multiple files and generated constraints.

Guessing across these forms would create false dependency identity. The first slice supports one complete form and abstains elsewhere.

## Patch evidence checks

A `ChangedFile` may be structurally valid while its patch evidence is absent or incomplete.

The interpreter checks:

1. patch exists and is non-empty;
2. visible added/deleted line counts agree with GitHub's file totals;
3. exactly one removed exact pin exists;
4. exactly one added exact pin exists;
5. both pins come from the same file;
6. file status is supported;
7. normalized package identities match;
8. versions differ.

Only then does it produce `PinnedDependencyChange`.

## Package-name normalization

Python distribution names compare runs of `.`, `_`, and `-` as equivalent separators under the current PEP 503 normalization rule.

Examples:

```text
demo.package
demo_package
demo-package
```

All normalize to:

```text
demo-package
```

Why preserve both forms?

- raw added spelling is useful for presentation;
- normalized spelling is useful for reliable identity comparison.

Current depth:

- understand and predict normalization;
- inspect or add a test;
- do not memorize the whole packaging specification.

## Unsupported dependency states

Examples:

### No changed files

Reason: nothing exists to interpret.

### Missing patch evidence

Reason: GitHub omitted or did not expose usable patch text.

### Incomplete patch evidence

Reason: visible patch line counts disagree with GitHub's reported totals.

### No supported exact pin

Reason: changes exist, but not in current `package==version` grammar.

### Ambiguous pinned changes

Reason: more than one candidate exists.

### Package mismatch

Reason: removed and added lines identify different normalized distributions.

These are normal bounded outcomes, not crashes.

## CI authority question

After exact dependency identity and exact-head Actions acquisition, UpgradePilot asks:

> Does at least one successful exact-head workflow directly prove that this dependency source was installed and this dependency was invoked?

## The first sufficient rule

One workflow is sufficient only when:

1. workflow run completed successfully;
2. at least one job completed successfully;
3. workflow definition is available at the exact head SHA;
4. workflow contains one statically identifiable job;
5. one command installs the exact changed source file using pip `-r` or `--requirement`;
6. one command directly invokes the changed package or Python module.

For S004:

```text
Install evidence:
. ./generate/bin/activate && pip install -r requirements.txt -r requirements-dev.txt

Execution evidence:
. ./regression/bin/activate && pytest --run-regression-tests tests/regression_test.py -n auto
```

This establishes direct exercise in the successful `Regression Tests` workflow.

## Three authority states

### Sufficient

The current rule directly proves the bounded exercise claim.

It does not mean complete coverage or safety.

### Insufficient

Evidence positively shows the required condition was not met.

Current example:

```text
no completed successful exact-head jobs
```

### Unresolved

Successful or potentially relevant evidence exists, but the current rule cannot prove or disprove exercise safely.

Examples:

- `tox -e py` without reading tox configuration;
- install command in one job and test command in another;
- reusable workflows;
- shell script indirection;
- richer YAML structure;
- unavailable exact-head workflow definition.

“Unresolved” prevents lack of parser capability from being mistaken for negative evidence.

## Why not combine commands across jobs?

Suppose:

```text
job A installs requirements-dev.txt
job B runs pytest
```

Combining them would assume shared environment or artifacts. GitHub Actions jobs normally run in separate environments unless explicit transfer exists.

Therefore cross-job combination would manufacture authority that the evidence does not establish.

## Why one sufficient workflow is enough for the overall result

The current overall claim is existential:

```text
At least one successful exact-head CI path directly exercised the dependency.
```

Therefore:

```text
one sufficient workflow
+ one unresolved workflow
→ overall sufficient
```

The unresolved workflow is retained because overall sufficiency must not erase per-workflow uncertainty.

## Why `Test + Deploy` stays unresolved

The workflow uses multiple jobs and tox indirection.

To claim authority, UpgradePilot would need to trace:

```text
tox command
→ tox configuration
→ environment dependency installation
→ actual pytest command
→ exact job/environment linkage
```

That work is currently unnecessary for S004 because `Regression Tests` already provides sufficient direct evidence.

The correct engineering rule is:

> Extend indirect tracing only when unresolved evidence is a material blocker.

## CI authority versus upgrade safety

CI authority answers:

```text
Was the changed dependency meaningfully exercised by relevant exact-head CI?
```

Upgrade safety requires more:

- package/release existence and metadata;
- supported Python constraints;
- upstream release/change evidence;
- repository-specific risk context;
- baseline comparison;
- known failures or contradictions;
- decision policy.

Therefore:

```text
sufficient CI authority
≠ safe update
≠ merge recommendation
```

## Classification drill

1. `pytest>=9` becomes `pytest>=9.0.3`.
2. Two packages are upgraded in one patch.
3. Exact pytest update exists, but patch counts disagree.
4. Workflow is green and runs only `tox -e py`.
5. Single successful job installs `requirements-dev.txt` and runs pytest.
6. Workflow failed before tests executed.

Expected:

1. unsupported dependency grammar;
2. ambiguous dependency changes;
3. incomplete patch evidence;
4. unresolved CI authority;
5. sufficient CI authority;
6. insufficient CI authority under the first rule.

## What you must master

- why exact pin support is narrow;
- completeness before interpretation;
- package normalization purpose;
- sufficient versus insufficient versus unresolved;
- existential overall authority;
- why CI authority is not recommendation.

## Operationally understand

- regular-expression `fullmatch` purpose;
- diff line markers;
- pip requirement flags;
- direct command/module invocation forms;
- shallow workflow command extraction.

## Deferred

- complete requirements parsing;
- lockfile support;
- complete YAML parsing;
- tox/script/reusable-workflow tracing;
- package and upstream evidence;
- final recommendation policy.

## Completion evidence

This file is mastered when you can explain S004's sufficient result, preserve `Test + Deploy` as unresolved, and reject the leap from green CI to merge safety.