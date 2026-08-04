# UpgradePilot Current Memory

**Last updated:** 2026-08-04  
**Authority:** Sole repository owner of live project position, latest material verification, blockers affecting continuation, selected continuation, and current learning depth.

## Live position

- **Execution branch:** `main`.
- **Route:** B2 — Public PR vertical slice.
- **Parent plan:** [`plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`](plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md).
- **Selected bounded plan:** [`plans/B2_TARGET_PYTHON_STEP_7_BOUNDED_EXTRACTOR_RUNTIME_INTEGRATION_PLAN.md`](plans/B2_TARGET_PYTHON_STEP_7_BOUNDED_EXTRACTOR_RUNTIME_INTEGRATION_PLAN.md).
- **Accepted semantic method:** [`docs/architecture/ADR-0006-bounded-local-support-drop-semantic-extractor.md`](docs/architecture/ADR-0006-bounded-local-support-drop-semantic-extractor.md).
- **Accepted source organization:** [`docs/architecture/ADR-0007-responsibility-based-python-subpackages.md`](docs/architecture/ADR-0007-responsibility-based-python-subpackages.md).
- **Selected product increment:** **Step 7B — deterministic crossed-release Markdown source windows**.

The earlier source-reconciliation stop line is closed. Step 7's own proof and stop boundaries still control the selected implementation work.

## Latest material verification

Source reconciliation and the post-reconciliation product baseline were accepted with:

- active product regression: **323 tests passed**;
- completed Step 6 experiment regression: **27 tests passed**;
- module and installed CLI entry points: **passed**;
- Step 7A exact-commit changelog-path discovery live proof: **passed**;
- Step 5 interval/changelog live proof after credential-contamination diagnosis: **passed**.

Primary evidence:

- [`working-memory/2026-08-04_B2-source-structure-reconciliation-final-acceptance.md`](working-memory/2026-08-04_B2-source-structure-reconciliation-final-acceptance.md)
- [`working-memory/2026-08-04_REPO-GOV_post-reconciliation-artifact-routing-alignment.md`](working-memory/2026-08-04_REPO-GOV_post-reconciliation-artifact-routing-alignment.md)
- [`working-memory/2026-08-04_B2-source-reconciliation-major-tranche-import-failure-and-corrections.md`](working-memory/2026-08-04_B2-source-reconciliation-major-tranche-import-failure-and-corrections.md)

Detailed source topology, migration history, test output, experiment scores, and incident narratives belong to those evidence records, source/tests, and accepted ADRs rather than this live continuation file.

## Retained Step 6 decision fact

The bounded local extractor was adopted for one narrow responsibility after the frozen evaluation gate:

```text
admitted crossed-release source text
→ bounded local candidate extraction
→ deterministic exact-source reconstruction
→ validate_support_drop_candidates(...)
→ grounded support-drop claim or explicit problem
```

Deployment identity and evaluation evidence remain controlled by ADR-0006, `ENVIRONMENT.md`, and the Step 6 working/evaluation records. This memory does not duplicate the full score table or provider configuration.

## Exact continuation

Resume with **Step 7B — deterministic crossed-release Markdown source windows**.

Required responsibility:

```text
trusted crossed-release interval
+ exact tagged changelog
→ exact matching Markdown release sections
→ preserved original lines and offsets
→ complete bounded source window
or explicit unresolved problem
```

Step 7B must remain deterministic and semantic-neutral. Do not begin product model-runtime integration until its deterministic proof obligations pass.

Use the current responsibility-based source architecture from ADR-0007. Do not recreate deleted flat compatibility paths or scaffold later Step 7 modules before their increment starts.

## Material blockers and caveats

No product blocker currently prevents Step 7B.

Environment, credential, and security facts must be obtained from `ENVIRONMENT.md` and `SECURITY.md` when they become relevant. In particular, historical ambient `GITHUB_TOKEN` contamination is an environment/security concern, not a reason to duplicate credential state here unless it blocks the selected continuation.

## Learning state

Current demonstrated depth is best described as **substantial implementation exposure with repeated evidence-driven debugging; no formal mastery assessment**.

Recent learning exposure includes:

- responsibility boundaries versus import wiring;
- provider/domain/application/interface ownership;
- compatibility-shim retirement and exact shared-symbol contracts;
- source identity versus evidence authority versus semantic claim state;
- product regression versus experiment regression versus live proof;
- diagnosing broad failures from a shared root cause;
- distinguishing authentication/environment failures from product evidence failures.

Record stronger ownership only after Ali demonstrates it through explanation, modification, testing, diagnosis, or transfer to changed cases.
