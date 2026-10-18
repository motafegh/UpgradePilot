# Investigator successor Build evidence

Owner: [Build cycle](../../2026-10-19_investigator-successor-build_lbd-cycle.md).
Scope: offline implementation proof under the [successor plan](../../../plans/INVESTIGATOR_RUN_CONTROL_COMPLETION_AND_CAPABILITY_DIAGNOSTIC_PLAN.md).

[Control proof](control-proof.json) records 202 passing focused/seam/nearest Workspace tests and the corresponding source hashes. The optional preserved SDK was selected for its actual queue/cancel control test without constructing a client or requesting inference.

Reproduction (run from repository root):

```sh
PYTHONPATH=src:.:/home/motafeq/.local/share/upgradepilot/investigator-runs/deployment-interface-2026-10-16-r1/sdk-1.5.0/lib/python3.12/site-packages .venv/bin/python -m unittest experiments.tests.test_investigator_run_control experiments.tests.test_investigator_model_interface experiments.tests.test_investigator_workspace_trial -q
PYTHONPATH=src:. .venv/bin/python -m unittest experiments.tests.test_workspace_investigator_seam -q
PYTHONPATH=src:.:tests .venv/bin/python -m unittest test_workspace_consumer_access test_workspace_host_integration test_workspace_lifecycle_publication -q
```

The SDK path is the installed optional environment, not a new project dependency. Without it, only the SDK-specific queue proof skips. Scripted/fake-channel success does not qualify actual backend cancellation, model-visible token fit or semantic usefulness. Original experiment roots and outcomes remain unchanged.
