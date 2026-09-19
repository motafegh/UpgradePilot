# Architecture Evolution, Proof Strategy, and Engineering Corrections

**Learning-artifact date:** 2026-09-19  
**Current evidence horizon:** main@0e15299d5f8ff80b536669a162a8a221440d1f8f  
**Roadmap responsibility:** Group 11 — architecture evolution, proof strategy, and engineering corrections  
**Artifact shape:** one retrospective/design note  
**Primary responsibility:** understand how UpgradePilot repeatedly corrected its architecture when implementation evidence exposed the wrong responsibility boundary, weak ownership, misleading names, insufficient proof, or a local patch that would preserve a deeper defect  
**Target depth:** implementation-adjacent engineering-ownership depth

This note is not another walkthrough of the current CI parser or product flow.

Those are already covered by Groups 8 and 10.

This note teaches the more transferable question:

> **How did UpgradePilot decide when to reset, refactor, share, split, rename, migrate, prove, or deliberately stop?**

The shortest evolution is:

~~~text
obsolete inherited implementation
→ clean active-source reset

flat growing package
→ responsibility-based subpackages

duplicated cross-consumer source interpretation
→ shared provider-owned structural representation

unclear proof-strength terminology
→ static/runtime evidence separation

duplicated textual shell splitting
→ parser-backed shared command structure

step-level runtime correlation
→ exact occurrence-level strengthening policy

project-local execution shorthand
→ semantic responsibility naming

local/focused tests
→ boundary/integration proof
→ full deterministic regression
→ installed/hosted proof where the proposition required it
~~~

The recurring principle is:

> **Correct the earliest sufficient owner of the broken proposition instead of repeatedly compensating downstream.**

---

## 1. Why this retrospective matters

UpgradePilot did not arrive at its current structure in one architecture pass.

Several earlier decisions were reasonable at their original scale and later became insufficient when real implementation pressure appeared.

That distinction matters.

A mature engineering response is not:

~~~text
old design changed
→ old design was stupid
~~~

It is:

~~~text
old design fit earlier evidence
→ new responsibilities exposed a real limitation
→ inspect the proposition and ownership
→ make the smallest durable correction
→ prove migration separately from new product behavior
~~~

This is the pattern worth retaining.

---

## 2. The first major correction: clean-slate B2 reset

Primary owner:

~~~text
docs/architecture/ADR-0003-clean-slate-b2-source-reset.md
~~~

Before B2, UpgradePilot already had an M2-era implementation containing:

~~~text
manual case identity
normalized evidence
one narrow decision rule
local-LLM semantic extraction
input-risk experiments
tests/scripts/evaluation outputs
~~~

But D1 simulations changed the required product boundary.

The project was no longer simply continuing the same narrow runtime.

Continuing from the old source would have imported assumptions that were not independently justified by the new responsibility.

---

## 3. Why archive-and-rewrite was chosen instead of incremental modification

The accepted decision was:

~~~text
preserve old implementation exactly in Git/archive
BUT
remove it from the active product/test path
AND
re-derive new behavior from current requirements/evidence
~~~

This is more subtle than deleting old work.

The old implementation remained:

~~~text
historical evidence
possible comparison input
recoverable provenance
~~~

but not:

~~~text
current architecture authority
active code library
automatic compatibility obligation
proof of current behavior
~~~

The important lesson is:

> **Historical implementation value and current implementation authority are different things.**

---

## 4. The reset also reset proof obligations

ADR-0003 explicitly accepted a cost:

~~~text
old passing tests
!= current product proof
~~~

Once active source was reset:

~~~text
new current contracts
→ new current implementation
→ new current tests
→ fresh install/import/runtime proof where required
~~~

This prevents a common engineering mistake:

~~~text
we used to have tests for something similar
→ therefore current behavior is covered
~~~

A proof belongs to the exact implementation/proposition horizon it exercised.

---

## 5. B1/B2 source and test reconciliation enforced that rule

The B1 current-source/test reconciliation work used the clean reset as a starting boundary.

The important model was:

~~~text
current source responsibility
↔ current active tests
↔ current admitted runtime behavior
~~~

Historical tests could inform design.

They could not remain silently counted as active product regression.

This established an important discipline used later throughout UpgradePilot:

> **Tests are evidence for the implementation they actually exercise, not reusable reputation points.**

---

## 6. The next pressure: a flat package stopped communicating ownership

ADR-0001 had originally kept:

~~~text
src/upgradepilot/
~~~

mostly flat.

That was deliberate.

Subpackages had been deferred until implementation demonstrated stable responsibility boundaries.

By August 2026, that trigger had been reached.

The package had durable families for:

~~~text
GitHub acquisition / identity
PyPI evidence
dependency extraction
CI interpretation
upstream authority
target evidence
application orchestration
CLI presentation
~~~

At that point the flat structure started obscuring rather than simplifying ownership.

---

## 7. ADR-0007: responsibility-based subpackages

Primary owner:

~~~text
docs/architecture/ADR-0007-responsibility-based-python-subpackages.md
~~~

The accepted structure kept:

~~~text
src/upgradepilot/
~~~

but organized real product responsibilities into bounded subpackages such as:

~~~text
dependency/
github/
pypi/
ci/
upstream/
target/
~~~

with application/interface owners such as:

~~~text
investigation.py
cli.py
~~~

remaining explicit.

The key rule was:

> **Create structure after stable responsibilities exist, not before.**

---

## 8. Why this was not just folder cleanup

ADR-0007 was not primarily cosmetic.

It clarified:

~~~text
who owns provider syntax
who owns dependency semantics
who owns CI interpretation
who owns target evidence
who owns orchestration
who owns presentation
~~~

It also separated executable categories:

~~~text
src/upgradepilot/
→ installable product runtime

tests/
→ deterministic product regression

experiments/
→ non-product research/evaluation

tools/
→ developer-operated diagnostics/live proof/maintenance
~~~

That distinction affects:

~~~text
trust
packaging
test meaning
dependency direction
lifecycle
proof interpretation
~~~

So file location became an architectural statement.

---

## 9. Cohesion and coupling became explicit design questions

A responsibility-based package should maximize **cohesion**:

~~~text
things inside the owner
→ participate in the same conceptual responsibility
~~~

and reduce accidental **coupling**:

~~~text
one responsibility
→ should not depend on unrelated implementation details
of another responsibility
~~~

This led to patterns such as:

~~~text
GitHub provider semantics
→ upgradepilot.github

dependency-selection meaning
→ upgradepilot.dependency

CI composition
→ upgradepilot.ci
~~~

The goal was not the smallest number of imports.

The goal was the clearest dependency direction.

---

## 10. Current source-topology tests protect architecture, not features

Current test owner:

~~~text
tests/test_source_topology.py
~~~

The test file explicitly says it protects:

~~~text
accepted responsibility-based source topology
~~~

not product feature behavior.

It verifies things such as:

~~~text
preferred responsibility owners import correctly
package root remains intentionally minimal
obsolete flat module paths stay absent
~~~

This demonstrates an important testing distinction:

~~~text
architecture/topology test
!= feature test
~~~

Both are valid, but they prove different propositions.

---

## 11. Structural migration can fail even when architecture is correct

The August 4 source-reconciliation migration produced a real failure.

Observed error:

~~~text
ImportError:
cannot import name 'repository_relative_path_parts'
from 'upgradepilot.repository_path'
~~~

The actual owner exported:

~~~text
repository_relative_parts
~~~

Several test modules and the CLI path failed because two migrated dependency consumers imported the wrong symbol name.

This was a migration wiring defect.

It was not evidence that the responsibility-based architecture itself was wrong.

---

## 12. Diagnose the smallest real failure

The useful diagnosis was:

~~~text
architecture decision:
shared source-neutral path helper owner
→ correct

consumer migration:
typed wrong imported symbol
→ defect
~~~

The project did not respond by:

~~~text
undoing subpackages
adding duplicate helper aliases everywhere
weakening path validation
~~~

It corrected the exact consumer imports.

This is a reusable lesson:

> **When a broad refactor fails, first classify whether the failure invalidates the architecture or only the migration.**

Do not treat all red tests as architecture rejection.

---

## 13. Independent proof prevented overdiagnosis

During that same failed migration run, the exact-commit changelog-discovery path still passed.

Why?

Because that path did not import the broken dependency modules.

This mattered.

The correct statement was:

~~~text
dependency import chain broken

BUT

independent GitHub/changelog behavior still valid
~~~

not:

~~~text
entire refactor broken
~~~

This shows why isolated proof paths are useful during structural changes.

They help localize failure.

---

## 14. Structural migration must preserve behavior, not just imports

Another migration correction involved Git object IDs.

A first centralized validator draft admitted only:

~~~text
40-character lowercase SHA-1
~~~

But existing behavior had already established a broader invariant:

~~~text
40- or 64-character hexadecimal immutable object ID
uppercase accepted and normalized
movable refs rejected
~~~

The shared validator was corrected before migration completed.

The lesson is:

> **A refactor that centralizes code must preserve already-proven semantics unless the behavior change is separately authorized.**

Centralization is not permission to narrow behavior accidentally.

---

## 15. Migration compatibility can be temporary and deliberate

A target-Python dataclass migration exposed another subtle issue.

The state field was conceptually constant:

~~~text
state = available
~~~

A tempting cleanup used:

~~~text
init=False
~~~

But current tests/fixtures still explicitly supplied the value.

The corrected migration used a normal default instead.

That allowed:

~~~text
new callers
→ omit the constant

transitional callers
→ still pass it explicitly
~~~

without creating a second model.

This is a good example of **bounded migration compatibility**.

Compatibility was retained because an actual transition needed it, not because all historical internal APIs must live forever.

---

## 16. Cross-responsibility pressure exposed a new architectural problem

After responsibility-based packaging, two different consumers began interpreting overlapping GitHub Actions workflow source:

~~~text
CI
→ dependency consumption/exercise

Target
→ target environment/configuration evidence
~~~

Both needed overlapping structure such as:

~~~text
jobs
run steps
pip/requirements declarations
working-directory/source context
~~~

But their conclusions were different.

This triggered the B2 cross-responsibility architecture reconciliation.

---

## 17. The key rule: share meaning, not merely syntax

The reconciliation stated:

~~~text
same raw syntax
!= same domain conclusion
~~~

This is one of the strongest architecture lessons in the project.

A shared provider-owned parser can be justified when the shared proposition is:

~~~text
what does this GitHub Actions source structurally declare?
~~~

But CI-specific conclusions such as:

~~~text
changed dependency consumed
~~~

and Target-specific conclusions such as:

~~~text
target environment declaration established
~~~

must remain in their own owners.

Shared structure does not justify shared domain meaning.

---

## 18. ADR-0008 established the provider-owned workflow-definition IR

Primary owner:

~~~text
docs/architecture/ADR-0008-bounded-static-github-actions-workflow-definition.md
~~~

The accepted direction became:

~~~text
RepositoryTextFile
→ bounded GitHub Actions static workflow-definition IR
   owner = upgradepilot.github
→ CI interpreter
→ Target interpreter
~~~

This moved common GitHub Actions structure to the earliest sufficient owner.

Why GitHub rather than a generic common package?

Because the syntax/semantics remained specifically GitHub Actions.

Shared across consumers:

~~~text
!=
source-neutral
~~~

---

## 19. Earliest sufficient owner is more precise than “DRY”

It would be easy to describe ADR-0008 as:

~~~text
remove duplication
~~~

but that is incomplete.

The stronger design question is:

> **What is the earliest layer that can truthfully own this proposition without importing downstream meaning?**

For workflow structure:

~~~text
provider layer
→ can own source structure

dependency layer
→ can own dependency command meaning

CI layer
→ can own CI consumption/exercise meaning

Target layer
→ can own target environment meaning
~~~

This avoids both:

~~~text
duplicated parsing
~~~

and:

~~~text
over-centralized domain semantics
~~~

---

## 20. Static and runtime evidence were deliberately separated

ADR-0008 explicitly preserved:

~~~text
static workflow definition
!= runtime workflow instance
!= runtime success
~~~

Current runtime GitHub evidence remained in:

~~~text
WorkflowRun
WorkflowJob
WorkflowStep
~~~

rather than being merged into one giant workflow object.

Why?

Because one static source definition can have:

~~~text
multiple runtime attempts
matrix expansion
conditional/skipped execution
different concrete runtime jobs
~~~

A broad combined static/runtime model would make identity and proof claims easier to overstate.

---

## 21. Proof-strength language had to be corrected too

Architecture is not only module structure.

Names and states can encode false claims.

For example, early Target wording such as:

~~~text
dependency environment formation = established
~~~

could sound like runtime environment formation even though the evidence came from static workflow declaration.

Likewise early CI wording could make successful run/job evidence + static command recognition sound stronger than it was.

The cross-responsibility reconciliation therefore included semantic correction:

~~~text
static declaration/configuration evidence
must remain static

runtime evidence
must remain separately justified
~~~

---

## 22. Naming is part of correctness when it changes interpretation

Primary standard:

~~~text
docs/specifications/UPGRADEPILOT_NAMING_CLARITY_SPECIFICATION.md
~~~

The core rule is:

> **Use names that let a competent maintainer recover the responsibility without memorizing project history.**

This applies to:

~~~text
source types/functions/modules
tests
plans
plan steps
MEMORY
working memories
learning routes
user-facing guidance
~~~

The concern is not style preference.

A misleading name can cause an engineer to infer the wrong proposition.

---

## 23. Responsibility naming replaced execution-coordinate naming

The project later found that many current artifacts still required remembering internal execution labels.

The correction strengthened current navigation toward names like:

~~~text
bounded LangChain abstraction investigation
cross-implementation architecture comparison
real pydantic Python-support LangGraph evidence-gap smoke
~~~

instead of opaque route/stage codes.

Historical identifiers remain when they are needed for provenance.

But current navigation should describe:

~~~text
what responsibility is owned
~~~

not:

~~~text
where in an old execution sequence it happened
~~~

This reduces cognitive coupling to project history.

---

## 24. Naming migrations also require executable proof

The semantic naming migration was not closed merely because filenames looked better.

The final renamed executable smoke was actually run.

The preserved result included:

~~~text
expected node path match
planner action identity
authority status
target relevance
applicability
product-result match
basic expectation match
~~~

The principle is:

~~~text
behavior-bearing rename/move
→ prove import/execution still works
~~~

whereas docstring-only changes do not require invented testing ceremony.

Proof should be proportional to the changed proposition.

---

## 25. A second major correction appeared in shell-command analysis

After shared workflow-definition parsing existed, the implementation still had another duplication deeper inside run-step text.

Dependency and CI layers independently split shell command strings using simple separators such as:

~~~text
&&
||
;
newline
~~~

That created false positives.

Controlled examples included:

~~~text
pip install wheel # -r requirements-dev.txt
~~~

and:

~~~text
echo "note; pip install -r requirements-dev.txt"
~~~

The local symptom looked like a tokenizer bug.

The deeper problem was larger.

---

## 26. Why patching the splitter was rejected

A quote-aware splitter could fix some immediate examples.

But it would leave:

~~~text
multiple layers reconstructing commands independently
weak shell-structure understanding
no canonical occurrence identity
no reliable structural context
step success still over-broad for internal commands
~~~

Real source such as:

~~~text
true || pip install ...
~~~

or:

~~~text
if false; then
    pip install ...
fi
~~~

showed that lexical correctness alone was insufficient.

This is the clearest example of:

> **Evidence justifying a larger foundational correction instead of repeated local patches.**

---

## 27. ADR-0009 moved command structure to a shared provider owner

Primary owner:

~~~text
docs/architecture/ADR-0009-parser-backed-static-workflow-command-analysis.md
~~~

The accepted architecture became:

~~~text
GitHub Actions RunStepDefinition
+ effective shell context
→ shell-family parser adapter
→ Tree-sitter
→ UpgradePilot-owned parser-neutral command IR
→ dependency consumers
→ CI consumers
→ separate CI runtime-strengthening policy
~~~

The important correction was not merely:

~~~text
use Tree-sitter
~~~

It was:

~~~text
one provider-owned source interpretation
+ one canonical occurrence identity
+ downstream responsibility-specific semantics
~~~

---

## 28. Parser substrate and product IR are separate

Tree-sitter is implementation machinery.

Its syntax-tree nodes do not become normal dependency/CI contracts.

Instead:

~~~text
Tree-sitter CST
→ provider adapter
→ UpgradePilot StaticCommandOccurrence / analysis types
~~~

This keeps:

~~~text
grammar details
~~~

from leaking into:

~~~text
dependency semantics
CI evidence contracts
runtime policy
~~~

The general architecture lesson is:

> **External library representation should usually stop at the adapter boundary when the product owns a more stable domain meaning.**

---

## 29. ADR-0008 and ADR-0009 are complementary, not duplicates

ADR-0008 owns:

~~~text
GitHub Actions YAML/workflow structure
~~~

using PyYAML-backed bounded workflow-definition parsing.

ADR-0009 later owns:

~~~text
shell command structure inside run-step source
~~~

using Tree-sitter shell-family parsing.

Conceptually:

~~~text
GitHub Actions YAML
→ workflow-definition IR
→ RunStepDefinition.command.text
→ shell parser
→ static command IR
~~~

Two different source languages and two different parsing responsibilities exist in one pipeline.

That is more precise than trying to make one parser abstraction cover both.

---

## 30. Canonical identity had to replace overloaded segment indices

Earlier textual splitting used segment indices.

That identifier became unsafe once different layers could segment source differently.

Cycle 2 corrected this with an exact command-source identity:

~~~text
workflow path/revision
job key
step source index
StaticCommandLocation
  → source span
  → source order
~~~

The key distinction is:

~~~text
identity
!= ordering
!= execution
~~~

One field should not silently stand in for all three.

---

## 31. Source order also could not become execution order

After canonical occurrence identity existed, another tempting shortcut remained:

~~~text
source order 0 before source order 1
→ command 0 executed before command 1
~~~

That is not generally true in shell control flow.

So static ordering became its own bounded proposition:

~~~text
ordered_after
not_after
unresolved
~~~

based on structure, not only numeric source position.

This is another example of splitting one overloaded concept into the smallest truthful propositions.

---

## 32. Step-level runtime correlation exposed the next proof gap

UpgradePilot could already correlate:

~~~text
static user-defined workflow step
↔ exact runtime step
~~~

and observe:

~~~text
completed
success
~~~

But one step may contain multiple commands.

Therefore:

~~~text
successful step
!= every internal command executed
~~~

This required a new occurrence-level policy.

The architecture did not solve this by weakening the claim.

It introduced a new explicit responsibility.

---

## 33. Cycle 3 introduced occurrence-level runtime strengthening

The new model became:

~~~text
exact static command occurrence
+ structural context
+ positive whole-step/position relation
+ execution profile
→ eligible | ineligible | unresolved

then

eligible occurrence
+ exact owning runtime step
+ no continue-on-error masking
+ successful runtime outcome
→ bounded Runtime-Correlated Support
~~~

This preserved the useful runtime signal without overstating it as direct command instrumentation.

---

## 34. Eligibility is a design correction, not a parser feature

The parser/provider layer establishes:

~~~text
source structure
whole-step relation
execution-profile evidence
~~~

The CI policy layer decides:

~~~text
can step-level runtime evidence strengthen this occurrence?
~~~

This separation is important.

Otherwise the parser would become responsible for:

~~~text
product-specific runtime inference
~~~

which is not syntax parsing.

Again the project placed meaning at the earliest sufficient owner, but not earlier.

---

## 35. Positive families were added from evidence, not completeness pressure

Current admitted positive families include:

~~~text
sole ordinary top-level command

first ordinary top-level command
in a sequential Bash/sh script
~~~

These were selected because real cases and GitHub execution-profile semantics justified them.

The system did not attempt general shell execution.

That is minimum useful generality in practice:

~~~text
support the smallest real family
that earns the proposition
without pretending to solve the whole language
~~~

---

## 36. S001, S002, and S004 became architecture pressure, not hardcoded cases

Historical real-case outcome:

~~~text
S001
sole ordinary top-level command
→ eligible

S002
first sequential Bash command
→ eligible

S004
&& short-circuit shape
→ unresolved/deferred
~~~

These cases did not become:

~~~text
if case == S001: allow
~~~

They pressured general structural rules.

This distinction is essential:

> **Cases should reveal the needed general responsibility, not become permanent special-case policy.**

---

## 37. Keeping S004 unresolved was a valid engineering result

A common temptation is:

~~~text
we found a real unsupported case
→ broaden immediately
~~~

UpgradePilot instead preserved:

~~~text
short-circuit structure
→ currently unresolved for runtime strengthening
~~~

because the evidence did not justify a safe general rule yet.

A correct unresolved boundary is preferable to unsupported coverage.

This is especially important in evidence systems.

---

## 38. Proof strategy evolved with architecture complexity

As responsibilities became more layered, proof also became layered.

A useful general proof ladder is:

~~~text
source reasoning
→ focused unit/contract tests
→ boundary/integration tests
→ full deterministic regression
→ installed-package smoke
→ hosted proof
→ live external/provider/model proof when required
~~~

Not every change requires every level.

But each claimed proposition needs a proof class that can actually establish it.

---

## 39. Unit tests answer local questions

Examples:

~~~text
parser recognizes quoted/comment boundaries
applicability composer handles refuted path
runtime eligibility classifies conditional occurrence
~~~

These tests are strong for local semantics.

They do not prove:

~~~text
application can normally produce the required evidence
CLI imports after migration
package installs
external GitHub behavior
live model quality
~~~

Do not ask a unit test to prove integration.

---

## 40. Boundary/integration tests prove producer→consumer reachability

Examples include:

~~~text
one shared StaticCommandAnalysis
→ direct requirements + project selection + package invocation

PublicPullRequestInvestigation
→ standalone synthesis preserves branch-stopping uncertainty
~~~

This level answers:

> Does the normal composition actually carry the evidence from its producer to the intended consumer?

That is different from testing either module alone.

---

## 41. Full deterministic regression protects breadth, not external reality

Cycle 3 final deterministic proof included:

~~~text
604 / 604
~~~

product tests at that historical horizon.

That gives broad confidence against deterministic regressions across the current test suite.

It does not prove:

~~~text
live GitHub still behaves exactly the same
live PyPI still responds
LM Studio model quality
target runtime compatibility
all real repositories
~~~

Full suite breadth and live-environment realism are separate axes.

---

## 42. Focused test counts are not additive

Cycle 3 had staged focused proof counts such as:

~~~text
18 / 18
40 / 40
76 / 76
~~~

Later focused suites included earlier tests.

Therefore:

~~~text
18 + 40 + 76
~~~

must not be presented as a larger unique-test total.

This seems small, but it reflects an important evidence habit:

> **Do not inflate proof by counting overlapping observations as independent.**

---

## 43. Hosted proof answers packaging/runtime questions

Historical final hosted Cycle-3 run:

~~~text
GitHub Actions run 35448172928
Python 3.12.14
fresh installation
pip check
installed CLI
focused investigation 15/15
Cycle-3 focused 76/76
full deterministic 604/604
~~~

This added evidence unavailable from local source inspection alone:

~~~text
fresh packaging/install works
declared dependencies resolve in hosted environment
installed CLI imports/executes
test suite works from installed product
~~~

But even this did not prove:

~~~text
exact target environment compatibility
command-level execution instrumentation
all live external services
~~~

---

## 44. Installed-package proof prevents repository-root illusions

A project can appear to work when Python imports directly from a repository checkout while packaging metadata is broken.

Installed proof checks a different proposition:

~~~text
distribution metadata
+ dependencies
+ package contents
+ console/module entry point
→ work from an installed artifact/environment
~~~

That is why ADR-0007 explicitly preserved installed-package testing as an important architecture proof.

---

## 45. Test responsibility must match change responsibility

Examples:

### Pure structural move

Need:

~~~text
imports/topology
focused migrated behavior
full regression
installed/CLI smoke
~~~

No new product behavior should appear.

### Parser architecture correction

Need:

~~~text
false-positive regressions
shell-family characterization
consumer composition
identity/order boundaries
runtime strengthening tests
full regression
hosted installed proof
~~~

### Naming-only docstring edit

May need:

~~~text
no fresh behavioral suite
~~~

unless import/module identity changed.

### Executable rename

Needs at least:

~~~text
new path imports/executes
~~~

This is proportional proof.

---

## 46. Regression tests should preserve the discovered failure mechanism

A good regression does not merely assert:

~~~text
old bug gone
~~~

It preserves the proposition that failed.

For ADR-0009 pressure, meaningful regressions include:

~~~text
comment text does not create command
quoted separator does not create command
conditional command remains structurally conditional
parse uncertainty fails closed
~~~

For migration pressure:

~~~text
preferred module owner imports
obsolete flat paths absent
package root minimal
~~~

These tests explain what must not regress.

---

## 47. Source/test reconciliation prevents architecture theater

A diagram or ADR can say:

~~~text
owner = upgradepilot.github
~~~

But source/test reconciliation asks:

~~~text
does current code actually import/use that owner?
do obsolete paths still exist?
do consumers still duplicate the old responsibility?
do tests protect the selected direction?
~~~

Architecture is only real when:

~~~text
accepted owner
→ implementation
→ consumer path
→ executable proof
~~~

align.

---

## 48. Cross-responsibility composition should be audited explicitly

A local module can be perfectly designed while the product composition loses important identity.

Current examples elsewhere in the project include:

~~~text
CI knows consuming job
BUT
Target composition does not yet receive it
~~~

This is why UpgradePilot repeatedly traces:

~~~text
proposition
→ producer
→ composition boundary
→ consumer
→ proof
~~~

Architecture quality is not just local cohesion.

It also depends on correct handoff across owners.

---

## 49. Why “common/utils” was repeatedly resisted

When duplication appears, a generic common package is tempting.

But:

~~~text
used by two modules
!= source-neutral responsibility
~~~

For example:

~~~text
GitHub Actions workflow structure
→ shared by CI and Target
BUT
still GitHub-specific
→ owner remains github
~~~

Likewise shell command structure inside GitHub Actions run steps remains provider-side evidence before dependency/CI semantics.

The general rule:

> **Share by semantic ownership, not by caller count.**

---

## 50. Why giant universal models were rejected

The project repeatedly rejected broad abstractions such as:

~~~text
universal workflow execution model
combined static/runtime workflow base object
generic environment reconstructor
generic impact/result object
universal evidence graph
generic planner
~~~

unless real product pressure justified them.

Why?

Because broad abstractions often:

~~~text
erase proposition boundaries
merge evidence strengths
increase hidden coupling
freeze guesses about future requirements
make tests less diagnostic
~~~

Minimum useful generality keeps models close to proven responsibilities.

---

## 51. Engineering corrections should preserve stronger existing evidence

A migration or refactor must not weaken:

~~~text
identity
provenance
validation
proof strength
negative/unresolved semantics
~~~

merely to simplify code.

Examples in this history include:

~~~text
Git object-ID validation
target evidence construction compatibility
static/runtime distinction
parser fail-closed behavior
exact occurrence identity
~~~

Refactoring is not simplification at any cost.

It is responsibility correction while preserving valid contracts.

---

## 52. Fail-closed behavior is an architectural choice

ADR-0009 deliberately rejected:

~~~text
parser uncertain
→ fall back to old splitter
→ maybe recover positive evidence
~~~

Why?

Because the weaker fallback could recreate the exact false-positive class the stronger parser was introduced to prevent.

The rule is general:

> **When a stronger evidence mechanism fails, do not automatically substitute a weaker mechanism if that weaker mechanism can fabricate the proposition.**

Unresolved is often the correct state.

---

## 53. Architecture change needs a stopping boundary

Each major correction also defined what it would not solve.

Examples:

### ADR-0003

Did not automatically re-admit old implementation/dependencies.

### ADR-0007

Did not create speculative future subpackages.

### ADR-0008

Did not build a full GitHub Actions execution engine.

### ADR-0009

Did not implement general shell execution/CFG semantics.

### Cycle 3

Did not admit S004 short-circuit runtime strengthening.

Stopping boundaries prevented each repair from becoming a whole-system rewrite.

---

## 54. The strongest recurring engineering pattern

Across all of these corrections, the recurring loop is:

~~~text
1. observe a real failure / duplication / pressure

2. identify the exact proposition that is wrong or duplicated

3. locate the earliest layer that can truthfully own it

4. separate nearby propositions that had been overloaded

5. compare the smallest credible correction
   against local patches and overly broad abstractions

6. preserve valid existing contracts/proof strength

7. migrate consumers

8. run proof at the level matching the change

9. keep unsupported extensions unresolved/deferred

10. promote durable semantics/method to the correct owner
~~~

This is the architecture method worth transferring to future work.

---

## 55. What changed in the project’s engineering style

The evolution can be summarized as several shifts.

### From inherited code to evidence-derived implementation

~~~text
old implementation exists
→ not enough

current responsibility independently requires it
→ implement/admit it
~~~

### From file-centric organization to responsibility ownership

~~~text
where can this code go?
→ weaker question

who owns this proposition?
→ stronger question
~~~

### From duplication removal to semantic sharing

~~~text
two callers look similar
→ not enough

two callers need the same fact with same meaning
→ share producer
~~~

### From success booleans to evidence-strength states

~~~text
works / fails
→ too coarse

established / refuted / unresolved / conflicted
+ provenance / proof limits
→ better
~~~

### From broad “CI passed” to proposition-specific runtime evidence

~~~text
green step
→ not enough

exact occurrence + admitted relation + exact runtime owner
→ bounded strengthening
~~~

### From naming as polish to naming as ownership aid

~~~text
short code label
→ may increase cognitive load

semantic responsibility name
→ improves navigation/review
~~~

---

## 56. What should not be learned from this history

Do not infer:

~~~text
always rewrite from scratch
always create subpackages
always use Tree-sitter
always add ADRs
always run the full suite for every edit
always introduce another evidence type
always prefer a larger architecture correction
~~~

Those would be cargo-cult conclusions.

The actual rule is evidence-relative:

~~~text
use the smallest correction
that truthfully fixes the demonstrated responsibility
at the earliest sufficient owner
with proof proportional to the claim
~~~

Sometimes that is one import fix.

Sometimes it is a new shared parser architecture.

---

## 57. Decision heuristic: local patch or foundational correction?

Ask:

### Question 1

Is the problem isolated to one implementation mistake?

Example:

~~~text
wrong imported symbol
→ local correction
~~~

### Question 2

Do multiple consumers independently reconstruct the same proposition?

Example:

~~~text
dependency + CI independently split same shell source
→ shared producer pressure
~~~

### Question 3

Would a local patch leave the same false assumption elsewhere?

Example:

~~~text
quote-aware splitter
→ still leaves duplicated parsing and execution ambiguity
→ foundational correction justified
~~~

### Question 4

Is the proposed abstraction broader than current evidence?

If yes:

~~~text
defer/generalize less
~~~

### Question 5

What proof distinguishes the alternatives?

Use the smallest test/case/investigation that can decide.

---

## 58. Decision heuristic: refactor or semantic change?

During migration, classify every meaningful difference:

~~~text
same behavior, new owner/path
→ refactor/migration

new evidence state / stronger-weaker claim
→ semantic change

new provider capability
→ feature/capability

new proof only
→ validation change
~~~

Do not hide semantic changes inside a structural migration.

That makes regression diagnosis much harder.

---

## 59. Decision heuristic: where should a new type live?

Trace:

~~~text
what fact does it represent?
who can establish that fact first?
is the meaning provider-specific, domain-specific, or cross-domain?
which consumers need it?
does moving it earlier accidentally add downstream semantics?
~~~

Examples:

~~~text
GitHub Actions run-step structure
→ github

pip/uv environment selection
→ dependency

changed-dependency CI consumption
→ ci

target Python declaration
→ target

mechanism applicability
→ impact
~~~

A type should live where its fact is first truthful.

---

## 60. Decision heuristic: how much proof is enough?

Ask what changed.

~~~text
pure helper logic
→ focused unit test may be enough

cross-module handoff
→ integration test

architecture migration
→ topology + focused behavior + full regression + install smoke

packaging/import boundary
→ installed proof

provider/live-service behavior
→ live/hosted proof when decision-critical

semantic model quality
→ live model evaluation when decision-critical
~~~

Do not automatically climb to the highest proof level.

But do not stop below the level that can establish the claim.

---

## 61. Current architecture confirms the historical corrections

At the current horizon, source topology shows:

~~~text
upgradepilot.github
upgradepilot.dependency
upgradepilot.ci
upgradepilot.pypi
upgradepilot.upstream
upgradepilot.target
upgradepilot.impact
~~~

with application/presentation owners remaining explicit.

Current topology tests verify obsolete flat paths are gone.

Current workflow command analysis is provider-owned and parser-backed.

Current dependency and CI consumers reuse that shared command analysis.

Current runtime strengthening remains a separate CI-owned policy.

The historical corrections therefore remain visible in active source, not only in documents.

---

## 62. Current facts versus historical snapshots

This retrospective uses two evidence categories.

### Current facts

Examples:

~~~text
responsibility-based source topology exists
parser-backed command analysis exists
current topology tests protect owners
current Group-8 runtime-strengthening design exists
~~~

These are checked against current main.

### Historical progression

Examples:

~~~text
clean reset rationale
August source-migration import failure
cross-responsibility architecture pressure
Cycle 1/2/3 staged proof
naming migration
~~~

These are used to explain how/why the current architecture emerged.

Historical records do not override current source.

---

## 63. Proof facts versus learning claims

Historical proof records establish implementation/proof outcomes such as:

~~~text
320-test migration run failed from import wiring
later source reconciliation accepted
58/58 semantic naming family proof
Cycle-3 18/40/76 staged focused proof
Cycle-3 final 604/604 deterministic proof
hosted fresh-install run passed
~~~

They do not prove:

~~~text
every current future commit
every external provider state
all user mastery
all possible GitHub Actions syntax
general shell execution correctness
~~~

Proof must always stay tied to its horizon and proposition.

---

## 64. Fast relearning route

Use this sequence:

~~~text
1. Read ADR-0003.
   Explain why old code was preserved but removed from active authority.

2. Read ADR-0007.
   Explain why subpackages were delayed first and justified later.

3. Read tests/test_source_topology.py.
   State exactly what architecture propositions it protects.

4. Read the August 4 import-failure working memory.
   Classify:
   architecture defect or migration defect?

5. Read the B2 cross-responsibility reconciliation plan
   and ADR-0008.
   Explain:
   share meaning, not merely syntax.

6. Read the Naming Clarity specification.
   Explain why responsibility naming affects maintainability/correctness.

7. Read ADR-0009.
   Explain why a better textual splitter was insufficient.

8. Revisit Group 8 notes.
   Recover:
   identity vs ordering vs execution,
   provider parse vs CI runtime policy.

9. Read Cycle-3 proof record.
   Explain what 18/40/76/604 and hosted proof each establish.

10. State the project-wide engineering rule:
    earliest sufficient owner
    + minimum useful generality
    + proportional proof.
~~~

---

## 65. Ownership / transfer questions

Without looking at this note, explain:

1. Why did UpgradePilot preserve the old M2 implementation while removing it from active authority?
2. Why were old passing tests not accepted as proof after the clean reset?
3. Why was a flat package reasonable initially but responsibility-based subpackages justified later?
4. What is the difference between a structural migration failure and an architecture failure?
5. Why did the August import failure not justify undoing ADR-0007?
6. Why does “two consumers use the same syntax” not automatically justify one shared domain abstraction?
7. Why is GitHub workflow structure owned by the GitHub/provider layer instead of a generic common package?
8. How are ADR-0008 and ADR-0009 different but complementary?
9. Why is StaticCommandLocation identity rather than execution proof?
10. Why can source order not automatically become execution order?
11. Why was step-level runtime correlation insufficient for command-level strengthening?
12. Why is runtime-strengthening eligibility owned by CI rather than the parser?
13. Why is S004 remaining unresolved an acceptable engineering result?
14. What does a full deterministic regression prove that a focused test does not?
15. What does hosted installed-package proof add beyond the full deterministic suite?
16. Why should overlapping focused test suites not be added together as independent proof counts?
17. When should a rename receive executable validation?
18. How would you decide whether a new duplicated helper belongs in github, dependency, ci, target, or nowhere new?

### Transfer exercise

Imagine a future feature introduces two consumers that both parse Dockerfile RUN instructions.

One consumer wants:

~~~text
dependency installation declarations
~~~

and the other wants:

~~~text
security-sensitive command patterns
~~~

Design only the ownership boundary.

Answer:

~~~text
what fact could be shared?
which layer should own the source parser?
what must remain consumer-specific?
what identity should survive?
what proof would justify introducing the shared layer?
what evidence would tell you NOT to generalize yet?
~~~

Then compare that reasoning with the ADR-0008/ADR-0009 evolution.

---

## 66. Evidence anchors

Current evidence horizon:

~~~text
main@0e15299d5f8ff80b536669a162a8a221440d1f8f
~~~

Durable architecture owners:

~~~text
docs/architecture/ADR-0003-clean-slate-b2-source-reset.md
docs/architecture/ADR-0007-responsibility-based-python-subpackages.md
docs/architecture/ADR-0008-bounded-static-github-actions-workflow-definition.md
docs/architecture/ADR-0009-parser-backed-static-workflow-command-analysis.md
~~~

Cross-cutting naming owner:

~~~text
docs/specifications/UPGRADEPILOT_NAMING_CLARITY_SPECIFICATION.md
~~~

Structural/reconciliation plans:

~~~text
plans/B1_CURRENT_SOURCE_AND_TEST_RECONCILIATION.md
plans/B2_SOURCE_CODE_STRUCTURE_RECONCILIATION_PLAN.md
plans/B2_CROSS_RESPONSIBILITY_ARCHITECTURE_RECONCILIATION_PLAN.md
plans/STATIC_WORKFLOW_COMMAND_ANALYSIS_AND_RUNTIME_STRENGTHENING_IMPLEMENTATION_PLAN.md
~~~

Representative historical engineering records:

~~~text
working-memory/2026-08-04_B2-source-reconciliation-major-tranche-import-failure-and-corrections.md
working-memory/2026-08-04_B2-source-structure-reconciliation-final-acceptance.md
working-memory/2026-08-15_B2-cross-responsibility-architecture-reconciliation-phase-d-closure.md
working-memory/2026-09-13_static-shell-direct-install-false-positive-recognition.md
working-memory/2026-09-14_static-command-consumer-migration-and-identity.md
working-memory/2026-09-17_cycle3-runtime-strengthening-phase-a-orientation.md
working-memory/2026-09-18_cycle3-runtime-strengthening-build.md
working-memory/2026-09-19_cycle3-integrated-learning-review.md
working-memory/2026-09-06_semantic-responsibility-naming-enforcement.md
~~~

Current architecture proof anchor:

~~~text
tests/test_source_topology.py
~~~

Current focused implementation learning:

~~~text
learning/2026-09-19-parser-backed-ci-command-evidence-and-runtime-strengthening/
~~~

Historical hosted Cycle-3 proof:

~~~text
GitHub Actions run 35448172928
Python 3.12.14
fresh install
pip check
installed CLI
focused investigation 15/15
Cycle-3 focused 76/76
full deterministic 604/604
~~~

This artifact is a learning retrospective.

It does not supersede current ADRs/specifications/source/tests, does not reopen closed implementation cycles, and does not authorize new refactors.

UP-SKILL:upgradepilot-learning-artifact
UP-SKILL:upgradepilot-planning-design
