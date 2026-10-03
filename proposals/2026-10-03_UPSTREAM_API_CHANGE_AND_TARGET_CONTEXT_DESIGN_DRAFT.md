# Upstream API changes and target context — design draft

**Proposal status:** Partially promoted design evidence. Source-association invariants/method are now owned by [Core §6.3](../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md#63-source-association-bases-and-permitted-effects) and [ADR-0011](../docs/architecture/ADR-0011-explicit-source-association-bases-and-proposal-boundary.md); the [feasibility plan](../plans/UPSTREAM_API_CHANGE_AND_TARGET_EXPOSURE_FEASIBILITY_PLAN.md) owns execution/proof. API semantic-role adoption and product integration remain unproven. This proposal retains comparison/rationale without competing with those owners.
**Responsibility:** Make ordinary upstream changes and exact target relationships inspectable enough to formulate honest technical-impact candidates through the normal public-PR investigation.
**Dated basis:** [three-case product check](../working-memory/evidence/2026-10-03-report-development-case-check/README.md) and [source-association feasibility evidence](../working-memory/evidence/2026-10-03-api-impact-design/README.md). These are known development pressures, not independent or unseen evaluation.
**Authority:** [Charter](../PROJECT_CHARTER.md), [Core](../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md), [Product Decision Model](../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md), [Minimum Useful Generality](../docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md) and [Security](../SECURITY.md) remain controlling. Live selection belongs only in [MEMORY.md](../MEMORY.md).

## 1. Product responsibility and problem

UpgradePilot's owning responsibility is dependency-update technical-impact investigation, including release changes, target usage and dependency relationships, activation/environment conditions, relevant evidence, uncertainty and eventual justified maintainer support. A report needs useful findings; faithful serialization cannot supply missing investigation knowledge.

The normal HTTPX `0.27.2 → 0.28.1` case demonstrates three separate missing premises:

1. Package-to-upstream association stops because the current resolver requires usable PyPI publisher provenance.
2. The only adopted release-language interpreter recognizes explicit Python support drops. Successful repository resolution would not make it an API interpreter.
3. Target imports, adapter code and version/resolution relationships are not acquired/evaluated by a normally reachable API-impact path.

The first trial should exercise explicit API call-contract changes and target exposure, with argument removal as an initial proof category. This category is a test slice, not a permanent product ceiling or one handcrafted interpreter per change class. Broader behavior/serialization/plugin effects and artifact/environment analysis remain part of the product horizon, with distinct proof. They must appear as unsupported or unassessed observations when encountered rather than silently disappear.

## 2. Established implementation facts and design questions

`UpstreamRepositoryResolver` in [upstream/repository.py](../src/upgradepilot/upstream/repository.py) reconciles package project links with PyPI-reported publisher identities; [test_upstream_source.py](../tests/test_upstream_source.py) deliberately rejects a homepage-only association. This contract must not be weakened by feeding another evidence basis into `UpstreamRepositoryEvidence`.

[ADR-0006](../docs/architecture/ADR-0006-bounded-local-support-drop-semantic-extractor.md) admits a narrow local support-drop role. Its model/configuration and historical score do not establish API interpretation quality. [upstream/interval.py](../src/upgradepilot/upstream/interval.py) distinguishes source roles and bounded release authority; an exact commit alone does not establish package association or completeness.

The unresolved choices are: which weaker declared associations may support which limited operations; how to gather complete-enough relevant source windows; how to discover target relationships without known-answer paths; and what proposal/validation/evaluation evidence is sufficient before product integration. This draft recommends a method and trial, not acceptance of those choices.

## 3. Proposed evidence flow

```text
exact PR and dependency transition
    ├─ exact package metadata/distribution identity
    │    → explicit package-to-repository association and its basis/problems
    │    → release/tag/commit/file/interval evidence and coverage
    │    → bounded semantic upstream-change proposals + exact source references
    └─ exact target source/configuration inventory, independent of CI-run availability
         → imports/calls, declared dependencies/extras and scoped adapter evidence
         → explicit missing resolved-version/activation/context propositions
                    ↓
       mechanism-specific candidate + supporting/refuting/unknown propositions
                    ↓
       existing applicability semantics, then report projection
```

Observed source facts, proposed meaning, source grounding, independent corroboration, applicability and action permission remain separate. The semantic component cannot assign its own source authority, completeness, compatibility or maintainer action. Acquisition/orchestration owns data access; report rendering does not perform discovery.

## 4. Source identity: two evidence bases, no silent trust upgrade

Retain the current publisher-provenance path. Compare a separately represented declared-source path for releases without that evidence:

| Basis | What it can establish | What it cannot establish |
| --- | --- | --- |
| PyPI-reported publisher association | The registry reports the distribution's publisher repository; preserve exact file/digest/API basis and conflicts. | Local cryptographic signature verification, trustworthy code, semantic truth or compatibility. The current client parses registry-reported identities; do not call it a new local signature verifier. |
| Publisher-declared source association | Exact release metadata/distribution headers declare a source repository; retain package/file identity and declaration scope. | An attested publisher, independent corroboration, or proof the shipped file was built from a resolved repository commit. |
| Tag-resolved commit/file | The retrieved text belongs to a pinned repository/commit/path and named release scope. | Package-to-repository ownership by itself or truth/completeness of release prose. |

PyPI documents attestations as distribution/identity binding, with limits on trust and code safety ([introduction](https://docs.pypi.org/attestations/), [security model](https://docs.pypi.org/attestations/security-model/)). That distinction motivates separate evidence meanings; it does not automatically authorize a weaker route.

The promoted ADR selects identity-validated exact-release registry source declarations and one unambiguous allowed GitHub repository for limited examination. Hash-verified distribution metadata is optional when shipped-metadata consistency or a conflict is material, rather than a mandatory authority prerequisite. Resolve exact tag/commit source and package/release identities separately. Preserve all examined declarations, samples and omissions. These declarations share publisher control; matching them is consistency, not independent validation. A sampled wheel supports its own metadata scope, not unanimity across every distribution of the release. Cross-release moves/renames and disagreement require explicit review states.

Missing provenance may leave a declared association investigable, with its weaker basis visible. A publisher mismatch, malformed identity or conflicting declared source must not be converted into success by falling back. Arbitrary documentation/search results and model-guessed repositories cannot become source authority.

**Proposed permission ceiling for the first trial:** declared associations support read-only source examination and attributed, conditional change/exposure proposals. They do not populate existing stronger authority objects or establish exact package-to-commit build correspondence. Eligibility for an admitted interval/claim contract remains a policy decision to resolve before product implementation. Existing grounded claims cannot receive stronger effects merely because this new route produced a candidate.

## 5. Upstream interpretation and coverage

Build source windows from exact release structure and the old-exclusive/proposed-inclusive interval. Retain covered releases, supplied source IDs/text, excluded context, unparseable structure, truncation and request/context limits. Do not select sentences using the expected answer or keywords such as `app`; do not silently omit a release to fit a prompt.

The fresh HTTPX window includes argument removals, deprecations and behavior changes. The proposed semantic responsibility is to discover attributed change observations from that window, with affected interface, release/time/direction, source references and uncertainty where supported. The first API trial may evaluate only a subset of mechanisms, but unassessed material observations stay visible. Empty candidates are not evidence of no impact.

Use a bounded local LLM as a proposed semantic method, with explicit schema, source-only input, no tools, no policy authority and no automatic correction loop. Reusing the installed model/provider is a pilot baseline, not adoption of the old support-drop score for a new task. Compare appropriate simpler mechanical evidence, such as scoped signature differences, without replacing broad language interpretation with fixture phrases. Deterministic validation checks identity, release membership, real source references/offsets, contradictions and allowed effects; it cannot prove every interpretation's meaning.

## 6. Exact target context and conditional adapter paths

Gather target source/configuration at the selected PR revision without requiring a successful CI run. An absent run limits execution evidence; it does not by itself make static repository files unavailable. Reuse existing providers for bounded exact-commit acquisition rather than introduce a crawler/service.

Candidate inputs include the changed dependency declaration, eligible Python source/test inventory, imports/calls and declared dependency/extra metadata. Record scope, excluded/generated files, syntax failures, dynamic imports/wrappers, truncated trees and file/read limits. Normal discovery must locate relevant relationships; a manually supplied `tests/test_routes.py` answer is not product discovery. AST-derived imports/calls are static facts, not proof of runtime execution or complete call reachability.

For framework-mediated paths, declared requirements constrain possible versions; they do not identify what was installed. Fetch version-specific adapter metadata/source only when the path and a discriminating question justify it. A large version range must remain a range unless proof closes it; do not inspect two familiar versions and call the interval exhausted.

Conditional dependency relationships must retain the declaration's version constraint, dependency extras and environment marker, together with the containing project extra/group/root and source identity where relevant. A dependency's requested extras and the project's containing extra are different facts. Selecting the containing extra, consuming a file or finding a lock entry does not establish that every conditional requirement applies to the selected environment. Compose only selection/applicability facts actually established by scoped evidence; unsupported or unbound conditions remain explicit unknowns. This is a preservation/claim constraint, not a requirement to implement a universal resolver or every marker dimension in the first trial.

The [parallel applicability handoff](../working-memory/2026-10-03_dependency-applicability-and-marker-propagation_handoff.md) supplies S015/S016 context for this refinement. A [read-only composition diagnostic](../working-memory/evidence/2026-10-03-marker-propagation-review/result.json) additionally reproduces an existing optional-extra problem: an unchanged `python_version < "3.12"` marker is lost after exact-pin extraction, and the normal static collector reports positive changed-dependency consumption when the selected workflow declares Python 3.12. This diagnostic uses synthetic exact files and a mocked acquisition provider; it does not establish live CLI output, runtime installation or overall compatibility. Repair, if admitted, belongs at the earliest adequate dependency/applicability owner before broader target-context integration, with conditional source facts retained and honest unresolved outcomes when applicability is not established. Report wording cannot repair an incorrect producer claim.

The HTTPX development example is:

```text
target tests use FastAPI TestClient
→ an older Starlette adapter passes app= to HTTPX Client
→ a fixed adapter branch does not
→ HTTPX removes that argument
→ target resolution/adapter branch is unknown
```

The manual packet shows a plausible version-dependent incompatibility mechanism, not an observed target failure. The target's unpinned `fastapi[standard]` does not identify a resolved Starlette version. A package constraint, static import, green image build or later merged PR cannot fill that missing observation. Runtime resolution/test execution remains a separate admitted investigation.

## 7. Candidate/result boundary and ownership

Dated follow-up: the [2026-10-03 correctness repair](../working-memory/2026-10-03_2123_conditional-optional-extra-correctness_lbd-cycle.md) preserves the optional requirement marker/dependency extras and makes selected marked consumption explicitly unresolved. It implements condition retention without marker truth evaluation or broader target-context/source-policy admission; the earlier diagnostic remains baseline evidence.

Conceptual records below describe evidence responsibilities, not frozen Python class names or a universal graph schema:

| Information family | Earliest adequate owner | Required distinctions |
| --- | --- | --- |
| Package/repository association | `pypi/` acquisition + `upstream/` association policy | Basis, exact release/distribution, examined declarations, conflict/absence and permitted source use |
| Release window/change proposal | `upstream/` | Exact interval/source scope, model/method identity, quote references, semantic uncertainty and coverage |
| Target source and dependency relationships | `target/` and `dependency/` where their meanings belong | Repository/revision/path; imports/calls versus inferred exposure; declarations versus actual resolution |
| Mechanism-specific candidate/applicability | `impact/` | Change, exposure, activation and consequence as separate known/unknown propositions; alternatives/path coverage |
| Normal composition | `investigation.py` | Coordinate owners and retain results; no duplicated semantic parser or authority inference |
| Human/saved representation | existing report owners | Preserve candidate/interpretation strength, missing premises, sources and coverage limits; no added final-action authority |

No database, persistent graph, generic agent layer or rewrite of the existing support-drop flow is required for the first feasibility trial. Retention must include the actual semantic input/source and method identity needed to review the result, without turning model prompts/raw responses into public dumps. New report/export fields require an explicit version/compatibility review; current saved reports must remain readable with their recorded meanings.

## 8. Inspectable comparison

These are engineering judgments for discussion, not measurements or numeric scores.

| Criterion | Keep publisher-provenance-only discovery | Distinct evidence bases + bounded change/context proposals |
| --- | --- | --- |
| Maintainer utility | Weak on the observed HTTPX input; honest missing state | Potentially stronger conditional mechanism/source explanation; unmeasured |
| Normal-producer reachability | Verified limit on this input | Metadata/source retrieval feasible; automated association/context semantics unproven |
| Truthfulness / false-confidence risk | Conservative source gate; may obscure available weaker evidence | Acceptable only with visible basis/unknowns; greater admission/interpretation risk |
| New evidence burden | Low extension cost, high dependence on provenance availability | Moderate: association scope, exact sources, target inventory and adapter/version constraints |
| Coverage dependency | Existing narrow horizons | Release/context completeness must be explicit; runtime is still separately missing |
| Independent testability | Existing resolver tests and normal failure reproduce | Association/grounding/static facts can be tested separately from real-model meaning and user utility |
| Complexity / maintenance | Lowest, but leaves the product gap | Higher; bounded existing providers and typed results avoid a generic infrastructure layer |
| Reversibility | Strong | Strong if trial remains isolated until admission and leaves existing stronger route intact |
| Learning / product leverage | Preserves known route but little new capability | Teaches source basis, semantic grounding and dependency-mediated applicability toward the Charter |

Recommendation: investigate the second design through a bounded feasibility trial, while retaining the first as the declared acquisition/producer baseline. Curated packets can calibrate semantic questions but cannot substitute for the normal-source acquisition proof. Model-generated repositories and expected-answer regexes are excluded by accepted evidence/generality constraints, rather than presented as equally credible alternatives.

## 9. Smallest complete trial and deferred responsibility

The proposed first trial should deliver an exact, source-linked API-change/exposure candidate or explained unresolved result through a reproducible input/result path. It must examine the crossed-release window, represent the association basis, obtain target context through ordinary capabilities, preserve version/activation uncertainty, and surface it for inspection. Source lookup alone and an offline hand-built diagnosis are incomplete outcomes.

Included: source-association comparison; bounded release/change interpretation; static target/dependency/adapter exposure; multiple change observations/coverage limits; candidate/report faithfulness; omission-sensitive evaluation. Initial explicit argument removal is a proof slice of that path.

Deferred: broad behavioral/data-format effects, arbitrary dynamic Python, full dependency resolution, actual target tests/installs, source-build observations, broad migration remedies, non-abstention permission and adaptive agent execution. These are temporarily unsupported proof responsibilities, not claims that those impacts do not matter. Expand when a real omitted mechanism or missing observation blocks a useful result and a proportional input/proof method is available. OpenCV's static environment question is a separate pressure; do not force it into an API schema.

This narrowing is justified by the observed end-to-end gap and a retrievable source/context path; it is not justified merely by an easy model case. If the first method only reproduces the known `app` story, requires caller-supplied interpretation, or cannot cover release/context variation, reject or keep it as a disposable experiment.

## 10. Trial sequence and proof conditions, if admitted

1. Resolve source-basis eligibility and preserve the current stronger contract. Define exact permitted effects and failure/declared/conflict states before implementation.
   The separately verified marker-retention repair is complete; use its explicit unresolved condition boundary when inspecting target declarations. General marker truth evaluation remains outside the trial.
2. Freeze trial inputs, code/model/prompt/contract identities, capability limits, expected/forbidden meanings outside producer inputs, and case roles. Known HTTPX and Soup Sieve controls are development data; identify separate variation/protected material before broader claims.
3. Implement only the minimal read-only acquisition/retention and structured proposal path in its admitted home. An isolated evaluation is not product integration; later product behavior belongs in `src/` with active product tests.
4. Test identity conflicts, absent provenance, contradictory links, release boundaries, grounding, partial context and malformed/untrusted output. Compare equivalent supplied evidence when comparing interpretation methods; compare acquisition modes separately.
5. Run real local-model semantic evaluation. Include deprecation versus removal, future/negated/added behavior, multiple changes, alias/wrapper paths, old/fixed/unknown adapter resolution and absent CI. Source-grounded false meanings must be caught by semantic review, not counted as accepted because JSON parses.
6. Verify ordinary PR-to-candidate/report reachability without known-answer injection, preservation of unresolved premises and existing support-drop/report behavior. Report measured cost/latency and case-specific omissions, not only test counts.
7. Review scoped outcomes before product admission or further expansion. Independent usefulness and broader generalization require their own reviewer/adjudication/protected-input proof.

Pass intent: no critical false/misattributed or unearned applicability/action claim; required scoped observations/unknowns retained; source/context path normally reachable; justified improvement over the declared baseline without losing correct information. Freeze precise task-specific acceptance before outputs, not after seeing failures. Independent semantic/utility admission cannot be marked passed while its reviewer/labels are unavailable.

Reject/re-enter for: silently promoting declared associations; hiding a publisher conflict; plausible but wrong grounded semantics; ignored material releases/changes; hardcoded target path/version; inferred resolution or execution; all-unknown output called useful; contaminated development results called unseen accuracy; a repair requiring validator weakening rather than corrected evidence/meaning.

## 11. Promotion and open decisions

Source-basis invariants are promoted to Core §6.3 and the durable representation/examination method to ADR-0011. The compact feasibility plan owns cases, budgets, ordinary producer reachability and acceptance/rejection gates. These accepted planning decisions do not establish implementation or API model quality.

A newly adopted semantic method still needs role-specific measured evidence and admission; ADR-0006 is not automatic permission. Product migration, proposal/report representation and independent usefulness remain separate decisions/proof. Read the promoted owners rather than this draft's illustrative sequence for execution.

Remaining decisions/proof: whether ordinary acquisition meets the selected inventory/window limits; whether semantic capability is strong enough on varied real evidence; independent adjudication/reviewer availability; and whether the resulting information justifies product integration. Eligibility/effect rules and initial operational budgets are now selected by the promoted owners, with explicit reassessment conditions. No draft assertion supplies implementation or quality proof.
