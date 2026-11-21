# Whole-project product and design audit

Ali requested a thorough audit of the current UpgradePilot product, code, design and supporting evidence. The [Charter](../PROJECT_CHARTER.md), [90-day route](../plans/UPGRADEPILOT_90_DAY_PLAN.md), [audit guidance](../audits/README.md) and [Operating Guide](../OPERATING_GUIDE.md) bound the work.

## Planning progression

The initial orientation reconciled local and remote `main` at `048aa570`. Two pre-existing untracked notes sat outside the committed audit baseline. The [October whole-project audit](../audits/2026-10-22_AUDIT-012_whole-project-value-capability-and-delivery.md) sampled product value, ordinary reachability, semantic reliability, delivery, evaluation and lifecycle at `afdd2b4a`. Later milestones include opt-in caller/signature and selected historical CI delivery, normal and offline CI report improvements, scoped matrix correlation and Workspace recovery. The [maintainer next-check review](2026-11-21_maintainer-next-check-review_lbd-cycle.md) supplies a candidate peer-pin consistency investigation for comparison with other potential investments. Independent maintainer usefulness remains a distinct open question.

Ali approved writing one execution plan and explicitly moved learning to a separate parallel effort. This audit proceeds as engineering work with verification and evidence recording. The initial Learning-by-Doing phase tracking ended at scope orientation. This record remains the dated working record for the same audit, with its original path retained for continuity.

The [whole-project audit plan](../plans/WHOLE_PROJECT_PRODUCT_AND_DESIGN_AUDIT_PLAN.md) defines nine coverage areas, required source and adverse-input traces, the retained-case proof strategy, focused and broader verification, and the formal report acceptance standard. It keeps baseline selection and evidence freshness explicit and uses the existing October audit as a historical comparator. Current source and test results for the audit are pending execution under that plan. Live continuation remains in [`MEMORY.md`](../MEMORY.md).

Ali added a request to identify future AI and model opportunities during the audit. The plan now requires an assessment of adopted model use, prior research and negative results, and concrete candidate seams. The report will rank opportunities alongside deterministic changes using the evidenced problem, affected layer, validation owner, simpler comparison, cost, and candidate-specific proof obligations. The plan records design and evaluation candidates for later selection.

Planning checks verified the local references and heading anchors, nine product coverage rows, six AI opportunity rows, and the link from the live handoff. This verification covers the plan and its routing. Product verification remains part of audit execution.

## Pre-audit documentation reconciliation

Ali requested that confirmed documentation drift be corrected before starting the audit. The live handoff now puts the matrix acceptance and the hosted verification boundary before dated qualification history. The old November 12 execution and ownership handoffs are time-scoped, and the ApplyPilot entry identifies its original report as the before-fix capture. The README documents saved workflow facts, scoped matrix evidence and the combined caller/signature profile. The documentation map points to the implemented delivery and the AV-Tracer example. ADR-0014 time-scopes its design context and links the installed acceptance while preserving the accepted method.

Verification used the editable WSL Python 3.12.3 environment. All 18 focused CLI tests passed with networking isolated. Offline CLI checks covered help, combined-profile argument guards, MapProxy attempt facts, unavailable-source exit 7, and AV-Tracer saved report and exact Workspace revision/source inspection. The initial local extraction used default directory permissions and the Workspace reader rejected it. Repeating the documented extraction with an owner-only umask passed, with all published checksums verified. The eight checked documents resolved their local links and Markdown anchors. Product source, tests, and hosted workflow match the matrix acceptance tree by path comparison. Audit execution remains pending.

## Audit execution baseline

Ali activated the written plan. Local main, its remote-tracking ref and the remote agreed at `2e74f20836424030d547b79113737f2c758bd4d4`, tree `a179cb0b6cca5c886f57bcd2fb997f5e98774fee`. Two pre-existing untracked records were excluded. Exported that Git tree into a private directory for checks. Compared the installed acceptance environment's entire 120-module source set against the export and verified byte identity. The first six focused groups passed 58 tests. The experiment dependency boundary, dependency consistency and both installed CLI entry points passed. The full isolated product regression started after the focused checks.

## Evidence and verification progression

The shared PR observation path admitted two controlled provider inputs explicitly marked private or internal. No authenticated source, private repository, or real credential was used. Source and installed client inspection confirmed that the local semantic request wrapper leaves the underlying HTTP redirect policy enabled while disabling ambient proxies. No redirect, model call, or external transfer was attempted. Ordinary GitHub JSON resource enforcement, target wheel evidence composition, partial Workspace migration and independent maintainer usefulness were recorded separately from these two verified contract discrepancies.

The first full run from the Git export reported three failures and one skip. The two observer checks needed loopback, and the Workspace checkout refusal needed actual Git metadata. Mapping the test user to root also skipped the filesystem write-permissions check. Rebuilt and installed the exact product wheel offline from local cached dependency wheels, with no optional experiment group. The module parity check and 16 investigation tests passed there. Fetched the pinned tree into a private shallow checkout from the local repository, activated only loopback in an isolated namespace, and dropped namespace capabilities before running tests as the normal user. All six harness rechecks passed, including the formerly skipped permissions check. A complete repeat with the corrected harness followed.

In the existing isolated product environment, retained report digests and meaningful verdicts for MapProxy, ApplyPilot, OpenCV, and Pydantic/Soup Sieve matched fresh offline opens. The MapProxy attempt view and seven unresolved package states matched, and the two checksum-verified AV-Tracer captures passed six report, Workspace, and original-source operations.

## Completed review and handoff

The corrected regression on the clean installed wheel passed **1,182 tests with zero skips**. The [verification receipt](evidence/2026-11-21-whole-project-audit/VERIFICATION.json) preserves both attempts, the exact clean wheel and dependency identities, controlled trust checks, experiment-boundary result and raw log digests. The [formal audit](../audits/2026-11-21_AUDIT-016_whole-project-product-and-design.md) maps public paths and all nine coverage areas, reconciles the six October findings, and ranks six AI opportunities against simpler baselines. The recommended first decision is selection of narrowly scoped public-target admission and local-model transport repairs. Product mutation, a fresh live check and AI execution are separate decisions. Independent maintainer usefulness remains open.

UP-SKILL:upgradepilot-planning-design

UP-SKILL:upgradepilot-repository-audit

UP-SKILL:upgradepilot-learning-by-doing (initial orientation only)

UP-SKILL:upgradepilot-working-memory
