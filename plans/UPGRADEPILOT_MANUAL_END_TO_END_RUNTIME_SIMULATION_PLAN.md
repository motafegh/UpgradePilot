# UpgradePilot Manual End-to-End Runtime Simulation Plan

**Status:** Current controlling product-discovery plan  
**Owner:** Ali Rajabi  
**Project position:** Bounded M2 interruption before resuming M2-S03  
**Workspace:** [`../product-simulation/`](../product-simulation/)  
**Implementation status:** Documentation and manual investigation only; no product implementation is authorized by this plan

## 1. Decision and outcome

Before implementing more of UpgradePilot, Ali and the AI assistant will manually perform the complete work that the intended product would perform for real public Python dependency-update cases.

The work begins from a real dependency-update trigger and continues through case identification, evidence discovery, investigation, uncertainty handling, reasoning, decision support, reporting, and the maintainer-facing result.

The required outcome is an evidence-derived operating model of the whole product runtime:

```text
real dependency-update event
→ invocation and case identity
→ evidence discovery and acquisition
→ raw evidence preservation
→ interpretation and investigation
→ repository-specific relevance analysis
→ checks, comparison, and corroboration where useful
→ missing/conflicting/uncertain evidence handling
→ bounded recommendation or abstention
→ human-readable and machine-consumable result
→ maintainer interaction and possible follow-up
```

This work discovers and validates complete product behavior. It does not design or implement the complete technical system upfront.

## 2. Problem being corrected

Incremental implementation without a concrete end-to-end product model can create locally reasonable but globally irrelevant work.

The demonstrated failure pattern is:

```text
unclear whole-product responsibility
→ narrow milestone task
→ method selected around the local task
→ extensive implementation and testing
→ late discovery that the task, threat, input, or control was misunderstood
```

The M2-S02 release-note extraction work produced useful evidence, but it also exposed missing shared answers to foundational questions:

- what exactly starts an UpgradePilot run;
- which data is supplied initially and which evidence is acquired later;
- who or what originates each item;
- what question each item can answer;
- what authority each observation or derived claim may receive;
- what happens when an item is missing, wrong, stale, ambiguous, adversarial, or irrelevant;
- what complete investigation the product performs;
- what the maintainer sees and can do;
- which responsibilities are essential, optional, deferred, or outside the product.

This plan corrects that gap through real manual execution rather than speculative architecture.

## 3. Relationship to existing project authority

The stable mission, user, supported decision, frozen product boundary, evidence doctrine, admission rules, and claim limits remain controlled by [`../PROJECT_CHARTER.md`](../PROJECT_CHARTER.md).

The 90-day route and milestone gates remain controlled by [`UPGRADEPILOT_90_DAY_PLAN.md`](UPGRADEPILOT_90_DAY_PLAN.md).

This plan temporarily owns the current bounded responsibility because the whole-product operating model must be clarified before M2-S03 implementation continues.

M2-S03 is paused, not rejected. Its implementation plan remains evidence to be evaluated against the manual runtime findings.

Where a manual case exposes a conflict with a stable project control:

1. preserve the observation and reasoning;
2. identify the practical consequence;
3. determine whether the conflict is real or only a misunderstanding;
4. propose the smallest correction;
5. change the owning project artifact only through a separate explicit decision.

A scenario result does not silently rewrite the charter, milestone route, specification, ADR, or implementation.

## 4. Core working principle

Use both of these principles together:

> Maintain a concrete, complete model of the intended product runtime.

> Implement the product incrementally and admit methods only when evidence justifies them.

Therefore:

- the whole runtime may be investigated now;
- any relevant evidence source, method, tool, analysis, or user interaction may be considered;
- no current milestone, existing module, previous method, or current implementation limits what may be discovered;
- discovery does not automatically authorize implementation or permanent architecture;
- a complete conceptual model is required, but a complete speculative technical design is not.

## 5. Open-world and non-exhaustive rule

Every list in this plan is a starting aid, not a closed taxonomy or hardcoded product boundary.

This applies to:

- actors;
- invocation inputs;
- acquired evidence;
- investigation stages;
- questions;
- failure modes;
- evidence states;
- candidate methods;
- diagrams;
- outputs;
- decision outcomes;
- scenario dimensions;
- completion evidence.

A real case may reveal that an item must be added, split, merged, renamed, reordered, removed, or treated differently.

No scenario may be forced into the current document structure when doing so would hide a real responsibility or distinction. The structure must adapt to the product evidence, not the reverse.

The project remains subject to safety, legal, privacy, credential, cost, and platform constraints. Within those constraints, method exploration is not limited by the current milestone's implementation prohibitions. A method may be investigated manually without being admitted into the supported product.

## 6. Scope

This plan covers the intended runtime from the first externally meaningful event through the maintainer-facing result and relevant follow-up.

It includes discovery of:

- triggering events and actors;
- invocation data and identity requirements;
- evidence producers and acquisition paths;
- raw and normalized information;
- evidence provenance, timing, and revision context;
- observations, claims, interpretations, findings, and decisions;
- target-repository context and dependency relevance;
- missing, inaccessible, stale, invalid, conflicting, rejected, unsupported, ambiguous, and not-applicable conditions where encountered;
- manual investigation questions and reasoning;
- candidate automation methods and their limits;
- user interactions, review points, and follow-up actions;
- human-readable and machine-consumable outputs;
- full data flow, evidence lineage, state transitions, and user flow;
- product responsibilities that are necessary, optional, conditional, or outside scope;
- implications for later specifications, architecture, milestones, implementation, tests, and evaluation.

The manual simulation may use lawful public information, local reasoning, public tools, model assistance, deterministic analysis, repository inspection, package inspection, test evidence, CI evidence, security information, or other relevant methods.

## 7. Explicit exclusions during this plan

Do not perform the following as part of the current responsibility:

- implement production or experimental product code;
- add runtime dependencies, services, databases, queues, agents, models, or infrastructure to the supported application;
- select permanent architecture merely because a method was useful manually;
- write exact implementation APIs, classes, schemas, package layouts, or database designs;
- treat an illustrative field list as a frozen contract;
- create a separate plan for every scenario;
- create empty placeholder artifacts before they have real content;
- rewrite stable project controls after each individual discovery;
- claim that ten cases or any finite set proves universal product completeness;
- force an outcome when evidence supports only uncertainty or abstention.

Illustrative machine-readable structures may be used to clarify information needs, but they are not implementation schemas unless later admitted through the proper specification process.

## 8. Workspace and artifact ownership

The working area is [`../product-simulation/`](../product-simulation/).

The initial durable files are:

- `product-simulation/README.md` — workspace orientation and navigation;
- `product-simulation/SCENARIO_EXECUTION_TEMPLATE.md` — minimum complete structure for one manual run;
- `product-simulation/SCENARIO_COVERAGE.md` — evolving coverage and case register.

Create additional artifacts only when real scenario evidence makes them useful. Expected later artifacts may include:

- `product-simulation/scenarios/<case-id>/CASE.md` — one complete manual execution record per case;
- `product-simulation/SYSTEM_OPERATING_MODEL.md` — cross-case runtime stages, actors, responsibilities, states, and boundaries;
- `product-simulation/INPUT_AND_EVIDENCE_CATALOG.md` — evidence-derived catalogue of inputs, origins, purposes, authority, and failure behavior;
- `product-simulation/DATA_FLOW_AND_USER_FLOW.md` — validated context, runtime, data-flow, evidence-lineage, state, and user-flow diagrams;
- `product-simulation/SYNTHESIS.md` — cross-case findings, conflicts with current plans/specifications, and recommended next implementation responsibility.

These names and separations are not mandatory if a simpler organization proves clearer. Do not split one coherent artifact merely to satisfy this candidate layout.

## 9. Manual system role

For each selected case, Ali and the AI assistant act as the complete UpgradePilot system.

They manually perform every currently believed product responsibility, including work that may later belong to separate modules or milestones.

The simulation must not start from a pre-supplied semantic answer that bypasses the work the future system is expected to perform. Manual human interpretation is allowed because the purpose is to discover the responsibility, but it must be recorded as human interpretation rather than disguised as automatically established fact.

The simulation must preserve distinctions among:

```text
source observation
→ attributed source claim
→ human or tool-derived interpretation
→ corroborated, contradicted, irrelevant, or unresolved finding
→ decision reason
→ bounded recommendation or abstention
```

## 10. Initial runtime model to challenge

The following is an initial hypothesis, not a frozen sequence:

1. a maintainer, update bot, or equivalent event presents a dependency-update change;
2. UpgradePilot identifies the exact repository, pull request or change reference, base state, and proposed state;
3. it determines what dependency relationship and version transition are actually proposed;
4. it discovers and preserves relevant evidence from the pull request, target repository, package ecosystem, upstream project, CI, and other useful sources;
5. it separates raw observations from interpretations and records missing or problematic evidence;
6. it investigates what changed upstream and whether those changes matter to the target repository;
7. it examines available behavioral, compatibility, security, dependency-path, and CI evidence as the case requires;
8. it identifies contradictions, unresolved questions, and evidence limitations;
9. it produces a bounded recommendation or abstention with traceable reasons;
10. it presents a useful result to the maintainer and records any required follow-up.

Every case must challenge this sequence. Stages may be reordered, repeated, skipped, added, or split when reality requires it.

## 11. Input and evidence analysis rule

For every supplied or acquired item, record at least:

1. **Name and practical meaning** — what the item actually represents;
2. **Origin or producer** — who or what created it;
3. **Acquisition path** — how UpgradePilot receives or obtains it;
4. **Identity and time context** — which repository, revision, release, run, or timestamp it belongs to;
5. **Purpose** — which investigation question it can help answer;
6. **Authority and limits** — what it may support and what it cannot establish alone;
7. **Failure behavior** — consequences of absence, inaccessibility, staleness, invalidity, ambiguity, contradiction, or manipulation;
8. **Downstream use** — which later reasoning, finding, decision, or report statement consumes it;
9. **Optionality** — whether the complete investigation requires it always, conditionally, or only in some cases;
10. **Replacement or corroboration** — whether another source can compensate for it.

These fields are minimum prompts, not a closed schema.

The simulation must distinguish:

- **invocation inputs:** data supplied when a run begins;
- **discovered identifiers:** data learned while resolving the case;
- **acquired evidence:** observations collected during investigation;
- **derived interpretations:** meaning assigned by a human, model, parser, or other transformation;
- **findings:** case-level conclusions supported by one or more evidence items;
- **decision inputs:** findings and limitations permitted to affect the recommendation;
- **outputs:** records and reports delivered to people or other systems.

## 12. Per-scenario execution procedure

Use the scenario template, adapting it where the case requires.

### Step 1 — Select and justify the real case

Record:

- public repository and update event;
- why the case is real and reproducible enough to study;
- which product uncertainty or coverage dimension motivated selection;
- known access, legal, timing, or reproducibility limits.

### Step 2 — Freeze the investigated case identity

Identify the exact change as precisely as the public evidence permits. Do not mix evidence from different revisions or later states without labeling the difference.

### Step 3 — Record the starting invocation

State what UpgradePilot would receive at runtime and what is not yet known.

Do not assume that everything visible in a browser is an invocation input. Separate supplied data from evidence the system would need to acquire.

### Step 4 — Map actors and sources

Identify every actor or system that produces, transmits, transforms, stores, or consumes material information in this case.

Add actors not anticipated by the current plan when they materially affect the flow.

### Step 5 — Define investigation questions

Before gathering everything available, state the questions that matter to the maintainer decision.

Questions may be added or removed as evidence changes the case.

### Step 6 — Acquire and preserve evidence manually

Collect only lawful and relevant public evidence. Preserve source identity, revision/time context, and transformation notes.

Do not interpret collection success as truth or relevance.

### Step 7 — Perform the investigation

For each question:

- inspect the relevant evidence;
- record direct observations;
- record interpretations separately;
- explain reasoning and alternatives;
- identify uncertainty and contradictions;
- perform useful comparisons or checks;
- stop methods that do not materially improve the decision.

### Step 8 — Test failure and changed-evidence behavior

Where practical, ask what changes if a material input or evidence item is missing, stale, contradictory, invalid, or different.

Do not manufacture arbitrary variants merely to complete a checklist. Use variants that reveal real product behavior.

### Step 9 — Construct the full product result manually

Produce:

- exact case identity;
- evidence inventory and lineage;
- findings and supporting evidence;
- unresolved questions and limitations;
- bounded recommendation or abstention;
- reasons and suggested next actions;
- human-facing report;
- conceptual machine-consumable result;
- user interaction or follow-up required.

### Step 10 — Evaluate candidate methods

For each manually performed responsibility that may later be automated, record credible candidate methods without prematurely selecting one.

### Step 11 — Update shared product understanding

Record which actor, input, stage, state, output, flow, responsibility, or assumption should be added, changed, removed, or left unresolved in the cross-case operating model.

### Step 12 — Stop the case

Stop when additional work no longer changes the product understanding, decision, material limitation, or method assessment enough to justify its cost.

A scenario does not need every possible source or technique to be complete.

## 13. Scenario selection strategy

Use at least ten substantially different real dependency-update cases before final synthesis.

Ten is a minimum discovery set, not a maximum, universal proof threshold, or fixed corpus size. Continue beyond ten when meaningful product uncertainty or uncovered behavior remains.

Select cases progressively rather than fixing all cases upfront.

The initial cases should first establish and challenge the normal end-to-end flow. Later cases should deliberately cover meaningful differences discovered from earlier work.

Potential diversity dimensions include, but are not limited to:

- patch, minor, major, pre-release, yanked, or replacement updates;
- direct, transitive, optional, development, test, build, or runtime dependencies;
- manifest-only, lockfile-only, or broader source changes;
- complete, missing, fragmented, ambiguous, or conflicting upstream information;
- relevant versus irrelevant upstream compatibility changes;
- changed interpreter, operating-system, architecture, or toolchain support;
- removed, deprecated, renamed, or behaviorally changed APIs;
- passing, failing, unavailable, flaky, skipped, or unrelated CI evidence;
- security-motivated updates and ordinary maintenance updates;
- single-package versus multi-package lockfile effects;
- pure-Python versus native/compiled packages;
- active versus unavailable or migrated upstream projects;
- clear recommendation versus necessary abstention;
- evidence agreement versus cross-source contradiction;
- cases where the product should discover that little or no extra investigation is useful.

The coverage file may add, split, or remove dimensions at any time.

## 14. Investigation questions

The following questions are initial prompts, not mandatory or exhaustive requirements for every case:

- What exact change is proposed?
- What dependency relationship does the target repository actually have?
- What changed between the old and new dependency states?
- Which upstream changes can affect this repository?
- How and where does the repository use the dependency?
- Which runtime, platform, interpreter, build, or tooling constraints matter?
- What relevant tests or checks exist, and what do they actually demonstrate?
- Are observed failures caused by the update, pre-existing, environmental, or unresolved?
- Is there known security information, and what does it establish or fail to establish?
- Which evidence sources corroborate, contradict, or fail to address each material claim?
- What evidence is missing, inaccessible, stale, ambiguous, or irrelevant?
- What action can be justified without overstating certainty?
- What should the maintainer inspect or run next?
- What should UpgradePilot explicitly refuse to conclude?

A case may require entirely different questions.

## 15. Candidate method analysis

For each investigation responsibility, record:

- the question being answered;
- the manual method used in the scenario;
- candidate automation methods;
- required inputs and preconditions;
- strengths and useful operating range;
- failure modes and blind spots;
- security, privacy, cost, latency, maintenance, and upgrade burden where relevant;
- what the result may legitimately establish;
- how errors could affect downstream decisions;
- whether unresolved/null output is acceptable;
- simplest credible baseline;
- evidence required before future adoption.

Candidate methods may include deterministic code, metadata parsing, repository analysis, static analysis, dynamic checks, test execution, search, retrieval, LLM assistance, learned models, human review, cross-source corroboration, or other techniques.

This list is open. A method is recorded because a scenario exposes a need, not because the technology is interesting.

Method status during this plan is limited to:

- observed manual method;
- plausible candidate;
- unsuitable for the observed responsibility;
- requires later experiment;
- unresolved.

No method becomes supported product architecture through this plan alone.

## 16. User and output analysis

For every case, determine:

- who initiates the run;
- what the user must supply;
- what the product can discover itself;
- when the user may need to clarify, authorize, inspect, or choose;
- what the user needs to understand the result;
- what action the result supports;
- what the product should do after user action or new evidence;
- whether rerun, replay, comparison, or history is useful.

Candidate output families include, but are not limited to:

- preserved case record;
- evidence inventory;
- findings and contradictions;
- limitations and unresolved questions;
- bounded recommendation or abstention;
- targeted next checks;
- human-readable report;
- machine-consumable result;
- comparison or change record;
- follow-up state.

The scenario evidence determines the actual output model. Do not freeze names or outcome vocabulary prematurely.

## 17. Data-flow and diagram development

Develop diagrams progressively from observed cases. Use text or Mermaid unless another representation materially improves understanding.

Candidate diagrams include:

1. **System context diagram** — UpgradePilot, maintainers, update producers, GitHub, target repositories, package indexes, upstream projects, CI, advisory sources, and newly discovered actors;
2. **End-to-end runtime flow** — sequence from trigger to user result and follow-up;
3. **Data-flow diagram** — producers, boundaries, transformations, preserved records, and consumers;
4. **Evidence-lineage diagram** — observation to attributed claim to interpretation to finding to decision reason to output;
5. **User flow** — supplied information, review points, questions, results, and actions;
6. **State-transition diagram** — case states and transitions revealed by the scenarios;
7. **Failure and degradation flow** — behavior when sources, evidence, methods, or checks fail.

These diagrams are not mandatory as separate files and are not closed categories. Create or revise a diagram only when it resolves a real ambiguity or captures a stable cross-case pattern.

## 18. Cross-scenario synthesis

After each case, update only the shared artifacts materially affected by its evidence.

Periodically synthesize:

- stable runtime stages;
- conditional and optional branches;
- actors and trust boundaries;
- invocation inputs versus acquired evidence;
- evidence kinds, authority, and lineage;
- product questions and responsibilities;
- user interactions and outputs;
- failure, degradation, and abstention behavior;
- candidate methods and unresolved choices;
- responsibilities that should be inside or outside UpgradePilot;
- implications for current milestones and specifications;
- gaps in the scenario set.

The final synthesis must distinguish:

- repeated cross-case evidence;
- one-case observations;
- hypotheses;
- unresolved questions;
- recommendations;
- decisions that still require Ali's approval.

## 19. Quality and realism criteria

A scenario is useful only when it:

- uses a real public dependency-update event or a clearly justified real-world equivalent;
- identifies the exact case and time/revision context as far as possible;
- distinguishes supplied input from acquired evidence;
- identifies the origin and purpose of material data;
- separates observation, interpretation, finding, and decision;
- explains why each investigation step matters;
- preserves missing and contradictory evidence;
- produces a full maintainer-facing result rather than stopping at one evidence item;
- records genuine limits and unresolved questions;
- identifies what the case changed in the product model;
- avoids conclusions unsupported by the available evidence.

A scenario is not made useful by length, number of sources, number of tools, or technical complexity.

## 20. Anti-hardcoding and anti-overfitting rules

- Do not define the product around the first case, one package, one repository, one sentence, one evidence type, or one decision outcome.
- Do not treat the current list of inputs or stages as complete.
- Do not choose cases only because they fit the existing implementation.
- Do not force every case through identical questions when the real decision differs.
- Do not add a new permanent product rule for every new example.
- Do not infer broad capability from one successful manual investigation.
- Use repeated and contrasting cases to determine whether a responsibility is stable, conditional, or case-specific.
- Preserve exceptions and counterexamples rather than editing the model until they disappear.
- Prefer an explicit unresolved state over a fabricated universal rule.

## 21. Anti-ceremony rules

- One controlling plan governs the complete simulation effort.
- Use one coherent `CASE.md` per scenario unless evidence volume genuinely requires separation.
- Do not create empty directories or placeholder documents.
- Do not create a separate approval, checklist, or retrospective file for ordinary scenario work.
- Do not duplicate complete scenario evidence into shared synthesis files.
- Link to case evidence instead of copying it.
- Update diagrams only when the operating model changes.
- Stop collecting evidence when additional work does not change the decision or product understanding materially.
- Remove or simplify artifacts that stop providing value.
- Keep the workspace a discovery system, not a second project-management system.

## 22. Relationship to M2-S03 and later implementation

M2-S03 remains paused while this plan is current.

After sufficient cross-case evidence exists:

1. map the validated operating model to the 90-day milestones;
2. identify which parts of M2-S03 remain correct;
3. identify contradictions, missing responsibilities, and premature constraints;
4. decide the smallest corrected implementation slice;
5. update only the owning plans or specifications that materially changed;
6. resume implementation through a separately authorized current plan.

The manual simulation may show that:

- M2-S03 is correct with minor wording changes;
- its input, output, or decision assumptions need correction;
- some responsibilities belong in later milestones;
- a previously deferred responsibility blocks a credible vertical slice;
- a proposed method is unnecessary;
- a new experiment is justified;
- the product boundary needs explicit reconsideration.

No conclusion is predetermined.

## 23. Completion condition

This responsibility is complete only when Ali reviews the evidence and the following are true:

- at least ten materially different real cases have been manually executed end to end;
- additional cases have been added where major uncertainty or uncovered behavior remained;
- the full runtime operating model is understandable and grounded in case evidence;
- invocation inputs, acquired evidence, origins, purposes, authority, and failure behavior are documented at the useful current depth;
- data flow, evidence lineage, user flow, state behavior, and major failure paths are represented clearly;
- output and recommendation responsibilities are concrete without pretending to be final implementation schemas;
- candidate methods are tied to observed responsibilities and limitations;
- conflicts with current plans/specifications are explicit;
- unresolved product questions remain visible;
- Ali can explain the end-to-end product, challenge its stages, and reason through changed-evidence cases;
- one explicit decision identifies the next implementation responsibility.

The minimum case count does not override evidence. Do not stop merely because ten cases exist, and do not continue merely to accumulate a larger number.

## 24. Stop lines

Stop and discuss before:

- changing the stable mission, user, supported decision, or frozen product boundary;
- admitting a permanent technology or architecture;
- resuming implementation;
- treating a manual method as validated automation;
- converting illustrative structures into binding schemas;
- making claims about product safety, completeness, or production readiness;
- using private, restricted, credential-sensitive, paid, or legally uncertain evidence;
- taking any external mutating action.

## 25. Immediate authorized action

Select the first foundational real public dependency-update case.

Create its record from [`../product-simulation/SCENARIO_EXECUTION_TEMPLATE.md`](../product-simulation/SCENARIO_EXECUTION_TEMPLATE.md), then manually execute the full runtime from trigger and case identity through final maintainer report and retrospective.

Do not implement product code during that case.