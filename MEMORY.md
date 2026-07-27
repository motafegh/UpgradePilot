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
- **Shared-contract source/test implementation:** `98a4914ce70b1cfe8d5ddd612185cb527d52a02c`.
- **Dated investigation closure:** `1bf6b4788da44c11f8a0b2fe2801acf9769205ad`.
- **Stable external-source reuse rule activated:** `f605f444a38bb41928dd8e9ace3ed1d5d43cec3e`.

The source-neutral JSON contract refactor is implemented and behavior-validated. The selected B2 plan now continues at the project-controlled, release-specific upstream-source boundary.

## Verified product evidence

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

The first regression attempt returned HTTP `401` while a local `GITHUB_TOKEN` environment variable was set. After removing that variable, the same public read-only command succeeded anonymously. This was an environment credential issue, not evidence of a source regression. No token value was exposed or recorded.

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

The project-link candidates are not yet trusted as release-specific upstream authority.

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

## Behavior-validated boundary

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

Current implementation responsibilities:

```text
json_contract.py       validated source-neutral JSON runtime value contracts
github_api.py          GitHub HTTP/JSON boundary and GitHub-specific contract adapters
github_client.py       PR identity and changed files
dependency_change.py   dependency interpretation
github_actions.py      workflow runs, jobs, and step summaries
github_repository.py   exact-head repository-file acquisition
workflow_commands.py   bounded workflow command reading
ci_authority.py        deterministic CI-authority classification
pypi_client.py         PyPI package/version identity and PyPI-specific contract adapters
cli.py                 current execution order and presentation
```

## Accepted architectural boundary

```text
source-neutral JSON value contracts
├── GitHub adapters preserve GitHub exceptions and messages
├── PyPI adapters preserve PyPI evidence/problem classification
└── source authority, identity, HTTP meaning, and provenance remain focused
```

Stable implementation rule:

> Before adding helpers for a new external source, classify each behavior as source-neutral mechanics or source-specific evidence semantics. Reuse shared primitives only when the meaning is identical; keep authority, identity, and failure interpretation in the focused source boundary.

No universal external-source HTTP client was admitted. Bounded body acquisition remains local to PyPI until another selected source demonstrates identical semantics.

## Accepted source direction

The selected B2 evidence plan requires two separately validated authorities:

```text
PyPI exact-release identity
+ project-controlled release-specific upstream source
```

Stable constraints:

- PyPI is authoritative for official Python distribution/version publication identity within this bounded responsibility;
- PyPI `project_urls` are discovery candidates, not automatically trusted upstream sources;
- a separately validated project-controlled source must be bound to the package and exact proposed version;
- package-specific URLs, adapters, known release pages, and exact wording remain rejected as accepted runtime behavior;
- semantic release-note interpretation remains unadmitted;
- PyPI existence, link metadata, or sufficient CI authority cannot establish compatibility, safety, or a final recommendation by themselves.

## Exact continuation

Perform one bounded source-resolution design decision before adding upstream code:

1. state the exact release-source claim the resolver must establish;
2. compare the smallest credible generalizable rules for turning PyPI project-link candidates into a project-controlled source applying to the exact proposed version;
3. choose the first supported source format and its authority rule;
4. define explicit unavailable, mismatched, unsupported, redirect, and ambiguity behavior;
5. identify the minimum controlled tests and one live read-only proof;
6. check whether the selected format creates a second consumer for PyPI's bounded response-body mechanics; extract those mechanics only if their meaning is genuinely identical;
7. present the method, tradeoffs, and proposed source boundary to Ali for approval;
8. only after approval, implement the smallest upstream-acquisition slice directly on `main`.

Do not begin semantic interpretation during this source-resolution decision.

## Product boundaries affecting continuation

Do not yet:

- produce the final maintainer recommendation;
- treat sufficient CI authority or PyPI existence as compatibility or safety proof;
- treat publisher-supplied project URLs as automatically authoritative;
- hardcode pytest, version `9.0.3`, the S004 answer, exact release wording, or a known release URL;
- add phrase tables or package-specific prose parsers as accepted semantic behavior;
- add a model, semantic service, persistence, replay infrastructure, agents, queues, or deployment layers without a separately admitted responsibility and approval;
- mutate a target repository or require private access.

## State-maintenance rule

When stage, selected plan, latest verified behavior, blocker, or exact continuation changes, update this file only. Change another file only when that file's stable route, requirement, decision, source behavior, test behavior, or dated historical evidence changes.