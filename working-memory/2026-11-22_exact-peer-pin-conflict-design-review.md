# Exact peer-pin conflict design review

- **Date:** 2026-11-22
- **Product revision inspected:** `86681c60af0d7ce412abda8cce3ef746fff8b82b`
- **Outcome:** retained-case comparison verified. Advance the design to a bounded acquisition proof before implementation.

- UP-SKILL:upgradepilot-planning-design
- UP-SKILL:upgradepilot-working-memory

Ali requested execution and recording for this audit follow-up and moved learning to a separate workstream. That replaces the normal Learning-by-Doing gates for this review. Project owners, evidence rules, and the product implementation boundary still apply. The selected responsibility was design and offline examination. No target, resolver, or model was executed.

## Decision and maintainer task

For a failed CI step that consumes a changed exact requirements pin, can an ordinary investigation identify a concrete, source-backed declared conflict that directs the maintainer to a narrower check? Use ApplyPilot #8 as exposed development evidence. Compare the actual ordinary report with an analyst sketch over the same retained review packet. The analyst knew the outcome. This qualifies neither independent maintainer usefulness nor normal automatic acquisition.

The [next-check review](2026-11-21_maintainer-next-check-review_lbd-cycle.md), [Q4 dependency research](evidence/2026-11-14-cross-profile-q4-applypilot/DEPENDENCY_CONSTRAINT_RESEARCH_NOTES.md), [whole-project audit](../audits/2026-11-21_AUDIT-016_whole-project-product-and-design.md), [product direction](../plans/PRODUCT_DIRECTION_AND_MAINTAINER_UTILITY_INVESTIGATION_PLAN.md#5-owner-reconciliation-and-decision-gate), and [usefulness plan](../plans/MAINTAINER_REPORT_PRESERVATION_AND_USEFULNESS_EVALUATION_PLAN.md#5-independent-usefulness-evaluation) establish the question and proof boundary.

| View | Supported answer | Remaining evidence needed |
|---|---|---|
| Current ordinary report, opened from the corrected November 21 retained CI replay | The exact API job's step 4, `python -m pip install -r requirements-lock.txt ruff==0.17.4`, completed with failure. Report action is `abstain`. The report contains no Playwright evidence. | Recover the install output to establish what the command reported when it failed. |
| Analyst sketch augmented with retained target and registry evidence | The selected requirements file pins both Playwright 1.64.1 and pyee 16.0.1. The retained PyPI release metadata for Playwright 1.64.1 declares `pyee>=13,<15`. The two declared pins conflict under that metadata. | In any recovered output, check whether pip actually applied that constraint and reported it as the failure. The historical anonymous log request returned 403. |

The second view supplies a package pair and a predicate the maintainer can inspect. The exact CI exit cause, effective index and artifact selection, installed behavior, and whole-environment resolution remain unresolved. The product action stays `abstain`. The added proposition comes from new evidence, so a presentation change or an LLM given only the existing report cannot supply it faithfully.

## Evidence and controls

- [S017 case manifest](../product-simulation/scenarios/S017-applypilot-pyee-lockfile-conflict/CASE_EVIDENCE.json) binds ApplyPilot PR #8, base `4996efaa87cb93289d2da899f306d779a84687f0`, head `3009f89f0d4f58fcc588647a5c33f3a8e95bf05f`, run `43073710410`, attempt 1 and job `130708096164`. The retained changed-files response shows one changed file, `services/api/requirements-lock.txt`, with one replacement, `pyee==14.0.0` → `pyee==16.0.1`.
- The baseline is the corrected CI replay from the [November 21 installed acceptance](evidence/2026-11-21-matrix-final-acceptance/RESULTS.md), report SHA-256 `189313e90a01814a5569c34de3f57c1ac68057c0d7955342efed3045f2a3320e`. Reopened with the current report reader and renderer and checked selected CI facts for the job identity and failed step. That replay used controlled release inputs. The [November 14 live capture](evidence/2026-11-14-cross-profile-q4-applypilot/RESULTS.md) owns the original live acquisition evidence and its earlier CI summary wording.
- The retained target archive yielded the head members under `applypilot-3009f89f0d4f58fcc588647a5c33f3a8e95bf05f/services/api/`. Archive SHA-256 calculated during this review is `ae29da42abcf227195dd240565fc19d8d398a074b0136bc6be317eb10a917dab`. The lock member matched the independently retained lockfile bytes and case manifest SHA-256 `02bc0a64c433d02f5bfd44e7af46089e5b6e692e90aa05ee548cfce61d344600`. Playwright and pyee are pinned on lines 38 and 45. The direct manifest member SHA-256 is `0afb27301d8680dae081a444906d3862dff34fb160b76bb7ad3d7b13981abbc0`. It declares `playwright>=1.49,<2` at line 20 and describes its relationship to the lock in its header. The lock header also names this direct file. These headers are target-authored selection evidence. The archive and direct manifest digests were measured here and have no independent byte-level receipt in the case manifest.
- The manifest records the Playwright 1.64.1 release JSON SHA-256 `eee88ef1964912c0a159a5eedb282af27ec0b82dd44626c3254849ed28c1f489`. The independent Q4 copy, SHA-256 `d5888a7b2b5979f2ac36902083370ca02eca0de5458664c593a3944906b67bee`, has the same canonical name, exact version, and unconditional `pyee<15,>=13` declaration. Both retained pyee release records declare only `typing-extensions` in `Requires-Dist`. Those forward dependencies do not identify Playwright.
- Offline checks ran in an isolated network namespace. The candidate calculation parsed the non-comment lines in the two simple retained requirements files with `packaging.Requirement`, grouped by canonical package name, and joined simple unique direct roots to simple unique exact lock pins, excluding pyee. The compatibility control used `SpecifierSet.contains` over the parsed Playwright requirement. This checks the proposed predicate and case selection, without exercising automated fetching, orchestration, product report projection, or general requirements-file parsing.

| Matched control | Observed outcome |
|---|---|
| Head pin, `pyee==16.0.1`, with the exact Playwright declaration | Conflict for the named requirement |
| Old pin, `pyee==14.0.0`, with that same declaration | Matches the named requirement |
| Head pin with peer metadata withheld in the diagnostic | Unresolved |

## Candidate selection and ownership

| Approach | What ApplyPilot establishes | Trade-off |
|---|---|---|
| Read only the changed distribution's metadata | Two pyee records reveal no Playwright dependency edge. | Existing ordinary acquisition cannot recover this reverse relationship from those records. |
| Ask for an exact peer from the operator | One exact metadata lookup can verify Playwright once nominated. | Useful for checking an existing suspicion. Discovery depends on the operator supplying the peer. |
| Scan every other exact co-pin | 59 candidate names in the selected requirements file. | Broader within this one file. Worst-case exact release reads grow with the full flat lock. Includes transitive candidates. |
| Join declared direct roots to exact CI-selected co-pins | 19 declared roots, 17 eligible peers. Playwright is eighth in canonical-name order. The two roots excluded by the simple first shape use extras. | Smaller candidate set. Transitive peers, extra-dependent or marked cases, and missing or ambiguous companion manifests limit coverage. |

Prefer the direct-root join for the next design proof. Bind the requirements file to the consuming command, work directory and head via the existing ordinary target evidence. Admit at most one exact-head, same-scope direct-declaration companion through a documented, reproducible rule. This case supports testing the same-directory companion hint plus reciprocal file references. Qualify how the rule handles coincidental file names, contradictory references, and a companion proven to belong to another scope. The companion only nominates candidates. Both exact pins in the CI-selected file and the identified peer release metadata are the evidence for the declared conflict.

For the first proof, restrict the eligible form to unique, unconditional, plain registry pins and peer edges. Keep includes, constraints, direct URLs, extras, markers, and effective package-index ambiguity visible as limits wherever they affect applicability. Missing or malformed release metadata leaves the candidate unresolved. If the selected file has unsupported syntax or conflicting pin records that could invalidate the comparison, stop the affected inference. An eligible successful comparison establishes a result only for the named peer edge. Even a fully scanned in-scope group cannot certify global consistency.

The acquisition bound to test is two exact-head file reads when neither file is already available, plus at most 20 version-scoped release reads before retries. This is a proof budget, proposed from the observed 17 candidates. It is not a permanent default, a measured latency, or a recommendation to process an arbitrary prefix when the set exceeds the cap. Above the cap, record incomplete coverage. Use deterministic order for reproducible receipt and deduplicate existing inputs. Record request counts, bytes, unavailable premises, and time in the proof.

[Dependency analysis](../src/upgradepilot/dependency/analysis.py) already creates the exact requirements source context. [GitHub repository acquisition](../src/upgradepilot/github/repository.py) owns exact-head file access. [Ordinary PyPI release acquisition](../src/upgradepilot/pypi/release.py) owns ordinary release facts. [Caller-signature acquisition](../src/upgradepilot/caller_signature/source_acquisition.py) already has an exact-release `Requires-Dist` parser whose marker, locator, and gap handling is relevant. If the route is admitted, evaluate sharing the provider parsing under the PyPI owner. The opt-in profile's types and graph are scoped to that profile. The ordinary report should receive the resulting typed evidence with identities, file and line locators, raw requirement, release metadata locator and coverage limits. The [product decision model](../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md) continues to own the distinction between declared facts, applicability and maintainer action. Exact-pin evidence for this pip requirements shape needs no `uv` reachability inference.

## Entry proof for a Build decision

Write a bounded acquisition comparison before product implementation. Freeze the companion admission rule, scope, request and retry limits, and control outcomes before examining the comparison cases. Use ApplyPilot as the known positive and select at least one separate retained target or genuine contrasting layout. Exercise a missing or ambiguous companion, a budget refusal, and the compatible and missing-metadata controls. Use the same evidence access for the current-report, operator-selected peer, and automatic nomination comparisons. Record whether each approach identifies a specific next observation, how many sources it needs, and whether it withholds claims when evidence is insufficient. Report when known coverage would miss a transitive peer. A separate set of cases and independent reviewers would be needed to claim usefulness.

Advance to a bounded implementation design only if the acquisition proof demonstrates defensible selection, correct refusal, and an acceptable measured request cost under the selected operating budget. If the automatic rule cannot be justified for real layouts, reconsider the explicit-peer diagnostic or preserve the finding as case research. AI remains a later comparison for explaining already verified findings against a concise deterministic presentation.
