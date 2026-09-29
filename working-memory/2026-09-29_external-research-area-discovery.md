# External Research Area Discovery — Pre-Research

**Recorded:** 2026-09-29
**Branch:** `analysis/ai-agentic-capability-map-2026-09-28`
**Status:** PRE-RESEARCH COMPLETE; deeper reports pending.
**Owner plan:** `plans/AI_AGENTIC_ARCHITECTURE_INDEPENDENT_CHALLENGE_AND_COMPARISON_PLAN.md`

This record preserves the broad discovery pass used to expand the independent research program. It is not an architecture verdict.

## Main discovery

The relevant external landscape is substantially broader than AI/agent architecture. UpgradePilot should later compare itself with product and engineering patterns from dependency bots, SCA/reachability platforms, remediation/codemod engines, dependency/evidence graphs, provenance standards, workflow/runtime observability, code/repository intelligence, PR-review agents, risk/confidence signals, maintainer workflow design, evaluation benchmarks, and execution-security systems.

## Research families discovered

1. Closest dependency-update products: Dependabot, Renovate/Mend, GitHub Dependency Review, Updatecli.
2. Risk/reachability/upgrade-impact: Endor Labs, Semgrep Supply Chain, Snyk, Socket.
3. Remediation/migration: OSV-Scanner guided remediation, OpenRewrite/Moderne, DepRepair, Griffe/japicmp.
4. Dependency/evidence graphs: deps.dev, GUAC, OSS Review Toolkit, Trivy/SBOM.
5. Provenance/standards: in-toto, SLSA, GitHub artifact attestations/Sigstore, SPDX/CycloneDX/VEX.
6. CI/workflow/runtime: actionlint, zizmor, StepSecurity, act.
7. Program analysis: CodeQL, Joern, symbolic execution.
8. Repository intelligence: RepoGraph, LocAgent, Repository Intelligence Graph, AutoCodeRover.
9. AI PR review/agents: GitHub Copilot code review/cloud agent, OpenHands, SWE-agent, Agentless.
10. Risk/confidence/reputation: Dependabot compatibility, Renovate Merge Confidence, OpenSSF Scorecard, release age/adoption/cooldown, package behavior.
11. Maintainer UX/policy: dashboards, approval, grouping, scheduling, rules, escalation, explanation.
12. Evaluation: BUMP, DepBench/DepRepair, SWE-bench-style evaluation, calibration/selective prediction, replay.
13. Agent execution security: sandbox/policy enforcement, untrusted repository/prompt-injection boundaries.
14. Ecosystem extensibility: manager/datasource/versioning adapters, analyzer/provider abstractions, recipe ecosystems.
15. Product positioning: maintainer pain, review load, differentiation, adoption friction, useful report/output shape.

## Pre-research signals

- Dependabot supports scheduling, cooldown and grouped updates; compatibility scores use CI outcomes from other public repositories.
- Renovate combines update automation with Dashboard approval/package rules and Merge Confidence signals.
- GitHub Dependency Review adds dependency-diff, vulnerability, license and scope policy.
- Endor Labs exposes reachability plus direct-dependency Upgrade Impact Analysis.
- Socket evaluates dependency behavior changes, not only known CVEs.
- OSV-Scanner guided remediation evaluates transitive graphs and alternative risk/change strategies.
- OpenRewrite/Moderne demonstrate upgrade recipes that can change dependency declarations and source/API usage together.
- deps.dev/GUAC/ORT demonstrate reusable dependency/supply-chain graph and policy pipelines.
- in-toto/SLSA/artifact attestations demonstrate portable provenance claims.
- StepSecurity demonstrates runtime process/network/file observation; zizmor demonstrates complementary static CI analysis.
- Griffe demonstrates Python API breaking-change detection.
- Copilot code review demonstrates a PR-review surface with agentic context gathering, repository instructions, skills/MCP, re-review, and configurable approval authority.

## Representative sources checked

- https://docs.github.com/en/code-security/concepts/supply-chain-security/dependabot-version-updates
- https://docs.github.com/en/code-security/concepts/supply-chain-security/dependency-review
- https://docs.renovatebot.com/key-concepts/dashboard/
- https://docs.renovatebot.com/merge-confidence/
- https://docs.endorlabs.com/scan-with-endorlabs/language-scanning/
- https://semgrep.dev/blog/2025/what-you-should-know-about-dependency-reachability-in-sca/
- https://docs.socket.dev/docs/socket-for-github
- https://google.github.io/osv-scanner/experimental/guided-remediation/
- https://docs.openrewrite.org/
- https://docs.moderne.io/
- https://docs.deps.dev/
- https://docs.guac.sh/guac/
- https://oss-review-toolkit.org/ort/docs/intro
- https://slsa.dev/
- https://in-toto.io/
- https://docs.stepsecurity.io/
- https://docs.zizmor.sh/
- https://mkdocstrings.github.io/griffe/
- https://docs.github.com/en/copilot/how-tos/use-copilot-agents/request-a-code-review/use-code-review
- https://scorecard.dev/

## Next

Start Tier-1 deep reports one family at a time. Each report must separate observed features/evidence from transferable ideas and from any later UpgradePilot recommendation.
