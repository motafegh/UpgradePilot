# Tier 1 Report 01 — Closest Dependency-Update Products and Workflows

**Recorded:** 2026-09-29  
**Branch:** `analysis/ai-agentic-capability-map-2026-09-28`  
**Status:** COMPLETE initial deep report  
**Research family:** Closest dependency-update products and workflows  
**Systems examined:** GitHub Dependabot / dependabot-core, Renovate / Mend Merge Confidence, GitHub Dependency Review, Updatecli  
**Purpose:** understand what adjacent systems actually optimize, how they represent/update dependencies, how maintainers control them, what evidence they expose, how they scale across ecosystems, and which product questions remain materially underserved.

This report is external research evidence. It does not change UpgradePilot architecture, specifications, plans, or live state.

---

## 1. Research questions

This report asks:

1. What exact maintainer problem does each system own?
2. What inputs/evidence does it use?
3. How does it decide what update to propose or allow?
4. What does it do with CI, release notes, vulnerability data, or crowd signals?
5. How much maintainer control does it expose?
6. How does it scale to many ecosystems?
7. What happens when evidence/configuration is missing or ambiguous?
8. What does it deliberately leave to the maintainer?
9. Which design patterns are transferable to UpgradePilot?
10. Which apparent features should not be copied because they solve a different product problem?

---

## 2. Executive comparison

| System | Primary product job | Main evidence/input | Main output | Core control model | Main non-goal visible from reviewed docs |
| --- | --- | --- | --- | --- | --- |
| Dependabot | discover available/security updates and open/update PRs | manifests/lockfiles, registries, advisories, package metadata, GitHub repo state | dependency-update PR | `dependabot.yml`, schedule, groups, cooldown, allow/ignore, PR commands | target-specific semantic compatibility analysis is not documented as its core responsibility |
| Renovate | highly configurable dependency-update orchestration across many ecosystems/platforms | repository package files, registries/datasources, versioning rules, package-manager tools, platform status checks, optional crowd confidence | branches/PRs, dashboard state, automerge | cascading config + `packageRules` + Dependency Dashboard + platform checks | deep repository-specific behavioral proof is not the documented decision engine |
| GitHub Dependency Review | show/enforce security/license policy over dependency diffs | base/head dependency graph diff, advisories, licenses, dependency scope | PR dependency diff + pass/fail policy gate | severity/license/scope allow/deny configuration | not an updater; not a general compatibility analyzer |
| Updatecli | declaratively propagate external values into repositories under explicit conditions | manifest-defined sources, conditions, targets, SCMs, actions; optional autodiscovery | file changes, branches, PRs/merge actions | explicit `source → condition → target → SCM → action` graph | does not infer whether an update is semantically safe for the target unless the user encoded the condition |

The central commonality is:

```text
these systems are excellent at
finding / proposing / routing / gating dependency changes

but they largely rely on
repository CI + declared policy + metadata + maintainer review
for the final target-specific compatibility judgment
```

This statement is limited to the public product responsibilities and documentation reviewed here. It is not a claim that their internal/private systems never perform additional analysis.

---

## 3. GitHub Dependabot

### 3.1 Product boundary

Dependabot version updates monitors configured package ecosystems and opens PRs when newer versions are available. Security updates are triggered by Dependabot alerts and attempt to move vulnerable dependencies to patched versions.

The maintainer workflow is intentionally familiar:

```text
configure dependabot.yml
→ Dependabot detects update
→ Dependabot opens PR
→ repository CI runs
→ maintainer reviews tests + PR summary/release notes/changelog
→ merge / ignore / rebase / close
```

GitHub explicitly describes the maintainer as checking that tests pass and reviewing release notes/changelog before merging.

### 3.2 Control and review-load management

Current controls include:

- schedule/frequency;
- customizable cooldown, with a default 3-day cooldown for version updates;
- dependency grouping;
- allow/ignore;
- versioning strategy;
- PR limits and target branches;
- labels/reviewers/assignees;
- rebase behavior;
- comment commands;
- automatic deactivation when maintainers stop interacting with Dependabot PRs.

This is significant: Dependabot does not only solve “is a newer version available?” It also solves **update-flow pressure management**.

### 3.3 Evidence surfaced to the maintainer

Dependabot PRs can include:

- release notes;
- changelog entries;
- commit details;
- vulnerability context for security updates;
- compatibility score in some security-update cases.

The compatibility score is population evidence:

```text
same version transition
→ public repositories where Dependabot generated that update
→ percentage of observed CI runs that passed
```

This is useful evidence about the update population, but it is not target-specific proof for the current repository.

Dependabot job logs also expose update execution details such as checked dependencies, resolution attempts, errors and stack traces.

### 3.4 Extensibility architecture

`dependabot-core` uses one ecosystem package/gem per language/package manager.

A new ecosystem normally implements:

- `FileFetcher`;
- `FileParser`;
- `UpdateChecker`;
- `FileUpdater`;

and optionally:

- `MetadataFinder`;
- ecosystem-specific `Version`;
- ecosystem-specific `Requirement`.

This is a strong architecture lesson:

> stable shared responsibilities + ecosystem-owned mechanics.

Dependabot does not attempt to make one generic dependency parser understand every package manager.

### 3.5 Failure/uncertainty behavior

Publicly visible failure handling is operational and ecosystem-centric:

- unsupported ecosystem/configuration;
- dependency/version constraint problems;
- private-registry/authentication errors;
- package-manager/update errors;
- update/rebase failures;
- job logs for diagnosis.

The documented product flow does not expose a rich proposition-level compatibility uncertainty model. In ordinary version updates, CI and maintainer review remain central.

### 3.6 Transferable ideas

Useful patterns:

1. **ecosystem adapter contract** rather than universal package parsing;
2. **flow-pressure controls** such as cooldown/grouping;
3. **population evidence** can be useful as context if scope is clearly labeled;
4. **diagnostic job logs** are a product feature, not merely implementation logging;
5. **release/changelog links belong close to the update PR**.

Do not copy blindly:

- treating public-CI population success as target proof;
- assuming green repository CI fully exercises the changed dependency;
- widening UpgradePilot into an update-generation bot merely because Dependabot has strong updater UX.

---

## 4. Renovate / Mend Merge Confidence

### 4.1 Product boundary

Renovate is the broadest updater/orchestrator in this report. Its documented flow is approximately:

```text
initialize repository/config
→ extract dependency references
→ look up releases
→ apply ecosystem versioning
→ generate/update files/artifacts
→ create/manage branches and PRs
→ observe platform status
→ optionally automerge
→ repeat/reconcile repository state
```

Renovate supports more than traditional language package managers; managers also cover Dockerfiles, CI configuration and many other dependency-bearing files.

### 4.2 Modular architecture

Renovate separates four major extension dimensions:

```text
Manager
→ where/how a dependency is declared and updated

Datasource
→ where releases/versions/digests come from

Versioning
→ how versions and constraints are parsed/ordered/compared

Platform
→ how repositories, branches, PRs, issues and statuses are managed
```

Per-repository workers orchestrate these modules.

This is more decomposed than Dependabot's ecosystem package contract and is an important architecture alternative for UpgradePilot's future ecosystem/generalization problem.

### 4.3 Package-manager execution strategy

A particularly valuable engineering principle appears in Renovate's package-manager development guidance:

> when lock/artifact files need updating, prefer calling the real package-manager tool rather than reverse engineering its lockfile behavior.

Examples include invoking npm/Poetry/etc. to synchronize lock files.

This deliberately delegates authoritative ecosystem semantics to the ecosystem tool where practical.

### 4.4 Maintainer policy and UX

Renovate's configuration surface is unusually rich:

- cascading configuration;
- `packageRules`;
- package/update-type/manager-specific behavior;
- schedules;
- grouping;
- minimum release age;
- dependency dashboard;
- pre-PR approval;
- automerge rules;
- PR/branch strategies;
- status-check integration.

The Dependency Dashboard is especially relevant. It acts as a repository issue containing update state and can become an approval surface before Renovate creates PRs.

This solves a different problem than semantic compatibility analysis:

> **maintainer attention allocation and update queue governance**.

### 4.5 Merge Confidence

Mend Merge Confidence exposes:

- Age;
- Adoption;
- Passing;
- Confidence.

Its data is derived from Renovate's broader update population. The confidence algorithm is private.

This is a stronger productized crowd signal than Dependabot's simple compatibility percentage, but the scope remains population-level rather than proof that the exact target repository is compatible.

### 4.6 Automerge and CI

By default Renovate does not automerge until it observes passing status checks/check runs. Its own documentation strongly recommends test coverage and warns about automerging without tests.

This creates a clear architecture:

```text
Renovate owns update orchestration
repository CI owns much of target validation
platform branch protection/status owns merge gating
```

The limitation is visible in Renovate's own guidance: good test coverage is assumed if green checks are going to justify automatic merging.

### 4.7 State invalidation lesson

Renovate only automerges an up-to-date branch and normally merges at most one PR per target branch per run because merging one update changes the base state and can invalidate assumptions about other open updates.

This is a strong transferable idea:

> evidence/decision state is revision-relative and can become stale after another dependency update lands.

### 4.8 Transferable ideas

Useful patterns:

1. **separate declaration extraction, release lookup, version semantics and platform integration**;
2. **delegate lock/artifact semantics to real ecosystem tools where appropriate**;
3. **configuration as policy composition**, not many hard-coded modes;
4. **Dependency Dashboard as attention/approval layer**;
5. **minimum-release-age / crowd signals as contextual risk evidence**;
6. **base-state invalidation and re-evaluation after merge**.

Do not copy blindly:

- huge configuration breadth before UpgradePilot has product need;
- confidence badges as substitutes for target evidence;
- automerge semantics until UpgradePilot's own decision boundary is independently justified;
- trying to support 90+ managers as a near-term goal.

---

## 5. GitHub Dependency Review

### 5.1 Product boundary

Dependency Review is not a dependency updater.

It compares the dependency graph between base and head commits for a PR and surfaces:

- added dependencies;
- removed dependencies;
- updated dependencies;
- release dates;
- known vulnerabilities;
- dependency popularity/use context;
- licenses;
- indirect dependency changes from supported lockfiles.

The Dependency Review Action turns this into an enforceable CI/policy gate.

### 5.2 Authority model

The action can fail a PR according to explicit policy such as:

- minimum vulnerability severity;
- denied/allowed licenses;
- dependency scope.

This is deterministic policy enforcement over GitHub's dependency-review evidence.

### 5.3 Important architecture pattern

Dependency Review cleanly separates:

```text
dependency graph/diff evidence
→ policy configuration
→ enforcement outcome
```

It does not try to reason broadly about all possible compatibility consequences.

That narrowness is a strength for its owned product responsibility.

### 5.4 Composition with other evidence

The dependency review API also integrates dependencies submitted through the dependency submission API.

This suggests a useful general pattern:

> allow additional producers to submit dependency evidence into a shared platform model, then consume that normalized model in policy/review.

### 5.5 Transferable ideas

Useful patterns:

1. base/head **dependency-diff as a first-class artifact**;
2. transitive dependency changes should remain visible;
3. separate evidence generation from policy enforcement;
4. organization-wide required-workflow enforcement;
5. explicit vulnerability/license/scope dimensions.

Do not copy blindly:

- security-oriented dependency graph evidence as a complete compatibility model;
- fail/pass policy as a replacement for uncertainty-aware technical investigation.

---

## 6. Updatecli

### 6.1 Product boundary

Updatecli is architecturally different from Dependabot/Renovate.

Its basic manifest pipeline is:

```text
Source
→ retrieve the value that could drive an update

Condition
→ decide whether declared prerequisites hold

Target
→ write the value into files

SCM
→ clone/branch/commit/push

Action
→ e.g. open/update a pull request or merge
```

It runs locally or in CI and intentionally needs no server/database; manifests and repository files hold the update state.

### 6.2 Declarative composition

Resources are plugin-based. The same general pipeline can connect values from:

- package registries;
- GitHub releases;
- Docker registries;
- files/APIs;
- Git repositories;

to many kinds of target files.

Updatecli also supports:

- autodiscovery/crawlers;
- reusable policies stored as OCI artifacts;
- multiple manifests composed together;
- dependency/order relations;
- graph visualization of manifests;
- multiple SCM/action implementations.

### 6.3 Why this matters

Updatecli demonstrates a third extensibility philosophy:

```text
Dependabot:
ecosystem adapter

Renovate:
manager + datasource + versioning + platform modules

Updatecli:
generic declarative pipeline of typed plugins
```

That is a valuable comparison for UpgradePilot. A future UpgradePilot does not automatically need to choose “one package-manager adapter per ecosystem” if some evidence/investigation responsibilities can be expressed as reusable typed capabilities.

### 6.4 Conditions are declared, not discovered

Updatecli conditions can prevent a target update unless a specified fact holds—for example, checking that an expected Docker image exists for an architecture.

But the system generally executes **conditions the manifest author selected**.

It is therefore closer to:

```text
declarative update policy executor
```

than:

```text
system that discovers all decision-relevant compatibility questions automatically
```

That distinction is important for UpgradePilot's research into candidate discovery.

### 6.5 Mutation decomposition

Updatecli separates target file mutation from SCM interaction and PR action. For GitHub, writing/committing/pushing and opening the PR are distinct responsibilities.

This is a strong authority/design seam.

### 6.6 Transferable ideas

Useful patterns:

1. explicit `source → condition → target` dependency graph;
2. separate evidence/condition evaluation from mutation/action;
3. reusable policy packages;
4. graph-renderable workflows;
5. typed plugins instead of one monolithic engine;
6. local/CI reproducibility with minimal server state.

Do not copy blindly:

- require maintainers to manually encode every compatibility condition UpgradePilot is supposed to discover;
- convert UpgradePilot into a generic configuration propagation engine.

---

## 7. Cross-system comparison

### 7.1 What these systems optimize

Across the four systems, the strongest product investments are in:

```text
finding updates
version/resolution mechanics
changing manifests/lockfiles
creating/managing PRs
reducing update noise
policy configuration
security/license gating
CI/status integration
approval/automerge workflow
ecosystem extensibility
```

These are mature problem areas.

### 7.2 What they commonly leave to other systems or the maintainer

The reviewed public product models largely rely on some combination of:

```text
release/changelog information
repository CI
security databases
crowd/population risk signals
maintainer knowledge/review
explicit configured conditions
```

for deciding whether a specific update is appropriate for the exact target.

No reviewed system documents, as its primary core responsibility, the complete chain:

```text
exact upstream technical change
→ exact target exposure/activation
→ proposition-specific CI/runtime coverage
→ unresolved evidence acquisition
→ cross-mechanism impact reasoning
→ explicit uncertainty-aware maintainer action
```

This is a **product-space observation**, not proof that UpgradePilot's existing implementation is therefore correct.

### 7.3 Closest conceptual overlap with UpgradePilot

The systems overlap different pieces:

- **Dependabot** supplies the triggering update PR and upstream/package metadata context.
- **Renovate** is the strongest reference for ecosystem adapters, update policy, queue governance and state invalidation.
- **Dependency Review** is the strongest reference for base/head dependency-diff evidence + deterministic policy enforcement.
- **Updatecli** is the strongest reference for declarative typed capability composition and separation of read/check/write/action phases.

None should be treated as a single direct competitor to the whole intended UpgradePilot responsibility.

---

## 8. Product-space hypothesis for UpgradePilot

A plausible underserved region is:

> **post-PR target-specific dependency-update decision intelligence**.

More concretely:

```text
Dependabot / Renovate / Updatecli
→ create/propose the update

Dependency Review / SCA
→ identify security/license/dependency-graph policy facts

CI
→ execute repository-defined checks

UpgradePilot hypothesis
→ explain whether the update's actual technical changes are materially relevant
   to this exact repository/environment,
   identify what the existing checks do or do not establish,
   pursue decision-relevant missing evidence,
   preserve uncertainty,
   and produce an inspectable maintainer-facing decision state
```

This hypothesis remains subject to the later Tier-1 reports—especially Endor Labs, Semgrep, Snyk, Socket, remediation systems and AI review agents—because those may already occupy more of this space than the updater products do.

---

## 9. Architecture lessons worth carrying forward

### 9.1 Ecosystem semantics should have bounded owners

Both Dependabot and Renovate strongly support modular ecosystem ownership.

This external evidence argues against building one universal dependency parser/resolver.

### 9.2 Separate what changes from where release data comes from

Renovate's Manager/Datasource/Versioning separation is especially compelling.

For UpgradePilot this suggests that:

```text
repository declaration semantics
!=
upstream release source
!=
version semantics
!=
platform integration
```

should remain separable even if the exact module boundaries differ.

### 9.3 Real ecosystem tools can be evidence/execution authorities

Renovate's refusal to reverse-engineer lockfile behavior where the real package manager can perform the update is a strong engineering precedent.

UpgradePilot should later compare:

```text
hand-reconstruct ecosystem semantics
vs
invoke real ecosystem tool in a controlled environment
```

for each responsibility rather than assuming one globally.

### 9.4 Maintainer attention is part of product design

Cooldown, grouping, dashboards, approval and schedule controls exist because dependency maintenance has a human attention budget.

UpgradePilot's eventual output should therefore optimize:

- priority;
- decisive evidence first;
- clearly separated unresolved questions;
- low-noise follow-up;
- batching/queue relevance where appropriate.

### 9.5 Population evidence is useful but scope-sensitive

Compatibility Score and Merge Confidence prove that maintainers value ecosystem-level risk priors.

Later research should evaluate whether UpgradePilot should consume such signals as **contextual priors**, while never confusing them with exact target proof.

### 9.6 Revision freshness is central

Renovate's rebase/re-evaluation behavior reinforces that evidence about an update is not timeless. Another merged dependency update can change whether a prior result remains valid.

### 9.7 Update generation and update judgment should stay conceptually separate

The mature updater products are already excellent at creating, grouping and routing changes.

UpgradePilot has stronger differentiation if it complements them rather than rebuilding them.

---

## 10. Things this report does NOT establish

This report does not prove:

- UpgradePilot has a unique market position;
- no competitor performs target-specific impact analysis;
- UpgradePilot should consume Renovate/Dependabot internals directly;
- crowd confidence should be part of final decision authority;
- a graph, agent or deterministic design is superior;
- current UpgradePilot architecture is independently validated.

Those questions depend on later Tier-1 families.

---

## 11. Follow-up hypotheses for later Track C

1. UpgradePilot should probably integrate with dependency-update PRs rather than own update generation.
2. A Renovate-like separation of declaration/source/version/platform concerns may generalize better than package-manager-specific vertical stacks.
3. An Updatecli-like typed capability graph may be useful for evidence acquisition/investigation orchestration.
4. Population risk signals may be useful as non-authoritative priors.
5. Maintainer attention/queue management may deserve a first-class product responsibility.
6. Exact revision freshness/supersession should be treated as a product-state concern, not just cache invalidation.
7. Runtime/package-manager execution should be evaluated as a source of ecosystem truth where static reconstruction becomes costly.
8. UpgradePilot's differentiation must be tested against the next research families before being accepted.

---

## 12. Sources checked

### GitHub / Dependabot
- https://docs.github.com/en/code-security/concepts/supply-chain-security/dependabot-version-updates
- https://docs.github.com/en/code-security/concepts/supply-chain-security/dependabot-security-updates
- https://docs.github.com/en/code-security/concepts/supply-chain-security/dependabot-pull-requests
- https://docs.github.com/en/code-security/concepts/supply-chain-security/dependabot-job-logs
- https://docs.github.com/en/code-security/tutorials/secure-your-dependencies/optimizing-pr-creation-version-updates
- https://docs.github.com/en/code-security/how-tos/secure-your-supply-chain/manage-your-dependency-security/controlling-dependencies-updated
- https://github.com/dependabot/dependabot-core
- https://github.com/dependabot/dependabot-core/blob/main/NEW_ECOSYSTEMS.md

### Renovate / Mend
- https://docs.renovatebot.com/key-concepts/dashboard/
- https://docs.renovatebot.com/key-concepts/automerge/
- https://docs.renovatebot.com/merge-confidence/
- https://docs.renovatebot.com/configuration-options/
- https://docs.renovatebot.com/modules/versioning/
- https://github.com/renovatebot/renovate/blob/main/docs/development/adding-a-package-manager.md
- https://github.com/renovatebot/renovate/blob/main/docs/development/design-decisions.md
- https://github.com/renovatebot/renovate/blob/main/lib/modules/datasource/readme.md

### GitHub Dependency Review
- https://docs.github.com/en/code-security/concepts/supply-chain-security/dependency-review
- https://docs.github.com/en/code-security/tutorials/secure-your-dependencies/customize-dependency-review-action
- https://docs.github.com/en/code-security/how-tos/secure-your-supply-chain/manage-your-dependency-security/configure-dependency-review-action

### Updatecli
- https://www.updatecli.io/docs/prologue/introduction/
- https://www.updatecli.io/docs/core/configuration/
- https://www.updatecli.io/docs/core/action/
- https://www.updatecli.io/docs/plugins/scm/github/
- https://www.updatecli.io/docs/plugins/actions/github/
- https://www.updatecli.io/docs/plugins/_actionscm/
- https://www.updatecli.io/docs/plugins/autodiscovery/githubaction/
- https://www.updatecli.io/docs/commands/updatecli_manifest_show/

## 13. Status / next report

**Tier-1 Report 01: COMPLETE.**

Next research family:

> **Tier-1 Report 02 — Dependency risk, reachability and upgrade-impact platforms**  
> Endor Labs, Semgrep Supply Chain, Snyk Open Source, Socket, and any materially similar system discovered during the deep pass.

That report is especially important because it can falsify or narrow the current hypothesis that target-specific update impact remains underserved.
