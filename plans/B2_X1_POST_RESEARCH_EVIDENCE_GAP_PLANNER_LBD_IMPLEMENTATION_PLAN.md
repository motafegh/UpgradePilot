# B2/X1 Post-Research EvidenceGapPlanner Learning-by-Doing Implementation Plan

**Status:** AUTHORIZED PLAN ARTIFACT — position-neutral; `MEMORY.md` alone selects live activation  
**Date:** 2026-08-30  
**Responsibility:** finish the post-E1–E5 B2/X1 planner decision by defining, building, and evaluating the smallest honest `EvidenceGapPlanner` experimental seam, then make an explicit X1 disposition without manufacturing multi-action value or prematurely integrating product runtime  
**Primary method:** Learning-by-Doing / Building  
**Product runtime integration:** NOT authorized by this plan itself

---

## 1. Why this plan exists

UpgradePilot has completed two substantial evidence blocks:

1. the main-side E1–E5 evidence-first exploration; and
2. the delegated product-simulation capability/value research.

Together they established useful AI/LLM engineering mechanisms while also exposing an important product-value limit:

```text
E1–E5
→ bounded typed-state reasoning works
→ closed action binding works
→ structured output has a distinct role
→ deterministic admission has a distinct role
→ stop / defer / unresolved remain meaningful

product-simulation capability research
→ real additional product capabilities exist
→ but no second capability is yet justified for LLM-owned selection
→ current one-action planner does not prove general adaptive-planner value
```

The project therefore needs one bounded plan that does **not** jump to either extreme:

```text
UNDER-ENGINEERING
→ discard the LLM/planner work because S001 is simple

OVER-ENGINEERING
→ build a generic agent platform or fabricate a second action to make the planner look agentic
```

This plan instead finishes the current `EvidenceGapPlanner` responsibility honestly, preserves the valuable engineering/learning work, and defines exactly when richer planning should reopen.

---

## 2. Applicable owners and evidence

Use the smallest relevant chain for each execution slice.

### Controlling/procedural owners

- `../AGENTS.md` — authorization, artifact/operation routing, default Learning-by-Doing loop;
- `../OPERATING_GUIDE.md` — Learning-by-Doing, proportionality, context discipline, evidence interpretation, assistance fading;
- `.agents/skills/upgradepilot-planning-design/SKILL.md` — planning/design procedure while this plan is being designed/reconciled;
- `.agents/skills/upgradepilot-build-implement/SKILL.md` — use when a later authorized substantive implementation slice begins;
- `.agents/skills/upgradepilot-learning-by-doing/SKILL.md` — full LbD composition when materially useful;
- `README.md` — plan responsibility / position neutrality.

### Stable technical owners

- `../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md` — accepted proposition/applicability/discriminating-investigation/stopping semantics;
- `../docs/specifications/UPGRADEPILOT_NAMING_CLARITY_SPECIFICATION.md` — durable naming clarity standard;
- `../docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md` — variable-input / anti-fixture behavior;
- `../docs/architecture/ADR-0006-bounded-local-support-drop-semantic-extractor.md` — accepted bounded upstream semantic-model method.

### Immediate evidence / continuity

- `../working-memory/2026-08-30_B2-X1-planner-responsibility-input-naming-and-next-route.md` — current detailed post-research reasoning owner;
- `../working-memory/2026-08-30_B2-X1-EvidenceGapPlanner-R2-model-visible-context.md` — active R2 field/context decisions;
- `../working-memory/2026-08-28_B2-X1-E1-support-drop-semantic-probes.md`;
- `../working-memory/2026-08-28_B2-X1-E2-s001-state-origin-and-projection.md`;
- `../working-memory/2026-08-28_B2-X1-E3-minimally-constrained-s001-planner.md`;
- `../working-memory/2026-08-28_B2-X1-E4-incremental-constraint-comparison.md`;
- `../working-memory/2026-08-28_B2-X1-evidence-first-strict-design-reconciliation.md`;
- `../working-memory/2026-08-28_B2-X1-product-simulation-capability-research-response.md`;
- `B2_AGENTIC_INVESTIGATION_ORCHESTRATION_EVALUATION_PLAN.md` — broader historical X1 checkpoint;
- `B2_X1_PHASE3_EVALUATION_PROTOCOL.md` — historical/consumed v2 protocol; evidence, not reusable final scorecard;
- `B2_X1_PRODUCT_SIMULATION_CAPABILITY_RESEARCH_PLAN.md` — completed delegated research plan.

Do not re-read all historical material for every slice. Use exact evidence only when a current decision depends on it.

---

## 3. Bounded outcome

This plan is complete when UpgradePilot has all of the following:

1. a precise, responsibility-oriented candidate name and definition for `EvidenceGapPlanner`;
2. a candidate `EvidenceGapDecision` vocabulary whose semantics are clear and do not collide ambiguously with unrelated project states;
3. an explicit model-visible input contract at the category/field level, including structured dependency-transition context and the role of selected structured planning evidence;
4. a coherent experiment-owned implementation of the evidence-refined seam under `experiments/`, with focused tests and no product-runtime import dependency;
5. one bounded development/replay proof that the integrated seam behaves as designed;
6. an explicit evidence-backed X1 disposition for the current responsibility;
7. a clear decision on whether a fresh v3 evaluation is justified for the narrow pilot claim;
8. a selected next independent product/AI capability direction or an explicit defer;
9. an explicit trigger for reopening richer multi-action/multi-turn planner work;
10. material learning closure for the AI/LLM/agent-engineering concepts encountered through the real work.

This plan does **not** require general adaptive-planner adoption.

---

## 4. Responsibility being evaluated

Use `EvidenceGapPlanner` as the plan-level working name.

The candidate responsibility is:

> Given one bounded UpgradePilot planning question, trusted typed proposition state, selected bounded structured planning evidence, trusted attempt history/budget, and a closed set of admitted bounded investigation capabilities, identify the material evidence gap that should be addressed next and select one useful admitted capability, or return an explicit no-tool disposition when no such action should execute.

The model does **not** own:

- source or repository authority;
- dependency identity/version truth;
- exact file/URL/command locator invention;
- action-catalog creation;
- execution authorization;
- evidence parsing/promotion;
- proposition truth or proof-strength composition;
- compatibility/safety/merge truth;
- maintainer action;
- target mutation;
- final trusted investigation state.

The accepted Product Decision Model already owns the framework-independent responsibility to identify uncertainty/conflict, select a justified discriminating investigation/small conditional sequence or preserve alternatives, and stop when no justified investigation remains. `EvidenceGapPlanner` is only a candidate implementation method for part of that accepted reasoning responsibility.

---

## 5. Current entry evidence: do not re-prove without contradiction

### E1 — semantic correctness and grounding are different

```text
model-derived English meaning
!=
deterministic exact-source/provenance grounding
```

The existing support-drop path can be perfectly grounded while semantic direction would still be wrong if the earlier model misclassifies the sentence.

### E2 — raw-text and semantic carryover are different

```text
small typed planner projection
→ raw changelog prose absent
→ model-influenced semantic state can still remain
```

Raw external evidence need not be injected into the current planner request merely because it exists inside nested product state.

### E3 — typed state can support the S001 reasoning

The model identified the missing exact target Python declaration without the closed action catalog, schema, admission, or raw release prose.

### E4 — separate responsibilities earned by controlled comparison

```text
typed state
→ reasoning context

closed action descriptor
→ exact capability binding

JSON Schema
→ machine-readable output shape

deterministic admission
→ fresh state/catalog/precondition revalidation
```

The model does not need to echo trusted action-owned repository/revision/path/target/result-family metadata.

### E5 — no-tool semantics are distinct

```text
stop
!= defer
!= unresolved
```

The meanings survived a small structured model output.

### Product-simulation research — current product-value gate

```text
real additional capabilities found
→ YES

second capability justified for LLM-owned selection
→ NO

strong evidence of adaptive planner advantage over small deterministic policy
→ NO
```

Do not manufacture a second action merely to advance the experiment.

---

## 6. Learning-by-Doing execution rule for every stage

Each substantive stage below follows this loop proportionately:

```text
A. PRE-ACTION ORIENTATION
   establish only the concepts/dataflow/owner needed for the coming work

B. OWNERSHIP / REASONING POINT
   Ali predicts, challenges, selects, or explains one material design/evidence point when useful

C. REAL BOUNDED WORK
   perform one design / implementation / evaluation slice

D. ACTUAL EVIDENCE
   inspect source/tests/model output/replay/result rather than assuming success

E. MODEL CORRECTION
   separate observation, interpretation, remaining uncertainty, and supported conclusion

F. PRESERVE MATERIAL STATE
   update working memory / MEMORY / plan only when the responsibility or continuation materially changes

G. POST-ACTION LEARNING CLOSURE
   explain what actually changed, why, what concept it demonstrates, and what remains deferred
```

Do not turn every edit or command into a separate ceremony.

---

# Stage R0 — Re-anchor the post-research baseline

## Question

Can the next work start from one coherent current understanding without reopening completed E1–E5 or delegated capability research?

## Work

1. Confirm current `main` and live `MEMORY.md` before an implementation slice.
2. Read this plan plus the 2026-08-30 working memory.
3. Inspect only the active experiment/source files required by the immediate next decision.
4. Treat historical v2 names/contracts as prototype evidence, not retention authority.
5. Confirm no new product-simulation result or product implementation has materially changed the entry assumptions.

## LbD concepts

- live state vs historical evidence;
- plan authority vs implementation truth;
- experiment vs product proof;
- why accepted product semantics can remain stable while implementation method changes.

## Pass condition

The current responsibility, evidence limits, and no-product-integration boundary are unambiguous.

## Stop line

Do not restart broad repo investigation or E1–E5 merely because a new execution session begins.

---

# Stage R1 — Freeze responsibility vocabulary before implementation

## Question

Can a competent maintainer infer the component's responsibility and decision meanings from the names without remembering X1 history?

## Current working vocabulary

```text
component
→ EvidenceGapPlanner

model result
→ EvidenceGapDecision

decision kind
→ EvidenceGapDecisionKind
```

Current preferred semantics from completed R1:

```text
ACTION_SELECTED
QUESTION_SETTLED
KNOWN_INVESTIGATION_NOT_ADMITTED
NO_JUSTIFIED_INVESTIGATION_IDENTIFIED
```

Preserve the E5 semantics even though the historical short identifiers changed.

## Work

1. Apply the Naming Clarity specification to the current generic experiment names:
   - `PlannerPlanState`;
   - `AgentPlanResult`;
   - generic `Planner` language.
2. Confirm `EvidenceGapPlanner` communicates the input/output responsibility better than `Planner` or `InvestigationPlanner`.
3. Define one concise durable responsibility sentence.
4. Decide how decision-state names should read in active code/logs.
5. Preserve the **semantics** proven by E5 even if identifiers change.

## LbD concepts

- responsibility-oriented naming;
- domain type + enum value as a semantic unit;
- naming as an API/maintenance design tool;
- why experiment vocabulary is not automatically product vocabulary.

## Evidence / proof

A small naming/responsibility table explaining each selected term, nearby rejected meaning, and source/consumer boundary.

## Pass condition

The candidate names are clear enough to use in the experiment-owned implementation without implying broader product authority than intended.

## Stop line

Do not launch a repository-wide rename. Historical experiment/evidence files remain historical unless active code must change to support the candidate implementation.

---

# Stage R2 — Freeze the candidate model-visible context contract

## Question

What exact trusted information should the `EvidenceGapPlanner` receive, and why does each field belong at the planner boundary?

## Candidate top-level request

The current candidate to prove is:

```text
planning_question

dependency_transition
    normalized_package
    old_version
    proposed_version

propositions
planning_evidence
attempted_actions
remaining_budget
allowed_actions
output_schema / provider structured-output contract
```

Target repository / PR / revision identity remains trusted system/evaluator/executor state but is not model-visible in the first seam.

This is a candidate contract to validate, not yet a framework-independent product specification.

## R2.1 — planning question

Pass one explicit bounded question.

It tells the model **which uncertainty/responsibility is being advanced**. It prevents every unresolved proposition from becoming automatic work.

The planning question remains deterministically/project-owned input. The model does not invent its own top-level mission.

## R2.2 — target/case identity remains deterministic-only

Do not pass these fields to the current model request:

```text
repository
pull_number
revision
```

They remain essential trusted state for traceability, replay, provider acquisition, exact action binding, stale-state checks, deterministic admission, and exact execution.

Why omit them from the model:

- `pull_number` has essentially no evidence-gap reasoning value;
- an immutable revision is critical authority state but the SHA itself adds negligible planning meaning;
- repository identity can invite pretrained/stale project knowledge that is not admitted evidence;
- E4 already demonstrated that trusted action metadata can remain deterministic and be rebound after action selection.

Omission from model context is not removal from system state.

## R2.3 — dependency transition

Promote the dependency transition into first-class structured context:

```text
normalized_package
old_version
proposed_version
```

Rationale:

- it is central upgrade context;
- already authoritative product state;
- compact and cheap;
- likely important when several mechanisms/capabilities later coexist;
- `normalized_package` is the canonical cross-source package identity already used by product comparison/reasoning, whereas `package` preserves source spelling for presentation;
- avoiding a structured transition in E3 was an experiment-isolation choice, not a proven reason to exclude it from the durable candidate request.

Do not claim the LLM establishes or normalizes these values.

## R2.4 — typed proposition projection

For each planner-relevant proposition, candidate fields are:

```text
key
state
  established | refuted | unresolved | conflicted

evidence_coverage
  sufficient | insufficient | applicable accepted vocabulary

detail
  bounded project-authored explanation
```

Explicitly decide whether these remain model-visible:

```text
evidence_owner
origin
raw_external_text flag
```

Decision rule:

> show metadata only when it can materially improve planning reasoning, traceability, or safe interpretation; do not expose metadata merely because it exists.

Do not pass whole nested domain objects merely to avoid writing a projection.

## R2.5 — selected structured planning evidence (`EvidenceGapPlanningEvidence`)

Propositions are the decision-state spine but are not required to be the entire reasoning input.

Current product evidence already preserves useful distinctions that can be lost by reducing everything to `established/refuted/unresolved`, for example CI separates:

```text
successful runtime CI authority
static changed-dependency consumption
stronger direct package exercise
```

and selected dependency/CI evidence can preserve:

```text
mechanism
reachability_kind
witness_path
conditional_candidate_path
unresolved_conditions
```

Use **`EvidenceGapPlanningEvidence`** as the working name for a bounded structured evidence item exposed specifically because its details can change evidence-gap selection.

It means:

> a project-owned structured projection of already-acquired/interpreted evidence whose mechanism, limitation, witness, reason, or unresolved condition can materially change which evidence gap or admitted capability has the highest discriminating value for the current planning question.

It is not:

- raw evidence storage;
- a second proposition system;
- model-generated truth;
- a generic evidence database;
- permission to copy arbitrary external prose into the prompt.

Relationship:

```text
PropositionAssessment
→ what is known / unknown and whether coverage is sufficient

EvidenceGapPlanningEvidence
→ selected structured evidence shape/details that can change what investigation is useful next
```

Candidate evidence families include, only when question-relevant:

- CI coverage/consumption/direct-exercise state and reason;
- consumption mechanism;
- direct/transitive reachability kind and witness path;
- conditional candidate path / unresolved conditions;
- interpreted target Python declaration/range;
- grounded upstream mechanism details such as dropped Python line / introduced version;
- bounded structured changed-file/change-scope facts;
- structured command semantics derived by deterministic interpretation.

Default three-level model:

```text
LEVEL 1
proposition state

LEVEL 2
selected EvidenceGapPlanningEvidence

LEVEL 3
raw evidence
```

Current first seam normally passes Level 1 + selected Level 2. Level 3 stays outside model context by default.

An evidence item earns model visibility only when:

1. it is already admitted/interpreted by a deterministic or separately authorized semantic owner;
2. it is relevant to the bounded planning question;
3. its structured details add discriminating information beyond proposition state alone;
4. exact provider/source identity is not needed for the model's reasoning;
5. exposing it does not transfer truth, execution authority, or final decision authority to the model.

When a bounded project-authored `reason` or `detail` is exposed, it must represent already interpreted evidence rather than arbitrarily copying external source prose.

## R2.6 — action/attempt history

Clarify the ownership model:

```text
planner selects an action
→ deterministic admission decides whether it may execute
→ executor/domain owner produces a result/problem
→ trusted state is updated
→ system records the action attempt/outcome
→ next planner turn receives trusted attempt history
```

This is **system-owned action history**, not free-form LLM memory.

Candidate attempt fields:

```text
action_id
outcome
  completed | problem | rejected
```

If a finding matters to future reasoning, represent it in updated trusted propositions/evidence state rather than depending on prose stored only in action history.

Later richer failure classification may add bounded typed outcome detail only when it changes replanning/retry semantics.

## R2.7 — remaining budget

Candidate:

```text
remaining_steps
```

Keep as trusted bounded state.

It becomes more valuable when multiple actions/costs exist, but it already protects bounded-loop semantics and future extensibility.

## R2.8 — closed allowed actions

Planner-visible action information should be enough to understand **what useful evidence the capability can obtain** without transferring capability definition to the model.

Candidate visible fields:

```text
action_id
purpose
target proposition / evidence gap addressed
required proposition/evidence precondition
cost_class
mutation_class
result-family summary
```

Exact locator/authority metadata remains deterministic-only by default:

```text
repository
revision
path / URL / command / source locator
```

The planner must not be required to echo or redefine those facts.

## R2.9 — explicitly excluded by default

Do not pass wholesale:

- raw release notes/changelog text;
- full GitHub Actions logs/payloads;
- full workflow YAML;
- complete changed-file diffs;
- arbitrary source files;
- complete lockfiles/dependency graphs;
- whole impact-assessment/domain object graphs;
- raw command text by default;
- evaluator case labels/oracles/expected answers;
- grading/protected-set metadata;
- synthetic untrusted-note channels created only for pressure testing;
- verbose policy strings whose behavior is already structurally enforced.

This exclusion does **not** prohibit bounded structured `EvidenceGapPlanningEvidence` derived from those product evidence families.

If later evidence shows one excluded raw/near-raw form is necessary for a richer responsibility, reconsider it at that time.

## R2 proof method

Construct a field/owner/why-visible/why-not-raw table and render at least:

- one S001 action state;
- one no-tool state;
- one state where selected Level-2 planning evidence is materially richer than proposition labels alone;
- one attempt-history or stale-action state if available from replay.

Inspect the rendered request directly.

## LbD concepts

- context engineering / request projection;
- state representation;
- full system state vs model observation;
- proposition state vs selected supporting evidence;
- provenance vs authority;
- semantic carryover vs raw-text carryover;
- agent memory vs trusted system state/history;
- information compression vs information loss;
- information sufficiency vs context dumping.

## Pass condition

Every model-visible field/evidence item has an explicit planning role and an authoritative non-model owner where appropriate; the request is rich enough for the bounded planning responsibility without depending on serializing entire product objects or arbitrary raw evidence.

---

# Stage R3 — Freeze the candidate output and admission contract

## Question

What is the smallest output that preserves useful reasoning/control semantics while leaving trusted metadata with deterministic owners?

## Candidate decision shape

Conceptually:

```text
decision_kind
  action_selected | question_settled | known_investigation_not_admitted | no_justified_investigation_identified

action_id
  trusted action ID | null

explanation
  non-empty text
```

A different equivalent JSON shape may be selected if it is clearer, but do not restore redundant model echoes solely because v2 contained them.

## Model may own

- evidence-gap reasoning;
- action choice from the closed catalog;
- no-tool semantic disposition;
- concise explanation/reasoning statement.

## Trusted code must own/rebind

- repository;
- revision;
- path/command/source locator;
- target proposition / evidence gap binding;
- required preconditions;
- mutation class;
- result/problem families;
- execution authorization;
- trusted state changes.

## Deterministic admission must re-check

At minimum when applicable:

```text
action ID exists in current catalog
action remains inside allowed mutation boundary
action was not blindly repeated when history forbids it
budget remains
current trusted proposition still satisfies action precondition
```

Do not confuse JSON Schema validity with semantic correctness or execution authorization.

## LbD concepts

- structured outputs / JSON Schema;
- tool/action allowlisting;
- capability-based authority;
- TOCTOU / stale-plan revalidation;
- model proposal vs execution authorization.

## Pass condition

One candidate decision can be parsed deterministically, rebound to trusted action metadata, and admitted/rejected without relying on model-echoed authority fields.

---

# Stage R4 — Build the coherent experiment-owned EvidenceGapPlanner seam

## Question

Can the evidence-refined design exist as one understandable executable experiment rather than only as separate E3/E4/E5 probes?

## Allowed implementation boundary

For this stage, implementation belongs under:

```text
experiments/
experiments/tests/
```

with imports from `src/upgradepilot/` only where existing product evidence/state types are genuinely required.

Product runtime under `src/upgradepilot/` must not import experiment code and should not gain a planner implementation in this stage.

## Expected implementation responsibilities

Use active source layout as a hint, not a fixed architecture requirement. The experiment should provide the smallest cohesive owners for:

1. `EvidenceGapPlanner` request/state types;
2. dependency-transition / proposition / `EvidenceGapPlanningEvidence` projection;
3. request rendering;
4. provider/local-model call boundary;
5. structured decision parser;
6. trusted action lookup/rebinding;
7. deterministic admission reuse or evidence-backed refinement;
8. deterministic trace/result preservation for replay/evaluation.

Prefer ordinary Python and direct local LM Studio HTTP unless a demonstrated blocker requires another mechanism.

Do not introduce LangChain, LangGraph, an agent framework, generic middleware, vector memory, or orchestration infrastructure merely because the concepts are relevant to learning.

## LangGraph/LangChain learning exposure

During this stage, explicitly teach the relationship:

```text
our ordinary-Python state
→ trusted full system state + bounded model observation

our action/admission/execution/update steps
→ state transitions / nodes conceptually

replanning loop
→ graph/agent-loop concept
```

Then compare at a high level with what LangGraph/LangChain could provide, but adopt neither unless ordinary Python creates a real current limitation that the framework solves materially better.

## Tests

Focused tests should prove only the candidate contract and boundaries needed now, such as:

- request projection includes intended fields and excludes evaluator/oracle/raw-object leakage;
- target repository/PR/revision remain outside model context while remaining available to trusted action/admission code;
- structured dependency transition carries normalized package identity and exact versions;
- selected `EvidenceGapPlanningEvidence` preserves planning-relevant distinctions without serializing wholesale raw evidence;
- action history remains trusted typed state;
- no-tool semantics remain representable;
- model output cannot redefine action-owned metadata;
- unknown/stale action remains rejected;
- experiment/product import direction is preserved.

Do not create a generalized test framework before repetition demonstrates the need.

## LbD concepts

- agent state;
- model observation;
- state transition;
- action space;
- nodes/edges as conceptual orchestration vocabulary;
- framework vs concept;
- separation of model plane and deterministic control plane.

## Pass condition

The experiment implements the candidate seam coherently with focused tests and no product-runtime planner dependency.

---

# Stage R5 — Bounded development/replay proof of the integrated seam

## Question

Does the integrated `EvidenceGapPlanner` experiment behave consistently with the responsibilities already isolated by E3–E5?

## Evidence use

Use already-consumed/development material freely for **development proof**, clearly labelled as such. Do not present it as fresh protected evidence.

Minimum useful proof should include:

1. one action case demonstrating evidence-gap reasoning + exact action selection;
2. at least one no-tool case demonstrating the selected disposition vocabulary;
3. one request where structured planning evidence adds meaningful context beyond proposition labels;
4. one deterministic admission rejection such as unknown or stale action;
5. exact request/output preservation for replay.

A small number of model calls is enough unless a concrete failure creates a decision-changing reason for more.

## Failure classification

Keep separate:

```text
model reasoning failure
structured-output/provider failure
request projection bug
deterministic admission rejection
transport/LM Studio failure
GitHub/acquisition failure
experiment/replay failure
```

Do not restart live GitHub/upstream acquisition when frozen replay is sufficient for the question being tested.

## LbD concepts

- smoke evaluation / capability probing;
- replay and reproducibility;
- controlled comparison / ablation;
- confounders;
- failure taxonomy / observability.

## Pass condition

The integrated seam reproduces the already-earned responsibility split without introducing unexplained behavior or hidden authority expansion.

## Stop line

Do not turn development proof into claims of reliability, generalization, or product advantage.

---

# Stage R6 — Make the explicit current X1 disposition

## Question

What honest claim does the current evidence support after the integrated seam exists?

Compare against the strongest real deterministic baseline, not a weak demo baseline.

## Serious dispositions

### `RETAIN AS LIMITED PILOT / CONTROL SEAM`

Use when:

- the seam remains useful for learning/evaluation/reusable architecture;
- bounded reasoning and control behavior are technically sound enough to retain;
- product advantage over deterministic one-action sequencing remains unproven;
- no product-runtime general adaptive-planner claim is made.

### `DEFER RICHER X1`

Use when:

- richer multi-action/multi-turn planning is not yet justified;
- work should resume only when independently admitted capabilities create a real non-trivial planning policy problem.

These dispositions can coexist conceptually:

```text
retain current bounded pilot/control artifact
+
defer richer product planner expansion
```

### `REJECT`

Use only if the integrated seam itself proves not worth retaining even as a bounded pilot/control mechanism.

### General adaptive-planner `ADOPT`

Not available from current evidence unless a later responsibility/evaluation materially expands the claim.

## Decision record requirements

Preserve:

- strongest supported claim;
- strongest unsupported claim;
- deterministic-baseline comparison;
- why current LLM use is or is not more than a trivial selector;
- exact trigger for richer planner reopening.

Update `MEMORY.md` only when the disposition becomes the live continuation decision.

## LbD concepts

- evaluation claim scope;
- strongest-baseline discipline;
- product value vs technical possibility;
- under-engineering vs justified defer;
- evidence-backed stopping.

## Pass condition

One explicit X1 disposition exists and no stronger claim is implied elsewhere.

---

# Stage R7 — Conditional fresh v3 evaluation for the narrow pilot claim

## Activation condition

Run this stage **only if** R6 decides that the current bounded pilot needs a fresh planner-quality evaluation before its final retain/reject/defer conclusion.

Do not run merely because v2 once existed.

## Sequence

```text
freeze exact candidate responsibility + input/output contract
→ define exact narrow claim
→ delegate fresh-case screening with exposure ledger
→ reserve untouched claim-specific holdouts before deep analysis
→ freeze v3 protocol
→ freeze model/config/prompt/schema
→ execute repeated protected evaluation
→ score deterministic + human semantic criteria
→ final narrow disposition
```

## Product-simulation use

Only after the claim is frozen, give product simulation a targeted handoff to:

- find fresh claim-specific candidates;
- record exposure from first screening;
- reserve plausible holdouts before deep inspection;
- avoid using historical S001–S012 as untouched final evidence.

## Required learning

- development/calibration vs protected evaluation;
- holdout contamination;
- repeated runs and reliability claims;
- model/configuration freeze;
- deterministic grading vs human semantic review;
- evaluation harness design.

## Stop line

Do not use protected outcomes to tune and then rescore the same cases as final evidence.

---

# Stage R8 — Select the next independently justified AI/product capability direction

## Question

After the current X1 disposition, what product responsibility should create the next real capability/learning value?

Do not select a capability merely because it would make the planner more agentic.

## Candidate directions from completed research

### A. Broader upstream semantic mechanism discovery

Potential AI-oriented responsibility:

```text
bounded authoritative upstream release evidence
→ discover several materially distinct change mechanisms
→ grounded typed mechanism candidates
→ deterministic authority / provenance / downstream applicability remain outside the model
```

Why promising:

- current upstream model is Python-support-drop specific;
- natural-language semantic variation is intrinsic;
- S010/research shows multi-mechanism transitions can exist;
- may materially enrich future typed investigation state and `EvidenceGapPlanningEvidence`.

Do not merge semantic discovery and planning merely because both use an LLM.

### B. Exact-head resolver/currentness/satisfiability evidence

Potential primarily deterministic responsibility:

```text
pre-bound exact target/resolver context
→ bounded resolver/currentness evidence
→ typed established/refuted/unresolved result/problem
```

Why promising:

- independently useful product evidence capability;
- proof boundary already has research support;
- current selection policy still appears simple enough for deterministic ownership.

### C. Other researched responsibilities

- mediated CI/environment-consumption interpretation;
- richer target artifact/environment evidence;
- targeted behavioral differential reproduction;
- persisted-artifact provenance/history;
- repository-purpose/reproduction-context semantics.

Each must earn its own owner/method based on recurrence, proof need, safe boundary, and strongest baseline.

## Selection test

For each serious candidate ask:

```text
real recurring responsibility?
variable semantic/reasoning input?
strongest deterministic baseline?
exact evidence output/proof boundary?
safe bounded execution/acquisition?
product value independent of planner?
AI/LLM value beyond a few stable rules?
learning value?
```

Learning value strengthens an already-real product responsibility; it does not create product necessity by itself.

## Output

Select one next responsibility or explicitly defer all. Create a separate bounded plan/ADR/specification only when that selected responsibility requires one.

Do not implement the next responsibility inside this X1 plan.

---

# Stage R9 — Richer EvidenceGapPlanner reactivation trigger

Do not schedule richer planner work by date or enthusiasm.

Reactivate when evidence demonstrates approximately:

```text
at least 2 independently admitted bounded capabilities
+
real states where more than one is plausibly useful
+
ordering/value changes with proposition state, selected structured evidence, prerequisites, attempt history, failures, cost, or budget
+
small fixed deterministic ordering becomes materially brittle, duplicated, combinatorial, or semantically contextual
```

Then the richer learning/build target becomes:

```text
trusted richer state
→ bounded model observation
→ EvidenceGapPlanner
→ choose among multiple capabilities / sequence / stop / defer / unresolved semantics
→ execute one capability
→ classify result/failure
→ update trusted state/evidence
→ re-plan
```

## Future LbD concepts activated at that trigger

- multi-action planning;
- information-gain prioritization;
- prerequisite/dependency planning;
- budgeted planning;
- real multi-turn agent loops/state machines;
- checkpoints;
- failure-aware replanning;
- stale-plan handling;
- tool-result feedback;
- model routing/retries only if concrete evidence requires them;
- LangGraph/LangChain/framework comparison only when the loop complexity creates a real implementation decision.

---

## 10. Planner-input decisions to settle explicitly during execution

Use this as a decision checklist, not a bureaucracy gate.

| Field / concept | Current candidate | Decision need |
|---|---|---|
| `planning_question` | include | required; already evidenced |
| repository / PR / revision | deterministic-only | required for trace/action/admission, not current model reasoning |
| `dependency_transition.normalized_package/old_version/proposed_version` | include | canonical transition context |
| proposition `key/state/evidence_coverage/detail` | include | core typed decision-state spine |
| `EvidenceGapPlanningEvidence` | include selectively | structured question-relevant mechanism/limitation/witness detail beyond proposition labels |
| `evidence_owner` | undecided | include only if useful to reasoning/trace |
| proposition `origin` | undecided | test whether it changes planning value |
| `raw_external_text` flag | probably omit if raw text already excluded | retain only with clear planning role |
| attempt `action_id/outcome` | include | trusted history, not LLM memory |
| attempt finding prose | do not rely on it | material findings become trusted proposition/planning-evidence state |
| remaining budget | include | bounded loop / future prioritization |
| allowed action ID/purpose/preconditions | include | reasoning/action-space context |
| exact locator metadata | deterministic-only by default | model must not own/echo it |
| raw changelog | exclude current seam | earlier semantic owner handles it; structured mechanism evidence may be projected |
| full CI logs/workflow YAML | exclude current seam | selected structured CI planning evidence may be projected |
| full diffs/source | exclude by default | project structured scope facts only when useful |
| raw commands | exclude by default | prefer deterministically interpreted command semantics |
| evaluator/oracle metadata | exclude | leakage/contamination boundary |

---

## 11. AI/LLM engineering learning map

This plan deliberately teaches through the real implementation rather than detached technology study.

### Directly used and expected to be learned well

- semantic extraction vs grounding;
- context engineering / request projection;
- full agent/system state vs model observation;
- typed proposition state vs selected structured planning evidence;
- action spaces / closed capability catalogs;
- structured outputs / JSON Schema;
- deterministic admission / guardrails;
- capability binding;
- TOCTOU / stale-plan validation;
- action history;
- no-tool dispositions / abstention;
- state transitions / agent-loop basics;
- replay / reproducibility;
- evaluation harnesses;
- contamination / holdout discipline;
- local inference / LM Studio boundary;
- failure taxonomy / observability;
- strongest deterministic baseline comparison.

### Adjacent, teach when the real stage makes them useful

- graph nodes / edges / state machines;
- LangGraph;
- LangChain;
- tool/function calling;
- checkpoints;
- hooks/lifecycle callbacks;
- middleware;
- retries and semantic retries;
- prompt/version management;
- model routing/fallbacks;
- LLM-as-a-judge;
- MCP;
- RAG;
- agent frameworks.

For adjacent topics:

```text
understand concept + relationship to UpgradePilot
!= adopt mechanism
```

Adoption requires a real current responsibility and evidence that ordinary existing mechanisms are insufficient.

---

## 12. Allowed modification boundary during later execution

When the user separately authorizes implementation of this plan, permitted areas are bounded by stage.

### Normally allowed

- `experiments/`;
- `experiments/tests/`;
- this selected plan when execution reveals a real ambiguity;
- dated `working-memory/` for material evidence/decisions;
- `MEMORY.md` when live continuation/disposition changes;
- active tests/tools only when directly required for the experiment proof and correct ownership supports it.

### Requires separate ownership decision before mutation

- `src/upgradepilot/` product planner integration;
- accepted product specifications;
- ADRs;
- existing upstream semantic product boundary;
- security/runtime provider policy;
- new dependencies/frameworks/services;
- product-simulation broad research scope.

Planning approval is not silent authorization for those product/architecture changes.

---

## 13. Proof hierarchy

Use the strongest proof appropriate to each claim.

```text
naming/design claim
→ naming spec + responsibility trace + maintainer recall test

request-projection claim
→ rendered request inspection + focused deterministic tests

parser/admission claim
→ focused deterministic tests + counterfactual rejection cases

model capability claim
→ actual local model output on development/fresh protected cases as applicable

reliability/generalization claim
→ repeated fresh protected evaluation, not one smoke

product behavior claim
→ product source/tests/runtime only after separate product integration
```

Do not use plan text as implementation proof.

---

## 14. Prohibited scope

Do not use this plan to:

- fabricate a second action for evaluation aesthetics;
- claim a general adaptive planner from S001;
- integrate a product planner before a later explicit adoption/build decision;
- broaden the upstream LLM merely to feed the planner;
- collapse semantic discovery and planning into one model role;
- add LangGraph/LangChain/agent framework merely for learning exposure;
- pass entire evidence object graphs to the model because projection is inconvenient;
- make raw external text planner-visible without a demonstrated reasoning need;
- reduce the planner permanently to label-only state when existing structured evidence contains material discriminating information;
- allow the model to invent repository/revision/path/commands;
- treat schema validity as semantic correctness;
- treat model proposal as execution authorization;
- reuse v2 protected material as uncontaminated final scoring evidence;
- continue product simulation merely for more cases;
- create a new plan after every stage;
- turn action history into untrusted conversational memory instead of typed system state;
- make compatibility/safety/maintainer claims from planner output.

---

## 15. Reassessment triggers

Pause and reassess this plan when any of these becomes true:

1. a second independently justified capability enters the product and creates real competing-action states;
2. broader upstream semantic discovery produces materially richer typed candidate state;
3. the selected structured `EvidenceGapPlanningEvidence` projection still loses decision-critical information for a real bounded planning question;
4. raw/near-raw evidence becomes demonstrably necessary for correct planning;
5. ordinary Python orchestration becomes materially difficult enough that a framework comparison is justified;
6. local model/provider configuration changes enough to invalidate prior behavioral evidence;
7. a fresh real failure contradicts E1–E5 assumptions;
8. planner value becomes clearly dominated by a smaller deterministic policy across the admitted responsibility;
9. product integration is explicitly selected and therefore requires a separate Build/ADR/specification decision.

---

## 16. Overall pass condition

This plan passes when the project can state, with inspectable evidence:

```text
what EvidenceGapPlanner exactly owns
what exact context it sees and why
what proposition state it sees
what selected structured planning evidence it sees and why
what exact decision it may propose
what deterministic code still owns
what the coherent experimental implementation proves
what it does not prove
whether the current seam is retained/rejected/deferred
whether fresh v3 is justified
what independent capability comes next
when richer multi-action planning should reopen
```

And the learner can trace the real flow at the appropriate depth:

```text
trusted evidence
→ domain interpretation / grounding
→ typed proposition state + selected structured planning evidence
→ bounded model observation
→ EvidenceGapPlanner
→ structured decision
→ deterministic action binding/admission
→ bounded execution
→ result/evidence interpretation
→ trusted state update
→ optional next turn
```

without confusing this with a LangGraph/LangChain requirement or with unbounded LLM authority.

---

## 17. Final stop line

The end of this plan is **not** automatically product integration.

A successful outcome may legitimately be:

```text
EvidenceGapPlanner experiment/control seam retained
+
current richer planner expansion deferred
+
next independent capability selected
+
clear trigger preserved for future multi-action/multi-turn planning
```

That is an evidence-backed engineering result, not a failure to build enough agent machinery.
