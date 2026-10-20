# Project-wide technical audit and correction program plan

**Artifact:** Controlling bounded program plan for the dedicated audit/correction branch. `MEMORY.md` alone owns the exact live continuation.

**Branch baseline:** `audit/project-wide-system-audit-2026-10-20`, created from `main` commit `a1c291c6cf9238493eeb666b184192ed178b90f1` on 2026-10-20.

**Responsibility:** Systematically audit UpgradePilot's governance, product-value logic, plans, architecture, implementation, tests, experiments, evidence, operational documentation and learning/ownership process; classify misleading, incorrect, weak, duplicated, stale or unnecessarily complex mechanisms; then repair selected findings through their proper owners with proportionate proof and preserved learning.

**Program outcome:** A smaller, more coherent and better-proven UpgradePilot whose important claims, owners, architecture, source paths, tests, experiments and user-facing instructions agree with each other and with the product thesis. The program may legitimately conclude that some inspected mechanisms are already correct and should be retained.

This plan does **not** predetermine a rewrite, architecture replacement, LLM/agent adoption, mass cleanup, product-value benchmark, or merge into `main`.

---

## 1. Why this program exists

UpgradePilot has accumulated substantial real capability and unusually strong evidence/claim discipline, but recent review exposed a second-order risk: the project now contains enough governance, plans, Workspace machinery, experiments, qualification evidence and historical controls that local correctness no longer guarantees global coherence.

The audit therefore asks two questions together:

1. **Are the current methods, designs, controls and claims technically correct and proportionate?**
2. **Are they still the best use of complexity for the product responsibility UpgradePilot is supposed to solve?**

The program must not invent defects merely because the system is sophisticated. Conversely, effort already spent, passing tests, historical plans, current callers and existing abstractions are not sufficient reasons to keep a mechanism.

The starting durable observations are preserved in [AUDIT-012](../audits/2026-10-20_AUDIT-012_project-wide-system-audit-baseline.md). They are entry evidence, not a closed list. New findings may strengthen, narrow, supersede or clear them.

The latest `main` input also includes [the product-value feasibility review patch notes](../working-memory/2026-10-20_product-value-feasibility-plan_review_patch-notes.md). Those notes remain non-controlling until their owning artifacts are reconciled; this audit branch must not silently execute or absorb their requested changes.

---

## 2. Authority, evidence and branch boundary

Use the existing owner model rather than creating a parallel governance system:

| Question | Primary owner / proof surface |
| --- | --- |
| Mission, supported user/decision, product boundary, evidence doctrine, claim limits | `PROJECT_CHARTER.md` |
| Project route and stable stage outcomes | `plans/UPGRADEPILOT_90_DAY_PLAN.md` |
| Exact live continuation on this branch | `MEMORY.md` |
| Project-wide working/learning method | `OPERATING_GUIDE.md`, root `AGENTS.md` |
| Stable product semantics/invariants | accepted `docs/specifications/` owner |
| Accepted consequential method/structure | accepted ADR under `docs/architecture/` |
| One bounded audit/fix sequence | this plan or a narrower selected plan when needed |
| Actual behavior | active source, tests, reproducible command/output evidence |
| Experiment behavior | `experiments/`, experiment tests and retained run evidence |
| Durable findings | `audits/` |
| Detailed dated progression | one active cycle record under `working-memory/` |

### Branch isolation

This branch is deliberately separate from `main` so audit findings and corrective work can evolve without silently redefining the canonical product while they are still under review.

Before every major audit or remediation cycle:

1. inspect the current `main` head;
2. compare it with this branch's last reconciled `main` base;
3. identify only material upstream deltas for the current responsibility;
4. record whether the branch remains valid, needs selective reconciliation, or has a conflict;
5. do not merge/rebase/cherry-pick `main` automatically merely because it moved.

A later upstream change may resolve a finding, create a new one, or invalidate a planned correction. Preserve that explicitly.

No branch merge into `main` is authorized merely because this program completes work. Final integration requires an explicit review of the branch diff, current-main divergence, unresolved findings and proof state.

---

## 3. Audit discipline

Each substantive finding should be classified with the smallest defensible conclusion.

### Finding type

Use one of these reasoning classes when useful:

- **implementation defect** — active behavior violates an admitted contract;
- **documentation drift** — current instructions/claims conflict with source or canonical owner;
- **governance/state drift** — authority/lifecycle/live-state boundaries are stale or duplicated;
- **proof gap** — behavior/scope is claimed more broadly than the available proof;
- **architecture/migration debt** — an accepted transition is incomplete and creates a material divergence risk;
- **experiment-method defect** — design/control/confounding makes an experiment misleading or inefficient;
- **unnecessary complexity / simplification opportunity** — mechanism cost is not justified by an independent current responsibility;
- **learning/ownership debt** — engineering completion materially outruns the project's explicit ownership objective;
- **open hypothesis** — plausible concern that needs discriminating evidence before being called a defect;
- **cleared concern / justified complexity** — audit confirms the current mechanism is correct and proportionate.

### Priority

- **P0** — evidence integrity, security or canonical-state problem that can materially invalidate current work; normally stop affected progression.
- **P1** — materially blocks product value, trustworthy integration, major architecture correctness or interpretable evaluation.
- **P2** — consequential drift, proof gap, migration risk, maintainability issue or bounded design weakness.
- **P3** — cleanup, clarity or optimization whose delay does not materially distort current engineering decisions.

Priority is about project consequence, not code size or difficulty.

### Minimum finding record

For a durable finding preserve:

```text
observation
→ evidence / inspected revision
→ exact owner / affected responsibility
→ interpretation
→ uncertainty / counterevidence
→ priority + finding type
→ cheapest credible correction or discriminating check
→ proof required after change
→ disposition
```

A concern may remain unresolved. Do not create a fix merely to make the ledger look complete.

---

## 4. Starting observations to carry into the audit

The initial audit baseline already records these concerns. They must be revalidated against current branch/main state before correction rather than treated as permanent truth:

1. **Product-value proof sequencing and experiment economics.** Recent Investigator work spent substantial effort on qualification/control machinery before the product-versus-transparent-baseline value question was sufficiently resolved. The October 19–20 strategic direction is a promising correction rather than something to discard.
2. **Canonical integration verification weakness.** `main` was unprotected at the branch point, the product workflow was manual-dispatch only, and the last observed hosted success predated the recent Workspace/Investigator work by more than two weeks.
3. **Live-state/governance drift.** Audit lifecycle indexes retained old current-coordination language while `MEMORY.md` had moved on.
4. **Operational documentation mismatch.** README local-model endpoint text conflicted with the canonical environment and current extractor implementation.
5. **Charter time-boundary staleness.** The controlling Charter's stated 90-day execution period ended before the current work continued.
6. **Accumulated Learning-by-Doing closure debt.** Several recent consequential cycles retain D/E or learner-ownership debt.
7. **Workspace migration dual-surface risk.** Current orchestration still exposes the legacy investigation result while Workspace adoption/cutover remains incomplete; this needs an end-to-end ownership audit, not an assumption that either surface is wrong.
8. **Python compatibility proof mismatch.** Package metadata declares Python `>=3.12` while hosted verification observed only Python 3.12.
9. **Universal Smart Situational Override concern.** The override mechanism may be correctly designed, but its breadth across governance artifacts deserves a dedicated audit for authority weakening, context cost and inconsistent enforcement.
10. **Current product-value plan amendment is pending.** `main` now contains review patch notes proposing S001–S016 light screening, explicit bounded multi-role evaluation as a candidate, semantic-premise adequacy and explicit pre-Build authorization. The owning plan/MEMORY had not yet incorporated those notes at the branch point.

These are starting inputs, not the audit's final result.

---

## 5. Audit domains

Audit by end-to-end responsibility rather than file count.

### Domain A — governance, authority and current-state integrity

Check:

- Charter/route/plan/MEMORY/ADR/specification ownership boundaries;
- stale execution periods, live-state leakage and lifecycle indexes;
- Smart Situational Override scope and whether it can weaken otherwise useful gates;
- duplicated procedural rules and unnecessary persistent context;
- branch/integration policy, hosted CI expectations and repository settings;
- documentation claiming current behavior from historical evidence;
- whether audit/proposal/working-memory artifacts are accidentally acting as control owners.

Expected output: exact governance defects/simplifications plus items confirmed correct.

### Domain B — product thesis, value and evaluation sequencing

Trace the Charter thesis through current product behavior and evaluation:

```text
transparent baseline
→ richer product evidence
→ actual additional maintainer information
→ interpretation/evaluation
→ synthesis/report
→ evidence that the extra machinery changes a useful decision
```

Audit:

- whether product-value evidence arrived at the correct time;
- current abstain-only boundary and what value can still be demonstrated before non-abstention;
- scenario selection/exposure and the new S001–S016 review proposal;
- protected versus exposed development evidence;
- semantic adequacy criteria;
- whether future deterministic, single-pass semantic, multi-role or deployment experiments answer distinct residual questions;
- cost/maintenance/information value of each candidate direction.

Do not execute the prepared six-hour feasibility investigation merely because it exists. Its current plan/amendment must first survive this program's consistency review or be explicitly selected later.

### Domain C — architecture and end-to-end evidence ownership

Trace the normal product path:

```text
public PR locator
→ acquisition and exact identity
→ native facts/assessments
→ Workspace capture/lifecycle/recovery state
→ interpretation/evaluation/applicability
→ maintainer-action synthesis
→ report projection/save/open
```

For each material fact/state/check:

- identify the normal producer;
- identify the earliest sufficient owner;
- trace projections/duplication;
- determine whether later validation proves a distinct proposition;
- identify material evidence lost in legacy/result projections;
- check invalidation/staleness/recovery/replay distinctions;
- locate temporary migration surfaces and their removal/reassessment triggers.

Particular pressure: ADR-0012/0013 versus the still-existing `PublicPullRequestInvestigation` path and Workspace consumer migration.

### Domain D — active implementation quality and proportionality

Inspect source only where it answers a responsibility question. Look for:

- duplicated transformations/authority checks;
- fixture-shaped branches or hardcoded semantic assumptions;
- overly generic records with weak product meaning;
- configuration hidden in source when it creates a real supported-deployment problem;
- dead/transitional code whose reason has expired;
- complex defensive boundaries that protect only fabricated internal states;
- exception/failure handling that turns operational failure into semantic evidence;
- names/comments/interfaces that obscure responsibility;
- unnecessary compatibility layers.

Do not optimize aesthetics at the cost of evidence semantics.

### Domain E — tests, CI, reproducibility and operational proof

Audit the proof system, not raw test count:

- focused versus integration/end-to-end responsibility coverage;
- duplicated tests and unprotected cross-module seams;
- local-only evidence versus hosted evidence;
- push/PR CI and branch protection needs;
- supported Python/version/dependency matrix versus actual proof;
- installation/package/CLI proof;
- deterministic replay versus recovery/inspection;
- model-free deterministic regressions versus live-provider qualification;
- failure and changed-case controls.

Target: the smallest sufficient proof set with a credible canonical integration gate.

### Domain F — Investigator/LLM/agent experiment methodology

Audit both useful mechanisms and accumulated experiment cost:

- qualification-to-semantic attempt ratio and information value;
- completion-affordability/controller invariants;
- model/deployment/runtime confounds;
- supplied-evidence versus autonomous discovery comparisons;
- source/reference/citation entailment;
- exposure/contamination and repeated tuning on known fixtures;
- reviewer independence and oracle leakage;
- whether a multi-role experiment would isolate responsibility decomposition or merely add calls;
- experiment/product boundary and adoption criteria;
- cleanup, accounting and unknown usage treatment.

A negative or rejected experiment remains valid progress when the method is rigorous.

### Domain G — learning, documentation and maintainership readiness

Audit whether the project remains a learning-by-building flagship rather than merely a high-quality AI-generated repository:

- D/E debt and unanswered ownership checks;
- repeated approval without demonstrated reasoning transfer;
- source areas Ali should be able to trace/modify/diagnose;
- README/operator instructions versus current implementation;
- whether documentation volume helps recovery or obscures current truth;
- whether future portfolio claims match actual ownership and proof.

Learning debt must not be used to retroactively invalidate correct engineering; it is a separate program responsibility.

---

## 6. Ordered program route

The route is deliberately progressive. New evidence may reorder bounded items under the existing Smart Situational Override rule, but material changes must be recorded.

### Stage 0 — branch/program preparation

- branch from exact current-main SHA;
- create this program plan;
- preserve initial audit baseline;
- initialize branch working-memory and branch-local live handoff;
- verify branch-only diff.

**Pass:** the branch can be resumed by another session without relying on chat context.

### Stage 1 — governance/current-state integrity audit

Start here because stale authority can invalidate conclusions in later domains.

Revalidate the initial governance/documentation/CI findings, inspect current-main changes, and decide which issues are defects versus deliberate temporary states.

**Stop:** do not mass-edit governance while still discovering its ownership model.

### Stage 2 — product-value and evaluation audit

Reconcile the strategic proposal, product-value plan, latest patch notes, simulations, retained experiment evidence and actual product output boundary.

Determine which next product-value questions are worth paying for and which existing experiment directions should be stopped/deferred.

**Stop:** no benchmark/model execution solely to complete an old denominator.

### Stage 3 — architecture/source-flow audit

Perform the producer → Workspace → evaluator/synthesis → report trace. Inspect Workspace replacement/migration, native capture/reconstruction, lifecycle validity, report compatibility and remaining dual surfaces.

**Stop:** do not refactor until a finding names the correct owner and lost/protected behavior.

### Stage 4 — test/proof/operational audit

Map important claims to focused/integration/hosted proof. Classify test duplication, missing integration gates, compatibility-scope mismatches and reproducibility gaps.

### Stage 5 — Investigator/experiment audit

Consolidate prior AUDIT-011 evidence with later Build/comparison results. Decide which experiment machinery remains justified, which is reusable infrastructure, and which has become dead/over-specialized research support.

### Stage 6 — consolidated decision review

Produce a prioritized cross-domain disposition:

```text
fix now
→ fix before merge but after prerequisite
→ simplify/remove
→ retain as justified
→ defer with trigger
→ investigate with exact missing premise
→ historical only
```

Resolve conflicts among findings before implementation. Do not implement two individually sensible fixes that create a worse combined architecture.

### Stage 7 — bounded remediation cycles

Each selected correction becomes one coherent cycle or a small group only when their owner/proof boundary is genuinely shared.

Normal sequence:

```text
reconcile current branch/main + owner
→ A1/A2 orientation
→ inspect exact finding
→ update spec/ADR/plan first only when that owner must change
→ implement smallest adequate correction
→ focused proof
→ broader regression / hosted proof when justified
→ D ownership learning
→ E closure + finding disposition
```

Examples:

- a stale README endpoint can be a tiny documentation correction;
- automatic CI/branch integration may require workflow plus repository-setting proof;
- Workspace cutover is a consequential migration responsibility, not a cleanup patch;
- experiment redesign requires a new frozen comparison contract rather than editing historical results.

### Stage 8 — integration readiness and closure

Before any merge to `main`:

- compare against latest `main`;
- review the complete branch diff by responsibility;
- ensure all P0 findings and all selected P1 corrections are resolved, rejected with evidence, or explicitly deferred with a defensible consequence;
- run the strongest applicable deterministic/hosted proof;
- confirm no historical experiment/audit evidence was rewritten to manufacture consistency;
- reconcile documentation and live state;
- preserve unresolved debt and learning boundary;
- explicitly decide merge/rebase/split/discard.

No automatic merge follows from passing tests.

---

## 7. Progressive recording model

Use the smallest durable artifact that matches the information:

- **one working-memory record per substantive audit/remediation cycle** for chronological progression and learning gates;
- **AUDIT-NNN records** for findings whose reasoning must survive beyond one cycle or drive separate follow-ups;
- **existing specifications/ADRs** when stable semantics/method actually change;
- **this plan** only when the durable program route/proof/stop logic changes;
- **MEMORY.md** only for current branch continuation/handoff;
- **source/tests/commands/evidence** for implemented truth.

Do not create a new plan/audit/ADR merely because another file is convenient. Do not put an evolving issue tracker into this plan.

When several findings are discovered during one audit cycle, preserve them in that cycle first; promote only material durable findings after review.

---

## 8. Proof expectations for corrections

Use proof proportional to the corrected responsibility.

| Change | Minimum expected proof |
| --- | --- |
| Documentation/current-owner correction | compare against canonical source/owner; inspect links/examples; no full product suite unless behavior changed |
| Governance/lifecycle correction | cross-owner consistency check and stale-state negative check; test automation if a deterministic enforcement mechanism is introduced |
| Product Python/source change | focused tests + nearest integration tests; full deterministic suite when central/shared behavior changes |
| Workspace migration/cutover | native semantic regressions, reconstruction/history/material-validity controls, consumer parity/removal proof, fresh-process/recovery proof as applicable |
| Workflow/package compatibility change | syntax/config validation + branch/hosted execution where available; package install/CLI checks when affected |
| Experiment controller/interface change | deterministic experiment tests + frozen pre-execution verification; actual model calls only when separately authorized by the selected experiment |
| Experiment conclusion | preregistered/frozen method, complete accounting, semantic review at the stated independence level, explicit non-generalization limits |

Passing tests establish only their protected behavior. They do not automatically establish product value, semantic adequacy, learner ownership or architecture necessity.

---

## 9. Prohibited shortcuts

Do not:

- rewrite historical evidence or experiment outputs to match current conclusions;
- treat `main` movement as an automatic instruction to merge it into this branch;
- mass-refactor before owner/finding classification;
- add an agent/model/framework because the project would look more advanced;
- delete a complex mechanism merely because it is complex;
- preserve a mechanism solely because it has tests/callers/history;
- use one passing fixture as proof of product generality;
- convert missing evidence into a negative fact;
- equate more citations with semantic adequacy;
- equate abstention with product value by itself;
- conflate Workspace recovery, saved-report reopening and deterministic replay;
- allow a complete findings packet to self-authorize Build/model/network/target execution;
- silently widen the supported ecosystem beyond public Python Dependabot work;
- claim learner ownership because AI-assisted implementation is correct;
- merge this branch automatically when the plan completes.

---

## 10. Program success and stopping conditions

The program is successful when we can defend all of the following, even if some individual findings are deliberately deferred:

1. Current product/governance claims identify the correct owner and do not materially contradict active implementation.
2. Central architecture has one clear authority path per material responsibility, with transitional duplication explicitly bounded.
3. Product-value work precedes expensive new interpretation machinery when it can discriminate the investment decision.
4. Important experiments answer isolated questions with interpretable costs and rejection conditions.
5. Canonical integration has proportionate automated proof rather than relying only on dated local evidence.
6. Supported compatibility claims match actual proof or are explicitly qualified.
7. Documentation/operator instructions describe current behavior and environment correctly.
8. Unnecessary complexity is removed or retained with an independent current rationale.
9. Remaining debt is explicit, prioritized and owned.
10. Ali has completed enough evidence-backed D/E work to explain, challenge, modify and diagnose the central paths changed by this program.

Stop/narrow the program if continued auditing stops changing engineering decisions and becomes checklist activity. A complete audit of every file is not a success criterion.

---

## 11. First selected follow-up after preparation

After Stage 0 is reviewed, begin **Stage 1: governance/current-state integrity audit** from the exact branch baseline and latest `main` comparison.

The first pass should revalidate, rather than immediately fix:

- `main` integration/hosted verification boundary;
- Charter time-boundary status;
- audit lifecycle current-state leakage;
- README/environment/provider endpoint mismatch;
- Smart Situational Override authority/duplication footprint;
- current product-value-plan amendment/live-handoff consistency.

Then present the classified findings and smallest recommended corrections before entering remediation.

No product source change, model call, benchmark, network acquisition, target execution or merge is part of this preparation stage.
