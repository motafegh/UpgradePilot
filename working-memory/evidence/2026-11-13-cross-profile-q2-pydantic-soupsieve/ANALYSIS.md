# Q2 — Pydantic/Soup Sieve: Product-behavior and decision-time analysis

**Date:** 2026-11-13. **Review role:** diagnose product capability activation, first causal stops, applicability, usefulness and proposed next research. **Not** a second primary-evidence receipt.
**Verified basis:** [RESULTS.md](RESULTS.md), frozen [pydantic/pydantic PR #13432](https://github.com/pydantic/pydantic/pull/13432), exact head `aa2dc024d33f61cdef50bf1973ab5adf0a974f5a`. Owner-private run card, raw report, source bodies and receipts are retained outside Git. **No feature implementation or automatic second PR run follows from this analysis.**

## What we were trying to learn

UpgradePilot aims to help a maintainer assess an actionable dependency change **before** approval, rejection or deferral. This selected PR was **already merged July 15, 2026**, so it is a deliberately exposed *historical development/diagnostic* case, **not** a contemporaneous decision-time utility test. The later merged outcome is **not** ground truth about upgrade safety or the accuracy of a particular risk claim.

The main reason to choose this case was to exercise a conditional path that **Q1 — CARLA/OpenCV: Normal Dependency and Artifact Investigation** could not: trustworthy upstream repository → tagged source interval → *actual* local language-model invocation → grounded support-drop claim → target declared-Python applicability. It also exposes a much richer CI/runtime contrast than CARLA: GitHub Actions run/job records are available here.

## Causal activation/first-stop matrix

| Product capability | Actual Q2 execution/result | First limitation and impact on usefulness |
| --- | --- | --- |
| Input identity and dependency | Supported: one `uv.lock` Soup Sieve `2.6→2.8.4` change at frozen base/head; exact PR/report match | Successful; proves a lockfile change, not all runtime dependency use |
| GitHub Actions run discovery | Activated: three exact-head `pull_request` runs, of which main CI/codspeed succeeded and third-party tests were skipped | Successful *workflow-level* observation; no automatic changed-package installation guarantee |
| Workflow static analysis and runtime bridge | `ci=supported_not_correlated`; main workflow static changed-dependency consumption supported, selected `lint` matrix strategy not admitted for exact step correlation | `static_job_strategy_unsupported` for matrix-expanded job and unresolved command selectors (`uv_selected_root_workspace_scope_not_exhausted`, `dynamic_runner_platform`); **no truthful step-level success correlation** |
| Available historical job-step data | Independent public API yielded 59 jobs (51 success/8 skipped), **0 returned step records**, including direct selected-job detail | Source/provider observation limits also prevent proving specific completed dependency-use step. Historical absence may be retention/scoping; **not** proof CI never performed steps |
| Runtime dependency state | `no_admitted_candidate` | The current first command-derived proof family requires supported direct-requirements/pip consumption; no such admitted candidate established. Do not infer `soupsieve==2.8.4` was installed/imported from a successful `uv sync` job |
| PyPI release evidence | Two exact files per release, all types and hashes independently matched | Successful acquisition; source distributions/wheels alone do not prove target installation |
| Upstream repository identity | **Available**, `facelessuser/soupsieve`, confirmed against new-version PyPI project link and the **two independently retrievable publisher-provenance bundles** | This passes the trust boundary that stopped Q1 — CARLA/OpenCV. Shows policy functioning on a modern attested release; does not prove whether requiring the same attestation for older releases is optimal |
| Tagged release/changelog interval | **Available**; exact pinned changelog source retained and independently re-fetched byte-for-byte; versions 2.7–2.8.4 crossed | Sufficient authority/source for the admitted *Python support-drop* selection; other kinds of release risk not globally evaluated |
| Local model dispatch/provider | Process-scoped metadata hook recorded one POST send entry and one **HTTP 200** response in the same child; **4,751-byte** serialized request. Gemma `gemma-4-e4b-it-ud` was loaded preflight | Positive conditional integration coverage for this invocation. Does **not** establish general model quality, complete actual request/prompt provenance, response token usage, or all upstream risk semantics |
| Deterministic semantic grounding | **Grounded:** Python 3.8 support removed at upstream version 2.8. Exact quote/offset/tagged source independently matched | Real grounded *one-claim* candidate; not an overall release summary or compatibility verdict |
| Target Python applicability | Pydantic `pyproject.toml` at exact head says `>=3.10`; `python-relevance=outside_declared_python_range` and `python-impact=established_not_applicable` | Correctly **refutes this specific Python-3.8 support-drop overlap**. Does not establish that all Pydantic deployments or all other behavior are compatible |
| Artifact path | `artifact-candidate=not observed`; environment/impact stages not activated | No bounded removed-wheel capability candidate. No proof of every installation path |
| Action and report | Source-backed report saved/reopened correctly, action `abstain` | Responsible nonpromotion. However an exclusively abstaining evaluator cannot yet show a maintainer which affirmative action is permitted, even with a grounded not-applicable finding |
| Original source/reader | Complete 17,370-byte changelog and 41-character quote accessible offline; source target declaration `source-29` reference only; PyPI provenance `source-19` selected facts but `--show-facts` explicitly unsupported | Report is inspectable but **not all original provider bodies or selected-fact families are openable** via the normal viewer; impact on maintainer workflow remains to be tested |

## The two most important causal distinctions

### CI success is not proof that the changed dependency was installed and used

The main CI run `29127613659` returned success. The independent GitHub Actions API still returned **59 job records**, including five successful `Lint 3.x` jobs, but every selected job's `steps` field was empty; a separately queried `Lint 3.10` job also had zero step entries. Exact-head `.github/workflows/ci.yml` includes a matrix and `uv sync` commands. Product evidence correctly distinguishes a successful **run/job** from correlation of a particular workflow source command to the **actual completed runtime step** that consumed the changed dependency.

Two **different** obstacles coexist:
1. *Provider/observation limit*: historical job step detail is absent from current API responses.
2. *Product admitted-proof limit*: the existing bounded source/runtime bridge refuses certain matrix-expanded jobs and cannot exhaust broad `uv` workspace selector scopes or dynamic platforms.

Neither limit may be rebranded as proof that no test ran. To determine **whether the product should expand its CI correlation**, first use a fresh open/actionable case with still-retained run/job/step execution and known dependency consumption, then compare the first failure against exact source and observed runtime. The old Q2 result alone cannot isolate how much the product limit matters if step data is already missing.

### Model invocation, grounded risk and target decision have different meanings

Observed POST/HTTP 200 proves this process reached the provider and received an HTTP response. The saved result and independent changelog check establish a **grounded candidate**, and the exact target declaration establishes that **Python 3.8 was already outside Pydantic's declared supported range**.

So the response to this support-drop question is **not applicable to the represented target Python range**, not “Soup Sieve updates are universally safe.” An unexamined behavioral incompatibility or runtime consumption gap remains outside that claim. The current evaluator deliberately returns `abstain`. That is a correct current-policy outcome **and** shows why separate maintainer-usefulness research is necessary.

## Cross-case understanding

| Aspect | Q1 — CARLA/OpenCV: Normal Dependency and Artifact Investigation | Q2 — Pydantic/Soup Sieve: Normal Investigation with Conditional Local Language Model |
| --- | --- | --- |
| Decision-time role | Closed, unmerged historical PR | Closed, merged historical PR |
| Main case strength | Independently reproduced wheel/tag capability changes | Independently grounded versioned Python support-drop and target nonoverlap |
| CI evidence | Exact-head run query returned zero; two workflow definitions + Jenkinsfile still exist | Three exact-head runs and job statuses remain; no step detail or safe installed-dependency correlation |
| Upstream trust | Project URL present, required file publisher attestation unavailable | Publisher attestation actually available for both new files; upstream authority established |
| Local model | Upstream prerequisite stopped path; dispatch not measured | One observed request boundary + one HTTP 200; grounded claim |
| Maintainer action | `abstain` | `abstain` |
| What neither establishes | General reliability or active maintainer usefulness | General reliability or active maintainer usefulness |

This contrast makes the **upstream provenance gate and target evidence** concrete. The existence of GitHub project metadata does not equal the stronger publisher-authenticated repository identity. The stronger policy is defensible for trust, but its impact on older releases needs a threat-modelled alternative if users routinely hit it. Do not relax it merely to increase LLM-call count.

## Evidence-backed research hypotheses, not approved Builds

| Candidate | Specific question and why it matters | Falsifying / next test | Current priority |
| --- | --- | --- | --- |
| **H1 — Current actionable CI/runtime example** | Are matrix and `uv` workspace constraints materially blocking UpgradePilot on fresh PRs **where job steps still exist**? | Screen a small transparent set of *open* dependency PRs with exact-head run/job/step and supported consumers; freeze an approved candidate, run normal CLI once and contrast actual first stop | **High** — closes an important unqualified current-use workflow |
| **H2 — Maintainer usefulness/action permission** | Does an accurate `abstain` plus nuanced non-applicability enable a concrete maintainer next step, or is a decision-guidance/consumer layer missing? | Decision-focused blinded contrasting maintainer task on current real evidence, with allowed actions/ownership explicitly separated | **High** — product mission, separate from correctness |
| **H3 — Matrix/uv workflow coverage** | Can direct code-owner analysis safely correlate bounded matrix-expanded `uv sync` with an actual step without inventing dependency version/install proof? | Target-owned fixtures with exact job identity, source scope and real step evidence; only if H1 exposes a concrete gap | **Conditional** — don't Build from missing historical steps |
| **H4 — Evidence/source retention and viewer parity** | Are reference-only target declarations and unopenable publisher `selected_facts` obstacles for maintainers who inspect a JSON report offline? | Run a targeted report-reader/maintainer inspection task comparing originals versus retained source facts | **Medium** — consumer-oriented bounded gap |
| **H5 — Inference reproducibility** | Does the report preserve enough model identity, prompt/config hash, request/response usage and exact source selection to distinguish later local-model behaviors? | Compare the existing report limits to a minimal non-sensitive metadata receipt/adapter owner design; test identical vs changed model/config without raw prompt leakage | **Medium** — provenance rather than more model requests |
| **H6 — Old releases and publisher provenance** | Are legitimate historical upstream intervals systematically blocked by mandatory publisher attestations, and can a different, explicitly lower-trust status help without weakening authoritative claims? | Matched old/new package cohort, mismatched URL/attestation adversarial controls, trust impact and downstream semantics review | **Conditional research**, no automatic relaxation |

The next authorization should **not** be “fix the first red CI status” or “build a more capable model.” It should use the cross-profile activation matrix and an active decision-time evidence gap to choose one bounded investigation or useful product feature.

## Learning ownership and stop

**Confirmed in this case:** real installed public CLI; exact PR/version; provider-supported upstream identity; tagged source and one grounded support-drop; actual local HTTP response; correct Python declaration nonoverlap; preserved report; run/job observations with deliberate correlation restraint.

**Unproven:** safe overall upgrade, dependency import in target CI, actual job steps, arbitrary active PR performance, all releases/semantic risks, non-abstain action permission and representative usefulness.

**Learning question:** If GitHub reports a successful CI run for Pydantic and the model correctly concludes the Python 3.8 drop is irrelevant to Pydantic's declared Python range, why must UpgradePilot still **not** claim that the full Soup Sieve upgrade has been validated?

**Status:** Q2 — Pydantic/Soup Sieve case is evidence-verified and analyzed; owner learning check/priority decision pending. No target code execution or changed product algorithms; no new active-PR run automatically started.
