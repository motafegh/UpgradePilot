# Native-adoption independent audit evidence

Date: 2026-11-01. Source revision: `e7082e96`, unchanged qualified producer sources. Supports [AUDIT-014](../../../audits/2026-11-01_AUDIT-014_caller-signature-native-integration-readiness.md) and the [audit cycle](../../2026-11-01_caller-signature-integration-independent-audit_cycle.md).

## Executed checks

Commands below run from the repository root. Tests use controlled inputs. No new live qualification, model inference, credential reads or target-code execution was selected. Git fetch was the repository synchronization operation; local and remote main matched.

```sh
PYTHONPATH=src:tests .venv/bin/python -m unittest discover -s experiments/tests -p 'test_api*.py'
```

[API output](api-tests.txt): **280 tests pass**, 15.583 seconds. The printed I001 no-observations/accounting-mismatch row is controlled test output, not a real model attempt. Initial execution without explicit `PYTHONPATH` resolved an older installed package and failed five module imports; [original output](api-tests-import-path-failure.txt) remains. No source or environment installation was repaired. Default import origin was `.venv/lib/python3.12/site-packages/upgradepilot/__init__.py`; explicit `PYTHONPATH=src` resolved this checkout's `src/upgradepilot/__init__.py`.

```sh
PYTHONPATH=tests:src .venv/bin/python -m unittest \
  test_workspace_native_reconstruction test_workspace_checkpoint_reconstruction \
  test_workspace_checkpoint_store test_workspace_lifecycle_publication \
  test_workspace_host_integration test_workspace_consumer_access \
  test_cli test_report test_report_file test_source_topology
```

[Product output](product-tests.txt): **192 tests pass**, 113.801 seconds. Expected CLI refusal/usage messages occur in negative controls. These tests protect current product behavior; the new profile/families do not exist yet.

```sh
.venv/bin/python tools/check_experiment_boundaries.py
```

[Boundary output](boundaries.txt): pass, 131 artifacts / 122 experimental Python modules / 262 internal import edges / 96 product Python files. This is static boundary proof, not an arbitrary dynamic-execution guarantee.

```sh
PYTHONPATH=src:. .venv/bin/python \
  working-memory/evidence/2026-11-01-native-adoption-independent-audit/check_retained.py
```

[Read-only check](check_retained.py), [summary](retained-checks.json), [output](retained-checks-log.txt): all 106 qualified source hashes match. Forty-nine indexed private artifacts match their public-safe recorded hashes: 18 across the three partial-analysis qualification captures, 26 in the Digimon outer/inner attempt, and five in the earlier curated HTTPX case. Indexed files retain mode0600. Fixed readers open those artifacts with the specified AST/HTTP/socket/discovery/comparison/credential hooks forbidden. Source text equality is checked against the unchanged prepared inputs for the three partial-analysis captures; recorded work matches. Digimon outer/inner closure and prior curated outcomes match. Hashes are rechecked after opening; original retained bytes are unchanged.

The script's first launch omitted `.` from `PYTHONPATH` and could not import `experiments`; [that output](retained-checks-import-path-failure.txt) remains. The corrected command above resolves the intended source. The final script additionally checks the earlier curated rejection control; the final summary supersedes the initial three-case-plus-Digimon check without altering any historical evidence.

Raw source, PR bodies and original private bundles are not copied into this packet. The script reads the existing configured owner-only paths and publishes only counts, outcomes, hash-check results and proof limits. It performs fixed opening, not producer replay, repair or regrading.

## Interpretation and limits

- Focused current tests: 280 experimental + 192 product, kept as distinct proof classes.
- Current static dependency/inventory and selected retained-artifact checks pass.
- Full product, full experimental and governance suites were not rerun. Historical broad/governance debt is linked in the audit and is not represented as current green proof.
- No native representation probe, source transfer, new report profile, live product attempt, human usability study or independent semantic evaluation was performed.
- The audit finding is a plan/interface clarification; optional recommendations are labelled as such. No controlling plan, source, test, specification, ADR or live project continuation was changed.
- [Document checks](document-checks.json) record local-reference validation and inspected-content hashes for this report and evidence packet. Git whitespace/diff checks are recorded in the cycle.
