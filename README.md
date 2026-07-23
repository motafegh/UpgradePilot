# UpgradePilot

UpgradePilot is a learning-by-building flagship for creating a
**production-oriented, evidence-backed dependency-update decision system** for maintainers
of public Python repositories.

Given a public Python Dependabot pull request, the product supports one bounded maintainer
action:

- merge after normal review;
- run targeted checks;
- investigate or block;
- defer;
- abstain.

It is decision support—not an automatic merge bot, generic vulnerability scanner, or proof
that an update is safe.

The stable mission, user, boundary, evidence doctrine, admission rules, and claim limits are
controlled by [`PROJECT_CHARTER.md`](PROJECT_CHARTER.md).

## Evidence-derived route

The original M0–M8 decomposition and M2-S03 report-first route were superseded after five
complete product simulations exposed the actual runtime, conditional responsibilities,
CI-authority requirements, baseline behavior, and stopping model.

The controlling route is
[`plans/UPGRADEPILOT_90_DAY_PLAN.md`](plans/UPGRADEPILOT_90_DAY_PLAN.md).

```text
D0 — initial evidence base
→ D1 — contrast closure
→ B1 — implementation responsibility freeze
→ B2 — executable run kernel
→ B3 — public acquisition and replay
→ B4 — deterministic context and decision support
→ B5 — persistence, diagnosis, and evaluation
→ X1 — evidence-gated experiments
→ C1 — hardening, ownership, and portfolio closure
```

Advancement depends on evidence gates, not elapsed time, artifact count, or a fixed number
of cases.

## Current stage

**B1 — Implementation responsibility freeze: active.**

D1 was accepted on 2026-07-23 after S001–S005 established:

- same-action but stronger evidence and calibration;
- missing CI authority requiring targeted checks;
- update-caused failing CI and recovery;
- baseline sufficiency and justified early stopping;
- a baseline-wrong-action case corrected by target-specific evidence.

Current control:

- [`plans/D1_ACCEPTANCE_AND_B1_ACTIVATION.md`](plans/D1_ACCEPTANCE_AND_B1_ACTIVATION.md)
- [`plans/B1_IMPLEMENTATION_RESPONSIBILITY_FREEZE_REQUIREMENTS.md`](plans/B1_IMPLEMENTATION_RESPONSIBILITY_FREEZE_REQUIREMENTS.md)
- [`plans/B1_CURRENT_SOURCE_AND_TEST_RECONCILIATION.md`](plans/B1_CURRENT_SOURCE_AND_TEST_RECONCILIATION.md)

## Clean active-source reset

After B1 inspected the previous M2 implementation, Ali directed the active source to restart
fresh because inherited AI-generated modules and tests could confuse learning and silently
constrain the new runtime.

Accepted decision:

- [`docs/architecture/ADR-0003-clean-slate-b2-source-reset.md`](docs/architecture/ADR-0003-clean-slate-b2-source-reset.md)

Historical archive:

- [`archive/2026-07-23_PRE_B2_M2_IMPLEMENTATION.md`](archive/2026-07-23_PRE_B2_M2_IMPLEMENTATION.md)
- exact pre-reset commit: `e7425dcfc20f093ac10c9a903f1c4ae50a8b2638`

The active package now contains only a minimal package marker and no runtime dependencies.
M2 source, tests, model scripts, and generated outputs are preserved in immutable history,
not active imports or current coverage.

Pydantic, OpenAI, model runtimes, and the former M2 class/file boundaries are neither
inherited nor automatically rejected. Every method and dependency must be justified again
from the clean B1 responsibility.

B2 product implementation remains paused until B1 freezes and Ali accepts the exact
responsibility, semantic boundary, representation, acceptance tests, and bounded plan.

## Discovered runtime

```text
invocation
→ exact frozen case identity
→ operations
→ evidence and evidence states
→ interpretations and findings
→ transparent baseline
→ conditional-stage activation or non-activation
→ bounded decision or abstention
→ machine and human reports
→ follow-up, rerun, and supersession
→ review, ownership, and validation
```

Simulation artifacts demonstrate logical responsibilities. They are not final production
schemas.

## Supported product boundary

UpgradePilot focuses on:

- public GitHub-hosted Python repositories;
- Dependabot dependency-update pull requests;
- lawful public GitHub, PyPI, upstream, repository, and available CI evidence;
- strict identity, provenance, evidence-state, and authority handling;
- repository-specific dependency and CI context;
- transparent baseline comparison;
- deterministic bounded recommendation or abstention;
- traceable machine-readable and human-readable reports;
- replay, evaluation, and later evidence-gated experiments.

Cross-ecosystem simulation cases may test transferable responsibilities. They do not expand
the supported core.

SemVer, CI color, merged status, model output, or a single score is never safety proof.

## Learning by building

```text
real responsibility
→ minimum blocking concept
→ Ali predicts or challenges
→ bounded implementation or investigation
→ inspect evidence
→ diagnose and correct
→ Ali modifies or tests a central part
→ Ali explains the path and limits
→ record demonstrated depth
```

Reading, approving, or running AI-generated work is not mastery.

## Project ownership

| Responsibility | Owner |
|---|---|
| Stable mission, user, boundary, and claim limits | `PROJECT_CHARTER.md` |
| Public orientation | `README.md` |
| Learning and ordinary execution | `OPERATING_GUIDE.md` |
| Route and gates | `plans/UPGRADEPILOT_90_DAY_PLAN.md` |
| Current continuation | `MEMORY.md` |
| Active B1 procedure | `plans/B1_IMPLEMENTATION_RESPONSIBILITY_FREEZE_REQUIREMENTS.md` |
| Discovery evidence | `product-simulation/` |
| Stable technical requirements | `docs/specifications/` |
| Accepted durable methods | `docs/architecture/` |
| Historical implementation snapshots | `archive/` and immutable Git history |
| Implemented truth | active source, active tests, commands, outputs, environment |

## Active source boundary

```text
UpgradePilot/
├── pyproject.toml                 # no runtime dependencies
├── src/
│   └── upgradepilot/
│       └── __init__.py            # package marker only
└── tests/
    └── README.md                  # new B2 tests not written yet
```

This layout does not preselect contracts, frameworks, services, databases, queues, agents,
model runtimes, or deployment systems.

## Start here

1. [`AGENTS.md`](AGENTS.md)
2. [`MEMORY.md`](MEMORY.md)
3. [`plans/UPGRADEPILOT_90_DAY_PLAN.md`](plans/UPGRADEPILOT_90_DAY_PLAN.md)
4. [`plans/B1_IMPLEMENTATION_RESPONSIBILITY_FREEZE_REQUIREMENTS.md`](plans/B1_IMPLEMENTATION_RESPONSIBILITY_FREEZE_REQUIREMENTS.md)
5. [`plans/B1_CURRENT_SOURCE_AND_TEST_RECONCILIATION.md`](plans/B1_CURRENT_SOURCE_AND_TEST_RECONCILIATION.md)
6. active `pyproject.toml`, `src/upgradepilot/`, and `tests/`
7. [`OPERATING_GUIDE.md`](OPERATING_GUIDE.md) when learning or process guidance matters
8. [`PROJECT_CHARTER.md`](PROJECT_CHARTER.md) when scope or claims are material

## Claim discipline

- Documentation does not establish executable behavior.
- Historical code and tests do not establish current behavior or coverage.
- Passing AI-generated tests does not establish Ali-owned capability.
- Product maturity, learning depth, and AI assistance remain separate.
- Default language is **production-oriented**, not production-ready.
- Preserve limitations, failures, abstentions, rejected methods, and uncertainty.