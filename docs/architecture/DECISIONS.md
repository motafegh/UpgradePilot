# Retained UpgradePilot Architecture Decision Proposals

**Status:** Retained historical proposal register — unreviewed, non-controlling, and not accepted  
**Originally recorded:** 2026-07-19  
**Origin:** AI-generated during the premature scaffold creation  
**Ownership:** None of the listed proposals is Ali-directed, Ali-verified, or Ali-owned  
**Current authority:** None; canonical Career controls, the active tracker, and later bounded decision records control

## Interpretation rule

The entries below preserve potentially useful rationale from the prior generated scaffold. They are **not architecture decisions**. Their former `Accepted`, `Planned`, or `Deferred` labels were unsupported because Ali had not learned, directed, reviewed, or owned the choices.

Each proposal must be reintroduced only when a bounded product responsibility requires it. The relevant baseline, limitation, alternatives, security/maintenance cost, success and rejection conditions, and Ali ownership evidence must be inspected before an explicit `adopt`, `retain as pilot`, `reject`, or `defer` decision is recorded.

| ID | Generated proposal | Current status | Retained rationale | Review trigger |
|---|---|---|---|---|
| D-001 | Use a Python 3.12+ `src/`-layout package | Unreviewed proposal | Matches the previously assumed environment, may reduce accidental root imports, and can support an installable CLI | First bounded package-structure responsibility |
| D-002 | Begin as a CLI-first modular monolith | Unreviewed proposal | A bounded investigation/report workflow may benefit from one process and explicit traceability | First user-visible interface and orchestration responsibility |
| D-003 | Keep the domain core dependency-free | Unreviewed proposal | Simple evidence states and rules may not need a framework; fewer dependencies can reduce maintenance and supply-chain cost | First central representation or policy responsibility |
| D-004 | Use versioned JSON as the canonical input and report contract | Unreviewed proposal | JSON is replayable, diffable, and machine-readable | First input/output representation responsibility; compare with simpler Python structures and the real M1 report |
| D-005 | Render Markdown from a canonical report | Unreviewed proposal | Maintainers need readable output without silently creating two conflicting sources of truth | First human-readable output responsibility |
| D-006 | Use a transparent deterministic policy before ML/LLM/agents | Unreviewed implementation proposal; charter principle remains controlling | A transparent baseline is required by the governing thesis, but the concrete policy shape is not decided | First recommendation-policy responsibility |
| D-007 | Preserve raw evidence separately from normalized contracts | Unreviewed implementation proposal; evidence-separation principle remains controlling | Separation can support provenance, replay, correction, and source-failure diagnosis | First evidence-input and normalization responsibility |
| D-008 | Adopt SQLite at the persistence stage | Unreviewed later-stage proposal | SQLite may provide relational behavior with low operating cost | M3 persistence entry after a real query/persistence need exists |
| D-009 | Keep network acquisition behind adapters and out of unit tests | Unreviewed later-stage proposal | Mutable external sources can make deterministic tests unreliable | First live-acquisition responsibility |
| D-010 | Pin GitHub Actions by immutable commit | Unreviewed CI-security proposal | Immutable action references can reduce workflow supply-chain drift | First authorized CI workflow responsibility |
| D-011 | Do not choose FastAPI, Pydantic, an ORM, Docker, or a cloud provider yet | Retained non-adoption suggestion; not a formal defer decision | None was required by the removed scaffold's legitimate current boundary | A named product or operating limitation creates a concrete need |
| D-012 | Treat advanced systems as branch/pilot comparisons around the core | Unreviewed implementation proposal; governing exposure policy controls | Bounded comparisons may preserve the core and avoid architecture theater | Relevant later exposure package under the approved policy |

## Retained dependency-admission checklist

This checklist is retained as a candidate review aid, not as an accepted architecture contract. Before adding a runtime dependency, an authorized session should record:

1. the exact current limitation;
2. the standard-library or existing baseline;
3. the smallest candidate integration;
4. measurable benefit and rejection condition;
5. security and maintenance cost;
6. how Ali will explain, modify, test, and diagnose it;
7. removal or migration path.

## Superseded first review instruction

The prior file instructed the project to convert UP-S01 into a generated JSON contract and then review selected decisions. That instruction is superseded because the JSON contract and implementation were created prematurely and removed.

The next bounded M2 session must derive its first responsibility from the completed M1 report and the active learning contract. It may inspect these proposals, but it must not treat them as defaults or restore the prior scaffold.