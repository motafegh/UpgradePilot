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

For the sole live project position, selected bounded plan, latest verified evidence, and exact
continuation, read [`MEMORY.md`](MEMORY.md).

## Evidence-derived route

The controlling route is
[`plans/UPGRADEPILOT_90_DAY_PLAN.md`](plans/UPGRADEPILOT_90_DAY_PLAN.md).

```text
D0 — initial evidence base
→ D1 — contrast closure
→ B1 — implementation responsibility freeze
→ B2 — public PR vertical slice
→ B3 — acquisition and replay robustness
→ B4 — deterministic context and decision support
→ B5 — persistence, diagnosis, and evaluation
→ X1 — evidence-gated experiments
→ C1 — hardening, ownership, and portfolio closure
```

Advancement depends on evidence gates, not elapsed time, artifact count, or a fixed number
of cases. The route file defines stage order and required outcomes; it does not record which
stage is selected.

## Historical clean-source decision

ADR-0003 records the accepted clean reset that separated the product source from the earlier
M2 implementation:

- [`docs/architecture/ADR-0003-clean-slate-b2-source-reset.md`](docs/architecture/ADR-0003-clean-slate-b2-source-reset.md)
- [`archive/2026-07-23_PRE_B2_M2_IMPLEMENTATION.md`](archive/2026-07-23_PRE_B2_M2_IMPLEMENTATION.md)
- exact pre-reset commit: `e7425dcfc20f093ac10c9a903f1c4ae50a8b2638`

Historical source and tests remain evidence, not active imports, coverage, or automatic design
precedent. Every dependency and consequential method must be justified from the selected
responsibility.

## Product flow

```text
public repository and Dependabot PR locator
→ read-only public acquisition
→ exact base, head, changed-file, dependency, and version identity
→ relevant repository, CI, package, and upstream evidence
→ explicit evidence states and provenance
→ observations, interpretations, and findings
→ transparent baseline and bounded context evaluation
→ conditional-stage activation or non-activation
→ bounded decision or abstention
→ concise human and machine output
→ captured evidence for reproducibility, tests, debugging, and replay
```

Internal lifecycle terminology and additional artifacts are introduced only when implemented
behavior creates a real need for them. Simulation artifacts demonstrate logical
responsibilities; they are not final production schemas.

## Supported product boundary

UpgradePilot focuses on:

- public GitHub-hosted Python repositories;
- Dependabot dependency-update pull requests;
- lawful public GitHub, PyPI, upstream, repository, and available CI evidence;
- strict identity, provenance, evidence-state, and authority handling;
- repository-specific dependency and CI context;
- transparent baseline comparison;
- deterministic bounded recommendation or abstention;
- traceable human-readable and machine-readable output;
- captured evidence, replay, evaluation, and evidence-gated experiments.

Cross-ecosystem simulation cases may test transferable responsibilities. They do not expand
the supported core.

SemVer, CI colour, merged status, model output, or a single score is never safety proof.

## Learning by building

```text
real user-visible responsibility
→ minimum blocking concept
→ Ali predicts or challenges
→ one bounded implementation or investigation action
→ inspect actual source, response, test, or failure evidence
→ diagnose and correct
→ Ali modifies or tests a central part
→ Ali explains the path and limits
→ record demonstrated depth only when material
```

Reading, approving, or running AI-generated work is not mastery.

## Project ownership

| Responsibility | Owner |
|---|---|
| Stable mission, user, boundary, and claim limits | `PROJECT_CHARTER.md` |
| Public orientation | `README.md` |
| Sole live position and continuation | `MEMORY.md` |
| Learning and ordinary execution | `OPERATING_GUIDE.md` |
| Route and gates | `plans/UPGRADEPILOT_90_DAY_PLAN.md` |
| Bounded scope, sequence, proof, and stop lines | applicable file under `plans/` |
| Discovery evidence | `product-simulation/` |
| Stable technical requirements | `docs/specifications/` |
| Accepted durable methods | `docs/architecture/` |
| Historical implementation snapshots | `archive/` and immutable Git history |
| Implemented truth | source, tests, commands, outputs, environment |

## Start here

1. [`AGENTS.md`](AGENTS.md)
2. [`MEMORY.md`](MEMORY.md)
3. the route or bounded plan selected by `MEMORY.md`
4. relevant source and tests
5. [`OPERATING_GUIDE.md`](OPERATING_GUIDE.md) when process guidance matters
6. [`PROJECT_CHARTER.md`](PROJECT_CHARTER.md) when scope or claims are material

## Claim discipline

- Documentation does not establish executable behavior.
- Historical code and tests do not establish current behavior or coverage.
- Passing AI-generated tests does not establish Ali-owned capability.
- Product maturity, learning depth, and AI assistance remain separate.
- Default language is **production-oriented**, not production-ready.
- Preserve limitations, failures, abstentions, rejected methods, and uncertainty.