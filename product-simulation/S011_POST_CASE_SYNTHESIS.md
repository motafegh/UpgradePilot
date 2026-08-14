# S011 Post-Case Synthesis — Optional Dependency Activation and CI Environment Coverage

**Date:** 2026-08-12  
**Status:** Completed bounded synthesis; non-controlling discovery/evaluation evidence  
**Scenario:** [`scenarios/S011-dictare-mlx-optional-extra-ci-coverage/README.md`](scenarios/S011-dictare-mlx-optional-extra-ci-coverage/README.md)  
**Product context inspected:** `main@538c5c1ae56ddcd60e1e9bcf0a8a2c6d22b90471`

## 1. Result

S011 establishes a real optional-dependency activation/coverage gap without claiming dependency incompatibility.

Exact proposal:

```text
Dictare optional [mlx] group
numpy==1.26.4
→
numpy==2.4.6
```

Exact target reality:

```text
Apple-Silicon development install
→ --extra mlx

optional group installed
+ macOS arm64
+ mlx_whisper discoverable
+ hardware acceleration enabled
→ MLXWhisperEngine selected
→ mlx / mlx_whisper / NumPy participate in runtime
```

Inspected test workflows:

```text
standard PR workflow
→ Ubuntu
→ pip install -e .[dev]

macOS test workflow
→ macos-latest
→ pip install -e .[dev]
```

Neither installs `.[mlx]`.

Therefore:

```text
platform-specific test workflow exists
!=
affected optional dependency environment exists
```

and:

```text
workflow success, if observed
!=
compatibility evidence for the MLX optional stack
```

## 2. New durable distinction — environment formation precedes behavior coverage

Earlier cases established:

- S002 — relevant tests may be skipped;
- S006 — broad test coverage may miss a discriminating behavior path;
- S008 — CI may install the same package but exercise a different artifact-selection branch.

S011 adds an earlier prerequisite:

```text
DEPENDENCY ENVIRONMENT FORMED?
Was the optional dependency family installed/resolved at all?

↓ only if yes

RUNTIME ACTIVATION CONDITIONS SATISFIED?
Platform / hardware / config / selection

↓ only if yes

BEHAVIOR PATH EXERCISED?
Did tests/checks reach the relevant behavior?
```

These are separate coverage questions.

A test suite cannot provide direct evidence about a dependency environment it never constructs.

## 3. Optional dependency declaration is not runtime presence

The target `pyproject.toml` contains NumPy inside `[project.optional-dependencies].mlx`.

That proves the dependency is part of an admitted installation mode.

It does **not** prove the package is installed in:

- a default installation;
- the standard CI environment;
- the macOS test environment;
- every user environment.

Therefore:

```text
optional dependency declared
!=
optional dependency installed
```

This is a machine-actionable applicability distinction.

A future product can represent the dependency declaration as evidence for a possible target relationship while leaving installation/activation propositions separate.

## 4. Platform match is not sufficient activation evidence

The dedicated macOS workflow is particularly valuable as a counterexample.

A simplistic evaluator could reason:

```text
MLX is macOS/Apple-Silicon related
+ macOS CI exists
→ relevant coverage exists
```

S011 falsifies that shortcut.

The workflow installs only `.[dev]`, so the MLX family is absent.

Additionally, the runtime's own availability check requires `darwin`, `arm64`, and discoverable `mlx_whisper`.

Thus:

```text
platform family matches
!=
exact platform/hardware condition proven
!=
optional package installed
!=
runtime engine selected
```

Those propositions may share evidence, but they are not interchangeable.

## 5. Activation can be compositional without requiring a universal logic engine

S011 gives a concrete real-world activation shape:

```text
(optional extra installed)
AND
(macOS arm64)
AND
(mlx_whisper discoverable)
AND
(hardware acceleration enabled)
AND
(not selecting a different model family)
→ MLX runtime path
```

This supports the Conversation-B observation that activation may be compositional.

It does **not** justify implementing a generic Boolean-expression engine merely because one case contains conjunctions.

A future bounded capability should use the minimum representation needed by the admitted mechanism.

## 6. CI coverage is proposition-relative, not workflow-name-relative

S011 reinforces a broader principle:

```text
"macOS tests"
```

is a workflow label, not an evidence conclusion.

For the proposition:

> Does the changed MLX optional dependency family install and participate successfully?

an adequate check must first form that environment.

For a different proposition, such as:

> Does core audio capture work on macOS?

the same `ci-macos.yml` workflow may be highly relevant.

Therefore a workflow can be:

```text
relevant evidence for proposition P1
and
non-discriminating for proposition P2
```

without contradiction.

## 7. Coordinated optional families add context without proving incompatibility

The exact `mlx` extra uses many exact pins and documents coordinated-version intent.

An adjacent Dependabot PR independently attempted to update `mlx` itself.

This suggests a real review concern:

```text
independent bot proposal against family member
+
coordinated family intent
→ family-coherence question may be justified
```

But S011 does not establish that NumPy 2.4.6 is incompatible with the other pinned versions.

The correct state is:

```text
coordinated-family context established
technical incompatibility unresolved/not investigated
```

That context may later help candidate discovery or synthesis, but it must not self-authorize an incompatibility claim.

## 8. Negative evidence rule for CI

S011 provides a useful negative-evidence boundary.

From exact workflow definitions we can establish:

```text
these inspected workflows do not install [mlx]
```

That is bounded negative evidence because the installation commands are explicit within the inspected workflow scope.

We cannot infer:

```text
no CI or automation anywhere ever installs [mlx]
```

without a complete relevant workflow/evidence boundary.

Therefore:

```text
closed-world reasoning can be valid locally
without becoming a repository-global closed world
```

This is consistent with Conversation B's proposition-specific completeness doctrine.

## 9. Candidate discovery implications

A future candidate-discovery system that only scans default dependencies may miss S011 entirely.

Potential discovery inputs include:

- optional dependency groups;
- environment markers;
- repository installation instructions;
- runtime feature/back-end selection;
- hardware/platform detection;
- exact CI installation commands.

But S011 does not justify scanning every extra for every proposal unconditionally.

The discovery need is claim-relative:

> If the dependency transition occurs inside optional group X, is X a real supported/reachable target environment, and what activates it?

That is much narrower than generic whole-repository environment reconstruction.

## 10. Evaluation implications

S011 is a future evaluation anchor for at least these failure modes.

### 10.1 Optional-extra erasure

Does the system treat an optional dependency as irrelevant merely because it is not in the default install?

### 10.2 Declaration-to-presence shortcut

Does the system assume the package is installed because it is declared in an extra?

### 10.3 Platform-label shortcut

Does the presence of a macOS workflow get treated as evidence for the Apple-Silicon MLX path without checking installation/hardware conditions?

### 10.4 CI-success overclaim

Does a successful workflow get used as compatibility evidence for a dependency family the workflow never installs?

### 10.5 Activation composition

Can the evaluator preserve the required conjunction of installation, platform/hardware, package availability, configuration, and engine selection without collapsing them into one opaque "used" flag?

### 10.6 Coordinated-family overclaim

Can the system preserve exact-pin/family context without inventing incompatibility between independently updated members?

## 11. Relation to current main design

S011 does not contradict the current A/B/C implementation direction.

It strengthens existing accepted principles:

- dependency presence does not establish mechanism activation;
- applicability propositions are candidate-specific;
- missing/irrelevant CI evidence must not become negative compatibility evidence;
- coverage is proposition-relative;
- exact target context can require independent evidence acquisition.

It adds a concrete future discovery/applicability shape around optional extras and platform/hardware activation.

No current product source change is justified solely from S011 because broad candidate discovery and generic optional-environment reasoning are not admitted in the current bounded implementation slice.

## 12. Investigation/stopping lesson

No Apple-Silicon runtime execution was needed for the owned question.

Static evidence already answers:

- whether the optional group is real;
- how the runtime selects the MLX engine;
- what platform/package conditions are required;
- whether the two inspected test workflows install the extra.

Running NumPy 2.4.6 with MLX would answer:

> Is this exact coordinated stack behaviorally compatible?

That is a separate question.

Therefore S011 again reinforces:

```text
possible useful future experiment
!=
required evidence for the current proposition
```

## 13. Main-thread handoff decision

**No immediate implementation handoff is required.**

S011 is strong future transfer/evaluation evidence, but it does not expose a defect in the currently admitted Python-support implementation.

A handoff becomes useful when main opens one of:

- broad target-driven candidate discovery;
- optional dependency/extras applicability;
- CI/environment coverage modeling;
- platform/hardware applicability;
- coordinated dependency-family synthesis.

At that point S011 should be used as an adversarial anchor alongside S008 and S010.

## 14. Claim limits

Do not infer from S011 that:

- NumPy 2.4.6 breaks Dictare;
- every macOS environment is Apple Silicon;
- every repository workflow omits MLX;
- a specific PR check outcome was green;
- optional dependencies are generally riskier than core dependencies;
- exact-pinned families must always update atomically;
- the PR should be blocked/deferred.

## 15. Stop

S011 is complete at its admitted depth.

Do not extend it into on-device MLX compatibility experiments or a full optional-dependency architecture unless a later product/evaluation question requires that evidence.