# ADR-0009 — Parser-Backed Static Workflow Command Analysis

**Status:** Accepted  
**Date:** 2026-09-13  
**Owner:** Ali Rajabi  
**Scope:** GitHub Actions run-command shell resolution, parser-backed command structure, shared command identity, and the boundary between static command evidence and step-level runtime strengthening

## Context

UpgradePilot currently interprets GitHub Actions `run:` text through bounded textual splitting in more than one layer.

The current path includes:

```text
RunStepDefinition.command.text
→ dependency/workflow_context.bounded_shell_segments(...)
   → direct requirements observation
   → project-environment selection

and independently

RunStepDefinition.command.text
→ ci/workflow_commands._shell_segments(...)
   → segment-index validation
   → direct changed-package invocation ordering
```

The current split over `&&`, `||`, `;`, and newline is not quote/comment aware. Controlled evidence has demonstrated false positives such as:

```text
pip install wheel # -r requirements-dev.txt
→ commented payload can become dependency-install evidence

echo "note; pip install -r requirements-dev.txt"
→ quoted separator payload can manufacture an install-looking segment
```

The design investigation also established that these are symptoms of a broader problem. A command can be genuine source syntax yet remain conditional or not execute on a successful path:

```text
true || pip install -r requirements-dev.txt
```

or:

```text
if false; then
    pip install -r requirements-dev.txt
fi
echo done
```

The existing runtime bridge correlates a user-defined GitHub Actions step to the factual runtime step and may observe the containing step as completed/successful. That is not automatically proof that every internal shell command executed or succeeded.

The accepted product semantics already require:

```text
workflow definition declares command X
!= command X executed
!= command X succeeded
```

The durable correction therefore needs a trustworthy shared command-structure boundary, not another local regex patch.

## Decision

### 1. Use parser-backed shell syntax rather than expanding handwritten splitters as the durable foundation

UpgradePilot will use Tree-sitter as the common parsing substrate for the admitted GitHub Actions shell-language families.

The intended architecture is:

```text
GitHub Actions RunStepDefinition
+ effective GitHub Actions shell context
        ↓
shell-family parser adapter
(Tree-sitter runtime + admitted grammar)
        ↓
UpgradePilot-owned static command IR
        ↓
   ┌──────────────┬────────────────────┬─────────────────────┐
   ▼              ▼                    ▼
direct        project-environment   CI package-invocation /
requirements selection              composition
        ↓
separate CI runtime-strengthening policy
```

Tree-sitter parser nodes are syntax machinery only. They do not become normal dependency/CI domain contracts.

### 2. Admit the normal GitHub Actions shell families relevant to the current product

The first architecture is designed for these shell-language families:

```text
Bash / sh
PowerShell / pwsh
Windows CMD / batch
```

The implementation may use separate Tree-sitter grammars behind one UpgradePilot adapter boundary.

Shell families are not assumed to have equal grammar maturity. Each adapter must earn admission through characterization/proof against representative real command shapes and the current UpgradePilot propositions.

A parser/grammar failure, syntax error affecting a material command region, or unsupported construct must remain conservative rather than fall back to the old textual splitter and guess positive evidence.

`python` shell mode is not treated as a shell-script dialect for pip/uv command interpretation merely because Python source may invoke subprocesses. Arbitrary custom interpreters likewise require separate evidence before they can enter this shell-command responsibility.

A custom GitHub Actions shell template that clearly uses an admitted shell executable may reuse that shell's **syntax family**, but its **execution profile** remains distinct and must not silently inherit GitHub's built-in wrapper guarantees.

### 3. Separate syntax family from execution profile

The design must distinguish at least these concepts:

```text
syntax family
→ how source text is parsed

execution profile
→ how GitHub invokes that script / what wrapper-level execution behavior is established
```

For example, a built-in Bash declaration and a custom `bash {0}` template may share Bash syntax while differing in wrapper flags and therefore in what step-level success can establish.

Effective shell resolution belongs with the GitHub Actions static-definition boundary because step/job/workflow shell declarations, runner/platform defaults, and custom shell templates are GitHub Actions semantics.

### 4. Introduce one UpgradePilot-owned static command IR

Dependency and CI consumers must not independently reconstruct shell segments from raw text.

The shared command representation must preserve only what current responsibilities need, including conceptually:

- exact source location/span or equivalent stable source identity;
- source order;
- command identity and safely recoverable arguments needed by current observers;
- shell family / parse state needed to interpret the occurrence;
- structural context sufficient to distinguish straightforward top-level execution from conditional/ambiguous control flow;
- enough relation information for downstream ordering questions without treating a flat integer ordinal as execution proof.

Exact class names, enums, and field names remain implementation-plan/source decisions.

Parser-library CST/AST nodes must stay behind the adapter boundary so grammar-library shape is not propagated throughout the product.

### 5. Retain static command occurrence separately from execution certainty

The command-analysis layer may establish that a real command occurrence exists in static source even when its runtime execution is conditional or cannot be established.

Conceptually:

```text
real pip install command exists in source
→ static declaration may be observed

command is inside conditional / short-circuit / otherwise uncertain flow
→ do not upgrade that occurrence to proven runtime execution merely because the containing step succeeded
```

This preserves useful static evidence without manufacturing runtime authority.

### 6. Step-level runtime success may strengthen only commands whose relationship is independently justified

Runtime correlation remains a CI-domain composition responsibility.

A successful correlated GitHub Actions step is evidence about that step. It may strengthen an internal command occurrence only when the selected static command structure **and** effective execution profile justify that inference.

The implementation must therefore not use:

```text
command found somewhere in run block
+ containing step success
→ command executed/succeeded
```

as a general rule.

Straightforward supported command shapes may earn stronger runtime evidence. Conditional, short-circuited, parser-ambiguous, execution-profile-ambiguous, or otherwise unsupported shapes remain static-only or unresolved at the stronger runtime proposition.

The exact first set of runtime-strengthenable shapes belongs to the bounded implementation plan and proof, not this ADR.

### 7. Treat current `segment_index` as migration pressure, not permanent architecture

Current `segment_index` values are useful source-order identifiers but are not sufficient execution semantics.

The migration should preserve required ordering/source identity while moving consumers toward the shared command IR. A flat segment ordinal must not remain the sole basis for claims such as "direct invocation definitely occurred after dependency consumption" when control-flow structure can invalidate that inference.

Exact compatibility/removal mechanics are implementation-plan decisions.

### 8. Do not use runtime logs as the primary correction mechanism

Job/step logs may later provide an independent evidence source for selected propositions, but ordinary logs are not assumed to be a complete structured command-execution ledger.

This decision therefore fixes static command interpretation first and keeps any future log/artifact evidence as a separate acquisition/provenance responsibility.

## Why this option was selected

### Compared with local regex or lexer patches

A local quote/comment repair would address the first reproduced fixtures but preserve duplicated command identity and would not solve conditional/short-circuit execution semantics.

Repeatedly extending a handwritten multi-shell scanner would increasingly make UpgradePilot responsible for maintaining partial Bash, PowerShell, and CMD parsers. That is not the simplest adequate long-term mechanism once the responsibility includes real command structure and control-flow context.

### Compared with standard-library `shlex`

`shlex` is useful Unix-shell lexical machinery but does not provide a sufficient multi-shell control-flow representation and cannot stand as general GitHub Actions shell semantics.

### Compared with shell-native heterogeneous parsers

Using each shell's native parser can offer excellent fidelity, but it creates materially different integration/runtime requirements across Bash, PowerShell, and CMD. A common parser substrate plus shell-specific grammars gives UpgradePilot one adapter pattern and one internal representation while still preserving dialect-specific syntax.

### Compared with runtime-log-first evidence

Command-level runtime evidence could strengthen some future propositions, but acquiring and interpreting logs introduces another evidence source with its own completeness, provenance, and observability limits. It does not remove the need for trustworthy static source interpretation.

### Balance / proportionality

The selected design is larger than a local bug fix, but the higher cost is justified because the same command-structure proposition is already shared across several evidence producers and now participates in runtime-strengthened CI evidence.

The project therefore applies this principle:

> implementation and migration cost are costs to weigh, not automatic vetoes; choose the smallest design that adequately satisfies the complete admitted responsibility and proof boundary, including foreseeable repeated-correction risk demonstrated by current evidence.

## Consequences

Positive:

- quoted/comment payload cannot be promoted merely by textual separator splitting;
- Bash/sh, PowerShell/pwsh, and CMD/batch can share one UpgradePilot command-analysis contract while retaining dialect-specific parsers;
- dependency and CI layers gain one source of command identity/order instead of duplicate splitters;
- static declaration evidence can remain useful even when runtime execution is uncertain;
- step-level runtime success no longer silently proves every internal command;
- future command-analysis additions can build on structured syntax instead of accumulating regex patches.

Costs:

- Tree-sitter and admitted grammar packages become material runtime dependencies once implementation begins;
- grammar versions/maturity become dependency-boundary risks requiring characterization tests;
- effective shell resolution and execution-profile modeling add implementation work;
- current `segment_index` consumers require coordinated migration;
- command-control-flow/runtime-strengthening rules require a new proof surface beyond parser correctness;
- parser success itself does not prove execution semantics, so UpgradePilot still needs a conservative analysis layer.

## Bounded scope / intentionally undecided

This ADR does not select:

- exact package version ranges;
- exact Python module/class names;
- exact command-IR field/enum names;
- a complete Bash, PowerShell, or CMD execution simulator;
- arbitrary custom interpreter support;
- Python-source subprocess analysis;
- complete path-sensitive shell control-flow evaluation;
- arbitrary variable expansion or environment simulation;
- exact first list of command structures eligible for step-success runtime strengthening;
- log/artifact parsing;
- matrix/reusable-workflow expansion;
- exact installed dependency version/wheel evidence;
- maintainer-action enablement.

Those belong to the implementation plan, future evidence responsibilities, or later architecture only when admitted.

## Reassessment triggers

Reassess this decision if evidence shows that:

- Tree-sitter runtime/grammar packaging creates unacceptable installation or platform constraints;
- a selected grammar cannot reliably parse the representative GitHub Actions command shapes UpgradePilot needs;
- maintaining three grammar adapters proves more costly or less trustworthy than another common mechanism;
- the command IR becomes too weak to express repeated downstream propositions without leaking parser-specific nodes;
- step-level runtime strengthening remains materially unsound even for the bounded first supported structures;
- command-level runtime evidence becomes available with sufficient identity/completeness to justify a different proof architecture;
- a second CI provider creates genuinely provider-neutral command-analysis semantics worth extracting from the GitHub-owned boundary.

## Evidence and related owners

- [`ADR-0008-bounded-static-github-actions-workflow-definition.md`](ADR-0008-bounded-static-github-actions-workflow-definition.md) — accepted GitHub Actions static workflow-definition IR and static/runtime separation.
- [`../specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md`](../specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md) — `OBS-001`, `STATE-001`, `JUST-003`, `JUST-004`, and related trust/ownership invariants.
- [`../specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md`](../specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md) — declaration/configuration evidence versus runtime execution/success semantics.
- [`../specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md`](../specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md) — variable-input/generalization acceptance boundary.
- [`../../working-memory/2026-09-13_static-shell-direct-install-false-positive-recognition.md`](../../working-memory/2026-09-13_static-shell-direct-install-false-positive-recognition.md) — A-1/A-2 investigation, alternatives, tooling evidence, and joint selection provenance.

Implementation proof, dependency installation, grammar behavior, tests, and live continuation remain owned by source/tests/commands/evidence and `MEMORY.md`, not by this ADR.
