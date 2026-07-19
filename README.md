# UpgradePilot

UpgradePilot is a 90-day learning-by-building flagship project for creating an evidence-backed dependency-update decision system for maintainers of public Python repositories.

Given a public Python Dependabot pull request, the eventual product will produce a provenance-backed, uncertainty-aware recommendation to:

- merge after normal review;
- run targeted checks;
- investigate or block;
- defer; or
- abstain.

It is decision support—not an automatic merge bot, a generic vulnerability scanner, or proof that an update is safe.

## Current state

| Field | State |
|---|---|
| Program window | 2026-07-20 through 2026-10-17 |
| Current route | R1 — Manual evidence reality |
| Current milestone | M1 — First manual evidence decision |
| Manual-evidence track | UP-S01 is active separately on `pydantic/pydantic#13432` |
| Repository track | Architecture and bounded bootstrap authorized by Ali on 2026-07-19 |
| First integration action | Convert the completed UP-S01 evidence into the canonical JSON input and run the deterministic report |

Ali explicitly authorized architecture and a bounded product scaffold to proceed in parallel while UP-S01 runs elsewhere. This local decision does not claim that M1 passed and does not silently modify the Career tracker. It authorizes the modular-monolith structure, evidence contracts, deterministic policy, CLI, tests, packaging, and CI contained here. Live acquisition, persistence, corpus construction, learned methods, services, queues, containers, agents, Kubernetes, and cloud work remain evidence-gated.

## Authority and provenance

The [Career repository](https://github.com/motafegh/Career) remains the canonical authority for the 90-day program, workload, gates, tracker, and approved session plans.

This repository contains a read-only local snapshot of every active UpgradePilot control document at Career commit `b226bd50ef94685166b1660da4320eabb12bbe13` from 2026-07-19. See [snapshot provenance](docs/program/SOURCE.md) for the exact file set and verification procedure.

If the canonical Career repository and this snapshot differ, Career controls. Update Career first, then refresh the snapshot as one reviewed synchronization change.

## Start here

Read the local authority snapshot in this order:

1. [Execution Contract](docs/program/career/governance/EXECUTION_CONTRACT.md)
2. [Strategy and Scope](docs/program/career/strategy/STRATEGY_AND_SCOPE.md)
3. [Governing Project Charter](docs/program/career/UpgradePilot.md)
4. [Capability and Prerequisite Specification](docs/program/career/strategy/UPGRADEPILOT_CAPABILITY_AND_PREREQUISITE_SPECIFICATION.md)
5. [Learning and Execution Contract](docs/program/career/governance/UPGRADEPILOT_LEARNING_AND_EXECUTION_CONTRACT.md)
6. [90-Day Master Roadmap](docs/program/career/plans/UPGRADEPILOT_90_DAY_MASTER_ROADMAP.md)
7. [Staged Milestone Plan](docs/program/career/plans/UPGRADEPILOT_STAGED_MILESTONE_PLAN.md)
8. [Evidence and Progress Tracker](docs/program/career/tracking/UPGRADEPILOT_EVIDENCE_AND_PROGRESS_TRACKER.md)
9. [First Session Plan](docs/program/career/plans/UPGRADEPILOT_FIRST_SESSION_PLAN.md)
10. [Session and Blocker Protocol](docs/program/career/operations/SESSION_PROTOCOL.md)

The retained learning profile, selection specification, advanced-systems policy, daily operating plan, security rules, and Career agent instructions are also preserved under [docs/program/career](docs/program/career/README.md).

## Begin the journey

UP-S01 is a bounded, read-only evidence session. Its required report belongs in the canonical Career repository at:

```text
tracking/evidence/UP-S01_pydantic-13432_manual-evidence-report.md
```

Begin with the exact start message from the [First Session Plan](docs/program/career/plans/UPGRADEPILOT_FIRST_SESSION_PLAN.md):

```text
START DAY 1
Actual date: YYYY-MM-DD
Mode: Green | Yellow | Red
Available focused minutes:
Current deliverable: UP-S01 manual evidence report for pydantic/pydantic#13432
First expected proof: verified PR identity, base/head revisions, changed file, and Ali's initial prediction
```

UP-S01 does not execute cloned upstream code, install the changed dependency, or create a corpus. Architecture and the bounded local bootstrap may proceed here in parallel, but the UP-S01 report and Career tracker remain canonical for the manual-evidence result. When the report completes, transform its verified evidence into the example input and inspect how the deterministic baseline responds.

## Run the bootstrap

The runtime has no third-party dependencies.

```bash
PYTHONPATH=src python -m upgradepilot validate examples/pydantic-13432.bootstrap.json
PYTHONPATH=src python -m upgradepilot analyze \
  examples/pydantic-13432.bootstrap.json \
  --output-dir artifacts
PYTHONPATH=src python -m unittest discover -s tests -v
```

The bootstrap example deliberately contains unresolved evidence and therefore must not be treated as the UP-S01 recommendation.

See [System Architecture](docs/architecture/ARCHITECTURE.md) and [Decision Record](docs/architecture/DECISIONS.md) before changing boundaries or adding dependencies.

## Operating principles

- One mission, one active milestone, one exact next action.
- Real evidence before automation; deterministic behavior before learned or agentic methods.
- Predict before consequential interpretation or execution.
- Preserve raw evidence, provenance, missing/conflicting states, tests, limitations, and AI assistance.
- Prefer the smallest credible product behavior; admit technology only after an observed need and a measurable comparison.
- Treat timeboxes as ceilings. Gates and evidence—not elapsed hours—determine progress.
- Claim only what the evidence supports: production-oriented is not production-ready.

## Repository layout

```text
UpgradePilot/
├── README.md                 # project entry point and current gate
├── AGENTS.md                 # repository operating rules for AI agents
├── SECURITY.md               # public-repository safety boundary
├── .gitignore                # secret, environment, and generated-file protection
├── pyproject.toml            # package metadata and CLI entry point
├── src/upgradepilot/         # modular-monolith product package
├── tests/                    # domain, adapter, CLI, and changed-case evidence
├── examples/                 # bounded manual-input examples
├── .github/workflows/ci.yml  # dependency-minimal CI
└── docs/
    ├── architecture/         # system design and decisions
    └── program/
        ├── SOURCE.md         # snapshot provenance and synchronization rules
        ├── FILES.txt         # exact mirrored file set
        └── career/           # read-only active Career authority snapshot
```
