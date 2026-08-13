# Cross-Candidate + Repository-Context Synthesis Pressure Test 01

**Date:** 2026-08-12  
**Status:** Completed bounded pressure test; non-controlling discovery/evaluation evidence  
**Branch:** `agent/product-simulation-case-screening-02`  
**Primary anchor:** S010 podcast-script / NumPy requirement broadening  
**Supporting contrasts:** S007–S009 and Candidate-Discovery Coverage Pressure Test 01

## 1. Owned question

The mature-system horizon leaves **cross-candidate + repository-context synthesis** open after candidate-specific A/B/C reasoning.

This pressure test asks:

> **What information must a future synthesis preserve so that several technical candidates, different candidate handling states, repository-context findings, discovery-coverage limits, and justified stopping do not collapse into one misleading scalar or premature maintainer action?**

This test does **not** design Conversation D, choose a final maintainer action, define a production schema, or create a scoring model.

## 2. Why S010 is the right anchor

S010 contains, inside one real proposal, all of the following:

```text
PROPOSAL
NumPy requirement broadened from <2 to <3

TECHNICAL CANDIDATE A
inaSpeechSegmenter v0.7.6 uses numpy.lib.pad
→ target protection at base = NumPy <2 guard
→ proposal removes that guard

TECHNICAL CANDIDATE B
pyannote viterbi generator → np.vstack compatibility issue
→ target-local compatibility shim already present

REPOSITORY/AUTOMATION CONTEXT
Dependabot semver-major ignore did not prevent requirement broadening

DISCOVERY COVERAGE LIMIT
two candidates are established enough for S010's purpose
but no claim that all NumPy-2 mechanisms were discovered
```

Any mature synthesis that loses one of those dimensions would distort the proposal state.

## 3. Shortcut under attack — one scalar “risk” or “compatibility” state

A tempting design is:

```text
candidate A = concerning
candidate B = mitigated
context finding = odd
→ aggregate score
→ one compatibility/risk label
```

That is unsafe because it destroys lineage and answerability.

For example, if the aggregate label were `medium risk`, the system could no longer explain:

- which mechanism remains exposed;
- which mechanism is locally mitigated;
- what the mitigation is;
- whether the proposal removes a guard;
- whether the repository automation itself is misaligned;
- what candidate-discovery blind spots remain;
- which unresolved questions were intentionally not investigated.

Therefore:

```text
useful synthesis
!=
early scalar collapse
```

## 4. Minimum information that survived the pressure test

A future synthesis must be able to preserve, conceptually, at least these responsibilities.

### 4.1 Proposal identity and proposal shape

S010 is a requirement broadening, not an exact installed-version transition.

The synthesis must not erase:

```text
<2 → <3
```

and replace it with an invented exact NumPy version.

### 4.2 Candidate set with stable mechanism identity

At least:

```text
Candidate A — np.lib.pad namespace removal
Candidate B — generator / np.vstack compatibility
```

These must remain independently addressable even though they share one dependency and runtime area.

### 4.3 Candidate-specific target state / handling

The synthesis must preserve the different target situations:

```text
A — compatibility guard exists at base and proposal removes it
B — local runtime compatibility shim exists
```

A future implementation may represent these facts differently; this pressure test does not require a `mitigation_state` enum.

### 4.4 Candidate-specific evidence and uncertainty

For each candidate, a reviewer must be able to distinguish:

- what is grounded;
- what is inferred;
- what remains unresolved;
- what evidence supports the state;
- what claim limits apply.

### 4.5 Repository-context findings outside technical applicability

S010's Dependabot requirement-broadening context must have somewhere to live without becoming Candidate C.

S009 independently strengthens the same separation with publication/reproducibility context.

Therefore:

```text
technical candidate set
+
material repository-context findings
```

is a more faithful synthesis surface than one universal candidate taxonomy.

### 4.6 Candidate-discovery coverage / blind spots

The synthesis must preserve:

```text
we discovered A and B
!=
we proved A and B are exhaustive
```

A broader later conclusion must know whether candidate discovery was:

- intentionally narrow;
- broad but bounded;
- limited by missing channels/evidence;
- sufficient only for a narrower claim.

### 4.7 Stopped questions and stop reasons

S010 intentionally did not execute the application or exhaustively enumerate NumPy 2 changes.

That is not missing work by default; it is a bounded stop for the owned question.

The synthesis must be able to preserve:

```text
question X unresolved
+
not investigated further
+
reason: cannot materially change the currently owned conclusion / outside admitted scope
```

without converting every unresolved item into an implicit to-do.

## 5. Candidate-specific resolution cannot automatically become proposal-level resolution

S007–S010 expose several ways this can fail.

### 5.1 One candidate eliminated

Suppose candidate C is established not applicable.

That means:

```text
C eliminated
```

not:

```text
proposal safe
```

unless the broader candidate set and discovery coverage justify that stronger conclusion.

### 5.2 One candidate mitigated

S010 Candidate B has a local compatibility shim.

That means the mechanism and mitigation remain material evidence.

It does not mean:

```text
all NumPy-2 concerns mitigated
```

or even:

```text
Candidate B can never regress
```

### 5.3 One candidate fully resolves the currently owned narrow question

S008 establishes a wheel-path transition and stops without source-building OpenCV.

That local result can be complete for its question while the whole dependency transition remains broader.

### 5.4 Repository context independently matters

S009 establishes a reproduction/provenance inconsistency without proving technical breakage.

Technical candidate resolution alone cannot erase that finding.

## 6. Synthesis should preserve an evidence vector before action projection

A useful conceptual pre-action state is closer to:

```text
proposal identity / shape

technical candidates
├── C1
│   ├── mechanism
│   ├── evidence / provenance
│   ├── candidate-specific state / handling
│   └── unresolved/stopped questions
├── C2
│   └── ...
└── Cn

repository-context findings
├── R1
└── ...

discovery coverage / blind spots

investigation history / stop reasons where material

remaining uncertainty
```

Only **after** preserving that structure should a later D-level responsibility consider overall evidence sufficiency, repository policy, residual uncertainty, and projection into the Charter's maintainer-facing actions.

This is a reasoning shape, not a requested runtime object graph.

## 7. Important non-equivalences

### CCS-01

```text
all currently known candidates resolved
!=
candidate discovery complete
```

### CCS-02

```text
candidate locally mitigated
!=
candidate absent
```

### CCS-03

```text
one applicable/unmitigated candidate
!=
automatic final action
```

The consequence severity, evidence sufficiency, other candidates, repository policy, CI/test evidence, and remaining uncertainty may still matter later.

### CCS-04

```text
repository-context finding
!=
technical applicability candidate
```

### CCS-05

```text
unresolved question
!=
mandatory further investigation
```

Question-specific stopping remains valid.

### CCS-06

```text
one aggregate scalar
!=
traceable synthesis
```

A scalar may someday be useful as a presentation/ranking aid, but it cannot replace the structured evidence state if doing so destroys causal/evidential lineage.

## 8. Ordering matters

A future system should avoid this order:

```text
candidate findings
→ aggregate score/action
→ attempt explanation afterward
```

because the explanation becomes post-hoc reconstruction.

The safer responsibility order is:

```text
preserve candidate/context evidence state
→ establish broader sufficiency/remaining uncertainty
→ apply admitted repository/policy relationship
→ project bounded maintainer-facing action
→ render explanation from preserved lineage
```

This is compatible with the existing evidence-first UpgradePilot doctrine and does not choose the exact D method.

## 9. Candidate relationship/deduplication pressure

S010 adds a specific cross-candidate problem:

```text
same dependency
+ same target subsystem
+ same broad major-version transition
```

does not imply two candidates are duplicates.

A future synthesis needs some way to preserve relationships such as:

- distinct;
- overlapping evidence;
- same root transition;
- one mitigation relevant to another;
- possible duplicate requiring review;

without double-counting or over-merging.

No relationship taxonomy is justified yet.

The durable requirement is simpler:

> Candidate relationship handling must not destroy materially different mechanism identity or evidence lineage.

## 10. Repository-context synthesis pressure

S009 and S010 show two different context shapes:

### S009

```text
repository purpose = reproduce published analysis
+ publication pin changed
+ provenance wording unchanged
→ reproduction/provenance inconsistency
```

### S010

```text
Dependabot configuration intended to constrain major updates
+ requirement broadening still proposed
→ automation/review-context tension
```

Neither should be forced into technical applicability.

Yet later overall synthesis may need them because they alter what evidence/action is appropriate for the repository.

Therefore repository-context findings should remain:

- evidence-backed;
- explicitly scoped;
- separately typed conceptually from technical candidates;
- available to later D-level reasoning only when that responsibility is admitted.

## 11. Evaluation implications

Future cross-candidate/synthesis evaluation should test at least these failure modes.

### 11.1 Candidate erasure

Does resolving or mitigating one candidate cause another candidate to disappear from the synthesis?

### 11.2 Over-merge

Does the system collapse materially different mechanisms because they share one dependency/path/category?

### 11.3 Double counting

Does the system count one mechanism twice because multiple evidence sources describe the same technical fact?

### 11.4 Context coercion

Does repository-purpose/policy evidence get misclassified as technical applicability?

### 11.5 Coverage overclaim

Does `all discovered candidates resolved` become `no material impact` without candidate-discovery coverage?

### 11.6 Unresolved-to-action shortcut

Does one unresolved item automatically force `run targeted checks` even when the question was legitimately stopped or irrelevant to the overall owned conclusion?

### 11.7 Explanation reconstruction

Can every synthesis statement traverse backward to candidate/context evidence and exact proposal identity without relying on an opaque final model assertion?

## 12. What this does NOT justify

Do not derive from this pressure test:

- a production `SynthesisState` schema;
- a universal candidate relationship enum;
- a risk score;
- weighting candidates numerically;
- severity aggregation rules;
- Conversation-D closure;
- one final maintainer action for S010;
- policy inference from repository text without evidence boundaries;
- implementation changes in the current B2 slice.

## 13. Main-thread handoff decision

**No immediate handoff is required.**

Current main's mature-system horizon already identifies cross-candidate + repository-context synthesis as open design. This pressure test supplies sharper evaluation obligations and failure modes but does not expose a contradiction in currently implemented behavior.

A handoff becomes high-value when main explicitly opens:

- cross-candidate synthesis design;
- Conversation D / overall sufficiency;
- candidate relationship/deduplication;
- repository-context/policy admission;
- maintainer-action projection.

At that point S009 and S010 should be primary adversarial anchors.

## 14. Stop

Pressure Test 01 is complete.

The next productive Cycle-02 move is **not more prose about synthesis**. Prefer either:

1. a new real-world screening pass specifically for candidate overlap/deduplication or context + technical coexistence; or
2. wait for main to open synthesis/D and then transfer-test the implementation against S009/S010.

Do not create a production synthesis model from this file.