# UpgradePilot Current Memory

**Last updated:** 2026-07-24  
**Purpose:** Concise project-local continuation. Active source, tests, commands, outputs,
and the actual environment remain the authority for implemented behavior.

## Current route

The controlling route remains
[`plans/UPGRADEPILOT_90_DAY_PLAN.md`](plans/UPGRADEPILOT_90_DAY_PLAN.md).
D1 is passed. Ali rejected the replay-first implementation sequence and directed the project
to learn and build through the real public PR-to-decision flow.

## Current implementation authorization

On 2026-07-24, Ali explicitly authorized the first bounded implementation increment after
reviewing the real S004 acquisition path and the minimum HTTP/error model.

This increment begins the public PR vertical slice with:

```text
public repository + PR number
→ read-only GitHub pull-request request
→ exact base/head identity validation
→ concise identity output
```

It does not yet retrieve changed files, determine dependency changes, inspect workflows,
evaluate evidence authority, or recommend an action.

## Implemented truth

Active source now includes:

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
infrastructure remain unselected.

## Validation state

The published source has now been validated by Ali in the actual WSL development
environment with Python 3.12.

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

## Immediate continuation

1. Inspect and explain the installed-package and editable-install behavior exposed by the
   initial `ModuleNotFoundError`.
2. Trace the real command path from CLI arguments through `GitHubReadClient` to the validated
   `PullRequestIdentity` output.
3. Ali explains one successful path and one failure boundary in his own words.
4. Add the next real capability: changed-file acquisition and one supported pinned Python
   dependency-change extraction.
5. Add deterministic tests for that new capability before extending to CI evidence.

Do not yet:

- claim a dependency recommendation or CI authority result;
- hardcode S004 or an expected decision;
- add workflow, upstream, persistence, replay, model, service, or deployment layers;
- restore archived M2 source or tests;
- treat AI-written passing tests or one successful command as independent Ali-owned
  capability;
- expose GitHub write operations or commit credentials.

## Ownership state

Ali chose the real-flow-first route, correctly reasoned about ambiguous `404`, timeout, and
insufficient-evidence behavior, authorized the first implementation, installed and executed
it successfully in WSL, and surfaced the first real environment failure. The current code
remains substantially AI-authored. Ownership now advances through Ali's explanation,
modification, testing, and diagnosis of this central path.