# S012 Candidate Screening — Freqtrade scikit-learn Persisted-Artifact Version Boundary

**Date:** 2026-08-12  
**Status:** Admitted prospective real-world simulation case  
**Branch:** `agent/product-simulation-case-screening-02`  
**Product context:** `main@1c7f7a79f7f2b56a572e6c460cdb7f11b7f654d4`

## 1. Candidate identity

**Target repository:** `freqtrade/freqtrade`  
**Pull request:** `#12638`  
**Base revision:** `9baa6eebbe49746241a344e67b5d9f50acdeae17`  
**Head revision:** `ca47882fa91a35bfabf92c54beddf522e6f95907`  
**Merge commit:** `46ee0921191dfb98f135d7cccdb004a135ac1b58`  
**PR state at observation:** closed, merged  
**Proposal:** scikit-learn `1.7.2 → 1.8.0` in the FreqAI and hyperopt requirements.

Changed files:

```text
requirements-freqai.txt
requirements-hyperopt.txt
```

The FreqAI requirement explicitly identifies scikit-learn as required for FreqAI.

## 2. Owned question

S012 owns one temporal artifact-applicability question:

> **Can a dependency update be materially applicable because the target intentionally reloads persisted artifacts produced under the old dependency version, such that artifact producer-version/provenance is a necessary target-context proposition even when the current repository revision and freshly formed environment are otherwise coherent?**

S012 does **not** own the stronger question:

> Does scikit-learn 1.8.0 actually break one particular FreqAI artifact?

That would require artifact-specific consequence evidence.

## 3. Why the existing corpus is insufficient

The nearest cases cover different responsibilities:

- S007 — package-family/environment coherence before runtime;
- S008 — binary artifact serviceability and source fallback during installation;
- S009 — repository reproducibility/provenance as decision context;
- S010 — multiple independently grounded mechanisms from one proposal;
- S011 — optional dependency environment formation and platform/hardware activation.

None isolates this shape:

```text
artifact produced under historical dependency environment
→ durable state survives
→ later runtime consumes that state under updated dependency environment
```

The new pressure is that **current repository state is not necessarily complete target context**.

## 4. Exact target persisted-artifact path

At the exact PR base, `freqtrade/freqai/data_drawer.py` contains a real durable producer/consumer path.

### Save path

For the `joblib` model type, FreqAI writes the trained model using:

```python
cloudpickle.dump(model, fp)
```

into a `_model.joblib` file.

It also persists:

```text
feature pipeline → cloudpickle
label pipeline   → cloudpickle
training data    → pandas pickle
metadata         → JSON
```

### Load path

Later, `load_data(...)` reloads:

```text
feature pipeline → cloudpickle.load(...)
label pipeline   → cloudpickle.load(...)
joblib-type model → cloudpickle.load(...)
```

This establishes:

```text
past FreqAI execution
→ persisted Python object state
→ later FreqAI execution
```

The path is target-owned behavior, not only a dependency capability.

## 5. Reuse is intentional product behavior

The exact-base `docs/freqai-running.md` explicitly describes **model reuse**.

After training, later backtests using the same configuration can locate previously trained models and load them instead of retraining. Users change the FreqAI `identifier` when they want a new model and can select an earlier model by using its identifier.

The documentation additionally supports saving backtest models for later live deployment.

Therefore:

```text
persisted model/pipeline exists
+
subsequent-run reuse path exists
```

is an intended target capability rather than a speculative historical-state scenario.

## 6. scikit-learn state can participate in persisted pipelines

The exact-base feature-engineering documentation shows custom FreqAI pipelines using scikit-learn transformations, including examples such as:

```text
QuantileTransformer
StandardScaler
```

through the FreqAI/DataSieve pipeline mechanism.

Those feature and label pipelines are among the objects saved and later loaded through cloudpickle.

This is sufficient to establish a supported artifact shape in which persisted FreqAI state contains scikit-learn-owned objects.

S012 does not claim every FreqAI model or pipeline contains such an object.

## 7. Authoritative upstream persistence contract

The scikit-learn **1.7.2** model-persistence documentation is the primary upstream authority for the producer-side version in the proposal.

It establishes:

- `pickle`, `joblib`, and `cloudpickle` persistence relies on a compatible Python dependency environment;
- supported model loading expects the same package versions as the training environment;
- loading models saved with a different scikit-learn version is not supported;
- a cross-version load may sometimes happen, but is unsupported and can yield unexpected results, errors, or process failure;
- dependency-version metadata should be preserved to reconstruct the training environment;
- `InconsistentVersionWarning` identifies estimators loaded under a scikit-learn version inconsistent with the one that pickled them.

Primary source:

- <https://scikit-learn.org/1.7/model_persistence.html>

This establishes a version-sensitive persistence boundary without proving failure of a particular FreqAI artifact.

## 8. Candidate-specific applicability propositions

The cross-version artifact concern is applicable only when the relevant historical state exists.

A useful bounded decomposition is:

### P1 — current affected consumer environment

The FreqAI runtime now resolves/uses scikit-learn 1.8.0 under the proposal.

**Status at proposal level:** established by the dependency transition for environments formed from the updated requirement.

### P2 — persisted artifact reuse path exists

The target can save and later load/reuse model and pipeline artifacts.

**Status:** established by exact target code and documentation.

### P3 — selected artifact contains scikit-learn-owned persisted state

For example, a persisted feature/label pipeline contains a scikit-learn transformer.

**Status:** supported as a real target artifact shape; not established for every artifact/user.

### P4 — selected artifact was produced under the old scikit-learn environment

The artifact being reused was persisted while scikit-learn 1.7.2 was active.

**Status:** not knowable for an arbitrary user from repository source alone.

### P5 — same artifact is consumed after the update

The reuse/identifier path selects that old artifact rather than retraining or selecting a newly produced artifact.

**Status:** possible and explicitly supported by target behavior; user-/artifact-specific occurrence is not established from repository source alone.

Therefore the case intentionally contains a conditional state:

```text
P1 + P2 established
P3 supported artifact shape
P4/P5 depend on historical target state
→ applicability can be established for a concrete artifact context
→ arbitrary-user applicability may remain unresolved
```

## 9. Important new distinction — provenance is part of technical context

S012 establishes that artifact provenance can be technically relevant, not merely documentary metadata.

For this mechanism:

```text
artifact bytes alone
```

may be insufficient context.

The materially relevant identity can include:

```text
artifact
+
producer dependency version/environment
+
consumer dependency version/environment
+
selection/reuse path
```

This does not authorize a universal provenance graph or artifact schema. It establishes only that a future product method must not erase producer-version context when the mechanism depends on it.

## 10. Current-state success cannot automatically close historical-artifact risk

Even if a target can:

- install the updated dependency;
- train a fresh model;
- run fresh-state tests;

those observations would not automatically establish:

> an artifact persisted under 1.7.2 is supported under 1.8.0.

That is a different proposition.

The distinction is:

```text
fresh-state compatibility
!=
cross-version persisted-state compatibility
```

S012 does not claim the repository's actual CI has this exact blind spot; exact CI coverage is outside the owned question unless separately inspected.

## 11. Evidence sufficiency and negative evidence

Repository source is sufficient to establish:

- the producer/consumer path;
- intended artifact reuse;
- supported use of scikit-learn objects in persisted pipelines.

Upstream documentation is sufficient to establish:

- the cross-version persistence support boundary.

Repository source is **not** sufficient to determine for an arbitrary deployment:

- whether an old artifact exists;
- the dependency version that created it;
- whether it contains scikit-learn-owned state;
- whether it will be selected after update.

Therefore:

```text
artifact history not visible in repository
!=
no old artifact exists
```

and:

```text
historical state unavailable
→ unresolved for that deployment/context
```

not `not applicable`.

## 12. Dynamic-check decision

A representative cross-version load experiment is technically possible:

```text
produce artifact under 1.7.2
→ preserve exact artifact
→ load/use under 1.8.0
→ observe warning / load result / behavior
```

But that check answers the narrower consequence question for the chosen artifact.

The S012 admission question is already resolved by authoritative static evidence, so dynamic execution would not materially improve the owned conclusion.

**Decision:** do not execute a reproduction for admission.

## 13. Admission gates

### Gate A — real public proposal

**Pass.** Exact public Dependabot PR with frozen base/head and a scikit-learn version transition.

### Gate B — supported boundary

**Pass.** Public Python dependency-update proposal; all target evidence is read-only.

### Gate C — distinct question

**Pass.** Existing cases do not isolate historical target artifacts whose producer dependency environment survives into a later consumer environment.

### Gate D — target relationship

**Pass.** FreqAI explicitly saves and reloads durable model/pipeline state; reuse across later runs is documented behavior.

### Gate E — dependency-owned state can be persisted

**Pass.** Supported FreqAI pipelines may contain scikit-learn transformations and are persisted with cloudpickle.

### Gate F — authoritative upstream boundary

**Pass.** scikit-learn 1.7.2 explicitly treats cross-version model persistence/loading as unsupported.

### Gate G — honest unresolved path

**Pass.** Specific artifact failure and arbitrary-user artifact history can remain unresolved without being converted into non-applicability.

### Gate H — bounded stop

**Pass.** No dynamic reproduction or full FreqAI model matrix is required to establish the owned applicability/provenance distinction.

## 14. Planned evidence bundle

Purpose-built records:

1. `CASE_IDENTITY_AND_TRANSITION.json`
2. `PERSISTED_ARTIFACT_PATH.json`
3. `UPSTREAM_PERSISTENCE_CONTRACT.json`
4. `ARTIFACT_ACTIVATION_AND_STATE.json`
5. `DISCOVERY_AND_STOPPING.json`
6. scenario `README.md`

## 15. Claim limits

S012 does **not** establish:

- that scikit-learn 1.8.0 breaks Freqtrade;
- that every FreqAI model is a scikit-learn model;
- that every persisted FreqAI pipeline contains scikit-learn state;
- that every user reuses an artifact produced under 1.7.2;
- that cross-version artifacts always fail to deserialize;
- that `InconsistentVersionWarning` is always fatal;
- that current Freqtrade CI does or does not test this history-dependent path;
- that PR #12638 should have been blocked or deferred;
- that every dependency update involving persisted data requires retraining;
- that UpgradePilot should now implement a universal artifact-provenance subsystem.

## 16. Stop line

Do not extend S012 into:

- a full scikit-learn 1.8 migration audit;
- all FreqAI model types;
- exhaustive Freqtrade CI analysis;
- downloading or executing user model artifacts;
- a generic temporal state database;
- a generic provenance graph;
- a maintainer recommendation.

## 17. Admission decision

**S012 admitted.**

Next: freeze the small evidence bundle, synthesize the temporal persisted-artifact lesson, update workspace navigation, and stop.