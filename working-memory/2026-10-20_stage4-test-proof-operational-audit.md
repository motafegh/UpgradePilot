# Stage 4 tests, proof, reproducibility and operational integrity audit

**Date:** 2026-10-20  
**Status:** ACTIVE  
**Mode:** cross-responsibility Repository Audit  
**Branch:** `audit/project-wide-system-audit-2026-10-20`  
**Main base last reconciled:** `a1c291c6cf9238493eeb666b184192ed178b90f1`  
**Program:** [Project-wide technical audit and correction program](../plans/PROJECT_WIDE_TECHNICAL_AUDIT_AND_CORRECTION_PROGRAM_PLAN.md)  
**Prior result:** [AUDIT-015](../audits/2026-10-20_AUDIT-015_workspace-authority-and-consumer-cutover.md)

## Audit-program cadence

`reconcile → audit/classify → verify → record → fix/route when justified → continue`

No separate D/E learning ceremony is required for this audit slice.

## Audit question

Determine whether UpgradePilot's current proof system is the smallest sufficient one for the claims and migration state that matter now.

Audit:

1. local deterministic product tests versus hosted verification;
2. Workspace native/lifecycle/recovery proof versus legacy/report proof;
3. missing parity/cutover proof exposed by AUDIT-015;
4. duplicated or implementation-shape tests that do not protect an independent responsibility;
5. clean installation/CLI/package proof;
6. Python support declaration versus tested interpreter matrix;
7. saved-report reopen, Workspace recovery and deterministic replay proof classes;
8. push/PR CI, required checks and branch protection;
9. experiment tests versus product proof and whether they are accidentally counted together;
10. what exact proof should gate a future Workspace direct-consumer cutover.

## Boundaries

- evaluate test value by independent proof responsibility, not raw count;
- do not delete tests during the audit pass;
- a hosted workflow can be useful without being a sufficient canonical integration gate;
- local passing suites do not establish hosted/installed behavior;
- model/experiment qualification stays outside ordinary deterministic product CI;
- Python `>=3.12` metadata is a compatibility declaration, not proof every future Python release works;
- recovery, report reopen and replay remain separate claims.

## Initial pressure points

- latest hosted success is far behind current main;
- `main` has no required check/ruleset;
- hosted workflow tests only Python 3.12 while package metadata is open-ended `>=3.12`;
- current Workspace tests are strong for the admitted subset but complete Workspace→synthesis/report parity is not yet present because cutover is not implemented;
- report tests strongly protect the legacy path;
- future migration must avoid retaining both full proof suites indefinitely after legacy retirement.

## Provenance

`UP-SKILL:upgradepilot-repository-audit`
