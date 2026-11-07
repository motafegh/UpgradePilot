# Caller-signature learning — module-by-module engineering-source map

**Reference horizon:** main `a0204b3a680e4cfe082951f158fee6342bb57c77` (November 7, 2026).

## Required procedure before each lesson and substantive chunk

1. **Name the full engineering responsibility** (not only A3/B1/C2). Check current `main` and `MEMORY.md` for material changes to its owners; this map is a verified historical navigation snapshot, not automatically current.
2. **Actually retrieve and read** the relevant Working Memory cycle's design/failed-run/correction sequence, the governing plan/design/ADR, the selected current source, and at least one related retained result/test. A link alone does not mean the file was read. For a multi-part module, read the relevant subpart's distinct history (e.g., B1 correspondence versus admission, D4 checkpoint versus paging).
3. Teach the **real-world reason the program behaves this way**, the engineering pressure, measured failures/alternatives, why the chosen design was selected, the implementation mechanism and the test's real purpose, ending with proof/non-proof and the learner's required depth. Explicitly separate observed intentions/measurements from inferred explanations. Do not relabel a synthetic test failure as a real incident or two source calls as two runtime executions.
4. Keep retrospective Working Memory as **historical evidence**, not an override of current source, accepted contracts, or root `MEMORY.md`. Preserve negative/superseded tests. Distinguish real public retained source, controlled authored HTTP, installed tests, live provider observations and independent human usefulness.
5. **Selective retrieval, not exhaustive reading:** the first linked Working Memory item, first design and most relevant code/proof pair normally suffice for an initial chunk. Read additional references to answer the actual engineering why/how or resolve a discrepancy. Preserve one fair check; never auto-mark independent mastery.

## Verified per-module entries

### A1 — Evidence claims: imported origin, correspondence, argument reception and runtime uncertainty

**Engineering journey / Working Memory:** [2026-10-26_capability-limits-for-explanation-milestone_discussion-cycle.md](../working-memory/2026-10-26_capability-limits-for-explanation-milestone_discussion-cycle.md) · [2026-10-28_second-real-caller-signature-case_qualification-and-evaluation-cycle.md](../working-memory/2026-10-28_second-real-caller-signature-case_qualification-and-evaluation-cycle.md).

**Governing plans, designs and decisions:** [DESIGN.md](../working-memory/evidence/2026-10-28-reusable-caller-signature-design/DESIGN.md) · [DETERMINISTIC_API_CALL_AND_SIGNATURE_EVIDENCE_PLAN.md](../plans/DETERMINISTIC_API_CALL_AND_SIGNATURE_EVIDENCE_PLAN.md).

**Source code, tests and retained evidence:** [REVIEW.md](../working-memory/evidence/2026-10-28-caller-signature-second-real-case/REVIEW.md) · [README.md](../working-memory/evidence/2026-11-04-caller-signature-connected-retained-qualification/README.md).

**What to explain:** Retained Digimon/Requests and glyphsLib/pytest source outcomes illustrate why a static imported origin or a bound signature is not proof of selected installed callable, execution or upgrade safety.

### A2 — Product kernel ownership: experiment transfer and retained equivalence

**Engineering journey / Working Memory:** [2026-11-01_caller-signature-native-representation-proof_cycle.md](../working-memory/2026-11-01_caller-signature-native-representation-proof_cycle.md) · [2026-11-01_caller-signature-integration-independent-audit_cycle.md](../working-memory/2026-11-01_caller-signature-integration-independent-audit_cycle.md).

**Governing plans, designs and decisions:** [CALLER_SIGNATURE_NATIVE_ADOPTION_AND_QUALIFICATION_PLAN.md](../plans/CALLER_SIGNATURE_NATIVE_ADOPTION_AND_QUALIFICATION_PLAN.md) · [CALLER_SIGNATURE_NATIVE_ADOPTION_IMPLEMENTATION_PLAN.md](../plans/CALLER_SIGNATURE_NATIVE_ADOPTION_IMPLEMENTATION_PLAN.md).

**Source code, tests and retained evidence:** [analysis.py](../src/upgradepilot/caller_signature/analysis.py) · [correspondence.py](../src/upgradepilot/caller_signature/correspondence.py) · [README.md](../working-memory/evidence/2026-11-01-native-caller-signature-kernel-transfer/README.md).

**What to explain:** Trace the recorded implementation-order correction, one-owner design, historical adapters and retained/installed proof; distinguish code relocation from qualified product behavior.

### A3 — Imported-origin analysis: scopes, branch alternatives, binding traces

**Engineering journey / Working Memory:** [2026-10-04_2102_ordered-and-scoped-bindings_lbd-cycle.md](../working-memory/2026-10-04_2102_ordered-and-scoped-bindings_lbd-cycle.md) · [2026-10-28_reusable-caller-signature-evidence_build-cycle.md](../working-memory/2026-10-28_reusable-caller-signature-evidence_build-cycle.md).

**Governing plans, designs and decisions:** [DESIGN.md](../working-memory/evidence/2026-10-28-reusable-caller-signature-design/DESIGN.md).

**Source code, tests and retained evidence:** [bindings.py](../src/upgradepilot/caller_signature/bindings.py) · [test_python_source_bindings.py](../tests/test_python_source_bindings.py) · [retained-results.json](../working-memory/evidence/2026-11-01-native-caller-signature-record-proof/retained-results.json).

**What to explain:** From real Python import/reassignment patterns to uncertain branch joins and source traces; explain that source occurrences do not establish which branches ran.

### A4 — Source facts and local argument checker: AST, declarations, premises

**Engineering journey / Working Memory:** [2026-10-28_reusable-caller-signature-evidence_design-cycle.md](../working-memory/2026-10-28_reusable-caller-signature-evidence_design-cycle.md) · [2026-10-28_reusable-caller-signature-evidence_build-cycle.md](../working-memory/2026-10-28_reusable-caller-signature-evidence_build-cycle.md).

**Governing plans, designs and decisions:** [DESIGN.md](../working-memory/evidence/2026-10-28-reusable-caller-signature-design/DESIGN.md).

**Source code, tests and retained evidence:** [validation.json](../working-memory/evidence/2026-10-28-reusable-caller-signature-design/validation.json) · [analysis.py](../src/upgradepilot/caller_signature/analysis.py) · [test_call_signature_analysis.py](../tests/test_call_signature_analysis.py).

**What to explain:** Study the actual Python inspect.Signature.bind discrepancy that challenged a standard-library shortcut. Explain known rejection, bound-with-premises and undetermined arguments (including forwarded **kwargs).

### B1 — Target-to-dependency correspondence and bounded whole-file work admission

**Engineering journey / Working Memory:** [2026-10-29_source-correspondence-and-ordinary-retention_build-cycle.md](../working-memory/2026-10-29_source-correspondence-and-ordinary-retention_build-cycle.md) · [2026-10-30_protocol-factory-source-correspondence_build-cycle.md](../working-memory/2026-10-30_protocol-factory-source-correspondence_build-cycle.md) · [2026-11-01_analysis-capacity-and-work-admission_cycle.md](../working-memory/2026-11-01_analysis-capacity-and-work-admission_cycle.md).

**Governing plans, designs and decisions:** [CALLER_SIGNATURE_ANALYSIS_WORK_ADMISSION_PLAN.md](../plans/CALLER_SIGNATURE_ANALYSIS_WORK_ADMISSION_PLAN.md) · [DESIGN.md](../working-memory/evidence/2026-10-28-pr-driven-caller-signature-design/DESIGN.md).

**Source code, tests and retained evidence:** [correspondence.py](../src/upgradepilot/caller_signature/correspondence.py) · [test_source_correspondence.py](../tests/test_source_correspondence.py) · [REVIEW.md](../working-memory/evidence/2026-11-01-analysis-capacity-and-work-admission/REVIEW.md) · [larger-profile-measurement.json](../working-memory/evidence/2026-11-01-analysis-capacity-and-work-admission/larger-profile-measurement.json).

**What to explain:** Separate path/premise construction from admission. Read original LifeLog refusal, full 5,443-fact measurement, 8,192-fact diagnostic JSON refusal and the resulting whole-file/paired admission policy.

### C1 — Bounded worker: exact input, subprocess states, results and coverage

**Engineering journey / Working Memory:** [2026-11-02_native-caller-signature-analysis-worker_cycle.md](../working-memory/2026-11-02_native-caller-signature-analysis-worker_cycle.md).

**Governing plans, designs and decisions:** [CALLER_SIGNATURE_NATIVE_ADOPTION_IMPLEMENTATION_PLAN.md](../plans/CALLER_SIGNATURE_NATIVE_ADOPTION_IMPLEMENTATION_PLAN.md) · [CALLER_SIGNATURE_ANALYSIS_WORK_ADMISSION_PLAN.md](../plans/CALLER_SIGNATURE_ANALYSIS_WORK_ADMISSION_PLAN.md).

**Source code, tests and retained evidence:** [worker.py](../src/upgradepilot/caller_signature/worker.py) · [test_caller_signature_worker.py](../tests/test_caller_signature_worker.py) · [README.md](../working-memory/evidence/2026-11-02-native-caller-signature-analysis-worker/README.md).

**What to explain:** Read the actual initial worker-transfer faults and timeout/error cases, then the installed/retained proof. A completed LifeLog worker still had 17 unexamined Python units.

### C2 — Historical result reconstruction: shared traces, graph integrity and version guards

**Engineering journey / Working Memory:** [2026-11-01_caller-signature-native-representation-proof_cycle.md](../working-memory/2026-11-01_caller-signature-native-representation-proof_cycle.md) · [2026-11-02_native-caller-signature-analysis-worker_cycle.md](../working-memory/2026-11-02_native-caller-signature-analysis-worker_cycle.md).

**Governing plans, designs and decisions:** [CALLER_SIGNATURE_ANALYSIS_WORK_ADMISSION_PLAN.md](../plans/CALLER_SIGNATURE_ANALYSIS_WORK_ADMISSION_PLAN.md) · [CALLER_SIGNATURE_NATIVE_ADOPTION_IMPLEMENTATION_PLAN.md](../plans/CALLER_SIGNATURE_NATIVE_ADOPTION_IMPLEMENTATION_PLAN.md).

**Source code, tests and retained evidence:** [retained-results.json](../working-memory/evidence/2026-11-01-native-caller-signature-record-proof/retained-results.json) · [evidence.py](../src/upgradepilot/caller_signature/evidence.py) · [native_codec.py](../src/upgradepilot/caller_signature/native_codec.py) · [result_codec.py](../src/upgradepilot/caller_signature/result_codec.py) · [test_caller_signature_native_codec.py](../tests/test_caller_signature_native_codec.py) · [test_caller_signature_worker.py](../tests/test_caller_signature_worker.py).

**New exact case:** [real LifeLog frozen Letterboxd file](https://github.com/VaHerinckx/LifeLog_Project/blob/2a0f4e2b6f8eae3a813edacc6095d78aa34c3197/pipeline/src/sources_processing/letterboxd/letterboxd_processing.py) has two distinct `requests.get` calls (L187 movie search, L212 details) used in a **conceptual** shared-observation demonstration, not a dump of private per-call traces. Move next to [qualified live HTTPX PR20 source/witness records](../working-memory/evidence/2026-11-07-native-proxy-successor/RESULTS.md) for real candidate graph, version, role/premise and cold decode checks. User reported improved but incomplete comprehension.

**What to explain:** Current lesson: start with real retained LifeLog trace repetition, why shared steps reduce representation cost, and then how the reader rejects invalid links without rerunning an analyzer. Label injected corruption tests as tests, not real incidents.

### D1 — Native source evidence: exact text, selection and acquisition provenance

**Engineering journey / Working Memory:** [2026-11-02_caller-signature-native-family-checkpoint_cycle.md](../working-memory/2026-11-02_caller-signature-native-family-checkpoint_cycle.md) · [2026-11-02_native-source-acquisition-owners_cycle.md](../working-memory/2026-11-02_native-source-acquisition-owners_cycle.md).

**Governing plans, designs and decisions:** [CALLER_SIGNATURE_NATIVE_ADOPTION_AND_QUALIFICATION_PLAN.md](../plans/CALLER_SIGNATURE_NATIVE_ADOPTION_AND_QUALIFICATION_PLAN.md) · [ADR-0011-explicit-source-association-bases-and-proposal-boundary.md](../docs/architecture/ADR-0011-explicit-source-association-bases-and-proposal-boundary.md).

**Source code, tests and retained evidence:** [source_evidence.py](../src/upgradepilot/caller_signature/source_evidence.py) · [source_codec.py](../src/upgradepilot/caller_signature/source_codec.py) · [README.md](../working-memory/evidence/2026-11-02-caller-signature-native-families/README.md).

**What to explain:** Contrast observed source bytes with supporting release/selection receipts. Use real historical glyphsLib missing-receipt limits rather than inventing captured provider data.

### D2 — Native comparison evidence: exact source basis, worker status and local findings

**Engineering journey / Working Memory:** [2026-11-02_caller-signature-native-family-checkpoint_cycle.md](../working-memory/2026-11-02_caller-signature-native-family-checkpoint_cycle.md).

**Governing plans, designs and decisions:** [CALLER_SIGNATURE_NATIVE_ADOPTION_IMPLEMENTATION_PLAN.md](../plans/CALLER_SIGNATURE_NATIVE_ADOPTION_IMPLEMENTATION_PLAN.md).

**Source code, tests and retained evidence:** [comparison_codec.py](../src/upgradepilot/caller_signature/comparison_codec.py) · [result_codec.py](../src/upgradepilot/caller_signature/result_codec.py) · [test_caller_signature_workspace.py](../tests/test_caller_signature_workspace.py) · [README.md](../working-memory/evidence/2026-11-02-caller-signature-native-families/README.md).

**What to explain:** Why comparison facts reference the source family rather than duplicating source bytes; failed analysis, unevaluated evidence and completed partial coverage remain distinct.

### D3 — Format/codec version versus semantic producer/method identity

**Engineering journey / Working Memory:** [2026-11-02_caller-signature-native-family-checkpoint_cycle.md](../working-memory/2026-11-02_caller-signature-native-family-checkpoint_cycle.md).

**Governing plans, designs and decisions:** [CALLER_SIGNATURE_NATIVE_ADOPTION_IMPLEMENTATION_PLAN.md](../plans/CALLER_SIGNATURE_NATIVE_ADOPTION_IMPLEMENTATION_PLAN.md) · [ADR-0013-versioned-native-reconstruction-and-workspace-checkpoint-storage.md](../docs/architecture/ADR-0013-versioned-native-reconstruction-and-workspace-checkpoint-storage.md).

**Source code, tests and retained evidence:** [native_representation.py](../src/upgradepilot/workspace/native_representation.py) · [comparison_codec.py](../src/upgradepilot/caller_signature/comparison_codec.py) · [test_workspace_native_reconstruction.py](../tests/test_workspace_native_reconstruction.py).

**What to explain:** Read actual unsupported-version and malformed-source refusal tests. Understanding a record shape does not authorize unsupported producer semantics.

### D4 — Workspace material edges, acknowledged revisions, view reuse and cold recovery

**Engineering journey / Working Memory:** [2026-11-02_caller-signature-native-family-checkpoint_cycle.md](../working-memory/2026-11-02_caller-signature-native-family-checkpoint_cycle.md) · [2026-11-04_caller-signature-connected-retained-qualification_cycle.md](../working-memory/2026-11-04_caller-signature-connected-retained-qualification_cycle.md).

**Governing plans, designs and decisions:** [ADR-0012-canonical-investigation-workspace-and-recovery-boundary.md](../docs/architecture/ADR-0012-canonical-investigation-workspace-and-recovery-boundary.md) · [ADR-0013-versioned-native-reconstruction-and-workspace-checkpoint-storage.md](../docs/architecture/ADR-0013-versioned-native-reconstruction-and-workspace-checkpoint-storage.md).

**Source code, tests and retained evidence:** [checkpoint_store.py](../src/upgradepilot/workspace/checkpoint_store.py) · [consumer_access.py](../src/upgradepilot/workspace/consumer_access.py) · [test_workspace_checkpoint_store.py](../tests/test_workspace_checkpoint_store.py) · [README.md](../working-memory/evidence/2026-11-04-bounded-native-navigation-repair/README.md) · [2026-11-04-bounded-native-navigation-and-view-reuse.md](2026-11-04-bounded-native-navigation-and-view-reuse.md).

**Actual measured cost:** [completed 60-page instrumented task](../working-memory/evidence/2026-11-06-independent-host-timing/RESULTS.md) and [AUDIT-015](../audits/2026-11-06_AUDIT-015_native-page-granularity-payload-and-publication-cost.md). View/basis reuse preserved validity but did not make repeated durable raw paging inexpensive; live paired source/report route used zero raw pages. Page cap is not proven optimal; no selected change.

**What to explain:** Two separate historical slices: checkpoint durability/unknown acknowledgement; six-page native-access refusal at 64 MiB and verified view/basis reuse enabling 60-page retained navigation without changing the guard.

### E1 — Provider acquisition policy: shared request budgets, retry and deadlines

**Engineering journey / Working Memory:** [2026-10-30_staged-source-acquisition-policy_build-cycle.md](../working-memory/2026-10-30_staged-source-acquisition-policy_build-cycle.md) · [2026-11-02_native-acquisition-ledger_cycle.md](../working-memory/2026-11-02_native-acquisition-ledger_cycle.md).

**Governing plans, designs and decisions:** [CALLER_SIGNATURE_NATIVE_ADOPTION_IMPLEMENTATION_PLAN.md](../plans/CALLER_SIGNATURE_NATIVE_ADOPTION_IMPLEMENTATION_PLAN.md) · [DESIGN.md](../working-memory/evidence/2026-10-28-pr-driven-caller-signature-design/DESIGN.md).

**Source code, tests and retained evidence:** [acquisition.py](../src/upgradepilot/caller_signature/acquisition.py) · [test_caller_signature_acquisition.py](../tests/test_caller_signature_acquisition.py) · [README.md](../working-memory/evidence/2026-11-02-native-acquisition-ledger/README.md).

**Observed live transport chain:** [first partial](../working-memory/evidence/2026-11-06-native-normal-product-live-qualification/RESULTS.md) → [TLS diagnosis](../working-memory/evidence/2026-11-06-pypi-transport-diagnosis/RESULTS.md) → [PyPI-only alternate route proof](../working-memory/evidence/2026-11-07-pypi-route-repair/RESULTS.md) → [successor 45 GitHub/63 total requests](../working-memory/evidence/2026-11-07-native-proxy-successor/RESULTS.md); distinguish transport configuration from product request budget or source evidence, with no implicit retry.

**What to explain:** Recover actual source-starvation and stage-budget motivation, physical attempt charges and narrow retry behavior. Distinguish transport success from admitted source evidence.

### E2 — Target source context: exact PR identity, declarations and import candidates

**Engineering journey / Working Memory:** [2026-10-29_pr-source-acquisition-integration_build-cycle.md](../working-memory/2026-10-29_pr-source-acquisition-integration_build-cycle.md) · [2026-11-02_native-source-acquisition-owners_cycle.md](../working-memory/2026-11-02_native-source-acquisition-owners_cycle.md).

**Governing plans, designs and decisions:** [DESIGN.md](../working-memory/evidence/2026-10-28-pr-driven-caller-signature-design/DESIGN.md) · [ADR-0011-explicit-source-association-bases-and-proposal-boundary.md](../docs/architecture/ADR-0011-explicit-source-association-bases-and-proposal-boundary.md).

**Source code, tests and retained evidence:** [source_context.py](../src/upgradepilot/target/source_context.py) · [test_target_source_context.py](../tests/test_target_source_context.py) · [REVIEW.md](../working-memory/evidence/2026-10-29-pr-source-acquisition-integration/REVIEW.md).

**What to explain:** Why exact revision/source tree, dependency declarations and import observations support different claims; preserve missing-file and unknown namespace limits.

### E3 — Old/proposed dependency source: release and module provenance, partial receipts

**Engineering journey / Working Memory:** [2026-10-31_ordinary-source-acquisition-blocker-resolution_cycle.md](../working-memory/2026-10-31_ordinary-source-acquisition-blocker-resolution_cycle.md) · [2026-11-02_native-source-acquisition-owners_cycle.md](../working-memory/2026-11-02_native-source-acquisition-owners_cycle.md).

**Governing plans, designs and decisions:** [CALLER_SIGNATURE_NATIVE_ADOPTION_IMPLEMENTATION_PLAN.md](../plans/CALLER_SIGNATURE_NATIVE_ADOPTION_IMPLEMENTATION_PLAN.md) · [DESIGN.md](../working-memory/evidence/2026-10-28-pr-driven-caller-signature-design/DESIGN.md).

**Source code, tests and retained evidence:** [source_acquisition.py](../src/upgradepilot/caller_signature/source_acquisition.py) · [test_caller_signature_source_acquisition.py](../tests/test_caller_signature_source_acquisition.py) · [README.md](../working-memory/evidence/2026-11-02-native-source-acquisition-owners/README.md).

**Real source acquisition:** initial [target-only partial capture](../working-memory/evidence/2026-11-06-native-normal-product-live-qualification/RESULTS.md) versus [successor exact HTTPX 0.27.2/0.28.1 source and conditional witnesses](../working-memory/evidence/2026-11-07-native-proxy-successor/RESULTS.md). Sampled Starlette/FastAPI versions are not target-installed identity; omitted candidates are not absence.

**What to explain:** Why package-version, repository declaration, tag, commit, module path and exact text are separate evidence steps. Teach failed reads and run-local versus durable facts.

### F1 — Source progress: publish acquired material before analysis, preserve earlier evidence

**Engineering journey / Working Memory:** [2026-11-03_caller-signature-source-progress_cycle.md](../working-memory/2026-11-03_caller-signature-source-progress_cycle.md).

**Governing plans, designs and decisions:** [CALLER_SIGNATURE_NATIVE_ADOPTION_IMPLEMENTATION_PLAN.md](../plans/CALLER_SIGNATURE_NATIVE_ADOPTION_IMPLEMENTATION_PLAN.md) · [ADR-0013-versioned-native-reconstruction-and-workspace-checkpoint-storage.md](../docs/architecture/ADR-0013-versioned-native-reconstruction-and-workspace-checkpoint-storage.md).

**Source code, tests and retained evidence:** [source_progress.py](../src/upgradepilot/caller_signature/source_progress.py) · [investigation.py](../src/upgradepilot/investigation.py) · [test_caller_signature_source_acquisition.py](../tests/test_caller_signature_source_acquisition.py) · [test_caller_signature_workspace.py](../tests/test_caller_signature_workspace.py).

**What to explain:** Investigate the real publication-failure correction and how confirmed source checkpoints survive a later source/worker/store failure without assuming a callback was durably acknowledged.

### F2 — CLI/report/source delivery: exact recovery and expected-revision guards

**Engineering journey / Working Memory:** [2026-11-03_caller-signature-user-delivery_cycle.md](../working-memory/2026-11-03_caller-signature-user-delivery_cycle.md) · [2026-11-06_caller-signature-cli-revision-guards_cycle.md](../working-memory/2026-11-06_caller-signature-cli-revision-guards_cycle.md).

**Governing plans, designs and decisions:** [CALLER_SIGNATURE_NATIVE_ADOPTION_IMPLEMENTATION_PLAN.md](../plans/CALLER_SIGNATURE_NATIVE_ADOPTION_IMPLEMENTATION_PLAN.md) · [CONTRACT.md](../working-memory/evidence/2026-11-06-native-normal-product-attempt-contract/CONTRACT.md).

**Source code, tests and retained evidence:** [caller_signature_delivery.py](../src/upgradepilot/caller_signature_delivery.py) · [cli.py](../src/upgradepilot/cli.py) · [test_caller_signature_delivery.py](../tests/test_caller_signature_delivery.py) · [README.md](../working-memory/evidence/2026-11-06-caller-signature-cli-revision-guards/README.md).

**Real delivery proof:** [partial first live Workspace revision](../working-memory/evidence/2026-11-06-native-normal-product-live-qualification/RESULTS.md) and [successor versioned-pair report/source cold recovery](../working-memory/evidence/2026-11-07-native-proxy-successor/RESULTS.md); exit0, partial coverage, durable publication and supported source-only answer must stay distinct.

**What to explain:** Reconstruct command success versus report save versus durable Workspace revision, lost acknowledgement and why the 40/64-hex identity-guard correction matters.

### F3 — Product qualification: real retained, controlled, installed, live and usefulness

**Engineering journey / Working Memory:** [2026-11-06_native-product-execution-readiness_cycle.md](../working-memory/2026-11-06_native-product-execution-readiness_cycle.md) · [2026-11-06_native-normal-product-live-qualification_cycle.md](../working-memory/2026-11-06_native-normal-product-live-qualification_cycle.md) · [2026-11-06_pypi-transport-diagnosis_cycle.md](../working-memory/2026-11-06_pypi-transport-diagnosis_cycle.md) · [2026-11-07_pypi-route-repair_cycle.md](../working-memory/2026-11-07_pypi-route-repair_cycle.md) · [2026-11-07_native-proxy-successor_cycle.md](../working-memory/2026-11-07_native-proxy-successor_cycle.md) · [2026-11-07_httpx-ci-runtime-applicability_cycle.md](../working-memory/2026-11-07_httpx-ci-runtime-applicability_cycle.md) · [2026-11-04_caller-signature-connected-retained-qualification_cycle.md](../working-memory/2026-11-04_caller-signature-connected-retained-qualification_cycle.md) · [2026-11-06_independent-host-timing-and-retained-traversal_cycle.md](../working-memory/2026-11-06_independent-host-timing-and-retained-traversal_cycle.md).

**Governing plans, designs and decisions:** [CALLER_SIGNATURE_NATIVE_ADOPTION_AND_QUALIFICATION_PLAN.md](../plans/CALLER_SIGNATURE_NATIVE_ADOPTION_AND_QUALIFICATION_PLAN.md) · [CONTRACT.md](../working-memory/evidence/2026-11-06-native-normal-product-attempt-contract/CONTRACT.md).

**Source code, tests and retained evidence:** [README.md](../working-memory/evidence/2026-11-04-caller-signature-connected-retained-qualification/README.md) · [README.md](../working-memory/evidence/2026-11-04-bounded-native-navigation-repair/README.md) · [README.md](../working-memory/evidence/2026-11-06-independent-host-timing/README.md) · [test_caller_signature_delivery.py](../tests/test_caller_signature_delivery.py).

**New live qualification/disposition:** [first partial attempt](../working-memory/evidence/2026-11-06-native-normal-product-live-qualification/RESULTS.md), [verified transport diagnosis](../working-memory/evidence/2026-11-06-pypi-transport-diagnosis/RESULTS.md), [route proof](../working-memory/evidence/2026-11-07-pypi-route-repair/RESULTS.md), [qualified exact old/proposed source task](../working-memory/evidence/2026-11-07-native-proxy-successor/RESULTS.md) and [CI/run applicability checkpoint](../working-memory/2026-11-07_httpx-ci-runtime-applicability_cycle.md). Preserve separate runs/horizons, conditional source-only pilot eligibility, three unexamined units/147 gaps, 38 baseline operations versus 26 report source reads (not controlled human usefulness), runtime uncertainty and explicit deferral of new CI/runtime implementation. Host-timed 2,380.532s native paging is a different workload from 43.820s live product invocation.

**What to explain:** Distinguish a prior failed attempt from a verified repair; separate CPU counts from inconclusive elapsed-time measurements, and controlled retained acquisition from live provider/human usefulness proof.

### G1 — Combined source/CI/runtime applicability design checkpoint (now completed; learning later)

**Engineering journey / Working Memory:** [2026-11-07_httpx-ci-runtime-applicability_cycle.md](../working-memory/2026-11-07_httpx-ci-runtime-applicability_cycle.md) · [2026-11-02_runtime-applicability-followup-plan-reconciliation_cycle.md](../working-memory/2026-11-02_runtime-applicability-followup-plan-reconciliation_cycle.md).

**Governing plans, designs and decisions:** [RUNTIME_DEPENDENCY_STATE_PROOF_COMPLETION_PLAN.md](../plans/RUNTIME_DEPENDENCY_STATE_PROOF_COMPLETION_PLAN.md) · [CALLER_SIGNATURE_NATIVE_ADOPTION_AND_QUALIFICATION_PLAN.md](../plans/CALLER_SIGNATURE_NATIVE_ADOPTION_AND_QUALIFICATION_PLAN.md) · [ADR-0010-package-manager-semantic-facts-and-runtime-dependency-state-composition.md](../docs/architecture/ADR-0010-package-manager-semantic-facts-and-runtime-dependency-state-composition.md).

**Source code, tests and retained evidence:** [investigation.py](../src/upgradepilot/investigation.py) · [test_impact_applicability.py](../tests/test_impact_applicability.py).

**Recorded disposition:** July retained Docker CI is not selected test-process proof; October exact-head CI response had zero runs and was verified by offline replay with 41 tests; November live HTTPX finding was conditional. CI `no_successful_ci`/`no_exact_head_workflows`, runtime `no_admitted_candidate`. Historical applicability unresolved; a decision-relevant target-owned test process with exact run/attempt, callable/loaded-file and path evidence is the re-entry condition. No new runner or combined profile selected. [Actual cycle](../working-memory/2026-11-07_httpx-ci-runtime-applicability_cycle.md).

**What to explain:** At the later gate only: what exact installed package, command, import/dispatch and affected-path execution evidence would change a conditional source claim.

### G2 — Deferred evidence-grounded AI and retrieval checkpoint

**Engineering journey / Working Memory:** [2026-11-07_httpx-ci-runtime-applicability_cycle.md](../working-memory/2026-11-07_httpx-ci-runtime-applicability_cycle.md) · [2026-11-03_evidence-grounded-ai-direction_planning-cycle.md](../working-memory/2026-11-03_evidence-grounded-ai-direction_planning-cycle.md) · [2026-10-19_investigator-evidence-first-interpretation-planning_lbd-cycle.md](../working-memory/2026-10-19_investigator-evidence-first-interpretation-planning_lbd-cycle.md).

**Governing plans, designs and decisions:** [UPGRADEPILOT_90_DAY_PLAN.md](../plans/UPGRADEPILOT_90_DAY_PLAN.md) · [INVESTIGATOR_EVIDENCE_FIRST_INTERPRETATION_COMPARISON_PLAN.md](../plans/INVESTIGATOR_EVIDENCE_FIRST_INTERPRETATION_COMPARISON_PLAN.md).

**Source code, tests and retained evidence:** [investigation.py](../src/upgradepilot/investigation.py) · [2026-11-03_evidence-grounded-ai-direction_planning-cycle.md](../working-memory/2026-11-03_evidence-grounded-ai-direction_planning-cycle.md).

**Updated product handoff:** after the CI-first design checkpoint found *missing execution evidence*, the next product design may test evidence interpretation/abstention, but must not let AI invent the absent runtime observation. No model/retrieval work yet activated; learner study still deferred.

**What to explain:** At the accepted future gate only: distinguish missing evidence, retrieval, interpretation and unsupported advice; inspect earlier negative/inconclusive trials before proposing agent capability.


## Immediate continuation

**C2 — Historical result reconstruction (native source-fact and result decoders).** Begin from the actual LifeLog retained repeated-trace measurements and November 1 representation decisions. Then inspect `evidence.py`, `native_codec.py` and `result_codec.py`, followed by targeted tests. The duplicate-call example is a *test fixture introduced for a real retention/relationship-integrity reason*, not the primary case.

**Status unchanged:** six modules covered interactively; C2 remains incomplete. These references are navigation, not proof of the learner's independent code ownership.
