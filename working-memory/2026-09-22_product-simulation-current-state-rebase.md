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


## 6. R1 + R2 first-pass current-product / simulation coverage rebase

### Product evolution reconstructed

The important post-corpus product evolution is not one Phase-B-only thread. The material sequence now includes:

1. **Parser-backed static workflow-command analysis and shell context**
   - shared parser-neutral command occurrences;
   - shell-family/effective-shell interpretation;
   - comments/quoted payload/control-flow separation;
   - static occurrence identity and source relationship.

2. **Cycle-3 Phase A/B runtime strengthening**
   - explicit separation of static command existence from execution/success;
   - positive whole-step/position relationships;
   - occurrence-level eligibility for exact correlated GitHub step success;
   - conditional/short-circuit/compound/ambiguous shapes remain weaker or unresolved.

3. **Evidence-to-action baseline repairs**
   - F3: abstention synthesis preserves material branch-stopping uncertainty more honestly;
   - F9: public GitHub acquisition is anonymous by default with explicit authenticated opt-in;
   - F11: audit lifecycle coordination corrected, but this is governance/coordination rather than a target-case simulation responsibility.

4. **Action-relative producer/composition work**
   - F4: exact CI-consuming `job_key` now composes into Target job selection instead of Target guessing among jobs;
   - F5: exact target wheel-tag evidence remains a separate stronger runtime witness; broad runner/Python labels are insufficient;
   - F6: exact successful install/sync command correlation is not automatically exact post-install dependency state.

5. **Current runtime dependency-state semantic work**
   - pip/uv package-manager semantics are now proposition-relevant;
   - flags/config/environment may change whether a command installs, where it installs, or which dependency/version is selected;
   - later mutation is a separate temporal/state issue;
   - generic job-log/package-state acquisition has not been assumed necessary.

### Existing Product Simulation coverage versus today's responsibilities

| Current responsibility | Existing Product Simulation evidence | Coverage classification | Rebase conclusion |
| --- | --- | --- | --- |
| Exact proposal identity / dependency-source relevance | S001–S012 consistently preserve frozen proposal identity and exact source relationships | **Broad historical support, but older implementation shape** | Useful foundation; no immediate new case family solely for identity |
| Behavior-path / targeted-check discrimination | S006, S007, S010 and Sept-11 investigate-vs-block report | **Strong design-pressure coverage** | Reuse before searching new cases |
| Artifact availability / environment specificity | S008 + Target Environment handoff | **Strong mechanism evidence, partial current producer coverage** | Still useful; exact current target-witness production is not solved by these cases |
| Optional environment formation / CI coverage | S011 | **Strong conceptual coverage** | Directly supports current Target/environment reasoning but does not test exact F4 job-key composition |
| Persisted/historical target state | S012 | **Strong bounded coverage** | Keep as mature-scope guard; do not import into every current slice |
| Overall investigate vs targeted-check vs block distinction | Sept-11 report using S003/S006/Cactus/Buildtest evidence | **Good design-level evidence** | Current F3 implementation should first be replayed/transferred against existing evidence before seeking a new action case |
| Parser-backed shell command truth: comments, quoted payloads, shell/control-flow structure | No direct retained Product Simulation case found; searches for current command-analysis/runtime terms returned no Product Simulation hits | **Not materially covered** | Fresh real-world pressure is justified |
| Occurrence-level runtime strengthening: whole-step success vs exact internal command execution | No direct Product Simulation case found | **Not materially covered** | Fresh real-world pressure is justified; keep distinct from parser correctness |
| Exact CI-consuming job → Target job composition in multi-job workflows | S011/S008 establish why environment/job specificity matters, but not the current exact `job_key` handoff | **Partial / predecessor-shape coverage** | Fresh real multi-job cases are justified |
| Exact target supported-wheel-tag witness | S008 establishes artifact-serviceability need; Aug handoff explicitly leaves exact tags unresolved; F5 later found S008 has no retained exact tag witness | **Mechanism covered, evidence-source gap remains** | Search only for real targets that actually emit target-owned compatible-tag evidence; do not infer tags from labels |
| Public GitHub authentication boundary | No Product Simulation case directly covers stale ambient token/.netrc behavior; F9 has direct observed environment evidence + controlled executable tests | **Simulation gap, but separate evidence already adequate for current bounded contract** | Low priority for new target cases unless contradictory evidence appears |
| Exact post-install dependency/version state | No older Product Simulation case directly provides this current proposition; F6 main-workstream research found Aruba installer logs and MontePy explicit package-state output | **Old corpus gap; fresh real evidence already emerging outside Product Simulation** | High-priority family to absorb/formalize in this research branch |
| Ambient pip/uv semantic modifiers | No older Product Simulation coverage found for `PIP_CONSTRAINT`, `UV_*`, etc. | **Not materially covered** | High-priority real-case family; recent Salt/Sigstore/ordinary-control research is directly relevant |
| Evidence/log retention for runtime package-state proof | Older cases contain availability limits, but current exact package-state/log-retention proposition was exposed later by F6 | **Partial** | Treat as a defeater/subcase of runtime-state evidence rather than an independent case-count goal |
| Audit lifecycle reconciliation (F11) | Not a target technical case responsibility | **Out of Product Simulation case scope** | Exclude from new scenario selection |

### First gap families after rebase

The current evidence supports four materially distinct fresh real-world research families rather than a generic request for more scenarios:

**G1 — Workflow command semantics and occurrence-level runtime truth**
- Real GitHub Actions steps containing installs/syncs inside conditionals, short-circuit chains, compound commands, quotes/comments, shell-family variation, or ordinary linear controls.
- Question: when does exact step success actually justify strengthening the exact parsed dependency-consuming occurrence?

**G2 — Multi-job dependency consumption → exact target environment**
- Real Dependabot PRs where multiple jobs differ in runner/Python/install path and one or several jobs actually consume the changed dependency source.
- Question: does current F4 composition preserve the right environments and avoid plausible-but-wrong job substitution?

**G3 — Runtime dependency-state proof and package-manager ambient semantics**
- Real pip/uv CI with ordinary controls, material ambient modifiers/config, installer-result evidence, explicit package-state witnesses, and later-state mutation/retention pressure.
- Question: what evidence really establishes that the proposed version is present in the relevant environment?
- Preliminary evidence already found in the current research conversation (Salt, MontePy, Sigstore, Aruba) should be treated as candidate evidence for this family, not yet as an automatically admitted numbered scenario.

**G4 — Exact target wheel-tag witness feasibility**
- Real public targets that explicitly emit `packaging.tags.sys_tags()`, `pip debug`, or equivalent exact compatible-tag evidence in the relevant target-owned CI environment.
- Question: is there a realistic normal public evidence source for the existing exact wheel-compatibility contract?

### Priority judgment

Initial priority for research value:

```text
G1 + G3
→ highest immediate value because current product semantics are actively being designed/built around these proof boundaries

G2
→ next, because F4 is implemented but currently proved mainly by controlled tests and predecessor simulation pressure

G4
→ valuable but evidence-source availability is uncertain; search boundedly and stop if no realistic target-owned witness appears
```

The Sept-11 maintainer-action evidence should be **replayed against the newer F3 synthesis implementation before admitting a new action scenario**.

F9 and F11 should not consume Product Simulation case effort merely because they are recent changes.

### Search result supporting the gap classification

Repository-wide searches restricted to Product Simulation found no direct retained Product Simulation material for the current implementation concepts/terms:

- `whole_step_relation`
- `runtime strengthening`
- `PIP_CONSTRAINT`
- `pip freeze`
- `GITHUB_TOKEN`
- `consuming_job_key`
- `selected_target_job_not_found`
- `supported_runtime_correlated`
- conditional-command / short-circuit terminology

This is supporting evidence only; absence of exact vocabulary is not by itself proof of conceptual non-coverage. The case/synthesis content above was also inspected to determine whether predecessor concepts materially cover the responsibility.

## 7. Updated slice status

**Slice: Product Simulation current-state rebase**

- **A — DONE:** governance, branch boundaries, whole-product scope and relevant current product evolution reconstructed.
- **B — IN PROGRESS:** first R1/R2 coverage audit completed; next action is to validate/prioritize the fresh case families and begin the highest-value real-world screening.
- **C — ACTIVE:** first coverage-gap map preserved here.
- **D — PENDING:** review the gap map and evidence boundaries with Ali after the first family screening gives concrete examples.
- **E — PENDING:** select/promote only the first case family that yields discriminating real evidence.

## 8. Immediate continuation

Begin with **G1 and G3 as a coordinated screening pass**, because they touch the same real install/sync command path but answer different propositions:

```text
G1
shell/control-flow structure
→ did this exact internal command earn runtime strengthening?

G3
package-manager semantics + resulting state
→ if it did execute successfully, what dependency-state proposition did that command actually establish?
```

Keep the two conclusions separate even when one real workflow supplies evidence for both.

In parallel, retain **G2** as the next dedicated multi-job search family and **G4** as a bounded witness-feasibility search, not a mandatory scenario target.
