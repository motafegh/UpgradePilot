# UpgradePilot Capability and Prerequisite Specification

**Owner:** Ali Rajabi  
**Status:** Approved and controlling capability-control artifact  
**Responsibility:** Capability taxonomy, prerequisites, D0–D5 depth, evidence requirements, readiness, deferral, and claim limits  
**Live state:** The canonical tracker records current capability evidence. This specification does not record the active session, exact next action, or current implementation state.

## 1. Purpose and boundary

This document specifies the capabilities needed to build and own UpgradePilot, when they become necessary, how prerequisite gaps are handled, and what evidence may justify a capability claim.

It does not redefine:

- the UpgradePilot mission, user, supported decision, or product boundary;
- Day-90 strategy, capacity, advanced-systems targets, or completion requirements;
- roadmap or milestone order;
- technical architecture or selected implementation methods;
- current progress.

It is not a generic curriculum, technology catalogue, course list, roadmap, milestone plan, session plan, architecture, or authorization to implement.

The governing rule is:

> Learn the smallest safe prerequisite before it blocks real work; deepen it through live UpgradePilot responsibilities; increase recorded capability only from preserved evidence at the required assistance and transfer level.

## 2. Assessment principles

1. Record what Ali can demonstrate, not what was mentioned, explained, generated, or successfully run.
2. Assess a **specific responsibility**, not an undifferentiated topic.
3. Keep exposure, guided performance, independent bounded performance, ownership, and advanced independent capability distinct.
4. Record assistance and ownership dimensions explicitly.
5. Require transfer, failure, delayed, and low-assistance evidence for higher depth where the responsibility supports it.
6. Do not average mixed sub-capabilities into an optimistic broad label.
7. Preserve limitations and contexts in every claim.
8. Repository sophistication, documentation volume, passing AI-generated tests, and successful command execution do not establish ownership by themselves.
9. Advanced-systems A-level exposure labels remain governed by the approved Advanced Systems Policy and do not substitute for D-level capability evidence.

## 3. Capability-depth model

| Depth | Controlled meaning |
|---|---|
| **D0 — Unassessed** | Reliable ability has not been established. Mentioning, reading, watching, discussing, or seeing generated work is not evidence. |
| **D1 — Introduced** | Ali recognizes the full term, practical purpose, principal responsibility, and relationship to UpgradePilot after teaching. |
| **D2 — Guided application** | Ali performs a bounded UpgradePilot-relevant task with substantial explanation, examples, prompts, or correction and interprets representative evidence correctly. |
| **D3 — Independent bounded application** | Ali performs a representative bounded responsibility with limited assistance, selects meaningful actions, handles changed cases, and diagnoses common relevant failures. |
| **D4 — Technical ownership** | Ali can design or challenge the responsibility, implement/materially modify it, test it, diagnose unfamiliar failures, explain trade-offs/system effects, and reproduce it with low assistance across relevant contexts. |
| **D5 — Advanced independent capability** | Ali repeatedly designs, operates, diagnoses, and evolves the responsibility across materially different contexts and substantial trade-offs with low assistance and explicit recognition of limitations. |

D5 is not required for the core during this 90-day project. D4 is reserved for genuinely central responsibilities. D2 or D3 may be an honest Day-90 result for bounded experiments or advanced exposure.

## 4. Evidence requirements by depth

### D0

No reliable evidence or evidence is too indirect, stale, broad, or assistance-dependent to support a claim.

### D1

Require:

- accurate recognition of the term/responsibility;
- own-words practical meaning;
- relationship to the current product flow;
- one basic boundary or failure distinction.

Immediate teaching may support D1 when the explanation is genuinely Ali's rather than copied wording.

### D2

Require:

- guided application to a real or representative case;
- correct interpretation of output/evidence;
- explicit assistance;
- one bounded check, modification, query, or test where applicable;
- a narrow transfer limit.

### D3

Require, where the responsibility supports it:

- a representative project case;
- one changed case or variant;
- one action, test, query, or diagnostic check selected with limited prompting;
- one relevant failure diagnosis or repair;
- one ownership-bearing implementation/test/evidence change;
- one delayed recall or reconstruction check;
- limited rather than central AI decomposition;
- an explicit context and transfer limit.

A single immediate guided success cannot establish D3.

### D4

Require:

- repeated evidence across sessions;
- changed-context transfer;
- design, challenge, or consequential decision participation;
- implementation/material modification ownership;
- test design or repair ownership;
- diagnosis of at least one unfamiliar failure;
- explanation of system-wide consequences and trade-offs;
- low-assistance reproduction or reconstruction;
- explicit limitations and boundary conditions.

### D5

Require sustained independent performance across materially different contexts, unfamiliar failures, substantial design trade-offs, and operational consequences.

## 5. Atomic capability records

Every capability claim must use a record shaped like:

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
Reassessment trigger:
```

Example:

```text
Capability family: Python testing
Specific responsibility: Diagnose and repair strict Pydantic validation unit tests
Depth: D2 guided
Context: InitialCaseRecord boundary models
Transfer limit: Does not establish integration-test design or broad pytest ownership
```

A broad family name such as “Python,” “testing,” “security,” or “data engineering” cannot receive a depth without specific bounded responsibility records underneath it.

## 6. Ownership vector

For central work, record ownership separately for:

- **problem understanding** — who identified and correctly framed the responsibility;
- **design** — who compared and selected the structure or method;
- **implementation** — who wrote or materially changed behavior;
- **testing** — who designed, wrote, repaired, and interpreted tests;
- **operation** — who executed and interpreted real behavior;
- **diagnosis** — who localized and repaired failures;
- **explanation** — who can explain boundaries, trade-offs, and system effects;
- **reproduction** — who can reconstruct or repeat central behavior with reduced prompting.

The overall claim must not exceed the weakest dimension required by the claimed responsibility.

Do not assign one optimistic ownership label to an artifact with mixed dimensions.

## 7. Assistance labels

Use:

- **AI-generated** — AI produced substantive artifact, implementation, or central reasoning;
- **AI-assisted** — Ali performed meaningful work with substantial AI explanation/generation/repair;
- **Ali-directed** — Ali materially defined the responsibility, constraints, approach, or decision;
- **Ali-verified** — Ali independently checked behavior/evidence and correctly stated proof and limits;
- **Ali-owned** — evidence supports explanation, modification, testing, diagnosis, and reduced-prompt reproduction at the stated scope.

These labels describe participation. D-level depth additionally requires the evidence conditions in this specification.

## 8. Performative-check prohibition

The following alone cannot establish strong ownership or D3+ capability:

- repeating an explanation immediately after AI;
- typing an AI-provided change;
- approving an AI-selected design;
- running a command successfully;
- passing AI-generated tests;
- producing one guided artifact;
- recognizing terminology;
- reading source and agreeing with its behavior;
- repository size or architectural sophistication.

Use these as partial evidence only when combined with the required reasoning, transfer, failure, and low-assistance evidence.

## 9. Confidence, freshness, and breadth

Do not make one confidence value carry several meanings.

Record separately:

- **confidence:** quality and directness of evidence;
- **freshness:** when it was last demonstrated;
- **breadth:** number and difference of relevant contexts;
- **assistance:** how much external decomposition/guidance was required;
- **transfer limit:** what the evidence does not establish.

Suggested confidence values: `High | Medium | Low`.

A high-confidence D1 claim is still D1. A low-confidence D3 estimate requires reassessment and must not be presented as stable ownership.

## 10. Progressive control transfer

The Learning and Execution Contract controls session behavior. Capability evidence determines how much technical control should transfer.

| Demonstrated depth | Expected learner control |
|---|---|
| D0–D1 | Understand, predict, question, and challenge AI-proposed decomposition |
| D2 | Select among bounded alternatives and explain the chosen next action |
| D3 | Propose decomposition, tests, evidence, and diagnostic checks |
| D4 | Control technical sequence and evidence plan; use AI mainly for review/challenge |
| D5 | Operate independently and use AI selectively |

If performance does not match the expected control level, narrow the claim or restore only the necessary scaffolding.

## 11. Prerequisite model

Classify encountered material as:

| Class | Meaning | Treatment |
|---|---|---|
| **Required core** | Active responsibility or gate directly depends on it | Teach the minimum complete mechanism and require reasoning/application evidence |
| **Supporting operational** | Needed to perform work but not a target capability | Explain purpose, safe use, key commands, and failure modes |
| **Deferred core** | Important capability owned by a later responsibility | Teach only the accurate operational layer needed now and name the later owner |
| **Optional exploration** | Interesting but not needed for the dependency chain | Defer unless a bounded exploration is explicitly authorized |

When a prerequisite blocks progress:

1. identify the exact missing link;
2. state why it blocks the responsibility;
3. define required depth now and deferred depth;
4. teach/practice the minimum complete mechanism;
5. verify through one meaningful task;
6. return to the original responsibility.

## 12. Prerequisite review checkpoint

The initial 90 focused minutes are a review checkpoint, not an automatic stop or course trigger.

At the checkpoint decide:

1. Can Ali safely continue the responsibility?
2. Is the remaining gap required now?
3. Can the responsibility be narrowed?
4. Should repair continue inside the same package?
5. Should remaining depth develop through later changed cases?
6. Does the gap materially change route scope or sequence?

Formal replanning is required only when scope/sequence is materially affected.

## 13. Diagnostic rules

A small project-embedded diagnostic is appropriate when:

- prior evidence is indirect or assistance-heavy;
- the context is new;
- a higher depth claim is being considered;
- capability is central to the next gate;
- previous evidence is stale or contradictory.

A diagnostic should:

- use a real or representative UpgradePilot responsibility;
- test reasoning or action rather than trivia;
- include clear assistance limits;
- produce a bounded artifact, output, test, query, or diagnosis;
- state what it proves and does not prove;
- avoid becoming a detached course or full-day ceremony.

## 14. Capability families and prerequisite order

The following families remain required by the approved UpgradePilot route. Exact activation is controlled by milestones.

### 14.1 Maintainer and repository workflow

Responsibilities include:

- public repository, commit, branch, pull request, diff, review, and history reasoning;
- Dependabot pull-request context;
- base/head snapshot identity;
- evidence and maintainer decision boundaries.

Prerequisites: basic Git/GitHub concepts before deep repository evidence work.

### 14.2 Python application and packaging

Responsibilities include:

- modules, imports, packages, source layout, application boundaries;
- `pyproject.toml`, dependency declarations, compatible version ranges, editable installation, and import proof;
- exceptions, configuration, and bounded CLI/application entrypoints where authorized.

Prerequisites: basic Python syntax and file/module reasoning before independent package construction.

### 14.3 Data contracts and transformation

Responsibilities include:

- raw versus trusted data;
- source-format parsing, normalization, type validation, semantic validation, and trusted-object creation;
- schema/invariant design;
- explicit failures, non-mutation, immutability, and provenance boundaries.

Prerequisites: Python structures/types and the product's conceptual information contracts.

### 14.4 External evidence acquisition

Responsibilities include:

- HTTP/REST/JSON;
- authentication and credential handling;
- pagination and rate limits;
- retries, backoff, caching, idempotency;
- partial source failure and schema change;
- public-source safety and legality.

Prerequisites: basic network/client-server and data-contract understanding.

### 14.5 Persistence and SQL

Responsibilities include:

- relational modeling;
- keys and relationships;
- reproducible schema setup/migrations;
- queries for traceability, comparison, evaluation, and diagnosis.

Prerequisites: stable data contracts and a demonstrated persistence need.

### 14.6 Testing and debugging

Responsibilities include:

- unit and integration tests;
- valid, invalid, boundary, changed, and non-mutation cases;
- failure localization and discriminating checks;
- reproducibility and regression protection.

Testing is developed continuously, but broader ownership claims require changed-case and failure evidence.

### 14.7 Deterministic decision and evaluation

Responsibilities include:

- explicit rules, heuristics, decision tables, uncertainty, abstention, and evidence sufficiency;
- asymmetric decision costs;
- labels/truth and evaluation design;
- baselines, metrics, error analysis, leakage prevention, and honest claims.

Prerequisites: reliable evidence contracts before evaluation and a measured deterministic baseline before ML adoption.

### 14.8 Secure and reliable engineering

Responsibilities include:

- input validation;
- secrets and credential handling;
- safe external execution boundaries;
- least privilege and trust boundaries;
- explicit degraded/failure behavior;
- reproducible operation, logging, and limitations.

Security is cross-cutting and does not become a mastery claim from conceptual discussion alone.

### 14.9 CI, containers, and operational reproducibility

Responsibilities include:

- automated checks;
- clean-environment reproducibility;
- container/runtime boundaries where justified;
- failure diagnosis and artifact/version identity.

Prerequisites: a working testable application baseline.

### 14.10 ML, graph, LLM, agentic, cloud, distributed, and MLOps systems

These remain governed by the existing approved strategy, advanced-systems exposure/adoption policy, roadmap, capacity, and milestone requirements.

This specification only controls capability evidence:

- exposure level does not establish D-level ownership;
- assisted operation must be labeled accurately;
- D3/D4 require the same transfer, diagnosis, design, and low-assistance evidence as other capabilities;
- professional mastery claims remain prohibited without evidence.

No Day-90 advanced-system target, capacity allocation, completion gate, or adoption requirement is changed by this specification revision.

## 15. Readiness decisions

Use:

- **Ready** — prerequisite depth and evidence are sufficient for the bounded responsibility;
- **Ready with embedded teaching** — small gap can be repaired during active work;
- **Prerequisite repair required** — execution would be unsafe or meaningless without bounded repair;
- **Blocked** — gap or external constraint materially prevents work;
- **Deferred** — capability belongs to a later authorized responsibility;
- **Not applicable** — capability is not required by the active boundary.

Readiness is responsibility-specific. A person may be ready for one narrow task and unready for another task in the same broad family.

## 16. Capability claim language

Prefer:

- introduced;
- guided application;
- independent bounded application;
- technical ownership of `<specific responsibility>`;
- advanced independent capability in `<specific responsibility>`.

Avoid broad claims such as:

- knows Python;
- understands testing;
- owns data engineering;
- production-ready engineer;
- expert;
- advanced systems engineer;

unless atomic evidence genuinely supports the scope.

## 17. Tracker schema relationship

The tracker is the canonical owner of current capability state. It should contain:

- atomic responsibility records;
- current depth;
- assistance;
- ownership dimensions;
- evidence links;
- changed/failure/delayed evidence;
- confidence, freshness, breadth, and transfer limits;
- reassessment trigger.

The tracker should summarize capability-changing conclusions, not copy full session transcripts.

## 18. Maintenance

Change this specification only when capability taxonomy, prerequisite logic, evidence requirements, readiness states, or claim standards change.

Do not add:

- current route or milestone state;
- exact next actions;
- selected technical implementation details owned by ADRs;
- live tracker entries;
- Day-90 strategy/capacity/completion changes without separate explicit authorization.