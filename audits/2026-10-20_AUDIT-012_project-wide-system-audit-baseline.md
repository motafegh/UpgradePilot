# AUDIT-012 — Project-wide system audit baseline

**Audit date:** 2026-10-20  
**Inspected `main` revision:** `a1c291c6cf9238493eeb666b184192ed178b90f1` (`Record review patch notes for product-value feasibility plan`)  
**Mode:** cross-responsibility audit baseline  
**Authority:** non-controlling evidence/recommendations. The branch program plan and `MEMORY.md` coordinate later work; findings do not self-authorize implementation.

## 1. Question and scope

This baseline begins a broader audit of whether UpgradePilot's recent governance, product-value sequencing, architecture, Workspace migration, tests/CI, Investigator experiments, documentation and Learning-by-Doing process remain technically correct, proportionate and mutually consistent.

It is deliberately **not** a claim that every listed concern is already a root-cause defect. The purpose is to preserve the strongest initial evidence-backed findings and the important unresolved hypotheses so later cycles can revalidate them against source and current `main` before correction.

The owning program route is [Project-wide technical audit and correction program plan](../plans/PROJECT_WIDE_TECHNICAL_AUDIT_AND_CORRECTION_PROGRAM_PLAN.md).

## 2. Overall assessment

UpgradePilot is not generally architecturally unsound. Several recent choices are strong and should be protected during correction:

- explicit separation of source evidence, interpretation/proposals, evaluation, proposition state and maintainer-action permission;
- a canonical Workspace direction rather than letting an LLM or report object become truth authority;
- strong uncertainty/claim discipline and explicit unresolved/problem states;
- bounded local inference rather than hidden cloud dependence;
- retained negative experiment evidence instead of rerunning until a favorable result appears;
- the October 19–20 strategic correction toward product-value/baseline feasibility before another large interpretation subsystem.

The main project-level risk is now **global coherence and sequencing**: the repository has enough plans, evidence surfaces, Workspace migration state, experiment controls and historical lifecycle artifacts that locally correct pieces can still disagree, overclaim, duplicate responsibility or consume disproportionate effort.

## 3. Findings and open concerns

### AUDIT-012-F1 — P1 — Product-value proof followed substantial Investigator-method investment

**Type:** product/evaluation sequencing risk.

**Observation:** [AUDIT-011](2026-10-18_AUDIT-011_investigator-experiment-validity-and-progress.md) reconciled one Investigator lineage at 460 qualification attempts plus 45 semantic attempts, approximately 91.1% qualification. Later supplied-evidence and instruction-only cohorts completed but remained semantically inadequate on the exposed cases. The [accepted product-direction proposal](../proposals/2026-10-19_INVESTIGATOR_RESPONSIBILITY_DECOMPOSITION_AND_PRODUCT_DIRECTION_PROPOSAL.md) now recommends proving useful product contribution beyond the transparent baseline before another interpretation subsystem.

**Finding:** The qualification/control work was not automatically waste; it exposed real runtime, reference, budget and cancellation defects. However, the product-value question was not sufficiently early in the sequencing relative to the amount of advanced-method machinery and evaluation cost accumulated.

**Consequence:** Future expensive Investigator/model/agent work should require a named product decision that the experiment can change. The new product-value direction should be preserved unless stronger evidence displaces it.

**Not established:** This does not prove LLMs/agents are unsuitable for UpgradePilot or that all existing Investigator infrastructure should be removed.

---

### AUDIT-012-F2 — P1 — Canonical `main` integration is not automatically protected by hosted product verification

**Type:** proof/integration gap.

**Observation:** At the inspected revision, GitHub reports `main` as unprotected with no required status checks. [.github/workflows/product-verification.yml](../.github/workflows/product-verification.yml) uses `workflow_dispatch` only. The latest observed successful hosted Product verification run was run #17 on 2026-10-02 at commit `1c371875ffb459ce2e2c9c913a5a87a10a434928`, while the branch point is 2026-10-20 `a1c291c6`.

**Finding:** Local cycle evidence can be strong, but recent canonical changes are not automatically subjected to the repository's hosted installed-package/deterministic-product check before becoming `main` history.

**Consequence:** The audit should determine the smallest credible integration gate: likely automatic push/PR deterministic product verification plus an appropriate protected-main/ruleset policy, while keeping GPU/model/live-acquisition proof outside the ordinary merge gate.

**Uncertainty:** Repository-setting changes may require manual GitHub administration even if workflow changes are implementable in source.

---

### AUDIT-012-F3 — P2 — Audit lifecycle indexes contain stale current-coordination language

**Type:** governance/state drift.

**Observation:** [audits/active/README.md](active/README.md) still lists AUDIT-009, AUDIT-010 and AUDIT-011 as inputs to the "current engineering responsibility" and includes dated wording such as AUDIT-009's 2026-10-02 "current coordination boundary" and then-current next responsibility. [MEMORY.md](../MEMORY.md) has since moved the live handoff to the October 20 product-value/baseline direction.

**Finding:** This is live-state leakage into a lifecycle index. The audit owner itself says `MEMORY.md` alone owns live continuation.

**Consequence:** Reclassify or rewrite lifecycle entries so they describe durable selection/relevance without claiming superseded live continuation. The later governance audit should decide whether the lifecycle index needs a structural wording rule or only local cleanup.

---

### AUDIT-012-F4 — P2 — README local-model endpoint contradicts canonical environment/source

**Type:** documentation drift.

**Observation:** The current [README.md](../README.md) states the semantic provider LM Studio base is `http://127.0.0.1:12345`. [ENVIRONMENT.md](../ENVIRONMENT.md) establishes the reusable service boundary at port `18080`, and [support_drop_extractor.py](../src/upgradepilot/upstream/support_drop_extractor.py) uses `http://127.0.0.1:18080`.

**Finding:** The README user instruction is stale and can cause a real operator failure.

**Consequence:** This is probably a small documentation correction after Stage 1 revalidation. Also inspect whether any other current-facing docs still repeat the former port.

---

### AUDIT-012-F5 — P2 — Charter time boundary is stale relative to continued project execution

**Type:** governance/claim drift.

**Observation:** [PROJECT_CHARTER.md](../PROJECT_CHARTER.md) remains controlling and states `Execution period: 2026-07-20 to 2026-10-17`, while substantive project work continued after October 17 and the Charter text still refers to the selected flagship for the "current 90-day execution period."

**Finding:** The stable mission may still be valid, but the explicit time-boundary metadata no longer describes the current project state.

**Consequence:** Decide whether the date was only historical planning metadata, whether the execution period should be explicitly extended/reframed, or whether the Charter should remove time language that no longer controls anything. Do not silently change the product boundary merely to fix the date.

---

### AUDIT-012-F6 — P2 — Consequential engineering has accumulated learner D/E closure debt

**Type:** learning/ownership debt.

**Observation:** Current [MEMORY.md](../MEMORY.md) explicitly preserves pending learner ownership/D/E closure for recent planning, Build and comparison work. Root [AGENTS.md](../AGENTS.md) and [OPERATING_GUIDE.md](../OPERATING_GUIDE.md) make evidence-backed D/E ownership transfer part of the flagship's substantive method.

**Finding:** Deferring D/E occasionally is reasonable; repeated deferral across consequential architecture/experiment work can undermine the project's stated learning-by-building outcome even when the engineering is correct.

**Consequence:** The audit program should maintain a small explicit learning-debt view and close high-value ownership gaps around the central paths changed by the program. Do not confuse learning debt with product correctness.

---

### AUDIT-012-F7 — P2 — Workspace adoption currently retains two semantically important result surfaces

**Type:** architecture/migration risk.

**Observation:** [ADR-0012](../docs/architecture/ADR-0012-canonical-investigation-workspace-and-recovery-boundary.md) selects native producers/evaluators → canonical Workspace → one-way consumer projections and permits the legacy `PublicPullRequestInvestigation` projection only for identified compatibility/proof needs. The current [investigation.py](../src/upgradepilot/investigation.py) still directly constructs `PublicPullRequestInvestigation` while also publishing an immutable Workspace revision. [The implementation/migration plan](../plans/INVESTIGATION_WORKSPACE_IMPLEMENTATION_AND_MIGRATION_PLAN.md) explicitly leaves consumer cutover to later stages.

**Finding:** This is not yet classified as an implementation violation; it is a real transitional dual-surface risk. Until cutover completes, consumers/tests can accidentally depend on different semantic surfaces or cause duplication to become permanent.

**Consequence:** The architecture/source-flow audit must trace all current consumers, parity obligations, omitted material and retirement triggers before recommending removal or further migration.

---

### AUDIT-012-F8 — P2 — Declared Python compatibility is broader than hosted compatibility proof

**Type:** proof/scope mismatch.

**Observation:** [pyproject.toml](../pyproject.toml) declares `requires-python = ">=3.12"`. The hosted product workflow currently runs Python 3.12 only.

**Finding:** There is no evidence here that later Python versions fail, but the installable compatibility declaration is broader than the hosted compatibility proof attached to it.

**Consequence:** Audit the intended compatibility policy. Either test a justified supported-version set or qualify/narrow the declaration. Do not add arbitrary matrix cost without deciding what support promise is intended.

---

### AUDIT-012-F9 — OPEN / P2 candidate — Smart Situational Override may be too globally permissive or costly

**Type:** governance hypothesis; not yet a confirmed defect.

**Observation:** Root `AGENTS.md`, plans, Charter, working-memory and operation Skills repeatedly incorporate the Smart Situational Override rule, including interpretation of project-local MUST/REQUIRED/STOP/GATE language.

**Concern:** The rule may be a valuable antidote to mechanical process-following, but broad duplication and override semantics may weaken the predictive force of gates, increase context cost, or make two agents interpret the same "mandatory" instruction differently.

**Required audit:** Trace canonical ownership, actual reinforcement sites, non-overridable boundaries, examples of legitimate overrides, and whether simpler language or narrower scope could preserve flexibility without diluting controls.

**Do not fix yet:** Complexity alone is not evidence that the rule is wrong.

---

### AUDIT-012-F10 — OBSERVATION — Product-value feasibility plan is under an unincorporated review amendment

**Type:** current planning consistency input.

**Observation:** `main` head `a1c291c6` added [2026-10-20_product-value-feasibility-plan_review_patch-notes.md](../working-memory/2026-10-20_product-value-feasibility-plan_review_patch-notes.md). The notes request four material changes before investigation execution: S001–S016 light screening then a discriminating deep cohort; explicit bounded multi-role semantic interpretation/validation as a candidate; material-premise rather than citation-cardinality adequacy; and explicit acceptance before any follow-on Build/execution. At the branch point, the owning plan and `MEMORY.md` still describe the previous six-case prepared plan.

**Assessment:** This is not itself a defect because the patch notes explicitly declare themselves non-controlling. It is a pending consistency boundary. The audit branch must not execute the old plan as though review were complete, nor silently treat the patch notes as accepted semantics.

---

## 4. Positive findings to protect

A project-wide audit must also prevent regressions caused by indiscriminate simplification.

### AUDIT-012-P1 — Evidence/authority separation is a strong architectural invariant

Current architecture correctly distinguishes exact/native evidence, model proposals, lifecycle processing outcomes, proposition truth state, evaluator authority and maintainer-action permission. Preserve this unless a stronger owner-level argument changes it.

### AUDIT-012-P2 — The bounded local support-drop extractor has meaningful trust controls

Although its README endpoint is stale, the implementation itself deliberately uses a loopback provider, disables ambient proxy inheritance for the request path, constrains the structured selection, recovers exact source lines deterministically and refuses malformed/unsupported outputs as unresolved. Audit portability/configuration separately; do not misclassify this as an uncontrolled LLM authority path.

### AUDIT-012-P3 — Recent negative Investigator results are useful evidence

The failure of supplied-evidence/instruction-only cohorts to reach semantic adequacy is a valid result at its stated scope. Preserve partial improvements, failures and costs. Do not regrade or overwrite historical results while designing a successor method.

### AUDIT-012-P4 — The new product-value-first strategic correction is technically promising

The current strategic proposal explicitly resists another generic parser/validator/agent programme before proving value and a real consumer. The audit should challenge details, including the new patch notes, without discarding this correction merely because it arrived late.

## 5. Initial disposition

| Item | Initial disposition |
| --- | --- |
| F1 product-value sequencing | retain as P1 program input; audit product/value chain before more expensive semantic work |
| F2 hosted/main integration gap | revalidate first; likely remediation candidate |
| F3 lifecycle state leakage | revalidate first; likely small governance remediation |
| F4 README endpoint | revalidate/search duplicates; likely immediate small correction after review |
| F5 Charter time boundary | governance decision required before edit |
| F6 learner D/E debt | track separately and repair proportionately during cycles |
| F7 Workspace dual surfaces | deep architecture/consumer trace before any removal |
| F8 Python support proof | decide support policy before changing matrix/metadata |
| F9 Smart Override breadth | dedicated governance audit; no premature rewrite |
| F10 plan patch notes | reconcile in product-value audit; no execution before explicit plan review/selection |

## 6. Immediate handoff

Begin with **governance/current-state integrity**, because inaccurate authority/current-state surfaces can distort every later audit.

The first cycle should inspect the exact owner chain and current branch/main evidence for F2–F5, F9 and F10; classify which require local edits, owner changes, repository settings, or no change. Preserve the audit before entering remediation.

No product source modification, model inference, benchmark, target execution or historical-evidence mutation is authorized by this audit record.
