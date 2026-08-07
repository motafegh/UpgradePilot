# Decision-Model Handoff — Challenge Pass 02

**Date:** 2026-08-07  
**Status:** Non-controlling simulation-to-design handoff  
**Source:** `CHALLENGE_CASE_SCREENING_02.md`  
**Target discussion:** `working-memory/2026-08-06_UPGRADEPILOT-product-decision-model-reconciliation.md`  
**Reconciliation baseline reviewed:** `main` at `808766417ec729ecc4ed9943271c40d76c4d533c`

## Purpose

This handoff carries only the parts of Challenge Screening Pass 02 that remain useful after the active reconciliation advanced through exposure/coupling analysis.

It deliberately does **not** ask the reconciliation to reopen conclusions it has already provisionally accepted.

At the reviewed `main`, the reconciliation already provisionally establishes that:

- technical exposure is a target relationship/pathway rather than merely a repository location;
- exposure may be multi-hop and graph-shaped;
- subsystem/artifact roles are contextual;
- exposure, activation, consequence, and evidence should remain conceptually distinct;
- technical target impact is narrower than all decision-relevant information.

Challenge Pass 02 substantially supports those conclusions with additional real cases. Its remaining contribution is therefore **stress-test evidence and two bounded refinements**, not a competing model.

## Evidence set

### 1. `pypa/pip-audit#620` — multi-hop compatibility

Frozen target evidence records the reason for its urllib3 `<2` constraint as:

```text
CacheControl's incompatibility with urllib3 ~= 2.0 by way of requests
```

Historical CacheControl issue evidence identifies the concrete incompatibility:

```text
CacheControl expects HTTPResponse.strict
urllib3 2 removes that response property/argument
```

The technically relevant interaction therefore occurs several ownership steps away from pip-audit-owned source:

```text
pip-audit
→ CacheControl
→ Requests / urllib3 response machinery
→ CacheControl assumption on urllib3.HTTPResponse
```

This is strong real evidence for the reconciliation's current multi-hop/path hypothesis.

### 2. `kedro-org/kedro#2782` — dynamic/inverted-control coupling

At exact PR head, Kedro:

- constructs Pluggy `PluginManager`;
- registers lifecycle hook specifications;
- loads installed plugins through the `kedro.hooks` entry-point group;
- dispatches lifecycle events using `hook_manager.hook.*`.

Pluggy 1.2's crossed semantics concern hook-wrapper dispatch/result/exception behavior.

The relationship is not only:

```text
Kedro → Pluggy API
```

but also:

```text
Kedro registers contracts/plugins
→ Pluggy dispatch machinery
→ registered plugin-owned code executes
→ result/exception returns through Pluggy
→ Kedro execution continues
```

This provides concrete evidence for execution/control-flow coupling in which directionality changes during the same interaction.

### 3. `dominodatalab/container-runtime-interface-api#101` — artifact-mediated coupling

Previously screened evidence shows:

```text
grpcio-tools
→ generation execution
→ generated Python source
→ committed/package artifact
→ later runtime consumption
```

This supports data/artifact-contract coupling and shows that dependency effects can be separated in time from later runtime consumption.

### 4. `shahzebsiddiqui/buildtest-1#74` — environment-mediated pathway, activation unresolved

The dependency update crosses urllib3's OpenSSL/native-environment support boundary.

The target has exact external HPC CI context, including a NERSC/Perlmutter pipeline loading a managed `python/3.9-anaconda-2021.11` module.

However, the exact linked SSL implementation/version for that historical environment was not established.

Therefore the correct state is:

```text
environment pathway exists
+ upstream environment constraint exists
+ exact target activation unresolved
```

This is useful evidence for the reconciliation's constraint/environment coupling hypothesis, while also demonstrating that environment applicability needs an independent evidence path rather than inference from source or broad CI labels.

## Refinement A — target relevance does not require target ownership of affected code

The strongest new pressure from Pass 02 is:

```text
target relevance
!=
target ownership of the technically affected code
```

In the pip-audit case, the actual incompatible object/API assumption lives in dependency-owned code.

In the Kedro case, dynamically loaded plugin implementations may live outside the target repository entirely.

The target can still be materially connected because it selects, composes, configures, registers, or executes the dependency/plugin graph.

### Question for reconciliation

Does the current phrase:

> target-owned or target-relevant relationship/pathway

already capture this adequately?

If yes, no new concept is needed.

If not, the model may need to make explicit that **ownership and relevance are independent dimensions**.

Do not add a new runtime field merely because this distinction exists conceptually.

## Refinement B — one version transition can fan out into multiple change mechanisms

The urllib3 1.x → 2.x interval contains several structurally different candidate changes, including:

- removed/changed APIs such as `HTTPResponse.strict`;
- Python support changes;
- SSL/native-environment support changes;
- TLS/hostname behavior changes;
- other response/runtime semantics.

Therefore:

```text
one dependency version transition
!=
one technical impact candidate
```

A safer reasoning shape is:

```text
exact proposed transition
→ authoritative candidate upstream change mechanisms
→ for each material mechanism:
     target relationship/path
     + activation condition(s)
     + possible consequence
     + evidence/applicability state
```

This is consistent with the current reconciliation but should be preserved explicitly enough that the future system does not create one aggregate `urllib3_2_risk`-style object from an entire release interval.

### Question for reconciliation

Is this already implied strongly enough by the current phrase:

```text
for each material technical candidate
```

If yes, no change is required.

If not, the discussion may want to clarify that a **candidate technical impact is mechanism-specific**, not version-transition-wide.

## What Pass 02 does not challenge anymore

Given current reconciliation progress, these should **not** be reopened solely because of Pass 02:

1. **Exposure as relationship/pathway** — the new cases support this.
2. **Multi-hop/graph-shaped exposure** — pip-audit provides concrete real evidence.
3. **Contextual subsystem roles** — existing S004–S006 plus these cases continue to support it.
4. **Small reusable coupling roots as a hypothesis** — Pluggy, codegen, environment, and multi-hop cases are compatible with the current candidate roots; they do not yet prove the exact count or names.
5. **Technical impact versus all decision-relevant information** — Pass 02 mostly concerns technical impact and therefore does not provide reason to collapse trust/policy/licensing/identity back into it.

## What remains genuinely open from the simulation side

### Environment activation evidence

A stronger real case is still wanted where exact target environment state proves activation of a native/platform/compiler/wheel constraint.

The Buildtest candidate demonstrates the evidence problem but does not close it.

### Multi-hop stopping boundary

The cases show that tracing may need more than one dependency edge. They do not define how far UpgradePilot should traverse.

A later product question may be:

> Once the exact incompatible contract has been located and tied to a target-relevant dependency path, what additional graph traversal can still change applicability, investigation choice, or confidence?

That question likely belongs partly to Conversations B/C rather than Conversation A.

### Dynamic-plugin applicability

Kedro proves the dynamic pathway, but determining whether a specific Pluggy change matters may require evidence of:

- which entry-point plugins are actually installed;
- which hook implementations/wrappers they register;
- which lifecycle events are reached;
- which wrapper/result/exception semantics are relied upon.

This is likely applicability/investigation evidence rather than a reason to invent more exposure categories.

## Scenario decision

No S007 is admitted by this handoff.

Pass 02 has produced useful design evidence, but the active reconciliation has already absorbed much of the conceptual direction. A controlled scenario should wait until the reconciliation identifies a specific behavior that needs validation—for example a multi-hop tracing/stopping contract or dynamic-plugin applicability method.

## Bounded handoff conclusion

Challenge Pass 02 is best read as **evidence that the reconciliation's current technical-exposure refinements survive harder real topologies**, with two candidate clarifications:

```text
1. target relevance does not require target ownership of affected code;
2. one proposed version transition may yield multiple mechanism-specific technical-impact candidates.
```

The reconciliation should adopt either clarification only if it improves the domain model without adding unnecessary ceremony or implementation structure.
