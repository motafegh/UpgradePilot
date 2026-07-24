# UpgradePilot Current Memory

**Last updated:** 2026-07-24  
**Purpose:** Concise project-local continuation. Active source, tests, commands, outputs, and the actual environment remain the authority for implemented behavior.

## Current route

- Controlling route: [`plans/UPGRADEPILOT_90_DAY_PLAN.md`](plans/UPGRADEPILOT_90_DAY_PLAN.md)
- Current bounded plan: [`plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md`](plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md)
- Detailed technical evidence: [`working-memory/B2_TECHNICAL_PROGRESS.md`](working-memory/B2_TECHNICAL_PROGRESS.md)
- Frozen earlier learning snapshot: [`learning/b2-pr-acquisition-and-pinned-extraction/`](learning/b2-pr-acquisition-and-pinned-extraction/)

D1 and B1 are passed. **B2 — Public PR vertical slice is active.**

Ali explicitly deferred the normalized-package ownership exercise on 2026-07-24. It is deferred, not passed, and establishes no ownership or mastery.

## Observed exact-head Actions proof

Ali validated commit `ffe6a899b88b6548d0da2f2fa949276983cccec2` in WSL2 with Python 3.12:

```text
editable installation succeeded
18 deterministic tests passed
live googlefonts/glyphsLib#1145 acquisition succeeded
head SHA: f3cda8a94600e58d27f1bc17c99b7693718b6350
2 exact-head workflow runs acquired
Regression Tests: success, 1 job
Test + Deploy: success, 6 jobs
CI authority: not yet evaluated
```

This proves factual exact-head workflow, job, and step-summary acquisition. It does not by itself prove dependency exercise, upgrade safety, or a maintainer action.

## Current implemented source path

The new source extends the path into the first bounded CI-authority evaluator:

```text
public repository + PR number
→ exact proposal and dependency identity
→ exact-head workflow runs, jobs, and steps
→ exact-run workflow path
→ workflow definition acquired at the same head SHA
→ shallow single-job command reading
→ sufficient, insufficient, or unresolved CI authority
→ transparent terminal reasons and command evidence
```

Responsibility boundaries:

```text
github_api.py          shared read-only HTTP/JSON trust boundary
github_client.py       PR identity and changed files
github_actions.py      workflow runs, jobs, and step summaries
github_repository.py   exact-head workflow-definition acquisition
workflow_commands.py   bounded jobs/run command reading
ci_authority.py        deterministic authority classification
dependency_change.py   dependency interpretation
cli.py                 execution order and presentation
```

No runtime dependency was added. The command reader is intentionally not a complete YAML parser.

## First authority rule

A workflow is sufficient only when:

1. the exact-head workflow run and at least one job completed successfully;
2. the workflow definition has one statically identifiable job;
3. a command installs the exact changed requirements file; and
4. a command directly invokes the changed package.

Tox-only, script-indirect, reusable-workflow, multi-job, unavailable, or richer YAML paths remain unresolved rather than guessed. For S004, the expected direct proof comes from the single-job `Regression Tests` workflow; `Test + Deploy` should remain unresolved because its tox configuration is not traced yet.

## Immediate continuation

Ali should pull and validate the new source:

```bash
git pull --ff-only origin main
source .venv/bin/activate
python3 -m pip install -e .
python3 -m unittest discover -s tests -v
python3 -m upgradepilot googlefonts/glyphsLib 1145
```

Expected new output includes:

```text
CI authority: sufficient|insufficient|unresolved
CI authority reason: <stable reason>
CI authority detail: <bounded explanation>
Authority workflow: <name> | status=<state> | reason=<reason>
Install evidence: <command when found>
Execution evidence: <command when found>
```

The suite now contains 28 deterministic test methods, but that count is not validated until Ali runs it.

## Current boundaries

Do not yet:

- equate sufficient CI authority with upgrade safety or a merge recommendation;
- infer indirect tox/script behavior that the current rule did not trace;
- acquire package/upstream evidence or produce the final decision;
- add PyYAML or broaden parsing without a demonstrated need and approval;
- add persistence, replay infrastructure, services, agents, models, or deployment layers;
- expose GitHub write operations or commit credentials;
- describe the deferred ownership exercise as completed.

## Ownership state

The current source and tests remain substantially AI-authored. Ali's run will establish bounded product evidence, not independent capability. The deferred ownership exercise remains available for later practice.
