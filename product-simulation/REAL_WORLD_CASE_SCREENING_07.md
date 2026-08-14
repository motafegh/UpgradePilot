# Real-World Case Screening 07 — Persisted Artifact and Serialization Boundaries

**Date:** 2026-08-12  
**Status:** Completed screening pass; S012 candidate selected  
**Branch:** `agent/product-simulation-case-screening-02`  
**Product context:** `main@1c7f7a79f7f2b56a572e6c460cdb7f11b7f654d4`

## 1. Screening question

This pass asked whether a real Python dependency update can expose a materially different applicability boundary around **persisted or exchanged artifacts** rather than only current source, current environment formation, or current runtime behavior.

The preferred shape was:

> a real public dependency proposal where the target intentionally produces or consumes durable state whose compatibility depends on the dependency version that produced it, so current-revision evidence alone may be insufficient to determine applicability.

The pass remained bounded. Package names associated with serialization, storage, model persistence, or data formats were not treated as evidence of target activation by themselves.

## 2. Candidate summary

| Candidate / search lead | Transition / shape | Screening result | Disposition |
|---|---|---|---|
| generic protobuf / Pydantic serialization updates | multiple release-level wire/JSON semantics | rich upstream changes, but bounded search did not establish a concrete target persisted/exchanged representation path strongly enough | reject as case source for this pass |
| Apache Superset #42415 | PyArrow `24.0.0 → 25.0.0` | target is artifact/data-heavy and dependency comments show compatibility awareness, but no specific changed 24→25 persistence mechanism was grounded to an activated Superset path in the bounded pass | retain as secondary signal; do not promote |
| google-research/TimesFM #456 | msgpack `1.1.0 → 1.2.1` | upstream release contains several decoder/representation changes, but target code search did not establish msgpack pack/unpack use | reject; dependency presence is insufficient |
| freqtrade/freqtrade #12638 | scikit-learn `1.7.2 → 1.8.0` | target intentionally saves and reloads FreqAI models/pipelines across runs; persisted pipelines may contain scikit-learn transforms; scikit-learn explicitly does not support cross-version model loading | **select for S012** |

## 3. Why generic serialization-release richness was insufficient

Initial screening around protobuf/Pydantic-style serialization changes surfaced an important but insufficient pattern:

```text
one dependency release interval
→ multiple wire / JSON / parser / representation changes
```

That is potentially valuable for mechanism decomposition, but it does not answer whether a target actually persists, produces, or consumes the affected representation.

The screening therefore applied the existing activation protection:

```text
serialization-capable dependency present
!=
affected persisted/exchanged representation activated
```

No case was promoted from this search axis without a concrete target producer/consumer path.

## 4. Apache Superset #42415 — data-oriented package without a sufficiently grounded changed mechanism

**Repository:** `apache/superset`  
**PR:** `#42415`  
**Proposal:** PyArrow `24.0.0 → 25.0.0`.

The proposal is real and merged. Superset's dependency declarations also carry explicit review context around PyArrow compatibility with database dependencies, and PyArrow participates in a data-oriented product domain where persisted/artifact boundaries are plausible.

However, this screening pass did not establish all of the following together:

1. one exact PyArrow 24→25 semantic/artifact change;
2. one exact Superset producer/consumer path for the affected representation;
3. the activation condition that makes that change relevant to the target.

Therefore:

```text
data/artifact-heavy dependency
+
real target dependency update
!=
proved persisted-artifact impact candidate
```

**Disposition:** retain as a possible future lead, not S012.

## 5. TimesFM #456 — useful negative control for dependency-presence shortcuts

**Repository:** `google-research/timesfm`  
**PR:** `#456`  
**Proposal:** msgpack `1.1.0 → 1.2.1`.

The crossed msgpack release contains several materially different changes, including decoding/error-handling behavior, map-key handling, timestamp behavior, recursion limits, and interpreter support.

A bounded target search for msgpack packing/unpacking use did not establish an active target representation path.

That does not prove TimesFM never reaches msgpack transitively. It establishes only that the evidence needed for this pass was not obtained.

The correct screening state is therefore:

```text
upstream change mechanisms available
+
target dependency relationship exists
+
concrete target representation path not established
→ do not promote
```

This is a useful negative control against turning release-note richness into target applicability.

## 6. Selected S012 candidate — Freqtrade #12638

**Repository:** `freqtrade/freqtrade`  
**Pull request:** `#12638`  
**Base:** `9baa6eebbe49746241a344e67b5d9f50acdeae17`  
**Head:** `ca47882fa91a35bfabf92c54beddf522e6f95907`  
**Merge commit:** `46ee0921191dfb98f135d7cccdb004a135ac1b58`  
**Proposal:** scikit-learn `1.7.2 → 1.8.0` in `requirements-freqai.txt` and `requirements-hyperopt.txt`.

The changed FreqAI requirement is not merely an unused analytical dependency.

At the exact base revision, FreqAI deliberately persists reusable state:

```text
training / pipeline construction
→ model + feature pipeline + label pipeline saved to disk
→ later run with same model identifier
→ saved model/pipelines loaded instead of necessarily retraining
→ prediction / backtest / live reuse
```

`freqtrade/freqai/data_drawer.py` uses `cloudpickle.dump(...)` and `cloudpickle.load(...)` for persisted models and pipelines. The FreqAI documentation explicitly describes model reuse across later runs and states that changing the model `identifier` is how users force retraining or select a different saved model.

The feature-engineering documentation additionally allows scikit-learn transformations such as `QuantileTransformer` and `StandardScaler` inside FreqAI pipelines. Those pipelines are among the objects persisted with cloudpickle.

## 7. Upstream persistence contract

The scikit-learn 1.7.2 model-persistence documentation establishes a strong version boundary for pickle-based persistence:

- pickle/joblib/cloudpickle consumers should use the same dependency versions as the training environment;
- loading a model trained with a different scikit-learn version is not supported;
- cross-version loads may sometimes succeed but remain unsupported and can produce unexpected behavior or errors;
- scikit-learn exposes `InconsistentVersionWarning` for an estimator loaded under a version inconsistent with the version that pickled it.

Authoritative source:

- <https://scikit-learn.org/1.7/model_persistence.html>

This is sufficient to establish a real compatibility proposition. It is **not** sufficient to claim that one particular FreqAI artifact fails under 1.8.0.

## 8. New applicability shape

S012 exposes a target-context dimension not isolated by the existing numbered cases:

```text
current target source
+
current dependency version
```

can be insufficient when the target consumes durable state created earlier.

The relevant shape is:

```text
historical persisted artifact
+
artifact producer dependency version
+
current consumer dependency version
+
real target reuse/load path
→ cross-version persisted-artifact compatibility proposition
```

Candidate activation can therefore depend on facts outside the current repository tree:

```text
FreqAI reuse path active
AND
existing persisted model/pipeline selected
AND
artifact contains scikit-learn state
AND
artifact was produced under scikit-learn 1.7.2
AND
consumer environment now uses scikit-learn 1.8.0
→ scikit-learn cross-version persistence boundary becomes applicable
```

A particular user's artifact population may remain unknown from repository evidence alone. That is an `unresolved` applicability fact, not evidence of non-applicability.

## 9. Why this is not duplication

### Versus S008

S008 concerns **package installation artifact serviceability**:

```text
compatible wheel available?
source fallback available?
source fallback succeeds?
```

S012 concerns **target-owned/target-managed persisted runtime state** created by an earlier environment and consumed by a later one.

### Versus S009

S009 concerns a repository reproducibility/provenance contract as decision context. S012 concerns a technical producer/consumer compatibility boundary for real persisted objects.

### Versus S010

S010 pressures candidate-discovery breadth across multiple mechanisms in one dependency proposal. S012 pressures temporal artifact provenance and applicability beyond current source state.

### Versus S011

S011 concerns whether an optional dependency environment is formed and activated. S012 can apply even when the current environment is formed correctly; the unresolved input may instead be the provenance/version of state created in an earlier environment.

## 10. Dynamic execution decision

No dynamic reproduction is required for the owned S012 question.

Static authoritative evidence already establishes:

- exact dependency transition;
- real FreqAI persisted-state producer and consumer path;
- intentional cross-run reuse;
- the possibility of scikit-learn objects inside persisted pipelines;
- the upstream unsupported cross-version persistence boundary.

A dynamic experiment such as producing a representative FreqAI artifact under 1.7.2 and loading/using it under 1.8.0 would answer a narrower consequence question:

> what happens to this exact representative artifact?

That is not necessary to establish the applicability/provenance responsibility being screened here.

## 11. S012 admission question

S012 should own:

> **Can a dependency update be materially applicable because the target intentionally reloads persisted artifacts produced under the old dependency version, such that artifact producer-version/provenance is a necessary target-context proposition even when the current repository revision and fresh-state environment are otherwise coherent?**

It should not own:

- universal scikit-learn persistence behavior;
- proof that Freqtrade 1.8.0 reuse fails;
- every FreqAI model type;
- all user artifact histories;
- a generic artifact/provenance graph;
- final maintainer merge/block/defer action.

## 12. Claim limits

Do not infer from this pass that:

- scikit-learn 1.8.0 definitely breaks Freqtrade;
- every persisted FreqAI artifact contains a scikit-learn estimator;
- every user has an old persisted artifact;
- a cross-version artifact necessarily fails to deserialize;
- an `InconsistentVersionWarning` necessarily becomes a runtime failure;
- PR #12638 should not have been merged;
- project-wide CI does or does not cover old artifacts without separate exact workflow/test evidence;
- all persisted artifacts require retraining after every dependency update.

## 13. Screening result

```text
broad serialization/persistence search
→ reject dependency-presence and release-richness shortcuts
→ require concrete target producer/consumer evidence
→ Freqtrade intentionally persists + reuses models/pipelines
→ persisted pipelines may include scikit-learn objects
→ scikit-learn 1.7.2 defines cross-version loading as unsupported
→ historical artifact provenance becomes a real applicability input
→ admit S012
```

## 14. Stop

Screening Pass 07 is complete.

Next: freeze a small S012 evidence bundle around exact proposal identity, persisted-artifact producer/consumer path, authoritative upstream version contract, activation/provenance state, and stopping. Do not expand into a generic persistence architecture or compatibility benchmark unless a later product/evaluation question requires it.