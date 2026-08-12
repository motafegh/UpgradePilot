# B2 Public PR Vertical Slice Plan

**Owner:** Ali Rajabi  
**Parent route:** [`UPGRADEPILOT_90_DAY_PLAN.md`](UPGRADEPILOT_90_DAY_PLAN.md)

## Purpose

Build a credible real UpgradePilot path:

```text
public repository + Dependabot PR number
→ exact proposal and dependency identity
→ relevant exact-head CI, repository, package, and upstream evidence
→ technical/context reasoning with explicit uncertainty
→ conditional investigation or justified stopping
→ bounded recommendation or honest abstention
→ concise traceable output
```

This file defines B2 scope, responsibility sequence, proof expectations, transfer pressure, and stop lines. It does not record progress, select the immediate implementation step, or state the next action. `../MEMORY.md` is the sole owner of those live facts.

## Working rule — broad responsibility horizon, small implementation increments

B2 still proceeds incrementally. A session may implement one function, contract, source seam, or test at a time.

However, the implementation and method horizon for a central responsibility is the **complete owning responsibility inside B2**, not the current repository, package, version, fixture, simulation case, or first mechanism.

Apply the controlling Minimum Useful Generality rule:

> **Bound the supported domain, not the known fixture.**

Therefore:

```text
small implementation increment
!= small architecture horizon
```

and:

```text
first working case
!= accepted general method
```

A completed lower increment does not authorize unrelated product scope, but neither does its stop line require future design to remain shaped around that first proof.

## B2 use of product-simulation evidence

`product-simulation/` is a discovery and pressure-test laboratory, not an implementation backlog.

Do not implement scenarios sequentially or increase case count for its own sake. Instead, use a small materially diverse transfer set when a central design decision needs pressure beyond the first implemented specimen.

For current decision-foundation work, useful contrasts include:

- Python-support-range reasoning as the existing implementation anchor;
- targeted dynamic investigation where static evidence is insufficient;
- authoritative static evidence that resolves a proposition and prunes execution;
- artifact/installability transitions that differ from API/support-range semantics;
- repository-purpose/provenance context that must remain separate from technical applicability.

A simulation case supplies evidence and architectural pressure. It does not automatically authorize ecosystem-specific production support, dynamic execution, or a new framework.

## Required B2 outcomes

B2 requires all of the following before its gate can close:

1. accept `owner/repository` and a pull-request number through one public command;
2. acquire and validate exact public PR identity;
3. acquire and reconcile all changed-file records;
4. identify supported exact-version Python dependency transitions through admitted representations without repository-, package-, version-, or fixture-specific hardcoding;
5. preserve explicit unsupported, malformed, incomplete, ambiguous, multiple, and conflicting dependency-change states where applicable;
6. acquire exact-head `pull_request` workflow runs, jobs, and required workflow definitions;
7. classify bounded CI authority as sufficient, insufficient, or unresolved without overclaiming safety or coverage;
8. acquire the minimum official package/upstream/repository evidence required by the activated reasoning path;
9. preserve source identity, exact version/revision identity, availability, acquisition failure, and provenance;
10. represent mechanism-specific technical impact candidates without allowing candidate generation to manufacture its own truth;
11. evaluate candidate-specific applicability with explicit proposition/evidence/path coverage and preserved unresolved/conflicted states;
12. when material uncertainty remains, identify a discriminating target and either select an admitted investigation, retain non-dominated alternatives, or justify no further investigation;
13. revalidate investigation value against the evidence/proposition state before execution when intervening evidence can make a previously selected investigation redundant;
14. keep technical applicability distinct from repository-purpose/policy/provenance context when they are different responsibilities;
15. produce a transparent bounded recommendation or abstention;
16. keep concise human output consistent with minimum machine-readable state;
17. preserve enough controlled evidence for deterministic tests and replay;
18. demonstrate the central variable-input reasoning architecture against at least one materially different transfer/implementation contrast so one known mechanism is not the sole justification for the method shape;
19. complete the required central owner-controlled modification, test, diagnosis, transfer argument, and explanation defined by the operating controls.

B2 does not require every outcome to activate for every PR. Conditional non-activation and justified stopping are product behavior.

## Responsibility sequence

The sequence below is a product-flow decomposition, not permission to design each responsibility only for its first fixture.

### 1. Public proposal identity

```text
repository + PR number
→ validated locator
→ exact PR, base, head, and changed-file identity
```

Proof requires deterministic input, response-shape, identity, pagination, and count reconciliation tests plus a safe read-only live request where network behavior is part of the claim.

### 2. Dependency identity

```text
complete changed-file evidence
+ exact base/head repository files when required by an admitted representation
→ source-specific deterministic candidates
→ canonical exact-version dependency transition(s)
   or explicit unsupported, malformed, incomplete, ambiguous, multiple, or conflicting result
```

The dependency-change foundation must:

- bound supported representations rather than known PRs;
- preserve source-specific evidence and provenance;
- separate where a change was established from how CI consumed that representation;
- reconcile equivalent evidence without guessing through conflicts;
- refuse to silently choose one package from a materially multi-change case;
- keep later package, upstream, target, impact, and decision responsibilities independent of source-file grammar.

B2 does not require universal package-manager support, complete dependency graphs, or broad lock semantics.

### 3. Exact-head CI authority

```text
validated exact-head workflow run
→ exact-run workflow path
→ workflow text at the same head SHA
→ bounded command/dependency-exercise evidence
→ sufficient, insufficient, or unresolved authority
```

CI evidence must not claim complete test coverage, compatibility, upgrade safety, or a maintainer recommendation merely because jobs are green.

Indirect tox, scripts, reusable workflows, matrices, lock consumption, or richer YAML tracing should expand when the owning CI-authority question requires them, not because every possible indirection should be modeled in advance.

### 4. Public package, upstream, and target/repository evidence

```text
validated dependency identity
+ activated reasoning question
→ exact authoritative source(s)
→ required bounded evidence
→ explicit available, unavailable, invalid, mismatched, unsupported, stale, or conflicting state
```

Acquire evidence according to the proposition/question being resolved rather than a fixed source checklist.

Do not hardcode package-specific answers, silently accept identity mismatch, or treat more expensive/dynamic evidence as inherently better than sufficient authoritative static evidence.

### 5. Technical impact and candidate-specific applicability

```text
trusted transition/evidence
→ one or more justified mechanism-specific technical impact candidates
→ candidate-specific propositions and applicability paths
→ established / refuted / unresolved / conflicted state
```

Required guards include:

- candidate formulation does not establish its own exposure, activation, completeness, or consequence truth;
- missing evidence is not refutation;
- evidence coverage, path-model coverage, and candidate-discovery coverage remain distinct;
- candidate-level non-applicability requires both sufficient elimination of represented viable paths and sufficient path-model coverage for that claim;
- mechanism-specific semantics stay separate where they materially differ.

The first Python-support-drop implementation is an anchor, not the universal impact model.

### 6. Discriminating investigation, feedback, and stopping

```text
material unresolved/conflicted proposition
→ uncertainty location
→ discriminating target
→ selected admitted investigation / bounded alternatives / justified stop
→ validate observation meaning
→ reevaluate proposition/candidate
```

Keep distinct:

```text
epistemic investigation value
!= UpgradePilot execution admissibility
!= later maintainer-facing recommendability
```

The same failed/unavailable investigation must not be selected again merely because uncertainty remains. A retry requires concrete justification.

A selected investigation is not permanent authorization to execute. If new admitted evidence resolves the proposition or closes the necessary path, the investigation must be re-evaluated and may be pruned before execution.

### 7. Responsibility-level transfer and architecture checkpoint

After the first complete technical-candidate → applicability → investigation/feedback loop works, compare the implementation against at least one materially different technical mechanism/evidence shape before accepting the architecture as sufficient for B2.

The goal is to discover:

- which contracts are genuinely shared;
- which semantics must remain mechanism-specific;
- whether orchestration is becoming one branch per known case;
- whether result representation can support heterogeneous evidence without a universal opaque score;
- whether a second mechanism exposes a missing product responsibility.

Prefer **evidence-earned abstraction**:

```text
real mechanism 1
+
real mechanism 2
→ compare
→ extract only demonstrated sameness
```

Do not create a generic planner, graph, engine, universal candidate, or plugin system merely to anticipate future mechanisms.

### 8. Overall synthesis and bounded action

```text
technical candidate results
+ CI/evidence authority
+ relevant repository/context evidence
+ residual uncertainty
→ overall sufficiency assessment
→ bounded recommendation or abstention
```

This responsibility must not collapse technical applicability, repository context, evidence quality, and maintainer-facing action into one opaque scalar.

The exact synthesis method should be opened around concrete evidence produced by the implemented reasoning path, not invented entirely in advance.

### 9. Output and controlled rerun evidence

Produce:

- one concise human-readable result;
- minimum machine-readable state sufficient for deterministic assertions and traceability;
- controlled captured-response or normalized-evidence fixtures where justified;
- no persistence system, service layer, or replay platform beyond demonstrated B2 need.

## Proof strategy

For each meaningful implementation increment:

1. test the narrow changed responsibility;
2. test representative failure/unavailable/unsupported/ambiguous/conflicting/unresolved behavior relevant to the change;
3. ask whether the implementation is being shaped by one known fixture rather than the owning responsibility;
4. where method generality is material, pressure-test against a structurally different real or controlled variation before accepting the design;
5. run the nearest complete deterministic suite required by the change;
6. run a safe live read-only example when network evidence is part of the claim;
7. state exactly what the result proves and does not prove;
8. stop the **increment** when its proof is sufficient, then use `MEMORY.md` to select the next highest-value move toward the B2 end-to-end outcome.

Stopping an increment is not the same as freezing the architecture around that increment.

## B2 stop boundary

B2 does not establish:

- universal Python dependency or package-manager support;
- exhaustive impact-candidate discovery across the Python ecosystem;
- complete dependency graphs, role/path interpretation, or multi-package update semantics;
- complete GitHub Actions or YAML interpretation;
- objective upgrade safety;
- private-repository access;
- target-repository mutation;
- arbitrary target code/dependency execution;
- persistence, distributed services, agents, generic planners, generic graphs, or deployment infrastructure;
- representative evaluation across the full mature product domain;
- B3 acquisition robustness or the systematic supported-domain breadth expected of B4.

B2 **does** require enough materially different pressure to prevent its central architecture from being justified solely by one first case.

## Plan maintenance

Change this file only when B2 required outcomes, responsibility sequence, proof obligations, transfer expectations, or stop lines change. Do not add progress checkboxes, active labels, latest validation results, blockers, or immediate continuation. Those belong only in `../MEMORY.md`.
