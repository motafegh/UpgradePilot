# UpgradePilot First Session Plan

**Session ID:** UP-S01  
**Owner:** Ali Rajabi  
**Nominal date:** 2026-07-20  
**Status:** Approved and active first technical session plan  
**Milestone:** M1 — First manual evidence decision  
**Route/Gate:** R1 / G1 — Manual evidence reality  
**Authority:** Executes the first bounded technical session under the UpgradePilot charter, approved capability specification, Learning and Execution Contract, master roadmap, staged milestone plan, and evidence/progress tracker  
**Activation effect:** Technical execution is authorized only within this plan's read-only, manual-evidence boundary. This plan does not authorize architecture, code, implementation-repository creation, corpus acquisition, model work, or infrastructure experiments.

## 1. Session outcome

By the end of the session, create a traceable manual evidence report for one real public Python Dependabot pull request:

> `pydantic/pydantic#13432` — `soupsieve 2.6 → 2.8.4`

Primary output path:

`tracking/evidence/UP-S01_pydantic-13432_manual-evidence-report.md`

The report must produce one weak, uncertainty-aware maintainer action:

- merge after normal review;
- run targeted checks;
- investigate or block;
- defer;
- abstain.

The session is not required to prove objective safety or reproduce the maintainer's historical decision.

## 2. Why this case

This case is appropriate for G1 because:

- it is a real public Python Dependabot PR;
- the change is bounded to one `uv.lock` package entry;
- the proposed update is visible and concrete;
- upstream release notes include compatibility-relevant information, including Python-version support changes;
- public CI and bot evidence exists but is not complete proof;
- the historical merged outcome can be observed while remaining explicitly excluded as ground truth;
- it can teach dependency, evidence, provenance, uncertainty, and recommendation reasoning without requiring automation or architecture.

Known PR identity for orientation:

- repository: `pydantic/pydantic`;
- PR: `#13432`;
- title: `Bump soupsieve from 2.6 to 2.8.4`;
- base branch: `main`;
- base revision: `652a61ce4f9d7d76eaada31535807a485ece0e21`;
- head branch: `dependabot/uv/soupsieve-2.8.4`;
- head revision: `aa2dc024d33f61cdef50bf1973ab5adf0a974f5a`;
- changed dependency: `soupsieve`;
- old version: `2.6`;
- proposed version: `2.8.4`;
- changed file observed in the PR diff: `uv.lock`.

These values must still be checked against the live public PR during the session and recorded with retrieval time.

## 3. Capacity and stop line

### Green mode

Maximum focused time: **240 minutes**.

Suggested checkpoints:

1. orientation and terms — up to 35 minutes;
2. PR and diff evidence — up to 45 minutes;
3. package/release evidence — up to 50 minutes;
4. repository and CI evidence — up to 45 minutes;
5. report, changed-evidence variant, and tracker closure — up to 65 minutes.

These are ceilings, not targets. Stop when the pass condition is met.

### Yellow mode

Maximum focused time: **150 minutes**.

Required Yellow outcome:

- preserve verified PR/diff evidence;
- create the report structure;
- complete at least the dependency-change and evidence-state sections;
- record the exact continuation point.

Do not force a weak recommendation if the evidence package is incomplete.

### Red mode

No technical work. Record a brief public-safe state note and resume UP-S01 later.

### Hard stop

Stop the session when:

- the session pass condition is satisfied;
- the maximum capacity is reached;
- the source becomes inaccessible;
- an unsafe credential, privacy, cost, or untrusted-execution request appears;
- work begins expanding into code, architecture, corpus construction, or unrelated dependency research.

## 4. Authorized sources and actions

Authorized:

- public GitHub PR page and public GitHub metadata;
- public PR diff and changed-file evidence;
- public repository files at the declared base/head revisions;
- public upstream Soup Sieve release notes and package metadata;
- available public CI/check summaries and public bot comments;
- browser or read-only API inspection;
- manual notes and the report file in the Career repository;
- small calculations or comparisons required by the report.

Not authorized:

- executing cloned or downloaded `pydantic` code;
- installing the changed dependency;
- running arbitrary untrusted repository workflows;
- posting comments or modifying the upstream repository;
- using private alerts or credentials;
- creating the UpgradePilot implementation repository;
- writing UpgradePilot code;
- building a database or corpus;
- beginning M2 or later work before M1 evidence is assessed.

## 5. Required concepts for this session

Teach these only as they become necessary around the real case.

### Pull request — PR

A proposed set of Git changes submitted for review and possible merge. For this session, distinguish:

- base branch and base revision;
- head branch and head revision;
- changed files and diff;
- PR state and historical outcome.

Current depth: introductory to guided application. Defer advanced Git history and review administration.

### Diff

A representation of changes between two revisions. It shows what text changed, not every behavioral consequence.

Current depth: identify changed file, package entry, versions, hashes, URLs, sizes, and timestamps. Defer Git diff internals.

### Lockfile

A file recording a concrete resolved dependency set and associated artifacts. Here the visible change is in `uv.lock`.

Current depth: understand what the entry records and what the lockfile change does not establish. Defer resolver algorithms and universal lockfile semantics.

### Direct and transitive dependency

A direct dependency is declared by the project; a transitive dependency reaches the project through another dependency.

Current depth: determine what the available repository evidence supports and preserve `unresolved` when the relationship cannot yet be established. Do not inspect the entire package graph.

### Semantic Versioning — SemVer

A convention where major, minor, and patch numbers communicate intended compatibility meaning. It is a weak signal, not proof that a specific repository is compatible.

Current depth: interpret `2.6 → 2.8.4` as a minor/patch-series change under the numbering pattern while checking actual release evidence. Defer formal ecosystem-wide policy analysis.

### Provenance

The source, revision, retrieval time, and transformation history of evidence.

Current depth: every material claim must identify where it came from and when it was observed.

### Evidence state

Classify relevant evidence as:

- observed;
- inferred;
- missing;
- inaccessible;
- stale;
- conflicting;
- invalid;
- accepted;
- rejected.

### Continuous Integration — CI

Automated checks run for a revision. Passing CI supports only the tested jobs, environment, commit, and scope; it does not certify universal compatibility.

## 6. Ali-owned actions

Ali must personally perform or materially direct these actions:

1. Restate the product boundary and why the session is read-only.
2. Predict what a one-line lockfile package-version change can and cannot establish before inspecting release evidence.
3. Identify the base/head revisions and changed file.
4. Explain the changed `soupsieve` lock entry.
5. State whether direct/transitive status is observed or unresolved from the evidence inspected.
6. Identify at least two plausible risk hypotheses from the upstream change.
7. Select the smallest relevant next evidence for each hypothesis.
8. Classify material evidence states.
9. Draft or materially revise the recommendation and limitations.
10. Respond to the changed-evidence variant.
11. Explain which parts were AI-generated, AI-assisted, Ali-directed, Ali-verified, and Ali-owned.

Ali is not required to independently know packaging terminology before it is taught.

## 7. AI responsibilities

The AI must:

- inspect current evidence before making claims;
- explain each new term to the depth needed now;
- ask for Ali's prediction before revealing consequential interpretation;
- avoid using the merged outcome as the answer;
- prevent literal inspection of every dependency in the repository;
- organize investigation by risk hypothesis and materiality;
- distinguish evidence from inference;
- challenge overconfident language;
- identify what passing CI and release notes do not prove;
- help structure the report without silently authoring Ali's reasoning;
- stop scope expansion;
- record capability evidence conservatively.

## 8. Execution sequence

### Step 1 — Open and orient

Read:

- this session plan;
- the current control state in `../tracking/UPGRADEPILOT_EVIDENCE_AND_PROGRESS_TRACKER.md`;
- the public PR.

Ali states:

- the maintainer decision UpgradePilot supports;
- the five possible output classes;
- why merged status is not ground truth;
- why the session will not execute repository code.

### Step 2 — Prediction before evidence expansion

Before reading detailed release notes, Ali predicts:

- what the lockfile diff likely proves;
- what it cannot prove;
- one compatibility risk that may matter;
- one likely low-cost check.

Record the prediction in the report before correction.

### Step 3 — Capture PR identity and diff

Record:

- PR URL and title;
- state and bot identity;
- base/head branches and revisions;
- retrieval timestamp;
- changed files;
- exact old/new package versions;
- changed lockfile fields visible in the diff;
- what the diff does not establish.

### Step 4 — Determine declaration and dependency context

Inspect only enough repository evidence to answer:

- where the dependency appears in the changed lockfile;
- whether the project directly declares it in an admitted dependency file;
- whether the current evidence supports direct, transitive, optional, development, runtime, or unresolved status.

Do not broaden to the full dependency graph unless a specific material hypothesis requires one bounded path.

### Step 5 — Inspect upstream package and release evidence

Record relevant changes between `2.6` and `2.8.4`, including:

- Python 3.8 support removal;
- Python 3.14 support addition;
- selector behavior additions or changes;
- fixes for inefficient patterns and selector limits;
- relevant metadata or release dates when observed.

For each item, state:

- source;
- observed fact;
- possible repository consequence;
- whether the consequence is established or only hypothesized;
- smallest relevant check.

### Step 6 — Inspect available repository and CI evidence

Record only available evidence, such as:

- changed-file scope;
- public check conclusions tied to the head revision;
- documentation preview evidence;
- performance-report evidence;
- missing logs, jobs, platforms, or environments.

Do not state that passing checks prove compatibility.

### Step 7 — Build the evidence matrix

Use this table in the report:

| Claim or question | Source and revision | Observed evidence | State | Interpretation | What remains unknown | Decision effect |
|---|---|---|---|---|---|---|

At minimum include:

- exact package/version change;
- declaration/direct-transitive status;
- dropped Python support;
- relevant behavior changes;
- CI/check evidence;
- missing evidence;
- historical merged outcome as workflow history only.

### Step 8 — Produce the weak decision report

Use the report structure in Section 9.

The recommendation must state:

- selected action class;
- evidence supporting it;
- highest material uncertainty;
- smallest targeted checks still warranted;
- why broader investigation is or is not proportionate;
- exact claim boundary.

Acceptable language includes:

> No material incompatibility was found within the inspected scope; the remaining uncertainty is bounded but not eliminated.

Do not use absolute safe/unsafe language.

### Step 9 — Changed-evidence variant

Apply this hypothetical change:

> Assume evidence now shows the target project officially supports Python 3.8 in an active environment, and no CI job covers that environment.

Ali must explain:

- which risk becomes material;
- which prior conclusion changes;
- which action class is now appropriate;
- the smallest targeted check or reason to defer/block;
- why the investigation should expand only along this relevant path.

### Step 10 — Close and update tracker

Record:

- focused minutes;
- report path;
- evidence links;
- result: Pass, Partial, Blocked, Invalid evidence, or Out of scope;
- assistance labels by report section;
- narrow capability evidence;
- corrections and changed mental model;
- exact next action.

Do not increase a capability above the evidence demonstrated.

## 9. Required report structure

Create:

`tracking/evidence/UP-S01_pydantic-13432_manual-evidence-report.md`

Use:

```markdown
# UP-S01 Manual Evidence Report — pydantic/pydantic#13432

## 1. Case identity and retrieval boundary

## 2. Ali's initial prediction

## 3. Observed PR and diff evidence

## 4. Dependency declaration and relationship status

## 5. Upstream package and release evidence

## 6. Repository and CI evidence

## 7. Evidence-state matrix

## 8. Risk hypotheses and proportional checks

## 9. Weak decision

### Action class

### Supporting evidence

### Material uncertainty

### Targeted checks

### Claim boundary

## 10. Changed-evidence variant

## 11. What the evidence does not prove

## 12. Assistance and ownership record

## 13. Sources and retrieval timestamps
```

## 10. Session pass condition

UP-S01 passes when:

- the report exists at the declared path;
- case identity and retrieval boundary are complete;
- Ali's initial prediction is preserved before correction;
- material factual claims trace to public evidence;
- dependency relationship status is supported or explicitly unresolved;
- at least two material risk hypotheses and proportional checks are recorded;
- the selected action class follows from the evidence;
- limitations and missing evidence are explicit;
- the changed-evidence variant is answered correctly;
- assistance and ownership are labeled honestly;
- the tracker is updated.

Passing UP-S01 may also close M1 when the AI audit confirms narrow D2 guided application for the required G1 responsibilities.

## 11. Failure and continuation behavior

### Partial

Continue the same report in the next session. Do not create a new plan.

### Evidence unavailable

Preserve the inaccessible state and use only a proportionate lawful alternative. Abstention may be the correct result.

### Case unsuitable

Record the exact reason. A replacement must remain one public Python Dependabot PR and must not broaden product scope.

### Conceptual gap

Teach the smallest missing concept, verify it with the current case, and return to the report.

### Scope expansion

Stop and return to the current unanswered report question.

## 12. Start message

Ali begins with:

```text
START DAY 1
Actual date: YYYY-MM-DD
Mode: Green | Yellow | Red
Available focused minutes:
Current deliverable: UP-S01 manual evidence report for pydantic/pydantic#13432
First expected proof: verified PR identity, base/head revisions, changed file, and Ali's initial prediction
```

If started after 2026-07-20, use the actual date. Do not restart the 90-day system or recreate planning documents.

## 13. Authorization result

**Audit result:** Passed.  
**Approval result:** Approved and active.  
**R0 planning closure:** Pass.  
**Technical execution status:** Ready to begin.  
**Exact next action:** Ali sends the start message above and begins UP-S01.  
**No additional planning artifact is authorized before execution.**
