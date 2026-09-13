# UpgradePilot Current Memory

**Last updated:** 2026-09-13  
**Authority:** sole owner of the live project position, current blockers, selected continuation, and current learning depth.

## Live position

- **Current responsibility:** static workflow-command semantic correctness and safe runtime strengthening for GitHub Actions dependency evidence.
- **Mode:** Learning-by-Doing — Phase A design/planning is complete. The next eligible stage is B/Build, but product source/tests remain read-only until Ali explicitly authorizes Build/Implement.
- **Selected parent plan:** `plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`.
- **Selected bounded implementation plan:** `plans/STATIC_WORKFLOW_COMMAND_ANALYSIS_AND_RUNTIME_STRENGTHENING_IMPLEMENTATION_PLAN.md`.
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

Phase A formally accepted:

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

### Bounded implementation/proof plan — ACCEPTED

Phase A-4 created:

`plans/STATIC_WORKFLOW_COMMAND_ANALYSIS_AND_RUNTIME_STRENGTHENING_IMPLEMENTATION_PLAN.md`

The plan is a single P2 consequential plan, not a plan family. It coordinates:

1. Tree-sitter runtime + grammar compatibility characterization before dependency ranges are fixed;
2. effective shell syntax-family/execution-profile resolution;
3. one parser-neutral UpgradePilot command-analysis IR;
4. Bash/sh, PowerShell/pwsh, and CMD/batch adapters;
5. direct-requirements migration;
6. project-environment migration;
7. CI package-invocation/shared command-identity migration;
8. deliberate `segment_index` retention/removal against actual current consumers;
9. explicit runtime-strengthening eligibility;
10. correction of same-step ordering/direct-exercise assumptions where source order is insufficient;
11. removal of obsolete duplicate splitters/fallback inference;
12. focused parser/observer proof → CI/runtime composition regressions → full deterministic proof.

The first required runtime-strengthening class is intentionally conservative: one cleanly parsed straightforward top-level command occurrence in a step with established syntax family and execution profile. Richer command/control-flow structures may be parsed and preserved as static evidence without receiving stronger runtime authority. Additional strengthening classes may be admitted only when shell-specific evidence proves the required implication.

Important plan gates:

- grammar trust is earned per shell family; Bash maturity does not automatically transfer to the newer PowerShell/CMD grammars;
- a grammar that fails the required characterization must remain unsupported/unresolved rather than falling back to textual splitting;
- parse errors that can affect a material command proposition cannot become `not_observed` merely for convenience;
- source span/occurrence identity becomes the canonical static-command identity; a source-order ordinal may remain only if independently justified and must not imply execution.

No product source/test implementation has occurred under this plan yet.

## Current Learning-by-Doing cycle

```text
Slice: static workflow-command semantic correctness and safe runtime strengthening

A — COMPLETE
    A-1 — COMPLETE
        problem/owner horizon reframed
    A-2 — COMPLETE
        architectures/tooling compared
    A-3 — COMPLETE / ACCEPTED
        ADR-0009 accepted
    A-4 — COMPLETE
        one P2 implementation/proof plan created and selected

B — NEXT / NOT STARTED
    requires explicit Build/Implement authorization

C — NOT STARTED
D — NOT STARTED
E — NOT STARTED
```

### Cycle granularity preference

Ali's default process preference remains:

> Treat A→B→C→D→E as the real cycle. Do not recursively turn each stage into another elaborate sub-cycle. By default, finish each stage in one or two substantive rounds; use more only when the situation genuinely requires it or Ali explicitly requests smaller sub-steps.

A-1/A-2/A-3/A-4 were an explicit exception for this consequential design responsibility.

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

- modify product source/tests until Ali explicitly authorizes B/Build;
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
