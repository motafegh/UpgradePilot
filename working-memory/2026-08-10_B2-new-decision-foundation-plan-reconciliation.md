# B2 New Decision-Foundation Plan Reconciliation

**Date:** 2026-08-10  
**Status:** Comparison complete — promotion subsequently applied; comparison body retained as historical pre-promotion reasoning  
**Purpose:** Compare the new clean-slate B2 A–C implementation/evaluation plan against the older Transparent Decision plan, accepted A–C reconciliation, AUDIT-003 amendments, B2/Charter boundaries, specifications, security rules, and current implementation so no useful requirement is lost and no stale responsibility is silently retained.  
**Live-state owner:** `../MEMORY.md` only.

> **Promotion result — 2026-08-10:** After three final bounded corrections (coverage-qualified candidate non-applicability, failed-investigation retry discipline, and conditional candidate-refinement implementation), the narrow Charter/B2/route/specification/Security/current-source recheck remained **PASS**. [`../plans/B2_IMPACT_APPLICABILITY_INVESTIGATION_FOUNDATION_PLAN.md`](../plans/B2_IMPACT_APPLICABILITY_INVESTIGATION_FOUNDATION_PLAN.md) was approved in commit `d3bf15e62cee8b20188b032f87c8a5c4556245e4`; [`../plans/B2_TRANSPARENT_DECISION_METHOD_PLAN.md`](../plans/B2_TRANSPARENT_DECISION_METHOD_PLAN.md) was superseded **in place** as historical/non-controlling material in commit `64f273655c43c5a1ec44aa69ae68e96de92f0062`; and `../MEMORY.md` selected the new plan in commit `036552a871f926410d0fbfe880fe677d9b64a784`. The pre-promotion language below is retained only as the comparison history and does not own current continuation.

## 1. Files compared

### New candidate plan

[`../plans/B2_IMPACT_APPLICABILITY_INVESTIGATION_FOUNDATION_PLAN.md`](../plans/B2_IMPACT_APPLICABILITY_INVESTIGATION_FOUNDATION_PLAN.md)

Final comparison baseline content commit:

```text
2c25f08f5056dc27c2af345dd04eea76c1a87edd
```

### Older selected plan

[`../plans/B2_TRANSPARENT_DECISION_METHOD_PLAN.md`](../plans/B2_TRANSPARENT_DECISION_METHOD_PLAN.md)

Current old-plan blob during comparison:

```text
a5d6cbc53d9e17f057c443b191e7b83f93980de1
```

### Governing/reconciliation sources

- [`../PROJECT_CHARTER.md`](../PROJECT_CHARTER.md)
- [`../AGENTS.md`](../AGENTS.md)
- [`../plans/UPGRADEPILOT_90_DAY_PLAN.md`](../plans/UPGRADEPILOT_90_DAY_PLAN.md)
- [`../plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md`](../plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md)
- [`../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md`](../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md)
- [`../docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md`](../docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md)
- [`../SECURITY.md`](../SECURITY.md)
- [`2026-08-06_UPGRADEPILOT-product-decision-model-reconciliation.md`](2026-08-06_UPGRADEPILOT-product-decision-model-reconciliation.md)
- [`../audits/2026-08-10_AUDIT-003_post-conversation-c-product-decision-model.md`](../audits/2026-08-10_AUDIT-003_post-conversation-c-product-decision-model.md)
- current `src/upgradepilot/investigation.py` / completed Target-Python relevance behavior as the implementation anchor.

## 2. Executive verdict

**PASS.**

The new plan is not merely a rewritten copy of the old Transparent Decision plan. It identifies a cleaner bounded responsibility that the old plan had mixed together with later final-action semantics:

```text
NEW PLAN
A — impact-candidate foundation
↓
B — candidate-specific applicability/evidence/composition
↓
C — discriminating-target / investigation-selection / feedback / investigation stopping
↓
explicit pre-D handoff
```

versus the older mixed shape:

```text
OLD PLAN
validated evidence
→ interpretation
→ overall sufficiency/stopping
→ maintainer action/abstention
→ presentation
```

The new plan therefore represents a justified **responsibility split**, not unnecessary duplicate planning.

The old plan still contains useful historical/future-D material, but it should not remain the controlling implementation plan for the next source work once the new plan is explicitly promoted.

No Charter, B2 parent-plan, route, specification, security, or current-source contradiction was found.

One retention gap was found during comparison—the old plan's explicit canonical dependency-input boundary and representation-neutral downstream semantics. That gap was corrected in the new plan before this record was finalized.

## 3. Why a new file is justified

Repository guidance normally prefers reusing an existing owner rather than creating parallel artifacts. In this case the reconciliation demonstrated that the older plan had become a **mixed responsibility**:

```text
A/B/C reasoning foundation
+
D overall sufficiency/action semantics
```

A–C are now sufficiently defined for implementation feedback, while D is deliberately unopened.

Trying to make one file simultaneously control:

- the immediate pre-D A–C implementation slice; and
- undefined future D final-action semantics

would recreate the exact conceptual coupling the reconciliation was designed to remove.

The new plan therefore owns a narrower, currently implementable responsibility. If promoted, there must still be only one controlling plan for that responsibility.

The old file should later become historical source material or be replaced by a future D-specific plan only after D is concretely required.

## 4. Old-plan requirement disposition matrix

### 4.1 Purpose: evidence to maintainer action

**Old:** directly turns validated evidence into bounded maintainer action/abstention.

**Disposition:** **split, not lost.**

- A–C reasoning needed before action → new plan.
- overall sufficiency/action projection → explicitly deferred to D.

This is a correction to responsibility order, not deletion of the Charter outcome family.

### 4.2 Owning product question and five Charter outcomes

**Old:** asks which maintainer action is justified and lists five Charter outcomes.

**Disposition:** **Charter relationship retained; final question deferred.**

The new plan repeats the Charter outcome family but explicitly states that it is building the internal reasoning foundation rather than deciding the final action prematurely.

### 4.3 B2 responsibility horizon / trusted canonical transition

**Old:** consumes one trusted canonical exact-version Python dependency transition and warns that representation provenance does not establish direct/transitive role, usage, CI consumption, compatibility, or safety.

**Disposition:** **retained explicitly after comparison correction.**

New plan §4.1 now preserves:

```text
trusted canonical transition
+ exact proposal/revision identity
+ source provenance
```

while rejecting representation → semantic meaning shortcuts.

It also keeps unsupported/malformed/incomplete/ambiguous/multiple/conflicting dependency-change problem states outside trusted A–C input.

### 4.4 S004 control-case role

**Old:** uses `googlefonts/glyphsLib#1145`, pytest `9.0.2 → 9.0.3` as a successful action/control case.

**Disposition:** **not copied as the first implementation anchor because its main role is D/final-action validation.**

Useful lessons retained independently:

- no fixture-specific answer;
- canonical transition source representation must not change downstream semantics;
- one known case is not product scope;
- controlled contrasts precede broad claims.

The new pre-D plan instead uses the already behavior-proven Target-Python/S001 mechanism because it exercises A–C with minimum new technical breadth.

S004 remains available as later D/action-level control evidence.

### 4.5 Old conceptual separation: acquisition → dependency interpretation → evidence interpretation → sufficiency → decision → presentation

**Disposition:** **superseded by a more precise responsibility decomposition.**

Retained upstream owners:

- acquisition;
- exact dependency identity;
- evidence authority/provenance.

Newly explicit:

- A impact candidate;
- B proposition/applicability reasoning;
- C investigation-selection/stopping;
- D later overall sufficiency/action.

Presentation remains a later output responsibility rather than being silently implemented inside A–C.

### 4.6 Step 1 old control-case evidence walkthrough

**Disposition:** **retained in stronger form.**

New Step 1 freezes the actual post-reconciliation source/test baseline and requires inspection of current orchestration/contracts rather than designing from prose alone.

The new controlled-transfer set also preserves concrete-case reasoning.

### 4.7 Step 2 old decision input/output contract

**Old:** output already includes action class, sufficiency/readiness, reasons, targeted checks, uncertainty.

**Disposition:** **split.**

New pre-D output preserves candidate/proposition/applicability/investigation/traceability state.

Final action and overall sufficiency fields are intentionally not accepted yet.

This prevents the implementation from answering Conversation D under another name.

### 4.8 Step 3 old outcome meanings and transition boundaries

**Disposition:** **deferred to D, not discarded.**

The meanings of normal review / targeted checks / investigate-block / defer / abstain still matter to the final B2 product and should be reconsidered with real A–C implementation evidence.

### 4.9 Step 4 old evidence sufficiency and stopping

**Disposition:** **split into C and D.**

New plan owns:

```text
investigation stopping
```

Later D owns:

```text
overall evidence sufficiency for a maintainer-facing result
```

This preserves the accepted boundary:

```text
no further justified investigation
!= overall evidence sufficient
```

### 4.10 Step 5 old upstream semantic boundary

**Disposition:** **substantially completed by the intervening Target-Python responsibility and reused as implementation foundation.**

The project already proved:

- exact crossed-release interval;
- exact immutable upstream source binding;
- bounded local semantic extraction;
- exact-source reconstruction/grounding;
- deterministic validation;
- target-Python relevance.

The new plan does not rerun that method-selection exercise merely because the old plan mentioned it.

Generality/model-authority guards remain inherited from accepted specifications/ADR/reconciliation.

### 4.11 Step 6 old design contrasts

**Disposition:** **retained and expanded structurally.**

New plan uses:

- S001 as primary implementation anchor;
- controlled missing/conflict/non-dominated variants;
- Kedro/Pluggy semantic-heavy transfer;
- pip-audit multi-hop transfer;
- C01 artifact/codegen transfer;
- C203 historical-environment transfer.

These cases challenge different topologies without forcing all mechanisms into the first implementation.

### 4.12 Step 7 old Ali approval

**Disposition:** **retained through candidate-plan promotion and ownership checkpoints.**

The new plan is explicitly non-controlling until reviewed/promoted, and it includes an Ali explanation/prediction/modification checkpoint before claiming ownership.

### 4.13 Step 8 old implementation shape

**Disposition:** **replaced by the bounded A–C vertical implementation path.**

The old evidence-sufficiency + decision-evaluation modules are not preselected because D has not been defined.

The new plan also prohibits premature generic `planner`, `graph`, `rules`, or `engine` layers.

### 4.14 Step 9 old controlled behavior proof

**Disposition:** **retained and materially strengthened.**

New proof includes:

- candidate component authority;
- canonical representation neutrality;
- upstream problem-state exclusion;
- four-state proposition/path behavior;
- coverage separation;
- C activation and discriminating targets;
- execution/evidence-validity separation;
- no-further-investigation;
- non-dominated alternatives;
- lineage;
- no hidden D action.

### 4.15 Step 10 old live read-only proof

**Disposition:** **retained with corrected claim scope.**

The new plan still requires a safe integrated public proof, but the proof demonstrates one mechanism-specific A–C slice rather than a final maintainer recommendation.

### 4.16 Old acceptance criteria

**Disposition:** **split according to responsibility.**

Retained now:

- non-hardcoding;
- representation neutrality;
- traceability;
- missing/conflicting state preservation;
- safe read-only behavior;
- controlled contrasts;
- ownership practice;
- no unapproved infrastructure/model authority.

Deferred to D/later B2 completion:

- accepted final outcome meanings;
- final overall sufficiency;
- one public command reaching final recommendation/abstention.

### 4.17 Old stop line

**Disposition:** **replaced with an earlier pre-D stop line.**

New plan stops when one real A–C foundation slice is behavior-validated and has produced enough implementation evidence to expose the next concrete D dependency or a bounded A/B/C correction.

This is intentionally not B2 gate completion.

## 5. AUDIT-003 amendment coverage

### F1 — candidate formulation does not smuggle truth

**Covered:** new §6.1 and Step 2.

### F2 — evidence/path/discovery completeness are distinct

**Covered:** new §6.3, Step 10, acceptance criteria.

### F3 — C includes genuine conflict

**Covered:** new §7.1 and controlled conflict variants.

### F4 — useful check vs execution vs maintainer recommendation

**Covered with the reviewed three-way refinement:** new §7.3 and Step 6.

### F5 — non-dominated alternatives

**Covered:** new §7.4 and tests.

### F6 — policy-relative cost/value

**Covered:** non-dominated alternatives plus explicit D boundary; no numeric utility or fake preference.

### F7 — minimum four-state composition

**Covered:** new §6.4 and Step 4, including mixed unresolved/conflicted alternatives.

### F8 — candidate-refinement lineage

**Covered:** new §7.6 and Step 7.

### F9 — old plan stale

**Resolved structurally by this candidate plan; authority change still pending.**

### F10 — keep B2 thin

**Covered:** new §8 explicit non-goals and Target-Python anchor.

### F11 — pre-D implementation is A–C slice, not final recommendation

**Covered throughout purpose, scope, stop line, and acceptance criteria.**

### F12 — no Charter change

**Preserved.**

### F13/F15 — live-state and authority-owner clarity

Already corrected in the main reconciliation record before this plan work. The new plan itself is position-neutral and points live status to `MEMORY.md`.

### F14 — keep MEMORY lean

Already handled in the prior post-audit memory consolidation; this comparison does not duplicate full A–C theory into live memory.

## 6. Governing-artifact conflict check

### Project Charter

**PASS.**

- public Python Dependabot boundary preserved;
- final five outcome classes preserved as future projection;
- no objective-safety claim;
- no automatic mutation;
- evidence/uncertainty discipline strengthened rather than weakened.

### B2 Public PR Vertical Slice Plan

**PASS.**

The parent plan requires eventual recommendation/abstention but permits detailed sequence/proof to live in bounded B2 plans.

The new file is explicitly a prerequisite foundation inside B2 and does not claim that its completion closes B2.

### 90-day route

**PASS.**

The new plan stays inside B2 and does not pull B3/B4/B5/X1 infrastructure into the current slice.

Broader dependency/path/context capabilities remain later expansion unless a concrete B2 need activates a thin portion.

### Core pipeline/trust specification

**PASS.**

Raw/trusted distinctions, evidence-state preservation, identity/provenance, model-authority limits, and explicit degraded/unresolved behavior remain compatible.

### Minimum Useful Generality specification

**PASS.**

The plan bounds the supported candidate family rather than S001 identity, requires controlled variation, rejects known-answer hardcoding, and does not represent one mechanism slice as universal impact support.

### Security

**PASS.**

The first executable C investigation is intentionally an already-supported public read-only acquisition of exact-head target declaration evidence.

Artifact/codegen/dynamic cases remain reasoning/transfer cases and do not authorize arbitrary target code execution or dependency installation.

### Current source organization/implementation

**PASS.**

The plan starts by inspecting current source/tests and prefers extending proven target/upstream/application boundaries rather than assuming new modules.

The Target-Python slice is a real implementation anchor, not a hypothetical rewrite.

## 7. Candidate-plan internal audit

### Found issue: canonical input boundary was initially too implicit

The first candidate draft relied on the existing dependency foundation but did not explicitly preserve the old plan's strong rule:

```text
trusted canonical dependency transition
!= source representation semantics
```

**Correction applied before final comparison:** new §4.1 plus controlled tests/acceptance criteria now make this explicit.

### No remaining blocker found

After that correction, no missing old-plan requirement was found that belongs inside the pre-D A–C responsibility and is absent from the new plan.

Material old-plan content not copied is intentionally classified as:

- already completed upstream foundation; or
- later D/final-action responsibility; or
- broader route responsibility outside this slice.

## 8. Recommended authority transition

The comparison supports the following later authority change, but this record does not perform it automatically:

```text
CURRENT
MEMORY selects B2_TRANSPARENT_DECISION_METHOD_PLAN.md
while implementation is paused
```

Recommended after explicit promotion decision:

```text
MEMORY selects
B2_IMPACT_APPLICABILITY_INVESTIGATION_FOUNDATION_PLAN.md
as the next bounded B2 responsibility
```

Then the old Transparent Decision plan should no longer remain a competing active implementation owner.

Preferred disposition after promotion:

- preserve its history in Git;
- archive/supersede the current mixed pre-reconciliation plan rather than silently delete it;
- later create or define D-specific sufficiency/action planning from current evidence when implementation actually exposes that need, using useful old material only as historical input.

Do not simply rename the old plan into a D plan without revalidating its final-action assumptions against post-A–C implementation evidence.

## 9. Files actually needed for the next step

The comparison supports a minimal artifact set:

1. **candidate bounded plan**  
   `plans/B2_IMPACT_APPLICABILITY_INVESTIGATION_FOUNDATION_PLAN.md`

2. **this reconciliation/comparison record**  
   `working-memory/2026-08-10_B2-new-decision-foundation-plan-reconciliation.md`

3. **existing `MEMORY.md`**  
   update only for the live promotion/continuation decision; do not create another tracker/handoff file.

No additional specification, ADR, roadmap, checklist, schema document, or child plan is justified before source inspection in Step 1 exposes a concrete need.

## 10. Final comparison verdict

**Candidate plan: PASS — ready for explicit promotion decision.**

The new plan:

- incorporates the accepted A–C domain model and post-audit guards;
- preserves all old-plan material that still belongs to the immediate implementation responsibility;
- explicitly classifies useful old final-action material as later D input rather than deleting it;
- keeps B2 thin;
- uses the completed Target-Python behavior as the first real implementation anchor;
- preserves canonical input/provenance boundaries;
- strengthens controlled proof and learning obligations;
- avoids prematurely selecting runtime schemas, graph/planner machinery, numeric optimization, autonomous execution, or final D semantics;
- does not conflict with the Charter, B2 parent plan, route, specifications, security rules, or current implementation.

The remaining task is **authority transition**, not more plan invention: explicitly decide whether to promote the new plan as the selected next B2 responsibility and then archive/supersede the old mixed plan without losing its historical/future-D value.
