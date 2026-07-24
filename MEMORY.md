# UpgradePilot Current Memory

**Last updated:** 2026-07-24  
**Purpose:** Concise project-local continuation. Active source, tests, commands, outputs,
and the actual environment remain the authority for implemented behavior.

## Current route

The controlling route is
[`plans/UPGRADEPILOT_90_DAY_PLAN.md`](plans/UPGRADEPILOT_90_DAY_PLAN.md).
D1 is passed, B1 has passed for B2 entry, and **B2 — Public PR vertical slice is active**.
Ali rejected the replay-first implementation sequence and directed the project to learn and
build through the real public PR-to-decision flow.

Ordinary learning and execution are controlled by
[`OPERATING_GUIDE.md`](OPERATING_GUIDE.md), including its post-run learning and ownership
review.

## Current implementation

The first B2 increment is:

```text
public repository + PR number
→ read-only GitHub pull-request request
→ exact base/head identity validation
→ concise identity output
```

It does not yet retrieve changed files, determine dependency changes, inspect workflows,
evaluate evidence authority, or recommend an action.

## Implemented truth

Active source includes:

```text
pyproject.toml
src/upgradepilot/__init__.py
src/upgradepilot/__main__.py
src/upgradepilot/cli.py
src/upgradepilot/github_client.py
tests/test_github_client.py
tests/README.md
```

The first increment provides:

- a minimal `upgradepilot` command and `python -m upgradepilot` entry point;
- public GitHub pull-request acquisition using `Requests`;
- optional `GITHUB_TOKEN` authentication;
- explicit connect/read timeouts;
- local repository and PR-number validation;
- exact PR number, author, state, base SHA, head SHA, and changed-file-count validation;
- separate input, transport/acquisition, HTTP, and successful-response validation failures;
- ambiguous `404` handling as `not_found_or_inaccessible`;
- no target-repository write operations.

Runtime dependency:

```text
requests>=2.32,<3
```

The dependency was admitted for a direct synchronous HTTP API, explicit timeout and error
handling, response headers/body access, and straightforward test substitution. Pydantic,
OpenAI, PyGithub, HTTPX, persistence, services, queues, models, agents, and deployment
infrastructure remain unselected. Pydantic is deliberately deferred while the current
response shape remains small enough for explicit manual validation.

## Validation state

The published source was validated by Ali in the actual WSL development environment with
Python 3.12.

The first attempt after activating the existing virtual environment failed with:

```text
ModuleNotFoundError: No module named 'requests'
```

This showed that activating a virtual environment does not synchronize newly declared
project dependencies. The existing editable UpgradePilot installation still pointed to the
source tree, but the environment had not been reinstalled after `Requests` was added to
`pyproject.toml`.

Ali then ran:

```bash
python -m pip install --upgrade pip
python -m pip install -e .
python -m unittest discover -s tests -v
upgradepilot googlefonts/glyphsLib 1145
```

Observed results:

- editable installation completed successfully;
- `requests`, `charset_normalizer`, and `urllib3` were installed as required dependencies;
- both active unit tests passed;
- the live public GitHub request completed successfully without a token;
- the command returned the expected exact S004 identity:
  - repository `googlefonts/glyphsLib`;
  - PR `1145`;
  - base SHA `044f19e4b1437bfc4343592486f4e3c6040306d9`;
  - head SHA `f3cda8a94600e58d27f1bc17c99b7693718b6350`;
  - one changed file.

This establishes the first live read-only request-to-validated-identity path in Ali's actual
environment. It does not establish changed-file extraction, CI authority, recommendation,
production readiness, or independent Ali ownership.

## Active learning and ownership style

After each meaningful implementation, test, live command, or failure:

- teach and inspect the concepts, execution paths, failure boundaries, syntax, and source
  behavior that are material to the current product responsibility, target career, safety,
  diagnosis, or ownership;
- do not study every line or incidental syntax equally;
- classify relevant material as **must master now**, **understand operationally**, or
  **deferred deliberately**;
- require one **Ali-owned practice** action through a meaningful prediction, explanation,
  modification, test, or diagnosis of a central boundary;
- state what the evidence proves and what it does not prove;
- record durable learning only when demonstrated depth, a material misconception, a reusable
  lesson, or continuation changed.

## Immediate continuation

1. Complete the targeted walkthrough of the current command path:
   - CLI input and exit boundary;
   - read-only HTTP request and timeout handling;
   - HTTP status versus transport failure;
   - manual validation of untrusted JSON;
   - exact `PullRequestIdentity` construction;
   - mocked unit evidence versus live-network evidence.
2. Ali explains the successful request path and at least one failure boundary in his own
   words.
3. Add changed-file acquisition and one supported pinned Python dependency-change
   extraction.
4. Add deterministic tests, run them in WSL, and run the safe real S004 path.
5. Perform the post-run learning-depth review and one Ali-owned modification, test, or
   diagnosis before extending to exact-head workflow evidence.

Do not yet:

- claim a dependency recommendation or CI authority result;
- hardcode S004 or an expected decision;
- add upstream, persistence, model, service, queue, agent, or deployment layers;
- restore archived M2 source or tests;
- treat AI-written passing tests or one successful command as independent Ali-owned
  capability;
- expose GitHub write operations or commit credentials.

## Ownership state

Ali chose the real-flow-first route, correctly reasoned about ambiguous `404`, timeout,
insufficient-evidence behavior, and deferred Pydantic; authorized the first implementation;
installed and executed it successfully in WSL; surfaced the first real environment failure;
and defined the required learning/ownership style. The current code remains substantially
AI-authored. Ownership advances through Ali's explanation, modification, testing, and
diagnosis of central paths.