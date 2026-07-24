# UpgradePilot Current Memory

**Last updated:** 2026-07-24  
**Purpose:** Concise project-local continuation. Source, tests, commands, outputs,
artifacts, and the actual environment remain the authority for behavior.

## Current route

The controlling route is
[`plans/UPGRADEPILOT_90_DAY_PLAN.md`](plans/UPGRADEPILOT_90_DAY_PLAN.md).

Historical M0–M8 and M2-S03 routes are superseded. The stable core remains a Python
implementation for maintainers of public Python repositories receiving Dependabot PRs.

## Completed discovery and acceptance

S001–S005 established:

```text
S001–S003: same broad action, materially stronger support
S004: baseline sufficient and early stop justified
S005: baseline wrong action corrected by target-specific evidence
```

Ali accepted D1 on 2026-07-23.

- Acceptance: [`plans/D1_ACCEPTANCE_AND_B1_ACTIVATION.md`](plans/D1_ACCEPTANCE_AND_B1_ACTIVATION.md)
- Synthesis: [`product-simulation/D1_FINAL_SYNTHESIS_AND_B1_ENTRY.md`](product-simulation/D1_FINAL_SYNTHESIS_AND_B1_ENTRY.md)

D1 is passed. No S006 is authorized merely to continue.

## Current stage

**B1 — Implementation responsibility freeze: active.**

Controlling procedure:

- [`plans/B1_IMPLEMENTATION_RESPONSIBILITY_FREEZE_REQUIREMENTS.md`](plans/B1_IMPLEMENTATION_RESPONSIBILITY_FREEZE_REQUIREMENTS.md)

Current reconciliation:

- [`plans/B1_CURRENT_SOURCE_AND_TEST_RECONCILIATION.md`](plans/B1_CURRENT_SOURCE_AND_TEST_RECONCILIATION.md)

## B1 route correction

Ali rejected the replay-first B2 sequence on 2026-07-24 because it made the learning path
begin with internal fixtures, run terminology, and prepared evidence rather than the real
product behavior.

The controlling sequence now begins B2 with the thinnest real vertical slice:

```text
public repository + Dependabot PR locator
→ read-only public acquisition
→ exact base/head and changed-file identity
→ minimum relevant evidence
→ bounded evaluation
→ recommendation or abstention
→ concise output
```

Captured responses and replay support deterministic tests, debugging, and reproducibility.
They are not the primary product interface or learning path.

## Clean active-source decision

After implemented-truth inspection, Ali explicitly rejected inheriting the substantially
AI-generated M2 source and tests because they could confuse his learning and silently
constrain the new runtime.

Accepted decision:

- [`docs/architecture/ADR-0003-clean-slate-b2-source-reset.md`](docs/architecture/ADR-0003-clean-slate-b2-source-reset.md)

Historical archive:

- [`archive/2026-07-23_PRE_B2_M2_IMPLEMENTATION.md`](archive/2026-07-23_PRE_B2_M2_IMPLEMENTATION.md)
- exact pre-reset commit: `e7425dcfc20f093ac10c9a903f1c4ae50a8b2638`

ADR-0002's Pydantic adoption is superseded. Pydantic, OpenAI, HTTP clients, validation
libraries, and other dependencies are neither inherited nor rejected; every dependency must
be justified again from the new responsibility.

## Current implemented truth

The active product tree is intentionally minimal:

```text
pyproject.toml                    # package metadata; no runtime dependencies
src/upgradepilot/__init__.py      # package marker only
tests/README.md                   # no active product tests yet
```

M2 runtime modules, tests, model scripts, and generated model outputs are absent from the
active tree and preserved only through immutable history.

No product runtime behavior is currently claimed. Structural validation passed for TOML
parsing, package compilation, and an isolated source-path import. A real clean checkout,
editable installation, live acquisition command, and active product test suite have not yet
been proven.

## Immediate continuation

1. Freeze the smallest complete public PR-to-decision vertical slice.
2. Define the initial repository/PR locator and minimum read-only public acquisition.
3. Define exact identity, supported dependency-change shape, relevant CI/check evidence,
   minimum upstream/package evidence, and honest unsupported or abstention behavior.
4. Define the bounded evaluation and concise output the first slice owns.
5. Define captured-response use only for deterministic tests, debugging, and later replay.
6. Select the smallest dependency, representation, and user-facing interface from zero.
7. Define universal and conditional responsibilities.
8. Define the minimum B2 live-smoke, captured-response, failure, and output-consistency tests.
9. Define Ali-owned implementation, test, diagnosis, and explanation work.
10. Create one bounded B2 implementation plan after the responsibility freeze is accepted.
11. Begin B2 only after its plan is authorized.

Do not:

- restore or import archived M2 source;
- copy archived tests or count them as current coverage;
- inherit old class names, file boundaries, Pydantic, OpenAI, model, or HTTP architecture;
- resume M2-S03;
- select S006 without a named blocker;
- start B2 code before B1 passes;
- begin from a replay-only product interface;
- copy simulation JSON files directly into production schemas;
- hardcode S004, another known PR, or an expected decision into product logic;
- select database, service, queue, model, agent, graph, or deployment architecture before
  its gate;
- infer product safety, production readiness, automated semantic reliability, or Ali-owned
  capability from historical or AI-generated work.

## Ownership state

Ali identified the simulation defect, authorized S001–S005, accepted D1, made the
controlling clean-source decision, and corrected the replay-first implementation sequence to
preserve real-world learning clarity. Technical execution and repository edits remain
substantially AI-assisted. B2 must introduce central Ali prediction, implementation,
testing, diagnosis, and explanation before capability claims.