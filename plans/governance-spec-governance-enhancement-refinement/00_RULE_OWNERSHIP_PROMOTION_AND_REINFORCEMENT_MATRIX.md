# Existing Rule Ownership, Promotion, and Reinforcement Matrix

**Artifact role:** mandatory traceability gate for the governance redesign  
**Branch:** `governance/spec-governance-enhancement-refinement`  
**Created:** 2026-08-23  
**Scope:** existing governance, learning, planning, audit, implementation, source-clarity, ownership, and agent-governance rules that may be retained, promoted, specialized, reinforced, or deliberately left local during Groups 3–7  
**Authority:** planning/traceability only; this file does not itself supersede `AGENTS.md`, `OPERATING_GUIDE.md`, specifications, Skills, package-local learning contracts, or other canonical owners

---

## 1. Why this matrix exists

UpgradePilot accumulated several strong rules through real work before the operation-Skill redesign existed. Some are in permanent controls, some in accepted specifications, some in the existing audit Skill, and some of the strongest learning/ownership rules were refined inside:

```text
learning/2026-08-17-b2-dependency-environment-ci-consumption-mastery/
```

The redesign must not accidentally lose a proven rule merely because it currently lives inside a specialized package, nor should it copy every package-specific rule into global context.

Required discipline:

```text
existing rule/pattern
→ identify the responsibility it actually serves
→ decide whether it is globally reusable or locally specialized
→ name one canonical semantic owner
→ name operation Skills that should apply it
→ decide whether deliberate reinforcement is justified
→ preserve package-local detail when generalization would add noise or distort meaning
```

This matrix is therefore a **migration trace**, not another standing governance contract.

---

## 2. Sources audited

The traceability pass inspected the current redesign branch versions of:

```text
AGENTS.md
OPERATING_GUIDE.md
SECURITY.md
plans/README.md
audits/README.md

docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md
docs/specifications/UPGRADEPILOT_NAMING_CLARITY_SPECIFICATION.md

.agents/skills/upgradepilot-repository-audit/SKILL.md
.agents/skills/upgradepilot-learning-by-doing/SKILL.md

tools/agent-governance/cases.json
plans/UPGRADEPILOT_AGENT_GOVERNANCE_REFINEMENT_AND_EVALUATION_PLAN.md

learning/2026-08-17-b2-dependency-environment-ci-consumption-mastery/
  00_LEARNING_SESSION_CONTRACT_AND_ROUTE.md
  00_PLAN_MASTERY_AND_DEPTH_INDEX.md
  CAREER_DAY30_OWNERSHIP_HANDOFF.md
  LEARNING_MEMORY.md role/boundary
  plan/depth-map family structure

plans/governance-spec-governance-enhancement-refinement/
  02_LEARNING_BY_DOING_MODE_PLAN.md
  03_AUDIT_REVIEW_MODE_PLAN.md
  04_PLANNING_DESIGN_MODE_PLAN.md
  05_BUILD_IMPLEMENT_MODE_PLAN.md
  06_LEARNING_ONLY_MODE_PLAN.md
  07_GOVERNANCE_CONSISTENCY_VALIDATION_AND_CLEANUP_PLAN.md
```

The B2 execution/depth plans were treated as specialization evidence. Their exact uv/CI route, case identities, and detailed technology-depth assignments were not candidates for global promotion merely because they are well written.

---

## 3. Disposition vocabulary

| Disposition | Meaning |
|---|---|
| **KEEP GLOBAL** | The reusable rule already has an appropriate project-wide canonical owner. |
| **PROMOTE GLOBAL** | A proven local rule is broadly reusable and should be expressed compactly in a project-wide owner. |
| **APPLY IN SKILL** | The rule is procedural/application detail best loaded only for the relevant operation. |
| **DELIBERATE REINFORCEMENT** | Repeat the essential high-salience instruction at an execution surface while keeping one canonical semantic owner. |
| **KEEP PACKAGE-LOCAL** | The rule is tied to one learning package, route, evidence vocabulary, technology, or Career overlay and should not inflate global context. |
| **PROMOTE PART / KEEP DETAIL LOCAL** | A general principle should move upward while exact package mechanics remain local. |

A rule can have more than one application surface, but it must not gain several independent semantic owners.

---

## 4. Rule traceability matrix

### A. Core Learning-by-Doing and learner interaction

| ID | Existing proven rule/pattern | Important existing source(s) | Disposition | Canonical owner / target | Skill application / reinforcement | Required redesign action |
|---|---|---|---|---|---|---|
| `RT-LBD-001` | Real project responsibility is the unit of learning; do not replace work with a detached tutorial. | `OPERATING_GUIDE.md`; B2 contract §§2,8–10 | **KEEP GLOBAL** | `OPERATING_GUIDE.md` | Learning-by-Doing Skill; Planning/Audit/Build/Learning-Only compose with it | Preserve. |
| `RT-LBD-002` | Prefer real source/tests/target evidence before synthetic examples when adequate real evidence exists. | B2 contract §§2,7–8,13; Learning-by-Doing Skill | **PROMOTE PART / KEEP DETAIL LOCAL** | `OPERATING_GUIDE.md` global real-evidence principle; package contracts may make it stricter | Learning-by-Doing and Learning-Only Skills | Global rule stays concise; S001/S011/S005 examples remain local. |
| `RT-LBD-003` | Background first for genuinely new material; teach only the minimum complete background needed for the active responsibility. | B2 contract §§2,8; `OPERATING_GUIDE.md` §§7–8 | **KEEP GLOBAL** | `OPERATING_GUIDE.md` | Learning-by-Doing and Learning-Only Skills | Preserve. |
| `RT-LBD-004` | One minimum-complete chunk/mechanism at a time; avoid both multi-mechanism jumps and meaningless fragmentation. | B2 contract §§2,9–10; `OPERATING_GUIDE.md` §§2,7 | **KEEP GLOBAL** | `OPERATING_GUIDE.md` | Learning-by-Doing/Learning-Only Skills | Preserve; package A–N chunk sequence remains local. |
| `RT-LBD-005` | Learner checkpoints must be fair: prediction/reasoning only when the required premises are already established; do not quiz untaught implementation detail. | B2 contract §§2,11; Career handoff Rule 1 | **PROMOTE GLOBAL** | `OPERATING_GUIDE.md` teaching/ownership section | Learning-by-Doing and Learning-Only Skills | Add compact global fairness rule; Skills operationalize it. |
| `RT-LBD-006` | Learner may interrupt, challenge, or backtrack; resolve the local premise before advancing and explicitly correct an earlier assistant oversimplification. | B2 contract §12 | **PROMOTE PART / KEEP DETAIL LOCAL** | `OPERATING_GUIDE.md` global teaching independence | Learning-by-Doing and Learning-Only Skills | Preserve current backtrack procedure; make self-correction/technical independence explicit. |
| `RT-LBD-007` | Do not optimize for agreement with Ali, the current code, or a previous assistant. Evaluate all hypotheses by evidence. | B2 contract §§2–5; Learning-by-Doing Skill | **KEEP GLOBAL / DELIBERATE REINFORCEMENT** | `OPERATING_GUIDE.md` | Learning-by-Doing + Audit Skills | Keep visible in both relevant Skills because conversational agreement failure is common and materially harmful. |
| `RT-LBD-008` | Assistance fades on repeated mechanisms but essential context must not be withheld to manufacture difficulty. | B2 contract §§2,14; Career handoff Rule 7; `OPERATING_GUIDE.md` §9 | **KEEP GLOBAL** | `OPERATING_GUIDE.md` | Learning-by-Doing/Learning-Only Skills | Preserve D0–D5 globally; exact package progression may specialize. |
| `RT-LBD-009` | AI use/manual typing/test green does not by itself demonstrate learner ownership. | B2 contract §§2,14,16; Career handoff; `OPERATING_GUIDE.md` §7 | **KEEP GLOBAL / DELIBERATE REINFORCEMENT** | `OPERATING_GUIDE.md` | Learning-by-Doing, Build, Learning-Only Skills | Preserve and repeat only at ownership evidence surfaces. |
| `RT-LBD-010` | Material learning depth needs a project-local reason; if a target does not unlock proposition ownership, control-flow understanding, later change/test/diagnosis, proof evaluation, target interpretation, or a later prerequisite, reduce depth. | B2 contract §§2,8,14–15; depth index §§3–4 | **PROMOTE GLOBAL** | `OPERATING_GUIDE.md` teaching/ownership section | Learning-by-Doing + Learning-Only Skills | Add compact depth-rationale rule; exact package depth maps remain local. |

### B. Engineering rationale, necessity, and audit thinking

| ID | Existing proven rule/pattern | Important existing source(s) | Disposition | Canonical owner / target | Skill application / reinforcement | Required redesign action |
|---|---|---|---|---|---|---|
| `RT-ENG-001` | Separate **current implementation fact**, **rationale/failure mode**, **engineering judgment**, and **authority boundary**. Source/tests prove what exists, not why it is correct or whether it should remain. | B2 contract §§3–4; Core `JUST-*`; `OPERATING_GUIDE.md` §4.1 | **PROMOTE GLOBAL** | `OPERATING_GUIDE.md`, with `JUST-*` remaining normative retention owner | Learning-by-Doing, Audit, Planning, Build, Learning-Only Skills | Add compact global reasoning distinction. |
| `RT-ENG-002` | Never invent a design rationale. If evidence establishes current behavior but not original/valid rationale, say `uncertain` and inspect further. | B2 contract §§2,4–5,10 | **PROMOTE GLOBAL / DELIBERATE REINFORCEMENT** | `OPERATING_GUIDE.md` | Learning-by-Doing + Audit Skills; Learning-Only when current code is being taught | Make explicit. |
| `RT-ENG-003` | When asked “why is X needed?”, answer through proposition/design goal → necessity class → correct owner/layer → evidence → alternatives/tradeoff, not “because the code uses it.” | B2 contract §4.1 | **PROMOTE GLOBAL** | `OPERATING_GUIDE.md` reasoning method | Audit, Planning, Build, Learning-by-Doing, Learning-Only Skills | Add compact global protocol; Skills apply proportionately. |
| `RT-ENG-004` | Necessity vocabulary: proposition-essential / current-implementation requirement / defensive-boundary hardening / uncertain-audit-needed. | B2 contract §4; depth index §3 | **PROMOTE GLOBAL as reasoning vocabulary, not product enum** | `OPERATING_GUIDE.md` | Audit/Learning-by-Doing/Learning-Only; Build/Planning when design necessity is questioned | State that labels are reasoning aids; Core `JUST-*` remains normative. |
| `RT-ENG-005` | Learning may include proportionate engineering audit, but every learning step must not become a formal repository audit. | B2 contract §5; Learning-by-Doing Skill | **KEEP GLOBAL** | `OPERATING_GUIDE.md` + operation routing in `AGENTS.md` | Learning-by-Doing Skill; full Audit Skill only when materially evaluative/explicit | Preserve. |
| `RT-ENG-006` | For overlapping evidence, identify what each artifact directly establishes, where information overlaps, what is primary/derived, what the implementation consumes, and what none proves alone. | B2 contract §6; Core proof/authority discipline | **APPLY IN SKILL** | Core specification owns evidence invariants; no new global prose owner required | Audit Skill primarily; Learning-Only when teaching multi-artifact evidence | Add to Group 3 audit procedure; avoid always-on expansion. |
| `RT-ENG-007` | Label materially different example states: normal path, invalid/failure state, test fixture, hypothetical design case, synthetic teaching example. Do not teach a defensive/test-only failure as normal operation. | B2 contract §7 | **APPLY IN SKILL** | `OPERATING_GUIDE.md` supplies truthfulness/evidence principle | Learning-by-Doing + Learning-Only Skills | Add compact example-state heuristic; do not globalize package terminology beyond these generic classes. |

### C. Source, tests, mutation, and debugging ownership

| ID | Existing proven rule/pattern | Important existing source(s) | Disposition | Canonical owner / target | Skill application / reinforcement | Required redesign action |
|---|---|---|---|---|---|---|
| `RT-SRC-001` | Source ownership requires reading executable constructs, not docstrings/comments/AI summaries alone. | B2 contract §10; Career handoff Rule 2 | **PROMOTE PART / KEEP DETAIL LOCAL** | `OPERATING_GUIDE.md` global ownership principle + source truth owners | Learning-by-Doing, Build, Learning-Only Skills | Skills should orient from comments but require executable reconstruction for material source ownership. |
| `RT-SRC-002` | A material code-bearing ownership block should connect source to at least one meaningful focused test when one exists; if no meaningful test exists, say so. | B2 contract §§10–11; Career handoff Rule 3 | **PROMOTE GLOBAL** | `OPERATING_GUIDE.md` teaching/ownership section | Learning-by-Doing, Build, Learning-Only Skills | Add compact global rule; Build/Learning-Only apply concretely. |
| `RT-SRC-003` | Before an ownership-bearing mutation, Ali forms a pre-change model: what changes, why this owner, what remains unchanged, expected result/proof boundary. | Career handoff §3C and Rule 4 | **PROMOTE PART / KEEP DETAIL LOCAL** | `OPERATING_GUIDE.md` ownership principle | Build Skill + Learning-by-Doing overlay | Group 5 must operationalize. No forced learner ceremony for tiny changes. |
| `RT-SRC-004` | After AI-assisted implementation, inspect the actual diff/source/test/result and compare it with the pre-change model. | Career handoff §3C and Rule 5 | **PROMOTE PART / KEEP DETAIL LOCAL** | `OPERATING_GUIDE.md` evidence/ownership principle | Build Skill + Learning-by-Doing overlay | Group 5 must operationalize. |
| `RT-SRC-005` | A real unexpected failure is a diagnosis opportunity; before immediate repair, form a hypothesis and discriminating check when safe/practical. Never manufacture failures for evidence. | Career handoff §3D and Rule 6; `OPERATING_GUIDE.md` §11 | **KEEP GLOBAL / APPLY IN SKILL** | `OPERATING_GUIDE.md` debugging | Build + Learning-by-Doing/Learning-Only when debugging | Group 5 reinforces; preserve no-manufactured-failure rule. |
| `RT-SRC-006` | Existing source/tests/callers are migration/regression evidence, not automatic architecture/retention authority. | Core `JUST-001..005`; `OPERATING_GUIDE.md` §§4.1–4.2; B2 contract | **KEEP GLOBAL / DELIBERATE REINFORCEMENT** | Core specification normative owner | Root, Audit, Planning, Build, Learning-by-Doing where retention is material | Preserve current deliberate reinforcement. |
| `RT-SRC-007` | Cross-layer ownership requires producer → integration/composition → consumer trace and earliest sufficient owner; later duplication needs independent justification. | Core `JUST-004`; `OPERATING_GUIDE.md` §4.2; B2 contract/learning findings | **KEEP GLOBAL / DELIBERATE REINFORCEMENT** | Core specification normative owner | Root + Audit/Planning/Build Skills | Preserve. |

### D. Source clarity and naming

| ID | Existing proven rule/pattern | Important existing source(s) | Disposition | Canonical owner / target | Skill application / reinforcement | Required redesign action |
|---|---|---|---|---|---|---|
| `RT-CLR-001` | Source clarity acceptance should be outcome-based: responsibility/orientation, data flow, input/output ownership, non-obvious reasoning, semantic/proof transformations, selective educational depth, truthfulness/maintenance. | redesigned `OPERATING_GUIDE.md` §6; former Source Clarity contract | **KEEP GLOBAL** | `OPERATING_GUIDE.md` | Build + Audit Skills | Preserve seven outcomes. |
| `RT-CLR-002` | Detailed Source Clarity heuristics remain useful: START-HERE map, bidirectional flow, import/domain-role explanation, constants/regex, why-comments, layered explanation, representative shapes, primary API, grouping, typing/narrowing, guard permissions, semantic algorithms, terminology collisions, current/transitional/legacy lifecycle. | pre-redesign `OPERATING_GUIDE.md` `SOURCE-CLARITY-001..022` | **APPLY IN SKILL** | Global outcomes remain in `OPERATING_GUIDE.md`; Naming spec remains naming owner | Build Skill primarily; Audit Skill as review lenses | Group 5 must preserve these as optional heuristics rather than restoring the 22-rule universal checklist. |
| `RT-CLR-003` | Names carry responsibility before comments compensate; one concept should have one clear term; important domain terms receive practical explanation. | Naming Clarity spec `NAME-001..012`; B2 teaching rules | **KEEP GLOBAL** | Naming Clarity specification | Build/Audit/Planning/Learning Skills as relevant | Preserve; do not copy full naming spec into Skills. |

### E. Planning, audit artifacts, context, and agent governance

| ID | Existing proven rule/pattern | Important existing source(s) | Disposition | Canonical owner / target | Skill application / reinforcement | Required redesign action |
|---|---|---|---|---|---|---|
| `RT-OPS-001` | Primary operation controls authorization; Learning-by-Doing normally overlays it; Learning-Only explicitly pauses product mutation. | `AGENTS.md`; `OPERATING_GUIDE.md`; Learning-by-Doing Skill | **KEEP GLOBAL / DELIBERATE REINFORCEMENT** | `AGENTS.md` action/operation router | All operation Skills | Preserve. |
| `RT-OPS-002` | Plans own bounded sequence/proof/stop scope; they do not own mission, live state, accepted product invariant, durable method, or implementation truth. Reference specifications/ADRs rather than re-specify them. | `plans/README.md`; Group 4 plan | **KEEP GLOBAL** | `plans/README.md` | Planning Skill | Group 4 operationalizes. |
| `RT-OPS-003` | Audit records are non-controlling and proportional; reuse existing audit, create durable record only when future review value warrants it. | `audits/README.md`; B2 contract §5 | **KEEP GLOBAL** | `audits/README.md` | Audit Skill | Group 3 operationalizes. |
| `RT-OPS-004` | Use smallest sufficient context; procedure/owner/evidence are loaded just in time; do not scan history/proposals/archives reflexively. | `AGENTS.md`; `OPERATING_GUIDE.md`; prior agent-governance plan | **KEEP GLOBAL** | `AGENTS.md` + `OPERATING_GUIDE.md` within their responsibilities | All Skills | Preserve. |
| `RT-OPS-005` | Repeated task-specific procedure belongs in an Agent Skill when justified; Skill is procedural/non-controlling and must not duplicate standing authority. | `AGENTS.md`; prior agent-governance plan; existing Skills | **KEEP GLOBAL** | `AGENTS.md` | All Skills | Preserve and validate in Group 7. |
| `RT-OPS-006` | Governance changes need behavior regression cases that grade trajectory/action properties rather than one exact prose answer. | prior agent-governance plan; `tools/agent-governance/cases.json` | **KEEP GLOBAL** | `tools/agent-governance/` governance harness | Group 7 + each group adds relevant cases | Preserve. |
| `RT-OPS-007` | Objective governance relationships should be deterministic checks; fuzzy semantic consistency belongs in audit/reasoning rather than brittle regex. | redesign plans; governance doctor boundary | **KEEP GLOBAL as redesign architecture** | `tools/agent-governance/` for deterministic checks; Audit Skill for semantic consistency | Group 7 | Implement in Group 7. |

### F. Package-local / overlay rules that should **not** be globalized

| ID | Existing local rule/pattern | Source | Disposition | Why it stays local |
|---|---|---|---|---|
| `RT-LOC-001` | Exact S001 → S011 → S005 learning/transfer route. | B2 contract and plans | **KEEP PACKAGE-LOCAL** | It is a B2 dependency/CI learning sequence, not a project-wide teaching invariant. |
| `RT-LOC-002` | Exact uv/`pyproject.toml`/GitHub Actions/tox/BFS technology-depth assignments. | B2 contract §13 and depth maps | **KEEP PACKAGE-LOCAL** | External-technology depth depends on the current package responsibility. |
| `RT-LOC-003` | A–N standard B2 chunk sequence and GREEN/YELLOW/RED package gate notation. | B2 contract §§9–10 | **KEEP PACKAGE-LOCAL** | The general principles are reusable; the exact chunk template would over-ceremonialize normal work. |
| `RT-LOC-004` | Evidence-strength labels `0 OBSERVED` through `7 EVALUATED`. | B2 contract §18 | **KEEP PACKAGE-LOCAL** | Useful teaching vocabulary for this evidence-heavy package; global owners already require observation/interpretation/proof separation without another universal enum. |
| `RT-LOC-005` | Exact B2 plan/depth-map pairs and `LEARNING_MEMORY.md` continuation. | B2 depth index/plans/memory | **KEEP PACKAGE-LOCAL** | They own package route/depth/learning state. |
| `RT-LOC-006` | Career Day-30 four evidence classes and later Career reassessment requirement. | `CAREER_DAY30_OWNERSHIP_HANDOFF.md` | **KEEP OVERLAY-LOCAL** | Career evidence is not UpgradePilot technical authority. General ownership principles may be promoted, but Career quotas/status must not control ordinary project work. |
| `RT-LOC-007` | “Two consecutive substantive sessions without executable contact” drift breaker. | Career handoff Rule 8 | **KEEP OVERLAY-LOCAL** | Useful for the specific Career correction, but globally enforcing it could incorrectly block legitimate multi-session governance/architecture responsibilities. |

---

## 5. Immediate promotions required before Group 3

The traceability pass found that Groups 1–2 preserve most proven global behavior, but several high-value B2 rules deserve stronger generic representation before later Skills are built.

### Promote into `OPERATING_GUIDE.md`

Compactly add:

1. `RT-ENG-001` — implementation fact vs rationale vs engineering judgment vs authority boundary;
2. `RT-ENG-002` — never invent rationale;
3. `RT-ENG-003` / `RT-ENG-004` — “why is X needed?” protocol and necessity vocabulary as reasoning aids;
4. `RT-LBD-005` — fair learner checkpoint rule;
5. `RT-LBD-010` — material depth assignments need project-local justification;
6. `RT-SRC-002` — material source ownership should connect to a meaningful focused test when one exists.

These belong in the everyday Learning-by-Doing owner because they recur across Audit, Planning, Build, and Learning-Only.

### Reinforce/apply in the Learning-by-Doing Skill

The Skill should explicitly operationalize:

- the `why is X needed?` reasoning path without inventing rationale;
- example-state labeling when a fixture/hypothetical/failure could be mistaken for normal behavior;
- fair checkpoints;
- depth rationale;
- source ↔ focused-test coupling for material source-ownership work.

Do not copy the B2 contract wholesale.

---

## 6. Mandatory inputs for Groups 3–7

### Group 3 — Audit / Review

Must consume at least:

```text
RT-LBD-007
RT-ENG-001..007
RT-SRC-006..007
RT-CLR-001..003
RT-OPS-003..004
```

The Audit Skill should become the main procedural home for overlapping-evidence analysis, explicit rationale/necessity evaluation, `JUST-*`, producer/integration/consumer tracing, cross-owner consistency, and proportional durable audit records.

### Group 4 — Planning / Design

Must consume at least:

```text
RT-LBD-005, RT-LBD-007, RT-LBD-010
RT-ENG-001..004
RT-SRC-006..007
RT-OPS-002, RT-OPS-004
```

Planning must not design from unexplained names, preserve existing mechanisms by inertia, or ask Ali to choose among alternatives before the decision model is understandable.

### Group 5 — Build / Implement

Must consume at least:

```text
RT-LBD-005, RT-LBD-008..010
RT-ENG-001..004
RT-SRC-001..007
RT-CLR-001..003
RT-OPS-004
```

Group 5 is where pre-change model, actual post-change diff inspection, source↔test coupling, real-failure diagnosis, and the former Source Clarity heuristics must be operationalized without turning them into universal checklists.

### Group 6 — Learning Only

Must consume at least:

```text
RT-LBD-001..010
RT-ENG-001..007
RT-SRC-001..002, RT-SRC-005..007
RT-OPS-004
RT-LOC-001..007 as locality constraints
```

The B2 package is the primary compatibility test. The universal Skill should discover and obey its contract/plan/depth/memory architecture rather than copy or replace it.

### Group 7 — Consistency / Validation / Cleanup

Must verify:

- every `PROMOTE GLOBAL` row has a real canonical owner;
- every `APPLY IN SKILL` row appears in the appropriate admitted Skill or has an explicit evidence-backed reason not to;
- deliberate reinforcement points to its owner and has not become an independent conflicting contract;
- package-local rows remain local unless new evidence justifies promotion;
- no old Source Clarity rule family with material value was silently lost;
- behavioral cases exercise the most failure-prone promoted rules.

---

## 7. Rule-migration acceptance test

Before declaring a redesign group complete, ask:

```text
What existing rule families did this group touch?
→ Which matrix IDs apply?
→ Where is each rule's canonical meaning now?
→ Which Skill applies it?
→ Is any repetition deliberate and owner-linked?
→ Did any package-specific detail accidentally become universal?
→ Did any proven rule disappear without an explicit disposition?
```

A group fails traceability if an important existing rule is removed, weakened, or relocated without a documented owner/disposition.

This requirement is about semantic preservation and correct activation, not word-for-word preservation.

---

## 8. Relationship to later cleanup

This matrix may eventually become historical planning evidence after the redesign is fully validated and merged. It is not intended to become another permanent always-on control.

Once Group 7 proves that the final owners/Skills/checks cover the accepted dispositions, retain this file as redesign provenance or archive it according to normal plan-history rules. Do not keep it loaded during ordinary UpgradePilot work.
