# Track 1 — Project understanding and documentation architecture

**Status:** ACTIVE research track; non-controlling  
**Branch:** `research/real-world-engineering-practices-2026-10-24`  
**Research horizon at initialization:** `99d62aa384e9f71e3ecd9c6bccb46280f3aa3e3f`  
**Parent study:** `working-memory/2026-10-24_real-world-engineering-practices_project-fit_cycle.md`  
**Research method:** `working-memory/evidence/2026-10-24-real-world-engineering-practices/research-sequencing-and-decision-method.md`

## Purpose

Determine the best human-facing documentation/understanding architecture for UpgradePilot without creating duplicate authority, stale summaries, unnecessary taxonomy, or documentation for documentation's sake.

This track should produce the minimum set of durable human-facing artifacts that materially improve:

- understanding of the current system;
- engineer onboarding/re-entry;
- architecture communication;
- terminology recall;
- safe modification and responsibility discovery;
- access to the engineering journey and rationale;
- portfolio/reviewer comprehensibility;
- future collaboration when it actually appears.

This research does **not** promote new canonical documentation to `main`, reorganize existing accepted owners, or modify product behavior. Promotion decisions come only after the track is closed and reconciled against then-current `main`.

## Current documentation reality

At this research horizon, UpgradePilot already has a strong responsibility-oriented documentation system:

- `README.md` — product/reviewer entry point, quickstart, product boundary, current user-facing operation examples and high-level repository controls.
- `PROJECT_CHARTER.md` — stable mission, user, product boundary, evidence doctrine and claim limits.
- `MEMORY.md` — sole live project position and continuation.
- `docs/README.md` — accepted documentation/decision navigation and promotion lifecycle; explicitly a findability/ownership layer rather than a whole-system tutorial.
- `docs/specifications/` — accepted framework-independent system behavior, invariants and engineering standards.
- `docs/architecture/` — ADRs for consequential implementation/structural decisions.
- `plans/` — bounded responsibility sequence, proof obligations and stop lines.
- `src/upgradepilot/`, tests and reproducible evidence — implemented truth.
- `working-memory/` — dated engineering evidence/reasoning trail: investigations, alternatives, failures, corrections, experiments, proof transitions, implementation handoffs and historical decision provenance.
- `learning/` — reusable educational/relearning artifacts and frozen learning snapshots.
- `audits/`, `product-simulation/`, experiments and tools — specialized evidence/research/diagnostic surfaces.
- `.agents/skills/`, `AGENTS.md`, `OPERATING_GUIDE.md` — AI/project-operation procedure and learning method, not a human technical model of the product.
- `chronicle/` — optional, subjective, human-led story of the journey; context only, not engineering evidence authority.

The accepted `docs/` directory itself currently contains only the documentation map plus `architecture/` and `specifications/`. That is evidence of a deliberately narrow durable surface, not a missing-directory bug.

The source tree is already responsibility-oriented (`ci`, `dependency`, `github`, `impact`, Workspace-related code, application orchestration, maintainer-action synthesis, CLI/report boundaries, etc.). Therefore the missing human-facing layer is primarily **system synthesis and navigation**, not an absence of technical ownership.

## Observed gaps to investigate

The current repository does not expose an obvious single human-facing answer to:

> I am an engineer joining, reviewing, modifying or returning to UpgradePilot. What is the system, how do its major responsibilities relate, what concepts must I understand, how did the important design corrections happen, and where do I go deeper?

Initial repository searches also found no established standalone:

- contributor/onboarding guide;
- project glossary;
- architecture/system diagram set;
- playbook/runbook collection;
- Mermaid-based architecture documentation convention.

Absence is not itself a reason to create any of these. Each must earn a distinct responsibility.

## External professional lenses — orientation, not adoption

### Diátaxis

Diátaxis distinguishes four user needs:

- **tutorial** — learning by being guided;
- **how-to guide** — achieving a specific goal;
- **reference** — factual description/information;
- **explanation** — understanding why/how a topic fits together.

Use this only as a **diagnostic lens** to ask whether an artifact has one clear job. Do not reorganize UpgradePilot around Diátaxis categories merely for conformity.

Preliminary mapping:

- `README.md` mixes product explanation, reference and practical how-to intentionally as the repository entry point.
- specifications are predominantly reference/normative contracts.
- ADRs are decision/rationale records with strong explanation content.
- `learning/` provides tutorial/explanation-oriented material.
- plans, future playbooks and runbooks are goal/action-oriented but have different authority/responsibility semantics.
- the proposed Engineering Guide is primarily **explanation + navigation**, not a tutorial or normative reference.
- `working-memory/` and `chronicle/` do not map cleanly onto Diátaxis because they are evidence/history surfaces rather than ordinary end-user documentation.

### C4 model

C4 provides hierarchical architecture views: system context, container, component and code, plus optional dynamic/deployment diagrams. Its own guidance notes that system-context and container-level views are sufficient for many teams.

Use C4 as a **diagram vocabulary**, not an architecture framework or mandatory notation.

For UpgradePilot, the likely useful levels are:

1. **System context-style view** — maintainer/user, public GitHub/PyPI/upstream evidence sources, local semantic provider where applicable, UpgradePilot, saved report/checkpoint/storage boundaries.
2. **Container/subsystem-style view** — one-process modular product showing major responsibility groups and their relationships; do not falsely imply separate deployable services merely because C4 uses the word `container`.
3. **Selected dynamic/data-flow diagrams** — only for flows whose sequence/authority boundaries are hard to understand statically, such as normal investigation, CI static↔runtime correlation, Workspace publication/reconstruction, report/source preservation, or maintainer-action synthesis.

A full component/code-diagram catalog is not currently justified.

## Track questions and sub-responsibilities

### A. Documentation information architecture

Questions:

- Which current artifact types already have clear, non-overlapping responsibilities?
- Where does a human reader still need synthesis rather than another canonical owner?
- Does any current document mix responsibilities enough to create real confusion?
- Can a standard documentation concept improve vocabulary without forcing restructuring?

Current direction:

- keep the existing responsibility-based ownership model;
- do **not** reorganize the repository into tutorials/how-to/reference/explanation directories;
- use external frameworks only to audit clarity and missing reader needs.

### B. UpgradePilot Engineering Guide

Existing research:

- `project-engineering-guide.md`
- `engineering-guide-pretemplate.md`

Current disposition: **strong positive candidate**, pending final Track-1 synthesis and then-current-main reconciliation.

Proposed responsibility:

> Current-system-first human technical mental model + navigation + selective engineering-evolution context, without duplicating canonical contracts or live status.

The guide should explain the present system, major flows, concepts, proof model, failure model, modification responsibility map and selected important engineering-history transitions.

### C. Architecture/system diagrams

Research questions:

- Which diagrams answer questions that prose/tables currently answer poorly?
- What abstraction level avoids misleading deployment/service implications?
- Which boundaries must be visible: product vs external providers, acquisition vs domain semantics, interpretation vs validation, Workspace/native vs legacy/report projection, product vs experiments/tools?
- What diagram representation is maintainable enough to stay synchronized with source?

Provisional recommendation:

- one context-style diagram;
- one high-level subsystem/responsibility diagram;
- a small number of dynamic flow diagrams only where sequence/provenance matters materially;
- no exhaustive component/class diagrams;
- distinguish **current** versus **future/proposed** architecture explicitly; never combine them silently in one picture.

Representation/tooling remains open. Mermaid or another text-as-code notation may be useful, but no diagram tool should be adopted until we test readability, Git reviewability and drift cost against one real UpgradePilot diagram.

### D. Core terminology / glossary

The accepted Naming Clarity Engineering Standard already requires clear names, one primary term per concept, and narrow durable definitions for non-obvious terminology. It explicitly says a glossary may support recall but must not compensate for vague naming.

Therefore the current candidate is **not** a giant standalone glossary.

Prefer initially:

- a `Core concepts and terminology` section inside the Engineering Guide;
- concise practical meaning;
- nearby term that must not be confused with it;
- link to the canonical specification/owner for exact semantics.

Candidate terms include evidence, authority, provenance, observation, proposal, evaluated proposition, exact identity, missing/unavailable/unsupported/unresolved, coverage, applicability, abstention, source reference vs retained original text, Workspace revision/checkpoint/reconstruction/recovery/replay, proof/non-proof.

Create a standalone glossary only if lookup volume or cross-artifact terminology genuinely outgrows the guide section.

### E. Engineer onboarding and contributor documentation

Distinguish two needs:

**Engineer onboarding/re-entry**
- understand product/system;
- trace one real flow;
- learn core semantics;
- inspect proof/test anchors;
- understand responsibility ownership;
- use selected working-memory records to learn important design corrections.

This should initially be an **onboarding route inside the Engineering Guide**, not another standalone document.

**External contribution workflow**
- local setup;
- branch/PR expectations;
- tests/checks;
- coding/documentation contribution conventions;
- review/release expectations.

A conventional `CONTRIBUTING.md` is not yet justified merely for professionalism. Trigger it when external human collaboration/contribution becomes a real supported responsibility or when README/Engineering Guide cannot represent contributor mechanics cleanly.

### F. Playbooks and runbooks

Current distinction:

- **playbook** — recurring scenario with branching judgment: what should we examine/decide when situation X occurs?
- **runbook** — repeatable operational execution: what exact steps/commands perform or recover operation X?

Do not create a `playbooks/` or `runbooks/` directory now.

Adoption trigger:

- the same scenario recurs;
- the reasoning/steps are stable enough to reuse;
- keeping them implicit causes repeated diagnosis/recovery cost or unsafe variation;
- the scenario is not already adequately owned by a specification, plan, tool, README diagnosis table or AI Skill.

Potential future candidates, not selected yet:

- evidence-acquisition diagnosis playbook;
- semantic-claim validation playbook;
- Workspace recovery playbook/runbook pair;
- report/projection diagnosis playbook;
- release verification runbook if release engineering becomes admitted.

### G. Working-memory and engineering journey

`working-memory/` is a first-class technical history/provenance surface. It should feed the Engineering Guide selectively through major transitions:

```text
current mechanism
→ original assumption or earlier design
→ observed pressure/failure
→ investigation/experiment
→ correction/accepted decision
→ current mechanism/proof state
→ remaining debt/non-proof
→ exact historical links
```

Candidate journey themes:

- clean-slate and responsibility-based architecture corrections;
- CI static/runtime correlation evolution;
- impact/applicability semantics evolution;
- semantic/LLM experiments and semantic failure discoveries;
- Workspace research → architecture → implementation → staged migration;
- report/source preservation evolution;
- product-usefulness/value investigations and unresolved acceptance questions.

Do not make the Engineering Guide a working-memory summary archive. Current source/canonical owners remain present truth.

### H. Chronicle boundary

`chronicle/` is deliberately subjective, voluntary and human-led. It may contain emotions, memories, reflections or imperfect recollections and explicitly does not prove technical events or decisions.

Therefore:

- do not automatically mine it to construct the Engineering Guide;
- do not treat it as technical rationale/proof;
- reference it only when Ali explicitly wants a human/reflective project-journey perspective distinct from engineering provenance.

### I. Maintenance and staleness control

The Engineering Guide and any accepted diagrams must not become snapshot documentation that silently drifts.

Candidate maintenance rule:

**Update in the same change/reconciliation when the durable mental model materially changes**, for example:

- major subsystem/responsibility introduced/removed;
- normal end-to-end flow changes;
- architecture/persistence/state boundary changes;
- core term/semantic boundary changes;
- supported proof/operational boundary changes;
- staged migration reaches a materially different durable state.

Do not churn the guide for routine implementation, dated validation, or live next-step changes.

Do not rely solely on `last reviewed` dates as freshness proof. A date can be useful metadata, but correctness requires reconciliation against source/tests/canonical owners.

Candidate drift controls:

- guide links to canonical owners rather than copying long rules;
- diagrams live close to the explanatory section that owns their meaning;
- each diagram labels scope and current/proposed status;
- architecture-changing reviews include a documentation-impact question;
- broken-link/reference checks may later be automated if the maintenance burden becomes real;
- no generated architecture diagram should be treated as authoritative merely because tooling produced it.

## Documentation responsibility matrix — provisional

| Reader need | Best current/future owner | Track-1 judgment |
| --- | --- | --- |
| What is UpgradePilot and how do I run it? | `README.md` | Keep |
| What is the stable product boundary? | `PROJECT_CHARTER.md` | Keep |
| Where is the project right now? | `MEMORY.md` | Keep exclusively |
| Where does durable knowledge belong? | `docs/README.md` | Keep |
| What must the system mean/guarantee? | specifications | Keep |
| Why was a structural method chosen? | ADR | Keep |
| What must this bounded work do/prove? | plan | Keep |
| What is actually implemented? | source/tests/evidence | Keep |
| How does the whole current system fit together? | **Engineering Guide candidate** | Missing / likely adopt |
| What are the important current architecture views? | Engineering Guide + selected diagrams | Missing / likely adopt selectively |
| What do core project terms mean in practice? | Engineering Guide term section + canonical owner links | Missing synthesis; no standalone glossary yet |
| How did consequential engineering decisions evolve? | working-memory + selective Engineering Guide synthesis | Existing history; missing curated entry |
| What did the journey feel like to Ali? | `chronicle/` | Existing, separate and optional |
| How do I learn/relearn one mechanism? | `learning/` | Existing |
| How do I handle recurring scenario X? | playbook if earned | Deferred until trigger |
| What exact operational steps perform/recover X? | runbook if earned | Deferred until trigger |
| How does an external human contribute? | `CONTRIBUTING.md` if collaboration becomes real | Deferred until trigger |

## Artifact admission test for Track 1

Before recommending any new documentation artifact, answer:

1. **Reader:** who needs it?
2. **Question:** what exact question does it answer?
3. **Current gap:** why can existing owners not answer that question adequately?
4. **Responsibility:** is it explanation, navigation, normative reference, scenario guidance, procedure, education, history, or live status?
5. **Authority:** what does it own, and what must it only link to?
6. **Maintenance trigger:** what changes require updating it?
7. **Drift risk:** how can it become stale or contradict canonical owners?
8. **Evidence:** what current source/docs/history support the content?
9. **Cost:** is the artifact cheaper to maintain than repeatedly reconstructing the knowledge?
10. **Exit/rejection:** under what conditions should it not be created or should it be removed/merged?

If those questions cannot be answered clearly, do not add the artifact.

## Diagram admission checklist

For each proposed diagram, record:

- exact reader/question;
- current vs proposed/future status;
- abstraction level;
- nodes/boundaries derived from actual source/deployment evidence;
- relationship semantics (data, control, evidence, storage, external dependency, etc.);
- critical non-claims;
- owning explanatory section;
- source/ADR evidence anchors;
- maintenance trigger;
- whether a table/prose explanation would be simpler and less stale.

The diagram is rejected if it mainly decorates documentation or creates false precision.

## Initial provisional dispositions

| Concept/artifact | Candidate disposition | Reason |
| --- | --- | --- |
| UpgradePilot Engineering Guide | `ADOPT_LATER_IF_EARNED` — strong positive | Real current-system synthesis gap |
| Diátaxis | `KEEP_PARTIAL` | Useful audit vocabulary; repo-wide restructuring unnecessary |
| C4 | `KEEP_PARTIAL` / `EXPERIMENT_IF_TRIGGERED` | Useful diagram vocabulary; only a few levels likely valuable |
| Context-style architecture diagram | `ADOPT_LATER_IF_EARNED` | Useful external/system-boundary mental model |
| Subsystem/responsibility diagram | `ADOPT_LATER_IF_EARNED` | Likely high onboarding/architecture value |
| Dynamic flow diagrams | `EXPERIMENT_IF_TRIGGERED` | Valuable only for genuinely sequence-heavy flows |
| Full component/class diagram catalog | `REJECT_FOR_CURRENT_PRODUCT` | High drift/maintenance cost with weak current benefit |
| Standalone glossary | `DEFER` | Naming standard + guide-local concepts likely sufficient initially |
| Engineer onboarding route | `KEEP_PARTIAL` / include in Engineering Guide | Real need; separate file not yet justified |
| `CONTRIBUTING.md` | `DEFER` | No current supported external-contributor workflow demonstrated |
| Playbook collection | `DEFER` | Create only after repeated scenario proves need |
| Runbook collection | `DEFER` | Same; exact procedures should be earned by stable operations |
| Working-memory integration | `RECOGNIZE_EXISTING` + curated guide use | Rich engineering journey already exists |
| Chronicle integration | `KEEP_SEPARATE` | Human subjective journey is intentionally not technical authority |

## Evidence still needed before Track 1 closure

1. Produce at least one real **context-style diagram candidate** from current UpgradePilot evidence and test whether it improves understanding.
2. Produce at least one **subsystem/responsibility diagram candidate** and verify it does not falsely imply service/deployment boundaries.
3. Decide diagram representation/tooling after evaluating readability, source reviewability and drift cost.
4. Audit whether the Engineering Guide term section is sufficient or whether a separate glossary would materially improve lookup.
5. Test the proposed fast onboarding route against a realistic `new/returning engineer` question set.
6. Identify 5–10 high-value working-memory transitions that deserve future Engineering Guide links; do not scan history indiscriminately.
7. Review current diagnosis/operation material to see whether any scenario already clearly earns a playbook/runbook rather than deferring all of them.
8. Reconcile this track against then-current `main` before final disposition.

## Track-1 completion criteria

Track 1 is complete when we can answer, with repository evidence:

- what human-facing documentation layers UpgradePilot should have;
- what each one owns and does not own;
- which new artifacts are genuinely justified;
- what diagrams are useful and at what abstraction level;
- how terminology should be presented;
- how onboarding should work;
- how working-memory and chronicle differ and feed current understanding;
- when playbooks/runbooks become justified;
- how accepted human-facing documentation stays current without becoming another live-status system.

Expected final output:

1. Track-1 synthesis and decision matrix;
2. refined Engineering Guide pre-template;
3. accepted/rejected diagram candidates;
4. terminology/onboarding/playbook/runbook decisions;
5. promotion candidates for later reconciliation with `main`;
6. explicit no-change/defer decisions where extra documentation would add maintenance burden without value.

## Immediate next research step

Start with **architecture/system diagrams** because they directly test whether the proposed Engineering Guide can make the current system easier to understand rather than merely becoming more prose.

The first candidate should be a current-state, C4-inspired **System Context** view grounded in actual UpgradePilot product/deployment boundaries. After that, create a high-level subsystem/responsibility view and compare whether both are necessary.