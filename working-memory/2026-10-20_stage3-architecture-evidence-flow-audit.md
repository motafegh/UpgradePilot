# Stage 3 architecture and end-to-end evidence-flow audit

**Date:** 2026-10-20  
**Status:** ACTIVE  
**Mode:** cross-responsibility Repository Audit  
**Branch:** `audit/project-wide-system-audit-2026-10-20`  
**Main base reconciled:** `a1c291c6cf9238493eeb666b184192ed178b90f1`  
**Program:** [Project-wide technical audit and correction program](../plans/PROJECT_WIDE_TECHNICAL_AUDIT_AND_CORRECTION_PROGRAM_PLAN.md)  
**Prior result:** [AUDIT-014](../audits/2026-10-20_AUDIT-014_product-value-and-evaluation-sequencing.md)

## Audit-program cadence

`reconcile → audit/classify → verify → record → fix/route when justified → continue`

No separate D/E learning ceremony is required for this audit slice.

## Audit question

Trace the actual current product path and determine whether accepted Workspace architecture and active implementation have one coherent authority path or unresolved competing state surfaces.

Primary trace:

```text
public PR locator/acquisition
→ native evidence/results
→ Workspace capture/revisions/lifecycle
→ interpretation/evaluation/applicability
→ maintainer-action synthesis
→ report projection/save/open
```

Questions:

1. What is the canonical owner of each material fact/result today?
2. Does `PublicPullRequestInvestigation` remain only a bounded compatibility/projection surface, or is it still an independent truth object alongside Workspace?
3. Are Workspace revisions built from the same native results or are facts recomputed/copied in ways that can drift?
4. Which downstream consumers read Workspace directly versus legacy investigation fields?
5. Does report/synthesis currently consume canonical Workspace state or legacy state?
6. Are recovery, saved-report reopen and deterministic replay still clearly separated?
7. Which temporary migration layers have explicit removal/cutover triggers, and which have become open-ended debt?
8. Do ADR-0012/0013, the Workspace implementation plan, source and tests still agree?

## Boundaries

- inspect normal producer/consumer paths before judging local duplication;
- passing tests do not justify a compatibility layer by themselves;
- temporary dual surfaces are not defects when one-way derivation, authority and removal trigger are clear;
- projections must not strengthen or recompute evidence authority;
- do not refactor source during the audit pass;
- preserve distinct recovery, saved-report inspection and deterministic replay semantics.

## Provenance

`UP-SKILL:upgradepilot-repository-audit`
