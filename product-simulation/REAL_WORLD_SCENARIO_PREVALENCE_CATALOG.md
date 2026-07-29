# Real-World Dependency-Update Scenario Prevalence Catalog

**Status:** Research-backed proposal support — non-controlling  
**Owner:** Ali Rajabi  
**Recorded:** 2026-07-29  
**Scope:** Evidence-informed occurrence bands for dependency-update and Dependabot-review situations relevant to the full UpgradePilot product horizon  
**Authority:** None. This catalog does not define product requirements, activate implementation, select a case, or claim statistically representative prevalence.

## 1. Purpose

This catalog provides a structured answer to two planning questions:

1. What situations commonly occur around real dependency-update pull requests?
2. Which common, unusual, or rare situations are valuable enough to become real cases, controlled variants, synthetic scenarios, or evaluation caselets for UpgradePilot?

The catalog is intended to support case selection. It is not a product schema and not a complete taxonomy of every package-manager or repository behavior.

## 2. Research method

### 2.1 Evidence classes

The occurrence bands below combine three evidence classes.

#### A. Official platform behavior

Primary GitHub documentation was reviewed for:

- Dependabot version and security update behavior;
- pull-request creation and grouping;
- rebase and inactivity behavior;
- update errors, timeouts, pull-request limits, and grouped-update failures;
- direct and transitive dependency handling;
- dependency-graph and manifest/lockfile behavior;
- private-registry and configuration boundaries.

#### B. Python packaging specifications

Primary Python Packaging Authority specifications and guidance were reviewed for:

- dependency specifiers;
- environment markers and extras;
- `pyproject.toml` dependency declarations;
- requirements files versus project metadata;
- lock files;
- dependency groups;
- yanked files;
- package-index metadata and provenance links;
- Python, ABI, and platform compatibility tags.

#### C. Public pull-request occurrence scan

A purposive GitHub search snapshot was performed on 2026-07-29 using recent public Dependabot pull requests, including searches returning up to 50 recent PRs whose bodies contained the common Python-style wording `Updates the requirements on` and a broader recent Dependabot sample.

The scan confirmed recurring examples of:

- single-dependency range updates;
- patch, minor, and major changes;
- release-note and changelog evidence;
- development-tool updates;
- grouped updates containing many dependencies;
- GitHub Actions and Docker updates;
- explicit breaking changes;
- Python and platform-support changes;
- security patch releases.

The scan is **not statistically representative**. It is recent-result and search-query biased, may overrepresent repositories that enabled many updates at once, and does not provide global GitHub percentages. It is used only to confirm that documented scenario forms occur publicly.

### 2.2 Prevalence labels

The labels are planning bands, not probabilities.

| Band | Meaning for case planning |
|---|---|
| **Very common** | Expected across a large share of ordinary dependency-update review; should be represented in normal-path coverage. |
| **Common** | Regularly recurring and important across many repositories, though not present in most individual PRs. |
| **Usual / recurring** | Recognized recurring condition that appears often enough to deserve planned coverage but may require targeted search. |
| **Less common** | Credible real-world condition that is not routinely visible and may be expensive to find naturally. |
| **Rare** | Edge, adversarial, severe, or timing-sensitive condition; often better exercised synthetically after realism is established. |

### 2.3 Confidence labels

| Confidence | Basis |
|---|---|
| **High** | Explicitly documented as normal/default behavior and repeatedly visible in public PRs. |
| **Medium** | Documented and/or repeatedly observed, but no representative frequency dataset exists. |
| **Low** | Plausible, documented as an edge condition, or known from ecosystem behavior, but public prevalence is uncertain. |

## 3. Catalog use rules

1. Prevalence is not the same as product value.
2. A rare high-consequence scenario may be more important than a very common low-risk scenario.
3. A very common scenario should usually appear in normal-path regression coverage, but it may not justify another full narrative case when S001–S005 already cover it.
4. Rare scenarios should not automatically become full cases; use controlled variants or caselets when repository-specific context is not material.
5. Every admitted case still requires a named uncertainty, non-duplication argument, evidence boundary, and useful stopping condition.
6. Scenario frequency should be revised when UpgradePilot later has a versioned corpus or shadow-mode evidence.

## 4. Proposal and dependency-change shapes

| ID | Scenario | Band | Confidence | Why it occurs | Product relevance | Preferred evidence form |
|---|---|---|---|---|---|---|
| `P-01` | One direct dependency updated in one manifest | Very common | High | Default Dependabot version-update behavior focuses on explicitly declared dependencies | Core identity, diff, package, and recommendation path | Real cases and normal regression fixtures |
| `P-02` | Patch or minor version increase | Very common | High | Routine maintenance produces many small updates | Tests whether low apparent version risk is kept separate from compatibility proof | Real normal-path cases |
| `P-03` | Dependency range widened to permit a newer version | Very common | High | Projects commonly use lower bounds, upper bounds, or compatible ranges rather than exact pins | Requires semantic comparison beyond literal old/new pin replacement | Real cases and controlled requirement variants |
| `P-04` | Exact pin changed from one version to another | Very common | High | Requirements and environment files often use exact versions for reproducibility | Simple supported identity boundary and replay seed | Real cases and fixtures |
| `P-05` | Manifest and lockfile change together | Very common | Medium | Lock-backed environments update concrete resolutions alongside declarations | Requires distinguishing declaration, resolution, and changed transitive set | Real cases; later repository-level synthetic cases |
| `P-06` | Development, test, lint, documentation, or build-tool dependency | Common | High | Repositories maintain non-runtime dependencies through Dependabot | Dependency role changes relevance, impact, and acceptable evidence | Real cases; S001, S004, and S005 already provide partial coverage |
| `P-07` | Major-version update with explicit migration or breaking-change notes | Common | High | Dependabot can propose major updates when configuration permits; public samples show broad range jumps and breaking releases | Baseline version category is useful but insufficient; migration and target usage matter | Real behavior-impact case |
| `P-08` | Security patch or security-update PR | Common | High | Dependabot security updates are a first-class GitHub feature | Adds advisory identity, vulnerable path, fixed version, and exploitability boundaries | Real cases; controlled advisory variants |
| `P-09` | Grouped update containing several dependencies | Common | High | GitHub supports grouped version and security updates, including cross-directory grouping | Requires multi-change identity, attribution, partial failure, and PR-action separation | Real grouped case or synthetic attribution host |
| `P-10` | Multiple directories or monorepo locations updated | Common | Medium | Dependabot supports multiple directories and group-by dependency across them | Adds repeated identity, scope, path, and CI mapping | Real monorepo case or repository-level synthetic case |
| `P-11` | Direct dependency range changes but resolved version remains unchanged in some environments | Usual / recurring | Medium | Abstract requirements and concrete resolutions are different layers | Prevents declaration changes from being mistaken for effective environment changes | Real-derived environment variants |
| `P-12` | Transitive dependency changed through a lockfile or parent update | Usual / recurring | High | Dependency graphs and lockfiles expose indirect dependencies; support differs by ecosystem and update type | Requires dependency-path and parent attribution | Real case; S001 provides one form |
| `P-13` | Optional extra or dependency group updated | Usual / recurring | Medium | Python metadata supports extras and dependency groups | Activation depends on installation mode and repository usage | Real-derived or synthetic activation cases |
| `P-14` | Environment-marker-conditioned dependency | Usual / recurring | High | Python dependency specifiers can depend on Python version, platform, implementation, or extras | Requires environment-specific activation and avoids universal conclusions | Synthetic matrix plus later real validation |
| `P-15` | GitHub Action update | Common in Dependabot generally; outside primary Python-package slice | High | GitHub Actions is a supported Dependabot ecosystem | Useful later for self-application and supply-chain analysis, but not a default Python package case | Reserve outside current supported case boundary |
| `P-16` | Docker base-image update | Common in Dependabot generally; outside primary Python-package slice | High | Docker is a supported Dependabot ecosystem | Can affect runtime and platform independently of Python package metadata | Reserve for later boundary expansion |
| `P-17` | Direct URL, VCS reference, local path, or editable requirement | Less common | Medium | Python specifications permit non-index and direct-reference forms | Challenges package identity, acquisition authority, and reproducibility | Controlled requirement case first |
| `P-18` | Pre-release, local version, epoch, or nonstandard version semantics | Less common | Medium | PEP 440 supports richer version semantics than simple dotted versions | Prevents naive comparison and category inference | Generated/version-contract cases |

## 5. Pull-request lifecycle and revision scenarios

| ID | Scenario | Band | Confidence | Why it occurs | Product relevance | Preferred evidence form |
|---|---|---|---|---|---|---|
| `L-01` | PR remains at one stable head during analysis | Very common | Medium | Many reviews complete before Dependabot rebases or new commits appear | Normal exact-head snapshot path | Real normal-path cases |
| `L-02` | Dependabot rebases to resolve conflicts or update the branch | Common | High | GitHub documents automatic Dependabot rebasing by default | Old evidence must not silently apply to the new head | Real external validation plus synthetic multi-snapshot case |
| `L-03` | Maintainer requests rebase or Dependabot update through a comment command | Common | High | Dependabot exposes explicit PR comment commands | Produces intentional head transition and potential evidence change | Real case if captured prospectively; otherwise synthetic timeline |
| `L-04` | Extra maintainer commits change Dependabot rebase behavior | Usual / recurring | High | GitHub documents that Dependabot normally stops rebasing after extra commits unless skip markers allow force-push behavior | Revision ownership and branch behavior become material | Synthetic repository timeline; later real validation |
| `L-05` | Stale open PR stops receiving automatic rebases after 30 days | Usual / recurring among stale PRs | High | GitHub documents the 30-day rebase stop | Evidence freshness and maintainer action differ from an actively maintained PR | Real stale PR or temporal synthetic case |
| `L-06` | Dependabot closes an older PR and opens or updates a grouped/replacement PR | Usual / recurring | High | Grouping and security-update changes can close old PRs and create new ones | Requires supersession rather than overwrite | Real multi-snapshot case |
| `L-07` | Pull request is manually closed, ignored, or deferred by policy | Common | High | Ignore commands and configuration are normal Dependabot controls | Historical action is context, not correctness proof; policy sensitivity matters | Real case with policy record |
| `L-08` | Pull-request conflict requires manual intervention | Usual / recurring | Medium | Dependency changes compete with repository evolution | Separates dependency acceptability from mergeability of the specific PR | Real PR-action divergence case |
| `L-09` | Open Dependabot PR limit prevents creation of another update | Usual / recurring at repository level | High | GitHub documents default version and security update PR limits | Product may need to distinguish absent PR from absent available update | Controlled source/state case rather than full PR scenario |
| `L-10` | Dependabot updates are paused after prolonged maintainer inactivity | Less common | High | GitHub documents automatic deactivation after inactivity conditions | Explains missing updates and stale corpus bias | Controlled repository-state case |
| `L-11` | PR target branch differs from normal default-branch assumptions | Less common | Medium | Security updates and repository configuration can target other branches | Requires exact base and policy identity | Real or synthetic branch-policy case |
| `L-12` | Force-push or rebased history invalidates previously captured file or CI references | Less common but high impact | Medium | Mutable PR branches and ephemeral run references create stale evidence | Central replay, lineage, and stale-state responsibility | Synthetic temporal case plus real validation |

## 6. CI, checks, and execution evidence

| ID | Scenario | Band | Confidence | Why it occurs | Product relevance | Preferred evidence form |
|---|---|---|---|---|---|---|
| `C-01` | All visible required checks pass | Very common | High | Normal pull-request review relies heavily on CI status | Passing CI is evidence, not safety or complete relevance proof | Real normal-path cases |
| `C-02` | No CI or no relevant successful workflow is available | Common | Medium | Small projects, configuration gaps, skipped workflows, or inaccessible evidence occur regularly | Usually drives targeted checks, defer, or unresolved authority | Real case or controlled absence variant |
| `C-03` | CI runs but only installs/builds and does not exercise the changed dependency | Common | Medium | Generic workflows often provide weaker authority than their green status suggests | Requires command-level relevance analysis | Real case; S002 provides one form |
| `C-04` | Relevant tests are skipped by path or event filters | Usual / recurring | High | Workflow filters and conditional jobs are common | Green overall status may hide absent relevant execution | Real case or workflow-level synthetic variant |
| `C-05` | One or more jobs fail after the update | Common | High | Compatibility, resolver, lint, build, test, or infrastructure failures occur | Requires attribution before block or targeted action | Real failure case; S003 provides one form |
| `C-06` | Failure is unrelated, flaky, or pre-existing | Usual / recurring | Medium | CI systems contain infrastructure and nondeterministic failures | Prevents automatic update-caused attribution | Real comparative case or synthetic competing-cause case |
| `C-07` | Matrix is partially successful across Python versions or platforms | Usual / recurring | High | CI commonly uses runtime and platform matrices | Requires environment-specific decision rather than aggregate status | Real matrix case; S005 provides one form |
| `C-08` | Workflow delegates through tox, nox, scripts, reusable workflows, or composite actions | Common | High | Repositories abstract commands behind tooling | Direct command evidence may be incomplete without bounded tracing | Real case when it blocks a decision; otherwise synthetic workflow case |
| `C-09` | Required check is pending, cancelled, neutral, skipped, or timed out | Usual / recurring | High | GitHub Actions supports multiple conclusions beyond pass/fail | Must preserve exact execution state and not collapse it into failure or success | Controlled execution-state matrix |
| `C-10` | Logs are unavailable or expired while run metadata remains | Less common but operationally important | Medium | Logs and artifacts are more ephemeral than run identity | Drives degraded evidence and replay requirements | Real-derived unavailable-log variant |
| `C-11` | CI passes against a different dependency resolution than the proposed evidence assumes | Less common | Medium | Caches, unconstrained resolution, lock drift, or install commands can change effective versions | Requires installed-version or resolution evidence before strong conclusions | Synthetic environment case; later real validation |
| `C-12` | CI permissions or fork/Dependabot security context changes workflow behavior | Less common | High | Dependabot-triggered workflows can have restricted tokens and secret access | Security, acquisition, and false-negative interpretation | Controlled workflow-permission case |

## 7. Upstream, package, and release evidence

| ID | Scenario | Band | Confidence | Why it occurs | Product relevance | Preferred evidence form |
|---|---|---|---|---|---|---|
| `U-01` | Exact package version exists on PyPI with normal metadata | Very common | High | Standard Python package updates resolve through package indexes | Core version and artifact identity | Real cases and fixtures |
| `U-02` | GitHub release notes or an upstream changelog are available | Very common | High | Dependabot PRs frequently embed release-note, changelog, or commit summaries | Useful locator and attributed source evidence, not independent truth | Real cases |
| `U-03` | Important evidence lies across several releases between old and proposed versions | Common | High | A final patch release may not repeat changes introduced earlier in the interval | Requires interval acquisition rather than final-tag-only reasoning | Real interval case; S001 exposed this need |
| `U-04` | Release notes contain breaking changes, migration steps, or deprecations | Common | High | Major and some minor releases document compatibility-relevant changes | Candidate claims must be grounded and mapped to target context | Real behavior-impact case |
| `U-05` | Release evidence is absent, incomplete, or only available as commit history | Common | Medium | Upstream projects vary in release discipline | Drives source hierarchy, degraded states, and stopping | Real case or controlled absence variants |
| `U-06` | Python support floor or ceiling changes | Usual / recurring | High | Package metadata and release notes commonly change supported Python versions over time | Must compare exact target declarations and environments | Real case; current S001 oracle covers one form |
| `U-07` | Wheel or platform coverage changes | Usual / recurring | Medium | Binary packages publish platform- and ABI-specific files; public PR examples include removed platform support | Can make an update installable on one environment and unavailable on another | Real platform case plus synthetic environment matrix |
| `U-08` | Source distribution remains but a required wheel disappears | Less common | Medium | Package release artifact sets can vary by version | Build-toolchain and platform consequences differ from package existence | Real-derived artifact-set case |
| `U-09` | Release or file is yanked after publication | Less common | High | PyPA formally supports yanking and allows yank state to change | Temporal evidence, installer policy, and retrospective decision can differ | Real yanked case or temporal synthetic case |
| `U-10` | Package metadata, source repository, release tag, or publisher identity is ambiguous or mismatched | Less common | Medium | Transfers, stale project URLs, mirrors, and naming differences occur | Central authority-degradation and abstention case | Prefer real candidate; controlled variants for coverage |
| `U-11` | Two authoritative-looking sources make contradictory claims | Less common | Low to medium | Changelogs, releases, metadata, and code can diverge | Contradiction must remain visible rather than collapsed | Real if available; otherwise synthetic conflict case |
| `U-12` | Index-hosted attestation or provenance is available | Less common but increasing | Medium | Python package indexes now expose provenance/attestation mechanisms | Adds verifiability without proving safety | Real provenance case later |
| `U-13` | Proposed version has weaker or missing provenance than previous version | Rare today; high consequence | Low | Attestation adoption is uneven and release pipelines change | Candidate supply-chain degradation signal | Real-derived provenance variant |
| `U-14` | Package is renamed, transferred, archived, or points to a different source host | Less common | Medium | Project ownership and hosting evolve | Exact package/source identity and historical authority | Real identity case or controlled transfer scenario |
| `U-15` | Release notes are generated, copied, truncated, malformed, or contain irrelevant bulk | Common | High | Dependabot bodies aggregate upstream content of varying quality | Requires locator, grounding, relevance, and content-size boundaries | Real examples plus controlled truncation variants |

## 8. Target repository context

| ID | Scenario | Band | Confidence | Why it occurs | Product relevance | Preferred evidence form |
|---|---|---|---|---|---|---|
| `T-01` | Dependency is directly declared and imported or invoked | Common | High | Runtime and tool dependencies are often directly used | Strong relevance path, but behavior and coverage remain separate | Real behavior-impact case |
| `T-02` | Dependency is declared but not statically imported | Common | Medium | Tools, plugins, CLI entry points, build dependencies, and indirect adapters may not appear as imports | Static non-observation is not non-use | Real case or synthetic activation variants |
| `T-03` | Dependency is used only in tests, docs, lint, build, or release automation | Common | High | Development dependencies are widespread | Changes acceptable evidence and consequence | Real cases; existing cycle covers several forms |
| `T-04` | Dependency is transitive and target usage occurs through a parent or adapter | Usual / recurring | High | Many practical dependencies are reached indirectly | Requires dependency path and interface mediation | Real case; S001 and S002 provide forms |
| `T-05` | Repository declares a broader or narrower Python range than CI executes | Common | High | Metadata and test matrices frequently drift | Declared support, tested support, and actual compatibility must remain distinct | Real or synthetic policy matrix |
| `T-06` | Repository supports multiple platforms but CI covers only a subset | Common | Medium | Cross-platform projects often have uneven CI | Platform gap can justify targeted checks or abstention | Real platform case |
| `T-07` | Optional extras or configuration activate the dependency only in some deployments | Usual / recurring | Medium | Python extras and application configuration create conditional paths | Requires activation evidence and explicit unresolved states | Synthetic activation matrix plus real validation |
| `T-08` | Dynamic import, plugin discovery, reflection, or generated code reaches the dependency | Less common | Medium | Frameworks and extensible applications resolve behavior at runtime | Static analysis must abstain from absence claims | Fully synthetic case first; real case later |
| `T-09` | Generated files or artifacts change because of the dependency | Less common | Medium | Formatters, code generators, schema tools, and build tools produce derived outputs | Relevant checks may be artifact comparisons rather than unit tests | Real behavior case or synthetic generated-artifact case |
| `T-10` | Dependency is present in several files with different constraints | Usual / recurring | Medium | Monorepos and multi-environment projects duplicate declarations | Requires reconciliation and scope identity | Real monorepo case or synthetic repository |
| `T-11` | Lockfile includes many unrelated transitive changes | Common | Medium | Resolver output can produce broad diffs | Attribution and baseline review cost increase | Real grouped/lockfile case |
| `T-12` | Repository policy forbids or requires a version, license, platform, source, or provenance condition | Less common explicitly; potentially common implicitly | Low to medium | Maintainer policy is often undocumented or encoded in configuration | Same evidence can justify different actions | Synthetic policy-diff case plus later real policy evidence |

## 9. Acquisition, API, and operational states

| ID | Scenario | Band | Confidence | Why it occurs | Product relevance | Preferred evidence form |
|---|---|---|---|---|---|---|
| `A-01` | Public anonymous API acquisition succeeds | Very common for supported public evidence | High | UpgradePilot's primary boundary is public read-only evidence | Normal live integration proof | Real smoke cases |
| `A-02` | Valid credential increases rate limit or access, while anonymous access remains possible | Common operational condition | High | GitHub supports authenticated and unauthenticated public access with different limits | Credential behavior and least-privilege configuration | Controlled auth/anonymous integration tests |
| `A-03` | Stale or invalid token causes 401/403 while public anonymous access would work | Usual / recurring operational failure | Medium | Local environments often retain expired credentials | Should not turn a public case into false source unavailability | Real-derived credential variant; already observed during B2 work |
| `A-04` | Rate limit is reached | Usual / recurring under scale | High | GitHub documents rate limiting; corpus and shadow modes increase request volume | Retry, backoff, partial run, and cost behavior | Service-level fake and later live bounded verification |
| `A-05` | Request times out | Usual / recurring under large or slow source workloads | High | Dependabot and external APIs document timeout conditions | Distinguish transient acquisition failure from absent evidence | Mock/fake variant |
| `A-06` | Resource returns 404, 410, or disappears after earlier availability | Less common but important | Medium | Logs, artifacts, releases, tags, or repository resources may be removed or expire | Replay, source state, and historical trace | Real-derived unavailable-resource case |
| `A-07` | Paginated acquisition is incomplete | Less common in small cases; common at scale | High | GitHub APIs paginate changed files, runs, jobs, and search results | Count reconciliation and partial-success handling | Service-level synthetic variant |
| `A-08` | Response is malformed, truncated, or has an unexpected schema | Less common | Medium | Networks, source changes, and untrusted upstream data can violate expectations | Parser failure versus source degradation | Controlled data/service case |
| `A-09` | One source succeeds while another fails | Common in multi-source analysis | High | Independent GitHub, PyPI, upstream, advisory, and attestation sources fail separately | Partial progress and evidence sufficiency | Real host plus controlled source variants |
| `A-10` | Retry returns duplicate or changed data | Less common but central to robust orchestration | Medium | Mutable sources and repeated requests create duplicate or superseded records | Idempotency, lineage, and stale-state behavior | Workflow-level synthetic case |
| `A-11` | Private dependency or registry cannot be resolved | Common in private-repository ecosystems; outside initial public-only product boundary | High | GitHub documents private registry and dependency access requirements | Important later, but should not distort current public scope | Reserve until private support is admitted |
| `A-12` | Worker or process stops after partial acquisition or persistence | Rare in small local runs; expected in production systems | Medium | Processes crash, are cancelled, or lose connectivity | Recovery, resumability, and duplicate prevention | Synthetic workflow case after state/persistence admission |

## 10. Decision and reporting scenarios

| ID | Scenario | Band | Confidence | Why it occurs | Product relevance | Preferred evidence form |
|---|---|---|---|---|---|---|
| `D-01` | Transparent baseline and richer investigation agree on merge after normal review | Common | Medium | Many routine updates have sufficient relevant evidence | Tests stopping and whether complexity adds no value | Existing S001/S004 forms; normal regressions |
| `D-02` | Baseline is too cautious; richer evidence supports normal review | Usual / recurring | Medium | Aggregate signals can miss target-scoped non-activation | Measures added value and cost reduction | Existing S005 form; future variants |
| `D-03` | Baseline is too permissive; richer evidence requires targeted checks | Common and central | Medium | Green CI or small version categories can hide missing relevance | Core UpgradePilot value hypothesis | Real behavior-impact case |
| `D-04` | Evidence supports investigate or block | Usual / recurring | Medium | Resolver, build, test, policy, or target-use evidence can reveal concrete blockers | Requires attribution and exact reason | Existing S003 form; future Python-specific case useful |
| `D-05` | Evidence is insufficient, so system defers or abstains | Common as an evidence state; absent as completed central case | Medium | Missing, conflicting, ambiguous, or inaccessible evidence is normal in multi-source systems | Essential honest output and stopping class | First-wave authority-degradation case |
| `D-06` | Dependency version appears acceptable but the specific PR should not merge as-is | Usual / recurring | Medium | PR conflicts, grouping, unrelated failures, or stale heads affect action independently | Requires separate dependency and PR dimensions | Real PR-action divergence case |
| `D-07` | Action stays the same but authority, uncertainty, or explanation changes | Common | High | Additional evidence often strengthens or weakens support without crossing an action threshold | Important for traceability and stopping | Multi-snapshot and counterfactual cases |
| `D-08` | Human-readable and machine-readable reports disagree | Rare if controlled; high-impact defect | Low | Rendering and serialization can drift | Acceptance invariant and regression requirement | Synthetic report-consistency case |
| `D-09` | Report references missing, stale, or wrong evidence identity | Rare if controlled; high-impact defect | Low | Lineage and report generation errors occur in complex pipelines | Must fail validation or degrade, never silently publish | Generated lineage caselets |
| `D-10` | Historical maintainer action differs from UpgradePilot's evidence-backed recommendation | Usual / recurring in retrospective evaluation | Medium | Maintainer choices reflect policy, constraints, or mistakes not visible to the tool | Historical action remains context, not a correctness label | Real retrospective case and adjudication record |

## 11. Security, adversarial, and severe edge scenarios

| ID | Scenario | Band | Confidence | Why it matters | Product relevance | Preferred evidence form |
|---|---|---|---|---|---|---|
| `S-01` | Ordinary untrusted text contains shell-like strings, paths, or commands | Common as content; harmless if contained | High | PRs, logs, and release notes routinely contain executable-looking text | Trust boundary must treat it as data | Controlled content fixtures |
| `S-02` | Explicit prompt injection in release notes, PR body, source, or logs | Rare today; expected adversarial test | Low | LLM-visible evidence may attempt to redefine policy or tool behavior | Central content-authority boundary | Synthetic adversarial caselet |
| `S-03` | Malicious branch name or PR text reaches a shell command | Rare but established automation risk class | Medium | Unsafe interpolation can create command injection | Tool and execution isolation | Synthetic security caselet; no external publication |
| `S-04` | Misleading log text imitates trusted test or tool output | Less common | Low to medium | Logs are untrusted and may include application-controlled text | Source identity and structured evidence matter | Synthetic log caselet |
| `S-05` | Typosquatted, dependency-confusion, or misleading package identity | Rare but high consequence | Medium | Similar package names and source mismatches create supply-chain risk | Identity, registry, and authority validation | Synthetic first; real evidence only when safely public |
| `S-06` | Upstream account, release, or artifact is compromised | Rare and severe | Low | Provenance signals may detect inconsistency but not prove compromise | Requires disciplined claims and security escalation | Do not simulate as factual public accusation; use fictional synthetic case |
| `S-07` | Oversized, deeply nested, malformed Unicode, duplicate-key, or resource-exhaustion payload | Rare as ordinary input; standard adversarial test | Medium | Parsers and models can fail or consume excessive resources | Limits, validation, and fail/degrade behavior | Generated adversarial corpus |
| `S-08` | Source content contains fake citations or forged provenance statements | Less common to rare | Low | Human-readable claims can imitate authority | Evidence identity must come from trusted acquisition, not text assertions | Synthetic grounding caselet |
| `S-09` | Private or sensitive data is accidentally captured in logs or fixtures | Less common but material | Medium | Diagnostic artifacts can preserve unrelated paths, tokens, or personal data | Minimization, redaction, and no-commit boundaries | Synthetic redaction tests; never preserve real secrets |
| `S-10` | Automated external mutation occurs without exact authorization | Rare if controls work; unacceptable | High as policy | Commenting, rerunning, approving, or merging can affect third-party repositories | Hard permission boundary | Deterministic authorization tests only |

## 12. Prevalence-to-case implications

### 12.1 Very common scenarios

These should mainly support:

- normal-path regression;
- baseline calibration;
- integration smoke checks;
- representative corpus coverage later.

They do not automatically justify new full cases because the existing cycle already covers many ordinary forms.

### 12.2 Common scenarios

These are strong candidates when they expose a missing decision, authority, or repository-context responsibility.

High-value common families include:

- grouped updates;
- major or breaking changes;
- incomplete CI relevance;
- direct versus development dependency roles;
- target Python/CI mismatch;
- partial multi-source success;
- defer or abstain.

### 12.3 Usual / recurring scenarios

These often require targeted candidate search or real-derived variants.

High-value recurring families include:

- head rebases and supersession;
- skipped CI paths;
- partial matrices;
- transitive paths;
- environment markers;
- stale PRs;
- dependency-versus-PR action divergence.

### 12.4 Less common scenarios

These are often ideal for the hybrid model:

- find one real host where feasible;
- isolate the condition through controlled variants;
- preserve explicit external-validation debt.

Examples:

- yanked releases;
- source identity mismatch;
- conflicting sources;
- dynamic usage;
- partial pagination;
- artifact-set changes;
- attestation regression.

### 12.5 Rare scenarios

These should normally be fictional, synthetic, generated, or adversarial caselets unless a safe public case is already well documented.

Examples:

- prompt injection;
- shell injection through untrusted metadata;
- package compromise;
- worker interruption at a precise persistence boundary;
- resource-exhaustion payloads;
- forged citations;
- lineage corruption.

Rarity does not reduce security importance. It changes the appropriate evidence form.

## 13. Initial highest-value scenario clusters

Based on coverage gaps, full-route leverage, and realistic feasibility, the catalog supports these clusters first:

### Cluster 1 — Evidence insufficiency and authority degradation

Relevant IDs:

- `U-05`, `U-10`, `U-11`, `A-06`, `A-09`, `D-05`.

Recommended form:

- real candidate where possible;
- real-derived unavailable/ambiguous/conflicting variants;
- synthetic source-conflict case only if necessary.

### Cluster 2 — Head change, stale evidence, and supersession

Relevant IDs:

- `L-02`, `L-03`, `L-05`, `L-06`, `L-12`, `A-10`, `D-07`.

Recommended form:

- synthetic multi-revision repository first;
- real rebased or superseded PR as external validation.

### Cluster 3 — Direct behavior impact and missing relevant coverage

Relevant IDs:

- `P-07`, `C-03`, `C-04`, `C-07`, `U-04`, `T-01`, `T-05`, `T-06`, `D-03`.

Recommended form:

- real public Python case;
- controlled pass/fail check counterfactuals;
- generated policy/environment variations later.

### Cluster 4 — Robust acquisition and replay

Relevant IDs:

- `A-03` through `A-10`, `C-10`, `L-12`.

Recommended form:

- real host plus service-level synthetic failures;
- workflow-level interruption only after run-state and persistence responsibilities are admitted.

### Cluster 5 — Adversarial evidence and trust boundaries

Relevant IDs:

- `S-01` through `S-09`, plus `U-15`.

Recommended form:

- synthetic or generated caselets attached to semantic extraction, reporting, and acquisition cases;
- no malicious external publication.

## 14. Research limitations and revision triggers

This catalog should be revised when one of the following becomes available:

1. a versioned UpgradePilot corpus with scenario labels;
2. shadow-mode observations across a defined sampling period;
3. a reproducible GitHub query/export methodology with deduplication and repository sampling controls;
4. measured frequencies by update type, dependency role, CI state, and action outcome;
5. evidence that one qualitative band is materially wrong;
6. route or supported-domain changes that add or remove scenario families.

Until then, use the bands as a planning aid, not a quantitative claim.

## 15. Primary references

### GitHub

- [Dependabot version updates](https://docs.github.com/en/code-security/concepts/supply-chain-security/dependabot-version-updates)
- [Dependabot security updates](https://docs.github.com/en/code-security/concepts/supply-chain-security/dependabot-security-updates)
- [Managing pull requests for dependency updates](https://docs.github.com/en/code-security/how-tos/secure-your-supply-chain/manage-your-dependency-security/manage-dependabot-prs)
- [Optimizing pull-request creation for Dependabot version updates](https://docs.github.com/en/code-security/tutorials/secure-your-dependencies/optimizing-pr-creation-version-updates)
- [Dependabot errors](https://docs.github.com/en/code-security/reference/supply-chain-security/troubleshoot-dependabot/dependabot-errors)
- [Dependabot updates stopped](https://docs.github.com/en/code-security/reference/supply-chain-security/troubleshoot-dependabot/dependabot-updates-stopped)
- [Controlling which dependencies are updated](https://docs.github.com/en/code-security/how-tos/secure-your-supply-chain/manage-your-dependency-security/controlling-dependencies-updated)
- [How the dependency graph recognizes dependencies](https://docs.github.com/en/code-security/concepts/supply-chain-security/dependency-graph-data)
- [Dependabot supported ecosystems and repositories](https://docs.github.com/en/code-security/reference/supply-chain-security/supported-ecosystems-and-repositories)

### Python Packaging Authority

- [Dependency specifiers](https://packaging.python.org/en/latest/specifications/dependency-specifiers/)
- [`pyproject.toml` specification](https://packaging.python.org/en/latest/specifications/pyproject-toml/)
- [Dependency groups](https://packaging.python.org/en/latest/specifications/dependency-groups/)
- [`pylock.toml` specification](https://packaging.python.org/en/latest/specifications/pylock-toml/)
- [`install_requires` versus requirements files](https://packaging.python.org/en/latest/discussions/install-requires-vs-requirements/)
- [File yanking](https://packaging.python.org/en/latest/specifications/file-yanking/)
- [Simple repository API](https://packaging.python.org/en/latest/specifications/simple-repository-api/)
- [Platform compatibility tags](https://packaging.python.org/en/latest/specifications/platform-compatibility-tags/)

## 16. Summary

```text
very common and common cases
→ normal-path realism and corpus coverage

usual and less-common cases
→ targeted real search plus controlled variants

rare and adversarial cases
→ synthetic or generated coverage with explicit claim limits

all bands
→ admission still controlled by product value, non-duplication, evidence feasibility, and stopping
```

This catalog supplies occurrence context. The companion case-selection matrix determines which situations are worth turning into actual UpgradePilot cases.