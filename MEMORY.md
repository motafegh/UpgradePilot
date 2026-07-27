# UpgradePilot Current Memory

**Last updated:** 2026-07-27  
**Authority:** Sole repository owner of live project position, selected plan, latest relevant commit evidence, blockers, and exact continuation.

Stable route, specifications, ADRs, source, tests, and dated evidence retain their own responsibilities. They must not duplicate this live state.

## Live position

- **Route:** B2 — Public PR vertical slice.
- **Controlling route:** [`plans/UPGRADEPILOT_90_DAY_PLAN.md`](plans/UPGRADEPILOT_90_DAY_PLAN.md)
- **B2 gate definition:** [`plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md`](plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md)
- **Selected bounded plan:** [`plans/B2_MINIMUM_PACKAGE_AND_UPSTREAM_EVIDENCE_PLAN.md`](plans/B2_MINIMUM_PACKAGE_AND_UPSTREAM_EVIDENCE_PLAN.md)
- **Last behavior-validated repository revision in Ali's environment:** `64b08fa93c16baa6f9557ba0f6b44ea97dff3098`.
- **Latest upstream source/test implementation awaiting validation:** `bf4ede1d6e902b22fda384d6d43339efe46bab8f`.
- **Dated implementation record:** `d4758bd65d0276a800832cb06e9ed4fe653b01a4`.

The stronger but narrower provenance-backed GitHub Release/tag source resolver is implemented on `main`. It has focused controlled implementation evidence but has not yet passed the complete repository suite or a live source-resolution proof in Ali's Python 3.12 environment.

Do not integrate it into the CLI or begin semantic interpretation until that validation gate passes.

## Previously verified product evidence

### Target-repository and CI evidence

Observed in Ali's WSL2 Python 3.12 environment and revalidated on 2026-07-27:

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

The first regression attempt returned HTTP `401` while a local `GITHUB_TOKEN` variable was set. After removing it, the same public read-only command succeeded anonymously. No token value was exposed or recorded.

### Package-registry identity evidence

Observed in Ali's WSL2 Python 3.12 environment and revalidated on 2026-07-27:

```text
live PyPI request: https://pypi.org/pypi/pytest/9.0.3/json
result type: PackageReleaseEvidence
state: available
requested identity: pytest==9.0.3
published identity: pytest==9.0.3
distribution-file records: 2
```

Permitted package claim:

> The implemented live client established that PyPI published an exact release record for `pytest==9.0.3` and preserved PyPI-supplied project-link candidates with provenance.

The previous live proof established only registry identity and project-link candidates. It did not validate the new exact-file provenance and upstream resolver behavior.

### Shared external-source foundation evidence

Observed after pulling repository revision `64b08fa93c16baa6f9557ba0f6b44ea97dff3098`:

```text
editable installation succeeded
41 active repository tests passed in 0.008 seconds
live GitHub regression path passed after removing an unusable token
live PyPI exact-release regression path passed
```

Permitted architecture claim:

> Source-neutral JSON runtime value contracts are shared, while GitHub and PyPI preserve their own field policy, identity, authority, HTTP meaning, and public failure contracts.

Detailed dated evidence:

- [`working-memory/B2_TECHNICAL_PROGRESS.md`](working-memory/B2_TECHNICAL_PROGRESS.md)
- [`working-memory/2026-07-27_B2-PYPI_source-selection-and-identity-slice.md`](working-memory/2026-07-27_B2-PYPI_source-selection-and-identity-slice.md)
- [`working-memory/2026-07-27_B2-shared-external-source-foundation-investigation.md`](working-memory/2026-07-27_B2-shared-external-source-foundation-investigation.md)
- [`working-memory/2026-07-27_B2-project-controlled-exact-release-source-resolution.md`](working-memory/2026-07-27_B2-project-controlled-exact-release-source-resolution.md)

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
→ bounded response and explicit evidence state
→ publisher-supplied project-link candidates without upstream-authority claims
```

## New implementation awaiting validation

```text
exact PyPI release evidence
→ immutable distribution filename, URL, package type, and SHA-256 records
→ bounded per-file PyPI Integrity API acquisition
→ PyPI-reported publisher identity
→ one well-known canonical GitHub Source candidate
→ publisher repository and Source candidate agreement
→ accepted exact-version tag forms: <version> or v<version>
→ published GitHub Release
→ exact refs/tags/<tag> object type and SHA
→ bounded release content
→ unresolved_claim; no semantic interpretation
```

Implemented responsibilities:

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
cli.py                 current validated execution order and presentation
```

Focused reconstructed-source validation available now:

```text
changed modules compiled
20 focused controlled tests passed
```

This is not a substitute for the complete active repository suite or a live-network proof.

## Accepted upstream authority boundary

```text
PyPI exact package/version/file identity
+ PyPI-reported exact-file publisher provenance
+ matching canonical GitHub Source candidate
+ one exact-version GitHub Release/tag reference
```

Stable constraints:

- project URL labels are normalized only to identify candidate intent;
- a Source candidate alone is not upstream authority;
- provenance is queried for every exact distribution file;
- at least one usable exact-file provenance record is required;
- all usable GitHub publisher repository identities must agree;
- valid non-GitHub provenance is unsupported, not malformed;
- source and provenance repository identities must match;
- exactly one of `<version>` or `v<version>` may resolve to a published release;
- tag reference object type and SHA are preserved;
- release body meaning remains unresolved;
- UpgradePilot does not yet independently verify attestation cryptography;
- compatibility, safety, and final recommendation remain unestablished.

## Exact continuation

Validate the implemented source boundary before any CLI integration or semantic work:

1. pull the latest `main` in Ali's WSL2 environment;
2. install editably using Python 3.12;
3. run the complete active unittest suite—expected count is **60** if no unrelated tests changed;
4. review any regression before proceeding;
5. run one unmocked `PyPIReleaseClient().get_release("pytest", "9.0.3")` followed by `UpstreamSourceResolver().resolve(...)`;
6. record whether the live result is `UpstreamReleaseEvidence` or an accurately classified problem;
7. inspect repository identity, provenance files, unavailable provenance files, accepted tag, tag-ref SHA, release URL, and `claim_state`;
8. after all checks pass, close the dated implementation record, update this live state, and decide the next product action.

Do not treat an unexpected but accurately classified live unsupported/unavailable result as a code failure without first examining the external evidence.

## Product boundaries affecting continuation

Do not yet:

- integrate package/upstream evidence into the CLI;
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
