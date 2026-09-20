# UpgradePilot Current Memory

**Last updated:** 2026-09-20  
**Authority:** sole owner of the live project position, current blockers, selected continuation, and current learning depth.

## Live position — main product workstream STARTED

- **Current responsibility:** AUDIT-008-F9 — deliberate public GitHub acquisition authentication trust boundary. **F3 is technically CLOSED** at its selected deterministic/installed-product proof horizon; F9 A completed after learner reorientation, B source/tests implemented and source-reviewed, executable product validation PENDING. Do not label F9 technically closed.
- **Primary mode:** bounded Build/Implement + canonical A → B → C → D → E Learning-by-Doing. Learning-note artifacts remain out of scope unless Ali explicitly requests one.
- **Selected execution/learning plan:** `plans/END_TO_END_PRODUCT_FLOW_LEARNING_AND_EVIDENCE_TO_ACTION_EXECUTION_PLAN.md`.
- **Parent execution plan:** `plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`.
- **Controlling current-system audit/input:** `audits/2026-09-19_AUDIT-008_current-system-evidence-to-action-readiness.md` (AUDIT-008).
- **Active main working memory:** `working-memory/2026-09-20_f9-public-github-authentication-phase-a.md` (F9 A/B/proof/deferred D/E). The prior F3 hosted-proof/F9 handoff is `working-memory/2026-09-19_f3-hosted-verification-and-f9-handoff.md`; prior detailed F3 analysis/implementation and interactive ownership remain in `working-memory/2026-09-19_1825_parent-synthesis-evidence-path-reaudit.md`.
- **Parallel learning:** `working-memory/2026-09-19_cycle3-integrated-learning-review.md` continues independently in another conversation. Its remaining exercises are not a gate blocking main product progression. Do not mark its outcomes complete or rewrite its record from this workstream.
- **Cycle status:** Cycle 1 CLOSED; Cycle 2 CLOSED; Cycle 3 CLOSED. Do not reopen accepted command-analysis implementation without concrete regression/contradiction.
- **Repository route:** `main` unless Ali selects another route. Only the selected F9 trust-boundary responsibility and necessary coordination updates are admitted; unrelated product changes, accepted spec/ADR changes, new action permissions and external-target mutation are out of scope.

## Immediate continuation

### F3 closure — exact hosted proof

F3 implementation Learning-by-Doing phases A/B/C/D/E were completed with Ali; its deferred executable validation subsequently completed A/B/C/D/E at the proportional verification depth. Ali manually dispatched the repository's existing `Product verification` workflow. GitHub Actions [run #6](https://github.com/motafegh/UpgradePilot/actions/runs/35465839476), run ID `35465839476`, attempt 1, completed **success**, checked out `08a3f70b5717255d7ed5f96ff3ec3ef67bfe4942` (contains F3 implementation/test commits). Ubuntu 24.04, Python 3.12.14; fresh installed package and `pip check` PASS; installed CLI entry points PASS; focused investigation integration **15/15 PASS**; full deterministic product regression **608/608 PASS**, including all seven synthesis tests and the new normal-path changelog-stop assertion. F3 is **CLOSED for the accepted bounded correctness/proof responsibility**. This is not live public-PR/model quality or new maintainer-action-permission proof. Detailed checkpoint is in the dated F3 hosted-proof working memory.

### F9 — source implemented, executable validation pending

**Concrete problem understood with Ali:** the historical public-PR integration workaround `env -u GITHUB_TOKEN ...` avoided accidental use of a stale shell token and resulting HTTP 401. This is distinct from the separately recorded ambient proxy/TLS issue. Earlier technical orientation alone did not establish Ali's understanding; it was redone using this familiar command before he authorized B. After source review, teach actual changed code starting with this simple explanation rather than jumping to HTTP internals.

**Implemented on `main`:** `src/upgradepilot/cli.py` defaults to anonymous (`upgradepilot owner/repo 123`), with `--github-auth token-env` explicitly reading `GITHUB_TOKEN` and rejecting missing/empty token before acquisition. The new GitHub-only `auth_session.py` excludes ambient `.netrc` credentials from prepared/redirected requests while retaining deliberate bearer and cross-host stripping; `github/api.py` selects this session by default without changing caller-injected sessions, HTTP outcome categories, proxy configuration or investigation/synthesis logic. New `tests/test_github_authentication.py` contains eight focused cases; `README.md` documents the changed CLI contract. Implementation/docs revision before state updates: `8e7a589e48805624ae445ecc7f116be6d99cedf3`. The active dated F9 working memory owns exact changes and stop conditions.

**Proof debt / next operation:** the isolated Requests 2.32.5 behavior simulation passed, but **no current F9 UpgradePilot test suite or hosted installed-product CI run has executed**. Manual `Product verification` must be run on an exact revision including F9 and its job logs checked: fresh installation, installed CLI, focused investigation and full deterministic regression including new auth tests. GitHub connector reads but cannot dispatch this workflow; assistant local container cannot clone repo due DNS. If CI fails, fix only demonstrated F9 issues and obtain new revision-specific proof. Source and authored tests are not an executable pass. No live public-PR/model proof or non-abstention action permission is inferred from a green deterministic run.

**F9 cycle:** A DONE; B source/test edits DONE, executable proof DEFERRED; C ONGOING; D PENDING (source-based explanation and short ownership check); E PENDING. Complete proportional D/E and the deferred executable-proof slice before closing F9 or moving to F11. F11 audit lifecycle reconciliation remains the next plan responsibility, followed by action-relative producer/reachability comparison.

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

**Cycle-3 authoritative hosted proof (historical, not F3 proof):** GitHub Actions run `35448172928`, Python 3.12.14, fresh installation/pip check/installed CLI PASS; focused investigation 15/15; Cycle-3 focused 76/76; full deterministic product regression 604/604. S001 sole ordinary top-level command and S002 first sequential Bash command are eligible positive families; S004 `&&` short-circuit remains unresolved/deferred. Earlier Cycle-2 hosted closure recorded 587/587 deterministic tests; these are different historical proof horizons, not additive tests.

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
- `working-memory/2026-09-20_f9-public-github-authentication-phase-a.md` — active F9 authentication source, implemented changes, learner reorientation and executable proof debt.

Keep `MEMORY.md` as the sole compact live-state owner. Promote accepted durable semantics or methods only to actual specification/ADR owners; dated working memory must not become a competing live-state authority.
