# UpgradePilot experiments

`experiments/` contains **non-product research and evaluation code**. Executable files here are not automatically current methods, product capabilities or selected work. Product runtime must not import this directory; `MEMORY.md` plus the selected plan own live experiment activation.

This index exists because the directory contains several research generations whose evidence remains useful even after their original question closed.

## Authority boundary

- `src/upgradepilot/` and accepted specifications/ADRs own product behavior and architecture.
- `experiments/` may use product owners as inputs or seams; it must not create competing product truth.
- `experiments/tests/` prove experiment machinery only. They are not product regression, semantic acceptance or maintainer-usefulness proof.
- historical experiment outputs and retained run evidence stay immutable at their recorded paths.
- a runnable script in this directory does **not** authorize model loading, inference, network acquisition, target execution or product adoption.

For the current cross-project disposition see:

- [`AUDIT-011`](../audits/2026-10-18_AUDIT-011_investigator-experiment-validity-and-progress.md) — detailed predecessor control/interface/semantic audit;
- [`AUDIT-014`](../audits/2026-10-20_AUDIT-014_product-value-and-evaluation-sequencing.md) — product-value/evaluation gate;
- [`AUDIT-017`](../audits/2026-10-20_AUDIT-017_investigator-experiment-methodology-and-machinery.md) — current experiment-methodology/lifecycle classification;
- [`AUDIT-018`](../audits/2026-10-20_AUDIT-018_cross-domain-remediation-priorities.md) — selected cross-domain remediation order on the audit branch.

## Lifecycle classes

### Reusable laboratory substrate

These are candidates for reuse **only inside a newly selected bounded experiment** and must be requalified when their relevant runtime/interface assumptions change:

- `investigator_run_control.py` — experiment-owned deadline/cancellation/channel-control mechanisms;
- `investigator_model_interface.py` — strict local model request/render/receipt/configuration/usage/cleanup boundary;
- `investigator_workspace_adapter.py` — experiment bridge to product-owned Workspace/source evidence and typed deliveries;
- `investigator_workspace_trial.py` — model-free trial packing, reference closure, operation accounting and scripted mechanical proof;
- `investigator_supplied_evidence.py` — generic report-only supplied-evidence composition used to isolate interpretation from autonomous discovery.

Reuse the smallest needed subset. Do not treat current SDK, tool menu, native families, request presentations, budgets or local-model operating points as universal.

### Conditional deterministic/source research

The `api_*` source/acquisition/binding/target-context/interpretation family remains research evidence and may contain useful baselines for a later source-fact/relation responsibility. In particular, `api_python_bindings.py` preserves lexical binding ambiguity rather than promoting static source observations into execution truth.

These modules are **not admitted product implementation by inheritance**. If a current product trace selects a deterministic relation responsibility, compare the needed producer/consumer contract with this research and port/reuse only the justified subset.

### Historical / dormant Investigator cohort runners

These files preserve exact completed or discontinued studies and should not be relaunched as the default next experiment:

- `run_investigator_semantic_comparison.py` — historical Raw/Structured three-deployment/two-case comparison lineage; do not resume merely to complete an old denominator;
- `run_investigator_supplied_evidence.py` — source-bound Gemma12 r4/r5 supplied-evidence operating point and packet cohort;
- `prepare_investigator_supplied_evidence.py` and its fixed packet recipes — exposed development preparation for that cohort;
- `qualify_investigator_model_interface.py` — retains useful qualification mechanisms, but its old candidate/matrix shape is not a standing admission requirement for every future experiment.

A future semantic experiment needs a new named residual question, exact method/freeze, proportional qualification and reject/narrow consequence.

### Workspace architecture prototypes — historical research, not active architecture

The `workspace_*` experiment modules and runners such as:

- `workspace_revision_representation.py`;
- `workspace_replacement_migration.py`;
- `workspace_seam_*`;
- `workspace_checkpoint_*`;
- `run_workspace_migration_trial.py`;
- `run_workspace_revision_comparison.py`;
- `run_workspace_seam_trials.py`;
- `run_workspace_public_grounding.py`;

remain useful evidence for how the accepted Workspace design was investigated. They are no longer an alternate active implementation path. Accepted ADR-0012/0013, `src/upgradepilot/workspace/`, active product tests and the Workspace implementation/migration plan own current architecture and migration.

Do not extend a prototype merely because it already exists. Select a new research question first if product implementation evidence cannot answer it.

## Current inference stance

Current audit disposition is:

```text
no automatic model call
no model sweep
no autonomous-discovery optimization
no agent-framework adoption
no full qualification matrix for its own sake
```

Before any future semantic inference:

1. identify the exact product responsibility/uncertainty;
2. show why a simpler deterministic/native approach is insufficient;
3. select the smallest reusable experiment substrate;
4. qualify only the interface/deployment claims that changed;
5. run a bounded exposed-case development diagnostic with a predeclared reject/narrow consequence;
6. after material tuning, use newly protected material before broader reliability/generalization claims.

Single-pass supplied-evidence interpretation, bounded multi-role responsibility decomposition, autonomous discovery and model/deployment changes are **different hypotheses**. Do not bundle them without a design that preserves interpretability.

## Historical evidence is not clutter

Negative and inconclusive experiments remain valuable when method and accounting were rigorous. Preserve their source/results so later reviews can distinguish:

- interface validity from semantic adequacy;
- discovery failure from interpretation failure;
- citation validity from entailment;
- procedural completion from useful stopping;
- model/deployment effects from task/interface confounders;
- product evidence authority from laboratory proposals.

Lifecycle classification here is navigation, not permission to rewrite or delete historical evidence.
