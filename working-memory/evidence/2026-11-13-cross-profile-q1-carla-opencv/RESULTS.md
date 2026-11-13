# Q1 — CARLA/OpenCV: Normal Dependency and Artifact Investigation

**Live case date:** 2026-11-13 (UTC).
**Disposition:** **One real installed-CLI investigation completed successfully.** Exact input, published artifact facts, rendering and supported unknown states were independently checked. This is an **exposed, deterministic, non-random case**, not proof of global reliability or complete activation of all product branches.
**Controlling plan:** [Cross-profile real-PR end-to-end qualification](../../../plans/CROSS_PROFILE_REAL_PR_END_TO_END_QUALIFICATION_EXECUTION_PLAN.md).
**Cycle:** [Cross-profile Learning-by-Doing record](../../2026-11-12_cross-profile_e2e_qualification_execution_lbd-cycle.md).

## Frozen input and execution

- Public PR: [carla-simulator/scenario_runner#1111](https://github.com/carla-simulator/scenario_runner/pull/1111), Dependabot `opencv-python 4.2.0.32 → 4.8.1.78` in `requirements.txt`, **closed and not merged**.
- Exact base `7758d066080f180f8296887ed89b7c723a54706a`; exact head `f32ad2d23a9abee47c566dfbed2b822d953a09e2`. The independent preflight found one changed file and verified the patch's version transition. Saved report identity **matches both frozen SHAs**, repository and version pair.
- Product installation: isolated, verified wheel from source `50f94fec713077122a8791e5e6f1495307fbf22a`; local runner/tooling main was `723afd7fe311dabacc8699473fecbb9893d0c5ec`. No product `src/` changes intervened. Wheel SHA-256 `190257ec38328a340cf2132513e09432c8f594af4c51da218bfad81cfca420ca`. The verified installed public CLI was invoked **exactly once**, with `--github-auth anonymous`, process-local direct GitHub routing and PyPI via the existing proxy. No target code execution or external mutation.
- Supervisor parent deadline: **150 seconds**; observed successful exit `0` in **12.500796 seconds**, reported as a local process observation rather than a general throughput metric.
- Saved report: **79,202 bytes**, SHA-256 `1bc63fa585ce1a543a3b4e4ee411e8589ba1e27d9eddf978ebe6d4c9bad680f8`. Private frozen card SHA-256 `9ca7d1b5688c74e91b3357336cfc7e64b7b94a74b022fa7a684076187af7869c`.
- The run receipt expressly records physical request counts and local-model POST attribution as **not measured**. The GitHub/API and PyPI preflight and subsequent independent corroboration use **separate request horizons**. Planning targets (e.g., 32 HTTP GETs) are not claimed to be enforced/global limits. Raw reports/source JSON and command receipts remain owner-private, outside the repository; they were **not automatically published**.

## Independently checked product evidence

| Product observation | Source / independent verification | Exact conclusion |
| --- | --- | --- |
| Exact dependency transition | Report dependency assessment; separate GitHub PR and changed-file API reads | **Supported:** one `requirements.txt` change from `opencv-python==4.2.0.32` to `opencv-python==4.8.1.78` at the frozen base/head |
| Proposed and old package inventories | Exact published PyPI release JSON independently reacquired after the CLI run; compared every file by **filename → (package type, SHA-256)** against report `source-6` and `source-8` | Old version: **27 wheels**, no source distribution. Proposed version: **6 wheels plus 1 source distribution**. All file identities and reported distribution counts matched |
| Wheel-tag capability changes | Independent `packaging.utils.parse_wheel_filename` tag-set comparison against report `source-13` | **27 removed** and **8 added** tag strings, matching the report. This is a *published-artifact candidate*, not proven target install failure |
| CI status | Report `ci=no_successful_ci`; independent GitHub Actions runs query for **exact head SHA** returned `total_count=0` | No exact-head workflow runs **in the queried API scope**. No successful proposed-version CI execution can be inferred |
| Runtime state | Report `runtime=no_admitted_candidate` | No admitted direct-requirements/pip command-completion proof; not an observed successful or failing target installation |
| Upstream semantic branch | Report `upstream-repository=source_unavailable`, `upstream-interval=not established`, `support-drop=not evaluated`, `target-python=not activated`, `python-relevance=not evaluated` | Honest prerequisite stop. **Model dispatch was not instrumented**, so this cannot be counted as an observed local-model activation or a proven zero model calls |
| Artifact applicability and decision | `artifact-environments=not established`, `artifact-impact=unresolved`, maintainer `action=abstain` | No target environment association establishes compatibility or incompatibility; no stronger maintainer action authorized |

The independent PyPI snapshots contained **36,671 bytes** for the old version and **26,429 bytes** for the proposed version. Original provider JSON was *not retained by the normal report* (its package sources have `selected_facts` retention); the independently fetched originals were retained privately with their own timestamps and digests. Independent artifact-check receipt SHA-256: `18a613de8b8abf337cae308da208f8255c99463fc78d659b8abfc47616256268`. Independent exact-head GitHub Actions query response SHA-256: `52d589da93373d1efadfa660185a0970a1b2320703a8b87d6ed693946661e1cd`.

**Verification-method correction:** The first after-run PyPI comparison made an invalid assumption that provider file-list order would match report `file_N` order. It stopped at an old-version item. The method was corrected to compare exact filename/type/digest identities and independently calculated tag sets; those checks passed. This was a verifier ordering error, **not** a detected UpgradePilot source error. No live product rerun or report editing occurred.

## Offline report and retention inspection

- The installed public CLI reopened the saved full JSON with exit `0`. The live and offline rendered report share **identical substantive lines**. Two expected presentation differences were confirmed: the mode label (`new investigation report` versus `saved report; no live refresh`) and the live-only `Saved report:` path footer.
- `--show-facts source-13` returned the selected artifact capability facts with exit `0`. `--show-source source-1` returned the retained original PR-description text with exit `0`.
- `--show-source source-2` correctly refused with exit `7`: **“This source has no retained original text.”** The original changed requirements file is a reference, not offline-retained text. This explicit boundary is part of correct evidence preservation, not a missing proof that can be silently filled from the source reference.
- Exactly **18 sources** were recorded: **1 retained original-text source**, **1 reference-only source**, **3 selected-facts sources** and **13 producer-result sources**. Producer-result descriptions do not substitute for raw original input.
- Private verification receipt SHA-256: `1546d3d522b756d6be2e051a28da0205fd2e65c27762491f8d8892258e53200b`.

## Qualification scope and continuation

**Qualified for this exact case:** properly installed public CLI executed real GitHub/PyPI acquisitions, preserved the correct frozen PR transition, produced a saved report, reported defensible artifact capability differences and uncertainty, and reopened verified original excerpts/selected facts offline. Claim is case-specific.

**Not established:** aggregate request/body budgets; same-invocation model dispatch count; complete CI/runtime test coverage; supported target installation or import identity; an upgrade counterfactual; broad correctness/reliability; independent human usefulness; all available branches or a non-`abstain` action. The normal public CLI still does **not** admit externally frozen expected base/head SHAs before its first request; independent preflight plus after-report identity checks qualify the delivered **case**, not an early expected-SHA guard.

**Next:** perform evidence-based D learning/ownership for this actual result and preserve this Q1 result. Only afterward separately freeze and admit **Q2 — Pydantic/Soup Sieve: Normal Investigation with Conditional Local Language Model** (current exact PR identity, model service readiness, trustworthy same-invocation model POST attribution and its own limits). **Q3 — AV-Tracer/HTTPX: Combined Source and Historical CI Investigation** stays the historical qualified reference. Do not turn this single success into general reliability, or start the model investigation by implication.
