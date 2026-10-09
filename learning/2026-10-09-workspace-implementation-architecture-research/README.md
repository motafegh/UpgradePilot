# Learning the Workspace implementation research

**Educational snapshot:** 2026-10-09, research commit **`7ae80a07d5fb9180ddb30145ea389bebe6553c5f`**. Product source at that horizon matches main baseline `08243e5b3e455ad26ae1cd142763f4d147269bc6`. These notes explain experiments and their reasoning, not an adopted production Workspace.

The central question is how to preserve evolving, exact-target investigation knowledge while native owners retain their facts and consumers receive honest projections. Four different responsibilities deserve separate study:

| Read in order | What you should be able to reason about afterward |
| --- | --- |
| [1. State, identity and material retention](01_workspace_state_identity_and_material_retention.md) | Build a stable successor, distinguish identity from equal content, and explain why a correct round trip can still lose required evidence. |
| [2. Persistence, interruption and recovery](02_checkpoint_persistence_interruption_and_recovery.md) | Locate the publication boundary, interpret ambiguous acknowledgement, compare the tested stores and explain recovery loss/backup limits. |
| [3. Revision-bound Investigator interaction](03_revision_bound_investigator_interaction.md) | Trace view → request → admission → attempt → observation → native evaluation, and distinguish original basis, current basis, authority and semantic truth. |
| [4. Native integration, migration and proof](04_native_integration_migration_and_engineering_proof.md) | Trace the real-data subset and controlled orchestration separately, explain consumer parity and the cold-native-codec gap, and evaluate the strength of a test oracle. |

Each note contains a source walkthrough, failure/correction lessons, calibrated depth, proof limits and a fast return route. Optional transfer questions support later study; writing or reading the notes is not evidence of mastery. The notes can be studied independently after the first reading, with this page supplying their common horizon and authority map.

## Evidence and authority

At this snapshot, main's distinct Workspace composition direction is selected, while [ADR-0012](https://github.com/motafegh/UpgradePilot/blob/7ae80a07d5fb9180ddb30145ea389bebe6553c5f/docs/architecture/ADR-0012-canonical-investigation-workspace-and-recovery-boundary.md) and its Core recovery insertion remain Proposed. The accepted [Core contract](https://github.com/motafegh/UpgradePilot/blob/7ae80a07d5fb9180ddb30145ea389bebe6553c5f/docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md), [Product Decision Model](https://github.com/motafegh/UpgradePilot/blob/7ae80a07d5fb9180ddb30145ea389bebe6553c5f/docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md), and [Maintainer Action Synthesis specification](https://github.com/motafegh/UpgradePilot/blob/7ae80a07d5fb9180ddb30145ea389bebe6553c5f/docs/specifications/UPGRADEPILOT_MAINTAINER_ACTION_SYNTHESIS_SPECIFICATION.md) retain their responsibilities. These notes do not promote proposals or authorize implementation.

The [research plan](https://github.com/motafegh/UpgradePilot/blob/7ae80a07d5fb9180ddb30145ea389bebe6553c5f/plans/INVESTIGATION_WORKSPACE_IMPLEMENTATION_ARCHITECTURE_RESEARCH_PLAN.md) supplies the questions and bounded recommendations. The [cycle record](https://github.com/motafegh/UpgradePilot/blob/7ae80a07d5fb9180ddb30145ea389bebe6553c5f/working-memory/2026-10-08_workspace-implementation-architecture-research_lbd-cycle.md) supplies corrections and reasoning history. Source/tests and dated results supply implementation/proof. Live continuation belongs to repository `MEMORY.md`, not this frozen package.

## Study and later source use

First read the mechanism and trace tables, then open the named functions and one independent test. Use the questions to predict a changed case before inspecting the answer in source. When returning later, use each note's fast relearning route rather than reread everything.

All repository web links in this package pin the same commit. For a local source view, run this from the repository root, substituting the required repository-relative path:

```sh
git show 7ae80a07d5fb9180ddb30145ea389bebe6553c5f:experiments/workspace_revision_representation.py
```

Later audio/quiz transforms should use a note plus its 1–3 selected source/test/evidence anchors at this horizon. Do not feed mutable main files into a transform and label it this snapshot. No derivative files, separate learning tracker or new research protocol are needed.

**Recorded verification:** the final migration receipt reports 121 scoped experiment tests and 115 focused product tests passing. Those results are historical evidence for the research code; authoring this package does not rerun them or establish product adoption, semantic adequacy or power-loss durability.

`UP-SKILL:upgradepilot-learning-artifact`

