# Occurrence-Level Runtime Strengthening and CI Proof Boundaries

**Learning-artifact date:** 2026-09-19  
**Source/test evidence horizon:** main@7e067aa8e749ec79d93e9b47dbf6c3e752b38932  
**Roadmap responsibility:** Group 8 — CI and workflow evidence without treating CI as a verdict  
**Package position:** Note 2 of 2  
**Prerequisite:** Note 1 — parser-backed static workflow-command evidence and consumer composition  
**Primary responsibility:** understand when exact GitHub Actions step-level runtime evidence may strengthen one exact static dependency-consumption or direct-exercise occurrence, how eligibility/correlation/runtime outcome are composed, and exactly what the strengthened result still does not prove  
**Target depth:** **must master / own** the strengthened proposition, candidate identity, eligible/ineligible/unresolved policy, exact static↔runtime step correlation, continue-on-error handling, factual runtime outcomes, static fallback, existential aggregation, direct-exercise separation, real S001/S002/S004 boundaries, and proof/non-proof

The central question is:

> **A real static dependency command exists inside a GitHub Actions run step, and GitHub reports the step successful. When is it sound to strengthen the evidence for that exact internal occurrence?**

The current answer is deliberately narrow:

~~~text
exact supported static occurrence
+ positively admitted whole-step/position relation
+ admitted GitHub execution profile
+ exact static↔runtime owning-step correlation
+ no visible continue-on-error masking
+ runtime step completed/successful
        ↓
bounded Runtime-Correlated Support
~~~

This is stronger than static source evidence.

But it still does **not** mean:

~~~text
direct command-level execution proof
direct command-level success proof
exact installed dependency version
selected wheel/sdist
compatibility
complete behavioral exercise
upgrade safety
maintainer-action permission
~~~

That proof boundary is the main lesson of this note.

---

## 1. Why the older static↔runtime bridge was not enough

The September 12 learning snapshot correctly established an earlier bridge:

~~~text
exact static workflow step
↔
exact runtime workflow step
~~~

That was necessary but not sufficient.

The problem is that one run step can contain several internal commands:

~~~text
- run: |
    if false; then
        pip install -r requirements-dev.txt
    fi
    echo done
~~~

GitHub may report:

~~~text
step status = completed
step conclusion = success
~~~

while the pip command never ran.

Therefore:

~~~text
step success
!= every internal command executed
~~~

Cycle 3 added a distinct responsibility between static command evidence and runtime step evidence:

> **runtime-strengthening eligibility for one exact internal command occurrence.**

---

## 2. Three evidence layers must remain separate

The current model has three different propositions.

### Layer A — static command occurrence

From Note 1:

~~~text
parser-backed workflow source
→ exact StaticCommandOccurrence
~~~

This can establish:

~~~text
the command is real source syntax
its exact source identity
its structural context
its bounded whole-step relation
~~~

### Layer B — static↔runtime owning-step correlation

From:

~~~text
src/upgradepilot/ci/workflow_runtime_correlation.py
~~~

This can establish:

~~~text
this exact static user-defined step
↔
this exact runtime GitHub step
~~~

It is identity correlation.

### Layer C — occurrence-level strengthening policy

From:

~~~text
src/upgradepilot/ci/runtime_strengthening.py
src/upgradepilot/ci/dependency_exercise.py
~~~

This asks:

> May the runtime result of that owning step strengthen this specific internal static occurrence?

These layers must not be collapsed.

---

## 3. Runtime correlation answers identity, not package semantics

Primary owner:

~~~text
src/upgradepilot/ci/workflow_runtime_correlation.py
~~~

Main entry point:

~~~text
correlate_workflow_runtime(source, run, jobs)
~~~

Its own module contract is explicit:

~~~text
correlation answers identity only
~~~

It does not interpret runtime status/conclusion as:

~~~text
dependency installed
package exercised
command succeeded
~~~

The WorkflowStep retains factual runtime fields, but stronger meaning belongs to later CI composition.

---

## 4. Exact revision coherence comes first

Positive workflow correlation requires:

~~~text
static workflow source revision
==
runtime workflow run head SHA
~~~

A mismatch produces unresolved correlation.

This prevents:

~~~text
source from commit A
+
runtime result from commit B
→ one apparently coherent proof
~~~

The broader UpgradePilot evidence rule is the same as elsewhere:

> **Runtime facts can strengthen source propositions only when identity/provenance are coherent.**

---

## 5. Current correlation class is deliberately bounded

The current correlation owner does not attempt every GitHub Actions shape.

Positive correlation currently requires an ordinary bounded workflow class.

Important constraints include:

~~~text
readable ordinary steps jobs
no reusable-workflow job in the first class
no strategy/matrix job in the first class
explicit literal unique static job display names
one-to-one static/runtime job-name match
explicit literal unique static step display names
runtime step summaries available
static step names matched exactly once and in order
~~~

Runtime-only steps such as:

~~~text
Set up job
Post checkout
Complete job
~~~

may exist between user-declared steps.

The bridge does not require static and runtime step arrays to be identical.

It requires a deterministic ordered match of the user-declared steps.

Unsupported/ambiguous correlation shapes return:

~~~text
state = unresolved
~~~

rather than guessing.

---

## 6. Exact internal occurrence identity must survive into runtime policy

A runtime-strengthening input is:

~~~text
RuntimeStrengtheningCandidate
~~~

It preserves:

~~~text
proposition_kind
workflow_path
workflow_revision
job_key
step_source_index
command_location
structural_context
whole_step_relation
execution_profile
~~~

Two proposition kinds are currently admitted:

~~~text
dependency_consumption
direct_package_exercise
~~~

The important design choice is:

> **Pass a narrow CI-owned strengthening candidate for one exact occurrence, not a vague step location and not the whole dependency-domain object.**

The candidate contains exactly the facts the strengthening policy needs.

---

## 7. Same step does not mean same candidate

Two static dependency commands can exist in one run step.

For example:

~~~text
command occurrence 0
command occurrence 1
~~~

They share:

~~~text
workflow
job
step_source_index
~~~

but differ in:

~~~text
StaticCommandLocation
~~~

Therefore they are separate RuntimeStrengtheningCandidate values.

Tests deliberately protect this.

One occurrence can be:

~~~text
eligible
~~~

while another occurrence in the same step is:

~~~text
unresolved
~~~

This is why exact command identity had to survive Cycle 2.

A step-level tuple alone would collapse distinct proof states.

---

## 8. Eligibility is a separate three-state policy

Primary owner:

~~~text
classify_runtime_strengthening_eligibility(...)
~~~

Current states:

~~~text
eligible
ineligible
unresolved
~~~

These meanings are distinct.

### eligible

The current bounded source structure + execution profile **positively justify** allowing owning-step runtime evidence to strengthen the occurrence.

### ineligible

The structure is understood well enough to know that successful step completion does **not** justify the admitted strengthening for this occurrence.

### unresolved

The product does not have enough admitted evidence or policy to decide the stronger relationship safely.

Do not flatten:

~~~text
ineligible
unresolved
~~~

into one false value.

They encode different knowledge.

---

## 9. Positive family 1 — sole ordinary top-level command

Current provider relation:

~~~text
sole_ordinary_top_level_command
~~~

When this is combined with an admitted GitHub execution profile, eligibility can become:

~~~text
eligible
~~~

The current admitted profile family includes built-in/default Bash/sh, PowerShell/pwsh, CMD, and current GitHub default/container variants represented by the execution-profile model.

Conceptually:

~~~text
one exact ordinary command owns the run script's positive whole-step relation
+
known admitted GitHub execution profile
→ step-level runtime outcome may strengthen that exact occurrence
~~~

This is the simplest positive family.

---

## 10. Positive family 2 — first sequential Bash/sh command

A second positive family was added for real product coverage.

Provider relation:

~~~text
first_ordinary_top_level_command_in_sequential_script
~~~

Example:

~~~text
pip install -r requirements.txt
echo ready
~~~

Under admitted Bash/sh GitHub profiles, the first command may be eligible.

Why only the first command?

Because the selected policy relies on the relevant GitHub Bash/sh fail-fast execution profile for this bounded implication.

The same first-sequential relation under PowerShell does **not** automatically inherit that rule.

The test therefore preserves:

~~~text
first sequential Bash/sh
→ eligible

same relation + PowerShell profile
→ unresolved
~~~

This is an important evidence-design lesson:

> **Similar source structure under different execution profiles need not justify the same runtime inference.**

---

## 11. Known disqualifying structures become ineligible

Current policy positively classifies several understood structures as:

~~~text
ineligible
~~~

including:

~~~text
conditional
loop
function_or_block
status_inverted
asynchronous
process_substitution
~~~

Why?

Because for these known relationships, successful enclosing-step completion can occur without giving the admitted runtime support to the exact occurrence.

Example:

~~~text
if false; then
    pip install ...
fi
echo done
~~~

The pip occurrence is real static source.

But if the step succeeds, that is not meaningful runtime support for the conditional command.

So:

~~~text
static declaration may remain supported
runtime strengthening = ineligible
~~~

The stronger proposition is not established.

---

## 12. Some structures remain unresolved instead of ineligible

Current coarse/unadmitted structures include examples such as:

~~~text
short_circuit
pipeline
nested_or_subshell
linear_chain without a positive relation
straightforward_top_level without a positive relation
~~~

These can remain:

~~~text
unresolved
~~~

rather than ineligible.

Why?

Because:

~~~text
no current positive strengthening rule
!=
proof that strengthening is impossible
~~~

This is especially important for:

~~~text
short_circuit
~~~

The project deliberately did not turn every unsupported structure into a negative theorem.

A future bounded rule could be added only if evidence justifies it.

---

## 13. Missing identity or execution profile also stays unresolved

Eligibility cannot be positive without:

~~~text
exact workflow path
exact workflow revision
job key
step source index
exact command location
execution profile
~~~

Missing exact occurrence identity yields unresolved.

Likewise:

~~~text
execution_profile = None
~~~

yields unresolved.

A custom shell template also remains unresolved by default:

~~~text
syntax may be parseable
but GitHub built-in wrapper guarantees are not inherited
~~~

This is why Note 1 separated:

~~~text
syntax_family
from
execution_profile
~~~

Cycle 3 consumes that distinction directly.

---

## 14. Eligibility does not inspect runtime status

This is a key ownership boundary.

runtime_strengthening.py decides:

~~~text
is this occurrence structurally/profile-eligible?
~~~

It does **not** decide:

~~~text
was the runtime step found?
did it succeed?
was continue-on-error active?
~~~

Those belong to the later composition in dependency_exercise.py.

This keeps the policy testable independently.

---

## 15. Runtime composition starts only from supported static evidence

Current coverage owner:

~~~text
src/upgradepilot/ci/dependency_exercise.py
~~~

Static CI evidence is classified first.

For consumption:

~~~text
supported
not_established
unresolved
~~~

Only supported exact static occurrences become runtime-strengthening candidates.

Likewise direct exercise has its own static classification.

The runtime layer does not create a package relationship that static evidence failed to establish.

That direction matters:

~~~text
static proposition first
→ runtime may strengthen it

runtime step success
→ must not invent missing static package meaning
~~~

---

## 16. Static dependency consumption and direct exercise remain different axes

A workflow can:

~~~text
install/consume the changed dependency
~~~

without directly invoking that package.

And it can contain a package invocation without a sound established consumption relationship.

Therefore current workflow results preserve:

~~~text
consumption_state
direct_exercise_state
runtime_consumption_state
runtime_direct_exercise_state
~~~

separately.

Direct exercise requires, at static level:

~~~text
supported dependency consumption
+
direct changed-package invocation
+
bounded ordered_after relation
~~~

Only then can the invocation become a direct-exercise runtime-strengthening candidate.

This avoids:

~~~text
pytest appears somewhere
→ therefore the changed pytest dependency was directly exercised after installation
~~~

without the required source relationship.

---

## 17. Correlation is computed before candidate-level runtime interpretation

For a workflow, CI builds:

~~~text
WorkflowRuntimeCorrelationResult
~~~

Possible broad states:

~~~text
correlated
unresolved
~~~

If workflow correlation itself is unresolved, supported static evidence is not erased.

Instead runtime strengthening can preserve:

~~~text
static fallback
~~~

This is a central product behavior:

> **Failure to strengthen evidence should not destroy weaker evidence that was already established independently.**

---

## 18. Exact owning runtime step is found by job + static step identity

For an eligible candidate, composition looks for the retained correlated owning step using:

~~~text
job_key
step_source_index
~~~

The exact command location remains important for occurrence identity/eligibility, while runtime GitHub records are currently step-level.

If the overall workflow bridge is correlated but the candidate's exact owning step cannot be retained/matched, the stronger proposition remains unresolved.

The product does not silently choose another runtime step.

---

## 19. continue-on-error can block positive interpretation

Even an eligible occurrence may belong to a step whose static definition contains:

~~~text
continue-on-error: true
~~~

or a dynamic/non-false value.

In that case, a successful-looking step conclusion cannot be interpreted as unmasked positive runtime evidence.

Current result:

~~~text
state = unresolved
basis = continue_on_error_unresolved
~~~

This is an important difference between:

~~~text
runtime observation
and
interpretation of that observation
~~~

GitHub may factually report the step status/conclusion.

But the step configuration can prevent UpgradePilot from assigning the stronger positive meaning.

---

## 20. Completed/successful owning step can establish bounded support

After:

~~~text
eligible exact occurrence
+ exact owning step correlation
+ no visible continue-on-error masking
~~~

the runtime record is inspected.

If:

~~~text
status = completed
conclusion = success
~~~

the candidate-level result becomes:

~~~text
state = supported
basis = supported
~~~

The detail preserves:

~~~text
job
step index
source order
runtime step number
factual status/conclusion
~~~

This earns the bounded proposition:

> **Runtime-Correlated Support for this exact static occurrence.**

Use that wording precisely.

Do not silently rename it to:

~~~text
command executed successfully
~~~

because the product intentionally does not claim direct command-level instrumentation.

---

## 21. Non-successful runtime outcomes remain factual

Suppose an eligible consuming step is correlated but GitHub reports:

~~~text
status = completed
conclusion = failure
~~~

Current behavior preserves that factual result and returns no positive runtime strengthening.

The detail explicitly avoids attributing the failure to the internal dependency command itself.

The correct mental model is:

~~~text
eligible occurrence
+ owning step failed
→ positive Runtime-Correlated Support not established

but
→ do not claim the dependency command caused the failure
~~~

Likewise skipped or otherwise non-successful outcomes remain factual runtime evidence.

This is another recurring UpgradePilot discipline:

> **Observed broader failure is not automatic causal attribution to the specific dependency proposition.**

---

## 22. Candidate result basis explains why strengthening did or did not happen

Internally, runtime-strengthening candidate results preserve a basis such as:

~~~text
supported
eligibility_ineligible
eligibility_unresolved
workflow_correlation_unresolved
step_correlation_unresolved
continue_on_error_unresolved
runtime_non_success
~~~

These are not all equivalent.

They tell later aggregation whether:

~~~text
we positively earned support
we understood the structure and rejected strengthening
we lacked enough evidence
the workflow bridge failed
the exact step was missing
masking semantics blocked interpretation
the runtime outcome was factually non-successful
~~~

That distinction is what enables honest static fallback versus broader unresolved behavior.

---

## 23. Static fallback is a first-class outcome

Suppose static consumption is supported, but runtime strengthening is not earned.

Examples:

~~~text
conditional occurrence
→ ineligible

short-circuit occurrence
→ unresolved

workflow names cannot be correlated
→ correlation unresolved
~~~

The existing static support can still survive.

At the workflow level this can yield:

~~~text
supported_not_correlated
~~~

Meaning approximately:

> Exact static changed-dependency consumption is supported, but the current bounded runtime bridge did not safely strengthen it.

This is **not** the same as:

~~~text
no dependency consumption evidence
~~~

and not the same as:

~~~text
runtime command did not execute
~~~

---

## 24. supported_runtime_correlated is stronger but still bounded

Top-level CI state:

~~~text
supported_runtime_correlated
~~~

means at least one supported static dependency-consumption occurrence has earned valid runtime-correlated support.

Its current docstring explicitly limits the claim.

It does not establish:

~~~text
exact resolved version
selected wheel
artifact identity
compatibility
full behavioral exercise
~~~

The current product-flow audit relies on exactly this distinction.

A green correlated install-related step cannot be promoted into exact installed-version or wheel-compatibility evidence.

---

## 25. Existential aggregation: one valid occurrence can establish the positive workflow proposition

A workflow may contain multiple relevant occurrences:

~~~text
candidate A → ineligible/unresolved
candidate B → eligible + correlated success
~~~

Current aggregation is existential:

~~~text
at least one exact occurrence earns valid Runtime-Correlated Support
→ runtime consumption aggregate = supported
~~~

The weaker candidate is not erased.

But it is also not allowed to veto a separate valid positive witness.

This distinguishes:

~~~text
every candidate is proven
~~~

from:

~~~text
at least one candidate establishes the current positive coverage proposition
~~~

Tests explicitly protect this.

---

## 26. Material runtime problems can dominate over simple static fallback

Not every failure to strengthen is equally weak.

If candidate results expose material runtime issues such as:

~~~text
exact step correlation missing
continue-on-error unresolved
runtime non-success
~~~

the aggregate can become broader:

~~~text
unresolved
or not_established
~~~

rather than merely saying static fallback.

This preserves the fact that the runtime path itself produced decision-relevant adverse/uncertain evidence.

By contrast, pure eligibility limitations can retain the weaker static result without pretending the runtime system observed a contradictory outcome.

---

## 27. Current top-level CI coverage states

Current:

~~~text
DependencyCICoverageState
~~~

includes:

~~~text
supported_runtime_correlated
supported_not_correlated
no_successful_ci
unresolved
~~~

These states should not be read as verdicts about upgrade safety.

### supported_runtime_correlated

A bounded static dependency-consumption occurrence earned runtime-correlated support.

### supported_not_correlated

Static consumption is supported; runtime strengthening was not safely established.

### no_successful_ci

The exact-head workflow evidence did not provide a completed successful CI job/run basis under the current rule.

### unresolved

The available evidence does not support a stronger trustworthy classification, or material runtime/static uncertainty remains.

None of these means:

~~~text
safe to merge
compatible
all relevant behavior tested
~~~

---

## 28. Green CI is not the same as dependency coverage

The current evaluator first asks whether exact-head runtime CI exists.

But even if the workflow/job is successful:

~~~text
green exact-head CI
!= changed dependency consumption established
~~~

The static workflow must independently establish the dependency relationship.

Likewise:

~~~text
green job
+ static dependency consumption
!= runtime-correlated support
~~~

until the eligible occurrence and exact runtime step bridge are established.

This yields the evidence ladder:

~~~text
successful exact-head CI
        ↓
supported static dependency consumption
        ↓
eligible exact static occurrence
        ↓
exact owning-step runtime correlation
        ↓
unmasked completed-successful runtime step
        ↓
bounded runtime-correlated support
~~~

Each arrow is a separate proof obligation.

---

## 29. Real case S001 — sole ordinary top-level command

Historical final proof used:

~~~text
S001 Pydantic / soupsieve
uv sync --all-packages --group docs
~~~

The command shape was:

~~~text
sole ordinary top-level command
~~~

and the selected execution profile was admitted.

Therefore:

~~~text
exact static consumption occurrence
+ sole-command positive relation
+ admitted profile
→ eligible
~~~

With exact runtime step correlation and successful unmasked runtime outcome, it can earn bounded Runtime-Correlated Support.

What this adds over Note 1:

~~~text
static selected uv environment/reachability
→ already established consumption

runtime strengthening
→ adds bounded evidence about the owning step's successful runtime result
~~~

What it still does not prove:

~~~text
exact soupsieve version installed
wheel identity
compatibility
all docs behavior exercised
~~~

---

## 30. Real case S002 — first sequential Bash command

Historical final proof used a shape like:

~~~text
first dependency-install command
second ordinary Bash command
~~~

The first install occurrence received:

~~~text
first_ordinary_top_level_command_in_sequential_script
~~~

Under the admitted GitHub Bash/sh execution profile:

~~~text
→ eligible
~~~

This case is important because restricting positive runtime strengthening to one-command steps would have unnecessarily discarded useful real product coverage.

But the rule remains narrow:

~~~text
first sequential Bash/sh command
!= arbitrary later command in any linear script
~~~

The architecture retained useful coverage without pretending to solve general shell execution.

---

## 31. Real case S004 — short-circuit remains deferred

Historical proof used a glyphsLib/pytest shape like:

~~~text
. ./generate/bin/activate && pip install ...
~~~

The relevant occurrence carried:

~~~text
short_circuit
~~~

and no admitted positive whole-step relation.

Current policy:

~~~text
→ unresolved
→ no runtime strengthening
~~~

This is intentional.

It demonstrates that the system prefers:

~~~text
preserve useful static evidence
+ withhold stronger runtime inference
~~~

over:

~~~text
broaden shell semantics merely to make more cases positive
~~~

S004 is therefore a re-entry pressure case, not a failed implementation.

---

## 32. Conditional success case — static fallback is correct

A focused regression test uses:

~~~text
if false; then
    pip install -r requirements-dev.txt
fi
~~~

with a successful owning runtime step.

Expected result:

~~~text
static consumption = supported
runtime consumption = not_established
workflow coverage = supported_not_correlated
~~~

and the static occurrence retains:

~~~text
conditional
~~~

This is one of the clearest demonstrations of the architecture.

The parser is correct to preserve the pip command.

The dependency/CI static layer is correct to preserve the declaration.

The runtime-strengthening policy is correct to reject positive strengthening.

No layer has to lie to make the others simple.

---

## 33. Short-circuit case — unresolved is different from ineligible

Another focused test uses:

~~~text
false || pip install -r requirements-dev.txt
~~~

Static occurrence exists and consumption can be supported.

But current strengthening policy has no admitted positive relation for the short-circuit occurrence.

Expected runtime strengthening:

~~~text
unresolved
~~~

while workflow-level evidence can preserve:

~~~text
supported_not_correlated
~~~

Why unresolved rather than ineligible?

Because current policy has not encoded a complete negative theorem for every short-circuit shape.

The distinction is:

~~~text
conditional body
→ known ineligible under current rule

short_circuit coarse structure
→ current stronger relationship unresolved
~~~

This prevents policy overreach.

---

## 34. continue-on-error case — successful step can still be unusable for positive strengthening

Focused coverage protects:

~~~text
continue-on-error: true
run: pip install -r requirements-dev.txt
~~~

Even with an otherwise eligible sole-command occurrence and a successful-looking correlated runtime step:

~~~text
runtime strengthening = unresolved
~~~

because the step's conclusion can be masked by configuration.

This is why strengthening requires more than:

~~~text
status=completed
conclusion=success
~~~

The step configuration participates in the interpretation boundary.

---

## 35. Failed eligible step preserves factual non-success

A focused case uses an eligible install step with:

~~~text
status = completed
conclusion = failure
~~~

The product preserves those exact facts in the runtime-consumption detail.

It does not rewrite them into:

~~~text
runtime status unknown
~~~

and does not claim:

~~~text
dependency command caused failure
~~~

This distinction matters downstream.

A factual runtime failure is stronger evidence than generic “could not correlate,” but still weaker than causal diagnosis.

---

## 36. Skipped consuming step does not become positive execution

A correlated static consuming step may have runtime:

~~~text
conclusion = skipped
~~~

The exact step bridge can still be correlated.

But positive runtime support is not established.

The important model is:

~~~text
correlation
!= successful execution evidence
~~~

Correlation answers:

~~~text
which runtime step belongs to this static step?
~~~

Status/conclusion answers:

~~~text
what GitHub reported for that runtime step?
~~~

Runtime strengthening combines them only under the admitted rule.

---

## 37. Direct exercise is runtime-strengthened independently

Suppose one job has:

~~~text
Install test dependencies
→ pip install -r requirements-dev.txt

Exercise pytest
→ pytest tests
~~~

Static composition can establish:

~~~text
dependency consumption = supported
direct exercise = supported
~~~

Then runtime strengthening independently evaluates:

~~~text
consumption occurrence
direct-exercise invocation occurrence
~~~

Both can earn runtime-correlated support if their exact candidates satisfy the policy.

This prevents one positive axis from silently proving the other.

For example:

~~~text
install step supported at runtime
!= direct package exercise supported at runtime
~~~

unless the direct invocation has its own exact evidence.

---

## 38. Why runtime logs were not used as the primary correction

ADR-0009 deliberately did not solve this problem by scraping arbitrary job logs.

Logs could eventually become a separate evidence source.

But they introduce their own questions:

~~~text
completeness
command echo behavior
shell/wrapper transformations
redaction
format stability
identity/provenance
what exactly a line proves
~~~

The current architecture first establishes trustworthy static source structure and a bounded step-level strengthening rule.

That is smaller and more explicit than assuming logs are a command-execution ledger.

Future log/artifact evidence requires a separately selected proposition and acquisition boundary.

---

## 39. Current source responsibilities

### workflow_command_analysis.py

Owns:

~~~text
parser-backed static occurrences
structural_context
whole_step_relation
~~~

Does not own runtime eligibility.

### workflow_command_shell.py

Owns:

~~~text
syntax family
execution profile
~~~

Does not claim execution.

### runtime_strengthening.py

Owns:

~~~text
RuntimeStrengtheningCandidate
eligible | ineligible | unresolved
~~~

Does not correlate runtime steps or interpret runtime conclusions.

### workflow_runtime_correlation.py

Owns:

~~~text
static job/step ↔ runtime job/step identity
~~~

Does not assign dependency meaning or success implications.

### dependency_exercise.py

Owns the final CI composition:

~~~text
static consumption/direct exercise
+ eligibility
+ correlation
+ continue-on-error
+ factual runtime outcome
→ workflow/top-level CI coverage state
~~~

This owner map is worth memorizing conceptually even if function names remain lookup-assisted.

---

## 40. Why the ownership split is necessary

A tempting monolithic function could try to answer:

~~~text
did CI test the changed dependency?
~~~

in one step.

But that phrase hides several independently fallible propositions:

~~~text
did exact-head CI run?
which source command exists?
does it consume the changed dependency?
which internal occurrence?
is its source structure compatible with step-level strengthening?
which runtime step owns the static step?
did GitHub report that step successful?
was success masked?
did the package get directly invoked afterward?
~~~

By keeping these propositions separate, UpgradePilot can preserve:

~~~text
where uncertainty entered
what evidence is still valid
what stronger claim was not earned
~~~

This is the core reason the architecture looks more explicit than a simple green/red CI check.

---

## 41. What supported_runtime_correlated really means

Use the phrase carefully.

It means approximately:

> At least one exact supported static changed-dependency consumption occurrence has an admitted static structural/profile relationship to its owning run step, that static step has been deterministically correlated to an exact-attempt runtime step, and GitHub reports the step completed successfully without visible continue-on-error masking.

It does **not** mean:

> We directly observed that exact shell command execute and succeed.

The distinction may feel conservative, but it is intentional.

The model records an evidence-supported inference from:

~~~text
source structure
+
GitHub wrapper semantics
+
owning-step runtime outcome
~~~

not command-level instrumentation.

---

## 42. What this evidence can and cannot support downstream

### It can strengthen

~~~text
confidence that the changed-dependency consumption proposition
has runtime support in the admitted bounded shape
~~~

### It cannot by itself answer

~~~text
which dependency version was actually resolved/installed
whether installation used wheel or source
which wheel filename/tags were selected
whether exact target compatibility holds
whether tests covered affected behavior sufficiently
whether the update should be merged
~~~

This boundary is directly relevant to the current parent product work.

The September 19 end-to-end audit explicitly preserves:

~~~text
runtime-correlated CI support
!= exact installed dependency/artifact identity
~~~

Do not reopen Cycle 3 merely because downstream evidence needs a stronger proposition.

That stronger fact needs its own producer.

---

## 43. Proof strategy and historical closure

Cycle 3 was implemented and proven in stages.

Historical final hosted proof:

~~~text
GitHub Actions run: 35448172928
Python 3.12.14
fresh pip install .
pip check
installed CLI checks
focused investigation: 15/15
Cycle-3 focused regression: 76/76
full deterministic product regression: 604/604
~~~

Real-case boundary proof:

~~~text
S001
sole ordinary top-level command
→ eligible

S002
first sequential Bash command
→ eligible

S004
short-circuit &&
→ unresolved/deferred
~~~

These historical results establish the implementation/proof horizon that this learning artifact teaches.

This authoring operation itself is **not** a fresh test run.

---

## 44. What the test families protect

Primary current anchors include:

~~~text
tests/test_ci_runtime_strengthening.py
tests/test_workflow_runtime_correlation.py
tests/test_ci_runtime_correlated_dependency_coverage.py
tests/test_parser_backed_ci_command_evidence.py
tests/test_static_command_order.py
~~~

They protect behavior such as:

~~~text
sole-command eligibility
first-sequential Bash eligibility
PowerShell first-sequential non-admission
known ineligible structures
coarse/unadmitted unresolved structures
custom shell unresolved
missing exact command identity unresolved
two same-step occurrences remain distinct
direct-exercise candidate identity
static/runtime workflow revision coherence
job/step identity matching
correlation ambiguity stays unresolved
conditional success preserves static fallback
short-circuit remains unresolved
continue-on-error blocks positive interpretation
failed/skipped runtime outcomes stay factual
one positive candidate can establish existential support
consumption and direct exercise remain separate axes
~~~

These tests are executable specifications of the current bounded rule.

---

## 45. Engineering progression worth retaining

The important progression is:

~~~text
earlier bridge:
static user-defined step ↔ runtime step
        ↓
new correctness pressure:
one step can contain multiple internal commands
        ↓
provider correction:
exact command identity + structural context
        ↓
design correction:
step success cannot strengthen every command
        ↓
new policy boundary:
RuntimeStrengtheningCandidate
+ eligible | ineligible | unresolved
        ↓
positive relation families:
sole command
first sequential Bash/sh command
        ↓
runtime composition:
exact owning-step correlation
+ continue-on-error
+ factual status/conclusion
        ↓
bounded Runtime-Correlated Support
        ↓
aggregate:
supported_runtime_correlated
or static fallback/unresolved
~~~

The transferable lesson is:

> **When broader runtime evidence is used to strengthen a narrower internal proposition, the relationship between the two must be independently justified.**

---

## 46. Current fact, rationale, judgment, and re-entry boundary

### Current implementation fact

UpgradePilot now has a bounded occurrence-level runtime-strengthening architecture over exact static dependency-consumption and direct-exercise evidence.

It supports:

~~~text
sole ordinary top-level commands
first sequential Bash/sh commands
~~~

under selected execution profiles, and conservatively handles known disqualifying or unresolved structures.

### Evidenced rationale

ADR-0009, the implementation plan, current source/tests, the false-positive examples, and Cycle-3 proof consistently support the same boundary:

~~~text
step success cannot generally prove internal command execution
~~~

### Engineering judgment

The current design is intentionally narrower than general shell execution semantics.

That is proportionate because it earns useful real-case positives while avoiding a universal shell interpreter or unsupported inference.

### Re-entry triggers

Revisit only when real product pressure justifies a new stronger proposition or positive family, for example:

~~~text
recurring decision-critical short-circuit shape
command-level runtime evidence with trustworthy identity/completeness
new execution-profile semantics
new CI provider creating provider-neutral pressure
a selected downstream action requiring stronger installed-version/artifact evidence
~~~

Do not broaden simply to increase the count of correlated-positive cases.

---

## 47. Depth calibration

### Must own

- step correlation is not occurrence strengthening;
- exact command identity must survive into the runtime candidate;
- eligible, ineligible, and unresolved have different meanings;
- sole-command and first-sequential Bash/sh are current positive families;
- known conditional/loop/etc structures can be ineligible;
- short-circuit and other unadmitted structures can remain unresolved;
- correlation requires exact revision/job/step identity;
- continue-on-error can invalidate positive interpretation;
- non-successful runtime outcomes remain factual without causal attribution;
- static support survives when stronger runtime evidence is not earned;
- one valid occurrence can establish existential workflow support;
- consumption and direct exercise are separate runtime axes;
- supported_runtime_correlated is not direct inner-command execution proof;
- this evidence does not prove exact installed version/artifact/compatibility/action.

### Understand operationally

- RuntimeStrengtheningCandidate fields;
- workflow_runtime_correlation bounded matching model;
- candidate classification basis/disposition;
- static fallback versus broader unresolved;
- top-level CI coverage states;
- how runtime step number/status/conclusion are preserved.

### Lookup-level

- every correlation helper;
- every result reason string;
- exact dataclass field order;
- all shell grammar details;
- complete GitHub Actions execution semantics.

### Deferred

- general shell CFG/path execution;
- S004 short-circuit admission;
- runtime log/artifact parsing;
- exact installed dependency/wheel evidence;
- target wheel-tag production;
- maintainer-action enablement.

---

## 48. Fast relearning route

Use this sequence:

~~~text
1. Recall:
   static command exists != command executed.

2. Open:
   ci/runtime_strengthening.py
   and inspect:
   RuntimeStrengtheningCandidate
   eligible | ineligible | unresolved.

3. Read tests:
   sole command
   first sequential Bash
   conditional/ineligible
   short-circuit/unresolved
   custom shell/unresolved.

4. Open:
   ci/workflow_runtime_correlation.py
   and explain why correlation is identity only.

5. Open:
   ci/dependency_exercise.py
   and trace one supported candidate:
   eligibility
   → exact step match
   → continue-on-error
   → runtime status/conclusion
   → candidate result.

6. Trace aggregation:
   one supported candidate
   → existential runtime support.

7. Read one conditional-success test
   and one failed/skipped test.

8. Revisit:
   S001 / S002 / S004.

9. State the non-claims:
   no exact installed version,
   no wheel identity,
   no compatibility,
   no maintainer action.
~~~

---

## 49. Ownership / transfer questions

Without looking at this note, explain:

1. Why is exact static↔runtime step correlation insufficient to strengthen every command inside the step?
2. What information must a RuntimeStrengtheningCandidate preserve that a simple job/step tuple cannot?
3. Why is a conditional occurrence ineligible while a short-circuit occurrence can remain unresolved?
4. Why does a custom Bash shell template reuse Bash syntax but remain unresolved for runtime strengthening?
5. Why can the first sequential Bash command be eligible while an arbitrary later linear command is not?
6. What exactly does workflow_runtime_correlation prove?
7. Why does continue-on-error change interpretation even when GitHub reports the step successful?
8. Why does a failed eligible step not prove that the dependency command caused the failure?
9. Why should static support survive when runtime correlation is unavailable?
10. Why can one supported occurrence establish the workflow's positive runtime-correlated consumption proposition without proving every occurrence?
11. Why is runtime direct exercise a separate axis from runtime dependency consumption?
12. What new evidence producer would be required before UpgradePilot could claim the exact installed dependency version?

### Transfer exercise

Consider:

~~~text
- name: Install and test
  run: |
    pip install -r requirements-dev.txt
    pytest tests
~~~

Assume:

~~~text
Bash default profile
exact static job/step correlation
runtime step completed/successful
no continue-on-error
~~~

Predict separately:

~~~text
pip occurrence eligibility
pytest occurrence eligibility
runtime-correlated dependency consumption
static direct exercise
runtime-correlated direct exercise
exact installed dependency version
~~~

Then change the first line to:

~~~text
false || pip install -r requirements-dev.txt
~~~

and explain which conclusions change and why.

---

## 50. Evidence anchors

Pinned source/test horizon:

~~~text
main@7e067aa8e749ec79d93e9b47dbf6c3e752b38932
~~~

Primary current source:

~~~text
src/upgradepilot/github/workflow_command_analysis.py
src/upgradepilot/github/workflow_command_shell.py
src/upgradepilot/ci/runtime_strengthening.py
src/upgradepilot/ci/workflow_runtime_correlation.py
src/upgradepilot/ci/dependency_exercise.py
src/upgradepilot/ci/static_command_order.py
~~~

Primary current tests:

~~~text
tests/test_ci_runtime_strengthening.py
tests/test_workflow_runtime_correlation.py
tests/test_ci_runtime_correlated_dependency_coverage.py
tests/test_parser_backed_ci_command_evidence.py
tests/test_static_command_order.py
~~~

Architecture / completed implementation coordination:

~~~text
docs/architecture/ADR-0009-parser-backed-static-workflow-command-analysis.md
plans/STATIC_WORKFLOW_COMMAND_ANALYSIS_AND_RUNTIME_STRENGTHENING_IMPLEMENTATION_PLAN.md
~~~

Directly relevant engineering records:

~~~text
working-memory/2026-09-17_cycle3-runtime-strengthening-phase-a-orientation.md
working-memory/2026-09-18_cycle3-runtime-strengthening-build.md
working-memory/2026-09-19_cycle3-integrated-learning-review.md
~~~

Historical prerequisite learning snapshot:

~~~text
learning/2026-09-12-ci-static-runtime-correlation-bridge.md
~~~

Current package prerequisite:

~~~text
learning/2026-09-19-parser-backed-ci-command-evidence-and-runtime-strengthening/
  01_parser_backed_static_workflow_command_evidence_and_consumer_composition.md
~~~

This file is a learning snapshot, not a specification, architecture decision, live-state owner, or product-change authorization.

UP-SKILL:upgradepilot-learning-artifact
