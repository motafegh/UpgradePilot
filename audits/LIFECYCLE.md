# Audit Lifecycle

Audit records are durable non-controlling review evidence. Their folder records **current lifecycle**, not authority.

```text
audits/active/    validated findings selected as inputs to current engineering work
audits/deferred/  validated findings/opportunities not selected for current work
audits/absorbed/  findings whose material conclusions have been incorporated into stronger owners
```

Lifecycle movement must preserve the audit ID and history. Moving an audit does not itself modify product behavior, specifications, ADRs, plans, or live state.

When an audit becomes active, the current plan/`MEMORY.md` must identify the selected responsibility. When it becomes absorbed, the stronger owner or completed work should make the disposition clear. Deferred audits should be re-entered only on a concrete trigger or explicit selection.
