# B2 Impact, Applicability, and Investigation Foundation Plan

**Status:** Approved B2 responsibility plan; revised 2026-08-12 for responsibility-shaped generality and continued end-to-end convergence. Live selection and continuation remain owned only by `../MEMORY.md`.  
**Owner:** Ali Rajabi  
**Parent gate:** [`B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md`](B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md)  
**Parent route:** [`UPGRADEPILOT_90_DAY_PLAN.md`](UPGRADEPILOT_90_DAY_PLAN.md)  
**Stable product authority:** [`../PROJECT_CHARTER.md`](../PROJECT_CHARTER.md)  
**Decision-model source:** [`../working-memory/2026-08-06_UPGRADEPILOT-product-decision-model-reconciliation.md`](../working-memory/2026-08-06_UPGRADEPILOT-product-decision-model-reconciliation.md)  
**Critical review evidence:** [`../audits/2026-08-10_AUDIT-003_post-conversation-c-product-decision-model.md`](../audits/2026-08-10_AUDIT-003_post-conversation-c-product-decision-model.md)  
**Generality control:** [`../docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md`](../docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md)  
**Trust/evidence invariants:** [`../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md`](../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md)  
**2026-08-12 planning correction:** [`../working-memory/2026-08-12_B2-responsibility-shaped-expansion-decision.md`](../working-memory/2026-08-12_B2-responsibility-shaped-expansion-decision.md)

## 1. Purpose

Define, implement, behavior-test, and pressure-test the B2 reasoning responsibility that turns trusted dependency-update evidence into explicit **technical impact candidates**, **candidate-specific applicability**, and **discriminating investigation / feedback / stopping** state, then hands concrete heterogeneous evidence forward to the minimum overall-sufficiency/synthesis responsibility required to complete B2.

The responsibility horizon is:

```text
trusted public-PR / dependency / upstream / target evidence
↓
mechanism-specific technical impact candidate(s)
↓
candidate-specific propositions and applicability
↓
material unresolved/conflicted state where applicable
↓
discriminating target
↓
selected investigation / conditional sequence / justified stop / non-dominated alternatives
↓
observation validation and feedback
↓
proposition reevaluation or candidate refinement
↓
heterogeneous technical/context evidence ready for overall B2 synthesis
```

This plan does **not** own the final maintainer-action method itself. It must, however, produce enough real implementation breadth that the later synthesis problem is exposed by actual product evidence rather than invented from one specimen.

## 2. Execution philosophy — responsibility horizon, incremental implementation

The earlier plan correctly prevented premature universalization, but its repeated `one thin slice → stop` posture is no longer sufficient for the current B2 learning and architecture needs.

Apply this rule throughout the remaining work:

```text
BOUND THE SUPPORTED DOMAIN
NOT THE KNOWN FIXTURE
```

Therefore:

```text
small coding step
!= small method horizon

first mechanism
!= universal architecture

stop one increment
!= stop broadening the owning responsibility
```

Implementation should remain small enough for Ali to trace, predict, test, diagnose, and learn. Consequential architecture/method decisions must be pressure-tested against the complete owning responsibility and materially different evidence shapes inside the admitted B2 domain.

Do not solve this by designing a universal framework in advance. Generality is **earned by contrast**:

```text
real mechanism 1
+
real mechanism 2
→ compare
→ extract demonstrated sameness
→ keep real differences mechanism-specific
```

## 3. Owning product question

For admitted public Python Dependabot dependency updates:

> What mechanism-specific technical concerns are justified by the evidence, what is known about whether each concern applies to the exact target/revision/context, what evidence is worth acquiring next when a material proposition remains non-final, and what trustworthy technical state should be handed to later overall B2 synthesis?

The later synthesis question remains separate:

> Given the technical results, repository context, evidence quality, and residual uncertainty, which supported maintainer action or abstention is justified overall?

This plan must not answer that second question implicitly through candidate state or investigation state.

## 4. Existing implementation foundation

The first implemented mechanism is the authoritative Python-support-drop / exact target-Python relation.

Existing anchor:

```text
bounded authoritative upstream Python-support-drop claim
+
exact target Python declaration
→ deterministic target-Python relevance
→ PythonSupportDropImpactCandidate
→ candidate-specific applicability
```

The implemented generic composition foundation already preserves:

- proposition state: established / refuted / unresolved / conflicted;
- proposition evidence coverage;
- conjunctive applicability paths;
- path-model coverage;
- candidate-level applicability while retaining path detail.

The mechanism-specific Python-support implementation preserves exact identity and can represent the important **pre-acquisition** state:

```text
target evidence not yet acquired
→ target proposition unresolved
→ evidence coverage insufficient
→ activation unresolved
→ candidate unresolved
```

That state is distinct from an acquisition/interpretation attempt that produced an explicit target-evidence problem.

The real application orchestration still acquires the target declaration in its pre-existing direct order. Runtime discriminating-investigation selection/feedback is therefore not yet implemented merely because the domain model can represent the pre-acquisition state.

S001 is an implementation anchor, not the product method horizon.

## 5. Required semantic guards

### 5.1 Candidate formulation does not create truth

```text
candidate component proposed
!= candidate component established
```

Candidate construction must preserve which mechanism/exposure/activation/consequence facts are independently established, derived, unresolved, or hypothetical.

No LLM, rule, parser, or candidate factory may self-authorize:

- exposure;
- activation;
- applicability;
- completeness;
- target impact absence;
- final maintainer action.

### 5.2 Candidate-specific applicability

Applicability is evaluated for one mechanism-specific candidate and exact target/revision/context.

Conceptual candidate states remain:

```text
established applicable
established not applicable
unresolved
conflicted
```

Protect:

```text
missing evidence != not applicable
not observed != absent without justified completeness
one established complete path can establish applicability
```

An unqualified `established not applicable` requires both:

1. every represented viable applicability path is sufficiently eliminated; and
2. path-model coverage is sufficient for that candidate-level negative claim.

Therefore:

```text
all represented paths refuted
+ path-model coverage unresolved/insufficient
→ preserve unresolved candidate-level limitation
```

### 5.3 Keep three coverage questions distinct

```text
EVIDENCE COVERAGE
Did admitted evidence sufficiently cover proposition P?
```

```text
PATH-MODEL COVERAGE
Did this candidate represent the material alternative applicability routes?
```

```text
CANDIDATE-DISCOVERY COVERAGE
Did technical-impact discovery identify enough material candidate mechanisms for any transition-level absence claim?
```

All discovered candidates being non-applicable does not establish transition-level absence of material impact without independently justified discovery coverage.

The remaining B2 work need not solve universal candidate-discovery completeness. It must avoid architecture and claims that pretend the known candidate families are exhaustive.

### 5.4 Deterministic composition should remain small and transparent

Where proposition/path logic is explicit and mechanical, keep it deterministic and behavior-tested.

Required composition contrasts include:

- one complete path established;
- all represented paths refuted + sufficient path-model coverage;
- all represented paths refuted + insufficient/unresolved path-model coverage;
- necessary proposition unresolved;
- genuine proposition conflict;
- established path plus irrelevant/conflicted alternative;
- unresolved alternative plus conflicted alternative.

Do not introduce a general Boolean AST, SAT solver, graph framework, or opaque scalar state merely because more than one mechanism now exists.

## 6. Discriminating investigation responsibility

### 6.1 Activation

Investigation reasoning starts only from a material non-final proposition/candidate state with an identifiable reason:

```text
unresolved
OR genuine conflict
+
uncertainty/conflict location
```

### 6.2 Discriminating target

Identify the missing fact, relation, observation, or counterfactual outcome that could materially change the justified state.

The target comes from the uncertainty, not a fixed source checklist.

### 6.3 Keep three boundaries distinct

```text
EPISTEMIC INVESTIGATION VALUE
Would the observation materially discriminate the owned proposition?
```

```text
UPGRADEPILOT EXECUTION ADMISSIBILITY
May UpgradePilot itself perform the investigation under capability/security/authorization/environment boundaries?
```

```text
MAINTAINER-FACING RECOMMENDABILITY
Should a maintainer later be asked to perform it?
```

The third remains later synthesis/action input.

### 6.4 Valid outcomes

The runtime reasoning must be capable of preserving:

```text
selected next investigation / small conditional sequence
```

or:

```text
no further justified investigation
```

or:

```text
multiple admissible non-dominated alternatives
with later preference unresolved
```

No numerical Value-of-Information optimizer is required.

### 6.5 Failed/unavailable investigation reuse

An investigation already attempted and failed/unavailable is not a fresh next investigation merely because the proposition remains unresolved.

```text
same failed investigation
→ retry only with concrete retry justification
```

Otherwise select a materially different justified investigation or preserve unresolved state with `no further executable investigation` as appropriate.

### 6.6 Revalidate before execution

Selection at time T1 is not permanent authorization to execute at time T2.

If newly admitted evidence resolves/refutes the target proposition or closes the necessary path before execution:

```text
selected investigation loses discriminating value
→ re-evaluate
→ prune/cancel if no longer justified
```

No queue/cancellation framework follows from this requirement. The invariant may be satisfied by a small state validation at the execution seam.

### 6.7 Feedback and candidate refinement

Normally:

```text
observation
→ validate evidential meaning
→ proposition/candidate reevaluation
```

If the observation exposes a materially different or incomplete mechanism:

```text
Candidate V1
→ triggering observation
→ Candidate V2 / refined candidate
```

Preserve minimum lineage and reason. Do not manufacture refinement or build an event-sourcing/history service merely to satisfy the invariant.

## 7. Materially diverse transfer set

Product-simulation evidence is used as architectural pressure, not as a sequential feature list.

### S001 — Python support-range interaction

Role:

- current real implementation anchor;
- deterministic applicability example;
- pre-acquisition target-declaration investigation anchor.

### S006 — targeted behavior-path investigation

Role:

- static evidence can leave an exact behavior proposition unresolved;
- dependency-version activation and target-code-path activation can be distinct;
- a differential execution can have real discriminating value;
- broad test presence is not equivalent to coverage of the implicated behavior path.

Do not infer that B2 now needs a universal differential executor.

### S007 — package-family contradiction and investigation pruning

Role:

- authoritative static package/build evidence can resolve a proposition before runtime semantics;
- one sufficient contradiction can prune redundant evidence;
- a selected check may become stale before execution;
- `no further check because resolved` differs from `no further executable check while unresolved`.

### S008 — artifact serviceability / installation mode

Role:

- **preferred second technical mechanism family** after the first real investigation loop;
- pressures package/interpreter admissibility, binary artifact availability, source fallback availability, and fallback success as separate propositions;
- demonstrates a technical impact before target application code executes;
- pressures heterogeneous candidate/result handling without requiring arbitrary target execution.

The product implementation must not hardcode CARLA/OpenCV identity. The mechanism must consume the real evidence form for the admitted capability.

### S009 — reproducibility/provenance context

Role:

- proves that decision-relevant repository context is not the same responsibility as technical applicability;
- prevents technical-candidate state from becoming an overloaded universal decision object;
- provides future overall-synthesis pressure, not a requirement to reopen technical applicability semantics.

## 8. Proportionality and non-goals

Broader responsibility pressure does **not** authorize speculative mature-system infrastructure.

Do not automatically introduce:

- universal impact-candidate generation;
- universal mechanism taxonomy;
- arbitrary repository-wide dependency graphs;
- universal plugin/framework analysis;
- generic investigation planner/decision tree;
- numerical ranking/utility optimization;
- generic differential-test executor;
- universal historical-environment reconstruction;
- autonomous target-repository code execution;
- one opaque universal impact/result score;
- automatic merge/approval/commenting or target mutation;
- persistence/service/queue infrastructure without separately demonstrated need.

Prefer existing source ownership. Create a new module/subpackage only when real implementation demonstrates a distinct responsibility and enters it in the same change.

## 9. Work sequence

The sequence is deliberately **incremental in implementation** but **broader in design pressure**.

### Phase 1 — complete the first real investigation loop

1. Inspect the active `investigation.py` orchestration seam and relevant impact/target/repository contracts before editing.
2. Use the existing Python-support candidate pre-acquisition state.
3. From `target declaration not yet acquired`, derive the exact target declaration as the discriminating target.
4. Select the existing read-only exact-head repository acquisition as the admitted investigation.
5. Validate the observation and feed it into the existing Target-Python relevance evaluator.
6. Reevaluate candidate applicability.
7. Preserve the materially different `already attempted and failed/unavailable` state without blind retry.
8. Add narrow tests before/alongside implementation, then run the nearest required regression proof.

This phase completes the first real:

```text
candidate
→ applicability
→ investigation selection
→ observation
→ reevaluation
```

runtime loop.

### Phase 2 — architecture/transfer checkpoint before declaring the foundation complete

After Phase 1 verification:

1. inspect the actual runtime/result/orchestration shape that now exists;
2. pressure it against S006, S007, S008, and S009 at the responsibility level;
3. identify where the design is genuinely reusable and where it is Python-support-specific;
4. specifically inspect whether `PublicPullRequestInvestigation` is growing toward one field/branch per known mechanism;
5. do **not** refactor merely for aesthetic symmetry; record only concrete pressure exposed by the contrast.

### Phase 3 — implement one second materially different technical mechanism family

The default selection is the S008-style **artifact-serviceability / installation-mode transition**, unless Phase 2 exposes a stronger lower-cost contrast.

The admitted first form should be the smallest credible real capability that can establish distinctions such as:

```text
package/interpreter admissibility
!= compatible binary artifact availability
!= source fallback availability
!= source fallback success
```

Use authoritative package/index/repository evidence and exact target context. Do not require dynamic source builds unless a proposition that actually matters remains unresolved and such execution is separately admissible.

The second mechanism must:

- preserve exact dependency/target/revision/provenance identity;
- formulate a mechanism-specific impact candidate without self-authorizing applicability;
- use the existing applicability composition only where its semantics genuinely fit;
- expose mechanism-specific propositions explicitly;
- support justified stop/non-activation when static evidence already resolves the owned proposition;
- reconnect to the real `PublicPullRequestInvestigation` path rather than existing only as a detached toy model;
- avoid known-case hardcoding.

### Phase 4 — earn or reject shared abstractions

With two implemented technical mechanisms available:

1. compare their candidate contracts, proposition ownership, applicability composition, evidence acquisition, investigation activation, and result integration;
2. extract only stable sameness demonstrated by both;
3. keep distinct mechanism semantics separate;
4. refactor orchestration only if the two real mechanisms demonstrate a concrete responsibility boundary;
5. reject generic abstractions whose only justification is imagined future breadth.

This is the main architecture-learning checkpoint.

### Phase 5 — explicit B2 synthesis handoff

After the first investigation loop and second mechanism/architecture checkpoint, ask:

```text
What concrete overall-sufficiency / repository-context /
residual-uncertainty / maintainer-output question now blocks
public PR → recommendation/abstention → traceable output?
```

Open only that concrete later responsibility. Do not continue deepening impact/applicability/investigation merely because more mechanisms exist.

The foundation is complete when it supplies credible heterogeneous technical state to this handoff and no foundational contradiction remains.

## 10. Proof obligations

Across the revised plan, controlled tests/evidence must establish at least:

- candidate formulation does not manufacture component truth;
- exact identity/revision/context survive candidate/proposition state;
- source-representation provenance does not silently change downstream meaning when canonical transition meaning is equivalent;
- dependency-change problem states do not enter as trusted transition evidence;
- missing evidence remains unresolved rather than refuted;
- candidate-level non-applicability requires sufficient represented-path elimination and path-model coverage;
- evidence/path/discovery coverage remain distinct;
- conflict remains distinct from unresolved;
- first pre-acquisition target evidence can activate a real admitted investigation;
- already-failed/unavailable acquisition does not create a blind retry loop;
- selected investigation can be revalidated/pruned when its discriminating value disappears;
- execution success alone does not establish evidential validity;
- `no further check because resolved` can remain distinguishable in explanation/state from `no further executable check while unresolved`;
- two materially different technical mechanisms can coexist without one universal opaque result or fixture-specific orchestration assumptions;
- the second mechanism processes real admitted input forms and representative variations rather than known repository/package/version answers;
- shared abstractions are supported by real cross-mechanism evidence;
- no later maintainer action is manufactured inside technical candidate/applicability/investigation state;
- the nearest complete deterministic suite passes after executable changes;
- safe live read-only proof is used where network evidence is part of a product claim.

## 11. Learning and ownership checkpoint

Ali should increasingly be able to:

1. explain why an upstream change is not yet target impact;
2. identify mechanism/exposure/activation/consequence for a concrete candidate;
3. predict proposition/path/candidate state transitions before a test runs;
4. explain why missing evidence is not negative evidence;
5. trace a non-final state into a discriminating target and investigation result;
6. distinguish epistemic investigation value, UpgradePilot execution permission, and later maintainer recommendation;
7. compare the Python-support and second technical mechanism and identify what is genuinely shared versus mechanism-specific;
8. identify when duplication is still healthier than abstraction and when two real mechanisms justify a common contract;
9. modify or add a bounded test and diagnose a failure with guidance appropriate to current depth;
10. explain how the implemented reasoning path moves the product toward the end-to-end B2 outcome.

Do not record mastery merely because AI-generated code passes.

## 12. Stop line

Stop **this plan** when all of the following are true:

```text
first Python-support candidate/applicability path
→ real discriminating investigation loop implemented and verified

+

one materially different technical mechanism family
→ implemented through the real application path
→ behavior-tested without case hardcoding

+

cross-mechanism architecture review
→ shared abstractions earned or explicitly rejected

+

heterogeneous technical state
→ concrete handoff question identified for B2 overall synthesis/output
```

Successful completion does **not** mean:

- the dependency update is safe;
- all Python impact mechanisms are supported;
- candidate discovery is complete;
- all applicability/exposure paths are modeled;
- all investigations are executable;
- the final five-action method is solved;
- B2 is automatically complete;
- B3/B4/B5/X1 breadth has moved into this plan.

The important change from the earlier stop line is:

> one successful Python-support specimen is no longer sufficient evidence to freeze the decision-foundation architecture.

## 13. Relationship to the older Transparent Decision plan

[`B2_TRANSPARENT_DECISION_METHOD_PLAN.md`](B2_TRANSPARENT_DECISION_METHOD_PLAN.md) remains superseded historical/pre-reconciliation and possible later-synthesis source material. It is not a second controlling plan for this responsibility and must not be silently reactivated.

## 14. Maintenance

Change this plan only when its responsibility horizon, admitted input/output boundary, work sequence, transfer expectations, proof obligations, or stop line changes.

Do not record live progress, latest commits, current blockers, or immediate continuation here. Those belong only in `../MEMORY.md`.
