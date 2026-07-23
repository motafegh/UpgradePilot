# UpgradePilot

UpgradePilot is a learning-by-building flagship for creating a **production-oriented, evidence-backed dependency-update decision system** for maintainers of public Python repositories.

Given a public Python Dependabot PR, the product supports one bounded maintainer action:

- merge after normal review;
- run targeted checks;
- investigate or block;
- defer;
- abstain.

It is decision support—not an automatic merge bot, generic vulnerability scanner, or proof that an update is safe.

The stable mission, product boundary, evidence doctrine, and claim limits are controlled by [`PROJECT_CHARTER.md`](PROJECT_CHARTER.md).

## Evidence-derived route

The historical M0–M8 and M2-S03 report-first routes were replaced after S001–S005 exposed the actual runtime, artifact lifecycle, conditional stages, stopping behavior, and baseline failure modes.

The controlling route is [`plans/UPGRADEPILOT_90_DAY_PLAN.md`](plans/UPGRADEPILOT_90_DAY_PLAN.md).

```text
D0 — initial evidence base complete
→ D1 — technical discovery complete; Ali review pending
→ B1 — minimum credible runtime responsibility freeze
→ B2 — executable replay-to-decision kernel
→ B3 — public acquisition and replay
→ B4 — deterministic repository context and decision support
→ B5 — persistence, diagnosis, and evaluation
→ X1 — evidence-gated experiments
→ C1 — hardening, ownership, and portfolio closure
```

Advancement depends on evidence gates, not elapsed time, documents, artifacts, or a fixed case count.

## Current stage

**D1 technical discovery is complete. Ali acceptance review is the remaining gate before B1.**

Completed contrasts:

- S001 — same action, stronger authority and calibration;
- S002 — same action, missing CI authority and targeted checks;
- S003 — same broad action, failing-install cause and recovery;
- S004 — baseline sufficient and justified early stop;
- S005 — baseline wrong action; target evidence changed `run_targeted_checks` to `merge_after_normal_review`.

Current sequence:

1. review [`product-simulation/D1_FINAL_SYNTHESIS_AND_B1_ENTRY.md`](product-simulation/D1_FINAL_SYNTHESIS_AND_B1_ENTRY.md);
2. record Ali's acceptance, corrections, or deferred disagreements;
3. activate [`plans/B1_IMPLEMENTATION_RESPONSIBILITY_FREEZE_REQUIREMENTS.md`](plans/B1_IMPLEMENTATION_RESPONSIBILITY_FREEZE_REQUIREMENTS.md);
4. inspect current source/tests and freeze the smallest credible executable responsibility;
5. create one bounded B2 implementation plan;
6. begin the replay-to-decision kernel through learning by building.

Implementation remains paused until the D1 acceptance/B1 freeze gate passes.

## Supported product boundary

UpgradePilot focuses on:

- public GitHub-hosted Python repositories;
- Dependabot dependency-update PRs;
- lawful public GitHub, PyPI, upstream, repository, and available CI evidence;
- strict identity, provenance, evidence-state, and authority handling;
- repository-specific dependency and CI context;
- transparent baseline comparison;
- bounded recommendation or abstention;
- traceable machine and human reports;
- replay, evaluation, and later evidence-gated experiments.

Cross-ecosystem discovery does not expand the frozen supported core. SemVer, CI color, merged status, model output, or a score is never safety proof.

## Project ownership

| Responsibility | Owner |
|---|---|
| Stable mission, user, boundary, and claim limits | `PROJECT_CHARTER.md` |
| Public orientation | `README.md` |
| Learning/execution and assistance fading | `OPERATING_GUIDE.md` |
| Route and gates | `plans/UPGRADEPILOT_90_DAY_PLAN.md` |
| Current continuation | `MEMORY.md` |
| D1 evidence and synthesis | `product-simulation/` |
| Current B1 procedure | `plans/B1_IMPLEMENTATION_RESPONSIBILITY_FREEZE_REQUIREMENTS.md` |
| Stable technical requirements | `docs/specifications/` |
| Durable selected methods | `docs/architecture/` |
| Implemented truth | source, tests, commands, outputs, and environment |

## Learning by building

```text
real responsibility
→ minimum blocking concept
→ Ali predicts or challenges
→ bounded investigation or implementation
→ inspect evidence
→ diagnose and correct
→ Ali modifies or tests a central part
→ Ali explains the path and limits
→ record demonstrated depth
```

## Source boundary

```text
UpgradePilot/
├── pyproject.toml
├── src/upgradepilot/
└── tests/
```

This does not pre-create speculative services, databases, queues, agents, models, or deployment systems.

## Start here

1. [`AGENTS.md`](AGENTS.md)
2. [`MEMORY.md`](MEMORY.md)
3. [`plans/UPGRADEPILOT_90_DAY_PLAN.md`](plans/UPGRADEPILOT_90_DAY_PLAN.md)
4. [`product-simulation/D1_FINAL_SYNTHESIS_AND_B1_ENTRY.md`](product-simulation/D1_FINAL_SYNTHESIS_AND_B1_ENTRY.md)
5. [`plans/B1_IMPLEMENTATION_RESPONSIBILITY_FREEZE_REQUIREMENTS.md`](plans/B1_IMPLEMENTATION_RESPONSIBILITY_FREEZE_REQUIREMENTS.md)
6. the nearest local instructions, specifications, source, tests, outputs, and evidence

## Claim discipline

- Documentation does not establish executable behavior.
- AI-generated completion does not establish Ali-owned capability.
- Product maturity, learning depth, and assistance remain separate.
- Default language is **production-oriented**, not production-ready.
- Preserve failures, limitations, abstentions, rejected methods, and uncertainty.