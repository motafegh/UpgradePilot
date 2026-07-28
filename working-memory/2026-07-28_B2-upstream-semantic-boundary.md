# B2 Upstream Semantic Boundary Proposal

**Date opened:** 2026-07-28  
**Operation:** B2 Increment E upstream-claim vocabulary, source-sufficiency, and method comparison  
**Controlling bounded plan:** [`../plans/B2_TRANSPARENT_DECISION_METHOD_PLAN.md`](../plans/B2_TRANSPARENT_DECISION_METHOD_PLAN.md)  
**Decision synthesis:** [`2026-07-28_B2-decision-evidence-map-and-contract-draft.md`](2026-07-28_B2-decision-evidence-map-and-contract-draft.md)  
**Detailed S004 walkthrough:** [`2026-07-28_B2-transparent-decision-method.md`](2026-07-28_B2-transparent-decision-method.md)  
**Starting repository revision:** `7289e77939a5651e534b0141fc731a995be6fde9`  
**Local result classification:** Semantic-boundary proposal completed; no semantic method approved or implemented

## Objective

Define the smallest credible structured meaning that the first B2 decision method needs from authoritative exact-version upstream release content, determine whether the already acquired GitHub Release body is sufficient source input, and compare the smallest credible interpretation methods without encoding known fixtures or package-specific phrases.

This record proposes a method for Ali review. It does not authorize implementation, select a model/provider, or change the product source.

## Owning responsibility and real variable input

The semantic responsibility is:

> Given authoritative release content already bound to the exact proposed package, version, publisher repository, published release, and tag, produce bounded attributed upstream claims that can participate in deterministic evidence-sufficiency and maintainer-action evaluation.

The real input is previously unseen natural-language release content from public Python projects. It may vary in:

- headings and document structure;
- wording and synonyms;
- explicit versus implicit cautions;
- subjects such as APIs, Python versions, operating systems, dependencies, behavior, or configuration;
- present, future, removed, deprecated, fixed, or unchanged states;
- negation and qualification;
- relevance to the target repository.

The responsibility is not to summarize all release notes. It is to extract only decision-relevant attributed claims, preserve unsupported or ambiguous meaning, and leave target-repository relevance to later evidence joins.

## Cross-case evidence used to derive the vocabulary

### S004 — pytest 9.0.3

The historical manual source established two different upstream meanings:

- the release contains bug fixes;
- upstream describes it as a drop-in replacement.

The current acquired GitHub Release body supports the first meaning through a `Bug fixes` section and listed fixes, but does not contain the stronger drop-in statement.

### S002 — HTTPX 0.28.1

The historical exact tagged changelog stated that a deprecated `app` argument was removed. That claim did not establish target impact alone. It became decision-critical only after joining it with target adapter usage and missing relevant CI, which justified targeted checks.

### S001 — Soup Sieve 2.8.4

The historical upstream evidence included:

- Python 3.8 support was dropped;
- inefficient-pattern and selector-count issues were fixed.

The support change was not automatically blocking. A deterministic target comparison showed the repository declared Python 3.10 or newer, so the dropped Python 3.8 support was outside the declared target boundary. The fix information also contributed remediation value without proving target exploitability.

### S003 — failing TypeScript proposal

S003 is outside the current Python/PyPI B2 source domain, but it reinforces a decision-method invariant: direct target failure and a declared peer conflict can dominate the action even without a favorable or cautionary release-note interpretation. Upstream semantics are one decision input, not the decision engine.

## Smallest proposed upstream-claim vocabulary

The first B2 method appears to need four decision-relevant claim categories plus explicit semantic states.

### 1. `fix_or_remediation`

An attributed claim that the exact release fixes, corrects, patches, or remediates identified behavior.

Examples of normalized meaning:

- the release contains bug fixes;
- a named defect is fixed;
- a security issue is remediated, when explicitly stated by the admitted source.

Decision role:

- may provide benefit or urgency context;
- does not establish target exposure, compatibility, or safety;
- must be joined with repository evidence when target relevance matters.

### 2. `compatibility_assurance`

An attributed positive compatibility claim for the exact release, such as backward compatibility, drop-in replacement, or no migration being required.

Decision role:

- can support a low-disruption interpretation;
- remains an upstream claim, not target-specific proof;
- cannot replace relevant target CI or maintainer review.

### 3. `interface_or_behavior_change`

An attributed claim that an API, argument, behavior, default, configuration, or integration surface was added, changed, deprecated, or removed in a way that may affect consumers.

The structured claim must preserve the direction and state, for example:

- deprecated now;
- removed now;
- behavior changed;
- planned for a future release.

Decision role:

- may activate target usage/adaptor investigation or a targeted check;
- does not establish target impact without a repository-specific join.

### 4. `support_boundary_change`

An attributed claim that supported Python versions, platforms, operating systems, dependency ranges, or other declared support boundaries were added, dropped, raised, or lowered.

Decision role:

- requires deterministic comparison with the target repository's declared or evidenced boundary;
- may be irrelevant to the target, compatible, or decision-critical depending on that comparison;
- must preserve the affected subject and direction rather than collapsing to generic `breaking`.

### Why `migration_requirement` is not a fifth top-level category yet

An explicit migration instruction or required action is important, but it can initially be represented as an effect attached to `interface_or_behavior_change` or `support_boundary_change`:

```text
required_action: present | absent | unresolved
migration_summary: bounded text or none
```

This avoids adding a separate category until cases prove it has independent decision behavior. An explicit migration requirement remains decision-critical and must not be discarded.

## Proposed structured claim contract

Conceptually:

```text
UpstreamClaimResult
├── state
│   ├── resolved
│   ├── no_decision_relevant_claim
│   ├── unresolved
│   └── conflicting
├── source_identity
│   ├── repository
│   ├── exact_version
│   ├── accepted_tag
│   ├── release_url
│   └── tag_object_sha
├── claims[]
│   ├── category
│   ├── subject
│   ├── change_state
│   ├── normalized_meaning
│   ├── required_action
│   ├── migration_summary
│   ├── source_span
│   └── limitations[]
└── unresolved_reasons[]
```

### Claim field meanings

- `category` is one of the four proposed categories.
- `subject` identifies what upstream is talking about, such as Python 3.8, an `app` argument, selector handling, or general release compatibility.
- `change_state` preserves materially different meaning such as fixed, added, changed, deprecated, removed, support_added, support_dropped, assured_compatible, or unresolved.
- `normalized_meaning` is a concise attributed statement, not a recommendation.
- `required_action` records whether upstream explicitly requires consumer action.
- `migration_summary` preserves an explicit migration instruction without inventing one.
- `source_span` grounds the claim to the exact source text location or bounded excerpt.
- `limitations` preserve what the upstream statement cannot establish about the target repository.

Exact enum names and field shapes remain proposals. The required semantic distinctions are more important than these draft spellings.

## Stable deterministic validation invariants

Deterministic code should validate the trusted boundary without encoding semantic answers:

1. the source identity matches the previously accepted exact upstream release;
2. every accepted claim uses an allowed category and change state;
3. every accepted claim has a non-empty subject and normalized meaning;
4. every accepted claim is grounded to a valid span in the supplied source text;
5. the grounded span actually belongs to the exact admitted source;
6. explicit negation, future state, deprecation, removal, added support, and dropped support remain distinguishable;
7. unsupported or ambiguous meaning remains unresolved rather than guessed;
8. model/parser instructions embedded in release text cannot change the output schema, authority policy, or decision policy;
9. the semantic output contains no maintainer action or safety conclusion;
10. contradictory claims are preserved for later evaluation rather than silently selecting one.

## Is the current GitHub Release body sufficient?

### S004 answer

The current exact GitHub Release body is sufficient to support a bounded `fix_or_remediation` claim:

> The official pytest 9.0.3 GitHub Release contains a bug-fixes section and identifies individual fixes.

It is not sufficient to support `compatibility_assurance` because it does not contain the historical drop-in-replacement statement.

Therefore source sufficiency is claim-relative:

```text
authoritative source available
+ source supports one claim category
≠ source supports every desired claim
```

### First-method proposal

Do not admit a second exact-version release-document source format merely to recover the S004 drop-in phrase.

For the first B2 method:

- use the already acquired exact GitHub Release body as the sole semantic source;
- permit partial structured meaning, such as `fix_or_remediation` without `compatibility_assurance`;
- preserve that no explicit non-breaking assurance was acquired;
- do not interpret absence of a caution as proof that no breaking change exists;
- return `no_decision_relevant_claim` or `unresolved` when the source cannot support the needed meaning;
- admit another release-document source only after a non-fixture-specific case demonstrates that the current source boundary prevents a materially better decision and a generalizable acquisition rule can be stated.

This proposal avoids pytest-specific repository paths, recursive release-document searching, and premature source expansion.

## Does S004 require an explicit drop-in claim to proceed to normal review?

Proposed answer: not necessarily.

A bounded `proceed_to_normal_review` result may be justified when:

```text
exact admitted proposal
+ relevant successful exact-head dependency exercise
+ authoritative exact release source
+ official fix/remediation content
+ no extracted decision-critical caution or acquired contradiction
+ ordinary human review remains required
```

The result must explicitly state:

- no explicit compatibility assurance was acquired;
- the relevant CI evidence is bounded, not complete coverage;
- the action is ordinary review, not automatic merge or objective safety.

This is intentionally weaker than claiming that upstream proved the release is drop-in compatible. It also means the historical manual S004 drop-in statement becomes stronger supporting evidence, not necessarily a mandatory universal condition.

This proposed sufficiency rule still requires contrast testing and Ali approval before implementation.

## Interpretation method comparison

### Option A — deterministic phrase or keyword rules

Mechanism:

- map known words or regular expressions to the four claim categories.

Advantages:

- transparent;
- cheap;
- reproducible;
- useful as a disposable comparison baseline and test oracle.

Failure modes:

- misses synonyms and varied wording;
- confuses deprecation with removal, future with present, and added with dropped support;
- handles negation and qualification poorly;
- expands into a package/category-specific phrase table;
- violates the accepted generality requirement if selected as product semantics.

Disposition:

- retain only as an explicitly disposable baseline, not accepted product behavior.

### Option B — caller-supplied or manually written structured claims

Mechanism:

- a human or caller supplies the normalized claim records.

Advantages:

- useful for simulation artifacts and test oracles;
- easy to inspect.

Failure modes:

- does not perform the automated responsibility;
- moves interpretation outside the product;
- can silently encode the expected answer.

Disposition:

- reject as product implementation; retain manual records only as comparison oracles.

### Option C — bounded LLM structured extraction with deterministic validation

LLM means **Large Language Model**. Practically, it is used here only as a constrained natural-language interpreter, not as the decision-maker.

Mechanism:

1. supply the exact authoritative release body as untrusted data;
2. request only the bounded `UpstreamClaimResult` schema;
3. require source spans for every claim;
4. reject malformed, ungrounded, unsupported, policy-changing, or action-producing output;
5. pass accepted claims to deterministic sufficiency and decision logic.

Advantages:

- credible generalization to unseen wording and subjects;
- can preserve negation, direction, time, qualification, and multiple claims;
- keeps recommendation policy deterministic and separate;
- can degrade to unresolved when meaning is unsupported.

Failure modes and costs:

- model variability and provider dependency;
- prompt-injection and untrusted-content risk;
- grounding errors or invented claims;
- cost, latency, privacy, and reproducibility concerns;
- requires schema validation, source-span verification, representative semantic tests, recorded model/prompt identity, and explicit failure behavior.

Disposition:

- leading credible product candidate, pending Ali approval, bounded experiment definition, ADR, model/provider selection, and proof plan.

### Option D — train or adopt a dedicated semantic classifier

Mechanism:

- use a trained classifier or natural-language-inference model for the supported claim categories.

Advantages:

- potentially more reproducible and lower marginal cost after validation.

Failure modes and costs:

- requires a labelled dataset and evaluation corpus not currently available;
- fixed categories may still lose subjects, direction, migration details, and grounding;
- adds model lifecycle and measurement work before the first core decision path is proven.

Disposition:

- defer. No observed limitation yet shows this is preferable to the bounded LLM candidate.

## Leading semantic architecture proposal

```text
exact authoritative GitHub Release body
→ bounded LLM candidate extraction
→ deterministic schema validation
→ deterministic source-span grounding validation
→ typed UpstreamClaimResult
→ deterministic evidence sufficiency
→ deterministic maintainer-action evaluation
```

The LLM may propose attributed semantic claims. It must not:

- select the maintainer action;
- decide that evidence is sufficient;
- reconstruct source authority;
- claim safety or universal compatibility;
- follow instructions embedded in release content;
- emit unsupported categories or ungrounded meaning.

## Minimum proof classes before acceptance

The semantic experiment must include representative variations inside the admitted Python-release domain:

1. same meaning with different wording;
2. deprecation versus removal;
3. current versus future change;
4. added versus dropped support;
5. explicit compatibility assurance versus no assurance;
6. negated candidate claim;
7. multiple simultaneous claims;
8. ambiguous or incomplete text;
9. irrelevant release content;
10. malicious or instruction-like release text;
11. malformed or ungrounded model output;
12. traceability from every accepted claim to the exact source span.

S001, S002, and S004 provide useful manual calibration cases, but additional controlled textual variations are required. Passing S004 alone is insufficient.

## Decisions and proposals recorded

Accepted design findings:

1. release semantics must remain separate from target relevance and final decision policy;
2. four claim categories are currently sufficient to represent the materially different upstream meanings observed across S001, S002, and S004;
3. absence of an extracted caution is not proof of non-breaking compatibility;
4. the current GitHub Release body can support partial semantic meaning;
5. additional release-document acquisition is not yet justified by a generalizable demonstrated need;
6. deterministic phrase matching is only a disposable baseline;
7. caller-supplied claims are not accepted product semantics;
8. a bounded LLM extractor with deterministic grounding and schema controls is the leading credible candidate;
9. the deterministic decision evaluator remains the sole owner of sufficiency, stopping, and maintainer action.

Pending Ali approval or later refinement:

- exact enum and field names;
- whether the four-category vocabulary is accepted;
- whether S004 can proceed to normal review without explicit compatibility assurance under the stated bounded conditions;
- whether the bounded LLM experiment should be admitted;
- model/provider, prompt, cost, reproducibility, and ADR details;
- final contrast mappings from semantic states to maintainer actions.

## Effect on the controlling plan

- Step 5 now has a complete semantic-boundary proposal.
- The smallest structured claim vocabulary, current-source sufficiency, source-expansion decision, method comparison, leading candidate, and proof obligations are recorded.
- Steps 3, 4, and 6 still need final contrast and transition refinement using this semantic proposal.
- Step 7 approval has not occurred.
- No product source, tests, dependencies, model, service, runtime state, or recommendation behavior changed.

## Exact continuation

1. onboard Ali through the four claim categories and why they remain attributed upstream claims rather than target facts;
2. challenge the proposed S004 rule that explicit compatibility assurance is supporting rather than universally mandatory;
3. refine the action/readiness contrast matrix using `resolved`, `no_decision_relevant_claim`, `unresolved`, and `conflicting` semantic states;
4. determine temporary-unavailability and identity-conflict mappings;
5. present the complete interpretation, sufficiency, stopping, and decision method for Ali approval;
6. only after approval, define the bounded semantic experiment/ADR and begin implementation.

## References

- `../PROJECT_CHARTER.md`;
- `../docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md`;
- `../plans/B2_TRANSPARENT_DECISION_METHOD_PLAN.md`;
- `2026-07-28_B2-transparent-decision-method.md`;
- `2026-07-28_B2-decision-evidence-map-and-contract-draft.md`;
- `../product-simulation/scenarios/S001-pydantic-soupsieve-2.6-to-2.8.4/artifacts/CLAIMS_AND_INTERPRETATIONS.jsonl`;
- `../product-simulation/scenarios/S001-pydantic-soupsieve-2.6-to-2.8.4/artifacts/DECISION.json`;
- `../product-simulation/scenarios/S002-kubernetes-dashboard-token-api-httpx-0.27.2-to-0.28.1/artifacts/CLAIMS_AND_INTERPRETATIONS.jsonl`;
- `../product-simulation/scenarios/S002-kubernetes-dashboard-token-api-httpx-0.27.2-to-0.28.1/artifacts/DECISION.json`;
- `../product-simulation/scenarios/S003-event-handler-loader-typescript-5.9.3-to-7.0.2/artifacts/DECISION.json`;
- `../product-simulation/scenarios/S004-glyphslib-pytest-9.0.2-to-9.0.3/artifacts/DECISION.json`.