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

Before repository publication, equivalent source was validated with:

```text
python -m compileall
python -m unittest discover -s tests -v
```

Two tests passed:

- successful response constructs exact PR identity and uses explicit timeouts;
- `404` preserves the nonexistence/access ambiguity.

This was local AI-side validation of the published source text. Ali's clean local install,
test execution, and live S004 command are the next required evidence.

## Run next

From a current checkout:

```bash
python -m venv .venv
python -m pip install -e .
python -m unittest discover -s tests -v
upgradepilot googlefonts/glyphsLib 1145
```

A GitHub token is optional for this public request. When used, provide it through the
`GITHUB_TOKEN` environment variable; never commit it.

## Immediate continuation

1. Ali runs the install, active tests, and live S004 command.
2. Inspect the actual output or failure together.
3. Ali explains the request path and one failure boundary.
4. Correct any installation, network, API, validation, or output defect found by the run.
5. Only then add the next real capability: changed-file acquisition and one supported pinned
   Python dependency-change extraction.

Do not yet:

- claim a dependency recommendation or CI authority result;
- hardcode S004 or an expected decision;
- add workflow, upstream, persistence, replay, model, service, or deployment layers;
- restore archived M2 source or tests;
- treat AI-written passing tests as Ali-owned capability;
- expose GitHub write operations or commit credentials.

## Ownership state

Ali chose the real-flow-first route, correctly reasoned about ambiguous `404`, timeout, and
insufficient-evidence behavior, and explicitly authorized this first implementation.
The current code remains substantially AI-authored. Ownership evidence begins with Ali's
local execution, explanation, modification, testing, and diagnosis of this central path.
