# Workstream Supervision Skill — Research and Design Working Memory

Date: 2026-09-05  
Session status: ACTIVE  
Primary responsibility/mode: Planning/Design + Working-Memory support  
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

The current working distinction is:

```text
Repository Audit / Review
→ materially evaluate a selected repository responsibility/finding under its own read-only operation procedure

Workstream Supervision
→ reconstruct and progressively supervise one or more parallel workstreams,
   determine which owners/operations/Skills apply,
   inspect process + result + evidence + project/learning fit,
   and decide proportionately whether intervention is needed
```

The exact final boundary remains a design question to pressure-test rather than a frozen conclusion.

### 2.2 Leading routing hypothesis

The leading hypothesis is that supervision should be a **support/composition Skill**, not a sixth primary operation.

Reasoning so far:

- a supervised workstream may itself be Build, Planning, Audit, Learning-Only, Learning-by-Doing, research, proposal work, or another responsibility;
- supervision needs to route/combine those existing procedures rather than replace them;
- making supervision a universal primary operation risks turning it into a competing governance authority or mega-procedure;
- UpgradePilot already has a precedent for support/composition Skills such as Working-Memory and Learning-Artifact.

This remains a hypothesis until the internal analysis, external research, and behavioral pressure tests are complete.

### 2.3 Default authority boundary

Current agreement:

```text
supervision = read-only by default
```

Finding a problem does not itself authorize mutation or takeover.

Normal intervention sequence should be:

```text
establish finding + evidence
→ explain consequence to Ali
→ propose smallest justified intervention
→ Ali + supervising agent decide action
→ route any chosen correction through the proper operation/authorization
```

### 2.4 Workstream discovery

The supervising agent cannot see another agent's private hidden session/reasoning. Ongoing work should instead be reconstructed from the smallest sufficient observable evidence, such as:

- Ali's direct description of which workstreams matter;
- branches/commits/PRs when relevant;
- selected plans, specifications, ADRs, and other owners;
- `MEMORY.md` only when live continuation is material;
- relevant dated working-memory records;
- produced artifacts such as source/tests, plans, proposals, research outputs, learning artifacts, or governance changes;
- actual execution/runtime evidence where the claim requires it.

Because UpgradePilot already uses plans and working memory extensively, workstream reconstruction is expected to be practical without inventing a separate tracking system.

### 2.5 Multi-workstream requirement

Ali confirmed that a supervision session should be able to cover several parallel workstreams when he identifies them.

The supervising procedure should first keep each workstream bounded, then examine only material relationships across them, for example:

- shared owner/spec/ADR pressure;
- dependencies/order constraints;
- conflicting assumptions;
- duplicated work;
- incompatible changes;
- one workstream making another's evidence or stated state stale;
- working-memory/live-state collisions;
- responsibility crossing;
- research/learning conclusions that materially affect another workstream.

It should not create heavyweight multi-agent coordination merely because several agents exist.

## 3. Preliminary external-research signals already discussed

These are **early research signals**, not yet final design evidence. They must be revisited and sourced properly during the dedicated research phase.

### 3.1 Independent review patterns

Existing public agent/code-review patterns suggest useful principles such as:

- independent/read-only reviewer context;
- inspecting actual changes/evidence instead of trusting the implementer's summary;
- separating specification/requirements compliance from code/technical quality;
- reviewing at meaningful checkpoints rather than only at final completion;
- using specialized review lenses where needed instead of one undifferentiated reviewer.

These patterns appear useful, but ordinary code-review Skills are narrower than the intended UpgradePilot supervision responsibility.

### 3.2 Continuous/loop supervision patterns

Current agent-engineering discussion contains a broader pattern of:

```text
observe/discover state
→ act or assess
→ verify
→ preserve relevant state
→ decide continue / escalate / stop
```

The UpgradePilot interpretation should be explicit and bounded rather than an endless autonomous loop. Material checkpoints and stop/escalation criteria are likely important.

### 3.3 Layered-supervision idea

A useful research direction is the idea that reliable AI-assisted engineering supervision may be distributed across:

- preventive guardrails/instructions;
- executable controls such as tests/validation;
- higher-level human/AI engineering judgment.

This potentially maps well to UpgradePilot's governance owners + executable evidence + Ali/supervising-agent judgment, but the source and exact implications still need proper research validation.

### 3.4 Skill-size warning

A repeated concern from current agent-Skill research is that large generic instruction bundles can add context cost or conflict with local repository guidance. This reinforces the design pressure toward a small supervision core with conditional composition, but this should be validated during research rather than treated as settled merely from early browsing.

## 4. Repository/governance findings established so far

The current UpgradePilot governance already provides several pieces the new Skill should compose rather than reimplement:

- `AGENTS.md` owns authorization, responsibility routing, primary-operation routing, support/composition boundaries, and context discipline;
- `OPERATING_GUIDE.md` owns Learning-by-Doing, proportionality, context engineering, evidence interpretation, assistance/ownership, and handoff principles;
- Planning/Design is the current primary operation for designing this new procedure;
- Working-Memory is explicitly a support/composition Skill and is the correct procedure for this dated trail;
- Learning-Artifact provides a useful precedent for how a support/composition Skill can coexist with the five primary operation routes;
- the governance-evaluation system already distinguishes deterministic structure, routing/activation observability, and behavioral trajectory;
- support-Skill behavioral banks already exist as a precedent, but deterministic routing-contract validation is not automatically generalized to every support Skill;
- previous governance work established the importance of positive/negative routing cases, provenance markers, progressive disclosure, and not treating a marker as proof of correct behavior.

A prior governance-evaluation plan also explicitly warned against pre-creating additional Skills merely for completeness and required an evidence-based admission gate. This supervision Skill therefore needs to demonstrate a distinct recurring procedural value rather than being admitted only because the concept sounds useful.

## 5. Plan established in this session

A dedicated branch was created:

```text
governance/engineering-supervision-skill-2026-09-05
```

The initial branch was created from main revision:

```text
0137837ac1fbfcfb6d86678ebe706284bdf4468a
```

The planning artifact was added in commit:

```text
90f7a6cd3ef431d1caa76a5643121c58918592b3
```

Plan:

[`../plans/UPGRADEPILOT_WORKSTREAM_SUPERVISION_SKILL_RESEARCH_DESIGN_AND_ADMISSION_PLAN.md`](../plans/UPGRADEPILOT_WORKSTREAM_SUPERVISION_SKILL_RESEARCH_DESIGN_AND_ADMISSION_PLAN.md)

The plan deliberately sequences:

```text
internal analysis
→ define exact supervision gap
→ external research
→ synthesize/reject/adopt patterns
→ freeze the smallest adequate Skill design
→ behavioral pressure cases
→ write the Skill
→ minimal governance integration
→ validation on representative UpgradePilot supervision scenarios
```

The final Skill name, exact vocabulary, and exact routing contract remain open until the design evidence is strong enough.

## 6. Progressive record

### 2026-09-05 — working-memory preservation added

Ali explicitly requested that the supervision-Skill investigation preserve its analysis, discoveries, decisions, and research progressively in one proper working-memory record so details are not lost before final Skill authoring.

Decision:

- create one dedicated working-memory record for this responsibility;
- continue this same record while the research/design responsibility remains coherent;
- update it at meaningful findings/decision changes rather than logging every search or tool call;
- keep the plan as the execution/sequence owner and this file as dated reasoning/evidence history;
- do not update `MEMORY.md` merely because this governance side responsibility exists, unless the canonical live project continuation itself later changes.

## 7. Current session route

Next intended progression for this responsibility:

1. **Internal analysis:** inspect the exact existing Skills/governance surfaces most likely to overlap with or support supervision, and identify the real procedural gap.
2. **Use-case pressure:** derive representative UpgradePilot supervision situations, including one workstream and several parallel workstreams, before deciding exact Skill mechanics.
3. **External research:** search current official/vendor guidance, public Skills/workflows, GitHub examples, Reddit/X practitioner patterns, and relevant research for reusable mechanisms and failure modes.
4. **Synthesis:** classify findings as directly reusable, adaptable, incompatible, unnecessary, or requiring UpgradePilot-specific design.
5. **Design freeze:** decide final responsibility, name, activation/routing, context-discovery procedure, supervision loop/lenses, intervention states, composition with existing Skills, stop line, and anti-patterns.
6. **Behavioral evaluation design:** create discriminating positive/negative cases that test whether the Skill changes agent trajectory usefully without over-routing or becoming a mega-procedure.
7. **Skill authoring/integration:** only after the design gate is satisfied.
8. **Representative validation:** exercise the new procedure against realistic UpgradePilot workstream supervision and record proof/limitations.

## 8. Open questions to resolve through analysis/research

- What is the sharpest responsibility boundary between Workstream Supervision and Repository Audit?
- What final name best covers code, planning, research, learning, proposals, governance, and mixed work without becoming vague?
- What supervision depth model is useful without introducing ceremony?
- Which supervision lenses belong in the Skill core versus conditional references/other Skills?
- How should one session represent multiple workstreams without creating a second live-state tracker?
- When should the supervising agent merely observe, when should it teach, and when should it recommend intervention?
- What exact evidence should justify `continue`, `watch`, `guide`, `intervene`, or `stop/reconcile` judgments, and should those remain informal judgments rather than repository enums?
- Which external patterns have evidence of real benefit, and which are merely popular workflow conventions?
- What behavioral cases best prove the Skill's incremental value over existing root governance + individual operation Skills?
- Does the governance evaluator need any structural extension for this support Skill, or is a focused manual/semantic case bank sufficient initially?

## 9. Current proof limits

Established:

- the recurring user need is explicit;
- the dedicated branch and plan exist;
- current governance supports support/composition Skills as a category;
- the responsibility can be described distinctly enough to justify further investigation;
- a working-memory trail is now intentionally part of the execution method.

Not yet established:

- final Skill name;
- final activation language;
- final routing/composition contract;
- final supervision states/lenses;
- whether any additional reference files are justified;
- whether deterministic governance tooling should change;
- whether external research materially changes the current support-Skill hypothesis;
- behavioral benefit versus current governance without the new Skill;
- final Skill quality/admission.

## 10. Skill provenance

`UP-SKILL:upgradepilot-planning-design`  
`UP-SKILL:upgradepilot-working-memory`
