# UpgradePilot Current Memory

**Last updated:** 2026-07-28  
**Authority:** Sole repository owner of live project position, selected plan, latest relevant commit evidence, blockers, and exact continuation.

Stable route, specifications, ADRs, source, tests, and dated evidence retain their own responsibilities. They must not duplicate this live state.

## Live position

- **Route:** B2 — Public PR vertical slice.
- **Controlling route:** [`plans/UPGRADEPILOT_90_DAY_PLAN.md`](plans/UPGRADEPILOT_90_DAY_PLAN.md)
- **B2 gate definition:** [`plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md`](plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md)
- **Selected bounded plan:** [`plans/B2_MINIMUM_PACKAGE_AND_UPSTREAM_EVIDENCE_PLAN.md`](plans/B2_MINIMUM_PACKAGE_AND_UPSTREAM_EVIDENCE_PLAN.md)
- **Last behavior-validated source/test implementation:** `bf4ede1d6e902b22fda384d6d43339efe46bab8f`.
- **Latest CLI source/test integration awaiting validation:** `2303f453a71948579ab2c48555314ed14fea25a3`.
- **Dated CLI integration record:** `78b4b70263b76e9b45e36f1a6784aafa914ee63c`.

The provenance-backed GitHub Release/tag source boundary remains behavior-validated. The already validated package and upstream evidence are now integrated into the public CLI on `main`, but the integrated command path has not yet passed the complete suite or a live command in Ali's environment.

Do not begin semantic interpretation or further B2 product work until this integration validation gate passes.

## Previously verified product evidence

### Target-repository and CI evidence

Observed in Ali's WSL2 Python 3.12 environment:

```text
public command: python3 -m upgradepilot googlefonts/glyphsLib 1145
exact dependency: pytest 9.0.2 → 9.0.3
exact head: f3cda8a94600e58d27f1bc17c99b7693718b6350
exact-head workflow runs: 2
Regression Tests: sufficient direct install-and-pytest authority
Test + Deploy: unresolved because multiple jobs were not combined heuristically
overall CI authority: sufficient
```

Permitted CI claim:

> At least one successful exact-head CI path installed the changed requirements file and directly exercised pytest.

A previous HTTP `401` occurred only while an unusable local `GITHUB_TOKEN` variable was set. Anonymous public acquisition succeeded after removing it. No token value was exposed or recorded.

### Package-registry identity evidence

Observed and revalidated in Ali's environment:

```text
live PyPI request: https://pypi.org/pypi/pytest/9.0.3/json
result type: PackageReleaseEvidence
state: available
requested identity: pytest==9.0.3
published identity: pytest==9.0.3
distribution files: 2
wheel SHA-256: 2c5efc453d45394fdd706ade797c0a81091eccd1d6e4bccfcd476e2b8e0ab5d9
sdist SHA-256: b86ada508af81d19edeb213c681b1d48246c1a91d304c6c81a427674c17eb91c
```

Permitted package claim:

> The implemented live client established that PyPI published an exact release record for `pytest==9.0.3` and preserved its exact distribution-file identities and publisher-supplied project-link candidates.

### Project-controlled exact-release source evidence

Observed after the complete active suite passed:

```text
editable installation succeeded
60 active repository tests passed in 0.012 seconds
live upstream result: UpstreamReleaseEvidence
state: available
repository: pytest-dev/pytest
claim state: unresolved_claim
usable provenance: wheel and sdist
publisher for both files: GitHub / pytest-dev/pytest / deploy.yml
provenance unavailable files: none
accepted tag: 9.0.3
release URL: https://github.com/pytest-dev/pytest/releases/tag/9.0.3
tag ref: refs/tags/9.0.3
tag object type: tag
tag object SHA: 24ec4b54c06a74721a285dcc317825b1735f4717
published at: 2026-04-07T17:16:45Z
prerelease: false
release body characters: 2136
```

Permitted upstream-source claim:

> PyPI reports provenance for both exact `pytest==9.0.3` distribution files identifying `pytest-dev/pytest`; that repository agrees with the package's well-known Source candidate; and the exact `9.0.3` tag resolves to a published GitHub Release and exact tag-reference object.

The implementation does not independently verify attestation cryptography. The release-body meaning remains unresolved.

Detailed dated evidence:

- [`working-memory/B2_TECHNICAL_PROGRESS.md`](working-memory/B2_TECHNICAL_PROGRESS.md)
- [`working-memory/2026-07-27_B2-PYPI_source-selection-and-identity-slice.md`](working-memory/2026-07-27_B2-PYPI_source-selection-and-identity-slice.md)
- [`working-memory/2026-07-27_B2-shared-external-source-foundation-investigation.md`](working-memory/2026-07-27_B2-shared-external-source-foundation-investigation.md)
- [`working-memory/2026-07-27_B2-project-controlled-exact-release-source-resolution.md`](working-memory/2026-07-27_B2-project-controlled-exact-release-source-resolution.md)
- [`working-memory/2026-07-28_B2-package-and-upstream-CLI-integration.md`](working-memory/2026-07-28_B2-package-and-upstream-CLI-integration.md)

## Last behavior-validated boundary

```text
public repository + PR number
→ validated locator and exact PR identity
→ complete changed-file acquisition
→ one supported exact pinned Python dependency update
→ exact-head workflow runs, jobs, and steps
→ exact-run workflow path
→ workflow definition at the same head SHA
→ bounded single-job command evidence
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
→ unresolved_claim; no semantic interpretation
```

## New implementation awaiting validation

The public CLI now orchestrates the full validated evidence chain:

```text
python3 -m upgradepilot <repository> <pull-number>
→ existing PR/dependency/CI output
→ Package evidence: available or exact package problem state
→ exact published package/version and distribution-file count
→ Upstream source: available or exact upstream problem state
→ repository, provenance coverage, unavailable files, accepted tag,
  release URL, tag-object SHA, and unresolved claim state
```

Implemented behavior:

- `PyPIReleaseClient` runs only after a supported pinned dependency is established;
- `UpstreamSourceResolver` runs only after successful package evidence;
- package and upstream problem states are printed without guessing or crashing;
- unsupported dependency extraction explicitly leaves CI, package, and upstream not evaluated;
- the full release body is not printed;
- normal unsupported, unavailable, malformed-evidence, and unresolved result values preserve the existing completed-analysis exit status;
- existing exceptional GitHub PR/CI input and acquisition exit behavior is unchanged.

Current implementation responsibilities:

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
cli.py                 full evidence-stage orchestration and concise presentation
```

Four controlled CLI tests were added for full success, package stopping, upstream stopping, and unsupported-dependency stage skipping. They still require execution inside the complete active suite.

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

## Exact continuation

Validate the integrated command path before any semantic or later B2 work:

1. pull the latest `main` in Ali's WSL2 environment;
2. install editably with Python 3.12;
3. run the complete active unittest suite—expected count is **64** if no unrelated tests changed;
4. review and repair any regression directly on `main`;
5. ensure an unusable `GITHUB_TOKEN` is not set for the anonymous public proof;
6. run `python3 -m upgradepilot googlefonts/glyphsLib 1145`;
7. verify the existing PR, dependency, and CI evidence remains unchanged;
8. verify package evidence reports `pytest==9.0.3` and two distribution files;
9. verify upstream evidence reports `pytest-dev/pytest`, provenance `2 of 2`, tag `9.0.3`, the exact release URL and tag-object SHA, and `unresolved_claim`;
10. verify no full release body or recommendation is printed;
11. after the suite and live command pass, close the dated integration record, update this live state, and decide the next bounded product action.

## Product boundaries affecting continuation

Do not yet:

- independently claim cryptographic attestation verification;
- search arbitrary tag patterns or package-specific release paths;
- recursively search repository trees for release documents;
- interpret release prose;
- produce compatibility, safety, or final maintainer recommendations;
- hardcode pytest, version `9.0.3`, a known release URL, or control-case wording;
- add a model, semantic service, persistence, replay infrastructure, agents, queues, or deployment layers;
- mutate a target repository or require private access.

## State-maintenance rule

When stage, selected plan, latest verified behavior, blocker, or exact continuation changes, update this file only. Change another file only when that file's stable route, requirement, decision, source behavior, test behavior, or dated historical evidence changes.
