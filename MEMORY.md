# UpgradePilot Current Memory

**Last updated:** 2026-09-13  
**Authority:** sole owner of the live project position, current blockers, selected continuation, and current learning depth.

## Live position

- **Current responsibility:** implement parser-backed static workflow-command semantic correctness and safe runtime strengthening through three bounded Learning-by-Doing cycles.
- **Mode:** Learning-by-Doing — **Cycle 1 / Phase A** orientation-design. Product source/tests remain read-only until Cycle 1 A closes and Ali explicitly authorizes Build/Implement.
- **Selected parent plan:** `plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`.
- **Selected bounded implementation plan:** `plans/STATIC_WORKFLOW_COMMAND_ANALYSIS_AND_RUNTIME_STRENGTHENING_IMPLEMENTATION_PLAN.md`.
- **Accepted method owner:** `docs/architecture/ADR-0009-parser-backed-static-workflow-command-analysis.md`.
- **Active working memory:** `working-memory/2026-09-13_static-workflow-command-three-cycle-implementation.md`.
- **Previous design/planning working memory:** `working-memory/2026-09-13_static-shell-direct-install-false-positive-recognition.md`.
- **Repository route:** continue directly on `main` unless Ali later requests otherwise.
- **Framework status:** ordinary-Python / LangGraph / LangChain comparison remains closed; no framework re-entry is justified.

The parent synthesis journey still prioritizes correctness/provenance reinforcement before broader evidence production or non-abstention maintainer-action expansion.

## Previous correctness cycle — exact-revision requirements/constraints provenance — CLOSED A→E

The requirements/constraints route previously could consume a mutable PR-files patch from head B while downstream source context still carried a frozen head A when the changed-file count stayed equal.

The provider-owned snapshot-fence repair is closed and validated:

```text
13 focused provider tests green
15 nearby regression tests green
566 full deterministic tests green
```

The admitted claim remains client-side observable snapshot coherence, not transactional/cryptographic linearizability. Exact commit comparison remains a stronger fallback only if future evidence justifies it.

Do not reopen that cycle without concrete regression evidence.

## Static workflow-command design/planning phase — CLOSED

The preceding design responsibility began from confirmed static false positives such as:

```text
pip install wheel # -r requirements-dev.txt
→ observed — false positive

echo "note; pip install -r requirements-dev.txt"
→ observed — false positive
```

It also exposed the deeper proposition boundary:

```text
real command occurrence
!= command guaranteed to execute
!= successful containing GitHub Actions step
```

The design phase completed:

```text
problem/owner reframe
→ architecture/tooling comparison
→ ADR-0009 accepted
→ P2 implementation/proof plan created
```

No product source/test implementation occurred during that design/planning phase.

### Accepted architecture — ADR-0009

```text
GitHub Actions RunStepDefinition
+ effective shell context
        ↓
Tree-sitter shell-family parser
        ↓
UpgradePilot-owned static command IR
        ↓
static dependency/project/invocation observers
        ↓
separate conservative runtime-strengthening policy
```

First architecture families:

```text
Bash / sh
PowerShell / pwsh
Windows CMD / batch
```

Retained boundaries:

- parse broadly, claim narrowly;
- Tree-sitter/parser nodes remain implementation machinery behind an UpgradePilot IR;
- syntax family and GitHub execution profile are distinct;
- static command occurrence may remain useful when runtime execution is conditional/uncertain;
- step-level runtime success may strengthen an internal command only when static structure + execution profile justify it;
- parser/grammar uncertainty must remain conservative and must not fall back to the old regex splitter for positive evidence;
- Python shell mode and arbitrary custom interpreters remain separate language responsibilities;
- current `segment_index` is migration pressure/source-order identity, not sufficient execution semantics.

ADR acceptance does not prove dependency installation, grammar behavior, source integration, or passing tests.

## Selected implementation plan — three-cycle execution structure

The durable implementation/proof plan remains one artifact:

`plans/STATIC_WORKFLOW_COMMAND_ANALYSIS_AND_RUNTIME_STRENGTHENING_IMPLEMENTATION_PLAN.md`

For execution and Learning-by-Doing, its coordinated responsibilities are grouped into **three top-level A→E cycles** rather than one giant cycle or many tiny cycles.

### Cycle 1 — parser, shell-context, and shared command-analysis foundation — CURRENT

```text
Tree-sitter runtime + grammar compatibility/characterization
→ effective GitHub Actions shell context resolution
→ parser-neutral UpgradePilot command-analysis IR
→ Bash/sh + PowerShell/pwsh + CMD/batch adapters
```

Purpose: establish and prove the shared producer/foundation before any downstream command observer migrates.

Current state:

```text
A — NEXT / NOT STARTED
B — NOT STARTED
C — NOT STARTED
D — NOT STARTED
E — NOT STARTED
```

Cycle 1 A should resolve only the remaining local implementation questions: exact compatible parser/grammar dependency set, effective-shell ambiguity/default rules, smallest IR fields required by current consumers, adapter error/admission behavior, focused characterization matrix, and Cycle 1 Build stop line. It must not reopen ADR-0009 absent new contradictory evidence.

### Cycle 2 — static evidence consumer migration and command identity correction — PLANNED

```text
shared command-analysis producer
→ direct requirements
→ project-environment selection
→ CI direct package invocation / composition
→ segment_index/source-order reconciliation
→ same-step static ordering correction
```

Purpose: move all current static consumers onto one command identity/structure source and close the known comment/quoted-payload false-positive class without retaining duplicated normal-path splitters.

Cycle 2 begins only after Cycle 1 E confirms the foundation is sufficient.

### Cycle 3 — runtime-strengthening correctness, consolidation, and broad proof — PLANNED

```text
static command occurrence
+ structural/control-flow context
+ effective execution profile
+ exact correlated runtime step evidence
→ bounded runtime-strengthening eligibility
```

Purpose: ensure whole-step runtime success strengthens only justified internal command occurrences, consolidate/remove obsolete inference routes, then perform focused → nearby → full deterministic proof and return to the parent synthesis journey.

The first required positive strengthening class remains conservative:

```text
one cleanly parsed straightforward top-level command
+ established syntax family
+ established execution profile
+ exact correlated completed/successful runtime step
→ eligible for the currently admitted stronger runtime proposition
```

Conditional, short-circuited, parser-ambiguous, and execution-profile-ambiguous occurrences remain static-only or unresolved at the stronger runtime proposition.

## Why three cycles

Three cycles are the selected proportional execution structure:

```text
one giant cycle
→ too much migration/proof risk before reassessment

many tiny cycles
→ fragmented implementation and excess ceremony
```

The three boundaries reflect real engineering ownership:

1. establish a trustworthy producer/foundation;
2. migrate static consumers onto it;
3. compose runtime authority only after static semantics are trustworthy.

Each cycle's E is a genuine reassessment gate; later cycles are not automatic if evidence changes the selected implementation boundary.

## Cycle granularity preference

Ali's default process preference remains:

> Treat A→B→C→D→E as the real cycle. Do not recursively turn each stage into another elaborate sub-cycle. By default, finish each stage in one or two substantive rounds; use more only when the situation genuinely requires it or Ali explicitly requests smaller sub-steps.

The previous A-1/A-2/A-3/A-4 breakdown was an explicit exception for the consequential architecture decision. The three implementation cycles now return to the normal A→E rhythm.

## Maintainer-action synthesis baseline retained

The accepted synthesis semantics remain unchanged. The deterministic evaluator is still intentionally abstention-only:

```text
PublicPullRequestInvestigation
→ synthesize_maintainer_action(...)
→ MaintainerActionSynthesis(action="abstain")
```

No merge, targeted-check, investigate, block, or defer permission is implemented yet. Stronger technical evidence does not create action permission by itself.

## Closed CI foundations retained

- exact run/job attempt coherence remains closed and proven;
- bounded static↔runtime correlation remains closed and proven within its admitted identity boundary;
- exact-revision requirements/constraints changed-file provenance remains closed and proven.

Do not reopen them without concrete regression evidence. Current work may narrow/refine which static command evidence is eligible for runtime strengthening without reopening the already-closed static↔runtime identity-correlation mechanism itself.

## Later evidence bottlenecks retained

After all three static-command implementation cycles close, reassess rather than broadening automatically:

1. preserve an already-known CI consuming `job_key` into Target composition;
2. acquire exact runtime dependency-version/artifact evidence only for a precise selected proposition;
3. produce exact target wheel-compatibility evidence through a normal producer;
4. freshly discriminate CI acquisition-failure containment if decision-relevant;
5. broaden matrix/reusable/dynamic-name correlation only under real case/product pressure.

These are not all correctness defects. Conservative unresolved/unsupported behavior remains valid where UpgradePilot cannot safely establish a fact.

## Durable journey

```text
accepted synthesis semantics
+ abstention-only evaluator
+ exact-attempt CI identity
+ bounded static↔runtime correlation
+ exact-revision requirements/constraints provenance
+ ADR-0009 + implementation plan
        ↓
CURRENT: Cycle 1 — parser/shell/command-analysis foundation
        ↓
Cycle 2 — static consumer migration / command identity
        ↓
Cycle 3 — runtime strengthening / consolidation / broad proof
        ↓
re-audit / retire corrected trust restrictions
        ↓
select next decision-critical evidence bottleneck
        ↓
re-evaluate non-abstention action reachability
```

## Current stop line

During Cycle 1 A, do not yet:

- modify product source/tests or dependency metadata until Cycle 1 A closes and Ali explicitly authorizes Build;
- migrate direct requirements, project-environment, or CI package-invocation consumers before the shared foundation is sufficiently designed/proven;
- expose Tree-sitter nodes as ordinary product/domain contracts;
- treat parser success as command execution proof;
- silently fall back to old regex splitters when parser/grammar evidence is uncertain;
- claim equal grammar maturity without per-family characterization;
- parse job logs/workflow artifacts as part of this correction;
- combine this correction with matrix/reusable-workflow expansion;
- add exact wheel/version installation semantics;
- redesign Target composition;
- enable a non-abstention maintainer action;
- reopen the closed exact-revision cycle without new failing evidence.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-planning-design`  
`UP-SKILL:upgradepilot-working-memory`
