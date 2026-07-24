# B2 Public PR Vertical Slice Plan

**Status:** Active  
**Owner:** Ali Rajabi  
**Parent route:** [`UPGRADEPILOT_90_DAY_PLAN.md`](UPGRADEPILOT_90_DAY_PLAN.md)  
**Technical evidence:** [`../working-memory/B2_TECHNICAL_PROGRESS.md`](../working-memory/B2_TECHNICAL_PROGRESS.md)

## Purpose

Build and understand the smallest credible real UpgradePilot path:

```text
public repository + Dependabot PR number
→ exact proposal and dependency identity
→ relevant exact-head CI and package/upstream evidence
→ bounded recommendation or honest abstention
→ concise traceable output
```

This is a lightweight implementation checklist, not a second roadmap.

## Working rule

Each increment follows one real responsibility, deterministic tests, a safe real example where applicable, explicit limitations, and a clear stop boundary. Learning and ownership work may be deferred only by Ali's explicit instruction; deferral is not completion.

## Progress checklist

- [x] Accept `owner/repository` and PR number through one command.
- [x] Acquire and validate exact public PR identity.
- [x] Acquire and reconcile all changed-file records.
- [x] Identify one supported exact pinned Python dependency update.
- [x] Preserve explicit unsupported dependency-change states.
- [x] Acquire exact-head `pull_request` workflow runs, jobs, and step summaries.
- [x] Validate the Actions increment in Ali's WSL2 environment with 18 tests and the live S004 command.
- [ ] **Current:** validate the first bounded CI-authority evaluator locally and against S004.
- [ ] Extend indirect CI tracing only where the first rule leaves a material blocker.
- [ ] Acquire the minimum public package or upstream evidence required by the supported case.
- [ ] Produce the first bounded recommendation or honest abstention.
- [ ] Keep human output consistent with minimum machine-readable state.
- [ ] Add captured-response or normalized-evidence tests for deterministic reruns.
- [ ] Complete at least one Ali-owned central modification, meaningful test, and diagnosis.

## Current increment — Direct exact-head CI authority

### Responsibility

```text
validated exact-head workflow run
→ exact-run workflow path
→ workflow text at the same head SHA
→ commands in one statically identifiable job
→ changed requirements file installation
→ changed package direct invocation
→ sufficient, insufficient, or unresolved authority
```

### Source separation

```text
github_repository.py   workflow path and exact-head text acquisition
workflow_commands.py   shallow jobs/run command extraction
ci_authority.py        authority outcomes and reasons
cli.py                 orchestration and presentation
```

This separation follows engineering responsibilities. It avoids adding workflow interpretation to the Actions acquisition module.

### Supported first rule

Authority is **sufficient** when one successful exact-head workflow has one statically readable job and its commands both:

- install the exact changed dependency source file through a pip requirement flag; and
- directly invoke the changed package as a command or Python module.

Authority is **insufficient** when no completed successful exact-head job exists.

Authority is **unresolved** when successful CI exists but the current evidence cannot prove direct exercise, including:

- tox or another indirection without config tracing;
- multiple jobs where cross-job combination would be unsafe;
- reusable workflows, scripts, richer YAML, or package-command aliases;
- unavailable exact-head workflow text.

### Expected S004 behavior

- `Regression Tests` should be sufficient because its single job installs `requirements-dev.txt` and directly runs `pytest`.
- `Test + Deploy` should remain unresolved because `tox -e py` requires later configuration tracing.
- One sufficient workflow makes the overall CI-authority result sufficient, while preserving the unresolved second workflow.

### Prepared tests

New deterministic tests cover:

- workflow run-detail identity and exact-head file decoding;
- explicit unavailable workflow text;
- named-step and direct-list-item `run` command extraction;
- sufficient direct install-and-invoke evidence;
- tox-only unresolved behavior;
- multi-job non-combination;
- no-successful-job insufficiency.

The complete suite now contains 28 test methods. Execution is intentionally left to Ali.

### Validation command

```bash
git pull --ff-only origin main
source .venv/bin/activate
python3 -m pip install -e .
python3 -m unittest discover -s tests -v
python3 -m upgradepilot googlefonts/glyphsLib 1145
```

### Stop boundary

This increment answers whether at least one bounded exact-head CI path directly exercised the dependency. It does not establish:

- complete test coverage;
- compatibility or upgrade safety;
- a merge or other maintainer recommendation;
- package/upstream evidence;
- indirect tox/script authority beyond the current rule.

## Deferred ownership gate

The normalized-package identity exercise remains explicitly deferred and unpassed.

## Plan maintenance

Update this checklist only when observable implementation or validation evidence changes. Keep detailed command output and limitations in `working-memory/B2_TECHNICAL_PROGRESS.md`.
