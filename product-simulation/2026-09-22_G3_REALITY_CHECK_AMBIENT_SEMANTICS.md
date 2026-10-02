# G3 — Real-world reality check: ambient package-manager semantics

**Date:** 2026-09-22
**Kind:** Non-controlling Product Simulation research.

## Purpose

Test whether package-manager semantic counterexamples discussed by the main workstream actually occur in public CI, and separate real implementation pressure from theoretical-only pressure.

## Bounded discovery snapshot

GitHub public code search under `.github/workflows` produced these exact-string snapshots:

| Search family | Matching workflow files |
| --- | ---: |
| `PIP_DRY_RUN` | 0 |
| `PIP_TARGET` | 9 |
| `PIP_CONSTRAINT` | 614 |
| `UV_CONSTRAINT` | 108 |
| `UV_NO_SYNC` | 812 |
| `PIP_DRY_RUN` + `GITHUB_ENV` in YAML | 0 |
| `PIP_CONSTRAINT` + `GITHUB_ENV` in YAML | 166 |

These are discovery counts, not prevalence estimates. Index coverage, forks/mirrors, syntax variation, default-branch state, and repository support boundaries all limit them. Co-occurrence in one file also does not establish a propagation relationship.

Immediate reality check: the exact `PIP_DRY_RUN` examples used in B4 have not appeared in this bounded search, while constraints and no-sync semantics are plainly present in real workflows. Product complexity should therefore be prioritized by observed evidence rather than treating every constructible variable equally.

## Strong real case — LangChain Dependabot #40646

- Repository: `langchain-ai/langchain`
- PR: `#40646`, Dependabot, `anyio 4.14.2 → 4.15.1` in `/libs/standard-tests`
- Head: `3908f2baf0db73c0f3242107df0428a510f4be47`
- Changed source: `libs/standard-tests/uv.lock`
- Head CI run: `35378301060` (`🔧 CI`), success

The exact patch changes the locked anyio version and artifacts to 4.15.1.

The exact-head primary workflow and reusable unit-test workflow both declare `UV_FROZEN=true` and `UV_NO_SYNC=true`.

The selected `libs/standard-tests` unit-test sequence is:

`setup uv → uv sync --group test --dev → make test → uv run --group test pytest ...`

Runtime job `105708268180` (Python 3.14) shows the inherited `UV_NO_SYNC=true`, then executes `uv sync --group test --dev`, reports `Installed 48 packages`, and logs `anyio==4.15.1`. The later test step still has `UV_NO_SYNC=true`, executes `uv run --group test pytest ...`, and pytest reports the `anyio-4.15.1` plugin. Python 3.10 job `105708268228` shows the same shape.

### Discriminating finding

`UV_NO_SYNC is visible` does **not** imply `the relevant environment was never synchronized`.

The setting is operation- and sequence-relative. The later `uv run` does not synchronize the environment, but an earlier explicit successful `uv sync` has already formed it. A global rule that treats any visible `UV_NO_SYNC` as a universal state-proof defeater would therefore be too strong.

Conversely, the later `uv run` must not be credited with the earlier sync. The useful proof chain is temporal: earlier state-forming operation → installed/result evidence → later no-sync execution using that formed environment.

This is broader than command-local B4 semantics and may matter to later evidence composition.

## Real shell-local semantic input — NVIDIA cuda-python

At public revision `1db44ecd79dbddc3c5d81e9e4620782f8bda93f5`, `.github/workflows/coverage.yml` contains steps that export `PIP_BUILD_CONSTRAINT` and `PIP_CONSTRAINT` inside a shell step before later `pip wheel` / `pip install` commands.

This is a real example where effective package-manager semantics depend on ordered shell-local state, not only workflow/job/step `env:`. It also intersects G1: enclosing-step success does not automatically prove arbitrary later internal command occurrences under the current runtime-strengthening contract.

The same file has unrelated `GITHUB_ENV` writes. Therefore raw co-occurrence search would be misleading if interpreted as `PIP_CONSTRAINT` propagation through `GITHUB_ENV`; exact relationship inspection is required.

## Other real controls

- MLflow `.github/workflows/r.yml`: workflow-level `PIP_CONSTRAINT`.
- napari benchmark workflow: step-level `PIP_CONSTRAINT`.
- Pydantic CI: selected steps use `UV_NO_SYNC=1` after explicit environment-formation work.

These confirm literal workflow/job/step environment declarations are a real evidence source class, while not proving complete effective process configuration.

## Current conclusion

The real-world evidence does not support treating ambient package-manager semantics as one uniformly severe problem. Constraints and no-sync are clearly real; exact `PIP_DRY_RUN` workflow pressure was not observed in this bounded search; arbitrary hidden propagation must be proved relationship-by-relationship.

LangChain #40646 is a strong candidate for scenario promotion because it is an untouched public Dependabot uv proposal with exact source/workflow/run evidence and it directly prevents an over-broad fail-closed interpretation. No scenario number is assigned yet.
## Sharper GITHUB_ENV reality check

A second bounded search looked specifically for assignment-like package-manager variables in files that also reference `GITHUB_ENV`. File-level co-occurrence still required exact inspection.

### Confirmed real PIP_CONSTRAINT propagation

LocalStack CLI at public revision `b169c51b72baa0eed7acf041ed0d676f20cee93f` contains a macOS-Intel-only step:

`echo "PIP_CONSTRAINT=$RUNNER_TEMP/constraints.txt" >> "$GITHUB_ENV"`

The following `Create virtual environment` step runs `make clean-venv venv`. This is a current real example of a package-manager semantic input being written through GitHub's environment-file mechanism for later-step use. It validates the *class* of B4 propagation concern, although this artifact has not yet traced the downstream Makefile/pip process far enough to claim the exact final value received by pip.

A historical but very explicit example also exists in `quantopian/trading_calendars`: a `Set Lockfile` step writes `PIP_CONSTRAINT=etc/${{matrix.requirements_file}}` to `GITHUB_ENV`, followed by `pip install -e .[dev]` in a later step.

### Confirmed real UV_NO_SYNC propagation

`maksimzayats/diwire` at revision `d86e4d1f05f767ceeef073b4625f3cea59a74bb3` conditionally runs an explicit `uv sync` for Python 3.15t and then writes `UV_NO_SYNC=1` to `GITHUB_ENV`. Subsequent steps use `uv run` for tooling/tests. This is a direct real instance of the pattern `state-forming sync → later propagated no-sync baseline → later uv run`.

### Negative boundary still useful

The corresponding exact search for `PIP_DRY_RUN=` plus `>> $GITHUB_ENV` returned zero matches in this bounded snapshot. That does not prove the shape never exists; it does mean the current B4 dry-run example has weaker incidence evidence than the constraint/no-sync families.

### Updated reality conclusion

The B4 *mechanism* is not merely synthetic: real workflows do propagate package-manager controls through `GITHUB_ENV`. But the important variables and usage patterns are uneven. Research should therefore prioritize the observed families and keep rare/unobserved examples as lower-confidence pressure until stronger evidence appears.
## Re-sync pressure — latest main B4 multiple-write and step-env override cases

Main subsequently added two more B4 design cases:

1. multiple proven `GITHUB_ENV` writes to the same variable, where the later write should become the later-step baseline;
2. a later step-local `env:` value overriding an inherited `GITHUB_ENV` baseline before exact-process semantics are considered.

These data-flow rules are logically coherent. Product Simulation then performed a bounded reality check rather than assuming their incidence.

### Same-variable multiple-write screening

A sample of mature/public `PIP_CONSTRAINT` + `GITHUB_ENV` workflow hits was inspected exactly.

- LocalStack CLI: one `PIP_CONSTRAINT` write to `GITHUB_ENV` in the inspected workflow.
- trading_calendars: one `PIP_CONSTRAINT` write, then later pip install.
- WMCore: one `PIP_CONSTRAINT` write in the inspected build workflow.
- Quri SDK search hits were shell-local `PIP_CONSTRAINT=... pip install ...`, not repeated `GITHUB_ENV` writes.
- PassageMath uses constraint values inside cibuildwheel environment configuration, not the synthetic two-write pattern.

No selected case in this bounded sample exhibited `same package-manager variable written twice to GITHUB_ENV before one consumer`.

### Step-env collision screening

File-level searches for package-manager variables plus `GITHUB_ENV` returned many hits, but exact inspection again showed why co-occurrence is not relationship evidence:

- MLflow has workflow-level `PIP_CONSTRAINT`, while its `GITHUB_ENV` write updates `USE_R_DEVEL`, not `PIP_CONSTRAINT`.
- msgspec has job-level `UV_NO_SYNC=true`, while its `GITHUB_ENV` write sets `UV_PYTHON`, not `UV_NO_SYNC`.
- deepagents has workflow-level `UV_NO_SYNC=true`, while its `GITHUB_ENV` mutations build `PYTEST_ADDOPTS`, not `UV_NO_SYNC`.

No selected case established the exact synthetic collision `GITHUB_ENV writes package-manager variable X → later step-local env overrides the same X`.

### Empirical disposition

At this bounded depth:

- single package-manager `GITHUB_ENV` propagation: **observed-real**;
- shell-local package-manager overrides: **observed-real**;
- workflow/job/step literal package-manager env: **observed-real**;
- same-variable multiple `GITHUB_ENV` writes before one package-manager consumer: **plausible-unobserved** in the inspected sample;
- same-variable `GITHUB_ENV` baseline then step-local override: **plausible-unobserved** in the inspected sample;
- `PIP_DRY_RUN` workflow/GITHUB_ENV examples: **plausible-unobserved** in the bounded exact-string search.

This does not invalidate the main B4 correctness rules. It changes their empirical priority: preserve correctness/fail-closed behavior where cheap, but do not let currently synthetic-only conflict shapes automatically justify a broad data-flow subsystem.