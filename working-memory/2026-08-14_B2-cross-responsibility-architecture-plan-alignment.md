# B2 Cross-Responsibility Architecture — Plan Alignment Record

**Date:** 2026-08-14  
**Type:** Dated planning/continuation alignment evidence  
**Live-state authority:** `../MEMORY.md` only

## Why this record exists

The target-artifact-environment learning/transfer review exposed a concrete architecture issue before further feature expansion:

```text
src/upgradepilot/ci/workflow_commands.py
and
src/upgradepilot/target/artifact_environment.py
```

independently interpret overlapping GitHub Actions workflow structure, while the two owning responsibilities have different proof semantics.

The same review exposed an important proof-strength distinction now captured by the canonical Product Decision Model specification:

```text
workflow definition declares command/path X
!= command/path X executed
!= command/path X succeeded
```

The project therefore needed a planning correction before additional target-environment capability or orchestration growth.

## Planning reconciliation performed

### 1. Selected B2 foundation plan revised

Updated:

- `plans/B2_IMPACT_APPLICABILITY_INVESTIGATION_FOUNDATION_PLAN.md`

The plan now:

- points to `docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md` as the canonical decision-semantics owner;
- retains the August 6 reconciliation and AUDIT-003 as historical rationale/review evidence;
- adds S011 as an explicit optional-environment/CI contrast;
- adds the static-definition versus runtime-execution proof guard;
- changes the work sequence so a concrete second-mechanism/source-consumer overlap triggers a **mandatory architecture reconciliation gate before further local target-environment expansion**;
- separates architecture decision, later source refactor, second-mechanism completion, and B2 synthesis handoff;
- updates proof obligations and stop line accordingly.

Implementation commit:

```text
9fb5a6a6df2fbec1b4dc052945261ca315c43d5f
```

### 2. New bounded architecture-reconciliation plan created

Created:

- `plans/B2_CROSS_RESPONSIBILITY_ARCHITECTURE_RECONCILIATION_PLAN.md`

The plan owns the inspection/design checkpoint for:

```text
GitHub Actions exact source acquisition
→ normalized/static workflow structure
→ CI-specific interpretation
→ Target-specific interpretation

static definition evidence
vs runtime run/job/step evidence

shared installation/configuration observation
vs CI exercise conclusion
vs Target environment conclusion

multiple-job structural preservation
vs consumer interpretation support

Python-support + artifact-serviceability
→ heterogeneous impact/orchestration pressure
```

It requires:

- current architecture/data-flow map;
- duplication inventory;
- proof-strength map;
- architecture alternatives/comparison;
- selected ownership/dependency direction;
- decisions on workflow structure, installation recognition, multiple jobs, and heterogeneous orchestration;
- future-pressure classification;
- ADR disposition;
- bounded implementation/refactor handoff if source changes are justified.

It explicitly does **not** pre-authorize a source refactor or new ADR.

Creation commit:

```text
758e46e9fa9dc37acf356ec3ab348302b6c92147
```

### 3. Historical source-reconciliation plan disambiguated

The older:

- `plans/B2_SOURCE_CODE_STRUCTURE_RECONCILIATION_PLAN.md`

already completed its different responsibility on 2026-08-04: transition from the former flat/transition-era source topology to responsibility-based subpackages and true shared primitives.

Its final acceptance remains:

- `working-memory/2026-08-04_B2-source-structure-reconciliation-final-acceptance.md`

Rather than rewriting the historical plan, the repository now marks it unambiguously as **COMPLETED / HISTORICAL PRECEDENT** in:

- the revised B2 foundation plan; and
- `plans/README.md`.

The same navigation states that it must not be reactivated as the answer to the newer CI/Target/workflow/orchestration question.

Plan-navigation commit:

```text
155d69031ab585ab3b3a14a064a3be79618cf603
```

## Route/parent-plan disposition

No substantive change was required to:

- `plans/UPGRADEPILOT_90_DAY_PLAN.md`;
- `plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md`.

Both already contain the controlling principles needed here:

```text
small implementation increment
!= small architecture horizon
```

and:

```text
real contrasting responsibilities
→ identify demonstrated sameness
→ keep real differences separate
```

The correction therefore belongs at the selected responsibility and subordinate architecture-checkpoint level rather than the route/gate level.

## Source/runtime impact

This alignment changes plans/navigation/live continuation only.

It does **not** modify:

- `src/upgradepilot/`;
- active product tests;
- current target-artifact-environment behavior;
- current CI dependency-exercise behavior;
- artifact-serviceability evaluation behavior.

No product-runtime verification is inferred or required from these documentation/planning changes.

## Next handoff

The next work is **inspection/design, not refactoring**.

Start the new plan at its baseline/source-map phase:

```text
canonical specifications + ADR-0007 + mature-system horizon
+
current GitHub / CI / Target / Impact / investigation source and tests
↓
current architecture/data-flow map
↓
actual duplication + proof-strength inventory
↓
credible architecture options
```

Do not add another target-artifact-environment capability until the architecture reconciliation determines the durable ownership/dependency direction.
