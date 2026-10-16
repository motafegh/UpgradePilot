# Common Investigator input snapshot — October 16, 2026

This dated evidence qualifies a **new** shared dependency/CI/source snapshot under [integration plan §3](../../../plans/INVESTIGATOR_INTEGRATION_AND_COMPARATIVE_EVALUATION_PLAN.md#3-recover-or-establish-the-common-input-freeze). It replaces unavailable old inputs for future use; it does not recover October 15's exact bytes or revise that historical qualification. [qualification.json](qualification.json) records exact target/content/checkpoint identities, acquisition windows, code identities, accounting, backup/cold results and file hashes. The [owning cycle](../../2026-10-16_2025_common-investigator-input-snapshot_lbd-cycle.md) preserves execution/learning; [MEMORY.md](../../../MEMORY.md) alone selects live continuation.

## Durable local files

```text
/home/motafeq/.local/share/upgradepilot/investigator-inputs/common-freeze-2026-10-16-2025/
  manifest.json
  qualification.json
  case-1/ and case-2/
    common-sources.json
    public-acquisition.json
    checkpoint/workspace.sqlite3
  validated-backup/
    manifest.json
    case-1/ and case-2/
      common-sources.json
      public-acquisition.json
      checkpoint/workspace.sqlite3
  backup-verification.json
  cold-original.json
  cold-backup.json
```

Directory modes are `0700`, file modes `0600`. Raw data stays outside Git/temp; the main branch retains this public-safe evidence. The earlier retained original corpus/metadata remain intact in the separate [research-input retention location](../2026-10-16-investigator-input-retention/README.md). This is same-machine retention and a validated local backup, not off-machine/device-loss protection.

## Observed preparation and proof

The unchanged [preparation diagnostic](../../../tools/prepare_investigator_inputs.py) ran once on the retained corpus/targets, with owner-only umask and anonymous public GET transport. Ambient token/proxy variables were removed only for that command as documented in ENVIRONMENT.md. No credential file was loaded and no target code/workflow or model was executed.

| Case | Public reads | Source files/profile bytes | Genuine native outcome |
| --- | --- | --- | --- |
| HTTPX dependency transition, PR 20 | 4 | 2,632 / 18,873,205 | Zero exact-head runs in this acquisition; `no_successful_ci` / `no_admitted_candidate`. |
| glyphsLib pytest transition, PR 1145 | 10 | 1,384 / 16,035,160 | Two workflow runs; `supported_not_correlated`, with native runtime uncertainty retained. |

All 14 recorded responses are HTTP 200 with actual acquisition start/completion times. Base/head, complete changed-file sets and dependency transitions match the declared targets. Dependency analysis, CI coverage and runtime-state owners each ran exactly once per case. The generic diagnostic exercise retains five deliveries, one attributed source citation and an explicitly unsupported proposal evaluation per case. These are qualification controls, not Investigator outputs or semantic support.

Fresh preflight passed **23 consumer-access tests** (0.910 s), rechecked every retained input hash and matched all **96 product source hashes**. Product source/tests and diagnostic code were unchanged; no full/installed suite was repeated for this data-only execution.

Each checkpoint was backed up through `CheckpointStore.backup`, with its separate source profile and receipts copied and byte-verified. Both backup stores passed supported read-only validation, exact target/revision/checkpoint-digest parity and source-profile identity/count checks. The source databases were unchanged.

Two fresh [guarded cold-reader](../2026-10-15-common-investigator-preparation/cold_inspect.py) processes inspected the original and backup bundles: **four case reads**, each child with **nine active forbidden-entry/network guards**. They reconstructed all 16 revisions per case, supported native/lifecycle history, five actual deliveries, one citation and unsupported evaluation. Source profiles were unnecessary for those retained-content reads. Original and backup projection digests/results match, read/resolve content matches, and database bytes remain unchanged. Separately decoding the copied full source profiles preserves availability of the full source universe.

The exact cold commands, from the main checkout, were:

```sh
PYTHONPATH=src .venv/bin/python3 working-memory/evidence/2026-10-15-common-investigator-preparation/cold_inspect.py /home/motafeq/.local/share/upgradepilot/investigator-inputs/common-freeze-2026-10-16-2025 current
PYTHONPATH=src .venv/bin/python3 working-memory/evidence/2026-10-15-common-investigator-preparation/cold_inspect.py /home/motafeq/.local/share/upgradepilot/investigator-inputs/common-freeze-2026-10-16-2025/validated-backup current
```

## Reuse and boundaries

The new snapshot is mechanically qualified and available offline at the recorded scope. Both future treatments must use this exact shared source/native offering, with restrictions only as declared by the comparison. Each assignment needs a fresh host/lineage and independent mutable accounting. Initialize from the retained native boundary through the supported host interface; do not feed the diagnostic's pre-existing view/proposal/citation history to the model or inherit its notes/selections. Exact adapter binding and isolation remain the next mechanical-integration responsibility.

Current acquisition-time CI responses do not establish original decision-time completeness or global historical absence. Static consumption does not establish installed version, runtime binding, later use or compatibility. Unsupported semantic/adequacy evaluation stays unsupported; citations alone establish no entailment. No independent usefulness, Investigator advantage, product replay, explicit continuation, installed-package equivalence or power-loss claim is added.

The data manifest contains no model configuration and needs no model-substitution rewrite. The plan's pre-run substitution selects Qwen3.8-27B from `unsloth/Qwen3.8-27B-GGUF`, `UD-Q4_K_M`, in the existing second deployment slot. Download completion and actual asset/runtime/template/reasoning identities remain unresolved until qualification; no model was loaded or called here. Historical model configurations and results remain separate references.
