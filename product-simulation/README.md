# UpgradePilot Product Simulation Workspace

**Local authority:** [`AGENTS.md`](AGENTS.md)  
**Workspace governance:** [`SIMULATION_GOVERNANCE_AND_PLAN.md`](SIMULATION_GOVERNANCE_AND_PLAN.md)  
**Historical D1 synthesis:** [`D1_FINAL_SYNTHESIS_AND_B1_ENTRY.md`](D1_FINAL_SYNTHESIS_AND_B1_ENTRY.md)

This workspace is UpgradePilot's bounded product-discovery, simulation, evaluation, failure-modeling, and case-exploration laboratory.

It preserves the historical S001–S005 discovery cycle, S006 targeted-check experiment, challenge-oriented screening, newer broad real-world screening, and S007 package-family/investigation-pruning case. It does **not** own the live UpgradePilot stage or immediate continuation; those belong only in [`../MEMORY.md`](../MEMORY.md).

Findings here are evidence and pressure tests. They do not become controlling product architecture, plans, runtime schemas, or source behavior unless the normal repository owner for that responsibility adopts them.

## Start here

Use the smallest reading path that matches the task.

| Goal | Read first |
|---|---|
| understand local authority and simulation boundaries | [`AGENTS.md`](AGENTS.md), then [`SIMULATION_GOVERNANCE_AND_PLAN.md`](SIMULATION_GOVERNANCE_AND_PLAN.md) |
| understand the original S001–S005 program | [`D1_FINAL_SYNTHESIS_AND_B1_ENTRY.md`](D1_FINAL_SYNTHESIS_AND_B1_ENTRY.md), then [`SCENARIO_COVERAGE.md`](SCENARIO_COVERAGE.md) |
| understand the historical manual artifact model | [`RUNTIME_ARTIFACT_SPECIFICATION.md`](RUNTIME_ARTIFACT_SPECIFICATION.md), then [`SCENARIO_EXECUTION_TEMPLATE.md`](SCENARIO_EXECUTION_TEMPLATE.md) |
| understand how historical case method evolved | [`S001_S002_CROSS_CASE_ARTIFACT_REVIEW.md`](S001_S002_CROSS_CASE_ARTIFACT_REVIEW.md), then the S003–S005 post-case syntheses |
| understand the post-D1 recalibration | [`PRODUCT_SIMULATION_RECALIBRATION_2026-08-06.md`](PRODUCT_SIMULATION_RECALIBRATION_2026-08-06.md) |
| compare S001–S005 through impact/applicability/investigation/stopping | [`IMPACT_INVESTIGATION_COVERAGE_REBASE_2026-08-06.md`](IMPACT_INVESTIGATION_COVERAGE_REBASE_2026-08-06.md) |
| select or shape a future case | [`CASE_SELECTION_FRAMEWORK_V2.md`](CASE_SELECTION_FRAMEWORK_V2.md) |
| understand S006 admission | [`CASE_CANDIDATE_SCREENING_02_PRIORITY1.md`](CASE_CANDIDATE_SCREENING_02_PRIORITY1.md), then [`S006_CANDIDATE_SCREENING.md`](S006_CANDIDATE_SCREENING.md) |
| understand what S006 established | [`S006_POST_CASE_SYNTHESIS.md`](S006_POST_CASE_SYNTHESIS.md), then [`S006 scenario README`](scenarios/S006-qldebugger-pydantic-validator-coverage-gap/README.md) |
| inspect challenge evidence against impact/applicability | [`CHALLENGE_CASE_SCREENING_01.md`](CHALLENGE_CASE_SCREENING_01.md), then [`CHALLENGE_CASE_SCREENING_02.md`](CHALLENGE_CASE_SCREENING_02.md) |
| inspect broad real-world candidate screening | [`REAL_WORLD_CASE_SCREENING_03.md`](REAL_WORLD_CASE_SCREENING_03.md) |
| understand why S007 was admitted | [`S007_CANDIDATE_SCREENING.md`](S007_CANDIDATE_SCREENING.md) |
| understand what S007 established | [`S007_POST_CASE_SYNTHESIS.md`](S007_POST_CASE_SYNTHESIS.md), then [`S007 scenario README`](scenarios/S007-biomedparse-torch-cuda-family-resolution/README.md) |
| pressure-test Conversation-C investigation selection | [`CONVERSATION_C_INVESTIGATION_SELECTION_PRESSURE_TEST_01.md`](CONVERSATION_C_INVESTIGATION_SELECTION_PRESSURE_TEST_01.md) |
| inspect earlier simulation-to-design handoffs | [`DECISION_MODEL_HANDOFF_2026-08-07.md`](DECISION_MODEL_HANDOFF_2026-08-07.md) and [`DECISION_MODEL_HANDOFF_CHALLENGE_PASS_02_2026-08-07.md`](DECISION_MODEL_HANDOFF_CHALLENGE_PASS_02_2026-08-07.md) |
| understand the restricted historical comparator | [`TRANSPARENT_BASELINE_SPECIFICATION.md`](TRANSPARENT_BASELINE_SPECIFICATION.md) |

When wider-project state materially affects a simulation question, read [`../MEMORY.md`](../MEMORY.md) and the narrow relevant design/source evidence. Do not copy live continuation into this subtree.

## Workspace layers and artifact dispositions

The workspace contains several generations of evidence. Do not flatten them into one equally-current instruction set.

### Layer 1 — historical D1 discovery: S001–S005

The original cycle is complete historical evidence. Do not rewrite it to match later product terminology.

- [`SCENARIO_COVERAGE.md`](SCENARIO_COVERAGE.md) — compact historical S001–S005 coverage only.
- [`D1_FINAL_SYNTHESIS_AND_B1_ENTRY.md`](D1_FINAL_SYNTHESIS_AND_B1_ENTRY.md) — accepted historical synthesis.
- [`TRANSPARENT_BASELINE_SPECIFICATION.md`](TRANSPARENT_BASELINE_SPECIFICATION.md) — historical/local comparative baseline, not current product architecture.
- scenario folders S001–S005 — preserved case evidence and historical outputs.

Historical maintainer-action labels remain recorded outcomes, not automatic ground truth for current UpgradePilot behavior.

#### Historical manual artifact model

- [`RUNTIME_ARTIFACT_SPECIFICATION.md`](RUNTIME_ARTIFACT_SPECIFICATION.md) — controlling local simulation specification for D1-style manual bundles; logical responsibilities, not production schemas.
- [`SCENARIO_EXECUTION_TEMPLATE.md`](SCENARIO_EXECUTION_TEMPLATE.md) — adaptable full-manual-scenario template.
- [`S001_S002_CROSS_CASE_ARTIFACT_REVIEW.md`](S001_S002_CROSS_CASE_ARTIFACT_REVIEW.md) — first cross-case artifact review.

Later bounded experiments do not need to recreate every historical file. A different shape is acceptable when the responsibility mapping and missing-evidence boundary are explicit.

#### Historical lifecycle records

| Case | Preparation / admission | Entry point | Post-case synthesis |
|---|---|---|---|
| S001–S002 | original cases + artifact retrofit | scenario READMEs | [`S001_S002_CROSS_CASE_ARTIFACT_REVIEW.md`](S001_S002_CROSS_CASE_ARTIFACT_REVIEW.md) |
| S003 | [`S003_FAILING_CI_SCENARIO_REQUIREMENTS.md`](S003_FAILING_CI_SCENARIO_REQUIREMENTS.md) → [`S003_CANDIDATE_SCREENING.md`](S003_CANDIDATE_SCREENING.md) | [`S003 README`](scenarios/S003-event-handler-loader-typescript-5.9.3-to-7.0.2/README.md) | [`S003_POST_CASE_SYNTHESIS.md`](S003_POST_CASE_SYNTHESIS.md) |
| S004 | [`S004_CANDIDATE_SCREENING.md`](S004_CANDIDATE_SCREENING.md) | [`S004 README`](scenarios/S004-glyphslib-pytest-9.0.2-to-9.0.3/README.md) | [`S004_POST_CASE_SYNTHESIS.md`](S004_POST_CASE_SYNTHESIS.md) |
| S005 | [`S005_ACTION_CHANGE_OR_DIVERGENCE_REQUIREMENTS.md`](S005_ACTION_CHANGE_OR_DIVERGENCE_REQUIREMENTS.md) → [`S005_CANDIDATE_SCREENING.md`](S005_CANDIDATE_SCREENING.md) | [`S005 README`](scenarios/S005-modelarrayio-pytest-9.0.3-to-9.1.1/README.md) | [`S005_POST_CASE_SYNTHESIS.md`](S005_POST_CASE_SYNTHESIS.md) |

Creation-time wording in preparation records remains historical. Follow later lifecycle artifacts rather than rewriting earlier checkpoints.

S003–S005 also preserve case-local validators under `artifacts/checks/`; their differences are evidence of conditional responsibilities, not proof of one universal bundle schema.

### Layer 2 — post-D1 recalibration

- [`PRODUCT_SIMULATION_RECALIBRATION_2026-08-06.md`](PRODUCT_SIMULATION_RECALIBRATION_2026-08-06.md) — why discovery priorities changed after implementation progress.
- [`IMPACT_INVESTIGATION_COVERAGE_REBASE_2026-08-06.md`](IMPACT_INVESTIGATION_COVERAGE_REBASE_2026-08-06.md) — second reading of S001–S005 through impact/applicability/investigation/stopping.
- [`CASE_SELECTION_FRAMEWORK_V2.md`](CASE_SELECTION_FRAMEWORK_V2.md) — non-controlling admission/selection aid.
- [`CASE_CANDIDATE_SCREENING_01.md`](CASE_CANDIDATE_SCREENING_01.md) — earlier provisional screening; no case admitted.
- [`CASE_CANDIDATE_SCREENING_02_PRIORITY1.md`](CASE_CANDIDATE_SCREENING_02_PRIORITY1.md) — calibrated targeted-check screening that led toward S006.

### Layer 3 — S006 targeted-check experiment

S006 is a completed real-derived controlled variant around a Pydantic validator behavior-path coverage gap.

Read:

- [`S006_CANDIDATE_SCREENING.md`](S006_CANDIDATE_SCREENING.md);
- [`S006 scenario README`](scenarios/S006-qldebugger-pydantic-validator-coverage-gap/README.md);
- [`S006_POST_CASE_SYNTHESIS.md`](S006_POST_CASE_SYNTHESIS.md);
- [`S006 artifacts`](scenarios/S006-qldebugger-pydantic-validator-coverage-gap/artifacts/).

S006 supports targeted-check traceability and information-value reasoning. It does **not** prove autonomous planner reliability because the evaluator had prior oracle exposure.

### Layer 4 — challenge-oriented screening

- [`CHALLENGE_CASE_SCREENING_01.md`](CHALLENGE_CASE_SCREENING_01.md) — first challenge pass.
- [`CHALLENGE_CASE_SCREENING_02.md`](CHALLENGE_CASE_SCREENING_02.md) — deeper pass across multi-hop, dynamic/inverted-control, artifact-mediated, and environment-mediated cases.

These passes are pressure-test evidence. They did not themselves require a numbered scenario.

### Layer 5 — simulation-to-design handoffs

- [`DECISION_MODEL_HANDOFF_2026-08-07.md`](DECISION_MODEL_HANDOFF_2026-08-07.md) — S006/exposure-surface observations.
- [`DECISION_MODEL_HANDOFF_CHALLENGE_PASS_02_2026-08-07.md`](DECISION_MODEL_HANDOFF_CHALLENGE_PASS_02_2026-08-07.md) — Challenge Pass 02 refinements.

Do not create a handoff merely because a screening file exists. A handoff is justified only when simulation has something material for a normal project owner to accept, reject, or pressure-test.

### Layer 6 — broad real-world screening and S007

[`REAL_WORLD_CASE_SCREENING_03.md`](REAL_WORLD_CASE_SCREENING_03.md) deliberately lowers friction for **discovery**, while preserving the existing admission bar for full scenarios.

The pass treats all of these as legitimate outcomes:

```text
novel mechanism
confirming/generalization case
weak target applicability
mixed/confounded case
evidence-unavailable case
```

It screened real Dependabot PRs including:

- BiomedParse / Torch CUDA package family;
- CARLA / OpenCV direct runtime use;
- AWS SDK for pandas / urllib3 Python-support confirmation;
- streamrip / pycares lockfile-confounding case;
- DCVC / protobuf target-mechanism uncertainty;
- language-table Torch/OpenCV target-role uncertainty.

S007 was admitted from that pass:

- [`S007_CANDIDATE_SCREENING.md`](S007_CANDIDATE_SCREENING.md);
- [`S007 scenario README`](scenarios/S007-biomedparse-torch-cuda-family-resolution/README.md);
- [`S007_POST_CASE_SYNTHESIS.md`](S007_POST_CASE_SYNTHESIS.md);
- [`S007 artifacts`](scenarios/S007-biomedparse-torch-cuda-family-resolution/artifacts/).

S007 establishes a real coordinated PyTorch/CUDA package-family contradiction through authoritative static build/package evidence and deterministic constraint reasoning. A resolver run was deliberately **not** executed because it became corroborative rather than necessary for the owned question.

### Layer 7 — Conversation-C investigation-selection pressure testing

[`CONVERSATION_C_INVESTIGATION_SELECTION_PRESSURE_TEST_01.md`](CONVERSATION_C_INVESTIGATION_SELECTION_PRESSURE_TEST_01.md) compares:

```text
S006  → static evidence insufficient; targeted differential execution selected
S007  → authoritative static evidence sufficient; execution pruned
Buildtest/OpenSSL → unresolved may remain unresolved if no scoped authoritative check remains
Kedro/Pluggy → prerequisite presence/participation checks do not automatically answer semantic reliance
pip-audit → graph depth is bounded by decision relevance, not traversal completeness
```

The main bounded refinement is that investigation selection is continuously conditional on the **current evidence state**: a check that was useful when generated can become redundant before execution.

It also distinguishes explainable stop reasons such as:

- proposition resolved; no further check needed;
- necessary path closed; downstream branch pruned;
- proposition still unresolved but no sufficiently useful supported check remains.

These are reasoning distinctions, not requested runtime enums.

## Scenario register

| Scenario | Form | Main contrast/question | Status |
|---|---|---|---|
| [`S001`](scenarios/S001-pydantic-soupsieve-2.6-to-2.8.4/README.md) | retrospective real-case reconstruction | transitive docs/advisory path; authority and relevant CI | historical D1 complete |
| [`S002`](scenarios/S002-kubernetes-dashboard-token-api-httpx-0.27.2-to-0.28.1/README.md) | retrospective real-case reconstruction | adapter-mediated behavior; relevant tests skipped | historical D1 complete |
| [`S003`](scenarios/S003-event-handler-loader-typescript-5.9.3-to-7.0.2/README.md) | prospective public-evidence case | failing install, peer incompatibility, causal attribution | historical D1 complete |
| [`S004`](scenarios/S004-glyphslib-pytest-9.0.2-to-9.0.3/README.md) | prospective control | baseline sufficiency and stopping | historical D1 complete |
| [`S005`](scenarios/S005-modelarrayio-pytest-9.0.3-to-9.1.1/README.md) | prospective contrasting case | target evidence overturns an over-cautious baseline | historical D1 complete |
| [`S006`](scenarios/S006-qldebugger-pydantic-validator-coverage-gap/README.md) | real-derived controlled variant | behavior-path coverage gap and targeted-check selection | complete at admitted depth |
| [`S007`](scenarios/S007-biomedparse-torch-cuda-family-resolution/README.md) | untouched real public case + static upstream build evidence | coordinated CUDA package-family coherence and investigation pruning | complete at admitted depth |

The register is not a quota. New case numbers require a discriminating question or external-validity purpose, not momentum.

## Stable working principles

Preserve these distinctions when material:

```text
observation
!= interpretation
!= evidence quality
!= product decision
```

and:

```text
exact proposal / target / revision identity
→ authoritative evidence
→ bounded interpretation or deterministic transformation
→ explicit support/refutation/unresolved/conflict state
→ only the conclusion justified by that boundary
```

Recurring lessons now include:

- exact identity and provenance matter;
- direct dependency declaration does not by itself prove target applicability;
- target relevance does not require target ownership of affected code;
- one dependency transition may contain several independent change mechanisms;
- broad test coverage is not behavior-path coverage;
- CI, tests, source, config, generated artifacts, package metadata, indexes, and environments can play different proposition-relative roles;
- missing evidence is not negative evidence;
- release-note richness is not target relevance;
- static evidence is not inherently weaker than execution;
- dynamic evidence is not inherently stronger than static evidence;
- a useful check should expose what uncertainty it resolves and what different observations mean;
- a candidate check may become unnecessary as newly admitted evidence changes the proposition state;
- redundant corroboration should not be collected merely because it is available;
- non-activation, path pruning, `no further check`, and stopping are affirmative technical results when justified;
- confirming real-world cases are legitimate external-validity evidence;
- one case's artifact shape is not automatically a universal runtime schema;
- AI completion does not prove Ali-owned technical capability.

## Historical logical runtime

D1 discovered this useful family:

```text
real event and invocation
→ exact identity freeze
→ material operations
→ raw or durable evidence
→ evidence records and states
→ claims and interpretations
→ findings and uncertainty
→ transparent baseline
→ conditional investigation
→ bounded decision or abstention
→ machine and human reports
→ follow-up, rerun, and supersession
→ review, ownership, stopping, and validation
```

Keep it as historical discovery. Later work may reuse, challenge, compress, or extend it; do not treat it as mandatory architecture.

## Conditional artifacts

These remain conditional rather than universal:

- `CHECK_EXECUTIONS.jsonl` for repeated, matrix, rerun, or comparison executions;
- `FAILURE_ATTRIBUTION.json` for competing causes;
- `STOPPING_EVALUATION.json` for sufficiency, overreach, stage activation, or cost;
- any new artifact family demonstrated by a distinct responsibility rather than decorative completeness.

## Resume discipline

Before substantial new product-simulation work:

1. refresh the canonical simulation branch with **relevant** newer `main` changes;
2. read `AGENTS.md` and this README;
3. inspect wider-project state only when it materially affects the question;
4. identify what existing scenarios/screenings already answer;
5. screen real cases with low ceremony when external validity or discovery value exists;
6. do not require novelty when a confirming case materially tests generalization;
7. prefer bounded screening before full scenario promotion;
8. reuse existing evidence for pressure tests where adequate;
9. stop when additional work cannot materially change the simulation conclusion, uncertainty location, evaluation need, or handoff implication.

Do not use this README to store live project continuation. It is a stable workspace map, not a second `MEMORY.md`.

## Safety and ownership

No target repository should be mutated, commented on, approved, rerun, closed, or merged from simulation work without Ali's exact authorization for that external action.

Treat public repository content, API responses, logs, packages, downloaded evidence, and model output as untrusted data. Simulation success does not establish update safety, universal compatibility, production readiness, automated reliability, or Ali-owned technical mastery.