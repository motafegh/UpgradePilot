# Reusable caller/signature evidence — design cycle

## Responsibility and status

Continue the [two-gap discussion](2026-10-26_capability-limits-for-explanation-milestone_discussion-cycle.md) into the expressly requested reusable capability design, under the [existing caller/signature plan](../plans/DETERMINISTIC_API_CALL_AND_SIGNATURE_EVIDENCE_PLAN.md). Ali selected reusable design grounded in retained HTTPX and broader evidence, after challenging a possible HTTPX-only implementation. This cycle owns concrete experiment contract design and its review, not a second product specification, completed implementation or Workspace migration decision.

- A0 — DONE: main cf394b1e; preceding findings/receipt, selected plan, shared binding producer and target/adapter manifests reconciled. Only the unrelated October3 untracked audit file exists; preserve it. The prior7-file qualification and12-test result are historical inputs, not repeated or upgraded into new proof.
- A1 — DONE for design continuity under the compression below: two source/interpretation gaps, existing reuse and generality concern carried forward. No independent mastery inferred.
- A2 — DONE for Planning/Design under the compression below: produce an explicit source/argument/signature/correspondence/result/retention/consumer contract with real and controlled proof, supported limits and adoption boundary. This does not pre-authorize executable implementation or resolve full migration.
- B — DONE for design: concrete [experiment contract](evidence/2026-10-28-reusable-caller-signature-design/DESIGN.md), real-case expectations, reusable supported forms, finite limits and implementation/adoption sequence delivered. No executable implementation.
- Verification gate — GREEN for design consistency:123 local references resolve, receipt JSON and pinned historical receipt verify, retained expectations agree,14 helper controls plus existing same-line span check pass; one further trusted control exposes helper disagreement and is preserved as a design correction. No new capability or independent usefulness proof.
- D — CURRENT: teach the resulting source-fact versus correspondence versus conditional-binding distinction, supported coverage, stdlib-helper correction and product-adoption limits; learner challenge/understanding remains open.
- E — PENDING: preserve design-review decisions/debt and the exact next implementation or design responsibility without claiming product acceptance.
- C — CONTINUOUS: retain decisions, alternatives, findings/corrections, verification and proof limits.

## Proportionate gate adaptation

Circumstance/evidence: continuous-context discussion already taught the real chain and reusable-versus-universal distinction; Ali now explicitly requests this design. Normal route: repeat separate A1/A2 stops before planning B. Why worse here: repeats the just-selected design question without new evidence or a consequential choice to resolve. Override: compress planning onboarding/orientation and perform the concrete design for review. Effect: planning records only; future executable Build remains subject to its own orientation, supported contract and authorization. Reconciliation: record the proposed trade-offs and unresolved implementation/product adoption obligations, and retain D/E for Ali's review. This adaptation neither certifies understanding nor removes an implementation gate.

## Living orientation map

- Known: PR/source observation, retained text, TestClient/FastAPI/Starlette/HTTPX chain, missing data versus incorrect interpretation, generic algorithm versus one fixture.
- Explain through the design: complete call/signature facts; parameter kinds and receiver binding; why a curated source pair is conditional; why an observed keyword mismatch can survive other unknown arguments; saved consumer evidence versus ordinary product integration.
- Preserve unknowns: actual installed framework identity, actual dispatch/activation, broader semantic behavior, independent usefulness and migration priority.
- Expected artifact: one dated experiment design linked from the existing plan, not another master plan/ADR; clear finite validation and no expected-answer inputs to automatic discovery.

## Initial source/design findings

Existing ReferenceFact already owns keyword names, syntactic positional count and BindingAssessment; exact trace spans use1-based lines/UTF-8 byte columns. The manifest does not preserve full source text, and line-only references cannot uniquely identify several calls on a line. Reuse binding semantics, but recover exact AST call spans from qualified bytes rather than infer precision from historical counts or duplicate another import analyzer.

The existing plan already demands constructor/receiver decisions, positional-only and **kwargs contrasts, variant names and a second materially different real case. The new contract must settle these concerns without silently reducing the capability to keyword-name subtraction, solving all Python dispatch or declaring experimental output a normal product report.

Applicable owners consulted: plans navigation, Core JUST/OBS/PROV/recovery boundaries, Product Decision Model, Minimum Useful Generality, Naming Clarity, ADR-0011/0012, relevant Operating Guide sections and Security source-data constraints. Python binding reference is checked at the local3.12 language boundary rather than using the unversioned documentation as a runtime compatibility claim.

## Concrete design checkpoint

The selected recommendation is a reusable declared-signature/argument binder with two explicit scopes: keyword reception and complete supported syntactic binding. It covers parameter kinds/default presence/variadic reception and non-expanded positional/keyword arguments. Caller expansions remain explicit; an independently definite unsupported explicit keyword can still be reported. This is broader than an HTTPX app-name rule without pretending to solve arbitrary Python execution.

Correspondence is independent of binding: curated source pair versus evidence-derived source link; no caller-supplied answer; receiver binding as-written, one receiver explicitly assumed, or unresolved. The real super call stays unknown under the existing analyzer; comparisons are conditional on reaching the selected initializer. Missing target installation/dispatch is not erased. Direct ordinary discovery and full product delivery are separate acceptance obligations rather than fabricated capabilities.

Existing full trace spans are sufficient to disambiguate supported references without a new binding manifest version. A direct check of two identical imported call spellings on one line retained distinct call spans. Extension adds missing argument/signature structure beside shared facts, not another import engine. Signature/argument values and full catalog/model input retention are unnecessary: default presence and selected full source files earn the admitted consumer/proof responsibilities.

The proposed consumer is one experiment compare/open entry with a saved result bound to a minimal existing-catalog subset. Reader integrity and offline inspection are distinct from reanalysis/Workspace recovery. Proposed work/candidate/output/time/memory caps are finite and unmeasured; time enforcement belongs around the parsing worker, not only after parsing. Normal product adoption requires explicit native evidence closure/report integration and active tests, with the separate migration subject still open.

Validation so far:14 trusted locally authored stdlib signature-binding controls match expected binding/rejection; existing same-line trace reuse checks pass; the historical receipt matches old/proposed app, retained cert, old/new forwarding and unknown super-binding design expectations. Selected7 files total195,501 UTF-8 bytes. [Validation receipt](evidence/2026-10-28-reusable-caller-signature-design/validation.json) labels these as design checks, not implementation tests. The first ad hoc span check mistakenly unpacked three values from the two-value analyze_python_bindings API; inspected the real producer and corrected the diagnostic. No source defect, source repair, new model result or new real-case acceptance follows.

The existing plan now links the concrete contract and requires reuse of historical qualified inputs after identity checks. No new master plan/ADR/specification is created. A second materially different real case remains required before broader real-case claims; no ready second case or normal PR-driven source route is invented.

## Review correction: stdlib delegation is not automatically adequate

During simpler-baseline review, considered constructing inspect.Signature from AST facts and delegating binding rather than implementing slot rules. A fifteenth trusted control exposed a local Python3.12.3 discrepancy: `def f(value=0, /, **options)` accepts `f(value=2)` with positional default0 and options containing value2, but inspect.signature(f).bind(value=2) rejects it as a positional-only keyword. Earlier14 controls passing were insufficient helper qualification. Preserve this result; it does not imply a target problem, a defect in shared UpgradePilot owners or failure of all stdlib versions.

Corrected design/proof: a small explicit source-shape binder follows documented Python rules, with trusted, side-effect-free locally authored calls as discriminating controls and the inspect helper as a limited comparator. Actual execution here is only the authored control function, never retained target/framework source, source defaults/annotations or a target environment. No stdlib patch or new dependency is justified. This is a meaningful design correction and rejected simpler alternative, not a hidden test repair.

## Design verification and handoff

The contract preserves governing Core/proposal/generality/Workspace boundaries; no accepted specification or ADR semantics change. Artifact checks resolve123 local file references across design, cycles, selected plan and root MEMORY; validation.json decodes, the original inspection receipt hash remains unchanged, and git diff --check passes. Compared with cf394b1e, executable product/experiment/test/tool and specification/ADR files have no diff. The unrelated untracked October3 audit file remains untouched. These checks establish a coherent reviewable design, not a working analyzer.

Publication is progressive: f281e6dc initialized the cycle/handoff;14117955 published the concrete contract and discovered helper discrepancy before final handoff. A concluding record update preserves verification/proof limits. No fresh target/source acquisition, model work, third-party code execution, new real-case acceptance or frozen-result modification occurred. Official Python docs were read for design rules, separately from case acquisition.

The implementation handoff, after concrete contract review/orientation, is one coherent experiment extraction/binding/saved-view increment using retained sources and the existing binding owner. Required controls, cold reopen, identity/timeout/limit behavior and the helper corner must be included. Broader real-case proof, ordinary discovery and normal native/report adoption retain their separate explicit obligations; neither full migration first nor indefinite consumer deferral is selected. D/E stay open for Ali's review; a request to design/develop the capability is not represented as completed Build or independent understanding.

UP-SKILL:upgradepilot-planning-design
UP-SKILL:upgradepilot-learning-by-doing
UP-SKILL:upgradepilot-working-memory
