# Governance Redesign Group Audit and Dependency Map

**Artifact role:** cross-group audit and dependency map for the governance operating-model redesign  
**Authority:** non-controlling planning evidence; existing governance/specification owners remain authoritative until changed through an accepted bounded implementation step  
**Baseline:** redesign branch created from repository revision `503e08c74102c9159a4aa82054ccdac464f843ec`  
**Scope:** governance/instruction/specification/Agent-Skill/tooling surfaces involved in how AI assistants orient, plan, audit, build, learn, and validate UpgradePilot work

---

## 1. Why this map exists

The redesign should not edit large governance files one by one in isolation. The same concepts currently appear across root instructions, the operating guide, product specifications, plan conventions, audit conventions, learning contracts, Agent Skills, and governance diagnostics.

The purpose of this map is to establish:

```text
what each redesign group owns
→ which existing files must be audited together
→ what may be moved/referenced/reinforced
→ what must remain canonical elsewhere
→ which later groups depend on earlier decisions
```

This prevents a local cleanup from silently weakening another operation mode or creating a second semantic owner.

---

## 2. Core architectural finding

The repository already distinguishes durable authority from procedural aids:

- root `AGENTS.md` owns repository-wide routing, authorization boundaries, responsibility registration, context discipline, and standing safeguards;
- `OPERATING_GUIDE.md` owns project-wide learning/execution method;
- specifications own accepted stable product invariants;
- ADRs own consequential implementation methods;
- plans own bounded execution/investigation coordination;
- `.agents/skills/` owns task-specific reusable agent workflows;
- source/tests/evidence own implementation truth;
- `MEMORY.md` alone owns live continuation.

The missing layer is not another universal specification. The missing layer is a more explicit **operation-routing and progressive-disclosure model**.

Therefore the five recurring operation families should normally be implemented as **Agent Skills**:

```text
Audit / Review
Planning / Design
Build / Implement
Learning by Doing
Learning Only
```

They may reference specifications, plans, ADRs, source/tests, learning contracts, and other owners, but they must not become competing semantic authorities.

A new specification should be created only if the redesign discovers a genuinely stable product invariant that has no existing owner. Operation procedure alone is not sufficient reason to create a specification.

---

## 3. Deliberate reinforcement rule

The redesign must preserve an important distinction:

```text
CANONICAL SEMANTIC OWNERSHIP
!=
OPERATIONAL REINFORCEMENT
```

A critical rule may deliberately appear in several surfaces when repeated assistant failures justify high-salience reinforcement.

Acceptable pattern:

```text
canonical owner
→ complete rule/invariant

AGENTS.md
→ short persistent safeguard
→ exact reference to canonical owner

operation Skill
→ operation-specific application/check
→ exact reference to canonical owner
```

Unacceptable pattern:

```text
three files independently define materially different versions
→ no clear owner
→ drift becomes possible
```

This redesign will therefore remove **accidental competing ownership**, not useful redundancy by default.

---

## 4. Audited baseline relationships

### 4.1 Root `AGENTS.md`

The root file already performs several distinct jobs:

- authority and request-to-action boundary;
- responsibility routing map;
- live-state/artifact rules;
- context loading guidance;
- critical safeguards;
- implementation/validation/claim guidance;
- instruction-admission maintenance rules.

It also contains substantial reinforcements for implementation retention and producer → integration → consumer ownership analysis, and a strong source-clarity completion statement.

**Redesign implication:** retain root-level high-salience safeguards, but remove full procedures that can be progressively disclosed through operation Skills.

### 4.2 `OPERATING_GUIDE.md`

The guide currently owns:

- core real-responsibility working loop;
- context engineering;
- Ceremony Tax;
- implementation-retention reasoning;
- end-to-end responsibility trace;
- session proportionality;
- decision/exploration/execution modes;
- a very large Source Clarity Contract;
- teaching/explanation;
- post-run review;
- commands/tools;
- debugging;
- prerequisite repair;
- assistance fading;
- evidence/ownership;
- completion/stopping;
- updates/handoff.

**Redesign implication:** it should remain the project-wide Learning-by-Doing operating owner, not be reduced to a tiny index. However, operation-specific multi-step procedures should move into Skills where that improves activation and context efficiency.

### 4.3 Core specification

`docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md` already owns accepted `JUST-001` through `JUST-005` implementation-retention invariants.

**Redesign implication:** preserve these as canonical normative invariants unless later analysis proves they do not belong in the specification. `AGENTS.md`, `OPERATING_GUIDE.md`, Audit, Planning, and Build Skills may reinforce/apply them without redefining them.

### 4.4 Existing audit Skill

`.agents/skills/upgradepilot-repository-audit/SKILL.md` is already a successful progressive-disclosure example. It explicitly:

- remains procedural/non-controlling;
- establishes scope;
- loads only needed owners;
- separates governance from implementation truth;
- classifies findings;
- checks responsibility/proportionality;
- preserves read-only audit boundaries.

**Redesign implication:** refine and broaden this existing Skill rather than creating a competing second repository-audit procedure.

### 4.5 Learning-only package

`learning/2026-08-17-b2-dependency-environment-ci-consumption-mastery/00_LEARNING_SESSION_CONTRACT_AND_ROUTE.md` already demonstrates a strong scoped learning architecture:

```text
project-wide Operating Guide
→ package learning contract
→ plan-specific route/depth maps
→ LEARNING_MEMORY.md
→ real source/tests/evidence
```

It also contains parallel audit/evaluation, technical independence, necessity classification, real-case preference, depth control, and learner-assistance rules.

**Redesign implication:** the Learning-Only Skill should route into package-local contracts like this; it should not duplicate their full rules or replace package-local learning memory.

### 4.6 Plan conventions

`plans/README.md` correctly says plans own bounded responsibility/sequence/proof/stop lines and must reference rather than re-specify specifications/ADRs. It also currently carries B2-specific present/recent navigation that does not belong in a durable generic plan convention.

**Redesign implication:** Planning/Design Skill must use these plan rules; generic plan governance should be purified from project-position navigation.

### 4.7 Audit conventions

`audits/README.md` correctly owns durable non-controlling critical examination and proportional audit-record formats. It also contains a dated `Current classification` block better owned by lifecycle indexes.

**Redesign implication:** Audit Skill should use audit conventions; root audit governance should describe lifecycle mechanics, while lifecycle indexes own classification state.

### 4.8 Security/trust controls

`SECURITY.md` contains useful boundaries but is much broader than the minimum required for many ordinary UpgradePilot sessions. Material reusable concerns include:

- credentials/private data when encountered;
- untrusted external evidence must not become project authority;
- unknown external code should not be executed merely for inspection;
- external writes require explicit authorization;
- ambient credentials/proxy transport must not silently change intended behavior where relevant.

**Redesign implication:** reassess the standalone file after root/mode routing is designed. Do not delete the underlying safeguards merely to reduce file count. If all remaining rules fit cleanly in existing owners without semantic loss, deletion is allowed; otherwise retain a much smaller scoped owner.

### 4.9 Governance diagnostics

`tools/agent-governance/governance_doctor.py` currently performs deterministic structural/schema/link/size checks. `cases.json` carries behavioral governance expectations.

**Redesign implication:** extend deterministic checks only for objective low-noise relationships; use behavioral cases/operation audits for semantic consistency and routing behavior.

---

## 5. Redesign groups

### Group 1 — Core Router + Operating Guide Boundary

Primary surfaces:

```text
AGENTS.md
OPERATING_GUIDE.md
SECURITY.md
ENVIRONMENT.md
docs/README.md
plans/README.md
audits/README.md
```

Owns redesign of:

- permanent always-on/bootstrap instructions;
- operating-mode routing;
- canonical-owner vs reinforcement convention;
- global Learning-by-Doing boundary;
- responsibility loading rules;
- disposition of broad security/trust guidance;
- prevention of live-state leakage in durable governance indexes.

**Dependencies:** none. This establishes the routing contract used by all later Skills.

### Group 2 — Learning-by-Doing Mode

Primary surfaces:

```text
OPERATING_GUIDE.md
AGENTS.md
new .agents/skills/... learning-by-doing Skill
selected references to plans/audits/source/tests
```

Owns:

- default UpgradePilot work philosophy;
- minimum teaching/ownership behavior during real work;
- how Learning-by-Doing composes with Audit, Planning, Build, Debugging, and Testing;
- assistance fading, prerequisite repair, evidence interpretation, and post-run review where globally useful;
- explicit/manual mode triggering without requiring it for ordinary sessions.

**Depends on:** Group 1 routing and owner boundary.

### Group 3 — Audit / Review Mode

Primary surfaces:

```text
.agents/skills/upgradepilot-repository-audit/SKILL.md
audits/README.md
OPERATING_GUIDE.md references
AGENTS.md routing
relevant specifications/ADRs/plans/source/tests/evidence
```

Owns:

- bounded implementation/design/governance review procedure;
- cross-owner consistency analysis when material;
- source/tests as implementation truth;
- `JUST-*` and producer → integration → consumer application;
- finding classification and durable-audit promotion criteria;
- read-only default for review/audit requests.

**Depends on:** Group 1; composes with Group 2 for normal Learning-by-Doing audits.

### Group 4 — Planning / Design Mode

Primary surfaces:

```text
new Planning/Design Skill
plans/README.md
AGENTS.md routing
OPERATING_GUIDE.md references
PROJECT_CHARTER.md
specifications
ADRs
MEMORY.md only when live selection matters
```

Owns:

- whether a durable plan is needed at all;
- proportional micro/normal/large planning;
- design-before-implementation reasoning;
- specification/ADR/plan ownership separation;
- plan entry evidence, allowed modification boundary, proof, pass condition, stop line;
- explicit plan writing when requested.

**Depends on:** Group 1; normally composes with Group 2.

### Group 5 — Build / Implement Mode

Primary surfaces:

```text
new Build/Implement Skill
AGENTS.md routing
OPERATING_GUIDE.md references
Source Clarity rules
Naming Clarity specification
Core `JUST-*`
selected plan/spec/ADR/source/tests
```

Owns:

- implementation entry conditions;
- source/test inspection before change;
- bounded modification and preservation of unrelated work;
- source-clarity application;
- naming clarity;
- implementation-retention burden;
- narrow-to-broad validation;
- proof/claim boundary;
- handoff/update routing.

**Depends on:** Group 1; normally composes with Group 2; consumes Group 4 outputs when a plan exists.

### Group 6 — Learning-Only Mode

Primary surfaces:

```text
new Learning-Only Skill
OPERATING_GUIDE.md references
learning/ package conventions
package-local learning contracts/plans/LEARNING_MEMORY.md
source/tests/evidence
```

Owns:

- explicit pause of product mutation;
- real-case/source/test-driven teaching;
- package-local route discovery;
- learning-depth/defer rules;
- learner checkpoints and assistance fading;
- learning memory continuity;
- parallel audit only to the proportion justified by the learning responsibility.

**Depends on:** Group 1; shares global teaching principles with Group 2 but must remain distinct from normal build progression.

### Group 7 — Governance Consistency + Validation + Cleanup

Primary surfaces:

```text
tools/agent-governance/governance_doctor.py
tools/agent-governance/cases.json
tools/agent-governance/README.md
AGENTS.md responsibility map
plans/README.md
audits/README.md
all new/modified Skills
selected governance/specification indexes
```

Owns:

- deterministic structural validation;
- behavioral routing regression cases;
- cross-owner consistency scenarios;
- deliberate-reinforcement drift checks where objectively possible;
- lifecycle/index cleanup;
- link/path/skill registration validation;
- final branch-wide governance audit and merge-readiness evidence.

**Depends on:** Groups 1–6 because it validates the resulting operating model.

---

## 6. Cross-group composition model

The five operation modes are not mutually exclusive in the sense of project philosophy.

Normal composition should be:

```text
Learning by Doing = default overlay / working philosophy

Audit task
→ Audit procedure
+ Learning-by-Doing behavior unless explicitly suppressed

Planning/design task
→ Planning/Design procedure
+ Learning-by-Doing behavior unless explicitly suppressed

Build task
→ Build/Implement procedure
+ Learning-by-Doing behavior unless explicitly suppressed

Learning-only task
→ Learning-Only procedure
→ product mutation paused
→ package-local learning contract when one exists
```

Do not implement this as five competing modes where only one can ever be active. The router should distinguish:

```text
PRIMARY OPERATION
Audit | Planning | Build | Learning Only | explanation/diagnosis/etc.

WORKING PHILOSOPHY
Learning by Doing is the normal UpgradePilot default for substantive work
```

This distinction is critical to avoid making Learning-by-Doing disappear whenever another operation Skill is invoked.

---

## 7. Canonical owner and reinforcement matrix

| Concern | Canonical semantic owner | Allowed reinforcement/application |
|---|---|---|
| Request-to-action boundary | `AGENTS.md` | operation Skills may restate the relevant boundary briefly |
| Live continuation | `MEMORY.md` | plans/Skills reference only |
| Mission/product boundary | `PROJECT_CHARTER.md` | Planning/Audit Skills consult when material |
| Stable product invariants | accepted specifications | AGENTS/Guide/Skills reference/apply |
| Consequential method | accepted ADR | plans/Skills reference/apply |
| Bounded execution coordination | selected plan | Build/Audit/Learning routes consume |
| Learning-by-Doing method | `OPERATING_GUIDE.md` | Learning-by-Doing Skill provides scoped procedure/manual trigger |
| `JUST-*` retention invariants | Core specification | AGENTS/Guide/Audit/Plan/Build reinforce/apply |
| Source clarity acceptance principles | redesign decision: likely `OPERATING_GUIDE.md` compact core | Build/Audit Skills apply detailed checks; naming spec remains complementary |
| Naming terminology standard | Naming Clarity specification | Build/Audit Skills apply |
| Audit-record lifecycle | `audits/README.md` + lifecycle indexes | Audit Skill routes records |
| Plan creation/structure | `plans/README.md` | Planning Skill operationalizes |
| Learning package method | package-local learning contract | Learning-Only Skill discovers/routes |
| Governance objective checks | `tools/agent-governance/` | final audit interprets results |

---

## 8. Key risks the group plans must prevent

### Risk A — Skills become second governance system

Mitigation:

- skills reference canonical owners;
- no product invariant is silently copied into a skill as independent authority;
- skill frontmatter and purpose explicitly state procedural/non-controlling role.

### Risk B — `OPERATING_GUIDE.md` becomes too thin

Mitigation:

- retain core Learning-by-Doing loop;
- retain assistance fading, prerequisite repair, evidence interpretation, proportionality, stopping, and other genuinely everyday rules;
- move only operation-specific procedure/detail that benefits from progressive disclosure.

### Risk C — critical rules become easy to miss after deduplication

Mitigation:

- preserve deliberate high-salience reinforcement in root and relevant Skills;
- canonical owner remains explicit;
- add behavioral regression cases for previously missed rules.

### Risk D — too many new Skills

Mitigation:

- create only the five demonstrated operation families;
- refine the existing audit Skill instead of creating a parallel one;
- do not create micro/medium/large variants when one proportional Skill can scale.

### Risk E — generic governance cleanup changes product semantics

Mitigation:

- governance redesign does not alter accepted product behavior merely to simplify instructions;
- specification/ADR changes require separate evidence that their semantics themselves are wrong or misplaced;
- changes to wording that only alter routing/procedure must preserve product invariants.

### Risk F — Learning-by-Doing and Learning-Only collapse into one mode

Mitigation:

- Learning-by-Doing permits real project mutation under normal authorization;
- Learning-Only explicitly pauses product mutation and uses package-local learning continuity;
- both share teaching quality rules but have different action boundaries.

---

## 9. Planned implementation order

Use the following dependency order unless evidence during a group audit requires rebounding:

```text
Group 1 — Core Router + Operating Guide Boundary
→ Group 2 — Learning by Doing
→ Group 3 — Audit / Review
→ Group 4 — Planning / Design
→ Group 5 — Build / Implement
→ Group 6 — Learning Only
→ Group 7 — Consistency / Validation / Cleanup
```

This is a dependency order, not live project-state ownership. `MEMORY.md` remains the only live continuation owner.

Each group must pass its own focused validation before the next group is treated as stable input.

---

## 10. Group-level acceptance rule

A group is ready to become input to the next group only when:

1. its canonical responsibility is explicit;
2. no new competing owner has been created;
3. its files/references are bounded and proportional;
4. deliberate reinforcement is identifiable as reinforcement;
5. operation routing is unambiguous;
6. relevant existing behavior is preserved unless separately justified;
7. deterministic checks that can be run at that stage pass;
8. at least one realistic behavioral scenario has been reasoned through;
9. cross-group dependencies are updated in this planning family when a material assumption changes.

---

## 11. Prohibited shortcuts

Do not:

- rewrite all governance files in one pass;
- delete repetition solely to satisfy DRY;
- create a new specification for every operation mode;
- convert Skills into controlling authorities;
- remove Learning-by-Doing rules from the Operating Guide merely because a Skill exists;
- merge before branch-wide governance consistency review;
- update `MEMORY.md` to use this planning family as live continuation unless a separate authorized live-state update is made;
- change product behavior merely to make governance simpler.
