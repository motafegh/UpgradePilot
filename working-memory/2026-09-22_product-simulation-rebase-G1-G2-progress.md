# Product Simulation Rebase — G1 Closure / G2 Bounded Handoff

**Date:** 2026-09-22  
**Status:** ACTIVE companion progression record; the [initial rebase working memory](2026-09-22_product-simulation-current-state-rebase.md) remains the branch-level anchor.  
**Branch:** `research/product-simulation-rebase-2026-09-22`  
**Mode:** Product Simulation research and analysis, parallel to `main`; `UP-SKILL:upgradepilot-working-memory`.

## 1. Starting point and corrected scope

The initial rebase reconstructed Phase A and later product changes against the older Product Simulation corpus. It identified G1 command/runtime truth, G2 exact CI-job → Target composition, G3 pip/uv package-state semantics, and G4 target wheel-tag witness feasibility. This workstream covers the whole current product, not only the current main workstream's Phase B question. Our independent research branch never owns changes to main product code/tests/specs/plans or root/main memory.

## 2. G1 meaningful progression — bounded screening completed

- **Black #5421 false positive corrected:** changed `pyproject.toml`'s optional `width-table` extra, but the successful `pip install .` step did not select it. Removed as changed-source consumption proof, preserved only as screened-out control.
- **Aruba #83:** two direct-source command shapes from distinct exact-head workflows: sole `-r requirements.txt` in `lint.yml`; second sequential `--requirement requirements.txt` in `test.yml`. Retained Test logs prove the second command ran in the observed run, but step success alone does not satisfy the current sole/first runtime strengthening rule. Preserve synthetic PR merge checkout vs bare head.
- **aiohttp #13785:** first-sequential install step uses exact changed `requirements/base.txt` through `-c`; current `-r`-only direct-source observer cannot admit that changed-source relation. The earlier sdist install logs multidict 6.9.0; never misattribute that result to the later slotscheck install. The real `-c` input is a substantive candidate product-breadth finding, not an authorized implementation change.
- Durable artifact: [G1 screening](../product-simulation/2026-09-22_G1_COMMAND_RUNTIME_REAL_CASE_SCREENING.md). G1 stopped after discriminating positive/conservative/source-breadth shapes, not arbitrary case count. No numbered scenario admitted.

## 3. G2 meaningful progression — complete at bounded search/design horizon

- **aiohttp #13785:** exact-head workflow has different static jobs and matrix-expanded runtime instances, but the selected changed requirement pin files enter the inspected relevant commands through `-c`. This is an upstream source-selection gap; the host cannot independently validate the current F4 positive `-r` path. Do not collapse runtime matrix instances into distinct static job keys.
- **Aruba #83:** `ruff`/`test` directly consume the changed source but belong to separate one-job workflow definitions; the unrelated Validate jobs do not consume it. This is cross-workflow identity pressure, not the missing same-workflow test.
- **Open WebUI #26494:** Dependabot changes `backend/requirements.txt` pytest `~=8.4.1 → ~=9.1.1`, head `ed99df86c8cb69e5848592f0af0df2fb0d3d0103`; matching `.github/workflows/backend.yaml` has only static key `format-check` with Python 3.11/3.12 matrix instances. They install Ruff independently, never visibly consume the changed requirements path; their observed formatting failures do not establish a pytest failure. This is a valuable non-consumer control, not F4 positive. Head-associated Python CI run `28488568057` had two failed formatting job instances.
- **MontePy #986:** multiple jobs and explicit state witness, but PR changes `pyproject.toml` build requirements consumed via project install, not an exact changed `-r` file. Retain for G3, not the narrow G2 proof.
- Durable artifacts: [G2 first screening](../product-simulation/2026-09-22_G2_MULTI_JOB_TARGET_FIRST_SCREENING.md) and [G2 non-consumer/stop](../product-simulation/2026-09-22_G2_NONCONSUMER_CONTROL_AND_STOP.md).
- **Bounded negative result:** no untouched host in this deliberately screened set met *all* gates for a clean same-workflow, multiple-STATIC-job, exact changed `-r`/`--requirement` source with inspectable relevant runtime evidence. This is not a population-prevalence claim. Do not force a positive case or continue broad low-information searches.
- Prepared [G2 real-derived controlled variant design](../product-simulation/2026-09-22_G2_REAL_DERIVED_JOB_COMPOSITION_VARIANT_DESIGN.md): freezes real Aruba PR and direct-source commands, *synthetically* combines consuming/non-consuming jobs into one workflow and contrasts declared Target environments. The altered workflow and runner contexts are explicitly not real Aruba observations. Expected identity, deduplication, missing-job, runtime proof boundaries and optional matrix controls are written. This is design-only; no replay/source or test change or target run was performed or authorized by it.

## 4. Current route and handoff

**R1/R2:** first current-product / simulation coverage rebase recorded in initial anchor. **R3/R4:** four gap families identified. **G1:** bounded screening closed. **G2:** bounded screening and alternative real-derived fixture *design* closed; no new numbered scenario or public F4 acceptance claim. **G3:** next active evidence family, reusing the earlier Salt/MontePy/Sigstore/Aruba exact-public-case research, especially ambient semantic selectors versus operational variables and post-install state proof. Do not repeat broad discovery before checking prior evidence. **G4:** deferred bounded witness-feasibility search.

**Next research slice:** write a tightly sourced, non-controlling G3 synthesis/research artifact from exact proposal/revision/workflow/job/log evidence, keeping four propositions separate: command execution, effective package-manager semantics, installer-result operation, independent target-owned state. Distinguish later mutation and log-retention evidence limits; stop when further cases cease to discriminate. Optionally hand off the observed aiohttp `-c` source-consumption gap to main as a *proposal for owner review*, never implement or change accepted product semantics from this branch. The G2 controlled fixture can be replayed by the F4 owner only if separately selected/authorized on then-current main.

**Branch boundary:** no product source/tests/stable specs/plans, root `MEMORY.md`, main workstream working memory, target repositories or external CI were mutated. No merge yet; reconcile with current `main` only for an explicitly authorized integration. This record supersedes its earlier same-workflow positive-search next-action as of this bounded stopping point.