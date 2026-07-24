# UpgradePilot Current Memory

**Last updated:** 2026-07-24  
**Purpose:** Concise project-local continuation. Active source, tests, commands, outputs, and the actual environment remain the authority for implemented behavior.

## Current route

- Controlling route: [`plans/UPGRADEPILOT_90_DAY_PLAN.md`](plans/UPGRADEPILOT_90_DAY_PLAN.md)
- Current bounded plan: [`plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md`](plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md)
- Ordinary learning and execution: [`OPERATING_GUIDE.md`](OPERATING_GUIDE.md)
- Detailed technical evidence and learning depth: [`working-memory/B2_TECHNICAL_PROGRESS.md`](working-memory/B2_TECHNICAL_PROGRESS.md)
- Frozen earlier learning snapshot: [`learning/b2-pr-acquisition-and-pinned-extraction/`](learning/b2-pr-acquisition-and-pinned-extraction/)

D1 is passed, B1 has passed for B2 entry, and **B2 — Public PR vertical slice is active**.

Ali explicitly deferred the normalized-package learning/ownership exercise on 2026-07-24 so implementation could continue. That exercise is **deferred, not passed**, and does not establish ownership or mastery.

## Implemented source path

The active source now extends the real public PR path through exact-head GitHub Actions acquisition:

```text
public repository + PR number
→ read-only PR metadata acquisition
→ exact base/head identity validation
→ paginated changed-file acquisition
→ response and count reconciliation
→ one supported exact pinned Python dependency update
→ exact-head pull_request workflow-run acquisition
→ latest-attempt job and step-summary acquisition
→ concise factual terminal output
```

The GitHub code is separated by responsibility:

```text
github_api.py        shared read-only HTTP/JSON trust boundary
github_client.py     pull-request identity and changed-file acquisition
github_actions.py    exact-head workflow-run, job, and step acquisition
dependency_change.py deterministic dependency interpretation
cli.py               user-visible execution order and output
```

Active source and tests:

```text
pyproject.toml
src/upgradepilot/__init__.py
src/upgradepilot/__main__.py
src/upgradepilot/cli.py
src/upgradepilot/github_api.py
src/upgradepilot/github_client.py
src/upgradepilot/github_actions.py
src/upgradepilot/dependency_change.py
tests/test_github_client.py
tests/test_github_actions.py
tests/test_dependency_change.py
tests/README.md
```

Current runtime dependency remains:

```text
requests>=2.32,<3
```

No framework, model, persistence, service, queue, or additional runtime dependency was added.

## Validation state

Previous observed WSL2 proof remains valid only through dependency identity:

```text
12 deterministic tests passed
live googlefonts/glyphsLib#1145 request succeeded
requirements-dev.txt acquired
pytest 9.0.2 → 9.0.3 extracted
```

For the new exact-head Actions increment, the assistant ran an isolated Python 3.13 deterministic check with `PYTHONPATH=src`:

```text
18 tests passed
syntax compilation passed
```

This is not a substitute for Ali's editable-install and live-network proof. Package installation could not be tested in the assistant environment because its package index was unavailable.

## Immediate continuation

Ali should validate the new increment in WSL2:

```bash
git pull --ff-only origin main
source .venv/bin/activate
python3 -m pip install -e .
python3 -m unittest discover -s tests -v
python3 -m upgradepilot googlefonts/glyphsLib 1145
```

Expected new factual output includes:

```text
Exact-head workflow runs: <count>
Workflow: <name> | status=<status> | conclusion=<conclusion> | jobs=<count>
  Job: <name> | status=<status> | conclusion=<conclusion> | steps=<count>
CI authority: not yet evaluated
```

After the run, inspect whether the exact head SHA is preserved across every workflow and job record. Record the observed commands, outputs, failures, and test count in `working-memory/B2_TECHNICAL_PROGRESS.md`.

## Next product question

After exact-head acquisition is validated, continue to:

```text
workflow/job/step facts
→ inspect workflow definitions and repository commands at the exact head
→ determine whether the changed dependency was installed and exercised
→ CI authority sufficient or insufficient
```

That later increment is interpretation. A green workflow alone must not become a merge recommendation.

## Current boundaries

Do not yet:

- claim that CI exercised the changed dependency;
- claim a dependency recommendation, upgrade safety, or production readiness;
- hardcode S004 or consume an expected decision in runtime logic;
- add upstream, persistence, replay infrastructure, model, service, queue, agent, or deployment layers;
- restore archived M2 source or tests;
- expose GitHub write operations or commit credentials;
- describe the deferred ownership exercise as completed.

## Ownership state

The current source and new Actions tests are substantially AI-authored. Passing tests and a successful live run will establish bounded product evidence, not independent Ali-owned capability. The earlier normalized-package exercise remains available for later ownership practice when Ali chooses to return to it.
