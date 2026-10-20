# AUDIT-016 — Test, proof and operational integrity

**Audit date:** 2026-10-20  
**Branch:** `audit/project-wide-system-audit-2026-10-20`  
**Main revision last reconciled:** `a1c291c6cf9238493eeb666b184192ed178b90f1`  
**Mode:** cross-responsibility test/proof/operations audit  
**Authority:** non-controlling audit evidence. This record does not itself authorize workflow/repository-setting/test cleanup or product implementation.

## 1. Question

Does UpgradePilot currently have the smallest sufficient proof system for its active product claims and incomplete Workspace migration, and what proof must exist before later integration/cutover?

This audit distinguishes:

- local deterministic product regression;
- hosted installed-package verification;
- compatibility breadth;
- exact environment reproduction;
- Workspace recovery/reconstruction;
- saved-report reopening;
- deterministic investigation replay;
- experiment/model qualification;
- direct Workspace consumer-cutover proof.

## 2. Executive assessment

UpgradePilot's **deterministic product test suite is substantially stronger than the stale hosted status suggests**. The sampled central tests protect real responsibility boundaries rather than merely increasing test count, especially Workspace cold reconstruction, lifecycle/store behavior, normal investigation composition, report preservation, CI/environment derivation and source topology.

The major proof weakness is not lack of local tests. It is that canonical `main` has no enforced fresh hosted proof despite a good existing workflow. The latest hosted Product verification success is October 2 at `1c371875ffb459ce2e2c9c913a5a87a10a434928`, while the audited main revision is 322 commits later.

Other important gaps are claim/proof classification rather than failing code:

- Python support is declared open-ended as `>=3.12`, but hosted compatibility is currently observed only on Python 3.12;
- clean hosted installation proves resolver/package compatibility at that moment, not deterministic recreation of an exact dependency set;
- Workspace recovery is strongly proven for admitted native families but is not deterministic investigation replay;
- complete Workspace→synthesis/report cutover parity cannot yet be tested because that migration is not implemented;
- a small set of historical-phase test names and duplicate import/interface assertions should be simplified later, but no broad test-suite reduction is justified by this audit.

## 3. Findings

### AUDIT-016-F1 — P1: canonical integration lacks enforced fresh hosted deterministic proof

The existing Product verification workflow is a good ordinary integration gate candidate:

- fresh Ubuntu 24.04 runner;
- Python 3.12;
- fresh venv;
- `pip install .` and `pip check`;
- selected revision and interpreter recorded;
- resolved packages recorded through `pip freeze`;
- both installed CLI entry points checked from outside the checkout;
- focused investigation composition then full deterministic product suite;
- experiment/model/live-proof machinery excluded;
- checkout permission read-only.

The weakness is repository integration policy:

- workflow trigger is only `workflow_dispatch`;
- `main` is unprotected;
- no required status checks/rulesets are configured;
- no current hosted status exists for the audited main head;
- last success is 322 commits behind.

**Disposition:** retain the workflow design, but before trustworthy branch integration make the deterministic product job run automatically on the chosen integration boundary (normally pull request and/or push as appropriate) and require its result for `main`. Keep model/GPU/live acquisition/experiment qualification outside this required ordinary gate.

This does not imply every exploratory/research branch must pay the same hosted cost before every commit. The gate belongs at canonical integration.

### AUDIT-016-F2 — P2: Python compatibility declaration exceeds observed hosted matrix

`pyproject.toml` declares:

```toml
requires-python = ">=3.12"
```

and README instructs users to use “Python 3.12 or newer.”

Current hosted verification tests Python 3.12 only. This is **not evidence Python 3.13+ fails**. It is a claim/proof mismatch: open-ended package compatibility is broader than the observed hosted environment.

**Disposition:** explicitly choose one policy before stronger compatibility claims:

1. define a supported interpreter matrix and test each supported minor line in hosted CI; or
2. define 3.12 as the currently supported/proven line and narrow public/package metadata accordingly; or
3. keep `>=3.12` as packaging admissibility but state that hosted verification currently qualifies only named tested minors.

Do not silently treat one 3.12 job as proof of all future Python versions.

### AUDIT-016-F3 — P2 requirement clarification: fresh install compatibility is not exact environment reproduction

The hosted workflow intentionally resolves from package ranges, for example `requests>=2.32,<3`, `packaging>=26.2,<27`, `PyYAML>=6.0.3,<7`, and build backend `setuptools>=68`; the tree-sitter compatibility set is pinned exactly.

`pip freeze` records the environment that was actually tested. It does not by itself provide an input that recreates that exact environment on a later day.

This is not automatically defective: a project often needs both:

- **fresh resolver compatibility** — does the product install and pass against currently allowed dependency versions?;
- **exact repeatability** — can a named verified environment be recreated byte/version-for-version when required for diagnosis/release evidence?

The Charter requires clean-setup reproducibility but does not necessarily require every ordinary CI run to use one frozen dependency set.

**Disposition:** preserve the current fresh-resolver job. If exact dependency-set recreation is required for release/debugging/portfolio proof, add a separate retained constraints/lock/receipt mechanism rather than converting the compatibility job into a permanently stale lock-only test. Do not claim exact reproducibility merely because `pip freeze` was printed in a transient log.

### AUDIT-016-F4 — RETAIN: Workspace recovery/reconstruction proof is strong for admitted families

`test_workspace_checkpoint_reconstruction.py` is a high-value boundary test, not redundant ceremony. A fresh subprocess receives only the durable store and explicit revision/target selection; network access is actively trapped, acquisition/model/evaluator paths are guarded, the database is verified unchanged by reads, and complete admitted CI/Python projections are compared.

Together with host integration, native reconstruction, lifecycle/publication and store tests, this provides credible evidence that admitted Workspace material can survive durable publication and fresh-process reconstruction without live recomputation.

**Disposition:** retain this proof. Do not add a generic duplicate hosted “recovery smoke” merely to repeat what this test already establishes. Hosted execution of the deterministic suite is sufficient when the canonical workflow is fresh/enforced.

### AUDIT-016-F5 — RETAIN: saved-report reopening has a distinct and well-tested responsibility

`test_report_file.py` protects:

- digest/corruption detection;
- schema and semantic validation after resigning;
- duplicate-key/nonfinite/deep/malformed input rejection;
- bounded file size;
- atomic non-replacing publication;
- race/interruption cleanup;
- regular-file-only reads;
- explicit read/save failures.

This is not Workspace recovery and not investigation replay. It is durable report-record validation/publication and offline inspection.

**Disposition:** retain as an independent proof family.

### AUDIT-016-F6 — P2 outstanding product obligation: deterministic replay remains separate and unproven as a user/product capability

The README truthfully states that reopening a report does not replay an investigation. ADR-0012/0013 truthfully separate Workspace recovery from deterministic replay. The route plan lists deterministic replay as a B3 outcome.

Current Workspace cold reconstruction proves restoration of retained native state for admitted families, not re-execution of the admitted deterministic investigation processing from retained inputs under a replay contract.

There is no contradiction as long as B3 replay is not claimed completed. The current issue is an **outstanding product/proof obligation**, not a defect in recovery.

**Disposition:** keep replay explicit in future route accounting. When selected, define retained input boundary, method/version identities, deterministic/non-deterministic intermediates and equivalence criteria. Do not rename Workspace recovery, report reopening or fixture-driven tests as replay.

### AUDIT-016-F7 — P1 before Workspace consumer cutover: migration parity proof must be explicit and temporary

AUDIT-015 established that current report/synthesis still consume `PublicPullRequestInvestigation` while Workspace captures only a subset of the broader report responsibility.

Before direct consumer cutover, the proof set must establish at least:

```text
legacy field / semantic proposition
→ current native owner / retained material
→ Workspace family or explicit non-migration disposition
→ normal-path value/state
→ recovered value/state when recovery applies
→ synthesis/report consumer meaning
```

Required cases must include success plus problem/unresolved/not-evaluated/unsupported states where meaningful. The normal and recovered Workspace paths must preserve the same semantic strength without inventing later evidence.

**Important:** parity proof is migration scaffolding. After consumers cut over and legacy plumbing is retired, remove tests whose sole responsibility was comparing two representations that no longer coexist. Do not preserve permanent dual-surface ceremony just because it once protected migration.

### AUDIT-016-F8 — RETAIN: controlled end-to-end composition tests protect distinct product seams

Sampled historical-name tests still protect useful permanent responsibilities. For example:

- `test_step7f_end_to_end.py` runs the normal application composition through source-window construction, controlled local semantic adapter/reconstruction, deterministic claim admission and conditional target activation;
- `test_r6_investigation_ci_integration.py` proves normal public-PR orchestration derives CI/dependency consumption from exact workflow/project/lock sources and retains the corresponding native Workspace capture.

These are not redundant merely because their names reference historical steps.

**Disposition:** retain their proof behavior. Rename/rehome by permanent responsibility when cleanup is selected rather than deleting them based on historical naming.

### AUDIT-016-F9 — P3: active test naming/documentation still exposes historical implementation phases

Active tests include names such as `test_r6_*`, `test_step7f_*`, `test_step8_*`, `test_f4_*` and `test_package_manager_route_a_semantic_fixture.py`. `tests/README.md` also predates the substantial Workspace/report proof families and no longer describes the active suite well.

This increases orientation cost and can make current proof look like retained phase archaeology.

**Disposition:** during a bounded maintainability cleanup, rename tests by permanent responsibility and refresh `tests/README.md`. Preserve Git history for phase provenance rather than keeping phase labels as the primary active test taxonomy.

### AUDIT-016-F10 — P3: small interface/topology test duplication can be reduced

`test_source_topology.py` and `test_package_interface.py` both assert the package root has `upgradepilot.__all__ == ()`. The package-interface test also imports several internal symbols and then only asserts they are not `None`; the topology test imports many owners and additionally checks that they are callable/types.

Successful test-module import already establishes much of this reachability. The unique valuable responsibilities are:

- package root remains intentionally minimal;
- removed legacy package attributes stay absent;
- obsolete flat module paths stay absent;
- responsibility-owned module paths remain importable.

**Disposition:** merge/shrink redundant positive import/read-back assertions while retaining the negative compatibility/topology guards. This is low-priority cleanup, not a correctness issue.

### AUDIT-016-F11 — RETAIN: product and experiment dependency/proof boundaries remain separated

Product dependencies live under `[project].dependencies`; `langgraph` is isolated under the `experiments` dependency group. The hosted product workflow installs `.` only and runs `tests/`, not `experiments/tests/` or live developer tools.

No evidence was found that ordinary product CI is accidentally counting model/agent experiment regression as product proof.

**Disposition:** preserve this split.

## 4. Minimum future canonical proof model

A proportionate steady-state proof hierarchy should be:

### Per-change local/focused

- responsibility-owned unit/contract tests;
- nearest integration/composition tests;
- targeted migration parity only while migration exists.

### Canonical deterministic integration

On the chosen PR/push integration boundary:

- fresh installed package;
- `pip check`;
- CLI entry points from outside checkout;
- supported Python matrix as deliberately defined;
- full deterministic `tests/` suite;
- required status before `main` integration.

### Separate, non-required ordinary gates

- live GitHub/PyPI acquisition proof;
- LM Studio/model quality/qualification;
- experiment suites;
- GPU/deployment qualification;
- public-case usefulness studies;
- protected semantic evaluation.

Those have their own plans/evidence and should not make ordinary deterministic integration flaky or hardware-dependent.

## 5. What not to do

Do not:

- delete tests because the suite is large;
- add duplicate recovery tests merely to increase hosted coverage;
- turn current deterministic CI into a live-network/model workflow;
- use `pip freeze` output as if it were an exact reproducibility input;
- infer Python 3.13+ incompatibility from absence of testing;
- call saved-report reopen or Workspace recovery deterministic replay;
- retain legacy-vs-Workspace parity tests forever after the legacy representation is removed.

## 6. Recommended correction order

1. **Canonical integration gate:** automatic deterministic workflow + required status/protection at main integration.
2. **Compatibility policy:** decide supported Python minor lines and align metadata/README/CI matrix.
3. **Workspace migration proof ledger:** specify parity obligations before direct synthesis/report cutover.
4. **Replay accounting:** keep deterministic replay explicitly pending until separately implemented/proven.
5. **Low-priority test cleanup:** responsibility-based names, refreshed tests README, remove duplicate import/interface assertions.
6. **Exact environment reproduction only if a real release/diagnostic need requires it**; preserve fresh-resolver compatibility separately.

## 7. Stop line

This audit does not authorize repository branch-protection changes, workflow edits, Python-support narrowing, test deletion/rename or replay implementation.

The next program stage should consolidate Investigator/LLM experiment methodology using AUDIT-011 plus the later completed/inconclusive cohorts, then Stage 6 can prioritize these proof corrections alongside product/architecture findings before remediation.

## References

- `.github/workflows/product-verification.yml`
- `pyproject.toml`
- `README.md`
- `PROJECT_CHARTER.md`
- `plans/UPGRADEPILOT_90_DAY_PLAN.md`
- `audits/2026-10-20_AUDIT-013_stage1-governance-current-state-integrity.md`
- `audits/2026-10-20_AUDIT-015_workspace-authority-and-consumer-cutover.md`
- `tests/README.md`
- `tests/test_workspace_checkpoint_reconstruction.py`
- `tests/test_workspace_host_integration.py`
- `tests/test_workspace_consumer_access.py`
- `tests/test_report_file.py`
- `tests/test_step7f_end_to_end.py`
- `tests/test_r6_investigation_ci_integration.py`
- `tests/test_source_topology.py`
- `tests/test_package_interface.py`

`UP-SKILL:upgradepilot-repository-audit`
