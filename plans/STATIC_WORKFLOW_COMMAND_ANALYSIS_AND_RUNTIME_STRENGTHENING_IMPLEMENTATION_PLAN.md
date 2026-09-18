# Static Workflow Command Analysis and Runtime Strengthening Implementation Plan

**Plan status:** Accepted bounded implementation/proof plan  
**Responsibility:** Implement ADR-0009's parser-backed static workflow-command architecture, migrate current command consumers to one shared command-analysis boundary, and prevent step-level runtime success from overstating internal command execution.  
**Parent journey:** [`OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`](OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md)  
**Architecture owner:** [`../docs/architecture/ADR-0009-parser-backed-static-workflow-command-analysis.md`](../docs/architecture/ADR-0009-parser-backed-static-workflow-command-analysis.md)

## 1. Bounded outcome

Replace the current duplicated textual command splitting used by dependency and CI observers with one parser-backed command-analysis responsibility that can distinguish real command occurrences from comments/quoted payload, preserve useful source/control-flow structure across admitted GitHub Actions shell families, and support conservative runtime strengthening only where the static command relationship and effective execution profile justify it.

The completed implementation must provide this trust shape:

```text
exact GitHub Actions run-step source
+ statically resolvable effective shell context
        ↓
shell-family parser adapter
        ↓
UpgradePilot-owned static command analysis
        ↓
shared command occurrence identity / source relation
        ↓
   ┌──────────────────┬──────────────────────┬─────────────────────┐
   ▼                  ▼                      ▼
direct requirements   project environment    CI package invocation
static declaration    static selection       / direct-exercise input
        ↓
separate runtime-strengthening eligibility
        ↓
step-level runtime evidence strengthens only justified command occurrences
```

Completion means the known comment/quoted-separator false positives cannot become positive dependency or package-exercise evidence, current valid ordinary command cases continue to work, shell-specific parsing is bounded and conservative, and successful runtime correlation cannot generally promote a merely present/conditional internal command into executed/succeeded evidence.

This plan coordinates implementation. It does not redefine ADR-0009, the Product Decision Model, or the parent maintainer-action synthesis semantics.

## 2. Applicable owners and constraints

Implementation must remain consistent with:

- [`../docs/architecture/ADR-0009-parser-backed-static-workflow-command-analysis.md`](../docs/architecture/ADR-0009-parser-backed-static-workflow-command-analysis.md) — accepted parser substrate, shared IR, shell-family boundary, and static/runtime separation;
- [`../docs/architecture/ADR-0008-bounded-static-github-actions-workflow-definition.md`](../docs/architecture/ADR-0008-bounded-static-github-actions-workflow-definition.md) — provider-owned GitHub Actions static workflow IR and static/runtime evidence separation;
- [`../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md`](../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md) — `STATE-001`, `PROOF-001`, `JUST-003`, `JUST-004`, evidence/failure distinctions;
- [`../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md`](../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md) — declaration/configuration evidence is not execution evidence and broader runtime success must not replace exact command-level proof where required;
- [`../docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md`](../docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md) — representative variation rather than fixture-specific fixes;
- [`../SECURITY.md`](../SECURITY.md) — public repository source is untrusted input and parser/resource behavior must remain bounded;
- [`../OPERATING_GUIDE.md`](../OPERATING_GUIDE.md) — proportional implementation, proof discipline, and Learning-by-Doing progression.

The accepted design principle for this responsibility is:

```text
parse broadly enough to understand the admitted source structure
+
claim only what the evidence relationship actually establishes
```

## 3. Entry evidence and current implementation pressure

Current source behavior includes:

```text
src/upgradepilot/dependency/workflow_context.py
→ bounded_shell_segments(...)
→ textual split on &&, ||, ;, newline

src/upgradepilot/dependency/direct_install.py
→ consumes those segments for requirements-file installation

src/upgradepilot/dependency/environment_selection.py
→ consumes those segments for pip/uv project-environment selectors

src/upgradepilot/ci/workflow_commands.py
→ independently reconstructs similar shell segments
→ uses segment indices for project-environment reconciliation and direct package invocation/order
```

Confirmed false-positive pressure includes:

```text
pip install wheel # -r requirements-dev.txt
→ must not become requirements-install evidence

echo "note; pip install -r requirements-dev.txt"
→ must not manufacture a pip-install command
```

The broader design pressure includes genuine but conditionally executed commands such as:

```text
true || pip install -r requirements-dev.txt
```

and:

```text
if false; then
    pip install -r requirements-dev.txt
fi
echo done
```

A clean syntax parse may establish that these commands exist in source; success of the enclosing GitHub Actions step does not by itself establish that those commands executed.

The previous exact-revision correctness cycle established the current broad deterministic baseline at 566 passing tests. That count is historical entry evidence only; later implementation must report its own current validation totals.

## 4. Allowed modification boundary

Expected implementation changes may include, where justified by the selected architecture:

- `pyproject.toml` — direct Tree-sitter runtime and admitted grammar dependencies;
- the GitHub Actions static-definition area under `src/upgradepilot/github/` — effective shell resolution and parser-backed command-analysis ownership;
- `src/upgradepilot/dependency/workflow_context.py` — removal/narrowing of obsolete command segmentation while retaining justified path/working-directory helpers;
- `src/upgradepilot/dependency/direct_install.py`;
- `src/upgradepilot/dependency/environment_selection.py`;
- `src/upgradepilot/ci/workflow_commands.py`;
- `src/upgradepilot/ci/dependency_exercise.py` or the narrow CI composition owner if runtime-strengthening semantics require correction;
- nearest focused tests and integration/regression tests;
- bounded verification tooling only if ordinary tests cannot make a material dependency/parser property inspectable;
- `MEMORY.md` and the active working-memory record for live progression/proof preservation.

New source files under the existing responsibility-based packages are permitted when they create the single accepted command-analysis owner or shell-specific adapters. Do not create a generic `common`, `utils`, or shell-execution framework merely for reuse.

No compatibility layer is required solely because current private/internal helpers exist. Retain compatibility only when a current admitted caller or real external contract independently requires it.

## 5. Explicitly prohibited scope

This plan does not authorize:

- executing arbitrary repository workflow scripts;
- building a GitHub Actions runner or universal shell interpreter;
- arbitrary GitHub expression evaluation;
- general matrix expansion, reusable-workflow execution, or dynamic-name correlation;
- runtime job-log/artifact parsing as the primary command-execution proof source;
- exact installed dependency version, selected wheel, or artifact-compatibility evidence;
- Target composition redesign unrelated to the command-analysis migration;
- non-GitHub CI providers;
- Python/Perl/Ruby or arbitrary custom-interpreter source analysis as shell commands;
- maintainer-action enablement beyond the current abstention-only baseline;
- reopening the closed exact-revision provenance repair absent new regression evidence.

If implementation exposes a separate material responsibility from this list, stop and return it to planning/selection rather than absorbing it silently.

## 6. Implementation sequence

### 6.1 Characterize and admit the parser dependencies

Before relying on parser behavior in product evidence, establish one compatible dependency set for Python 3.12 using direct packages rather than a broad language pack:

```text
tree-sitter
tree-sitter-bash
tree-sitter-pwsh
tree-sitter-batch
```

Characterization must establish, for each grammar used in the product path:

- installation/import compatibility with the selected Tree-sitter runtime;
- parser construction through the supported Python binding;
- representative command, comment, quote/string, separator/chain, and control-flow nodes needed by this responsibility;
- parse-error/recovery behavior relevant to conservative admission;
- source byte/point span fidelity needed for command occurrence identity;
- no unsupported assumption that all three grammars have equal maturity or node schemas.

Select bounded dependency version ranges only after this compatibility check. Do not pin versions merely because they were the latest during A-2 research. Record the exact selected versions/ranges in dependency metadata and proof evidence once characterized.

**Gate:** if one grammar cannot credibly support the required current propositions, do not invent a fallback textual splitter for that family. Preserve that family as unresolved/unsupported and reassess the adapter/dependency choice before broadening claims.

### 6.2 Implement effective shell context resolution

Create one GitHub Actions-owned resolver that determines the effective command syntax family and execution profile from the existing static workflow IR.

Apply GitHub Actions precedence:

```text
step shell
> job defaults.run.shell
> workflow defaults.run.shell
> platform default when statically established
```

The resolver must distinguish at least:

```text
syntax family
→ bash/sh | powershell | cmd | unsupported/unknown

execution profile
→ built-in/default GitHub wrapper semantics
  | custom shell template
  | unresolved/unsupported
```

Required conservative behavior:

- dynamic/expression-backed shell declarations remain unresolved when syntax family cannot be established;
- explicit admitted shell declarations can establish syntax even when runner platform is otherwise ambiguous;
- unspecified shell requires enough literal runner/platform evidence to apply a GitHub default safely;
- self-hosted/unknown/dynamic runner context must not be guessed into a platform default;
- custom templates whose executable clearly maps to an admitted family may reuse that syntax parser, but keep a distinct custom execution profile;
- Python and arbitrary custom interpreters remain outside shell-command interpretation.

Focused tests must cover precedence, hosted Linux/macOS/Windows defaults where statically knowable, dynamic ambiguity, explicit shell overrides, and custom-template separation.

### 6.3 Introduce the shared UpgradePilot command-analysis IR

Create one parser-neutral internal representation owned at the GitHub Actions/static-command boundary. Parser-library nodes must not escape into dependency/CI contracts.

The representation should preserve the smallest fields that current responsibilities earn, including:

- shell context / syntax family;
- parse/admission state and structured problems;
- one stable occurrence identity based on source span plus deterministic source order;
- raw source slice for traceability;
- statically recoverable command/executable identity and argument information needed by current observers;
- structural/control-flow context relevant to evidence strength;
- enough relationship information to answer supported source-order/path questions without pretending an ordinal is execution proof.

Do not freeze exact names from this plan when implementation evidence suggests a clearer representation. The invariant is more important than the class spelling.

Parser/admission states must distinguish at least:

```text
cleanly analyzable
unsupported shell/construct
material parse ambiguity/error
```

A parse error that overlaps or can materially affect candidate command structure must not silently degrade to `not_observed` or fall back to regex parsing.

### 6.4 Implement shell-family adapters behind the shared IR

Implement adapters for the admitted first-family set:

```text
Bash / sh
PowerShell / pwsh
CMD / batch
```

Each adapter maps grammar-specific CST structure into the same UpgradePilot command concepts. Do not require identical grammar node layouts.

Representative adapter proof must cover, where meaningful for that shell family:

- comments do not become arguments/commands;
- separators inside strings/quoted payload do not manufacture commands;
- ordinary multiple top-level commands preserve source order;
- conditional/short-circuit structures remain structurally distinguishable from straightforward top-level commands;
- pipelines and nested structures do not get flattened into false independent top-level execution claims;
- malformed/error-recovered regions cannot create positive evidence unless the relevant occurrence remains independently unambiguous under an explicit supported rule.

Use source spans for traceability and deterministic occurrence order. Do not define identity from parser object identity or grammar-specific node indexes.

### 6.5 Migrate direct requirements observation

Replace `bounded_shell_segments(...)` as the command-meaning source in `direct_install.py` with the shared command analysis.

Preserve the existing dependency-domain responsibility:

```text
real static pip-install command occurrence
+ independently established requirements path
+ resolved working-directory context
→ direct installation declaration observation
```

The observer must no longer scan comment/string payload as command arguments.

If the shell/command region is materially unresolved and could affect whether the dependency source is directly installed, return the appropriate unresolved state rather than `not_observed`.

Current supported positive forms such as `pip install -r ...`, `pip3`, and `python -m pip` must remain supported where the parser exposes the required literal command/arguments safely.

### 6.6 Migrate project-environment selection

Move pip local-project and uv selector interpretation onto the same command occurrence IR.

Preserve current dependency semantics while removing duplicate lexical assumptions:

- comments cannot create `-e`, extras, groups, or uv selectors;
- quoted payload does not create commands;
- effective working-directory/path behavior remains separately owned by the existing context resolver;
- dynamic or unsupported argument/path context remains unresolved rather than guessed;
- shell parser structure identifies the command occurrence; dependency-domain code still owns pip/uv meaning.

Do not make the GitHub command-analysis layer dependency-aware.

### 6.7 Migrate CI package invocation and command identity

Remove the independent private shell splitter in `ci/workflow_commands.py` once all justified consumers use the shared command analysis.

Direct package invocation detection must operate on real command occurrences, not arbitrary source fragments.

Reconcile `segment_index` deliberately:

1. trace every remaining producer/consumer/test that depends on it;
2. treat current use as migration evidence, not retention authority;
3. make source span/occurrence identity the canonical static-command identity;
4. retain a derived source-order ordinal only if a current admitted contract genuinely needs it;
5. do not let a retained ordinal imply runtime execution or same-path ordering.

Project-environment evidence reconciliation must compare identities produced by the same shared command-analysis owner rather than independently re-splitting raw command text.

### 6.8 Introduce explicit runtime-strengthening eligibility

Separate static occurrence from the proposition that whole-step success can strengthen that occurrence.

The strengthened Cycle-3 proposition is **Runtime-Correlated Support Proposition**:

```text
exact supported static occurrence
+ positively admitted structural relationship
+ established execution profile
+ exact correlated completed/successful owning runtime step
+ no visible continue-on-error masking
→ supported runtime-correlated occurrence
```

This is stronger than static declaration alone, but it is not direct observation/proof that the exact inner command executed or succeeded. It does not prove exact installed version, selected artifact, compatibility, update safety, or maintainer action.

CI must classify occurrence strengthening as:

```text
eligible
ineligible
unresolved
```

Do **not** infer positive eligibility from absence of currently known negative tags. The provider command-analysis adapter must positively establish the bounded whole-step/position relation required by the admitted family while keeping Tree-sitter CST nodes private.

The accepted first positive family is:

```text
Sole Ordinary Top-Level Command Admission

cleanly analyzable step
+ exact target positively established as the sole ordinary top-level command statement
+ admitted GitHub built-in/default Bash/sh, PowerShell/pwsh, or CMD execution profile
→ structural/profile candidate for Runtime-Correlated Support
```

and:

```text
First Sequential Bash/sh Command Admission

cleanly analyzable Bash-family step
+ exact target positively established as the first ordinary top-level command statement
+ admitted GitHub built-in/default Bash/sh profile with fail-fast -e behavior
+ target outside conditional/status-inverting/nested/asynchronous structure
→ structural/profile candidate for Runtime-Correlated Support
```

The First Sequential Bash/sh Command Admission exists to retain real product coverage such as S002's first dependency-install command in a normal multi-command Bash step. It does not authorize arbitrary later linear-chain occurrences.

The provider adapter must use the existing Tree-sitter syntax tree to prevent false-straightforward admission, including relevant cases such as:

- Bash negated commands (`! command`);
- Bash asynchronous/background commands (`command &`);
- Bash process substitution and compound/brace nesting;
- PowerShell flow-control, try/trap, class/script-block or equivalent structures when they affect the target's whole-step relation;
- CMD goto/exit/parenthesized or equivalent non-`cmd` statements when they affect the target's whole-step relation.

Prefer one small parser-neutral positive relation/whole-step shape over leaking grammar-specific node types or constructing a general shell CFG/interpreter.

Classify **ineligible** when the known relationship positively allows successful step completion without meaningful runtime support for the exact target occurrence, including positively identified conditional bodies, loop bodies, deferred function bodies, status inversion, background/asynchronous execution, process substitution, and `||` rescue positions.

Classify **unresolved** when the current representation/profile is too coarse to decide honestly, including generic `short_circuit` where `&&` and `||` are collapsed, generic pipelines, generic nested/subshell structures, compound blocks, later generic linear-chain occurrences, complex unrecognized PowerShell/CMD structure, parser ambiguity, unresolved execution profile, and custom shell templates.

Do not automatically strengthen commands merely because:

```text
source_order == 0
one collected command occurrence exists
no currently-known negative tag fired
```

Those facts do not necessarily describe every shell statement in the script.

A later increment may admit selected `&&`, pipeline, or later-chain shapes only after the IR preserves the bounded operator/position/status-contribution relation required by the proposition and shell-specific characterization demonstrates the implication. S004-style `. ./venv/bin/activate && pip install ...` is the current concrete re-entry case.

This policy must preserve:

```text
static command exists
!= command executed
!= command succeeded
```

### 6.9 Correct same-step ordering/direct-exercise composition

Current direct-exercise logic uses step/segment ordering. Replace any assumption that simple source order alone means same execution path.

For different user-defined steps, retain only ordering propositions already justified by the workflow/correlation model.

For multiple occurrences inside one `run` step, direct-exercise composition may use same-step order only when the command analysis establishes a supported relation strong enough for that proposition. Otherwise keep static invocation visible but do not claim that it occurred after dependency consumption on the same execution path.

Do not introduce a generic control-flow graph unless actual implementation evidence shows the bounded structural relation cannot be represented more simply.

### 6.10 Remove obsolete splitters and duplicated inference

After all admitted consumers are migrated:

- remove or narrow `bounded_shell_segments(...)` if it no longer owns an independent responsibility;
- remove CI `_shell_segments(...)` duplication;
- remove obsolete regex/tokenization assumptions that are now subsumed by parser-backed command occurrence;
- keep path/working-directory helpers that remain independently justified;
- do not leave old and new command-identification routes active in parallel as fallback behavior.

The final normal flow must have one earliest sufficient command-structure owner.

## 7. Proof strategy

Validation proceeds narrow-to-broad. Passing tests are evidence only for the behavior they exercise.

### Parser/dependency characterization

Prove:

- selected runtime + three grammar packages import and parse under the supported Python environment;
- representative nodes/source spans needed by adapters are stable enough for the bounded contract;
- relevant parse errors/recovery are detectable and conservatively handled.

### Shared shell/command-analysis proof

Add focused tests for each admitted shell family covering representative:

```text
real command
comment payload
quoted/string separator payload
multiple top-level commands
conditional command
short-circuit command
malformed/error-recovered source
source span/order identity
```

Do not require identical syntax fixtures across Bash, PowerShell, and CMD; use idiomatic cases for each language while proving equivalent UpgradePilot invariants.

### Dependency observer proof

For direct requirements and project-environment selection prove:

```text
real admitted command → positive/static evidence remains
comment-only payload → no false positive
quoted command-looking payload → no false positive
unsupported/materially ambiguous parse → unresolved where the proposition cannot be decided
working-directory/path behavior → existing supported semantics preserved
```

### CI/direct-exercise proof

Prove:

- direct package invocation comes only from real command occurrences;
- occurrence identity agrees across dependency/CI composition;
- same-step source ordering is not automatically treated as execution-path ordering;
- conditional/short-circuit commands can remain static observations without receiving unjustified runtime authority.

### Runtime-correlation proof

Add end-to-end cases demonstrating both sides of the boundary:

```text
straightforward supported static command
+ exact correlated completed/successful runtime step
→ admitted runtime strengthening remains available
```

and:

```text
comment/quoted false static premise
+ successful runtime step
→ cannot become runtime-correlated dependency support
```

and:

```text
real but conditional/path-dependent command
+ successful containing runtime step
→ static occurrence may remain visible
→ stronger command-execution proposition remains unestablished/unresolved
```

Retain existing continue-on-error protections.

### Nearby regression proof

Run focused/nearby suites for at least:

- GitHub static workflow definition;
- direct-install declaration;
- project-environment selection;
- workflow dependency evidence;
- static/runtime correlation;
- runtime-correlated dependency coverage;
- investigation/application paths that consume CI coverage.

### Broad deterministic proof

Run the complete deterministic test suite after focused and nearby proof are green.

Record exact counts at execution time. Do not copy the historical `566` total as if it were the new proof result.

## 8. Pass condition

This plan's implementation responsibility passes only when all of the following are true:

1. ADR-0009's parser-backed command-analysis path is the normal product path for admitted shell families.
2. Bash/sh, PowerShell/pwsh, and CMD/batch adapters have representative characterization/proof sufficient for the current command propositions, or any family that fails its gate is explicitly left unsupported/unresolved without regex fallback and the resulting product boundary is reconciled before claiming completion.
3. The known comment and quoted-separator false positives no longer create direct-install, project-environment, or direct-package-invocation evidence.
4. Dependency and CI consumers use one shared command occurrence identity/order source.
5. Static real-command occurrence remains distinguishable from runtime execution/success.
6. Successful step-level runtime correlation strengthens only explicitly eligible command structures.
7. Conditional/path-dependent command presence is not promoted solely because the enclosing step succeeded.
8. Existing admitted ordinary positive cases remain green unless a previous claim is deliberately corrected as overstated and the correction is preserved in evidence/state.
9. Focused, nearby, and full deterministic validation is green under the final implementation.
10. Active working memory and `MEMORY.md` accurately preserve the implemented proof and non-proof boundaries before the cycle advances.

## 9. Stop / reassessment conditions

Stop implementation and return to Planning/Design or ADR reassessment if evidence shows that:

- Tree-sitter or an admitted grammar cannot safely/proportionately provide the required current structure;
- the PowerShell/CMD grammar maturity creates material incorrect positive evidence that cannot be bounded by characterization/error policy;
- effective shell identity cannot be established for a material class without broader GitHub expression/matrix execution semantics;
- the proposed command IR requires a general shell AST/control-flow graph rather than the bounded relations this responsibility needs;
- runtime strengthening requires actual command-level runtime evidence rather than a bounded structural relation to step success;
- migration exposes an independently justified compatibility contract not covered here;
- a product requirement would require Python/arbitrary custom-interpreter analysis or another shell family.

Do not hide these discoveries behind additional regex fallbacks or ad-hoc downstream checks.

## 10. Handoff after implementation

After the implementation/proof responsibility closes, return to the parent synthesis journey and re-audit the evidence path rather than automatically adding another evidence feature.

The next question is then:

> With exact-revision provenance, static↔runtime correlation, and static workflow-command semantics corrected, what remaining evidence proposition actually prevents the next justified maintainer-action path?

Previously retained candidates such as consuming-job preservation into Target, exact runtime dependency/artifact evidence, or target wheel compatibility remain candidates only; the next responsibility must be selected from current evidence at that time.

`UP-SKILL:upgradepilot-planning-design`
