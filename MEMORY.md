# UpgradePilot Current Memory

**Last updated:** 2026-07-28  
**Authority:** Sole repository owner of live project position, selected plan, latest relevant commit evidence, blockers, and exact continuation.

Stable route, specifications, ADRs, source, tests, and dated evidence retain their own responsibilities. They must not duplicate this live state.

## Live position

- **Route:** B2 — Public PR vertical slice.
- **Controlling route:** [`plans/UPGRADEPILOT_90_DAY_PLAN.md`](plans/UPGRADEPILOT_90_DAY_PLAN.md)
- **B2 gate definition:** [`plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md`](plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md)
- **Completed bounded plan:** [`plans/B2_MINIMUM_PACKAGE_AND_UPSTREAM_EVIDENCE_PLAN.md`](plans/B2_MINIMUM_PACKAGE_AND_UPSTREAM_EVIDENCE_PLAN.md)
- **Last behavior-validated repository revision in Ali's environment:** `bc5aafece111802f1e777dd2b8151ccad1fd822e`.
- **CLI integration validation closure:** `4ff281565593f5e74f5f79491497c9b36363050f`.

B2 Increment D — Minimum package and upstream evidence — is complete. The public command now behavior-validly exposes the full admitted evidence chain. B2 continues at Increment E — Transparent decision — but no recommendation method has yet been selected or implemented.

## Verified integrated product evidence

Observed in Ali's WSL2 Python 3.12 environment after pulling revision `bc5aafece111802f1e777dd2b8151ccad1fd822e`.

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
- a merge, defer, or block recommendation.

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
- release body meaning remains unresolved;
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

## Exact continuation

Perform one bounded Increment E transparent-decision design before adding recommendation code:

1. create a dated working-memory record for the B2 transparent-decision method;
2. state the exact supported maintainer question and the strongest recommendation or abstention claim the first method may produce;
3. inventory which current evidence fields can be decisive and which remain only contextual;
4. define explicit decision result states, including recommendation, abstention, unresolved evidence, conflicting evidence, and unsupported case behavior;
5. determine whether the current GitHub Release body is sufficient input for the first control case or whether exact-tag release-document acquisition must be admitted first;
6. compare the smallest transparent deterministic baseline with credible semantic alternatives without hardcoding pytest, version `9.0.3`, known wording, or the historical merge outcome;
7. define how CI authority and upstream claims combine without turning either into objective safety proof;
8. specify explanation, uncertainty, and claim-limit output required for every result;
9. identify minimum controlled tests and one safe live proof;
10. present the decision method, tradeoffs, and proposed source/interpretation boundary to Ali for approval;
11. implement only after approval.

Do not begin Increment F machine-readable/replay expansion until the transparent decision boundary is proven.

## Product boundaries affecting continuation

Do not yet:

- independently claim cryptographic attestation verification;
- search arbitrary tag patterns or package-specific release paths;
- recursively search repository trees without a separately admitted source-format rule;
- interpret release prose through package-specific phrases or fixture wording;
- produce compatibility, safety, merge, defer, or block recommendations before the decision method is selected;
- treat the historical maintainer merge as correctness proof;
- hardcode pytest, version `9.0.3`, the known release URL, announcement path, or control-case wording;
- add a model, semantic service, persistence, replay infrastructure, agents, queues, or deployment layers without a separately admitted responsibility;
- mutate a target repository or require private access.

## Detailed dated evidence

- [`working-memory/B2_TECHNICAL_PROGRESS.md`](working-memory/B2_TECHNICAL_PROGRESS.md)
- [`working-memory/2026-07-27_B2-PYPI_source-selection-and-identity-slice.md`](working-memory/2026-07-27_B2-PYPI_source-selection-and-identity-slice.md)
- [`working-memory/2026-07-27_B2-shared-external-source-foundation-investigation.md`](working-memory/2026-07-27_B2-shared-external-source-foundation-investigation.md)
- [`working-memory/2026-07-27_B2-project-controlled-exact-release-source-resolution.md`](working-memory/2026-07-27_B2-project-controlled-exact-release-source-resolution.md)
- [`working-memory/2026-07-28_B2-package-and-upstream-CLI-integration.md`](working-memory/2026-07-28_B2-package-and-upstream-CLI-integration.md)

## State-maintenance rule

When stage, selected plan, latest verified behavior, blocker, or exact continuation changes, update this file only. Change another file only when that file's stable route, requirement, decision, source behavior, test behavior, or dated historical evidence changes.
