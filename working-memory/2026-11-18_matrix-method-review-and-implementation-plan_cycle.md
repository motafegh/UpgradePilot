# Matrix method review and implementation planning

2026-11-18 · [ADR-0014](../docs/architecture/ADR-0014-literal-matrix-specialization-and-scoped-ci-evidence.md) · [Design cycle](2026-11-18_literal-matrix-dependency-evidence_design-cycle.md)

- **A0 — DONE.** Local and fetched origin main agree at `fcf56a65`. Reconciled the proposed ADR with Ali's architectural agreement and explicit final acceptance requirements.
- **A1/A2 — DONE at the review/planning scope.** Ali specified the full matrix/ordinary-job acceptance case, identity migration, adversarial checks, normal-product and regression gates, and the stop before Build. The preceding design supplied the rationale and proof boundaries.
- **B — DONE.** Reviewed the remaining methods, recorded architectural acceptance with qualification boundaries, and prepared the implementation/qualification plan.
- **Verification — GREEN for planning.** Checked the actual consumer assumptions, two targeted diagnostic receipts, local references and coverage of Ali's five acceptance concerns. Product implementation gates remain unexecuted.
- **D — DONE at the planning walkthrough scope.** The handoff explains the per-variant migration and the difference between a milestone and final feature completion.
- **E — CLOSED at the review-before-Build boundary.** Present sequence, risks and gates for Ali's requested review.
- **C — DONE.** Preserved decisions, scope, diagnostic correction, proof and handoff.

The immediate detailed user request and preceding design already provide the orientation for this planning responsibility. Compress repeated orientation stops while retaining the explicit stop before Build. Architectural agreement does not establish implementation correctness or a learner-ownership pass.

The orientation map is the eight-instance acceptance case → remaining matching/shell/identity decisions → producer-to-consumer migration → adversarial and historical controls → installed normal-entry-point and complete regression proof → final completion decision. Interim milestones retain their own proof without substituting for that final gate.

## Method review findings

| Observation from active source/evidence | Execution decision |
| --- | --- |
| runtime_execution selects the first matching job key, and candidate deduplication lacks a matrix context. ExactCICommandIdentity and package-state command recovery make the same ordinary-job assumption. | Migrate the full address through every consumer before connecting matrix values to positive execution/state paths. |
| The existing ordered-step matcher returns a whole-job problem when any required step is missing. | Split unique job association from per-step evidence. Preserve useful independent witnesses and scoped failures instead of dropping the remaining variants. |
| A retained MapProxy 3.12 job with install step 6 removed still has a unique Use python/Run tests witness. Removing the distinguishing Python witness leaves four test candidates. | Keep association where its independent basis survives, make the missing install unknown, and refuse coordinate choice when distinguishing evidence is gone. |
| The shell classifier's current positive later-command relation is absent, and the initial private design controls covered only a small straight-line set. | Qualify the full structural and shell-profile premise against explicit defeaters before enabling the second requirements install. |
| A self-authored Bash startup file can exit successfully before the script or install an ERR trap that masks its failure. | Treat material startup/environment settings as part of execution-profile qualification. A launch flag alone cannot establish the stronger premise. |
| Report decoding admits only named assessment/state families, and native capture currently selects CI family codec versions from existing result shape. | Migrate producer, codec/version selection, material-basis validation and report state admission together. |
| Historical matrix input records have no new variant provenance. | Preserve their old unscoped meaning, without decoding them into ordinary instances or new matrix positives. |
| The previous CI design replay fabricated an unrelated unavailable PyPI branch to isolate the diagnostic. | Final normal-product qualification must use genuine provider observations for all reached branches through the installed public CLI. The earlier diagnostic is insufficient as final execution evidence. |

The review reused ADR-0008/0009/0010/0013 and Core report/recovery invariants. The existing hosted product-verification workflow confirms that the maintained full product regression command is unittest discovery over tests. Architecture/import checks and experiments consuming modified CI/native/report contracts are additional relevant gates. No hosted dispatch is implied by local qualification.

## Diagnostic evidence

The retained-input witness check used the actual GitHub parsers and current step matcher, with temporary specialized values in private diagnostic objects. It reproduced runtime_step_match_missing for the 3.12 install omission. The two surviving source-defined step names identify only that static variant among the eight admitted instances. Removing the Python discriminator leaves four potential test variants. This supports the association/step-completeness distinction. It does not implement the new partial association method.

Private witness-review receipt SHA-256 `bde3698039926ee2a8c046a7844bc15218db229098ff336ff5b038787a743b52`.

Self-authored startup controls used GNU Bash 5.2.21 with an explicit environment and an ephemeral BASH_ENV file. An early startup exit produced code 0 without running the script. An ERR trap also produced code 0 after a failing command. The initial prediction that startup set +e alone would let the script continue was false on this launch path. The retained disable-flag control exited 1, and the plan relies on the observed early-exit/trap defeaters. All target workflow text remained inert.

Private startup-control receipt SHA-256 `98d3181ae018f237593b0c64ccc29b3ce03047e8cbe5cba9a13a3178000e39c4`. These are design controls on the local shell. They do not qualify every GitHub shell/profile.

## Planning outcome and handoff

[ADR-0014](../docs/architecture/ADR-0014-literal-matrix-specialization-and-scoped-ci-evidence.md) records Ali's agreement to the architecture/general direction and ties implementation acceptance to the explicit gates. The [implementation and qualification plan](../plans/LITERAL_MATRIX_CI_EVIDENCE_IMPLEMENTATION_AND_QUALIFICATION_PLAN.md) contains the eight-instance inventory, remaining method resolutions, complete identity migration map, dependency order, adversarial expectations and final gate.

The plan distinguishes baseline freeze, scoped provider work, cross-consumer migration, association, sequential execution, public delivery/recovery and final installed-product qualification. Every engineering milestone remains interim until all required final evidence exists. Installed-state and behavior questions retain their own missing premises, and an existential workflow positive cannot become all-variant coverage.

Ali requested this plan and its risks before Build. The next step is that review. Product source and tests remain at their prior revision. Independent learner ownership and maintainer usefulness remain open.

Provenance: `UP-SKILL:upgradepilot-planning-design`, `UP-SKILL:upgradepilot-repository-audit`, `UP-SKILL:upgradepilot-working-memory`.
