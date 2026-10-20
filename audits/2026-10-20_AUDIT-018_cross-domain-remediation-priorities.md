# AUDIT-018 — Cross-domain remediation priorities and dependency order

**Audit date:** 2026-10-20  
**Branch:** `audit/project-wide-system-audit-2026-10-20`  
**Original branch base:** `main@a1c291c6cf9238493eeb666b184192ed178b90f1`  
**Latest reconciled main:** `bfcc8b916fc33523a535f7c5a994d118d09552b8`  
**Mode:** consolidated cross-domain decision review  
**Inputs:** AUDIT-013 through AUDIT-017  
**Authority:** non-controlling audit disposition. Individual corrections still belong to their owners/proof boundaries.

## 1. Executive decision

The project does **not** need a broad rewrite. The strongest current architecture/evidence controls should be retained. The remediation strategy should instead remove misleading/stale control surfaces, strengthen canonical integration proof, preserve the product-value-first gate, and finish existing migration responsibilities before introducing more semantic/agent complexity.

The central sequencing decision is:

```text
truth / ownership cleanup
→ canonical deterministic integration proof
→ execute product-value feasibility only if selected after review
→ complete exact Workspace migration ledger before cutover work
→ bounded architecture remediation
→ only then consider a residual semantic experiment if product evidence still justifies it
```

No current evidence justifies an immediate model sweep, autonomous-discovery optimization, agent-framework adoption, generic proposition framework, Workspace redesign or test-suite purge.

## 2. Upstream convergence during audit

While this branch was auditing, main advanced by one commit to `bfcc8b91` and revised the product-value plan/proposal/live handoff. That upstream revision independently incorporated most of the October 20 correction request:

- S001–S016 light screening;
- smallest discriminating deep cohort;
- bounded multi-role candidate;
- material-premise semantic adequacy;
- explicit review before follow-on execution.

This confirms the direction rather than invalidating Stage 2.

The audit branch's plan still adds two useful explicit distinctions not as clearly named upstream:

1. **current-source projection** as a proof mode separate from fresh product, replay, component proof and historical simulation;
2. **information value versus action permission** as separate evaluation dimensions under the current abstain-only synthesis boundary.

Final integration should reconcile these semantically instead of choosing a version by commit order.

## 3. Remediation waves

### Wave 1 — FIX NOW: truth, lifecycle and navigation corrections

These changes are low-risk, high-signal and do not require product execution:

1. **README LM Studio endpoint** — replace stale `127.0.0.1:12345` with the canonical `18080` boundary and retain the environment link.
2. **Charter time-boundary wording** — stop calling the July 20–October 17 window the current execution period. Preserve it as the initial 90-day horizon and explicitly state whether the same Charter remains controlling until superseded/reframed/terminated.
3. **Audit lifecycle indexes** — remove AUDIT-009/010/011 from `active`; classify them under the correct lifecycle with rationale. Their evidence remains immutable at canonical paths.
4. **Experiment lifecycle map** — add `experiments/README.md` separating reusable substrate, conditional research, historical/dormant cohort runners and Workspace prototypes superseded as active architecture.
5. **Smart Situational Override semantic boundary** — clarify at root that procedural routing/order/depth/gates may be adapted, but accepted Charter/specification/ADR semantic requirements and acceptance invariants require explicit owner change rather than an “override.” Child boilerplate reduction can follow later.
6. **Branch/upstream reconciliation note** — record `bfcc8b91` as the latest main horizon and preserve the product-plan sibling-edit conflict for final integration.

These corrections reduce the chance that later engineering selects stale work or misreads a control boundary.

### Wave 2 — FIX BEFORE TRUSTWORTHY INTEGRATION: canonical proof

1. Change Product verification from manual-only to an automatic deterministic integration check on the deliberately chosen PR/push boundary while retaining manual dispatch.
2. Keep the workflow hardware/network/model independent beyond package installation; do not add LM Studio, GPU, live GitHub/PyPI acquisition or experiment suites.
3. Configure `main` protection/ruleset so the deterministic status is required before integration. The current connector exposes protection/ruleset reads but no administration write action, so repository-setting activation may require Ali's GitHub UI or another authorized administration route.
4. Decide Python support policy and align README/package metadata/CI matrix. Until then, state tested interpreter scope accurately.

This wave is independent of whether the product-value feasibility investigation executes.

### Wave 3 — PRODUCT-VALUE GATE: select/execute only after branch/main reconciliation

The product-value feasibility direction is the right strategic gate. Do not run it merely because the plan exists.

Before activation:

- reconcile upstream `bfcc8b91` and the audit-branch plan additions;
- freeze the final plan text/hash;
- preserve S001–S016 as exposed development evidence;
- keep six active hours and zero model/GPU/network/target/benchmark execution;
- use exact proof modes and separate information value from action permission.

The investigation should decide which next product increment is worth engineering or whether to narrow/stop. Its result may select a deterministic repair, finite comparison, source relation, action-permission work, semantic diagnostic, bounded multi-role experiment, deployment test or no further investment.

### Wave 4 — WORKSPACE MIGRATION PRECONDITION: ledger before refactor

Before Stage 4/5 Workspace consumer cutover Build, produce the exact:

```text
legacy result field / proposition
→ native semantic owner
→ retained material/input identity
→ Workspace family / missing-family disposition
→ normal consumer
→ recovered consumer requirement
→ migration disposition
```

Then use that ledger to decide the smallest missing capture/reconstruction set required by actual report/synthesis consumers.

Do not remove `PublicPullRequestInvestigation` before Workspace can represent every still-supported consumed meaning. Do not add generic parallel truth types.

### Wave 5 — WORKSPACE DIRECT-CONSUMER CUTOVER

Only after Wave 4:

```text
complete required family/material closure
→ prove normal/recovered semantic parity
→ migrate synthesis
→ migrate report/CLI projections
→ retain old bridge only for named compatibility/proof caller
→ retire obsolete legacy plumbing and migration-only parity tests
```

This is a consequential source migration and deserves its own bounded Build/proof cycle.

### Wave 6 — DEFER UNTIL NAMED RESIDUAL: semantic/agent experiments

Current default is no new inference.

A future experiment requires:

- a named product responsibility not cheaply solved by deterministic/native work;
- explicit simpler baseline;
- smallest relevant lab substrate;
- proportional point-specific qualification;
- bounded development diagnostic;
- reject/narrow consequence;
- newly protected material before broader post-tuning claims.

Autonomous discovery, single-pass semantics, multi-role decomposition and deployment/model change are distinct hypotheses and must not be bundled casually.

### Wave 7 — LATER MAINTAINABILITY CLEANUP

After more consequential corrections stabilize:

- rename active `R6`/`Step7F`/`F4` style tests by permanent responsibility;
- refresh `tests/README.md`;
- merge/shrink duplicate package-interface/import assertions;
- reduce repeated Smart Override boilerplate in child Skills after root semantics are unambiguous;
- physically archive/move historical experiment runners only after reference/import impact is checked.

Do not let this cleanup displace product-value, proof or migration work.

## 4. Finding disposition matrix

| Area | Disposition |
| --- | --- |
| Product-value-first strategy | **RETAIN** |
| Hybrid Evidence → Interpretation → Validation → Decision architecture | **RETAIN** |
| Workspace ADR-0012/0013 | **RETAIN** |
| Current partial Workspace/legacy coexistence | **TEMPORARY / FIX BEFORE CUTOVER**, not architecture failure |
| README provider endpoint | **FIX NOW** |
| Charter expired-current-period wording | **FIX NOW** |
| Audit lifecycle current-state leakage | **FIX NOW** |
| Smart Override semantic ambiguity | **FIX NOW** at root; boilerplate cleanup later |
| Experiments lifecycle ambiguity | **FIX NOW** with index, no mass file move |
| Hosted workflow structure | **RETAIN** |
| Automatic/required hosted integration | **FIX BEFORE INTEGRATION** |
| Python `>=3.12` claim versus 3.12-only hosted proof | **RECONCILE BEFORE STRONGER SUPPORT CLAIM / INTEGRATION** |
| Exact environment reproduction | **DEFER unless release/diagnostic need is selected**; keep separate from fresh resolver CI |
| Workspace cold recovery proof | **RETAIN** |
| Saved-report reopen proof | **RETAIN** |
| Deterministic replay | **OUTSTANDING ROUTE OBLIGATION**, do not mislabel recovery/open as replay |
| Broad experiment qualification matrices | **NARROW / PROPORTIONAL REQUALIFICATION ONLY** |
| r4/r5 supplied-evidence runners | **HISTORICAL / DORMANT after concluded question** |
| old Raw/Structured comparison runner | **HISTORICAL / DO NOT RESUME DENOMINATOR** |
| reusable run-control/reference/accounting substrate | **RETAIN conditionally** |
| multi-role/agent framework | **NOT SELECTED** |
| test-suite mass reduction | **REJECT** based on current evidence |

## 5. P1 dependency order

The current P1 findings do not all block each other.

### Must happen before branch integration

- canonical automatic hosted deterministic proof + required main protection;
- reconcile latest main divergence;
- no unresolved contradictory plan/Charter/current-state wording introduced by this branch.

### Must happen before Workspace direct-consumer Build/cutover

- legacy/native/material/consumer ledger;
- missing family disposition;
- parity proof contract.

### Must happen before another semantic experiment

- product-value/deep trace identifies a residual semantic question;
- simpler deterministic/native option is insufficient;
- selected experiment has its own finite protocol/qualification/reject boundary.

No current P1 requires stopping the broad audit branch itself.

## 6. Corrections explicitly rejected for now

Do not currently:

- rewrite Workspace architecture;
- create a generic semantic-evaluation framework;
- make a new agent framework permanent;
- run a model sweep;
- finish old experiment denominators;
- benchmark all S001–S016;
- narrow product claims solely to make existing tests easier;
- delete `PublicPullRequestInvestigation` before consumer/family closure;
- delete historical experiments/results;
- lock all dependencies and thereby lose fresh-resolver compatibility checking;
- merge large test families based on file count.

## 7. Immediate next action

Begin Wave 1 with bounded documentation/governance/lifecycle corrections on the audit branch. Verify each against its canonical owner. Keep executable product behavior unchanged.

After Wave 1, reassess latest main before Wave 2 or the product-value gate.

`UP-SKILL:upgradepilot-repository-audit`
