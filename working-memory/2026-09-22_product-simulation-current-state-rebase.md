# Product Simulation Current-State Rebase — Active Working Memory

**Date:** 2026-09-22  
**Session status:** ACTIVE  
**Branch:** `research/product-simulation-rebase-2026-09-22`  
**Primary responsibility/mode:** Product Simulation research + current-state coverage rebase  
**Related owners:** `product-simulation/AGENTS.md`, `product-simulation/SIMULATION_GOVERNANCE_AND_PLAN.md`, `product-simulation/CASE_SELECTION_FRAMEWORK_V2.md`, root governance and current product evidence  
**Working-memory procedure:** `UP-SKILL:upgradepilot-working-memory`

## 1. Session anchor

This is a parallel, non-blocking Product Simulation workstream isolated from the ongoing main progress.

The existing Product Simulation corpus was created against earlier product states. UpgradePilot has since accumulated substantial Phase A work, later Phase B work, audits, parser/runtime strengthening, evidence-path repairs, and additional product responsibilities. The current research arm therefore must not narrow itself to the main conversation's immediate Phase B question.

The purpose of this branch is to rebase Product Simulation against the **whole current product surface**, identify what newly built or changed responsibilities lack adequate real-world pressure, and research only the real cases that can materially validate, challenge, or refine current product assumptions.

### Boundaries

- Do not modify product source, tests, stable specifications, accepted plans, root `MEMORY.md`, or the main workstream's active working memory unless Ali explicitly authorizes it.
- Keep this branch's work focused on Product Simulation research/evidence and its own working memory.
- Target repositories are read-only evidence sources: no comments, approvals, reruns, pushes, merges, credential use, or other mutation.
- Do not create scenarios merely to increase case count.
- Do not assume current design is correct; real evidence may validate, narrow, challenge, or contradict it.
- Do not generalize convenience-sample prevalence to ecosystem prevalence.
- Do not immediately number a new scenario. First establish a discriminating question and evidence gap.

## 2. Current research route / TODO

### R1 — Reconstruct product evolution relevant to Product Simulation
- Review the important product changes since the last substantial simulation wave.
- Include Phase A records and outcomes, later Phase B work, relevant audits, completed implementation plans, current source/test behavior, and active evidence responsibilities.
- Separate accepted/current behavior from historical plans and superseded assumptions.

### R2 — Rebase existing Product Simulation coverage
- Map current Product Simulation cases, screenings, pressure tests, and syntheses against today's product responsibilities.
- For each current responsibility classify coverage as:
  - adequately pressure-tested by real evidence;
  - partially covered / older product shape;
  - synthetic-only;
  - not materially covered.

### R3 — Build a coverage-gap / research-question inventory
- Convert uncovered or stale areas into explicit real-world questions.
- Prefer questions that can discriminate between materially different product interpretations.
- Include positive, negative, ambiguous, degraded-evidence, and ordinary-control shapes where useful.
- Candidate areas are not fixed in advance; likely seams to inspect include command semantics/control flow, CI consumption identity, runtime strengthening, package-manager semantics, package-state proof, target/environment evidence, artifact applicability, public acquisition/authentication effects, evidence retention, uncertainty and stopping.

### R4 — Prioritize case families before individual cases
For each candidate family, establish:
- exact question;
- why existing Product Simulation evidence is insufficient;
- what decision/design/proof boundary it could change;
- real evidence feasibility;
- negative-result value;
- claim limit;
- stop condition.

Use `CASE_SELECTION_FRAMEWORK_V2.md` as a discovery/evaluation aid rather than mechanically scoring everything.

### R5 — Screen real public cases broadly
- Prefer public Python Dependabot / GitHub Actions cases when they fit the question.
- Search broadly enough to see ordinary controls and counterexamples, not only unusual edge cases.
- Preserve exact repository, PR, revision, workflow/job/step, command/configuration, runtime evidence, and evidence availability for any retained case.
- Distinguish:
  - positively established behavior;
  - plausible but unproven effect;
  - unresolved behavior.

### R6 — Promote only discriminating cases
- Promote a case only when it materially adds evidence beyond existing cases.
- Keep ordinary controls when they are needed to avoid overfitting to pathological examples.
- Prefer a small evidence-rich case set over a large case count.
- Stop a case family when further screening no longer changes the credible alternatives.

### R7 — Synthesize for the main workstream
Produce concise handoffs answering:
- what current UpgradePilot behavior is supported by reality;
- what should be narrowed or reconsidered;
- what remains unresolved;
- which additional investigation, if any, has material information value;
- whether a durable Product Simulation artifact/scenario should be created.

### R8 — Branch closure / merge readiness
Before proposing merge:
- reconcile this branch with current `main`;
- ensure Product Simulation artifacts remain non-controlling discovery evidence;
- verify no accidental product/spec/plan/main-memory mutation;
- summarize retained findings and unresolved items;
- merge only after the work reaches a coherent stopping point and Ali authorizes integration.

## 3. Progressive record

### 2026-09-22 — workstream isolation

Ali explicitly chose to run Product Simulation research in parallel with the ongoing main work and requested isolation to avoid disrupting or conflicting with `main`.

Created branch:

`research/product-simulation-rebase-2026-09-22`

The workstream's scope was corrected from a Phase-B-centric view to a whole-current-product view. Phase A records and the substantial product progress after the older Product Simulation cases must be included before new real-case selection.

Initial governance orientation confirms:
- Product Simulation is discovery evidence, not the live project-stage owner.
- Existing cases must not be restarted merely for case count.
- New cases need a material uncertainty/evidence gap and honest claim limits.
- Working memory is the appropriate dated operational record for this parallel branch.

No product source, tests, stable specifications, accepted plans, root `MEMORY.md`, or main workstream working memory were modified in this setup slice.

## 4. Current slice status

**Slice: Product Simulation current-state rebase**

- **A — IN PROGRESS:** branch/governance/boundaries established; broader whole-product rebase direction established. Detailed current-product reconstruction remains next.
- **B — PENDING:** perform the actual product-evolution and existing-simulation coverage audit.
- **C — ACTIVE:** this record will be updated at meaningful research progression points.
- **D — PENDING:** review what the rebase actually shows and check ownership/understanding.
- **E — PENDING:** select the first evidence-driven real-world research family after coverage gaps are established.

## 5. Immediate next move

Start with **R1 + R2 together**:

1. reconstruct the material current product responsibilities from recent Phase A onward;
2. inventory what the existing Product Simulation corpus already covers;
3. produce the first coverage-gap map.

Do not begin broad new-case collection until that map tells us which real-world questions are actually missing.
