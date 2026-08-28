# UpgradePilot Agent Skills Governance — Final Whole-Branch Audit Plan

**Plan status:** Completed — final audit executed, bounded repairs applied, targeted re-audit passed; ready for latest-main reconciliation  
**Authority:** Non-controlling audit coordination. Root `AGENTS.md`, `OPERATING_GUIDE.md`, admitted Skills, responsibility owners, and current user authorization remain authoritative.  
**Audit mode:** The final audit itself was read-only; the later bounded repair pass was separately authorized by Ali and is recorded in §23.  
**Working branch:** `agent/skills-governance-evolution-2026-08-27`  
**Branch base:** `main@f0322a5c997b201da740a4333faaeae9db74669d`  
**Plan-entry branch tip:** `ca4386d5c9acff45b85f903281c2a958c6754399`

## 1. Responsibility

Perform the final system-level audit of the complete Agent Skills/governance evolution branch before deciding whether it is ready to reconcile with latest `main` and later merge.

The audit must answer a stronger question than whether individual Markdown files look correct:

> Does the complete governance system give an AI assistant a clear, reachable, proportionate, non-conflicting path from the user's request to the right operation, owners, real work, evidence, learning behavior, stopping point, and claims?

The audit must evaluate both semantic correctness and practical agent usability. It must explicitly test the real failure pressures observed during project work: important rules can be missed because they are nested, or over-applied because many conditional rules are treated as mandatory ceremony.

## 2. Audit outcome

The audit must end with one of these dispositions:

```text
READY FOR MAIN RECONCILIATION
→ no unresolved governance blocker remains
→ branch can proceed to latest-main comparison/reconciliation

REPAIR REQUIRED BEFORE MAIN RECONCILIATION
→ exact findings and smallest owner-specific repairs identified
→ no repair performed inside the read-only audit

UNRESOLVED
→ evidence is insufficient for one or more material claims
→ smallest discriminating follow-up identified
```

The audit itself does not merge, rebase, modify `main`, run destructive Git actions, or silently repair findings.

## 3. Core audit principles

### 3.1 Audit the system as an agent experiences it

Do not inspect files only in isolation. Trace representative request paths through:

```text
user request
→ root AGENTS.md
→ primary operation
→ default Learning-by-Doing method when substantive
→ applicable operation Skill
→ conditional reference only when triggered
→ exact responsibility owner(s)
→ active evidence / implementation
→ proof / state preservation / learning closure
→ stop
```

For each path, ask both:

```text
UNDER-APPLICATION
Did an important rule become too remote, implicit, or easy to miss?

OVER-APPLICATION
Did a conditional/proportional rule become treated as universal ceremony?
```

### 3.2 Preserve canonical ownership while testing reachability

A rule does not need to be duplicated everywhere to be reachable. Prefer:

```text
one canonical owner
+ short high-salience reinforcement when evidence justifies it
+ precise trigger/pointer to deeper procedure
```

Flag both semantic duplication and insufficient execution-surface reinforcement when either can materially change behavior.

### 3.3 Proportional evidence, not exhaustive archaeology

Use the smallest evidence capable of answering each audit question.

Do not scan all repository history, all archived plans, all learning packages, or unrelated product source merely for completeness. Use historical material only for a precise provenance/drift question.

External Agent Skills research already captured in the proposal remains design evidence. Re-open external research only if a material current question cannot be resolved from the existing proposal/references or a current standard may have changed in a way that could alter the conclusion.

## 4. In-scope surfaces

Audit the complete branch changes and directly related current owners, including proportionately:

- `AGENTS.md`;
- `OPERATING_GUIDE.md`;
- all five admitted operation Skills:
  - `.agents/skills/upgradepilot-repository-audit/SKILL.md`;
  - `.agents/skills/upgradepilot-planning-design/SKILL.md`;
  - `.agents/skills/upgradepilot-build-implement/SKILL.md`;
  - `.agents/skills/upgradepilot-learning-by-doing/SKILL.md`;
  - `.agents/skills/upgradepilot-learning-only/SKILL.md`;
- admitted conditional Skill references;
- `tools/agent-governance/governance_doctor.py`;
- `tools/agent-governance/README.md`;
- all governance behavioral case banks affected by this evolution;
- `proposals/2026-08-27_UPGRADEPILOT_AGENT_SKILLS_AND_GOVERNANCE_EVOLUTION_PROPOSAL.md`;
- Stage 1–7 governance/Skills plans;
- `working-memory/2026-08-28_AGENT-SKILLS_sixth-skill-admission-deferral.md`;
- `plans/README.md` and other exact responsibility owners when needed to judge ownership or lifecycle correctness;
- the complete branch diff against `f0322a5c997b201da740a4333faaeae9db74669d`.

Inspect product source/tests only when necessary to verify that this governance branch did not accidentally change product behavior or when a governance statement makes a concrete product/source claim that requires executable truth.

## 5. Explicitly out of scope

The audit must not:

- redesign UpgradePilot product architecture;
- resume R2/R3/R4/R5 product work;
- create a sixth Skill;
- reopen the completed sixth-Skill candidate investigation unless contradictory evidence appears;
- invent a new governance framework merely because the audit is comprehensive;
- create client-specific Skill metadata or a live evaluation runner;
- create a new learner-profile, repetition, or teaching framework;
- turn every observed wording preference into a finding;
- run the full local repository-wide `governance_doctor.py` executable validation before the agreed post-merge local stage;
- merge/rebase/cherry-pick into `main`;
- repair findings during the read-only audit.

## 6. Audit lens A — authority, ownership, and semantic coherence

Verify that:

1. root authorization and request-to-action boundaries remain clear and controlling;
2. Skills remain procedural, not semantic/project authority;
3. `OPERATING_GUIDE.md` remains the canonical owner of project-wide working/learning method;
4. specifications/ADRs/plans/source/tests/state owners retain their own responsibilities;
5. one durable rule has one canonical semantic owner unless deliberate reinforcement is justified;
6. reinforcement preserves meaning and points back to the owner;
7. no plan, proposal, working-memory record, Skill, or case bank silently becomes live-state or product-semantic authority;
8. no stale branch/stage/current-position statement leaks into a durable position-neutral owner.

### Stop criterion

Stop this lens when every material changed rule has a clear canonical owner and no unresolved same-responsibility conflict remains.

## 7. Audit lens B — default Learning-by-Doing reachability and execution

This is a high-priority user-driven lens.

Verify that Learning-by-Doing remains unmistakably the default method for substantive UpgradePilot work unless Ali explicitly changes the mode.

The system should preserve this practical model:

```text
substantive real responsibility
→ identify primary operation
→ proportionate pre-action orientation
→ real bounded work
→ inspect actual evidence
→ preserve material state
→ post-action learning closure
→ ownership/reasoning transfer when useful
→ continue or stop
```

Audit specifically:

1. **Cold-start reachability** — after root `AGENTS.md`, the assistant should already know that substantive work uses Learning-by-Doing by default.
2. **Operation inheritance** — selecting Audit, Planning/Design, Build/Implement, Debug/Diagnose, testing, or review must not silently disable the default Learning-by-Doing method.
3. **Method vs Skill distinction** — not loading the full Learning-by-Doing Skill for tiny/familiar work must not be interpreted as disabling the default method.
4. **Explicit mode change** — standalone Learning-Only remains a deliberate user-selected primary mode with product mutation paused.
5. **Pre-action orientation** — enough is taught before unfamiliar premises are used, without front-loading a detached course.
6. **Post-action closure** — substantive work does not silently end after implementation/audit/test merely because the AI already explained the plan.
7. **Adaptive depth** — orientation, learning closure, and ownership steps scale with novelty, consequence, repetition, and evidence; they are not fixed-size ceremony.
8. **Real-work breadth** — Learning-by-Doing applies to design, audit, debugging, evidence work, testing, and implementation, not coding only.
9. **Progressive material-state preservation** — determine whether current wording makes clear that material state may be preserved before, during, or after a bounded slice when needed, while `MEMORY.md`, `working-memory/`, and other owners keep their existing distinct responsibilities.
10. **No artificial teaching work** — the system must not manufacture quizzes, failures, code changes, or detached lessons merely to demonstrate Learning-by-Doing.

### Behavioral pressure routes

At minimum, reason through representative prompts where Ali does **not** explicitly say “use Learning-by-Doing”:

```text
Continue implementing the next bounded responsibility.
Critically audit this existing design and stop there.
Design the smallest safe approach for this responsibility.
Diagnose this failing focused test without changing code.
Run the focused validation and interpret what it proves.
```

For each, verify that the correct primary operation remains primary while proportionate Learning-by-Doing behavior survives.

### Stop criterion

Stop this lens when the default mode is reachable from root, survives primary-operation routing, remains proportional, and has no material ambiguity between “default method” and “full Skill activation.”

## 8. Audit lens C — navigation, progressive disclosure, and instruction reachability

Audit the complete navigation path rather than treating more files as automatically better organization.

Verify:

1. root routes every admitted operation unambiguously;
2. each Skill description/activation boundary is distinct enough to avoid shadowing;
3. conditional references contain branch-trigger language that tells the agent when to load them;
4. conditional detail is actually deeper than always-relevant behavior;
5. critical default behavior is not hidden behind several optional hops;
6. deeper files specialize rather than silently change the meaning of higher-level rules;
7. important owners are reachable without speculative repository scans;
8. no stale hard-coded B2/package route remains in generic Learning-Only/Learning-by-Doing procedure;
9. no missing pointer forces an assistant to reconstruct a responsibility from history;
10. no reference exists merely because progressive disclosure is fashionable.

Use this practical heuristic:

```text
higher / always-loaded surface
→ authorization + critical defaults + routing

deeper Skill
→ operation-specific reusable procedure

deeper conditional reference
→ branch-specific detail needed only under a real trigger
```

### Stop criterion

Stop when every important path has a short, explicit navigation chain and no material behavior depends on discovering an obscure nested instruction by accident.

## 9. Audit lens D — routing and Skill composition

Verify all five admitted Skills remain necessary, distinct, and composable:

```text
Audit / Review
Planning / Design
Build / Implement
Learning-by-Doing overlay
Learning-Only primary mode
```

Audit collision boundaries including:

- Audit vs Planning;
- bounded diagnosis vs Audit/Build;
- Planning followed by Build when both are authorized;
- Learning-by-Doing overlay vs Learning-Only primary mode;
- tiny factual request vs full operation Skill;
- governance subject matter vs Audit/Planning/Build action mode;
- research/evidence activity vs the responsibility it serves.

Confirm the recorded sixth-Skill deferral is consistent with the actual system and does not need reinforcement in root governance unless a real reachability failure is found.

### Stop criterion

Stop when representative requests select one clear primary operation, only necessary overlays/references, and no sixth-Skill responsibility gap is revealed by current evidence.

## 10. Audit lens E — proportionality, forward progress, and anti-rabbit-hole behavior

This is a high-priority user-driven lens.

Verify that governance encourages sufficient rigor without analysis paralysis, perfectionism, or unnecessary ceremony.

Audit for both extremes:

```text
UNDER-ENGINEERING
→ responsibility/risk is not actually satisfied

OVER-ENGINEERING
→ mechanism/process materially exceeds demonstrated responsibility/risk
```

Check that the system prefers:

```text
real responsibility
→ smallest blocking uncertainty
→ smallest discriminating investigation
→ smallest adequate decision/action
→ sufficient proof for the claim/risk
→ stop and continue forward
```

rather than:

```text
interesting uncertainty
→ broad investigation
→ more possible uncertainty
→ more research
→ more process
→ delayed real work without a blocking reason
```

Audit specifically:

1. **Investigation stopping** — unknown-but-irrelevant/deferred questions do not block progress; only material blocking uncertainty requires resolution.
2. **No perfection requirement** — “best imaginable” is not silently substituted for “smallest adequate for the admitted responsibility.”
3. **Planning proportionality** — P0/P1/P2/P3 depth is selected by real coordination/risk, not task size alone.
4. **Audit proportionality** — bounded review does not automatically produce a formal audit artifact or repository-wide scan.
5. **Validation proportionality** — narrow discriminating proof precedes broader regression; broad suites are run only when claim/risk/plan justifies them.
6. **Governance proportionality** — governance checks do not become a project within the project.
7. **LLM work** — LLM-related responsibilities receive calibrated safeguards and evaluation appropriate to current risk/maturity rather than requiring an exhaustive research/evaluation program before the first bounded useful implementation.
8. **Progressive rigor** — observed failures/risks can justify stronger evaluation/hardening later; future possibilities alone do not force full machinery now.
9. **No necessary rigor removed** — anti-ceremony language must not weaken safety, evidence, authorization, correctness, or real product obligations.
10. **Stop-line quality** — plans/Skills/audits contain usable stopping conditions and do not encourage endless nearby cleanup or refinement.

### Stop criterion

Stop when every consequential process requirement can be traced to a useful capability, material risk, or real obligation, and the system still provides a practical path to real work without unnecessary preconditions.

## 11. Audit lens F — communication and source clarity

Verify that the Stage 6 communication/source-clarity refinements remain coherent:

- exact technical terms are retained where precise;
- surrounding explanation uses clear, direct, literal ordinary English;
- unfamiliar project/technical terms are explained rather than replaced with inaccurate simplification;
- Source Clarity remains an implementation-quality outcome, not a comment-volume quota;
- comments/docstrings are required where important responsibility, cross-file flow, invariants, reasoning, semantic/proof transformations, or proof limits would otherwise be unclear;
- obvious syntax is not decorated with redundant explanatory prose;
- Build and Audit conditional Source-Clarity references activate only under their intended pressures.

### Stop criterion

Stop when the rules protect developer/learner understanding without converting source files or assistant responses into tutorials by default.

## 12. Audit lens G — learning quality and transfer

Verify the learning system remains one coherent framework rather than several overlapping pedagogy systems.

Check:

- first exposure teaches required premises before testing them;
- later natural recurrence may use fair retrieval/reconstruction before replaying prior explanation;
- retrieval calibrates assistance rather than becoming a pass/fail gate;
- partial/inaccurate retrieval restores missing explanation;
- immediate recognition is not treated as durable ownership;
- no flashcard/repetition schedule/interleaving bureaucracy was introduced;
- package-local learning depth/mastery remains package-local;
- real source/tests/evidence remain the preferred learning substrate;
- learner ownership is not inferred from AI-generated code or green tests alone.

### Stop criterion

Stop when `OPERATING_GUIDE.md`, Learning-by-Doing, Learning-Only, and package-local owners form one non-duplicative learning hierarchy.

## 13. Audit lens H — governance evaluation harness

Audit `tools/agent-governance/` as an evaluation system, not as semantic authority.

Verify:

1. structural checks remain objective/deterministic;
2. fuzzy semantic judgments are not encoded as brittle regexes;
3. exact Skill/reference targets in case banks are valid routing contracts, not authority claims;
4. every admitted Skill and conditional reference has meaningful positive and negative coverage;
5. cross-operation cases cover important collision/under-application/over-application paths;
6. current cases adequately protect default Learning-by-Doing inheritance across substantive primary operations;
7. current cases adequately protect proportionality/anti-ceremony behavior;
8. if coverage gaps exist, classify them as proposed repairs rather than mutating the case banks during the audit;
9. manual baseline-vs-Skill evaluation limitations remain honestly stated;
10. no unsupported claim of a live runner or statistical pass rate exists.

### Stop criterion

Stop when the harness cleanly separates structure, routing, and behavioral judgment and material new governance rules have discriminating regression surfaces or an explicit justified reason not to add one.

## 14. Audit lens I — branch-diff completeness and unintended changes

Compare the full audit-branch tip against the branch base:

`f0322a5c997b201da740a4333faaeae9db74669d`

Classify every changed file as one of:

```text
INTENDED GOVERNANCE CHANGE
INTENDED SKILL / REFERENCE CHANGE
INTENDED GOVERNANCE-EVALUATION CHANGE
INTENDED PLAN / PROPOSAL / EVIDENCE RECORD
UNEXPECTED OR UNEXPLAINED CHANGE
```

Verify:

- no product source/test behavior changed accidentally;
- no unrelated project work was absorbed into the branch;
- every Stage 1–7 plan's claimed modification boundary matches the actual cumulative history where material;
- the sixth-Skill deferral record is scoped correctly;
- no abandoned experimental governance file remains unintentionally active;
- no file was created merely because a previous design direction once considered it.

### Stop criterion

Stop when every branch change has a clear responsibility and all unexplained changes are either resolved as intended or reported as blockers.

## 15. Audit lens J — lifecycle, proposal, and plan closure

Audit the governance-evolution proposal and Stage plans as historical/execution records.

Verify:

- completed stages are clearly interpretable as completed historical execution coordination;
- proposal wording does not misleadingly present already-resolved questions as still pending where that would cause future agents to restart completed work;
- proposal remains non-controlling provenance/design evidence;
- no plan claims live continuation;
- sixth-Skill deferral is recorded without turning working-memory into a new standing governance owner;
- no stale “next stage” wording can accidentally route a future assistant back into completed governance work;
- any lifecycle/status cleanup needed before merge is identified precisely.

### Stop criterion

Stop when future agents can distinguish completed provenance, standing governance, and live continuation without reconstructing the branch history from conversation.

## 16. Audit lens K — latest-main divergence readiness

The final audit should determine whether the branch is internally ready for latest-main reconciliation, but it must not perform that reconciliation yet unless separately authorized.

Inspect latest `main` only enough to answer:

- has `AGENTS.md` changed since the branch base?
- has `OPERATING_GUIDE.md` changed?
- have any five admitted Skills/references changed?
- has `tools/agent-governance/` changed?
- have plan/governance ownership rules changed materially?
- are changes on latest `main` unrelated product work or overlapping governance work?

Classify divergence as:

```text
NO MATERIAL OVERLAP
→ likely straightforward later reconciliation

MATERIAL OVERLAP
→ exact files/responsibilities requiring reconciliation identified

SEMANTIC CONFLICT
→ not merge-ready until owning conflict is resolved
```

Do not merge/rebase during this audit.

## 17. Behavioral scenario set

The audit should use a small representative scenario set rather than an unbounded prompt catalog.

At minimum include:

1. substantive Build without explicit Learning-by-Doing wording;
2. substantive Audit without explicit Learning-by-Doing wording;
3. substantive Planning/Design without explicit Learning-by-Doing wording;
4. bounded read-only diagnosis;
5. explicit Learning-Only switch;
6. tiny factual lookup that should not load full Skills;
7. tiny familiar Build that should use compact proportional learning behavior;
8. non-trivial Build triggering Source-Clarity reference;
9. governance-system audit triggering Audit governance probes;
10. LLM-related first bounded implementation where some evaluation is needed but exhaustive pre-implementation research is not justified;
11. high-risk/claim-sensitive LLM change where stronger evaluation is justified;
12. investigation with an interesting but non-blocking tangent that should be deferred;
13. completed adequate implementation where optional further refinement should stop;
14. a genuinely under-engineered proposal that must not be accepted merely in the name of simplicity.

For each scenario record qualitatively:

```text
primary operation
Learning-by-Doing default behavior expected?
Skill(s) / conditional references expected?
minimum owners/evidence needed
what must happen
what must not happen
stop condition
```

Do not invent statistical pass rates.

## 18. Finding classification

Every finding should be classified proportionately:

### BLOCKER
A material authorization, ownership, routing, safety, default-mode, proof, or semantic conflict that makes merge unsafe or predictably unreliable.

### MATERIAL REPAIR
Not a fundamental architecture failure, but likely to cause recurring agent drift, over/under-application, stale navigation, or misleading lifecycle behavior.

### MINOR CLEANUP
Clear improvement with low behavioral risk; should not block merge unless several combine into a material ambiguity.

### NO CHANGE / DELIBERATE
Observed repetition, length, or complexity is justified and should remain.

### DEFERRED / EVIDENCE-TRIGGERED
Possible future improvement without enough current evidence; preserve a concrete reconsideration trigger rather than implementing speculatively.

For each non-trivial finding record:

```text
observation
→ affected responsibility
→ evidence
→ consequence
→ classification
→ smallest justified disposition
→ proof needed after any later repair
```

## 19. Audit sequence

Execute in this order to reduce bias and unnecessary scanning:

### Phase 1 — freeze audit identity

Record:

- branch name;
- exact branch tip;
- branch base;
- latest `main` tip when main-divergence analysis begins;
- audit limitations.

### Phase 2 — root and canonical method

Inspect `AGENTS.md` and `OPERATING_GUIDE.md` first for authority, default Learning-by-Doing, proportionality, context/navigation, and canonical method ownership.

### Phase 3 — operation Skills and references

Trace each Skill against root/Guide and inspect activation, action boundary, composition, progressive disclosure, completion, and collision risks.

### Phase 4 — behavioral/evaluation surfaces

Inspect case banks, governance doctor semantics, and evaluation README against the behavior the governance now claims.

### Phase 5 — proposal/plans/evidence lifecycle

Check Stage 1–7 completion records, proposal state, sixth-Skill deferral, and stale restart pressure.

### Phase 6 — complete branch diff

Classify every changed file and verify no accidental scope drift.

### Phase 7 — latest-main overlap

Inspect latest-main changes only after the branch is internally understood, so upstream differences are not confused with branch-design defects.

### Phase 8 — scenario pressure review

Run the bounded representative scenario set against the current governance model and identify under-application or over-application gaps.

### Phase 9 — final disposition

Produce one final audit report with:

- strengths preserved;
- blockers;
- material repairs;
- minor cleanup;
- deliberate no-change decisions;
- deferred/evidence-triggered ideas;
- branch-diff classification summary;
- latest-main overlap summary;
- explicit merge-readiness disposition.

## 20. Proof and limitations

The audit may establish semantic consistency, routing design quality, static branch-diff truth, case coverage, and repository ownership relationships from GitHub-visible evidence.

It must not claim:

- repository-wide executable doctor PASS without the deferred local run;
- statistical model-routing reliability without controlled repeated client trials;
- runtime behavior from documentation alone;
- merge readiness if a material latest-main conflict remains unresolved;
- that a governance rule will never drift merely because prose is currently consistent.

Where client Skill-load traces are unavailable, distinguish declared routing contracts from observed live Skill-loading behavior.

## 21. Pass condition

The final governance audit passes only when all of the following are true at the reviewed revision:

```text
0 unresolved authorization/authority conflicts
+ 0 unresolved semantic-owner conflicts
+ default Learning-by-Doing is reachable and preserved across substantive operation routes
+ Learning-by-Doing method vs full Skill activation is unambiguous
+ Learning-Only boundary remains explicit and product-read-only
+ operation Skill routing is distinct and composable
+ critical defaults are high-salience enough to resist nesting drift
+ conditional detail remains genuinely conditional
+ no material instruction under-application gap remains
+ no material instruction over-application / ceremony gap remains
+ proportionality supports forward progress without weakening real obligations
+ over-engineering and under-engineering boundaries are coherent
+ communication/source-clarity rules remain proportional
+ learning-transfer rules remain fair and non-bureaucratic
+ governance evaluation structure/routing/behavior responsibilities remain separated
+ no stale B2/package-specific global coupling
+ no unexplained branch changes
+ completed proposal/plan/evidence lifecycle is not misleading
+ latest-main overlap is classified and no unresolved semantic conflict is hidden
+ proof limitations are explicit
```

A pass means **ready for the next reconciliation/merge-readiness step**, not “already merged” and not “repository-wide executable doctor passed.”

## 22. Stop line

Stop the audit when:

- all lenses above have a supported disposition;
- every material finding has the smallest owner-specific repair recommendation or is explicitly deferred with a trigger;
- branch changes are classified;
- latest-main overlap is classified;
- merge readiness is stated honestly.

Do **not** inside this audit:

- implement the repairs;
- merge/rebase to `main`;
- run destructive Git operations;
- create a sixth Skill;
- expand into unrelated product/governance redesign;
- keep investigating once additional evidence cannot materially change the merge-readiness conclusion.

If repairs are required, the next step is a separate bounded repair pass authorized from the audit findings. After repairs, rerun only the affected audit lenses plus the necessary final integration checks rather than restarting the entire investigation blindly.

## 23. Execution result and bounded repair closure

### 23.1 Audit execution

The read-only final audit was executed from branch tip `bbc66710ed639119edbcb897b9a1f8bed344418d` against branch base `f0322a5c997b201da740a4333faaeae9db74669d` and the then-current `main` line.

The audit found no fundamental five-Skill architecture failure and no sixth-Skill need. It initially returned **REPAIR REQUIRED BEFORE MAIN RECONCILIATION** for three material issues plus one minor wording cleanup:

1. the default Learning-by-Doing method was strong in root/Guide prose but insufficiently protected against being lost after primary-operation routing when Ali did not explicitly name the mode;
2. material-state ownership was correct, but the loop could be read as requiring preservation only after work rather than progressively when needed;
3. Stage-1 and proposal lifecycle wording could make already-completed work look pending;
4. the root loop heading used project-identity `Learning-by-Building` wording where the actual operating mode is `Learning-by-Doing`.

The audit also deliberately kept the global proportionality/anti-rabbit-hole system unchanged: real B2/X1 evidence showed the recent LLM over-ceremony problem was a local plan-sequencing defect, while the root/Guide proportionality rules were already adequate.

### 23.2 Separately authorized repair pass

Ali subsequently authorized the complete bounded repair/refinement pass. The repair changed only governance/evaluation/lifecycle surfaces required by the findings:

- `AGENTS.md`
  - renamed the root loop to **Mandatory Learning-by-Doing execution loop** while preserving learning-by-building as project identity;
  - states explicitly that substantive work uses the Learning-by-Doing method even when Ali does not name it;
  - states that primary-operation selection does not disable the method;
  - separates default method from proportional full Learning-by-Doing Skill loading;
  - clarifies progressive material-state preservation and rejects continuous logging ceremony.
- `OPERATING_GUIDE.md`
  - mirrors the canonical default-method vs full-Skill distinction;
  - makes progressive before/during/after material-state preservation explicit;
  - keeps tiny/repetitive work compact and standalone Learning-Only distinct.
- `tools/agent-governance/consistency_cases.json`
  - adds `CONSISTENCY-016`, a critical default-mode case for substantive Build when Ali does not explicitly invoke Learning-by-Doing;
  - requires pre-action orientation, real work, evidence, proportional preservation, post-action closure, and no ceremonial full-Skill loading.
- `tools/agent-governance/README.md`
  - documents the default-method regression surface and includes silent loss of substantive Learning-by-Doing behavior in the critical regression policy.
- `plans/UPGRADEPILOT_AGENT_SKILLS_GOVERNANCE_STAGE1_CORRECTIONS_PLAN.md`
  - reconciles Stage 1 as structurally complete;
  - makes the full repository doctor run an explicit final post-merge obligation rather than an open Stage-1 continuation gate.
- `proposals/2026-08-27_UPGRADEPILOT_AGENT_SKILLS_AND_GOVERNANCE_EVOLUTION_PROPOSAL.md`
  - marks the proposal `Partially admitted`;
  - preserves future-tense candidate text as historical provenance rather than an open queue;
  - records the six original pre-implementation decisions as resolved;
  - preserves sixth-Skill and client/live-runner ideas as deferred/evidence-triggered rather than active.

No operation Skill, product source/test, specification, ADR, product plan, or root `MEMORY.md` was changed by this final repair pass.

### 23.3 Targeted re-audit

Only the affected lenses plus final integration checks were rerun, as required by §22.

Results:

```text
Authority / canonical ownership
→ PASS at reviewed scope
→ root and Guide preserve their existing owners; Skills remain procedural

Default Learning-by-Doing reachability
→ PASS
→ cold-start rule is at root
→ primary operation does not disable it
→ full Learning-by-Doing Skill loading remains proportional

Learning-by-Doing vs Learning-Only
→ PASS
→ standalone Learning-Only still requires explicit pause and remains product-read-only

Progressive material-state preservation
→ PASS
→ may occur before/during/after when material
→ no continuous-memory/write ceremony introduced

Progressive disclosure
→ PASS
→ conditional Build/Audit references remain conditional; no new reference/Skill introduced

Proportionality / anti-rabbit-hole behavior
→ PASS
→ no new global LLM ceremony added
→ smallest adequate work/evidence/stopping rules preserved

Behavioral regression protection
→ PASS structurally/semantically at the reviewed case-contract level
→ CONSISTENCY-016 directly protects the real observed default-mode drift risk
→ no statistical live-agent reliability claim is made

Lifecycle closure
→ PASS
→ Stage 1 no longer looks open
→ proposal no longer presents resolved pre-implementation questions as current work

Sixth Skill
→ DEFERRED / NO CHANGE
→ exactly five admitted Skill directories remain the intended catalog
```

### 23.4 Branch-diff and latest-main readiness

The complete governance branch remains scoped to governance/Skills/references/plans/proposal/evaluation/working-memory surfaces; no product `src/` or product-test behavior was absorbed by this branch.

Latest-main was rechecked at:

`main@be8682b4e48a1836a93fabb2f857fa8c28aa33ad`

Compared with the shared base, those 27 main-line commits affect B2 `MEMORY.md`, B2 plans/working-memory, experiment source/tests, one developer smoke runner, and audit lifecycle state. They do **not** modify:

- root `AGENTS.md`;
- `OPERATING_GUIDE.md`;
- any of the five admitted Skills or their references;
- `tools/agent-governance/`;
- the governance-evolution proposal/plans.

Latest-main divergence is therefore classified:

```text
NO MATERIAL GOVERNANCE OVERLAP
```

No semantic merge conflict is currently visible from the GitHub compare evidence.

### 23.5 Final disposition

At the reviewed repair state, the final audit disposition is:

```text
READY FOR MAIN RECONCILIATION
```

This means the governance/Skills branch is internally ready to be reconciled with the latest `main` and then considered for merge. It does **not** authorize or perform that merge by itself.

Remaining explicit limitation/obligation:

```text
NO repository-wide executable governance_doctor.py PASS is claimed yet.
```

The agreed final executable validation remains:

```text
finalize/reconcile branch
→ merge only after Ali's explicit merge authorization
→ pull merged main locally
→ python tools/agent-governance/governance_doctor.py
→ repair only concrete failures if any
```

No sixth Skill, live model-evaluation runner, client-specific invocation metadata, or additional governance redesign is required before main reconciliation by the evidence established in this audit/repair cycle.