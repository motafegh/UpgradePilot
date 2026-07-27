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
- **Last behavior-validated repository revision in Ali's environment:** `70bc133d3d3d0fbffddfadeb881ae98825f147b7`.
- **Latest source/test implementation awaiting validation:** `98a4914ce70b1cfe8d5ddd612185cb527d52a02c`.
- **Latest dated implementation record update:** `4cb7c69a048aa6ea7dfcb8a079061a901756a78b`.

The deterministic PyPI package/version identity capability remains the last behavior-validated
product boundary. A small approved source-neutral JSON contract refactor is implemented on
`main`, but it has not yet been validated in Ali's Python 3.12 environment. Upstream-source
design must resume only after this regression gate passes.

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
directly exercised pytest.

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

- the shared JSON-contract refactor preserves all GitHub and PyPI behavior;
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
- [`working-memory/2026-07-27_B2-shared-external-source-foundation-investigation.md`](working-memory/2026-07-27_B2-shared-external-source-foundation-investigation.md)

## Behavior-validated product boundary

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
json_contract.py       source-neutral JSON runtime value contracts; awaiting validation
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

The refactor is intended to change architecture only. It does not extend the permitted product
claim until its regression proof is complete.

## Accepted architectural boundary

```text
source-neutral JSON value contracts
├── GitHub adapters preserve GitHub exceptions and messages
├── PyPI adapters preserve PyPI evidence/problem classification
└── source authority, identity, HTTP meaning, and provenance remain focused
```

No universal external-source HTTP client was admitted. Bounded body acquisition remains local to
PyPI until another selected source demonstrates identical semantics.

## Accepted source direction

The selected B2 evidence plan requires two separately validated authorities:

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

Validate the approved shared-contract implementation before any upstream-source work:

1. pull the latest `main` in Ali's WSL2 environment;
2. install the repository editably with Python 3.12;
3. run the complete active unittest suite—expected count is 41 if no other tests changed;
4. run `python3 -m upgradepilot googlefonts/glyphsLib 1145` as the GitHub-path smoke check;
5. run one unmocked `PyPIReleaseClient().get_release("pytest", "9.0.3")` smoke check;
6. verify that GitHub classifications/messages and PyPI evidence/problem states remain unchanged;
7. repair any regression directly on `main` and repeat the relevant checks;
8. after all checks pass, close the dated investigation, activate the stable external-source
   reuse instruction in `AGENTS.md`, update this live state, and resume the bounded upstream-source
   resolution decision.

## Product boundaries affecting continuation

Do not yet:

- begin upstream-source implementation before the shared-contract regression gate passes;
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
