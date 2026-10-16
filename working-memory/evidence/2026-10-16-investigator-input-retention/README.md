# Investigator research-input retention — October 16, 2026

This dated record preserves the available input data from the separate research worktree for reuse from the main checkout. [retention-manifest.json](retention-manifest.json) records paths, SHA256 identities, exact targets, document counts, verification and missing artifacts. [MEMORY.md](../../../MEMORY.md) alone owns current project continuation; the [session record](../../2026-10-16_1930_project-reentry-and-critical-continuation_lbd-cycle.md) preserves the reasoning and scope.

## Retained inputs and location

The complete original research corpus, its two historical freeze/selection metadata files, an exact PR target mapping and a retention manifest are copied to:

```text
/home/motafeq/.local/share/upgradepilot/investigator-inputs/research-corpus-2026-10-07-retained-2026-10-16/
  corpus.json
  pre-inference-freeze.json
  selection-freeze.json
  targets.json
  retention-manifest.json
```

The directory and its new UpgradePilot parents have mode `0700`; the five files have mode `0600`. Original research files remain intact. The new directory is independent of the research worktree and temporary directories. It is local retention on the same machine, not an off-machine backup or disk-loss guarantee.

Raw source data and local run artifacts remain outside Git, consistent with the preparation tool and accepted storage method. This main-branch record contains only public-safe identities, locators and reuse instructions. A fresh clone obtains the record, not the 40 MB corpus; it requires the retained local files or an explicitly supplied verified copy.

| Case | Retained original documents | Exact target |
| --- | --- | --- |
| HTTPX dependency transition | 2,628 | `Aidan-Wallace/kubernetes-dashboard-token-api`, PR 20, HTTPX 0.27.2 → 0.28.1 |
| glyphsLib pytest transition | 1,372 | `googlefonts/glyphsLib`, PR 1145, pytest 9.0.2 → 9.0.3 |

Both cases and their existing source/acquisition context are in the single original `corpus.json`, **40,036,196 bytes**, SHA256 `e6e068de4eacc2ab2ee2028132dedb0bf7f547e18649fbbb0d159c6dfc6d0ebc`. Historical comparison settings are provenance only, not qualified settings or controls for a future experiment. No historical model replies, worker logs or hidden reasoning were copied.

## Verification observed

- Copied corpus/freeze/selection files are byte-identical to their research-worktree originals. The corpus also matches the original-source hash in the [October 15 qualification](../2026-10-15-common-investigator-preparation/qualification.json).
- The canonical whole-bundle identity matches the historical freeze. Recomputed descriptors for all 4,000 documents reproduce both per-case corpus identities, without duplicate source/path pairs.
- Repository, base/head and dependency transitions match October 15's exact targets. `targets.json` derives PR numbers/base/head from that committed qualification; it contains no newly acquired data.
- The main checkout's bounded strict corpus reader opens the retained copy with network/provider entry points forbidden. No native producer, model or target-code execution occurs.
- All five historical method-code hashes match the pinned research Git commit recorded in the manifest. The original research worktree is not needed to read the new corpus copy.
- Every retained file is readable and has the recorded permissions. File/directory synchronization completed; no stronger device durability claim follows.

To recheck local file integrity from the main checkout:

```sh
.venv/bin/python3 - <<'PY'
import hashlib
import json
from pathlib import Path

record = Path('working-memory/evidence/2026-10-16-investigator-input-retention/retention-manifest.json')
manifest = json.loads(record.read_text())
directory = Path(manifest['local_directory'])
for item in manifest['files']:
    path = directory / item['file']
    assert path.stat().st_size == item['bytes'], item['file']
    assert hashlib.sha256(path.read_bytes()).hexdigest() == item['sha256'], item['file']
print('All retained input and metadata hashes match.')
PY
```

## Remaining boundary

This action resolves retention of the surviving original corpus and its comparison metadata. It does **not** recover the enriched October 15 `common-sources.json` profiles, `public-acquisition.json` receipts or Workspace checkpoint stores formerly under `/tmp/upgradepilot-common-preparation.ObOR9V`. Those are distinct later artifacts, and no matching copies were found in the searched locations.

The source corpus cannot manufacture missing later provider bodies. Before paired Investigator runs, locate a complete matching old bundle or explicitly activate a new anonymous-public preparation/freeze under [the integration plan](../../../plans/INVESTIGATOR_INTEGRATION_AND_COMPARATIVE_EVALUATION_PLAN.md#3-recover-or-establish-the-common-input-freeze). The existing [preparation tool](../../../tools/prepare_investigator_inputs.py) can use the retained `corpus.json` and `targets.json` as inputs, with a new owner-only output directory alongside this retained corpus, outside Git/temp. That operation makes public requests and produces a new snapshot; it was not run by this retention action.

Existing interface qualification and historical test results retain their original scope. No checkpoint restoration, product replay, fresh native qualification, inference, semantic quality or maintainer usefulness is established here.
