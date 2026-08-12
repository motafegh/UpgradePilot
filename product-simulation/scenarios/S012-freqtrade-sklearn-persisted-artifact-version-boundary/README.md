# S012 — Freqtrade scikit-learn Persisted-Artifact Version Boundary

**Date:** 2026-08-12  
**Status:** Complete at admitted simulation depth  
**Form:** untouched real public dependency proposal + exact target persisted-state evidence + authoritative upstream persistence contract  
**Product context:** `main@1c7f7a79f7f2b56a572e6c460cdb7f11b7f654d4`

## Case identity

Target:

```text
freqtrade/freqtrade#12638
```

Proposal:

```text
scikit-learn 1.7.2
→
scikit-learn 1.8.0
```

Frozen revisions:

```text
base  9baa6eebbe49746241a344e67b5d9f50acdeae17
head  ca47882fa91a35bfabf92c54beddf522e6f95907
merge 46ee0921191dfb98f135d7cccdb004a135ac1b58
```

No target repository was mutated or contacted during this simulation.

## Owned question

> Can a dependency update be materially applicable because the target intentionally reloads persisted artifacts produced under the old dependency version, making artifact producer-version/provenance part of the applicability context?

This case does **not** attempt to prove that one concrete FreqAI model fails after the update.

## Why this case exists

The target deliberately supports this lifecycle:

```text
train / construct pipeline
→ persist model and pipelines
→ later process/run
→ select existing model identifier
→ reload persisted state
→ reuse for prediction/backtest/live work
```

At the exact base revision, FreqAI persists model and pipeline objects through cloudpickle and reloads them later.

The feature-engineering documentation shows that FreqAI pipelines may include scikit-learn transformations such as `QuantileTransformer` and `StandardScaler`.

The producer-side scikit-learn 1.7.2 documentation says cross-version loading of pickle/joblib/cloudpickle-persisted scikit-learn models is unsupported and recommends matching the training/persistence environment's package versions.

Therefore the dependency proposal creates a real conditional compatibility boundary whenever an old scikit-learn-containing artifact is reused under the new environment.

## Core distinction

S012 separates:

```text
CURRENT-STATE COMPATIBILITY
Can the updated environment install and operate on freshly produced state?
```

from:

```text
PERSISTED-STATE COMPATIBILITY
Can the updated environment consume selected state produced under the earlier dependency environment?
```

Those are not equivalent propositions.

A successful fresh install, fresh training run, or fresh-state test cannot automatically establish cross-version persisted-state compatibility.

## Applicability shape

The bounded candidate has a history-sensitive activation path:

```text
updated FreqAI environment uses scikit-learn 1.8.0
AND
persisted-state reuse path is active
AND
selected artifact contains scikit-learn-owned state
AND
artifact was produced under scikit-learn 1.7.2
AND
that same artifact is selected after the update
→ cross-version persistence boundary applicable
```

Repository evidence establishes the reuse mechanism and supported artifact shape.

Repository evidence does not establish every user's artifact history.

Therefore:

```text
artifact provenance unknown
!=
artifact absent
```

and a concrete deployment may remain `unresolved` until its artifact history is acquired.

## Evidence bundle

Read in this order:

1. [`CASE_IDENTITY_AND_TRANSITION.json`](artifacts/CASE_IDENTITY_AND_TRANSITION.json) — exact proposal and revision identity.
2. [`PERSISTED_ARTIFACT_PATH.json`](artifacts/PERSISTED_ARTIFACT_PATH.json) — target producer/consumer path and documented reuse behavior.
3. [`UPSTREAM_PERSISTENCE_CONTRACT.json`](artifacts/UPSTREAM_PERSISTENCE_CONTRACT.json) — scikit-learn 1.7.2 persistence/version contract.
4. [`ARTIFACT_ACTIVATION_AND_STATE.json`](artifacts/ARTIFACT_ACTIVATION_AND_STATE.json) — candidate-specific propositions and unresolved historical-state boundary.
5. [`DISCOVERY_AND_STOPPING.json`](artifacts/DISCOVERY_AND_STOPPING.json) — novelty, dynamic-check pruning, handoff, and stop.

Supporting analysis:

- [`../../S012_CANDIDATE_SCREENING.md`](../../S012_CANDIDATE_SCREENING.md)
- [`../../S012_POST_CASE_SYNTHESIS.md`](../../S012_POST_CASE_SYNTHESIS.md)
- [`../../REAL_WORLD_CASE_SCREENING_07.md`](../../REAL_WORLD_CASE_SCREENING_07.md)
- [`../../REAL_WORLD_SCREENING_PROCESS_JOURNAL_CYCLE_02.md`](../../REAL_WORLD_SCREENING_PROCESS_JOURNAL_CYCLE_02.md) — non-authoritative process chronology.

## Primary evidence sources

Target public evidence:

- <https://github.com/freqtrade/freqtrade/pull/12638>
- exact base `freqtrade/freqai/data_drawer.py`
- exact base `docs/freqai-running.md`
- exact base `docs/freqai-feature-engineering.md`

Upstream authority:

- <https://scikit-learn.org/1.7/model_persistence.html>

## Dynamic reproduction decision

A cross-version artifact experiment was considered but not selected.

It could answer:

> What happens to this exact representative artifact when created under 1.7.2 and consumed under 1.8.0?

It is unnecessary for the admitted question because the exact target code plus official upstream documentation already establish the producer/consumer path and unsupported cross-version compatibility boundary.

This is a positive stopping result, not missing work.

## What S012 establishes

At the admitted depth:

- exact real dependency transition;
- intentional persisted FreqAI model/pipeline lifecycle;
- cross-run model reuse as documented target behavior;
- supported scikit-learn state inside persisted FreqAI pipelines;
- authoritative scikit-learn 1.7.2 cross-version persistence boundary;
- artifact producer-version can be a necessary applicability fact;
- arbitrary deployment artifact history can remain unresolved from repository evidence alone;
- dynamic consequence reproduction is not required for this bounded conclusion.

## What S012 does not establish

Do not infer:

- scikit-learn 1.8.0 breaks Freqtrade generally;
- every FreqAI artifact contains scikit-learn state;
- every user has artifacts created under 1.7.2;
- all cross-version loads fail;
- any warning is fatal;
- current CI covers or misses this path;
- the merged PR was a maintainer mistake;
- retraining is universally required;
- a generic persisted-artifact architecture is now justified.

## Stop

S012 stops at the persisted-artifact applicability/provenance boundary.

Reopen only for a concrete later question such as:

- artifact-provenance acquisition;
- history-dependent applicability representation;
- provenance-matched targeted-check design;
- transfer pressure on a product implementation that would otherwise treat current revision/environment as complete context.