# UpgradePilot Current Memory

**Last updated:** 2026-07-24  
**Purpose:** Concise project-local continuation. Active source, tests, commands, outputs, and the actual environment remain the authority for implemented behavior.

## Current route

- Controlling route: [`plans/UPGRADEPILOT_90_DAY_PLAN.md`](plans/UPGRADEPILOT_90_DAY_PLAN.md)
- Current bounded plan: [`plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md`](plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md)
- Ordinary learning and execution: [`OPERATING_GUIDE.md`](OPERATING_GUIDE.md)
- Detailed technical evidence and learning depth: [`working-memory/B2_TECHNICAL_PROGRESS.md`](working-memory/B2_TECHNICAL_PROGRESS.md)
- Current frozen study snapshot: [`learning/b2-pr-acquisition-and-pinned-extraction/`](learning/b2-pr-acquisition-and-pinned-extraction/)

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

## Learning snapshot

The current educational package is frozen against behavioral source/test commit `0ea16d0fbc51312fc70ac6a257e3c97550baeacc`.

It separates:

- request-to-evidence flow and failure boundaries;
- source behavior Ali must own versus syntax that only needs operational understanding;
- deterministic test claims, live-smoke limitations, and failure localization;
- one SMART study session ending with the normalized-package ownership test.

Later implementation changes should create a new learning snapshot rather than silently rewriting this one.

## Immediate continuation

Follow the current checklist in `plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md`.

Current responsibility:

```text
study and reconstruct the validated acquisition/extraction increment
→ Ali-owned central normalized-package test
→ deterministic rerun and explanation
```

Next sequence:

1. Study the focused files under `learning/b2-pr-acquisition-and-pinned-extraction/`.
2. Reconstruct the request-to-result flow and failure classifications without notes.
3. Predict why `demo.package==1.0.0 → demo_package==1.1.0` should be supported as the same normalized package.
4. Add one test for that behavior to `tests/test_dependency_change.py`.
5. Run the full deterministic suite and inspect the result.
6. Explain which boundary a failure would localize and record ownership evidence.
7. Only then extend to exact-head GitHub Actions workflow/check evidence.

## Current boundaries

Do not yet:

- claim a dependency recommendation or CI authority result;
- hardcode S004 or an expected decision;
- add upstream, persistence, replay infrastructure, model, service, queue, agent, or deployment layers;
- restore archived M2 source or tests;
- treat AI-written passing tests, passive study, or one successful command as independent Ali-owned capability;
- expose GitHub write operations or commit credentials.

## Ownership state

Ali has demonstrated the current conceptual flow, predicted pagination and evidence-consistency behavior, distinguished acquisition from extraction, and executed the deterministic and live proofs. Current source and the new learning package remain substantially AI-authored. Ownership advances only when Ali studies the material, authors the selected normalized-package identity test, interprets its result, and explains the protected boundary.