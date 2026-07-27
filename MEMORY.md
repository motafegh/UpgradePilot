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
- **Latest repository baseline inspected before this governance update:** `2ff844ed3da1d68354098ca1505fd1c81c54f490`
- **Last behavior-validated source/test commit:** `bdd178f38ad23e82a93cc5f3505932e5d0ef3b53`

The later commits through `2ff844ed…` changed source/test explanation and presentation. Their
product behavior has not been separately revalidated in Ali's environment, so the validated
behavior claim remains pinned to `bdd178f…`.

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

Not established:

- complete CI coverage;
- compatibility or upgrade safety;
- that every workflow exercised the dependency;
- package or upstream release authority;
- a maintainer recommendation;
- production readiness.

Detailed dated evidence:

- [`working-memory/B2_TECHNICAL_PROGRESS.md`](working-memory/B2_TECHNICAL_PROGRESS.md)

## Implemented boundary

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
→ transparent terminal evidence
```

Responsibility boundaries:

```text
github_api.py          shared read-only HTTP/JSON trust boundary
github_client.py       PR identity and changed files
dependency_change.py   dependency interpretation
github_actions.py      workflow runs, jobs, and step summaries
github_repository.py   exact-head repository-file acquisition
workflow_commands.py   bounded workflow command reading
ci_authority.py        deterministic CI-authority classification
cli.py                 execution order and presentation
```

## Exact continuation

Execute the source-selection decision in
[`plans/B2_MINIMUM_PACKAGE_AND_UPSTREAM_EVIDENCE_PLAN.md`](plans/B2_MINIMUM_PACKAGE_AND_UPSTREAM_EVIDENCE_PLAN.md)
before writing package/upstream acquisition code.

The next action is:

1. freeze the minimum claim required from package/upstream evidence for the supported control
   case;
2. compare the plan's three source strategies:
   - PyPI release metadata only;
   - PyPI identity plus a project-controlled release source;
   - package-specific known URL or adapter;
3. reject the package-specific strategy as accepted product behavior;
4. determine whether PyPI plus an official project-controlled release source provides the
   smallest credible generalizable boundary;
5. specify exact evidence identity, authority, failure states, and proof before implementation;
6. obtain Ali's approval for any consequential source-selection or semantic-interpretation
   method.

No implementation begins until the source-selection result is explicit enough to determine
what evidence can be trusted and what must remain unresolved.

## Product boundaries affecting continuation

Do not yet:

- produce the final maintainer recommendation;
- treat sufficient CI authority as compatibility or safety proof;
- broaden tox, script, reusable-workflow, matrix, or YAML interpretation unless it becomes a
  material blocker for the selected product question;
- hardcode pytest, version `9.0.3`, the S004 answer, exact release wording, or a known release URL;
- use PyPI existence alone as proof of release compatibility or drop-in behavior;
- add phrase tables or package-specific prose parsers as accepted semantic behavior;
- add a model, semantic service, persistence, replay infrastructure, agents, queues, or
  deployment layers without a separately admitted responsibility and approval;
- mutate a target repository or require private access.

## State-maintenance rule

When stage, selected plan, latest verified behavior, blocker, or exact continuation changes,
update this file only. Change another file only when that file's stable route, requirement,
decision, source behavior, test behavior, or dated historical evidence changes.