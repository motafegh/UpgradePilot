# B2/X1 EvidenceGapPlanner R2 — Model-Visible Context

**Date:** 2026-08-30  
**Status:** ACTIVE R2 WORKING MEMORY  
**Plan:** `../plans/B2_X1_POST_RESEARCH_EVIDENCE_GAP_PLANNER_LBD_IMPLEMENTATION_PLAN.md`  
**Responsibility:** decide and justify the exact trusted context projected into the `EvidenceGapPlanner` model request, without serializing whole product state or inventing model authority.

## 1. Entry state

R0/R1 are complete. Current working vocabulary:

```text
EvidenceGapPlanner
→ EvidenceGapDecision
→ EvidenceGapDecisionKind
```

Preferred decision semantics currently are:

```text
ACTION_SELECTED
QUESTION_SETTLED
KNOWN_INVESTIGATION_NOT_ADMITTED
NO_JUSTIFIED_INVESTIGATION_IDENTIFIED
```

Historical experiment request fields remain evidence only; they are not retention authority.

## 2. R2 decision rule

For every candidate model-visible field ask:

```text
what exact reasoning does this enable?
is that reasoning part of EvidenceGapPlanner responsibility?
is this fact already trusted before the model?
is the same meaning already represented more appropriately elsewhere?
does exposing it add useful context or only duplicate trace/authority metadata?
what remains deterministic even if the model can see the value?
```

Do not equate:

```text
important product state
=
model-visible state
```

The planner request is an explicit projection.

## 3. Dependency transition — first R2 decision

Trusted source owner: `src/upgradepilot/dependency/change.py::DependencyVersionChange`.

That product type preserves both:

```text
package
→ source spelling / presentation form

normalized_package
→ canonical cross-source identity used for comparison/agreement
```

### Decision

Use the canonical identity in planner context:

```text
dependency_transition:
    normalized_package
    old_version
    proposed_version
```

Do **not** include `package` merely to preserve source spelling.

### Why

- `EvidenceGapPlanner` reasons about one trusted dependency transition, not presentation spelling.
- UpgradePilot already uses normalized package identity across downstream dependency/environment reasoning.
- One canonical identity avoids giving cosmetic spelling variation semantic weight.
- The model does not create or normalize this identity; deterministic product code remains authoritative.
- This is not primarily a performance or "less parsing" optimization. It is an identity-consistency/context-quality decision.

### Explicit non-fields from `DependencyVersionChange`

Do not automatically project:

```text
package
source_evidence
limitations
```

Those remain with their existing evidence/product owners unless a later planner reasoning requirement specifically earns them.

## 4. Historical case-identity behavior

The historical Phase-3B request renderer exposed:

```text
repository
pull_number
revision
```

while deliberately excluding evaluator/development/protected `case_key` and oracle metadata.

This historical choice proves only that the prototype exposed those fields. It does not prove all three are required for `EvidenceGapPlanner` reasoning.

Important precedent:

```text
system-important trace/evaluation identity
!=
model-visible reasoning context
```

## 5. Current open R2 question — target/case identity

Decide separately for:

```text
repository
pull_number
immutable revision
```

Do not keep them as one indivisible "case identity" bundle merely because `InvestigationSnapshot` currently does.

Questions to answer:

1. Does `repository` provide useful semantic context to the model, or does it mainly expose target identity that deterministic code already owns?
2. Does `pull_number` change any EvidenceGapPlanner reasoning, or is it trace/UI identity only?
3. Does the exact revision need to be model-visible, or only deterministically bound to available actions/evidence/execution?
4. Could repository/revision exposure encourage unsupported model prior knowledge about a named project instead of reasoning from supplied trusted state?
5. If a field is omitted from the model request, where does it remain available for logging, replay, action binding, evidence acquisition, and admission?

## 6. Current likely direction — not yet frozen

The strongest current hypothesis is:

```text
system/evaluator/executor state:
    repository
    pull_number
    revision

model-visible state:
    omit pull_number
    critically evaluate repository
    critically evaluate revision
```

Reason: the planner selects an evidence-resolution responsibility, while trusted code already owns exact locators and later admission/execution. E4.3 already showed that model-emitted locator/target metadata is unnecessary; R2 must now decide whether merely *seeing* exact target identity adds reasoning value.

Do not freeze this hypothesis until the current reasoning point is completed.

## 7. Next R2 sequence

After target/case identity, continue field-by-field through:

1. bounded planning question;
2. typed propositions — key/state/evidence coverage/detail/evidence owner/origin;
3. trusted attempted-action history and outcome semantics;
4. remaining budget;
5. model-visible capability descriptor vs deterministic-only action metadata;
6. explicit exclusions and final candidate request projection.

Preserve material decisions here as they are earned. Do not implement the final experiment contract until R2 is complete enough to make the context boundary unambiguous.
