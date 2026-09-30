# Step 4 — Existing AI / LLM / Agent Work Reconciliation

**Recorded:** 2026-09-29  
**Branch:** \`analysis/ai-agentic-capability-map-2026-09-28\`  
**Status:** COMPLETE initial reconciliation  
**Live-main anchor:** \`b16c984daa8f5e78ebe83856c5b010c137a405ee\`  
**Main product state:** Increment 3 CLOSED; Increment 4 selected and not yet started at the time of this analysis.  
**Owner:** supporting architecture analysis only; this file does not change accepted main-branch plans, ADRs, specifications, or live continuation.

---

# 1. Purpose

Step 3 established the whole product responsibility map.

Step 4 asks a narrower question:

> **Where do the AI/LLM/agent components already built or proposed in UpgradePilot belong in that map, and what should happen to each of them?**

This step does **not** ask:

- what interesting AI framework should be added next;
- how to turn UpgradePilot into a general agent;
- how to maximize AI usage;
- whether a technology is fashionable.

Each existing AI/agent artifact is evaluated against:

1. exact Step-3 responsibility;
2. current product status;
3. Track-B external evidence;
4. Track-C architecture disposition;
5. whether a simpler non-AI owner exists;
6. missing evaluation evidence;
7. appropriate next status.

---

# 2. Disposition vocabulary

- **KEEP ADOPTED** — already justified as product architecture for its bounded responsibility.
- **RETAIN AS PILOT** — useful experiment/architecture evidence; not product-adopted.
- **DEFER ACTIVATION** — conceptually valid but product prerequisites do not yet exist.
- **DEFER FRAMEWORK ADOPTION** — experiment may remain valuable, but the framework has not earned product use.
- **EXPAND LATER** — responsibility is real and evidence supports eventual broader work, but not now.
- **REWORK BEFORE ACTIVATION** — idea is useful but assumptions should be updated before implementation.
- **RETIRE / REJECT** — no longer justified.
- **NOT A GAP** — absence is intentional and should not trigger implementation.

---

# 3. Executive reconciliation

The existing AI/agent work is **better placed than it may appear when viewed file-by-file**.

It maps cleanly onto three separate Step-3 responsibilities:

\`\`\`text
Stage 8/9
semantic impact discovery / candidate formulation
→ adopted support-drop LLM extractor

Stage 11
evidence-gap / next-action investigation planning
→ ordinary-Python EvidenceGapPlanner pilot
→ LangGraph alternative experiment

Stage 13–15
cross-evidence synthesis / action explanation / maintainer report
→ bounded LLM synthesis proposal
\`\`\`

The correct result is therefore **not** to merge them into one generic agent.

Their responsibilities are different:

\`\`\`text
"What changed?"
!=
"What evidence should I acquire next?"
!=
"What should the maintainer do with the total evidence?"
\`\`\`

The architectural pattern that survives across all three is:

\`\`\`text
trusted deterministic state
→ explicit bounded model observation
→ structured model proposal
→ deterministic validation/admission
→ trusted product state
\`\`\`

But the degree of model context and authority may differ by responsibility.

---

# 4. Artifact 1 — bounded local support-drop semantic extractor

## Artifact

- \`docs/architecture/ADR-0006-bounded-local-support-drop-semantic-extractor.md\`
- \`src/upgradepilot/upstream/support_drop_extractor.py\`

Current method:

\`\`\`text
authoritative crossed-release source window
→ local Gemma model via LM Studio
→ structured support-drop candidate
→ deterministic exact source-line reconstruction
→ deterministic candidate validation
→ grounded claim / explicit unresolved problem
\`\`\`

## Step-3 owner

**Stage 8 — broad impact-candidate discovery, bounded mechanism slice**  
**Stage 9 — candidate formulation/grounding**

## Current status

**Real product-adopted method.**

ADR-0006 is accepted.

The adoption was evidence-gated against a frozen corpus rather than selected by preference.

The model owns only the missing natural-language semantic interpretation.

Deterministic code retains:

- source authority;
- package/version identity;
- source bytes/offsets;
- candidate category/direction bounds;
- exact grounding;
- downstream authority.

## Track-B / Track-C comparison

External research strongly supports this architecture pattern:

- Semgrep uses structured target/dependency evidence before LLM upgrade reasoning;
- DepRepair found distilled evidence materially stronger than raw evidence;
- mature agent systems separate context/tooling from authority;
- Track C independently supported bounded semantic extraction with deterministic source validation.

## Main limitation

The method is **correctly scoped but deliberately narrow**.

Its input world is primarily trusted release/changelog evidence.

Tier-1 showed the mature upstream evidence family should also consider:

- deterministic old/new API differences;
- upstream source diff;
- migration guides;
- package behavior change;
- possibly target-aware structural context.

This is a limitation of **evidence breadth**, not a reason to weaken ADR-0006.

## Disposition

### **KEEP ADOPTED**

Do not reopen or replace the current support-drop extractor merely because richer discovery methods now exist.

### **DO NOT generalize this module into the whole candidate-discovery engine**

The support-drop extractor should remain a bounded semantic producer.

Future broad discovery should compose multiple producers rather than mutate this implementation into a universal LLM analyzer.

## Next evidence when relevant

Run E2:

\`\`\`text
changelog semantic extraction
vs
Griffe/API diff
vs
combined evidence
\`\`\`

on a protected Python dependency-update corpus.

## Learning / portfolio value

This is already real project experience with:

- local model serving;
- LM Studio;
- structured JSON-schema output;
- prompt contract design;
- source grounding;
- model/evidence authority separation;
- failure/abstention handling;
- model evaluation and adoption gates.

---

# 5. Artifact 2 — ordinary-Python EvidenceGapPlanner

## Artifacts

Plan:

- \`plans/BOUNDED_PRODUCT_AGENTIC_INVESTIGATION_PLANNER_AND_ORCHESTRATION_EVALUATION_PLAN.md\`

Key experiment modules:

- \`experiments/evidence_gap_planner_model_boundary.py\`
- \`experiments/local_evidence_gap_planner.py\`
- \`experiments/evidence_gap_action_admission.py\`
- \`experiments/evidence_gap_investigation_transition.py\`
- \`experiments/evidence_gap_product_planner_composition.py\`

Architecture:

\`\`\`text
real product evidence state
→ bounded EvidenceGapPlannerContext
→ local model
→ ACTION_SELECTED / settled / defer / unresolved-like disposition
→ fresh deterministic action admission
→ exact read-only action
→ deterministic domain interpretation
→ immutable next state / replay trace
\`\`\`

Current first action:

\`\`\`text
acquire_exact_target_python_declaration
\`\`\`

## Step-3 owner

**Stage 11 — evidence-gap analysis and discriminating investigation**

This is exactly the right responsibility for an adaptive planner.

It is **not** candidate discovery.

It is **not** final action synthesis.

## What is architecturally strong

The experiment correctly separates:

\`\`\`text
model-visible semantic state
from
hidden execution authority
\`\`\`

The model does not invent:

- repository;
- revision;
- path;
- mutation class;
- result-family authority;
- action preconditions.

The action is rebound against fresh trusted state after the model returns.

This directly matches external ACI/tool-authority lessons from SWE-agent/OpenHands-style systems while remaining substantially safer and narrower.

## Main limitation

The current catalog has only one meaningful real action.

Therefore it can test:

- evidence-gap diagnosis;
- action vs no-action judgment;
- contract following;
- stale/action admission;
- stop/defer/unresolved behavior.

It **cannot** establish general adaptive planning value.

A planner becomes materially different from a fixed rule only when:

\`\`\`text
several legitimate next actions exist
AND
which action is best depends on current evidence
\`\`\`

## Track-C comparison

Track C independently supports:

\`\`\`text
fixed pipeline first
→ bounded planner only for state-dependent evidence selection
\`\`\`

That means the planner responsibility is correct, but product adoption is premature.

## Disposition

### **RETAIN AS PILOT**

Architecture lesson: retain.

Product integration: do not activate yet.

General planner adoption remains unavailable from a one-action evaluation.

The existing main plan's open disposition gate remains valid; this branch does not rewrite that authority.

## Promotion gate

Before product adoption, E6 must become possible:

\`\`\`text
same protected evidence-gap cases

fixed deterministic investigation sequence
vs
bounded model planner

with >= 2 independently justified real actions
\`\`\`

Measure:

- correct next evidence action;
- stop correctness;
- unnecessary investigation count;
- evidence gain/action;
- invalid/unauthorized choices;
- repeated-run stability;
- cost;
- cases resolved beyond the fixed baseline.

## Important update from Tier-1

The mature action catalog should not necessarily stay permanently closed to one tiny static list.

But expansion should mean:

\`\`\`text
trusted capability registry
+ typed parameters
+ deterministic policy/admission
\`\`\`

not:

\`\`\`text
model invents arbitrary shell/tool actions
\`\`\`

## Learning / portfolio value

The current experiment already provides defensible hands-on exposure to:

- agent state/action spaces;
- structured model planning;
- context projection;
- tool allowlisting;
- deterministic action admission;
- stale-state rebinding;
- read-only capability execution;
- trajectory/replay design;
- prompt injection boundaries;
- model-vs-authority separation.

---

# 6. Artifact 3 — LangGraph EvidenceGapPlanner implementation

## Artifacts

- \`plans/LANGGRAPH_BOUNDED_EVIDENCE_GAP_PLANNER_INDEPENDENT_DESIGN_IMPLEMENTATION_AND_COMPARISON_PLAN.md\`
- \`experiments/langgraph/evidence_gap_workflow.py\`

Current graph shape:

\`\`\`text
START
→ PLAN
→ AUTHORIZE
→ INVESTIGATE
→ CONCLUDE
→ END
\`\`\`

The implementation deliberately owns LangGraph-native workflow types rather than wrapping the ordinary-Python experiment object-for-object.

## Step-3 owner

Same as ordinary Python:

**Stage 11 — adaptive investigation orchestration**

LangGraph is therefore an **implementation alternative**, not another product responsibility.

## What it proved

The experiment provides genuine hands-on architecture evidence around:

- StateGraph;
- explicit nodes/transitions;
- runtime context;
- planner ports;
- authority ports;
- workflow state;
- graph-controlled branching;
- framework-neutral final result;
- separation of planning and authorization.

## Track-B / Track-C comparison

The independent research did not produce evidence that UpgradePilot currently needs:

- checkpoint/resume;
- durable distributed graph execution;
- multiple concurrent agents;
- complex branching;
- long-running HITL orchestration;
- workflow-engine persistence.

The current bounded investigation still has one real action and a simple loop.

Ordinary Python can express that responsibility clearly.

## Disposition

### **RETAIN EXPERIMENT EVIDENCE**
### **DEFER FRAMEWORK ADOPTION**

Do not delete the experiment: it is valuable architecture and learning evidence.

Do not adopt LangGraph into product runtime now.

## Re-entry trigger

Reconsider LangGraph or another workflow engine only when at least one real product pressure appears, such as:

- several investigation actions with branching loops;
- pause/resume over human input;
- durable checkpointing;
- multi-stage retry/recovery;
- long-running orchestration;
- multiple agents/actors that are independently justified;
- state-machine complexity that materially worsens ordinary Python.

## What should not happen

Do not continue expanding the LangGraph experiment simply to keep gaining framework exposure.

The learning objective has already been materially achieved.

---

# 7. Artifact 4 — bounded LLM-assisted maintainer decision/report synthesis proposal

## Artifact

- \`proposals/2026-09-10_LLM_ASSISTED_MAINTAINER_DECISION_AND_REPORT_SYNTHESIS_PROPOSAL.md\`

Candidate architecture:

\`\`\`text
validated heterogeneous evidence
→ DecisionEvidenceBundle
→ deterministic DecisionPermissionEnvelope
→ one structured LLM synthesis call
→ action + evidence references + report priority
→ deterministic validation
→ deterministic rendering / fallback
\`\`\`

## Step-3 owner

Primarily:

- **Stage 13 — cross-candidate synthesis**
- **Stage 14 — overall sufficiency / action permission**
- **Stage 15 — maintainer-facing report**

The proposal correctly keeps investigation planning separate from final synthesis.

## What is strong

The following design ideas remain strong:

- deterministic action authority remains outside the model;
- model operates only after evidence has been earned;
- model cites supplied evidence identifiers;
- structured semantic result precedes rendering;
- provider failure remains different from semantic abstention;
- deterministic fallback exists;
- no multi-agent design without demonstrated need;
- final report prose cannot silently upgrade model-derived evidence.

## What Tier-1 / Track-C changed

The proposal predates several new findings.

### 7.1 PermissionEnvelope should remain a hypothesis

Track C did not establish that:

\`\`\`text
deterministically compute all permitted actions
→ LLM merely chooses among them
\`\`\`

is necessarily the mature optimum.

Possible alternatives remain:

- deterministic action selection + model explanation;
- deterministic minimum permission + calibrated model claim admission;
- interactive maintainer choice;
- action-specific mixed deterministic/semantic prerequisites.

Therefore \`DecisionPermissionEnvelope\` is a strong experiment design, not yet a final architecture.

### 7.2 Model context may need progressive source access

The proposal intentionally favors a bounded \`DecisionEvidenceBundle\`.

That is still a strong default.

But Tier-1 repository-intelligence research warns against permanently banning controlled exact-source retrieval when explanation/synthesis exposes an ambiguity.

The future experiment should measure whether the compact projection is sufficient before hard-coding it as the permanent context policy.

### 7.3 Evaluation must include maintainer outcomes

The original proposal already rejects “nicer prose” as success.

Tier-1 strengthens this considerably.

A future synthesis experiment should measure:

- decision correctness;
- time-to-decision;
- evidence-use accuracy;
- appropriate trust;
- ability to detect a wrong model synthesis;
- information overload;
- external lookups.

Not only:

- action-label agreement;
- prose quality.

## Current prerequisite gap

Today UpgradePilot still lacks mature:

- cross-candidate synthesis state;
- non-abstention action permission contracts;
- protected synthesis corpus;
- decision-quality UX surface.

The current maintainer-action evaluator intentionally admits only \`abstain\`.

Therefore there is no honest product input yet for evaluating the proposed final synthesizer.

## Disposition

### **DEFER ACTIVATION**
### **RETAIN AS A STRONG FUTURE EXPERIMENT DESIGN**
### **REWORK BEFORE ACTIVATION using Track-C findings**

Do not implement it during current runtime dependency-state work.

## Activation gate

Activate only after:

1. at least two materially different technical candidate families coexist in real synthesis;
2. cross-candidate state is represented;
3. first non-abstention action semantics are accepted;
4. a transparent deterministic baseline exists;
5. a protected synthesis corpus exists;
6. an observed deterministic limitation is recorded.

Then compare the LLM method against the actual baseline.

---

# 8. Artifact 5 — Mature System Horizon AI/agent sections

## Artifact

- \`proposals/UPGRADEPILOT_MATURE_SYSTEM_HORIZON.md\`

This is not an AI component.

It is a non-controlling whole-system horizon containing concepts such as:

- broad candidate discovery;
- hybrid semantic methods;
- investigation;
- cross-candidate synthesis;
- experimental models/graphs/agents.

## Step-3 owner

It spans Stages 8–15.

## Track-C relationship

The horizon's major structural thesis survives:

\`\`\`text
candidate discovery
→ candidate formulation
→ applicability
→ investigation
→ synthesis
\`\`\`

Step 3 now adds more explicit:

- CI/runtime/package-state evidence layers;
- repository-intelligence views;
- external standards/provenance;
- runtime telemetry;
- AI placement;
- architecture experiment triggers;
- maintainer decision-quality evaluation.

## Disposition

### **KEEP AS NON-CONTROLLING HORIZON**
### **DO NOT update it immediately only to mirror this analysis branch**

After Step 5 selects actual follow-up changes, reconcile the horizon once at its proper authority level.

Avoid churn where a proposal is repeatedly rewritten before architecture decisions are accepted.

---

# 9. Missing AI responsibility discovered by Step 3 — broad impact candidate discovery

This is the most important Step-4 finding.

UpgradePilot already has:

- one adopted semantic extractor;
- one bounded planner family;
- one future synthesis proposal.

But the mature AI role with the **largest expected product value** still has no general evaluated implementation:

> **Broad technical impact-candidate discovery.**

## Step-3 owner

**Stage 8**

Question:

> Given this dependency transition, upstream changes, target repository structure, CI/build/package context, what materially plausible impact mechanisms should be evaluated?

## Why this is not the support-drop extractor

The support-drop extractor answers one known semantic family:

\`\`\`text
Does this authoritative release evidence explicitly state a current Python support drop?
\`\`\`

Broad discovery asks an open-world question:

\`\`\`text
What material mechanisms might exist at all?
\`\`\`

These require different evaluation.

## Why this is not the EvidenceGapPlanner

Planner:

\`\`\`text
given a known unresolved proposition
→ which evidence should we acquire next?
\`\`\`

Discovery:

\`\`\`text
which candidate propositions should exist?
\`\`\`

## Why this is not final synthesis

Synthesis assumes the important candidate state already exists.

Discovery happens before applicability and investigation.

## Mature candidate architecture

Track B/C supports:

\`\`\`text
deterministic update/package/source signals
+ upstream changelog/API/source diff
+ repository structural context
+ package/build/CI context
→ bounded semantic candidate discovery
→ typed candidate set
→ later applicability evaluation
\`\`\`

## Disposition

### **EXPAND LATER — strongest future AI responsibility**

Do not activate it now merely because it is important.

Its prerequisites include:

- more trustworthy evidence infrastructure;
- candidate schema/generalization work;
- upstream API/source-diff experiment;
- context/repository-intelligence comparison;
- protected candidate-discovery evaluation corpus.

This should become a major future AI experiment when Stage 8 becomes active.

---

# 10. AI work that should NOT be added now

## 10.1 Generalist OpenHands-style product agent

### Disposition: **NOT A GAP**

A broad agent is a later long-tail comparator/escalation.

Do not build one now.

Use only when bounded evidence capabilities demonstrably fail on real atypical repositories.

---

## 10.2 Multi-agent debate / specialist swarm

### Disposition: **NOT A GAP**

External evidence does not justify it as the default architecture.

A challenger/verifier may later be useful selectively.

No current product responsibility requires a permanent multi-agent topology.

---

## 10.3 LangChain abstraction layer

### Disposition: **NOT A GAP**

Direct LM Studio HTTP remains adequate for the adopted support-drop role.

The planner experiment likewise does not need framework abstraction merely for model invocation/tool calling.

Reconsider only when provider/tool/model routing complexity becomes real.

---

## 10.4 Generic RAG/vector database

### Disposition: **NOT A GAP**

Repository retrieval is a real future problem.

A vector database is not automatically the answer.

Future E5 should compare:

- lexical;
- structural;
- graph;
- embedding;
- hybrid;
- exact raw-source retrieval.

Technology follows measured retrieval need.

---

## 10.5 LLM-as-a-judge as product authority

### Disposition: **NOT A GAP / DO NOT ADOPT**

A model judge may later be an evaluation aid under controlled conditions.

It must not become the source of product truth merely because human labels are expensive.

---

# 11. AI/agent responsibility map after reconciliation

| Step-3 responsibility | Existing AI/agent work | Step-4 disposition |
|---|---|---|
| exact identity | none | correct; no AI needed |
| dependency transition | none | correct; no AI needed |
| package-manager semantics | none | correct; no AI needed |
| upstream semantic extraction | support-drop local LLM | **KEEP ADOPTED** |
| broad candidate discovery | no general system | **EXPAND LATER — major future AI role** |
| candidate grounding | support-drop deterministic validation pattern | **KEEP pattern** |
| applicability | deterministic/mechanism-specific | keep authority deterministic/hybrid |
| evidence-gap selection | ordinary-Python planner pilot | **RETAIN AS PILOT** |
| agent orchestration framework | LangGraph experiment | **RETAIN evidence / DEFER adoption** |
| runtime evidence acquisition | planner can eventually request capability | no AI authority; future capability |
| cross-candidate synthesis | no product model yet | design first |
| final action/report synthesis | LLM proposal | **DEFER ACTIVATION / REWORK before use** |
| generalist investigation | none | **NOT A GAP** |
| multi-agent | none | **NOT A GAP** |
| AI evaluation | support-drop frozen eval + planner protocol | expand later into shared protected evaluation discipline |

---

# 12. Shared architectural pattern worth preserving

Across the successful/current experiments, one pattern is now independently validated enough to keep as a **design principle**, without turning it into one universal framework:

\`\`\`text
1. Establish trusted deterministic state.

2. Project only the semantic context needed for the current model responsibility.
   - projection may be narrow for extraction/planning;
   - future discovery may allow controlled progressive retrieval.

3. Treat model output as an untrusted structured proposal.

4. Rebind proposal identifiers to exact trusted state.

5. Apply deterministic authority/admission/policy.

6. Execute or compose only admitted effects.

7. Preserve model origin and transformation identity.

8. Keep unresolved/model failure/provider failure distinct.

9. Evaluate against a real deterministic/fixed baseline.

10. Promote only the responsibility/method that earned evidence.
\`\`\`

This is more important than whether the implementation uses:

- direct HTTP;
- LangGraph;
- LangChain;
- OpenHands;
- another framework.

---

# 13. Framework disposition

## Direct LM Studio HTTP

**Current support-drop responsibility:** justified and adopted.

**Planner pilot:** proportional and sufficient.

Disposition:

### **KEEP where currently justified**

Do not create a generic provider abstraction until at least two real owners require materially shared behavior.

---

## LangGraph

Disposition:

### **RETAIN AS HANDS-ON / ARCHITECTURE COMPARISON EVIDENCE**
### **DEFER PRODUCT ADOPTION**

Re-entry requires real orchestration pressure.

---

## LangChain

Disposition:

### **DEFER / no current product need**

No evidence currently shows it improves an admitted responsibility.

---

## OpenHands or similar generalist agent framework

Disposition:

### **FUTURE COMPARATOR ONLY**

Use after bounded-agent limitations are demonstrated on long-tail cases.

---

# 14. Current experience-evidence status

This reconciliation also clarifies what can accurately be claimed as experience.

## Product-integrated / validated bounded AI experience

### Local LLM semantic extraction

Real code + accepted ADR + evaluation.

Reasonable future portfolio wording can accurately describe hands-on work with:

- LM Studio;
- local GGUF/LLM inference;
- OpenAI-compatible structured output;
- JSON Schema contracts;
- evidence grounding;
- deterministic model validation;
- model safety/authority boundaries.

## Hands-on experimental agent experience

### EvidenceGapPlanner

Real experiment code exists for:

- planner context;
- structured output;
- action selection;
- deterministic admission;
- read-only action execution;
- replay/state transitions.

Accurate wording:

> designed and implemented a bounded local-LLM investigation-planner experiment with deterministic tool admission and replayable state transitions.

Do not describe it as a production agent.

## Hands-on LangGraph experience

Real \`StateGraph\` implementation exists.

Accurate wording:

> implemented and compared a bounded LangGraph workflow separating planning, authorization, investigation, and conclusion.

Do not claim LangGraph product adoption.

## LLM final synthesis

Proposal/research only.

Do **not** claim implementation experience until the experiment exists.

---

# 15. Immediate consequences

## For main / Increment 4

**No change.**

Step 4 provides no reason to insert AI into the command-derived package-state composer.

Increment 4 remains deterministic composition.

## For Increment 5

Also no model requirement.

The package-state witness should first be integrated into the application/evidence flow.

## For current AI work

Do not start a new AI implementation now.

Preserve:

- support-drop extractor as adopted;
- planner as pilot;
- LangGraph as comparison evidence;
- synthesis as deferred proposal.

## For the next AI activation

The most valuable future AI responsibility is broad candidate discovery.

But activate it only after the product route reaches that responsibility and the E2/E5/evaluation prerequisites exist.

---

# 16. What should be changed later, after Step 5

Step 4 itself should not mutate controlling main artifacts.

After Step 5 selects actual architecture actions, likely reconciliation candidates include:

1. mature-system horizon:
   - add multi-view repository intelligence;
   - runtime telemetry as optional producer;
   - standards interoperability;
   - refined AI role placement.

2. planner plan:
   - explicitly record Track-C requirement for >=2 real actions before general adoption;
   - preserve fixed-pipeline comparison.

3. synthesis proposal:
   - update PermissionEnvelope from implied mature architecture to explicit experiment hypothesis;
   - add maintainer decision-quality evaluation;
   - reconsider permanent narrow-context assumptions.

4. future candidate-discovery plan:
   - create only when that responsibility is actually activated.

Do not make these edits until Step 5 decides the exact scope.

---

# 17. Step-4 final dispositions

\`\`\`text
Support-drop semantic extractor
→ KEEP ADOPTED

Ordinary-Python EvidenceGapPlanner
→ RETAIN AS PILOT
→ no product adoption yet

LangGraph planner implementation
→ RETAIN EXPERIMENT EVIDENCE
→ DEFER FRAMEWORK ADOPTION

LLM-assisted final synthesis proposal
→ RETAIN STRONG FUTURE DESIGN
→ DEFER ACTIVATION
→ REWORK BEFORE ACTIVATION

Mature-system AI/agent horizon
→ KEEP NON-CONTROLLING
→ reconcile after Step 5

Broad impact candidate discovery
→ MAJOR MISSING FUTURE AI RESPONSIBILITY
→ EXPAND LATER, not now

Generalist product agent
→ NOT A CURRENT GAP

Multi-agent system
→ NOT A CURRENT GAP

LangChain / generic agent framework
→ NOT A CURRENT GAP

Generic vector/RAG infrastructure
→ NOT A CURRENT GAP
\`\`\`

---

# 18. Main architectural conclusion

UpgradePilot's existing AI work does **not** form one half-built “agent architecture.”

It forms three intentionally different experiments/product slices:

\`\`\`text
SEMANTIC EXTRACTION
"What does this evidence say?"
→ adopted bounded LLM

INVESTIGATION PLANNING
"What evidence should we inspect next?"
→ bounded planner pilot

DECISION SYNTHESIS
"Given the earned evidence, what should the maintainer see/do?"
→ future proposal
\`\`\`

The missing mature AI layer between extraction and planning is:

\`\`\`text
BROAD CANDIDATE DISCOVERY
"What relevant impact mechanisms might exist at all?"
\`\`\`

That is the next major AI architecture question when the product reaches that responsibility.

The product should continue to be defined by its evidence-backed maintainer decision responsibility—not by any model, framework, graph, or agent topology.

---

# 19. Step status

\`\`\`text
Track A                           COMPLETE
Track B / Tier-1                  COMPLETE
Track C                           COMPLETE
Step 3 whole-pipeline map         COMPLETE
Step 4 AI/agent reconciliation    COMPLETE

Next:
Step 5 select actual changes / experiments / ADRs / deferrals
\`\`\`

Step 5 must convert the research into a **small set of concrete architecture decisions**.

It should answer:

- which current artifacts need no change;
- which main artifacts should later be updated;
- which experiments are queued and at what trigger;
- which ideas are explicitly deferred;
- whether any new specification/ADR is justified now;
- how this analysis branch should ultimately integrate back without disrupting Increment 4.
