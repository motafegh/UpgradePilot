# UpgradePilot Agent Skills and Governance Evolution Proposal

**Status:** Partially admitted — selected governance responsibilities executed; remaining future candidates deferred  
**Authority:** Non-controlling proposal  
**Recorded:** 2026-08-27  
**Working branch:** `agent/skills-governance-evolution-2026-08-27`  
**Branch base:** `main@f0322a5c997b201da740a4333faaeae9db74669d`

## Lifecycle disposition — 2026-08-28

This file began as the **Candidate** proposal that preceded implementation. Its original analysis, candidate wording, and staged recommendations are intentionally preserved below as design/provenance evidence, but they must no longer be read as an open execution queue.

Subsequent bounded plans executed the selected responsibilities through Stages 1–7, including structural corrections, Build and Audit progressive disclosure, Learning-by-Doing/Learning-Only reconciliation, routing/evaluation strengthening, root/Operating-Guide refinement, and learning-transfer refinement. The sixth-Skill admission review concluded **defer / admit no sixth Skill now**; future reconsideration requires real recurring behavioral evidence.

The final whole-branch audit and its bounded repair pass own the branch-readiness conclusion. Repository-wide execution of `python tools/agent-governance/governance_doctor.py` remains deliberately deferred until the finalized governance branch is merged/pulled locally; this proposal makes no executable PASS claim.

Section 17 now records how the original pre-implementation questions were resolved. Future-tense wording elsewhere in this proposal describes the proposal's original candidate design, not current project continuation or authorization.

## 1. Purpose

This proposal records a candidate evolution of UpgradePilot's project-local Agent Skills and the governance surfaces that route, validate, and maintain them.

It is based on two evidence classes:

1. direct audit of UpgradePilot's current governance, five admitted operation Skills, governance doctor, behavioral case banks, specifications, and documentation ownership model;
2. external research into the current Agent Skills ecosystem and practitioner methods, including the open Agent Skills specification and best practices, Matt Pocock / AI Hero, Jesse Vincent's Superpowers, Addy Osmani's `agent-skills`, PostHog's large-scale Skill deployment experience, current public practitioner discussion, and recent research on Skill-library scale and routing interference.

External material is evidence and design input only. It does not control UpgradePilot. Any admitted change must still satisfy UpgradePilot's own Charter, governance ownership, proportionality, evidence doctrine, Learning-by-Doing method, and Ceremony Tax.

## 2. Executive proposal

The current UpgradePilot Skill architecture should be **evolved, not replaced**.

The five admitted operation Skills already form a coherent, project-specific routing model:

- `upgradepilot-repository-audit`
- `upgradepilot-planning-design`
- `upgradepilot-build-implement`
- `upgradepilot-learning-by-doing`
- `upgradepilot-learning-only`

The proposal therefore does **not** recommend importing a large external Skill library or creating a Skill for every useful technique seen elsewhere.

Instead, the recommended direction is:

```text
keep the small operation catalog
→ correct confirmed internal drift
→ improve progressive disclosure and context pointers
→ strengthen Skill structure/routing validation
→ add repeatable behavioral pressure-testing
→ selectively improve the learning procedures
→ consider any new Skill only after evidence shows a real recurring responsibility gap
```

The central design goal is not "more Skills". It is **higher behavioral reliability per admitted Skill with lower unnecessary context load and lower routing ambiguity**.

## 3. Current UpgradePilot strengths to preserve

### 3.1 Small, responsibility-oriented catalog

UpgradePilot currently has five operation-level Skills rather than a broad marketplace-style catalog. This is a strength.

Recent external evidence increasingly suggests that large Skill catalogs can create routing interference or Skill shadowing. Therefore catalog growth should require evidence that a new responsibility cannot be handled clearly by an existing operation Skill plus an on-demand reference.

### 3.2 Skills are procedural, not controlling authority

Root `AGENTS.md` explicitly states that Skills are procedural aids and cannot supersede project owners, user authorization, specifications, ADRs, source truth, or other responsibility owners.

This separation is stronger than many public Skill collections and should be retained.

### 3.3 Explicit operation routing

UpgradePilot already routes Audit, Planning/Design, Build/Implement, Learning-by-Doing, and Learning-Only explicitly.

This gives us a stable basis for evaluating both:

- missed invocation: a Skill should have been used but was not;
- false invocation / shadowing: the wrong Skill was selected or too many Skills were activated.

### 3.4 Canonical semantic ownership plus deliberate reinforcement

The project already distinguishes canonical ownership from high-salience reinforcement. This is important and should not be replaced by simplistic "deduplicate everything" guidance.

For example, Core `JUST-*` rules may correctly remain canonically owned in the Core specification while being briefly reinforced at execution surfaces where repeated assistant failure or material risk justifies it.

### 3.5 Existing governance test foundation

`tools/agent-governance/` already contains:

- deterministic governance checks;
- operation-specific behavioral case banks;
- cross-system consistency cases;
- explicit expected Skill routing surfaces.

This is a strong foundation for the next step: testing not only whether governance files exist, but whether Skills actually alter agent behavior as intended.

## 4. External lessons worth adapting

### 4.1 Progressive disclosure should follow branches, not arbitrary file size

The open Agent Skills guidance recommends keeping the main Skill concise and loading references on demand. Matt Pocock's `writing-for-agents` sharpens this into an information hierarchy:

```text
in-file steps
→ in-file reference needed by most runs
→ disclosed reference needed only by some branches
```

The useful principle for UpgradePilot is:

> Keep in `SKILL.md` what every material invocation needs. Move branch-specific heuristics, examples, specialized checklists, or deep references behind explicit context pointers.

This is not merely token optimization. It protects the procedure from having its main sequence buried inside optional detail.

### 4.2 Context pointers are behavioral routing surfaces

A pointer is useful only if its wording tells the agent **when** to follow it.

Therefore references such as:

```text
See X for more detail.
```

are weaker than pointers that state the branch condition:

```text
When a material source change contains non-obvious cross-file flow or semantic/proof transformations, load `references/source-clarity-heuristics.md`.
```

UpgradePilot should audit important pointers by trigger quality, not only by whether the target path exists.

### 4.3 No-op pruning should become an audit lens

A durable instruction should earn its context cost.

For each sentence or repeated mechanism, ask:

```text
would removing this materially change agent behavior, routing, proof, safety, or ownership?
```

If not, the instruction may be a no-op, stale sediment, or exposition better left to a responsibility owner or reference.

This is an audit heuristic, not a mandate to minimize prose mechanically. High-salience reinforcement may still be justified when evidence shows it prevents material regressions.

### 4.4 Completion criteria should be checkable

External Skill-authoring methods repeatedly converge on strong stopping conditions.

UpgradePilot already has explicit completion/stop sections in several Skills. These should be preserved and strengthened where a step still ends in vague states such as "understand enough" or "review thoroughly" without an observable bound.

### 4.5 Skill authoring should be pressure-tested like executable behavior

Superpowers' strongest transferable idea is to evaluate a Skill through a behavioral loop:

```text
run a realistic pressure scenario without the target Skill
→ observe the failure/rationalization/default behavior
→ apply the Skill
→ rerun the same scenario
→ verify the intended behavior changed
→ refine the smallest instruction that fixes the failure
```

UpgradePilot already has case banks but not yet a fully repeatable live execution runner. A future governance improvement should close that gap.

### 4.6 Routing quality needs its own evaluation layer

A strong Skill can still fail if its description does not trigger reliably or overlaps another Skill.

Addy Osmani's public Skill work and the broader Agent Skills ecosystem distinguish:

1. structural validity;
2. trigger/routing quality;
3. behavioral execution quality.

UpgradePilot currently covers structural validity well and has designed behavioral cases. Trigger/routing quality should become an explicit measured responsibility.

### 4.7 Stable procedure should not cache volatile project facts

PostHog's large-scale experience reinforces a principle UpgradePilot already mostly follows: Skills should describe durable procedure while volatile facts stay in canonical project owners, source, config, tests, environment evidence, or live memory.

A Skill that copies current paths, package states, stage state, or package-specific learning routes becomes a cache that can rot.

### 4.8 Learning should distinguish immediate fluency from durable ownership

Matt Pocock's `/teach` Skill emphasizes the difference between:

- immediate fluency: the learner can follow/explain while the context is present;
- storage strength: the learner can later retrieve, reconstruct, transfer, or diagnose without being walked through the same explanation.

UpgradePilot should selectively adapt this distinction because learner technical ownership is already part of the project method.

It should **not** import `/teach`'s full standalone-course workspace architecture. UpgradePilot already has package-local contracts, depth maps, learning memory, real source/tests/evidence, and Learning-by-Doing governance. Adding parallel lesson/mission/resource machinery globally would create duplicate ownership and ceremony.

## 5. Confirmed corrections proposed first

These are not speculative architecture changes. They address concrete inconsistencies or objective validation gaps already observed.

### 5.1 Fix stale Learning-by-Doing → Learning-Only wording

`upgradepilot-learning-by-doing/SKILL.md` currently contains wording equivalent to:

> Until a dedicated Learning-Only Skill is admitted...

A dedicated Learning-Only Skill **is already admitted** and root routing explicitly names it.

Proposed correction:

- remove the stale pre-admission wording;
- make the transition explicit: when Ali requests Learning-Only, switch to the admitted `upgradepilot-learning-only` procedure while preserving the no-product-mutation boundary.

### 5.2 Extend `governance_doctor.py` to validate the Agent Skills structural standard

The doctor currently verifies presence, frontmatter parsing, non-empty name/description, name-directory equality, uniqueness, and expected Skills.

Proposed deterministic additions:

- Skill `name` length within the admitted standard;
- lowercase letters/numbers/hyphens only;
- no leading/trailing hyphen;
- no consecutive hyphens;
- `description` within the admitted maximum length;
- retain exact directory-name equality;
- report, rather than automatically fail, main-Skill line/token size unless UpgradePilot later adopts a hard local bound.

The external `500 lines` guidance should be treated as a design signal, not blindly converted into a repository failure condition.

### 5.3 Add a regression case for the admitted Learning-Only transition

The governance suite should protect the fact that:

```text
explicit Learning-Only request
→ admitted Learning-Only Skill
→ product mutation paused
```

This prevents the stale pre-admission state from silently returning.

## 6. Progressive-disclosure modifications by current Skill

### 6.1 `upgradepilot-build-implement`

**Disposition:** NARROW, do not replace.

Keep in the main `SKILL.md`:

- authorization/action boundary;
- exact responsibility definition;
- inspect executable truth first;
- current fact vs rationale vs judgment vs authority;
- `JUST-*` retention and end-to-end ownership application;
- smallest adequate implementation;
- core naming and Source Clarity outcome;
- test/proof obligations;
- narrow-to-broad validation;
- debugging entry behavior;
- post-change inspection;
- correct owner updates;
- completion/stop line.

Candidate disclosed reference:

```text
.agents/skills/upgradepilot-build-implement/
├── SKILL.md
└── references/
    └── source-clarity-heuristics.md
```

Move the detailed optional Source Clarity application heuristics to the reference if live testing confirms that they are not required on every Build invocation.

The main Skill should contain an explicit branch-trigger pointer, for example:

> Load the Source Clarity heuristics when a material source change contains non-obvious cross-file flow, semantic/proof transformations, layered APIs, terminology collisions, or other explanation pressure beyond the core outcomes.

Do **not** create a separate Source-Clarity operation Skill merely because the reference is substantial.

### 6.2 `upgradepilot-repository-audit`

**Disposition:** NARROW, preserve the audit model.

Keep in the main Skill:

- read-only boundary;
- audit depth selection;
- exact audit question;
- owner/evidence selection;
- independent implementation truth;
- cross-owner trace when material;
- finding classification;
- smallest disposition;
- proof limitations;
- stop line.

Candidate disclosed reference:

```text
.agents/skills/upgradepilot-repository-audit/
├── SKILL.md
└── references/
    └── audit-lenses.md
```

Detailed lens probes such as Source Clarity sub-checks, optional complexity probes, or specialized overlap questions can move behind this reference if they are branch-specific.

Core lenses such as correctness, proof strength, ownership, necessity, and governance consistency should remain visible enough that ordinary audits do not skip them.

### 6.3 `upgradepilot-learning-only`

**Disposition:** GENERALIZE global procedure; preserve package-local specialization.

The generic Skill should own reusable Learning-Only behavior:

```text
no-product-mutation boundary
→ discover the applicable learning package
→ load package contract/index/memory/plan/depth only as needed
→ use real source/tests/evidence
→ teach in bounded chunks
→ require fair ownership/retrieval steps
→ preserve learning state in the correct package owner
→ return to Build only when explicitly authorized
```

The currently hard-coded B2 compatibility route is useful as regression evidence but creates global coupling to one learning package.

Preferred direction:

- keep generic package-discovery semantics in the global Skill;
- keep B2's exact route in the B2 package owners;
- keep a behavioral regression case proving B2 remains discoverable and correctly routed;
- move any necessary B2 compatibility note to a narrow reference only if a real compatibility reason remains.

Do not copy B2-specific chunk labels, depth mechanics, evidence enums, case routes, or quotas into the global Skill.

### 6.4 `upgradepilot-learning-by-doing`

**Disposition:** CORRECT + selectively strengthen learning transfer.

First fix the stale Learning-Only statement.

Then evaluate small additions around durable learner ownership:

- after a new mechanism has been explained and used, occasionally ask Ali to retrieve or reconstruct it without replaying the full explanation;
- distinguish first-pass comprehension from later independent retrieval/transfer;
- use increasing difficulty only where it strengthens the exact project capability being built;
- avoid turning every slice into a quiz or formal lesson;
- continue to use real code/tests/evidence as the learning substrate.

This should reinforce the existing assistance-fading model rather than create a second teaching framework.

### 6.5 `upgradepilot-planning-design`

**Disposition:** KEEP mostly intact; audit for pointer/no-op opportunities after the other Skills.

The Planning Skill is already comparatively well-bounded and separates:

- stable semantics;
- durable method;
- implementation truth;
- unresolved design;
- execution coordination.

It also has proportional planning levels and clear stop-before-implementation behavior.

Possible later improvements should be evidence-driven, primarily:

- sharpen branch-specific references;
- remove any no-op/expository instructions that do not affect planning behavior;
- ensure completion criteria remain checkable.

No new planning sub-Skills are proposed.

## 7. Root `AGENTS.md` and `OPERATING_GUIDE.md`

### 7.1 Do not mechanically shorten `AGENTS.md`

External examples often use very small root instruction files, but line count alone is not an UpgradePilot requirement.

UpgradePilot's root file contains high-value material that is genuinely always relevant or risk-sensitive:

- action authorization;
- ownership routing;
- operation routing;
- context discipline;
- destructive/external safeguards;
- canonical-owner rules;
- mandatory Learning-by-Building reinforcement.

Therefore the proposal is **not** "make AGENTS.md 100 lines."

Instead, audit each section using four questions:

```text
must this be known on most substantive runs?
does it materially change behavior?
is this the correct canonical owner or justified reinforcement?
can a branch-specific detail move behind a stronger pointer?
```

### 7.2 Preserve `OPERATING_GUIDE.md` as the durable project-wide method owner

Do not migrate Learning-by-Doing philosophy, Ceremony Tax, assistance fading, debugging philosophy, evidence interpretation, or Source Clarity outcomes into independent Skills merely because public libraries expose similar topics separately.

Skills should compose and apply the guide, not duplicate it.

## 8. Routing and invocation improvements

### 8.1 Add deterministic trigger/routing cases

For each admitted Skill, record realistic positive and negative request examples:

```text
SHOULD ROUTE
request phrases / situations that should activate the Skill

SHOULD NOT ROUTE
near-neighbor situations that belong to another Skill or require no full Skill
```

Evaluate both false negatives and false positives.

Especially test collisions such as:

- Audit vs Planning;
- Audit vs Build diagnosis;
- Learning-by-Doing overlay vs Learning-Only primary mode;
- Planning vs Build when the user asks for both in one request;
- tiny factual clarification vs substantive operation.

### 8.2 Investigate explicit invocation metadata, but do not admit it yet

Matt Pocock's current Skills distinguish user-invoked and model-invoked procedures and use client-specific metadata where supported.

UpgradePilot should investigate whether equivalent metadata such as `agents/openai.yaml` can reinforce intentional mode boundaries without:

- creating client-specific semantic authority;
- making the repository unusable across other compatible agents;
- duplicating root routing;
- causing a Skill to become unreachable when implicit invocation is actually valuable.

Candidate principle:

> Use explicit invocation policy only where human selection is itself part of the operation contract.

This remains an investigation, not a proposed immediate change.

## 9. Behavioral Skill evaluation proposal

The next major governance capability should be a repeatable Skill behavioral evaluation loop.

### 9.1 Three evaluation layers

#### Layer A — structure

Deterministic and cheap:

- file/frontmatter validity;
- naming rules;
- expected routing references;
- duplicate names;
- case schema;
- canonical known relationships.

`governance_doctor.py` largely owns this layer.

#### Layer B — routing

Evaluate whether the model selects the intended Skill(s) for representative requests.

Measure:

- expected primary Skill selected;
- unexpected Skill selected;
- required overlay selected when material;
- no full Skill loaded when the request is intentionally below the materiality threshold.

#### Layer C — behavior

For high-value governance behaviors, execute realistic pressure cases and evaluate whether the agent trajectory satisfies the case expectation.

Examples:

- audit request stays read-only;
- planning request stops before implementation;
- build inspects source/tests before modifying executable behavior;
- Learning-Only never mutates product code;
- stale implementation does not become retention authority;
- cross-layer responsibility is traced before duplicating validation;
- evidence limitations are stated rather than overstated.

### 9.2 Baseline-vs-Skill pressure tests

For important or newly modified instructions, compare:

```text
baseline agent behavior without target Skill
vs
behavior with target Skill
```

The purpose is to prove that the instruction actually changes the failure mode we care about.

Do not add a paragraph merely because it sounds wise. Add it because a case demonstrates the model needs it.

### 9.3 CI admission should be gradual

Do not immediately make expensive model-based behavioral evaluations a mandatory CI gate.

Recommended progression:

```text
manual/repeatable local runner
→ collect variance and false positives
→ stabilize scoring/rubric
→ automate deterministic portions
→ admit selected high-value behavioral gates only when reliability/cost justify them
```

## 10. Learning enhancements proposed

These are selective enhancements to existing Learning-by-Doing / Learning-Only behavior, not a new teaching subsystem.

### 10.1 Retrieval over recognition

After first exposure, sometimes require Ali to:

- predict the next flow step;
- reconstruct an input/output contract;
- explain why an owner belongs at one layer rather than another;
- identify what evidence proves or fails to prove;
- diagnose a familiar failure without being given the previous answer.

### 10.2 Spacing through real project recurrence

Do not manufacture flashcard schedules globally.

When the same mechanism naturally reappears later in the project, use the recurrence as spaced retrieval before re-explaining it.

### 10.3 Interleaving only where the real task already combines concepts

Do not mix topics merely because interleaving is pedagogically fashionable.

Use it when UpgradePilot's real responsibility requires, for example, parser structure + evidence strength + target applicability in the same reasoning path.

### 10.4 Zone of proximal development without a new learner bureaucracy

Use existing learning memory, package depth maps, prior demonstrated ownership, and current real task difficulty to decide how much support to give.

Avoid adding a separate global learner-profile framework unless the current owners prove insufficient.

## 11. New Skills: proposed admission policy

### 11.1 Default: add no new operation Skill now

The current research does not yet demonstrate that UpgradePilot needs more than its five operation Skills.

External catalogs contain useful Skills such as TDD, debugging, research, code review, handoff, domain modeling, and Skill authoring. Those names alone are not reasons to add equivalent UpgradePilot Skills.

First ask:

```text
is this a recurring UpgradePilot responsibility?
does the model perform it materially badly under the current routed Skill/owner?
is its procedure distinct enough that embedding it causes sprawl or ambiguity?
does it have a clear activation condition and completion boundary?
would a reference, deterministic tool, test, or existing owner solve the problem more simply?
```

Only then consider admission.

### 11.2 Future candidates worth watching, not admitting yet

#### Candidate A — dedicated Debug/Diagnose Skill

Potential value:

- disciplined red reproduction;
- minimization;
- competing hypotheses;
- instrumentation;
- smallest evidence-backed fix;
- regression proof.

Why not now:

- debugging is already owned at project-method level and appears inside Build;
- a new Skill could create Audit/Build/Debug routing collisions;
- we need behavioral evidence that the current composition is failing before adding a sixth operation surface.

#### Candidate B — Agent Governance Authoring / Skill Maintenance Skill

Potential value:

- recurring audits of agent-consumed documents;
- context pointer quality;
- progressive disclosure;
- no-op pruning;
- completion criteria;
- behavioral-eval updates.

Why not now:

- current Audit + Planning + Build procedures can govern this work;
- this proposal itself should first prove whether such maintenance recurs often enough to deserve a dedicated user-invoked Skill.

#### Candidate C — Research/Evidence Skill

Potential value:

- explicit primary-source-first external research procedure;
- source ownership and citation discipline.

Why not now:

- Audit already supports evidence gathering;
- web research is not always a distinct project operation;
- a new Skill may shadow Audit and Planning.

## 12. Candidate target structure

If the proposal is admitted after validation, the likely Skill tree remains small:

```text
.agents/skills/
├── upgradepilot-repository-audit/
│   ├── SKILL.md
│   └── references/
│       └── audit-lenses.md              # only if disclosure testing justifies it
├── upgradepilot-planning-design/
│   └── SKILL.md
├── upgradepilot-build-implement/
│   ├── SKILL.md
│   └── references/
│       └── source-clarity-heuristics.md # only if disclosure testing justifies it
├── upgradepilot-learning-by-doing/
│   └── SKILL.md
└── upgradepilot-learning-only/
    └── SKILL.md
```

The goal is **not** to create references everywhere. A reference is justified only when a real branch does not need that material on every invocation.

## 13. Proposed staged admission sequence

### Stage 1 — Correctness and objective structure

Implement only:

- stale Learning-by-Doing / Learning-Only correction;
- Agent Skills structural validation improvements in `governance_doctor.py`;
- exact regression coverage for the admitted Learning-Only transition.

Then validate existing governance cases.

### Stage 2 — Progressive-disclosure experiment

Use Build first because it contains the clearest large branch-specific reference candidate.

Process:

```text
capture baseline behavioral cases
→ split only the candidate optional Source Clarity heuristics
→ add explicit branch pointer
→ rerun routing/behavior cases
→ compare omission/overreach/clarity
```

If behavior is preserved or improved, apply the same method cautiously to Repository-Audit.

### Stage 3 — Learning Skill reconciliation

- remove stale coupling;
- generalize Learning-Only package discovery;
- keep B2 exact rules local;
- add modest retrieval/storage-strength behavior to the existing learning model;
- verify no extra ceremony is introduced.

### Stage 4 — Routing/evaluation capability

- formalize positive/negative trigger cases;
- add a repeatable live runner if feasible;
- establish baseline-vs-Skill pressure tests for high-risk behaviors;
- keep expensive model evals outside mandatory CI until stable.

### Stage 5 — Root/governance pruning audit

Only after operation Skills are cleaner, audit `AGENTS.md` and `OPERATING_GUIDE.md` for:

- weak pointers;
- no-op wording;
- stale cached facts;
- unnecessary branch-specific detail;
- unjustified duplication;
- completion ambiguity.

Do not use line-count targets as the acceptance criterion.

### Stage 6 — New Skill admission review

Only now decide whether evidence supports a sixth Skill.

Default outcome remains **no new Skill** unless recurring behavior demonstrates a responsibility gap.

## 14. Acceptance criteria for any admitted changes

A governance/Skill change should not be promoted to `main` merely because the files are shorter or look cleaner.

At minimum, the final admitted package should show:

- no lost authorization, safety, ownership, or evidence boundary;
- all five admitted operation routes remain recoverable;
- no new routing collision introduced;
- structural Skill validation passes;
- current deterministic governance checks pass;
- affected behavioral cases pass;
- branch-specific references are reached when required and skipped when irrelevant;
- stale package-specific global coupling is removed or explicitly justified;
- Learning-Only remains product-read-only;
- Learning-by-Doing still closes the pre-action/action/evidence/post-action/ownership loop;
- canonical semantic owners remain canonical;
- deliberate high-salience reinforcement remains where evidence justifies it;
- no new Skill, file hierarchy, evaluator, or process exists without a demonstrated responsibility.

For behaviorally consequential rewrites, prefer evidence that the changed Skill performs at least as well as the prior version on representative cases rather than relying only on textual review.

## 15. Explicit non-goals

This proposal does **not** currently propose to:

- replace UpgradePilot governance with Matt Pocock's, Superpowers', Addy's, PostHog's, or another external framework;
- install a large public Skill catalog into the repository;
- make every engineering technique its own Skill;
- turn external line/token recommendations into arbitrary hard failures;
- remove deliberate high-salience reinforcement merely because it duplicates a canonical concept;
- replace `OPERATING_GUIDE.md` with Skills;
- create a standalone teaching-course workspace for UpgradePilot;
- make proposals, plans, or Skills controlling product authority;
- introduce expensive model-evaluation CI before a reliable local methodology exists;
- change product source behavior as part of this governance proposal.

## 16. External research references

Primary/current references used as design evidence include:

- Agent Skills specification: <https://agentskills.io/specification>
- Agent Skills best practices: <https://agentskills.io/skill-creation/best-practices>
- Matt Pocock public Skills repository: <https://github.com/mattpocock/skills>
- AI Hero Skills index: <https://www.aihero.dev/skills>
- Matt Pocock `writing-for-agents`: <https://www.aihero.dev/skills-writing-for-agents>
- Matt Pocock `teach`: <https://www.aihero.dev/skills-teach>
- Jesse Vincent / Superpowers: <https://github.com/obra/superpowers>
- Addy Osmani / agent-skills: <https://github.com/addyosmani/agent-skills>
- PostHog Skill-authoring experience: <https://newsletter.posthog.com/p/what-nobody-tells-you-about-writing>
- Databricks research on Skill libraries / shadowing: <https://arxiv.org/abs/2605.24050>

Practitioner posts on X and other social sources were used as supplementary signals and discovery aids, not as sole authority for an admitted recommendation.

## 17. Historical pre-implementation decisions — resolved

The original proposal stopped before modifying the Skills and asked six questions. They were subsequently resolved through bounded plans and evidence-backed review:

1. **Preserve the five-operation architecture and require evidence before a sixth Skill?** — **Yes.** The five admitted Skills remain the operation catalog; the sixth-Skill review later concluded defer/no new Skill now.
2. **Admit Stage 1's concrete corrections?** — **Yes.** Stage 1 was executed and later lifecycle-reconciled as structurally complete; the full repository doctor run remains a post-merge validation obligation.
3. **Use Build as the first progressive-disclosure experiment?** — **Yes.** Build Source-Clarity detail was moved behind a conditional reference with positive/negative behavioral coverage.
4. **Reconcile Learning-by-Doing / Learning-Only relative to disclosure work?** — **Yes.** The learning-mode reconciliation was executed after the Build/Audit disclosure stages, followed by later learning-transfer refinement.
5. **Add a live behavioral Skill-evaluation runner before promotion?** — **No for this cycle.** Structure/routing contracts and a repeatable manual behavior protocol were strengthened; a live runner remains evidence-triggered until a concrete client/runtime and observable load traces justify it.
6. **Admit client-specific invocation metadata?** — **No for this cycle.** It remains an investigation only; no client-specific semantic authority was added.

This proposal therefore remains non-controlling historical/design provenance for both the admitted and deferred ideas. It does not select current work, authorize additional governance changes, or make the remaining candidate ideas active. Current continuation belongs to the normal live-state owner, and final governance-branch readiness belongs to the final whole-branch audit/repair record.