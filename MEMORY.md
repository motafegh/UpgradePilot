# UpgradePilot Current Memory

**Last updated:** 2026-07-28  
**Authority:** Sole repository owner of live project position, selected plan, latest relevant commit evidence, blockers, and exact continuation.

Stable route, specifications, ADRs, source, tests, and dated evidence retain their own responsibilities. They must not duplicate this live state.

## Live position

- **Route:** B2 — Public PR vertical slice.
- **Controlling route:** [`plans/UPGRADEPILOT_90_DAY_PLAN.md`](plans/UPGRADEPILOT_90_DAY_PLAN.md)
- **B2 gate definition:** [`plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md`](plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md)
- **Completed bounded plan:** [`plans/B2_MINIMUM_PACKAGE_AND_UPSTREAM_EVIDENCE_PLAN.md`](plans/B2_MINIMUM_PACKAGE_AND_UPSTREAM_EVIDENCE_PLAN.md)
- **Selected bounded plan:** [`plans/B2_TRANSPARENT_DECISION_METHOD_PLAN.md`](plans/B2_TRANSPARENT_DECISION_METHOD_PLAN.md)
- **Detailed evidence walkthrough:** [`working-memory/2026-07-28_B2-transparent-decision-method.md`](working-memory/2026-07-28_B2-transparent-decision-method.md)
- **Decision synthesis record:** [`working-memory/2026-07-28_B2-decision-evidence-map-and-contract-draft.md`](working-memory/2026-07-28_B2-decision-evidence-map-and-contract-draft.md)
- **Upstream semantic-boundary proposal:** [`working-memory/2026-07-28_B2-upstream-semantic-boundary.md`](working-memory/2026-07-28_B2-upstream-semantic-boundary.md)
- **Last behavior-validated repository revision in Ali's environment:** `bc5aafece111802b8151ccad1fd822e`.
- **CLI integration validation closure:** `4ff281565593f5e74f5f79491497c9b36363050f`.
- **Transparent-decision plan revision:** `2a6664f4fae17583afdfcdd59889f5fa3cd0ef06`.
- **Evidence walkthrough latest revision:** `27a72c5a36501eca16eca946777f1f4253d8232c`.
- **Decision synthesis revision:** `71e0a14735c39aceccd476412f746b21a5a3dce6`.
- **Semantic-boundary proposal revision:** `5b553602e9777292e8fb9359237aa55ea689d55e`.

B2 Increment D — Minimum package and upstream evidence — is complete. B2 Increment E — Transparent decision — remains selected under its dedicated bounded plan. The concrete S004 evidence walkthrough, complete decision-evidence map, first decision-contract draft, and upstream semantic-boundary proposal are now recorded. No semantic interpretation method, decision contract, recommendation policy, model/provider, or recommendation code has yet been approved or implemented.

Ali should continue to be onboarded through the real evidence-to-decision path. Explain every proposed semantic category, readiness state, and transition through the concrete problem it solves before approval or implementation.

## Verified integrated product evidence

Observed in Ali's WSL2 Python 3.12 environment after pulling revision `bc5aafece111802b8151ccad1fd822e`.

### Complete deterministic suite

```text
Ran 64 tests in 0.021s
OK
```

This includes the four CLI orchestration tests and the previous 60 source, acquisition, parsing, identity, reconciliation, and CI-authority tests.

### Integrated public command

```text
command: python3 -m upgradepilot googlefonts/glyphsLib 1145
repository: googlefonts/glyphsLib
PR: 1145
exact dependency: pytest 9.0.2 → 9.0.3
exact head: f3cda8a94600e58d27f1bc17c99b7693718b6350
CI authority: sufficient
package evidence: available
published package: pytest==9.0.3
distribution files: 2
upstream source: available
upstream repository: pytest-dev/pytest
provenance coverage: 2 of 2 files
provenance unavailable files: none
accepted tag: 9.0.3
release URL: https://github.com/pytest-dev/pytest/releases/tag/9.0.3
tag object SHA: 24ec4b54c06a74721a285dcc317825b1735f4717
claim state: unresolved_claim
```

The command preserved all previously validated PR, dependency, workflow, job, and CI-authority output and continued through package and upstream evidence in one execution.

## Permitted claims

### CI authority

> At least one successful exact-head CI path installed the changed requirements file and directly exercised pytest.

### Package identity

> PyPI published an exact release record for `pytest==9.0.3`, including the exact wheel and source-distribution identities and SHA-256 digests.

### Upstream source authority

> PyPI reports provenance for both exact `pytest==9.0.3` distribution files identifying `pytest-dev/pytest`; that repository agrees with the package's well-known Source candidate; and the exact `9.0.3` tag resolves to a published GitHub Release and exact tag-reference object.

### Integrated product path

> The public UpgradePilot command behavior-validly connects exact PR and dependency identity, bounded exact-head CI authority, exact PyPI package/file identity, PyPI-reported publisher provenance, matching upstream repository identity, and an exact GitHub Release/tag reference into one concise evidence report.

These claims do not establish:

- independent cryptographic verification of the PyPI attestation envelopes;
- complete CI coverage;
- release-prose meaning;
- target-repository compatibility or objective upgrade safety;
- a merge, targeted-check, investigate/block, defer, or abstain recommendation.

## Behavior-validated boundary

```text
public repository + PR number
→ validated locator and exact PR identity
→ complete changed-file acquisition
→ one supported exact pinned Python dependency update
→ exact-head workflow runs, jobs, and steps
→ exact-run workflow path
→ workflow definition at the same head SHA
→ bounded command evidence
→ sufficient, insufficient, or unresolved CI authority
→ trusted exact package + proposed version
→ official PyPI exact-release request
→ normalized package and exact-version validation
→ immutable distribution filename, URL, package type, and SHA-256 records
→ publisher-supplied project-link candidates
→ bounded per-file PyPI Integrity acquisition
→ PyPI-reported publisher identities
→ one canonical GitHub Source candidate
→ Source candidate and publisher repository agreement
→ accepted exact-version tag form
→ published GitHub Release
→ exact tag-ref object type and SHA
→ bounded release body
→ concise public CLI presentation
→ unresolved_claim; no semantic interpretation or recommendation
```

## Current implementation responsibilities

```text
json_contract.py       source-neutral JSON runtime value contracts
pypi_api.py            shared bounded mechanics for focused PyPI JSON clients
pypi_client.py         exact package/version and immutable distribution-file evidence
pypi_provenance.py     exact-file PyPI-reported provenance and publisher identities
github_api.py          GitHub HTTP/JSON boundary and GitHub-specific contract adapters
github_client.py       PR identity and changed files
github_actions.py      workflow runs, jobs, and step summaries
github_repository.py   exact-head repository-file acquisition
github_release.py      published release and exact tag-ref evidence
upstream_source.py     source/provenance/repository/version reconciliation
dependency_change.py   dependency interpretation
workflow_commands.py   bounded workflow command reading
ci_authority.py        deterministic CI-authority classification
cli.py                 complete evidence-stage orchestration and concise presentation
```

No source module yet owns release-claim interpretation, evidence sufficiency, investigation stopping, or maintainer-action evaluation.

## Accepted authority boundaries

### Shared mechanics rule

> Before adding helpers for a new external source, classify each behavior as source-neutral mechanics or source-specific evidence semantics. Reuse shared primitives only when the meaning is identical; keep authority, identity, and failure interpretation in the focused source boundary.

### Upstream source rule

```text
PyPI exact package/version/file identity
+ PyPI-reported exact-file publisher provenance
+ matching canonical GitHub Source candidate
+ one exact-version GitHub Release/tag reference
```

Stable constraints:

- project URL labels identify candidate intent only;
- a Source candidate alone is not upstream authority;
- provenance is queried for every exact distribution file;
- at least one usable exact-file provenance record is required;
- all usable GitHub publisher repositories must agree;
- valid non-GitHub provenance is unsupported, not malformed;
- Source and provenance repository identities must match;
- exactly one of `<version>` or `v<version>` may resolve;
- tag-reference object type and SHA are preserved;
- release body meaning remains unresolved in current code;
- UpgradePilot does not independently verify attestation cryptography;
- compatibility, safety, and final recommendation remain unestablished.

## Increment D completion

The completed minimum package and upstream evidence plan reached its stop line:

- exact package/version evidence is exposed through the public command;
- project-controlled exact-release source evidence is exposed through the public command;
- explicit unavailable, unsupported, mismatched, ambiguous, malformed, and acquisition-failed states are preserved;
- no package-specific runtime answer or recommendation was introduced;
- deterministic and live proof both passed.

The completed plan must not be extended informally into semantic interpretation.

## Increment E selected responsibility

The selected transparent-decision plan controls the movement from validated evidence to one bounded maintainer action or abstention:

```text
validated evidence
→ bounded decision-relevant interpretation
→ evidence sufficiency and stopping
→ maintainer action or abstention
→ reasons, uncertainty, required checks, and claim limits
```

The stable product responsibility remains broader than S004. S004 is the first control and live-proof candidate, not the product scope or hidden expected answer.

### Design progress recorded

The concrete evidence walkthrough now classifies:

- exact dependency/change identity as an admission requirement;
- direct successful exact-head dependency exercise as target-specific decision support;
- package/provenance/source/release binding as an authority prerequisite;
- filenames, historical merge status, and unclassified version shape as context rather than decision authority;
- contradiction evaluation, evidence sufficiency, stopping, and maintainer action as remaining unimplemented responsibilities.

The first contract draft proposes typed decision inputs, an explainable decision result, charter-aligned action vocabulary, evidence-readiness distinctions, a stopping rule, and materially different contrast cases.

The semantic-boundary proposal adds:

- four upstream claim categories: `fix_or_remediation`, `compatibility_assurance`, `interface_or_behavior_change`, and `support_boundary_change`;
- semantic states: `resolved`, `no_decision_relevant_claim`, `unresolved`, and `conflicting`;
- source-span grounding and deterministic validation invariants;
- a proposal to use the already acquired exact GitHub Release body as the first semantic source and not add pytest-specific release-document searching;
- a proposal that explicit compatibility assurance is supporting rather than universally mandatory for ordinary review;
- deterministic phrase matching as a disposable baseline only;
- bounded LLM structured extraction with deterministic validation as the leading credible candidate, pending Ali approval, experiment definition, ADR, model/provider selection, and proof;
- deterministic sufficiency, stopping, and maintainer-action evaluation remaining outside model control.

These remain design proposals. No semantic method or transition mapping is approved.

## Exact continuation

Follow [`plans/B2_TRANSPARENT_DECISION_METHOD_PLAN.md`](plans/B2_TRANSPARENT_DECISION_METHOD_PLAN.md) without implementing recommendation code yet:

1. onboard Ali through [`working-memory/2026-07-28_B2-upstream-semantic-boundary.md`](working-memory/2026-07-28_B2-upstream-semantic-boundary.md), especially the four claim categories, claim-relative source sufficiency, and the separation between upstream meaning and target facts;
2. challenge and refine the proposed S004 rule that explicit compatibility assurance is supporting rather than universally mandatory;
3. refine the action/readiness contrast matrix using `resolved`, `no_decision_relevant_claim`, `unresolved`, and `conflicting` semantic states;
4. resolve temporary-unavailability behavior and whether identity conflict maps to `investigate_or_block`, `abstain`, or a resolvability-dependent transition;
5. specify exact targeted-check activation and stopping conditions;
6. present the complete interpretation, sufficiency, stopping, and decision method to Ali for challenge and approval;
7. only after Ali approval, define the bounded semantic experiment and required ADR, select model/provider details proportionally, and begin implementation;
8. after approval, add controlled semantic and decision contrasts, run the complete suite, and perform one safe live S004 proof only after non-hardcoded behavior is established;
9. do not begin Increment F machine-readable/replay expansion until the transparent decision boundary is behavior-validated.

## Product boundaries affecting continuation

Do not yet:

- independently claim cryptographic attestation verification;
- search arbitrary tag patterns or package-specific release paths;
- recursively search repository trees without a separately admitted source-format rule;
- interpret release prose through package-specific phrases or fixture wording;
- produce compatibility, safety, merge, targeted-check, investigate/block, defer, or abstain recommendations before the method is approved;
- treat the historical maintainer merge or manual S004 answer as correctness proof;
- hardcode pytest, version `9.0.3`, the known release URL, announcement path, control-case wording, or expected outcome;
- add a model, semantic service, persistence, replay infrastructure, agents, queues, or deployment layers without Ali approval and separately admitted responsibility;
- mutate a target repository or require private access.

## Detailed dated evidence

- [`working-memory/B2_TECHNICAL_PROGRESS.md`](working-memory/B2_TECHNICAL_PROGRESS.md)
- [`working-memory/2026-07-27_B2-PYPI_source-selection-and-identity-slice.md`](working-memory/2026-07-27_B2-PYPI_source-selection-and-identity-slice.md)
- [`working-memory/2026-07-27_B2-shared-external-source-foundation-investigation.md`](working-memory/2026-07-27_B2-shared-external-source-foundation-investigation.md)
- [`working-memory/2026-07-27_B2-project-controlled-exact-release-source-resolution.md`](working-memory/2026-07-27_B2-project-controlled-exact-release-source-resolution.md)
- [`working-memory/2026-07-28_B2-package-and-upstream-CLI-integration.md`](working-memory/2026-07-28_B2-package-and-upstream-CLI-integration.md)
- [`working-memory/2026-07-28_B2-transparent-decision-method.md`](working-memory/2026-07-28_B2-transparent-decision-method.md)
- [`working-memory/2026-07-28_B2-decision-evidence-map-and-contract-draft.md`](working-memory/2026-07-28_B2-decision-evidence-map-and-contract-draft.md)
- [`working-memory/2026-07-28_B2-upstream-semantic-boundary.md`](working-memory/2026-07-28_B2-upstream-semantic-boundary.md)

## State-maintenance rule

When stage, selected plan, latest verified behavior, blocker, or exact continuation changes, update this file only. Change another file only when that file's stable route, requirement, decision, source behavior, test behavior, or dated historical evidence changes.