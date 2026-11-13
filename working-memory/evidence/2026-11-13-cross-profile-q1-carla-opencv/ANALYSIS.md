# Q1 — CARLA/OpenCV: Product-behavior and decision-time analysis

**Date:** 2026-11-13. **Status:** Reviewed diagnostic analysis; no product change or new CLI run.
**Case:** [carla-simulator/scenario_runner pull request #1111](https://github.com/carla-simulator/scenario_runner/pull/1111), `opencv-python==4.2.0.32 → 4.8.1.78`. Exact head `f32ad2d23a9abee47c566dfbed2b822d953a09e2`; base `7758d066080f180f8296887ed89b7c723a54706a`. Closed, unmerged when rechecked.
**Evidence verification owner:** [RESULTS.md](RESULTS.md). **Cycle:** [active Learning-by-Doing record](../../2026-11-12_cross-profile_e2e_qualification_execution_lbd-cycle.md). This analysis is **not a second evidence receipt**: it diagnoses the reasons for activation/absence, consumer usefulness and future decision questions. Underlying raw original outputs remain private.

## Case role and decision-time relevance

**Role:** exposed historical development/diagnostic case for one current installed normal public-CLI invocation. **Not** an active maintainer decision or a sample of the product's future open-PR workload. Closed/unmerged status is context, **not proof** of upgrade unsafety, lack of past tests or a ground-truth recommendation.

The intended product goal is to assist a maintainer **before** an upgrade decision using evidence available at that decision time. A historical replay may qualify individual mechanisms, nonactivation and offline recovery, but historical evidence availability may differ from the original decision time; the original decision-time environment must not be retroactively invented. For future decision-time cases, prioritize open/actionable PRs with captured exact-head runs, jobs and relevant dependency consumption; freeze evidence before its retention or PR state changes. Record candidate-selection failures and do not call a preselected success case representative reliability.

## Activation and causal-stop inventory

| Capability | What the real Q1 report / independent evidence established | Why that branch did not go further | Diagnostic ownership / question |
| --- | --- | --- | --- |
| PR/dependency acquisition | Exact base/head and changed `requirements.txt` version transition matched independent API facts | Activated successfully | `dependency.change`; supported |
| GitHub Actions acquisition and CI correlation | Report `ci=no_successful_ci`, `reason=no_exact_head_workflows`; separate exact-head runs query returned 0 | No **observable exact-head Actions run/job/step instances** for the queried API scope; no actual step correlation or test outcome could be established | `ci.dependency_exercise` and `github.actions`; distinguish unavailable execution from absent workflow definitions |
| Native command-derived runtime dependency state | `runtime=no_admitted_candidate` | No supported direct-requirements/pip consuming job and executed step was available to establish the command-completion proof family | `ci.dependency_state`; not an installation success or failure |
| PyPI package/artifact comparison | Exact inventories independently verified: old 27 wheels, proposed 6 wheels and 1 source distribution; 27 removed/8 added wheel-tag strings | Deterministic published-artifact comparison **executed successfully** | `impact.artifact_serviceability`; cannot infer target installation from tags |
| Target artifact applicability | `artifact-environments=not established`, `artifact-impact=unresolved` | No admitted target environment association or runtime installation result | Target/workflow environment owners; could be investigated separately, not assumed |
| Upstream repository identity | `upstream-repository=source_unavailable`; PyPI metadata contains `Homepage: https://github.com/opencv/opencv-python` | Product policy requires **both** accepted project-link identity and file publisher provenance corroborating it. None of the exact release files yielded usable PyPI publisher provenance for the resolver. Two separately checked Integrity API endpoints (one wheel and the source distribution) returned 404, consistent with but not exhaustive proof of all per-file results | `upstream.repository` / `pypi.provenance`; evaluate whether strong mandatory corroboration is proportionate to historical release coverage |
| Upstream tagged release interval and changelog | `upstream-interval=not established` | Upstream repository authority prerequisite failed; no authoritative interval admitted | `upstream.interval`; **not** evidence that OpenCV had no changelog or release |
| Local language-model support-drop extraction and grounding | `support-drop=not evaluated`; target Python branch not activated | No authoritative source interval to supply to the conditional support-drop evaluator; model stage **not reached under inspected control flow** | `upstream.claim` + local model adapter; no same-invocation POST instrumentation was installed, therefore actual model request count = **not measured**, not observed zero |
| Maintainer action | `abstain` | Missing target/CI applicability evidence and current non-abstention admission rules | `maintainer_action`; correct conservatism does **not** establish useful decision guidance or positive action capability |
| Durable original evidence | Saved JSON and selected-facts view reopened, PR original text retained; changed requirement source reference-only; original PyPI response bodies not retained by the normal report | Consumer can inspect supported facts and preserved PR description, but cannot reconstruct every original observation offline from JSON alone | `report` and `source-retention`; ask whether a maintainer needs retained original inputs in normal reports |

### Important new independent CI-configuration finding

An exact-head **Git tree** read returned 477 entries (`truncated=false`). This revision **contains**:
- `.github/workflows/static_code_check.yml` (3,030 bytes; SHA-256 `19db4f39e49c5181e5828e2705cd07dbb3d82fd1ffcc9490dd57053c0413a55d`)
- `.github/workflows/unit_test.yml` (734 bytes; SHA-256 `de153331f6532459ffa54c5535abad76093c08fa7c02d4265abc076a3d998f87`)
- `Jenkinsfile` (7,316 bytes; SHA-256 `d31e7c165b35b2afec8e00a69ef8a8ca16e711e57fe00e4467ea59242a86f9bf`)

Both GitHub Actions workflow definitions declare `pull_request` triggers on `master`. The independent exact-head API query still returned **zero GitHub Actions workflow-run records**. Saved read-only configuration receipt SHA-256 `ede4a049d9ae9a92b85f050046a44f213d683e1c9e6c526866871c335a5c13c3` links exact-head definitions and the previous query. The private receipt/files are outside Git; exact sources are addressable by pinned GitHub commit + path.

**Interpretation:** `no_exact_head_workflows` accurately reports a lack of acquired *runtime observations* for the supported GitHub Actions scope; it must **not** be paraphrased as “the repository has no CI configuration,” “no CI ever ran,” “Jenkins ran successfully,” or “the upgrade passed CI.” Whether the GitHub Actions run information was never generated, was pruned, occurred under a different event/head, or is inaccessible remains **unresolved**. Jenkins is visible only as a repository configuration, not observed Jenkins job execution. Static workflow orientation without live runs is a possible new product capability; it must be separately threat-modeled and scoped, not silently equated to existing runtime correlation.

## Product usefulness versus correct refusal

A maintainer can learn that the release files and supported wheel tags changed and that the available evidence does **not** establish the specific target's compatibility. This supports **investigation planning**, but the current report does not give an evidence-backed environment-specific upgrade disposition, an observed test result or a supported non-abstain action. It is therefore a **case-specific partial diagnostic success**, **not** a demonstrated decision-ready recommendation.

Correctly classifying unavailable evidence and stopping the local model is desirable under current rules; it does not settle whether the rules are ideal for the product's intended use. A source problem may be a legitimate safety constraint **and** a coverage/usability limitation at once. Do not optimize only for increasing model-call or green-report rates.

## Focused opportunity/hypothesis ledger (not approved implementation)

| Candidate question | Why it matters | What evidence/test would decide it | Current disposition |
| --- | --- | --- | --- |
| **H1 — Active decision-time relevance** | A historical, closed PR does not demonstrate utility when maintainers still have a choice and live CI is available | An open/actionable PR sampled and frozen at an explicit observation time, with exposed CI evidence and a maintainer task | **Test-selection/process gap.** Prioritize an active run-bearing case in the next contrasting cohort without discarding historical development fixtures |
| **H2 — CI static orientation with no runs** | The exact head contains two Actions workflows and Jenkinsfile, but normal report says only `no_exact_head_workflows` | Read-only workflow owner analysis, intended trigger/consumption checks and a user-facing consumer task; never imply that static YAML executed | **Potential product/report usefulness improvement.** No design or implementation yet |
| **H3 — Upstream authority proportionality** | Mandatory publisher corroboration may block older releases that have an obvious PyPI-linked GitHub project | Compare legitimate modern/historical PyPI packages with and without supported attestations, spoofed/mismatched project URLs and an explicit lower-trust classification alternative | **Security/coverage trade-off to research**, not authorization to relax the trust boundary |
| **H4 — Normal-profile evidence durability** | JSON saves selected PyPI facts but not raw provider bodies/changed file; later independent corroboration adds time/cost and cannot substitute for same-invocation originals | Consumer replay/maintainer inspection exercise comparing retained excerpt/facts with bounded original-source retention | **Possible retention/UX improvement**, defer to cross-profile review |
| **H5 — Conditional model coverage** | No model source interval admitted and model dispatch not measured | Q2 — Pydantic/Soup Sieve: Normal Investigation with Conditional Local Language Model, with exact same-invocation provider dispatch and grounding | **Pending targeted live qualification**, not a defect established by CARLA |
| **H6 — Broader CI providers** | A Jenkinsfile exists at this head; GitHub Actions alone may not cover every target's CI | Inventory actual supported providers and representative maintainers; require legitimate job provenance before any causality claim | **Out-of-scope potential product expansion**, not immediately required |

**Prioritization:** complete the selected **Q2 — Pydantic/Soup Sieve: Normal Investigation with Conditional Local Language Model** after its own freeze/authorization; then choose a **live, actionable exact-head CI case** if the matrix still lacks normal-route CI/runtime coverage. Keep H2/H3 as explicit design hypotheses for an evidence-based future decision; do not enlarge the current run merely to chase every idea.

## Lessons and follow-up gate

1. “Observed source absence” means no admissible **observed** runtime event, not that no static CI configuration exists.
2. “Correct safeguard” must be reviewed for the mission it serves. An upstream policy can be simultaneously well-defended and excessively restrictive for legitimate older packages.
3. “One normal CLI run completed” means only activated branches were observed; success of one branch cannot promote untested source, model or CI capabilities.
4. Historical case usefulness for debugging and real-time case usefulness for active maintainer decisions are separate proof claims.
5. A case-specific behavior analysis should be written **before** closure, not only when the user notices missing activation.

**Learning/owner check:** Could a maintainer responsibly conclude from the CARLA/OpenCV report that the upgrade had *no CI configured*, or only that **no exact-head CI execution evidence was acquired**? Why does the pinned workflow-tree observation change the appropriate explanation?

**Next stage:** update the controlling plan with a required post-run causal/decision-time analysis and screen future cases for active decision status and actually available exact-head evidence. Continue the single Learning-by-Doing cycle; do not start Q2 model execution or authorize a feature build as a result of this diagnostic record alone.
