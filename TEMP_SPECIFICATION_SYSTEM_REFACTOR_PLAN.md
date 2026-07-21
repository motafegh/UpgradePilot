# Temporary Specification System Refactor Plan

**Status:** Temporary controlling plan for the specification-system review and modification work only  
**Location:** UpgradePilot repository root  
**Created:** 2026-07-21  
**Removal condition:** Delete this file after all approved modifications, validation, snapshot refresh, and final review are complete  

> This file does not change the UpgradePilot product mission, current technical decisions, current milestone, implementation authorization, capability evidence, or progress state. It controls only the bounded work required to improve the project’s specification, governance, instruction, state, and documentation system.

---

## 1. Purpose

The current UpgradePilot/Career control system contains many strong ideas:

- mission-driven learning;
- real-input and failure-led engineering;
- just-in-time prerequisite repair;
- accurate technical mental models;
- conservative capability claims;
- explicit AI-assistance disclosure;
- learner ownership requirements;
- evidence-based architecture decisions;
- narrow product boundaries;
- safeguards against uncontrolled planning and architecture growth.

The purpose of this refactor is to preserve those strengths while removing structural friction that causes one logical decision or session result to propagate through many files.

The central problem is not that individual updates are always unjustified. The problem is that temporary state, stable rules, technical requirements, decision records, session evidence, navigation, and mirrored program controls are currently mixed or duplicated. This creates:

- excessive ceremony;
- state duplication;
- change amplification;
- mixed document responsibilities;
- repeated AI interpretation of similar rules;
- documentation work that competes with implementation;
- over-directed sessions;
- weak or performative ownership evidence;
- insufficient distinction between legitimate design exploration and unbounded tangents;
- pressure to obtain shallow exposure across too many advanced systems.

This plan defines the complete modification program needed to correct those issues without weakening rigor, safety, evidence quality, or continuity.

---

## 2. Triggering example and design smell

The acceptance of ADR-0002 was one logical technical decision:

> Use Pydantic v2 as the runtime-contract representation method.

That decision caused updates to the ADR, architecture index, technical specification, current memory, session working memory, UpgradePilot README, Career amendment, Career tracker, Career README, Career AGENTS.md, mirrored Career files, and snapshot provenance.

Some updates were legitimate. The overall propagation still revealed five structural problems:

1. **State duplication** — the same current fact existed in several files.
2. **Change amplification** — one decision required many physical edits.
3. **Temporal coupling** — stable documents changed whenever temporary state changed.
4. **Mixed responsibility** — files acted as rulebook, dashboard, history, and tracker simultaneously.
5. **Snapshot tax** — canonical Career changes were copied into UpgradePilot and then required provenance maintenance.

The refactor must make a similar future architecture decision require only the smallest set of authoritative updates.

---

## 3. Required outcomes

The work is complete only when the following outcomes are true.

### 3.1 One fact has one authoritative owner

Every important class of information must have one primary authoritative location. Other files may link to it or show a deliberately bounded summary, but must not independently restate detailed transient facts.

### 3.2 Stable files remain stable

Stable files must not require routine edits when:

- one session ends;
- a test passes or fails;
- an implementation sub-gate changes;
- the exact next action changes;
- a method comparison closes;
- a small blocker is repaired.

### 3.3 Process is proportional to the work

The system must support lightweight, standard, and formal execution modes. A small reversible implementation step must not require the same ceremony as a milestone transition or consequential architecture decision.

### 3.4 AI direction fades as capability grows

The specifications must explicitly transfer responsibility for decomposition, next-action selection, testing strategy, diagnosis, and technical decisions from AI to Ali as demonstrated depth increases.

### 3.5 Ownership evidence measures real capability

Ownership checks must evaluate changed-case reasoning, delayed recall, failure diagnosis, design judgment, modification, testing, and reduced-prompt reproduction where appropriate. Immediate repetition or mechanically performing an AI-selected action must not be treated as strong independent ownership.

### 3.6 Legitimate technical exploration remains available

The system must distinguish:

- execution after a decision;
- consequential decision-making;
- bounded exploration;
- unbounded tangent or planning diversion.

The one-next-action rule must control execution, not suppress necessary comparison or justified technical challenge.

### 3.7 Advanced-system breadth does not destroy depth

Advanced-system exposure must remain honest, mission-connected, bounded, and evidence-dependent. It must not force six shallow implementation packages at the expense of core Python, testing, data, SQL, evaluation, debugging, and product ownership.

### 3.8 Technical requirements and implementation decisions remain separate

Technical specifications must define required behavior, invariants, contracts, and proof. ADRs must define selected implementation methods and trade-offs. Framework-specific mechanics must not be unnecessarily duplicated across both.

### 3.9 The Career snapshot has a bounded synchronization policy

The local snapshot must no longer force a full copy-and-provenance update after every session-level or decision-level Career change.

### 3.10 The plan deletes itself

After the refactor is accepted and validated, this temporary file must be removed from the repository root.

---

## 4. Non-goals

This refactor must not, by itself:

- change the UpgradePilot mission;
- change the primary user or supported decision;
- reopen project selection;
- reverse ADR-0002;
- change the current technical milestone or implementation order unless a direct contradiction is discovered;
- create new product architecture;
- write product source code;
- create tests for product behavior;
- inflate or reduce capability claims without evidence;
- erase historical evidence;
- remove safety, privacy, legal, cost, credential, or untrusted-code controls;
- weaken the distinction between AI-generated work and Ali-owned capability;
- create another permanent governance layer.

The work is a control-system refactor, not a product redesign.

---

## 5. Core design principles

All modifications must follow these principles.

### 5.1 Single source of truth

A fact that changes frequently must have one canonical owner.

### 5.2 Reference instead of repetition

Lower-authority files should link to higher-authority rules rather than rewrite them.

### 5.3 Stable rules versus live state

Stable documents define what should govern. State files record what is currently true.

### 5.4 Normative versus descriptive separation

Plans and specifications define requirements. Trackers and evidence records state whether requirements were satisfied.

### 5.5 Proportional ceremony

The cost of the procedure must be proportional to the consequence, novelty, irreversibility, and learning importance of the action.

### 5.6 Progressive transfer of control

Scaffolding is temporary. The system must deliberately reduce AI planning control as evidence supports greater learner responsibility.

### 5.7 Evidence quality over checklist completion

A required action is not automatically strong capability evidence merely because it appears in a session record.

### 5.8 Product mission remains visible

The refactor must not turn the project into a documentation exercise. Every control must support safer, clearer, more ownable product execution.

### 5.9 No hidden weakening

Simplification must remove duplication and unnecessary process, not remove essential reasoning, testing, security, or evidence requirements.

### 5.10 No new permanent file unless an existing responsibility cannot own the rule

The default solution is to improve or consolidate existing documents.

---

## 6. Target information architecture

The final system should assign responsibilities as follows.

| Artifact class | Primary responsibility | Must not become |
|---|---|---|
| `UpgradePilot.md` | Mission, user, supported decision, product boundary, outcome classes, termination and claim limits | Live session dashboard or exact-next-action record |
| Capability specification | Capability taxonomy, prerequisites, D0–D5 meaning, assessment evidence, claim rules | Current progress tracker |
| Learning and Execution Contract | Mandatory Ali–AI learning, execution, ownership, assistance, and evidence behavior | Current milestone plan |
| Learning and Project Design Profile | Evidence and hypotheses about Ali’s learning mode, motivation, fit, and known risks | Operating checklist repeated in every session |
| Learning Preferences | Teaching presentation, terminology, pacing, interaction style, and correction preferences | Duplicate execution contract |
| 90-Day Execution Contract | Stable workload, capacity, review, route-change, and anti-diversion commitments | Session-level status dashboard |
| Session and Blocker Protocol | Lightweight, standard, formal session templates and blocker handling | Project-state authority or duplicate curriculum |
| Strategy and Scope | Stable career identity, priority order, project allocation, and scope policy | Exact implementation continuation |
| Advanced Systems Policy | Orientation/exposure/pilot/adoption definitions and evidence-dependent admission | Mandatory technology checklist detached from project evidence |
| Master roadmap | Route capacity, ordered capability development, milestone relationships | Daily state tracker |
| Milestone plan | Milestone outcomes, required deliverables, gates, and boundaries | Historical result log |
| Session plan or amendment | Requirements and execution boundaries for one bounded session/work package | Rewritten tracker after every result |
| Technical specification | System requirements, contracts, invariants, failure semantics, proof obligations | Framework implementation guide duplicated from ADRs |
| ADR | One consequential technical decision, alternatives, rationale, consequences, reassessment triggers | Current project dashboard |
| Tracker | Canonical program-level state, gate result, capability evidence, assistance, limitations, next controlled responsibility | Full session transcript |
| `MEMORY.md` | Concise project-local continuation pointer and unresolved context | Duplicate tracker, roadmap, or decision record |
| Working-memory record | Session evidence, reasoning, challenge, output, assistance, unresolved local details | Canonical state authority |
| README | Public/project orientation, high-level maturity, navigation, run/use instructions when implemented | Exact session-level next action |
| `AGENTS.md` | Stable agent behavior, authority routing, safety, repository boundaries, state lookup rules | Current milestone, method, or exact-next-action record |
| Snapshot source record | Snapshot origin, refresh point, and verification | Live program tracker |

---

## 7. Canonical ownership of changing facts

The modification must establish the following ownership rules.

| Fact | Canonical owner | Allowed bounded references |
|---|---|---|
| Product mission and boundary | `UpgradePilot.md` | README, specs, plans through links or concise quotations |
| Current milestone/gate state | Career tracker | `MEMORY.md` concise pointer; README high-level milestone only if useful |
| Exact next controlled responsibility | Career tracker | Project `MEMORY.md`; current session plan where structurally required |
| Exact next command or action | Current session/working-memory context | Must not be copied into stable governance files |
| Accepted architecture method | ADR index + accepted ADR | Technical spec references selected ADR; tracker records decision gate result |
| Required system behavior | Technical specification | Tests and ADR consequences reference requirement IDs |
| Actual implemented behavior | Source, tests, outputs, committed evidence | Tracker summarizes verified proof |
| Capability depth | Career tracker under capability-spec rules | Memory may point to it, not reproduce it |
| Session reasoning and assistance | Working-memory/session evidence | Tracker records only capability-relevant conclusion |
| Workload/capacity rule | 90-Day Execution Contract | Session start selects mode without rewriting the rule |
| Learning presentation preference | Learning Preferences | Contract may link to it |
| Snapshot origin | `docs/program/SOURCE.md` | Snapshot files must not claim live canonicality |

---

## 8. Modification program

The work must proceed in the order below. Canonical Career controls are modified first. UpgradePilot-local files and the Career snapshot are modified only after the canonical Career set is internally coherent.

---

# Phase 0 — Freeze scope and inventory responsibility

## Objective

Create a precise change map before rewriting rules, without creating another permanent planning artifact.

## Actions

1. Inspect the latest canonical Career files and UpgradePilot files listed in this plan.
2. For each file, classify every substantial section as one of:
   - stable authority;
   - live state;
   - navigation;
   - historical evidence;
   - session evidence;
   - technical requirement;
   - implementation decision;
   - duplicated rule.
3. Identify direct statements of:
   - current milestone;
   - exact next action;
   - active session;
   - selected/unselected method;
   - implementation status;
   - capability status.
4. Identify rules duplicated across three or more files.
5. Mark each candidate change as:
   - preserve;
   - move;
   - replace with link;
   - narrow;
   - remove duplicate;
   - rewrite for precision.
6. Do not update the Career snapshot during this phase.

## Output

The working checklist may remain in the active conversation or temporary working notes. Do not create another repository plan file.

## Pass condition

Every proposed edit has a named responsibility problem and a target authoritative owner.

---

# Phase 1 — Establish explicit document responsibility boundaries

## Objective

Make each canonical document state what it owns and what it does not own.

## Canonical Career files to modify

- `UpgradePilot.md`
- `governance/UPGRADEPILOT_LEARNING_AND_EXECUTION_CONTRACT.md`
- `governance/UPGRADEPILOT_LEARNING_PREFERENCES.md`
- `governance/90_DAY_EXECUTION_CONTRACT.md`
- `governance/SESSION_AND_BLOCKER_PROTOCOL.md`
- `strategy/LEARNING_AND_PROJECT_DESIGN_PROFILE.md`
- `strategy/UPGRADEPILOT_CAPABILITY_AND_PREREQUISITE_SPECIFICATION.md`
- `strategy/STRATEGY_AND_SCOPE.md`
- `strategy/ADVANCED_SYSTEMS_EXPOSURE_AND_ADOPTION_POLICY.md`
- `plans/UPGRADEPILOT_90_DAY_MASTER_ROADMAP.md`
- `plans/UPGRADEPILOT_STAGED_MILESTONE_PLAN.md`
- `tracking/UPGRADEPILOT_EVIDENCE_AND_PROGRESS_TRACKER.md`

## Actions

1. Add or refine a concise responsibility/authority boundary near the top of each file.
2. State where current state is maintained.
3. State which related document governs overlapping rules.
4. Remove repeated authority lists when a shorter reference is sufficient.
5. Preserve substantive rules until their owning phase below modifies them deliberately.

## Pass condition

A future agent can answer “Which file owns this fact or rule?” without inspecting several overlapping documents.

---

# Phase 2 — Remove transient state from durable files

## Objective

Stop routine milestone/session changes from rewriting stable governance, strategy, roadmap, plan, README, and agent-instruction files.

## Files likely to modify

### Canonical Career

- `README.md`
- `AGENTS.md`
- `UpgradePilot.md`
- `governance/90_DAY_EXECUTION_CONTRACT.md`
- `governance/SESSION_AND_BLOCKER_PROTOCOL.md`
- `governance/UPGRADEPILOT_LEARNING_AND_EXECUTION_CONTRACT.md`
- `strategy/STRATEGY_AND_SCOPE.md`
- `strategy/UPGRADEPILOT_CAPABILITY_AND_PREREQUISITE_SPECIFICATION.md`
- `plans/UPGRADEPILOT_90_DAY_MASTER_ROADMAP.md`
- `plans/UPGRADEPILOT_STAGED_MILESTONE_PLAN.md`
- current and historical session plans/amendments where they mix requirements with live result state

### UpgradePilot

- `README.md`
- `AGENTS.md`
- `MEMORY.md`
- relevant working-memory records only where their role is unclear
- `docs/program/SOURCE.md`

## Actions

1. Remove exact session-level next actions from stable files.
2. Remove current method-selection status from `AGENTS.md`.
3. Remove current-session instructions from `AGENTS.md` except stable routing to the tracker/current plan.
4. Reduce README status to a deliberately coarse summary, for example:
   - active milestone;
   - implemented/not implemented maturity category;
   - link to canonical live state.
5. Do not place exact commands or session start blocks in README files.
6. Convert plan/amendment result sections into either:
   - fixed historical completion metadata; or
   - tracker-owned state references.
7. Plans should define what must happen and pass conditions. The tracker should record whether it happened.
8. `MEMORY.md` should contain only the minimum continuation context required inside UpgradePilot:
   - accepted decisions relevant to continuation;
   - what remains unimplemented or unresolved;
   - current responsibility pointer;
   - links to canonical state/evidence.
9. Working-memory records should preserve session reasoning and evidence, not claim canonical current authority.
10. Stable files may contain historical activation statements only when clearly labeled as historical and not current controls.

## Pass condition

Changing the exact next action no longer requires changes to README, `AGENTS.md`, charter, capability specification, learning contract, strategy, roadmap, or milestone definitions.

---

# Phase 3 — Consolidate duplicated learning and execution rules

## Objective

Keep the strong learning model while giving each rule one primary owner.

## Primary owners

### Capability Specification owns

- capability families;
- D0–D5 definitions;
- prerequisite relationships;
- evidence required for each depth;
- capability claim limits;
- atomic evidence-record structure.

### Learning and Execution Contract owns

- mandatory Ali–AI loop;
- decision and execution behavior;
- assistance disclosure;
- ownership transfer;
- evidence interpretation;
- stopping behavior.

### Learning Preferences owns

- terminology treatment;
- explanation depth and chunking;
- analogy use;
- command explanation style;
- correction style;
- interaction pacing;
- diagrams/comparisons when useful.

### Learning and Project Design Profile owns

- evidence about motivation and learning fit;
- known weak-fit patterns;
- hypotheses still being tested;
- project-design implications.

### Session Protocol owns

- session templates;
- blocker workflow;
- prerequisite repair workflow;
- continuation format.

## Actions

1. Identify repeated rules and retain the most complete formulation in the correct owner.
2. Replace duplicate formulations with concise references.
3. Preserve project-specific refinements only where they add information.
4. Remove duplicate lists of what AI may/must not do when the contract already controls them.
5. Ensure removal does not weaken the effective rule.

## Pass condition

No important learning or execution rule requires reconciling multiple independently worded versions.

---

# Phase 4 — Introduce proportional session modes

## Objective

Prevent small technical steps from requiring full formal-session ceremony.

## Modify

- `governance/SESSION_AND_BLOCKER_PROTOCOL.md`
- `governance/UPGRADEPILOT_LEARNING_AND_EXECUTION_CONTRACT.md`
- `governance/UPGRADEPILOT_LEARNING_PREFERENCES.md` only for presentation implications

## Required model

### 4.1 Lightweight continuation

Use for small, reversible work inside an already understood and authorized responsibility.

Minimum structure:

```text
Current responsibility:
Next observable result:
Prediction or risk when meaningful:
Action:
Proof:
Stop/continue condition:
```

A lightweight continuation does not require a full session-start or session-end form unless meaningful state must be handed off.

### 4.2 Standard learning session

Use for a new concept/responsibility or meaningful implementation increment.

Required flow:

```text
brief product orientation
→ prerequisite check
→ minimum-complete explanation
→ Ali prediction/reasoning
→ bounded action
→ inspect real evidence
→ correction or continuation
→ ownership-bearing change/check
→ concise evidence record
```

### 4.3 Formal session

Use for:

- milestone or responsibility transition;
- consequential design decision;
- material blocker;
- formal capability assessment;
- work requiring multi-conversation continuity;
- safety-, cost-, credential-, or architecture-sensitive execution.

The full Session Order and Session End structures remain available here.

## Selection rule

Choose the least ceremonial mode that still protects safety, continuity, learning, and evidence quality.

## Escalation rule

A lightweight or standard session escalates when:

- a consequential decision appears;
- assumptions materially fail;
- the task crosses a responsibility boundary;
- assistance/ownership evidence becomes ambiguous;
- the work cannot be safely continued without durable state.

## Pass condition

A 15–30 minute reversible implementation step can proceed without producing an administrative workload comparable to the technical work.

---

# Phase 5 — Add explicit AI-assistance fading

## Objective

Make reduced AI direction a required part of capability growth.

## Modify

- `governance/UPGRADEPILOT_LEARNING_AND_EXECUTION_CONTRACT.md`
- `strategy/UPGRADEPILOT_CAPABILITY_AND_PREREQUISITE_SPECIFICATION.md`
- `governance/SESSION_AND_BLOCKER_PROTOCOL.md`
- tracker evidence schema

## Required control-transfer model

| Demonstrated depth | Default responsibility distribution |
|---|---|
| D0–D1 | AI may propose the next action and explain the decomposition; Ali must understand, predict where meaningful, and challenge |
| D2 | AI presents bounded alternatives or questions; Ali selects and explains the next action |
| D3 | Ali proposes the decomposition, test, or diagnostic action; AI reviews and corrects only as needed |
| D4 | Ali controls the technical sequence and evidence plan; AI acts mainly as reviewer, challenger, or targeted assistant |
| D5 | Ali operates independently across changed cases and uses AI selectively without depending on it for central decomposition |

## Apply the model to

- next-action selection;
- implementation decomposition;
- test design;
- diagnostic hypothesis selection;
- evidence selection;
- architecture comparison;
- stopping decisions;
- explanation and reproduction.

## Anti-regression rule

If evidence shows the learner cannot perform the responsibility at the expected assistance level, reduce the claim or temporarily restore scaffolding. Do not preserve an optimistic depth label.

## Pass condition

The system no longer allows repeated AI-selected execution to be mistaken for growing independent engineering judgment.

---

# Phase 6 — Distinguish decision mode, exploration mode, and execution mode

## Objective

Preserve focus without suppressing legitimate technical judgment.

## Modify

- Learning and Execution Contract
- Session and Blocker Protocol
- Learning Preferences
- Strategy/anti-rabbit-hole rules where necessary

## Required modes

### Decision mode

Use when a consequential choice is unresolved.

```text
responsibility and constraints
→ simplest baseline
→ two to four credible alternatives
→ trade-offs and failure modes
→ evidence needed
→ Ali challenges/selects
→ decision record when warranted
```

### Bounded exploration mode

Use when a technical question may affect the active responsibility but is not yet known to require a decision.

Requirements:

- explicit question;
- time/scope ceiling;
- relationship to active responsibility;
- expected information gain;
- stop and return condition;
- no permanent architecture admission without a decision gate.

### Execution mode

Use after the decision is made.

```text
one selected action
→ execute
→ inspect
→ continue, repair, or reopen decision only with evidence
```

### Tangent/diversion mode

Use when the question does not block or materially affect the active responsibility. Record briefly and return.

## Pass condition

“One next action” applies strongly during execution but does not prohibit the comparison needed to make a sound consequential decision.

---

# Phase 7 — Strengthen capability and ownership evidence

## Objective

Prevent checklist-complete but weak ownership claims.

## Modify

- Capability Specification
- Learning and Execution Contract
- tracker schema
- Learning Preferences only where assessment interaction is described

## 7.1 Atomic capability records

Replace broad evidence claims with records shaped like:

```text
Capability family:
Specific responsibility:
Depth:
Context:
Evidence:
Assistance level:
Ownership dimensions:
Changed-case evidence:
Failure evidence:
Delayed evidence:
Last demonstrated:
Breadth:
Confidence:
Transfer limit:
```

Example:

```text
Capability family: Python testing
Specific responsibility: Diagnose and repair strict Pydantic validation unit tests
Depth: D2 guided
Transfer limit: Does not establish integration-test design or general pytest ownership
```

## 7.2 Ownership vector

For central work, record ownership separately for:

- problem understanding;
- design;
- implementation;
- testing;
- operation;
- diagnosis;
- explanation;
- reduced-prompt reproduction.

The overall claim must not exceed the weakest dimension required by that capability.

## 7.3 Evidence expectations by depth

### D1

- accurate recognition or explanation after teaching.

### D2

- guided application to the current case;
- correct interpretation of representative evidence.

### D3

Require, where the responsibility supports it:

- one changed case;
- one action selected with limited prompting;
- one relevant failure diagnosis;
- one delayed recall or reconstruction check;
- one ownership-bearing modification or test.

### D4

Require:

- repeated evidence across sessions;
- changed-context transfer;
- design or challenge of the responsibility;
- implementation and test ownership;
- diagnosis of an unfamiliar failure;
- explanation of system-wide consequences;
- low-assistance reproduction.

### D5

Require sustained independent performance across materially different contexts and explicit recognition of limitations.

## 7.4 Performative-check prohibition

Do not treat the following alone as strong ownership:

- repeating an explanation immediately after the AI;
- typing an AI-provided change;
- approving an AI-selected design;
- running a command successfully;
- passing AI-generated tests;
- producing one guided artifact.

## Pass condition

Capability claims describe exactly what Ali can do, under what assistance, in which context, with explicit transfer limits.

---

# Phase 8 — Refine prerequisite, command, planning, and workload rules

## Objective

Keep safeguards but remove rigid interpretations that can reduce learning quality.

## 8.1 Prerequisite repair

Modify the 90-minute rule into an initial review checkpoint, not an automatic stop.

At the checkpoint determine:

1. Can Ali safely continue the active responsibility?
2. Is the remaining gap required now?
3. Can the responsibility be narrowed?
4. Should the repair continue inside the same package?
5. Should remaining depth be distributed across later changed cases?
6. Does the gap materially change route scope or sequence?

Formal replanning is required only for the final condition or another material program impact.

## 8.2 Adaptive command explanation

Define three levels:

### New or consequential

Explain name, purpose, key flags/operators, inputs/outputs, side effects, risks, failure categories, and what the evidence proves.

### Familiar but changed

Explain changed arguments, context, risk, and expected difference.

### Repeated and safe

Use a concise reminder or no repeated explanation unless requested or misunderstood.

Increase explanation whenever the command is destructive, credential-sensitive, networked, capability-evidence-bearing, or unexpectedly behaves differently.

## 8.3 Planning categories

Separate:

- **governance planning** — roadmaps, milestone redesign, program restructuring;
- **technical decision record** — ADR, specification amendment, experiment protocol, threat model;
- **execution sketch** — short current-step sequence, tests, evidence, and stop line.

Anti-planning rules apply strongly to unnecessary governance planning. They must not prohibit normal technical decomposition or warranted decision records.

## 8.4 Workload and cognitive stop

Preserve weekly capacity commitments, but add:

> Do not begin a new consequential responsibility merely to fill remaining hours when concentration, comprehension, or diagnostic quality has materially declined.

Safe remaining capacity may be used for:

- reviewing already-written code;
- replaying established behavior;
- organizing evidence;
- delayed recall;
- bounded cleanup;
- another already-authorized low-risk continuation.

Hours remain a capacity target, not proof of capability or justification for poor-quality advancement.

## Pass condition

Timeboxes and workload controls support disciplined execution without forcing premature continuation or unnecessary administrative work.

---

# Phase 9 — Rebalance the advanced-systems policy

## Objective

Preserve meaningful career exploration while protecting core depth and product credibility.

## Modify

- `strategy/ADVANCED_SYSTEMS_EXPOSURE_AND_ADOPTION_POLICY.md`
- `strategy/STRATEGY_AND_SCOPE.md`
- `plans/UPGRADEPILOT_90_DAY_MASTER_ROADMAP.md`
- `plans/UPGRADEPILOT_STAGED_MILESTONE_PLAN.md`
- `governance/90_DAY_EXECUTION_CONTRACT.md`
- Capability Specification if exposure evidence intersects capability claims

## Replace the default target

### Required orientation

All six areas reach A0 accurate orientation:

- Kubernetes;
- microservices;
- distributed queues;
- multi-cloud systems;
- bounded autonomous multi-agent systems;
- advanced MLOps.

A0 must still include accurate responsibility, baseline, trade-offs, and mission relationship.

### Required hands-on selection

Two or three areas reach A1 according to:

- project relevance;
- prerequisite readiness;
- expected information gain;
- career-learning value;
- available capacity;
- ownership health.

### Required integrated pilot

At least one area reaches A2 when a defensible representative project workload and simpler baseline exist.

### Conditional second pilot

A second A2 is authorized only if:

- the core product remains on track;
- evidence quality is healthy;
- Ali’s ownership is not falling behind;
- the pilot is not artificial;
- sufficient capacity remains.

### Stretch exposure

A1 for remaining areas and any A3 adoption are evidence-dependent stretch outcomes.

## Negative-decision evidence

For every area not admitted to A1/A2, record:

```text
Current project need:
Prerequisite state:
Simpler baseline:
Reason not admitted:
Opportunity cost:
Reconsideration trigger:
```

This is valid technical judgment, not a failed requirement.

## Capacity rule

Replace a fixed 20–30% obligation with a bounded range reviewed against core progress. Reserve capacity only after the first credible end-to-end core and basic ownership gates are healthy.

## Pass condition

The advanced-system program produces honest orientation, selected depth, and defensible adoption/rejection decisions without becoming a six-technology checklist.

---

# Phase 10 — Refine technical specification and ADR boundaries

## Objective

Make technical control precise, traceable, and resistant to framework duplication.

## Modify in UpgradePilot

- `docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md`
- `docs/architecture/README.md`
- ADR files only when their responsibility boundaries need clarification
- future tests/spec references when implementation work resumes; do not write product tests as part of this governance-only phase

## Actions

### 10.1 Requirement language

Define and use consistently:

- **MUST** — required for acceptance;
- **MUST NOT** — prohibited;
- **SHOULD** — expected unless a documented reason exists;
- **MAY** — permitted.

Retain accepted/provisional/deferred as decision or maturity status, not requirement strength.

### 10.2 Stable requirement identifiers

Assign identifiers to important invariants, for example:

```text
PR-ID-001: Pull-request number must be a positive non-boolean integer.
SHA-001: Base and head revisions must contain 40 hexadecimal characters.
RAW-001: Normalization must not mutate supplied raw input.
PATH-001: Normalized changed-file paths must be unique.
```

Use an identifier scheme grouped by responsibility rather than one global undifferentiated number sequence.

### 10.3 Contract-to-proof mapping

Add a concise traceability structure:

| Requirement | Required proof category | Current implementation evidence |
|---|---|---|
| `RAW-001` | non-mutation test | pending/linked test |
| `SHA-001` | valid and invalid cases | pending/linked tests |

The technical specification defines proof obligations. The tracker or implementation evidence records actual proof status.

### 10.4 Framework boundary

The specification controls:

- strict validation behavior;
- undeclared-field handling;
- trusted/raw separation;
- immutable trusted structures;
- explicit adapter behavior;
- structured failures;
- externally observable contract behavior.

ADR-0002 controls:

- Pydantic v2 selection;
- `BaseModel`/configuration mechanisms;
- framework-specific validator choices;
- major-version policy;
- framework trade-offs and reassessment triggers.

The specification may link to the accepted ADR but should avoid repeating unnecessary Pydantic mechanics.

### 10.5 Clarify semantic order

Explicitly define the order and boundary among:

- raw preservation;
- source-format parsing;
- normalization;
- type validation;
- semantic validation;
- trusted-object creation.

Clarify which failures belong to which layer.

### 10.6 Clarify M2 raw-input scope

State whether M2 preserves only the input mapping supplied to the adapter or whether it constructs the later full raw-source record. Avoid implying a broader provenance contract than the milestone implements.

## Pass condition

A future test can cite a stable requirement ID, while a future framework change can be handled primarily through an ADR without rewriting unrelated contract language.

---

# Phase 11 — Redesign README, AGENTS, MEMORY, and working-memory behavior

## Objective

Make repository entry points useful without turning them into duplicate trackers.

## UpgradePilot README

Retain:

- product purpose;
- primary user and supported decision;
- high-level flow;
- current maturity category at coarse granularity;
- project layout;
- run/use instructions when implementation exists;
- links to specification, ADR index, tracker snapshot/source, and limitations.

Remove or avoid:

- exact next session action;
- detailed current gate sequence;
- full Pydantic decision restatement;
- detailed milestone contract duplication;
- session start instructions.

## Career README

Retain:

- program purpose;
- selected flagship;
- stable authority/navigation;
- coarse current route pointer;
- link to tracker for exact state.

Do not duplicate exact method status or session continuation.

## UpgradePilot and Career `AGENTS.md`

Retain:

- stable authority resolution;
- repository boundaries;
- safety and untrusted-code rules;
- how to locate live state;
- evidence and claim discipline;
- snapshot handling;
- file-edit responsibility rules.

Remove:

- exact current method;
- exact current session;
- exact next action;
- temporary milestone details;
- detailed active implementation instructions.

## `MEMORY.md`

Use a compact continuation structure:

```text
Current responsibility:
Accepted decisions relevant now:
Implemented/verified state:
Unresolved item:
Canonical state/evidence links:
Immediate continuation pointer:
```

Do not duplicate full governance rules, ADR rationale, roadmap, or tracker entries.

## Working memory

Working-memory records may contain:

- what happened;
- Ali’s challenge or reasoning;
- actual output;
- assistance used;
- local unresolved questions;
- evidence links.

They must clearly state that the tracker/accepted artifacts control current state.

## Pass condition

A reader can orient quickly, but a session-level decision no longer forces entrypoint rewrites.

---

# Phase 12 — Redesign the Career snapshot policy

## Objective

Keep local continuity without doubling every canonical edit.

## Modify

- `docs/program/SOURCE.md`
- snapshot-related rules in UpgradePilot `AGENTS.md`
- snapshot navigation text
- mirrored Career files only once after canonical Career modifications are complete

## Target policy

### Snapshot nature

The snapshot is a reviewed point-in-time program context, not a live mirror updated after every canonical change.

### Refresh triggers

Refresh only when one of these occurs:

- milestone transition;
- formal program review;
- material governance change that affects UpgradePilot operation;
- project-local continuation would otherwise be materially wrong;
- explicit manual refresh request.

Do not refresh merely because:

- one test changes;
- one session ends;
- one exact next action changes;
- one implementation sub-gate passes;
- one working-memory entry changes.

### Canonical precedence

When canonical Career access is available, canonical files control. The snapshot must state its source commit and age clearly.

### Refresh execution

After all canonical Career refactor commits are reviewed:

1. select one canonical Career commit;
2. copy the approved snapshot set once;
3. verify exact content equality;
4. update `docs/program/SOURCE.md` once;
5. do not perform intermediate snapshot refreshes during the refactor.

### Future automation

A lightweight script may be added if useful to:

- copy the approved snapshot set;
- record source commit;
- verify hashes/content equality;
- report differences.

The script must reduce manual ceremony and must not create another live synchronization requirement.

## Pass condition

A normal ADR or session result does not automatically require canonical Career edits, mirrored edits, and provenance edits in the same operation.

---

# Phase 13 — Add bounded consistency validation

## Objective

Prevent responsibility drift without creating a heavy documentation platform.

## Candidate checker

Add one small script only if it materially reduces future manual review. It may check:

- broken local Markdown links;
- exact-next-action phrases in files that are prohibited from carrying transient state;
- current milestone/session fields inside `AGENTS.md` or durable specifications;
- duplicate or missing requirement IDs;
- missing ADR index entries;
- snapshot source metadata and content equality when a refresh is intentionally performed;
- prohibited claims such as production-ready/mastery without required evidence markers.

## Limits

The checker must not:

- become a general documentation framework;
- require complex infrastructure;
- infer semantic truth it cannot reliably determine;
- force every wording change through an elaborate schema;
- block product work for stylistic differences.

## Pass condition

The checker catches high-value structural mistakes with low maintenance cost.

---

# Phase 14 — Validate through change-amplification scenarios

## Objective

Test the redesigned system against realistic future events.

## Scenario A — Accept a new architecture ADR

Expected updates:

1. new/updated ADR;
2. architecture index;
3. technical specification only if a direct requirement/status statement changes;
4. tracker decision-gate result;
5. concise project memory pointer if continuation materially changes.

Not normally expected:

- README updates;
- `AGENTS.md` updates;
- roadmap rewrites;
- learning-contract rewrites;
- immediate snapshot refresh;
- rewriting the plan that originally required the ADR.

Target: normally no more than four or five canonical logical updates.

## Scenario B — One implementation test passes

Expected updates:

- source/test evidence;
- working-memory/session evidence;
- tracker only if a gate or capability state materially changes;
- `MEMORY.md` only if continuation changes.

No governance or README changes.

## Scenario C — Exact next action changes inside the same milestone

Expected updates:

- tracker or current execution context;
- concise `MEMORY.md` continuation pointer.

No stable-file changes.

## Scenario D — Milestone transition

Expected updates may include:

- tracker;
- milestone activation metadata;
- project memory;
- coarse README maturity summary if useful;
- one intentional Career snapshot refresh.

This is an appropriate higher-ceremony event.

## Scenario E — Ali challenges an accepted method

Expected behavior:

- enter bounded decision/exploration mode;
- inspect the accepted ADR and reassessment triggers;
- collect discriminating evidence;
- do not reject the challenge as a tangent merely because one action was previously selected;
- update ADR/spec only if the decision actually changes.

## Scenario F — A prerequisite exceeds 90 minutes

Expected behavior:

- perform the review checkpoint;
- continue, narrow, distribute, or escalate based on evidence;
- do not automatically create a new roadmap.

## Scenario G — Advanced-system opportunity appears

Expected behavior:

- identify real project/learning question;
- check core health and prerequisites;
- compare with simpler baseline;
- authorize bounded A1/A2 only when justified;
- allow explicit reject/defer evidence.

## Pass condition

Each scenario has a small, predictable update set and preserves the intended learning safeguards.

---

## 9. File-by-file modification register

The exact edits must be based on the latest file contents at execution time. The following register defines expected treatment.

### Canonical Career repository

| File | Expected treatment |
|---|---|
| `README.md` | Reduce transient state; retain navigation and coarse program status |
| `AGENTS.md` | Remove live milestone/method/session details; retain stable agent rules and state routing |
| `UpgradePilot.md` | Preserve mission/product contract; remove active-next-artifact/session language or label completed historical activation clearly |
| `governance/UPGRADEPILOT_LEARNING_AND_EXECUTION_CONTRACT.md` | Consolidate execution rules; add proportional modes, decision/execution distinction, assistance fading, evidence quality |
| `governance/UPGRADEPILOT_LEARNING_PREFERENCES.md` | Keep presentation preferences; remove duplicated mandatory execution and assessment rules where contract/spec owns them |
| `governance/90_DAY_EXECUTION_CONTRACT.md` | Remove session-level state; add cognitive stop; retain workload/capacity/review rules |
| `governance/SESSION_AND_BLOCKER_PROTOCOL.md` | Replace single heavy protocol with lightweight/standard/formal modes; remove active project state |
| `strategy/LEARNING_AND_PROJECT_DESIGN_PROFILE.md` | Preserve evidence/hypotheses; avoid duplicating operational mandates already owned elsewhere |
| `strategy/UPGRADEPILOT_CAPABILITY_AND_PREREQUISITE_SPECIFICATION.md` | Add atomic capability evidence, delayed/transfer requirements, ownership vector relationship, prerequisite checkpoint refinement |
| `strategy/STRATEGY_AND_SCOPE.md` | Remove exact current session state; retain stable strategy and priorities; align advanced-system policy |
| `strategy/ADVANCED_SYSTEMS_EXPOSURE_AND_ADOPTION_POLICY.md` | Replace six mandatory A1/two mandatory A2 target with A0 breadth plus selected A1/A2 depth and negative decisions |
| `plans/UPGRADEPILOT_90_DAY_MASTER_ROADMAP.md` | Preserve route; remove stale live activation; rebalance advanced exposure capacity and gates |
| `plans/UPGRADEPILOT_STAGED_MILESTONE_PLAN.md` | Preserve milestone requirements; avoid acting as live tracker; align advanced exposure targets |
| `plans/UPGRADEPILOT_M2_S01_TECHNICAL_CONTRACT_AMENDMENT.md` | Separate normative gate from result state; remove duplicate exact continuation if tracker owns it |
| `tracking/UPGRADEPILOT_EVIDENCE_AND_PROGRESS_TRACKER.md` | Become clear canonical current-state owner; adopt refined capability/ownership evidence without becoming a transcript |
| Other project-selection/strategy inputs | Review for direct contradictions and duplicated live state; change only when necessary |

### UpgradePilot repository

| File | Expected treatment |
|---|---|
| `README.md` | Reduce current-state dashboard and duplicated contract details; retain product orientation and links |
| `AGENTS.md` | Remove transient M2/session wording; retain stable repository, safety, authority, and state lookup rules |
| `MEMORY.md` | Convert to concise continuation pointer |
| current working-memory file(s) | Clarify session-evidence role; do not rewrite historical reasoning unnecessarily |
| `docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md` | Add normative keywords, requirement IDs, proof mapping, framework boundary, semantic-order clarity |
| `docs/architecture/README.md` | Keep concise ADR navigation and decision status |
| `docs/architecture/ADR-0002-pydantic-runtime-contract-models.md` | Review boundary; preserve accepted decision; remove only duplicated specification material if appropriate |
| other ADRs | Review for consistent status, scope, consequence, and reassessment structure |
| `docs/program/SOURCE.md` | Define point-in-time snapshot and bounded refresh policy |
| `docs/program/career/**` | Refresh once after canonical Career refactor is complete |
| optional consistency/snapshot script | Add only if low-cost and clearly useful |
| this temporary plan | Delete after final acceptance |

---

## 10. Commit and execution strategy

The refactor must not be performed as one opaque mass rewrite.

Recommended commit sequence:

1. **Career: clarify document responsibilities and remove transient state**
2. **Career: simplify session execution and add assistance fading**
3. **Career: strengthen capability/ownership evidence**
4. **Career: rebalance advanced-system exposure and roadmap implications**
5. **UpgradePilot: refine specification/ADR boundaries and requirement traceability**
6. **UpgradePilot: simplify README, AGENTS, MEMORY, and working-memory roles**
7. **UpgradePilot: establish snapshot refresh policy and perform one final Career snapshot refresh**
8. **Validation: run responsibility, link, duplication, and scenario checks**
9. **Cleanup: delete this temporary plan**

Each commit must state:

- responsibility corrected;
- files changed;
- substantive rules preserved;
- rules intentionally changed;
- state moved or removed;
- validation performed.

Do not refresh the Career snapshot after every canonical Career commit. Refresh once from the final reviewed canonical commit.

---

## 11. Review method for every proposed edit

Before changing a section, answer:

1. What responsibility does this section currently serve?
2. Is that responsibility appropriate for this file?
3. Is the content stable or transient?
4. Does another file already own the rule/fact?
5. Would removing it weaken safety, learning, evidence, or continuity?
6. Can it be replaced by a link or shorter boundary statement?
7. What future event would force this section to change again?
8. Is that future change appropriate for this file?
9. Does the edit increase or decrease AI control over Ali?
10. Does it improve real evidence or merely reduce visible ceremony?

No change should be made solely to shorten a file. The goal is responsibility clarity and lower change amplification.

---

## 12. Validation checklist

### Authority and responsibility

- [ ] Every file has a clear responsibility boundary.
- [ ] There is one canonical current-state owner.
- [ ] There is one canonical capability-evidence owner.
- [ ] Technical requirements and implementation decisions are separated.
- [ ] Session evidence is not treated as state authority.

### Transient state

- [ ] Exact next action is absent from stable governance files.
- [ ] Exact current method/session state is absent from `AGENTS.md`.
- [ ] README files do not function as duplicate trackers.
- [ ] Plans define gates rather than repeatedly recording live results.

### Learning and ownership

- [ ] Lightweight, standard, and formal execution modes exist.
- [ ] Decision, bounded exploration, execution, and tangent modes are distinct.
- [ ] AI-assistance fading is explicit.
- [ ] D3/D4 require changed-case, delayed, failure, and low-assistance evidence where appropriate.
- [ ] Ownership is recorded by dimension for central responsibilities.
- [ ] Immediate repetition alone cannot establish strong capability.

### Workload and prerequisites

- [ ] The 90-minute prerequisite rule is a review checkpoint.
- [ ] Command explanation is adaptive.
- [ ] Governance planning, technical decision records, and execution sketches are distinct.
- [ ] A cognitive stop rule prevents low-quality hour filling.

### Advanced systems

- [ ] All-six A0 orientation is preserved.
- [ ] A1/A2 selection is evidence-dependent.
- [ ] At least one credible A2 pilot remains targeted.
- [ ] Negative adoption decisions count as valid evidence.
- [ ] Core depth and ownership gates protect against checklist expansion.

### Technical specification

- [ ] MUST/SHOULD/MAY terminology is defined.
- [ ] Important requirements have stable IDs.
- [ ] Proof obligations map to tests/evidence categories.
- [ ] Pydantic mechanics primarily belong to ADR-0002.
- [ ] Raw preservation, normalization, type validation, semantic validation, and trusted-object creation are clearly ordered.

### Snapshot

- [ ] Snapshot is explicitly point-in-time.
- [ ] Refresh triggers are bounded.
- [ ] One final canonical Career commit is used.
- [ ] Mirrored files match the selected canonical content.
- [ ] SOURCE records the final refresh once.

### Change amplification

- [ ] A future ADR does not require README/AGENTS/roadmap/session-plan rewrites by default.
- [ ] A test result changes only evidence/state files that genuinely need it.
- [ ] A milestone transition remains allowed to have higher ceremony.

---

## 13. Final acceptance gate

The modification program passes only when all of the following are demonstrated:

1. The strong original learning principles remain present and authoritative.
2. Stable and transient information are structurally separated.
3. The accepted Pydantic decision remains accurately represented.
4. No capability or implementation claim is inflated.
5. AI control is explicitly designed to decrease with demonstrated ability.
6. Ownership evidence becomes harder to satisfy performatively.
7. Small work can use lightweight execution.
8. Consequential decisions can still compare alternatives.
9. Advanced-system exposure is broad at orientation level and selective at hands-on/integrated depth.
10. Technical requirements can be traced to proof without duplicating framework mechanics.
11. The Career snapshot no longer requires routine per-session synchronization.
12. The change-amplification scenarios pass.
13. Canonical Career and UpgradePilot-local controls are internally coherent.
14. All links and navigation are valid.
15. This temporary plan is no longer needed.

---

## 14. Removal procedure

After the final acceptance gate passes:

1. Record the final canonical Career commit used for the snapshot.
2. Record the final UpgradePilot refactor commit(s).
3. Confirm that no remaining file links to this temporary plan as a permanent authority.
4. Delete `TEMP_SPECIFICATION_SYSTEM_REFACTOR_PLAN.md`.
5. Commit the deletion with a message such as:

```text
Remove completed specification refactor plan
```

The deletion is part of the planned work, not optional cleanup.

---

## 15. Exact next action for this refactor

Begin **Phase 0 — Freeze scope and inventory responsibility**.

Do not modify all files immediately. First produce the file-by-file responsibility and duplication map from the latest canonical Career and UpgradePilot contents, then apply the phases in order.