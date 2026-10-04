# ADR-0011 — Explicit source-association bases and proposal boundary

**Status:** Accepted design decision for source representation and limited examination effects; implementation and API semantic-role adoption require their own proof/admission.
**Date:** 2026-10-03
**Responsibility:** Permit useful upstream source examination without relabeling publisher declarations as publisher provenance or stronger claim authority.
**Requirements:** [Core §6.3](../specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md#63-source-association-bases-and-permitted-effects), [Product Decision Model](../specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md), [Minimum Useful Generality](../specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md), [Security](../../SECURITY.md).
**Execution coordination:** [API-change/target-exposure feasibility plan](../../plans/UPSTREAM_API_CHANGE_AND_TARGET_EXPOSURE_FEASIBILITY_PLAN.md).

## Context

The [design evidence](../../working-memory/evidence/2026-10-03-api-impact-design/README.md) shows retrievable HTTPX release/source declarations despite the current resolver's missing publisher-provenance result. The gap has three owners: source association, release meaning and exact target exposure. Repository retrieval alone cannot fill the latter two.

The existing [upstream resolver](../../src/upgradepilot/upstream/repository.py) owns a stronger project-link/publisher-provenance agreement contract. Its evidence type and consumers must retain that meaning. Existing [ADR-0006](ADR-0006-bounded-local-support-drop-semantic-extractor.md) admits only the measured support-drop role. New source access does not adopt a new API interpreter.

## Decision

Represent source associations with separate concrete evidence bases and separately evaluated examination eligibility. Preserve acquisition records, problems and examined candidates; avoid a generic confidence score or one `trusted` boolean.

| Evidence basis | Representation/effect |
| --- | --- |
| Registry-reported publisher association | Preserve the existing resolver/result and its current admitted effects; label the reported basis accurately. |
| Exact-release publisher-declared repository | Separate declaration record; may permit bounded read-only examination and source-attributed change/exposure proposals under this decision. |
| Pinned repository tag/commit/file | Exact examined text identity, linked to its association basis; no inferred distribution build correspondence. |

The first declaration method starts from identity-validated exact PyPI release metadata. Normalize recognized source/repository labels using generic label/URL grammar; accept only one unambiguous public HTTPS GitHub repository identity from explicit source/repository declarations. Homepage/documentation links alone remain insufficient for this method. Preserve ignored labels and all examined source declarations; conflicting identities remain conflicted rather than selecting the convenient one. Reconstruct provider requests from validated repository identity rather than fetching arbitrary declared URLs.

An exact-release registry declaration is sufficient for this *limited examination* proposition. A mandatory wheel download would add cost without supplying independent publisher authority. Inspect a distribution's non-executed metadata only when the declared/shipped-metadata relationship or a conflict is a material question. If sampled, require registry digest equality, parsed name/version agreement, bounded archive/member handling and explicit sample scope; reconcile contrary links. Distribution inspection is never an install/build, and matching declarations remain same-controller consistency.

Inspect publisher records independently of the existing resolver’s project-link eligibility gate; its combined result is not a publisher-only verdict. Homepage rejection under that older gate cannot by itself establish conflicting publisher provenance.

Missing usable provenance permits the separately labeled declared-source route. Existing identity mismatch, ambiguous/malformed provenance or an acquisition failure is retained. An adverse or undecidable result must block positive *association eligibility* where it prevents this method establishing its own premises; it is not erased by fallback. Other unaffected evidence may still be recorded. Unknown/unsupported publisher forms do not become positive declared-source eligibility merely to bypass the stronger resolver.

Resolve release/tag/file identity separately. Structural release boundaries and exact commit text may support an attributed proposal with its declared-source basis; they do not populate `UpstreamRepositoryEvidence`, `AuthoritativeUpstreamIntervalEvidence` or grounded support-drop contracts by coercion. New proposal results remain distinct from existing trusted claims. Missing tag/window coverage, identity disagreement and truncation remain explicit outcomes.

## Consequential composition boundary

Deterministic code owns acquisition, association eligibility, identity, source-window scope, references, schema and allowed effects. A trial LLM may propose change meaning or a target relationship; it cannot select source authority, declare completeness, resolve actual target versions, evaluate its own applicability or grant an action.

Target declarations, markers/extras, imports/calls, adapter-version source, actual resolution and runtime exercise are separate propositions. Preserve missing premises rather than flatten conditional edges. Direct source-grounded proposals can be shown as proposals; complete applicability requires the Product Decision Model's independent composition rules. Maintainer-action permission is unchanged.

## Initial implementation home and reversal

Evaluate the new API path first in `experiments/`, importing existing product providers/contracts only where their meanings fit. New read-only acquisition adapters stay in that trial until their supported producer responsibility is proved. Start from ordinary PR identity and acquired files, without injecting known-answer paths, model meanings, dependency contexts or positive membership results. Curated mode is a separate calibration proof class.

The trial may render its own structured proposal summary beside an unchanged baseline product report; it must not serialize API proposals as accepted v1 product findings. Product adoption requires a reviewed migration to `src/` and active tests, source/role-specific admission and explicit report/version compatibility decisions. Product runtime must not import the trial. No framework, database, autonomous agent, target execution or dependency addition is selected here.

## Alternatives and consequences

- Keeping only publisher-provenance discovery is the lowest-cost baseline but leaves retrievable, weaker information unused on the observed input.
- Casting declared links into existing stronger objects would obscure authority and break consumer meanings; rejected.
- Requiring matching registry/wheel declarations for every examination adds same-controller consistency at extra cost; retain it as a discriminating check when needed rather than an authority prerequisite.
- Broad web search, model-guessed repositories and arbitrary link following have no adequate association basis in this method; excluded.

The chosen route increases evidence-state/coverage work while preserving stronger existing behavior. It is reversible by disabling declared-source eligibility or declining trial adoption without changing existing resolver/report meanings. Failure on ordinary acquisition or varied semantic/context evidence returns to design; useful prose cannot compensate for missing producers.

## Reassessment and proof boundary

Reassess before widening hosts, labels, metadata sampling, permitted effects, inference roles, source windows or normal target discovery. A publisher conflict, false source attribution, overconfident target claim, material omitted change or need for a package-specific answer is a re-entry trigger. The plan owns exact cases/budgets/proof; dated evidence owns results. Acceptance of this design establishes no implemented capability, semantic accuracy, independent usefulness or learner mastery.
