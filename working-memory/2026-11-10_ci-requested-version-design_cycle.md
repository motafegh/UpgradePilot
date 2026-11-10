# CI requested-version design cycle

Ali selected the design handoff after the [OmniMatch trace](2026-11-10_omnimatch-ci-report-evidence-trace_cycle.md). Main and origin/main reconciled at `95051d20`. Continue from the established difference between a declared argument, a successful job, and a version loaded by pytest. For this bounded planning slice, the preceding lesson and Ali's continuation supply orientation. Preserve the next Build gate for the new producer and storage contract.

UP-SKILL:upgradepilot-planning-design. UP-SKILL:upgradepilot-working-memory.

The design question is whether existing parser output can identify the changed package's literal inline pin with exact command provenance, and which report surface best answers why these green jobs leave proposed-version verification open. Compare raw workflow inspection, a structured static detail and runtime observation. No source/test changes or target execution during design.

## Existing parser check

Read the two public workflow files at the pinned OmniMatch head `22fc7709642599feca7b9527fe4f44874d04e520` with two anonymous Contents GETs. Both HTTP 200 payloads matched the SHA-256 values from the [previous case record](2026-11-09_targeted-check_cross-case-qualification_cycle.md#distinct-positive-check-candidate-on-omnimatch). Passed the unchanged files through `parse_workflow_definition` → `analyze_run_step_commands` → `parse_package_manager_operation`. Checked the admitted HTTPX atom with the existing packaging requirement parser.

| Workflow | Job and static step index | Occurrence | What the parser exposed |
| --- | --- | --- | --- |
| `.github/workflows/passwordless.yml` | `signatures`, 2 | Order 0, bytes 0–256 of the run text | One pip install declaration with literal `httpx==0.27.0` and no option operands |
| `.github/workflows/advanced-models.yml` | `cpu-models`, 4 | Order 0, bytes 0–309 of the run text | One pip install declaration with literal `httpx==0.27.0` and a separate literal `-r` operand |

The parser gives command-level source spans and literal atoms. The probe deliberately selected the known atom and establishes feasibility only. It neither classifies all install argument roles nor supplies the planned producer. The mixed command makes option-role handling mandatory. Without it, an option value that resembles a pin could become a false dependency request.

## Design disposition

The [bounded plan](../plans/CI_REQUESTED_DEPENDENCY_VERSION_REPORT_PLAN.md) selects a structured static request in existing per-workflow CI detail. A raw link is the simplest baseline and remains the citation. A runtime version record would answer a different question. Normal and saved report facts can carry the detail without a new report schema. The owner split is shell syntax → dependency interpretation → CI source binding → native record → report projection. New native coverage needs an explicit codec version, while the historical version keeps its original meaning and decoding path. The existing generic version-1-only dispatch is an implementation constraint to resolve for the CI coverage family, with an explicit stop if it requires a broader storage change.

Forty-three focused existing parser, coverage and report tests passed. Governance doctor and documentation checks passed. These verify the starting point and plan references. Planned positive/negative/cold-recovery proof remains Build work. The handoff is the literal argument-admission increment before persistence or rendering, with the OmniMatch pair and pedido-service as the closest contrast.

```text
A0/A1/A2 — Reconciled main and carried forward the selected design from the report trace.
B — Compared delivery options and scoped the owner, grammar, persistence, and qualification path.
Verification — Two exact workflow parser probes and 43 existing controls passed.
D/E — Explain requested versus installed/tested and the option-value boundary. Build orientation and qualification remain separate.
C — Design decisions and proof limits preserved here and in the selected plan.
```
