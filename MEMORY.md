# UpgradePilot Current Memory

**Last updated:** 2026-09-13  
**Authority:** sole owner of the live project position, current blockers, selected continuation, and current learning depth.

## Live position

- **Current responsibility:** static workflow-command semantic correctness and safe runtime strengthening for GitHub Actions dependency evidence.
- **Mode:** Learning-by-Doing + Planning/Design — Phase A-4 bounded implementation/proof planning. Product source/tests remain read-only until the plan exists and Build/Implement is explicitly authorized.
- **Selected parent plan:** `plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`.
- **Accepted method owner:** `docs/architecture/ADR-0009-parser-backed-static-workflow-command-analysis.md`.
- **Active working memory:** `working-memory/2026-09-13_static-shell-direct-install-false-positive-recognition.md`.
- **Previous working memory:** `working-memory/2026-09-12_exact-revision-requirements-constraints-evidence-coherence.md`.
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

## Current correctness cycle — static workflow-command semantic correctness

### Why this is next

The earlier static↔runtime CI bridge can strengthen static dependency-consumption evidence when a user-defined workflow step is correlated to factual completed/successful runtime evidence.

A wrong static command interpretation can therefore become stronger wrong evidence.

Controlled false positives included:

```text
pip install wheel # -r requirements-dev.txt
→ observed — false positive

echo "note; pip install -r requirements-dev.txt"
→ observed — false positive
```

Phase A also established a deeper control-flow problem:

```text
true || pip install -r requirements-dev.txt
```

or a command inside an `if` body can be real static source without necessarily executing even when the containing GitHub step succeeds.

Therefore the current responsibility is broader than quote/comment-aware splitting:

```text
real command occurrence
!= unconditional execution
!= successful containing step
```

### Accepted architecture — ADR-0009

A-1 reframed the problem and owner path. A-2 compared credible options. A-3 formally accepted:

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

Key accepted boundaries:

- parse broadly, claim narrowly;
- Tree-sitter/parser nodes remain implementation machinery behind an UpgradePilot IR;
- syntax family and GitHub execution profile are distinct;
- static command occurrence may remain useful when runtime execution is conditional/uncertain;
- step-level runtime success may strengthen an internal command only when static structure + execution profile justify it;
- parser/grammar uncertainty must remain conservative and must not fall back to the old regex splitter for positive evidence;
- Python shell mode and arbitrary custom interpreters are separate language responsibilities;
- current `segment_index` is migration pressure/source-order identity, not sufficient execution semantics.

ADR acceptance does not prove dependency installation, grammar behavior, source integration, or passing tests.

### Current A-4 planning responsibility

The accepted architecture crosses enough modules/dependencies/proof layers that one bounded **P2 consequential implementation plan** is now justified.

Recommended plan identity:

`plans/STATIC_WORKFLOW_COMMAND_ANALYSIS_AND_RUNTIME_STRENGTHENING_IMPLEMENTATION_PLAN.md`

The plan should coordinate, without re-specifying ADR-0009:

1. Tree-sitter runtime + grammar dependency integration and characterization gate;
2. effective shell context/resolution;
3. Bash/sh, PowerShell/pwsh, and CMD/batch parser adapters + UpgradePilot command IR;
4. direct-requirements migration;
5. project-environment selection migration;
6. CI direct-package invocation / source-order migration;
7. runtime-strengthening eligibility migration;
8. `segment_index` compatibility/removal decision against actual consumers;
9. focused multi-shell characterization/proof;
10. static→runtime composition/regression proof;
11. full deterministic regression proof;
12. explicit stop/prohibited scope.

One plan is sufficient; a plan family would be unnecessary ceremony unless A-4 discovers genuinely separate owners/gates that cannot be represented coherently in one plan.

## Current Learning-by-Doing cycle

```text
Slice: static workflow-command semantic correctness and safe runtime strengthening

A — IN PROGRESS
    A-1 — COMPLETE
        problem/owner horizon reframed
    A-2 — COMPLETE
        architectures/tooling compared
    A-3 — COMPLETE / ACCEPTED
        ADR-0009 accepted
    A-4 — NEXT
        write one P2 implementation/proof plan; then close Phase A

B — NOT STARTED
C — NOT STARTED
D — NOT STARTED
E — NOT STARTED
```

### Cycle granularity preference

Ali's default process preference remains:

> Treat A→B→C→D→E as the real cycle. Do not recursively turn each stage into another elaborate sub-cycle. By default, finish each stage in one or two substantive rounds; use more only when the situation genuinely requires it or Ali explicitly requests smaller sub-steps.

A-1/A-2/A-3/A-4 are an explicit exception for this consequential design responsibility.

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

Do not reopen them without concrete regression evidence. Current work may **narrow/refine what static command evidence is eligible for runtime strengthening** without reopening the already-closed static↔runtime identity-correlation mechanism itself.

## Later evidence bottlenecks retained

After static-command correctness is trustworthy, reassess rather than broadening automatically:

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
        ↓
CURRENT: parser-backed static workflow-command correctness
        ↓
re-audit / retire corrected trust restrictions
        ↓
select next decision-critical evidence bottleneck
        ↓
re-evaluate non-abstention action reachability
        ↓
admit one action path at a time through normal producer proof
```

## Current stop line

Do not yet:

- modify product source/tests before the A-4 plan is written and Build is explicitly authorized;
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
