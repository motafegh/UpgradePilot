# Stage 5 Investigator / LLM / agent experiment methodology and machinery audit

**Date:** 2026-10-20  
**Status:** CLOSED — experiment lifecycle/methodology classified; no inference selected  
**Mode:** cross-responsibility Repository Audit  
**Branch:** `audit/project-wide-system-audit-2026-10-20`  
**Main base last reconciled:** `a1c291c6cf9238493eeb666b184192ed178b90f1`  
**Program:** [Project-wide technical audit and correction program](../plans/PROJECT_WIDE_TECHNICAL_AUDIT_AND_CORRECTION_PROGRAM_PLAN.md)  
**Prior result:** [AUDIT-016](../audits/2026-10-20_AUDIT-016_test-proof-and-operational-integrity.md)  
**Durable result:** [AUDIT-017](../audits/2026-10-20_AUDIT-017_investigator-experiment-methodology-and-machinery.md)

## Audit-program cadence

`reconcile → audit/classify → verify → record → fix/route when justified → continue`

No separate D/E learning ceremony is required for this audit slice.

## 1. Question answered

Stage 5 reconciled AUDIT-011 with the later r4/r5 supplied-evidence results, the completed broader Fixed/Agent research branch and current experiment source. It classified which mechanisms still have a current reusable lab responsibility versus which runners now primarily reproduce historical cohorts.

## 2. Main result

The experiment programme's live bottleneck has changed.

AUDIT-011's broad autonomous comparison exposed real control/interface/discovery/semantic confounds and recommended a supplied-evidence interpretation diagnostic. Main later executed that localization:

- r4: 5/5 roles complete, zero control failures, 0/4 semantic cases adequate;
- r5 instruction-only comparison: 5/5 roles complete, 0/4 adequate despite partial improvements;
- broader Fixed/Agent research: 8/8 mechanically valid reports, 0/8 advice-ready; Agent cost/discovery advantages mixed with persistent semantic failures.

Therefore **another autonomous-discovery optimization or prompt/model sweep is not the default next move**. Future inference needs a named residual product responsibility that simpler deterministic/native work cannot answer.

## 3. Lifecycle classification

### Reusable laboratory substrate

Retain, under experiment-only authority and future requalification when their interface/runtime assumptions change:

- `investigator_run_control.py`;
- `investigator_model_interface.py` lower-level strict request/receipt/config/cleanup mechanisms;
- `investigator_workspace_adapter.py` as a lab bridge into product-owned Workspace/source authority;
- `investigator_workspace_trial.py` model-free protocol/packing/reference/publication proof;
- `investigator_supplied_evidence.py` as a generic simpler report-only semantic baseline.

### Narrow/requalify rather than use wholesale

- `qualify_investigator_model_interface.py`: retain identity/backend/render/capacity mechanisms, but do not treat the old six-model Raw/Structured matrix as the standing admission cost for future experiments.
- deterministic API/source research such as `api_python_bindings.py`: retain as candidate research input only; port/reuse into product only if a later selected producer/consumer responsibility independently justifies it.

### Historical/dormant cohort runners

- `run_investigator_semantic_comparison.py`: exact old three-deployment/two-case/Raw-Structured comparison is closed/inconclusive and should not be resumed to finish its denominator.
- `run_investigator_supplied_evidence.py`: binds the specific Gemma12 operating point, packet roles and r4/r5 freeze; retain for provenance/reproduction, not as the default launcher for a new hypothesis.
- exact supplied-evidence packet recipes: exposed development material and historical reproduction input, not a protected future corpus.

### Superseded as active architecture

Workspace prototype/revision/migration experiment modules remain historical architecture evidence. ADR-0012/0013 and `src/upgradepilot/workspace/` now own the accepted/current Workspace method. Future product migration should extend active product owners/tests, not prototype experiment routes, unless a new research question explicitly selects them.

## 4. Methodology decisions

- future model calls require a named residual product question;
- autonomous discovery should not be optimized before a selected interpretation method earns semantic adequacy on supplied evidence;
- requalification must be proportional to the interface/deployment claim that changed;
- multi-role decomposition is a valid candidate only as a discriminating same-evidence responsibility-isolation experiment;
- materially tuned semantics require newly protected future cases for broader claims;
- strict references/accounting/cleanup/freeze retention earned real value and should be preserved proportionately;
- negative/inconclusive experiment outputs remain immutable useful evidence.

## 5. New repository-structure finding

`experiments/` has no README/lifecycle index despite mixing reusable substrate, conditional deterministic research, historical cohort runners and superseded architecture prototypes.

This is a P2 maintainability/selection problem because executable historical files can look equally current to a new session.

The first experiment-area correction should be a compact `experiments/README.md` lifecycle/ownership map, not a general framework rewrite or physical file purge. Moving/deleting files should wait for reference/import auditing.

## 6. Verification boundary

No model call, model load, GPU action, target execution, experiment rerun or historical evidence mutation occurred. The audit used retained experiment evidence, current source and the completed research-branch checkpoint at `cde0ea9906fa37e4184962d0ba65577e4d62396e`.

## 7. Handoff

Stage 5 closes under the focused audit-program cadence.

**Next:** Stage 6 consolidated cross-domain decision review. It should resolve priorities/dependencies among AUDIT-013 through AUDIT-017 and select a correction order before broad remediation. Low-risk documentation/lifecycle corrections may then be applied first; architecture/proof/CI changes should follow their own bounded owner/proof boundaries.

`UP-SKILL:upgradepilot-repository-audit`
