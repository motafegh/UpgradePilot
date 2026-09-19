# Parser-Backed Static Workflow Command Evidence and Consumer Composition

**Learning-artifact date:** 2026-09-19  
**Source/test evidence horizon:** main@7e067aa8e749ec79d93e9b47dbf6c3e752b38932  
**Roadmap responsibility:** Group 8 — CI and workflow evidence without treating CI as a verdict  
**Package position:** Note 1 of 2  
**Primary responsibility:** understand how UpgradePilot converts GitHub Actions run-step source into one shared parser-neutral static command representation and then composes dependency/CI evidence from that same occurrence identity  
**Target depth:** **must master / own** shell-context resolution, parser-backed occurrence formation, source identity, consumer ownership, one-traversal composition, static ordering, and proof/non-proof boundaries; Tree-sitter grammar/node internals remain lookup-level

This note teaches the **static half** of the current CI evidence architecture.

The next note teaches the distinct runtime-strengthening responsibility.

The shortest mental model is:

~~~text
exact workflow source
→ bounded workflow definition
→ effective shell context
→ shell-family Tree-sitter parser
→ parser-neutral StaticCommandAnalysis
→ exact StaticCommandOccurrence(s)
→ canonical StaticCommandLocation
→ dependency-owned command meaning
   + CI-owned composition
→ static dependency consumption
   + static direct package invocation
   + bounded static ordering
~~~

The central rule is:

~~~text
real command occurrence in source
!= command executed
!= command succeeded
~~~

Static source evidence can be strong and useful without being runtime evidence.

---

## 1. Why this architecture had to replace textual command splitting

Before ADR-0009, more than one layer reconstructed shell-like fragments from raw run text.

The broad historical shape was:

~~~text
RunStepDefinition.command.text
→ dependency-side textual splitting
→ direct requirements / project selection

and separately

RunStepDefinition.command.text
→ CI-side textual splitting
→ package invocation / segment ordering
~~~

That design exposed two different problems.

### Problem A — lexical false positives

Simple splitting over separators such as:

~~~text
&&
||
;
newline
~~~

could treat text inside comments or quoted strings as executable commands.

Controlled examples included shapes such as:

~~~text
pip install wheel # -r requirements-dev.txt
~~~

where a commented requirements fragment could be misinterpreted, and:

~~~text
echo "note; pip install -r requirements-dev.txt"
~~~

where quoted text could manufacture a false pip-install-looking segment.

### Problem B — real syntax is still not execution proof

Even a genuine command occurrence may be path-dependent:

~~~text
true || pip install -r requirements-dev.txt
~~~

or:

~~~text
if false; then
    pip install -r requirements-dev.txt
fi
echo done
~~~

A better lexer alone would not solve this.

The architecture therefore had to distinguish:

~~~text
is this a real syntactic command?
from
what structural context contains it?
from
did it execute?
~~~

### Problem C — duplicated identity drift

When dependency and CI layers independently split the same raw source, an integer such as an old segment index can accidentally mean different fragments in different layers.

That is an ownership problem:

> **one source proposition should have one earliest trustworthy owner.**

ADR-0009 therefore selected one provider-owned command-analysis boundary rather than repeated downstream reconstruction.

---

## 2. Accepted architecture: parse broadly, claim narrowly

ADR-0009 selected Tree-sitter as a common parsing substrate for the admitted shell families:

~~~text
Bash / sh
PowerShell / pwsh
CMD / batch
~~~

The architecture is:

~~~text
GitHub Actions workflow definition
+ exact run step
        ↓
effective shell resolver
        ↓
syntax family + execution profile
        ↓
Tree-sitter shell parser
        ↓
UpgradePilot parser-neutral command IR
        ↓
dependency and CI consumers
~~~

Two constraints are fundamental.

### Tree-sitter is syntax machinery, not product-domain truth

Tree-sitter nodes do not flow through dependency and CI contracts.

UpgradePilot converts parser-specific syntax into its own types.

This keeps downstream code independent of grammar-specific node layouts.

### Parser success does not create runtime authority

The static layer answers questions such as:

~~~text
which commands are syntactically present?
which arguments are statically recoverable?
where exactly is the occurrence?
what structure contains it?
~~~

It does not answer:

~~~text
did this command execute?
did it succeed?
which package version was installed?
which wheel was selected?
is the dependency compatible?
~~~

That separation is preserved through the whole architecture.

---

## 3. Effective shell context is resolved before parsing

Primary owner:

~~~text
src/upgradepilot/github/workflow_command_shell.py
~~~

One run step may inherit shell behavior from several GitHub Actions levels.

Current precedence is:

~~~text
step shell
> job defaults.run.shell
> workflow defaults.run.shell
> job-container default
> statically known runner-platform default
~~~

The result is:

~~~text
EffectiveShellContext
~~~

with two deliberately separate concepts.

### Syntax family

~~~text
bash
powershell
cmd
~~~

This answers:

> Which parser understands the source language?

### Execution profile

Examples include:

~~~text
github_builtin_bash
github_builtin_sh
github_builtin_pwsh
github_builtin_powershell
github_builtin_cmd
github_default_non_windows
github_default_windows
github_default_container_sh
custom_shell_template
~~~

This answers a different question:

> Which GitHub wrapper/execution semantics have actually been established?

This distinction matters later.

For example:

~~~text
shell: bash
~~~

and a custom shell template beginning with Bash may share:

~~~text
syntax_family = bash
~~~

while differing in:

~~~text
execution_profile
~~~

A custom template can therefore be parseable without inheriting the same runtime-strengthening authority as a built-in GitHub Bash profile.

---

## 4. Conservative shell resolution

The resolver does not guess.

Examples:

### Dynamic higher-precedence shell

If the step shell is expression-backed, lower-level defaults are not used to manufacture certainty.

Result:

~~~text
state = unresolved
reason = dynamic_shell_declaration
~~~

### Python shell

A Python step is not interpreted as shell source merely because Python can invoke subprocesses.

Result:

~~~text
state = unsupported
reason = python_shell_is_separate_language
~~~

### Unknown/self-hosted runner without explicit shell

The system does not guess a platform default.

Result remains unresolved.

### Job container without explicit shell

GitHub container semantics provide a distinct default-sh execution profile.

The important lesson is:

> **Syntax selection and wrapper semantics are evidence, not convenience defaults.**

---

## 5. Shared parser-neutral command analysis

Primary owner:

~~~text
src/upgradepilot/github/workflow_command_analysis.py
~~~

Main entry point:

~~~text
analyze_run_step_commands(workflow, job, step)
~~~

Its flow is:

~~~text
resolve effective shell
→ select admitted Tree-sitter grammar
→ parse exact UTF-8 run text
→ collect real command nodes
→ sort deterministically by source span
→ convert each into StaticCommandOccurrence
→ return StaticCommandAnalysis
~~~

The analysis state is explicit:

~~~text
analyzable
unresolved
unsupported
parse_error
~~~

This is important because failure to understand command structure is not converted into false absence.

---

## 6. Fail closed: no textual fallback after parser uncertainty

A material Tree-sitter parse error produces:

~~~text
state = parse_error
command_occurrences = ()
problem.reason = material_shell_parse_error
~~~

The implementation deliberately does **not** say:

~~~text
parser failed
→ use old regex/splitter
→ maybe recover a positive command
~~~

Why?

Because that would preserve the exact false-positive architecture the parser was introduced to replace.

The safe rule is:

> **Parser uncertainty cannot create stronger positive evidence through a weaker fallback.**

The source also bounds syntax-tree traversal by node-count and depth limits. A resource bound becoming active produces unresolved evidence rather than pretending the rest of the tree does not exist.

---

## 7. What one StaticCommandOccurrence contains

A successful analysis produces one or more:

~~~text
StaticCommandOccurrence
~~~

Each occurrence preserves:

~~~text
source_order
source_span
raw_source
executable
arguments
structural_context
whole_step_relation
~~~

These fields answer different questions.

### source_span

~~~text
CommandSourceSpan
~~~

preserves UTF-8 byte positions and row/column points.

The byte-based identity matters because non-ASCII source still needs deterministic source-location fidelity.

### source_order

Commands are ordered from parser spans.

This is deterministic source order.

It is **not** runtime execution order.

### executable and arguments

Each is represented as:

~~~text
StaticCommandAtom
~~~

with state such as:

~~~text
literal
dynamic
unsupported
~~~

The provider layer only establishes recoverable syntax-level atoms.

It does not interpret:

~~~text
pip install
uv sync
pytest
~~~

as dependency or CI semantics.

Those belong downstream.

---

## 8. Structural context preserves source meaning without simulating the shell

Current parser-neutral structures include:

~~~text
straightforward_top_level
linear_chain
short_circuit
conditional
loop
pipeline
function_or_block
nested_or_subshell
status_inverted
asynchronous
process_substitution
~~~

This is not a complete shell control-flow graph.

It is the bounded structure needed by current product propositions.

Examples:

~~~text
true || pip install -r requirements.txt
→ pip occurrence exists
→ structural_context includes short_circuit
~~~

~~~text
if false; then
    pip install -r requirements.txt
fi
→ pip occurrence exists
→ structural_context includes conditional
~~~

~~~text
printf x | grep x
→ command occurrences exist
→ pipeline context preserved
~~~

The important separation is:

~~~text
parser found a real command
→ static presence can still be useful

structure is path-dependent
→ runtime certainty remains separate
~~~

---

## 9. Positive whole-step relation is stronger than a generic structure tag

Cycle 3 later required the provider to preserve a small positive relation:

~~~text
StaticCommandWholeStepRelation
~~~

Current positive forms are:

~~~text
sole_ordinary_top_level_command
first_ordinary_top_level_command_in_sequential_script
~~~

These are intentionally narrow.

### Sole ordinary top-level command

Conceptually:

~~~text
one ordinary top-level command
→ provider can positively establish that relation
~~~

This exists across admitted shell families where the parser structure supports it.

### First sequential Bash/sh command

For selected Bash/sh shapes:

~~~text
command A
command B
~~~

the first ordinary top-level command can receive:

~~~text
first_ordinary_top_level_command_in_sequential_script
~~~

because later runtime policy may combine this fact with GitHub Bash/sh fail-fast execution semantics.

### Absence of a positive relation is not automatically negative

A command may be:

~~~text
real
well parsed
statically meaningful
~~~

while:

~~~text
whole_step_relation = None
~~~

That does not mean the command definitely did not execute.

It means the provider did not establish one of the currently admitted positive whole-step relationships.

The runtime policy decides the stronger proposition later.

---

## 10. Canonical command identity

Primary owner:

~~~text
src/upgradepilot/github/workflow_command_location.py
~~~

Current identity value:

~~~text
StaticCommandLocation
    source_span
    source_order
~~~

derived directly from one StaticCommandOccurrence.

This replaced the overloaded historical segment-index concept.

The distinction is crucial:

~~~text
StaticCommandLocation
→ identifies one static source occurrence

StaticCommandLocation
!= execution identity
!= success proof
!= same-path ordering proof
~~~

The complete outer identity of a command-bearing CI proposition usually also includes:

~~~text
workflow path
workflow revision
job key
step source index
command location
~~~

This gives downstream layers one shared answer to:

> Which exact source occurrence are we discussing?

---

## 11. One workflow traversal, one command analysis per run step

Primary CI owner:

~~~text
src/upgradepilot/ci/workflow_commands.py
~~~

The normal path now has one workflow-level traversal.

For each readable steps job:

~~~text
for each run step
    → analyze_run_step_commands(...) once
    → reuse that same StaticCommandAnalysis for:
         direct requirements observation
         project-environment selection
         direct package invocation
~~~

This is one of the most important architectural corrections.

The source docstring explicitly preserves this contract:

~~~text
one parsed workflow traversal
+ one StaticCommandAnalysis per run step
→ all current static command consumers
~~~

Why this matters:

1. no consumer invents a separate source segmentation;
2. all consumers refer to the same occurrence identity;
3. parser failure has one meaning across consumers;
4. structural context is shared consistently;
5. later runtime strengthening receives one canonical occurrence handoff.

A compatibility/test seam for precomposed project-environment evidence remains, but it is not a second normal production implementation.

---

## 12. Provider meaning versus dependency meaning versus CI meaning

The architecture deliberately separates ownership.

### GitHub/provider layer owns

~~~text
workflow structure
effective shell context
syntax parsing
command occurrence
literal/dynamic atoms
source span/order
structural context
whole-step relation
~~~

### Dependency layer owns

~~~text
is this pip?
is it an admitted requirements install?
which requirements path?
is this a pip local-project install?
which extras were selected?
is this uv sync/run?
which groups/extras/package scope were selected?
does the selected source/lock environment contain or reach the changed dependency?
~~~

### CI layer owns

~~~text
which job/step/occurrence is in CI?
was the target repository checked out at workspace root?
does this static declaration consume the changed dependency?
does a later direct invocation exercise the changed package?
what bounded static ordering relation exists?
~~~

The rule is:

> **The provider should know command syntax, not dependency semantics. Dependency code should know package-manager meaning, not parse shell source. CI should compose evidence, not duplicate either parser or dependency semantics.**

---

## 13. Direct requirements observation consumes shared command atoms

Primary owner:

~~~text
src/upgradepilot/dependency/direct_install.py
~~~

Its proposition is intentionally narrow:

> Does one real parsed static command declaration directly name the independently established dependency requirements source?

Inputs include:

~~~text
RunStepDefinition
StaticCommandAnalysis
known dependency source path
workflow/job working-directory context
~~~

Current admitted pip forms include bounded shapes such as:

~~~text
pip install -r ...
pip3 install -r ...
python -m pip install -r ...
~~~

The observer works from typed atoms rather than splitting raw shell text.

It then resolves the requirements path relative to the effective working directory.

A successful observation produces:

~~~text
state = observed
matched requirement path
StaticCommandLocation
~~~

But still means only:

~~~text
static source directly declares installation from this requirements source
~~~

It does **not** mean:

~~~text
the command executed
installation succeeded
the changed dependency version was installed
~~~

---

## 14. Material uncertainty stays unresolved

Dependency consumers distinguish:

~~~text
observed
not_observed
unresolved
~~~

Examples that can keep the proposition unresolved include:

~~~text
command analysis itself unresolved
dynamic material command atom
dynamic requirements path
dynamic/invalid working-directory relation
~~~

This is stronger epistemic discipline than flattening every failure to:

~~~text
not_observed
~~~

because:

~~~text
not_observed
→ admitted evidence was readable and no qualifying declaration was established

unresolved
→ available evidence could not safely decide the proposition
~~~

That distinction later survives CI composition.

---

## 15. Project-environment selection also consumes the same analysis

Primary owner:

~~~text
src/upgradepilot/dependency/environment_selection.py
~~~

It interprets bounded project-selection semantics from StaticCommandOccurrence atoms.

Current examples include:

~~~text
pip install -e ".[dev]"
python -m pip install ".[dev,mlx]"
uv sync --group docs
uv sync --all-packages --group docs
uv run --extra mlx pytest
~~~

It preserves typed selectors such as:

~~~text
OptionalExtraSelector
DependencyGroupSelector
AllOptionalExtrasSelector
AllDependencyGroupsSelector
~~~

and package scope such as:

~~~text
bound_project
all_workspace_packages
~~~

This static selection still does not prove that the environment formed.

For uv, later dependency-owned reachability determines whether a selected root has an admitted exact-lock path to the changed dependency.

The responsibilities remain:

~~~text
command parser
→ what command syntax exists

environment selection
→ what project environment the command statically selects

source membership / uv reachability
→ whether that selected environment contains/reaches the changed dependency

CI consumption
→ whether this static CI declaration therefore consumes the changed dependency
~~~

No one layer pretends to own all four propositions.

---

## 16. CI preserves repository-checkout provenance

Static command meaning alone is not enough.

A workflow may run:

~~~text
pip install -r requirements-dev.txt
~~~

after checking out another repository.

So CI tracks a bounded repository-root checkout state while traversing each job:

~~~text
not_established
current_repository
other_repository
unresolved
~~~

For actions/checkout declarations, it interprets enough static inputs to determine whether the changed repository is established at the GitHub workspace root.

Consequences include:

~~~text
current repository at root
+ matching direct requirements declaration
→ may support changed-dependency consumption
~~~

~~~text
other repository at root
→ do not rebind that command to the changed repository
~~~

~~~text
dynamic/ambiguous checkout path or repository
→ preserve unresolved provenance
~~~

This is a good example of cross-evidence composition:

> **A real pip command is not enough; the source relationship also needs repository provenance.**

---

## 17. StaticDependencyConsumptionEvidence is a CI proposition

Primary type:

~~~text
StaticDependencyConsumptionEvidence
~~~

It preserves fields including:

~~~text
state
mechanism
normalized package
workflow path
workflow revision
job key
step source index
source path
command
command location
structural context
whole-step relation
execution profile
reachability witness/conditions when relevant
~~~

Current states are:

~~~text
supported
not_established
unresolved
~~~

Current mechanisms include:

~~~text
direct_requirements
project_environment
~~~

For a supported direct requirements shape:

~~~text
trusted dependency source context
+ current-repository checkout provenance
+ parsed matching requirements declaration
→ supported static consumption
~~~

For uv/project selection:

~~~text
parsed project selection
+ exact project/lock evidence
+ dependency-owned membership/reachability
→ composed static consumption
~~~

The detail strings explicitly retain the boundary:

~~~text
runtime execution and success are not established
~~~

---

## 18. Direct package invocation is a separate static axis

CI also recognizes a real parsed command occurrence that directly invokes the changed package.

Type:

~~~text
DirectPackageInvocationEvidence
~~~

Examples of bounded wrapper shapes include current admitted forms such as:

~~~text
pytest
python -m pytest
uv run pytest
poetry run pytest
pipenv run pytest
coverage run -m pytest
~~~

This does not automatically mean the changed dependency was exercised meaningfully.

CI first keeps separate:

~~~text
dependency consumption
direct package invocation
~~~

Then the direct-exercise proposition asks whether an invocation is statically ordered after supported consumption in the same job.

This prevents:

~~~text
package command exists somewhere
→ therefore changed dependency was exercised
~~~

---

## 19. Identity and ordering are separate responsibilities

After canonical StaticCommandLocation replaced segment identity, CI still needed to answer a different question:

> Is a direct invocation statically after supported consumption?

Primary owner:

~~~text
src/upgradepilot/ci/static_command_order.py
~~~

The bounded relation is:

~~~text
ordered_after
not_after
unresolved
~~~

### Different run steps

If invocation is in a later user-defined run step in the same static job:

~~~text
later step_source_index
→ ordered_after
~~~

This is still static ordering, not runtime execution.

### Same run step

If both occurrences are in the same run step, source order can contribute only when structure is sufficiently clean for the bounded rule.

A later occurrence under a short-circuit/path-dependent shape does not automatically earn ordered-after.

For example tests preserve:

~~~text
same-step source order 0 then 1
+ clean structure
→ ordered_after
~~~

but:

~~~text
later occurrence
+ short_circuit structure
→ unresolved
~~~

Likewise path-dependent structures such as:

~~~text
status_inverted
asynchronous
process_substitution
~~~

do not earn clean same-step ordering merely from numeric source order.

This is the key distinction:

~~~text
source position
!= guaranteed same-path execution order
~~~

---

## 20. Why source order was not enough

A naïve migration could have replaced:

~~~text
segment_index
~~~

with:

~~~text
source_order
~~~

and declared the problem solved.

That would have repeated the same conceptual error.

Identity asks:

~~~text
which command occurrence?
~~~

Ordering asks:

~~~text
what bounded relation can source structure establish between two occurrences?
~~~

Execution asks:

~~~text
what happened at runtime?
~~~

These are three different propositions.

The current architecture uses:

~~~text
StaticCommandLocation
→ identity

static_command_order relation
→ bounded static ordering

runtime-strengthening/correlation
→ later runtime proposition
~~~

This separation is reusable well beyond this particular refactor.

---

## 21. Important current parser examples

Focused tests under:

~~~text
tests/test_github_workflow_command_analysis.py
~~~

protect representative behavior.

### Same ordinary command across shell families

A command such as:

~~~text
python -m pip install -r requirements.txt
~~~

is parsed into comparable literal atoms across Bash, PowerShell, and CMD.

### Comment/quoted false positives are gone

Commented or quoted pip text does not manufacture a second pip command.

### Short circuit remains a real command occurrence

~~~text
true || python -m pip install -r requirements.txt
~~~

still produces the install occurrence.

But the occurrence carries:

~~~text
short_circuit
~~~

rather than pretending it is straightforward.

### Conditional occurrence remains visible

A pip command inside an if-body exists as source evidence and carries:

~~~text
conditional
~~~

It is not flattened into a top-level execution claim.

### Pipelines remain structurally distinct

Commands inside a pipeline carry pipeline context.

### Parse errors fail closed

Malformed shell source produces parse_error and no partial positive occurrences.

### UTF-8 identity is tested

Source spans use UTF-8 byte boundaries rather than assuming character count equals byte count.

---

## 22. Single-pass composition is explicitly tested

Focused owner:

~~~text
tests/test_single_pass_workflow_static_evidence.py
tests/test_parser_backed_ci_command_evidence.py
~~~

The important contract is that one parsed command analysis supplies the different static consumers.

A representative two-command run block:

~~~text
pip install -r requirements-dev.txt
pytest tests
~~~

can produce:

~~~text
consumption command location
→ source order 0

package invocation command location
→ source order 1
~~~

from one shared parser result.

That gives CI a trustworthy basis for later composition.

The test is not proving execution.

It is proving:

~~~text
shared source owner
+ canonical occurrence identities
+ consumers agree on those identities
~~~

---

## 23. Multi-job workflows are preserved at the CI static layer

The static CI evidence owner does not impose a one-job restriction.

A workflow can contain:

~~~text
unit job
lint job
~~~

while only the unit job carries changed-dependency consumption.

Static evidence preserves:

~~~text
job_count = 2
consumption.job_key = unit
~~~

This is important for the later Target integration issue documented in Group 7:

> CI already knows the consuming job; another downstream owner may still fail to use that relation.

The current CI static architecture should therefore not be confused with Target's narrower current job-selection capability.

---

## 24. Engineering progression: what changed in our mental model

The valuable progression is:

~~~text
first symptom:
comment/quoted text can create false commands
        ↓
initial temptation:
repair splitting/lexing locally
        ↓
broader discovery:
real commands can still be conditional/path-dependent
        ↓
ownership discovery:
dependency and CI also reconstruct command identity independently
        ↓
architecture correction:
one provider-owned parser-backed command analysis
        ↓
consumer migration:
direct requirements + project selection + package invocation reuse it
        ↓
identity correction:
StaticCommandLocation replaces overloaded segment identity
        ↓
ordering correction:
explicit ordered_after | not_after | unresolved relation
        ↓
next distinct responsibility:
runtime strengthening
~~~

The transferable lesson is:

> **When several consumers depend on the same source fact, repair the earliest sufficient shared owner instead of repeatedly patching downstream interpretations.**

---

## 25. Why Tree-sitter was chosen instead of smaller-looking fixes

The design investigation compared several approaches.

### Local regex/quote-aware patch

Could fix the first reproduced examples.

But it would preserve:

~~~text
duplicated command reconstruction
weak control-flow semantics
future repeated shell-specific fixes
~~~

### shlex-style tokenization

Useful for some Unix lexical problems.

But it does not provide the required common multi-shell structural model.

### Separate native shell parsers

Potentially high-fidelity, especially for some shells.

But they create different integration/runtime patterns and no consistent common substrate.

### Tree-sitter + UpgradePilot-owned IR

Selected because it offers:

~~~text
common parser model
shell-specific grammars
syntax-tree structure
source spans
bounded parser adapters
one product-owned downstream representation
~~~

The project did **not** treat Tree-sitter syntax as execution semantics.

The design principle remained:

> **parse broadly enough to identify admitted source structure; claim only what downstream evidence justifies.**

---

## 26. What the static layer proves

A successful static path can establish propositions such as:

~~~text
this exact workflow revision contains this command occurrence
this occurrence has these literal/dynamic atoms
this occurrence is in this job/step
the changed repository is statically established at the workspace root
this command directly declares installation from the changed requirements source
this uv/pip command selects this project environment
dependency-owned source/lock evidence says the selected environment contains/reaches the changed dependency
this exact static CI declaration therefore consumes the changed dependency
a direct package invocation exists after consumption under the bounded static ordering rule
~~~

Those are useful product facts.

---

## 27. What the static layer does not prove

Even perfect parser/static evidence does not prove:

~~~text
the workflow ran
the job ran
the run step ran
the inner command ran
the inner command succeeded
installation succeeded
the exact updated version was installed
a particular wheel/sdist was selected
the target environment is compatible
tests exercised all affected behavior
the update is safe
a maintainer action is justified
~~~

This boundary is not a weakness of the parser.

It is correct evidence ownership.

The next Group-8 note begins exactly where this one stops.

---

## 28. Focused test owners and proof interpretation

Primary current test anchors include:

~~~text
tests/test_github_workflow_command_analysis.py
tests/test_parser_backed_ci_command_evidence.py
tests/test_single_pass_workflow_static_evidence.py
tests/test_direct_install_declaration.py
tests/test_project_environment_selection.py
tests/test_workflow_dependency_evidence.py
tests/test_static_command_order.py
~~~

They protect:

~~~text
shell precedence and platform defaults
syntax-family/execution-profile separation
Bash/PowerShell/CMD parser behavior
comments/quotes/control structures
fail-closed parse errors
source-span/source-order identity
parser-backed direct requirements
parser-backed pip/uv environment selection
one-analysis consumer composition
checkout provenance
multi-job static evidence
canonical command identity
bounded static ordering
~~~

### Fresh-proof boundary

This learning-authoring operation is inspecting current source/tests.

It is not running a fresh test suite.

Historical Cycle-3 closure later reported a hosted final proof including:

~~~text
focused investigation 15/15
Cycle-3 focused regression 76/76
full deterministic product regression 604/604
~~~

That historical proof is relevant context, but it is not a fresh result for this authoring session.

---

## 29. Depth calibration

### Must own

- why duplicated textual splitting was unsafe;
- syntax family versus execution profile;
- what StaticCommandAnalysis and StaticCommandOccurrence establish;
- parser failure must not fall back to weaker positive parsing;
- structural context versus positive whole-step relation;
- StaticCommandLocation is source identity, not execution;
- one workflow traversal reuses one command analysis per run step;
- provider, dependency, and CI responsibilities are different;
- checkout provenance matters to consumption;
- direct consumption and direct package invocation are distinct;
- source order and bounded static ordering are distinct;
- static evidence does not prove runtime execution/success.

### Understand operationally

- Tree-sitter is the parser substrate;
- the admitted shell families;
- literal/dynamic/unsupported atom states;
- pip/direct-requirements argument interpretation;
- pip/uv project-environment selectors;
- how job/step/command identity is carried;
- why selected-root/source-membership evidence is composed rather than reparsed.

### Lookup-level

- exact Tree-sitter grammar node names;
- every parser helper function;
- full Bash/PowerShell/CMD grammar;
- every pip/uv option;
- exact source-span arithmetic;
- every focused test fixture helper.

### Deferred

- full shell execution simulation;
- arbitrary dynamic expression evaluation;
- matrix/reusable-workflow expansion;
- runtime logs as command-level proof;
- exact installed package/artifact evidence;
- compatibility/action synthesis.

---

## 30. Fast relearning route

Use this sequence:

~~~text
1. Recall:
   command source presence != execution.

2. Open:
   github/workflow_command_shell.py
   and explain syntax_family vs execution_profile.

3. Open:
   github/workflow_command_analysis.py
   and inspect:
   StaticCommandAnalysis
   StaticCommandOccurrence
   structural_context
   whole_step_relation.

4. Read:
   test_comment_and_quoted_payloads_do_not_manufacture_commands
   plus one conditional/short-circuit test.

5. Open:
   github/workflow_command_location.py
   and explain why location is identity only.

6. Open:
   ci/workflow_commands.py
   and trace one RunStepDefinition:
   one analysis
   → direct requirements
   → project environment
   → package invocation.

7. Trace:
   StaticDependencyConsumptionEvidence.

8. Open:
   ci/static_command_order.py
   and explain ordered_after vs unresolved.

9. State the stopping boundary:
   none of this proves runtime command execution.
~~~

---

## 31. Ownership / transfer questions

Without looking at this note, explain:

1. Why was a quote-aware textual splitter still insufficient after the first false-positive examples?
2. Why must syntax family and execution profile remain separate?
3. Why can a conditional pip command still be valid static declaration evidence?
4. Why does parser failure produce unresolved/parse_error rather than falling back to regex?
5. What exact proposition does StaticCommandLocation establish?
6. Why is one shared StaticCommandAnalysis per run step preferable to each consumer reparsing source independently?
7. Why does a matching pip requirements command still need repository checkout provenance?
8. Why are dependency consumption and direct package invocation separate pieces of evidence?
9. Why can source_order=1 after source_order=0 still yield an unresolved same-step ordering relation?
10. Which layer is responsible for deciding whether a uv-selected group actually reaches the changed dependency?

### Transfer exercise

Consider:

~~~text
- run: |
    if false; then
        pip install -r requirements-dev.txt
    fi
    pytest tests
~~~

Predict the static evidence you would expect for:

~~~text
pip occurrence existence
pip structural context
requirements declaration presence
pytest invocation presence
same-step consumption→invocation ordering
runtime execution
~~~

Then explain which of those answers belong to this note and which must be deferred to the runtime-strengthening note.

---

## 32. Evidence anchors

Pinned source/test horizon:

~~~text
main@7e067aa8e749ec79d93e9b47dbf6c3e752b38932
~~~

Primary current source:

~~~text
src/upgradepilot/github/workflow_command_shell.py
src/upgradepilot/github/workflow_command_analysis.py
src/upgradepilot/github/workflow_command_location.py
src/upgradepilot/dependency/direct_install.py
src/upgradepilot/dependency/environment_selection.py
src/upgradepilot/ci/workflow_commands.py
src/upgradepilot/ci/consumption.py
src/upgradepilot/ci/static_command_order.py
~~~

Primary tests:

~~~text
tests/test_github_workflow_command_analysis.py
tests/test_parser_backed_ci_command_evidence.py
tests/test_single_pass_workflow_static_evidence.py
tests/test_direct_install_declaration.py
tests/test_project_environment_selection.py
tests/test_workflow_dependency_evidence.py
tests/test_static_command_order.py
~~~

Architecture / implementation coordination:

~~~text
docs/architecture/ADR-0009-parser-backed-static-workflow-command-analysis.md
plans/STATIC_WORKFLOW_COMMAND_ANALYSIS_AND_RUNTIME_STRENGTHENING_IMPLEMENTATION_PLAN.md
~~~

Directly relevant engineering progression:

~~~text
working-memory/2026-09-13_static-shell-direct-install-false-positive-recognition.md
working-memory/2026-09-14_static-command-consumer-migration-and-identity.md
~~~

Historical prerequisite snapshot:

~~~text
learning/2026-09-12-ci-static-runtime-correlation-bridge.md
~~~

That September 12 artifact remains a useful frozen earlier horizon. It is not rewritten by this note.

This file is a learning snapshot, not a specification, architecture decision, live-state owner, or product-change authorization.

UP-SKILL:upgradepilot-learning-artifact
