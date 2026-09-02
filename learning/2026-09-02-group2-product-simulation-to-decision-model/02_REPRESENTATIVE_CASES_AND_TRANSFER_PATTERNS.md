# Group 2 — Representative Product-Simulation Cases and Transfer Patterns

**Learning-artifact date:** 2026-09-02  
**Evidence horizon:** `main@8f25bcb4e158f4f6e779ce63c264957f97e44771`  
**Refinement:** 2026-09-02 proportionality edit; evidence horizon and engineering scope unchanged  
**Roadmap responsibility:** Group 2 from `../../plans/UPGRADEPILOT_WHOLE_PROJECT_LEARNING_ARTIFACT_ROADMAP_PLAN.md`  
**Artifact role:** representative case + practical transfer companion  
**Target depth:** learn the distinct transfer patterns; use original case evidence for package-specific detail  
**Primary companion:** [`01_PRODUCT_SIMULATION_PRESSURES_AND_DECISION_MODEL_EVOLUTION.md`](01_PRODUCT_SIMULATION_PRESSURES_AND_DECISION_MODEL_EVOLUTION.md)

Note 1 owns the historical pressure → accepted decision-model evolution and the canonical reasoning spine. This companion does **not** reteach that model case by case. It keeps detailed treatment only where the case contrast adds distinct practical transfer value.

---

## 1. Case-to-concept map

Use this matrix first. Open the original simulation evidence when you need exact repository/package/run detail.

| Case / pressure | Distinct lesson to retain | Detail level here | Primary evidence |
|---|---|---|---|
| **S001** | one target-specific applicability path can be refuted without closing the whole transition | short reference | [`S001_S002_CROSS_CASE_ARTIFACT_REVIEW.md`](../../product-simulation/S001_S002_CROSS_CASE_ARTIFACT_REVIEW.md), [`IMPACT_INVESTIGATION_COVERAGE_REBASE_2026-08-06.md`](../../product-simulation/IMPACT_INVESTIGATION_COVERAGE_REBASE_2026-08-06.md) |
| **S002** | direct declaration can still involve mediated exposure and insufficient exact behavior coverage | short reference | [`S001_S002_CROSS_CASE_ARTIFACT_REVIEW.md`](../../product-simulation/S001_S002_CROSS_CASE_ARTIFACT_REVIEW.md), [`IMPACT_INVESTIGATION_COVERAGE_REBASE_2026-08-06.md`](../../product-simulation/IMPACT_INVESTIGATION_COVERAGE_REBASE_2026-08-06.md) |
| **S003** | failing CI needs responsibility-level causal decomposition; strong attribution can remain bounded | short reference | [`S003_POST_CASE_SYNTHESIS.md`](../../product-simulation/S003_POST_CASE_SYNTHESIS.md) |
| **S004** | baseline sufficiency and justified stopping | **detailed** | [`S004_POST_CASE_SYNTHESIS.md`](../../product-simulation/S004_POST_CASE_SYNTHESIS.md) |
| **S005** | exact target evidence can legitimately weaken coarse caution | **detailed** | [`S005_POST_CASE_SYNTHESIS.md`](../../product-simulation/S005_POST_CASE_SYNTHESIS.md) |
| **S006** | bounded dynamic execution can be the uniquely discriminating investigation | **detailed** | [`CONVERSATION_C_INVESTIGATION_SELECTION_PRESSURE_TEST_01.md`](../../product-simulation/CONVERSATION_C_INVESTIGATION_SELECTION_PRESSURE_TEST_01.md), [`DECISION_MODEL_HANDOFF_2026-08-07.md`](../../product-simulation/DECISION_MODEL_HANDOFF_2026-08-07.md) |
| **S007** | a sensible planned check can lose value after stronger evidence arrives | **detailed** | [`CONVERSATION_C_HANDOFF_S007_2026-08-09.md`](../../product-simulation/CONVERSATION_C_HANDOFF_S007_2026-08-09.md) |
| **S008** | local mechanism closure does not establish transition-level discovery completeness | short reference | [`CANDIDATE_DISCOVERY_COVERAGE_PRESSURE_TEST_01.md`](../../product-simulation/CANDIDATE_DISCOVERY_COVERAGE_PRESSURE_TEST_01.md) |
| **S009** | material repository context can remain distinct from technical impact candidates | short reference | [`CANDIDATE_DISCOVERY_COVERAGE_PRESSURE_TEST_01.md`](../../product-simulation/CANDIDATE_DISCOVERY_COVERAGE_PRESSURE_TEST_01.md) |
| **S010** | one transition can contain multiple independent mechanisms; first candidate found is not discovery completeness | short transfer | [`S010_POST_CASE_SYNTHESIS.md`](../../product-simulation/S010_POST_CASE_SYNTHESIS.md) |
| **S011** | optional declaration → environment formation → activation → behavior coverage are separate propositions | **detailed** | [`S011_POST_CASE_SYNTHESIS.md`](../../product-simulation/S011_POST_CASE_SYNTHESIS.md) |
| **S012** | active target context can include historical persisted state and producer-version provenance | **detailed** | [`S012_POST_CASE_SYNTHESIS.md`](../../product-simulation/S012_POST_CASE_SYNTHESIS.md) |

The matrix is a transfer map, not a scenario taxonomy or universal rule set.

---

## 2. S004 — stopping is an evidence-backed technical result

### Case pressure

S004 studied pytest `9.0.2 → 9.0.3` in glyphsLib as a deliberate baseline-sufficient control.

The relevant evidence established that:

- the changed development dependency was actually consumed by tox;
- exact proposed-version test responsibilities ran at the PR head;
- ordinary and regression pytest paths passed across relevant environments;
- official upstream material described the patch as a bug-fix/drop-in replacement;
- no decision-critical contradiction or named unresolved question remained.

Baseline and full simulation both selected `merge_after_normal_review`.

### Transfer lesson

The useful reasoning was not `patch + green CI → merge`. It was:

```text
baseline action looks plausible
→ confirm the assumptions that give that action authority
→ exact changed responsibility is genuinely exercised
→ no material contradiction or discriminating open question remains
→ keep deeper conditional stages inactive
→ stop
```

This case is the control against over-investigation. Available tools, budget, or curiosity do not create an evidence need.

### Proof boundary

S004 did **not** prove general patch-update safety. It proved only that the bounded case/question had enough authority-critical evidence to stop without deeper work.

---

## 3. S005 — evidence must be able to remove an unnecessary gate

### Case pressure

S005 studied pytest `9.0.3 → 9.1.1` in ModelArrayIO.

The transparent baseline saw direct dependency status, passing CI, and literal `breaking` / removal / deprecation language, so it selected `run_targeted_checks`.

The full investigation then established that:

- the exact proposed pytest version was consumed by the lock-backed test path;
- relevant matrix executions passed;
- the upstream breaking behavior required activation conditions the target did not use;
- named deprecated surfaces were absent or used in supported form;
- no remaining target-specific question could justify a useful additional check.

The full action became `merge_after_normal_review`.

### Transfer lesson

Turn upstream prose into concrete candidate-specific activation propositions:

```text
upstream change statement
→ exact mechanism / activation condition
→ exact target configuration, source, or usage surface
→ scoped execution/evidence
→ unresolved question OR closure
```

A system that can only escalate caution but cannot remove a coarse unsupported caution is not well calibrated.

### Proof boundary

S005 did not establish that warning language is generally unimportant or that negative search alone proves absence. The action changed because several exact target/evidence conditions jointly closed the bounded concern.

---

## 4. S006 — dynamic execution is justified when it uniquely discriminates

### Case pressure

The qldebugger/Pydantic pressure case involved changed Pydantic validator `TypeError` behavior across a major-version boundary. The target had a validator that intentionally raised `TypeError` for a non-string handler.

Static evidence could establish the upstream semantic change, the target framework/declarative exposure, and the implicated branch. It could not settle the exact old/new observable exception behavior.

Several checks were nearby but weak for the owned proposition:

- import-only execution;
- valid-handler execution;
- install-only resolution;
- a broad unconstrained test-suite run.

The bounded old/new differential reproduction directly activated the implicated branch and produced interpretable contrast.

### Transfer lesson

Do not rank evidence by category alone:

```text
static evidence not enough for this exact behavioral proposition
+ bounded experiment instantiates the activation condition
+ plausible outcomes change the proposition state
→ dynamic differential execution has unique discriminating value
```

The important property is **discrimination**, not “dynamic is stronger.”

### Proof boundary

S006 does not authorize full-suite or runtime execution whenever static evidence is incomplete. The experiment was valuable because it was narrowly aligned with the exact changed behavior.

---

## 5. S007 — investigation value is stateful

### Case pressure

S007 involved a BiomedParse Torch-family proposal. At admission, exact wheel metadata and an isolated resolver dry-run were reasonable candidate investigations.

Further authoritative source/build evidence then established that the retained TorchVision 0.21 release contract required the corresponding Torch 2.6 family while the target proposed `torch==2.8.0`. For the owned package-family proposition, the compatible version sets had no intersection.

### Transfer lesson

A planned check is not an execution obligation:

```text
T1: resolver run could materially discriminate
↓
new authoritative evidence arrives
↓
T2: proposition already refuted
↓
resolver run becomes corroborative/redundant
→ cancel/prune it
```

Investigation selection must be recomputed against the **current admitted evidence state**.

### Related stopping distinction

S007 is a **resolved** stop. Keep it distinct from:

- **path-pruned** stop — a necessary proposition closes a branch; and
- **unresolved/no-justified-check** stop — the material proposition remains non-final but the available checks cannot produce sufficiently scoped, authoritative, discriminating, proportionate evidence.

Those endpoints can share “no next check” as an operational surface while preserving different knowledge states.

---

## 6. S010 — discovery breadth is a separate question from candidate applicability

S010 does not need another full walkthrough, but its transfer lesson is worth retaining.

A real NumPy requirement broadening exposed at least two independently grounded mechanisms in the same transitive runtime area, with different target handling states. One mechanism related to an existing `<2` guard that the proposal removed; another had a target-local compatibility shim.

This pressure established:

```text
one valid candidate found
!= transition discovery complete
```

and:

```text
same dependency / broad compatibility label
!= same mechanism
```

It is a concrete transfer anchor for the **candidate-discovery coverage** distinction explained in Note 1. It also preserves an important proposal-shape detail: requirement broadening is not the same thing as one exact old-version → exact proposed-version replacement.

---

## 7. S011 — environment formation precedes activation and behavior coverage

### Case pressure

S011 studied NumPy inside Dictare's optional `[mlx]` dependency family.

The repository supported an Apple-Silicon MLX path, but the inspected standard and macOS workflows installed `.[dev]`, not `.[mlx]`.

A simplistic reading could say “macOS CI exists, so the macOS/MLX path is covered.” The exact install commands refuted that shortcut.

### Transfer model

For this mechanism, several propositions must remain separate:

```text
OPTIONAL DEPENDENCY DECLARED?
↓
OPTIONAL ENVIRONMENT FORMED?
extra actually installed/resolved?
↓
RUNTIME ACTIVATION CONDITIONS SATISFIED?
platform + architecture + package availability + configuration/selection?
↓
BEHAVIOR PATH EXERCISED?
relevant runtime behavior actually covered?
```

Therefore:

```text
declaration
!= environment formation
!= runtime activation
!= behavior coverage
```

The same workflow can be strong evidence for one proposition and irrelevant to another.

### Negative-evidence boundary

Exact workflow definitions can support a local statement such as “these inspected workflows do not install `[mlx]`.” They do not automatically prove that no CI/automation anywhere forms that environment unless the broader evidence boundary is independently complete.

### Proof boundary

S011 did not establish that NumPy 2.4.6 breaks Dictare or that every optional dependency needs dedicated CI. It established a real activation/coverage gap and the propositions needed to describe it honestly.

---

## 8. S012 — current source can be exact yet still omit active historical state

### Case pressure

S012 studied scikit-learn `1.7.2 → 1.8.0` in a Freqtrade/FreqAI persistence path.

The target can persist model/feature/label pipeline state and reuse it later. Such persisted state may contain scikit-learn-owned objects. Upstream scikit-learn evidence states that persisted objects are not supported for loading across different scikit-learn versions.

### Transfer model

For this mechanism, applicability can span two dependency environments:

```text
producer environment/version
→ persisted target artifact/state
→ later consumer environment/version
```

So:

```text
fresh-state compatibility
!= persisted-state compatibility
```

The current repository revision and current dependency environment remain necessary evidence, but they are not always the complete active target context.

### Investigation consequence

If a later question requires consequence evidence, the check must instantiate the actual activation boundary:

```text
representative artifact created under old dependency environment
→ preserved unchanged
→ loaded under proposed environment
→ observe the relevant result
```

A fresh training/test run would answer a different proposition.

### Negative-evidence boundary

Failure to find deployment artifact history in the repository cannot become `no old artifact exists`. For a concrete deployment, producer-version provenance may remain unresolved.

### Proof boundary

S012 did not establish that scikit-learn 1.8 breaks Freqtrade, that every deployment contains old state, or that every persisted artifact fails. It established a real history-dependent applicability mechanism and the evidence identity it would require.

---

## 9. Short references for S001–S003 and S008–S009

These cases remain important, but their main conceptual work is already taught in Note 1.

- **S001:** use when practising candidate/path-local non-applicability. A Python-support concern can close against exact target range evidence without becoming transition-level safety.
- **S002:** use when practising mediated exposure. Direct declaration and passing install/build do not establish that the affected adapter/runtime behavior was exercised.
- **S003:** use when practising causal failure decomposition. Localize workflow → step → command → dependency relation and compare competing causes; strong attribution can remain non-absolute when reproduction is unavailable.
- **S008:** use when separating local mechanism closure from candidate-discovery completeness; resolving an artifact-serviceability question does not prove the broader OpenCV transition fully understood.
- **S009:** use when separating technical-candidate reasoning from material repository-purpose/provenance context.

Follow the matrix links rather than duplicating the original scenario mechanics here.

---

## 10. Practical transfer checklist for a new case

Use the canonical reasoning spine in Note 1 for the full model. For day-to-day transfer, this shorter checklist is usually enough:

1. **Freeze the exact object.** What PR/revision, dependency transition or constraint change, and target context are actually being evaluated?
2. **Name one mechanism-specific candidate.** What changed, through which target relationship, under what activation condition, with what possible consequence?
3. **Separate the propositions.** What is already established/refuted, and what remains unresolved/conflicted? Do not turn missing evidence into refutation.
4. **Check the proof boundary.** Are you reasoning about proposition evidence coverage, candidate path-model coverage, or broader candidate-discovery coverage?
5. **If non-final, identify the discriminating target.** What exact observation could materially change the state? Prefer the smallest supported investigation that actually instantiates the mechanism.
6. **Re-evaluate after material evidence changes.** Previously planned investigations may lose value; new evidence may prune a path or expose a different mechanism.
7. **Stop with the correct meaning.** Resolved, path-pruned, and unresolved-with-no-justified-check are different outcomes. None means “the whole update is proven safe.”

---

## 11. Transfer checks worth being able to answer

A small set is enough for this companion:

1. Why is S004 a stopping/sufficiency case rather than evidence that patch updates with green CI are safe?
2. What exact evidence gave S005 authority to remove the baseline's targeted-check requirement?
3. Why was old/new differential execution discriminating in S006, while the planned resolver execution became redundant in S007?
4. In S011, what does a successful macOS workflow prove if it never installs the affected optional extra?
5. In S012, why can producer and consumer dependency versions both be necessary facts in one applicability question?
6. Given a new case, name one observation that is relevant but not discriminating for your owned proposition.

---

## 12. Fast relearning route and boundaries

Fast return:

1. Read the matrix in Section 1.
2. Revisit S004/S005 for **stop vs action revision**.
3. Revisit S006/S007 for **investigation gains vs loses value**.
4. Revisit S011/S012 for **new target-context mechanisms**.
5. Apply the seven-item checklist to one unfamiliar dependency-update example.

For deeper concept theory, use existing frozen learning material instead of expanding this companion:

- [`2026-08-10-seven-concept-foundation-pre-a-c-implementation.md`](../2026-08-10-seven-concept-foundation-pre-a-c-implementation.md)
- [`2026-08-10-product-decision-model-a-b-c-mastery-note.md`](../2026-08-10-product-decision-model-a-b-c-mastery-note.md)

Current accepted semantics remain owned by:

- [`UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md`](../../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md)

The historical cases do not establish target safety, representative frequency, complete candidate recall, production readiness, or universal policy/actions. Exact case mechanics and validation history remain available in their original evidence rather than being reproduced here.