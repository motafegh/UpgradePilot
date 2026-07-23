# S005 Candidate Screening — Action-Changing Contrast

**Status:** Selected and complete  
**Date:** 2026-07-23  
**Purpose:** Select the strongest available public Python Dependabot case where repository-specific evidence can change the transparent baseline's broad action or establish a genuine dependency-versus-PR decision divergence.

## Admission criteria

A qualifying case must provide:

- exact public repository, PR, base, head, changed file, dependency, and version identity;
- a transparent-baseline result that can be frozen before final interpretation;
- exact-head CI tied to workflow, job, step, command, dependency identity, and result;
- material evidence hidden from the baseline that can plausibly change the broad action;
- enough upstream and target evidence to map caution signals to concrete repository surfaces;
- a bounded, public-safe investigation and an honest stop or abstention point.

Passing status alone is insufficient. The proposed dependency version must be the version exercised by the relevant checks.

## Screened candidates

### Rejected — `Simon-McIntosh/imas-codex#17`

Update: `mcp` 1.26.0 → 1.28.1.

The upstream notes contain deprecation language whose target relevance could potentially overturn baseline caution. The PR was manually closed without merge, however, and the only public discussion is Dependabot acknowledging an ignore action. No technical, supersession, policy, or unrelated-failure explanation identifies why the PR was closed.

**Reason for rejection:** dependency acceptability and PR action could not be separated causally without inventing the closure reason.

### Rejected — `Bluetooth-Devices/bleak-retry-connector#301`

Update: pytest 9.0.3 → 9.1.1.

The exact lock was installed and pytest passed across Python 3.10–3.14. The repository uses `-Wdefault`, not warnings-as-errors, and the available public interface did not expose a complete warning-free job log. Source searches were favorable but did not make this the strongest available action-changing case.

**Reason for rejection:** clean execution was established, but warning diagnostics and target-surface exclusion were less authoritative than the selected candidate.

### Rejected — `Jc2k/aiohomekit#558`

Update: pytest 8.4.2 → 9.1.1.

The PR had broad multi-platform CI, but the repository did not promote pytest deprecation warnings to errors and a cleaner exact-lock case was available.

### Rejected — `CLARIAH/grlc#577`

Update: pytest 9.0.2 → 9.1.1.

The PR changed one pinned test requirement, but no exact-head workflow run or commit status was available through the public interfaces used for screening.

**Reason for rejection:** current CI authority could not be established.

### Rejected — `tkoyama010/pyvista-wasm#250`

Update: pytest 9.0.3 → 9.1.0.

The repository uses warnings-as-errors and broad CI. The workflow installs tox and tox-uv independently, while `tox.ini` declares `pytest>=7.0`; the test environment is therefore not proven to use the pytest version changed in `uv.lock` or the updated project upper bound.

**Reason for rejection:** green tests did not establish exact proposed dependency identity.

### Rejected — `timhoefer/eRechnung#4`

Update: pytest 9.0.3 → 9.1.1.

The PR changed `requirements-dev.txt`, but the exact-head CI workflow hard-coded `pytest==9.0.3` in its install command.

**Reason for rejection:** the passing tests exercised the old dependency version, not the proposal.

## Selected candidate

### `PennLINC/ModelArrayIO#85`

Update: pytest 9.0.3 → 9.1.1.

Frozen target identity:

- repository: `PennLINC/ModelArrayIO`;
- PR: `#85`;
- base SHA: `915781a6c967f22b9236ecba072300932c2f41f0`;
- head SHA: `b590cfe93fbe49235f0f68d2b87102672f8a0aa0`;
- observed merge commit: `f7f58496507477c7ebaba40921859c18c771c1e4`;
- changed file: `uv.lock`;
- exact mutation: pytest 9.0.3 → 9.1.1, including artifact hashes.

## Why it is the strongest contrast

The transparent baseline sees:

- minor update;
- passing current CI;
- direct test dependency;
- literal caution signals including `breaking`, `removals`, and `deprecations`.

Baseline v0.1 must therefore select B04:

> `run_targeted_checks`

The target-specific evidence hidden from that baseline is unusually strong:

- pytest is a direct `test` extra dependency;
- the PR changes only pytest in `uv.lock`;
- tox's `latest` environments use `uv-venv-lock-runner`, so the exact changed lock determines pytest identity;
- exact-head CI passed those environments on Python 3.11, 3.12, 3.13, and 3.14;
- a separate minimum-dependency environment also passed;
- the official pytest 9.1.1 changelog scopes the breaking behavior to `--doctest-modules` plus inline non-function autouse fixtures;
- the frozen repository does not enable `--doctest-modules`;
- searches found none of the deprecated private APIs, hook markers, pastebin, `console_main`, `yield_fixture`, or teardown `getfixturevalue` use;
- every frozen-head parametrization site inspected uses a concrete list or tuple rather than a deprecated one-shot iterable;
- later default-branch changes modified only workflows and lock data, not source or tests, so current negative code-search results do not hide a deleted frozen-head usage.

## S005 question

> Does exact dependency identity, complete upstream-surface mapping, frozen repository usage, and exact-head lock-backed CI justify changing the baseline action from `run_targeted_checks` to `merge_after_normal_review`?

## Prospective execution rule

The selected identity and restricted baseline must be durably frozen before the final full-case findings and decision are published. Selection-stage observations may identify the candidate, but the baseline artifact must use only its four permitted input families. Full evidence must then establish or reject the action change without forcing the preferred classification.