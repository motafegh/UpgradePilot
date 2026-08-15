# UpgradePilot

UpgradePilot is a learning-by-building flagship for creating a **production-oriented, evidence-backed dependency-update decision system** for maintainers of public Python repositories.

Given a public Python Dependabot pull request, the intended product supports a bounded maintainer action:

- merge after normal review;
- run targeted checks;
- investigate or block;
- defer;
- abstain.

It is decision support—not an automatic merge bot, generic vulnerability scanner, or proof that an update is safe.

## Product boundary

UpgradePilot focuses on:

- public GitHub-hosted Python repositories;
- Dependabot dependency-update pull requests;
- lawful public GitHub, PyPI, upstream, repository, and available CI evidence;
- exact identity, evidence state, provenance/authority, uncertainty, and abstention;
- repository-specific dependency/CI context;
- bounded decision reports with traceable evidence;
- captured evidence, replay, evaluation, and evidence-gated experiments.

The stable mission, user, product boundary, evidence doctrine, admission rules, termination conditions, and claim limits are controlled by [`PROJECT_CHARTER.md`](PROJECT_CHARTER.md).

## Product flow

```text
public repository and Dependabot PR locator
→ read-only public acquisition
→ exact repository / PR / base / head / dependency identity
→ relevant CI, package, upstream, and repository evidence
→ explicit evidence states and authority
→ bounded interpretation/evaluation
→ conditional analysis or non-activation
→ bounded recommendation or abstention
→ concise human and machine output
→ captured evidence for testing, replay, and diagnosis
```

Passing CI, a version number, merged status, model output, or one score is never proof that an update is safe.

## Repository executable boundaries

```text
src/upgradepilot/   → installable product runtime
tests/              → active deterministic product regression
experiments/        → bounded non-product research/evaluation
experiments/tests/  → regression of experiment/evaluation machinery
tools/              → developer-operated diagnostics and live proofs
```

Product runtime does not import `tests/`, `experiments/`, or `tools/`.

The durable source/package decisions are recorded in:

- [`docs/architecture/ADR-0001-initial-python-source-layout.md`](docs/architecture/ADR-0001-initial-python-source-layout.md)
- [`docs/architecture/ADR-0007-responsibility-based-python-subpackages.md`](docs/architecture/ADR-0007-responsibility-based-python-subpackages.md)

The earlier M2 implementation is historical evidence rather than an active code/design baseline; see [`docs/architecture/ADR-0003-clean-slate-b2-source-reset.md`](docs/architecture/ADR-0003-clean-slate-b2-source-reset.md).

## Project controls

Use the owner that matches the question rather than treating every Markdown file as equivalent authority. [`docs/README.md`](docs/README.md) is the detailed documentation/decision map and durable decision-promotion guide.

| Need | Read |
|---|---|
| Repository-wide agent/artifact rules | [`AGENTS.md`](AGENTS.md) |
| Documentation/decision ownership and promotion map | [`docs/README.md`](docs/README.md) |
| Sole live position and exact continuation | [`MEMORY.md`](MEMORY.md) |
| Stable product mission/boundary/claims | [`PROJECT_CHARTER.md`](PROJECT_CHARTER.md) |
| Route sequence and gates | [`plans/UPGRADEPILOT_90_DAY_PLAN.md`](plans/UPGRADEPILOT_90_DAY_PLAN.md) |
| Learning/execution method | [`OPERATING_GUIDE.md`](OPERATING_GUIDE.md) |
| Reusable local environment baseline | [`ENVIRONMENT.md`](ENVIRONMENT.md) |
| Security/privacy/credential/external-action rules | [`SECURITY.md`](SECURITY.md) |
| Stable technical invariants/standards | [`docs/specifications/`](docs/specifications/) |
| Accepted impact/applicability/investigation/stopping semantics | [`docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md`](docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md) |
| Accepted consequential methods/structures | [`docs/architecture/`](docs/architecture/) |
| Bounded implementation/investigation plans | [`plans/`](plans/) |

Detailed execution evidence, learning snapshots, proposals, audits, historical implementation, and the informal chronicle remain in their dedicated repository areas. Root [`AGENTS.md`](AGENTS.md) is the canonical artifact-routing owner.

## Evidence-derived route

The route is controlled by [`plans/UPGRADEPILOT_90_DAY_PLAN.md`](plans/UPGRADEPILOT_90_DAY_PLAN.md):

```text
D0 → D1 → B1 → B2 → B3 → B4 → B5 → X1 → C1
```

The route file defines stage order and required outcomes only. [`MEMORY.md`](MEMORY.md) states the live selected position.

## Learning by building

UpgradePilot is also a learning system: important responsibilities are meant to be understood through explanation, prediction, implementation, testing, diagnosis, and changed-case practice—not merely by accepting AI-generated code or seeing tests pass.

The detailed operating/learning model lives in [`OPERATING_GUIDE.md`](OPERATING_GUIDE.md).

## Claim discipline

- Documentation/ADRs/plans do not prove implemented behavior.
- Historical code/tests do not establish active coverage.
- Product regression and experiment regression prove different responsibilities.
- AI-generated output or passing tests do not establish learner ownership.
- Product maturity, evidence quality, learning depth, and AI assistance remain separate.
- Default language is **production-oriented**, not production-ready.
- Preserve limitations, failures, abstentions, rejected methods, and uncertainty.
