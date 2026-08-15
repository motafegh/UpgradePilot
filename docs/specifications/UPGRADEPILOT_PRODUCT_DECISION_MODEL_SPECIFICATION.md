# UpgradePilot Product Decision Model Specification

**Status:** Accepted controlling technical specification  
**Owner:** Ali Rajabi  
**Responsibility:** Stable framework-independent semantics for technical impact candidates, candidate-specific applicability, evidence/coverage reasoning, discriminating investigation, reevaluation, and the boundary to later maintainer-facing synthesis  
**Implementation decisions:** ADRs under `../architecture/`  
**Actual behavior:** Source, tests, commands, outputs, and relevant evidence  
**Historical rationale / pressure evidence:** [`../../working-memory/2026-08-06_UPGRADEPILOT-product-decision-model-reconciliation.md`](../../working-memory/2026-08-06_UPGRADEPILOT-product-decision-model-reconciliation.md), [`../../audits/2026-08-10_AUDIT-003_post-conversation-c-product-decision-model.md`](../../audits/2026-08-10_AUDIT-003_post-conversation-c-product-decision-model.md)

## 1. Purpose and boundary

This specification is the durable owner for UpgradePilot's accepted product decision/reasoning semantics that were previously distributed across dated reconciliation records, audit amendments, pressure-test evidence, and implementation handoffs.

It answers:

> **Once exact dependency-update identity and admitted evidence exist, how must UpgradePilot represent a technical concern, evaluate whether it applies to the exact target, decide whether more evidence is worth pursuing, incorporate the result, and stop without manufacturing certainty?**

It governs the meaning of the reasoning stages, not their concrete implementation method.

It does **not**:

- define the project mission, user, supported product boundary, or final claim limits owned by `../../PROJECT_CHARTER.md`;
- define live project position or continuation owned only by `../../MEMORY.md`;
- activate every mature-system responsibility merely because it is described here;
- select a programming framework, package layout, model, graph, planner, database, service, provider, or agent architecture;
- define a universal impact-mechanism taxonomy;
- define a universal Boolean/rule engine;
- define Conversation-D/final maintainer-facing synthesis beyond the accepted boundary stated here;
- prove that any source implementation currently satisfies these semantics.

The selected plan determines which applicable responsibility is admitted for implementation. ADRs select consequential implementation/structural methods. Source/tests and observed evidence establish implemented truth.

## 2. Relationship to other owners

This specification specializes, but does not replace, the stable trust/evidence invariants in [`UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md`](UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md).

In particular:

```text
core specification
→ observation / interpretation / evidence quality / decision separation
→ provenance / identity / failure-state discipline
→ authority and grounding protections

this specification
→ impact-candidate semantics
→ candidate applicability semantics
→ coverage / negative-inference boundaries
→ discriminating investigation and stopping
→ result feedback / candidate lineage
→ boundary to later synthesis
```

Variable-input implementations are additionally governed by [`UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md`](UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md).

The evolving mature-system orientation remains in [`../../proposals/UPGRADEPILOT_MATURE_SYSTEM_HORIZON.md`](../../proposals/UPGRADEPILOT_MATURE_SYSTEM_HORIZON.md). That horizon may explore open future responsibilities; it cannot redefine the accepted semantics here.

## 3. Normative language

- **MUST** — required for acceptance when the requirement applies to an admitted responsibility.
- **MUST NOT** — prohibited within the admitted responsibility.
- **SHOULD** — expected unless evidence justifies a bounded exception.
- **MAY** — permitted.

## 4. Accepted reasoning spine

The accepted product reasoning spine is:

```text
PUBLIC DEPENDENCY-UPDATE PR
↓
EXACT PROPOSAL / TARGET / DEPENDENCY / VERSION / REVISION IDENTITY
↓
AUTHORITATIVE OR OTHERWISE ADMITTED EVIDENCE ABOUT THE EXACT TRANSITION
↓
ZERO OR MORE MECHANISM-SPECIFIC TECHNICAL IMPACT CANDIDATES
↓
CANDIDATE COMPONENTS RETAIN THEIR EVIDENTIAL STATUS
↓
DERIVE CANDIDATE-SPECIFIC APPLICABILITY PROPOSITIONS / PATHS
↓
EVALUATE PROPOSITIONS AGAINST SCOPED EVIDENCE
    established / refuted / unresolved / conflicted
↓
COMPOSE ONLY THE EXPLICIT LOGIC REQUIRED BY THE CANDIDATE
↓
CANDIDATE APPLICABILITY KNOWLEDGE STATE
    established applicable
    established not applicable
    unresolved
    conflicted
↓
IF A MATERIAL NON-FINAL STATE REMAINS
    identify uncertainty/conflict location
    → identify discriminating target
    → select one justified investigation / small conditional sequence
       OR preserve non-dominated alternatives
       OR stop because no further justified investigation exists
↓
OBSERVATION / RESULT
↓
VALIDATE RESULT IDENTITY, SCOPE, CONTEXT, CONTRAST, AND EVIDENTIAL MEANING
↓
REEVALUATE CURRENT PROPOSITION
    OR REFINE / SUPERSEDE CANDIDATE WITH LINEAGE
↓
REPEAT ONLY WHILE MATERIAL NON-FINAL STATE REMAINS
AND A JUSTIFIED USEFUL INVESTIGATION EXISTS
↓
INVESTIGATION STOP
↓
LATER OVERALL SUFFICIENCY / POLICY / MAINTAINER-FACING SYNTHESIS
```

This is a domain contract. It is not authorization for a generic runtime planner or universal pipeline framework.

## 5. Technical impact candidate

### 5.1 Definition

A technical impact candidate is a target-relevant proposition that the proposed dependency transition could cause or enable a technical consequence through a technical relationship with the exact target under relevant activation conditions.

Conceptually:

```text
UPSTREAM CHANGE MECHANISM
+
TARGET-RELEVANT EXPOSURE / PATH
+
ACTIVATION CONDITION(S)
+
POSSIBLE TARGET-RELEVANT CONSEQUENCE
=
TECHNICAL IMPACT CANDIDATE
```

### 5.2 Required boundaries

The following distinctions MUST remain intact:

```text
upstream change != target impact
```

```text
target relevance != target ownership
```

```text
one dependency transition != one aggregate impact candidate
```

```text
presence / use != activation
```

A target-relevant relation MAY be direct, multi-hop, framework/plugin-mediated, artifact-mediated, environment-mediated, dependency-owned, or another justified coupling. No universal exposure taxonomy is required by this specification.

### 5.3 Candidate formulation must not self-authorize truth

Candidate generation/formulation MUST NOT upgrade the evidential status of its components.

```text
candidate proposes exposure X
!= exposure X established
```

```text
candidate contains activation condition Y
!= Y active in the exact target context
```

```text
candidate describes possible consequence Z
!= consequence Z observed
```

Some components MAY already be independently established. Others MAY remain hypotheses or propositions requiring evidence. The candidate representation and downstream evaluation MUST preserve those distinctions.

A model-generated candidate MUST NOT assign its own applicability authority, evidence completeness, or final decision effect.

## 6. Candidate-specific applicability

### 6.1 Applicability scope

Applicability is evaluated for one mechanism-specific candidate against one exact target/revision/context.

The accepted candidate-level knowledge states are:

- **established applicable** — at least one complete represented viable applicability path is sufficiently established;
- **established not applicable** — every represented viable applicability path is sufficiently eliminated **and** the required path-model/evidence boundary is justified;
- **unresolved** — a material proposition needed to decide applicability cannot currently be established or refuted within the supported evidence boundary;
- **conflicted** — credible evidence about the same normalized proposition remains genuinely contradictory after relevant identity/revision/context/scope/time normalization.

### 6.2 Hard semantic protections

```text
applicable != consequence proven
```

```text
not applicable != missing evidence
```

```text
unresolved != negative evidence
```

```text
dependency/framework present != activation established
```

```text
target relevance != target ownership
```

### 6.3 Proposition-based evaluation

Candidate structure determines the necessary propositions and paths. There is no universal candidate checklist.

For a conjunctive path:

```text
A AND B AND C
```

refuting one necessary proposition eliminates that path.

For alternatives:

```text
A AND (B OR C)
```

refuting `B` alone does not eliminate the candidate while `C` remains viable.

Therefore:

- one sufficiently established complete viable path MAY establish positive candidate applicability;
- candidate-level non-applicability requires elimination of every represented viable path plus sufficient path-model coverage for the bounded candidate;
- unresolved/conflicted path detail MUST be preserved when collapsing it would erase material information.

A general Boolean AST, SAT engine, rule engine, or graph engine is not required by these semantics.

## 7. Three distinct coverage questions

The following MUST remain separate:

### 7.1 Evidence coverage

```text
Did the admitted evidence universe sufficiently cover proposition P?
```

This controls whether non-observation can support a stronger negative proposition within a justified bounded universe.

### 7.2 Path-model coverage

```text
Did this candidate represent the material alternative applicability routes
before claiming every viable route was eliminated?
```

A model of `A AND B` cannot claim global closure if a materially relevant `(A AND B) OR C` route belongs to the same candidate and `C` was omitted.

### 7.3 Candidate-discovery coverage

```text
Did impact discovery identify enough material mechanism-specific candidates
before making a transition-level claim that no relevant impact exists?
```

Therefore:

```text
evidence completeness
!= path-model completeness
!= candidate-discovery completeness
```

and:

```text
all discovered candidates not applicable
!= transition proven to have no material target impact
```

unless candidate-discovery coverage is independently justified.

Candidate granularity matters: an omitted route inside the same mechanism is path-model incompleteness; an omitted materially different mechanism/consequence is candidate-discovery incompleteness.

## 8. Open-world reasoning and negative evidence

Open-world reasoning is the safe default:

```text
not observed
→ unresolved / not observed within the admitted scope
```

not:

```text
not observed
→ absent
```

Closed-world reasoning is proposition-local and requires a justified bounded universe of discourse.

Strong negative evidence MAY arise from patterns such as:

1. explicit authoritative exclusion;
2. complete bounded inventory;
3. deterministic derivation from authoritative facts.

These are not declared exhaustive.

Completeness is itself an evidence claim. Model confidence MUST NOT manufacture completeness, absence, refutation, or non-applicability.

## 9. Evidence identity, scope, and observation strength

### 9.1 Identity and scope precede semantic use

Evidence used for a candidate/proposition MUST retain the material repository, revision, source, environment/job/path, time, and transformation identity needed to know what it actually supports.

Evidence from different scopes MUST NOT be silently combined into a stronger synthetic observation unless a separately justified composition rule establishes that the scopes describe the same proposition/context.

Examples of prohibited scope substitution include:

```text
Python 3.6 observed in environment A
+
requirements installation observed in environment B
→ Python-3.6 dependency environment established
```

unless evidence independently establishes that A and B are the same relevant environment/path.

### 9.2 Declaration/configuration evidence is not execution evidence

Static source/configuration evidence and runtime execution evidence are different observation classes.

```text
workflow definition declares command X
!= command X executed
!= command X succeeded
```

```text
environment formation path is statically declared
!= environment formation was observed at runtime
```

A consumer MAY legitimately answer a static proposition from definition evidence, but it MUST name the proposition at that strength. It MUST NOT relabel static declaration as runtime exercise/success merely because the configuration looks executable.

Likewise, runtime success MUST NOT be inferred from a successful broader job/run when exact step/command correlation is required by the owned proposition but has not been established.

### 9.3 Proxy and reconstructed evidence

Proxy evidence MAY narrow uncertainty but MUST NOT inherit exact-context authority.

A reconstruction MUST earn sufficient temporal/context/contrast fidelity for the proposition it is used to support. Same command, package label, runner label, or environment name at a later time does not by itself establish the same historical solved environment.

## 10. Deterministic and semantic authority

Source identity and authority precede semantic interpretation.

Prefer deterministic procedures for genuinely mechanical questions such as:

- exact identity;
- version membership/order;
- changed-file/source-span membership;
- bounded inventory membership;
- explicit set/configuration relations;
- validated dependency edges;
- deterministic applicability composition once proposition/path logic is explicit.

Bounded semantic reasoning MAY handle irreducible software meaning, provided it remains attributed, evidence-bound, reconstructable/grounded where practical, and uncertainty-preserving.

```text
deterministic transformation != authoritative source
```

```text
authoritative source != automatically deterministic meaning
```

The preferred trust shape is:

```text
deterministic acquisition / identity / scope
↓
bounded semantic interpretation where needed
↓
grounding / deterministic validation where possible
↓
bounded proposition evaluation
↓
minimum deterministic composition where explicit logic permits it
```

## 11. Investigation selection

### 11.1 Input to investigation reasoning

Investigation begins only from a **material non-final proposition state**, including:

```text
unresolved
OR
genuine conflict remaining after normalization
```

plus the location/reason of the uncertainty or conflict.

### 11.2 Discriminating target

A discriminating target is the missing fact, relation, observation, or counterfactual outcome whose resolution could materially change the proposition state or another decision-relevant investigation state.

Generate/check investigations from the uncertainty/conflict location and discriminating target, not from the broad dependency topic or whichever tools happen to be available.

### 11.3 Relevant is not enough

```text
relevant evidence != discriminating evidence
```

```text
information gain != decision-relevant information gain
```

Useful discrimination may fully resolve a proposition or materially reduce/prune uncertainty.

### 11.4 Three investigation boundaries

The following MUST remain separate:

**Epistemic investigation value / evidence admissibility**

```text
If obtained correctly, could this observation materially discriminate the proposition
and support a valid evidential interpretation?
```

**UpgradePilot automated-execution admissibility**

```text
May UpgradePilot itself perform this check under current capability,
security, authorization, environment, cost, non-mutation, and selected-plan boundaries?
```

**Maintainer-facing check recommendability**

```text
Should the maintainer later be asked to perform this otherwise useful check,
given repository policy, risk tolerance, urgency, budget, and final output semantics?
```

Therefore:

```text
epistemically useful
!= UpgradePilot-executable
!= maintainer-recommendable
```

The third boundary belongs partly to later synthesis/policy reasoning and MUST NOT be silently decided by Conversation-C investigation logic alone.

### 11.5 Comparison and sequencing

No numeric Value-of-Information optimizer is required.

Relevant investigation options SHOULD be compared qualitatively using proposition-relative considerations such as:

- discrimination direction/power;
- authority and exact scope/context alignment;
- coverage relevance;
- pruning/shared-gate leverage;
- cost/latency/invasiveness;
- reproducibility;
- complementarity/corroboration.

Clearly dominated options MAY be removed. Genuine trade-offs MUST remain explicit.

Investigation order need not equal proposition order, source order, cheapest-first, strongest-first, static-first, or dynamic-first.

Prefer conditional/adaptive sequencing:

```text
choose next justified investigation / small bundle
→ observe
→ validate
→ re-evaluate
```

rather than constructing a universal investigation tree.

## 12. Investigation validity and result feedback

```text
successful execution != valid evidence
```

An investigation result cannot receive stronger evidential meaning than its identity, temporal, context, contrast, and reconstruction fidelity permits.

Decision-relevant proposal-level discrimination remains distinct from causal mechanism attribution.

Normally:

```text
investigation result
→ validate evidential meaning
→ proposition evaluation
```

But an observation may expose an incomplete or materially different mechanism.

When that occurs, do not silently mutate the candidate. Preserve minimum lineage:

```text
Candidate V1
↓
Observation O exposes missing/different mechanism
↓
Candidate V2 refines or supersedes V1
```

The lineage must preserve enough information to explain:

- the original candidate;
- the triggering observation;
- the refined/new candidate;
- why the relationship changed.

No event-sourcing or persistence framework is implied.

## 13. Investigation stopping and the boundary to later synthesis

Investigation MAY stop when a check is impossible, unavailable/unrecoverable, non-discriminating, invalid for the proposition, unsafe/unauthorized for the attempted execution boundary, or otherwise incapable of producing useful admissible evidence.

A valid endpoint is:

```text
unresolved or conflicted
+
no further justified investigation
```

This MUST NOT be rewritten as:

```text
not applicable
safe
overall evidence sufficient
merge/defer recommendation
```

Investigation stopping and later maintainer-facing sufficiency are different responsibilities:

```text
INVESTIGATION
Should we acquire more evidence, what next check is worth pursuing,
and has worthwhile investigation stopped?
```

```text
LATER SYNTHESIS / POLICY
Given all candidates, repository context, observations, failures, and remaining uncertainty,
is the overall evidence state sufficient for a maintainer-facing output and how do policy/
residual-risk considerations affect that output?
```

The mature contract for the latter remains intentionally outside this specification until separately admitted and accepted.

## 14. Cross-candidate and repository-context boundary

One dependency transition may produce multiple mechanism-specific candidates plus material repository-context findings that do not belong inside one technical candidate.

This specification requires that implementations MUST NOT:

- force every material context/provenance inconsistency into a mechanism-specific applicability result;
- double-count semantically equivalent candidates merely because they were discovered by different methods;
- collapse distinct mechanisms into one opaque score;
- interpret completion of one candidate as proof that candidate discovery is complete.

The mature method for deduplication, candidate relationships, broad discovery coverage, and final cross-candidate synthesis remains open unless separately admitted.

## 15. Implementation acceptance guards

When an admitted implementation claims to satisfy part of this model, acceptance evidence SHOULD demonstrate the relevant smallest credible set of:

- exact candidate/transition/target identity;
- candidate formulation without self-authorized applicability;
- explicit proposition states and evidence coverage;
- correct necessary/alternative path composition;
- preservation of unresolved/conflicted information;
- negative inference only inside a justified bounded universe;
- declaration/configuration evidence not mislabeled as runtime execution;
- investigation selected from a concrete uncertainty/conflict location;
- execution/safety/recommendability boundaries kept distinct where relevant;
- observation validation before proposition reevaluation;
- candidate lineage when an observation changes the mechanism model;
- justified stopping without upgrading uncertainty into a final maintainer action.

Passing one fixture or mechanism proves only that bounded behavior. The complete owning responsibility remains governed by the Minimum Useful Generality specification.

## 16. Provenance and promotion history

This specification promotes durable accepted semantics from the following historical reasoning/evidence owners without rewriting those records:

- [`../../working-memory/2026-08-06_UPGRADEPILOT-product-decision-model-reconciliation.md`](../../working-memory/2026-08-06_UPGRADEPILOT-product-decision-model-reconciliation.md) — progressive Conversations A/B/C reconciliation and accepted decision index;
- [`../../audits/2026-08-10_AUDIT-003_post-conversation-c-product-decision-model.md`](../../audits/2026-08-10_AUDIT-003_post-conversation-c-product-decision-model.md) — independent pressure audit and accepted amendments on candidate formulation, coverage, conflicted states, investigation boundaries, composition, lineage, and stopping;
- C01 and C203 pressure-test evidence preserved by those records;
- subsequent B2 implementation/transfer evidence that exercised the accepted semantics without changing their owner.

Those artifacts remain valuable for **why/how** the decisions were reached. This specification is the normal owner for **what the accepted semantics are now**.

A future dated working-memory discussion that changes these semantics is not itself enough to silently supersede this specification. Once the change is accepted as durable, this owner must be updated explicitly with the relevant provenance link.

## 17. Change control

Change this specification only when the stable product decision/reasoning semantics change, including:

- impact-candidate meaning;
- applicability/coverage/negative-inference semantics;
- investigation-selection or stopping semantics;
- result-feedback/lineage rules;
- the accepted boundary to later synthesis.

Do not update it for:

- one implementation increment;
- one test pass/failure;
- one new mechanism-specific class;
- one working session;
- current stage/plan selection;
- source-file reorganization that preserves these semantics;
- a speculative mature-system idea not yet accepted.

When a durable change is accepted, update this specification and preserve the dated reasoning/audit/simulation evidence that motivated the change rather than requiring future sessions to reconstruct the accepted model from historical records.