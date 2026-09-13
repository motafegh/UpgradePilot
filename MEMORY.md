# UpgradePilot Current Memory

**Last updated:** 2026-09-13  
**Authority:** sole owner of the live project position, current blockers, selected continuation, and current learning depth.

## Live position

- **Current responsibility:** implement parser-backed static workflow-command semantic correctness and safe runtime strengthening through three bounded Learning-by-Doing cycles.
- **Mode:** Learning-by-Doing — **Cycle 1 / Phase A complete; B/Build is next and not yet started**. Product source/tests/dependency metadata remain unchanged until Ali explicitly authorizes Build/Implement.
- **Selected parent plan:** `plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`.
- **Selected bounded implementation plan:** `plans/STATIC_WORKFLOW_COMMAND_ANALYSIS_AND_RUNTIME_STRENGTHENING_IMPLEMENTATION_PLAN.md`.
- **Accepted method owner:** `docs/architecture/ADR-0009-parser-backed-static-workflow-command-analysis.md`.
- **Active working memory:** `working-memory/2026-09-13_static-workflow-command-three-cycle-implementation.md`.
- **Previous design/planning working memory:** `working-memory/2026-09-13_static-shell-direct-install-false-positive-recognition.md`.
- **Repository route:** continue directly on `main` unless Ali later requests otherwise.

The parent synthesis journey still prioritizes correctness/provenance reinforcement before broader evidence production or non-abstention maintainer-action expansion.

## Closed foundations retained

- exact run/job attempt coherence is closed and proven;
- bounded static↔runtime correlation is closed and proven within its admitted identity boundary;
- exact-revision requirements/constraints changed-file provenance is closed and proven, with the previous validation horizon of 13 focused + 15 nearby + 566 full deterministic tests green;
- the static workflow-command architecture/design phase is closed: ADR-0009 is accepted and the bounded P2 implementation/proof plan exists.

Do not reopen these without concrete contradictory/regression evidence.

## Accepted workflow-command architecture

ADR-0009 selects:

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
- syntax family and GitHub execution profile are distinct;
- Tree-sitter nodes remain implementation machinery behind UpgradePilot-owned contracts;
- static command occurrence does not establish command execution/success;
- parser/grammar uncertainty remains conservative and must not fall back to the old regex splitter for positive evidence;
- Python shell mode and arbitrary custom interpreters remain separate language responsibilities.

## Three-cycle implementation structure

### Cycle 1 — parser, shell-context, and shared command-analysis foundation — CURRENT

```text
Tree-sitter runtime + grammar compatibility/characterization
→ effective shell resolution
→ parser-neutral command IR
→ Bash/sh + PowerShell/pwsh + CMD/batch adapters
```

Current state:

```text
A — COMPLETE
B — NEXT / NOT STARTED
C — NOT STARTED
D — NOT STARTED
E — NOT STARTED
```

Cycle 1 A selected the following local build boundary:

- begin parser compatibility characterization from the trial set:
  - `tree-sitter==0.24.0`
  - `tree-sitter-bash==0.25.1`
  - `tree-sitter-pwsh==0.38.1`
  - `tree-sitter-batch==0.11.1`
- treat those as characterization versions, not final dependency ranges;
- resolve shell precedence as `step > job defaults > workflow defaults > safely established platform default`;
- keep `syntax_family` separate from `execution_profile`;
- infer hosted platform defaults conservatively and leave dynamic/self-hosted ambiguity unresolved;
- use one parser-neutral command IR with source span/order, literal/dynamic command atoms, and bounded structural-context tags;
- fail closed on material parser errors/unsupported structure; no positive regex fallback;
- characterize each grammar independently using simple commands, comments, quoted separators, multiple commands, short-circuit, conditionals, pipelines/nesting, malformed input, and Unicode/span fidelity;
- stop Cycle 1 before migrating direct-install, project-environment, CI invocation/segment identity, or runtime-strengthening consumers.

Ali's A ownership review is sufficient. The important refinements retained are:

```text
compatibility-first dependency selection
syntax family != GitHub execution profile
parser uncertainty must remain uncertainty
prove the shared producer before migrating consumers
```

### Cycle 2 — static evidence consumer migration and command identity correction — PLANNED

```text
shared command-analysis producer
→ direct requirements
→ project-environment selection
→ CI direct package invocation/composition
→ segment_index/source-order reconciliation
→ same-step static ordering correction
```

Cycle 2 begins only after Cycle 1 reaches E and the foundation is accepted.

### Cycle 3 — runtime-strengthening correctness, consolidation, and broad proof — PLANNED

```text
static command occurrence
+ structural/control-flow context
+ effective execution profile
+ exact correlated runtime step evidence
→ bounded runtime-strengthening eligibility
```

Cycle 3 owns runtime-strengthening policy, final obsolete-path removal, and focused → nearby → full deterministic proof.

## Immediate next action

When Ali authorizes Build/Implement, enter Cycle 1 B through the Build/Implement procedure.

B should begin with the parser dependency/grammar characterization gate before relying on Tree-sitter behavior in product source. Only after that gate is credible should B integrate final dependency ranges and implement the effective-shell resolver, shared command IR, shell adapters, and focused foundation tests.

## Current stop line

Until B is explicitly authorized, do not:

- modify product source/tests or dependency metadata;
- migrate direct requirements, project-environment, or CI package-invocation consumers;
- expose Tree-sitter nodes as product/domain contracts;
- treat parser success as execution proof;
- fall back to old regex splitters for positive evidence;
- parse runtime logs/artifacts;
- combine this work with matrix/reusable-workflow expansion, exact installed-version/wheel evidence, Target redesign, or maintainer-action enablement.

After all three static-command cycles close, re-audit the evidence path and select the next decision-critical bottleneck rather than broadening automatically.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-planning-design`  
`UP-SKILL:upgradepilot-working-memory`
