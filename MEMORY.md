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
- **PyPI identity implementation merged to `main`:** PR [#13](https://github.com/motafegh/UpgradePilot/pull/13).
- **Merged implementation commit:** `a3b416358669035ed9bf5db3e8043bcf49334a6d`.
- **Last behavior-validated source/test commit in Ali's environment:** `bdd178f38ad23e82a93cc5f3505932e5d0ef3b53`.

The PyPI identity code is now part of `main`. It passed seven isolated controlled tests during
implementation, but the complete repository suite and an unmocked live client run have not yet
been performed in Ali's WSL2 Python 3.12 environment. It is therefore implemented but not yet
added to the behavior-validated product claim.

## Verified product evidence

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

Permitted claim:

> At least one successful exact-head CI path installed the changed requirements file and
> directly exercised pytest.

Not yet established in Ali's environment:

- package/version acquisition through the new PyPI client;
- project-controlled upstream release authority;
- compatibility or upgrade safety;
- complete CI coverage;
- that every workflow exercised the dependency;
- a maintainer recommendation;
- production readiness.

Detailed dated evidence:

- [`working-memory/B2_TECHNICAL_PROGRESS.md`](working-memory/B2_TECHNICAL_PROGRESS.md)
- [`working-memory/2026-07-27_B2-PYPI_source-selection-and-identity-slice.md`](working-memory/2026-07-27_B2-PYPI_source-selection-and-identity-slice.md)

## Implemented boundary on `main`

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

For the selected plan:

- PyPI is accepted for official Python package/version publication identity;
- PyPI project URLs are candidates, not automatically trusted upstream release sources;
- PyPI existence alone cannot establish compatibility or a drop-in release claim;
- PyPI identity plus a separately validated project-controlled release source remains the
  product-level direction;
- package-specific URLs or adapters remain rejected as accepted runtime behavior;
- semantic release-note interpretation remains unadmitted.

## Exact continuation

Validate the new `main` implementation before adding more package/upstream behavior:

1. pull the latest `main` in Ali's WSL2 environment;
2. install the repository editably with Python 3.12;
3. run the complete active unittest suite;
4. execute one clearly identified unmocked live `PyPIReleaseClient` smoke check for
   `pytest` version `9.0.3`;
5. verify that the result establishes only exact PyPI identity and link candidates, not
   compatibility or upstream authority;
6. repair any source or test failure directly on `main` and repeat the relevant checks;
7. only after validation, decide the smallest generalizable rule for binding a PyPI package to
   one supported project-controlled release source.

The upstream-source resolver must not begin until the PyPI identity boundary is validated and
its output contract is accepted.

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
