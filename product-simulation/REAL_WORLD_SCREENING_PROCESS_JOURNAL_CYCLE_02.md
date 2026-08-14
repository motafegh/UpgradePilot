# Cycle-02 Real-World Screening Process Journal

**Started:** 2026-08-12  
**Status:** Open execution journal for Cycle-02 screening  
**Branch:** `agent/product-simulation-case-screening-02`

> **Role and authority:** This is a non-authoritative execution journal. It records the search path, discarded leads, evidence pivots, reasoning chronology, and why screening decisions were made. It is not a project-state owner, decision-model authority, case conclusion, or substitute for exact case artifacts. Current project state belongs to `MEMORY.md`; stable case conclusions belong to the corresponding screening/scenario/synthesis files.

The journal is intentionally more process-oriented than the normal product-simulation artifacts. It exists so a later reader can reconstruct **how** broad-world screening reached a result, including unsuccessful paths that would otherwise disappear from the final concise case record.

## Journal discipline

Record only materially useful investigative events:

- the question or uncertainty that started a search;
- why a search axis was chosen;
- a promising lead and why it looked promising;
- evidence inspected;
- evidence that was missing or insufficient;
- the reason a lead was rejected, retained, or promoted;
- a pivot that changed the search strategy;
- evidence that materially changed the interpretation;
- the final admission/stopping decision.

Do **not** turn this into:

- a transcript of every tool call;
- a second `MEMORY.md`;
- a status tracker requiring updates for ordinary repository work;
- a mandatory template for every future case;
- an authority over the final evidence bundle.

If later screening work continues Cycle-02, append only when the process itself contains useful learning or explains a decision that the result artifacts alone would hide.

---

# 2026-08-12 — Persisted-artifact / serialization screening leading to S012

## 1. Starting point

Cycle-02 already contained completed S010 and S011 evidence.

The next screening goal was not "find S012." The goal was to continue broad real-world pressure testing and ask whether an important dependency-update responsibility remained underrepresented.

Two candidate gaps looked promising:

1. persisted data / schema / serialization contracts;
2. candidate overlap or deduplication across mechanisms.

Persisted state was chosen first because the existing numbered corpus already contained strong examples around:

- source/runtime behavior;
- environment formation;
- package-family resolution;
- install artifacts;
- repository provenance;
- multi-mechanism discovery;
- optional dependency activation and CI coverage.

What was less directly isolated was this question:

```text
Can compatibility depend on durable state produced before the current revision/environment?
```

That would pressure a different notion of target context.

## 2. First search axis — generic serialization ecosystems

The first broad pass looked for dependency updates in serialization-oriented libraries, including protobuf- and Pydantic-related changes.

### What looked promising

Several release ranges contained multiple wire, JSON, parsing, or representation changes.

That initially looked useful for two reasons:

1. it could expose a persisted/wire compatibility mechanism;
2. it could also pressure S010's lesson that one transition may contain multiple mechanisms.

### What blocked promotion

The target-side evidence was too weak.

The recurring pattern was:

```text
serialization-capable dependency exists
+
upstream release has representation changes
```

without enough evidence for:

```text
target actually persists / produces / consumes the affected representation
```

The important correction was therefore to reject the shortcut:

```text
serialization library present
→ serialization mechanism applicable
```

That is the same category of reasoning error already rejected elsewhere for framework/dependency presence and optional extras.

### Pivot

The search criterion became stricter:

> Prefer targets where persisted or exchanged artifacts are an explicit product behavior, with a visible producer/consumer path.

This changed the search from package-name-driven discovery to target-behavior-driven discovery.

## 3. Secondary lead — Apache Superset / PyArrow

A real Dependabot proposal surfaced:

- `apache/superset#42415`
- PyArrow `24.0.0 → 25.0.0`
- merged.

### Why it looked promising

PyArrow is directly associated with columnar data, IPC, and Parquet-style artifacts. Superset is also data-heavy, and its dependency declarations contain explicit compatibility-review comments around PyArrow and database dependencies.

So this was a plausible place to find a durable data-format or artifact-serviceability issue.

### What was actually established

The proposal and target compatibility concern were real.

### What remained missing

The bounded pass did not obtain a clean chain of:

```text
exact PyArrow 24→25 artifact/representation change
+
exact Superset producer/consumer path for that changed representation
+
activation condition
```

Without that chain, promoting the case would have relied too much on domain association:

```text
PyArrow is about data artifacts
→ therefore this update is a persisted-artifact case
```

That was rejected.

### Outcome

Retain as a secondary lead/control, not a numbered case.

### Process lesson

A dependency's domain can help prioritize search, but it cannot substitute for mechanism-specific target grounding.

## 4. Negative-control lead — TimesFM / msgpack

Another real public proposal surfaced:

- `google-research/timesfm#456`
- msgpack `1.1.0 → 1.2.1`.

The crossed msgpack release contained several concrete changes involving unpacking, map-key behavior, timestamps, recursion limits, and interpreter support.

### Why it looked promising

Unlike a general-purpose numerical dependency, msgpack is explicitly a serialization format/library. If TimesFM used it to persist or exchange target state, the case could have become highly discriminating.

### Target check

A bounded repository search for msgpack packing/unpacking use returned no target code evidence.

### Interpretation

This did **not** establish global absence of every transitive msgpack path.

It established that the evidence required for this screening objective was not present in the inspected scope.

### Outcome

Reject for this pass.

### Process lesson

This became a useful negative control:

```text
serialization dependency declaration
+
rich upstream changes
+
no concrete target producer/consumer path established
→ do not promote
```

## 5. Search pivot — persisted machine-learning model artifacts

The previous leads suggested that the strongest case would likely come from a system where durable artifacts are deliberately reused across executions.

That moved the search toward machine-learning model persistence.

scikit-learn was particularly interesting because its official persistence guidance makes dependency-version provenance explicit rather than merely implying it.

The new target criterion became:

```text
real dependency bump
+
target explicitly saves artifacts
+
target explicitly reloads/reuses them later
+
artifacts can contain dependency-owned state
+
upstream documents cross-version persistence boundary
```

This is much stronger than simply searching for `pickle` or `joblib` package names.

## 6. Freqtrade / scikit-learn lead

A strong real proposal surfaced:

- `freqtrade/freqtrade#12638`
- scikit-learn `1.7.2 → 1.8.0`
- base `9baa6eebbe49746241a344e67b5d9f50acdeae17`
- head `ca47882fa91a35bfabf92c54beddf522e6f95907`
- merged as `46ee0921191dfb98f135d7cccdb004a135ac1b58`.

The PR changes only `requirements-freqai.txt` and `requirements-hyperopt.txt`; the FreqAI requirement itself labels scikit-learn as required for FreqAI.

At first this was still only a dependency proposal. Promotion depended on target persistence evidence.

## 7. Target evidence acquisition — save/load path

The exact PR base version of `freqtrade/freqai/data_drawer.py` materially changed the screening confidence.

The file explicitly saves:

- a model through `cloudpickle.dump(...)` for the joblib model type;
- the feature pipeline through `cloudpickle.dump(...)`;
- the label pipeline through `cloudpickle.dump(...)`;
- additional training data through pandas pickle formats.

The same component later reloads:

- feature pipeline through `cloudpickle.load(...)`;
- label pipeline through `cloudpickle.load(...)`;
- the persisted joblib-model file through `cloudpickle.load(...)`.

This was the first decisive evidence pivot because it established a real producer/consumer artifact path in product code rather than a hypothetical serialization capability.

The candidate now had a concrete target relationship:

```text
past runtime environment
→ durable model/pipeline artifact
→ later runtime environment
```

## 8. Target evidence acquisition — reuse is intentional product behavior

The exact-base FreqAI running documentation then strengthened the result.

It explicitly says that after training:

- subsequent backtests with the same configuration can find and load trained models instead of retraining;
- changing the FreqAI `identifier` is how a user requests a new model;
- saved backtest models can later be used for live deployment;
- predictions and model state can be reused across later runs.

This matters because it converts the save/load code from an implementation detail into an intentional supported user path.

The important reasoning change was:

```text
artifact persistence exists in code
```

became:

```text
artifact reuse across executions is an intended target behavior
```

That makes historical artifact provenance decision-relevant.

## 9. Target evidence acquisition — scikit-learn state can be inside persisted pipelines

The exact-base feature-engineering documentation shows user-defined FreqAI pipelines using scikit-learn transformations such as:

- `QuantileTransformer`;
- `StandardScaler`;
- other scikit-learn transformation steps wrapped for the pipeline.

Those feature/label pipelines are exactly among the objects persisted through cloudpickle.

This avoids another potential shortcut.

The case does **not** need every FreqAI model type to be a scikit-learn estimator. It is enough to establish a supported persisted artifact path in which scikit-learn-owned object state can participate.

## 10. Upstream evidence — exact scikit-learn 1.7.2 persistence boundary

The authoritative scikit-learn 1.7.2 model-persistence documentation was then checked.

It establishes that:

- pickle/joblib/cloudpickle persistence requires the same dependency environment for supported use;
- loading a model trained/persisted with another scikit-learn version is not supported;
- cross-version loading might happen but is unsupported and can yield unexpected behavior/errors;
- dependency-version metadata matters for reproducing the training environment;
- `InconsistentVersionWarning` exists specifically for estimators loaded under a version inconsistent with the one that pickled them.

Source:

- <https://scikit-learn.org/1.7/model_persistence.html>

This was the second decisive evidence pivot.

Before this evidence, the target persistence path was real but the version boundary was only a concern.

After this evidence:

```text
old producer version
+
new consumer version
+
persisted sklearn-containing artifact
```

became an authoritative unsupported-compatibility proposition.

## 11. Admission reasoning — why S012 is new

The candidate was compared against the existing numbered cases rather than admitted merely because it was interesting.

### Not S008 again

S008 asks whether a current environment can obtain/use an installation artifact:

```text
wheel / source fallback / source-build path
```

S012 asks whether a current environment can safely consume **historical target state** produced under an earlier dependency environment.

### Not S009 again

S009 makes repository provenance/reproducibility decision-relevant. S012 makes artifact producer-version provenance part of a technical applicability proposition.

### Not S011 again

S011 asks whether the affected optional environment is formed at all. S012 can occur after the new environment forms successfully; the missing fact may be what historical artifact it consumes.

### New pressure

The case introduces this durable pressure:

```text
current revision identity
!=
complete target context
```

because a relevant input may have been created by an earlier revision/dependency environment and survive into the current one.

That was sufficient novelty to admit S012.

## 12. Consequence versus applicability — dynamic check considered and pruned

A natural next experiment would be:

1. produce a representative FreqAI model/pipeline under scikit-learn 1.7.2;
2. load and exercise it under 1.8.0;
3. observe warnings, load success/failure, or prediction differences.

That check could be useful for the narrower proposition:

> What happens to this exact representative artifact?

But it is not needed for the current owned question:

> Is historical artifact producer-version a real applicability input for this dependency update?

The target save/reuse/load path plus upstream authoritative persistence contract already answer that.

So the execution was deliberately pruned.

This preserves the existing investigation-selection lesson:

```text
possible experiment
!=
required experiment
```

## 13. Branch-context interruption before freezing S012

Before writing the case, the UpgradePilot `main` branch had advanced materially while Cycle-02 remained on its prior base.

A compare showed the simulation branch was:

```text
18 ahead
8 behind
```

The newer main work changed the B2 planning posture toward:

```text
BOUND THE SUPPORTED DOMAIN
NOT THE KNOWN FIXTURE
```

with materially different real-case pressure and evidence-earned abstraction.

That change was relevant to how S012 should be framed: as future adversarial/transfer evidence for a broader responsibility horizon, **not** as a sequential feature request.

Following the simulation workspace's resume discipline, the branch was synchronized non-destructively through internal PR #25:

- head: `main@1c7f7a79f7f2b56a572e6c460cdb7f11b7f654d4`;
- base: `agent/product-simulation-case-screening-02`;
- merge commit: `9b0d9fd4b71d3f81cd15913b43eb3b66309c84f1`.

After sync:

```text
branch ahead of main: 19
branch behind main: 0
merge base: 1c7f7a79f7f2b56a572e6c460cdb7f11b7f654d4
```

No history rewrite or force update was used.

### Why this belongs in the journal

This is not merely Git mechanics. The product context materially changed before S012 was frozen, and the sync prevents the simulation document from silently describing the case against stale planning assumptions.

The final S012 artifacts therefore use:

```text
Product context: main@1c7f7a79f7f2b56a572e6c460cdb7f11b7f654d4
```

## 14. Final Cycle-02 decision for this pass

The screening path was:

```text
generic serialization search
→ too much upstream richness, too little target grounding
→ require concrete producer/consumer path
→ PyArrow/Superset plausible but insufficiently mechanism-specific
→ msgpack/TimesFM negative control: no target use established
→ pivot to intentionally persisted ML artifacts
→ Freqtrade save/load path established
→ cross-run reuse established
→ scikit-learn objects can inhabit persisted pipelines
→ official 1.7.2 cross-version persistence boundary established
→ compare against S008/S009/S011
→ distinct historical artifact-provenance applicability pressure
→ admit S012
→ prune unnecessary dynamic reproduction
```

Result artifact:

- [`REAL_WORLD_CASE_SCREENING_07.md`](REAL_WORLD_CASE_SCREENING_07.md)

Case artifacts:

- `S012_CANDIDATE_SCREENING.md` and the S012 scenario directory once frozen.

## 15. Stop for this journal entry

This entry stops at the S012 admission and evidence-freeze boundary.

Do not extend the journal with speculative architecture merely because the case exposes temporal artifact provenance. Future entries should be added only when subsequent broad-world screening contains a meaningful search path, rejection pattern, or reasoning pivot worth preserving.