# Effective Package-Manager Semantics — Package-State Proof Boundary Review (2026-09-24)

**Status:** CANDIDATE REVIEW FINDING — supporting the ACTIVE `2026-09-24_effective-package-manager-semantics-system-design.md`; not an accepted architecture, new product proof contract, plan replacement, implementation, or Build authorization.

**Owners and prior work:** `MEMORY.md` (live selection); `plans/RUNTIME_DEPENDENCY_STATE_PROOF_COMPLETION_PLAN.md` (bounded execution and proof sequence); `2026-09-24_runtime-state-reconciled-design-baseline.md` (index of existing accepted proof contracts and source references); `2026-09-21_f6-post-install-package-state-feasibility.md` §§6–9 (existing explicit observation, provenance, time, and later-use requirements); `2026-09-24_r2_state-witness-scope-checkpoint.md` (reuse an already sufficient witness rather than requiring redundant later checks).

## Review question and current design candidate

How can **Command-Derived Requirement-State Proof** (historical Route A) and **Direct Target-Owned Package-State Observation** (historical Route B) contribute trustworthy package-state evidence without conflating their source, environment, or time boundaries or forcing duplicate observations?

**Candidate common claim envelope, not a concrete data-type selection:**

- **What:** exact proposed distribution/package identity, version, and exact proposition established (requirement satisfied versus directly observed installed-distribution presence, without silently claiming selected artifact or actual use).
- **Where:** target repository/head, workflow run and attempt, job, exact relevant execution/interpreter/package destination environment, and a *positively supported* relation to the selected dependency-consuming environment. Same job or matching package/version text alone is not environment equality.
- **When:** exact command-completion boundary for command-derived proof, or exact observation occurrence/position for direct state inspection; explicit ordering/available time evidence, rather than inventing a wall-clock timestamp when only occurrence/step order is established.
- **How known:** command semantics plus exact admitted runtime-success/operation guarantee, **or** direct target-owned inspection output bound to an actual executing occurrence, with source/retention limits and unresolved fields preserved.

Two qualified witnesses may independently support a suitably scoped state proposition; they are **not simultaneously required**. Do not collapse their different claims and provenance into a generic unqualified `package_installed=true`. An already sufficient command-completion witness needs no later inventory for *that same bounded claim*. Direct observations are conditional on real target-owned output being available and positively attributable; a syntactically visible `pip inspect`/`pip list` invocation, an installer `--report` under dry-run, or a successful enclosing step alone is not automatically an installed-state observation.

## Concrete existing-source constraint

`src/upgradepilot/ci/runtime_strengthening.py` currently permits a sole ordinary top-level command under selected GitHub execution profiles, and a first ordinary top-level command in an admitted sequential Bash/sh script. Other positions/shapes remain unresolved unless stronger evidence is provided. Therefore an inspection appearing later in a multicommand step must **not** inherit positive execution support merely from the step's success. Any future direct-observation adapter must respect that existing bound and separately establish that the exact observed output came from the exact target-owned inspection occurrence. This does not say such observations are impossible; it says the current correlation proof cannot simply be reused beyond its admitted scope.

## Claim-relative continuation, not automatic persistence

A claim that a later test used the proposed version needs extra positive relationships: matching relevant interpreter/environment and selected version, suitable ordering, and sufficient continuity across *material* intervening mutations, plus actual consumption/invocation evidence. These are previously identified downstream proof gaps, not a new automatically selected subsystem or mandatory condition on every state result. Missing material relationships remain unresolved; do not scan every intermediate command indiscriminately or equate package presence with compatibility or maintainer-action permission.

## Still to review before boundary selection

1. Which *normal real supported* target-owned outputs and execution shapes can satisfy the direct-inspection identity/execution/environment requirements? The earlier investigation establishes feasibility, not a universal producer.
2. Can the common proposition remain sufficiently precise without erasing the difference between `requirement satisfied at command completion` and `installed distribution observed at time T`? Preserve origin-specific limitations even if a later composition shares a normalized fact.
3. How do command/process-level effective environment facts resolve unknown upstream configuration only for material dimensions, without requiring a full runner/shell emulator? This remains the larger active subsystem-boundary question.

**Next discussion:** contrast an exact-version command-completion witness with an inspection in a different Python environment. Decide which environment-identity relationship must be positively proven before either witness may support the selected dependency-consuming environment. Continue descriptive names first; historical labels only parenthetically for retrieval.

UP-SKILL:upgradepilot-planning-design  
UP-SKILL:upgradepilot-learning-by-doing  
UP-SKILL:upgradepilot-working-memory
