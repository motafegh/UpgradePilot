# Workstream Supervision Skill — Research and Design Working Memory

Date: 2026-09-05  
Session status: ACTIVE  
Primary responsibility/mode: Planning/Design + bounded Repository-Audit composition + Working-Memory support  
Branch: `governance/engineering-supervision-skill-2026-09-05`  
Base revision: `0137837ac1fbfcfb6d86678ebe706284bdf4468a`  
Related plan: [`../plans/UPGRADEPILOT_WORKSTREAM_SUPERVISION_SKILL_RESEARCH_DESIGN_AND_ADMISSION_PLAN.md`](../plans/UPGRADEPILOT_WORKSTREAM_SUPERVISION_SKILL_RESEARCH_DESIGN_AND_ADMISSION_PLAN.md)

## 1. Session anchor

Ali wants a reusable UpgradePilot Skill for a recurring supervision pattern that happens while other AI agents/workstreams are progressing in parallel.

The intended use is broader than code review. Ali may start a fresh conversation and ask the supervising agent to understand one or several ongoing workstreams—coding, planning, research, proposals, Learning-by-Doing, Learning-Only, governance, testing, learning-artifact work, or another bounded responsibility—then independently check whether those workstreams are progressing in the right direction under UpgradePilot governance and the applicable Skills.

The supervising session should also help Ali understand and learn material decisions/mechanisms when useful, without forcing unnecessary lessons. If a material issue is found, Ali and the supervising agent should decide whether to instruct the active agent, continue watching, stop/reconcile, or perform a separately authorized correction in the supervision session.

This work is being developed separately from the current product/experiment implementation. It must not silently redirect or mutate R4-B or another active workstream merely because a supervision procedure is under design.

## 2. Starting design understanding

### 2.1 What this is not

The proposed responsibility is not merely another final code-review procedure and should not duplicate the existing Repository-Audit Skill.

Working distinction:

```text
Repository Audit / Review
→ materially evaluate a selected repository responsibility/finding under its own read-only operation procedure

Workstream Supervision
→ reconstruct and progressively supervise one or more parallel workstreams,
   determine which owners/operations/Skills apply,
   inspect process + result + evidence + project/learning fit,
   and decide proportionately whether intervention is needed
```

The exact final boundary remains subject to research and behavioral pressure testing.

### 2.2 Leading routing hypothesis

The leading hypothesis is that supervision should be a **support/composition Skill**, not a sixth primary operation.

Reasons:

- a supervised workstream may itself be Build, Planning, Audit, Learning-Only, Learning-by-Doing, research, proposal work, or another responsibility;
- supervision needs to route among or inspect those existing procedures rather than replace them;
- making supervision a universal primary operation risks competing with the existing authorization/operation system;
- UpgradePilot already has support/composition precedents such as Working-Memory and Learning-Artifact.

This is strengthened by the internal analysis below, but remains a hypothesis until external research and behavioral evaluation are complete.

### 2.3 Default authority boundary

Current agreement:

```text
supervision = read-only by default
```

Finding a problem does not itself authorize mutation or takeover.

Normal intervention sequence:

```text
establish finding + evidence
→ explain consequence to Ali
→ propose smallest justified intervention
→ Ali + supervising agent decide action
→ route any chosen correction through the proper operation/authorization
```

### 2.4 Workstream discovery

The supervising agent cannot see another agent's private hidden session/reasoning. Ongoing work must be reconstructed from the smallest sufficient observable evidence, such as:

- Ali's direct description of which workstreams matter;
- branches/commits/PRs when relevant;
- selected plans, specifications, ADRs, and other owners;
- `MEMORY.md` only when live continuation is material;
- relevant dated working-memory records;
- produced artifacts such as source/tests, plans, proposals, research outputs, learning artifacts, or governance changes;
- actual execution/runtime evidence where the claim requires it.

Because UpgradePilot already uses plans and working memory extensively, workstream reconstruction should normally reuse those surfaces instead of creating another tracker.

### 2.5 Multi-workstream requirement

Ali confirmed that one supervision session should be able to cover several parallel workstreams when he identifies them.

The procedure should first keep each workstream bounded, then inspect only material cross-workstream relationships such as:

- shared owner/spec/ADR pressure;
- dependency/order constraints;
- conflicting assumptions;
- duplicated work;
- incompatible changes;
- one workstream making another's evidence or stated state stale;
- working-memory/live-state collisions;
- responsibility crossing;
- research/learning conclusions that materially affect another workstream.

It should not create heavyweight multi-agent coordination merely because several agents exist.

## 3. Preliminary external-research signals already discussed

These are early signals only and must be revisited/sourced during the dedicated research phase.

### 3.1 Independent review patterns

Public agent/code-review patterns suggest useful principles such as:

- independent/read-only reviewer context;
- inspecting actual changes/evidence instead of trusting an implementer's summary;
- separating requirement/spec compliance from technical quality;
- reviewing at meaningful checkpoints rather than only at final completion;
- using specialized review lenses where needed instead of one undifferentiated reviewer.

These patterns appear useful but are narrower than the intended UpgradePilot supervision responsibility.

### 3.2 Continuous/loop supervision patterns

Current agent-engineering discussion contains a broader pattern of:

```text
observe/discover state
→ assess/act
→ verify
→ preserve relevant state
→ decide continue / escalate / stop
```

UpgradePilot should interpret this as bounded material checkpoints, not an endless autonomous monitoring loop.

### 3.3 Layered-supervision idea

A useful research direction is supervision distributed across:

- preventive guardrails/instructions;
- executable controls such as tests/validation;
- higher-level human/AI engineering judgment.

This potentially maps well to UpgradePilot governance owners + executable evidence + Ali/supervising-agent judgment, but needs proper research validation.

### 3.4 Skill-size warning

A repeated concern in current agent-Skill research is that large generic instruction bundles can add context cost or conflict with repository guidance. This reinforces pressure toward a small supervision core with conditional composition, but remains a research question rather than a frozen conclusion.

## 4. Repository/governance findings established so far

Current UpgradePilot governance already supplies most of the **deep procedures** that supervision will need:

- `AGENTS.md` owns authorization, responsibility routing, primary-operation routing, support/composition boundaries, and context discipline;
- `OPERATING_GUIDE.md` owns Learning-by-Doing, proportionality, context engineering, evidence interpretation, assistance/ownership, and handoff;
- Repository-Audit owns materially evaluative correctness/necessity/ownership/proof/governance inspection;
- Planning/Design owns unresolved design/scoping/sequence/proof questions;
- Build/Implement owns authorized mutation and validation;
- Learning-by-Doing owns the full teaching/reasoning/action/evidence/ownership overlay when useful;
- Learning-Only owns standalone mastery with mutation paused;
- Working-Memory owns dated execution/reasoning/evidence history;
- Learning-Artifact provides a precedent for a support/composition Skill that can compose with primary operations;
- the governance-evaluation system already separates deterministic structure, routing/activation observability, and behavioral trajectory;
- support-Skill behavioral banks already exist as a precedent, while deterministic routing-contract validation is not automatically generalized to all support Skills.

The current governance-quality probes also require new persistent agent machinery to demonstrate a recurring responsibility, routing distinctness, acceptable activation/context cost, behavioral coverage, and a simpler-baseline check.

A prior governance-evaluation plan explicitly warned against adding Skills merely for completeness. This new Skill must therefore prove incremental procedural value over root governance + existing operation/support Skills.

## 5. Plan and branch established

Branch:

```text
governance/engineering-supervision-skill-2026-09-05
```

Created from main revision:

```text
0137837ac1fbfcfb6d86678ebe706284bdf4468a
```

Plan commit:

```text
90f7a6cd3ef431d1caa76a5643121c58918592b3
```

Plan:

[`../plans/UPGRADEPILOT_WORKSTREAM_SUPERVISION_SKILL_RESEARCH_DESIGN_AND_ADMISSION_PLAN.md`](../plans/UPGRADEPILOT_WORKSTREAM_SUPERVISION_SKILL_RESEARCH_DESIGN_AND_ADMISSION_PLAN.md)

Execution sequence:

```text
internal analysis
→ define exact supervision gap
→ use-case pressure
→ external research
→ synthesis
→ design freeze
→ behavioral pressure cases
→ Skill authoring + minimal integration
→ representative validation
```

The final Skill name, exact vocabulary, and routing contract remain open.

## 6. Progressive record

### 2026-09-05 — working-memory preservation added

Ali explicitly requested that this investigation preserve analysis, discoveries, decisions, research, rejected ideas, and changed understanding progressively so nothing material is lost before final Skill authoring.

Decision:

- maintain one dedicated record while this responsibility remains coherent;
- update it at meaningful progression points rather than logging every search/tool call;
- keep the plan as sequence/proof/stop owner and this file as dated reasoning/evidence history;
- do not update `MEMORY.md` merely because this governance side responsibility exists unless canonical live project continuation changes.

### 2026-09-05 — internal Skill/governance gap analysis

Inspected the current root/Operating-Guide model plus the Planning/Design, Repository-Audit, Learning-by-Doing, Build/Implement, Learning-Only, Working-Memory, Learning-Artifact, governance-quality probes, and support-Skill behavioral-evaluation precedent.

#### Existing procedures already cover the deep work

The proposed Skill should **not** reproduce:

```text
cross-owner correctness / necessity / proof audit
→ Repository-Audit

design/scoping/sequence/proof decisions
→ Planning/Design

authorized edits and validation
→ Build/Implement

teaching during real project work
→ Learning-by-Doing + OPERATING_GUIDE

standalone mastery
→ Learning-Only

dated progression preservation
→ Working-Memory

reusable study artifacts
→ Learning-Artifact
```

This substantially narrows the genuine missing responsibility.

#### Exact procedural gap identified

No existing Skill currently owns the full recurring sequence:

```text
fresh supervision session
→ discover/reconstruct the named ongoing workstream(s)
→ establish each workstream's responsibility, expected route, owner set, evidence horizon, and current checkpoint
→ distinguish what the active agent claims from what observable repository/evidence establishes
→ select only the supervision lenses / existing procedures needed for this checkpoint
→ inspect process trajectory + produced result + proof + project/learning fit
→ compare material relationships across several workstreams when needed
→ keep Ali oriented/learning at the useful depth
→ decide whether no action, watch, guidance, intervention, or stop/reconciliation is justified
→ preserve a precise corrective prompt or handoff when intervention is chosen
→ continue supervision at the next material checkpoint without becoming the workstream's implementation owner
```

Repository-Audit can perform the evaluative core of an individual checkpoint, but it does not own workstream reconstruction, concurrent-workstream topology, progressive supervision cadence, intervention orchestration, or Ali-facing supervisory continuity.

#### Important two-level routing problem discovered

Supervision introduces a distinction not currently made explicit in the existing Skills:

```text
SUPERVISION SESSION ROUTE
what procedure/authorization this supervising conversation itself is executing

vs

SUPERVISED WORKSTREAM EXPECTED ROUTE
what operation/Skill/owners the other agent's work should be following
```

Example:

```text
supervising session
→ read-only supervision + bounded Repository-Audit

supervised workstream
→ Build/Implement + Learning-by-Doing + Working-Memory
```

The supervisor may need to inspect the Build Skill as the expected procedure for the *subject workstream* without thereby gaining Build mutation authority in the supervision session.

This creates a design question around terminology and Skill provenance: **consulting a Skill as the audited/expected procedure is not necessarily the same thing as activating that Skill as the current session's operation procedure.** The final design must make this distinction clear without weakening current provenance or authorization rules.

This is currently one of the strongest UpgradePilot-specific reasons a supervision Skill is useful.

#### Observable-process boundary

The supervisor cannot establish hidden reasoning or private tool usage from repository artifacts alone.

Process judgments therefore need evidence classes such as:

```text
observable artifact/commit/test/runtime evidence
claimed procedural provenance (for example UP-SKILL marker)
working-memory/agent-written reasoning record
inferred trajectory from observable changes
unobservable/private agent behavior
```

A marker or working-memory claim may strengthen reconstruction, but neither proves compliant behavior. The supervising Skill should avoid statements like "the agent followed Build correctly" when the evidence only shows a marker plus plausible artifacts.

#### Workstream map should be temporary, not a new state owner

A supervision session likely needs a compact per-workstream mental/context map such as:

```text
workstream identity
responsibility / allowed scope
expected operation + support Skills
canonical owners
observable evidence horizon
current checkpoint / unresolved claims
next meaningful proof or decision boundary
material dependencies on other supervised workstreams
```

This should normally live in conversation context (and this supervision working memory when intentionally maintained), not become a new repository tracker or competitor to `MEMORY.md`, plans, or workstream working memories.

#### Progressive supervision should use material checkpoints

The existing governance already rejects micro-step rerouting and continuous documentation. The supervision procedure should inherit the same principle:

Useful checkpoints may include:

- a plan/design gate closes;
- a material source slice lands;
- tests/proof become available;
- a working-memory handoff changes direction;
- an external research/proposal reaches a consequential conclusion;
- a blocker/failure changes the route;
- one workstream begins depending on another;
- the agent is about to cross a stop/authorization boundary.

Not useful by default:

- every commit;
- every test rerun;
- every minor wording edit;
- every agent message.

#### Learning role clarified

Ali's understanding is a supervision concern, but the new Skill should not own another teaching framework.

Expected composition:

```text
ordinary substantive supervision
→ default Learning-by-Doing method from OPERATING_GUIDE

material learn-while-supervising need
→ compose full Learning-by-Doing when useful

Ali explicitly pauses everything to master a subject
→ Learning-Only becomes the selected primary learning route
```

Likewise, auditing a Learning-Only workstream does not automatically make the supervising conversation itself Learning-Only.

#### Intervention boundary clarified

The new Skill should own **supervisory judgment and handoff**, not corrective mutation.

A likely informal decision vocabulary remains:

```text
CONTINUE
CONTINUE / WATCH
GUIDE BEFORE NEXT MATERIAL STEP
INTERVENE NOW
STOP / RECONCILE
```

These are currently only communication/judgment aids. They should not become product enums, mandatory repository statuses, or a second workflow state machine without evidence.

If Ali chooses an intervention, the supervising Skill should produce the smallest precise instruction to the other agent or hand off to a separately authorized Planning/Audit/Build responsibility here.

#### Multi-workstream value is genuinely distinct

Existing operation Skills mainly reason about one selected responsibility. Supervision adds a cross-workstream layer that should be used only when several named workstreams are actually material.

The supervisor should first understand each stream independently, then inspect only material joins:

```text
shared semantic/method owner
one workstream invalidating another's assumptions/evidence
order/dependency pressure
conflicting edits or plans
responsibility overlap
state/working-memory conflict
duplicated investigation
research/learning conclusion that should alter another stream
```

This is coordination-by-evidence, not a new multi-agent runtime.

#### Evaluation precedent

`learning_artifact_cases.json` confirms a useful support-Skill evaluation pattern: natural-language positive routing, negative/non-trigger cases, composition with a primary operation, and explicit mutation boundaries can be tested behaviorally without first extending deterministic governance tooling.

Internal conclusion: the supervision Skill should likely receive its own focused behavioral bank **only if** the later design is admitted and the cases are sufficiently discriminating. Deterministic evaluator extension is not currently required merely to create the Skill.

## 7. Initial use-case pressure set

These are design inputs, not final behavioral cases yet.

### Case A — one active Build/Learning-by-Doing workstream

Ali opens a fresh session and asks to supervise an agent implementing a planned slice.

Supervisor must reconstruct plan/working-memory/diff/tests, determine expected Build/LbD route, independently inspect claims/proof, teach only material mechanisms, and either allow continuation or give a precise intervention. It must not automatically modify the agent's branch.

### Case B — planning/proposal work with no code

Another agent is writing a substantial plan or research proposal.

Supervisor must judge owner/scope/evidence/research quality and process alignment without forcing source-code/test review merely because the project is software engineering.

### Case C — Learning-Only workstream

Another agent is teaching current code under a Learning-Only pause.

Supervisor checks whether the teaching uses current real evidence, appropriate depth, fair ownership checkpoints, and no accidental Build; it does not itself switch to Learning-Only unless Ali requests mastery in the supervision session.

### Case D — multiple parallel workstreams

Ali names, for example, one implementation stream and one research/proposal stream.

Supervisor reconstructs both separately, then detects only material dependencies/conflicts. It must not merge them into one generic status report or invent a shared plan.

### Case E — agent report says green but evidence is weaker

Working memory/agent summary claims a gate is complete, while actual tests/runtime evidence prove less.

Supervisor must preserve report vs evidence distinction and intervene at the claim/proof boundary.

### Case F — issue found during supervision and Ali wants correction here

Supervision first establishes the finding. Only after Ali explicitly authorizes the correction does the session transition/compose into the proper Planning/Build operation. The supervision Skill itself never acts as mutation authority.

### Case G — trivial checkpoint

Ali asks whether a small routine workstream is still on track after a minor change.

Supervisor should use the smallest sufficient evidence and avoid full Audit/Skill loading/report ceremony when the answer is obvious and low-risk.

## 8. Current session route

Internal analysis is complete enough to proceed.

Next progression:

1. refine the above use-case pressure only if another materially distinct case appears;
2. conduct dedicated external research across official/vendor guidance, public Skills/workflows, GitHub, Reddit/X practitioner patterns, and recent research;
3. classify every useful external mechanism as `directly reusable`, `adaptable`, `incompatible`, `unnecessary`, or `UpgradePilot-specific gap remains`;
4. return to this working record with sourced findings before freezing the Skill design;
5. only after synthesis decide final name, activation/routing, supervision loop, lenses, intervention vocabulary, optional reference files, governance integration, and evaluation cases.

## 9. Open questions sharpened by internal analysis

- How should the final Skill express the **supervision-session route vs supervised-workstream expected route** distinction?
- When a supervisor reads another operation Skill as an evaluation contract, how should provenance be represented without falsely implying that operation is active for the supervising session?
- What is the minimal workstream-reconstruction shape that supports continuity without becoming another state artifact?
- When is a full Repository-Audit composition justified versus lightweight supervisory checking?
- Which external patterns best support independent reviewer context, checkpoint cadence, escalation/stop logic, and multi-workstream coordination?
- What evidence should distinguish `watch` from `guide/intervene` without turning judgment into rigid statuses?
- What final name covers coding, planning, research, proposals, learning, governance, and mixed work clearly?
- Does any external evidence justify a separate reference file, or can the Skill remain one compact procedure?
- What behavioral cases demonstrate incremental value specifically from supervision rather than from Audit alone?
- Should deterministic governance tooling remain unchanged initially, as current evidence suggests?

## 10. Current proof limits

Established:

- the recurring user need is explicit;
- the branch, plan, and working-memory trail exist;
- current governance supports support/composition Skills as a category;
- existing Skills already own most deep inspection/execution/learning procedures;
- a distinct meta-level gap exists around fresh workstream reconstruction, expected-route mapping, progressive checkpoint supervision, cross-workstream reasoning, Ali-facing supervisory continuity, and intervention handoff;
- a meaningful two-level routing/provenance issue exists and needs deliberate design;
- a support-Skill classification is now better supported by internal evidence than before;
- a focused support-Skill behavioral bank has an existing repository precedent.

Not yet established:

- final Skill admission after external research/evaluation;
- final name;
- exact activation language;
- exact two-level routing/provenance wording;
- final supervision loop/lenses/depth model;
- final intervention vocabulary;
- whether any reference file is justified;
- whether deterministic governance tooling should change;
- behavioral improvement versus current governance without the Skill;
- which external patterns materially improve the design.

## 11. Skill provenance

`UP-SKILL:upgradepilot-planning-design`  
`UP-SKILL:upgradepilot-repository-audit`  
`UP-SKILL:upgradepilot-working-memory`
