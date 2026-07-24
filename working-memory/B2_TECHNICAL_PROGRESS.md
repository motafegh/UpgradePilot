# B2 Technical Progress

**Status:** Living technical evidence; non-controlling  
**Current plan:** [`../plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md`](../plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md)

## Current environment

Observed in Ali's environment on 2026-07-24:

```text
Platform: WSL2 / Linux shell
Repository: ~/projects/UpgradePilot
Python: 3.12
Virtual environment: .venv
Install mode: editable
Network scope: public GitHub REST API, read-only
Authentication used for live runs: none
```

## Observed exact-head Actions validation

Ali pulled merge commit `ffe6a899b88b6548d0da2f2fa949276983cccec2`, installed the editable package, and ran:

```text
python3 -m unittest discover -s tests -v
→ 18 tests passed in 0.003s

python3 -m upgradepilot googlefonts/glyphsLib 1145
→ dependency pytest 9.0.2 → 9.0.3
→ exact head f3cda8a94600e58d27f1bc17c99b7693718b6350
→ 2 exact-head workflow runs
```

Observed workflows:

```text
Regression Tests: completed/success, 1 successful job, 12 steps
Test + Deploy: completed/success, 6 jobs
- four successful matrix test jobs
- one successful lint job
- one skipped deploy job
```

This proves read-only exact-head workflow, job, and step-summary acquisition for one real public PR. It does not prove dependency exercise or upgrade safety.

## Current source path

```text
PR locator and metadata
→ changed files and exact pinned dependency
→ exact-head Actions runs/jobs/steps
→ run-specific workflow path
→ workflow text at exact head SHA
→ bounded command evidence
→ CI authority result
```

New source awaiting Ali validation:

```text
src/upgradepilot/github_repository.py
src/upgradepilot/workflow_commands.py
src/upgradepilot/ci_authority.py
updated src/upgradepilot/cli.py
tests/test_github_repository.py
tests/test_ci_authority.py
```

## First CI-authority rule

The evaluator claims sufficient authority only when one completed successful exact-head workflow:

- has one statically identifiable job;
- installs the changed requirements file using pip `-r` or `--requirement`; and
- directly invokes the changed package or Python module.

The evaluator preserves unresolved results for indirect tox/script paths, multiple jobs, unavailable workflow text, richer YAML, and package-command aliases.

Expected S004 interpretation:

```text
Regression Tests → sufficient
Test + Deploy → unresolved (tox config not traced)
overall → sufficient
```

This means at least one successful exact-head CI path directly exercised pytest. It does not mean every workflow exercised it or that the update is safe.

## Immediate technical action

Ali runs:

```bash
git pull --ff-only origin main
source .venv/bin/activate
python3 -m pip install -e .
python3 -m unittest discover -s tests -v
python3 -m upgradepilot googlefonts/glyphsLib 1145
```

Record:

- full test count and any failure;
- workflow-file acquisition failures;
- overall authority status/reason/detail;
- per-workflow authority results;
- printed install and execution commands.

## Boundaries and ownership

No new runtime dependency was admitted. The shallow command reader is not a full YAML parser. The normalized-package ownership exercise remains deferred, not completed. Current source remains substantially AI-authored; local execution is bounded product proof rather than independent capability.
