# UpgradePilot Workstream Supervision Skill — Research, Design, and Admission Plan

## Responsibility

Research, design, validate, and—only after the design is sufficiently justified—admit one UpgradePilot-specific **workstream-supervision support/composition Skill** for independently understanding and supervising meaningful work being performed by one or more other AI agents/workstreams.

The intended capability is broader than ordinary code review and different from the existing Repository-Audit operation. It should let Ali start a fresh conversation, identify the relevant ongoing workstreams, understand what each one is doing, map each workstream to the correct UpgradePilot owners/governance/Skills, inspect both the process and the produced results/evidence, learn the material that matters, and decide proportionately whether to continue, guide, intervene, stop/reconcile, or perform a separately authorized corrective action.

This plan owns the **research/design/admission workflow** for that reusable procedure. It does not own product semantics, current product implementation, current live project position, or the behavior of the parallel workstreams being supervised.

## Bounded outcome

The completed responsibility should leave UpgradePilot with:

1. a clear evidence-backed definition of the recurring supervision problem;
2. an explicit distinction between workstream supervision and the existing Audit/Review operation;
3. a clear composition model showing when the supervision procedure routes to other Skills/owners and when it should remain lightweight;
4. a practical method for discovering and reconstructing one or more ongoing workstreams from repository evidence plus Ali's direct context;
5. a proportional supervision loop that checks process, artifacts, evidence, project direction, governance/Skill compliance, and Ali's understanding without micromanaging every child action;
6. a defined intervention boundary that is read-only by default and never treats supervision as implicit authorization to mutate or redirect another workstream;
7. a multi-workstream model able to detect relevant overlap, dependency, contradiction, duplication, or sequencing pressure when several parallel responsibilities are in scope;
8. a researched comparison against credible external agent-review/supervision patterns, including official/vendor guidance, public Agent Skills/workflows, GitHub examples, practitioner discussion on Reddit/X where useful, and relevant recent research;
9. one smallest adequate UpgradePilot Skill if the research/design gate supports admission;
10. only the minimum justified governance integration needed to make the Skill discoverable and composable;
11. focused behavioral pressure cases and structural validation sufficient to show that the new Skill adds useful supervision behavior without becoming a generic mega-procedure or a sixth primary operation by accident;
12. a clear handoff explaining what the Skill does, what it deliberately does not do, how Ali invokes it, and how future sessions should use it.

## Current working hypothesis — not yet a frozen design

The leading hypothesis is that this should become a **support/composition Skill**, not a sixth primary operation.

Conceptually:

```text
parallel workstream(s)
    ↓
supervision procedure
    ↓
identify responsibility / owners / operation / evidence horizon
    ↓
compose only the relevant existing Skill(s) or lightweight root procedure
    ↓
inspect process + output + evidence + learning/project fit
    ↓
supervisory judgment
    ↓
continue / watch / guide / intervene / stop-reconcile
    ↓
Ali decides any material corrective action or new authorization
```

This hypothesis must be pressure-tested against the current governance, existing Skills, external research, and behavioral cases. The plan must not force the final Skill to use this exact vocabulary if a better design is established.

The final Skill name is also intentionally open. Candidate concepts include `upgradepilot-workstream-supervision`, `upgradepilot-engineering-supervision`, or another clearer name justified by the design. Because the responsibility includes planning, research, proposals, learning, coding, and mixed work—not only software implementation—the final name must not accidentally narrow the Skill to code-only review.

## User-intent requirements to preserve

The design must preserve these requirements from the admitted responsibility:

### A. Fresh-session supervision

Ali should be able to enter a new conversation and say, in ordinary language, that this session is for checking/supervising work happening elsewhere.

The supervising agent should then reconstruct the relevant workstream state from the smallest sufficient combination of:

- Ali's direct description of which workstreams matter;
- current branches/commits/PRs when relevant;
- selected plans/specifications/ADRs;
- `MEMORY.md` only when live continuation is material;
- relevant working-memory records;
- actual produced artifacts such as source/tests, plans, proposals, learning artifacts, research outputs, or governance changes;
- executable/runtime evidence when the claim requires it.

The procedure must not pretend it can see another agent's private internal session or hidden reasoning.

### B. Work-type agnostic

The supervised responsibility may be:

- Build/Implement;
- Planning/Design;
- Audit/Review;
- Learning-by-Doing;
- Learning-Only;
- research/analysis;
- proposal writing;
- learning-artifact work;
- working-memory/governance work;
- testing/debugging/evidence collection;
- or another bounded UpgradePilot responsibility admitted by the repository and Ali's request.

The Skill therefore cannot assume that every supervised workstream has a diff, tests, or code.

### C. Governance-aware and Skill-aware

For each workstream, supervision should determine:

```text
what responsibility is actually active?
what operation/method is being used?
which canonical owners govern the work?
which existing Skills should have been used or composed?
which conditional owners/references became material?
what artifacts/evidence establish what happened?
what claims remain unproven?
```

It must use existing Skills rather than duplicate their detailed procedures.

### D. Process + result supervision

Supervision must be able to inspect both:

```text
PROCESS
how the work is being approached, scoped, reasoned about, routed, preserved, validated, and stopped

RESULT
what source/plan/proposal/learning artifact/evidence/decision/etc. was actually produced
```

A technically plausible artifact does not automatically mean the workstream followed the correct responsibility, evidence boundary, project direction, learning method, or stopping line.

### E. Ali understanding and learning

Supervision is also a project-ownership and learning surface.

The supervising session should help Ali understand material decisions, mechanisms, evidence, and deviations when that understanding is useful. It must not force a detached lesson or repeat already-mastered material merely because a supervision checkpoint occurred.

When a supervised workstream is itself Learning-by-Doing or Learning-Only, the supervision procedure must respect that learning method rather than replacing it.

### F. Intervention is separate from observation

Default supervision is read-only.

When a material issue is found, the normal sequence is:

```text
establish finding and evidence
→ explain the consequence to Ali
→ propose the smallest useful intervention
→ Ali and supervising agent decide the next action
```

Possible next actions may include:

- send a precise corrective prompt/instruction to the active agent;
- continue and watch the concern until a better discriminating checkpoint;
- pause/stop that workstream;
- perform a separate Planning/Design or Audit responsibility here;
- perform a separately authorized Build/fix here;
- intentionally accept the deviation with documented reasoning.

The supervision Skill itself must not silently authorize repository mutation, external mutation, or scope expansion.

### G. Multiple parallel workstreams

When Ali identifies several concurrent workstreams, the supervision procedure should treat each as a bounded responsibility first, then inspect only material cross-workstream relationships such as:

- shared owner/spec/ADR pressure;
- dependency/order constraints;
- conflicting assumptions;
- duplicate work;
- incompatible changes;
- one workstream making another's evidence/stated state stale;
- working-memory or live-state collisions;
- one agent crossing into another agent's responsibility;
- learning/research conclusions that should affect another workstream.

Do not create a heavyweight multi-agent coordinator merely because more than one workstream exists.

### H. Proportionality

The procedure must support different supervision depths.

A tiny, obvious, reversible workstream checkpoint may need only a light inspection. A consequential architecture/governance/evidence boundary may require deeper owner/evidence tracing and composition with Audit/Planning/Build/Learning procedures.

The Skill must not require:

- scanning the whole repository every time;
- reading every working-memory record;
- reviewing every commit individually;
- loading every Skill;
- generating a report/checklist for every checkpoint;
- interrupting active agents for non-material stylistic differences;
- proving the same settled fact repeatedly.

## Explicit exclusions

This responsibility does **not** authorize or require:

- modification of product behavior under `src/upgradepilot/`;
- modification of unrelated tests/experiments/product-simulation artifacts;
- changes to current R4-B implementation merely because this Skill is being designed in parallel;
- automatic takeover of another agent's branch or responsibility;
- reading or claiming access to another agent's hidden/private reasoning;
- a general-purpose multi-agent execution framework;
- a background monitoring service, daemon, webhook system, scheduler, or persistent autonomous supervisor;
- automatic messaging to other agents;
- automatic merge/rebase/cherry-pick behavior;
- permanent agent personas merely to simulate reviewer roles;
- a new dependency/framework merely to author the Skill;
- copying a third-party Skill wholesale;
- creating a sixth primary operation unless the design evidence demonstrates a real responsibility that cannot be represented correctly as support/composition;
- duplicating the Repository-Audit Skill's detailed audit procedure inside the new Skill;
- turning all existing Skills into subordinate modules of one giant master Skill;
- rewriting historical working-memory/plans merely to make old work look compliant with the new procedure.

## Repository authority and required design references

Execution must follow the responsibilities already owned by:

- [`../AGENTS.md`](../AGENTS.md) — authorization, responsibility ownership, primary-operation routing, context discipline, support/composition Skill boundary, and artifact routing;
- [`../OPERATING_GUIDE.md`](../OPERATING_GUIDE.md) — Learning-by-Doing, context engineering, proportionality, evidence interpretation, assistance/ownership, completion/handoff;
- [`README.md`](README.md) — plan responsibility and position-neutral plan rules;
- [`../.agents/skills/upgradepilot-planning-design/SKILL.md`](../.agents/skills/upgradepilot-planning-design/SKILL.md) — this plan/design responsibility;
- [`../.agents/skills/upgradepilot-repository-audit/SKILL.md`](../.agents/skills/upgradepilot-repository-audit/SKILL.md) — existing materially evaluative Audit/Review procedure that must not be duplicated or confused with supervision;
- [`../.agents/skills/upgradepilot-learning-by-doing/SKILL.md`](../.agents/skills/upgradepilot-learning-by-doing/SKILL.md) — full Learning-by-Doing composition when materially useful;
- [`../.agents/skills/upgradepilot-working-memory/SKILL.md`](../.agents/skills/upgradepilot-working-memory/SKILL.md) and [`../working-memory/README.md`](../working-memory/README.md) — execution/reasoning/evidence preservation when working-memory maintenance becomes material;
- [`../.agents/skills/upgradepilot-learning-artifact/SKILL.md`](../.agents/skills/upgradepilot-learning-artifact/SKILL.md) — precedent for an admitted support/composition Skill and its interaction with primary operations;
- [`../tools/agent-governance/README.md`](../tools/agent-governance/README.md) — governance behavioral evaluation, Skill provenance, support-skill case-bank precedent, and deterministic-vs-behavioral proof separation.

Consult Build, Learning-Only, environment, security, specifications, ADRs, source/tests, or other owners only when the corresponding execution/research/design question makes them material.

`MEMORY.md` remains the sole owner of the live project position. This plan does not itself replace or select the product continuation.

## Design anchor

This plan was created from current `main` revision:

```text
0137837ac1fbfcfb6d86678ebe706284bdf4468a
```

The implementation/research branch is:

```text
governance/engineering-supervision-skill-2026-09-05
```

The revision is a design anchor, not a future claim that `main` remains unchanged. Before later Skill/governance edits, re-read the then-current targets and reconcile concurrent main changes proportionately.

# Execution sequence

## Phase 0 — Re-establish the exact internal problem and evidence horizon

Before external research or Skill authoring:

1. inspect the current root/support-Skill routing and relevant recent governance evolution;
2. inspect the existing Audit, Planning/Design, Build, Learning-by-Doing, Learning-Only, Working-Memory, and Learning-Artifact boundaries only to the depth needed to map overlap;
3. inspect `tools/agent-governance/` support-skill evaluation precedent;
4. inspect a small sample of recent real UpgradePilot parallel-agent work where supervision pressure is visible—for example planning/build/working-memory/evidence progression—not to audit those workstreams, but to identify concrete recurring supervision needs;
5. reconstruct the real failure/opportunity classes this new Skill must address;
6. explicitly list what is already solved adequately by existing governance/Skills so the new procedure does not duplicate it.

Required Phase-0 output:

```text
recurring supervision responsibilities
existing owners/procedures that already solve parts of them
gaps not cleanly owned today
overlap/conflict risks
candidate activation language
candidate non-activation cases
```

If Phase 0 shows that the recurring problem can already be solved cleanly with a small root clarification or existing Skill composition, stop and do not create another Skill merely because the idea was initially attractive.

## Phase 1 — Define the supervision responsibility independently of a template

Before looking for a third-party Skill to copy, define the responsibility in UpgradePilot terms.

At minimum, work through these questions:

### 1.1 Activation

What user requests should naturally activate this supervision procedure?

Examples to pressure-test:

```text
we are going to supervise what the other agent is doing
check the parallel workstreams with me
review how the active agents are progressing and help me understand it
keep an eye on this implementation/research/planning work while another agent does it
let us inspect their process/results and decide whether to intervene
```

Also define negative cases where ordinary Audit, Planning, Learning-Only, Build, or a simple explanation should remain the correct route without this Skill.

### 1.2 Unit of supervision

Determine whether the procedure's smallest unit should be called a:

- workstream;
- bounded responsibility;
- parallel responsibility;
- supervised slice;
- or another direct term.

The unit must map cleanly to existing UpgradePilot responsibility ownership and material-boundary rules.

### 1.3 Discovery

Define the smallest sufficient workstream-reconstruction route.

Candidate sources include:

```text
Ali's direct statement
→ branch/commit/PR or exact artifact when relevant
→ selected plan / working-memory / live state when material
→ actual changed/produced artifact
→ actual evidence/proof
```

The procedure must not require every source in every case.

### 1.4 Supervision lenses

Determine which concerns belong in the core Skill versus conditional composition. Candidate lenses include:

- authorization/scope;
- correct owner/governance/Skill routing;
- project-direction alignment;
- reasoning/design quality;
- implementation/artifact correctness;
- evidence/proof strength;
- working-memory/live-state consistency;
- Learning-by-Doing or Learning-Only quality;
- Ali understanding/ownership;
- proportionality/overengineering/ceremony;
- source/naming/maintainability where relevant;
- workstream dependency/conflict pressure;
- stopping/handoff quality.

Do not turn this list into a mandatory checklist if materiality-based routing is clearer.

### 1.5 Supervisory outcomes

Research whether a small stable set of judgment outcomes improves clarity. Candidate conversational outcomes include:

```text
CONTINUE
CONTINUE / WATCH
GUIDE BEFORE NEXT MATERIAL STEP
INTERVENE NOW
STOP / RECONCILE
```

These are currently only design candidates. Do not create product enums, repository state, or formal ceremony unless a real need is demonstrated.

## Phase 2 — External research and pattern collection

After the UpgradePilot problem is independently defined, research current external practices for reusable agent review/supervision procedures.

### 2.1 Source priority

Use a layered evidence strategy:

#### Primary / authoritative

- official OpenAI/Codex Agent Skills, review-agent, AGENTS/project-instruction, orchestration, and evaluation guidance where relevant;
- official Anthropic/Claude Code Skill/review/subagent/evaluation guidance where relevant;
- official GitHub Copilot Agent Skills/code-review/custom-instruction guidance where relevant;
- other official vendor/tool documentation only when it materially contributes a distinct pattern.

#### Public implementations/templates

Search GitHub for real reusable Skills/workflows that demonstrate:

- independent reviewer context;
- spec/plan compliance review;
- implementation/code-quality review;
- multi-agent reviewer orchestration;
- bounded read-only reviewer behavior;
- evidence/verification loops;
- progressive or checkpoint-based supervision;
- review/refuter/adversarial roles;
- multi-workstream coordination without full autonomous orchestration.

Prefer current, inspectable repositories and exact Skill/procedure files over blog summaries.

#### Practitioner discussion

Use Reddit and X when useful for discovering real operational patterns, failure modes, trade-offs, and terminology such as:

- implementer/reviewer separation;
- fresh-context review;
- plan-first review;
- review early/often;
- layered supervision;
- loop/state-machine supervision;
- refuter/adversarial review;
- over-review/micromanagement failure modes;
- parallel-agent coordination failures.

Treat social-media claims as practitioner evidence, not authority. Prefer threads/posts that expose concrete workflows or reproducible examples rather than generic opinions.

#### Research literature

Search recent software-engineering/agent research for materially relevant findings on:

- agent supervision;
- multi-agent software-engineering workflows;
- process/trajectory evaluation;
- independent verification;
- agent Skills/instructions effectiveness;
- context overload or harmful instruction conflict;
- layered guardrails/human supervisory judgment;
- parallel-agent coordination.

### 2.2 Research questions

For each useful external pattern, capture only what helps answer:

```text
what recurring problem does it solve?
what is the review/supervision unit?
when is it invoked?
what context does the supervisor receive?
is the reviewer independent/read-only?
how are spec/plan compliance and technical quality separated?
how are verification/evidence handled?
how are several agents/workstreams handled?
how are findings reconciled or escalated?
what failure/overhead does the pattern create?
what should UpgradePilot borrow, adapt, or reject?
```

### 2.3 Research evidence discipline

Do not:

- select one popular Skill first and redesign UpgradePilot around it;
- treat stars/upvotes/likes as proof of correctness;
- copy large third-party instructions into the repository;
- infer effectiveness from prose quality alone;
- claim a pattern is current/trending without fresh evidence;
- make X/Reddit a controlling source;
- adopt framework-specific machinery when the useful principle is framework-independent.

Preserve material findings in one bounded research/working record if needed for handoff and comparison. Do not create a document per source.

## Phase 3 — Comparative synthesis

Create a compact comparison of the strongest external patterns against UpgradePilot's needs.

For each candidate/pattern, classify:

```text
DIRECTLY REUSABLE PRINCIPLE
useful with little change

ADAPTABLE PATTERN
useful but must be reshaped around UpgradePilot owners/Skills/Learning-by-Doing

NOT SUFFICIENT
solves only code review or only final-state review

REJECT
adds unnecessary framework, ceremony, context, autonomy, or conflicts with UpgradePilot governance
```

The comparison should explicitly answer:

1. Why is the existing Repository-Audit Skill insufficient by itself for this recurring responsibility?
2. What should the supervision Skill delegate to Repository-Audit rather than duplicate?
3. Which parts of supervision are genuinely meta/compositional?
4. How should the Skill distinguish supervision from ordinary project continuation/orientation?
5. How should it preserve Ali's learning/ownership without turning every checkpoint into Learning-Only?
6. How should it remain useful for non-code work?
7. How should several parallel workstreams be represented without inventing a multi-agent framework?
8. What is the smallest useful intervention language/output?

## Phase 4 — Freeze the UpgradePilot-specific design

Only after internal analysis + external research + comparison, freeze the design.

The design should establish at least:

### 4.1 Skill identity

- final name;
- concise description/frontmatter activation language;
- support/composition status versus primary-operation status;
- exact relationship to Audit/Planning/Build/Learning/Working-Memory;
- one provenance marker.

### 4.2 Activation and non-activation contract

Define when the Skill should be loaded and when it should not be loaded reflexively.

A central requirement is that **ordinary Audit/Review remains Audit**. The new Skill should activate when the recurring responsibility is supervising another ongoing/recent workstream or several workstreams across progression/checkpoints—not merely because the user says “check this file.”

### 4.3 Workstream map

Define the minimum representation needed to reason about each supervised workstream, for example:

```text
identity / responsibility
user authorization
primary operation/method
selected owner/plan when material
work horizon / branch / artifact / evidence anchor
reported current step
independently established current step
material dependencies/conflicts
next material boundary
```

Keep this conceptual unless a durable data structure is actually needed. The Skill is instructions, not a product database.

### 4.4 Core supervision loop

Freeze the smallest complete loop. A candidate is:

```text
1. identify supervised workstream(s)
2. reconstruct the smallest sufficient state/evidence horizon
3. classify each workstream's responsibility and applicable owners/Skills
4. inspect process + actual output + evidence
5. compare with authorization/governance/plan/method/project direction
6. onboard/teach Ali on material mechanisms/findings when useful
7. classify concerns by materiality and confidence
8. inspect cross-workstream pressure when several streams are in scope
9. produce a proportional supervisory judgment
10. propose the smallest intervention only when justified
11. stop for Ali's decision when new mutation/scope/direction authorization is required
12. preserve material supervision evidence only when future handoff would otherwise lose it
```

### 4.5 Confidence/evidence discipline

The Skill should distinguish at least:

```text
observed current fact
agent-reported claim
historical evidence
inference/judgment
unresolved uncertainty
actual proof strength
```

It must never treat another agent's working-memory or summary as implementation proof merely because it is well written.

### 4.6 Intervention contract

Define how a supervision finding becomes action without violating authorization boundaries.

The Skill should prefer the smallest useful corrective instruction and avoid taking over the workstream unless Ali explicitly authorizes that change of responsibility.

### 4.7 Learning/ownership contract

Define what should be explained during supervision and when active Learning-by-Doing/Learning-Only procedures should be composed rather than duplicated.

### 4.8 Multi-workstream contract

Define how to inspect relationships across several streams and when to isolate them into separate supervision passes to preserve context quality.

## Phase 5 — Design behavioral pressure cases before final authoring

Before considering the Skill complete, create representative cases that distinguish useful supervision from ordinary Audit/Planning/Build/Learning.

The case set should include both positive and negative routing pressure.

Minimum candidate families:

### Positive supervision cases

1. one active Build workstream with a plan + working-memory + recent source/tests/evidence;
2. one active Planning/Design workstream where no source change exists yet;
3. one proposal/research workstream requiring process/result supervision but not product proof;
4. one Learning-by-Doing workstream where Ali needs to understand what the active agent is building and whether the learning loop is being closed;
5. one Learning-Only workstream where product mutation must remain paused;
6. two parallel workstreams with a real dependency or conflict;
7. agent report claims progress that actual artifacts/evidence do not yet prove;
8. technically good result but wrong owner/scope/method/stopping line;
9. process is fine and the correct outcome is “continue; do not disturb the agent”;
10. material finding where the correct next step is a precise prompt to the active agent rather than a local fix.

### Negative / non-activation cases

1. ordinary one-file code review → Repository-Audit only;
2. user asks to design a new component → Planning/Design only;
3. user asks to fix a known bug → Build under existing authorization;
4. user asks to relearn one file with no parallel-agent supervision need → Learning-Only or ordinary explanation as appropriate;
5. user asks only for current project state/orientation → normal owner/state route;
6. tiny familiar continuation where loading a full supervision Skill would add ceremony.

### Failure cases

Pressure-test that the Skill does not:

- scan the whole repo automatically;
- assume another agent's report is true;
- automatically mutate after finding an issue;
- convert every concern into Repository-Audit;
- load every existing Skill;
- force a lesson at every checkpoint;
- micromanage harmless implementation choices;
- ignore cross-workstream conflicts;
- call a plan/working-memory entry implementation proof;
- claim access to private agent state;
- become the live-state owner;
- broaden into a generic autonomous coordinator.

Use `tools/agent-governance/` conventions. Decide during execution whether a dedicated support-skill behavioral bank is justified or whether the smallest useful set fits an existing cross-system/support evaluation surface. Do not generalize deterministic evaluator machinery merely to make the new Skill look formally integrated.

## Phase 6 — Author the smallest adequate Skill

Only after the design gate is sufficiently closed:

1. create one Skill directory under `.agents/skills/`;
2. use valid Agent Skills frontmatter and name/description bounds;
3. add exactly one `UP-SKILL:<canonical-name>` provenance identity;
4. keep the core `SKILL.md` compact enough for progressive disclosure;
5. put detailed optional/reference material under `references/` only when a conditional concern genuinely earns separate context;
6. reference existing canonical owners/Skills instead of copying their procedures;
7. preserve read-only supervision as the default action boundary;
8. make the multi-workstream route proportional rather than mandatory;
9. keep outputs conversational/actionable rather than creating mandatory reports/forms;
10. stop before unrelated project/product changes.

### Candidate reference split — decide only if useful

Possible conditional reference topics include:

- workstream reconstruction/discovery heuristics;
- cross-workstream dependency/conflict review;
- supervision lenses / concern classification;
- intervention-prompt construction;
- supervision of learning workstreams.

Do not create these files merely because the topics can be named. Keep them in the core Skill unless progressive disclosure demonstrably improves context and routing.

## Phase 7 — Minimal governance integration

If the Skill is admitted, update only the owners that actually need to know it exists.

Likely candidates to evaluate:

- `AGENTS.md` support/composition Skill section;
- `OPERATING_GUIDE.md` support/composition relationship;
- `tools/agent-governance/README.md` / behavioral case registration if justified;
- deterministic governance checks only if objective structure/routing coverage genuinely requires a small extension.

Do **not** add it to the five-primary-operation table unless Phase 4 explicitly overturns the support/composition hypothesis with strong evidence.

Do not duplicate its procedure in root governance. Root should contain only the minimum discoverability/routing rule required for agents to find the Skill.

## Phase 8 — Validation and admission evidence

Validation should separate structural proof from behavioral evidence.

### 8.1 Structural validation

At minimum, run the applicable governance diagnostics for:

- Skill directory/frontmatter/name correctness;
- provenance-marker identity;
- repository-relative links;
- case-bank schema/registration if changed;
- no accidental primary-operation routing regression;
- no broken governance references.

### 8.2 Behavioral evaluation

Use representative supervision cases and compare trajectories rather than prose style.

Where practical, include:

```text
BASELINE
current governance without the new Skill procedure

WITH-SKILL
same realistic supervision request with the new Skill available
```

Compare whether the Skill materially improves:

- workstream discovery/reconstruction;
- correct owner/Skill routing;
- separation of agent report from independent evidence;
- process + result supervision;
- read-only/default authorization discipline;
- cross-workstream dependency/conflict detection;
- proportional intervention;
- Ali's understanding/learning support;
- avoidance of unnecessary repository scans/context/ceremony;
- stopping behavior.

One trial is one trajectory, not a pass rate. Do not manufacture statistical confidence.

### 8.3 Real-project pressure test

After focused cases, use one genuine current UpgradePilot parallel workstream as a realistic supervision exercise.

The goal is not to modify that workstream. The goal is to ask whether the new Skill helps reconstruct, understand, evaluate, and communicate the ongoing work more cleanly than the pre-Skill procedure.

If the Skill mainly restates existing Audit/Operating-Guide behavior or adds noticeable context/ceremony without improving supervision quality, narrow or reject it.

## Phase 9 — Documentation, handoff, and stopping point

When admission is justified:

1. preserve any material design/research conclusions in the correct durable owner;
2. keep detailed dated research/execution evidence in working-memory only when independently useful for future reasoning/handoff;
3. update root/guide/tooling only to the minimum required by the admitted Skill;
4. explain to Ali:
   - what the Skill is for;
   - how to invoke it naturally;
   - how it differs from Repository-Audit;
   - how it composes with other Skills;
   - how multi-workstream supervision works;
   - why it is read-only by default;
   - what remains deliberately outside its responsibility;
5. stop before using the new Skill to redirect or modify any existing workstream unless Ali separately authorizes that supervision action.

## Required research/design questions

The responsibility is not complete until these questions are answered explicitly or deliberately left open with evidence needs:

1. Is support/composition definitively the correct routing class?
2. What is the clearest final name given that work may be code, planning, research, proposals, learning, or mixed?
3. What exact supervision need remains after composing current Audit + Operating Guide + other Skills?
4. What should the Skill always do versus conditionally delegate?
5. What should count as a material checkpoint worth supervision?
6. How should a fresh session reconstruct active work without scanning everything?
7. How should it handle discrepancies between agent reports, working-memory, plans, source, tests, and actual runtime evidence?
8. How should it supervise a process that is itself Learning-by-Doing or Learning-Only?
9. What concern/confidence classification is useful without becoming bureaucracy?
10. Are stable supervisory outcomes useful, and if so how informal should they remain?
11. When should several workstreams be reviewed together versus separately?
12. How should cross-workstream conflicts be surfaced without becoming an autonomous coordinator?
13. When should Repository-Audit be composed?
14. When should Planning/Design or Build become a newly authorized follow-up rather than part of supervision?
15. What evidence demonstrates that this Skill adds value beyond existing governance?
16. What context/token/process cost does it add, and how will we keep that cost proportional?

## Pass condition

This plan passes when:

- the recurring supervision responsibility is independently established from real UpgradePilot use;
- external research has been completed across authoritative, implementation, practitioner, and research sources proportionately;
- reusable principles have been separated from vendor/framework-specific machinery;
- the supervision-vs-Audit boundary is unambiguous;
- the final routing class/name/activation/non-activation contract is justified;
- the Skill composes existing procedures rather than duplicating them;
- fresh-session workstream discovery and multi-workstream pressure are handled clearly;
- default read-only/intervention authorization is explicit;
- Ali's understanding/learning responsibility is integrated proportionately;
- focused behavioral cases exist for both positive and negative activation;
- structural governance validation passes for all changed governance surfaces;
- at least one realistic supervision exercise supports actual incremental value;
- no product behavior or unrelated workstream is changed merely to admit the Skill;
- the resulting procedure remains smaller and clearer than a generic “master agent” instruction set.

## Stop / reassessment conditions

Stop and reassess before authoring or integrating the Skill if:

- Phase 0 shows no distinct recurring responsibility beyond current Skills;
- the design collapses into a duplicate Repository-Audit procedure;
- the proposed Skill needs to load most governance/Skills for ordinary use;
- it requires broad repo/history scans to function;
- it implicitly claims access to another agent's private live state;
- it silently authorizes mutation or takeover;
- external research suggests a materially better framing that changes the responsibility;
- a concurrent governance change on `main` materially changes Skill routing/support composition;
- adding the Skill would require a large evaluator/governance redesign not justified by the supervision capability;
- behavioral pressure shows the Skill increases ceremony/context without improving the trajectory.

## Prohibited scope

Do not, under this plan alone:

- modify current R4-B product/experiment implementation;
- redirect any active agent;
- send corrective prompts to active agents;
- merge the branch to `main`;
- modify external systems;
- create background monitoring infrastructure;
- add an agent framework or dependency;
- create a generic autonomous supervisor;
- create multiple overlapping supervision/reviewer Skills;
- duplicate existing operation Skills in the new Skill;
- rewrite old plans/working-memory/history for retrospective compliance;
- claim Skill effectiveness from structural checks alone.

## Learning-by-Doing route for this responsibility

This governance/Skill work is itself a real Learning-by-Doing responsibility.

Use the loop proportionately:

```text
understand one supervision problem/design question
→ establish the minimum mental model with Ali
→ inspect/research real evidence
→ compare candidate patterns
→ let Ali challenge/select important boundaries when useful
→ make one bounded design/admission change
→ inspect structural/behavioral evidence
→ explain what the evidence changed
→ preserve only material research/design continuation
→ continue
```

Do not write the entire Skill from abstract theory before testing the boundaries against real UpgradePilot examples.

## Completion provenance

When the Planning/Design procedure is materially used to execute/refine this plan, expose the normal provenance marker when practical:

```text
UP-SKILL:upgradepilot-planning-design
```

If the full Learning-by-Doing Skill is later explicitly/materially composed, its marker remains separate. Markers record claimed procedure activation only; they do not prove that the design or Skill is correct.
