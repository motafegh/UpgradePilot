# Playbook — term analysis for UpgradePilot

**Status:** analyzed / decision candidate  
**Study branch:** `research/real-world-engineering-practices-2026-10-24`  
**Study owner:** `working-memory/2026-10-24_real-world-engineering-practices_project-fit_cycle.md`

## WHAT

A software-engineering **playbook** is scenario-oriented operational guidance for recurring classes of situations. It normally answers: when this situation occurs, what should the engineer inspect, how should they reason, what options are available, what must not be assumed, what evidence is needed, when should they stop/escalate, and which narrower procedures or authoritative owners should they use.

A playbook is usually broader and more judgment-oriented than a runbook, but narrower and more situational than an engineering handbook.

Useful distinction:

- **Handbook:** how engineering works here overall; principles, practices, ownership and navigation.
- **Playbook:** how to handle a recurring type of engineering situation.
- **Runbook:** exact/repeatable operational procedure for a comparatively specific task or incident.
- **Specification:** required technical behavior/invariants, not response guidance.
- **ADR:** why a consequential architectural decision was made.

A playbook may link to runbooks, specifications, ADRs, tools and owners rather than duplicating them.

## WHY

Playbooks reduce repeated reinvention when situations recur but cannot be safely reduced to one fixed command sequence. They help preserve expert reasoning, decision criteria, escalation/stop conditions, failure distinctions and ownership boundaries while still allowing situational judgment.

They are especially useful when:

- the same class of problem appears repeatedly;
- several diagnostic or decision branches are legitimate;
- engineers need to know what evidence to gather before acting;
- there are important failure modes or prohibited shortcuts;
- the exact action depends on context;
- a simple runbook would be too rigid.

## PROJECT MAPPING

UpgradePilot already contains substantial **playbook-like responsibility**, although it does not usually use that label.

Strong examples:

- `.agents/skills/upgradepilot-repository-audit/` — scenario-specific guidance for substantive repository audit/review.
- `.agents/skills/upgradepilot-planning-design/` — scenario-specific guidance for planning/design responsibilities.
- `.agents/skills/upgradepilot-build-implement/` — scenario-specific guidance for implementation work, including scope, ownership, proof and escalation logic.
- `.agents/skills/upgradepilot-learning-only/` and the Learning-by-Doing skill — guidance for recurring learning/engineering situations.
- `.agents/skills/upgradepilot-working-memory/` and workstream supervision skills — specialized recurring-work procedures.
- `OPERATING_GUIDE.md` contains broader project-wide methods and decision guidance that individual playbooks specialize.
- `ENVIRONMENT.md` and `SECURITY.md` include some narrower diagnostic/response guidance that can become runbook- or playbook-like depending on the section.

The current Skills are primarily **AI-agent procedural playbooks**, not necessarily human-facing engineering playbooks. That distinction matters.

Potential future human-facing UpgradePilot playbooks, only if recurring need justifies them, could include:

- public-provider/acquisition failure diagnosis;
- CI evidence interpretation and unsupported-shape handling;
- evidence conflict / provenance mismatch handling;
- semantic-model failure / invalid-grounding diagnosis;
- Workspace recovery/checkpoint integrity diagnosis;
- release/packaging verification;
- security/trust-boundary response for untrusted source content.

These should exist only where the scenario recurs and current owners do not already provide a sufficiently usable route.

## CURRENT EVIDENCE

Root `AGENTS.md` explicitly routes substantive operation families to reusable Skills, and `OPERATING_GUIDE.md` describes Skills as reusable procedures rather than authority. The Build skill, for example, contains the characteristic playbook structure: activation conditions, required/conditional context, decision branches, prohibited actions, escalation conditions, implementation/proof sequence and stop boundaries.

Therefore UpgradePilot already uses the **playbook concept in substance**, especially for AI-assisted engineering operations.

## DISTINCTION FROM NEARBY TERMS

### Playbook vs runbook

A runbook is usually more deterministic:

`condition → execute these concrete steps → verify result`

A playbook allows more judgment:

`recognize situation → inspect evidence → classify → choose appropriate response path → verify/escalate/stop`

For example, "restore this SQLite checkpoint from this backup with these exact commands" would be runbook-like. "A Workspace checkpoint cannot be reconstructed: determine whether this is corruption, unsupported schema, missing material, stale revision, or storage failure, then choose the appropriate response" is playbook-like.

### Playbook vs handbook

A handbook is broad and organizational. A playbook is problem/situation oriented. A handbook may say what engineering principles and owners exist; a playbook says how to apply them in one recurring class of situation.

### Playbook vs specification

A playbook tells an engineer how to respond. A specification tells the software what behavior/invariants it must satisfy. Playbooks must not become shadow specifications.

## BENEFIT / COST / FAILURE MODES

Potential benefit for UpgradePilot:

- clearer transfer of recurring diagnostic/decision reasoning;
- better human/AI onboarding to non-trivial situations;
- less repeated rediscovery of evidence, owners and stop conditions;
- strong fit with UpgradePilot's evidence-first and explicit-uncertainty philosophy;
- useful transferable professional engineering artifact.

Risks:

- duplicating `AGENTS.md`, `OPERATING_GUIDE.md`, Skills, specs or security/environment owners;
- stale playbooks becoming competing authority;
- excessive procedural ceremony for rare situations;
- turning flexible judgment into rigid checkbox execution;
- creating human-facing files for procedures currently needed only by AI agents.

The correct design, if adopted, should keep playbooks thin and route authoritative requirements to their existing owners.

## TRIGGER OR REJECTION CONDITION

Create or promote a dedicated human-facing playbook only when a recurring scenario shows one or more of:

1. the same reasoning/diagnostic route is repeatedly reconstructed;
2. errors occur because responders miss important evidence/stop/escalation conditions;
3. current authoritative documents are correct but difficult to compose quickly during the situation;
4. another engineer/contributor needs a stable scenario guide;
5. the scenario contains multiple legitimate branches that are too contextual for a runbook.

Reject a new playbook when it would merely copy an existing Skill/guide/specification or when the situation is rare enough that a normal document section is clearer.

## DISPOSITION CANDIDATE

**`RECOGNIZE_EXISTING + CLARIFY_TERMINOLOGY + ADOPT_LATER_IF_EARNED`**

UpgradePilot already has playbook-like mechanisms, most clearly in `.agents/skills/`. No new generic `PLAYBOOK.md` is justified merely to adopt the industry term. A future human-facing `playbooks/` surface could be useful if repeated real engineering scenarios demonstrate a navigation/response need.

## UNRESOLVED QUESTIONS

- Should any current AI-agent Skill eventually have a parallel human-facing playbook, or should one artifact be readable by both?
- Which recurring UpgradePilot situations actually produce enough repeated decision pressure to justify a human playbook?
- Would a `playbooks/` directory improve navigation, or would it overlap too much with `docs/`, `ENVIRONMENT.md`, `SECURITY.md` and Skills?

## LEARNING TAKEAWAY

A playbook is not "more documentation" in general. Its distinctive responsibility is preserving **how to handle a recurring class of situations when judgment is required**. UpgradePilot already does this substantially for AI-agent operations; future adoption should focus on human-facing recurring scenarios only when evidence shows the need.
