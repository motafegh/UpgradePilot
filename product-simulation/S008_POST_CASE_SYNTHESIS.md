# S008 Post-Case Synthesis — Artifact Availability, Installation Mode, and Stopping

**Date:** 2026-08-11  
**Status:** Completed bounded synthesis; non-controlling discovery/evaluation evidence  
**Scenario:** [`scenarios/S008-carla-opencv-python36-artifact-fallback/README.md`](scenarios/S008-carla-opencv-python36-artifact-fallback/README.md)  
**Product context inspected:** `main@6202548eeff8c76405b8b53e0e35f0caeef53ef3`

## 1. What S008 established

For the exact real proposal `carla-simulator/scenario_runner#1111`:

```text
opencv-python 4.2.0.32
→
opencv-python 4.8.1.78
```

and the bounded CPython-3.6 Linux question:

- the old release provides compatible prebuilt Linux wheels;
- the new release does not publish a CPython-3.6-compatible binary wheel;
- the new release still publishes a source distribution and retains Python-3.6 package/build metadata;
- the exact target has a real OpenCV dependency/runtime relationship, a documented Python-3 full-requirements installation path, and explicit Python-3.6 repository context;
- the inspected target workflows do not establish coverage of the exact Python-3.6 artifact transition;
- no source-build observation was needed to establish the owned artifact transition.

The bounded technical result is therefore:

```text
prebuilt binary path available
→
prebuilt binary path unavailable
+ source fallback remains
```

not:

```text
Python 3.6 is impossible
```

and not:

```text
source build fails
```

## 2. New durable distinction — support metadata vs artifact serviceability

S008 adds an important proposition separation:

```text
PACKAGE/INTERPRETER ADMISSIBILITY
Does package metadata permit interpreter P?

!=

BINARY ARTIFACT AVAILABILITY
Does release R publish a compatible wheel for P/platform A?

!=

SOURCE FALLBACK AVAILABILITY
Can installation fall back to an sdist/source path?

!=

SOURCE FALLBACK SUCCESS
Does that path actually succeed in exact environment E?
```

These are related but not interchangeable facts.

A product that collapses them into one `supported / unsupported` flag can overclaim in both directions:

- `Requires-Python >=3.6` could hide loss of a prebuilt installation path;
- absence of a wheel could be misreported as total incompatibility even when a source path remains.

This does not yet justify a universal runtime schema. It is a discovered modeling responsibility for any future artifact-availability capability.

## 3. Installation-mode change is a real technical impact mechanism

S008 broadens the impact model beyond source/API behavior.

A dependency update can change:

```text
artifact selection
→ installation mechanism
→ external prerequisites / build surface / time / failure modes
```

before target application code executes.

The possible consequence is therefore not necessarily a changed API result or exception. It can be a changed **environment-formation obligation**.

That supports the existing Conversation-A principle that exposure/path is broader than repository-owned call sites and that one dependency transition can contain multiple mechanism-specific candidates.

## 4. S008 validates the implemented A/B proposition discipline

The current `src/upgradepilot/impact/applicability.py` model is intentionally small and mechanism-agnostic enough to describe the S008 reasoning without pretending the product already supports OpenCV artifacts.

Conceptually:

```text
P1 old compatible wheel exists        established
P2 new compatible wheel exists        refuted
P3 new source fallback exists         established
P4 target context is relevant         bounded established
P5 exact CI coverage exists           unresolved
P6 source fallback succeeds           unresolved
```

The important success is that the current A/B implementation does not require all six propositions to collapse into one binary answer.

S008 therefore provides **transfer confirmation**, not evidence that the first Python-support candidate implementation is wrongly designed.

## 5. Conversation-C lesson — expensive observation can be correctly inactive

For the owned question:

> Did the binary artifact path disappear while a source fallback remains?

exact static package evidence is already discriminating.

A native source-build observation would answer:

> Does the fallback build succeed in exact environment E?

That is a separate proposition.

Therefore S008 reinforces:

```text
more realistic / expensive / dynamic evidence
!=
more useful evidence for the current proposition
```

and:

```text
unresolved downstream proposition
!=
automatic authorization to investigate it
```

This is an important complement to the current first runtime-C anchor:

- current main case: missing exact target evidence may justify an existing read-only acquisition;
- S008: the owned proposition may already be resolved, so a deeper build observation is correctly inactive even though another downstream proposition remains unresolved.

## 6. CI lesson — environment specificity matters

The inspected ScenarioRunner workflow installs requirements on Ubuntu but does not explicitly exercise Python 3.6.

Therefore:

```text
same package installed in CI
!=
same artifact-selection branch exercised
```

This generalizes S006's `broad coverage != discriminating path coverage` lesson into packaging/environment selection.

Coverage must be scoped to the proposition that matters.

## 7. Cross-case map

### S001 — support-range exclusion

```text
upstream support drop
+ exact target range
→ concern outside target range
```

### S003 — install failure

```text
real dependency constraints
→ resolver/install fails
→ causal attribution possible
```

### S007 — package-family contradiction

```text
coordinated package constraints conflict
→ intended environment cannot form coherently
→ deeper runtime work pruned
```

### S008 — artifact-serviceability transition

```text
package still source-permits interpreter
+ prebuilt artifact disappears
→ installation path changes
→ source-build success remains separate
```

These four cases should not be collapsed into one generic `compatibility` label.

## 8. Product implications — bounded only

S008 suggests that a future admitted dependency-impact mechanism may need to reason about:

- interpreter/platform wheel availability;
- source-distribution availability;
- artifact-selection branches;
- exact target environment relevance;
- CI coverage of the relevant artifact branch.

But **no implementation should be added now merely because this mechanism exists**.

The current B2 plan explicitly avoids universal impact generation, generic dependency graphs, broad environment reconstruction, and generic investigation planners. S008 does not challenge that proportionality boundary.

## 9. Handoff decision

**No immediate main-thread correction or architecture handoff is required.**

Reason:

- S008 does not contradict the current A/B implementation;
- it supports the proposition/evidence/coverage model;
- its C lesson is already compatible with the accepted rule that investigation selection is proposition-relative and may legitimately stop;
- the specific artifact-availability mechanism is outside the currently admitted first runtime slice.

Preserve S008 as transfer/evaluation evidence. Revisit it when a future implementation claims broader impact-candidate generation, packaging/environment applicability, or investigation selection across materially different mechanisms.

## 10. Stop

S008 is complete at its admitted depth.

Do not extend this scenario into:

- a full OpenCV source build;
- general Python-3.6/OpenCV migration analysis;
- every crossed OpenCV API/security change;
- a CARLA runtime test program;
- a maintainer recommendation;
- generic wheel-analysis product implementation.

Those would be different questions requiring separate justification.