# Product Simulation Scenario Coverage

**Status:** D1 coverage complete and accepted  
**Project route:** [`../plans/UPGRADEPILOT_90_DAY_PLAN.md`](../plans/UPGRADEPILOT_90_DAY_PLAN.md)  
**Accepted synthesis:** [`D1_FINAL_SYNTHESIS_AND_B1_ENTRY.md`](D1_FINAL_SYNTHESIS_AND_B1_ENTRY.md)  
**Acceptance record:** [`../plans/D1_ACCEPTANCE_AND_B1_ACTIVATION.md`](../plans/D1_ACCEPTANCE_AND_B1_ACTIVATION.md)

This file records compact cross-case coverage. It is not a production schema, frequency
claim, case-count rule, or implementation authorization.

## Scenario register

| Scenario | Main contrast | Baseline/full relationship | Full decision | Review state |
|---|---|---|---|---|
| [`S001`](scenarios/S001-pydantic-soupsieve-2.6-to-2.8.4/README.md) | Python transitive docs/advisory path; relevant green CI | same action; stronger authority, calibration and auditability | merge after normal review | factual correction complete; Ali accepted cross-case synthesis |
| [`S002`](scenarios/S002-kubernetes-dashboard-token-api-httpx-0.27.2-to-0.28.1/README.md) | direct declaration; adapter path; relevant tests skipped | same action; exact relevance and targeted checks added | run targeted checks | AI recheck complete; behavior remains externally unconfirmed |
| [`S003`](scenarios/S003-event-handler-loader-typescript-5.9.3-to-7.0.2/README.md) | failing install; peer conflict; comparison and attribution | same broad action; exact failure, cause and recovery added | block current proposal as-is | public evidence strongly supports result; local reproduction unavailable |
| [`S004`](scenarios/S004-glyphslib-pytest-9.0.2-to-9.0.3/README.md) | exact relevant green control; stopping | baseline sufficient | merge after normal review | validation passed with method degradation |
| [`S005`](scenarios/S005-modelarrayio-pytest-9.0.3-to-9.1.1/README.md) | exact lock-backed matrix; target-scoped caution | baseline wrong action | merge after normal review | validation passed with method degradation |

## Comparative classes

| Class | Evidence |
|---|---|
| Same action, materially stronger support | S001, S002, S003 |
| Baseline sufficient | S004 |
| Baseline wrong action | S005 |
| Dependency/PR action divergence | limited one-case exposure; not required for B1 |
| Unresolved comparison | not directly covered; does not currently block B1 |

The cases are contrasting evidence, not representative validation.

## Repeated logical responsibilities

- invocation distinct from exact identity;
- stable run and record identities;
- operation history;
- evidence records with explicit states and provenance;
- observation, interpretation, and finding separation;
- transparent baseline;
- bounded decision or abstention;
- machine and human reports from the same state;
- follow-up, rerun, supersession, and changed-boundary transitions;
- review and ownership separation;
- conditional activation and non-activation;
- raw or durable evidence references;
- structural validation;
- no target mutation by default.

These are logical responsibilities, not approved physical production artifacts.

## Conditional responsibilities

- advisory and exploitability analysis;
- adapter/framework compatibility;
- package identity and hash checks;
- repeated or matrix execution comparison;
- causal failure attribution;
- semantic-version and declared-range analysis;
- stopping, cost, and overreach evaluation;
- dynamic or isolated execution;
- private or credentialed acquisition;
- platform, native, compiler, or toolchain analysis;
- post-merge publication and deployment evidence;
- separate dependency-update and PR-action dimensions.

Conditional work must not become universal merely because one case used it.

## Conditional artifact dispositions

- `CHECK_EXECUTIONS.jsonl` — repeated conditional stable candidate after S003/S005;
- `FAILURE_ATTRIBUTION.json` — conditional candidate demonstrated in S003;
- `STOPPING_EVALUATION.json` — conditional candidate demonstrated in S004.

## Contradicted assumptions

- one dependency-role enum is adequate;
- direct imports are the only relevance path;
- green or red CI color has global authority;
- a workflow name proves the responsibility exercised;
- advisory vocabulary always requires exploitability analysis;
- merge history proves correctness;
- every case needs dynamic execution or deep investigation;
- more artifacts or investigation imply higher quality;
- the full method must always change the action;
- manual success proves automation.

## Automation boundary at B1 entry

Strong deterministic candidates:

- IDs and frozen identity;
- simple version/lock mutations;
- baseline execution;
- record and reference validation;
- extraction of supplied workflow/job/step/command evidence;
- matrix execution representation;
- report rendering from accepted state;
- transition mechanics.

Tool-assisted or interpretive:

- complex dependency path and role;
- CI authority;
- upstream activation-condition extraction;
- target relevance and negative-evidence sufficiency;
- failure attribution;
- proportionate action;
- stopping and cost judgment.

Human controlled:

- target mutation;
- residual-risk acceptance;
- repository policy and override;
- architecture and method admission;
- capability assessment.

## Gate status

D1 technical evidence and Ali acceptance gates are satisfied.

Current project stage:

> **B1 — Implementation responsibility freeze**

No additional simulation is authorized by default. Another case requires a named B1 or
later evaluation uncertainty.

Coverage does not establish target safety, production-schema fitness, automated
reliability, representative frequency, or independently owned capability.
