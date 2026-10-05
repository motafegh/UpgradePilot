# Source-only interpretation implementation — engineering evidence

This record establishes experiment mechanics with controlled providers. It does not establish live-model meaning/omission quality, target applicability, product adoption or maintainer usefulness.

Implementation: [interpreter](../../../experiments/api_change_interpretation.py) and [opt-in trial/offline reader](../../../experiments/api_change_interpretation_trial.py). Coordination and the actual engineering evolution remain in the [single cycle record](../../2026-10-05_1950_api-change-interpretation-implementation_lbd-cycle.md); the feasibility plan and ADR retain authority.

- Before implementation: 100 active API-trial tests on the unchanged executable baseline.
- Final focused interpreter/ordinary-composition suite: **31/31**.
- Final six-module active API-trial regression: **120/120** (20 new test methods with parameterized adversaries).
- Touched Ruff check and format check: pass. Module CLI help: pass. Documentation/scope/whitespace checks are retained in the cycle record.
- No `src/`, product tests, dependencies, existing acquisition-only entry, specifications, ADRs or workflows changed. Full product/installed regression and unrelated full experiment regression were not rerun for this experiment-only responsibility.
- No live model inference, fresh external acquisition, tokenizer/context measurement, schema-provider acceptance or semantic adjudication ran. The default local provider returns `effective_capacity_unverified` before HTTP inference.
- Earlier unrelated governance marker failure and broader historical experiment-suite failures remain disclosed in the cycle/live owners. The hosted workflow is manual product verification; no hosted run is claimed for this experiment increment.

[Controlled HTTPX recovery](controlled-httpx-recovery.json) records a fresh interpreter/save/actual offline-CLI proof using the previously normally acquired public PR packet. All 1,367 available source characters remain in scope. The controlled proposal cites the authentic `proxies` removal line; code recovers its exact quotation, character range, UTF-8 hash, release and repository/commit/path. Target and adapter branches survive unchanged. The full redundant packet stays locally under `.tmp/api-interpretation-implementation/historical-httpx-controlled-final.json`; this public record contains bounded reviewed evidence and identities. No assembled prompt or model response archive was saved.

The normal fresh PR-to-proposal composition uses controlled public acquisition responses in tests, rather than claiming another live acquisition. Tests distinguish that proof from the historical-real-source component proof. A deliberately incorrect source interpretation still passes shape/reference validation: semantic correctness is explicitly outside this engineering gate. Save/read checks establish consistency, not origin authenticity or execution resume.

Reproduce the final active trial regression:

```sh
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -m unittest \
  experiments.tests.test_api_change_source_acquisition \
  experiments.tests.test_api_target_context \
  experiments.tests.test_api_python_bindings \
  experiments.tests.test_api_adapter_exploration \
  experiments.tests.test_api_public_pr_context \
  experiments.tests.test_api_change_interpretation
```

The focused `test_retained_real_httpx_window_recovers_exact_quote_with_controlled_proposal` test reconstructs the historical-source recovery proof. The ordinary acquisition/save/read and CLI tests exercise the new opt-in entry. `run` needs separately measured request-bound capacity before genuine local inference; `open` is offline:

```sh
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -m experiments.api_change_interpretation_trial --help
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -m experiments.api_change_interpretation_trial open PATH
```

The JSON record freezes final producer code, prompt/schema and exact historical-source request identities before any live API-role output. Its request hash is not token-fit proof. The next evaluation must inspect the actual deployment/tokenizer/template, measure complete input plus schema and 1,536 reserved output tokens, verify provider support and review the frozen development cases independently of citation validity.
