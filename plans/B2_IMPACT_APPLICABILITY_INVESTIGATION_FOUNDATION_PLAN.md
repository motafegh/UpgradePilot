# B2 Impact, Applicability, and Investigation Foundation Plan

**Status:** Approved B2 responsibility plan; revised 2026-08-14 to align the accepted decision-model owner and add the evidence-earned cross-responsibility architecture gate. Live selection and continuation remain owned only by `../MEMORY.md`.  
**Owner:** Ali Rajabi  
**Parent gate:** [`B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md`](B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md)  
**Parent route:** [`UPGRADEPILOT_90_DAY_PLAN.md`](UPGRADEPILOT_90_DAY_PLAN.md)  
**Stable product authority:** [`../PROJECT_CHARTER.md`](../PROJECT_CHARTER.md)  
**Canonical decision-model semantics:** [`../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md`](../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md)  
**Historical decision-model rationale:** [`../working-memory/2026-08-06_UPGRADEPILOT-product-decision-model-reconciliation.md`](../working-memory/2026-08-06_UPGRADEPILOT-product-decision-model-reconciliation.md)  
**Critical review evidence:** [`../audits/2026-08-10_AUDIT-003_post-conversation-c-product-decision-model.md`](../audits/2026-08-10_AUDIT-003_post-conversation-c-product-decision-model.md)  
**Generality control:** [`../docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md`](../docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md)  
**Trust/evidence invariants:** [`../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md`](../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md)  
**Cross-responsibility architecture gate:** [`B2_CROSS_RESPONSIBILITY_ARCHITECTURE_RECONCILIATION_PLAN.md`](B2_CROSS_RESPONSIBILITY_ARCHITECTURE_RECONCILIATION_PLAN.md)  
**2026-08-12 planning correction:** [`../working-memory/2026-08-12_B2-responsibility-shaped-expansion-decision.md`](../working-memory/2026-08-12_B2-responsibility-shaped-expansion-decision.md)

## 1. Purpose

Define, implement, behavior-test, pressure-test, and structurally reconcile the B2 reasoning responsibility that turns trusted dependency-update evidence into explicit **technical impact candidates**, **candidate-specific applicability**, and **discriminating investigation / feedback / stopping** state, then hands concrete heterogeneous evidence forward to the minimum overall-sufficiency/synthesis responsibility required to complete B2.

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
evidence-earned architecture reconciliation across real mechanisms/source consumers
↓
heterogeneous technical/context evidence ready for overall B2 synthesis
```

This plan does **not** own the final maintainer-action method itself. It must, however, produce enough real implementation breadth that the later synthesis problem and the necessary shared architecture are exposed by actual product evidence rather than invented from one specimen.

## 2. Execution philosophy — responsibility horizon, incremental implementation

Apply throughout the remaining work:

```text
BOUND THE SUPPORTED DOMAIN
NOT THE KNOWN FIXTURE
```

and:

```text
small coding step
!= small method/architecture horizon

first mechanism
!= universal architecture

second implementation pressure
!= automatic permission to generalize everything

stop one increment
!= stop broadening the owning responsibility
```

Implementation should remain small enough for Ali to trace, predict, test, diagnose, and learn. Consequential architecture/method decisions must be pressure-tested against the complete owning responsibility and materially different evidence shapes inside the admitted B2 domain.

Generality is earned by contrast:

```text
real mechanism/source consumer 1
+
real mechanism/source consumer 2
→ compare
→ extract demonstrated sameness
→ keep real differences responsibility-specific
```

A second consumer is also an architecture trigger when it independently reimplements the same raw-source interpretation or when proof-strength semantics begin diverging. At that point, architecture reconciliation may become higher-value than further local feature growth.

## 3. Owning product question

For admitted public Python Dependabot dependency updates:

> What mechanism-specific technical concerns are justified by the evidence, what is known about whether each concern applies to the exact target/revision/context, what evidence is worth acquiring next when a material proposition remains non-final, and what trustworthy technical state should be handed to later overall B2 synthesis?

The later synthesis question remains separate:

> Given the technical results, repository context, evidence quality, and residual uncertainty, which supported maintainer action or abstention is justified overall?

This plan must not answer that second question implicitly through candidate state or investigation state.

## 4. Existing implementation foundation and intended pressure

The first mechanism family is the authoritative Python-support-drop / exact target-Python relation:

```text
bounded authoritative upstream Python-support-drop claim
+
exact target Python declaration
→ deterministic target-Python relevance
→ PythonSupportDropImpactCandidate
→ candidate-specific applicability
```

The shared deterministic applicability foundation preserves:

- proposition state: established / refuted / unresolved / conflicted;
- proposition evidence coverage;
- conjunctive applicability paths;
- path-model coverage;
- candidate-level applicability while retaining path detail.

The mechanism-specific Python-support path can represent pre-acquisition target uncertainty separately from an attempted acquisition that produced an explicit problem.

S001 remains an implementation anchor, not the product method horizon.

The selected materially different mechanism family is S008-style artifact serviceability / installation mode. It is intended to pressure:

```text
package/interpreter admissibility
!= compatible binary artifact availability
!= source fallback availability
!= source fallback success
```

It also provides a deliberate second-mechanism architecture contrast and, through target-environment evidence, can expose shared raw-source interpretation responsibilities with CI.

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

### 5.4 Keep proof classes distinct

The product decision model's observation/interpretation boundary applies directly to repository automation evidence:

```text
workflow definition declares command/path X
!= command/path X executed
!= command/path X succeeded
```

Likewise:

```text
successful CI job
!= implicated dependency behavior/path comprehensively covered
```

Static configuration can establish a static proposition at its own strength. It must not be mislabeled as runtime execution/success evidence.

### 5.5 Deterministic composition should remain small and transparent

Required composition contrasts include:

- one complete path established;
- all represented paths refuted + sufficient path-model coverage;
- all represented paths refuted + insufficient/unresolved path-model coverage;
- necessary proposition unresolved;
- genuine proposition conflict;
- established path plus irrelevant/conflicted alternative;
- unresolved alternative plus conflicted alternative.

Do not introduce a general Boolean AST, SAT solver, graph framework, or opaque scalar state merely because more than one mechanism exists.

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

Product-simulation evidence is architectural pressure, not a sequential feature list.

### S001 — Python support-range interaction

- first implementation anchor;
- deterministic applicability example;
- target-declaration investigation anchor.

### S006 — targeted behavior-path investigation

- static evidence can leave an exact behavior proposition unresolved;
- dependency-version activation and target-code-path activation can differ;
- broad test presence is not equivalent to implicated behavior coverage;
- a differential execution may have discriminating value.

### S007 — package-family contradiction and investigation pruning

- authoritative static evidence can resolve a proposition before runtime work;
- sufficient contradiction can prune redundant investigation;
- a selected check may become stale before execution.

### S008 — artifact serviceability / installation mode

- preferred materially different technical mechanism;
- pressures artifact inventory, target compatibility, source fallback, and source-build distinctions;
- exposes technical impact before target application code executes;
- pressures target-environment evidence and heterogeneous mechanism handling.

### S011 — optional-extra / CI-environment formation contrast

- runner/platform/Python presence does not prove the affected optional dependency environment is formed;
- `.[dev]` installation does not imply `.[mlx]` installation;
- static workflow evidence must be scoped to the exact job/source proposition;
- `not_observed` must not become established absence.

### S009 — reproducibility/provenance context

- decision-relevant repository context is not identical to technical applicability;
- future synthesis pressure must not overload one technical candidate object.

## 8. Proportionality and non-goals

Do not automatically introduce:

- universal impact-candidate generation;
- universal mechanism taxonomy;
- arbitrary repository-wide dependency graphs;
- universal plugin/framework analysis;
- generic investigation planner/decision tree;
- numerical ranking/utility optimization;
- generic differential-test executor;
- universal historical-environment reconstruction;
- universal GitHub Actions execution model;
- autonomous target-repository code execution;
- one opaque universal impact/result score;
- automatic merge/approval/commenting or target mutation;
- persistence/service/queue infrastructure without separately demonstrated need.

Prefer existing source ownership. Create shared primitives/modules only where the architecture reconciliation demonstrates identical responsibility/meaning and a precise owner.

## 9. Work sequence

The sequence is incremental in implementation but explicitly contains an architecture gate when real cross-responsibility pressure appears.

### Phase 1 — complete the first real investigation loop

1. inspect `investigation.py` and relevant impact/target/repository contracts;
2. derive a discriminating target from the Python-support pre-acquisition state;
3. select the admitted exact target-declaration acquisition;
4. validate the observation;
5. feed it into target relevance;
6. reevaluate candidate applicability;
7. preserve already-attempted/unavailable state without blind retry;
8. behavior-test and validate.

This phase completes:

```text
candidate
→ applicability
→ investigation selection
→ observation
→ reevaluation
```

### Phase 2 — first responsibility-level transfer checkpoint

After the first loop is proven:

1. pressure its result/orchestration shape against S006, S007, S008, and S009;
2. identify what is genuinely reusable and what is Python-support-specific;
3. inspect whether `PublicPullRequestInvestigation` is trending toward one field/branch per known mechanism;
4. record concrete pressure rather than refactoring for symmetry.

### Phase 3 — implement the second materially different mechanism until it creates real contrast

Use S008-style artifact serviceability as the default second mechanism.

The mechanism must:

- consume real admitted package/repository evidence;
- preserve exact dependency/target/revision/provenance identity;
- formulate a mechanism-specific candidate without self-authorizing applicability;
- expose its propositions explicitly;
- use shared applicability composition only where semantics genuinely fit;
- preserve explicit unresolved/insufficient target evidence;
- avoid known-case hardcoding.

Implementation may proceed in coherent increments, but **must pause before further local expansion once the second mechanism/source consumer exposes a concrete shared-ownership or proof-strength question**.

### Phase 4 — mandatory cross-responsibility architecture reconciliation gate

When Phase 3 exposes concrete cross-responsibility pressure, execute:

[`B2_CROSS_RESPONSIBILITY_ARCHITECTURE_RECONCILIATION_PLAN.md`](B2_CROSS_RESPONSIBILITY_ARCHITECTURE_RECONCILIATION_PLAN.md)

The gate must reconcile at least:

```text
GitHub Actions exact acquisition
→ normalized/static workflow structure
→ CI-specific interpretation
→ Target-specific interpretation

static workflow definition
!= runtime run/job/step evidence

shared installation/configuration observation
!= CI exercise conclusion
!= target runtime-formation conclusion

Python-support mechanism
+
artifact-serviceability mechanism
→ heterogeneous orchestration pressure
```

No further target-artifact-environment capability or cross-mechanism orchestration refactor should proceed through an unresolved ownership/proof-strength boundary.

The reconciliation decides whether a new ADR, an existing-ADR amendment, a bounded refactor plan, or explicit deferral is warranted.

### Phase 5 — implement the accepted architecture/refactor handoff

Only if Phase 4 justifies source changes:

1. implement the smallest coherent shared/source-contract migration;
2. preserve CI-specific and Target-specific semantics;
3. refine proof-strength naming/contracts if the accepted architecture requires it;
4. migrate tests by responsibility;
5. keep multiple-job/matrix/reusable/container support bounded to the admitted interpretation surface;
6. run focused + nearest + full regression validation.

If Phase 4 rejects a shared abstraction, preserve the explicit reason and continue with separated implementations under clarified semantics.

### Phase 6 — resume and complete the second mechanism through the real application path

After the architecture gate/handoff:

1. continue target evidence toward exact compatibility only where justified;
2. reconnect artifact serviceability to the real `PublicPullRequestInvestigation` path;
3. integrate heterogeneous technical results using only abstractions earned by the two mechanisms;
4. preserve mechanism-specific evidence/candidate semantics;
5. stop deeper investigation when static evidence is sufficient or no justified next observation remains.

### Phase 7 — explicit B2 synthesis handoff

Ask:

```text
What concrete overall-sufficiency / repository-context /
residual-uncertainty / maintainer-output question now blocks
public PR → recommendation/abstention → traceable output?
```

Open only that concrete later responsibility. Do not continue deepening impact/applicability/investigation merely because more mechanisms exist.

The foundation is complete when it supplies credible heterogeneous technical state to this handoff and no foundational architecture contradiction remains.

## 10. Proof obligations

Across this plan, controlled tests/evidence must establish at least:

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
- selected investigation can be revalidated/pruned when discriminating value disappears;
- execution success alone does not establish evidential validity;
- static workflow declaration/configuration remains distinct from runtime execution/success;
- `no further check because resolved` remains distinguishable from `no further executable check while unresolved`;
- two materially different mechanisms can coexist without one opaque universal result or fixture-specific orchestration assumptions;
- the second mechanism processes real admitted inputs/variations rather than known repository/package/version answers;
- duplicated/shared source interpretation is reconciled before it expands into parallel architectures;
- any shared abstraction is supported by real semantic sameness, not only repeated syntax;
- CI and Target retain distinct proof responsibilities;
- multi-environment evidence is not flattened into one repository-wide union;
- no later maintainer action is manufactured inside technical candidate/applicability/investigation state;
- the nearest complete deterministic suite passes after executable changes;
- safe live read-only proof is used where network evidence is part of a product claim.

## 11. Learning and ownership checkpoint

Ali should increasingly be able to:

1. explain why an upstream change is not yet target impact;
2. identify mechanism/exposure/activation/consequence for a concrete candidate;
3. predict proposition/path/candidate state transitions;
4. explain why missing evidence is not negative evidence;
5. trace a non-final state into a discriminating target and investigation result;
6. distinguish epistemic investigation value, UpgradePilot execution permission, and later maintainer recommendation;
7. compare Python-support and artifact-serviceability and identify genuinely shared versus mechanism-specific semantics;
8. distinguish raw source acquisition, normalized workflow structure, static configuration evidence, runtime execution evidence, and domain interpretation;
9. identify when duplication remains healthier than abstraction and when a second real consumer justifies a shared primitive;
10. reason about package dependency direction and ownership rather than only function-level code;
11. modify/add a bounded test and diagnose a failure with guidance appropriate to current depth;
12. explain how the implemented reasoning path moves UpgradePilot toward the end-to-end B2 outcome.

Do not record mastery merely because AI-generated code passes.

## 12. Stop line

Stop **this plan** when all of the following are true:

```text
first Python-support candidate/applicability path
→ real discriminating investigation loop implemented and verified

+

one materially different technical mechanism family
→ implemented with real admitted evidence and target-applicability pressure

+

cross-responsibility architecture reconciliation
→ shared source/proof/orchestration boundaries explicitly decided
→ required refactor implemented or explicit deferral/rejection recorded

+

second mechanism
→ connected through the real application path
→ behavior-tested without case hardcoding

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
- GitHub Actions is universally interpreted;
- repository environments are universally reconstructed;
- the final five-action method is solved;
- B2 is automatically complete;
- B3/B4/B5/X1 breadth has moved into this plan.

## 13. Relationship to historical plans

[`B2_TRANSPARENT_DECISION_METHOD_PLAN.md`](B2_TRANSPARENT_DECISION_METHOD_PLAN.md) remains superseded historical/pre-reconciliation and possible later-synthesis source material. It is not a second controlling plan for this responsibility.

[`B2_SOURCE_CODE_STRUCTURE_RECONCILIATION_PLAN.md`](B2_SOURCE_CODE_STRUCTURE_RECONCILIATION_PLAN.md) is a **completed historical structural precedent** for responsibility-based packages and evidence-earned shared primitives. It must not be silently reactivated as the plan for the new CI/Target/workflow/orchestration architecture question. The new question is owned by [`B2_CROSS_RESPONSIBILITY_ARCHITECTURE_RECONCILIATION_PLAN.md`](B2_CROSS_RESPONSIBILITY_ARCHITECTURE_RECONCILIATION_PLAN.md).

## 14. Maintenance

Change this plan only when its responsibility horizon, admitted input/output boundary, work sequence, architecture gate, transfer expectations, proof obligations, or stop line changes.

Do not record live progress, latest commits, current blockers, or immediate continuation here. Those belong only in `../MEMORY.md`.