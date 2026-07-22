# UpgradePilot

UpgradePilot is a learning-by-building flagship for creating a
**production-oriented, evidence-backed dependency-update decision system** for
maintainers of public Python repositories.

Given a public Python Dependabot pull request, the product supports one bounded
maintainer action:

- merge after normal review;
- run targeted checks;
- investigate or block;
- defer; or
- abstain.

It is decision support—not an automatic merge bot, generic vulnerability scanner,
or proof that an update is safe.

The stable mission, user, product boundary, evidence doctrine, admission rules,
termination conditions, and claim limits are controlled by
[`PROJECT_CHARTER.md`](PROJECT_CHARTER.md).

## Evidence-derived route

The original M0–M8 decomposition and M2-S03 report-first implementation route were
replaced after three complete product simulations exposed the actual runtime and
artifact lifecycle.

The controlling route is:

[`plans/UPGRADEPILOT_90_DAY_PLAN.md`](plans/UPGRADEPILOT_90_DAY_PLAN.md)

Current route:

```text
D0 — S001–S003 evidence base complete
→ D1 — S004/S005 contrast closure
→ B1 — minimum credible runtime responsibility freeze
→ B2 — executable run kernel
→ B3 — public acquisition and replay
→ B4 — deterministic repository context and decision support
→ B5 — persistence, diagnosis, and evaluation
→ X1 — admitted experiments and advanced exposure
→ C1 — hardening, ownership, and portfolio closure
```

Advancement depends on evidence gates, not elapsed time, document count, artifact
count, or a fixed number of scenarios.

## Current stage

**D1 — Contrast closure**

Completed:

- S001 — retrospective Python transitive/advisory case;
- S002 — retrospective Python adapter/partial-green-CI case;
- S003 — prospective failing-install/peer-conflict transfer case.

Next:

1. S004 — deliberately simple baseline-sufficient control;
2. S005 — baseline-wrong-action or dependency-versus-PR-action divergence;
3. focused synthesis;
4. freeze the first credible implementation responsibility.

Implementation remains paused until that gate passes.

The locally governed simulation workspace is
[`product-simulation/`](product-simulation/).

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

Cross-ecosystem simulation cases may test transferable reasoning or artifact
responsibilities. They do not expand the frozen supported core.

SemVer, passing CI, failing CI, merged status, model output, or a single score is
never safety proof.

## Project ownership

| Responsibility | Owner |
|---|---|
| Stable mission, user, boundary, and claim limits | `PROJECT_CHARTER.md` |
| Public orientation and navigation | `README.md` |
| Learning, execution, blockers, and assistance fading | `OPERATING_GUIDE.md` |
| Route, stages, capacity protection, and gates | `plans/UPGRADEPILOT_90_DAY_PLAN.md` |
| Current bounded continuation | `MEMORY.md` |
| Current simulation execution | nearest local files under `product-simulation/` |
| Required technical behavior and invariants | `docs/specifications/` |
| Accepted consequential methods | `docs/architecture/` |
| Actual implementation truth | source, tests, commands, outputs, and environment |
| Material execution evidence | `working-memory/` or the active governed evidence workspace |

Career contains durable career/program state and formal capability assessments.
It is not the live project-control system.

## Learning by building

The operating loop is:

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

Learning material belongs in [`learning/`](learning/) only when it preserves
reusable understanding, correction, transfer, diagnosis, or ownership value.

## Source boundary

```text
UpgradePilot/
├── pyproject.toml
├── src/
│   └── upgradepilot/
└── tests/
```

This does not pre-create speculative services, databases, queues, agents, model
runtimes, or deployment systems.

## Start here

1. [`AGENTS.md`](AGENTS.md)
2. [`MEMORY.md`](MEMORY.md)
3. [`plans/UPGRADEPILOT_90_DAY_PLAN.md`](plans/UPGRADEPILOT_90_DAY_PLAN.md)
4. the nearest local `AGENTS.md` and current local plan
5. [`OPERATING_GUIDE.md`](OPERATING_GUIDE.md) when process or learning guidance matters
6. [`PROJECT_CHARTER.md`](PROJECT_CHARTER.md) when product scope or admission is material
7. the applicable specification or ADR
8. current source, tests, outputs, and evidence

## Repository layout

```text
UpgradePilot/
├── README.md
├── PROJECT_CHARTER.md
├── AGENTS.md
├── OPERATING_GUIDE.md
├── MEMORY.md
├── SECURITY.md
├── src/
├── tests/
├── learning/
├── plans/
├── product-simulation/
├── proposals/
├── working-memory/
├── examples/
├── chronicle/
└── docs/
    ├── specifications/
    └── architecture/
```

## Claim discipline

- Documentation or ADRs do not establish executable behavior.
- Passing AI-generated tests does not establish Ali-owned capability.
- Product maturity, learning depth, and AI assistance remain separate.
- Default language is **production-oriented**, not production-ready.
- Preserve limitations, failures, abstentions, rejected methods, and uncertainty.
