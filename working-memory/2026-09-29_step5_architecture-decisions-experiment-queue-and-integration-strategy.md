# Step 5 — Architecture Decisions, Experiment Queue, Deferrals, and Integration Strategy

**Recorded:** 2026-09-29  
**Branch:** \`analysis/ai-agentic-capability-map-2026-09-28\`  
**Status:** COMPLETE initial convergence decision  
**Live-main anchor:** \`e63019cddaa64565504c3de98c87449d49838667\`  
**Live product state:** Increment 4 A1 CURRENT; Increment-4 A0 DONE; no Build authorized until A1 and A2 clear.  
**Branch relationship to main at convergence:** 49 commits ahead / 81 commits behind, with branch-only changes limited to research/plan/working-memory documentation.

This record converts the completed Track A/B/C + Step 3/4 research into concrete project dispositions. It does not itself authorize Increment-4 Build work or modify live \`MEMORY.md\`.

---

# 1. Executive decision

The completed research does **not** justify a product-architecture reset.

The correct project decision is:

> **Keep the current evidence/trust spine and Increment-4/5 sequence intact; adopt no new AI/agent/framework dependency now; preserve the research as architecture evidence; activate only a small set of comparative experiments when their owning product responsibilities actually become current.**

The architecture work changes **future method selection**, not current implementation sequencing.

The project should therefore avoid two equal mistakes:

\`\`\`text
MISTAKE A
ignore the research and keep hand-building every future capability

MISTAKE B
interrupt current verified work to adopt CodeQL/graphs/agents/frameworks now
\`\`\`

The chosen route is:

\`\`\`text
continue current R4 product work
+
preserve new architecture constraints
+
run discriminating experiments only at responsibility triggers
+
reconcile durable horizon/spec/ADR owners when a decision becomes active
\`\`\`

---

# 2. Bucket A — CHANGE NOW

Very little should change now.

## A1. Current implementation sequencing

### Decision

**NO CHANGE to Increment 4 or Increment 5 sequencing.**

\`\`\`text
Increment 4
→ command-derived RequirementSatisfiedAtCommandCompletion composer

Increment 5
→ application/investigation integration
\`\`\`

### Reason

Track C independently supports the selected proof contract.

No researched technology solves this bounded package-manager semantic composition responsibility better than the accepted deterministic method.

### Explicit exclusions

Do not add to Increment 4:

- CodeQL;
- repository graphs;
- runtime telemetry;
- LLMs;
- EvidenceGapPlanner;
- LangGraph;
- standards adapters;
- broad impact discovery;
- maintainer-action synthesis.

---

## A2. Architecture decision discipline

### Decision

From now on, every proposed advanced method should name:

1. the exact Step-3 responsibility it owns;
2. the current baseline;
3. the observed limitation;
4. the comparative experiment;
5. the admission/rejection criterion.

This becomes the practical interpretation of the project's existing technology-admission discipline.

### Why

The research showed that technologies become misleading when discussed without product ownership.

Example:

\`\`\`text
"Should we use CodeQL?"
\`\`\`

is not a valid architecture question.

The valid question is:

\`\`\`text
"Before expanding UpgradePilot's GitHub Actions CFG/dataflow responsibility,
does CodeQL Actions provide better evidence coverage/cost/maintainability
than the current custom route for this exact proposition family?"
\`\`\`

---

## A3. Preserve AI responsibility separation

### Decision

Keep these responsibilities distinct in all future planning:

\`\`\`text
semantic extraction
!=
candidate discovery
!=
applicability
!=
investigation planning
!=
cross-candidate synthesis
!=
action permission
!=
report rendering
\`\`\`

Do not create a generic \`Agent\` or \`AIEngine\` owner that erases these boundaries.

---

## A4. Preserve model visibility vs authority distinction

### Decision

Retain the proven authority rule:

\`\`\`text
model may inspect / interpret / propose / prioritize
!=
model may self-authorize evidence, proof strength, execution, or action
\`\`\`

But do **not** freeze “tiny typed projection only” as a universal mature rule.

Future broad discovery may use controlled progressive retrieval of:

- exact raw source;
- graph/query results;
- upstream source/API changes;
- repository instructions.

Authority remains separately validated.

---

# 3. Bucket B — LEAVE UNTOUCHED

These artifacts/responsibilities should not be reopened by this research.

## B1. ADR-0006 support-drop semantic extractor

**Decision: KEEP ADOPTED.**

No redesign.

Future broad discovery should compose around it, not mutate it into a universal LLM subsystem.

---

## B2. Increment-1/2/3 runtime dependency-state work

**Decision: CLOSED / DO NOT REOPEN.**

Track C found no contradiction.

Current bounded syntax/environment coverage may later gain additional evidence producers, but that is future expansion, not a defect in the accepted increments.

---

## B3. ADR-0010 package-manager semantic/runtime-state contract

**Decision: KEEP.**

Its package-state/later-use/action boundaries are independently supported.

---

## B4. Current abstain-only maintainer-action implementation

**Decision: KEEP FOR CURRENT STAGE.**

Do not broaden actions before their positive permission semantics are owned and evidenced.

This remains a project-stage boundary, not the mature final behavior.

---

## B5. Direct LM Studio HTTP for current adopted semantic role

**Decision: KEEP.**

No generic provider abstraction is justified now.

---

# 4. Bucket C — QUEUED EXPERIMENTS

The research produced ten possible experiments, but they should not all become project work.

They are now ordered by **product trigger**, not novelty.

---

## E1 — CodeQL Actions comparator

**Priority:** HIGH when trigger activates  
**Owner:** workflow/CI CFG-dataflow evidence  
**Current status:** QUEUED, NOT ACTIVE

### Trigger

Activate **before** materially expanding custom support for:

- complex workflow conditions;
- reusable workflows;
- matrix/context propagation;
- cross-step environment/data flow;
- generalized Actions CFG reasoning.

### Question

\`\`\`text
current custom workflow model
vs
CodeQL Actions
\`\`\`

Which gives stronger proposition coverage at acceptable:

- precision;
- implementation complexity;
- provenance mapping;
- setup/runtime cost;
- maintainability?

### Learning value

Very high:

- QL;
- CFG;
- dataflow;
- taint;
- GitHub Actions security/program analysis.

---

## E2 — Upstream API/source-diff comparator

**Priority:** HIGH when Stage-8 discovery activates  
**Owner:** upstream evidence / candidate discovery  
**Current status:** QUEUED

### Candidate tools

- Griffe for Python API diff;
- direct old/new source comparison where needed.

### Compare

\`\`\`text
changelog/release evidence
vs
API/source diff
vs
combined evidence
\`\`\`

### Why

This is likely the first experiment needed before broad candidate discovery becomes credible.

### Learning value

Very high:

- API compatibility;
- semantic versioning evidence;
- Python introspection/static structure;
- source-diff reasoning.

---

## E3 — Runtime telemetry comparator

**Priority:** CONDITIONAL HIGH  
**Owner:** CI/runtime observation  
**Current status:** QUEUED ON REAL GAP

### Trigger

A decision-critical runtime proposition remains unresolved after accepted static/GitHub evidence.

### Compare

\`\`\`text
static inference
vs
instrumented process/network/file observation
\`\`\`

Potential reference system:
StepSecurity-like telemetry.

### Rule

Do not introduce telemetry infrastructure without a real unresolved proposition.

---

## E4 — Small multi-view repository-intelligence experiment

**Priority:** MEDIUM/HIGH, trigger-driven  
**Owner:** repository intelligence  
**Current status:** QUEUED

### Trigger

Two or more real responsibilities repeatedly need the same structural relations, such as:

- package usage;
- callers/importers;
- affected tests;
- CI consumers;
- build/test ownership.

### Experiment

Build the smallest useful Python repository view, potentially RIG-like.

Do **not** start with Neo4j or a universal graph.

Compare query value before backend commitment.

---

## E5 — Model context experiment for broad discovery

**Priority:** HIGH when Stage-8 AI discovery activates  
**Owner:** candidate discovery  
**Current status:** QUEUED

### Compare

\`\`\`text
typed bounded projection only
vs
typed projection + structural retrieval
vs
progressive exact raw-source retrieval
\`\`\`

Measure:

- candidate recall;
- unsupported candidate rate;
- context noise;
- grounding;
- token/cost.

### Coupling

Prefer to run with E2 on the same protected candidate-discovery corpus.

---

## E6 — Fixed investigation vs EvidenceGapPlanner

**Priority:** REQUIRED BEFORE PLANNER ADOPTION  
**Owner:** Stage-11 investigation  
**Current status:** BLOCKED ON SECOND REAL ACTION

### Trigger

At least **two independently justified real investigation actions** exist.

### Compare

\`\`\`text
best fixed deterministic sequence
vs
bounded model planner
\`\`\`

Measure:

- useful action choice;
- stop correctness;
- evidence gain/action;
- unnecessary actions;
- invalid/unauthorized actions;
- repeated-run stability;
- cost.

### Current disposition

EvidenceGapPlanner remains a pilot until this trigger exists.

---

## E7 — Bounded planner vs generalist agent

**Priority:** LOW / LONG-TAIL  
**Owner:** atypical repository investigation  
**Current status:** DEFERRED UNTIL E6 + REAL LONG-TAIL CASES

### Candidate comparator

OpenHands or equivalent sandboxed software agent.

### Rule

Do not run this experiment on routine cases merely for exposure.

---

## E8 — Calibrated model-claim admission

**Priority:** LATER  
**Owner:** semantic claim trust/admission  
**Current status:** DEFERRED

### Trigger

A semantic model produces enough protected cases that deterministic-only admission materially limits useful coverage.

### Required evidence

- risk/coverage curves;
- accepted-claim precision;
- OOD cases;
- calibration drift;
- source-grounding failure behavior.

Until then, current conservative model authority remains.

---

## E9 — Standards/interoperability mapping

**Priority:** NON-BLOCKING LAB  
**Owner:** provenance/export/interchange  
**Current status:** OPTIONAL QUEUE

### Experiment

Map one real UpgradePilot evidence case into:

- CycloneDX;
- SPDX;
- in-toto/SLSA where applicable.

### Goal

Discover reusable interoperability without forcing internal semantics into external schemas.

---

## E10 — Maintainer decision-quality study

**Priority:** LATE PRODUCT MATURITY  
**Owner:** report/decision UX  
**Current status:** DEFERRED

### Trigger

- multiple real candidate families;
- stable report surface;
- at least one non-abstention action family.

### Measure

- decision correctness;
- decision time;
- appropriate trust;
- external lookups;
- ability to detect wrong system claims;
- cognitive load.

---

# 5. Experiment activation order

Do not read E1–E10 as a chronological roadmap.

The trigger graph is:

\`\`\`text
CURRENT
Increment 4 → Increment 5

later workflow complexity?
→ E1

broad candidate discovery activates?
→ E2 + E5
→ possibly E4 if structural reuse appears

multiple real investigation actions?
→ E6
→ only if bounded planner struggles on real long-tail cases → E7

decision-critical runtime evidence gap?
→ E3

enough semantic-model protected evidence?
→ E8

interoperability/reporting need?
→ E9

stable mature maintainer UX?
→ E10
\`\`\`

This avoids an “experiment project” replacing the actual product.

---

# 6. Bucket D — EXPLICIT DEFERRALS

The following are now explicitly deferred rather than left as vague future possibilities.

## D1. LangGraph product adoption

**DEFER.**

Re-enter only for concrete orchestration pressure:

- checkpoint/resume;
- human pause/resume;
- complex branching;
- durable state;
- multi-stage recovery;
- independently justified multiple actors.

The current hands-on experiment is sufficient for learning evidence.

---

## D2. LangChain

**DEFER.**

No current responsibility is blocked by direct HTTP / ordinary Python.

---

## D3. Generalist software agent as default architecture

**DEFER / reject as default.**

May later be a long-tail comparator after E6.

---

## D4. Multi-agent/debate architecture

**DEFER.**

No current evidence shows value exceeding cost/complexity.

A challenger/verifier may later be tested selectively.

---

## D5. Generic vector database / RAG platform

**DEFER.**

Retrieval is a future responsibility; vector DB technology is not yet justified.

E5 decides context/retrieval needs first.

---

## D6. Universal repository/evidence graph

**DEFER / reject as starting architecture.**

If graph value is proven, prefer multiple bounded views with stable identities and provenance.

---

## D7. Standards-native internal domain model

**DEFER / reject.**

UpgradePilot should keep its domain-specific reasoning model.

Standards may become adapters.

---

## D8. Automatic remediation / patch generation

**DEFER.**

Remain outside the current core until decision-support value is established.

Future candidate:
Griffe + LibCST + validation, with model repair only where evidence justifies it.

---

## D9. LLM final synthesis activation

**DEFER.**

The proposal is retained, but activation requires:

- real cross-candidate state;
- non-abstention action semantics;
- deterministic baseline;
- protected corpus;
- observed baseline limitation.

---

## D10. Broad general AI trust

**REJECT as a concept.**

Trust remains responsibility-specific and evidence-specific.

An adopted model for one bounded task does not transfer authority to another task.

---

# 7. ADR / specification decisions

## 7.1 New ADR now?

### Decision: **NO NEW ADR NOW**

Reason:

The research produced several strong architecture principles, but the unresolved ones are method competitions, not accepted implementation decisions.

Creating ADRs now for:

- CodeQL;
- graph architecture;
- planner adoption;
- model context breadth;
- selective authority;
- standards integration;

would prematurely convert hypotheses into architecture.

## 7.2 Existing ADR changes now?

### Decision: **NO**

ADR-0006 and ADR-0010 remain valid.

## 7.3 Product decision-model specification changes now?

### Decision: **NO IMMEDIATE CHANGE**

Its trust/proposition/uncertainty spine survived Track C.

Later changes may be warranted when:

- broad discovery contracts activate;
- repository-intelligence evidence types become real;
- action permission semantics expand.

## 7.4 New durable architecture record?

### Decision: **YES, BUT AS A NON-CONTROLLING SYNTHESIS AFTER INTEGRATION**

The durable content worth promoting from this research is:

1. Step-3 whole-pipeline responsibility map;
2. Step-4 AI-role reconciliation;
3. Step-5 decision/experiment/deferral register.

These should be condensed into **one main-branch non-controlling architecture/research reconciliation artifact**, rather than making all Tier-1 research files controlling documents.

Suggested future target:

\`proposals/UPGRADEPILOT_EVIDENCE_AI_ARCHITECTURE_RECONCILIATION.md\`

Its role:

- durable architecture orientation;
- experiment triggers;
- AI placement;
- explicit non-decisions.

It must reference, not replace:

- Charter;
- specs;
- ADRs;
- plans;
- \`MEMORY.md\`.

Do not create this on active main until integration timing is chosen.

---

# 8. Existing main artifact reconciliation

## 8.1 Mature System Horizon

### Decision: **UPDATE ONCE, AFTER THIS BRANCH IS INTEGRATED**

Required changes should be bounded:

- add explicit evidence-producer/repository-intelligence layer;
- add optional runtime telemetry;
- state multi-view rather than universal graph hypothesis;
- clarify model-visible context vs authority;
- refine AI role locations;
- add protected evaluation + maintainer decision-quality direction.

Do not turn the horizon into a detailed research dump.

---

## 8.2 EvidenceGapPlanner plan

### Decision: **NO IMMEDIATE REWRITE REQUIRED**

The current plan already correctly states:

- one-action catalog cannot justify general planner adoption;
- a second real action is required;
- fixed deterministic baseline is required;
- framework adoption is not automatic.

Step 5 therefore finds the plan already substantially aligned.

Potential future small reconciliation:
add explicit reference to E6 once the second action appears.

---

## 8.3 LangGraph plan

### Decision: **KEEP HISTORICAL/EXPERIMENTAL; NO EXPANSION**

No product-runtime integration.

No need to keep evolving the plan absent a re-entry trigger.

---

## 8.4 LLM synthesis proposal

### Decision: **UPDATE ONLY WHEN ACTIVATION BECOMES REAL**

Before activation, revise it to incorporate:

- PermissionEnvelope as experiment hypothesis, not assumed mature optimum;
- maintainer decision-quality evaluation;
- controlled progressive source/context possibility;
- protected corpus requirements;
- calibration/selective-risk findings.

No need to rewrite it now.

---

# 9. Branch integration decision

Current compare:

\`\`\`text
analysis branch
→ 49 commits ahead of main
→ 81 commits behind main
→ branch-only files are research/plan/working-memory additions
→ no source/test modifications
\`\`\`

## Decision

### **DO NOT MERGE THIS BRANCH WHOLESALE INTO ACTIVE MAIN**

Reasons:

1. \`main\` is already in Increment-4 A1 and has advanced substantially since branch creation.
2. The branch contains many deep research records that are useful evidence but would add large volume to the live project surface.
3. Most Tier-1 reports are research provenance, not controlling artifacts.
4. A wholesale merge would blur historical research with the current product cycle.
5. There are no source changes requiring preservation through merge.

## Preserve the branch

### Decision: **KEEP THE ANALYSIS BRANCH AS RESEARCH PROVENANCE**

Do not delete it after convergence.

It is the detailed evidence archive.

## Selective integration set

When main integration is appropriate, port only a distilled set:

### Must preserve durably

1. **Step 3 — whole-pipeline architecture map**
2. **Step 4 — AI/agent reconciliation**
3. **Step 5 — decision/experiment/deferral register**
4. **Research technology/learning exposure ledger**

### Preserve by reference / branch provenance

- Tier-1 Reports 01–07;
- external research-area discovery;
- Step 2B-X;
- Step 2C;
- large analysis working memory;
- closed supporting analysis plan.

They remain available on this branch/commit history and can be cited by the distilled main artifact.

## Integration mechanism

Preferred:

\`\`\`text
current main
→ after a safe LbD stop boundary
→ create one fresh main-based integration branch
→ copy/distill the selected durable artifacts
→ reconcile Mature System Horizon once
→ verify no live-plan/MEMORY ownership is changed
→ merge as documentation-only architecture reconciliation
\`\`\`

Do **not** rebase/merge the old analysis branch merely to preserve every research commit.

---

# 10. Integration timing

Main is currently:

\`\`\`text
Increment 4
A0 DONE
A1 CURRENT
\`\`\`

The current cycle is actively onboarding.

## Decision

### **DO NOT interrupt A1/A2 with architecture-document integration.**

Earliest clean integration point:

- after an explicit Increment-4 STOP boundary; preferably after the cycle closes, unless a Track-C finding becomes directly relevant to Increment-4 proof truth.

Current research found no such contradiction.

Therefore default:

\`\`\`text
finish Increment 4 normally
→ integrate distilled architecture research
→ continue Increment 5 with the durable whole-system context available
\`\`\`

A Smart Situational Override remains possible if new evidence makes the architecture record immediately necessary, but there is no current reason.

---

# 11. Main-roadmap consequences

The research does not replace the current roadmap.

It does create later decision gates.

## Current

\`\`\`text
Increment 4
→ Increment 5
\`\`\`

## After runtime-state sequence

The next major architecture focus should be chosen based on current live plans and evidence, but Step 5 suggests likely high-value pressure areas:

1. application-level use of package-state evidence;
2. broader candidate discovery;
3. cross-candidate synthesis;
4. action permission;
5. robust evaluation.

Do not automatically start E1/E2/E4 simply because the research is finished.

---

# 12. Learning/exposure decisions

Research findings should contribute to Ali's learning path, but project adoption remains evidence-driven.

## Strong future hands-on candidates

When triggered:

- CodeQL / QL;
- Griffe;
- LibCST;
- runtime telemetry/eBPF-adjacent CI security;
- RIG-style graph modeling;
- GUAC / GraphQL;
- CycloneDX / SPDX;
- SLSA / in-toto / Sigstore;
- calibration / selective prediction;
- OpenHands comparator;
- reproducible benchmark/eval harnesses.

## Already earned experience

- local LLM inference with LM Studio;
- structured outputs;
- source grounding;
- model trust boundaries;
- bounded agent planning;
- deterministic tool admission;
- replayable state transitions;
- LangGraph StateGraph design/comparison.

## Rule

Do not integrate a technology only to be able to list it as experience.

Use a bounded lab when learning value is high but product need is absent.

---

# 13. Concrete project decision register

| Item | Decision now | Re-entry trigger |
| --- | --- | --- |
| Increment 4 composer | **CONTINUE** | none; current route |
| Increment 5 integration | **CONTINUE LATER** | Increment 4 closes |
| support-drop LLM | **KEEP ADOPTED** | ADR reassessment triggers only |
| EvidenceGapPlanner | **RETAIN PILOT** | second real action → E6 |
| LangGraph | **DEFER PRODUCT ADOPTION** | real orchestration pressure |
| final LLM synthesis | **DEFER** | synthesis/action prerequisites |
| broad candidate-discovery AI | **QUEUE FUTURE** | Stage 8 activates |
| CodeQL | **QUEUE E1** | broader workflow reasoning pressure |
| Griffe/API diff | **QUEUE E2** | broad candidate discovery |
| runtime telemetry | **QUEUE E3** | decision-critical unresolved runtime fact |
| repository graph/RIG | **QUEUE E4** | repeated structural-query need |
| raw-source model context | **QUEUE E5** | candidate-discovery model experiment |
| generalist agent | **DEFER** | bounded planner fails long-tail after E6 |
| calibrated AI authority | **DEFER** | protected corpus + coverage pressure |
| CycloneDX/SPDX/in-toto | **OPTIONAL E9 LAB** | interoperability/provenance need |
| maintainer study | **DEFER E10** | stable mature report/actions |
| universal graph | **DO NOT ADOPT** | only reconsider with contrary evidence |
| LangChain | **DO NOT ADD** | real shared orchestration/provider need |
| multi-agent default | **DO NOT ADD** | explicit measured challenger need |
| generic RAG/vector DB | **DO NOT ADD** | E5 demonstrates retrieval need |
| remediation engine | **DEFER** | core decision support proven |
| new ADR from research | **NO** | experiment selects durable method |
| spec rewrite from research | **NO** | product responsibility changes |
| whole branch merge | **NO** | not recommended |
| distilled docs integration | **YES LATER** | clean Increment-4 stop/closure |

---

# 14. What Step 5 intentionally does NOT decide

The following remain open by design:

- CodeQL vs custom workflow modeling;
- exact repository-intelligence backend;
- exact broad-discovery model/context architecture;
- whether calibrated model claims ever enter trusted state;
- exact mature action-permission algorithm;
- final synthesis LLM vs deterministic method;
- graph database selection;
- generalist-agent value;
- standards adapter format;
- remediation architecture.

These are not failures to decide.

Each now has a concrete experiment or activation prerequisite.

---

# 15. Final architecture position after the research program

The research program converges on this project stance:

\`\`\`text
KEEP
the current exact/provenance/open-world evidence spine

CONTINUE
Increment 4 → Increment 5

USE
deterministic methods for mechanical facts

USE
bounded semantic models where open-ended meaning is the real missing capability

USE
bounded adaptive agents only when next evidence choice is genuinely state-dependent

ALLOW
controlled repository/source visibility when discovery needs it

ADD
runtime observation when inference cannot settle a decision-critical proposition

EVALUATE
advanced methods against strong fixed baselines and protected cases

PRESERVE
unresolved/conflicted states instead of forcing decisions

OPTIMIZE EVENTUALLY FOR
maintainer decision quality, not AI autonomy

DO NOT DEFINE UPGRADEPILOT AS
an LLM system
an agent system
a graph system
a static analyzer
or a dependency bot

DEFINE IT AS
an evidence-backed dependency-update decision-support system
whose methods are selected responsibility by responsibility
\`\`\`

---

# 16. Research-program closure status

\`\`\`text
Track A
  Step 1 limitation inventory                       COMPLETE
  Step 2A project-conditioned classification        COMPLETE

Track B
  independent/de-anchored research                 COMPLETE
  Tier-1 #01–#07                                   COMPLETE
  Step 2B-X architecture refresh                    COMPLETE

Track C
  Step 2C adversarial reconciliation                COMPLETE

Step 3 whole-pipeline architecture map              COMPLETE
Step 4 AI/agent reconciliation                      COMPLETE
Step 5 decisions/experiments/integration strategy   COMPLETE
\`\`\`

The architecture research program is therefore **CLOSED at the analysis level**.

The next action on this branch is not more broad research.

The main product workstream should continue Increment 4.

The research branch should remain preserved until the selected distilled artifacts are integrated at a clean main-branch stop boundary.
