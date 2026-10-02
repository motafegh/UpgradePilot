# UpgradePilot Post-Runtime-State Product Direction, Audit, and AI Activation Proposal

**Date:** 2026-10-02  
**Proposal status:** Candidate — non-controlling, open to revision  
**Authority:** This document is a proposal only. It does not select live work, authorize Build/Implement, change accepted semantics, create an ADR, or override `MEMORY.md`, specifications, accepted ADRs, or admitted plans.  
**Planning provenance:** `UP-SKILL:upgradepilot-planning-design`

## Post-proposal evidence update — AUDIT-009 completed

The proposed current-state delta reconciliation has now been performed and preserved as [AUDIT-009 — Post-Runtime-State Delta Readiness Audit](../audits/2026-10-02_AUDIT-009_post-runtime-state-delta-readiness.md).

That audit materially supports this proposal's transition framing:

- F3/F4/F9/original-F11 are closed/absorbed;
- bounded F6/Runtime Dependency-State Cycle 1 is established rather than wholly missing;
- F5 exact target wheel compatibility remains conditional;
- F7 candidate/context discovery remains a major action-reachability question;
- the new runtime-state result reaches the application boundary but has no action/presentation consumer yet;
- AI candidate discovery is now a legitimate method candidate only if the refreshed action comparison shows discovery is the earliest blocker.

This update does not admit the proposal or select an implementation. `MEMORY.md` continues to select the parent action-relative reachability comparison as the next responsibility.

---

## 1. Purpose

UpgradePilot has just closed the first bounded Runtime Dependency-State Proof program through Increment 5. The project is therefore at a useful transition point: the recent work established a stronger evidence spine, but the next product responsibility should not be chosen merely by continuing the same technical family.

This proposal suggests a **possible next direction** for discussion and later selection. It is intentionally written as a candidate route rather than a mandatory roadmap.

The proposal addresses three questions:

1. what product responsibility may be most useful to evaluate next;
2. whether a new full-system audit is useful now or should wait for a stronger milestone;
3. when AI/LLM/agent capabilities should move from preserved research/pilots into active product experiments.

The central thesis is:

> UpgradePilot may now benefit from shifting from evidence-feature accumulation toward **action-relative product reasoning**: determine what maintainer decision the current evidence system can actually support, identify the closest missing premise if none is reachable, and activate AI only when that selected responsibility genuinely benefits from adaptive semantic reasoning.

This thesis is deliberately falsifiable. If current-state review shows a more fundamental correctness, provenance, or architecture problem, the route should change.

---

## 2. Why this proposal exists now

The recent Runtime Dependency-State work closed a coherent technical sequence:

```text
reusable exact execution evidence
→ package-manager operation declaration
→ bounded process/environment/config evidence
→ effective package-manager semantic facts
→ command-derived requirement-state composition
→ normal application integration
```

Product Verification #17 established the integrated Increment-5 behavior on exact head `1c371875ffb459ce2e2c9c913a5a87a10a434928` with:

- fresh installed-package / `pip check`: PASS;
- installed CLI entry points: PASS;
- focused investigation composition: 16/16 PASS;
- deterministic product regression: 714/714 PASS.

The closed cycle also deliberately preserved limitations such as uv runtime package-state proof, Docker-inner-command provenance, some matrix/job-correlation shapes, and bounded venv/PATH propagation rather than expanding them merely for completeness.

This creates a natural question:

```text
we can now prove more technical facts
        ↓
which facts actually matter to a maintainer action?
```

The parent evidence-to-action plan already treats that question as the next selection responsibility.

### Primary references

- [`../MEMORY.md`](../MEMORY.md) — current live handoff selects the parent action-relative reachability comparison as the next responsibility, while keeping Runtime-State Cycle 2 unselected.
- [`../plans/RUNTIME_DEPENDENCY_STATE_PROOF_COMPLETION_PLAN.md`](../plans/RUNTIME_DEPENDENCY_STATE_PROOF_COMPLETION_PLAN.md) — states that after bounded Cycle-1 closure, control should return to the parent evidence-to-action route rather than automatically adding stronger runtime-state acquisition.
- [`../plans/END_TO_END_PRODUCT_FLOW_LEARNING_AND_EVIDENCE_TO_ACTION_EXECUTION_PLAN.md`](../plans/END_TO_END_PRODUCT_FLOW_LEARNING_AND_EVIDENCE_TO_ACTION_EXECUTION_PLAN.md) — requires action-relative comparison of missing premises instead of implementing F4/F5/F6/F7 as a backlog.
- [`../working-memory/2026-09-30_2119_increment-5_runtime-dependency-state-application-integration_lbd-cycle.md`](../working-memory/2026-09-30_2119_increment-5_runtime-dependency-state-application-integration_lbd-cycle.md) — records the verified Increment-5 result, real-case limitations, D/E learning, and explicit deferrals.

---

## 3. Proposed decision frame

A useful next decision may be:

> **Given the current producer graph, does one accepted non-abstention maintainer action now have normally reachable positive prerequisites? If not, what single missing proposition is closest to changing that?**

This is narrower than a new full roadmap and broader than another local evidence feature.

A candidate reasoning chain is:

```text
accepted maintainer action
→ required positive permission
→ current normal producers
→ current composition
→ exact missing/weak premise
→ closest defeater
→ product value if repaired
→ implementation/proof cost
```

The proposal recommends evaluating the accepted action families individually rather than treating “better recommendations” as one generic target:

- merge after normal review;
- run targeted checks;
- investigate;
- block;
- defer.

The project should not assume in advance that any one of these is next.

### Why this direction is plausible

AUDIT-008 already found that the product is still primarily an evidence-report system rather than a mature maintainer-action product, and that this is not itself a defect. The parent plan intentionally deferred non-abstention action admission until positive permission could be earned through normal producers.

The recent evidence work now makes it reasonable to revisit that question.

### References

- [`../audits/2026-09-19_AUDIT-008_current-system-evidence-to-action-readiness.md`](../audits/2026-09-19_AUDIT-008_current-system-evidence-to-action-readiness.md) — current-system evidence-to-action audit and F1–F11 finding basis.
- [`../docs/specifications/UPGRADEPILOT_MAINTAINER_ACTION_SYNTHESIS_SPECIFICATION.md`](../docs/specifications/UPGRADEPILOT_MAINTAINER_ACTION_SYNTHESIS_SPECIFICATION.md) — accepted action-permission semantics.
- [`../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md`](../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md) — accepted technical proposition/applicability/investigation model.
- [`../working-memory/2026-09-20_action-relative-producer-reachability-comparison.md`](../working-memory/2026-09-20_action-relative-producer-reachability-comparison.md) — earlier action-relative comparison that selected F4 before later F5/F6 work changed the producer graph.

---

## 4. Candidate near-term route

The following is a **recommended candidate route**, not a required sequence.

### Candidate step A — current-state delta reconciliation — completed as AUDIT-009 evidence

The compact current-state reconciliation against the post-#17 source/evidence state has now been completed as AUDIT-009. The questions below remain the rationale for that completed step and a reusable checklist for future re-entry.

This should answer:

```text
what is implemented?
what is hosted/deterministically proven?
which AUDIT-008 findings are closed or materially changed?
which limitations are deliberate supported-domain boundaries?
which limitations are current correctness/ownership defects?
which limitations are future breadth only?
which limitations currently block a maintainer action?
```

The purpose is not to reread the entire repository or regenerate AUDIT-008. It is to prevent the next action comparison from using stale September assumptions.

A future LbD A0 should consume AUDIT-009 rather than repeat this reconciliation unless new product/source evidence has materially changed the baseline.

### Candidate step B — refreshed action-relative reachability comparison

Use current source, accepted action semantics, the closed F4/F5 work, the closed F6/Runtime-State Cycle 1, and representative product-simulation evidence.

For each action, identify the **earliest missing positive premise**, if any.

The comparison should select at most one next responsibility.

Possible outcomes include:

#### Outcome 1 — one action is now normally reachable enough

Then the next responsibility may be a bounded first non-abstention action admission.

Example shape:

```text
accepted positive permission
+ normal current producers
+ close defeaters
→ one action evaluator branch
→ unchanged honest fallback
```

This outcome should not be assumed before the comparison.

#### Outcome 2 — one exact deterministic producer/composition gap remains closest

Then implement that exact gap rather than broadening multiple evidence families.

This may or may not be an existing audit label such as F7.

#### Outcome 3 — candidate discovery becomes the nearest real bottleneck

If existing action-relative reasoning shows that the system cannot reliably enumerate the material impact candidates needed for the selected action, then Stage-8 broad candidate discovery may become the correct next product responsibility.

This is the primary point at which a new AI/LLM experiment may become justified.

#### Outcome 4 — a deeper correctness/provenance problem appears

If current reconciliation finds a defect more fundamental than action reachability, repair that first and revisit this proposal afterward.

---

## 5. Audit strategy proposal

### 5.1 Proposed default: do not immediately repeat a full AUDIT-008-scale audit

A second broad full-system audit immediately after the recent evidence program may have diminishing value because the project already has:

- AUDIT-008;
- the parent evidence-path re-audit;
- the action-relative comparison;
- F4/F5 investigations and closures;
- the F6/runtime dependency-state investigation;
- five Increment cycles with hosted verification;
- product-simulation evidence;
- merged AI/agent architecture research.

A new full audit today could spend substantial effort restating known supported-domain boundaries while delaying the action-relative product decision.

### 5.2 Proposed near-term substitute: compact delta audit / capability reconciliation

The next A0/A1 could produce a bounded current-state classification, potentially recording:

| Area | Candidate classification |
| --- | --- |
| exact identity/provenance | established strength / retain |
| dependency transition/source | supported bounded families |
| CI consumption/runtime correlation | verified bounded support + explicit unsupported shapes |
| runtime dependency state | bounded pip Route-A proven; broader families deferred |
| target/artifact applicability | current F4/F5 state |
| candidate discovery | evaluate whether breadth is now action-critical |
| maintainer action | abstention-only implementation until positive permission is earned |
| presentation | evidence reporting; action presentation still downstream |
| AI/LLM | adopted bounded support-drop extractor + pilots/research; new activation trigger-driven |

This artifact need not become a new formal audit unless the work discovers material findings that deserve audit lifecycle ownership.

### 5.3 Suggested trigger for the next full system audit

A stronger milestone for another comprehensive audit may be after one of these events:

1. first non-abstention maintainer action is implemented and proven;
2. first integrated maintainer-action presentation path is active;
3. first credible bounded public-PR synthesis proof is completed;
4. a major AI candidate-discovery responsibility is adopted;
5. a substantial architecture/trust change alters multiple evidence owners;
6. current delta reconciliation exposes enough cross-owner contradictions that a full audit becomes justified earlier.

This timing would allow the next full audit to evaluate a qualitatively more mature system rather than mostly compare incremental producer improvements.

### Alternative: perform a full audit now

This remains a valid option if the project owner values a complete fresh inventory more than near-term progress.

Trade-off:

- **gain:** maximal confidence in whole-system state;
- **cost:** likely significant repetition and delayed action-selection work.

The proposal does not forbid this route.

---

## 6. AI/LLM activation proposal

### 6.1 Current position

The project should not be described as “waiting to start AI.”

It already has differentiated AI/agent experience and architecture:

- adopted bounded local-LLM semantic extraction for support-drop evidence;
- an EvidenceGapPlanner pilot;
- hands-on LangGraph orchestration experiments;
- a proposed LLM-assisted final synthesis design;
- a large merged research program mapping AI/agent roles to product responsibilities.

The important question is therefore:

> **Which AI responsibility, if any, has now earned product activation?**

### References

- [`2026-09-29_UPGRADEPILOT_EVIDENCE_AI_ARCHITECTURE_PROPOSAL.md`](2026-09-29_UPGRADEPILOT_EVIDENCE_AI_ARCHITECTURE_PROPOSAL.md) — evidence-first AI architecture proposal.
- [`../working-memory/2026-09-29_step4_existing-ai-agent-work-reconciliation.md`](../working-memory/2026-09-29_step4_existing-ai-agent-work-reconciliation.md) — reconciles adopted AI, pilots, deferred synthesis, broad-discovery gap, and non-gaps.
- [`../working-memory/2026-09-29_step5_architecture-decisions-experiment-queue-and-integration-strategy.md`](../working-memory/2026-09-29_step5_architecture-decisions-experiment-queue-and-integration-strategy.md) — experiment triggers, explicit deferrals, and activation order.
- [`2026-09-10_LLM_ASSISTED_MAINTAINER_DECISION_AND_REPORT_SYNTHESIS_PROPOSAL.md`](2026-09-10_LLM_ASSISTED_MAINTAINER_DECISION_AND_REPORT_SYNTHESIS_PROPOSAL.md) — retained future final-synthesis experiment design.

---

## 7. Candidate AI responsibility: broad technical impact-candidate discovery

The merged research identifies the strongest future AI opportunity as **Stage-8 broad impact-candidate discovery**.

Candidate question:

> Given an exact dependency transition, upstream changes, target repository structure, package/build/CI context, what materially plausible impact mechanisms should UpgradePilot evaluate?

Candidate architecture:

```text
trusted deterministic update/package/source signals
+ upstream changelog/API/source-diff evidence
+ bounded repository structural context
+ package/build/CI context
        ↓
AI-assisted candidate discovery
        ↓
typed candidate set
        ↓
deterministic grounding / admission
        ↓
later applicability and investigation
```

This is materially different from:

- support-drop extraction — one known semantic family;
- EvidenceGapPlanner — choosing evidence actions for an already-known unresolved proposition;
- final synthesis — deciding/explaining after important candidates have already been evaluated.

### Proposed activation test

Do not activate broad discovery solely because the research is complete.

Activate it if the refreshed parent reachability comparison shows that:

1. an action-relevant decision is blocked by incomplete or brittle candidate discovery;
2. deterministic candidate families are no longer sufficient for the selected product responsibility;
3. a bounded protected evaluation corpus can be assembled;
4. the first experiment can be compared against a transparent deterministic/fixed baseline.

If those conditions do not hold, continue deterministic product work and leave the AI responsibility queued.

---

## 8. Suggested AI experiments if Stage 8 activates

The research already proposes a useful experiment family. A reasonable candidate sequence is:

### Experiment A — upstream API/source-diff comparator

Reference: Step-5 experiment E2.

Compare:

```text
changelog/release evidence
vs
API/source diff
vs
combined evidence
```

Possible Python tooling includes Griffe or bounded exact-source comparison.

Purpose:

- determine what additional candidate mechanisms become discoverable;
- measure precision/noise before adding model reasoning.

### Experiment B — model-context strategy

Reference: Step-5 experiment E5.

Compare:

```text
typed bounded projection only
vs
typed projection + structural retrieval
vs
progressive exact raw-source retrieval
```

Measure:

- candidate recall;
- unsupported-candidate rate;
- grounding quality;
- context noise;
- token/runtime cost.

### Experiment C — small multi-view repository intelligence, only if repeated structural pressure exists

Reference: Step-5 experiment E4.

Possible views:

- dependency → imports/callers;
- dependency → tests;
- dependency → CI consumers;
- package/build ownership;
- selected source relationships.

Do not start with a universal graph or graph database.

### Candidate AI authority rule

Even if the model proposes candidates:

```text
LLM candidate
!= trusted product fact
```

The model may increase search/discovery breadth. Candidate grounding, applicability, action permission, and final authority should remain separately validated according to their owning contracts.

---

## 9. AI capabilities that probably remain premature

This proposal suggests retaining the existing deferrals unless new evidence activates them.

### Final LLM maintainer decision/report synthesis

Keep deferred until the activation prerequisites from the merged research are met, including:

- materially different candidate families;
- represented cross-candidate state;
- at least one accepted non-abstention action;
- transparent deterministic baseline;
- protected synthesis corpus;
- observed deterministic limitation.

At that point, compare the LLM design rather than assuming it is superior.

### EvidenceGapPlanner product adoption

Keep as a pilot until at least two independently justified real investigation actions exist and a fixed deterministic baseline can be compared against the planner.

### LangGraph product adoption

Keep experimental unless real orchestration pressure appears:

- checkpoint/resume;
- human pause/resume;
- complex branching;
- durable state;
- recovery;
- multiple independently justified actors.

### Generalist software agent / OpenHands-style default

Keep as a later long-tail comparator, not the default architecture.

### Multi-agent/debate architecture

Do not activate without an explicit measured responsibility where it beats a simpler baseline.

### LangChain/general provider abstraction

No current evidence shows that direct local-model HTTP or ordinary Python is blocking the product.

---

## 10. Interaction between action work and AI work

The proposal recommends avoiding a false binary:

```text
deterministic product work
OR
AI work
```

A more useful model is:

```text
product responsibility selected
        ↓
choose the simplest method that satisfies it
        ↓
if open-world semantic/adaptive reasoning is material
        ↓
run bounded AI comparator/experiment
        ↓
adopt only if evidence beats the baseline
```

This means AI can become active soon **if the next selected product responsibility is candidate discovery or adaptive investigation**.

If the next blocker is instead a mechanical identity/composition fact, deterministic engineering should remain the default.

---

## 11. Candidate decision tree after the next comparison

```text
Refresh current producer/action reachability
        │
        ├─ One action has normal positive prerequisites
        │      ↓
        │   consider first non-abstention action admission
        │
        ├─ One exact mechanical producer/composition premise is missing
        │      ↓
        │   build that bounded premise
        │
        ├─ Candidate-discovery breadth is the closest blocker
        │      ↓
        │   activate Stage-8 AI experiments
        │   (E2 + E5; E4 only if structural reuse justifies it)
        │
        ├─ Investigation choice becomes genuinely adaptive
        │      ↓
        │   once two real actions exist, evaluate E6 planner vs fixed baseline
        │
        └─ Cross-owner correctness/trust defect appears
               ↓
            repair/audit before broader product expansion
```

This tree is guidance only. Evidence may justify a different branch or sequence.

---

## 12. Proposed treatment of known limitations

The recently identified limitations should be retained as **capability pressure**, not automatically converted into work:

- unnamed-job runtime correlation;
- matrix/strategy correlation;
- uv runtime package-state semantics;
- Docker action → Dockerfile install provenance;
- venv/PATH propagation;
- explicit target-owned package-state observation;
- exact target wheel tags where mechanism-specific decisions require them;
- bounded positive candidate-discovery horizon;
- non-abstention synthesis;
- action presentation.

A limitation should become active work when it is:

```text
real
+ action/decision relevant
+ closest blocker
+ proportionate to repair
```

This preserves the project's “smartest useful solution” preference without turning supported-domain boundaries into permanent excuses.

---

## 13. Alternative project routes preserved by this proposal

### Alternative 1 — full audit first

Perform a fresh comprehensive repository/system audit before action comparison.

Use if confidence in current cross-owner state is insufficient.

### Alternative 2 — action comparison first, delta audit embedded

This proposal's default suggestion.

Use A0/A1 to refresh current system state, then compare action reachability without creating another large audit unless material findings justify it.

### Alternative 3 — AI candidate-discovery lab now, parallel to main

A bounded non-controlling lab could be useful for learning even before product activation.

It should be clearly separated from main product adoption and should not redirect the live route.

This route is valid if the goal is explicitly learning/experimental exposure rather than product necessity.

### Alternative 4 — select one known evidence breadth expansion first

For example uv, Docker, or matrix support.

Use only if current evidence shows that exact capability is already blocking a selected action or representative high-value case.

### Alternative 5 — first non-abstention action immediately

Use only if a fresh reachability check shows its positive permission is already satisfied through normal producers. Do not manufacture fixtures to make this true.

---

## 14. Proposed proof and evaluation philosophy

Whichever route is selected later, continue the evidence discipline established by the project:

```text
source/design reasoning
→ focused contract tests
→ normal application integration
→ broader deterministic regression
→ hosted/live proof only when needed
→ representative public case when the claim requires it
```

For AI experiments, add:

```text
protected corpus
+ transparent baseline
+ repeated-run stability
+ source-grounding evaluation
+ unsupported-claim rate
+ useful-recall / decision-value measure
```

AI success should not be defined as “more impressive output.”

Where the responsibility is maintainer-facing, evaluation should eventually include decision quality, trust calibration, decision time, and ability to detect incorrect system claims.

---

## 15. Proposed next-cycle shape

If this proposal is considered useful, a possible next Learning-by-Doing cycle is:

### A0 — current-state reconciliation

- verify current main/live owners;
- reconcile AUDIT-008 findings against completed F4/F5/F6 work;
- classify current limitations by correctness / deliberate boundary / future breadth / action blocker;
- preserve current product proof state.

### A1 — action-permission reachability orientation

- reconstruct each accepted action's positive prerequisites;
- map current normal producers to those prerequisites;
- use representative product-simulation cases only where they discriminate the comparison;
- identify the closest missing premise per action.

### STOP

Review the comparison together before choosing the next responsibility.

### A2 — only after selection

Orient exactly one selected responsibility:

- action admission;
- deterministic evidence producer/composition;
- Stage-8 AI candidate discovery;
- other demonstrated blocker.

Then STOP again before Build according to normal governance.

This is a candidate execution shape, not a new controlling plan.

---

## 16. Reassessment triggers

This proposal should be revised or bypassed if any of the following occurs:

1. current-state reconciliation finds a correctness/provenance defect more fundamental than action reachability;
2. a representative case proves one deferred runtime/workflow limitation is already the closest action blocker;
3. product-simulation evidence shows candidate-discovery incompleteness is materially affecting decisions;
4. the first non-abstention action becomes normally reachable sooner than expected;
5. new accepted specifications or ADRs change the decision model;
6. AI evaluation evidence contradicts the merged research assumptions;
7. project priorities intentionally shift toward a learning lab rather than the main product route.

Changing the proposal in response to evidence is expected behavior, not proposal failure.

---

## 17. Reference map and rationale

| Reference | Why it matters to this proposal |
| --- | --- |
| [`../MEMORY.md`](../MEMORY.md) | Sole live-state owner; currently hands off from closed runtime-state work to parent action-relative comparison. |
| [`../plans/END_TO_END_PRODUCT_FLOW_LEARNING_AND_EVIDENCE_TO_ACTION_EXECUTION_PLAN.md`](../plans/END_TO_END_PRODUCT_FLOW_LEARNING_AND_EVIDENCE_TO_ACTION_EXECUTION_PLAN.md) | Owns the current evidence-to-action journey and explicitly requires action-relative gap selection rather than backlog execution. |
| [`../plans/RUNTIME_DEPENDENCY_STATE_PROOF_COMPLETION_PLAN.md`](../plans/RUNTIME_DEPENDENCY_STATE_PROOF_COMPLETION_PLAN.md) | Closes bounded Runtime-State Cycle 1 and says stronger target-owned state evidence should remain conditional on action-critical need. |
| [`../audits/2026-09-19_AUDIT-008_current-system-evidence-to-action-readiness.md`](../audits/2026-09-19_AUDIT-008_current-system-evidence-to-action-readiness.md) | Broad cross-system baseline for strengths, defects, evidence gaps, action reachability, and presentation state. |
| [`../working-memory/2026-09-19_1825_parent-synthesis-evidence-path-reaudit.md`](../working-memory/2026-09-19_1825_parent-synthesis-evidence-path-reaudit.md) | Source-traced producer/composition/consumer re-audit and separation of current evidence from action permission. |
| [`../working-memory/2026-09-20_action-relative-producer-reachability-comparison.md`](../working-memory/2026-09-20_action-relative-producer-reachability-comparison.md) | Earlier comparison framework; useful baseline to refresh after F4/F5/F6 progress. |
| [`../working-memory/2026-09-21_f6-post-install-package-state-feasibility.md`](../working-memory/2026-09-21_f6-post-install-package-state-feasibility.md) | Shows why F6 mattered, what it could/could not authorize, and why explicit runtime evidence remained conditional. |
| [`../working-memory/2026-09-30_2119_increment-5_runtime-dependency-state-application-integration_lbd-cycle.md`](../working-memory/2026-09-30_2119_increment-5_runtime-dependency-state-application-integration_lbd-cycle.md) | Final verified F6/Runtime-State integration, proof limits, real-case pressure, and closure. |
| [`2026-09-29_UPGRADEPILOT_EVIDENCE_AI_ARCHITECTURE_PROPOSAL.md`](2026-09-29_UPGRADEPILOT_EVIDENCE_AI_ARCHITECTURE_PROPOSAL.md) | Consolidated evidence-first AI architecture proposal. |
| [`../working-memory/2026-09-29_step4_existing-ai-agent-work-reconciliation.md`](../working-memory/2026-09-29_step4_existing-ai-agent-work-reconciliation.md) | Distinguishes adopted LLM extraction, planner pilot, deferred synthesis, broad discovery, and AI non-gaps. |
| [`../working-memory/2026-09-29_step5_architecture-decisions-experiment-queue-and-integration-strategy.md`](../working-memory/2026-09-29_step5_architecture-decisions-experiment-queue-and-integration-strategy.md) | Defines trigger-driven experiments E1–E10 and explicit framework/AI deferrals. |
| [`2026-09-10_LLM_ASSISTED_MAINTAINER_DECISION_AND_REPORT_SYNTHESIS_PROPOSAL.md`](2026-09-10_LLM_ASSISTED_MAINTAINER_DECISION_AND_REPORT_SYNTHESIS_PROPOSAL.md) | Strong future final-synthesis design, but with prerequisites that are not yet fully satisfied. |
| [`../docs/specifications/UPGRADEPILOT_MAINTAINER_ACTION_SYNTHESIS_SPECIFICATION.md`](../docs/specifications/UPGRADEPILOT_MAINTAINER_ACTION_SYNTHESIS_SPECIFICATION.md) | Canonical action-permission semantics; prevents this proposal from inventing new action meanings. |
| [`../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md`](../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md) | Canonical technical decision model; preserves candidate/applicability/investigation boundaries. |
| [`../docs/architecture/ADR-0010-package-manager-semantic-facts-and-runtime-dependency-state-composition.md`](../docs/architecture/ADR-0010-package-manager-semantic-facts-and-runtime-dependency-state-composition.md) | Accepted package-manager/runtime-state architecture that this proposal does not reopen. |
| [`README.md`](README.md) | Proposal-directory authority: proposals are non-controlling and require later admission through the correct owners. |

---

## 18. Proposal boundaries / non-goals

This proposal does **not**:

- select the next live cycle;
- authorize product source or test changes;
- authorize AI/LLM implementation;
- require a full audit or prohibit one;
- declare F7 to be next;
- declare candidate discovery to be next;
- declare one maintainer action reachable;
- activate Runtime-State Cycle 2;
- reopen closed runtime-state increments;
- select LangGraph, LangChain, OpenHands, CodeQL, Griffe, a graph database, RAG, or another framework;
- change action semantics;
- change AI authority;
- supersede AUDIT-008 or the merged AI research.

Its purpose is to preserve a coherent **candidate direction and decision frame** for the transition after the completed runtime-state program.

---

## 19. Candidate recommendation summary

A reasonable default, subject to evidence, is:

```text
closed Runtime Dependency-State Cycle 1
        ↓
compact current-state / AUDIT-008 delta reconciliation
        ↓
fresh action-relative reachability comparison
        ↓
select ONE next responsibility
        │
        ├─ first non-abstention action, if already earned
        ├─ one closest deterministic producer/composition gap
        ├─ Stage-8 AI candidate-discovery experiment, if discovery is the real bottleneck
        └─ correctness/audit repair, if a deeper defect appears
        ↓
continue normal A0 → A1 → A2 → B → Verification → D → E discipline
```

A full system audit is proposed as **milestone-triggered by default**, not prohibited.

AI/LLM work is proposed as **responsibility-triggered**, not postponed indefinitely and not activated for novelty.

The most important question for the next selection remains:

> **Has UpgradePilot's deterministic evidence spine become strong enough that candidate discovery is now the highest-value remaining bottleneck, or does maintainer-action reachability still fail earlier?**

The next current-state/action comparison should answer that before architecture or implementation is committed.

---

## 20. Proposal lifecycle

**Current proposal-local state:** Candidate.

Possible future dispositions:

- **Partially admitted** — one or more responsibilities are selected into controlling plans while the rest remains open;
- **Deferred** — useful direction but not current priority;
- **Superseded** — a later proposal or audit provides a better route;
- **Rejected** — evidence shows the recommended framing is not useful;
- **Admitted in part** — promoted to the appropriate plan/specification/ADR owners after explicit review.

No lifecycle transition should be inferred merely because this file exists on `main`.
