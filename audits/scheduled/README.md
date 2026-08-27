# Scheduled Audits

This folder is the **scheduled lifecycle index** for validated audit questions or opportunities that are not the current implementation responsibility but have been explicitly selected for a concrete future activation trigger and owning execution plan.

Scheduled is stronger than deferred:

```text
deferred
→ valid but no guaranteed near-term execution point

scheduled
→ selected responsibility
→ explicit prerequisite / activation trigger
→ owning plan
→ non-skippable handoff when the trigger is satisfied
```

A scheduled audit is still non-controlling review evidence. Its owning plan defines execution and `MEMORY.md` owns live activation.

Current scheduled audits:

- None.

AUDIT-005 left this index after successful R7 acceptance satisfied its recorded trigger. Its current classification is maintained in `../active/README.md` while the B2/X1 checkpoint is the live responsibility.

If a scheduled trigger becomes invalid before activation, do not silently move on. Reassess the audit/plan and record an explicit reject/defer/reschedule disposition in the owning plan and `MEMORY.md`.
