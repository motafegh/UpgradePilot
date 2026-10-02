# State-proof routes, environment/time, and exercise — cross-case reality check

**Date:** 2026-09-24  
**Kind:** Non-controlling Product Simulation synthesis; no new numbered case or product architecture authorization.

## Research question

For the current main design's **Command-Derived Requirement-State Proof** versus **Direct Target-Owned Package-State Observation**, when does real evidence already establish the bounded requirement/package-state claim, and when is additional environment, continuity, or exercise evidence actually necessary?

**Current main owner at research time:** `MEMORY.md` and `working-memory/2026-09-24_effective-package-manager-semantics-system-design.md` at `main@b27f0c8fc8e2e04746f715d779c0fa55d9878c03`. Main describes the subsystem boundary as a candidate, not approved architecture/Build. This research branch has not merged that main head; refer to its live owners for later changes.

## Reused real cases — no duplicate scenario

| Case | What/where/when is established | What additional evidence would be needed for a stronger claim? |
| --- | --- | --- |
| **S014 — production-ready-cicd #11** | Exact PR requirement `pip==26.2.1`; dependency-audit job's `pip install -r requirements-tooling.txt` reports `Requirement already satisfied` in the selected CPython site-packages. This is direct operation-time state evidence; the command did not freshly install pip. | For a later actual use of *that pip version*, identify the later consumer's interpreter/environment, timing, and use of pip. The later `pip-audit --requirement requirements.txt` step alone does not establish that the changed `pip` version was the behavior under test. Do not require a redundant later inventory for the already-established command-time claim. |
| **S016 — Thumbor #1867** | In the tests-selected uv environment, `uv sync --locked --extra tests` succeeds and reports `+ coverage==7.15.4`. In the release/build-selected environment, a separate successful uv operation excludes coverage. | To prove later coverage execution, establish its use in the same selected environment after the applicable state boundary. The release/build job's success cannot be borrowed; nor is another inventory automatically necessary for the tests-scope command-completion claim. |
| **S013 — LangChain #40646** | Earlier explicit `uv sync` reports `anyio==4.15.1` in the selected test environment; later `uv run` with `UV_NO_SYNC=true` executes pytest and reports the anyio plugin in that test context. | The later observation is relevant because the desired claim crosses from earlier sync time to later test execution. Test success/plugin listing still does not prove that all changed-package behavior was exercised or that the package remains present indefinitely. |
| **S015 — charset-normalizer #769** | The changed marker-scoped pytest requirement is active for Python 3.8 but ignored for Python 3.9. The 3.8 install fails; the 3.9 install succeeds against its different active requirement. | No package-state positive can be borrowed across matrix rows. Failure to install a required version does not prove global package absence. The current UpgradePilot extractor conservatively does not admit the marker-decorated exact pin. |

## Exact proposition boundaries

A. `requirement R satisfied in selected environment E at completion of command C`:
- A positively closed command-derived path can be sufficient. A later inventory is not a universal additional gate.
- A trusted directly observed same-time/same-environment state may be an independent route; it does not prove command C *caused* the state.

B. `package/version P present in E at observation time T`:
- Requires observation tied to package/version, selected environment, runtime/source identity, and T. Cannot be silently treated as the state at a different time or job.

C. `later command X used P in E`:
- Needs positive identity of the later environment and a bounded relation to the earlier state, plus actual use/consumption evidence for X. Inspect intervening state mutation only to the extent material to this later claim.

D. `changed behavior was exercised successfully`:
- Stronger still. Package presence, a green unrelated job, an installer log, or a plugin being listed is insufficient by itself.

## Incremental information / over-engineering test

Ask of each proposed additional witness:

> Which *new* proposition will this witness establish that is not already positively supported by the nearest trustworthy source?

- If the answer is only to repeat an already-supported command-time fact, do not require it as another gate.
- If the target is a later time, different environment, or actual behavior, acquire only the positive linking evidence relevant to that specific claim.
- If a required link remains missing, preserve `unresolved` rather than inventing continuity or converting missing evidence into negative evidence.
- Keep operation-derived inference and direct observation as distinct provenance paths even if they eventually support the same precisely scoped state proposition.

## Fastavro #867 screening — not a new scenario

A current-read real manually authored PR, `fastavro/fastavro#867`, adds `backports.zstd ; python_version<'3.14'` to `developer_requirements.txt` and includes a Python 3.14 / older-Python CI matrix that executes `pip install -r developer_requirements.txt`. The packaging specification says a false environment marker causes the dependency to be ignored. The PR head `f4503ee855767bae48278206c901f68cf3d4d48d` has a successful Python 3.14 Linux job `58131685639` in run `20196007734`, but its log returned HTTP 410 and cannot be used as an observed installer-result witness.

**Disposition:** useful independent *mechanism/control* example, but a weaker match than already admitted S015: not Dependabot, no exact version transition for backports.zstd, and runtime log unavailable. Do not assign a new scenario number or treat it as fresh evidence of installed state.

## Main handoff / stopping

The current proposed two-route subsystem boundary is consistent with these real cases **provided** it preserves package/version, selected environment, observation time/command completion, exact run/job scope, proof provenance, and non-claims. The examples do not select a data schema, parser, generic environment resolver, or product Build.

**Stop this slice:** Existing retained cases suffice for the marker/selector question and initial where/when/provenance comparison. Next evidence work should target a genuinely missing relationship—particularly an exact changed-dependency consumer retargeted to a different environment with an observable later use—or a concrete main design choice that these retained cases cannot discriminate.
