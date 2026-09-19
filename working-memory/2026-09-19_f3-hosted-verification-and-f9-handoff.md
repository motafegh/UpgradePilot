# F3 hosted verification closure and F9 handoff — 2026-09-19

**Responsibility:** dated evidence and handoff for the F3 executable-validation slice and the next F9 public-acquisition trust boundary. `MEMORY.md` alone owns live state.

## F3 validation — canonical A → B → C → D → E

- **A — DONE:** proof requirement was bounded synthesis correctness, application investigation→synthesis preservation, deterministic regression and fresh installed-product behavior at a revision containing F3. No live public-PR/model-quality or new maintainer-action permission claim was sought.
- **B — DONE:** Ali manually dispatched `.github/workflows/product-verification.yml` on `main`. GitHub Actions [Product verification run #6](https://github.com/motafegh/UpgradePilot/actions/runs/35465839476), run ID `35465839476`, attempt 1, completed `success`, checked out `08a3f70b5717255d7ed5f96ff3ec3ef67bfe4942` on 2026-09-19. That commit includes the F3 source/test changes ending at `b3b1963e3466eac9b829f269293e86d43109ddb1`. Ubuntu 24.04 / Python 3.12.14; fresh package installation and `pip check` passed; installed CLI entry points passed. Focused investigation composition: 15/15 PASS, including `test_upstream_source_problem_stops_semantics_target_and_impact_but_not_ci`. Full deterministic product regression: 608/608 PASS, including all seven `test_maintainer_action.py` tests (the four added F3 cases and three retained cases).
- **C — DONE:** exact run, revision, environment, test counts, outcome and proof limits preserved here. The historical Cycle-3 run `35448172928` is not reused as F3 proof.
- **D — DONE (proportionate):** green focused normal-path integration and complete deterministic regression support the selected F3 synthesis repair. They do not establish live public-source availability/model extraction behavior, comprehensive scenario coverage, exact runtime environment compatibility, or permission for merge/investigate/block/etc. No failing test was observed in the hosted run.
- **E — DONE:** no test failure to diagnose and no additional F3 repair justified by this proof. F3 technical responsibility CLOSED at this bounded executable-proof horizon. Next plan responsibility is F9 public acquisition authentication trust, then F11 audit lifecycle reconciliation; later action-relative F4/F5/F6/F7 comparison remains downstream.

## F9 — next bounded cycle, A orientation only

**Question:** can an unrelated ambient `GITHUB_TOKEN` silently change or break otherwise-public PR evidence acquisition, and what is the smallest explicit configuration boundary that preserves legitimate authenticated public access?

**Expected path:** inspect canonical `SECURITY.md`, the selected plan and Build procedure, then actual `cli.py` / GitHub adapter token handling and tests. Distinguish anonymous public mode, explicit authenticated mode, rate-limit/authorization needs, ambient shell/proxy conditions, and acquisition error versus source absence. Review current behavior before selecting the smallest implementation design; do not introduce credential management or rewrite general networking.

**Stop:** no F9 implementation recorded yet. No learning-note artifact unless explicitly requested. No external target mutation or secret exposure. Start with A (brief concrete teaching) before B and use A→B→C→D→E.
