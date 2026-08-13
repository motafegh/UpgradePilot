# S010 Post-Case Synthesis — Discovery Breadth, Guards, and Per-Candidate Handling

**Date:** 2026-08-12  
**Status:** Completed bounded synthesis; non-controlling discovery/evaluation evidence  
**Scenario:** [`scenarios/S010-podcast-script-numpy-discovery-breadth/README.md`](scenarios/S010-podcast-script-numpy-discovery-breadth/README.md)  
**Product context inspected:** `main@538c5c1ae56ddcd60e1e9bcf0a8a2c6d22b90471`

## 1. Result

S010 answers its owned question positively.

One real NumPy requirement-broadening proposal contains at least two independently grounded compatibility mechanisms on the same transitive runtime area, and the exact target handles those mechanisms differently.

```text
proposal
numpy >=1.26,<2.0
→ numpy >=1.26,<3.0

runtime area
podcast-script
→ inaSpeechSegmenter 0.7.6
→ NumPy-dependent segmentation stack
```

Candidate A:

```text
inaSpeechSegmenter v0.7.6 feature framing
→ numpy.lib.pad
→ NumPy-2 np.lib surface no longer retains pad
→ target protection at base = NumPy <2 guard
→ proposal removes that guard
```

Candidate B:

```text
inaSpeechSegmenter dependency path
→ pyannote viterbi generator-style values
→ np.vstack compatibility issue
→ target executes local list-materializing compatibility shim
→ separately mitigated mechanism
```

Therefore:

```text
first valid candidate found
!=
discovery complete
```

and:

```text
same transition
+ same transitive runtime area
!=
same mechanism
!=
same target handling state
```

## 2. Candidate discovery breadth is independent from candidate applicability/state

S010 sharpens `CANDIDATE_DISCOVERY_COVERAGE_PRESSURE_TEST_01.md` with real evidence.

A discovery process could find Candidate A first and correctly identify it as material. That would still not justify stopping transition-level discovery if the attempted conclusion requires broader coverage, because Candidate B exists independently.

Conversely, Candidate B being locally mitigated does not erase it from the discovered candidate set. Its state belongs to later candidate-specific evaluation.

The correct separation is approximately:

```text
DISCOVERY
What materially distinct mechanisms are justified enough to consider?

↓

CANDIDATE-SPECIFIC EVALUATION
For each mechanism, what target relation / activation / mitigation / applicability state is established?
```

A discovery layer that filters out already-mitigated mechanisms too early can lose useful evidence about target adaptations and future regression obligations.

## 3. A version constraint can be a target mitigation/guard

S010 adds a useful interpretation of dependency declarations.

A version constraint is not always merely package-management configuration.

In this case:

```text
numpy <2
```

is explicitly documented by the target as a compatibility guard around a known transitive runtime incompatibility.

Therefore the proposal's technical meaning is not only:

```text
allowed version range changed
```

It can also be:

```text
existing mitigation boundary weakened/removed
```

This suggests a mature target-driven discovery process may eventually need to distinguish:

- ordinary dependency declaration;
- compatibility guard / exclusion;
- environment/policy pin;
- repository-purpose pin such as S009;

when exact target evidence justifies that interpretation.

This is not a frozen taxonomy and should not become a generic enum solely from S010.

## 4. Candidate deduplication must be mechanism-aware

A naive deduplication rule might collapse both findings because they share:

- NumPy 2;
- inaSpeechSegmenter/segmentation;
- a broad `compatibility` label.

That would be technically wrong.

The candidates differ in:

- exact upstream/transitive operation;
- failure/behavior mechanism;
- target mitigation;
- evidence lineage;
- what future evidence would reevaluate them.

Therefore any future candidate deduplication/relationship handling must preserve materially distinct mechanism identity rather than grouping solely by dependency, target file, transitive path, or high-level category.

S010 does **not** prove what the mature deduplication algorithm should be.

## 5. Local mitigation does not mean candidate disappearance

Candidate B is important precisely because the target already contains a compatibility shim.

That gives a useful distinction:

```text
mechanism absent / non-applicable
!=
mechanism applicable but locally mitigated
```

Those states have different implications for:

- explanation;
- regression testing;
- future removal of the shim;
- later dependency upgrades;
- confidence in a broader update conclusion.

The current A/B implementation does not need to add a generic `mitigated` state from this case. The narrower lesson is that candidate formulation and later synthesis should not erase an applicable/relevant mechanism merely because target code contains a mitigation.

## 6. Requirement broadening is a distinct proposal shape worth preserving

S010 is not an exact old-version → proposed-version transition.

The proposal changes:

```text
allowed range <2
→ allowed range <3
```

A fresh resolver may select any compatible version in that larger domain.

That creates an important identity distinction:

```text
exact version update
!=
constraint broadening that admits a new major-version family
```

The technical candidate can still be grounded against the newly admitted family boundary, but exact runtime consequence may require a later exact resolution/evidence state.

Do not silently normalize every requirement-broadening PR into one invented exact proposed version.

## 7. Repository automation context remains separate

The PR discussion indicates the repository had a Dependabot semver-major ignore but still received this requirement-broadening proposal.

That supports:

```text
update-generation policy
!=
review-time technical suitability
```

and:

```text
version-update suppression
!=
requirement-broadening suppression
```

But this is repository/automation context, not a third NumPy technical impact candidate.

S010 therefore reinforces S009's lesson that material context findings may coexist with technical candidates without being forced into the same candidate taxonomy.

## 8. Discovery coverage remains bounded

S010 intentionally does **not** claim that Candidate A and Candidate B are the complete NumPy-2 candidate set for podcast-script.

NumPy 2.0 also changes many other Python API, promotion, copy, ABI/C-API, and behavior surfaces.

The bounded claim is:

> At least two materially distinct, independently grounded mechanisms exist in this real proposal and target context, and they have different target handling states.

That is sufficient to falsify:

```text
one valid candidate found
→ discovery complete
```

It is not sufficient to assert universal candidate recall.

## 9. Evaluation implications

S010 is a strong future evaluation anchor for broad candidate discovery.

Useful tests derived from it include:

### 9.1 Secondary-mechanism recall

Given evidence sufficient to discover Candidate A, does the method continue far enough to discover Candidate B when the broader coverage claim requires it?

### 9.2 Candidate over-merge test

Does the method collapse both candidates into one generic NumPy/inaSpeechSegmenter compatibility item?

### 9.3 Per-candidate target-state preservation

Can later evaluation preserve:

```text
A → protected by version guard that proposal removes
B → target-local compatibility shim already present
```

without converting this into one scalar compatibility score?

### 9.4 Mitigation-aware explanation

Can the system distinguish:

```text
mechanism not present
vs
mechanism present but mitigated
```

when exact target evidence supports the latter?

### 9.5 Proposal-shape test

Can the product preserve requirement broadening as a range change rather than hallucinating one exact proposed version?

## 10. Relation to current main design

S010 does not contradict the implemented A/B foundation.

It strengthens two responsibilities already left open in the mature-system horizon:

1. broad candidate discovery before mechanism-specific A/B evaluation;
2. candidate-discovery coverage for broader conclusions.

It also gives concrete future pressure for the open candidate deduplication/relationship problem.

No current source change is justified solely from S010 because broad candidate discovery is not yet an admitted implementation responsibility in the current bounded B2 slice.

## 11. Conversation-C/stopping lesson

No dynamic execution was needed for S010's owned question.

Static exact evidence already distinguishes the two mechanisms and target handling states.

A resolver run or application execution would answer different questions, for example:

- which NumPy 2 release actually resolves in one environment;
- whether the segmentation path reaches Candidate A for a chosen input;
- whether all local shims collectively make the runtime stack work.

Those are valid future questions only if separately admitted.

Therefore:

```text
unresolved behavioral consequence
!=
automatic reason to execute
```

when the current discovery/evaluation question is already resolved.

## 12. Main-thread handoff decision

**No immediate architecture or implementation handoff is required.**

Reason:

- current main already identifies broad candidate discovery and candidate-discovery coverage as open mature-system responsibilities;
- S010 strengthens those responsibilities rather than exposing a contradiction in current implementation;
- candidate deduplication/relationship handling is already recognized as open;
- forcing S010 into the current B2 implementation would expand scope prematurely.

Preserve S010 as a high-value evaluation/transfer anchor for the point when broad discovery or cross-candidate handling is legitimately admitted.

A future handoff becomes useful if main begins to define:

- candidate-discovery output contracts;
- candidate deduplication/relationship handling;
- discovery-coverage claims;
- mitigation/context handling in cross-candidate synthesis.

## 13. Claim limits

Do not infer from S010 that:

- NumPy 2 is globally incompatible with podcast-script;
- every permitted fresh resolution selects NumPy 2;
- Candidate B's local shim guarantees compatibility;
- Candidate A and B are exhaustive;
- the exact historical pyannote source revision was reconstructed;
- the PR should be blocked or merged;
- UpgradePilot already has a complete candidate-discovery method.

## 14. Stop

S010 is complete at its admitted depth.

Do not extend it into exhaustive NumPy-2 migration work, full lock-graph reconstruction, or runtime execution unless a future distinct question explicitly needs that evidence.