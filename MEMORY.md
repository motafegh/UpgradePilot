# UpgradePilot Current Memory

**Last updated:** 2026-09-19  
**Authority:** sole owner of the live project position, current blockers, selected continuation, and current learning depth.

## Live position — main product workstream STARTED

- **Current responsibility:** AUDIT-008-F3 honest abstention-synthesis residual-uncertainty preservation — **implementation slice phase D (post-implementation ownership check)**. A/B/C are complete for what was actually implemented/source-reviewed; executable validation remains explicit proof debt.
- **Primary mode:** Build/Implement + canonical A → B → C → D → E Learning-by-Doing. Learning-note artifacts remain out of scope unless Ali explicitly requests one.
- **Selected execution/learning plan:** `plans/END_TO_END_PRODUCT_FLOW_LEARNING_AND_EVIDENCE_TO_ACTION_EXECUTION_PLAN.md`.
- **Parent execution plan:** `plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`.
- **Active current-system audit/input:** `audits/2026-09-19_AUDIT-008_current-system-evidence-to-action-readiness.md` (AUDIT-008).
- **Active main working memory:** `working-memory/2026-09-19_1825_parent-synthesis-evidence-path-reaudit.md`.
- **Selected earlier bounded implementation plan:** `plans/STATIC_WORKFLOW_COMMAND_ANALYSIS_AND_RUNTIME_STRENGTHENING_IMPLEMENTATION_PLAN.md` — COMPLETE, historical implementation/proof owner, **not** the active new Build task.
- **Parallel learning:** `working-memory/2026-09-19_cycle3-integrated-learning-review.md` continues independently in another conversation. Its remaining exercises are **not a gate** blocking the main product re-audit. Do not mark its learning outcomes complete or rewrite its record merely because the main workstream moved on.
- **Cycle status:** Cycle 1 CLOSED; Cycle 2 CLOSED; Cycle 3 CLOSED. Do not automatically reopen command-analysis implementation or duplicate its integrated learning in this workstream.
- **Accepted architecture:** `docs/architecture/ADR-0009-parser-backed-static-workflow-command-analysis.md`.
- **Repository route:** `main`, unless Ali later requests otherwise. Main review authorizes only necessary working-memory/live-state coordination writes; no product source/tests, accepted specifications/ADRs, plan, or external-target mutation merely from review findings.

## Immediate continuation

Continue the **current F3 implementation slice at phase D**, not at a new Build responsibility.

### Current canonical cycle state

```text
A — DONE
    oriented the F3 synthesis responsibility, owner boundaries and proof limits

B — DONE for implementation/source-test mutation
    implemented bounded residual-uncertainty projection
    added focused + normal-shaped integration proof cases
    corrected one misplaced integration assertion during source review

C — DONE
    preserved commits, exact proof limitation and executable-validation debt
    F3 remains IMPLEMENTED / PROOF-PENDING

D — ACTIVE NOW
    inspect/teach from the actual F3 source and tests
    distinguish planned behavior from implemented behavior
    reason about causal de-duplication, closed vs unresolved states,
    domain ownership, and proof/non-proof
    perform a small ownership check with Ali

E — NEXT
    repair any important reasoning gap
    orient the deferred executable-validation responsibility and stop line
```

After E, do **not** pretend the implementation slice's deferred tests ran. When an executable path becomes available, open a separate bounded **F3 executable-validation evidence slice** with its own proportional A → B → C → D → E:

```text
A — orient exact proof claims
B — run tests/verification
C — preserve exact outputs
D — interpret what passed/failed and proof limits
E — repair if needed; close F3 only on sufficient proof, otherwise orient repair
```

Required executable proof remains:

```text
tests/test_maintainer_action.py
→ relevant tests/test_investigation.py integration
→ full deterministic product regression
→ hosted installed-package verification if required for final closure
```

Current execution limitation remains: `.github/workflows/product-verification.yml` is manual `workflow_dispatch`; the available GitHub connector has no dispatch action and there is no run/status for the current F3 code horizon. Therefore source review/test code is **not** executable proof.

**Current stop line:** complete F3-D and F3-E before selecting another substantive slice. F9 remains downstream and must not be treated as active while F3 required proof is unresolved. Do not add non-abstention actions, change accepted synthesis semantics, wire CLI recommendations, or create learning-note artifacts.

## Retained completed foundations and proof

Do not reopen without concrete regression or contradiction evidence:

- exact GitHub run/job attempt coherence and bounded static↔runtime step identity correlation;
- exact-revision dependency-source provenance;
- ADR-0009 parser-backed static workflow command architecture;
- Cycle 1: effective shell context, shared parser-neutral command analysis/occurrence/atom/source span and structure for Bash/sh, PowerShell/pwsh and CMD/batch;
- Cycle 2: one workflow job/step traversal, one shared command analysis reused by direct requirements, project environment and package invocation; canonical occurrence location/identity and bounded static source ordering;
- Cycle 3: positive whole-step/position structural admission, exact-occurrence candidate/eligibility handoff, conservative runtime composition and basis-aware aggregation.

Accepted architecture, in brief:

```text
GitHub Actions run-step + effective shell context
→ Tree-sitter shell-family parser / provider-owned structural facts
→ UpgradePilot-owned parser-neutral command analysis and canonical occurrence identity
→ dependency / project-environment / CI invocation observers
→ CI-owned occurrence-level runtime-strengthening eligibility
→ exact correlated runtime step outcome and bounded aggregate
```

**Cycle-3 authoritative hosted proof (historical, not a fresh check in the active review):** GitHub Actions run `35448172928`, Python 3.12.14, fresh installation / pip check / installed CLI PASS; focused investigation 15/15; Cycle-3 focused 76/76; full deterministic product regression 604/604. S001 sole ordinary top-level command and S002 first sequential Bash command are eligible positive families; S004 `&&` short-circuit remains unresolved/deferred. Earlier Cycle-2 hosted closure recorded 587/587 deterministic tests; these are different historical proof horizons, not additive tests.

**Essential proof limits:** static command presence is not execution/success; source order is not execution order. An eligible exact static occurrence correlated to a successful, unmasked runtime step earns bounded `supported_runtime_correlated`, **not** direct proof of inner-command execution or success, exact installed version/artifact, wheel/tag compatibility, update safety, or permission to recommend a maintainer action. An ineligible occurrence does not earn runtime strengthening; insufficient structural/profile/correlation facts remain unresolved; known non-successful runtime status remains factual even when broader CI coverage is unresolved. Retain weaker static support where justified. Parser grammar nodes remain private; syntax family and execution profile are distinct; parser uncertainty never creates a regex-based positive fallback.

## Parent synthesis position and known boundaries

`PROJECT_CHARTER.md` owns the public outcome family; `docs/specifications/UPGRADEPILOT_MAINTAINER_ACTION_SYNTHESIS_SPECIFICATION.md` owns accepted action-relative permission and abstention semantics; the parent synthesis plan coordinates the evidence/producer journey. The technical investigation/product decision-model specification owns mechanism-specific semantics. Current `src/upgradepilot/maintainer_action.py` admits only `abstain`; other Charter actions are not implemented simply because their stable semantics or simulation pressure exist.

The parent plan's accepted direction after reliable source and command-meaning work is to re-audit normal producer and application composition, choose the next decision-critical evidence bottleneck, evaluate whether any non-abstention permission is truly reachable, then admit one action path at a time with positive and defeater proof. A source-traced resilience risk is not automatically a freshly reproduced defect; a deliberately unsupported input shape is not automatically a correctness bug. Missing capability does not automatically justify `defer` or a targeted check; green CI does not prove compatibility or a favorable merge recommendation.

Candidate investigation anchors, **not findings or Build authorization:** preserve an already identified CI consuming job through Target composition rather than independently re-solving it; establish exact version/artifact or wheel-tag runtime evidence only for a selected needed proposition; examine a newly discovered, more fundamental producer/composition issue first if evidence warrants. Real public simulation cases may discriminate a material question, but historical case actions are not runtime policy and synthetic controls alone cannot establish real-case action reachability.

## Historical and parallel detail owners

The previous expanded `MEMORY.md` snapshot at commit `0201069d91f2d2bc776b84616870fe0926386f3f` contains the detailed historical Cycle-1/2/3 design and progress narrative. This live-state file now keeps the compact current position and retained proof/limits; historical detail remains available in Git history and its actual dated owners:

- `working-memory/2026-09-17_cycle3-runtime-strengthening-phase-a-orientation.md` — completed Cycle-3 design decisions and reasoning;
- `working-memory/2026-09-18_cycle3-runtime-strengthening-build.md` — three build stages and final technical closure;
- `working-memory/2026-09-16_cycle2-phase-d-integrated-learning-plan.md` — Cycle-2 D/E closure and deferred learning;
- `working-memory/2026-09-19_cycle3-integrated-learning-review.md` — separate in-progress integrated recall/relearning;
- `working-memory/2026-09-19_1825_parent-synthesis-evidence-path-reaudit.md` — active main-product review, engineering findings, learning checks and handoff.

Keep `MEMORY.md` as the sole compact live-state owner and preserve detailed current-session evolution in its active working-memory record. Promote newly accepted durable semantics or methods to their actual specification/ADR owners when appropriate; do not make a working memory or historical document a second live-state authority.
