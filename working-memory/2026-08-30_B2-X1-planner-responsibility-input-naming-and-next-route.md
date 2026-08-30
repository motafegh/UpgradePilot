# B2/X1 Planner Responsibility, Input Boundary, Naming, and Next Route

**Date:** 2026-08-30  
**Status:** ACTIVE MAIN-SIDE WORKING MEMORY — post E1–E5 + product-simulation capability research  
**Route:** B2/X1 — Product Agentic Investigation / Orchestration Evaluation  
**Purpose:** retain the latest design/learning conclusions and unresolved decisions before the next X1 plan/disposition is frozen

## 1. Continuity / prior owners

Read this file together with, in order of immediate relevance:

1. `../MEMORY.md` — live project position;
2. `2026-08-28_B2-X1-evidence-first-llm-risk-and-design-exploration.md` — evidence-first exploration parent;
3. `2026-08-28_B2-X1-E1-support-drop-semantic-probes.md` — semantic extraction vs grounding;
4. `2026-08-28_B2-X1-E2-s001-state-origin-and-projection.md` — raw-text vs semantic carryover / projection boundary;
5. `2026-08-28_B2-X1-E3-minimally-constrained-s001-planner.md` — minimally constrained planning behavior;
6. `2026-08-28_B2-X1-E4-incremental-constraint-comparison.md` — closed actions, structured output, deterministic admission, replay;
7. `2026-08-28_B2-X1-evidence-first-strict-design-reconciliation.md` — evidence-refined first-seam design;
8. `2026-08-28_B2-X1-product-simulation-capability-research-response.md` — completed delegated capability/value research;
9. `../plans/B2_X1_PRODUCT_SIMULATION_CAPABILITY_RESEARCH_PLAN.md` — completed research plan/method;
10. `../plans/B2_AGENTIC_INVESTIGATION_ORCHESTRATION_EVALUATION_PLAN.md` — broader historical X1 checkpoint plan.

The product-simulation research is now integrated into `main`. Do not continue product-simulation merely to accumulate more cases; main first owns the next responsibility/disposition decision.

---

## 2. Current combined evidence position

E1–E5 established distinct responsibilities:

```text
typed proposition projection
→ model reasoning context

closed trusted action descriptors
→ capability/action binding

strict JSON Schema
→ machine-readable output shape

deterministic admission
→ execution-time catalog/state/precondition revalidation

stop | defer | unresolved
→ distinct no-tool control-flow semantics
```

The delegated product-simulation research then found:

```text
real missing/incomplete product investigation capabilities
→ YES

second capability already justified for LLM-owned selection
→ NO

general adaptive-planner product value proven
→ NO

fresh claim-specific v3 holdout reserved
→ NO
```

The strongest additional capability candidate was exact-head resolver/currentness/satisfiability evidence. It appears independently useful, but current evidence still supports a compact deterministic selection policy rather than LLM-owned selection.

Important interpretation:

```text
FIRST-SEAM CONTROL CONTRACT
!=
FINAL LLM CAPABILITY CEILING
```

Do not minimize UpgradePilot for minimalism. Grow complexity/capability when real product responsibility, reasoning value, failure handling, observability, or learning value earns it. Avoid redundant/speculative complexity and also avoid under-engineering.

---

## 3. Planner responsibility and naming concern

### 3.1 `Planner` and `InvestigationPlanner` are probably too broad as durable names

UpgradePilot as a whole is already an investigation system. Therefore a product component called only `Planner` or even `InvestigationPlanner` does not communicate enough about the bounded responsibility.

Current first-seam responsibility is more specific:

```text
bounded planning question
+ typed evidence/proposition state
+ admitted capability catalog/history/budget
→ identify the material unresolved evidence gap / next useful evidence-acquisition step
→ select one admitted capability OR no-tool disposition
```

It does not plan the entire UpgradePilot process, compatibility decision, maintainer action, remediation, verification, or project execution.

### 3.2 Naming candidates to evaluate before product integration

Do not freeze a name yet. Candidate responsibility-oriented names include:

- `EvidenceGapPlanner`
- `EvidenceResolutionPlanner`
- `EvidenceGapRouter`
- `NextEvidencePlanner`
- `InvestigationStepPlanner`
- `EvidenceAcquisitionPlanner`

Current preference to examine further: **`EvidenceGapPlanner`** or **`EvidenceResolutionPlanner`** because the input is typed evidence/proposition state and the output is the next evidence-resolution action/no-tool disposition.

Trade-off:

- `EvidenceAcquisitionPlanner` may become too narrow if future actions include behavioral reproduction or resolver checks rather than simple acquisition;
- `Router` may understate non-trivial reasoning/prioritization;
- `InvestigationPlanner` is clearer than `Planner` but still broad inside a product whose overall purpose is investigation.

Future UpgradePilot may legitimately contain other distinct planner-like roles if real responsibilities emerge, e.g. bounded remediation or verification planning. Do not create those components pre-emptively.

---

## 4. Exact current planner-input boundary: decided vs not yet frozen

This must remain explicit. “Planner-relevant evidence” is not sufficient documentation.

### 4.1 Historical v2 experiment request

The existing v2 experiment/harness constructed a model request from:

```text
task / generic planner instruction
planning_question
InvestigationSnapshot
output_schema
```

The snapshot historically owns:

```text
repository
pull_number
revision
ordered propositions
attempted_actions
allowed_actions
remaining_steps
hard_constraints
untrusted_evidence_notes
```

Evaluator-only case keys, oracle expected answers, baseline relationship, evidence-source paths, and grading metadata are intentionally excluded from the model request.

This historical request is evidence/prototype material, not automatically the final product contract.

### 4.2 Evidence-refined first-seam fields that are currently justified

The current E1–E5 reconciliation supports passing these categories to the model:

1. **Bounded planning question**
   - tells the model exactly which uncertainty/responsibility it is advancing;
   - prevents adjacent unresolved facts from automatically becoming work.

2. **Exact case identity needed for trace/context**
   - repository;
   - pull request number where applicable;
   - immutable target revision;
   - these are trusted context, not model-generated authority.

3. **Ordered typed proposition/evidence-state projection**
   - proposition key/meaning;
   - state such as established/refuted/unresolved/conflicted;
   - evidence coverage such as sufficient/insufficient;
   - bounded project-authored detail when useful;
   - evidence owner may be useful for context/trace;
   - the projection represents the *result of evidence processing*, not every raw evidence object.

4. **Attempt/action history**
   - which admitted investigation actions have already been attempted;
   - outcome category when relevant to planning/retry semantics;
   - required to avoid blind repetition and enable later failure-aware replanning.

5. **Remaining investigation budget / step allowance**
   - allows bounded stopping/prioritization behavior;
   - trusted state, not model authority.

6. **Closed trusted action descriptors**
   - action ID;
   - purpose / evidence question resolved;
   - target proposition/preconditions as useful planner context;
   - cost/read-only/result-family/locator metadata may be exposed selectively;
   - exact repository/revision/path/capability meaning remain deterministically owned even if model-visible.

7. **Output contract / schema**
   - current evidence supports a small structured decision such as decision state/disposition + action ID when applicable + explanation.

### 4.3 What is intentionally NOT passed in the current first seam

Do not pass these merely because UpgradePilot stores them:

- whole `PythonSupportDropImpactAssessment` or arbitrary nested product objects;
- raw tagged changelog prose/source quotes when typed propositions already represent the required fact;
- full CI logs or complete GitHub Actions payloads;
- complete changed-file contents/diffs;
- complete dependency graphs/lockfiles;
- arbitrary source files;
- evaluator/oracle labels and expected answers;
- protected/development case identity labels;
- grading metadata;
- synthetic `untrusted_evidence_notes` channel created only for prompt-injection pressure;
- verbose hard-constraint tuples whose invariants are already enforced structurally.

### 4.4 Direct answer for common evidence categories

Current first-seam intent:

```text
CI result objects/logs
→ NO direct wholesale planner input
→ their established/refuted/unresolved conclusions may become typed propositions

changed files / full diff
→ NO direct wholesale planner input by default
→ exact identity or a typed proposition derived from them may be passed if the planning question needs it

dependency old/new versions
→ not a mandatory standalone planner field today
→ may appear inside trusted proposition detail/planning question or future structured context when materially needed

raw release notes/changelog
→ NO for current first seam
→ earlier semantic owner converts relevant meaning into typed state

target declaration / resolver / CI / artifact evidence
→ underlying raw evidence remains with deterministic/domain owners
→ planner receives typed proposition/evidence state describing what is established/refuted/unresolved and why, unless a future responsibility proves raw/near-raw context necessary
```

### 4.5 What remains intentionally unfrozen

We have **not** finalized the production request schema. In particular these field-level questions remain design decisions:

- exact name/type of the planner component;
- exact decision/disposition enum names;
- whether `evidence_owner` is always model-visible;
- whether proposition `origin` metadata is model-visible;
- whether `raw_external_text` flags remain useful once raw text is excluded;
- how much action metadata should be model-visible versus retained only for deterministic admission;
- whether dependency transition identity deserves a first-class structured field in a richer future planner state;
- whether future richer planners need selected bounded raw/near-raw evidence for semantic comparison.

Therefore the **category-level boundary is evidence-backed; the final product schema is not yet frozen**.

---

## 5. Existing upstream LLM responsibility and possible expansion

Current accepted upstream AI is deliberately narrow:

```text
bounded authoritative crossed-release text
→ identify explicit CURRENT Python X.Y support-drop candidate(s)
→ source-line IDs / structured candidate
→ deterministic exact-source reconstruction and grounding
```

It is not a general upstream-release intelligence component.

It currently does not own:

- arbitrary upstream mechanism discovery;
- API/behavior/binary/toolchain change extraction broadly;
- general release-note summarization;
- target applicability;
- compatibility/safety decisions;
- action planning.

Product-simulation research identified **upstream multi-mechanism discovery** as a plausible separate semantic/LLM responsibility because one version transition may contain several materially different mechanisms. This is a real future direction, but it is not yet adopted.

### Route principle

Do **not** make broader upstream semantic discovery a prerequisite merely so X1 can continue. The two responsibilities are separable:

```text
upstream semantic discovery
→ discovers/grounds what mechanisms changed

next-evidence planning
→ reasons over trusted typed investigation state and admitted capabilities
```

Broader upstream discovery may later enrich planner state and create more meaningful investigation paths, but it should receive its own evidence-backed design/evaluation responsibility. Do not collapse extraction/discovery and planning into one LLM because both use AI.

---

## 6. Learning topics still ahead and when they become active

E1–E5 did not prove or practice everything. Retain this learning ladder:

### L1 — reliability / repeated observations

If main retains the first seam as a real pilot, a fresh claim-specific v3 should teach:

- repeated runs;
- holdout discipline;
- consistency/failure rates;
- semantic grading;
- model/configuration freeze and reproducibility.

### L2 — multiple real actions / prioritization

Activate only when at least two independently justified capabilities naturally coexist and real states make more than one plausible.

Learn/practice:

- action-space reasoning;
- prerequisite/dependency planning;
- information-value prioritization;
- cost/budget trade-offs;
- irrelevant unresolved facts;
- deterministic-baseline comparison.

### L3 — real multi-turn loop

When an admitted action can execute safely:

```text
plan
→ execute
→ classify result/failure
→ update trusted state
→ re-plan
```

Learn:

- state machines/agent loops;
- checkpoints/replay;
- stale-plan revalidation;
- action history;
- failure-aware replanning;
- stopping.

### L4 — retry/failure ownership

Use the product-simulation transfer finding:

```text
typed domain/evidence problem
!= transient provider/transport failure
```

Learn when retry belongs to deterministic executor/provider policy versus when the planner should see a completed/problem/rejected attempt and choose/defer/stop.

### L5 — richer semantic discovery/context

If product work selects broader upstream mechanism discovery or repository-purpose interpretation, learn those as separate LLM responsibilities and evaluate how their typed results enter later planning.

---

## 7. Plan status after product-simulation research

### Existing plans

`B2_AGENTIC_INVESTIGATION_ORCHESTRATION_EVALUATION_PLAN.md` remains the broad historical X1 checkpoint owner and still requires an explicit X1 disposition.

`B2_X1_PRODUCT_SIMULATION_CAPABILITY_RESEARCH_PLAN.md` has completed its delegated responsibility. Do not use it as the next main execution plan.

`B2_X1_PHASE3_EVALUATION_PROTOCOL.md` v2 is historical/consumed for final scoring of the reconciled candidate and must not be reused as an uncontaminated scorecard.

### Fresh plan need

A **new compact main-side post-research X1 plan is warranted**, because the live decision has changed materially.

Proposed responsibility:

> Decide and, if selected, prepare the honest next-evidence-planning responsibility after E1–E5 and capability research, including final naming/input/disposition choices, without fabricating multi-action value or prematurely integrating product runtime.

Possible plan title:

`B2_X1_POST_RESEARCH_PLANNER_RESPONSIBILITY_AND_DISPOSITION_PLAN.md`

It should be small and should cover roughly:

1. settle precise responsibility/name vocabulary;
2. freeze the candidate input/output ownership boundary at the right level—not necessarily code schema yet;
3. decide X1 disposition:
   - retain first seam as limited pilot/control, or
   - defer richer planner until real multi-capability trigger;
4. decide whether broader upstream semantic mechanism discovery is a separate near-term B2 responsibility or remains deferred;
5. if retaining a pilot, decide exact narrow claim and then search/reserve fresh holdout material before v3;
6. if deferring richer X1, preserve reusable agentic machinery/learning and return to independently justified product capability work;
7. define explicit triggers for reopening richer multi-action/multi-turn planning.

Do not build another long protocol before this responsibility decision.

---

## 8. Product-simulation next-use decision

The delegated capability research is complete and current `MEMORY.md` says not to continue simulation merely for more cases.

Therefore **do not give product simulation another broad research job yet**.

First main should decide:

- precise next-evidence-planner responsibility/name;
- first-seam input/output ownership boundary;
- retain-limited-pilot vs defer-richer-X1 disposition;
- whether broader upstream semantic mechanism discovery is selected as a separate responsibility.

After that, product simulation can be reused for a precise new job, for example:

### If first-seam pilot proceeds

- perform claim-specific fresh-case screening;
- preserve exposure from first screening;
- reserve untouched holdout candidates for v3 before deep analysis.

### If upstream semantic discovery proceeds

- research a bounded multi-mechanism upstream corpus;
- identify recurring mechanism families and semantic ambiguities;
- compare LLM semantic discovery against strongest deterministic baselines;
- preserve planner/action questions as separate.

### If richer planner trigger later appears

- find real cases where multiple admitted capabilities are simultaneously plausible;
- pressure state/history/budget-dependent ordering;
- test whether a small deterministic policy remains sufficient.

No new product-simulation work is justified now simply to create volume.

---

## 9. Naming of no-tool states remains open for product contract

E5 established the **semantics**, not necessarily final durable identifiers.

Current experimental terms:

```text
stop
→ bounded planning question sufficiently settled / no additional justified investigation

defer
→ useful next investigation is known but outside current admitted capability/support boundary

unresolved
→ evidence remains insufficient/conflicted and no justified supported or known outside resolving capability is identified
```

Concern: these short words also appear in other project domains and may be ambiguous when detached from their type/context.

Before product integration, evaluate expressive domain-qualified naming such as:

```text
EvidencePlanningDisposition.STOP
EvidencePlanningDisposition.DEFER
EvidencePlanningDisposition.UNRESOLVED
```

or more explicit values such as:

```text
QUESTION_SETTLED
KNOWN_INVESTIGATION_UNAVAILABLE
NO_RESOLUTION_PATH_IDENTIFIED
```

Do not choose longer names merely for verbosity. Prefer an expressive type/component name plus values that remain readable in code/logs. Existing experimental names are not naming authority.

---

## 10. Immediate main-side route

Current preferred order:

```text
1. continue E1–E5 technical/conceptual mastery while decisions are fresh

2. settle terminology/responsibility:
   what exactly is the model component planning/routing?

3. write the compact post-research X1 responsibility/disposition plan

4. make explicit X1 decision:
   RETAIN AS LIMITED PILOT / CONTROL SEAM
   or
   DEFER RICHER X1 until multi-capability trigger

5. separately decide whether a broader upstream semantic-discovery slice should be a near-term product/learning route

6. only after an exact claim is selected:
   use product simulation for targeted fresh holdout/corpus work
   and freeze v3 if a planner-quality evaluation is actually warranted
```

Do not start product `src/upgradepilot` planner integration before steps 2–4 are resolved.

---

## 11. Retained engineering principles from current discussion

- Product/system power is not measured by mechanism count or LLM autonomy.
- Do not simplify useful capability merely to reduce complexity.
- Do not give the LLM redundant ownership of facts/locators/authority deterministic code already owns.
- Do not keep the LLM responsibility permanently trivial merely because the first control seam is small.
- A real missing capability is not automatically a planner-visible capability.
- A useful LLM semantic responsibility is not automatically a planning responsibility.
- Raw evidence retained by UpgradePilot is not automatically planner input.
- Context projection is an architectural boundary, not merely prompt shortening.
- Future planner expansion should be triggered by real multi-capability composition and non-trivial state/history/budget-dependent policy pressure.
- Naming should communicate bounded responsibility and state semantics; existing prototype terminology can be changed before product adoption.
