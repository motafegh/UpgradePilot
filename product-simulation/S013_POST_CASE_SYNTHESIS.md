# S013 Post-Case Synthesis — Prior State Formation and Later No-Sync Exercise

**Date:** 2026-09-22
**Status:** Completed bounded synthesis; non-controlling discovery/evaluation evidence
**Scenario:** `scenarios/S013-langchain-anyio-uv-no-sync-prior-sync-state/README.md`

## 1. Result

S013 establishes a real dependency-update sequence in which visible ambient `UV_NO_SYNC=true` does not make the whole CI path non-state-forming.

The observed sequence is:

`changed uv.lock → explicit uv sync → proposed anyio 4.15.1 reported installed → later uv run under no-sync → tests exercise environment`.

The exact runtime checked out GitHub PR merge commit `63e06a2ba490c0bcdc7de672d38e5210f7cc0650`, not the bare proposal head.

## 2. Durable distinction

Package-manager semantics are operation-relative and sequence-relative.

`later command is no-sync` does not imply `no earlier command formed the environment`.

Likewise:

`later command succeeds` does not imply `later command performed the state formation`.

Evidence should remain attached to the operation that owns it.

## 3. New cross-stage composition pressure

S013 introduces a practical temporal composition shape:

`state-producing command at T1 → bounded state evidence → state-preserving/no-sync exercise at T2`.

This differs from S012's historical persisted-artifact problem. S013 stays inside one CI job and one ephemeral project environment; the temporal distinction is between commands, not between durable runs/artifacts.

## 4. Reality-check value

Main B4 correctly treats `UV_NO_SYNC` as a material semantic input, but S013 shows why a global fail-closed rule based only on its presence would overestimate the counterexample.

The real-world question is narrower:

> Which exact operation is being evaluated, what state existed before it, and is there positive evidence connecting that state to the later exercise?

This supports Product Simulation's standing rule that theoretical counterexamples should be checked for real shape and consequence before driving broad product complexity.

## 5. Evidence hierarchy exposed by the case

For this observed sequence:

1. exact changed lock/source identifies the proposed version;
2. explicit `uv sync` identifies a state-forming operation;
3. runtime sync output reports the proposed version installed;
4. workflow ordering shows no package-mutating step before the selected test step;
5. later pytest execution reports the same anyio version in the running test environment.

No single item should silently replace the others.

## 6. Implementation pressure — bounded

S013 does not demand a generic temporal engine or complete environment reconstruction.

It does create pressure against designs that:

- classify semantic modifiers without operation scope;
- discard valid earlier state evidence when a later command uses no-sync;
- attribute earlier state formation to a later exercise command;
- ignore ordering when composing state and exercise evidence.

A future implementation may answer this with bounded typed evidence and ordering rather than broad machinery.

## 7. Relationship to G3 reality screening

The broader G3 search found real `PIP_CONSTRAINT`, `UV_CONSTRAINT`, `UV_NO_SYNC`, shell-local exports, and `GITHUB_ENV` propagation, while the exact `PIP_DRY_RUN` workflow shape was not observed in the bounded search.

S013 therefore anchors G3 in a high-information observed family rather than a synthetic-only one.

## 8. Main-thread handoff

This case is immediately relevant to the main workstream's B4/B5 design boundary because it shows a real positive path that an over-broad ambient fail-closed rule could erase.

The handoff should be conceptual/evidence-based:

- preserve command-local semantic eligibility;
- preserve earlier explicit state-forming evidence separately;
- compose later exercise only when ordering/continuity is positively bounded;
- do not infer generic continuity across arbitrary mutation.

No product implementation is authorized from this research branch.

## 9. Claim limits

Do not infer ecosystem prevalence, universal uv semantics across all workflows, generic state continuity, bare-head runtime execution, or a mandatory architecture.

## 10. Stop

S013 is complete at the admitted depth. Reopen only if main selects a concrete implementation/proof design that needs transfer testing, or if a new real case challenges the same temporal boundary.