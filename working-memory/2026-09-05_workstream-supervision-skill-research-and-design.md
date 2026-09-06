# Workstream Supervision Skill — Research and Design Working Memory

Date: 2026-09-05  
Session status: ACTIVE — PRE-MERGE VALIDATION  
Primary responsibility/mode: Planning/Design → Build/Implement + bounded Repository-Audit + Workstream-Supervision composition + Working-Memory support  
Branch: `governance/engineering-supervision-skill-2026-09-05`  
Base revision: `0137837ac1fbfcfb6d86678ebe706284bdf4468a`  
Related plan: [`../plans/UPGRADEPILOT_WORKSTREAM_SUPERVISION_SKILL_RESEARCH_DESIGN_AND_ADMISSION_PLAN.md`](../plans/UPGRADEPILOT_WORKSTREAM_SUPERVISION_SKILL_RESEARCH_DESIGN_AND_ADMISSION_PLAN.md)

## 1. Session anchor

Ali wants a reusable UpgradePilot Skill for supervising meaningful work being performed in parallel by other AI agents/workstreams.

In a fresh conversation Ali may identify one or several ongoing or recently completed-but-not-reconciled workstreams—coding, planning, research, proposals, Learning-by-Doing, Learning-Only, governance, testing, learning artifacts, or mixed responsibilities. The supervisor should reconstruct each relevant stream, map it to the correct UpgradePilot owners/governance/Skills, independently inspect process + output + evidence, help Ali understand/learn material points, and decide proportionately whether the work should continue, be watched, be guided, be interrupted, or be reconciled.

Finding a problem does not itself authorize mutation. Ali and the supervisor decide whether to send a corrective prompt to the active agent, keep watching, pause/stop the stream, or transition this session into a separately authorized Planning/Audit/Build responsibility.

This governance work must not silently redirect or mutate the current product/experiment work merely because the supervision procedure is under design.

## 2. Repository/governance baseline

Current UpgradePilot governance already supplies most of the deep procedures supervision should reuse:

- `AGENTS.md` → authorization, responsibility ownership, operation routing, support/composition boundary, context discipline;
- `OPERATING_GUIDE.md` → Learning-by-Doing, proportionality, context engineering, evidence, assistance/ownership, stopping/handoff;
- Repository-Audit → material correctness/necessity/ownership/proof/governance evaluation;
- Planning/Design → unresolved design/scoping/sequence/proof decisions;
- Build/Implement → authorized mutation and validation;
- Learning-by-Doing → full teaching/reasoning/action/evidence/ownership overlay when useful;
- Learning-Only → standalone mastery with mutation paused;
- Working-Memory → dated progression/evidence/reasoning history;
- Learning-Artifact → precedent for a support/composition Skill.

Governance-quality probes require any new persistent Skill to demonstrate a recurring responsibility, distinct routing value, acceptable context cost, behavioral coverage, and a simpler-baseline comparison. Skills are procedural, not semantic authority.

## 3. Exact internal procedural gap

No existing Skill owns the complete recurring sequence:

```text
fresh supervision session
→ discover/reconstruct named ongoing workstream(s)
→ establish each responsibility, expected route, owners, evidence horizon, checkpoint
→ distinguish agent claims from observable evidence
→ select only needed supervision lenses / existing procedures
→ inspect process trajectory + produced result + proof + project/learning fit
→ compare material cross-workstream relationships when needed
→ keep Ali oriented/learning at useful depth
→ decide no action / watch / guidance / intervention / stop-reconcile
→ produce exact corrective prompt/handoff when chosen
→ continue at the next material checkpoint without becoming implementation owner
```

Repository-Audit can provide the evaluative core of an individual checkpoint, but it does not own fresh workstream reconstruction, concurrent-workstream topology, progressive supervision cadence, intervention orchestration, or Ali-facing supervisory continuity.

### 3.1 Two-level routing problem

A central UpgradePilot-specific distinction:

```text
SUPERVISION SESSION ROUTE
what this conversation is authorized/executing

vs

SUPERVISED WORKSTREAM EXPECTED ROUTE
what operation/Skill/owners the other agent should be following
```

Example:

```text
supervising session
→ Workstream Supervision + bounded Repository-Audit

supervised workstream
→ Build/Implement + Learning-by-Doing + Working-Memory
```

Reading Build as the subject stream's expected procedure must not grant this session Build mutation authority.

Therefore:

> Consulting another Skill as the **expected procedure/evaluation contract for the supervised workstream** is distinct from **activating/materially applying that Skill as this supervision session's procedure**.

Only the latter should produce that Skill's `UP-SKILL:*` activation marker.

### 3.2 Observable-process boundary

The supervisor cannot establish another agent's hidden reasoning or private tool usage merely from repository state.

Distinguish:

```text
observable artifact / commit / test / runtime evidence
claimed procedural provenance (e.g. UP-SKILL marker)
working-memory / agent-written reasoning record
inferred trajectory from observable changes
unobservable/private agent behavior
```

A marker or working-memory claim helps reconstruction but does not prove compliant behavior.

### 3.3 Workstream map is temporary

The session may maintain a compact mental/context map per stream:

```text
workstream identity
responsibility / allowed scope
expected operation + support Skills
canonical owners
claimed state
observable evidence horizon / verified state
current checkpoint / unresolved questions
next meaningful proof or decision boundary
material dependencies on other supervised streams
```

This is not a new repository tracker or live-state owner. Use existing plans, `MEMORY.md`, workstream working-memory, git/PR state, and artifacts.

### 3.4 Material checkpoint cadence

Useful checkpoints include:

- plan/design gate closure;
- material source slice landing;
- tests/proof becoming available;
- working-memory handoff changing direction;
- consequential research/proposal conclusion;
- blocker/failure changing route;
- one stream beginning to depend on another;
- imminent stop/authorization boundary.

Do not default to every commit, test rerun, wording edit, or agent message.

## 4. External research synthesis

External sources are design evidence, not UpgradePilot authority. Official/vendor sources carry more weight than practitioner anecdotes.

### 4.1 Strong directly reusable principles

**OpenAI Codex review-agent** — independent read-only direct inspection of change, surrounding code, tests, and call sites:
<https://github.com/openai/codex/blob/main/codex-rs/skills/src/assets/samples/review-agent/SKILL.md>

**OpenAI Superpowers requesting-code-review** — fresh reviewer gets precisely crafted context and exact base/head SHAs, not the implementer's full session history:
<https://github.com/openai/plugins/blob/main/plugins/superpowers/skills/requesting-code-review/SKILL.md>

**GitHub Agent Skills guidance** — standing instructions vs detailed task-specific Skills; Skills are loaded when relevant:
<https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills>
<https://docs.github.com/en/copilot/concepts/agents/code-review>

**Anthropic Agent Skills** — composable, dynamically discovered procedural resources:
<https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills>

**Anthropic long-running agents** — fresh sessions recover from git history + structured progress files rather than guessing prior context:
<https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents>

**Anthropic agent evals** — distinguish trajectory from outcome; agent statement is not proof of environment outcome:
<https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents>

**OpenAI internal coding-agent monitoring** — monitor claims/actions against intent and evidence; monitoring is only one defense layer and depends on observability:
<https://openai.com/index/how-we-monitor-internal-coding-agents-misalignment/>

### 4.2 Closest public template components found

#### `muster` — best workstream discovery/reconstruction template

<https://github.com/howells/skills/blob/main/muster/SKILL.md>

It reconstructs concurrent/older work from several fallible sources, checks claims against live git/PR state, reports unavailable sources explicitly, and treats concurrency as the reason the procedure earns a Skill.

Useful UpgradePilot adaptation:

```text
Ali's description + relevant workstream records
→ live repo/branch/PR/artifact evidence
→ reconcile
→ bounded workstream brief
```

Do not copy its transcript/session APIs or its own status vocabulary; UpgradePilot already has plans, working-memory, `MEMORY.md`, and its own authority model.

#### XMemo `audit-progress` — best progress-claim reconciliation template

<https://github.com/yonro/xmemo-claude-plugin/blob/main/skills/audit-progress/SKILL.md>

Core sequence:

```text
baseline → claims → evidence → reconcile → verdict → checkpoint
```

It atomizes completion/progress claims and prevents source-agent identity from counting as evidence.

Useful UpgradePilot adaptation: explicitly separate reported progress from verified state and proof gaps. Do not import XMemo's memory model, status enums, or update API.

XMemo `resume-work` also reinforces fresh-session continuity via latest verified checkpoint + live evidence reconciliation:
<https://github.com/yonro/xmemo-claude-plugin/blob/main/skills/resume-work/SKILL.md>

#### `codex-orchestrator` — best verification/intervention structural template

<https://github.com/alexzh3/codex-orchestrator/blob/main/skills/orchestrate/SKILL.md>
<https://github.com/alexzh3/codex-orchestrator/blob/main/skills/orchestrate/references/review.md>

Useful mechanics:

- monitor without editing files owned by active agent;
- treat handoff as claims;
- inspect actual repository/evidence;
- evaluate acceptance criteria;
- send exact finding back on failure;
- use fresh reviewer only for material risk/distinct unresolved question;
- avoid repeated identical reviews.

Do not import its agent-launching, worktree, durable journal, or runtime orchestration machinery.

### 4.3 Adaptable patterns

**Superpowers subagent-driven-development** separates spec compliance from technical quality and has explicit breaker/escalation logic:
<https://github.com/openai/plugins/blob/main/plugins/superpowers/skills/subagent-driven-development/SKILL.md>

UpgradePilot generalization:

```text
trajectory / authorization / owner / requirement alignment
!=
artifact-specific quality
```

The artifact may be code, plan, proposal, research, governance, or learning—not necessarily software source.

**PAAD agentic-review** uses specialist lenses and verifies findings to reduce false positives:
<https://github.com/Ovid/paad/blob/main/plugins/paad/skills/agentic-review/SKILL.md>

Use only for consequential/high-risk checkpoints where distinct independent lenses add value; do not make multi-agent dispatch mandatory.

**Agent Audits** ties completion claims to current evidence and detects stale proof:
<https://github.com/aiswarya797/agent-audits/blob/main/agent-audits/SKILL.md>

Borrow `claim/criterion → current evidence → review → proof limit`; do not copy its mandatory CLI/ledger/hash machinery.

### 4.4 Proportionality and stopping evidence

Anthropic's March 2026 generator/evaluator harness produced stronger results on hard tasks but was >20× more expensive in one comparison (`$200` vs `$9`). With stronger models, the evaluator became unnecessary overhead for tasks inside the model's reliable solo capability and remained valuable near the capability boundary:
<https://www.anthropic.com/engineering/harness-design-long-running-apps>

Anthropic's parallel C-compiler work found parallelism useful for independently discriminable work, but many agents duplicated/overwrote each other on one tightly coupled task until the environment/verifier was redesigned:
<https://www.anthropic.com/engineering/building-c-compiler>

A current X response to broad “agent loops” says “design state machines,” reinforcing explicit stopping/escalation rather than endless loops:
<https://x.com/dzhng/status/2063931263312892406>

Recent Reddit multi-agent discussions repeatedly identify reconciliation/stopping as harder than spawning agents and emphasize task/workstream ownership plus human architectural/final-merge judgment:
<https://www.reddit.com/r/ClaudeCode/comments/1udrdgy/is_anyone_here_actually_using_multiagent_parallel/>
<https://www.reddit.com/r/ClaudeCode/comments/1uldb2g/how_i_stopped_my_parallel_claude_code_agents_from/>

These are practitioner signals, not authoritative evidence.

### 4.5 Skill effectiveness evidence

`SWE-Skills-Bench` evaluated 49 public SWE Skills: 39 had zero pass-rate improvement; average gain was +1.2%; token overhead reached +451%; some Skills hurt performance because guidance conflicted with repository context:
<https://arxiv.org/abs/2603.15401>

`SkillsBench` found curated Skills useful overall but software-engineering gains smaller (+4.5 percentage points), some tasks worsened, and focused Skills with 2–3 modules outperformed comprehensive documentation:
<https://arxiv.org/abs/2602.12670>

Current OpenAI model guidance warns that unclear/conflicting Skill guidance can cause blocking/divergence and recommends explicit priority and transparent identification of the Skill that changed behavior:
<https://developers.openai.com/api/docs/guides/latest-model>

Consequence: the supervision Skill must stay narrow at its true meta-responsibility and reuse existing procedures rather than restating them.

### 4.6 Rejected/unnecessary external mechanics

Do not copy by default:

- mandatory review after every task regardless of materiality;
- mandatory multi-specialist parallel review;
- automatic agent launching/management;
- durable orchestration journals/worktrees solely for supervision;
- mandatory evidence ledger/hashing for every workstream;
- endless reviewer/fix loops;
- automatic cross-agent messaging/merge/correction;
- worktree management as part of this Skill simply because parallel agents exist.

### 4.7 External-research conclusion

No public Skill/template found owns all of:

- fresh reconstruction of already-running external workstreams;
- work-type agnostic supervision;
- two-level supervision-session vs subject-workstream routing;
- UpgradePilot operation/support Skill composition without accidental authority activation;
- UpgradePilot plan/working-memory/evidence ownership;
- Ali's Learning-by-Doing ownership;
- proportional multi-workstream reconciliation;
- read-only-by-default intervention handoff decided with Ali.

Therefore the correct path is a small UpgradePilot-specific synthesis, not wholesale adoption.

## 5. Final design freeze for v1

The research/design gate is sufficiently resolved for a first Skill implementation on this branch.

### 5.1 Name

Use:

```text
upgradepilot-workstream-supervision
```

Reason: `workstream` covers code, planning, research, proposals, learning, governance, testing, and mixed responsibilities better than `engineering`, while remaining more concrete than a generic `supervision` name.

### 5.2 Category

**Support/composition Skill. Not a sixth primary operation.**

It may compose with the active supervision session's primary operation where genuinely needed, especially Repository-Audit for material evaluative checkpoints and Learning-by-Doing for substantial learn-while-supervising work.

### 5.3 Activation

Trigger when Ali explicitly or clearly asks to:

- supervise/check/watch work another AI agent/workstream is doing;
- review ongoing parallel agent work together;
- catch up on named workstreams and verify they remain on track;
- reconcile progress/results from several active agents;
- independently check another agent's process/result/evidence while keeping Ali oriented.

Do **not** trigger merely for:

- an ordinary one-off repository Audit/Review with no workstream-supervision responsibility;
- continuing this session's own ordinary Build/Planning task;
- general project status with no named other-agent/workstream supervision;
- automatic agent orchestration/dispatch.

Recently completed but not independently reconciled work may still qualify as a supervised workstream.

### 5.4 Authority

Read-only by default.

Supervision may recommend or draft an intervention. Mutation here requires separate user authorization and routing to the applicable operation. The Skill never inherits another workstream's mutation authority.

### 5.5 Core loop

```text
1. scope the supervised workstream(s)
2. reconstruct each stream from smallest sufficient observable evidence
3. map each stream's expected operation / support Skills / canonical owners
4. separate claims, observed facts, inference, uncertainty, and proof
5. choose proportional supervision depth + only relevant lenses
6. inspect each stream independently
7. inspect material cross-stream joins only when several streams are in scope
8. orient/teach Ali on material mechanisms or deviations when useful
9. decide continue / watch / guide / intervene / stop-reconcile
10. produce the smallest exact handoff/intervention if needed
11. preserve meaningful supervision progression only when justified
12. stop at the current material checkpoint; repeat later when new evidence changes the story
```

### 5.6 Supervision depth

Use plain-language depth, not new stable project codes:

- **light** — low-risk/familiar checkpoint with direct coherent evidence; no full Audit ceremony;
- **standard** — meaningful progress requiring route + artifact + evidence + learning/state check;
- **deep** — material discrepancy, architecture/owner/proof/security pressure, consequential novelty, or cross-workstream coupling; compose the appropriate deeper Skill/procedure.

Depth is a judgment aid, not a persisted status.

### 5.7 Selective lenses

Potential lenses; use only those material to the stream:

- authorization/scope;
- expected operation/Skill + canonical-owner alignment;
- process/trajectory and stop-line discipline;
- artifact-specific correctness/quality (delegate to existing Audit/Planning/Build/Learning procedures as appropriate);
- evidence/proof/claim strength;
- working-memory/live-state consistency;
- Learning-by-Doing / learner-ownership quality;
- proportionality/overengineering/underengineering;
- cross-workstream dependency/conflict/reconciliation.

The Skill should not duplicate the detailed checklist of any existing operation Skill.

### 5.8 Supervisory decision vocabulary

Allow optional concise judgments:

```text
CONTINUE
CONTINUE / WATCH
GUIDE BEFORE NEXT MATERIAL STEP
INTERVENE NOW
STOP / RECONCILE
```

They are not repository enums, gates, or automatic actions. The finding/evidence/consequence matters more than the label.

### 5.9 Intervention contract

When intervention is warranted:

```text
finding
→ evidence / uncertainty
→ why it matters before the next material step
→ smallest exact instruction or decision request
```

Prefer a precise prompt for the active agent when that is the natural owner of the repair. If Ali asks the supervision session to perform the repair, explicitly transition/compose into the proper authorized operation.

### 5.10 Provenance semantics

The new Skill gets:

```text
UP-SKILL:upgradepilot-workstream-supervision
```

Only emit a Skill's marker when that Skill is **actually activated/materially applied in the current supervision session**.

If Build/Planning/Learning-Only/etc. is read only to determine whether a supervised agent followed the expected procedure, it is an **evaluated procedure reference**, not an active current-session operation, and its marker should not be emitted solely for that reason.

This distinction deserves a compact project-wide provenance clarification because it can recur in future meta-review/support procedures.

### 5.11 Artifact shape

v1 should be one compact `SKILL.md` with no scripts and no dedicated reference file.

Reason:

- existing operation/support Skills already provide detailed subordinate procedures;
- one additional reference would mostly restate those owners;
- external evidence favors focused Skills and progressive disclosure;
- if real use later shows one repeated deep supervision lens becoming too large, extract it then.

### 5.12 Minimal governance integration

If implementation follows this design:

1. add `.agents/skills/upgradepilot-workstream-supervision/SKILL.md`;
2. add one compact support/composition routing sentence to `AGENTS.md` and conditional-loading guidance;
3. update `OPERATING_GUIDE.md` support-Skill paragraph and clarify evaluated-procedure reference vs current-session Skill activation/provenance;
4. add `tools/agent-governance/workstream_supervision_cases.json` as a focused manual/semantic support-Skill behavioral bank;
5. register/described that bank in `tools/agent-governance/README.md`;
6. **do not modify `governance_doctor.py` initially**: it already discovers every Skill for objective frontmatter/provenance validation, while support-bank semantic routing remains manual by the repository's current design;
7. do not change `MEMORY.md` solely for this side governance responsibility.

## 6. Behavioral cases required before/with Skill authoring

At minimum cover:

1. single active Build + Learning-by-Doing stream;
2. plan/proposal stream with no code;
3. Learning-Only stream;
4. multiple parallel streams with a material dependency/conflict;
5. agent report says green but executable evidence is weaker;
6. negative routing: ordinary one-off repository Audit should not load supervision;
7. negative routing: ordinary continuation of this session's own Build/Planning work should not load supervision;
8. trivial low-risk supervision checkpoint should stay light and avoid automatic full Audit;
9. issue found, then Ali separately authorizes correction here → explicit operation transition, not implicit mutation;
10. recently completed other-agent work that still needs independent reconciliation.

The cases must specifically exercise the **two-level routing/provenance distinction**.

## 7. Implementation and integration result

The v1 Skill and its bounded governance integration were implemented on the selected branch after the design freeze.

Implementation commits:

```text
38fe1236e5c5914d6a440ec8f01ce980e640d47a
→ add focused workstream-supervision behavioral cases

b1c497df0c81c36666e29140aeb3e4a00c06f24b
→ add .agents/skills/upgradepilot-workstream-supervision/SKILL.md

9e5b1f4895468ec9ee9dfa340071614b44932422
→ add root support/composition routing + conditional loading

e21db84c87ec8093ba98a09856da561775a25e4e
→ document workstream-supervision support behavioral bank

ede280854bdd5ec1d72bc9393f6ac3a52677058c
→ integrate Operating-Guide support/provenance semantics
```

Implemented artifacts/surfaces:

- `.agents/skills/upgradepilot-workstream-supervision/SKILL.md`;
- `tools/agent-governance/workstream_supervision_cases.json`;
- compact routing/discovery integration in `AGENTS.md`;
- support/provenance integration in `OPERATING_GUIDE.md`;
- support-bank documentation in `tools/agent-governance/README.md`.

Deliberately unchanged:

- `governance_doctor.py` — no support-bank deterministic-registration expansion;
- `MEMORY.md` — this side governance responsibility did not replace canonical live product continuation;
- product source/tests/experiments/product-simulation;
- existing five-primary-operation table.

### 7.1 v1 Skill behavior implemented

The Skill now owns the meta-procedure for:

```text
scope named other-agent workstreams
→ reconstruct from smallest sufficient observable evidence
→ map subject-workstream expected route/owners
→ keep current-session route/authorization distinct
→ reconcile REPORTED / OBSERVED / INFERRED / UNRESOLVED
→ choose light / standard / deep supervision proportionately
→ apply only material supervision lenses
→ inspect streams independently before material cross-stream joins
→ keep Ali oriented/learning without duplicate course ceremony
→ CONTINUE / WATCH / GUIDE / INTERVENE / STOP-RECONCILE when useful
→ hand off exact intervention without silently taking mutation authority
→ preserve supervision progression only when justified
```

The selected judgment/depth vocabulary remains explicitly conversational and non-normative; it is not a new product or repository state model.

### 7.2 Two-level routing/provenance integration

The strongest design discovery was promoted into the appropriate project-wide procedural surfaces:

```text
consulting another Skill as the supervised workstream's expected/evaluated procedure
!=
activating that Skill for the current supervision session
```

`AGENTS.md`, `OPERATING_GUIDE.md`, the new Skill, and behavioral cases now agree that evaluated-procedure reference use does not inherit mutation authority and does not justify emitting that procedure's provenance marker.

This is a procedural clarification; it does not redefine the semantics of the five primary operations.

## 8. Validation and post-authoring review

### 8.1 Changed-scope inspection

A branch comparison against base `0137837ac1fbfcfb6d86678ebe706284bdf4468a` after integration showed only the seven planned files changed:

```text
.agents/skills/upgradepilot-workstream-supervision/SKILL.md
AGENTS.md
OPERATING_GUIDE.md
plans/UPGRADEPILOT_WORKSTREAM_SUPERVISION_SKILL_RESEARCH_DESIGN_AND_ADMISSION_PLAN.md
tools/agent-governance/README.md
tools/agent-governance/workstream_supervision_cases.json
working-memory/2026-09-05_workstream-supervision-skill-research-and-design.md
```

At that checkpoint the branch was 10 commits ahead and 0 behind its recorded base. No product/experiment/test/product-simulation files were changed.

### 8.2 Skill structural checks

Established by inspection against `governance_doctor.py` contracts:

- Skill directory and frontmatter `name` agree: `upgradepilot-workstream-supervision`;
- name length is 35 characters, under the 64-character limit;
- description length is 529 characters, under the 1024-character limit;
- name grammar satisfies the lowercase/hyphen format;
- provenance identity matches the Skill name;
- root and Operating Guide contain exact references to the new Skill;
- the existing doctor dynamically discovers all Skill directories for frontmatter/name/provenance checks, so adding this support Skill does not require modifying `EXPECTED_OPERATION_SKILLS`;
- the support behavioral bank is intentionally not part of the doctor's six registered operation/cross-system case banks under the current evaluation design.

The behavioral JSON was parsed successfully before commit and contains the planned ten cases with positive, negative, cross-workstream, claim-vs-evidence, Learning-Only, light-depth, and explicit-intervention-transition pressure.

### 8.3 Design-to-case semantic review

Static review of the Skill against the ten cases found explicit coverage for:

- single Build/Learning-by-Doing subject stream;
- non-code planning/proposal stream;
- Learning-Only subject stream without current-session Learning-Only activation;
- several parallel streams and material joins only;
- agent completion claim stronger than executable evidence;
- negative one-off Repository-Audit routing;
- negative own-session Build/Planning continuation routing;
- lightweight supervision without automatic full Audit;
- explicit later correction authorization and operation transition;
- recently completed but not yet reconciled other-agent work.

No case currently requires a new script/reference file or doctor expansion.

### 8.4 Size/proportionality review

The Skill is one focused file (414 lines) and does not copy the detailed Audit, Planning, Build, Learning, or Working-Memory checklists. Its length comes mainly from the cross-workstream/meta-routing procedure, evidence categories, proportional depth/lenses, intervention boundary, and negative rules that discriminate it from existing operations.

Current judgment: keep the single-file v1 rather than splitting it prematurely. Reassess after real usage if context cost or one repeated subsection becomes independently valuable enough to justify progressive-disclosure extraction.

### 8.5 Proof limits before final pre-merge audit

Not established at the initial closure checkpoint:

- a real execution of `governance_doctor.py` against this remote branch;
- fresh isolated `BASELINE_WITHOUT_TARGET_SKILL` versus `CURRENT_WITH_SKILL` client trials;
- a statistically meaningful behavioral pass rate;
- real-world supervision performance across several future UpgradePilot workstreams.

The repository's own governance-evaluation documentation explicitly says no portable live agent runner is admitted. Therefore these limitations were expected, not silently converted into a pass.

## 9. Initial handoff before final pre-merge audit

Initial research/design/admission/build responsibility was complete enough to stop before the dedicated merge-readiness audit.

What existed at that checkpoint:

```text
new support Skill
+ root/Operating-Guide discovery and provenance semantics
+ focused behavioral pressure bank
+ research/design provenance
+ bounded working-memory history
```

The first recommended behavioral evidence was a real supervision use rather than adding more machinery.

`MEMORY.md` remained unchanged because this work did not replace the canonical live product continuation.

## 10. Skill provenance before final pre-merge audit

`UP-SKILL:upgradepilot-planning-design`  
`UP-SKILL:upgradepilot-repository-audit`  
`UP-SKILL:upgradepilot-build-implement`  
`UP-SKILL:upgradepilot-working-memory`

## 11. Final pre-merge audit and first real supervision trial

A dedicated read-only final governance/system audit was performed before merge.

### 11.1 Audit result

The core design remained sound:

- Workstream-Supervision remains a support/composition Skill, not a sixth primary operation;
- read-only default authority is explicit;
- supervision-session route and supervised-workstream expected route remain distinct;
- root/Operating-Guide integration is minimal and consistent;
- no product source/tests/experiments/product-simulation or `MEMORY.md` changes were introduced by this governance branch;
- `main` was still at the original branch base `0137837ac1fbfcfb6d86678ebe706284bdf4468a` during the audit, so no concurrent-main reconciliation was required at that checkpoint.

The audit found two small repository-contract cleanups and one proof gap rather than a redesign.

### 11.2 Behavioral-bank routing-target cleanup

The first version of several `owners_expected` entries combined an exact Skill path with prose such as `as the supervised workstream's expected procedure`. The governance-evaluation contract expects exact repository-relative Skill paths when a Skill routing target is represented explicitly.

Repaired:

- `WSUP-001` Build target;
- `WSUP-002` Planning/Design target;
- `WSUP-003` Learning-Only target;
- `WSUP-009` Build and Planning/Design transition targets.

The subject/current-session semantics remain in `must_do` / `must_not_do` / `notes`, while the routing targets are now exact paths.

Repair commits:

```text
c463ac5a39c01b3d120329a0b1c8a75beea6cabd
cc5145cb266ae8b4aae331e79a34213474aece22
```

### 11.3 Plan historical wording cleanup

The plan heading `Current working hypothesis — not yet a frozen design` was stale after the design had been frozen and implementation completed.

It was changed to:

```text
Initial working hypothesis — before design freeze
```

This preserves the plan's historical design path without presenting an old hypothesis as current state.

Repair commit:

```text
fd1146315bf14dbb4c69a504a4aab04b170faa92
```

### 11.4 First real Workstream-Supervision trial

The new Skill was then used for a genuine read-only supervision pass on the actual current R4-B LangGraph workstream on `main`.

Smallest sufficient evidence used:

```text
MEMORY.md
→ selected R4-B bounded plan
→ latest R4-B coupling-correction working memory
→ native LangGraph workflow source
→ focused LangGraph graph test source
→ experiment test-directory evidence for the adapter test family
```

The trial reconstructed the workstream correctly without scanning unrelated project history:

```text
REPORTED / LIVE POSITION
R4-B first native source slice written after representation-coupling correction;
executable validation still pending.

OBSERVED
native graph source exists under experiments/langgraph/;
R4-B graph-facing contracts are R4-B-owned;
focused graph tests exist;
adapter-focused test family exists;
latest corrective working memory explicitly limits proof to source/repository inspection.

UNRESOLVED
normal WSL dependency resolution/install;
LangGraph import/compile/invoke;
focused graph + adapter test execution;
controlled R4-A/R4-B semantic comparison;
real S001 LangGraph run;
framework-adoption value.
```

Supervisory judgment:

```text
CONTINUE / WATCH
```

Reason:

- the workstream is coherent with its selected Build/Learning-by-Doing route at the observable source/progression level;
- no evidence justifies calling the missing executable proof a failure;
- the missing WSL executable boundary remains load-bearing before stronger completion claims or later comparison stages;
- product integration remains unauthorized.

Next meaningful checkpoint for that supervised stream:

```text
WSL experiments dependency resolution/install
→ LangGraph import/compile/invoke
→ focused native graph tests + adapter tests
→ diagnose if needed
→ only then controlled semantic comparison
```

This first real use supports actual incremental value for the new Skill: it reconstructed the correct workstream from a small evidence set, kept the subject Build procedure distinct from current-session read-only supervision, reconciled written claims with actual source/test evidence, avoided over-scanning, and produced a useful next checkpoint without taking over the workstream.

It is **one observed trajectory**, not a pass rate and not proof of universal Skill effectiveness.

### 11.5 Deterministic governance validation remains pending

The plan requires structural governance validation to pass before admission/merge.

Actual execution of:

```text
python3 tools/agent-governance/governance_doctor.py
```

has still **not** been established on this branch.

Available execution surfaces in this session could not close that gap:

- the GitHub connector can inspect/write repository state but cannot execute repository Python;
- the branch has no reported CI/status check that runs the doctor;
- this assistant runtime has no local UpgradePilot checkout and outbound GitHub name resolution failed, so it could not clone the branch and execute the diagnostic independently.

Therefore static inspection is strong but must not be mislabeled as an executed doctor PASS.

### 11.6 Current merge-readiness judgment

Established:

- design/system audit: PASS;
- routing/authorization model: PASS;
- behavioral-bank contract after cleanup: PASS by static inspection;
- plan wording/state hygiene: PASS;
- one real R4-B Workstream-Supervision trajectory: useful/PASS for the exercised responsibility;
- changed scope remains governance-only by branch inspection to the latest checked head;
- no redesign is indicated.

Pending:

- one actual `governance_doctor.py` execution on the final branch head.

Exact final validation action:

```text
checkout governance/engineering-supervision-skill-2026-09-05 in the normal UpgradePilot WSL environment
→ run python3 tools/agent-governance/governance_doctor.py
→ if PASS, record the executed result here
→ re-check branch vs main
→ close this working memory
→ merge only after Ali's merge authorization
```

Until that execution is observed, the branch is **conceptually merge-ready but not yet fully admitted under its own plan's structural-validation pass condition**.

## 12. Current Skill provenance

`UP-SKILL:upgradepilot-planning-design`  
`UP-SKILL:upgradepilot-repository-audit`  
`UP-SKILL:upgradepilot-build-implement`  
`UP-SKILL:upgradepilot-working-memory`  
`UP-SKILL:upgradepilot-workstream-supervision`
