# Static Shell / Direct-Install False-Positive Recognition — Working Memory

**Date:** 2026-09-13  
**Session status:** ACTIVE  
**Primary mode:** Learning-by-Doing + Planning/Design — Phase A design investigation  
**Selected parent plan:** [`../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`](../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md)  
**Previous:** [`2026-09-12_exact-revision-requirements-constraints-evidence-coherence.md`](2026-09-12_exact-revision-requirements-constraints-evidence-coherence.md)

## Starting point

The preceding exact-revision requirements/constraints provenance cycle is closed A→E. Its provider-owned changed-file snapshot fence was implemented and validated with:

```text
13 focused provider tests green
15 nearby regressions green
566 full deterministic tests green
```

The next selected correctness responsibility is the remaining confirmed static shell/direct-install false-positive recognition defect already retained by the parent synthesis journey.

This selection follows the current priority discipline:

```text
wrong / overstated evidence
before
broader evidence production or action expansion
```

Runtime correlation can strengthen a static dependency-consumption premise by proving that the containing workflow step ran successfully. It therefore becomes more important that the static premise itself not be a false positive.

## Confirmed failure shape retained from prior investigation

The earlier controlled investigation reproduced examples such as:

```text
pip install -r requirements-dev.txt
→ observed

pip install wheel
→ not_observed

pip install wheel # -r requirements-dev.txt
→ observed — false positive

echo "pip install -r requirements-dev.txt"
→ not_observed

echo "note; pip install -r requirements-dev.txt"
→ observed — false positive
```

These examples are now treated as symptoms of a broader command-semantics problem rather than as the complete implementation horizon.

## Phase A structure for this responsibility

Ali explicitly asked to keep the overall A→E cycle intact while subdividing this consequential design stage enough to reason properly:

```text
A-1 — preserve/reframe the real correctness problem and current implementation/owner trace
A-2 — investigate and compare credible architectural options, including higher-cost options when they may reduce future correction debt
A-3 — Ali + AI decide the selected design together, record the decision/proof boundary, and formally close Phase A
```

This is an explicit exception to the normal preference to finish one stage in one or two shots. It is not a reusable nested-cycle pattern.

## A-1 — PROBLEM / OWNER REFRAME — COMPLETE

A-1 is read-only. No product source or test mutation has occurred.

### User correction that changed the design horizon

Ali rejected a too-narrow interpretation of proportionality. The corrected principle for this responsibility is:

> Implementation complexity and migration cost are costs to weigh, not vetoes. Prefer the design that is professionally balanced across correctness, supported product breadth, maintainability, migration cost, future repair cost, and proof strength. A higher-cost change is justified when evidence shows that a smaller repair would preserve a weak foundation and likely create more expensive repeated corrections later.

This is consistent with `JUST-003` / proportionality: “simpler” means the simplest design that adequately satisfies the admitted responsibility and proof boundary, not the fewest changed lines today.

### Current source path and ownership trace

The shell-like command proposition is currently established more than once:

```text
GitHub workflow run scalar
→ RunStepDefinition.command.text

→ dependency/workflow_context.bounded_shell_segments(...)
   → direct_install.observe_direct_installation_declaration(...)
   → environment_selection.observe_project_environment_selection(...)

→ ci/workflow_commands._shell_segments(...)
   → project-environment segment-index validation
   → direct package invocation detection / source ordering
```

This matters because `segment_index` is carried across layers as static source identity/order. If dependency observers and CI composition use different segmentation rules, the same integer can refer to different command fragments even when each local parser appears internally correct.

Under Core `JUST-004`, that proposition should have one earliest sufficient owner unless a later layer has an independent reason to reconstruct it.

### Shared dependency segmentation owner

`src/upgradepilot/dependency/workflow_context.py` currently owns:

```python
bounded_shell_segments(command)
```

implemented as a textual split over:

```text
&&
||
;
newline
```

It is deliberately not a shell AST and currently has no quote/comment awareness.

### Direct requirements installation

`src/upgradepilot/dependency/direct_install.py` consumes `bounded_shell_segments(...)`, recognizes a pip-install-looking prefix, then searches the whole candidate segment for `-r` / `--requirement`.

Therefore:

```text
pip install wheel # -r requirements-dev.txt
```

remains one segment, starts like a pip install, and the requirements-file matcher can see the commented `-r` payload. The comment is therefore promoted into positive installation semantics.

Quoted separator data creates a different failure:

```text
echo "note; pip install -r requirements-dev.txt"
```

The textual semicolon split manufactures a second segment beginning with `pip install`, even though the semicolon is quoted data.

### Project-environment selection is affected by the same lexical defect

`src/upgradepilot/dependency/environment_selection.py` also consumes `bounded_shell_segments(...)` before interpreting pip local-project and uv selector commands.

The module uses `shlex.split(..., posix=True)` after a candidate segment is selected, but that does not repair incorrect upstream segmentation and default `shlex.split` comment handling is not a general GitHub Actions shell model.

Consequently shapes such as:

```text
pip install wheel # -e .[dev]
uv sync # --group docs
```

can expose comment payload as meaningful arguments after the segment has already been admitted as a candidate command.

### CI composition duplicates the same textual splitter

`src/upgradepilot/ci/workflow_commands.py` has a separate private `_shell_segments(...)` with the same regex split.

It uses that duplicate for two material responsibilities:

1. validating that externally supplied project-environment evidence references a segment index inside the same static command segmentation;
2. locating direct changed-package invocation and preserving its segment index for same-job ordering/direct-exercise evidence.

Therefore a repair only in dependency `workflow_context.py` could create cross-layer disagreement. The duplicate CI splitter is not an independent semantic owner; it reconstructs the same static segment identity from the same command text.

It also has the same false-positive shape for direct invocation. For example, quoted/comment text containing a separator followed by `pytest ...` can be split into a manufactured segment beginning with `pytest`, which may become false direct-exercise evidence.

### Broader command-control-flow problem discovered after the initial lexical framing

The corrected A horizon also exposes a second class that is not solved merely by quote/comment-aware splitting:

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

The install command can be real source syntax yet not execute. Current runtime correlation is at the GitHub Actions user-defined step level; it can establish that the whole step completed successfully, not that every internal shell command executed successfully.

Current coverage logic can strengthen a supported static consumption when the containing correlated run step is completed/successful. Therefore the design must keep at least these propositions distinct:

```text
real command occurrence exists in static source
≠ command is guaranteed to execute on every successful path
≠ containing GitHub step completed successfully
```

This is directly consistent with Product Decision Model §9.2:

```text
workflow definition declares command X
!= command X executed
!= command X succeeded
```

and the rule that broader job/run success must not substitute for exact step/command correlation when the owned proposition requires it.

### Existing proof surfaces

`tests/test_direct_install_declaration.py` already protects ordinary direct requirements installs, working-directory precedence, dynamic/unresolved paths, a nonmatching requirements file, a simple quoted echo negative case, ordinary multi-segment ordering, and invalid dependency-source paths.

`tests/test_project_environment_selection.py` protects ordinary pip/uv selectors, dynamic/unresolved context, a simple echoed-pip negative, valid multi-segment indices, and malformed quoting.

`tests/test_workflow_dependency_evidence.py` and `tests/test_ci_runtime_correlated_dependency_coverage.py` provide the nearest composition/runtime proof surfaces: static positive consumption/direct-exercise evidence can flow into runtime-correlated CI evidence when the containing step is correlated and successful.

### Shell-dialect boundary

GitHub Actions does not have one universal shell grammar. The provider already preserves explicit step/job/workflow shell fields and `runs-on` static structure.

GitHub's documented built-in behavior materially includes:

```text
non-Windows unspecified → bash -e {0}, sh fallback
explicit bash           → bash --noprofile --norc -eo pipefail {0}
sh                      → sh -e {0}
Windows unspecified     → pwsh (PowerShell Desktop fallback on self-hosted if Core absent)
pwsh / powershell       → PowerShell script execution with GitHub-added failure handling
cmd                     → cmd.exe with no equivalent general fail-fast mode
python                  → python {0}
custom                   → command [options] {0} [more_options]
```

Therefore syntax family and execution profile are separate facts. For example, `shell: bash {0}` still uses Bash syntax, but it is a custom execution profile and does not inherit GitHub's built-in explicit-Bash `-eo pipefail` behavior.

A future command-analysis boundary should preserve this distinction rather than representing shell identity as one string.

### A-1 outcome

The original “Unix-like quote/comment-aware splitter” recommendation is **superseded as too narrow**.

The active design question is now:

> What shared command-analysis architecture gives UpgradePilot a trustworthy, maintainable basis for static command occurrence, ordering/control-flow confidence, and later step-level runtime strengthening across the materially relevant GitHub Actions shell domain, without attempting to execute arbitrary workflow programs?

## A-2 — ARCHITECTURE / OPTION INVESTIGATION — COMPLETE / READY FOR A-3

A-2 remained read-only. No product source/tests/specification/plan mutation occurred.

### Comparison dimensions used

1. correctness against the confirmed comment/quote failures;
2. ability to distinguish static command occurrence from execution certainty/control-flow;
3. shell-family breadth appropriate to the current product;
4. one shared source of command identity/order across dependency and CI layers;
5. long-term maintainability and future correction cost;
6. dependency/supply-chain/runtime cost;
7. migration impact on existing source contracts such as `segment_index`;
8. ability to fail conservatively on unsupported/ambiguous syntax;
9. testability and source traceability;
10. proportionality relative to UpgradePilot’s maintainer-decision evidence role.

### Option family 1 — enhanced handcrafted lexical scanner

A shared in-project scanner/state machine could handle quoting, escaping, comments and separators much more safely than the current regex.

Advantages:

- no new dependency;
- small initial runtime footprint;
- complete control over failure behavior;
- enough to fix the two original false positives.

But after A-1's broader control-flow discovery, this no longer looks like a durable primary architecture. To support Bash/sh + PowerShell + cmd and distinguish `&&`, `||`, branches, loops, pipelines, here-strings/heredocs, escapes and shell-specific comments, the scanner would evolve into a home-grown multi-language parser. The maintenance burden would move into UpgradePilot and every new shell edge would become our parser bug.

**A-2 assessment:** useful only as a tiny fallback/adapter utility; not preferred as the main command-analysis architecture.

### Option family 2 — Python `shlex`, bashlex, ShellCheck-style narrow tooling

`shlex` is useful Unix-shell lexical machinery and is already used locally, but it is not a Bash control-flow parser and does not model PowerShell/cmd.

`bashlex` produces a Bash AST but is Bash-only, GPLv3+, and its latest PyPI release is old relative to the current toolchain. It does not solve the multi-shell ownership problem.

ShellCheck provides strong shell analysis for shell-family scripts but is an external Haskell tool/process and does not provide a unified PowerShell/cmd story.

**A-2 assessment:** none supplies the balanced shared multi-shell foundation by itself.

### Option family 3 — shell-native parsers per family

PowerShell exposes an official parser through `System.Management.Automation.Language.Parser.ParseInput(...)`, returning a `ScriptBlockAst`, tokens and parse errors. This is semantically attractive for PowerShell.

However a shell-native strategy would likely become heterogeneous:

```text
Bash parser A
PowerShell SDK/runtime parser B
CMD parser C
```

with different installation/runtime assumptions and adapter behavior. There is also no equivalent simple official cross-platform CMD AST API that completes the set.

**A-2 assessment:** technically credible, especially for PowerShell, but not the best common substrate for UpgradePilot's Python package at this stage.

### Option family 4 — Tree-sitter parser family behind an UpgradePilot-owned IR

This is the strongest parser-substrate candidate found.

Current evidence as of 2026-09-13:

- `tree-sitter` Python runtime is current (0.26.0 released 2026-06-30), MIT, Python >=3.10, and provides current CPython 3.12 wheels;
- `tree-sitter-bash` is an established Tree-sitter-organization grammar (PyPI 0.25.1, MIT, Python >=3.10, active repository, Python bindings);
- `tree-sitter-pwsh` is much newer (PyPI 0.38.1 released 2026-05-16) but active, MIT, publishes Python ABI3 wheels, and its grammar explicitly covers commands, strings/interpolation, pipelines/chains, if/loops, try/catch and other control structures;
- `tree-sitter-batch` is also new (PyPI 0.11.1 released 2026-04-21) but active, MIT, publishes Python ABI3 wheels, and explicitly covers `IF`/`ELSE`, `FOR`, `GOTO`, command operators, quoting/variables and CMD comments;
- the Bash grammar is materially more mature than the newer PowerShell/CMD grammars, so grammar trust must be evaluated per family rather than inherited from Tree-sitter generally.

Tree-sitter's error-tolerant behavior is useful for untrusted workflow source: parse trees expose `ERROR` and `MISSING` nodes and a `has_error` signal. UpgradePilot can therefore refuse positive interpretation when parse errors overlap a material command/control-flow region instead of pretending the recovered tree is certainly correct.

Important limitation: a syntax tree is **not execution semantics**. Tree-sitter can tell us that a command occurs inside an `if`, chain, loop, pipeline, etc.; UpgradePilot must still decide what evidence strength that context earns.

**A-2 assessment:** best available common parsing substrate, provided parser-library ASTs remain behind an UpgradePilot-owned adapter/IR and positive evidence is guarded against grammar errors/unsupported structures.

### Direct grammar packages vs a broad language pack

A current `tree-sitter-language-pack` exists and is actively released, but it bundles a broad parser set under one package/maintainer. UpgradePilot needs only a few shell families.

**A-2 preference:** if Tree-sitter is selected, depend directly on the runtime plus the exact grammars we admit rather than importing a broad language pack. This keeps the dependency and supply-chain surface aligned with the actual product responsibility.

### Option family 5 — parser-backed syntax + UpgradePilot conservative semantic analysis

This is the strongest complete architecture, rather than Tree-sitter alone.

Conceptually:

```text
RunStepDefinition + workflow/job context
        ↓
resolve effective shell
        ↓
ShellContext
    syntax_family
    execution_profile
        ↓
shell-specific parser adapter
        ↓
UpgradePilot StaticCommandAnalysis IR
        ↓
command observers
    direct requirements
    project environment
    direct package invocation
        ↓
separate runtime-strengthening eligibility
        ↓
step-level runtime correlation only when the command relationship justifies it
```

The important design is **parse broadly, claim narrowly**:

- a real command inside conditional control flow may still be valid static declaration evidence;
- that same command does not automatically become runtime-supported merely because the containing GitHub step succeeded;
- unsupported or ambiguous execution relationships remain unresolved rather than erasing useful static source evidence.

This architecture prevents the original false positives while also addressing the deeper declaration-vs-execution boundary exposed by A-1.

**A-2 assessment:** current leading option for A-3.

### Option family 6 — runtime logs / command-level runtime evidence

GitHub provides job/step logs and optional debug logging, but ordinary logs are primarily diagnostic output. GitHub explicitly provides extra step/runner debug modes when normal logs lack enough detail. A repository owner/collaborator can enable those modes, but UpgradePilot cannot assume an arbitrary public PR run was produced with command tracing enabled.

Therefore logs are not a stable general command-execution ledger. Parsing ordinary logs for command execution would introduce new acquisition, formatting, redaction, shell-output and provenance responsibilities and can still be incomplete.

**A-2 assessment:** do not make runtime logs the primary repair. They may later become an independent stronger evidence source for selected investigations, but they do not remove the need for sound static command semantics.

### Option family 7 — deliberately narrow positive contract

A conservative positive contract remains necessary, but it should be **policy on top of richer parsing**, not the whole architecture.

For example, UpgradePilot can parse a broad class of Bash/PowerShell/CMD scripts and preserve command occurrences, while initially allowing runtime strengthening only for command/control-flow shapes whose relationship to step success is actually justified.

This avoids the two bad extremes:

```text
parse narrowly → repeatedly miss real project shapes
```

and

```text
parse broadly → overclaim execution semantics we do not possess
```

**A-2 assessment:** required as part of the selected evidence policy, not sufficient by itself as the parser architecture.

### Effective shell resolution findings

Current provider IR already preserves the material static inputs:

- workflow `defaults.run.shell`;
- job `defaults.run.shell`;
- step `shell`;
- job `runs-on` as a typed static value.

A shared resolver can therefore apply the same precedence pattern already used for working directories:

```text
step shell
> job defaults.run.shell
> workflow defaults.run.shell
> GitHub platform default when runner platform is statically established
```

Dynamic expressions or self-hosted/ambiguous runner labels can remain unresolved when they prevent default-shell determination.

A-2 identified a useful representation split:

```text
syntax_family
→ how the run script must be parsed

execution_profile
→ how GitHub invokes that syntax and what step-success implications may exist
```

Examples:

```text
shell: bash
→ syntax_family = bash
→ execution_profile = github_builtin_bash_pipefail

unspecified + literal ubuntu-latest
→ syntax_family = bash/sh-compatible
→ execution_profile = github_nonwindows_default_bash_e_with_sh_fallback

shell: bash {0}
→ syntax_family = bash
→ execution_profile = custom_shell_template

shell: pwsh
→ syntax_family = powershell
→ execution_profile = github_builtin_pwsh
```

This split is important because the same syntax can have different fail-fast/exit behavior.

### Internal representation direction

Do not expose Tree-sitter node types to dependency or CI evidence contracts. A parser library is implementation machinery, not product representation.

A likely UpgradePilot-owned shape is conceptually:

```text
StaticCommandAnalysis
    shell_context
    parse_state / problems
    command_occurrences[]

StaticCommandOccurrence
    stable source span / source order identity
    command form needed by observers
    raw source slice
    structural context
        top-level / chain / branch / loop / pipeline / nested / unsupported
    runtime-strengthening classification
        eligible / conditional-or-uncertain / unsupported
```

The exact fields/names remain an A-3 decision; this is not yet an implementation contract.

`segment_index` should no longer be independently reconstructed in multiple modules. A-3 must decide whether it is retained as a derived compatibility/source-order field or replaced by a stronger source-span/occurrence identity.

### Shell-family breadth for A-3

A-2 does **not** recommend a Unix-only architecture.

The materially relevant built-in shell families to consider for the parser architecture are:

```text
Bash / sh
PowerShell / pwsh
Windows cmd
```

Python and arbitrary custom interpreters are different language responsibilities. They should not be force-parsed as shells. However a custom GitHub shell template whose executable clearly belongs to a supported syntax family may still be parseable under that syntax family while retaining a distinct custom execution profile.

This gives broader static understanding without pretending that every interpreter is a shell.

### Runtime-strengthening conclusion

Parser-backed command recognition solves **where/what a real command is**. It does not prove **whether that command ran**.

The selected design should therefore create a distinct runtime-strengthening classifier rather than treating source order or `segment_index` as execution proof.

A-3 must choose the first admitted strength class. Credible examples include:

- sole/simple command step;
- selected final `&&`-style chains where shell semantics + whole-step success justify the relation;
- other parser-proven structures only when their execution implication is explicit;
- branches/loops/short-circuit alternatives/ambiguous parser regions remain static-only or unresolved for runtime strengthening.

The important decision is not maximum breadth in B; it is that future breadth can be added by extending one explicit semantic classifier rather than by inventing new regex rules in several consumers.

### A-2 comparative result

Current ranking for A-3 discussion:

```text
1. Tree-sitter shell parsers + UpgradePilot-owned command IR + conservative runtime-strengthening policy
   → strongest balance of correctness, breadth, maintainability and extensibility

2. Shell-native/heterogeneous parsers + common IR
   → high fidelity potential but higher environment/integration complexity and no clean CMD/common substrate

3. Shared handcrafted multi-shell parser/scanner
   → avoids dependencies but transfers a large, growing parser-maintenance burden to UpgradePilot

4. Narrow lexical scanner / local fixes
   → insufficient long-term foundation after the broader failure analysis

Runtime logs
   → potential later independent evidence source, not a substitute for static parsing
```

This ranking is evidence-informed but **not yet the accepted design**. A-3 is intentionally reserved for the joint decision.

### Architecture-cost reality

Selecting the leading option would be a consequential change:

- add parser runtime + admitted grammar dependencies to a currently small runtime dependency surface;
- introduce one shared command-analysis/IR owner;
- migrate direct-install, project-environment and CI direct-invocation consumers away from independent splitting;
- revisit the meaning/retention of `segment_index`;
- add shell resolution and parser-error policy;
- refine runtime-strengthening behavior;
- add multi-shell representative tests and broad regression proof.

Those costs are real. A-2's judgment is that they may be justified because the mechanism sits underneath several evidence producers and stronger runtime-correlated claims. The cost should be compared to repeated future parser corrections and evidence overclaim risk, not only to the two known fixtures.

### ADR / plan consequence

The existing parent synthesis plan remains sufficient; no new large plan is justified by A-2.

If A-3 selects a shared external parser substrate + new cross-module command IR, the decision is consequential and durable enough to justify a focused ADR covering:

- parser substrate and dependency choice;
- shared command-analysis ownership boundary;
- separation between parser syntax and UpgradePilot evidence semantics;
- parser error/unsupported behavior;
- shell-family admission strategy.

The ADR would own the accepted method; the active working memory would retain the investigation history and B handoff.

## A-3 — JOINT DESIGN DECISION — NEXT

A-3 will decide together:

1. whether the parser-backed hybrid is accepted or another option should win;
2. exact admitted shell families for the first B implementation;
3. effective-shell/syntax-family/execution-profile representation;
4. shared command-analysis owner/layer;
5. whether `segment_index` remains derived or is replaced/narrowed;
6. initial runtime-strengthening eligibility semantics;
7. exact parser-error/unsupported behavior;
8. dependency/ADR consequences;
9. B implementation/proof boundary and stop line.

Only after A-3 will Phase A be marked complete and B become eligible for explicit Build/Implement authorization.

## Learning-by-Doing granularity rule

Ali previously clarified the overall cycle rhythm:

> A→B→C→D→E are the real cycle stages. Do not recursively turn each stage into another elaborate sub-cycle. By default, finish each stage in one or two substantive rounds. Use more only when the situation genuinely demands it or Ali explicitly asks for smaller sub-steps.

A-1/A-2/A-3 are explicitly requested for this consequential design decision and should not become a reusable nested-cycle pattern.

## Stop line

Phase A remains read-only. Do not yet:

- modify product source/tests before A-3 selects the design and Build is explicitly authorized;
- choose an external parser merely because it is feature-rich or educational;
- reject a stronger design solely because migration/dependency cost is higher;
- claim support for a shell family without evidence that its parser/analysis boundary is sound enough;
- treat parser success as proof that a command executed;
- parse runtime logs/artifacts unless a later responsibility independently admits command-level runtime evidence;
- combine this responsibility with matrix/reusable-workflow expansion;
- add exact installed-version/wheel semantics;
- redesign Target composition;
- enable a non-abstention maintainer action;
- reopen the closed exact-revision provenance cycle without new regression evidence.

## Current Learning-by-Doing state

```text
Slice: static workflow-command semantic correctness and safe runtime strengthening

A — IN PROGRESS
    A-1 — COMPLETE
        problem/owner horizon reframed; narrow lexical-only repair superseded
    A-2 — COMPLETE
        architecture/tooling/control-flow/shell-family options compared; leading option identified
    A-3 — NEXT
        joint design decision + formal A closure

B — NOT STARTED
C — NOT STARTED
D — NOT STARTED
E — NOT STARTED
```

`UP-SKILL:upgradepilot-planning-design`  
`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-working-memory`
