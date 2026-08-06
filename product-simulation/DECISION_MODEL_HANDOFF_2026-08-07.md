# Product-Simulation Handoff to Decision-Model Reconciliation

**Status:** Non-controlling simulation evidence handoff  
**Date:** 2026-08-07  
**Source branch:** `agent/product-simulation-case-screening-01`  
**Target discussion:** `working-memory/2026-08-06_UPGRADEPILOT-product-decision-model-reconciliation.md`  
**Purpose:** Surface only the product-simulation observations that materially help the current Conversation A question about target exposure surfaces. This file does not modify or settle the decision-model reconciliation.

## 1. Current design checkpoint observed from `main`

At `main` commit `093c762e88ef70c6a66e5a09575765cf8c0e9d27`, the reconciliation records:

- Conversation A is in progress;
- foundational impact semantics and materiality are provisionally accepted;
- the immediate next question is how to define **target exposure surfaces** without collapsing exposure, activation, consequence, and evidence;
- the emerging multidimensional model separates at least:
  1. upstream change mechanism;
  2. target exposure surface;
  3. activation condition;
  4. possible consequence;
  5. target applicability;
  6. evidence/coverage state.

The observations below are offered as concrete case evidence for that discussion only.

## 2. S006 gives a clean exposure-versus-activation distinction

S006 used the real qldebugger/Pydantic anchor.

Relevant target source:

```python
class ConfigLambda(BaseModel):
    @validator('handler', pre=True)
    def _split_handler(cls, v):
        if not isinstance(v, str):
            raise TypeError('should be a str')
```

Relevant upstream change:

- Pydantic V2 changes validator `TypeError` propagation so the error is raised directly rather than wrapped into Pydantic `ValidationError`.

The case suggests the following separation:

```text
upstream behavior change
→ target exposure: Pydantic validator/framework API semantics used by target source
→ activation layer 1: an affected Pydantic V2 version is selected/compared
→ activation layer 2: the validator receives a non-string handler
→ possible consequence: observable exception contract changes
→ evidence/coverage: tests, workflow configuration, reproduction results
```

### Handoff observation A

**Dependency-version selection should not automatically be classified as the target exposure surface.**

In S006, selecting Pydantic V2 determines whether the upstream changed behavior is active in the installed environment, but the place where the target actually encounters that behavior is the target's validator/framework integration.

This is evidence that exposure and activation may be separate even when both are necessary for an impact to occur.

## 3. Framework/declarative integration belongs somewhere under source/API exposure

S006 is not merely a direct function-call case.

The target encounters Pydantic through:

- `BaseModel` inheritance;
- the `@validator` decorator;
- validation lifecycle semantics controlled by the framework.

### Handoff observation B

A candidate exposure model should account for **framework/declarative hooks**, not only explicit dependency function calls.

However, S006 does not by itself prove that framework/declarative integration deserves a separate top-level exposure category. It may be a subtype of source/API usage. The useful requirement is that the eventual concept must be broad enough to include dependency-controlled callbacks, decorators, inheritance, plugins, or lifecycle hooks where the dependency invokes or interprets target code.

## 4. Tests and CI are evidence in S006, not the exposure surface

After the controlled withholding of the exact test, the visible repository still had tests exercising nearby `ConfigLambda` behavior and a workflow configured to run the test tree.

Those artifacts answer questions such as:

- is the affected behavior branch exercised?
- what is known about the result?
- is execution evidence retained?

They do not constitute the runtime path by which Pydantic's validator behavior reaches qldebugger.

### Handoff observation C

**`tests` and `CI` cannot be classified globally as either exposure or evidence. Their role is contextual.**

For S006:

```text
runtime dependency behavior
→ target validator source is exposure
→ tests/CI are evidence about that exposure
```

For historical pytest cases such as S004/S005, the dependency itself is a test/development tool, so test execution can be the actual target exposure surface.

This contrast may help Conversation A avoid a category error:

> the same repository subsystem can be an exposure surface in one dependency role and evidence/observation machinery in another.

## 5. Behavior-path coverage should remain separate from exposure

S006 showed that the component and validator were broadly exercised, while the exact `TypeError` branch was not present in the controlled visible evidence.

### Handoff observation D

The model should avoid treating any of these as equivalent:

```text
dependency is present
!= target uses dependency
!= target exposes the affected behavior
!= target path is activated
!= tests cover the activated behavior
!= retained execution evidence proves the behavior result
```

Exposure answers **where the target can encounter the changed dependency behavior**.
Coverage/evidence answers **what we know about that exposed path and its behavior**.

## 6. S006 also suggests a possible exposure test

A candidate concept can be challenged with this question:

> If the upstream dependency changed behavior, what target-owned or target-relevant interface/path would have to exist for that changed behavior to reach the repository before we look at whether the condition is activated or whether tests cover it?

Applied to S006:

- exposure: `ConfigLambda`'s Pydantic validator/framework integration;
- activation: affected dependency version + non-string handler input;
- consequence: exception surface changes;
- evidence: target tests, workflow configuration, differential reproduction.

This test is offered only as a discussion aid, not a formal definition.

## 7. What S006 does **not** justify

Do not infer from this handoff that:

- `source/API`, `framework`, `configuration`, `CI`, or any other labels are accepted top-level exposure categories;
- dependency-version activation is always separate from exposure in every ecosystem;
- the S006 structure should become a runtime schema;
- all impacts require exactly two activation layers;
- tests/CI are never exposure surfaces;
- the decision-model reconciliation should adopt S006 terminology unchanged.

The case provides a concrete discriminator for the current discussion, not a taxonomy answer.

## 8. Additional simulation evidence likely useful later, not necessarily now

The completed simulation set contains other contrasts that may become useful as Conversation A continues:

- **S003:** dependency/peer-constraint and installation path — useful for testing whether dependency graph/resolution is an exposure surface, an activation mechanism, or a distinct impact mechanism;
- **S004/S005:** pytest as development/test tooling — useful for testing contextual roles of tests/CI as actual exposure rather than merely evidence;
- **S001:** target runtime-support declaration — useful for distinguishing target configuration/declaration exposure from applicability evidence;
- **S002:** adapter/framework-mediated behavior — useful for comparing direct API use with mediated framework/adapter exposure.

These should be brought in selectively as the reconciliation asks specific questions; do not force all historical cases into Conversation A at once.

## 9. Recommended handoff use

For the immediate exposure-surface discussion, the highest-value S006 contribution is the three-way distinction:

```text
target exposure
where changed dependency behavior reaches the target

activation/applicability
what must be true for that exposed behavior to matter in this exact case

evidence/coverage
what observations support, refute, cover, conflict with, or leave that path unresolved
```

If this distinction survives comparison against S001–S005 and other real dependency roles, it may help the reconciliation define exposure surfaces without mixing them with activation conditions or evidence sources.
