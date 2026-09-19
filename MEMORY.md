# UpgradePilot Current Memory

**Last updated:** 2026-09-19  
**Authority:** sole owner of the live project position, current blockers, selected continuation, and current learning depth.

## Live position — main product workstream STARTED

- **Current responsibility:** execute the post-audit end-to-end product-flow learning/evidence-to-action journey, beginning with the source-verified product-flow reconstruction and ownership baseline. Ali explicitly selected this combined learning/building plan on 2026-09-19.
- **Primary mode:** Learning-by-Doing over the operation appropriate to each plan slice. The first slice is read-only source/test reconstruction and ownership transfer; product Build is **not yet entered or authorized**.
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

Begin the **Product-flow reconstruction and ownership baseline** slice from the selected execution/learning plan.

Trace the actual current normal path from source/tests:

```text
CLI/input
→ exact PR / base / head identity
→ dependency transition + source contexts
→ CI run/job/workflow evidence
→ static consumption + bounded runtime strengthening
→ PyPI/upstream evidence
→ target relevance + mechanism-specific applicability
→ artifact Target boundary
→ PublicPullRequestInvestigation
→ standalone maintainer-action synthesis
→ current evidence-report CLI
```

For each important seam establish:

1. producer and exact input;
2. evidence/proposition produced and identity/provenance carried;
3. consumer/composition boundary;
4. unresolved/unsupported/failure behavior;
5. proof and non-proof;
6. normal-path reachability.

Use the real source and representative tests; use product-simulation cases only where they materially discriminate a boundary. Apply A → B → C → D → E and teach unfamiliar premises before reasoning checks.

After the flow is source-verified, create one durable product-flow learning/reference artifact through the normal learning-artifact procedure. Do not create it from assumptions or use it as a second specification/live-state owner.

**Current stop line:** this first slice is read-only product reconstruction/learning. Do not modify product source/tests/specifications/ADRs, implement AUDIT-008-F3/F9/F4/F5/F6/F7, or admit a new maintainer action until the reconstruction slice is completed and the next bounded Build responsibility is explicitly entered.

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
