# UpgradePilot Specification-System Governance Refactor Plan

**Status:** Bounded documentation/governance refactor plan  
**Responsibility:** Improve the clarity, proportionality, authority resolution, and maintenance cost of UpgradePilot's active control/specification system without changing product behavior or live project position

## Purpose

Refactor the active project-control Markdown system so that each rule or fact has one clear normal owner, mandatory reading is smaller, historical evidence does not occupy active normative surfaces unnecessarily, and plans/ADRs/specifications remain distinct artifacts.

This work changes documentation structure and governance expression only. It does not change product behavior, route state, selected implementation work, source code, tests, environment configuration, or the completed `product-simulation/` subsystem.

## Non-goals

This refactor must not:

- change UpgradePilot's product mission, supported user, supported decision, or frozen product boundary;
- change the live route, selected product increment, or exact product continuation;
- modify `product-simulation/` or its local controls/specifications;
- create a new branch or pull request;
- rewrite dated working-memory, learning, proposal, chronicle, or historical simulation records merely for stylistic consistency;
- create another master-governance, authority-map, tracker, or control layer;
- change source code, product tests, experiment code, or runtime dependencies.

## Design principles

1. **Strict precedence is short.** Safety/platform constraints, Ali's explicit instruction, and nearest applicable `AGENTS.md` form the strict instruction hierarchy. After that, resolve conflicts by the artifact that owns the responsibility rather than by one universal document ranking.
2. **One rule, one normal owner.** Secondary files may summarize a rule only when the summary is needed at the point of use; they should link to the owner rather than re-specify it.
3. **Bootstrap files stay cheap.** `AGENTS.md` should contain repository routing, mandatory safeguards, reading decisions, and change discipline—not full copies of operating, environment, architecture, learning, or specification policy.
4. **Live memory is a continuation index.** `MEMORY.md` owns present position, latest material verification, blockers, exact continuation, and concise learning state. Detailed evidence, architecture narratives, test logs, and incident histories remain with their stronger owners.
5. **Environment reference is durable baseline, not evidence archive.** `ENVIRONMENT.md` keeps reusable topology, paths, stable hardware/service facts, safe recurring commands, re-check rules, and recurring caveats; dated measurements and model-inventory detail stay in evidence records.
6. **Specifications state required behavior.** Active technical specifications should not carry large historical contracts that are no longer activation candidates merely for traceability.
7. **ADRs state decisions.** ADRs should preserve context, decision, alternatives, rationale, consequences, reversal/reassessment, and the minimum proof boundary needed to understand the decision; detailed test matrices and implementation plans belong elsewhere.
8. **Plans coordinate execution.** Plans may state the consequences of accepted decisions, but should reference rather than re-own stable specifications and ADR details.
9. **Ceremony is proportional.** Audit and evidence templates are defaults, not mandatory bureaucracy for every small concern.
10. **Public orientation remains public.** `README.md` should orient readers and link to control owners without duplicating the internal control system.

## Modification set

### 1. Root `AGENTS.md`

Refactor toward:

- repository purpose;
- strict instruction order;
- responsibility-based truth ownership;
- concise artifact-placement rules;
- required-reading decision table;
- critical repository safety/change constraints;
- concise validation/claim discipline;
- links to `OPERATING_GUIDE.md`, `ENVIRONMENT.md`, specifications, ADRs, and plans instead of duplicated policy.

Remove or substantially compress duplicated route narrative, environment workflow detail, learning procedure, minimum-generality detail, architecture-admission procedure, and document-update repetition when those already have canonical owners.

### 2. `OPERATING_GUIDE.md`

Preserve the operating and learning model. Replace its broad linear post-AGENTS precedence with responsibility-owner resolution. Avoid duplicating repository routing already owned by `AGENTS.md`.

### 3. `MEMORY.md`

Compress to the minimum continuation state:

- live route and selected bounded plan;
- latest material verified evidence and commit references;
- material blocker/caveat only when it affects continuation;
- exact next product action and stop line;
- concise current learning depth;
- links to architecture/evidence records instead of duplicated source trees, test logs, incident narratives, experiment score tables, and path maps.

No live product position may change as part of this refactor.

### 4. `ENVIRONMENT.md`

Keep reusable environment truth and recurring safe controls. Remove detailed historical inventory, point-in-time GPU measurements, experiment-result narrative, and long evidence reproductions when dated evidence already owns them. Preserve links to those records.

### 5. `PROJECT_CHARTER.md`

Remove project-charter ownership of career-program exposure quotas or A1/A2/A3 obligations. Keep project-local technology admission and learning/ownership requirements. Career/program commitments may influence future reviews but do not become product-charter requirements automatically.

### 6. Route plan

Keep stage order, gates, required outcomes, route principles, and stable product flow. Compress discovery-history and lower-level implementation detail that can be linked to evidence or bounded plans.

### 7. Specification meta-control

Preserve `docs/specifications/README.md` as the specification boundary owner while clarifying that cross-artifact disagreements are resolved by responsibility ownership and explicit supersession rather than a generic total ordering.

### 8. Core specification historical separation

Refactor `UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md` to contain active stable project invariants and validation/failure principles only.

Move the retained historical M2-specific contract to a clearly historical non-controlling archive artifact with an immutable-context explanation. Active specification links may reference it for traceability without making it part of current normative reading.

### 9. Naming standard classification

Keep the useful naming rules but classify them as an accepted project-wide engineering/naming standard rather than pretending they are system-behavior requirements. Avoid creating a new governance directory solely for classification purity.

### 10. ADR proportionality

Slim the largest ADRs, especially ADR-0004, ADR-0005, and ADR-0006:

- preserve the durable decision and essential boundary;
- preserve alternatives, rationale, consequences, reversibility, and reassessment triggers;
- link detailed execution/test obligations to the controlling plan/evidence where appropriate;
- remove implementation-path inventories and exhaustive proof matrices when they are not part of the durable decision itself.

Do not alter accepted decisions.

### 11. Plan proportionality

Update `plans/README.md` so plans explicitly reference accepted specifications/ADRs rather than re-specifying them.

Trim the selected target-Python parent plan and Step 7 bounded integration plan where accepted ADRs now own method details. Preserve their execution sequence, proof obligations, modification boundaries, and stop lines.

### 12. Directory-level controls

Leave strong `working-memory/`, `learning/`, `proposals/`, and `chronicle/` controls substantively intact unless a cross-reference must change.

### 13. Audit proportionality

Refactor `audits/README.md` so small audits may use a compact structure, while numbered finding IDs and the full formal structure are required only when cross-reference, multi-finding follow-up, or consequential review justifies them.

### 14. Root `README.md`

Reduce duplication of internal route, source-layout, learning, and ownership controls. Keep concise product orientation, supported boundary, architecture/source entry points, and links to the canonical owners.

### Explicit exclusion

No changes to `product-simulation/`, including:

- `product-simulation/AGENTS.md`;
- `SIMULATION_GOVERNANCE_AND_PLAN.md`;
- `RUNTIME_ARTIFACT_SPECIFICATION.md`;
- `TRANSPARENT_BASELINE_SPECIFICATION.md`;
- scenario bundles or historical simulation evidence.

## Validation

After edits:

1. verify every changed file still names the correct owner and scope;
2. verify `MEMORY.md` remains the sole live-state owner;
3. verify no non-memory file accidentally gains live-state language;
4. verify the strict instruction hierarchy is consistent between `AGENTS.md` and `OPERATING_GUIDE.md`;
5. verify specification/ADR/plan responsibilities are non-overlapping enough to resolve conflicts by owner;
6. verify all links affected by the historical M2 extraction and naming-standard wording remain valid;
7. verify no `product-simulation/` file changed;
8. verify no product source/test/runtime dependency changed;
9. compare the final changed-file set against this plan and record deviations explicitly.

## Working-memory closure

Create one dated `working-memory/` record after validation containing:

- audit trigger and inspected/refactored control surfaces;
- major problems found;
- exact structural changes made;
- reasoning for each responsibility move;
- intentionally unchanged areas;
- risks and tradeoffs introduced by compression;
- validation performed;
- resulting commit range/SHA references;
- future reassessment triggers.

The working-memory record is historical evidence only. It must not become a second live-state owner.
