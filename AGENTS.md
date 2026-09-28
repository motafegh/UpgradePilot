# Agent Instructions — UpgradePilot

## **Smart Situational Override Rule**

Apply UpgradePilot's project-local procedures, gates, plans, Skills, defaults, and stop lines with engineering judgment rather than mechanically.

When current evidence, product responsibility, risk, complexity, learning state, or proof needs make the normal route materially worse than a justified alternative, adapt it proportionately. A material override should make explicit:

```text
circumstance / evidence
→ normal route
→ why the normal route is worse here
→ chosen override
→ effect on scope / proof / risk / learning / ownership
→ required reconciliation
```

Record material overrides in the active cycle working memory or correct owner. The rule does not create authorization, change evidence truth, or silently redefine an accepted specification/ADR/plan responsibility. Security/trust/credential/external-action boundaries remain owned by `SECURITY.md`, and higher-authority constraints plus Ali's explicit authorization remain controlling.

Unless explicitly stated otherwise, project-local `MUST`, `REQUIRED`, `DO NOT`, `NEVER`, `STOP`, `GATE`, fixed ordering, slice size, and routing language are interpreted under this rule.
## Mandatory canonical Learning-by-Doing loop / cycle

UpgradePilot remains a learning-by-building flagship at the project-identity level. Its default **operating and teaching method** for substantive project work is Learning-by-Doing.

When Ali says **`loop`**, **`cycle`**, **`LbD loop`**, or **`LbD cycle`** without naming some other procedure, interpret those words as the canonical progression **A0 → A1 → A2 → B → Verification → D → E**, with **C active continuously across the whole cycle**. A remains the pre-work learning/orientation responsibility, now made explicit as A0/A1/A2; C remains canonical state preservation, but it is cross-cutting rather than a sequential stop. This vocabulary is deliberately kept near the top of `AGENTS.md` so any AI agent can recover the expected working rhythm before entering project details.

For every **substantive** UpgradePilot slice, this loop is not optional background style; it should normally be completed before silently moving to the next slice. Selecting Audit, Planning/Design, Build/Implement, debugging, testing, or review as the primary operation does **not** switch the method off. The primary operation still owns authorization and detailed procedure; this loop owns the project-level learning/building rhythm. `OPERATING_GUIDE.md` remains the canonical broader method owner, and `.agents/skills/upgradepilot-learning-by-doing/SKILL.md` remains the reusable full procedural overlay when explicitly invoked or materially useful.

Use the following cycle proportionately.

### Canonical phase gates and cadence

The canonical cycle is a **learning/ownership and engineering progression**, not a generic project-management checklist. Apply it under the **Smart Situational Override Rule**. The normal route is deliberately strong because substantive UpgradePilot cycles commonly begin in a fresh conversation; unusual trivial or continuous-context cases may be compressed only when the situation justifies it explicitly.

```text
A0 — CURRENT-STATE RECONCILIATION + CYCLE INITIALIZATION
     Reconstruct the real current state from the live owner and the evidence needed for this
     responsibility: applicable governance, controlling plan/spec/ADR, previous cycle/handoff,
     material recent commits/parallel work, and relevant current source/tests.
     Reconcile stale or contradictory state before teaching or acting.
     Create the single cycle working-memory record and seed a living A-phase
     orientation/learning map for A1/A2.
     If fresh evidence invalidates the expected route, reconcile the route first.
     → continue directly to A1.

A1 — CONTINUITY / RECENT-WORK ONBOARDING
     Bring Ali from the last genuinely understood point to the actual current state.
     Explain the meaningful work, decisions, discoveries, corrections, proof and changed
     assumptions that matter for the present cycle; record material understanding gaps.
     ↓
     CONTINUITY / ONBOARDING GATE — STOP
     Do not continue to A2 until Ali has had a meaningful opportunity to question, challenge,
     correct, or explain the current-state model.

A2 — UPCOMING RESPONSIBILITY ORIENTATION
     Bridge the established current state to the upcoming responsibility. Teach proportionately
     what will be built/changed/investigated/proved, why it is needed, the important engineering
     concepts/files/types/data/control/evidence flow, expected result, meaningful failure or
     unresolved states, acceptance/proof boundary and explicit non-goals.
     A2 is anticipatory and minimum-complete; it is normally lighter than D.
     ↓
     PRE-B UNDERSTANDING GATE — STOP
     Do not begin substantive B until Ali understands what B will do, why it belongs there,
     the important engineering/proof boundaries, and what the work will and will not establish.

B — REAL BOUNDED BUILD / ACTION
     Perform the authorized coherent responsibility: implement/code/test/debug/analyze/design/
     audit/review as selected. Avoid both oversized semantic batches and ceremonial micro-work.

VERIFICATION / EVIDENCE GATE
     After B has a result, run or inspect the strongest focused/broader proof justified by the
     responsibility. If proof fails or is unavailable, remain in B/diagnosis/repair (or preserve
     explicit proof debt/blocker) rather than presenting the result as accepted.

D — POST-WORK EVIDENCE-BACKED LEARNING / OWNERSHIP
     After sufficient verification, teach from what actually happened: real source/result,
     control/data/evidence flow, decisions, failures/surprises/corrections, tests/evidence and
     proof limits. Compare A2 expectations with reality. Prefer teaching examples in this order:
     existing real project/product-simulation cases → suitable external real cases → synthetic
     examples only when real cases are unavailable or impractical. Choose depth situationally:
     deeper for new architecture/proof/trust boundaries, moderate for meaningful familiar work,
     compact for repetitive/simple work. Check ownership with a small number of meaningful
     reasoning questions and identify/characterize material gaps for E.

E — GAP REPAIR + CYCLE CLOSURE / NEXT-RESPONSIBILITY HANDOFF
     Repair important D gaps or preserve them explicitly as deferred. Consolidate what the cycle
     established and did not establish, residual limitations/debt and proof state. Identify or
     confirm the next responsibility and briefly state why it is next; do not perform the next
     cycle's full orientation/teaching here. Reconcile MEMORY.md and other owners only when
     their responsibility changed, then close the cycle.
     ↓
     STOP — CYCLE CLOSED

C — CONTINUOUS STATE PRESERVATION
     C is active from A0 through E. Preserve the meaningful engineering and learning progression
     in the single cycle working-memory record: current-state reconciliation, onboarding gaps,
     orientation decisions, implementation evolution, failures/corrections, verification,
     ownership findings, gap repair and handoff. Continuous preservation is not continuous
     logging; summarize routine activity and retain only what helps reconstruct the real path.
```

For each substantive cycle, maintain **one coherent cycle working-memory record** created in A0. That record is the normal detailed owner of A0/A1/A2/B/verification/D/E status plus continuous C preservation. Higher-authority plan/ADR/specification owners remain separate and change only when their own responsibility changes; `MEMORY.md` remains the sole live-position owner.

A0 is complete when current state is sufficiently reconciled, the cycle record exists, and its A-phase learning/orientation map is grounded in current evidence. A1 is complete only after the continuity gate. A2 is complete only after the pre-B understanding gate. D identifies and characterizes material ownership gaps; E owns their repair/defer decision and truthful cycle closure.
### Slice sizing and adaptation

A good slice is the **smallest coherent responsibility that can be oriented, performed, evidenced, preserved, learned, and handed off meaningfully**. Do not batch several architectural/semantic responsibilities merely for speed, and do not split one obvious implementation into meaningless file-by-file ceremony.

The loop is adaptive rather than rigid:

- for non-Build work, B means the real bounded primary operation rather than literal coding;
- tiny familiar/repetitive or genuinely continuous-context child steps may compress A0/A1/A2/D/E under the Smart Situational Override Rule while preserving their intent;
- a new architecture boundary, proof model, failure mechanism, or consequential implementation may need a deeper D stage;
- if Ali explicitly asks to pause implementation and learn, obey the Learning-Only boundary instead of forcing B;
- if the required verification/evidence gate cannot be executed now, keep the cycle at B / the verification gate, preserve the proof debt continuously in C, and pause if needed. Later validation resumes that same cycle gate; advance to D only after the result is sufficiently evidenced. Never rename missing proof as successful completion.

### Product-responsibility balance and plan challenge

Bounded work is a method for controlling complexity and proof, **not** permission to shrink UpgradePilot's real product responsibility until an easy test passes. Keep the selected slice connected to the accepted project/product responsibility, end-to-end evidence path, and foreseeable next capability.

Plans, working memories, and previously selected boundaries are important coordination and evidence artifacts, but they are not instructions to follow mechanically when new reasoning or evidence exposes a better route. Respect higher-authority owners, accepted specifications/ADRs, current authorization, and explicit stop lines; within those constraints, actively challenge a plan or local design when a better, simpler, safer, more general, or more product-faithful approach becomes credible. If the improved route materially changes the selected plan, scope, proof obligation, or accepted design responsibility, return to the proper Planning/Design/owner boundary and update it before implementing the changed route rather than silently deviating or blindly continuing.

When proposing a deliberately narrow increment, explain proportionately **before asking Ali to approve the consequential trade-off**:

```text
full product responsibility relevant to this decision
→ capability included in the proposed slice
→ important cases/capabilities/evidence excluded or deferred
→ why the narrowing is technically justified rather than merely convenient
→ whether the exclusion is temporary, intentionally unsupported, or outside product scope
→ what evidence/condition would justify later expansion or re-entry
```

Do not equate “smallest coherent slice” with “smallest implementation that can pass.” A narrow first increment is good only when it remains an honest step toward the real responsibility and its omissions are explicit.

Ali is learning many project concepts while the system is being built. Do not offload expert balancing decisions onto him before the necessary mental model exists. For a consequential choice involving unfamiliar concepts, first teach the minimum decision-relevant model, show the credible alternatives/trade-offs and product consequences, state your engineering recommendation when warranted, and then involve Ali at the point where he can meaningfully challenge or choose. Routine technical judgments may be made directly inside an accepted responsibility, but consequential narrowing, responsibility changes, or architecture/proof trade-offs must not be disguised as simple approval questions.

### Working-memory reflection

A substantive cycle's working-memory record is created during A0 and remains the one coherent progression owner until E closes the cycle. Keep a compact visible status such as:

```text
Cycle <coherent responsibility>
A0 — DONE / CURRENT / PENDING / DEFERRED: <current-state reconciliation + cycle initialization>
A1 — DONE / CURRENT / PENDING / DEFERRED: <continuity/onboarding + gate result>
A2 — DONE / CURRENT / PENDING / DEFERRED: <upcoming responsibility orientation + gate result>
B — DONE / CURRENT / PENDING / DEFERRED: <real bounded work result>
Verification gate — GREEN / FAILED / BLOCKED / PENDING: <exact proof>
D — DONE / CURRENT / PENDING / DEFERRED: <evidence-backed learning + ownership findings>
E — DONE / CURRENT / PENDING / DEFERRED: <gap repair + closure/handoff>
C — CONTINUOUS / DONE: <meaningful engineering + learning progression preserved across A0→E>
```

The A0 learning/orientation map is a **living cycle aid**, not a second plan. It may be refined when A1 exposes a gap or when current evidence changes what A2 must cover.

Update C at meaningful progression points across the whole cycle, not after every message or command. Preserve decisions, changed understanding, failures/corrections, proof/non-proof and handoff without turning working memory into a transcript.

The pre-work A2 orientation does not replace D. A2 teaches enough to act intelligently; D learns from the actual sufficiently evidenced result and normally goes deeper when the cycle creates important architecture, proof, trust or ownership value. E repairs the important D gaps and closes the cycle; it gives only a brief next-responsibility pointer because the next cycle's A0/A1/A2 owns fresh reconstruction, onboarding and teaching.
## Purpose

Operate UpgradePilot with one clear owner for each durable responsibility. Keep root context high-signal and route detailed procedure to the owner or Skill that actually needs it.

Use clear, direct English and precise technical terminology. `OPERATING_GUIDE.md` owns the fuller communication and working-method rules. Career is not the live project-control system unless Ali explicitly requests Career work.

## Authority and request-to-action boundary

Follow higher-authority constraints, then Ali's explicit instruction, then the nearest applicable local `AGENTS.md`. Within project-local procedure, apply the Smart Situational Override Rule.

Interpret requested action before mutation:

- **review / audit / explain / diagnose / compare / research** → read/inspect by default;
- **plan / design** → planning artifacts only unless implementation is also authorized;
- **change / implement / build / fix / refactor / update** → bounded in-scope mutation plus relevant non-destructive validation;
- **learning only** → product mutation paused;
- **material scope expansion** → do not infer authorization from the existing task.

Security-, privacy-, credential-, destructive-Git-, paid-action-, untrusted-content-, and external-target safeguards are owned by `SECURITY.md`; consult it whenever those boundaries are material.

## Responsibility ownership

| Responsibility | Normal owner |
|---|---|
| Mission, user, supported decision, product boundary, evidence doctrine, claim limits | `PROJECT_CHARTER.md` |
| Stage sequence/gates/outcomes | `plans/UPGRADEPILOT_90_DAY_PLAN.md` |
| Live position, latest material verification, blockers, continuation | `MEMORY.md` |
| Reusable machine/runtime facts and re-check rules | `ENVIRONMENT.md` |
| Security/privacy, credentials, untrusted evidence, destructive/external/paid action safeguards | `SECURITY.md` |
| Project-wide Learning-by-Doing method, communication, proportionality, debugging, evidence interpretation, handoff | `OPERATING_GUIDE.md` |
| Documentation/decision navigation and durable promotion lifecycle | `docs/README.md` |
| One bounded responsibility's scope/sequence/proof/stop line | selected file under `plans/` |
| Stable framework-independent technical behavior/invariants | accepted file under `docs/specifications/` |
| Technical impact/applicability/investigation/stopping semantics | `docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md` |
| Naming/terminology standard | `docs/specifications/UPGRADEPILOT_NAMING_CLARITY_SPECIFICATION.md` |
| Consequential implementation/structural method | ADR under `docs/architecture/` |
| Actual product behavior | `src/upgradepilot/`, active `tests/`, reproducible evidence |
| Non-product experiments/evaluations | `experiments/`, `experiments/tests/`, dated evidence |
| Developer diagnostics/live proofs | `tools/` |
| Hosted verification workflows | `.github/workflows/` |
| Reusable agent procedures | `.agents/skills/` |
| Durable non-controlling examination | `audits/` |
| Discovery evidence | `product-simulation/` and local controls |
| Dated execution/reasoning/handoffs | `working-memory/` |
| Reusable understanding/study artifacts | `learning/` |
| Unadmitted substantial ideas | `proposals/` |
| Historical implementation | `archive/` and Git history |
| Informal project story | `chronicle/` |

Agent Skills are procedural aids, not authority. They may orchestrate owners but may not supersede this file, another responsibility owner, or current user authorization.

## Operation routing

Choose one primary operation from the requested responsibility. The primary operation owns action authorization/detail; the canonical Learning-by-Doing cycle remains the default method for substantive project work.

| Operation | Route |
|---|---|
| **Audit / Review** | `.agents/skills/upgradepilot-repository-audit/SKILL.md` for substantive evaluative review; read-only unless change intent is explicit. |
| **Planning / Design** | `.agents/skills/upgradepilot-planning-design/SKILL.md` + relevant plan/spec/ADR owners; planning does not authorize implementation. |
| **Build / Implement** | `.agents/skills/upgradepilot-build-implement/SKILL.md` for substantive Build; tiny familiar reversible edits may use the compact root/Operating-Guide route. |
| **Learning by Doing** | Default method for substantive UpgradePilot work; full procedure in `.agents/skills/upgradepilot-learning-by-doing/SKILL.md`. |
| **Learning Only** | `.agents/skills/upgradepilot-learning-only/SKILL.md`; product mutation stays paused. |

Load a full operation Skill once per substantive responsibility, not for every child edit/test/command. Re-route only when responsibility, owner, risk, proof obligation, or selected mode materially changes.

Support Skills are conditional:

- `upgradepilot-project-reentry-orientation` — standalone read-only orientation when Ali wants status/re-entry **without yet entering a substantive LbD cycle**. Once a substantive cycle is being entered, A0/A1 own current-state reconstruction and onboarding; do not duplicate them with the re-entry Skill.
- `upgradepilot-learning-artifact` — only for requested durable study/relearning artifacts.
- `upgradepilot-workstream-supervision` — only for supervision/reconciliation of parallel workstreams.
- `upgradepilot-working-memory` — when creating/updating/closing the active working-memory record.

Normal local design judgment inside Build remains Build. If Build exposes a new substantive unresolved design responsibility, route that decision through Planning/Design before continuing implementation.

## Live state, artifacts, and executable boundaries

`MEMORY.md` is the **only** repository file permitted to state the live project position, blocker/deferral, selected continuation, and current handoff.

Choose artifact homes by responsibility. `docs/README.md` owns detailed documentation/decision navigation and the promotion lifecycle from dated evidence to durable owners. Do not create a competing owner when an existing owner fits.

Executable dependency direction:

```text
tests/             → src/upgradepilot/
experiments/       → src/upgradepilot/
experiments/tests/ → experiments/ + src/upgradepilot/
tools/             → src/upgradepilot/
```

Product runtime must not import `tests/`, `experiments/`, or `tools/`. Adopted experiment behavior belongs under `src/upgradepilot/` with product tests.

## Context discipline

Use the smallest sufficient context:

```text
nearest applicable AGENTS.md
→ applicable operation/support Skill
→ exact responsibility owner(s)
→ exact source/evidence required for the claim
```

Load `MEMORY.md` when live continuation matters, `ENVIRONMENT.md` when runtime/environment facts matter, and `SECURITY.md` when its trust/authorization boundaries matter. Load canonical plan/spec/ADR owners before reconstructing accepted decisions from dated history.

Do not speculatively scan archives, superseded plans, unrelated working memories, proposals, learning snapshots, or unrelated source/tests. History is for a precise provenance/comparison question, not normal orientation.

For substantive work, consult the relevant `OPERATING_GUIDE.md` sections when its owned Learning-by-Doing, communication, proportionality, debugging, evidence, Source-Clarity, assistance-fading, or handoff responsibilities are material.

## Critical persistent engineering safeguards

- Inspect active source/tests before editing executable behavior.
- Preserve unrelated work; make focused diffs. Ordinary development goes directly to `main` unless Ali explicitly selects another workflow.
- **Existing implementation is evidence, not retention authority.** Apply the Core specification's `JUST-*` invariants.
- Do not decide material cross-layer ownership from the local file alone; trace producer → orchestration/integration → consumer and identify the earliest sufficient owner.
- Direct internal callability or fabricated fixtures are not independent production contracts unless explicitly admitted and tested as such.
- Do not add dependencies, frameworks, package layers, top-level areas, or durable agent machinery without an authorized responsibility and simpler-baseline check.
- Keep product, experiment/evaluation, and developer-tool proof classes distinct.
- Material source changes must satisfy Source Clarity in `OPERATING_GUIDE.md` and the Naming Clarity specification.

## Implementation, validation, and claims

Use accepted specifications for stable behavior, accepted ADRs for consequential method/structure, and the selected bounded plan for execution/proof coordination. Older implementation/history is evidence, not automatic authority.

Use the proof owner appropriate to the claim: product claims require active product source/tests and reproducible evidence; experiment claims require experiment evidence; developer diagnostics require their own tool/output evidence.

Run narrow relevant checks before broader checks required by the selected responsibility. Do not claim more than the evidence establishes, including learner ownership from AI-generated work or passing tests alone.

## Instruction admission and maintenance

Keep always-loaded guidance limited to rules needed broadly. Put operation/responsibility-specific multi-step procedure in the scoped owner/Skill, prefer references over copied contracts, and avoid adding durable guidance that source/tests/tooling already make reliable.

Deliberate root reinforcement is justified only for repeated material failure/risk/high salience; keep reinforcement shorter than the canonical owner and remove it when the reason disappears.

## Updates

Update only the normal owner whose responsibility changed. One-run execution/validation evidence belongs in `working-memory/`; live continuation belongs only in `MEMORY.md`.
