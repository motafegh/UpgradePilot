# Step 3 — Whole-Pipeline Architecture Map

**Recorded:** 2026-09-29  
**Branch:** \`analysis/ai-agentic-capability-map-2026-09-28\`  
**Status:** COMPLETE initial whole-system map  
**Live-main snapshot:** \`b16c984daa8f5e78ebe83856c5b010c137a405ee\`  
**Live product state:** Increment 3 CLOSED / Product Verification #14 GREEN / Increment 4 selected but A0 not yet started  
**Inputs:** Project Charter, Core Pipeline/Contract Specification, Product Decision Model Specification, current \`investigation.py\`, current maintainer-action evaluator, mature-system horizon, Track A, Tier-1 research, Step 2B-X independent architecture refresh, Step 2C adversarial reconciliation.

This is an architecture/reconciliation map. It does not authorize implementation, change accepted specifications/ADRs, or alter \`MEMORY.md\`.

---

# 1. Purpose

This record answers:

> **From one public Dependabot dependency-update pull request to the final maintainer-facing output, what responsibilities must UpgradePilot perform, what exists today, what is independently supported as the mature direction, where AI/agents may participate, and which architecture decisions remain unresolved?**

The map intentionally separates:

- **product responsibility** — what must be achieved;
- **evidence producer** — where facts can come from;
- **reasoning mechanism** — deterministic/model/agent/human;
- **authority** — what may promote a claim;
- **current implementation status** — what source/tests establish today;
- **mature direction** — what Track B/C independently supports;
- **optional future subsystems** — useful but not core requirements.

---

# 2. Status legend

Each responsibility may carry more than one label.

- **[CURRENT]** — implemented in current \`main\` and part of the real product flow.
- **[VERIFIED]** — current behavior has an accepted evidence/verification boundary.
- **[SELECTED-NEXT]** — accepted next responsibility selected by live \`MEMORY.md\`, but not implemented yet.
- **[ACCEPTED-CONTRACT]** — durable spec/ADR responsibility exists, though full implementation may not.
- **[SUPPORTED-MATURE]** — independently supported by Track B/C as a mature direction.
- **[PROJECT-CHOICE]** — valid current project-stage choice, not yet established as the mature optimum.
- **[EXPERIMENTAL]** — plausible method requiring comparative evidence.
- **[UNRESOLVED-COMPETITION]** — two or more credible methods remain; experiment/research is required.
- **[OPTIONAL-FUTURE]** — useful downstream capability but not required for the current core.
- **[OUTSIDE-CORE]** — explicitly outside the frozen Charter boundary.

---

# 3. Whole-system map at one glance

\`\`\`text
PUBLIC DEPENDABOT PR
        │
        ▼
┌──────────────────────────────────────────────────────────────┐
│ 1. ADMISSION + EXACT IDENTITY                                │
│ repo / PR / base / head / changed files / dependency source │
│ [CURRENT] [SUPPORTED-MATURE]                                │
└──────────────────────────────────────────────────────────────┘
        │
        ▼
┌──────────────────────────────────────────────────────────────┐
│ 2. EXACT DEPENDENCY TRANSITION + SOURCE CONTEXT              │
│ package / old version / proposed version / source context    │
│ [CURRENT] [SUPPORTED-MATURE]                                │
└──────────────────────────────────────────────────────────────┘
        │
        ├───────────────────────────────────────────────────┐
        │                                                   │
        ▼                                                   ▼
┌──────────────────────────────┐              ┌──────────────────────────────┐
│ 3A. TARGET / CI EVIDENCE     │              │ 3B. PACKAGE / UPSTREAM       │
│ workflows / jobs / commands  │              │ release / repo / interval   │
│ env / runtime correlation    │              │ changelog / source/API diff │
│ [CURRENT + EXPANDING]        │              │ [CURRENT + EXPANDING]        │
└──────────────────────────────┘              └──────────────────────────────┘
        │                                                   │
        ├──────────────────────────────┬────────────────────┤
        │                              │                    │
        ▼                              ▼                    ▼
┌───────────────────┐       ┌───────────────────┐  ┌─────────────────────────┐
│ 4A. CI / EXECUTION│       │ 4B. PACKAGE-STATE │  │ 4C. REPOSITORY          │
│ EVIDENCE          │       │ EVIDENCE          │  │ INTELLIGENCE            │
│ static + runtime  │       │ effective package │  │ code/build/test/usage   │
│ [CURRENT]         │       │ manager semantics │  │ [PARTIAL/FUTURE]        │
│                   │       │ + exact execution │  │                         │
│                   │       │ [INC 4/5 PATH]    │  │                         │
└───────────────────┘       └───────────────────┘  └─────────────────────────┘
        │                              │                    │
        └──────────────────────────────┼────────────────────┘
                                       ▼
┌──────────────────────────────────────────────────────────────┐
│ 5. BROAD IMPACT-CANDIDATE DISCOVERY                          │
│ "what material mechanisms might this update create here?"   │
│ deterministic signals + semantic reasoning + structure      │
│ [ACCEPTED RESPONSIBILITY] [OPEN DESIGN]                     │
└──────────────────────────────────────────────────────────────┘
                                       │
                          0..N technical candidates
                                       ▼
┌──────────────────────────────────────────────────────────────┐
│ 6. CANDIDATE GROUNDING / FORMULATION                         │
│ source evidence + mechanism + target propositions + lineage  │
│ [PARTIAL CURRENT] [SUPPORTED-MATURE]                        │
└──────────────────────────────────────────────────────────────┘
                                       │
                                       ▼
┌──────────────────────────────────────────────────────────────┐
│ 7. CANDIDATE-SPECIFIC APPLICABILITY                          │
│ established applicable / not applicable / unresolved /       │
│ conflicted + evidence/path coverage                          │
│ [PARTIAL CURRENT] [SUPPORTED-MATURE]                        │
└──────────────────────────────────────────────────────────────┘
                                       │
                                material gap/conflict?
                                  ┌────┴────┐
                                  │         │
                                 no        yes
                                  │         ▼
                                  │  ┌────────────────────────┐
                                  │  │ 8. INVESTIGATION       │
                                  │  │ choose discriminating  │
                                  │  │ evidence/check         │
                                  │  │ fixed first; bounded   │
                                  │  │ planner when justified │
                                  │  └────────────────────────┘
                                  │         │
                                  │         ▼
                                  │  evidence / observation
                                  │         │
                                  └────┬────┘
                                       ▼
┌──────────────────────────────────────────────────────────────┐
│ 9. CROSS-CANDIDATE + REPOSITORY-CONTEXT SYNTHESIS            │
│ applicable + eliminated + unresolved + conflicted candidates │
│ + candidate-discovery coverage + material context findings   │
│ [OPEN DESIGN] [SUPPORTED-MATURE]                            │
└──────────────────────────────────────────────────────────────┘
                                       │
                                       ▼
┌──────────────────────────────────────────────────────────────┐
│ 10. OVERALL EVIDENCE SUFFICIENCY + ACTION PERMISSION         │
│ action-specific prerequisites / residual uncertainty/policy  │
│ [CURRENT: ABSTAIN ONLY] [MATURE OPEN DESIGN]                │
└──────────────────────────────────────────────────────────────┘
                                       │
                                       ▼
┌──────────────────────────────────────────────────────────────┐
│ 11. MAINTAINER DECISION REPORT                               │
│ orient → evidence → applicability → CI limits → uncertainty  │
│ → next check / action explanation                            │
│ [PARTIAL CURRENT] [SUPPORTED-MATURE]                        │
└──────────────────────────────────────────────────────────────┘
                                       │
                                       ▼
                           HUMAN MAINTAINER DECISION

Cross-cutting across all stages:
IDENTITY / PROVENANCE / TRUST / REPLAY / SECURITY / EVALUATION
\`\`\`

---

# 4. Stage 1 — Admission and exact identity

## Responsibility

Establish the exact public decision object:

\`\`\`text
repository
+ Dependabot PR number
+ PR identity
+ base SHA
+ head SHA
+ changed files
+ evidence acquisition context
\`\`\`

The purpose is not merely routing.

Every later fact must know **which exact repository/revision/update** it describes.

## Current reality

**[CURRENT] [VERIFIED]**

\`investigate_public_pull_request()\` begins by acquiring:

1. pull-request identity;
2. exact changed files;
3. dependency-change analysis.

Current code preserves exact head/revision identity through downstream workflow and source evidence.

## Mature direction

**[SUPPORTED-MATURE]**

Track B strongly confirmed that stable identity is prerequisite for:

- graph reasoning;
- CI/runtime correlation;
- attestations;
- dependency submissions;
- static-analysis results;
- replay;
- cross-source evidence composition.

## Mechanism

Primarily deterministic.

No AI is justified here.

## AI role

None for authoritative identity.

AI may later explain identity mismatches, but it must not establish them.

## Proof boundary

\`\`\`text
accepted PR identity
!=
dependency update established

accepted PR identity
!=
evidence complete
\`\`\`

---

# 5. Stage 2 — Exact dependency transition and source context

## Responsibility

Determine:

\`\`\`text
which dependency?
old version?
proposed version?
which declaration/lock source owns the transition?
what exact source context applies?
\`\`\`

This stage converts a generic PR into an exact dependency-transition object.

## Current reality

**[CURRENT] [VERIFIED]**

Current source calls \`analyze_dependency_change(...)\` and returns either:

- a \`DependencyVersionChange\` plus typed source contexts; or
- an explicit \`DependencyChangeProblem\`.

Existing source-context work includes bounded requirements, pyproject/optional/dependency-group, and uv-lock semantics.

## Mature direction

**[SUPPORTED-MATURE]**

Independent research across Dependabot/Renovate/ORT/deps.dev strongly supports ecosystem-specific adapters and explicit distinction among:

- declaration;
- lock/resolution;
- installed/runtime state.

## Mechanism

Deterministic parser/ecosystem interpretation.

## AI role

No authority role.

Possible later assistance for exotic source formats is low priority and would require deterministic admission.

## Proof boundary

\`\`\`text
dependency transition established
!=
dependency used in target
!=
dependency installed in CI
!=
update technically relevant
\`\`\`

---

# 6. Stage 3 — Multi-source evidence acquisition

This stage is best viewed as **parallel evidence families**, not one sequential fetch routine.

---

## 6A. Target repository / source evidence

### Responsibility

Acquire exact head files needed by admitted analyses.

Examples:

- dependency source files;
- \`pyproject.toml\`;
- lockfiles;
- workflow definitions;
- Python-version declarations;
- future code/API usage files.

### Current reality

**[CURRENT]**

The application already acquires exact-head repository files on demand.

### Mature direction

**[SUPPORTED-MATURE]**

Keep acquisition demand-driven, but allow a broader repository-intelligence/query layer later.

### AI role

A future discovery model may request additional **read-only** source ranges/files through an admitted capability.

It does not select arbitrary authority merely by naming a path.

---

## 6B. GitHub Actions / CI evidence

### Responsibility

Acquire:

- exact-head workflow runs;
- jobs/steps;
- exact workflow definitions;
- runtime status/conclusion;
- evidence needed to correlate static definition with historical execution.

### Current reality

**[CURRENT] [VERIFIED]**

Current application:

\`\`\`text
get exact-head workflow runs
→ get jobs
→ fetch exact workflow file
→ evaluate dependency CI coverage
\`\`\`

Increment 1 added reusable step/exact-command execution evidence.

Increment 3 added bounded workflow/process environment and executable/config evidence required by the selected Route-A package-manager semantics.

### Mature direction

**[SUPPORTED-MATURE]**

Preserve both:

- static workflow definition;
- historical runtime observation.

Add optional richer runtime telemetry only when justified.

### Architecture competition

**[UNRESOLVED-COMPETITION]**

For future broad workflow CFG/dataflow:

\`\`\`text
extend custom parser/model
vs
CodeQL Actions as evidence producer
\`\`\`

Do not decide before E1 comparator.

---

## 6C. Package-index / release evidence

### Responsibility

Acquire exact old/proposed package-release information.

### Current reality

**[CURRENT]**

Current flow fetches:

- proposed release;
- old release when needed.

These feed artifact-serviceability analysis and upstream repository resolution.

### Mature direction

**[SUPPORTED-MATURE]**

Potential enrichers include:

- deps.dev;
- external package graph metadata;
- release artifacts;
- package behavior metadata.

These remain contextual evidence, not exact target runtime truth.

---

## 6D. Upstream repository / release interval evidence

### Responsibility

Establish:

\`\`\`text
package
→ upstream repository
→ crossed release interval
→ proposed-version tag/commit
→ authoritative upstream source
\`\`\`

### Current reality

**[CURRENT]**

The current application resolves:

1. upstream repository;
2. PyPI release index;
3. crossed release set;
4. exact proposed-version Git tag;
5. changelog path;
6. tagged changelog evidence;
7. authoritative upstream interval.

### Mature direction

**[SUPPORTED-MATURE] but [INCOMPLETE]**

Tagged changelog evidence remains useful.

Track C says it must not become the only mature upstream semantic source.

Future evidence producers may include:

- Griffe/API diff;
- direct old/new source diff;
- migration guides;
- upstream tests/examples;
- package behavior delta.

### Architecture competition

**[UNRESOLVED-COMPETITION]**

E2:

\`\`\`text
changelog only
vs
API/source diff
vs
combined
\`\`\`

---

## 6E. Runtime / process telemetry

### Responsibility

Observe actual process/network/file effects where static/runtime correlation is insufficient.

### Current reality

**[OPTIONAL-FUTURE]**

Current core uses GitHub-provided runtime/job/step evidence, not StepSecurity-like process telemetry.

### Mature direction

**[SUPPORTED-MATURE]**

Runtime instrumentation can be a first-class optional evidence producer.

It must remain distinct from:

- source configuration;
- historical normal logs;
- emulated execution;
- package-state success.

### Architecture competition

E3:

\`\`\`text
static inference
vs
instrumented direct observation
\`\`\`

Only activate when a real proposition needs it.

---

# 7. Stage 4 — Evidence normalization, provenance and reusable repository views

This stage is cross-cutting and should not be confused with impact reasoning.

## Responsibility

Convert heterogeneous evidence into typed, revision-bound, provenance-preserving representations.

Each material evidence item should eventually retain enough information to answer:

\`\`\`text
what is claimed?
which exact object/revision/environment?
which source?
which producer?
which transformation?
which observation method?
what coverage/completeness limitation?
\`\`\`

## Current reality

**[CURRENT] [ACCEPTED-CONTRACT]**

UpgradePilot already strongly implements typed evidence/problem states and exact identity/provenance across many domains.

It does not currently have one general evidence graph or universal repository-intelligence service.

## Mature direction

**[SUPPORTED-MATURE]**

Keep the domain-specific internal reasoning model.

Potentially add standards adapters for:

- CycloneDX;
- SPDX;
- in-toto/SLSA;
- GitHub attestations/dependency submission.

## Repository views

Possible future views:

\`\`\`text
CodeStructureView
BuildTestView
WorkflowView
DependencyView
SupplyChainView
DecisionEvidenceView
\`\`\`

**[EXPERIMENTAL] [UNRESOLVED-COMPETITION]**

Track C explicitly rejects building one universal graph by default.

First run E4.

## AI role

AI may query views.

AI does not define their trusted edges merely by asserting relationships.

---

# 8. Stage 5 — CI exercise / execution evidence

## Responsibility

Answer bounded questions such as:

- does a workflow statically consume the changed dependency source?
- was the relevant step correlated to the exact head run?
- is a specific command occurrence structurally eligible for positive execution inference?
- does the historical runtime support that exact command occurrence?

## Current reality

**[CURRENT] [VERIFIED]**

Implemented responsibilities include:

- workflow static parsing;
- dependency-consuming command analysis;
- static/runtime job/step correlation;
- exact-command execution evidence for admitted shell/execution profiles;
- preservation of unsupported/unresolved structures.

## Mature direction

**[SUPPORTED-MATURE]**

Keep exact-command proof as its own proposition family.

Possible future producer improvements:

- CodeQL CFG/dataflow;
- runtime telemetry;
- stronger provider-specific evidence.

## Important boundary

\`\`\`text
CI exercise
!=
dependency installed

dependency installed
!=
behavior exercised

behavior exercised
!=
compatibility proven
\`\`\`

---

# 9. Stage 6 — Effective package-manager semantics

## Responsibility

For one exact package-manager operation, establish independent effective semantic facts.

Current first Route-A facts are conceptually:

- manager/environment selection;
- installation destination;
- mutation/dry-run mode;
- direct requirement handling.

## Current reality

**[CURRENT] [VERIFIED]**

Increment 2:

- created shared package-manager operation declaration;
- created independent semantic facts/problems.

Increment 3:

- added bounded executable/interpreter evidence;
- exact-process environment evidence;
- persistent config/default closure;
- controlled fixture proving all four facts;
- preserved ordinary ambient cases as unresolved.

## Architecture

\`\`\`text
parser-neutral command
→ package-manager operation declaration
→ command line
→ process env
→ persistent config
→ manager default
→ independent semantic facts
\`\`\`

## Mature direction

**[INDEPENDENTLY SUPPORTED]**

Track C found this architecture sound.

## AI role

None for authoritative pip/uv precedence in the current design.

A model could help explain an unresolved semantic problem, but not decide a precedence fact.

---

# 10. Stage 7 — Runtime dependency-state proof

## Responsibility

Establish the bounded proposition:

> the exact proposed direct requirement is satisfied in the resolved package-state scope when the exact successful command completes.

## Current reality

### Evidence producers

**[CURRENT]**

The prerequisites now exist after Increment 3.

### Composer

**[SELECTED-NEXT] [ACCEPTED-CONTRACT]**

Increment 4 will compose:

\`\`\`text
exact dependency/source applicability
+ package-manager semantic facts
+ exact command execution
→ RequirementSatisfiedAtCommandCompletion
\`\`\`

with explicit unresolved/not-established results.

### Application integration

**[FUTURE ACCEPTED SEQUENCE]**

Increment 5 later carries this result through the normal investigation/application path.

## Mature direction

**[SUPPORTED-MATURE]**

Track C explicitly found no contradiction.

## Important claim limit

The witness does **not** establish:

- fresh install causality;
- exact wheel/artifact identity;
- later persistence;
- later import/use;
- test coverage;
- behavioral compatibility;
- maintainer action.

## Future alternate producer

**[OPTIONAL-FUTURE]**

Direct target-owned package-state observation may coexist with command-derived proof.

Do not force both into the same evidence-strength category.

---

# 11. Stage 8 — Broad technical impact-candidate discovery

This is the largest important mature responsibility not yet generally implemented.

## Responsibility

Given the exact transition plus relevant upstream/target evidence:

> what materially plausible dependency-update mechanisms should UpgradePilot evaluate for this repository?

Examples may include:

- API/signature changes;
- behavioral/default changes;
- import/module movement;
- Python/runtime support;
- package artifact/serviceability changes;
- dependency/resolution changes;
- build/install changes;
- configuration/tooling integration;
- package behavior/security changes;
- persisted-state changes;
- CI/action/tooling changes.

## Current reality

**[PARTIAL CURRENT]**

UpgradePilot currently has real mechanism-specific discovery/formulation for bounded families including:

- Python support drop;
- artifact serviceability.

It does **not** yet provide general candidate-discovery coverage.

## Mature direction

**[ACCEPTED-CONTRACT] [SUPPORTED-MATURE] [OPEN DESIGN]**

Track A and independent research converge on hybrid discovery:

\`\`\`text
deterministic structured signals
+
upstream source/API evidence
+
target repository structure
+
bounded semantic reasoning
→ structured technical candidates
\`\`\`

## AI role

This is one of the strongest justified AI roles.

Model may:

- interpret open-ended upstream changes;
- propose candidate mechanisms;
- connect semantic changes to repository structure;
- propose missing propositions.

Model may **not** establish:

- applicability;
- candidate-discovery completeness;
- action permission.

## Model context architecture

**[UNRESOLVED-COMPETITION]**

E5 compares:

- narrow typed projection only;
- progressive graph/search/raw-source access.

Track C currently favors progressive controlled access for broad discovery, while keeping authority separate.

---

# 12. Stage 9 — Candidate grounding / formulation

## Responsibility

Turn a discovered mechanism into a challengeable technical candidate.

A mature candidate should retain:

\`\`\`text
candidate identity
mechanism
dependency transition
source evidence
target scope
required propositions
possible applicability paths
provenance
lineage
known coverage limits
\`\`\`

## Current reality

**[PARTIAL CURRENT]**

The Python support-drop vertical slice already provides a concrete candidate/application model.

The artifact-serviceability branch provides another bounded mechanism.

## Mature direction

**[SUPPORTED-MATURE]**

Keep candidate formulation separate from applicability.

## AI role

AI may formulate candidate semantics from evidence.

Deterministic code must preserve source binding, identity and authority class.

## Strong current pattern

Existing support-drop extractor:

\`\`\`text
bounded trusted source window
→ model selects semantic candidate + source-line ID
→ deterministic exact source recovery
→ untrusted candidate result
→ later grounding/application logic
\`\`\`

**[CURRENT] [SUPPORTED-MATURE]**

This is a reusable architecture pattern, not necessarily the final context width for all discovery.

---

# 13. Stage 10 — Candidate-specific applicability and coverage

## Responsibility

For each candidate:

> does this mechanism actually apply to the exact target repository/revision/context?

Accepted states:

- established applicable;
- established not applicable;
- unresolved;
- conflicted.

Keep three coverage questions separate:

\`\`\`text
evidence coverage
path-model coverage
candidate-discovery coverage
\`\`\`

## Current reality

**[CURRENT PARTIAL] [ACCEPTED-CONTRACT]**

Python support-drop has real target relevance/applicability flow.

Artifact-serviceability has bounded target-environment/application evidence.

The general multi-mechanism engine is incomplete.

## Mature direction

**[SUPPORTED-MATURE]**

External reachability systems strongly support:

- explicit positive path evidence;
- asymmetry between positive and negative conclusions;
- unsupported/inconclusive states;
- analyzer coverage limitations.

## AI role

AI can help identify possible paths/propositions.

It should not self-establish completeness or non-applicability.

---

# 14. Stage 11 — Evidence-gap analysis and investigation

## Responsibility

When a material proposition remains unresolved/conflicted:

1. identify the **discriminating** missing evidence;
2. determine whether useful admissible evidence can be acquired;
3. select the next check;
4. execute/query through an authorized capability;
5. interpret the result;
6. update state;
7. stop when further evidence is unavailable, unsafe, non-discriminating or no longer decision-relevant.

## Current reality

### Fixed/mechanism-specific investigation

**[CURRENT PARTIAL]**

The Python support-drop path can select exact target Python declaration acquisition when needed.

### Bounded agent planner

**[EXPERIMENTAL] [PROJECT-CHOICE]**

Existing experiments support:

\`\`\`text
typed InvestigationSnapshot
→ model proposes one pre-bound action / stop / defer / unresolved
→ deterministic admission
→ read-only capability
→ deterministic interpretation
→ updated state
\`\`\`

The one-action catalog does **not** establish general planner value.

## Mature direction

**[SUPPORTED-MATURE]**

Fixed-first escalation:

\`\`\`text
fixed deterministic/semantic pipeline
→ gap remains?
→ bounded adaptive planner
→ rare generalist-agent escalation only if necessary
\`\`\`

## Architecture competitions

E6:

\`\`\`text
fixed action sequence
vs
bounded planner
\`\`\`

E7:

\`\`\`text
bounded planner
vs
generalist sandboxed agent
\`\`\`

## Agent authority

Agent may own:

- next-action proposal;
- evidence-gap diagnosis;
- search/navigation priority.

Agent must not own:

- source identity;
- authorization;
- mutation permission;
- evidence promotion;
- proof-strength upgrades;
- final maintainer action.

---

# 15. Stage 12 — Observation feedback and candidate refinement

## Responsibility

New evidence normally updates proposition state.

Sometimes new evidence shows that the **candidate model itself was wrong/incomplete**, requiring candidate refinement/supersession with lineage.

## Current reality

**[ACCEPTED-CONTRACT] [LIMITED CURRENT]**

Current product model preserves proposition updates and some intermediate lineage, but broad multi-candidate refinement is not a mature implemented subsystem.

## Mature direction

**[SUPPORTED-MATURE]**

Especially important once discovery uses models/graphs/agents.

Need to distinguish:

\`\`\`text
same candidate, new evidence
vs
candidate definition changed
vs
new distinct candidate discovered
\`\`\`

---

# 16. Stage 13 — Cross-candidate and repository-context synthesis

## Responsibility

Combine the full decision state without flattening it prematurely.

Mature synthesis should preserve:

\`\`\`text
candidate set
├─ applicable
├─ established not applicable
├─ unresolved
└─ conflicted

+ repository-context findings
+ candidate-discovery coverage
+ evidence limitations
+ CI/runtime proof boundaries
\`\`\`

## Current reality

**[OPEN DESIGN]**

The current application returns one \`PublicPullRequestInvestigation\` containing several typed branch results, but there is no mature general cross-candidate reasoning layer.

The current maintainer-action evaluator extracts residual uncertainty from the investigation, but it is not the final mature synthesis architecture.

## Mature direction

**[SUPPORTED-MATURE]**

This is one of the largest design gaps after current runtime-state work.

## AI role

Potential strong bounded role:

- prioritize findings;
- summarize relationships;
- explain why evidence matters;
- identify contradictions.

But machine-readable synthesis must remain reconstructable from validated evidence.

---

# 17. Stage 14 — Overall sufficiency, policy relationship and action permission

## Responsibility

Determine whether the total evidence state justifies one of Charter's action classes:

1. merge after normal review;
2. run targeted checks;
3. investigate or block;
4. defer;
5. abstain.

This is not the same as candidate applicability.

## Current reality

**[CURRENT] [PROJECT-CHOICE]**

Current \`maintainer_action.py\` admits only:

\`\`\`text
MaintainerAction = "abstain"
\`\`\`

and explicitly refuses to infer a more active action from technical results before positive prerequisites are proven.

This is a valid conservative current proof boundary.

## Mature direction

**[ACCEPTED PRODUCT OUTCOME] [OPEN DESIGN]**

Each non-abstention action needs its own positive prerequisite/permission semantics.

## AI role

Possible later bounded synthesis/phrasing.

A model must not simply choose a five-way action from raw evidence.

## Architecture competition

The existing PermissionEnvelope-style proposal remains:

**[UNRESOLVED-COMPETITION]**

Alternatives include:

- deterministic action projection;
- deterministic permission envelope + model selection/phrasing;
- interactive human decision support;
- empirically calibrated model-derived claim admission before action projection.

Do not decide before real action contracts and protected cases exist.

---

# 18. Stage 15 — Maintainer-facing decision report

## Responsibility

The output should help a maintainer understand and decide, not merely emit a label.

Track-B maintainer/review research suggests the report should follow:

\`\`\`text
ORIENTATION
What changed? Why might it matter?

EVIDENCE
What is actually established?

APPLICABILITY
How does it connect to this repository?

CI / RUNTIME INTERPRETATION
What did existing execution prove or not prove?

UNCERTAINTY / CONFLICT
What remains unknown?

NEXT DISCRIMINATING ACTION
Only when it can change the decision.

ACTION EXPLANATION
What is permitted/recommended and why?

CLAIM LIMITS
What this report does not establish.
\`\`\`

## Current reality

**[PARTIAL CURRENT]**

Current maintainer-action synthesis already preserves:

- decisive reasons;
- residual uncertainty;
- limitations;
- claim limits.

But action breadth and mature UX are not complete.

## Mature direction

**[SUPPORTED-MATURE]**

Optimize for:

- decision correctness;
- decision time;
- appropriate trust;
- inspectability;
- ability to detect a wrong AI claim;
- low attention/noise burden.

## Human authority

**[CHARTER CORE]**

The maintainer retains the final decision.

UpgradePilot does not auto-merge, approve or mutate repositories.

---

# 19. Optional future remediation subsystem

Remediation is **not part of the required core decision path**.

If later justified:

\`\`\`text
accepted decision/impact state
→ remediation planner
→ strategy selection
→ deterministic recipe/codemod OR grounded model patch
→ validator
→ new evidence
→ decision state reevaluated
\`\`\`

Potential Python research stack:

\`\`\`text
Griffe API diff
→ target localization
→ migration rule
→ LibCST codemod
→ tests/build/static validation
\`\`\`

Status:

**[OPTIONAL-FUTURE]**

Automatic external repository mutation remains outside the current Charter core.

---

# 20. Cross-cutting responsibility — provenance, replay and standards

## Current reality

**[CURRENT PARTIAL] [ACCEPTED-CONTRACT]**

Source/revision/provenance is central throughout the implementation.

Full persisted/replayable run architecture is later-route work.

## Mature direction

**[SUPPORTED-MATURE]**

Potential interoperability:

- CycloneDX;
- SPDX;
- in-toto/SLSA;
- Sigstore/GitHub artifact attestations;
- GitHub dependency submission;
- GUAC.

## Architecture

Preferred current Track-C hypothesis:

\`\`\`text
UpgradePilot internal domain model
↕ adapters
external standards
\`\`\`

not standards-native internal reasoning.

## Competition

E9 mapping experiment is non-blocking.

---

# 21. Cross-cutting responsibility — repository intelligence

## Purpose

Avoid repeatedly forcing models or bespoke components to rediscover stable repository structure.

Potential capability interface:

\`\`\`text
find_symbol
find_references
find_callers
find_importers
find_tests_for_component
find_build_owner
find_package_usage
find_ci_consumers
retrieve_exact_source
search_repository
get_project_instruction
\`\`\`

## Current reality

**[PARTIAL CURRENT]**

UpgradePilot has several domain-specific structural analyzers but no unified repository-intelligence boundary.

## Mature direction

**[EXPERIMENTAL] [SUPPORTED AS A NEED, NOT YET AS AN IMPLEMENTATION]**

Possible backends:

- current parsers;
- CodeQL;
- small custom graph;
- RIG-like build/test extractor;
- Sourcegraph;
- future graph store.

## Important design principle

Expose a stable **capability/query interface** before committing the product to a specific graph database.

---

# 22. Cross-cutting responsibility — AI / LLM participation map

The whole pipeline now makes AI placement clearer.

## AI should normally stay out of authoritative mechanical identity

Examples:

- exact repo/PR/SHA;
- exact package/version;
- path normalization;
- parser selection;
- command occurrence identity;
- package-manager precedence when deterministically modeled;
- evidence-source identity;
- action authorization.

## AI is strongest at open-ended semantics

### Role A — semantic evidence extractor

Current example:

\`\`\`text
release evidence
→ Python support-drop candidate
\`\`\`

### Role B — broad impact candidate discovery

Future high-value role:

\`\`\`text
transition + upstream + target context
→ plausible technical mechanisms
\`\`\`

### Role C — evidence-gap planner

Future/experimental:

\`\`\`text
unresolved proposition state
→ next discriminating admitted action
\`\`\`

### Role D — cross-candidate synthesis / explanation

Later:

\`\`\`text
validated evidence state
→ prioritized, understandable maintainer explanation
\`\`\`

### Role E — rare generalist investigation

Only for unusual long-tail cases that bounded capabilities cannot handle.

## Key authority rule

\`\`\`text
model may see / interpret / propose / prioritize / navigate
!=
model may self-authorize trusted state or action
\`\`\`

Track C keeps this rule while relaxing the idea that models must permanently see only tiny typed projections.

---

# 23. Cross-cutting responsibility — evaluation architecture

Every stage needs its own evaluation.

## Layer 1 — case/oracle quality

- exact revisions;
- exact transition;
- environment;
- oracle;
- oracle limitations;
- freshness;
- contamination.

## Layer 2 — evidence-producer correctness

- proposition precision;
- recall where measurable;
- provenance correctness;
- unsupported-state correctness.

## Layer 3 — candidate discovery

- relevant mechanism recall;
- unsupported candidate rate;
- discovery-coverage honesty.

## Layer 4 — applicability

- applicable / not-applicable / unresolved / conflicted correctness.

## Layer 5 — investigation

- evidence gain per action;
- unnecessary actions;
- stop correctness;
- authority violations;
- repeated-run stability.

## Layer 6 — semantic model

- source grounding;
- hallucination;
- abstention;
- risk/coverage;
- OOD behavior.

## Layer 7 — final report

- uncertainty preserved;
- citations/provenance;
- no unsupported action;
- concision/clarity.

## Layer 8 — maintainer outcome

- decision accuracy;
- time;
- external lookups;
- appropriate trust;
- ability to challenge the system;
- cognitive load.

## Current reality

**[CURRENT PARTIAL]**

Strong deterministic regression/product-simulation discipline exists.

Protected general AI/product evaluation is not mature.

## Mature direction

**[SUPPORTED-MATURE]**

A Python dependency-update protected corpus is a high-value future project artifact.

---

# 24. Current implementation overlay — what the application actually does today

At live main \`b16c984...\`, \`investigate_public_pull_request()\` executes approximately:

\`\`\`text
repo + PR
→ exact PR identity
→ changed files
→ dependency transition + source contexts

if transition established:

    → exact-head workflow runs/jobs
    → exact workflow definitions
    → dependency CI coverage

    → proposed package release
    → old package release

    ├─ artifact serviceability candidate
    │  → artifact serviceability impact
    │  → target artifact environment association
    │
    └─ upstream repository
       → release index
       → crossed release interval
       → proposed-version tag commit
       → changelog path
       → tagged changelog evidence
       → authoritative upstream interval
       → semantic support-drop extraction
       → grounded support-drop claim

           → Python-support impact candidate
           → pre-investigation applicability
           → if exact target Python evidence is discriminating:
                acquire exact target declaration
                → target relevance
                → final support-drop applicability

→ PublicPullRequestInvestigation
→ current maintainer-action synthesis
→ explained abstain
\`\`\`

### Important current gap relative to the accepted new work

Increment 1–3 runtime dependency-state capabilities are implemented in their domain modules, but the mature state proof is not yet in this application result.

The planned progression is:

\`\`\`text
Increment 4
→ compose command-derived package-state witness

Increment 5
→ integrate that witness into the normal investigation path
\`\`\`

This distinction must remain explicit when describing current product capability.

---

# 25. Mature responsibility overlay

The current application is a **vertical-slice implementation**, while the mature architecture is a **multi-mechanism decision system**.

The expansion is not:

\`\`\`text
keep adding one hardcoded mechanism forever
\`\`\`

It is:

\`\`\`text
current exact/evidence infrastructure
        │
        ├─ retain mechanism-specific analyzers where deterministic
        │
        ├─ add broad hybrid candidate discovery
        │
        ├─ add reusable repository intelligence where proven useful
        │
        ├─ add bounded investigation orchestration
        │
        ├─ add runtime evidence producers when justified
        │
        └─ add cross-candidate synthesis/action semantics
\`\`\`

---

# 26. Responsibility/status matrix

| # | Responsibility | Current status | Mature classification | AI/agent role |
|---|---|---|---|---|
| 1 | PR/revision identity | CURRENT | SUPPORTED-MATURE | none authoritative |
| 2 | dependency transition/source context | CURRENT | SUPPORTED-MATURE | none authoritative |
| 3 | target repository acquisition | CURRENT bounded | SUPPORTED-MATURE | model may request admitted reads later |
| 4 | CI workflow/run acquisition | CURRENT | SUPPORTED-MATURE | none authoritative |
| 5 | package release metadata | CURRENT | SUPPORTED-MATURE | optional summarization |
| 6 | upstream repository/interval/changelog | CURRENT | SUPPORTED but incomplete | semantic extraction useful |
| 7 | upstream source/API diff | not core current | SUPPORTED-MATURE candidate | model may interpret; deterministic diff preferred |
| 8 | static CI consumption | CURRENT | SUPPORTED-MATURE | minimal |
| 9 | static/runtime step correlation | CURRENT | SUPPORTED-MATURE | none |
| 10 | exact-command execution | CURRENT bounded | SUPPORTED-MATURE | none authoritative |
| 11 | effective package-manager semantics | CURRENT | SUPPORTED-MATURE | none authoritative |
| 12 | command-derived package-state composition | SELECTED-NEXT | SUPPORTED-MATURE | none needed |
| 13 | package-state application integration | later accepted sequence | SUPPORTED-MATURE | none needed |
| 14 | direct runtime package-state observation | absent | OPTIONAL-FUTURE / supported | agent may request admitted check |
| 15 | repository code/build/test intelligence | fragmented | EXPERIMENTAL substrate | model may query/navigate |
| 16 | broad impact-candidate discovery | partial mechanisms only | ACCEPTED responsibility / OPEN DESIGN | **strong AI role** |
| 17 | candidate formulation/grounding | partial current | SUPPORTED-MATURE | strong bounded semantic role |
| 18 | candidate applicability | partial current | SUPPORTED-MATURE | AI can propose paths, not authority |
| 19 | coverage reasoning | accepted/partial | SUPPORTED-MATURE | AI cannot manufacture completeness |
| 20 | evidence-gap selection | mechanism-specific current | SUPPORTED-MATURE | **bounded planner role** |
| 21 | adaptive investigation orchestration | experimental | EXPERIMENTAL | **agent role** |
| 22 | generalist repo investigation | absent | rare OPTIONAL escalation | broad agent only when justified |
| 23 | candidate refinement/lineage | limited | SUPPORTED-MATURE | AI may propose refinement |
| 24 | cross-candidate synthesis | open | SUPPORTED-MATURE / OPEN DESIGN | strong bounded synthesis role |
| 25 | overall sufficiency/policy | minimal | OPEN DESIGN | AI optional, not authority |
| 26 | maintainer action permission | CURRENT abstain-only | PROJECT-CHOICE → future 5 actions | model cannot self-authorize |
| 27 | maintainer report UX | partial | SUPPORTED-MATURE | phrasing/prioritization useful |
| 28 | persistence/replay | partial/future route | SUPPORTED-MATURE | none authoritative |
| 29 | standards/attestation adapters | absent | OPTIONAL / experimentally useful | none required |
| 30 | remediation/patch generation | outside current core | OPTIONAL-FUTURE | bounded model/agent possible |
| 31 | protected corpus/evaluation | partial | SUPPORTED-MATURE | used to evaluate AI/whole product |
| 32 | final maintainer decision | human | CHARTER CORE | human authority |

---

# 27. Where the current project is on this map

The main product workstream is currently deep inside **evidence strengthening**, not yet broad discovery/synthesis.

Approximate current position:

\`\`\`text
Stages 1–3
identity / transition / core acquisition
→ substantial real implementation

Stages 5–7
CI execution + package-manager semantics + package state
→ Increment 1–3 done
→ Increment 4 next
→ Increment 5 later

Stages 8–10
broad candidate discovery/formulation/applicability
→ first real vertical slices exist
→ mature general discovery remains open

Stage 11
investigation
→ mechanism-specific path exists
→ bounded planner experimental

Stages 13–15
cross-candidate synthesis / five-action policy / maintainer UX
→ largest later product gap
→ current implementation intentionally abstains
\`\`\`

This explains why current work can feel “low-level” while still being architecturally necessary:

> UpgradePilot is strengthening the evidence substrate needed before broader semantic discovery and action synthesis can truthfully rely on CI/runtime/package-state facts.

---

# 28. What Step 3 changes

Step 3 does **not** change the live Increment-4 route.

It changes our architectural visibility.

We now have a clear separation between:

### Layer A — trusted evidence infrastructure

Current main is building this deeply.

### Layer B — impact discovery/applicability

Partially implemented; major generalization work remains.

### Layer C — investigation orchestration

Mechanism-specific today; bounded agent experimental.

### Layer D — cross-candidate decision synthesis

Mostly open.

### Layer E — maintainer decision experience

Partially implemented; mature UX/evaluation open.

### Cross-cutting — repository intelligence / runtime / standards / evaluation

These become evidence-backed method choices, not random future technologies.

---

# 29. Immediate implications for Increment 4

Step 3 confirms the current next cycle should stay narrow and truthful.

Increment 4 should own only:

\`\`\`text
existing exact dependency/source evidence
+
existing semantic facts
+
existing exact-command execution evidence
→ command-completion requirement-state witness/problem
\`\`\`

It should **not** absorb:

- CodeQL;
- graph infrastructure;
- broad impact discovery;
- AI planning;
- runtime telemetry;
- action synthesis;
- standards export.

But its result should preserve:

- exact identity;
- producer/provenance;
- command-completion boundary;
- command-derived inference status;
- limitations needed by later consumers.

That keeps the witness composable into the mature map.

---

# 30. Architecture experiments and where they belong

The Track-C experiment queue now has explicit pipeline owners.

| Experiment | Pipeline owner / trigger |
|---|---|
| E1 CodeQL Actions comparator | Stage 5 — before broad custom workflow CFG/dataflow expansion |
| E2 Griffe/API diff | Stage 8 — before mature upstream candidate discovery |
| E3 runtime telemetry | Stage 5/7/11 — when static evidence leaves a decision-critical runtime gap |
| E4 small RIG/multi-view graph | Stage 4/15 — when repeated structural queries justify repository intelligence |
| E5 raw-source vs typed model context | Stage 8 — before broad discovery model adoption |
| E6 fixed vs bounded planner | Stage 11 — before planner adoption |
| E7 planner vs generalist agent | Stage 11 — only long-tail repository cases |
| E8 calibrated model authority | Stage 9/10/13 — after protected semantic corpus exists |
| E9 standards mapping | cross-cutting provenance/export — non-blocking |
| E10 maintainer study | Stage 15 — once report/action surface stabilizes |

This prevents experiments from becoming disconnected technology exercises.

---

# 31. Learning-by-doing exposure map

The same pipeline provides a coherent engineering-learning path.

### Current / near-term actual experience

Already strong or actively developing:

- Python typed domain modeling;
- GitHub API integration;
- GitHub Actions parsing/runtime correlation;
- package-manager semantics;
- evidence/provenance design;
- deterministic testing;
- local LLM structured extraction;
- bounded agent planning experiments;
- governance / agent skills / project memory.

### High-value future hands-on experiments tied to real responsibilities

- CodeQL / QL / CFG/dataflow;
- Griffe + LibCST;
- RIG-style graph design;
- GUAC + GraphQL + SBOM standards;
- SLSA/in-toto/Sigstore;
- runtime CI telemetry;
- calibration/risk-coverage;
- agent trajectory evaluation;
- OpenHands comparator;
- reproducible dependency-update evaluation corpus.

The rule remains:

\`\`\`text
research
!=
hands-on experiment
!=
project integration
!=
validated/operated experience
\`\`\`

---

# 32. Step-3 architecture conclusion

The mature UpgradePilot organism is now visible without committing prematurely to one framework:

\`\`\`text
EXACT UPDATE IDENTITY
→ MULTI-SOURCE EVIDENCE
→ PROVENANCE / NORMALIZATION
→ REPOSITORY + CI + PACKAGE-STATE INTELLIGENCE
→ BROAD IMPACT DISCOVERY
→ CANDIDATE GROUNDING
→ APPLICABILITY / COVERAGE
→ TARGETED INVESTIGATION
→ OBSERVATION FEEDBACK
→ CROSS-CANDIDATE SYNTHESIS
→ ACTION-SPECIFIC SUFFICIENCY / PERMISSION
→ MAINTAINER DECISION REPORT
→ HUMAN DECISION

with:
deterministic authority where computable
+ bounded semantic models where meaning is open-ended
+ bounded agents where next evidence action is state-dependent
+ runtime observation where inference is insufficient
+ explicit unresolved state everywhere evidence is inadequate
+ protected evaluation over the full path
\`\`\`

The important architectural statement is:

> **UpgradePilot is not an agent, graph, LLM, static analyzer, package-state prover, or dependency bot. Those are possible methods/evidence producers inside a larger evidence-backed maintainer decision system.**

---

# 33. Step status

\`\`\`text
Track A
  Step 1   limitation inventory                       COMPLETE
  Step 2A  project-conditioned classification        COMPLETE

Track B
  external/de-anchored research                      COMPLETE
  Tier-1 #01–#07                                    COMPLETE
  Step 2B-X independent architecture refresh         COMPLETE

Track C
  Step 2C adversarial reconciliation                 COMPLETE

Step 3
  whole-pipeline architecture map                    COMPLETE

Next
  Step 4 reconcile this map with existing
  UpgradePilot AI/LLM/agent experiments              READY
\`\`\`

Step 4 should not redo the broad research.

It should take the AI/agent components that already exist or are proposed—support-drop extractor, EvidenceGapPlanner, LangGraph experiment, LLM-assisted synthesis proposal—and place each one against the exact Step-3 responsibility it is supposed to own, then classify:

- already correctly placed;
- too narrow but valid;
- premature;
- redundant with stronger non-AI tooling;
- missing comparative evidence;
- should be expanded;
- should remain experimental;
- should be retired/deferred.
