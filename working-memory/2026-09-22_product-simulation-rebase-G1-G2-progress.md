# Product Simulation Rebase — G1 Closure / G2 Continuation

**Date:** 2026-09-22  
**Status:** ACTIVE companion progression record; the [initial rebase working memory](2026-09-22_product-simulation-current-state-rebase.md) remains the branch-level anchor and route.  
**Branch:** `research/product-simulation-rebase-2026-09-22`  
**Mode:** Product Simulation research and analysis, non-blocking relative to `main`  
**Procedure:** `UP-SKILL:upgradepilot-working-memory`

## 1. Starting point

The branch-level rebase reconstructed material Phase A and later product changes against the older Product Simulation corpus and identified G1 command/runtime truth, G2 job-to-Target composition, G3 package-state semantics, and G4 target wheel-tag witness feasibility as candidate research families. Its first screening suggested `aiohttp#13785` and `black#5421`; these needed tighter source-to-command checking before any scenario selection.

## 2. Material progression / corrected assumptions

1. **Corrected the Black false positive.** Black #5421 changes only `pyproject.toml`'s optional `width-table` extra (`wcwidth==0.2.14 → ==0.8.4`). The inspected successful `python -m pip install .` does not select this extra. Successful execution of that unrelated command does not prove changed-dependency consumption. Excluded Black from retained G1 cases; preserved it only as a rejected screening control. This corrected the earlier, too-broad preliminary screening interpretation.
2. **Completed the bounded G1 set without forcing a third unrelated PR.** Aruba #83 gives two distinct exact-source command shapes: sole pip install in `lint.yml`, and second sequential pip install in `test.yml`. The Test log independently confirms the second command ran, while successful containing-step metadata alone would not satisfy current sole/first runtime-strengthening policy. Test runner checked out a synthetic PR merge ref, not bare head; preserve this difference. aiohttp #13785 gives first-sequential Bash structure but the exact changed source `requirements/base.txt` is consumed via `-c`, which the current `-r`-only direct requirements observer does not recognize. Runtime from an earlier sdist install logs multidict 6.9.0; do not misattribute that to the later slotscheck step.
3. **Preserved G1 evidence as a distinct non-controlling research artifact**, not an approved scenario: [G1 command/runtime real-case screening](../product-simulation/2026-09-22_G1_COMMAND_RUNTIME_REAL_CASE_SCREENING.md). The `aiohttp` constraints-source relationship is a serious **candidate** for future real simulation and an actionable research handoff, but the main product owner must decide whether/how its proof contract should change.
4. **Started G2 through exact-source, exact-job screening.** The same aiohttp PR changes `runtime-deps.txt`, `base.txt`, `test.txt` and other pin files. The exact-head workflow includes a concrete Ubuntu/Python 3.11 `lint-from-sdist` job and a matrix-expanded static `test` job with OS/Python-dependent contexts. The changed relevant `*.txt` paths enter inspected commands through `-c`, so the current direct-source observer cannot establish those selected paths through its admitted `-r` contract. This **upstream gap prevents using aiohttp alone as clean positive end-to-end F4 evidence**. A static job key is not a matrix runtime row.
5. **Aruba is a cross-workflow control, not the missing same-workflow F4 case.** Lint/test are separate one-job workflow definitions with direct changed-source installs; Validate has two unrelated action jobs and no visible direct requirements install. Success of Validate does not transfer changed-dependency consumption to Lint/Test. Preserved G2's first-pass findings and proof limits in [G2 first screening](../product-simulation/2026-09-22_G2_MULTI_JOB_TARGET_FIRST_SCREENING.md).

## 3. Current status and route

- **R1/R2 — first-pass done:** material current-product / older-simulation rebase documented in initial anchor.
- **R3/R4 — first gap inventory and research priorities done:** G1–G4 identified, provisional priorities retained.
- **R5/R6 G1 — bounded screening done:** three discriminating command shapes from Aruba/aiohttp, plus one screened-out Black false positive. No numbered scenario admitted. Stop further G1 lookalike collection unless new counterevidence changes the boundary.
- **R5/R6 G2 — IN PROGRESS:** two real hosts screened; neither independently validates the selected *same-workflow multi-job* F4 seam because one is blocked by predecessor `-c` source semantics and the other separates consumers into different workflows.
- **G3 — evidence already available from the earlier Salt/MontePy/Sigstore/Aruba pass:** do not repeat the same broad query; formalize a targeted G3 artifact only when a new discriminating finding or a main-workstream handoff needs preservation.
- **G4 — deferred bounded witness feasibility.**

**Immediate next research question:** Find **one** untouched Python Dependabot PR with an exact changed `-r/--requirement` source in a workflow containing multiple static jobs with contrasting declared Target contexts, one/both of which consume that same source. Preserve exact PR head/merge-ref distinction, workflow job keys, execution status, and whether a matrix row is dynamically selected. Check whether the actual current CI-to-Target producer can bind that source/selected job; don't substitute a familiar job name. If no clean sample appears after a bounded search, record the absence and use a real-derived controlled variant rather than claiming real F4 acceptance.

**No branch integration yet.** Continue research in isolation, do not change product source/tests/spec/plans/root `MEMORY.md`/main workstream memory, and merge only upon explicit authorization after a coherent stopping point.
