# UpgradePilot Current Memory

**Last updated:** 2026-09-20  
**Authority:** sole owner of the live project position, current blockers, selected continuation, and current learning depth.

## Live position — main product workstream STARTED

- **Current responsibility:** **AUDIT-008-F11 — audit/live-state lifecycle reconciliation; index updates DONE, post-change learning/closure NEXT**. F3 and F9 are CLOSED at their selected bounded proof/learning horizons. Do not reopen them without concrete regression or contradiction.
- **Primary mode:** bounded Audit/Review + canonical A → B → C → D → E Learning-by-Doing. Learning-note artifacts remain out of scope unless Ali explicitly requests one.
- **Selected execution/learning plan:** `plans/END_TO_END_PRODUCT_FLOW_LEARNING_AND_EVIDENCE_TO_ACTION_EXECUTION_PLAN.md`.
- **Parent execution plan:** `plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`.
- **Controlling current-system audit/input:** `audits/2026-09-19_AUDIT-008_current-system-evidence-to-action-readiness.md` (AUDIT-008).
- **Active main working memory:** `working-memory/2026-09-20_f11-audit-lifecycle-reconciliation.md` (F11 source/rationale, index changes, learning/proof). Closed F9 handoff: `working-memory/2026-09-20_f9-public-github-authentication-phase-a.md`. Historical F3 proof/F9 handoff: `working-memory/2026-09-19_f3-hosted-verification-and-f9-handoff.md`; earlier detailed F3 work: `working-memory/2026-09-19_1825_parent-synthesis-evidence-path-reaudit.md`.
- **Parallel learning:** `working-memory/2026-09-19_cycle3-integrated-learning-review.md` continues independently in another conversation. Its remaining exercises are not a gate blocking main product progression. Do not mark its outcomes complete or rewrite its record from this workstream.
- **Cycle status:** Cycle 1 CLOSED; Cycle 2 CLOSED; Cycle 3 CLOSED. Do not reopen accepted command-analysis implementation without concrete regression/contradiction.
- **Repository route:** `main` unless Ali selects another route. Current F11 work is audit lifecycle coordination only, not product source mutation, new action permissions, agentic evaluation or external-target mutation.

## Immediate continuation

### F3 closure — exact hosted proof

F3 implementation Learning-by-Doing phases A/B/C/D/E were completed with Ali; its deferred executable validation subsequently completed A/B/C/D/E. [Product verification run #6](https://github.com/motafegh/UpgradePilot/actions/runs/35465839476), ID `35465839476`, attempt 1, success at `08a3f70b5717255d7ed5f96ff3ec3ef67bfe4942` containing F3 source/tests. Ubuntu 24.04, Python 3.12.14; fresh installation/pip check/installed CLI PASS; focused investigation **15/15 PASS**, deterministic regression **608/608 PASS**, including F3 synthesis and normal-path integration cases. F3 is CLOSED at its bounded proof horizon; no live public-PR/model or new maintainer-action permission follows.

### F9 — CLOSED: deliberate public GitHub authentication

**Concrete problem and selected contract:** historical public-PR investigations used `env -u GITHUB_TOKEN ...` to avoid unintended use of a stale shell credential and HTTP 401. Proxy/TLS issues are separate. After Ali asked for a more accessible Phase-A explanation, we used that existing workaround to establish the bounded responsibility before implementation. Ordinary `upgradepilot owner/repo 123` now defaults to anonymous access; `--github-auth token-env` deliberately reads `GITHUB_TOKEN`, rejecting missing/empty values before acquisition. The new GitHub-owned Requests session suppresses implicit `.netrc` authentication on initial and redirected requests while preserving deliberate bearer credentials, cross-host stripping and normal environment proxy configuration. `README.md` documents the changed contract. The closed dated F9 working record owns exact source, tests and limits.

**Exact F9 hosted proof:** Ali dispatched [Product verification run #7](https://github.com/motafegh/UpgradePilot/actions/runs/35516933780), ID `35516933780`, attempt 1, success on 2026-09-20 at checkout/logged HEAD `2afc566a4ce2139f3439d6a4c3cf9596896b3841`, containing F9 source/docs/tests. Ubuntu 24.04.5, Python 3.12.14, Requests 2.34.2. Fresh install, `pip check` and both installed CLI help entry points PASS; focused investigation **15/15 PASS**; deterministic product regression **616/616 PASS**, including **8/8 F9 authentication tests**. F3's older proof is not reused for F9.

**Learning/closure:** A/B/C/D/E DONE. After code-level teaching from the familiar `env -u GITHUB_TOKEN` case, Ali correctly reasoned that an expired ambient token will not be used by the ordinary command absent deliberate `--github-auth token-env`. This establishes bounded user-facing configuration ownership, not independent mastery of Requests redirect internals. No material learning or test gap remains for the selected F9 scope. **F9 CLOSED**. No live public-PR, real token/rate-limit acceptance, arbitrary proxy behavior, local-model quality, or non-abstention action is proved by the controlled hosted tests.

### F11 — index correction completed; learning and closure next

`audits/LIFECYCLE.md` distinguishes a valid audit's evidence from its current or future execution selection. The `audits/active/README.md` entry for AUDIT-005 was stale relative to `MEMORY.md`; its former link to `plans/B2_AGENTIC_INVESTIGATION_ORCHESTRATION_EVALUATION_PLAN.md` was also outdated. F11 moved AUDIT-005's **index entry only** from ACTIVE to SCHEDULED, retaining its original canonical audit and its approved, undispositioned evaluation checkpoint. `audits/active/README.md` now lists AUDIT-008 as the current audit input; `audits/scheduled/README.md` links the actual `plans/BOUNDED_PRODUCT_AGENTIC_INVESTIGATION_PLANNER_AND_ORCHESTRATION_EVALUATION_PLAN.md` and its accepted protocol.

**Explicit future handoff, not live activation:** when the selected evidence-to-action execution journey completes or is explicitly stopped/replanned, **before ordinary B2 continuation**, revisit the still-open B2/X1 agentic evaluation checkpoint. At that handoff explicitly activate the owning evaluation plan or record an evidence-backed reschedule/defer/reject decision in the appropriate owning plan and `MEMORY.md`; do not silently skip it. The old R7 activation prerequisite was satisfied historically but does not make the checkpoint today's selected work. Scheduling does not imply adoption, rejection, actual model evaluation, or ending a separate Learning-Only pause. AUDIT-005's technical conclusions are retained as valid review evidence, not a competing live instruction.

**F11 cycle:** A DONE (lifecycle/owner orientation); B DONE (correct audit indexes and named plan/handoff); C ongoing (dated F11 working record and post-change index/live-state review); D NEXT (teach distinction and ask one practical changed-case question); E PENDING (close after any needed learning repair). This is documentation-only: review exact file contents and diff, not unrelated product CI. **After F11:** begin the execution plan's action-relative evidence-producer/reachability comparison; do not preselect F4/F5/F6/F7.

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

**Cycle-3 authoritative hosted proof (historical, not F3/F9 proof):** GitHub Actions run `35448172928`, Python 3.12.14, fresh installation/pip check/installed CLI PASS; focused investigation 15/15; Cycle-3 focused 76/76; full deterministic product regression 604/604. S001 sole ordinary top-level command and S002 first sequential Bash command are eligible positive families; S004 `&&` short-circuit remains unresolved/deferred. Earlier Cycle-2 hosted closure recorded 587/587 deterministic tests; these are separate proof horizons, not additive tests.

**Essential proof limits:** static command presence is not execution/success; source order is not execution order. An eligible exact static occurrence correlated to a successful, unmasked runtime step earns bounded `supported_runtime_correlated`, **not** direct proof of inner-command execution or success, exact installed version/artifact, wheel/tag compatibility, update safety, or permission to recommend a maintainer action. An ineligible occurrence does not earn runtime strengthening; insufficient structural/profile/correlation facts remain unresolved; known non-successful runtime status remains factual even when broader CI coverage is unresolved. Retain weaker static support where justified. Parser grammar nodes remain private; syntax family and execution profile are distinct; parser uncertainty never creates a regex-based positive fallback.

## Parent synthesis position and known boundaries

`PROJECT_CHARTER.md` owns the public outcome family; `docs/specifications/UPGRADEPILOT_MAINTAINER_ACTION_SYNTHESIS_SPECIFICATION.md` owns accepted action-relative permission and abstention semantics; the parent synthesis plan coordinates the evidence/producer journey. Technical investigation/product decision-model specification owns mechanism-specific semantics. Current `src/upgradepilot/maintainer_action.py` admits only `abstain`; other Charter actions are not implemented merely because stable semantics or simulation pressure exist.

After F3 baseline and F9/F11 trust/coordination repairs, compare exact action-relative evidence producer and application-composition gaps; select one decision-critical responsibility rather than implementing every audit finding. A source-traced resilience risk is not automatically a newly reproduced defect; a deliberately unsupported input shape is not automatically a correctness bug. Missing capability does not automatically justify `defer` or a targeted check; green CI does not prove compatibility or a favorable merge recommendation.

Candidate investigation anchors, **not findings or Build authorization:** preserve an already identified CI consuming job through Target composition rather than independently re-solving it; establish exact version/artifact or wheel-tag runtime evidence only for a selected needed proposition; examine a newly demonstrated more fundamental producer/composition issue first if warranted. Real public simulation cases may discriminate a material question, but historical case actions are not runtime policy and synthetic controls alone cannot establish real-case action reachability.

## Historical and parallel detail owners

The previous expanded `MEMORY.md` snapshot at commit `0201069d91f2d2bc776b84616870fe0926386f3f` contains historical Cycle-1/2/3 design and progress. This file keeps compact live position and retained proof/limits; dated detail remains in Git history and actual working-memory owners:

- `working-memory/2026-09-17_cycle3-runtime-strengthening-phase-a-orientation.md` — completed Cycle-3 design decisions;
- `working-memory/2026-09-18_cycle3-runtime-strengthening-build.md` — Cycle-3 build and technical closure;
- `working-memory/2026-09-16_cycle2-phase-d-integrated-learning-plan.md` — Cycle-2 D/E and deferred learning;
- `working-memory/2026-09-19_cycle3-integrated-learning-review.md` — separate integrated recall/relearning in progress;
- `working-memory/2026-09-19_1825_parent-synthesis-evidence-path-reaudit.md` — AUDIT-008 review, end-to-end reconstruction and F3 implementation/ownership;
- `working-memory/2026-09-19_f3-hosted-verification-and-f9-handoff.md` — exact F3 hosted proof and historical F9 handoff;
- `working-memory/2026-09-20_f9-public-github-authentication-phase-a.md` — closed F9 source, learner reorientation, exact hosted proof and ownership evidence;
- `working-memory/2026-09-20_f11-audit-lifecycle-reconciliation.md` — F11 lifecycle decision, index updates, future handoff and ownership check.

Keep `MEMORY.md` as the sole compact live-state owner. Promote accepted durable semantics or methods only to actual specification/ADR owners; dated working memory must not become a competing live-state authority.