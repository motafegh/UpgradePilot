# Implemented Foundation Transfer Evaluation — S006/S007 Against the First A/B Runtime Slice

**Date:** 2026-08-11  
**Status:** Completed bounded post-implementation transfer evaluation; non-controlling discovery/evaluation evidence  
**Product revision inspected:** `main@6202548eeff8c76405b8b53e0e35f0caeef53ef3`  
**Simulation evidence:** S006, S007, Conversation-C Pressure Test 01, and the earlier challenge cases  

## 1. Purpose

This evaluation asks a narrower question than the earlier pre-implementation Conversation-C handoff:

> Now that UpgradePilot has implemented its first mechanism-specific technical impact candidate and candidate-specific applicability state, do the resulting machine contracts preserve the important lessons from S006/S007, and what concrete evaluation obligations remain for the first runtime investigation-selection slice?

This file does **not** propose a new product plan, reopen Conversations A/B/C, request PyTorch/OpenCV support, define a generic investigation planner, or state the live project continuation.

## 2. Product behavior inspected

The inspected implementation separates two layers.

### Reusable bounded applicability composition

`src/upgradepilot/impact/applicability.py` represents:

- proposition state: `established | refuted | unresolved | conflicted`;
- proposition evidence coverage;
- conjunctive applicability paths;
- path-model coverage;
- candidate-level applicability while retaining path results.

Its deterministic composition preserves these important rules:

```text
one refuted necessary proposition
→ conjunctive path refuted

one complete established path
→ candidate established applicable

all represented paths refuted
+ sufficient path-model coverage
→ candidate established not applicable

all represented paths refuted
+ insufficient/unresolved path-model coverage
→ candidate remains unresolved
```

It deliberately does not implement candidate-discovery completeness, final maintainer action, numerical scoring, or a generic Boolean/rule engine.

### Mechanism-specific Python-support candidate

`src/upgradepilot/impact/python_support.py` keeps the first impact-candidate family specific to an authoritative Python-support drop.

Candidate construction establishes the grounded upstream mechanism but does not self-authorize target exposure or activation. Exact target/dependency identity is preserved. Candidate-specific applicability can be evaluated both:

```text
before exact target evidence acquisition
→ target declaration proposition unresolved
→ evidence coverage insufficient
→ activation unresolved
→ candidate unresolved
```

and after exact target evidence is available.

This is behavior-tested in `tests/test_impact_applicability.py` and `tests/test_python_support_impact.py`.

## 3. Transfer result A — the implementation does not overfit S001 into a universal engine

**Result: supported.**

The reusable layer contains only the state/composition machinery that multiple cases actually need. The package-specific impact formulation remains separate.

That is consistent with the simulation lesson:

```text
reusable reasoning responsibility
!= universal impact detector
```

S007 therefore does **not** imply that the current runtime should add a generic package-family candidate, dependency graph, PyTorch analyzer, wheel resolver, or artifact schema merely because its evidence can be described with the same proposition/path concepts.

The current split is the preferred direction:

```text
generic bounded proposition/path composition
+
mechanism-specific candidate/evidence adapters only when a real product responsibility is admitted
```

## 4. Transfer result B — S007 can be represented semantically without being implemented as a product capability

**Result: supported at the model level; not implemented as an admitted mechanism.**

S007's bounded package-family question can be expressed conceptually with the current composition semantics:

```text
P1 exact proposal declares torch==2.8.0                       established
P2 retained torchvision package contract requires Torch 2.6 established
P3 one coherent Torch version can satisfy both               refuted

necessary package-family path contains P3
→ path refuted
```

But the current product has no admitted runtime responsibility for:

- generating this package-family impact candidate;
- acquiring the required Torch/TorchVision build metadata generically;
- establishing package-family path-model coverage;
- converting that evidence into the proposition assessments above.

That absence is currently **correct scope discipline**, not an implementation defect.

S007 is therefore transfer/evaluation evidence for future mechanism admission, not a request to widen the present B2 slice.

## 5. Transfer result C — S006 remains a valid opposite investigation-selection control

S006 demonstrates a case where static evidence leaves the exact behavior proposition unresolved and a bounded old/new differential execution has unique discriminating value.

```text
S006
static evidence insufficient for exact behavior
→ targeted execution worth selecting
```

S007 demonstrates the opposite:

```text
S007
new authoritative static evidence resolves the owned proposition
→ previously plausible resolver execution becomes redundant
→ no further check for that owned question
```

Together they remain a strong paired control for the future runtime investigation-selection responsibility.

The current product does not need a generic differential-test executor to preserve this lesson. The transferable requirement is about **selection validity**, not universal execution capability.

## 6. New post-implementation evaluation obligation — selected investigations must be revalidated before execution

The inspected main revision can represent pre-acquisition unresolved applicability, but runtime discriminating-investigation selection is not yet implemented.

S007 contributes one concrete regression condition for that future runtime slice:

```text
T1
proposition P unresolved
→ investigation I is justified and selected

T2, before I executes
new admitted evidence E resolves/refutes P
OR closes the necessary path I was meant to discriminate

→ I must be re-evaluated
→ I must not execute merely because it was selected earlier
```

This is distinct from the already-recognized failed-check rule:

```text
I executed/attempted and failed
→ do not select identical I again without concrete retry justification
```

The S007 condition is instead:

```text
I has not executed
+ its epistemic value disappears because evidence state changed
→ prune/cancel I
```

No queue, cancellation service, event-sourcing system, or runtime enum follows from this observation. A first implementation may satisfy it with a much smaller invariant: selection/execution must be validated against the proposition/evidence state it is supposed to discriminate.

## 7. Three C-runtime contrasts worth preserving in evaluation

The existing corpus now supplies three materially different conditions for investigation-selection tests.

### C1 — evidence not yet acquired

```text
exact target declaration not yet acquired
→ target-declaration proposition unresolved
→ exact declaration is the discriminating target
→ supported read-only acquisition can be selected
```

This is the natural first runtime activation in the current Python-support anchor.

### C2 — acquisition already failed/unavailable

```text
same exact acquisition already attempted
+ failure/unavailability preserved
→ unresolved remains unresolved
→ identical acquisition is not a fresh next check without retry justification
```

This protects against blind retry loops.

### C3 — selected check becomes stale before execution

```text
check selected while P unresolved
+ different admitted evidence resolves/closes P before execution
→ selected check loses discriminating value
→ prune/re-evaluate before execution
```

S007 is the canonical current simulation example.

These three states should not be collapsed into one `uncertain → acquire evidence` behavior.

## 8. No-further-check meaning remains proposition-relative

S007 and Buildtest/OpenSSL still show why an operationally similar result can have different epistemic meaning.

```text
S007:
proposition resolved
→ no further check needed
```

versus:

```text
Buildtest/OpenSSL:
proposition unresolved
+ no sufficiently scoped/authoritative useful investigation remains
→ no further check available/justified
→ unresolved preserved
```

A future runtime surface may or may not need distinct enums for these reasons. The requirement is only that the explanation and underlying proposition state not be erased.

## 9. Confirmation from the current tests

The current source/tests already preserve several simulation-derived safeguards:

- candidate creation does not establish its own exposure/activation;
- pre-acquisition missing evidence is explicitly unresolved rather than negative evidence;
- an acquisition problem is distinguishable from evidence not yet requested;
- unsupported comparison is distinguishable from missing target evidence;
- exact target revision mismatch is rejected;
- a grounded candidate cannot consume unresolved upstream state;
- refuting one necessary proposition eliminates a conjunctive path;
- all represented paths refuted is insufficient for candidate-level non-applicability without sufficient path-model coverage;
- path-level conflict/unresolved state is preserved when candidate state is composed.

This is strong evidence that the A/B decisions have successfully crossed from design prose into machine state and executable invariants.

## 10. What this evaluation does not justify

Do not infer from this evaluation that UpgradePilot should now implement:

- S007/PyTorch package-family analysis;
- CARLA/OpenCV behavior analysis;
- universal package-resolution reasoning;
- arbitrary dependency graphs;
- a generic investigation planner;
- a generic differential executor;
- numerical Value-of-Information scoring;
- final maintainer action or Conversation-D semantics.

Those require their own admitted product responsibility and evidence.

## 11. Bounded conclusion

The first implemented A/B foundation survives the S006/S007 transfer check well.

```text
SIMULATION LESSONS
        ↓
small reusable proposition/path machine state
+ mechanism-specific candidate adapter
        ↓
implemented + tested without universalizing the cases
```

No corrective redesign is indicated by S006 or S007 at this revision.

The main new regression/evaluation obligation contributed by S007 is:

> **A selected investigation must remain discriminating for the current admitted proposition/evidence state at execution time; selection at an earlier state is not permanent authorization to execute.**

This is non-controlling discovery/evaluation evidence for future implementation and review.