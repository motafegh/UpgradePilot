# Retained Verification Scripts

`tools/verification/` contains **developer-operated verification scripts worth retaining as executable records**.

These scripts exist for cases where a bounded implementation/debugging step needs an exact runnable proof or smoke check that should remain available for later inspection, replay, or comparison, but the script itself is **not** one of the following:

- product runtime behavior (`src/upgradepilot/`);
- permanent deterministic product regression (`tests/`);
- non-product research/evaluation (`experiments/`);
- an end-user/reviewed usage example (`examples/`).

## Responsibility

A retained verification script answers questions such as:

> What exact executable check did we run for this implementation/debugging checkpoint, with what inputs and expected outcomes?

It is a **developer proof aid and historical executable record**, not a second test suite.

The durable proof boundary remains:

```text
product behavior
→ src/upgradepilot/
→ tests/

one bounded manual/developer verification
→ tools/verification/
→ dated run evidence in working-memory/
```

A passing retained verification script does not replace required product regression coverage.

## When a script belongs here

Use this directory when all of the following are true:

1. the check is developer-operated rather than product runtime;
2. keeping the exact runnable check has future diagnostic, replay, learning, or provenance value;
3. it is not better expressed only as a permanent regression test;
4. it is not exploratory research/evaluation that belongs in `experiments/`;
5. the script exercises admitted product code rather than inventing a parallel implementation.

A short disposable shell/Python command that has no future value does not need to become a repository artifact.

## Dependency boundary

Retained verification scripts may import and exercise:

```text
tools/verification/ → src/upgradepilot/
```

They must not depend on test-only helpers or experiment internals:

```text
tools/verification/ -X-> tests/
tools/verification/ -X-> experiments/
```

If a retained verification needs fixtures, construct the smallest explicit fixture locally in the script or move genuinely reusable product construction into an appropriate product responsibility. Do not turn test helpers into an unofficial runtime API.

## Script requirements

Each retained verification script should state near the top:

- what responsibility/check it verifies;
- why the check is retained instead of being only an inline command;
- what it **does not** prove;
- any required local environment assumptions;
- a clear success/failure result.

Prefer a filename that carries enough scope to remain understandable later, for example:

```text
YYYY-MM-DD_<route-or-responsibility>_<check>.py
```

Do not encode volatile live-state claims into generic reusable script names.

## Evidence and lifecycle

The script is the retained **procedure**. The dated `working-memory/` record owns the observed **execution evidence**: command, relevant commit/revision, environment facts, pass/fail output, diagnosis, and continuation consequence.

If the behavior becomes accepted product behavior, permanent regression coverage still belongs in `tests/`. The retained verification script may remain when it has independent replay/diagnostic/learning value; otherwise it can later be removed or archived deliberately.

This directory does not change the repository-wide executable boundary: `tools/` remains developer diagnostics/live proofs as defined by root `AGENTS.md` and `README.md`.
