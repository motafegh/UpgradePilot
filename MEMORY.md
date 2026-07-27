# UpgradePilot Current Memory

**Last updated:** 2026-07-27  
**Authority:** Sole repository owner of live project position, selected plan, latest relevant
commit evidence, blockers, and exact continuation.

Stable route, specifications, ADRs, source, tests, and dated evidence retain their own
responsibilities. They must not duplicate this live state.

## Live position

- **Route:** B2 — Public PR vertical slice.
- **Controlling route:** [`plans/UPGRADEPILOT_90_DAY_PLAN.md`](plans/UPGRADEPILOT_90_DAY_PLAN.md)
- **B2 gate definition:** [`plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md`](plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md)
- **Selected bounded plan:** [`plans/B2_MINIMUM_PACKAGE_AND_UPSTREAM_EVIDENCE_PLAN.md`](plans/B2_MINIMUM_PACKAGE_AND_UPSTREAM_EVIDENCE_PLAN.md)
- **PyPI identity implementation merged to `main`:** PR [#13](https://github.com/motafegh/UpgradePilot/pull/13), commit `a3b416358669035ed9bf5db3e8043bcf49334a6d`.
- **Last behavior-validated repository revision in Ali's environment:** `70bc133d3d3d0fbffddfadeb881ae98825f147b7`.
- **Latest evidence/plan reconciliation commit before this state update:** `3436920e5aa4fd5e970ef5cf939439cc8e115fd3`.

The deterministic PyPI package/version identity slice is implemented and behavior-validated.
The selected plan now continues at the separate project-controlled, release-specific upstream
source boundary.

## Verified product evidence

### Target-repository and CI evidence

Observed in Ali's WSL2 environment with Python 3.12 on 2026-07-24:

```text
editable installation succeeded
28 deterministic tests passed
live googlefonts/glyphsLib#1145 acquisition succeeded
exact dependency: pytest 9.0.2 → 9.0.3
exact head: f3cda8a94600e58d27f1bc17c99b7693718b6350
Regression Tests: sufficient direct install-and-pytest authority
Test + Deploy: unresolved because multi-job/tox indirection was not traced
overall CI authority: sufficient
```

Permitted CI claim:

> At least one successful exact-head CI path installed the changed requirements file and
> directly exercised pytest.

### Package-registry identity evidence

Observed in Ali's WSL2 Python 3.12 virtual environment on 2026-07-27 at repository revision
`70bc133d3d3d0fbffddfadeb881ae98825f147b7`:

```text
editable installation succeeded
35 active repository tests passed
live PyPI request: https://pypi.org/pypi/pytest/9.0.3/json
result type: PackageReleaseEvidence
state: available
requested identity: pytest==9.0.3
published identity: pytest==9.0.3
distribution-file records: 2
PyPI serial: 38199665
publisher-supplied Changelog, Contact, Funding, Homepage, Source, and Tracker links preserved
```

Permitted package claim:

> The implemented live client established that PyPI published an exact release record for
> `pytest==9.0.3`, and it preserved PyPI-supplied project-link candidates with provenance.

The project-link candidates are not yet trusted as release-specific upstream authority.

Not yet established in Ali's environment:

- a validated project-controlled source applying to the exact proposed release;
- a trusted structured upstream claim about what changed;
- compatibility or upgrade safety;
- complete CI coverage;
- that every workflow exercised the dependency;
- a maintainer recommendation;
- production readiness.

Detailed dated evidence:

- [`working-memory/B2_TECHNICAL_PROGRESS.md`](working-memory/B2_TECHNICAL_PROGRESS.md)
- [`working-memory/2026-07-27_B2-PYPI_source-selection-and-identity-slice.md`](working-memory/2026-07-27_B2-PYPI_source-selection-and-identity-slice.md)

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

Responsibility boundaries:

```text
github_api.py          shared read-only GitHub HTTP/JSON trust boundary
github_client.py       PR identity and changed files
dependency_change.py   dependency interpretation
github_actions.py      workflow runs, jobs, and step summaries
github_repository.py   exact-head repository-file acquisition
workflow_commands.py   bounded workflow command reading
ci_authority.py        deterministic CI-authority classification
pypi_client.py         PyPI package/version identity boundary
cli.py                 current execution order and presentation
```

## Accepted source direction

The selected plan now requires two separately validated authorities:

```text
PyPI exact-release identity
+ project-controlled release-specific upstream source
```

Stable constraints:

- PyPI is authoritative for official Python distribution/version publication identity within
  this bounded responsibility;
- PyPI `project_urls` are discovery candidates, not automatically trusted upstream sources;
- a separately validated project-controlled source must be bound to the package and exact
  proposed version;
- package-specific URLs, adapters, known release pages, and exact wording remain rejected as
  accepted runtime behavior;
- semantic release-note interpretation remains unadmitted;
- PyPI existence, link metadata, or sufficient CI authority cannot establish compatibility,
  safety, or a final recommendation by themselves.

## Exact continuation

Perform one bounded source-resolution design decision before adding upstream code:

1. state the exact release-source claim the resolver must establish;
2. compare the smallest credible generalizable binding rules for turning PyPI project-link
   candidates into a project-controlled source applying to the exact proposed version;
3. choose the first supported source format and its authority rule;
4. define explicit unavailable, mismatched, unsupported, redirect, and ambiguity behavior;
5. identify the minimum controlled tests and one live read-only proof;
6. present the method, tradeoffs, and proposed source boundary to Ali for approval;
7. only after approval, implement the smallest upstream-acquisition slice directly on `main`.

Do not begin semantic interpretation during this source-resolution decision.

## Product boundaries affecting continuation

Do not yet:

- produce the final maintainer recommendation;
- treat sufficient CI authority or PyPI existence as compatibility or safety proof;
- treat publisher-supplied project URLs as automatically authoritative;
- hardcode pytest, version `9.0.3`, the S004 answer, exact release wording, or a known release URL;
- add phrase tables or package-specific prose parsers as accepted semantic behavior;
- add a model, semantic service, persistence, replay infrastructure, agents, queues, or
  deployment layers without a separately admitted responsibility and approval;
- mutate a target repository or require private access.

## State-maintenance rule

When stage, selected plan, latest verified behavior, blocker, or exact continuation changes,
update this file only. Change another file only when that file's stable route, requirement,
decision, source behavior, test behavior, or dated historical evidence changes.
