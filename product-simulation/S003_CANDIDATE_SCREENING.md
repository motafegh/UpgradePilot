# S003 Candidate Screening

**Status:** Complete; one candidate selected  
**Screening date:** 2026-07-22  
**Screening actor:** AI assistant under Ali's authorization  
**Governing requirements:** [`S003_FAILING_CI_SCENARIO_REQUIREMENTS.md`](S003_FAILING_CI_SCENARIO_REQUIREMENTS.md)

This record precedes the selected S003 run. It has no S003 run ID and must not be treated as selected-case runtime evidence.

## Screening objective

Select one real public dependency-update pull request with:

- exact base and proposed-head identity;
- actual failing decision-relevant CI;
- accessible workflow, run, job, step, command, and bounded log evidence;
- at least one credible comparison boundary;
- genuine causal alternatives;
- safe and manageable scope;
- materially new coverage beyond S001 and S002.

## Candidates reviewed

| Candidate | Initial observation | Screening result |
|---|---|---|
| `xayanide/event-handler-loader#341` — TypeScript 5.9.3 → 7.0.2 | Exact one-dependency update; `Linters` failed while CodeQL passed; failure occurs in `Clean install NPM dependencies` before ESLint; exact base/head available; public job log available; adjacent PR #342 from the same base passed the same workflow | **Selected** |
| `xayanide/event-handler-loader#342` — `@types/node` 24.10.2 → 26.1.1 | Exact same base as #341; both `Linters` and CodeQL passed; useful comparison execution but no failing CI | Rejected as S003 candidate; retained as comparison evidence |
| `ayunis-core/ayunis-core#870` — OpenAI Node 4.104.0 → 6.48.0 | Large two-major-version update inside a broader backend repository; no bounded failing job and causal comparison were established during screening | Rejected for this scenario because scope and attribution boundary were not yet bounded |
| `communitiesuk/prsdb-webapp#1636` — Immutable 5.1.5 → 5.1.9 | Security/fix-oriented patch update; no failing run was frozen during bounded screening and the security-remediation shape overlaps S001 | Rejected for S003; potentially useful for a later baseline/security control |
| `Twijune/athletickle-website#4` — ESLint 9.39.2 → 10.7.0 | Major tooling update and non-mergeable PR, but the initial screen did not establish an accessible failing run, command, and comparison boundary before a stronger candidate was found | Rejected for S003; failure evidence not sufficiently frozen during screening |

## Selected candidate

**Repository:** `xayanide/event-handler-loader`  
**Pull request:** `#341`  
**Update:** `typescript` `5.9.3` → `7.0.2`  
**Base:** `05df3f80631ec061ee2d55307b7492d200c03faf`  
**Proposed head:** `f6d6daba48567457018bf6cc171f235d4dda4ef2`  
**Observed pull-request merge ref:** `f019e9b25a1476f393a3ecf525871f6990017cb8`

### Why it satisfies S003

1. The PR changes only `package.json` and `package-lock.json` for one direct development dependency.
2. Pull-request workflow run `29954108891` has a failed `Lint code` job (`89038742970`).
3. The failed step is `Clean install NPM dependencies`, executing `npm ci`; the actual `Lint code` step is skipped.
4. The same workflow's `Lint commit` job passes, and CodeQL run `29954108920` passes.
5. Adjacent Dependabot PR `#342`, created from the exact same base SHA and executed minutes later, passes `npm ci` and the lint step in workflow run `29954113594`.
6. Both compared lint jobs use Ubuntu 24.04.4, runner-image version `20260714.240.1`, Node `lts/*` resolving to Node 24, and the same workflow definition at the shared base.
7. The proposed lockfile records `typescript-eslint` 8.65.0 parser and TypeScript-ESTree peer ranges of `>=4.8.4 <6.1.0`, while the root proposal selects TypeScript 7.0.2.
8. Competing initial explanations remain worth preserving: update-caused peer conflict, invalid generated lock state, runner/npm environmental change, or a broader pre-existing repository issue.
9. The comparison boundary is strong enough to test those alternatives without mutating the target repository.
10. The case adds actual failing-CI attribution, repeated check executions, prospective persistence, and the dependency-assessment versus PR-action question.

## Selection limits

Selection does not predetermine the final causal classification. In particular:

- the workflow name `Linters` does not mean lint rules failed;
- a failed `npm ci` step does not by itself identify which dependency constraint is causal;
- the adjacent passing PR is highly useful but is not identical to a base/head controlled reproduction;
- no target repository mutation or rerun is authorized;
- local reproduction is conditional on whether public evidence leaves a material unresolved question and whether an isolated environment can be constructed safely.

## Next state

Create the S003 selected-and-frozen checkpoint with a new prospective run identity. Preserve the restricted baseline before using deeper repository, lockfile, peer-range, and comparison evidence in the full investigation.
