# Manual Runtime Scenario Template

> This template is a starting structure, not a closed checklist or implementation schema. Add, split, reorder, or remove sections when the real case requires it. Never force a case into this structure if doing so would hide a material actor, input, responsibility, uncertainty, or outcome.

## Scenario identity

- **Scenario ID:**
- **Status:** selected / active / complete / stopped
- **Repository:**
- **Dependency update:**
- **Public change reference:**
- **Investigated revision or time boundary:**
- **Date investigated:**
- **Investigators:** Ali and AI assistant

## Live case state

Update this section only after a material transition so another human or AI can resume the case without reconstructing its current state.

- **Current phase:**
- **Current primary question:**
- **Current working hypothesis:**
- **Last material finding:**
- **Current recommendation state:**
- **Current material limitations:**
- **Next selected action:**
- **Reason for next action:**
- **Last updated:**

## 1. Why this case was selected

Describe:

- why this is a real and useful dependency-update case;
- which current uncertainty, assumption, or coverage dimension it tests;
- how it differs materially from completed scenarios;
- known access, legal, reproducibility, or timing limits;
- what would make the case no longer worth continuing.

## 2. Initial real-world event

Describe what happened before UpgradePilot begins.

Questions to consider:

- Who or what created the update proposal?
- What does the maintainer see?
- Is the event a Dependabot pull request or another justified equivalent?
- What state exists before UpgradePilot is invoked?
- What is known to the user but not necessarily supplied to the system?

## 3. Intended invocation

Record only what UpgradePilot would actually receive at the start.

| Item | Value | Supplied by | Why supplied | Required, conditional, or optional | Missing/wrong consequence |
|---|---|---|---|---|---|

Distinguish browser-visible information from true invocation input.

Record open questions about invocation design without freezing a contract.

## 4. Case identity and reproducibility boundary

Identify the exact case as far as public evidence permits.

Potential identity elements may include repository, pull-request or change reference, base revision, head revision, dependency name, old version, new version, update producer, relevant run, and observation time.

These are prompts, not mandatory fields for every future case.

Explain:

- which identity elements are authoritative;
- which were discovered later;
- whether any evidence belongs to a later revision or state;
- what another investigator would need to reproduce the case;
- what cannot be reproduced exactly.

## 5. Actors and systems

List every material producer, transmitter, transformer, store, investigator, decision maker, and consumer involved in this case.

| Actor or system | Role | Data produced or consumed | Trust/authority limits | Interaction with UpgradePilot |
|---|---|---|---|---|

Add actors not anticipated by existing project documents.

## 6. Initial questions for the maintainer decision

State the real questions before gathering all available material.

For each question, explain why its answer could affect the recommendation or report.

| Question | Why it matters | Evidence likely needed | Consequence if unresolved |
|---|---|---|---|

Questions may be added, removed, narrowed, or reordered as the case develops.

## 7. Evidence discovery map

Before collecting evidence, record where relevant information might originate.

Potential sources may include the pull request, target repository, manifests, lockfiles, package index, upstream repository, tags, changelogs, release notes, documentation, source code, CI, issue tracker, advisories, test artifacts, or other public systems.

This list is not exhaustive and no source is required merely because it appears here.

| Potential source | Question it may answer | Expected authority | Access path | Worth acquiring now? |
|---|---|---|---|---|

## 8. Evidence inventory

For every material item actually supplied or acquired, record at least the useful current depth of:

- practical meaning;
- origin or producer;
- acquisition path;
- repository/revision/release/run/time identity;
- raw preserved form or stable reference;
- question it may answer;
- authority and what it cannot establish;
- missing/stale/invalid/ambiguous/manipulated consequences;
- downstream use;
- whether another source can corroborate or replace it.

| Evidence ID | Item | Origin | Identity/time context | Observation | Purpose | Authority/limits | State | Downstream use |
|---|---|---|---|---|---|---|---|---|

Use additional fields when the case exposes a distinction not represented here.

## 9. Full progressive manual investigation log

Use this as the live primary execution record. Document material steps while their rationale and result remain current and in the order they actually happen. Do not wait until the investigation is finished and reconstruct an artificially clean path.

A material step is one that changes or materially tests a question, evidence set, hypothesis, finding, recommendation, product responsibility, method assessment, uncertainty, limitation, or next branch. Group routine navigation, repeated safe lookups, and mechanically related commands instead of creating a step for every operation.

For every material step, preserve this chain:

```text
current state and question
→ approach selection and reason
→ expected output and stop criteria
→ execution
→ raw output and direct observations
→ interpretation, alternatives, and verification
→ output and outcome
→ next action and reason
```

Record concise professional rationale sufficient for review. Do not expose or request hidden private chain-of-thought or unrestricted scratchpad text.

### Investigation step N — descriptive name

#### A. State before action

- **Current question or uncertainty:**
- **Why this matters:**
- **Current evidence:**
- **Current working hypothesis:**
- **Current recommendation or decision effect:**
- **Current product-model implication:**

#### B. Approach selection

- **Selected approach:**
- **Why selected now:**
- **Alternatives considered:**
- **Why alternatives were not selected now:**
- **Required inputs and assumptions:**
- **Expected useful output:**
- **What success would establish:**
- **What success would not establish:**
- **Stop, switch, or escalation condition:**
- **Approach proposed by:**
- **Approach selected or approved by:**

#### C. Execution

- **Performed by:**
- **Actions taken:**
- **Tools, commands, APIs, or sources:**
- **Identity, revision, and time boundary:**
- **Reads, writes, external effects, or risk:**
- **Execution problems or deviations:**

#### D. Output and observations

- **Raw output or preserved reference:**
- **Direct observations:**
- **Missing, invalid, stale, conflicting, or inaccessible output:**
- **What the output demonstrates:**
- **What the output does not demonstrate:**

#### E. Interpretation and verification

- **Interpretation:**
- **Reasoning summary:**
- **Alternative explanations:**
- **Supporting evidence:**
- **Contradicting evidence:**
- **Uncertainty and limitations:**
- **Interpreted by:**
- **Verification or challenge performed by:**

#### F. Outcome

- **Question answered or current state:**
- **Step output:**
- **Step outcome:**
- **Finding created, changed, rejected, or left unresolved:**
- **Effect on recommendation:**
- **Effect on product understanding:**
- **What remains unchanged:**

#### G. Progressive continuation

- **Next selected action:**
- **Why it follows from this outcome:**
- **Other possible actions not pursued now:**
- **Current approach status:** complete / repeat / stopped / deferred / replaced
- **If replaced, replacement approach and reason:**

Duplicate this subsection only for material steps. When a material approach fails or is abandoned, preserve why it was attempted, what it produced, why the result was inadequate, what was retained, why it stopped, and what replaced it. When later evidence changes a finding, preserve the prior finding as superseded, identify the new evidence, explain the revision, and record its downstream effect rather than silently rewriting history.

## 10. Observation, interpretation, and finding separation

Summarize material reasoning chains explicitly.

```text
source observation
→ attributed source claim
→ human/tool/model interpretation
→ corroborated / contradicted / irrelevant / unresolved finding
→ permitted decision effect
```

| Chain ID | Observation | Interpretation source | Finding state | Supporting/contradicting evidence | Permitted decision effect |
|---|---|---|---|---|---|

Do not call a claim corroborated merely because it was extracted accurately from its source.

Every final recommendation or abstention reason must trace backward through a finding, interpretation, direct observation, preserved evidence, and exact case identity. No material decision reason should appear for the first time only in the final report.

## 11. Repository-specific relevance

Explain how the dependency and proposed changes matter—or do not matter—to the target repository.

Potential questions include:

- Is the dependency direct, transitive, optional, development-only, test-only, build-time, or runtime?
- Where and how is it declared or resolved?
- Where and how is it used?
- Which upstream changes intersect with that usage?
- Which interpreter, platform, architecture, build, or deployment constraints matter?
- What cannot be inferred from static references alone?

These are prompts, not mandatory analyses for every case.

## 12. Checks, comparisons, and observed behavior

Record any useful test, CI, static, dynamic, metadata, source, or cross-version comparison.

| Check or comparison | Question answered | Inputs/revision | Result | What it demonstrates | What it does not demonstrate | Reliability limits |
|---|---|---|---|---|---|---|

Distinguish update-caused failures from pre-existing, environmental, flaky, unrelated, and unresolved failures.

## 13. Missing, inaccessible, conflicting, and uncertain evidence

| Item or question | State | Why | Decision/report consequence | Possible recovery or alternative |
|---|---|---|---|---|

Add new states when reality requires them. Do not force all problems into a fixed vocabulary.

## 14. Changed-evidence or failure variant

Use one or more realistic variants only when they reveal material product behavior.

Examples may include missing release information, stale CI, a different base revision, contradictory metadata, unavailable upstream repository, or a changed repository constraint.

For each variant:

- what changed;
- why the variant is realistic;
- which observations or findings change;
- which conclusions remain stable;
- how the report changes;
- whether the recommendation changes;
- what this teaches about the product.

Do not invent a decision change merely to satisfy a test expectation.

## 15. Manual decision construction

State the most justified maintainer action at the current evidence level.

- **Candidate outcome:**
- **Decision reasons:**
- **Evidence supporting each reason:**
- **Material limitations:**
- **Unresolved questions:**
- **Why a stronger or weaker outcome is not justified:**
- **Suggested next action or targeted check:**
- **Human judgment still required:**

Outcome vocabulary is not frozen. Use the clearest bounded action for the case and flag any new outcome class that may need cross-case evaluation.

## 16. Human-readable report

Write the report the maintainer should receive.

It should identify:

- the exact case;
- what changed;
- evidence-based findings;
- repository-specific relevance;
- important contradictions or missing evidence;
- recommendation or abstention;
- reasons;
- limitations;
- next actions;
- provenance references useful to the maintainer.

Do not hide uncertainty or imply safety proof.

## 17. Conceptual machine-consumable result

Describe the information another system would need without freezing an implementation schema.

Possible information groups include:

- case identity;
- invocation context;
- evidence references and states;
- observations and attributed claims;
- findings and lineage;
- limitations and unresolved questions;
- decision outcome and reasons;
- suggested next actions;
- report/provenance metadata;
- user follow-up state.

Use a table, outline, or illustrative data structure. Clearly label it non-binding.

## 18. User interaction and follow-up flow

Describe:

- what the user supplied;
- what UpgradePilot discovered;
- where clarification or authorization was needed;
- what the user sees;
- what the user may do next;
- whether new evidence or action should trigger a rerun, comparison, replay, or state transition;
- what should be remembered across runs.

## 19. Candidate methods by responsibility

| Responsibility/question | Manual method used | Candidate automation methods | Simplest credible baseline | Strengths | Failure modes | Downstream risk | Evidence needed before adoption |
|---|---|---|---|---|---|---|---|

The method list is open and may include deterministic parsing, repository analysis, static analysis, dynamic tests, retrieval, search, LLMs, learned models, cross-source comparison, or human review.

Do not select permanent architecture in this scenario record.

## 20. Data-flow and operating-model changes revealed

Record what this case adds, changes, removes, or leaves unresolved regarding:

- system actors;
- trust boundaries;
- invocation inputs;
- acquired evidence;
- runtime stages;
- optional or conditional branches;
- evidence lineage;
- state transitions;
- user interactions;
- outputs;
- decision authority;
- failure/degradation behavior;
- product boundary.

Include an updated local diagram when it materially improves understanding. Shared diagrams should be updated only after the pattern is sufficiently cross-case or otherwise important.

## 21. Scenario retrospective

Answer:

- What did this case teach us that existing documents did not make clear?
- Which assumed input or stage was unnecessary?
- Which missing input or responsibility became important?
- Which local method looked useful, weak, or misleading?
- Which product responsibility appeared to be conditional rather than universal?
- What should remain outside UpgradePilot?
- What current plan or specification may conflict with the observed runtime?
- What should be tested by a contrasting future case?
- Did further investigation stop at the right point?
- What remains unresolved?
- What can Ali now explain without assistance?
- Which material decision or investigation step did Ali personally perform, challenge, or verify?
- What still depends substantially on AI interpretation or control?

## 22. Coverage update

Update [`SCENARIO_COVERAGE.md`](SCENARIO_COVERAGE.md):

- register the completed case;
- mark only dimensions genuinely covered;
- add newly discovered dimensions;
- record the most useful contrasting next-case need.

## 23. Progressive-record audit

A scenario cannot be declared complete until the following are true at the useful depth required by the case:

- [ ] Every material investigation step has a stated question and reason.
- [ ] Every material approach has a selection rationale.
- [ ] Material alternatives and reasons for not pursuing them are visible.
- [ ] Expected output and stop, switch, or escalation criteria were recorded before or at execution rather than invented only after the result.
- [ ] Raw outputs and direct observations are separated from interpretations.
- [ ] Step outputs are separated from step outcomes.
- [ ] Findings trace to preserved evidence and exact case identity.
- [ ] Recommendation or abstention reasons trace to findings and limitations.
- [ ] Each material next action traces to the prior outcome and has an explicit reason.
- [ ] Failed or abandoned material approaches remain visible.
- [ ] Superseded findings remain visible with the evidence and reason that changed them.
- [ ] Human and AI contributions are honestly attributed at the level needed to assess the work.
- [ ] Missing, conflicting, stale, inaccessible, and uncertain evidence remains explicit.
- [ ] No material conclusion appears for the first time only in the final report.
- [ ] Routine operations were grouped rather than documented ceremonially.
- [ ] Further investigation stopped when it ceased to change the decision, material limitation, product understanding, or method assessment enough to justify its cost.

The audit verifies traceability and progressive execution. It is not permission to make every scenario long or to fill fields that do not materially apply.

## 24. Completion statement

State:

- why the scenario is complete or why it was stopped;
- which outputs were produced;
- which evidence was unavailable;
- what conclusions are supported;
- what conclusions are not supported;
- the single most important product-model change caused by the case;
- the most valuable next contrasting scenario.
