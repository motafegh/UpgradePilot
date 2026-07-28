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

### 2026-07-28 — S004 dependency shape and role walkthrough

**Observation**

The active `dependency_change.py` evaluator establishes exactly one same-file transition of the form `package==old_version` to `package==new_version`. It requires complete visible patch evidence, one removed pin, one added pin, the same normalized package identity, a changed version string, and an in-place modified file.

For a supported result, `PinnedDependencyChange` stores only:

```text
source_file
package
normalized_package
old_version
proposed_version
```

It does not store a dependency-role classification such as `development`, `test`, or `runtime`. It also does not classify the version transition as patch, minor, or major. The current CLI prints those same source-file, package, and version facts without adding either classification.

The tests prove that the extractor accepts one complete exact-pin replacement and abstains on missing patch evidence, unsupported range syntax, package mismatch, multiple pinned changes, and incomplete patch evidence. The test fixture uses `requirements-dev.txt`, but no assertion treats that filename as a formal dependency-role rule.

The separate CI-authority path does establish that one successful exact-head workflow installs the changed `requirements-dev.txt` and directly invokes pytest. The historical manual evidence additionally inspected `requirements-dev.in` and `tox.ini`, where pytest appears with test tooling and the tox test environment installs `requirements-dev.txt` before invoking pytest.

**Interpretation**

The product currently proves a strong bounded change-shape claim:

> The PR contains exactly one supported same-file exact-pin transition for pytest from `9.0.2` to `9.0.3`.

It also proves an operational role claim when combined with CI authority:

> The changed pytest declaration belongs to at least one exercised CI test path.

That operational claim is stronger and more defensible than inferring `development dependency` from the filename alone. However, it is narrower than a general repository-wide semantic classification that pytest is exclusively a development/test dependency in every context.

A human can recognize `9.0.2` to `9.0.3` as a patch-like numeric transition, and the historical simulation used that interpretation. The current product has not established a version-classification contract or parser, so `patch update` is not yet a product-supported fact.

The decision significance of these facts differs:

- exactly one complete pin transition is decisive for admission to the current B2 slice and limits ambiguity;
- the source filename is contextual evidence, not sufficient role authority by itself;
- proven installation and invocation in a test workflow is decision-relevant target context;
- a patch/minor/major label remains unresolved product meaning until a justified classifier is admitted.

**Decision**

Do not add a broad dependency-role classifier or version-transition classifier during this walkthrough.

For the first decision design, prefer the directly evidenced statement `changed dependency is installed and exercised in a successful exact-head CI test path` over the broader label `development dependency` unless additional evidence and a stable role contract justify that label.

Preserve exact old and proposed version strings as trusted input. Determine later whether the first transparent decision actually requires an explicit patch/minor/major classification; if it does, compare the smallest standards-aware method rather than implementing numeric string splitting or treating Dependabot wording as authority.

**Effect**

- plan question 4 gains a concrete evidence inventory for change shape and role;
- the future decision contract should not assume that `source_file` implies dependency role;
- the decision method may consume the existing CI exercise relationship directly without inventing a broader role taxonomy;
- version transition category remains an open derived input rather than an established fact;
- no source, test, dependency, or runtime output changed.

**Reference**

- `src/upgradepilot/dependency_change.py`;
- `tests/test_dependency_change.py`;
- `src/upgradepilot/workflow_commands.py`;
- `src/upgradepilot/ci_authority.py`;
- `src/upgradepilot/cli.py`;
- `pyproject.toml`;
- `product-simulation/scenarios/S004-glyphslib-pytest-9.0.2-to-9.0.3/artifacts/raw/ev-003-direct-role-and-tox-path.txt`.

### 2026-07-28 — S004 package identity, provenance, and upstream binding walkthrough

**Observation**

The active package and upstream path uses a layered exact-identity chain rather than trusting one plausible release link:

```text
trusted proposed package + exact version
→ exact PyPI release response
→ returned package-name and version validation
→ immutable distribution filename, URL, package type, and SHA-256 records
→ PyPI Integrity lookup for each exact distribution file
→ PyPI-reported publisher kind, repository, and workflow
→ canonical GitHub Source candidate from package metadata
→ Source candidate and provenance publisher repository agreement
→ exactly one accepted exact-version tag form
→ published GitHub Release and exact tag-reference object
```

`pypi_client.py` rejects a successful response when the returned normalized package name or exact version conflicts with the request. It preserves every distribution filename and SHA-256 digest and rejects malformed digests or duplicate filenames. Publisher-supplied project URLs are stored as candidates; the `Source` label does not establish authority by itself.

`pypi_provenance.py` queries provenance for an exact distribution that must belong to the supplied exact release evidence. It preserves the file identity and PyPI-reported publisher identities. Its contract explicitly does not claim that UpgradePilot independently verified the attestation envelopes.

`upstream_source.py` requires usable exact-file provenance, supported GitHub publisher identity, one agreeing publisher repository, agreement between that publisher repository and the package's canonical GitHub Source candidate, and exactly one published GitHub Release among the accepted `<version>` and `v<version>` tag forms. A provenance/source mismatch stops before GitHub release acquisition; conflicting Source candidates or two resolving tag forms remain ambiguous.

For the live S004 control, the integrated command established:

```text
published package: pytest==9.0.3
distribution files: 2
provenance coverage: 2 of 2
provenance unavailable files: none
upstream repository: pytest-dev/pytest
accepted tag: 9.0.3
published GitHub Release: available
exact tag object SHA: 24ec4b54c06a74721a285dcc317825b1735f4717
claim state: unresolved_claim
```

**Interpretation**

This chain answers an authority and binding question:

> Is the release material being considered tied to the exact proposed PyPI package/version and to the GitHub project PyPI reports as publishing the exact distribution files?

For S004, the bounded answer is yes. The chain prevents UpgradePilot from silently interpreting:

- a different package with a similar name;
- a different version returned by a successful endpoint;
- a package metadata URL whose repository conflicts with exact-file publisher provenance;
- two competing source repositories;
- a release under an ambiguous exact-version tag form;
- a plausible GitHub release that is not bound to the accepted package/upstream identity chain.

This is primarily an authority gate, not favorable compatibility evidence. It establishes that later release-content interpretation is attached to the correct admitted package, version, publisher repository, published release, and tag reference. It does not establish:

- semantic meaning of the release body;
- that the release is compatible with the target repository;
- objective update safety;
- complete equivalence between GitHub source content and the published distribution bytes;
- independent cryptographic verification of PyPI's attestation envelopes;
- a normal-review, targeted-check, block, defer, or abstain decision.

The evidence roles are materially different:

- exact PyPI name/version equality is decisive for package identity;
- distribution filenames and SHA-256 digests preserve exact immutable file identities;
- the package Source URL is a discovery candidate and contextual corroboration, not authority alone;
- exact-file PyPI-reported publisher provenance is decisive for the supported publisher-repository binding, within the stated non-verification limit;
- repository agreement prevents source substitution;
- exact published release and tag-reference evidence bind the acquired release source to one accepted exact-version Git identity;
- `unresolved_claim` correctly preserves the separate semantic gap.

**Decision**

Preserve package/upstream identity as a prerequisite evidence gate for semantic interpretation and later decision evaluation. Do not treat `Upstream source: available`, full provenance coverage, or an exact tag as a positive recommendation signal by themselves.

The first transparent decision contract should consume the typed package/upstream result and its explicit problem states rather than reconstructing authority from raw URLs in the decision evaluator. A later method may decide how unavailable, mismatched, ambiguous, unsupported, or malformed authority evidence affects the maintainer outcome, but that mapping is not selected during this walkthrough.

Preserve the claim limit that PyPI provenance is PyPI-reported evidence. Do not claim independent attestation verification or source-to-distribution reproducibility.

**Effect**

- plan question 4 gains a complete evidence-role classification for package identity, file identity, provenance, repository agreement, and exact release/tag binding;
- package/upstream authority is identified as a prerequisite gate that makes semantic release claims admissible, not as independent evidence that an update should proceed;
- identity mismatch and ambiguity are confirmed as materially different from missing semantic meaning;
- the future decision method should accept typed authority outcomes and preserve their reasons and claim limits;
- no source, test, dependency, semantic method, or recommendation behavior changed.

**Reference**

- `src/upgradepilot/pypi_client.py`;
- `src/upgradepilot/pypi_provenance.py`;
- `src/upgradepilot/upstream_source.py`;
- `src/upgradepilot/github_release.py`;
- `tests/test_pypi_client.py`;
- `tests/test_pypi_provenance.py`;
- `tests/test_upstream_source.py`;
- `working-memory/2026-07-28_B2-package-and-upstream-CLI-integration.md`.

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
