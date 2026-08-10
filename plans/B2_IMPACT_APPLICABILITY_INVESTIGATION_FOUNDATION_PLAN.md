# B2 Impact, Applicability, and Investigation Foundation Plan

**Status:** Candidate bounded plan — not controlling until explicitly selected in `../MEMORY.md`  
**Owner:** Ali Rajabi  
**Parent gate:** [`B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md`](B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md)  
**Parent route:** [`UPGRADEPILOT_90_DAY_PLAN.md`](UPGRADEPILOT_90_DAY_PLAN.md)  
**Stable product authority:** [`../PROJECT_CHARTER.md`](../PROJECT_CHARTER.md)  
**Decision-model source:** [`../working-memory/2026-08-06_UPGRADEPILOT-product-decision-model-reconciliation.md`](../working-memory/2026-08-06_UPGRADEPILOT-product-decision-model-reconciliation.md)  
**Critical review evidence:** [`../audits/2026-08-10_AUDIT-003_post-conversation-c-product-decision-model.md`](../audits/2026-08-10_AUDIT-003_post-conversation-c-product-decision-model.md)  
**Applicable generality control:** [`../docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md`](../docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md)  
**Applicable trust/evidence invariants:** [`../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md`](../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md)

## 1. Purpose

Define, implement, and behavior-test the smallest credible B2 product slice that turns already trusted dependency/update evidence into explicit **technical impact-candidate**, **candidate-specific applicability**, and **targeted investigation-selection** state before UpgradePilot attempts final overall sufficiency or maintainer-action semantics.

The bounded responsibility is:

```text
validated public-PR / dependency / upstream / target evidence
↓
mechanism-specific technical impact candidate
↓
candidate-specific propositions and applicability state
↓
material unresolved/conflicted state where applicable
↓
discriminating target
↓
bounded next investigation / conditional sequence / justified stop / non-dominated alternatives
↓
observation feedback into proposition evaluation or candidate refinement
↓
explicit pre-D handoff state
```

This plan intentionally stops **before** Conversation-D ownership of:

- overall evidence sufficiency for a maintainer action;
- repository-policy and residual-risk acceptance;
- final decision stopping relative to an action;
- final maintainer-facing action vocabulary and projection.

It is therefore a decision-foundation plan, not a hidden final recommendation engine.

## 2. Why this new plan exists

The earlier [`B2_TRANSPARENT_DECISION_METHOD_PLAN.md`](B2_TRANSPARENT_DECISION_METHOD_PLAN.md) was written before the A–C reconciliation. It usefully preserved the B2 user boundary, traceability, abstention discipline, controlled contrast testing, non-hardcoding, and safe live-proof requirements, but its central method shape still moves too directly from evidence interpretation to sufficiency and maintainer action.

A–C reconciliation established responsibilities that must exist before final decision semantics can be implemented safely:

```text
A — technical impact candidate
B — candidate-specific applicability / evidence / negative inference
C — uncertainty/conflict-driven investigation selection and stopping
D — later overall sufficiency / policy / maintainer-facing synthesis
```

This candidate plan is written from that post-reconciliation model rather than using the old plan's section structure as a constraint.

The old plan remains historical/source material until an explicit comparison and promotion decision determines whether it should be superseded, narrowed to later D work, or archived.

## 3. Owning product question

For one admitted public Python Dependabot dependency-update pull request:

> **What mechanism-specific technical concern is justified by the evidence, what is currently known about whether that concern applies to the exact target/revision/context, and—when material state remains unresolved or genuinely conflicted—what evidence acquisition or check is worth pursuing next?**

This plan does **not** yet answer the later question:

> Which final maintainer action is justified overall?

That distinction is deliberate.

## 4. Relationship to the Charter and B2

The Project Charter still owns the final supported decision family:

1. merge after normal review;
2. run targeted checks;
3. investigate or block;
4. defer;
5. abstain.

This plan does not replace or redefine those outputs. It supplies the internal evidence-backed reasoning foundation required before a later method can project technical findings and remaining uncertainty into that action family.

B2 remains the public-PR vertical slice. Whole-product reasoning may be broader than B2 implementation, but B2 must implement only the thinnest credible manifestation needed to learn from real behavior.

Therefore:

```text
whole-product A–C semantics
!= implement every possible A–C technique in B2
```

### 4.1 Admitted input boundary

This plan begins **after** the existing B2 dependency-change foundation has established one trusted canonical exact-version Python dependency transition from an admitted representation.

The admitted downstream input preserves exact proposal/repository/base/head/dependency/version identity and source provenance. Representation provenance remains relevant evidence, but it does not silently establish semantic facts that belong later in the reasoning path.

Preserve:

```text
dependency representation
→ where/how package + version transition was established
```

but not:

```text
dependency representation
→ direct/transitive role established
→ target usage established
→ CI consumption established
→ technical impact established
→ compatibility/safety established
```

Unsupported, malformed, incomplete, ambiguous, multiple, or conflicting dependency-change inputs remain explicit upstream problem states and must not be forced through A–C reasoning as if a trusted transition existed.

Equivalent trusted canonical transitions established from different admitted source representations must not acquire different A–C meaning merely because their provenance differs, unless that provenance supplies independently relevant evidence for a later proposition.

This plan does not reimplement the already-proven dependency parser/normalizer merely to exercise decision semantics.

## 5. Existing implementation foundation

The first implementation anchor should reuse the strongest already behavior-validated responsibility rather than introduce a new ecosystem mechanism merely to exercise the model.

Current anchor:

```text
bounded upstream Python support-drop claim
+
exact target Python declaration
→ deterministic target-Python relevance
```

The completed S001 path already proves important building blocks:

- exact PR/dependency/version identity;
- authoritative upstream interval evidence;
- bounded semantic extraction with deterministic source reconstruction/validation;
- exact target `requires-python` interpretation;
- deterministic target relevance;
- explicit unresolved/problem states;
- safe read-only orchestration.

The first A–C slice should make the **reasoning responsibilities around that proven mechanism explicit** instead of adding broad new acquisition capability first.

### 5.1 First mechanism-specific implementation anchor

Representative impact candidate:

```text
UPSTREAM MECHANISM
proposed dependency transition crosses an authoritative Python-support drop
+
EXPOSURE / RELATION
exact target declares an installation Python range that may intersect that dropped support
+
ACTIVATION
at least one Python version admitted by the exact target declaration is affected by the upstream support change
+
POSSIBLE CONSEQUENCE
the proposed dependency may no longer support part of the target's declared installation range
```

This is one bounded candidate family. It is **not** the universal impact model.

S001 may exercise a resolved/not-applicable-like target-range relation, while controlled variants should exercise unresolved, conflicted, and investigation-selection behavior without hardcoding S001's expected answer.

## 6. Required semantic guards

### 6.1 Candidate formulation does not create truth

```text
candidate component proposed
!= candidate component established
```

Candidate construction must preserve which mechanism/exposure/activation/consequence facts are independently established, which are derived, and which remain hypotheses requiring B-level evaluation.

An LLM- or rule-generated candidate must not self-authorize exposure, activation, applicability, completeness, or final action.

### 6.2 Candidate-specific applicability

Applicability is evaluated for one mechanism-specific candidate and one exact target/revision/context.

Conceptual states remain:

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
one established complete viable path can establish applicability
```

An unqualified `established not applicable` candidate state requires **both**:

1. every represented viable applicability path is sufficiently eliminated; and
2. path-model coverage is sufficiently justified for the candidate-level non-applicability claim.

Therefore:

```text
all represented paths refuted
+
path-model coverage sufficient
→ established not applicable may be justified
```

but:

```text
all represented paths refuted
+
path-model coverage unresolved / insufficient
→ do not assign unqualified established not applicable
```

In the latter case, preserve the represented path refutations **and** the unresolved coverage limitation. Do not let closure of the paths currently modeled masquerade as proof that every material applicability route for that candidate has been represented and eliminated.

### 6.3 Three coverage questions

Keep distinct:

```text
EVIDENCE COVERAGE
Did the admitted evidence sufficiently cover proposition P?
```

```text
PATH-MODEL COVERAGE
Did this candidate represent the material alternative applicability routes?
```

```text
CANDIDATE-DISCOVERY COVERAGE
Did impact discovery identify enough material mechanism-specific candidates
for any transition-level absence claim?
```

Therefore:

```text
all discovered candidates not applicable
!= transition proven to have no material target impact
```

unless discovery coverage is independently justified.

The first slice does not need to solve universal candidate-discovery coverage. It must simply refuse to overclaim beyond the bounded candidate family it actually supports.

### 6.4 Minimum deterministic composition only

Where proposition/path logic is explicit and mechanical, composition should be deterministic.

The first implementation must define and test only the minimum behavior needed for the selected slice across:

```text
established
refuted
unresolved
conflicted
```

including at least:

```text
one complete path established + unnecessary alternative conflicted
```

```text
all represented alternatives refuted + sufficient path-model coverage
```

```text
all represented alternatives refuted + unresolved/insufficient path-model coverage
```

```text
one alternative unresolved + another conflicted
```

Do not assume a scalar state-precedence table is automatically lossless. Preserve path-level information when collapsing it would erase material uncertainty/conflict or an unresolved path-model-coverage limitation.

Do not introduce a general Boolean AST, SAT solver, graph framework, or rule engine merely to satisfy this proof.

## 7. Conversation-C investigation responsibility

### 7.1 Activation input

C activates only from a material non-final proposition state:

```text
unresolved
OR genuine conflict remaining after B normalization
+
uncertainty/conflict location or reason
```

### 7.2 Discriminating target

Identify the missing fact, relation, observation, or counterfactual outcome that could materially change the justified state.

For the first Target-Python anchor, examples may include:

- the exact target Python declaration at the frozen PR head;
- whether a specific target range actually admits an affected Python version;
- whether conflicting target declarations are genuinely contradictory after scope/revision normalization.

The investigation question comes from the uncertainty location—not from a fixed source checklist.

### 7.3 Three investigation boundaries

Preserve separately:

```text
EPISTEMIC INVESTIGATION VALUE
Would this check, if correctly obtained, materially discriminate the proposition?
```

```text
UPGRADEPILOT EXECUTION ADMISSIBILITY
May UpgradePilot itself perform the check under capability/security/authorization/environment boundaries?
```

```text
MAINTAINER-FACING RECOMMENDABILITY
Should the maintainer later be asked to run the check given policy/risk/budget/output semantics?
```

The third is not owned by this plan; it is retained as later D input.

### 7.4 Valid C outcome families

The bounded selection method must be capable of representing:

```text
selected next investigation / small conditional sequence
```

or:

```text
no further justified investigation
```

or:

```text
multiple admissible non-dominated alternatives remain;
residual preference depends on later maintainer/policy/decision context
```

No numerical Value-of-Information optimizer is required or accepted.

### 7.5 Investigation validity and failed-check reuse

```text
successful execution != valid evidence
```

Observation meaning cannot exceed identity, temporal, context, contrast, and reconstruction fidelity.

Proxy evidence may narrow uncertainty without inheriting exact-context authority. Scope substitution is prohibited.

An investigation that has already been attempted and failed or proved unavailable does not become a fresh justified next investigation merely because the proposition remains unresolved.

```text
same failed investigation
→ retry only with a concrete retry justification
```

A concrete retry justification must identify what materially changed or why another attempt is now expected to produce usable evidence—for example, a transient/recoverable failure condition has cleared, the request defect has been corrected, or an admitted bounded retry condition has become true. Otherwise select a materially different justified investigation if one exists, or preserve `no further executable investigation` and the unresolved/conflicted proposition state as appropriate.

### 7.6 Investigation feedback and lineage

Normally:

```text
observation
→ validate evidential meaning
→ B proposition reevaluation
```

If an observation exposes a materially different/incomplete mechanism:

```text
Candidate V1
↓
Observation O
↓
Candidate V2 refines/supersedes V1
```

Preserve the minimum lineage required to explain what changed and why. No event-sourcing or persistence framework is implied.

## 8. Proportionality and explicit non-goals

The first implementation/evaluation slice must **not** automatically introduce:

- universal impact-candidate generation;
- arbitrary repository-wide dependency graph infrastructure;
- universal plugin/framework analysis;
- generic investigation planner/decision tree;
- numerical VoI/ranking;
- generic differential-test executor;
- universal historical-environment reconstruction;
- autonomous target-repository code execution;
- complete impact/exposure/investigation taxonomy;
- final D-level sufficiency formula;
- final five-action recommendation engine;
- automatic merge/approval/commenting or target mutation;
- persistence/service/queue infrastructure without separately demonstrated need.

The implementation should reuse current source organization and existing evidence contracts unless a real responsibility cannot be represented cleanly.

## 9. Work sequence

### Step 1 — Freeze the post-reconciliation baseline

Before editing product source:

- inspect the current `investigation.py` orchestration path and relevant target/upstream domain contracts;
- inspect active tests for Target-Python relevance and problem states;
- record the last verified implementation proof without silently upgrading it;
- confirm no uncommitted/parallel work is being overwritten.

Do not redesign from working-memory diagrams alone.

### Step 2 — Define the first bounded A candidate contract

Using the Target-Python support-drop mechanism, define the smallest representation needed to preserve:

- exact proposal/dependency/target identity;
- upstream mechanism evidence/claim reference;
- target-relevant relation/exposure;
- activation proposition(s);
- possible consequence;
- evidential status of candidate components.

Do not encode S001 repository/package/version identity or expected answer.

Do not decide a universal candidate schema if a narrower mechanism-specific representation provides better learning evidence.

### Step 3 — Derive explicit B propositions and path logic

For the selected candidate, specify only the propositions actually needed to determine applicability.

At minimum separate:

- upstream affected-version/mechanism establishment;
- exact target declaration/context establishment;
- intersection/activation relation;
- any alternative path represented by the selected candidate.

For every proposition identify:

- evidence owner/source;
- deterministic versus semantic evaluation responsibility;
- possible established/refuted/unresolved/conflicted result;
- what coverage boundary is required for negative inference.

### Step 4 — Define minimum composition semantics with controlled examples

Before generic composition code, freeze the bounded behavior for the selected proposition/path shapes.

Exercise at least:

1. one complete path established;
2. all represented paths refuted **and path-model coverage sufficiently justified** → candidate-level `established not applicable` may be justified;
3. all represented paths refuted **but path-model coverage unresolved/insufficient** → preserve the refutations and coverage limitation; do not assign unqualified `established not applicable`;
4. necessary proposition unresolved;
5. genuine proposition conflict;
6. established complete path plus irrelevant/conflicted alternative;
7. unresolved alternative plus conflicted alternative.

The output must preserve enough path/proposition/coverage detail to explain the candidate state.

### Step 5 — Define one real C activation from the current evidence path

Use an actual uncertainty that can arise in the Target-Python path rather than inventing a generic planner scenario.

Distinguish two materially different situations.

**A. Exact target declaration evidence has not yet been acquired:**

```text
grounded upstream Python support-drop candidate
+
exact target Python declaration not yet acquired
→ unresolved activation proposition
→ discriminating target = exact authoritative target declaration
→ candidate investigation = acquire/read the exact-head declaration
   through an already-supported read-only repository interface
```

This is a legitimate first acquisition because the discriminating evidence has not yet been requested through that admitted path.

**B. The exact acquisition was already attempted and failed or is unavailable:**

```text
exact-head acquisition already attempted
+
failed / unavailable
→ do not simply select the identical failed investigation again
```

Retry the same acquisition only when a concrete retry justification exists and is recorded. Otherwise:

- select a materially different justified investigation that can still discriminate the proposition; or
- preserve `no further executable investigation` and the unresolved/conflicted state when no such admitted investigation exists.

Also define controlled variants for:

- genuine conflicting target declarations → conflict-driven investigation target;
- two non-dominated useful check descriptions where later policy would be needed to prefer one, without requiring UpgradePilot to execute either.

### Step 6 — Define investigation selection/output contract

The minimum pre-D C result should preserve:

- triggering proposition/candidate identity;
- uncertainty/conflict reason;
- discriminating target;
- proposed/selected investigation or bounded alternatives;
- epistemic evidential value;
- whether UpgradePilot execution is admitted;
- reason for non-activation/non-selection where material;
- prior failed/unavailable investigation state and concrete retry justification when the same investigation is reconsidered;
- no-further-investigation reason when applicable;
- evidence required to reevaluate the proposition;
- later maintainer-recommendability left explicitly undecided where D-owned.

Names/field shapes remain implementation decisions until the bounded contract is reviewed.

### Step 7 — Preserve candidate-refinement feedback behavior when naturally exercised

The invariant remains mandatory whenever an observation causes candidate refinement or supersession:

```text
original Candidate V1
→ triggering observation
→ Candidate V2 / refined candidate
→ explicit relationship/reason
```

However, the first Target-Python implementation slice must **not manufacture a candidate-refinement scenario merely to satisfy the plan**.

During design, ensure the selected representation does not make future refinement lineage impossible. Actual implementation and testing of refinement behavior are required in this slice only if the selected Target-Python behavior naturally exercises candidate refinement/supersession. Otherwise preserve the invariant as a future activated obligation and continue without fabricating a case.

Do not implement a generic candidate-history service.

### Step 8 — Review architecture placement before coding

Map responsibilities onto the existing source organization.

Prefer extending existing target/upstream/application/domain boundaries where ownership is already clear.

Create a new module only when a distinct responsibility is demonstrated by the selected slice.

Do not create generic `planner`, `graph`, `rules`, `engine`, `common`, or `utils` modules merely because the conceptual model contains those words.

If a consequential new semantic/model method is required, apply normal ADR/technology-admission rules before permanent adoption.

### Step 9 — Implement the smallest vertical A–C slice

Implementation should reconnect to the real read-only public-PR path rather than exist only as a detached toy model.

Expected conceptual path:

```text
existing trusted evidence
→ bounded impact candidate
→ explicit proposition evaluation
→ candidate applicability state
→ C activation only for material non-final state
→ bounded investigation result
→ observation feedback where supported
```

Keep existing evidence acquisition/results visible rather than replacing them with a single opaque decision object.

### Step 10 — Prove controlled behavior

Narrow tests must prove:

- candidate formulation does not self-establish component truth;
- exact identity/revision/context survive into candidate/proposition state;
- equivalent canonical dependency transitions from different admitted source representations do not change A–C meaning solely because their provenance differs;
- unsupported/malformed/incomplete/ambiguous/multiple/conflicting dependency-change problem states do not enter A–C as trusted transitions;
- positive applicability needs one established complete represented path;
- candidate-level `established not applicable` requires both closure of every represented viable path **and** sufficient path-model coverage for that non-applicability claim;
- all represented paths being refuted while path-model coverage remains unresolved/insufficient does **not** produce an unqualified `established not applicable` state;
- missing evidence remains unresolved without justified completeness;
- genuine conflict remains distinct from unresolved;
- evidence/path/discovery coverage are not conflated;
- mixed unresolved/conflicted alternatives do not lose material state;
- C activates from unresolved or genuine conflict only when a discriminating target exists;
- target evidence not yet acquired can select the existing exact-head read-only acquisition, while an identical acquisition already attempted and failed/unavailable is not immediately selected again without concrete retry justification;
- after an already failed/unavailable acquisition, a materially different justified investigation may be selected, or `no further executable investigation` preserves the unresolved/conflicted state;
- one real read-only investigation can be selected and executed only under the admitted capability boundary;
- execution success still requires evidence validation;
- no-further-investigation preserves unresolved/conflicted state;
- multiple non-dominated alternatives can remain without fake ranking;
- **if** candidate refinement/supersession is naturally exercised by the selected slice, minimum V1 → triggering observation → V2/refined-candidate lineage is preserved; absence of a naturally triggered refinement does not fail this first slice;
- no D-level final maintainer action is invented.

Then run the nearest complete deterministic suite required by the active source boundary.

### Step 11 — Run one safe integrated proof

Use the existing public command or the nearest real application entry point to exercise the bounded A–C state through one supported public case after controlled tests establish non-hardcoded behavior.

The proof must state exactly what it demonstrates and does not demonstrate.

A successful Target-Python anchor proves one mechanism-specific A–C slice, not universal candidate discovery, universal applicability, or recommendation correctness.

### Step 12 — Ownership and learning checkpoint

Ali should be able to:

1. explain why an upstream change is not yet target impact;
2. identify candidate mechanism/exposure/activation/consequence for the implemented slice;
3. predict at least one proposition-state transition before running the test;
4. explain why missing evidence is not refutation;
5. trace one unresolved/conflicted state into its discriminating target and investigation result;
6. distinguish epistemic check value from UpgradePilot execution permission and later maintainer recommendation;
7. modify or add one bounded proposition/composition/investigation test with guidance appropriate to current learning depth;
8. explain the exact stop line and why broader planner/graph/D work was deferred.

Do not record mastery merely because AI-generated code passes.

### Step 13 — Post-slice architecture and D-dependency review

After implementation/evaluation, ask:

```text
Did real code expose a foundational A/B/C contradiction?
```

If yes, reopen only the affected concept with concrete evidence.

Otherwise ask:

```text
What specific overall-sufficiency / repository-policy /
maintainer-output question now blocks completing B2?
```

Open Conversation D only around that concrete dependency.

Do not expand theory simply because D is next alphabetically.

## 10. Controlled contrast and transfer set

The first implementation anchor is Target-Python, but the design must be challenged against structurally different evidence without implementing all of them.

Use as review/transfer material:

### S001 — Python-support range interaction

Purpose:

- primary real implementation anchor;
- deterministic target-relevance path;
- resolved-range example;
- basis for controlled missing/conflicting target-evidence variants.

### Kedro / Pluggy

Purpose:

- semantic-heavy plugin/inverted-control challenge;
- protects `uses dependency != participates in mechanism != relies on changed property`;
- tests that the selected representation is not falsely claimed universal.

### pip-audit / CacheControl / urllib3

Purpose:

- multi-hop/transitive path challenge;
- tests path-model versus candidate-discovery coverage boundaries;
- must not force graph infrastructure into the first slice.

### C01 grpcio-tools code generation

Purpose:

- artifact-mediated challenge;
- tests direct interventional investigation reasoning, contrast validity, and candidate-refinement feedback;
- must not authorize arbitrary target execution.

### C203 Buildtest / OpenSSL

Purpose:

- environment/historical challenge;
- tests proxy evidence, reconstruction fidelity, recoverability, and `unresolved + no further justified investigation`.

Transfer review passes when the first-slice model can explain where these cases differ and what would need additional bounded capability, without hardcoding them or pretending to support them automatically.

## 11. Acceptance evidence

This plan passes only when all of the following are demonstrated for the admitted first slice:

- one trusted canonical dependency transition enters independently of its admitted source representation;
- upstream dependency-change problem states remain distinct and do not masquerade as trusted A–C input;
- one mechanism-specific impact candidate is represented from real trusted evidence without fixture identity hardcoding;
- candidate formulation preserves rather than manufactures component evidential status;
- explicit candidate-specific propositions are evaluated with source/identity/coverage discipline;
- minimum deterministic path composition is behavior-tested across established/refuted/unresolved/conflicted combinations required by the slice;
- candidate-level non-applicability is never promoted to unqualified `established not applicable` unless both all represented viable paths are sufficiently eliminated and path-model coverage is sufficient for that claim;
- evidence coverage, path-model coverage, and candidate-discovery coverage are not collapsed;
- one material unresolved/conflicted state can produce a grounded discriminating target and bounded investigation result;
- investigation selection distinguishes not-yet-acquired evidence from an identical acquisition already attempted and failed/unavailable, and does not create unjustified retry loops;
- epistemic investigation value remains distinct from UpgradePilot execution admissibility and later maintainer-facing recommendability;
- no-further-investigation and non-dominated-alternative outcomes can be represented without manufacturing certainty or utility;
- observation validity/context fidelity is checked before proposition reevaluation;
- candidate refinement, **when naturally exercised**, preserves minimum lineage; the first slice is not required to fabricate a refinement case;
- the implementation reconnects to the existing real public-PR evidence path;
- controlled variations demonstrate non-hardcoded behavior within the admitted responsibility;
- the nearest complete relevant deterministic suite passes;
- one safe integrated public proof is recorded with exact claim limits;
- Ali completes the required ownership/explanation exercise;
- no final D-level maintainer recommendation is implemented implicitly.

## 12. Stop line

Stop this plan when one thin, real, behavior-validated A–C foundation slice has produced enough implementation evidence to evaluate the domain representation and expose the next concrete dependency.

Successful completion means:

```text
real evidence
→ impact candidate
→ candidate propositions/applicability
→ targeted investigation behavior where needed
→ validated feedback / preserved uncertainty
→ explicit pre-D handoff
```

It does **not** mean:

- the dependency update is safe;
- universal Python dependency impact is supported;
- candidate discovery is complete across the ecosystem;
- all exposure paths are modeled;
- all investigations are executable;
- the five final maintainer actions have accepted sufficiency semantics;
- B2 as a whole is automatically complete.

After the stop line, use observed implementation evidence to select either:

1. a narrowly required Conversation-D sufficiency/output question; or
2. a bounded correction to A/B/C if implementation exposed a real contradiction.

## 13. Explicit deferrals

Defer until evidence activates them:

- universal candidate-discovery mechanism;
- arbitrary graph/path traversal;
- general exposure taxonomy;
- universal semantic proposition evaluator;
- generic adaptive planner;
- numeric information-value optimization;
- general dynamic/differential executor;
- historical-environment reconstruction framework;
- repository-policy schema;
- final overall sufficiency formula;
- final maintainer action semantics;
- persistence/replay platform expansion;
- B3/B4/B5/X1 breadth not required by this slice.

## 14. Promotion and relationship to the older plan

This file is intentionally created as a **candidate** so it can be audited against the older [`B2_TRANSPARENT_DECISION_METHOD_PLAN.md`](B2_TRANSPARENT_DECISION_METHOD_PLAN.md) before authority changes.

Before promotion:

1. compare every durable old-plan responsibility/guard with this plan;
2. confirm nothing still valid was accidentally dropped;
3. identify old-plan material that belongs later to Conversation D rather than this pre-D foundation;
4. check for conflict with Charter, B2 parent plan, route, specifications, security boundaries, and current source behavior;
5. decide whether the old plan should be archived, superseded, or narrowed to a later responsibility;
6. only then update `MEMORY.md` and any navigation/authority references that actually require change.

Do not keep two controlling plans for the same responsibility.

## 15. Maintenance

Once promoted, change this plan only when its bounded responsibility, admitted input/output boundary, implementation sequence, proof obligations, or stop line changes.

Do not record live progress, latest commits, current blockers, or immediate continuation here. Those belong only in `../MEMORY.md`.
