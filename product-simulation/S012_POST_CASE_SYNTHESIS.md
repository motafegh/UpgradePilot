# S012 Post-Case Synthesis — Historical Artifact Provenance and Cross-Version Persistence

**Date:** 2026-08-12  
**Status:** Completed bounded synthesis; non-controlling discovery/evaluation evidence  
**Scenario:** [`scenarios/S012-freqtrade-sklearn-persisted-artifact-version-boundary/README.md`](scenarios/S012-freqtrade-sklearn-persisted-artifact-version-boundary/README.md)  
**Product context inspected:** `main@1c7f7a79f7f2b56a572e6c460cdb7f11b7f654d4`

## 1. Result

S012 establishes a real history-dependent technical applicability boundary without claiming a concrete FreqAI failure.

Exact proposal:

```text
Freqtrade FreqAI / hyperopt requirements
scikit-learn 1.7.2
→
scikit-learn 1.8.0
```

Exact target behavior:

```text
past run
→ persist model / feature pipeline / label pipeline
→ later run
→ reuse model identifier
→ reload persisted state
```

Supported pipeline shape:

```text
FreqAI pipeline
→ may contain scikit-learn transforms
→ pipeline persisted through cloudpickle
```

Authoritative upstream boundary:

```text
scikit-learn 1.7.2 persisted state
→ loading under a different scikit-learn version is unsupported
```

Therefore:

```text
current source + current dependency environment
!=
complete applicability context
```

when the target intentionally consumes state produced by an earlier dependency environment.

## 2. New durable distinction — fresh state versus persisted state

S012 adds a technical distinction not isolated by the earlier cases:

```text
FRESH-STATE COMPATIBILITY
updated dependency + state created under updated environment
```

versus:

```text
PERSISTED-STATE COMPATIBILITY
updated dependency + state created under earlier environment
```

A system can succeed in the first condition while the second remains unresolved or unsupported.

Therefore:

```text
fresh install succeeds
+
fresh training succeeds
+
fresh-state tests succeed
```

would not automatically prove:

```text
old persisted model/pipeline is supported under the updated dependency
```

This is proposition separation, not a claim about Freqtrade's actual CI outcome.

## 3. Artifact provenance can be technical applicability evidence

S009 established that repository provenance/reproducibility can be decision-relevant context without automatically becoming technical applicability.

S012 shows a different role for provenance.

For persisted Python object state, the producer environment can directly affect whether the consumer environment is supported.

The relevant identity can therefore be:

```text
artifact identity
+
producer dependency version/environment
+
consumer dependency version/environment
+
reuse/selection path
```

Producer-version provenance is not decoration in this mechanism. It helps determine whether the cross-version persistence proposition is activated.

This does not mean every product decision needs a universal provenance model.

## 4. Current repository identity can be insufficient target context

Much of dependency-update analysis naturally starts from:

```text
proposal
+
exact target base/head revision
+
current target environment
```

S012 demonstrates a bounded case where that can still leave a material proposition unresolved.

The artifact selected by the target may predate the current repository revision and current dependency environment.

Therefore:

```text
exact current revision
```

remains necessary, but is not always sufficient to describe all active target state.

This is not permission to reconstruct unlimited history. Historical evidence should be acquired only when a candidate mechanism makes it necessary.

## 5. Producer and consumer version are separate facts

A common simplification would be to attach one dependency version to the whole evaluation context.

S012 shows why that can be wrong for persisted state:

```text
producer environment: scikit-learn 1.7.2
consumer environment: scikit-learn 1.8.0
```

Both can be true at the same time because the artifact survives the environment transition.

The technical question exists **because** the two version identities differ.

A future product method handling this mechanism must preserve that asymmetry rather than normalizing all evidence onto only the current dependency version.

## 6. Artifact-history absence is not negative evidence

The repository can establish that old-state reuse is supported, but it cannot establish the persisted artifact inventory of every deployment.

Therefore:

```text
no artifact-history evidence in repository
```

must not become:

```text
no old artifact exists
```

For a concrete deployment, propositions such as these may remain unresolved:

- does a persisted artifact exist?
- does it contain scikit-learn-owned state?
- which scikit-learn version produced it?
- will the current identifier/config select it after the update?

This is a direct extension of the existing negative-evidence doctrine into durable runtime state.

## 7. Activation can cross execution boundaries

Earlier activation examples mostly concern conditions observable within a current environment or current invocation.

S012 adds a cross-execution shape:

```text
T1: produce state under dependency version A
↓ persisted artifact survives
T2: update dependency to version B
↓
T3: select and consume T1 state under version B
```

The activation condition is therefore partly historical.

This does not require a general temporal logic engine. It establishes that a candidate-specific proposition may refer to a prior producer context when the mechanism demands it.

## 8. Target relevance can include state outside the repository tree

S012 reinforces the broader exposure-as-relationship/path principle.

The relevant target object is not source code alone. The relationship is:

```text
FreqAI producer code
→ persisted model/pipeline artifact
→ FreqAI consumer code
```

The artifact can live outside the repository while still being part of the target-relevant technical path.

Thus:

```text
not stored in Git
!=
not target-relevant
```

when the target explicitly produces and consumes that state.

## 9. Investigation implications — provenance-matched checks

If a later decision needs actual consequence evidence, a generic fresh-state check would be weakly discriminating for this mechanism.

The useful experiment would need to preserve the relevant provenance:

```text
representative artifact created under exact old dependency environment
→ preserved unchanged
→ consumed under exact proposed environment
→ observe warning/load/behavior outcome
```

That is a **provenance-matched** targeted check.

The principle is:

```text
check setup must instantiate the candidate's activation conditions
```

not merely execute nearby code under the new dependency.

## 10. Why no dynamic check was run

The owned question was applicability/provenance, not concrete failure.

Static target evidence establishes:

- the persisted producer/consumer path;
- intentional cross-run reuse;
- supported scikit-learn content inside persisted pipelines.

Authoritative upstream evidence establishes:

- cross-version scikit-learn persistence is unsupported.

Therefore the proposition:

> old scikit-learn-containing artifact reused after the dependency update creates a real version-sensitive compatibility boundary

is already sufficiently grounded.

A dynamic reproduction would move to:

> what happens to this exact selected artifact?

That is a different question.

The decision to stop is therefore evidence-based pruning rather than lack of ambition.

## 11. Relation to S007 and S008

S007 established that an earlier environment-formation contradiction can make deeper runtime testing unnecessary.

S008 established that package compatibility must distinguish wheel availability, source fallback, and source-build success.

S012 adds another artifact category:

```text
INSTALLATION ARTIFACT
package wheel / source distribution
```

versus:

```text
TARGET PERSISTED ARTIFACT
model / pipeline / durable runtime state produced by the target
```

The word `artifact` therefore does not define one universal technical responsibility. Artifact roles remain mechanism-specific.

## 12. Relation to S009

S009's provenance concern is about repository purpose and reproducibility context.

S012's provenance concern is technical:

```text
which dependency version created the object state?
```

The same broad term `provenance` can therefore participate in different decision-model roles.

A future implementation should not collapse them merely because the vocabulary overlaps.

## 13. Relation to S011

S011 established:

```text
optional dependency declared
!=
optional environment formed
!=
runtime activated
```

S012 establishes a later distinction:

```text
current environment formed successfully
!=
historical artifact compatible with that environment
```

These can compose in future real cases, but no combined generic model is warranted from the current corpus alone.

## 14. Candidate-discovery implications

A discovery system focused only on current source API calls may miss S012-like concerns.

Potential bounded evidence inputs, when a persistence mechanism is actually discovered, include:

- save/load code paths;
- model/cache/state reuse documentation;
- artifact naming/selection identifiers;
- persistence format/library;
- producer dependency metadata if available;
- current consumer dependency version;
- explicit migration/retraining behavior.

Do not scan every repository for arbitrary historical files merely because persisted-state cases exist.

A reasonable activation for deeper discovery is first establishing a real durable producer/consumer path.

## 15. Evaluation implications

S012 is a future evaluation anchor for these failure modes.

### 15.1 Current-state erasure

Does the system assume the exact current repository revision contains all target-relevant state?

### 15.2 Producer/consumer version collapse

Does it assign only the proposed/current dependency version to an artifact created under the old version?

### 15.3 Missing-history false negative

Does unavailable artifact provenance become `not applicable` rather than `unresolved`?

### 15.4 Fresh-test overclaim

Does successful fresh-state execution get treated as evidence for historical artifact compatibility without instantiating the old artifact?

### 15.5 Generic-check mismatch

If execution is needed, does the selected check reproduce the relevant producer/consumer version boundary, or merely exercise current code?

### 15.6 Artifact-role collapse

Does the evaluator conflate package installation artifacts, generated build artifacts, and target-persisted runtime state into one undifferentiated artifact concept?

## 16. Relation to current main design

Current main explicitly broadens the B2 responsibility horizon beyond the first Python-support fixture and expects materially different real-case pressure before consequential abstractions are frozen.

S012 fits that role as transfer/adversarial evidence.

It does **not** justify changing the current immediate implementation route by itself. Main currently prioritizes completing the first real investigation loop, pressure-testing architecture against existing diverse cases, and then introducing a second mechanism through evidence-earned implementation.

S012 should become active product input only when a concrete architecture/implementation decision touches:

- historical target state;
- persisted artifact compatibility;
- producer/consumer version identity;
- artifact-provenance evidence acquisition;
- provenance-matched investigation design.

Until then it remains durable non-controlling simulation evidence.

## 17. Main-thread handoff decision

**No immediate implementation handoff is required.**

Creating a new handoff now would duplicate information without a current product owner asking this question.

A handoff becomes useful when main reaches a specific design seam where current-revision-only context or artifact identity would otherwise be frozen too narrowly.

At that point S012 should be considered alongside S008, S009, S011, and the relevant current implementation evidence.

## 18. Claim limits

Do not infer from S012 that:

- scikit-learn 1.8.0 breaks Freqtrade;
- all FreqAI models/pipelines contain scikit-learn state;
- every deployment has old artifacts;
- every old artifact fails or even warns;
- current Freqtrade CI is inadequate;
- the merged PR was technically wrong;
- all dependency updates with caches/models require artifact migration;
- UpgradePilot should retain arbitrary historical state;
- a generic provenance graph, temporal engine, or artifact schema is justified.

## 19. Stop

S012 is complete at its admitted depth.

The durable result is:

```text
real dependency update
+
intentional durable producer/consumer target path
+
persisted state can contain dependency-owned objects
+
authoritative cross-version persistence boundary
→ artifact producer-version/provenance can be a necessary applicability input
→ concrete deployment history may remain unresolved
→ dynamic consequence testing pruned for this owned question
```

Do not extend the case unless a later product/evaluation question specifically requires artifact-specific consequence evidence or history-dependent applicability transfer.