# B2 Decision Evidence Map and Contract Draft

**Date opened:** 2026-07-28  
**Operation:** B2 Increment E evidence synthesis and first decision-contract draft  
**Controlling bounded plan:** [`../plans/B2_TRANSPARENT_DECISION_METHOD_PLAN.md`](../plans/B2_TRANSPARENT_DECISION_METHOD_PLAN.md)  
**Detailed evidence walkthrough:** [`2026-07-28_B2-transparent-decision-method.md`](2026-07-28_B2-transparent-decision-method.md)  
**Starting repository revision:** `27a72c5a36501eca16eca946777f1f4253d8232c`  
**Local result classification:** Evidence map completed; first contract and contrast draft recorded; no method approved or implemented

## Objective

Synthesize the completed S004 evidence walkthrough into:

1. one complete decision-evidence map;
2. the smallest proposed input and output contract for the first B2 decision method;
3. initial outcome and evidence-readiness distinctions;
4. contrast cases that prevent the method from becoming an S004 detector;
5. the exact unresolved method questions that remain before implementation approval.

This record is a design draft and evidence trail. It does not authorize implementation or replace `../MEMORY.md` as the live-state owner.

## Controlling product question

> For an admitted public Python Dependabot dependency-update pull request, what bounded maintainer action is justified by the decision-relevant evidence available for that case?

The charter permits these broad outcomes:

1. merge after normal review;
2. run targeted checks;
3. investigate or block;
4. defer;
5. abstain.

The first runtime vocabulary may use clearer names, but it must preserve those meanings and must not turn S004 into the product scope or expected answer.

## S004 complete decision-evidence map

| Evidence item | Current S004 state | Evidence role | Question answered | What it cannot establish |
|---|---|---|---|---|
| Public repository, PR number, base/head identity | Established | Admission and frozen-run identity | Which exact proposal is being evaluated? | Correctness, safety, or final action |
| Complete changed-file acquisition | Established | Admission and ambiguity control | Did UpgradePilot inspect the complete visible file-change set? | That the change is behaviorally safe |
| One same-file exact pin transition, `pytest==9.0.2` to `pytest==9.0.3` | Established | Admission requirement and decisive change identity | What exact package/version transition is proposed? | Dependency role, patch/minor/major meaning, compatibility |
| Source filename `requirements-dev.txt` | Established | Context only | Where is the pin declared? | A general `development` or `test` role by filename alone |
| Changed requirements file installed and pytest directly invoked in successful exact-head CI | Established | Strong target-repository decision support | Did at least one relevant successful path consume and exercise the proposed dependency? | Complete coverage, all environments, objective safety, final action |
| Exact PyPI release `pytest==9.0.3` | Established | Package-authority prerequisite | Does the exact proposed published package/version exist? | Upstream meaning or target compatibility |
| Exact distribution filenames, package types, URLs, and SHA-256 digests | Established | Immutable file identity | Which exact published files are tied to the release record? | Who produced them, whether they are safe, reproducible source equivalence |
| PyPI-reported provenance for both exact files | Established, 2 of 2 | Publisher-binding prerequisite | Which publisher identity does PyPI report for the exact files? | Independent attestation verification |
| Package Source candidate agrees with provenance publisher repository `pytest-dev/pytest` | Established | Upstream-authority prerequisite | Is the candidate source repository consistent with exact-file publisher identity? | Release semantics or compatibility |
| Exactly one accepted exact-version tag form resolves | Established, `9.0.3` | Exact-version upstream binding | Which exact project-controlled version identity is admitted? | That the release is favorable or safe |
| Published GitHub Release and exact tag-reference object | Established | Exact release-source authority | Is there a published release bound to the admitted exact tag? | Meaning of the release body |
| GitHub Release body contains a `Bug fixes` section and individual fixes | Available but uninterpreted in product | Partial semantic source material | Does the acquired source contain bug-fix information? | The historical stronger `drop-in replacement` claim |
| Exact tagged announcement says bug-fix release and drop-in replacement | Established only in historical manual simulation | Manual decision oracle; not current product evidence | What stronger official upstream characterization supported S004 manually? | A general runtime interpretation method |
| Historical PR merged status | Known historically | Excluded context | What did the real maintainer eventually do? | Whether UpgradePilot's method is correct |
| No decision-critical contradiction | Established manually in S004 simulation, not yet represented by product decision code | Required favorable-path condition | Did any acquired primary evidence oppose the normal-review path? | Universal absence of undiscovered risk |
| Complete compatibility or safety | Not established | Explicit claim limit | None; this is intentionally outside the product claim | Must never be inferred from the evidence chain |

## Evidence-role classification

### Admission requirements

The current B2 decision method may run only after the product establishes:

```text
public Dependabot PR identity
+ complete changed-file evidence
+ one supported same-file exact pinned Python dependency transition
```

Unsupported or ambiguous dependency changes must not be forced through the decision method.

### Authority prerequisites

Before release content can contribute semantic evidence, the product must establish:

```text
exact PyPI package/version
+ exact distribution file identities
+ usable PyPI-reported publisher provenance
+ Source/provenance repository agreement
+ one exact published GitHub Release/tag reference
```

These facts make release interpretation admissible. They are not positive recommendation signals by themselves.

### Decision-supporting target evidence

The strongest current target-repository evidence is:

> At least one successful exact-head CI path installed the changed requirements file and directly invoked the changed package.

This is relevant evidence for the proposal because it connects the changed declaration to actual successful execution. It remains narrower than complete test coverage or safety.

### Context only

Context that must not silently become decision authority includes:

- the filename `requirements-dev.txt`;
- the PR title or Dependabot wording;
- a human-recognized patch-like version shape;
- the historical merged outcome;
- a Source URL without provenance agreement;
- green CI without proof that the changed dependency was exercised.

### Missing decision evidence in the current product

The current product still lacks:

1. an approved structured upstream-claim contract;
2. an approved method to interpret authoritative release content into that contract;
3. a tested contradiction evaluation across decision-critical evidence;
4. an evidence-sufficiency and stopping result;
5. a maintainer-action result and explanation contract.

For the historical S004 normal-review rationale, the current product source also lacks the exact `drop-in replacement` statement because the acquired GitHub Release body does not contain it.

### Potential contradiction classes

The first design must preserve materially different contradictions, including:

- exact-head relevant CI failure;
- package/version identity mismatch;
- Source/provenance repository disagreement;
- more than one source repository or accepted tag identity;
- upstream material reporting breaking changes, required migration, or another claim that opposes the favorable path;
- a materially changed PR head, dependency set, requirements file, or workflow after evidence acquisition.

### Permanent claim limits

No first B2 decision may claim:

- objective update safety;
- universal compatibility;
- complete CI coverage;
- independent cryptographic verification of PyPI attestations;
- reproducible equivalence between GitHub source and PyPI distribution bytes;
- authorization for automatic merge;
- replacement of normal maintainer judgment.

## Current S004 decision readiness

The current automated evidence chain establishes:

```text
exact admitted proposal
+ relevant successful target CI exercise
+ exact package/upstream authority
```

It does not yet establish:

```text
approved decision-relevant upstream semantic claim
+ explicit contradiction result
+ evidence-sufficiency and stopping result
+ maintainer action
```

Therefore the current product remains correctly at:

```text
claim_state = unresolved_claim
no recommendation
```

The historical manual simulation provides a comparison oracle:

```text
same admitted proposal
+ relevant successful exact-head CI
+ official drop-in bug-fix characterization
+ no decision-critical contradiction
→ proceed through normal maintainer review
```

That oracle informs design. It is not implementation proof or permission to encode the answer.

## First proposed decision input contract

The smallest credible decision input should consume typed, already-validated results rather than raw URLs, raw JSON, or caller-supplied conclusions.

Conceptually:

```text
DecisionInput
├── proposal_identity
│   ├── repository
│   ├── pull_number
│   └── exact_head_sha
├── dependency_change
│   ├── source_file
│   ├── package identity
│   ├── old version
│   └── proposed version
├── ci_authority_result
├── package_release_result
├── upstream_source_result
└── upstream_claim_result
```

### Why each input exists

- `proposal_identity` binds the result to one frozen PR head and supports rerun conditions.
- `dependency_change` defines the exact update under review.
- `ci_authority_result` contributes target-specific exercise evidence and preserves insufficient/unresolved states.
- `package_release_result` preserves exact package identity or a typed package problem.
- `upstream_source_result` preserves authority, mismatch, ambiguity, unavailable, unsupported, and malformed outcomes.
- `upstream_claim_result` would contain only bounded attributed claims produced by an approved interpretation method.

The decision evaluator should not:

- refetch evidence;
- parse release prose;
- reconstruct repository authority from raw links;
- infer dependency role from filenames;
- accept a caller-supplied final action.

## First proposed decision output contract

Conceptually:

```text
DecisionResult
├── maintainer_action
├── evidence_readiness
├── decisive_reasons
├── supporting_reasons
├── unresolved_questions
├── conflicting_evidence
├── required_checks
├── inactive_investigations
├── stopping_reason
├── claim_limits
└── rerun_conditions
```

### Field meanings

- `maintainer_action` is one bounded charter-aligned action or abstention.
- `evidence_readiness` explains whether evidence is sufficient for that selected action, contains a bounded resolvable gap, remains semantically unresolved, conflicts, or is unsupported.
- `decisive_reasons` are the minimum evidence-backed reasons without which the action would change.
- `supporting_reasons` improve explanation but are not independently action-selecting.
- `unresolved_questions` preserve missing decision-critical meaning.
- `conflicting_evidence` preserves evidence that opposes or invalidates a candidate action.
- `required_checks` names a concrete discriminating check when targeted checking is recommended.
- `inactive_investigations` records material stages not activated and why.
- `stopping_reason` states why further supported investigation is or is not justified.
- `claim_limits` prevents the result from expanding into safety or universal-compatibility claims.
- `rerun_conditions` states which changes invalidate the frozen result.

These names and shapes are a draft. They are not approved runtime classes.

## Proposed runtime action vocabulary

For production clarity, the historical `merge_after_normal_review` label should be reconsidered. UpgradePilot does not perform the merge, and normal review may still reject the proposal.

A clearer proposed vocabulary is:

```text
proceed_to_normal_review
run_targeted_checks
investigate_or_block
defer
abstain
```

Mapping to the charter:

| Proposed runtime action | Charter meaning |
|---|---|
| `proceed_to_normal_review` | merge after normal review |
| `run_targeted_checks` | run targeted checks |
| `investigate_or_block` | investigate or block |
| `defer` | defer |
| `abstain` | abstain |

`proceed_to_normal_review` means only:

> No special blocker or decision-critical unresolved question has been established by the supported method; continue through the repository's ordinary human review process.

It does not mean automatic merge or guaranteed acceptance.

## Proposed evidence-readiness distinctions

The smallest credible first model appears to need at least:

```text
sufficient_for_action
resolvable_gap
unresolved_meaning
conflicting
unsupported
```

A separately preserved acquisition problem may also justify `defer` when a required source is temporarily unavailable. The design must decide whether temporary unavailability is a distinct readiness state or remains a typed cause attached to `defer`.

### Relative sufficiency rule

Evidence readiness is always relative to the selected action:

- normal review requires enough favorable and non-conflicting evidence for normal review;
- targeted checking requires enough evidence to identify one concrete unresolved question and a discriminating check;
- investigation/block requires enough evidence to identify a material failure or contradiction;
- defer requires enough evidence to identify a required condition that is temporarily unresolved or unavailable;
- abstention requires enough evidence to establish that the case or meaning lies outside the supported method.

Therefore `sufficient_for_action` does not mean sufficient to prove safety. It means sufficient to justify the bounded action actually returned.

## Initial contrast matrix

These are design hypotheses to test and refine before approval, not implemented rules.

| Contrast | Expected bounded result | Reason |
|---|---|---|
| S004-like evidence plus an approved official non-breaking/drop-in bug-fix claim and no contradiction | `proceed_to_normal_review` | Relevant exact-head CI exercised the update; authority and favorable upstream meaning are established; no material question justifies special work |
| Relevant exact-head CI exists but direct dependency exercise is unresolved, and one concrete repository command can answer the question | `run_targeted_checks` | A specific check can discriminate between proceeding and blocking |
| Relevant exact-head CI fails on the changed dependency path | `investigate_or_block` | Positive target evidence identifies a material concern |
| Required public source acquisition fails transiently or CI is still pending | `defer` | A required condition may become available later; stronger action would be premature |
| Package/source/provenance identities conflict | `investigate_or_block` | The evidence chain is contradictory and the PR should not proceed under untrusted upstream identity |
| Dependency syntax or source format is outside the supported B2 method | `abstain` | UpgradePilot cannot responsibly apply its decision rules |
| Authoritative release source is available but required meaning remains unresolved and no approved discriminating method or check exists | `abstain` under the current method | Missing meaning must not silently become favorable evidence |
| Upstream reports a breaking change or required migration while target evidence does not resolve its relevance | `run_targeted_checks` or `investigate_or_block`, depending on whether one bounded check can discriminate | The upstream claim is decision-critical and opposes immediate normal review |
| PR head, dependency set, requirements file, or workflow changes after acquisition | new run required | The decision is bound to frozen evidence and must not survive material identity change |

## Proposed stopping rule

Investigation should stop when:

```text
one bounded maintainer action is justified
+ all authority-critical conditions for that action are evaluated
+ no material contradiction remains hidden in acquired evidence
+ no supported additional stage is expected to change the action,
  material uncertainty, or required checks
```

Investigation should continue only when another supported stage can answer a named decision-relevant question and discriminate among materially different actions.

The amount of evidence collected, number of tests, or availability of unused investigation capacity is not itself a reason to continue.

## Why this is not an S004 detector

The proposed contract consumes typed variable evidence and explicitly supports multiple outcomes. It does not contain:

- `pytest`;
- version `9.0.3`;
- `googlefonts/glyphsLib`;
- the known release URL;
- the phrase `drop-in replacement` as a package-specific rule;
- the historical merge result;
- a fixed expectation that green CI produces normal review.

The contrast matrix requires the same method to react differently to unresolved CI, failed CI, transient absence, identity conflict, unsupported input, and contradictory upstream claims.

## Decisions recorded in this draft

1. The complete S004 evidence map is accepted as the closure of the plan's concrete walkthrough step.
2. Package/upstream authority remains a prerequisite gate, not favorable recommendation evidence.
3. Direct target CI exercise remains separate from upstream semantic meaning.
4. The first decision evaluator should consume typed evidence results rather than raw source material.
5. A decision result must preserve action, readiness, reasons, unresolved/conflicting evidence, required checks, stopping, limits, and rerun conditions.
6. `proceed_to_normal_review` is the leading clearer runtime name for the charter's `merge after normal review` class, but the name is not yet approved.
7. The contract, readiness vocabulary, outcome transitions, and contrast expectations remain proposals pending semantic-boundary resolution and Ali approval.

## Effect on the controlling plan

- Step 1, concrete S004 walkthrough and evidence-role classification, is complete at design-record level.
- Step 2, first decision-contract definition, has a complete initial draft.
- Steps 3 and 4, outcome boundaries and evidence sufficiency/stopping, have initial hypotheses but require contrast review.
- Step 5, upstream semantic boundary, remains the central unresolved method decision.
- No product source, test, dependency, runtime state, semantic method, or recommendation behavior changed.

## Exact next design questions

1. What smallest structured upstream-claim vocabulary is actually required by the first B2 method?
2. Is the current GitHub Release body sufficient for that vocabulary, or must one separately bound exact-version release-document format be acquired?
3. What is the simplest credible interpretation baseline that avoids package-specific phrase enumeration?
4. Which contrast mappings above need correction before they become approved rules?
5. Is temporary unavailability a separate evidence-readiness state or a typed cause attached to `defer`?
6. Should identity conflict map to `investigate_or_block`, `abstain`, or depend on whether the conflict is resolvable?

## References

- `../PROJECT_CHARTER.md`;
- `../plans/B2_TRANSPARENT_DECISION_METHOD_PLAN.md`;
- `2026-07-28_B2-transparent-decision-method.md`;
- `../product-simulation/scenarios/S004-glyphslib-pytest-9.0.2-to-9.0.3/artifacts/DECISION.json`;
- `../product-simulation/S004_POST_CASE_SYNTHESIS.md`;
- active source and tests named in the detailed evidence walkthrough.
