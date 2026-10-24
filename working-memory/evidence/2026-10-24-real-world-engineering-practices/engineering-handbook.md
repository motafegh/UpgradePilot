# Engineering Handbook — term analysis for UpgradePilot

**Status:** analyzed; decision candidate only  
**Study branch:** `research/real-world-engineering-practices-2026-10-24`  
**Repository horizon checked:** branch base `1781bb6aa70fb0824a2de2271cf7ce6b4052e44b` plus current study branch  
**Parent working memory:** `working-memory/2026-10-24_real-world-engineering-practices_project-fit_cycle.md`

## WHAT

In software organizations, an **Engineering Handbook** (often also called a Developer Handbook or Engineering Playbook/Wiki in looser usage) is a living reference for **how the engineering team works**. It commonly consolidates engineering principles, development workflow, coding/review/testing expectations, delivery/operations practices, decision processes, onboarding guidance, tool conventions and links to deeper authoritative material.

`Technical handbook` is a broader and less precise label. It can mean an engineering handbook, but it may also mean a reference manual about a technology, system or engineering discipline. Therefore, when discussing team/project practice, `Engineering Handbook` is the more precise term.

Public examples inspected for orientation include Atlassian's Engineering Handbook and NASA's Software Engineering and Assurance Handbook. They vary in formality, but both use the handbook as a maintained guidance/reference layer rather than as source-code truth.

## WHY

The main problems a handbook addresses are fragmented institutional knowledge, inconsistent engineering practices, slow onboarding, repeated explanation, process ambiguity, and difficulty discovering the correct deeper policy or technical owner.

A handbook should reduce questions such as:

- How do we normally design, implement, test and review changes?
- What engineering principles guide trade-offs?
- Where is the authoritative rule for security, architecture, releases or incident handling?
- What should a new contributor learn first?
- Which practices are mandatory, recommended, situational or historical?

It should not become a duplicated copy of every specification, runbook, ADR or source comment.

## DISTINCTION FROM NEARBY TERMS

- **Technical/system documentation:** explains the system, APIs, architecture or implementation; handbook mainly explains how engineering work is conducted and where authoritative knowledge lives.
- **Developer/Contributing Guide:** usually narrower: setup, local development and contribution workflow.
- **Runbook:** step-by-step procedure for a repeatable operation or incident.
- **Playbook:** broader guidance for handling a class of situations; often less mechanical than a runbook.
- **ADR:** records one consequential architecture decision and its rationale/trade-offs.
- **Specification:** defines stable required behavior/invariants.
- **README:** usually entry-level product/repository orientation, not the complete engineering operating model.

## PROJECT MAPPING / CURRENT EVIDENCE

UpgradePilot already contains much of the *substance* that an engineering handbook would normally contain, but deliberately distributes it among responsibility-specific owners:

- `AGENTS.md` — repository-wide instruction/operation routing and owner map.
- `OPERATING_GUIDE.md` — controlling project-local engineering/learning working method, communication, proportionality, debugging/evidence interpretation and handoff.
- `PROJECT_CHARTER.md` — mission, user, product boundary, evidence doctrine and technology-admission rules.
- `SECURITY.md` — security/trust/credential/external-action safeguards.
- `ENVIRONMENT.md` — environment/runtime facts and re-check guidance.
- `docs/specifications/` — stable technical behavior and invariants.
- `docs/architecture/` — ADRs for consequential architecture decisions.
- `plans/` — bounded execution/design responsibilities.
- `working-memory/` — dated progression and handoffs.
- `learning/` — durable learning/relearning artifacts.

`OPERATING_GUIDE.md` is the closest single existing artifact to the **how we engineer/work** portion of a conventional Engineering Handbook. Its declared responsibility explicitly covers the project-wide Learning-by-Doing method, communication clarity, context discipline, proportionality, implementation-retention reasoning, debugging, evidence interpretation, completion and handoff. `AGENTS.md` complements it with repository-wide routing and responsibility ownership.

Therefore UpgradePilot does **not** currently suffer from absence of engineering-process documentation. The more realistic issue is that the handbook-like responsibility is **distributed and authority-sensitive**, which is intentional but can increase discovery/onboarding cost.

## FIT / BENEFIT / COST

A conventional monolithic `ENGINEERING_HANDBOOK.md` that repeats the current owners would be harmful: it would create a second authority surface, duplicate rules and become stale as plans/specifications/ADRs evolve.

A **thin handbook/navigation layer** could become useful later if it solves a demonstrated onboarding/discovery problem. Its purpose would be to explain the engineering model and route readers to canonical owners, not duplicate those owners. A possible future shape would include:

1. engineering principles and project engineering philosophy;
2. repository/architecture mental model;
3. normal development lifecycle from idea → design → implementation → verification → release;
4. testing/evidence philosophy;
5. security and trust model pointers;
6. documentation/decision artifact taxonomy;
7. setup/contribution/release/incident pointers where applicable;
8. concise owner/index map to the actual canonical files.

This would be especially valuable if UpgradePilot gains external contributors or is used as a portfolio artifact where a professional engineer needs to understand **how the project is engineered** without first learning the complete project-specific governance vocabulary.

## TRIGGER / REJECTION CONDITION

Consider a formal Engineering Handbook only if one or more of these become observable:

- new contributors repeatedly cannot find the correct engineering guidance;
- the repository's artifact taxonomy materially slows onboarding;
- the same cross-cutting engineering principles are repeatedly re-explained in multiple files;
- external portfolio/reviewer use needs a concise professional engineering entry point;
- collaboration grows enough that shared team practice needs a human-facing stable navigation surface.

Reject or narrow the idea if the proposed handbook mostly copies `AGENTS.md`, `OPERATING_GUIDE.md`, Charter/specifications/ADRs/plans, or becomes another live-state owner.

## DISPOSITION CANDIDATE

**`KEEP_PARTIAL` + `CLARIFY_TERMINOLOGY`**.

UpgradePilot already has much of the responsibility of an Engineering Handbook, especially through `OPERATING_GUIDE.md` + `AGENTS.md` + the canonical owner structure. Do **not** create a large new handbook now merely because the term is common in industry.

Retain the concept in this study. Later, evaluate whether a small human-facing **Engineering Handbook / Engineering Guide index** would materially improve onboarding and transferable professional presentation while remaining a routing layer rather than a duplicated authority.

## LEARNING TAKEAWAY

An Engineering Handbook is not primarily a book about the code. It is the maintained reference for **how engineers are expected to work on the system and where the authoritative knowledge lives**. UpgradePilot already implements much of that responsibility, but in a deliberately distributed form. The question for us is therefore not “do we have engineering guidance?” but “would a conventional human-facing handbook layer reduce discovery/onboarding cost without duplicating authority?”
