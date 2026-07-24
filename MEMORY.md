# UpgradePilot Current Memory

**Last updated:** 2026-07-24  
**Purpose:** Concise project-local continuation. Active source, tests, commands, outputs, and the actual environment remain the authority for implemented behavior.

## Current route

- Controlling route: [`plans/UPGRADEPILOT_90_DAY_PLAN.md`](plans/UPGRADEPILOT_90_DAY_PLAN.md)
- Current bounded plan: [`plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md`](plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md)
- Ordinary learning and execution: [`OPERATING_GUIDE.md`](OPERATING_GUIDE.md)
- Detailed technical evidence and learning depth: [`working-memory/B2_TECHNICAL_PROGRESS.md`](working-memory/B2_TECHNICAL_PROGRESS.md)

D1 is passed, B1 has passed for B2 entry, and **B2 — Public PR vertical slice is active**. The project learns and builds through the real public PR-to-decision path; replay remains supporting test and reproducibility behavior.

## Implemented truth

The current B2 path is implemented through exact dependency identity:

```text
public repository + PR number
→ read-only PR metadata acquisition
→ exact base/head identity validation
→ paginated changed-file acquisition
→ response and count reconciliation
→ patch-evidence classification
→ one exact pinned Python dependency update
→ supported result or explicit unsupported state
→ concise terminal output
```

Active source:

```text
pyproject.toml
src/upgradepilot/__init__.py
src/upgradepilot/__main__.py
src/upgradepilot/cli.py
src/upgradepilot/github_client.py
src/upgradepilot/dependency_change.py
tests/test_github_client.py
tests/test_dependency_change.py
tests/README.md
```

Current runtime dependency:

```text
requests>=2.32,<3
```

Pydantic and other larger dependencies remain deliberately deferred until current implementation evidence creates a concrete need.

## Observed validation

Ali validated the changed-file and pinned-dependency increment in WSL2 with Python 3.12 and an editable `.venv` installation.

Observed sequence:

```text
git pull --ff-only origin main
→ fast-forward to 0ea16d0fbc51312fc70ac6a257e3c97550baeacc
→ python3 -m pip install -e . succeeded
→ 12 deterministic tests passed
→ live googlefonts/glyphsLib#1145 request succeeded
→ requirements-dev.txt acquired
→ pytest 9.0.2 → 9.0.3 extracted
```

This establishes the current supported request-to-dependency-identity path for one real public PR. It does not establish CI authority, upgrade safety, recommendation correctness, broad dependency syntax support, production readiness, or independent ownership.

Detailed commands, outputs, learning depth, and limitations are kept in `working-memory/B2_TECHNICAL_PROGRESS.md` rather than duplicated here.

## Immediate continuation

Follow the current checklist in `plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md`.

Current responsibility:

```text
validated changed-file and dependency extraction increment
→ Ali-owned central test or rule modification
→ deterministic rerun and explanation
```

Next sequence:

1. Ali predicts why `demo.package==1.0.0 → demo_package==1.1.0` should be supported as the same normalized package.
2. Ali adds one test for that behavior to `tests/test_dependency_change.py`.
3. Run the full deterministic suite and inspect the result.
4. Explain which boundary a failure would localize.
5. Record ownership evidence.
6. Only then extend to exact-head GitHub Actions workflow/check evidence.

## Current boundaries

Do not yet:

- claim a dependency recommendation or CI authority result;
- hardcode S004 or an expected decision;
- add upstream, persistence, replay infrastructure, model, service, queue, agent, or deployment layers;
- restore archived M2 source or tests;
- treat AI-written passing tests or one successful command as independent Ali-owned capability;
- expose GitHub write operations or commit credentials.

## Ownership state

Ali has demonstrated the current conceptual flow, predicted pagination and evidence-consistency behavior, distinguished acquisition from extraction, and executed the deterministic and live proofs. Current source remains substantially AI-authored. Ownership now advances through the selected Ali-authored normalized-package identity test and its diagnosis/explanation.
