# AUDIT-013 — Stage 1 governance and current-state integrity

**Date:** 2026-10-20  
**Status:** Audit findings; non-controlling until reviewed/selected through the normal owner and live-state process  
**Audit branch:** `audit/project-wide-system-audit-2026-10-20`  
**Main revision revalidated:** `a1c291c6cf9238493eeb666b184192ed178b90f1`  
**Program:** [Project-wide technical audit and correction program](../plans/PROJECT_WIDE_TECHNICAL_AUDIT_AND_CORRECTION_PROGRAM_PLAN.md)  
**Starting baseline:** [AUDIT-012](2026-10-20_AUDIT-012_project-wide-system-audit-baseline.md)

## 1. Audit question

Revalidate the Stage-1 governance/current-state concerns before fixing them:

1. canonical integration/hosted verification and repository enforcement;
2. Charter time-boundary status;
3. audit lifecycle/live-state leakage;
4. README/environment/provider endpoint consistency;
5. Smart Situational Override authority and duplication footprint;
6. product-value feasibility amendment versus its owning plan/proposal/live handoff;
7. the related Python support-versus-proof scope where it materially affects hosted verification claims.

This audit does not modify product source, tests, accepted specifications/ADRs, historical evidence or the affected governance owners. Recording this audit and its active cycle is the only mutation in this pass.

## 2. Executive disposition

No P0 evidence-integrity failure was found. The core owner model remains materially sound: Charter/specification/ADR/plan/source/audit/working-memory responsibilities are explicitly separated, and the recent product-value direction remains a useful correction rather than something this audit recommends discarding.

The Stage-1 pass confirms **six material governance/documentation/proof findings**, one secondary proof-scope finding, and several cleared/qualified concerns:

| ID | Priority | Type | Disposition |
| --- | --- | --- | --- |
| G1 | P1 before trustworthy integration | proof gap + governance/integration control gap | fix before this audit branch can be treated as safely integrated into `main` |
| G2 | P2 | governance/documentation drift | correct Charter time-boundary meaning deliberately |
| G3 | P2 | governance/state drift | reconcile audit lifecycle entries and stale current-facing metadata |
| G4 | P2 | documentation drift | correct README LM Studio endpoint against canonical environment/source |
| G5 | P2 + P3 | governance ambiguity + context/duplication cost | narrow override semantics; then simplify repeated boilerplate |
| G6 | P2 | live-state/plan reconciliation gap | incorporate or reject the pending product-value plan amendments before that investigation is executed |
| G7 | P2, Stage-4 handoff | proof/claim-scope gap | decide verified Python support scope versus `>=3.12`/`3.12+` claims |

No Stage-1 finding authorizes its own remediation.

---

## 3. G1 — canonical integration has useful hosted verification but no enforced current proof

### Observation

`.github/workflows/product-verification.yml` is a legitimate hosted product proof surface. It:

- installs the package in a fresh environment;
- uses Ubuntu 24.04 and Python 3.12;
- checks dependency consistency and installed CLI entry points;
- runs focused investigation tests and the full deterministic product suite;
- deliberately excludes local-model/live-proof/experiment work.

However:

- the workflow trigger is only `workflow_dispatch`;
- `.github/workflows/` contains no other workflow;
- GitHub reports `main` as unprotected with no required status checks;
- the repository has no rulesets;
- current `main` has no commit status attached;
- the latest Product verification success is run #17 on 2026-10-02 at `1c371875ffb459ce2e2c9c913a5a87a10a434928`;
- current `main` `a1c291c6` is **322 commits ahead** of that hosted-success revision;
- that delta includes substantial product changes: Workspace implementation, investigation/report/source changes, tests and architecture work.

### Interpretation

This is **not evidence that current product code fails**. Numerous local/focused proofs are retained elsewhere, and manual dispatch was an explicit earlier choice.

It is nevertheless no longer a sufficient canonical integration posture for a repository whose central architecture has moved materially. A contributor/process can publish to `main` without any enforced deterministic fresh-install/product-suite proof, and the only observed hosted proof predates the current product by hundreds of commits.

The route places final CI hardening in C1, so automatic checks were not necessarily required at the moment the manual workflow was first introduced. That historical rationale does not justify leaving canonical integration indefinitely unguarded while the product changes substantially.

### Finding

**P1 before trustworthy integration — proof gap + governance/integration control gap.**

The current state is acceptable as a temporary development posture only if it is explicitly treated as proof debt. It should not be used to imply current hosted reproducibility or a protected canonical branch.

### Smallest credible correction

Later remediation should separate two steps:

1. prove the current selected revision through the existing deterministic hosted workflow;
2. decide and implement a low-noise canonical gate: normally push/PR deterministic product verification plus branch/ruleset protection requiring that check.

Keep model inference, live acquisition, GPU/provider qualification and experiment suites out of the required canonical gate unless a distinct future responsibility justifies them.

Repository-setting changes may require an external GitHub/UI/admin action and must be verified as settings, not inferred from workflow YAML.

### Required proof

- current-head hosted installed-package/CLI/product-test success;
- automatic trigger behavior if introduced;
- actual required-check/ruleset/branch protection state, not just documented intent;
- negative confirmation that live model/network/experiment execution is not accidentally in the required deterministic gate.

---

## 4. G2 — the controlling Charter has passed its stated execution period

### Observation

`PROJECT_CHARTER.md` is explicitly marked `Controlling stable project charter` and states:

```text
Execution period: 2026-07-20 to 2026-10-17
```

It also says UpgradePilot is the selected flagship for the **current 90-day execution period**. Work continues on 2026-10-20. The Charter has no explicit continuation/extension/re-charter statement.

The route plan, meanwhile, explicitly says stages are **evidence gates, not calendar promises**.

### Interpretation

The product mission and frozen boundary do not become invalid merely because October 17 passed. Nothing inspected suggests an intentional mission change.

The problem is governance meaning: a controlling owner still frames itself around a period that ended three days ago, while a second controlling route says advancement is evidence-based rather than calendar-based. A future reader cannot tell whether:

- the 90-day date was only the original planning horizon;
- the Charter expired and needs renewal;
- or the same Charter was deliberately extended.

### Finding

**P2 — governance/documentation drift.**

This is stale control metadata/decision framing, not a product-boundary failure.

### Smallest credible correction

Make one deliberate Charter-level decision rather than silently changing dates:

- either explicitly extend/re-charter the execution period while preserving the accepted mission/boundary;
- or reword the date as the **initial 90-day planning window** and state how the ongoing evidence-gated project continues after it.

Do not use this correction to reopen mission, user, supported decision or frozen product boundary unless separate evidence justifies that change.

---

## 5. G3 — the audit lifecycle index leaks superseded current-state metadata

### Observation

`audits/LIFECYCLE.md` defines `active` as a validated finding selected as input to the **current engineering responsibility**. `audits/active/README.md` currently lists AUDIT-009, AUDIT-010 and AUDIT-011.

The entries contain old current-facing coordination:

- AUDIT-009 points to the October 2 action-relative reachability continuation and Product Verification #17 as the anchor;
- AUDIT-010 points to the Workspace/Investigator-interface design responsibility before the later accepted Workspace ADR/implementation progress;
- AUDIT-011 points to the successor run-control/capability plan even though that line has since produced later completed/inconclusive results and the live handoff moved to product-value feasibility.

`MEMORY.md` itself warns that retained successor paragraphs are historical and that its current-position section owns continuation. The lifecycle index does not provide the same qualification and, by definition, is itself the current lifecycle-state owner for audits.

### Interpretation

The canonical audit records are not wrong merely because later work occurred. The defect is the **active lifecycle metadata**, not historical audit evidence.

It is also too early to assert that all three audits must simply be deleted from `active`:

- AUDIT-010 is a strong candidate for `absorbed` because later accepted architecture/work incorporated its compatibility conclusions;
- AUDIT-009 is also likely absorbed/historical, but its exact unresolved findings should be checked before movement;
- AUDIT-011 may still contain unresolved experiment-method findings useful to Stage 5, but its current execution-owner text is stale even if some finding remains active.

### Finding

**P2 — governance/state drift.**

### Smallest credible correction

Perform one bounded lifecycle reconciliation:

```text
AUDIT-009 / 010 / 011
→ inspect remaining unresolved finding responsibility
→ ACTIVE / SCHEDULED / DEFERRED / ABSORBED
→ update only lifecycle indexes and necessary live references
```

Do not rewrite the dated canonical audits to make them look current.

---

## 6. G4 — README points operators to the former LM Studio endpoint

### Observation

The README's conditional semantic-provider section says:

```text
LM Studio base: http://127.0.0.1:12345
```

Current canonical environment says:

```text
listener: 127.0.0.1
port: 18080
OpenAI-compatible: http://127.0.0.1:18080/v1
```

and explicitly describes `12345` as the **former** endpoint involved in an ambient-proxy incident.

Active product source sets:

```python
LM_STUDIO_BASE_URL = "http://127.0.0.1:18080"
```

### Interpretation

This is a confirmed operator-facing contradiction. A reader following README can configure the wrong local service endpoint while the product calls 18080.

### Finding

**P2 — documentation drift.**

The correction itself is small, but the consequence is material enough to exceed cosmetic P3 because it can make a model-backed product run fail or be misdiagnosed at the transport/provider boundary.

### Smallest credible correction

Update README to the current 18080 endpoint and preserve `ENVIRONMENT.md` as the topology/re-check owner. Do not duplicate volatile runtime details beyond what the quickstart genuinely needs.

No product test suite is required for this documentation-only correction; source/environment consistency inspection is the relevant proof.

---

## 7. G5 — Smart Situational Override is useful, but its root scope is too semantically broad

### Positive evidence / cleared concern

The override mechanism is **not** an uncontrolled escape hatch in the inspected governance:

- root `AGENTS.md` says it does not create authorization, change evidence truth or silently redefine accepted owners;
- Charter explicitly protects mission, supported decision, frozen boundary, evidence doctrine and claim limits;
- operation Skills consistently say they are procedural/non-controlling and cannot create Build/external authorization;
- material overrides are expected to record circumstance, displaced rule, rationale, proof/risk/learning/ownership effect and reconciliation.

No inspected evidence establishes that the rule has actually been used to falsify proof or silently override accepted product semantics.

### Remaining ambiguity

Root `AGENTS.md` also says, unless explicitly stated otherwise, project-local:

```text
MUST / REQUIRED / DO NOT / NEVER / STOP / GATE / fixed ordering / ...
```

are interpreted under the Smart Situational Override Rule.

The accepted Core specification independently defines:

```text
MUST — required for acceptance when the requirement applies
MUST NOT — prohibited within the admitted responsibility
```

and then uses those terms for product/evidence invariants.

The root statement can therefore be read more broadly than intended: it does not syntactically distinguish **procedural route/gate language** from **normative accepted product semantics**. The later prohibition on silently redefining accepted specifications/ADRs substantially mitigates the risk, but leaves avoidable ambiguity about whether an explicit temporary override may violate a normative accepted requirement before owner reconciliation.

### Duplication/context cost

The full Smart Override explanation is repeated in root governance, the Operating Guide, route plan, Charter boundary and multiple operation/support Skills. Most copies correctly point back to root, so this is not yet semantic drift, but it increases context size and future divergence risk.

### Finding

**G5a — P2 governance ambiguity.** Narrow the canonical root wording so the override clearly applies to project-local **procedure, routing, cadence, gates, defaults and execution coordination**, while accepted normative Charter/specification/ADR semantics require an explicit owner change rather than an override.

**G5b — P3 context/simplification opportunity.** After the root meaning is unambiguous, reduce child-artifact repetition to a concise reference plus only genuinely local boundary-specific consequences. Preserve high-salience reinforcement where it has independent value.

This is not a recommendation to remove adaptive engineering judgment.

### Proof after correction

A governance review should be able to answer unambiguously:

- can a procedure/gate be adapted? yes, with recorded reason and without creating authorization;
- can accepted product semantics be changed by invoking the override alone? no;
- can security/evidence truth/external constraints be bypassed? no;
- can a material owner change occur without updating that owner? no.

Avoid brittle lint that tries to mechanize semantic engineering judgment.

---

## 8. G6 — product-value patch notes are correctly non-controlling, but the live handoff is incomplete

### Observation

The October 20 review patch notes explicitly mark themselves **non-controlling until incorporated** and say the prepared plan should be revised before investigation execution is authorized.

The owning feasibility plan still contains the exact surfaces the notes challenge:

- fixed deep readiness work around S001–S006;
- no explicit bounded multi-role semantic interpretation/validation alternative in the next-increment table;
- the structural rule that an asserted/inferred recommendation with no supporting recommendation evidence is inadequate.

The plan already contains broader authorization safeguards: plan preparation does not execute the investigation, and its disposition table says execution remains separately selected. Root governance also prevents a findings packet from self-authorizing Build. Therefore patch D is useful local hardening, not evidence of an existing P0 authorization bypass.

The accepted proposal remains directionally compatible with the amendments: it already treats source relations as conditional, model/task decomposition as empirical, and additional semantic roles as conditional on a named residual uncertainty. It does not need churn merely to duplicate the plan wording.

`MEMORY.md`, however, still summarizes the prepared continuation as a **six-case readiness inventory** and does not mention that a material review amendment request now blocks treating that exact plan text as ready for execution.

### Interpretation

The owner separation is working: review evidence has not silently rewritten the plan. The remaining issue is **handoff completeness**. A future agent that reads only the sole live-state owner can miss the pending amendment and resume from stale plan scope after a later generic “go ahead.”

### Finding

**P2 — live-state/plan reconciliation gap.**

### Smallest credible correction

Before the product-value feasibility investigation is ever executed:

1. review and incorporate/reject the four amendments in the owning plan;
2. update the planning-cycle record with the review delta;
3. update `MEMORY.md` to the actually reviewed prepared-plan scope;
4. review the resulting diff;
5. require explicit execution authorization afterward.

No product source/test/model/benchmark work belongs to that documentation reconciliation.

---

## 9. G7 — Python `>=3.12`/`3.12+` scope is broader than observed hosted proof

### Observation

`pyproject.toml` declares:

```text
requires-python = ">=3.12"
```

and README tells users to use Python **3.12 or newer**.

The hosted Product verification workflow currently proves only Python 3.12. The reusable environment baseline records Python 3.12.3.

### Interpretation

An open-ended lower-bound requirement is not automatically a false claim that every future Python release has been independently certified. Nevertheless the README phrasing functions as a user-facing support instruction, and the repository currently has no hosted evidence across a newer-version matrix.

### Finding

**P2 proof/claim-scope gap, handed to Stage 4 for final design.**

Do not add an arbitrary upper bound merely to make the proof easier. Decide what “supported” should mean for UpgradePilot:

- test a deliberate small supported Python matrix; or
- qualify documentation so 3.12 is the verified development/hosted baseline while newer compatible interpreters are not independently claimed; or
- choose another explicit compatibility policy backed by dependency/runtime evidence.

This is not evidence that Python 3.13+ currently fails.

---

## 10. Positive governance mechanisms to preserve

The audit should not flatten mechanisms that are working:

1. **Owner separation is strong.** Charter, route, specs, ADRs, plans, source/tests, audits and working-memory explicitly claim different responsibilities.
2. **Audit records are correctly non-controlling.** The lifecycle mechanism is good in principle; its current index data is what drifted.
3. **The manual hosted workflow is well scoped.** It exercises installed product behavior without mixing model/provider/experiment work into the deterministic proof surface.
4. **The product-value review amendment preserved authority boundaries.** It requested owner revisions instead of editing frozen experiment evidence or treating review notes as a new plan.
5. **Smart Override has important safeguards worth retaining.** The issue is scope wording and duplication, not the existence of adaptive judgment.
6. **The October 19–20 product-value-first direction remains technically preferable to automatic continued tuning on exposed Investigator fixtures.** Stage 2 should audit it further rather than reverse it reflexively.

---

## 11. Recommended correction order after review

This audit deliberately stops before remediation. If Ali accepts these classifications, the lowest-risk order is:

```text
1. branch/live-state bookkeeping and pending-plan handoff clarity
2. README endpoint correction
3. audit lifecycle reconciliation
4. Charter continuation/time-boundary decision
5. Smart Override semantic narrowing + duplication cleanup
6. hosted canonical integration gate / branch protection
7. Python support matrix/claim design during Stage 4
```

The order is not the same as priority. G1 is the highest integration risk, but governance wording/lifecycle/docs can be corrected without first changing repository administration; the required hosted/protection gate must be established before final branch integration.

## 12. Stop line

Do not begin these corrections under this audit result alone. Review the findings first. For consequential governance changes (Charter, Smart Override, canonical CI/protection), establish the exact correction design and proof boundary before mutation.

`UP-SKILL:upgradepilot-repository-audit`
