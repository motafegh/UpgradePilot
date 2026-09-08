# System limitations and correctness investigation plan

**Artifact status:** Investigation plan requested by Ali; does not authorize product fixes or capability expansion.
**Responsibility:** Independently assess implemented limitations, suspected defects, reliability gaps and proof gaps, then supply evidence for a decision about subsequent work.

## Outcome and ownership

Produce a reviewable finding set that distinguishes deliberate scope limits from incorrect behavior inside supported scope. Each material item must identify the affected proposition, source-to-consumer path, rationale, evidence strength, practical consequence, uncertainty and smallest justified disposition. A result that disproves an earlier assistant concern is a successful investigation outcome.

This is a separate supporting investigation alongside the [artifact integration plan](ARTIFACT_SERVICEABILITY_PUBLIC_INVESTIGATION_INTEGRATION_PLAN.md), not a competing build route. [MEMORY.md](../MEMORY.md) retains canonical project continuation. The [dated investigation record](../working-memory/2026-09-08_system-limitations-and-correctness-investigation.md) preserves this task's progression and time-scoped handoff; it does not replace live project state.

Applicable owners:

- [Charter](../PROJECT_CHARTER.md): supported product, evidence doctrine and claim limits.
- [Core contracts](../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md): snapshot, provenance, failure, authority and implementation-retention obligations.
- [Decision model](../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md): impact, applicability, uncertainty and investigation semantics.
- [Workflow architecture](../docs/architecture/ADR-0008-bounded-static-github-actions-workflow-definition.md): provider structure and static/runtime separation.
- [Dependency/CI plan](B2_DEPENDENCY_ENVIRONMENT_AND_CI_CONSUMPTION_EVIDENCE_PLAN.md): admitted environment consumption and excluded correlation work.
- [Delivery route](UPGRADEPILOT_90_DAY_PLAN.md): acquisition robustness and later capability admission.
- [Operating guide](../OPERATING_GUIDE.md), [environment](../ENVIRONMENT.md), [security](../SECURITY.md): reasoning, proof environment and external-evidence handling.

## Scope and permitted work

Trace the normal CLI/application path through PR identity and files, dependency sources, CI acquisition and interpretation, PyPI/upstream evidence, semantic extraction, target relevance, artifact applicability and presentation. Inspect the relevant tests and existing proof records. Review persistence/replay and overall decision/evaluation gaps only to classify their relationship to this flow; their existing proposals retain design ownership.

During investigation, source, tests, controls and the other task's working records remain read-only. Maintain this plan and its own working record; retain public-safe diagnostic evidence when a concrete check needs it. No product repair, CLI redesign, database implementation, dependency change, framework experiment, target-code execution, live model call or hosted workflow dispatch follows automatically from this plan.

The initial planning slice ends after these artifacts and documentation checks. Later investigation uses bounded non-mutating inspection and, when the applicable environment and user constraints permit, isolated deterministic diagnostic checks. Existing executable-proof deferrals must not be bypassed merely because another tool appears available. If execution remains unavailable, continue source/API/fixture reasoning and mark the outcome unverified by execution.

## Coordination and revision discipline

At each substantive checkpoint:

1. Inspect Git status, exact local and remote revisions, current main-plan boundary and affected source diff. Do not overwrite or stage another task's edits.
2. Identify whether the suspected behavior still exists. Record the precise revision for every finding; use file hashes as well when uncommitted changes affect the inspected path.
3. Compare relevant changes with the previous checkpoint. Preserve corrections and supersession explicitly; do not carry a missing-feature claim forward after implementation appears.
4. If a file changes during a check, mark that result as applying to its captured snapshot or repeat only the affected check. Avoid drawing one conclusion from mixed revisions.
5. Reuse main-task test evidence only when its revision, inputs, command and assertion boundary actually match. Neither duplicate its proof campaign nor claim its completion from written tests.

Freshness reads/fetches do not imply permission to reset, rebase or replace the shared checkout. An isolated checkout may be used later if needed for a reproducible diagnostic; record its revision and keep it outside the product working changes. Findings affecting the main task are reported to Ali with a concrete source/evidence handoff; this plan does not authorize unsolicited messages to other agents or tasks.

## Investigation sequence

### Establish the dated baseline

Map producer → application composition → consumer for each relevant responsibility. Record implemented behavior, intended boundary, authored test coverage and separately observed execution evidence. Consult earlier acquisition/CI audits only for the exact overlapping concern; determine whether each was absorbed, deferred or superseded before duplicating it.

Finish when the inventory can distinguish missing implementation, deliberate abstention, suspected wrong positives, operational failure and absent proof without assuming that every limitation should be removed.

### Investigate correctness and identity first

Treat the following as seed hypotheses from the preceding source review, not verdicts. Recheck them against the baseline before diagnosis.

| Question | Smallest discriminating case / comparison | Proof needed |
|---|---|---|
| Can command recognition promote comment or quoted data into a requirements-install declaration? | Compare a real `pip install -r requirements.txt` declaration with `pip install pytest # -r requirements.txt`; add quoted separator/heredoc contrasts only where the same mechanism is implicated | Trace parser → direct-install observer → CI support → Target admission; establish whether unsupported syntax abstains or creates a false positive |
| Can changed-file patches be associated with the wrong PR revision? | Provider sequence in which head changes between identity and files while file count remains constant; contrast an unchanged head | Show exactly where revision correspondence is established or missing, including patch-derived source contexts; distinguish API snapshot limits from count completeness |
| Can run metadata and jobs refer to different attempts? | A rerun between run discovery and `latest` job acquisition with unchanged run ID/head SHA; contrast a stable attempt | Inspect attempt identity, endpoint semantics and downstream success classification; determine whether another owner already prevents mixing |
| Can CI acquisition failure erase or prevent independent evidence? | Timeout, malformed response or rate limit on runs/jobs after valid PR/dependency evidence; contrast typed unavailable workflow content | Trace exceptions versus typed problems through the application and CLI; distinguish legitimate prerequisite failure from unrelated branch failure |
| Which diagnostic states are lost at presentation? | Supply or inspect distinct tag/index/changelog problems and compare the rendered stopping reason; refresh artifact rendering separately | Identify information already available in the result but absent or misleading in output, without prescribing a report redesign |

Use the cheapest sufficient proof boundary. A local helper reproduction does not establish an application failure; include composition evidence where the claim depends on it. A deterministic fake-provider sequence establishes handling of that sequence, not the frequency of races in public operation. Do not execute third-party workflow text to understand it.

Finish each question as confirmed within a named proof boundary, disproved, intentional limitation, superseded, or unresolved with one missing discriminating check. Do not leave “potential issue” as an unqualified permanent verdict.

### Assess intentional limits against real cases

Evaluate these families proportionately:

- CI event/source coverage, reusable workflows, command recognition and static-to-runtime correlation;
- Target multi-job selection, matrices/containers, uv/project-environment composition and exact wheel compatibility;
- dependency declaration formats, single-transition selection and conditional lock reachability;
- publisher provenance, tag/changelog discovery, semantic source-window bounds, multiple support drops and target Python declaration scope;
- acquisition request/body bounds, repeated reads, latency budgets and failure diagnosis;
- saved evidence, replay/recovery, report completeness and evaluation maturity.

For each, identify the supported proposition and rationale from its actual owner. Separate proposition-essential uncertainty from a current implementation choice that could be improved. A conservative limit may be correct while materially restricting usefulness.

Start from already preserved production-simulation/development cases after reading their local controls. Do not rerun simulations. Select only cases that exercise the boundary under review, and disclose source revision, prior design exposure and capability mismatch. Record cases considered, usable, blocked by each limit and non-comparable, with the reason. A small purposive sample supports case-specific prioritization, not prevalence or generalization claims. No arbitrary numerical target or repository-wide census is required.

Finish when each material proposed expansion has concrete case pressure, an expected useful conclusion it could unlock, simpler alternatives, feasibility/dependencies and a reason to act or defer. Absence of measured pressure remains uncertainty, not proof that the feature has no value.

### Reconcile and prioritize findings

For each material finding, compare:

- consequence: false evidence/identity versus lost availability, missing coverage or presentation friction;
- confidence: source trace, bounded reproduction, integration proof or observed public case;
- reach: affected supported paths and disclosed case evidence;
- feasibility: likely owning boundary, design uncertainty, proof effort and parallel-work overlap;
- dependencies: what must settle before a repair or extension can be evaluated.

Use qualitative priority with reasons; do not manufacture a composite score. High-confidence false positives or mixed provenance generally outrank wider coverage. An untested serious hypothesis earns a diagnostic first, not automatic redesign. Explain exceptions using actual product consequences.

Compare the smallest credible dispositions: keep, clarify, validate, fix within accepted semantics, design an extension, defer, or reject the concern. Identify whether a future accepted change belongs in source/tests, a specification, an ADR or an execution plan. Avoid turning one finding into a request for a new framework or infrastructure platform.

## Progressive evidence record

Maintain one dated working record at meaningful transitions. For each question retain:

```text
question / hypothesis and origin
snapshot / affected files / canonical owner
expected proposition and current rationale
producer → composition → consumer trace
case or command / environment / inputs and assistance
observation / actual output or bounded source evidence
interpretation / uncertainty / counterevidence
correction to earlier understanding, if any
consequence / priority rationale / smallest disposition
remaining check and time-scoped handoff
```

Summarize routine commands; retain exact reproducer inputs and relevant outputs when necessary to recover a finding. Link larger public-safe evidence rather than copying logs. Do not store tokens, ambient environment contents, private artifacts or raw unrelated data. If a reusable diagnostic script or separate durable audit becomes justified, define its responsibility and permitted file scope before creating it; do not silently turn investigation into implementation.

Track the A–E learning cycle per coherent investigation checkpoint: orient the proposition, perform the check, preserve its result, explain the evidence and invite a focused ownership response, then repair gaps or orient the next question. Agreement with an assistant finding does not establish independent understanding or proof.

## Completion and decision gate

The investigation is complete enough for a next-work decision when:

- each seed question has a bounded disposition or explicit missing proof;
- material deliberate limits have rationale and disclosed case pressure or an honest evidence gap;
- source facts, authored tests and executed proof remain separate;
- superseded findings and parallel changes have been reconciled;
- priorities and smallest next actions are reviewable with their affected owners;
- the working record preserves the progression and outstanding uncertainty.

Present that finding set to Ali and stop. Fixes, capability expansion and new proposals are selected from the results; they are not pre-authorized outcomes of this investigation. If a serious finding warrants earlier attention, report it promptly with its evidence and scope without waiting for the full inventory or changing product code.

Provenance: `UP-SKILL:upgradepilot-planning-design`; `UP-SKILL:upgradepilot-repository-audit`.
