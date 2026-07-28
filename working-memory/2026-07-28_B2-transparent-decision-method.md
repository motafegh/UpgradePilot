# B2 Transparent Decision Method Working Record

**Date opened:** 2026-07-28  
**Operation:** B2 Increment E transparent-decision method design and proof  
**Controlling bounded plan:** [`../plans/B2_TRANSPARENT_DECISION_METHOD_PLAN.md`](../plans/B2_TRANSPARENT_DECISION_METHOD_PLAN.md)  
**Plan creation revision:** `2a6664f4fae17583afdfcdd59889f5fa3cd0ef06`  
**Starting repository revision:** `c62c2dae0eef16617fb597dd95d0a3bee3c56800`  
**Local result classification:** Opened; design discussion captured; no decision method selected or implemented

## Objective

Preserve the material observations, decisions, alternatives, uncertainties, controlled examples, implementation results, and validation evidence produced while UpgradePilot moves from its behavior-validated evidence engine to one transparent bounded maintainer decision.

The work should be learned through the real S004 request-to-output path before abstract contracts or modules are finalized.

## Context entering the operation

The public CLI has behavior-validly established this evidence chain:

```text
public repository + PR number
→ exact PR and changed-file identity
→ one supported exact pinned Python dependency update
→ bounded exact-head CI authority
→ exact PyPI package/version and distribution files
→ PyPI-reported publisher provenance
→ matching project-controlled GitHub repository
→ exact GitHub Release and tag-reference object
→ unresolved_claim
```

The complete deterministic suite passed with 64 tests, and the live S004 command preserved the earlier PR/dependency/CI output while adding package and upstream evidence.

What is not yet established:

- release-prose meaning;
- evidence sufficiency for a maintainer action;
- investigation stopping or conditional-stage activation in product code;
- a merge-after-review, targeted-check, investigate/block, defer, or abstain result;
- a tested explanation and claim-limit contract.

## Stable scope confirmed during the discussion

The permanent UpgradePilot responsibility is not limited to S004. The controlling product question is:

> For an admitted public Python Dependabot dependency-update pull request, what bounded maintainer action is justified by the decision-relevant evidence available for that case?

The charter's broad outcome classes remain:

1. merge after normal review;
2. run targeted checks;
3. investigate or block;
4. defer;
5. abstain.

S004 is the first successful control case and live proof candidate. It must not become the product scope, a phrase-matching rule, or a hidden expected answer.

## Important distinctions reached in discussion

### Product question versus investigation questions

UpgradePilot has one owning maintainer question: what bounded action is justified for the PR.

Individual investigations answer narrower questions only when needed, for example:

- did exact-head CI install and exercise the proposed dependency?;
- does the exact package release exist?;
- is the upstream source authoritative for the exact version?;
- what bounded claim does upstream make?;
- does an unresolved question justify a targeted check?;
- can further investigation change the action, required check, or material uncertainty?

### Evidence availability versus evidence sufficiency

```text
evidence acquired
≠
evidence interpreted
≠
evidence sufficient for a particular action
≠
upgrade proven objectively safe
```

“Enough evidence” must be evaluated relative to one permitted maintainer action. It should not be a generic boolean or confidence score.

### B2 slice versus permanent product scope

```text
permanent project responsibility
    evidence-backed public Python Dependabot decisions

B2 vertical slice
    first narrow real end-to-end supported evidence and decision path

S004 control
    one concrete case used to learn, design, test, and prove that path
```

### Human authority remains

A result such as ordinary review means the PR may continue through the repository's normal human process. It does not authorize automatic merge, replace maintainer review, or establish universal compatibility or safety.

## Current concrete control

S004 identity:

```text
repository: googlefonts/glyphsLib
PR: 1145
dependency: pytest 9.0.2 → 9.0.3
role observed manually: pinned development/test dependency
CI authority: sufficient for at least one exact-head path
package evidence: exact pytest==9.0.3 available
upstream repository: pytest-dev/pytest
provenance: 2 of 2 distribution files
accepted tag: 9.0.3
claim state in product: unresolved_claim
```

The historical manual simulation selected `merge_after_normal_review` after additionally confirming an official drop-in bug-fix characterization and no decision-critical contradiction. That result is a design oracle and comparison case, not implementation proof.

## Questions to resolve through the plan

The record should accumulate evidence for these questions rather than answering them by intuition:

1. What exact input and output contract does the first B2 decision method need?
2. What do the charter outcome classes mean operationally in product behavior?
3. What sufficiency states are materially distinct and necessary?
4. Which current evidence fields are decisive, contextual, missing, or potentially contradictory?
5. What exact upstream semantic claim is needed for the first method?
6. Is the acquired exact-tag GitHub Release body sufficient source input?
7. What is the simplest credible semantic baseline, and what alternatives merit comparison?
8. How do CI authority and upstream claims combine without becoming a safety proof?
9. When should investigation stop, activate a targeted stage, block, defer, or abstain?
10. What controlled contrasts prove the method is not an S004 detector?
11. What must Ali explain, modify, test, or diagnose for ownership practice?

## Working-record discipline

Append only material developments under the dated log below. Each entry should separate:

- **Observation:** source, command, code, output, or case fact actually inspected;
- **Interpretation:** what the observation may mean and its uncertainty;
- **Decision:** accepted, rejected, deferred, or still open method choice;
- **Effect:** which contract, plan question, test, implementation, or claim limit changes;
- **Reference:** source file, commit, test, command, or preserved artifact.

Do not turn this file into a second live tracker. `../MEMORY.md` remains the sole owner of selected status and exact continuation.

## Dated progress log

### 2026-07-28 — Record opened

**Observation**

No dedicated Increment E bounded plan existed. The repository had the broad B2 gate, the completed Increment D plan, and an exact continuation in `MEMORY.md` requiring a transparent-decision design before recommendation code.

**Interpretation**

The design responsibility is material enough to require one bounded plan and one dated evidence trail. It spans semantic interpretation, sufficiency, stopping, decision policy, explanation, tests, and a live proof; relying only on chat history would create avoidable ambiguity.

**Decision**

Created and referenced [`../plans/B2_TRANSPARENT_DECISION_METHOD_PLAN.md`](../plans/B2_TRANSPARENT_DECISION_METHOD_PLAN.md). The plan starts with the concrete S004 flow, then derives contracts and method choices, presents them for Ali approval, and permits implementation only afterward.

**Effect**

No product source or test behavior changed. No semantic method, decision rule, runtime state name, dependency, service, model, or architecture was selected.

**Reference**

- plan revision: `2a6664f4fae17583afdfcdd59889f5fa3cd0ef06`;
- behavior-validated source revision entering the operation: `bc5aafece111802f1e777dd2b8151ccad1fd822e`;
- prior live-state revision: `c62c2dae0eef16617fb597dd95d0a3bee3c56800`.

### 2026-07-28 — S004 upstream source sufficiency walkthrough

**Observation**

The exact GitHub Release body acquired by the current product for tag `9.0.3` is an official pytest release record with a titled `Bug fixes` section and individual fix entries. It does not contain the statement that the release is a drop-in replacement.

The historical manual S004 evidence instead used the exact tagged repository announcement at `doc/en/announce/release-9.0.3.rst`. That announcement explicitly states that pytest `9.0.3` is a bug-fix release and a drop-in replacement.

The manual interpretation layer preserved this as an attributed official-upstream claim and separately limited target-specific confirmation to repository CI.

**Interpretation**

The current product-acquired GitHub Release body appears sufficient to establish a narrow attributed claim that the exact release contains bug fixes. It is not sufficient to establish the stronger S004 decision-critical claim that upstream presents the release as a drop-in replacement.

Therefore `claim_state="unresolved_claim"` remains accurate for the full manual S004 upstream condition. The gap is not source authority or version identity; those are established. The gap is source-content sufficiency for the exact semantic claim used by the manual decision.

This also demonstrates why evidence acquisition and evidence sufficiency are separate responsibilities: an authoritative exact-version source can be available while lacking the content required for a particular maintainer action.

**Decision**

Do not yet select a semantic interpretation method, emit a recommendation, or broaden acquisition automatically. Preserve the named question:

> Is the existing exact-tag GitHub Release body sufficient for the first general B2 decision method, or must one additional generalizable exact-tag release-document source format be admitted?

The answer must be evaluated across the B2 responsibility rather than solved through a pytest-specific path or phrase.

**Effect**

- plan question 5 is narrowed to the structured claims that the first method truly needs;
- plan question 6 has a concrete partial answer for S004: the current GitHub Release body supports bug-fix content but not the historical drop-in replacement claim;
- no source, test, runtime contract, or recommendation behavior changed;
- the next walkthrough should classify the other S004 evidence items by what decision question they answer and what claim limit remains.

**Reference**

- current exact GitHub Release: `https://github.com/pytest-dev/pytest/releases/tag/9.0.3`;
- historical tagged announcement: `product-simulation/scenarios/S004-glyphslib-pytest-9.0.2-to-9.0.3/artifacts/raw/ev-006-upstream-release.rst`;
- historical interpretation: `product-simulation/scenarios/S004-glyphslib-pytest-9.0.2-to-9.0.3/artifacts/CLAIMS_AND_INTERPRETATIONS.jsonl`.

### 2026-07-28 — S004 CI-authority contribution walkthrough

**Observation**

The current `ci_authority.py` rule classifies CI as `sufficient` when at least one successful exact-head workflow installs the changed requirements file and directly invokes the changed package. It preserves all per-workflow assessments, including unresolved workflows, rather than treating one sufficient path as proof that every workflow is understood.

For S004, the accepted evidence chain is:

```text
pytest is pinned in requirements-dev.txt
→ the owning test configuration installs requirements-dev.txt
→ the test command invokes pytest
→ the exact-head pull-request workflow executes that path
→ a completed successful job is observed
```

The separate regression workflow also reinstalled the changed requirements and directly invoked pytest, then passed.

**Interpretation**

`CI authority: sufficient` answers a bounded target-repository question:

> Did at least one successful exact-head CI path consume the proposed dependency declaration and directly exercise the changed package?

For S004, the answer is yes. This makes the green result relevant to the proposed pytest update rather than merely coincidental repository CI.

The result does not establish complete coverage, behavior in every environment, absence of hidden incompatibility, production runtime safety, objective upgrade safety, or the final maintainer action. It is strong target-specific supporting evidence, but it is not independently sufficient for `merge_after_normal_review`.

This also explains why the unresolved `Test + Deploy` workflow does not cancel the sufficient `Regression Tests` path: the current rule is existential for the narrow exercise claim. Conversely, one sufficient path must not be promoted into a universal coverage claim.

**Decision**

Preserve CI authority as a distinct decision input with its existing narrow status vocabulary and claim limits. Do not reinterpret `sufficient` as `safe`, `compatible`, or `recommend merge`.

Do not yet freeze how `sufficient`, `insufficient`, or `unresolved` CI maps to the charter's maintainer outcomes. That mapping must be evaluated together with dependency role, upstream claims, contradictions, and any justified targeted check.

**Effect**

- plan question 4 gains a concrete classification: S004 CI authority is decision-relevant and potentially decisive against unnecessary targeted testing, but it cannot alone select the final action;
- plan question 8 gains a required invariant: CI authority and upstream claims must remain separate inputs whose combination may support a bounded action without becoming a safety proof;
- future decision output must preserve the exact CI claim and its limitations;
- no decision policy, source module, test, or runtime output changed.

**Reference**

- `src/upgradepilot/ci_authority.py`;
- `product-simulation/scenarios/S004-glyphslib-pytest-9.0.2-to-9.0.3/artifacts/EVIDENCE_ITEMS.jsonl`;
- `product-simulation/scenarios/S004-glyphslib-pytest-9.0.2-to-9.0.3/artifacts/CLAIMS_AND_INTERPRETATIONS.jsonl`;
- live CLI output validated in Ali's environment on 2026-07-28.

## Checks performed at opening

- searched the repository for a dedicated transparent-decision or Increment E plan;
- reviewed `AGENTS.md` ownership and document-routing rules;
- reviewed `working-memory/README.md` creation and record requirements;
- reviewed the completed Increment D bounded plan and its semantic stop line;
- reviewed `MEMORY.md` exact continuation;
- reviewed the controlling charter's user, decision classes, product definition, and claim limits;
- confirmed that no product implementation was authorized by opening this record.

## Remaining uncertainty at opening

- exact runtime outcome names and contract shapes;
- whether evidence sufficiency is represented as one result or part of a larger decision result;
- minimum semantic claim taxonomy;
- accepted interpretation method;
- whether the current release body is sufficient source input;
- minimum contrast set required before implementation;
- implementation module boundaries;
- final controlled and live proof obligations beyond the bounded plan.
