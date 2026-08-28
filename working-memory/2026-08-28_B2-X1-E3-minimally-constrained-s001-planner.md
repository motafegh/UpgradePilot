# B2/X1 E3 — Minimally Constrained Real-S001 Planner Probe

**Date:** 2026-08-28  
**Status:** E3 COMPLETE  
**Parent exploration:** `working-memory/2026-08-28_B2-X1-evidence-first-llm-risk-and-design-exploration.md`

## Purpose

Observe what the adopted local model naturally proposes from the real S001 typed pre-investigation state before imposing the previously designed strict planner controls.

The experiment intentionally omitted:

```text
closed action catalog
pre-bound action arguments
JSON Schema
deterministic admission
hard-constraint list
evaluator oracle / expected answer
raw upstream changelog text
```

No model proposal was executed.

Experiment source:

`experiments/b2_x1_e3_minimal_s001_planner_probe.py`

## Execution note

The first attempted launch used file-path execution:

```text
python experiments/b2_x1_e3_minimal_s001_planner_probe.py
```

and failed before experiment execution because the source imports another `experiments.*` module while the repository root was not the import root.

The correct package-style execution is:

```text
python -m experiments.b2_x1_e3_minimal_s001_planner_probe
```

A repository import sanity check then passed before the live run.

This was an execution-context/import issue, not model or E3 semantic evidence.

## Exact live case

```text
repository: pydantic/pydantic
pull_number: 13432
revision: aa2dc024d33f61cdef50bf1973ab5adf0a974f5a
model: gemma-4-e4b-it-ud
temperature: 0
seed: 0
elapsed_seconds: 5.030969338999967
capability_executed: false
```

Planner input contained the bounded planning question plus three typed propositions from the real pre-investigation product state.

### Proposition 1

```text
upstream_python_support_drop_crossed
state: established
evidence_coverage: sufficient
origin: model_derived_semantics_deterministically_grounded
```

### Proposition 2

```text
exact_target_python_declaration_established
state: unresolved
evidence_coverage: insufficient
origin: deterministic_pre_acquisition_state
```

### Proposition 3

```text
declared_python_range_intersects_dropped_line
state: unresolved
evidence_coverage: insufficient
origin: deterministic_derived_state
```

The remaining investigation-step budget was 1.

## Raw model output

```text
**Next Investigation Step:** Acquire evidence for `exact_target_python_declaration_established`.

**Evidence Obtained:** This step would obtain the actual declared Python version range used by the target project.

**Why it Helps:** The planning question asks if the upstream support drop affects the *target project's exact declared Python range*. Currently, we know when the upstream dropped support (`upstream_python_support_drop_crossed` is established), but we do not know what the target project requires (`exact_target_python_declaration_established` is unresolved). Acquiring this evidence is necessary to resolve the final condition (`declared_python_range_intersects_dropped_line`) and answer the planning question.
```

## Deterministic baseline/control

The already-built product selector independently selected:

```text
kind: acquire_exact_target_python_declaration
repository: pydantic/pydantic
revision: aa2dc024d33f61cdef50bf1973ab5adf0a974f5a
path: pyproject.toml
proposition_key: exact_target_python_declaration_established
```

## Finding E3-F1 — minimally constrained reasoning found the correct evidence gap

The model correctly distinguished:

```text
already-established upstream fact
from
actionable unresolved prerequisite
from
dependent unresolved consequence
```

It selected the exact target-declaration proposition rather than the dependent range-intersection proposition.

This is positive evidence for H3/H4 on the simplest real S001 state.

## Finding E3-F2 — heavy planner controls were not necessary for this reasoning step

The model reached the same conceptual next investigation as the deterministic baseline without:

- action allowlisting;
- action IDs;
- JSON Schema;
- deterministic admission;
- explicit hard-constraint prompting;
- raw upstream evidence.

Therefore those controls should not be credited with producing this correct reasoning result.

This does **not** mean they are unnecessary for execution authority, integration reliability, malformed-output handling, or higher-consequence future actions.

## Finding E3-F3 — correct reasoning was not yet exact execution authority

The model proposed acquiring the target declaration, but the free-form answer did not itself bind that proposal to the exact trusted executable locator:

```text
repository: pydantic/pydantic
revision: aa2dc024d33f61cdef50bf1973ab5adf0a974f5a
path: pyproject.toml
```

That is expected because E3 deliberately withheld the action catalog.

The next question is therefore narrower than the previous strict design:

> Is supplying a trusted closed action descriptor enough to convert correct natural planning into an exact action selection, before adding JSON Schema or deterministic admission?

## What E3 does not prove

E3 is one real case and one model execution. It does not establish:

- general planner reliability;
- stability across repeats/models;
- correct STOP behavior;
- correct behavior with multiple truly actionable alternatives;
- that free-form text is safe or convenient for automation;
- that exact action arguments should be model-generated;
- that JSON Schema or deterministic admission are unnecessary for an executable integration.

## Next discriminating step

Proceed to **E4.1 — closed action binding only**.

Keep the same real S001 typed state and model configuration, add the existing trusted `acquire_exact_target_python_declaration` action descriptor, and ask the model to select an action ID or no action.

Do **not** add JSON Schema or deterministic admission in E4.1. The purpose is to isolate what the closed action catalog itself changes.
