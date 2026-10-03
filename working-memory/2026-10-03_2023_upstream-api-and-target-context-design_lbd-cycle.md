# Upstream API changes and target context — design cycle

Date: 2026-10-03 (Asia/Tehran). Primary operation: Planning/Design.
Session status: ACTIVE.
Previous: [report development-case/repair cycle](2026-10-03_1959_report-development-case-check_lbd-cycle.md).
Owners: [Charter](../PROJECT_CHARTER.md), [Core](../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md), [Product Decision Model](../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md), [Minimum Useful Generality](../docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md), [report-plan re-entry](../plans/MAINTAINER_REPORT_PRESERVATION_AND_USEFULNESS_EVALUATION_PLAN.md).

UP-SKILL:upgradepilot-planning-design; UP-SKILL:upgradepilot-learning-by-doing; UP-SKILL:upgradepilot-working-memory.

## Cycle progression

A0 — DONE: fetched origin and reconciled local/fetched main at `7edb33c7869c92c527d8f282c998f4710f3326d2`; read controlling product/trust/generality/report owners, current acquisition/interpretation boundaries, directly relevant case evidence and previous closure; initialized this record.
A1 — DONE at continuous-context depth: Ali received the three-case findings and reporting repair explanation, then explicitly selected the recommended design responsibility before any implementation decision.
A2 — DONE at planning orientation depth: explained source identity versus target-specific meaning, design-only mutation boundary and draft → teaching → user decision order. Deeper alternatives will be taught from the draft rather than assumed already understood.
B — DONE: traced source/semantic/target boundaries, obtained read-only association/source feasibility evidence and prepared one non-controlling design/architecture/trial proposal with inspectable alternatives and proof conditions.
Verification gate — GREEN for planning artifact consistency: source/owner trace, exact distribution hash/name/version, pinned repository/tag/source/excerpt identity, local link and unchanged executable-diff checks. No source-policy, model/API or implementation acceptance implied.
D — CURRENT: draft and recommendation prepared for the evidence-backed teaching/review handoff; Ali's understanding/challenges are not yet assessed.
E — PENDING: questions/decision before draft promotion or implementation admission.
C — CONTINUOUS.

## A0 and living orientation map

- User authorization is explicitly planning/research/preservation/teaching, followed by a later decision about implementing. Standing commit/push cadence applies to the coherent draft; it does not permit executable changes or acceptance of a trust policy.
- Fetch updated an unrelated remote learning branch, not main. Another session's untracked broad-audit working memory remains untouched. No incoming main delta required pull.
- Normal HTTPX result exposes three distinct problems: publisher-provenance-only repository identity stops acquisition; the adopted semantic role extracts Python support drops, not API changes; target adapter/resolved-version context is not acquired through a normally reachable API mechanism. Fixing only the first problem cannot establish the other two.
- Core and Product Decision Model require source/identity authority before interpretation, honest authority/uncertainty, and candidate-specific applicability. Current `UpstreamRepositoryResolver` reconciles package project links with PyPI-reported publisher provenance. Its missing-provenance problem is implementation truth; canonical invariants do not automatically make this the only possible future source-association method.
- ADR-0006 admits one narrow local support-drop role. It does not authorize a new API interpreter, reuse its historical quality score for that role, or admit an agent/tool loop.
- Minimum Useful Generality requires the method to address the broader owning responsibility rather than accumulate one phrase parser or manually supplied answer per known example.
- A1 bridge: reports faithfully expose current limits after the small empty-environment repair; missing product capability needs evidence/meaning responsibilities, not extra prose.
- A2 map: package-to-repository association; exact release/source interval; upstream change proposal; exact target usage/dependency/adapter context; unresolved resolution/activation; evidence-backed candidate; applicability/report boundary. Contrast weaker declared associations with publisher provenance without relabeling either. Retain an explicit record of omissions and unsupported paths.
- Expected result: one reviewable proposal with an inspectable decision rubric, conceptual data/control flow, smallest complete trial, proof/rejection conditions, promotion map and open questions. No accepted schema/ADR/spec change, runtime mutation, model adoption, target execution or action permission.

## Proportionate cadence adaptation

Ali explicitly requested findings/drafts/architecture first, then explanation and a decision about implementation. Normal separate A1/A2 stops would repeat the immediately preceding continuity and require teaching unresolved designs before the evidence-backed draft exists. Use that continuous onboarding plus compact design-only orientation, perform authorized planning, then stop at the meaningful D/E review/admission boundary. This follows the requested order, records the adaptation and does not infer learner mastery or silently accept a source-trust method. Any implementation or stable-policy promotion remains outside this turn's authorization.

## B — design evolution and discriminating evidence

Read active resolver/provenance/interval/claim/extractor sources and upstream identity tests. Current resolver/test semantics intentionally require project-link/PyPI-reported-publisher agreement; the provenance client parses registry-reported publisher records, not a new local cryptographic verification path. Current interval/claim types cannot silently receive a weaker declared association under their stronger meaning. The accepted support-drop method covers only its named role; its score/configuration is not API adoption evidence.

The [read-only feasibility manifest](evidence/2026-10-03-api-impact-design/source-association-feasibility.json) confirms HTTPX 0.28.1's PyPI project metadata and hash-matched universal wheel headers both declare `encode/httpx`. The exact tag resolves to commit `26d48e0634e6ee9cdc0533996db289ce4b430177`; bounded 0.28.1/0.28.0 source text is retained with range/full-source/excerpt hashes and original license. Source bytes were inspected without installation/execution or model calls. This is manually guided planning feasibility, not an implemented normal association/windowing/target producer. Matching declarations share publisher control and provide consistency rather than independent corroboration; pinned source does not prove distribution build correspondence.

Fresh source review changed the draft's omission emphasis: the interval contains `proxies` as well as `app` removal, SSL deprecations and behavior changes. A known-`app` search would ignore material text. Require whole admitted crossed-release windows, attributed multiple observations and explicit unsupported/omitted coverage. Initial argument removal is a proof category, not the method/product horizon. Retained target records show a FastAPI TestClient path but unpinned framework/resolution; distinguish static usage/constraints, possible old/fixed adapter branches and actual resolved/executed state.

Consulted official PyPI attestation introduction/security model and the index-hosted attestation specification. The proposed declared-source eligibility is an engineering recommendation, not a conclusion those external documents authorize. No repository-fallback policy was accepted. Security/generality owners exclude model-guessed source authority, case-specific regex interpretation and external content instructions. A weaker association with disclosed effects requires its own accepted owner/admission before runtime use.

Produced [one design draft](../proposals/2026-10-03_UPSTREAM_API_CHANGE_AND_TARGET_CONTEXT_DESIGN_DRAFT.md) rather than an accepted ADR or speculative plan family. It contains responsibility/scope, source/semantic/target architecture, distinct evidence bases/limits, logical owner/data flow, qualitative comparison rubric, smallest complete trial and deferrals, normal reachability versus curated calibration, real-model/semantic/independent utility proof separation, rejection cases, and required promotion/open decisions. Recommendation is a bounded feasibility trial of evidence-basis-aware change/context proposals while keeping the existing stronger path as baseline. No graph/agent/database or model retry architecture is selected.

## Verification and teaching handoff

Validated relative links, metadata name/version/digest, excerpt identity/range, tag/commit capture and absence of executable changes. Documentation whitespace/publication scope are checked with the coherent increment. No product/experiment test suite or inference evaluation was run because this is a documentation-only planning responsibility; prior product results remain dated evidence. Neither retrievable source nor a plausible architecture proves semantic quality, autonomous target discovery, independent usefulness, applicability or learner ownership.

Teach source association versus origin/trust, release meaning versus target exposure, declared constraints versus actual resolution, AI proposal versus deterministic grounding/composition, and initial trial versus accepted product capability. The HTTPX example should lead to a conditional mechanism with explicit unknown adapter resolution, not a compatibility/failure verdict. D/E remain open for Ali's questions/challenges and the implementation-or-trial decision. Any accepted source policy, ADR/plan/schema promotion or actual implementation is a subsequent authorized responsibility.

Publication follow-up: the general staged whitespace check flagged a trailing-space line and final blank lines in the exact captured HTTPX source excerpt. The orchestration continued to commit/push before that result was classified; acknowledged this sequencing mistake. Circumstance is preserved external source bytes; normal route is an all-file whitespace pass; trimming that data would falsify the declared exact excerpt. Chosen exception is only the raw excerpt, with authored-document whitespace checked separately and captured hashes revalidated. No source bytes or hashes were changed, and no repository-wide lint suppression was introduced. The exception and check scope are explicit in the evidence README.
