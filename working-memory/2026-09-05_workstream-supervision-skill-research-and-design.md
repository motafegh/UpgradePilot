# Workstream Supervision Skill — Research and Design Working Memory

Date: 2026-09-05  
Session status: ACTIVE  
Primary responsibility/mode: Planning/Design + bounded Repository-Audit composition + Working-Memory support  
Branch: `governance/engineering-supervision-skill-2026-09-05`  
Base revision: `0137837ac1fbfcfb6d86678ebe706284bdf4468a`  
Related plan: [`../plans/UPGRADEPILOT_WORKSTREAM_SUPERVISION_SKILL_RESEARCH_DESIGN_AND_ADMISSION_PLAN.md`](../plans/UPGRADEPILOT_WORKSTREAM_SUPERVISION_SKILL_RESEARCH_DESIGN_AND_ADMISSION_PLAN.md)

## 1. Session anchor

Ali wants a reusable UpgradePilot Skill for a recurring supervision pattern while other AI agents/workstreams progress in parallel.

The intended use is broader than code review. In a fresh conversation Ali may ask the supervising agent to understand one or several ongoing workstreams—coding, planning, research, proposals, Learning-by-Doing, Learning-Only, governance, testing, learning-artifact work, or another bounded responsibility—then independently check whether they are progressing in the right direction under UpgradePilot governance and the applicable Skills.

The supervising session should also help Ali understand/learn material decisions and mechanisms when useful, without forcing unnecessary lessons. If a material issue is found, Ali and the supervising agent decide whether to instruct the active agent, continue watching, stop/reconcile, or perform a separately authorized correction here.

This governance work is separate from current product/experiment implementation and must not silently redirect or mutate R4-B or another active workstream.

## 2. Starting design understanding

### 2.1 Distinction from Repository Audit

```text
Repository Audit / Review
→ materially evaluate a selected repository responsibility/finding under its own read-only procedure

Workstream Supervision
→ reconstruct and progressively supervise one or more parallel workstreams,
   determine which owners/operations/Skills apply,
   inspect process + result + evidence + project/learning fit,
   and decide proportionately whether intervention is needed
```

Repository-Audit may be composed for a material checkpoint, but supervision should not duplicate its deep audit procedure.

### 2.2 Leading routing hypothesis

The leading hypothesis is a **support/composition Skill**, not a sixth primary operation.

Reasons:

- the supervised workstream may itself be Build, Planning, Audit, Learning-Only, Learning-by-Doing, research, proposal work, or another responsibility;
- supervision needs to inspect/compose existing procedures rather than replace them;
- making it a primary operation risks competing with the current authorization/operation model;
- UpgradePilot already has support/composition precedents such as Working-Memory and Learning-Artifact.

This hypothesis is increasingly supported, but admission remains open until design/evaluation complete.

### 2.3 Default authority boundary

```text
supervision = read-only by default
```

Finding a problem does not authorize mutation or takeover.

Normal sequence:

```text
establish finding + evidence
→ explain consequence to Ali
→ propose smallest justified intervention
→ Ali + supervisor decide action
→ route chosen correction through proper authorization/operation
```

### 2.4 Workstream discovery

The supervisor cannot see another agent's private hidden session/reasoning. Reconstruct from smallest sufficient observable evidence:

- Ali's description of relevant workstreams;
- branches/commits/PRs where relevant;
- selected plans/specifications/ADRs/owners;
- `MEMORY.md` only when live continuation is material;
- directly relevant working-memory records;
- produced artifacts such as source/tests, plans, proposals, research outputs, learning artifacts, or governance changes;
- actual runtime/execution evidence where the claim requires it.

Use existing plans/memory/artifacts rather than creating another tracker.

### 2.5 Multi-workstream requirement

Understand each named stream independently first, then inspect only material joins such as:

- shared semantic/method owner pressure;
- dependency/order constraints;
- conflicting assumptions;
- duplicated work;
- incompatible changes;
- one stream making another's evidence/state stale;
- working-memory/live-state collisions;
- responsibility overlap;
- research/learning conclusions that should alter another stream.

Do not create a multi-agent runtime merely because several workstreams exist.

## 3. Repository/governance findings

Current UpgradePilot governance already supplies most deep procedures supervision should reuse:

- `AGENTS.md` → authorization, responsibility routing, primary operations, support Skill boundary, context discipline;
- `OPERATING_GUIDE.md` → Learning-by-Doing, proportionality, context engineering, evidence, assistance/ownership, handoff;
- Repository-Audit → material correctness/necessity/ownership/proof/governance evaluation;
- Planning/Design → unresolved design/scoping/sequence/proof decisions;
- Build/Implement → authorized mutation and validation;
- Learning-by-Doing → teaching/reasoning/action/evidence/ownership overlay;
- Learning-Only → standalone mastery with mutation paused;
- Working-Memory → dated progression/evidence/reasoning history;
- Learning-Artifact → precedent for support/composition Skill behavior.

Governance-quality probes require persistent agent machinery to demonstrate recurring responsibility, routing distinctness, acceptable activation/context cost, behavioral coverage, and a simpler-baseline check. Prior governance work explicitly warns against adding Skills merely for completeness.

## 4. Exact internal procedural gap

No existing Skill owns this complete recurring sequence:

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
→ continue at next material checkpoint without becoming implementation owner
```

Repository-Audit can provide the evaluative core of a checkpoint but does not own fresh workstream reconstruction, concurrent-workstream topology, progressive supervision cadence, intervention orchestration, or Ali-facing supervisory continuity.

### 4.1 Two-level routing problem

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
→ read-only supervision + bounded Repository-Audit

supervised workstream
→ Build/Implement + Learning-by-Doing + Working-Memory
```

Reading Build as the subject workstream's expected procedure must not give this supervision session Build mutation authority.

This creates a provenance question: **consulting a Skill as an evaluation contract is not necessarily activating that Skill as this session's operation procedure.** Final design must make this explicit without weakening current provenance rules.

### 4.2 Observable-process boundary

Process judgments must distinguish:

```text
observable artifact / commit / test / runtime evidence
claimed procedural provenance (e.g. UP-SKILL marker)
working-memory / agent-written reasoning record
inferred trajectory from observable changes
unobservable/private agent behavior
```

A provenance marker or working-memory claim helps reconstruction but does not prove compliant behavior.

### 4.3 Temporary workstream map

Likely useful in session context:

```text
workstream identity
responsibility / allowed scope
expected operation + support Skills
canonical owners
observable evidence horizon
current checkpoint / unresolved claims
next meaningful proof or decision boundary
material dependencies on other supervised streams
```

Normally keep this in conversation (and an intentionally maintained supervision working-memory record), not a new durable state owner.

### 4.4 Material-checkpoint cadence

Useful checkpoints include:

- plan/design gate closure;
- material source slice landing;
- tests/proof becoming available;
- working-memory handoff changing direction;
- consequential proposal/research conclusion;
- blocker/failure changing route;
- one stream beginning to depend on another;
- imminent stop/authorization boundary.

Do not default to every commit, test rerun, wording edit, or agent message.

### 4.5 Learning role

```text
ordinary substantive supervision
→ default Learning-by-Doing method from OPERATING_GUIDE

material learn-while-supervising need
→ compose full Learning-by-Doing when useful

Ali explicitly pauses to master a subject
→ Learning-Only becomes the selected primary route
```

Auditing a Learning-Only workstream does not itself make the supervision session Learning-Only.

### 4.6 Intervention judgment

Leading informal vocabulary:

```text
CONTINUE
CONTINUE / WATCH
GUIDE BEFORE NEXT MATERIAL STEP
INTERVENE NOW
STOP / RECONCILE
```

These are communication/judgment aids only, not product enums or repository status fields.

## 5. Initial use-case pressure set

### A — Build + Learning-by-Doing workstream
Reconstruct plan/working-memory/diff/tests, determine expected Build/LbD route, inspect claims/proof, teach material mechanisms, and either continue or issue precise intervention without automatically editing its branch.

### B — planning/proposal work with no code
Judge owner/scope/evidence/research/process quality without forcing code/test review.

### C — Learning-Only workstream
Check real-evidence grounding, depth, fair ownership checkpoints, and no accidental Build; current supervision session does not become Learning-Only unless Ali asks.

### D — several parallel workstreams
Reconstruct independently, then inspect only material dependencies/conflicts; do not invent one shared plan/status tracker.

### E — report says green but evidence is weaker
Keep agent/working-memory claim distinct from tests/runtime proof and intervene at the claim boundary.

### F — issue found and Ali wants correction here
First establish finding; only after explicit authorization hand off/transition to proper Planning/Build operation.

### G — trivial checkpoint
Use smallest sufficient evidence; avoid full Audit/report/Skill ceremony when risk and ambiguity are low.

## 6. External research — first dedicated synthesis

External sources are design evidence, not UpgradePilot authority. Official/vendor sources carry more weight than practitioner anecdotes; Reddit/X are useful pressure signals and counterexamples.

### 6.1 Directly reusable patterns

#### Fresh, independent reviewer context

OpenAI Codex sample `review-agent` is explicitly read-only and requires direct inspection of the requested change, surrounding code, tests, and call sites rather than author claims:
- <https://github.com/openai/codex/blob/main/codex-rs/skills/src/assets/samples/review-agent/SKILL.md>

OpenAI Superpowers `requesting-code-review` gives a fresh reviewer precisely crafted context rather than the implementation session's entire history, with exact base/head SHAs:
- <https://github.com/openai/plugins/blob/main/plugins/superpowers/skills/requesting-code-review/SKILL.md>

`codex-orchestrator` has an especially close verification pattern: monitor without editing files owned by the active agent, treat the handoff as claims, inspect the actual repository, verify acceptance criteria, and send exact findings back on failure:
- <https://github.com/alexzh3/codex-orchestrator/blob/main/skills/orchestrate/SKILL.md>
- <https://github.com/alexzh3/codex-orchestrator/blob/main/skills/orchestrate/references/review.md>

**UpgradePilot consequence:** workstream handoff/working-memory should orient the supervisor but remain claims/evidence inputs; actual artifacts/proof must be inspected independently when the claim matters.

#### Progressive disclosure / task-specific Skill admission

GitHub documents Skills as detailed task-specific workflows loaded only when relevant, while `AGENTS.md`/instructions own broader standing rules:
- <https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills>
- <https://docs.github.com/en/copilot/concepts/agents/code-review>

Anthropic likewise describes Agent Skills as dynamically discovered composable procedural resources:
- <https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills>

**UpgradePilot consequence:** external guidance supports the current support/composition hypothesis and keeping the supervision procedure out of always-loaded root context.

#### Fresh-session state reconstruction from durable artifacts

Anthropic's long-running-agent harness explicitly starts fresh sessions by reading git history and progress files; structured progress artifacts prevent the new session from guessing prior state:
- <https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents>

**UpgradePilot consequence:** our plans + working-memory + git history are already the right substrate; a separate supervisor tracker/harness is unnecessary by default.

#### Outcome/evidence must dominate self-report

Anthropic's agent-evaluation guidance separates trajectory from outcome and warns that a final statement such as “booked” is not the outcome unless the environment actually contains the reservation:
- <https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents>

OpenAI's internal coding-agent monitoring also explicitly flags misrepresentation of tool use/results and concealed uncertainty, while noting that monitoring is only one layer and depends on monitorability:
- <https://openai.com/index/how-we-monitor-internal-coding-agents-misalignment/>

**UpgradePilot consequence:** supervision should explicitly grade claim strength against observable evidence and never imply access to hidden behavior. OpenAI's full-trace monitoring architecture is **not** directly portable because our supervisor does not see another agent's private chain of thought/tool trace.

### 6.2 Adaptable patterns

#### Separate compliance from quality

Superpowers' subagent-driven workflow uses a fresh task review with both spec compliance and code quality, plus a broader final review:
- <https://github.com/openai/plugins/blob/main/plugins/superpowers/skills/subagent-driven-development/SKILL.md>

`paad:agentic-review` similarly includes a distinct Spec Compliance lens alongside specialist technical lenses and verifies findings to reduce false positives:
- <https://github.com/Ovid/paad/blob/main/plugins/paad/skills/agentic-review/SKILL.md>

**UpgradePilot adaptation:** do not hard-code “spec review + code review” because supervised work may be a proposal or learning session. Preserve the more general distinction:

```text
trajectory / authorization / owner / requirement alignment
!=
artifact-specific technical or content quality
```

Load the relevant deeper lens only when the workstream demands it.

#### Specialized lenses + verifier/refuter

PAAD and recent Reddit multi-agent review workflows use parallel specialist lenses followed by verification/refutation to limit false positives and context overload.

Representative practitioner source:
- <https://www.reddit.com/r/ClaudeWorkflows/comments/1vcvcm9/workflow_multiagent_code_review_with_parallel/>

**UpgradePilot adaptation:** potentially useful for a consequential/high-risk checkpoint or truly independent questions, but not an always-on multi-agent requirement. Existing operation Skills are already our specialist lenses in many cases.

#### Evidence receipts / stale-proof awareness

The public `agent-audits` Skill ties acceptance criteria to explicit evidence, distinguishes strong vs weak proof, detects stale/mutated artifacts, and refuses completion claims when current proof is missing:
- <https://github.com/aiswarya797/agent-audits/blob/main/agent-audits/SKILL.md>

**UpgradePilot adaptation:** preserve its conceptual discipline—criterion/claim → current evidence → review → proof limit—but do not import its mandatory ledger/hashing/CLI machinery into general supervision. UpgradePilot already owns evidence semantics and working-memory.

#### Explicit stopping and reconciliation

A current X response to “design loops that prompt agents” argues instead: “design state machines”:
- <https://x.com/dzhng/status/2063931263312892406>

Recent Reddit multi-agent practitioners repeatedly identify reconciliation/stopping, not simply spawning agents, as the hard problem; one useful formulation is “the task is the unit, not the session,” with humans retaining architecture/final reconciliation:
- <https://www.reddit.com/r/ClaudeCode/comments/1udrdgy/is_anyone_here_actually_using_multiagent_parallel/>

**UpgradePilot adaptation:** supervision should use explicit material checkpoints + continue/watch/intervene/stop judgments, not an open-ended autonomous loop. The bounded workstream/responsibility is the unit of supervision, not the AI session identity.

### 6.3 Strong proportionality evidence

Anthropic's March 2026 long-running application harness separated generator and evaluator and found real quality gains on hard tasks. But the initial full harness cost about `$200` versus `$9` for a solo run (>20×), and later stronger models made the evaluator unnecessary overhead for tasks they could reliably handle alone; the evaluator remained valuable at the capability boundary:
- <https://www.anthropic.com/engineering/harness-design-long-running-apps>

Anthropic's parallel-C-compiler work also found parallelism useful when work could be decomposed into independently discriminable failures, but multiple agents duplicated/overwrote work on one tightly coupled Linux-kernel failure until the verifier/environment was redesigned:
- <https://www.anthropic.com/engineering/building-c-compiler>

**UpgradePilot consequence:** deep supervision is not fixed ceremony. Escalate depth when ambiguity, risk, novelty, cross-workstream coupling, weak proof, or capability-boundary pressure justifies it; otherwise keep supervision light.

### 6.4 Skill-size/effectiveness evidence

`SWE-Skills-Bench` evaluated 49 public software-engineering Skills: 39 produced zero pass-rate improvement, average gain was only +1.2%, token overhead reached +451%, and some Skills degraded performance because guidance conflicted with repository context:
- <https://arxiv.org/abs/2603.15401>

`SkillsBench` found curated Skills helpful overall but software-engineering gains much smaller (+4.5 percentage points), some tasks worsened, and focused Skills with 2–3 modules outperformed comprehensive documentation:
- <https://arxiv.org/abs/2602.12670>

Current OpenAI model guidance also warns that unclear/conflicting Skill guidance can cause blocking/divergence and recommends explicit priority and transparency about which Skill caused a change in behavior:
- <https://developers.openai.com/api/docs/guides/latest-model>

**UpgradePilot consequence:** the new Skill must stay narrow at its true meta-responsibility, reuse existing owners, and be tested against a no-new-Skill baseline. A mega-Skill that restates every operation is specifically contraindicated.

### 6.5 Practitioner multi-workstream signals

Recent Reddit reports are anecdotal, but several independent threads converge on:

- isolate parallel work only when parallelism is real/useful;
- written task/spec boundaries reduce duplicated work;
- branches/worktrees isolate writes but do not solve reconciliation;
- inspect/reconcile results serially at controlled points;
- human judgment remains important for cross-cutting architecture/final merge;
- tightly coupled work often benefits more from one directed agent + review than many agents.

Representative sources:
- <https://www.reddit.com/r/ClaudeAI/comments/1uldb2g/how_i_stopped_my_parallel_claude_code_agents_from/>
- <https://www.reddit.com/r/ClaudeCode/comments/1udrdgy/is_anyone_here_actually_using_multiagent_parallel/>
- <https://www.reddit.com/r/ClaudeCode/comments/1uvysm6/best_practices_for_running_multiple_coding_agents/>

**UpgradePilot consequence:** the supervision Skill should supervise **named workstream responsibilities**, not assume each agent/session deserves its own permanent lane or infrastructure.

### 6.6 Patterns currently rejected / unnecessary

Do **not** copy these external mechanics by default:

- Superpowers-style mandatory review after every task and “never skip because simple” — conflicts with UpgradePilot proportionality;
- PAAD-style mandatory many-specialist parallel dispatch for every review — too costly and code-specific;
- `codex-orchestrator`'s durable run journal/worktree/agent-launch machinery — useful template mechanics but outside our supervision responsibility because agents already run elsewhere;
- `agent-audits` mandatory acceptance ledger, artifact hashing, and CLI gate for every supervised workstream — evidence discipline is useful, machinery is disproportionate/general-purpose duplication;
- endless loop/automatic reviewer cycles;
- automatic cross-agent messaging, merging, or correction;
- worktree orchestration as part of this Skill merely because parallel agents exist.

### 6.7 UpgradePilot-specific gap remains

No external Skill/template found so far owns all of:

- fresh reconstruction of already-running external workstreams;
- work-type agnostic supervision (code + plans + proposals + research + learning + governance);
- two-level `supervision-session route` vs `supervised-workstream expected route`;
- composition with existing project-local operation/support Skills without activating the wrong mutation authority;
- UpgradePilot owner/plan/working-memory/evidence semantics;
- Ali's Learning-by-Doing understanding/ownership as part of supervision;
- proportional cross-workstream dependency/conflict reasoning;
- read-only-by-default intervention handoff decided with Ali.

**Research conclusion so far:** there is no suitable wholesale template. The strongest design direction is a small UpgradePilot-specific meta-procedure synthesized from several external patterns.

## 7. Candidate template classification

| External source | Classification | Most useful borrowed idea |
|---|---|---|
| OpenAI Codex `review-agent` | directly reusable principle | read-only independent direct inspection |
| Superpowers `requesting-code-review` | adaptable | fresh reviewer + exact evidence range |
| Superpowers `subagent-driven-development` | adaptable / partly incompatible | compliance vs quality split; explicit breakers, but mandatory per-task review is too heavy |
| `codex-orchestrator` | closest structural template, adaptable | monitor without editing; handoff-as-claims; acceptance verification; exact recheck |
| PAAD `agentic-review` | adaptable for high-risk cases | specialist lenses + finding verification |
| `agent-audits` | adaptable evidence model | current evidence/proof receipts and stale-proof awareness |
| Anthropic long-running harnesses | directly reusable principles | fresh-session reconstruction; structured handoff; evaluator only when load-bearing |
| GitHub Agent Skills guidance | directly reusable principle | task-specific Skill + progressive disclosure |
| Reddit/X multi-agent patterns | secondary/adaptable | reconciliation/stop is hard; task/workstream as unit; human-owned cross-cutting judgment |

## 8. Current route

Internal gap analysis and the first broad external-research pass are complete enough to narrow the remaining research.

Next:

1. run a last gap-focused search for **non-code supervision/project-review** and any direct “supervisor/foreman/conductor” Skill that handles already-running work rather than launching it;
2. check whether those results materially challenge the support-Skill / two-level-routing design;
3. then synthesize the final design choices: name, activation, workstream reconstruction, routing/provenance wording, supervision depth/checkpoints/lenses, intervention handoff, optional references, behavioral cases, and governance integration;
4. do **not** author the Skill until that design is sufficiently frozen.

## 9. Open questions after first external synthesis

- What wording cleanly separates reading another Skill as the supervised stream's expected contract from activating it in the current supervision session?
- Should the final Skill name emphasize `workstream`, `engineering`, or `supervision` without becoming code-only?
- Can one compact Skill contain all necessary mechanics, or does a small conditional reference for supervision lenses/workstream reconstruction materially reduce context?
- What exact triggers justify full Repository-Audit composition instead of lightweight supervision?
- Should intervention labels remain optional prose aids (current preference) rather than formal states?
- What behavioral baseline case most clearly fails under existing Skills but succeeds with the new meta-procedure?
- Is any deterministic governance-doctor extension justified now? Current evidence says **probably no**.

## 10. Current proof limits

Established:

- recurring user need is explicit;
- branch, plan, and progressive working-memory trail exist;
- current governance supports support/composition Skills;
- existing Skills own most deep inspection/execution/learning procedures;
- a distinct meta-level gap exists around workstream reconstruction, expected-route mapping, progressive checkpoint supervision, cross-workstream reasoning, Ali-facing continuity, and intervention handoff;
- the two-level routing/provenance issue is real and requires deliberate design;
- multiple current external sources independently support fresh-context review, direct evidence over self-report, progressive disclosure, explicit stopping/reconciliation, and proportional evaluator use;
- no suitable wholesale external template has been found;
- large/general Skills and fixed multi-agent review machinery have measurable/credible cost and regression risks;
- support-Skill classification is now materially better supported.

Not yet established:

- final Skill admission after design/evaluation;
- final name;
- exact activation language;
- exact two-level routing/provenance wording;
- final supervision loop/lenses/depth model;
- final intervention wording;
- whether any reference file is justified;
- whether deterministic governance tooling should change;
- behavioral improvement versus current governance without the Skill;
- whether the final gap-focused external search reveals a materially better template.

## 11. Skill provenance

`UP-SKILL:upgradepilot-planning-design`  
`UP-SKILL:upgradepilot-repository-audit`  
`UP-SKILL:upgradepilot-working-memory`
