# UpgradePilot Maintainer Action Synthesis Specification

**Status:** Accepted controlling technical specification  
**Owner:** Ali Rajabi  
**Responsibility:** Stable framework-independent semantics for overall evidence sufficiency, maintainer-action permission, action projection, residual uncertainty, and honest abstention after bounded technical investigation  
**Upstream technical-decision semantics:** [`UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md`](UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md)  
**Trust/evidence invariants:** [`UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md`](UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md)  
**Product mission/outcome authority:** [`../../PROJECT_CHARTER.md`](../../PROJECT_CHARTER.md)

## 1. Purpose and boundary

This specification is the durable owner for UpgradePilot's accepted **overall evidence-sufficiency and maintainer-action synthesis semantics**.

It answers:

> Given the bounded evidence, mechanism-specific investigation results, material repository context, uncertainty, and limitations that UpgradePilot actually owns, what maintainer-facing action is positively justified, and what action claims are not justified?

Its input begins **after** the technical responsibilities owned by the Product Decision Model have produced their current states or stopped.

Conceptually:

```text
TECHNICAL INVESTIGATION / APPLICABILITY
→ mechanism-specific evidence, propositions, applicability, attempted investigations,
  problems, residual uncertainty, and investigation stopping

↓

MAINTAINER-ACTION SYNTHESIS
→ overall action-relative evidence sufficiency
→ one bounded Charter action or abstention
→ decisive reasons, remaining uncertainty, follow-up, provenance, and claim limits
```

This specification does **not**:

- redefine the project mission, supported user, outcome family, or product claim limits owned by `PROJECT_CHARTER.md`;
- redefine candidate/applicability/investigation/stopping semantics owned by the Product Decision Model;
- define candidate-discovery algorithms, repository-context discovery methods, exact evidence-acquisition mechanisms, or provider behavior;
- select a Python representation, package layout, rule engine, graph, planner, LLM, agent framework, database, service, or persistence model;
- claim that every Charter action is currently reachable from the implemented product;
- claim objective update safety or replace maintainer judgment;
- authorize implementation by itself.

## 2. Relationship to other owners

The responsibility split is:

```text
PROJECT CHARTER
→ supported maintainer outcome family and claim limits

CORE PIPELINE + CONTRACT SPECIFICATION
→ identity, provenance, evidence, authority, failure, and trust invariants

PRODUCT DECISION MODEL SPECIFICATION
→ technical candidate/applicability/investigation/stopping semantics

THIS SPECIFICATION
→ overall action-relative sufficiency
→ maintainer-action permission and projection
→ residual uncertainty / follow-up / abstention semantics

ADRs
→ consequential implementation or structural method, if later required

PLANS
→ bounded implementation/proof sequence and stop lines

SOURCE + TESTS + OBSERVED OUTPUTS
→ actual implemented behavior
```

A mechanism-specific result MUST NOT acquire maintainer-action authority merely because it exists. Synthesis consumes already-owned technical meaning and decides only the later action responsibility.

## 3. Normative language

- **MUST** — required when the synthesis responsibility is admitted and applicable.
- **MUST NOT** — prohibited within this responsibility.
- **SHOULD** — expected unless evidence justifies a bounded exception.
- **MAY** — permitted.

## 4. Synthesis input boundary

Synthesis may consume only evidence/state whose identity, scope, provenance, interpretation strength, and limitations are available at sufficient proof strength for the permission being evaluated.

Relevant input may include:

- exact proposal / repository / revision / dependency identity;
- mechanism-specific candidate/applicability results;
- investigation selections, observations, problems, and stopping state where established;
- CI or other execution/configuration evidence at its actual proof strength;
- repository-context findings from an admitted context owner;
- acquisition, unsupported, unavailable, invalid, stale, conflicting, or unresolved states;
- residual uncertainty and known evidence limitations;
- concrete maintainer-performable checks, broader inquiry scope, or outside/future responsibility when a producer has actually established them.

Synthesis MUST NOT:

- manufacture missing candidate-discovery completeness;
- manufacture absent repository context;
- infer an outside responsibility merely because UpgradePilot lacks a capability;
- reinterpret mechanism-specific technical truth into a stronger state;
- upgrade static configuration into runtime execution;
- use evidence above its validated identity/provenance/interpretation strength.

## 5. Action-relative evidence sufficiency

Overall sufficiency is **action-relative**, not a universal boolean and not equivalent to resolving every proposition.

The governing question is:

```text
Is the owned evidence state sufficient to justify this particular bounded maintainer action,
while preserving material residual uncertainty and prohibiting unsupported stronger claims?
```

Therefore:

```text
some uncertainty remains
!= evidence insufficient for every action
```

and:

```text
all currently represented technical candidates look non-concerning
!= favorable overall permission established
```

A separate generic `sufficient = true/false` state is not required by these semantics. An implementation MAY add a distinct readiness/sufficiency field only if it has independent meaning that does not collapse the action-permission distinctions defined here.

## 6. Positive permission is required

Every emitted maintainer action MUST be positively justified by its own permission conditions.

The system MUST NOT use a fallback ladder such as:

```text
nothing bad found → merge
unresolved → investigate
missing capability → defer
high concern → block
```

Missing evidence, unsupported evidence, and absent producers do not satisfy positive permission.

If no non-abstention action is positively justified, synthesis MUST preserve that limitation rather than fabricate a more active-sounding recommendation.

## 7. Charter action family and required meanings

The public action family remains the one defined by the Charter:

1. `merge after normal review`;
2. `run targeted checks`;
3. `investigate or block`;
4. `defer`;
5. `abstain`.

The third Charter action contains two materially different operational dispositions. Synthesis MUST preserve whether the justified disposition is **investigate** or **block** rather than rendering the combined label alone.

This does not add a sixth Charter outcome. It refines the reason and next-step meaning inside the existing `investigate or block` family.

### 7.1 Merge after normal review

Permission requires positive closure over an explicitly bounded evidence/context/coverage horizon.

At minimum, the synthesis must establish that:

- exact decision identity is trustworthy enough for the action;
- the bounded evidence/mechanism/context horizon relied upon by the decision is explicitly owned and positively covered at the required proof strength;
- material candidates/concerns admitted within that horizon are resolved or otherwise non-defeating for ordinary review;
- evidence relied upon for closure has sufficient authority for the proposition it supports;
- admitted material repository-context findings have been incorporated rather than ignored;
- no material condition requiring targeted checks, broader investigation, block, or defer remains;
- residual uncertainty is recorded and is not decision-critical to returning the proposal to ordinary review.

This action means:

> UpgradePilot's bounded responsibility is sufficiently closed to return the proposal to ordinary maintainer review.

It MUST NOT mean:

- the update is objectively safe;
- all possible mechanisms were discovered unless that coverage was independently established;
- repository policy has approved the change;
- review is complete;
- the system should merge automatically.

Absence of a known blocker is not sufficient permission.

### 7.2 Run targeted checks

Permission requires:

- one or a small stable set of exact decision-critical unresolved propositions;
- concrete bounded maintainer-performable checks whose plausible observations materially discriminate those propositions;
- enough interpretation/stopping logic to explain how the observations would change the decision state;
- no justified UpgradePilot-executable investigation that should perform the same work before outsourcing it to the maintainer;
- no material concern requiring a broader adaptive inquiry instead of the bounded check set;
- no independently established block condition.

Generic uncertainty, a vague request to "test more", or a check that cannot materially change the decision MUST NOT satisfy this permission.

### 7.3 Investigate disposition within `investigate or block`

Permission requires:

- a grounded material target-relevant concern or uncertainty;
- a concrete broader/adaptive inquiry responsibility with identifiable discriminating directions;
- inquiry scope and stopping/pruning logic sufficient to make the work purposeful rather than open-ended;
- the useful inquiry is not adequately represented by one stable bounded check or small stable check set;
- current evidence is not yet sufficient to justify withholding the proposal as-is solely from an established block condition.

Intermediate findings MAY change which branch deserves the next evidence action. That adaptive structure is the principal distinction from `run targeted checks`.

Uncertainty alone, missing CI alone, a major-version label, or incomplete discovery alone MUST NOT create an investigate disposition.

### 7.4 Block disposition within `investigate or block`

Permission requires at least one material exact proposal-level failure, constraint, incompatibility, or other hold condition established at sufficient proof strength such that normal progression of the **current proposal as-is** should be withheld.

Further investigation MAY still be useful for remediation, explanation, or alternative design, but it is not required to justify the hold itself.

Block MUST NOT mean:

- permanent incompatibility;
- the dependency can never be supported;
- every unresolved concern is severe;
- repository mutation or automatic PR closure is authorized.

### 7.5 Defer

Permission requires:

- a decision-critical question remains unresolved;
- no justified admitted UpgradePilot-executable investigation currently resolves it;
- a **specific useful outside or future responsibility/condition** is known;
- that responsibility/condition could materially change the decision;
- a concrete reassessment or re-entry trigger can be named.

A missing product capability alone is not a defer reason.

If one bounded maintainer-performable check can answer the question now, `run targeted checks` may be the correct action instead. If a current broader adaptive inquiry is justified, `investigate` may be the correct action instead.

### 7.6 Abstain

Permission requires that no other Charter action is positively justified at the current proof strength.

Abstention is especially appropriate when:

- material evidence remains insufficient, unsupported, conflicted, or correctness-limited;
- favorable bounded coverage cannot be established;
- no concrete targeted check is justified;
- no grounded broader investigation program is justified;
- no specific outside/future responsibility with a re-entry condition is established;
- no independent block condition is established.

Abstain MUST preserve why the stronger-looking alternatives were unavailable. It MUST NOT be rewritten as a negative technical conclusion.

This specification governs abstention only when synthesis receives enough structured input to evaluate permissions. Operational failures that prevent formation of a synthesis input remain owned by the relevant acquisition/application responsibility.

## 8. The actions are not a severity ladder

The action family MUST NOT be modeled as a universal ordering such as:

```text
merge < targeted checks < investigate < block < defer < abstain
```

The actions express different evidence/responsibility structures.

Examples:

- `defer` is about a specific outside/future dependency, not higher severity than investigate;
- `abstain` means no justified action permission, not maximum risk;
- a highly material issue may still call for one targeted check if that observation is the correct discriminator;
- `block` depends on sufficient proof for withholding the current proposal, not a numeric risk threshold.

A numeric or opaque risk/confidence score MUST NOT own action authority under this specification.

## 9. Overlap and projection rules

Synthesis MUST preserve all material concerns, but it emits one Charter action for the bounded decision.

Use evidence structure rather than a universal total ordering.

### 9.1 Independent block condition

If an independently established block permission exists, the emitted Charter action is `investigate or block` with disposition `block` even when additional investigation or checks would help remediation. The additional work may be preserved as follow-up but is not required to justify the hold.

### 9.2 Targeted checks versus investigate

`run targeted checks` is permitted only when the material currently actionable uncertainty is adequately represented by the bounded listed check set.

If at least one decisive current concern requires broader/adaptive inquiry whose next evidence action can change after intermediate findings, use `investigate or block` with disposition `investigate` rather than pretending the whole inquiry is a fixed check list.

### 9.3 Defer versus current action

Use `defer` only when the decisive unresolved dependency is a specific outside/future responsibility or condition and no currently justified UpgradePilot or maintainer investigation/check can resolve that decision dependency now.

### 9.4 Favorable projection

`merge after normal review` is permitted only when no material non-favorable permission remains and its own positive bounded-coverage permission is satisfied.

### 9.5 Honest fallback

If none of the non-abstention permissions is satisfied, emit `abstain` when synthesis has a valid input boundary.

These rules define semantic projection, not a generic planner or reusable policy engine.

## 10. Trust and correctness gate

Before an evidence item or derived result can satisfy an action permission, its proof strength must satisfy the Core and Product Decision Model invariants relevant to that permission.

In particular:

```text
identity/provenance uncertainty
→ cannot be silently ignored

known interpretation weakness
→ cannot authorize a stronger proposition than it actually proves

known correctness defect affecting a producer path
→ affected evidence remains preserved but cannot satisfy a permission above its trustworthy strength
```

A current implementation MAY enforce a narrower supported-input restriction when that restriction is producer-grounded and testable. It MUST NOT simply assume the problematic condition did not occur.

Current bugs/limitations themselves remain implementation/evidence facts, not permanent semantic clauses of this specification.

## 11. Producer reachability and semantic availability

A valid action semantic may exist even when the current product cannot yet produce the prerequisites required to emit it.

Therefore:

```text
semantic action exists
!= action currently reachable
```

An implementation MUST NOT weaken a permission merely to make an action reachable from current producers.

When required producer-grounded facts are unavailable:

- the affected action permission is unavailable;
- another independently justified action may still be emitted;
- otherwise synthesis abstains when it has a valid input boundary.

Missing upstream capability should be repaired at the responsibility that owns that evidence/investigation rather than by inventing downstream synthesis metadata.

## 12. Minimum synthesis-result contract

The concrete implementation representation remains open, but an admitted synthesis result MUST preserve enough information to recover:

- exact repository / pull request / revision / dependency-transition identity relevant to the decision;
- one Charter action;
- `investigate` versus `block` disposition when the Charter action is `investigate or block`;
- decisive evidence-backed reasons for the action;
- material residual uncertainty/conflicts;
- evidence/provenance references and material trust/coverage limitations;
- concrete targeted checks when the action is `run targeted checks`;
- concrete broader inquiry scope when the disposition is `investigate`;
- concrete outside/future responsibility and reassessment trigger when the action is `defer`;
- claim limits, including what the result does not establish.

The result SHOULD preserve enough structure to render both machine-readable and human-readable projections without parsing prose back into semantics.

It is not necessary to duplicate every mechanism-specific field into the synthesis result when a stable reference/projection can preserve traceability.

## 13. Deterministic baseline requirement

The first admitted synthesis method MUST be transparent and deterministic over the accepted typed evidence/state boundary.

A model, LLM, graph, agent, planner, learned ranker, or opaque score MUST NOT receive final action authority merely because the synthesis responsibility contains heterogeneous evidence.

A more advanced method may be investigated later only under the Charter's technology-admission rules after a concrete limitation of the deterministic baseline is demonstrated.

## 14. Implementation acceptance guards

An implementation claiming to satisfy this specification SHOULD demonstrate, at the smallest credible proof boundary:

- exact identity preserved through synthesis;
- mechanism-specific states consumed without semantic reinterpretation;
- each emitted action has its positive permission established;
- missing/unsupported/correctness-limited evidence cannot satisfy positive permission;
- favorable action requires positive bounded coverage rather than absence of findings;
- targeted checks contain actual discriminating maintainer checks;
- investigate and block remain distinguishable within the combined Charter action;
- defer contains a specific outside/future responsibility and re-entry trigger;
- abstention preserves the reason other actions were unavailable;
- residual uncertainty and claim limits survive human/machine rendering;
- current unreachable actions remain unavailable rather than being forced by fixtures;
- no objective-safety claim or external repository mutation is implied.

Passing one fixture or one mechanism proves only that bounded path. Minimum Useful Generality remains applicable to variable-input automated synthesis.

## 15. Provenance and promotion history

This specification promotes stable accepted conclusions from the following design/evidence trail:

- [`../../working-memory/2026-09-11_synthesis-action-permission-matrix.md`](../../working-memory/2026-09-11_synthesis-action-permission-matrix.md) — first coherent action-permission matrix and favorable-permission pressure;
- [`../../working-memory/2026-09-11_synthesis-producer-reachability-and-correctness.md`](../../working-memory/2026-09-11_synthesis-producer-reachability-and-correctness.md) — current producer/reachability map and correctness constraints;
- [`../../product-simulation/INVESTIGATE_VS_BLOCK_EXISTING_EVIDENCE_REPORT_2026-09-11.md`](../../product-simulation/INVESTIGATE_VS_BLOCK_EXISTING_EVIDENCE_REPORT_2026-09-11.md) — bounded existing-evidence investigation of investigate-versus-block pressure;
- [`UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md`](UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md) — accepted upstream technical investigation/stopping boundary;
- real and real-derived product-simulation cases and pressure tests referenced by the dated synthesis records.

Those dated artifacts preserve **why/how** the synthesis semantics were reached. This specification owns **what the accepted synthesis semantics are now**.

## 16. Change control

Change this specification when accepted stable maintainer-action synthesis semantics change, including:

- action-relative sufficiency meaning;
- positive permission boundaries;
- investigate-versus-block disposition semantics;
- overlap/projection semantics;
- minimum synthesis-result semantic content;
- stable abstention/defer/favorable-action boundaries.

Do not update it merely for:

- one new product-simulation case that does not change accepted semantics;
- one implementation increment;
- one source/test refactor preserving this contract;
- one current producer gap or bug;
- live project position or exact next action;
- a speculative advanced synthesis method.

When durable semantics change, preserve the evidence/reasoning that motivated the change and update this owner explicitly rather than requiring future sessions to reconstruct the rule from dated working memory.
