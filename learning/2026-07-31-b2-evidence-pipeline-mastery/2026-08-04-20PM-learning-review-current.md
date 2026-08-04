

UpgradePilot learning review — current checkpoint

This review is aligned to the restructured repository, not the old flat module layout. The learning package is pinned through the architecture-aligned checkpoint, and the plan explicitly says that Units 1–4 continue rather than restart because the CI algorithm survived the restructuring materially unchanged. Our exact continuation remains inside src/upgradepilot/ci/workflow_commands.py, immediately after the first jobs:-discovery stage of _extract_job_definitions(...).

I am going to review four different kinds of knowledge together:

PRODUCT MEANING
What question UpgradePilot is answering and what claims are legitimate.

ARCHITECTURE
Which responsibility owns which behavior and why.

IMPLEMENTATION LOGIC
How data and evidence actually flow through the current Python code.

PYTHON / SYNTAX
The language mechanisms you need to understand the implementation rather than merely recognize it.

I will also distinguish things you should understand now from things we have deliberately not reached yet.


---

1. First rebuild the project architecture in your head

The largest change since we began learning was architectural.

Originally, many responsibilities lived as flat modules:

upgradepilot/
├── ci_dependency_exercise.py
├── workflow_commands.py
├── dependency_change.py
├── github_repository.py
├── packaging_method.py
├── target_python.py
├── upstream_claim.py
└── ...

That became difficult to reason about because one directory mixed:

provider acquisition
domain interpretation
application orchestration
technical implementation methods
interface code

ADR-0007 reorganized the product around responsibility ownership.

The current mental map is:

src/upgradepilot/
│
├── ci/
│   ├── dependency_exercise.py
│   └── workflow_commands.py
│
├── dependency/
│   ├── analysis.py
│   ├── change.py
│   ├── requirements.py
│   ├── uv_lock.py
│   └── versioning.py
│
├── github/
│   ├── actions.py
│   ├── api.py
│   ├── changelog.py
│   ├── identity.py
│   ├── pull_request.py
│   ├── release.py
│   ├── repository.py
│   └── tag.py
│
├── pypi/
│   ├── api.py
│   ├── provenance.py
│   └── release.py
│
├── upstream/
│   ├── claim.py
│   ├── interval.py
│   ├── interval_evidence.py
│   └── repository.py
│
├── target/
│   ├── python.py
│   ├── python_specifier.py
│   └── relevance.py
│
├── investigation.py
├── cli.py
│
├── package_identity.py
├── repository_path.py
└── json_contract.py

The essential question is:

> Which responsibility owns this behavior?



Not:

> Which technical category can I dump this code into?



That is why UpgradePilot deliberately avoids generic directories such as:

services/
managers/
helpers/
common/
misc/

unless a real responsibility eventually justifies one.

Provider versus domain

This distinction is important.

github/ owns things that are specifically about obtaining and validating GitHub evidence:

workflow runs
workflow jobs
exact repository files
Git refs/tags
GitHub releases
PR identity

But GitHub does not decide what those facts mean for UpgradePilot's product claims.

For example:

github/actions.py
→ acquire WorkflowRun / WorkflowJob evidence

ci/dependency_exercise.py
→ interpret that evidence for the CI dependency-exercise question

That separation is:

provider acquisition
≠
domain interpretation

This pattern appears throughout the new architecture.


---

2. Application versus interface

Another major restructuring lesson is:

application orchestration
≠
CLI presentation

The architecture is moving toward:

CLI input
    ↓
investigate_public_pull_request(...)
    ↓
typed PublicPullRequestInvestigation
    ↓
CLI rendering / exit policy

investigation.py coordinates product responsibilities.

cli.py should deal primarily with the interface:

arguments
display
labels
exit behavior

This matters because a giant cli.py that:

constructs clients
acquires data
interprets evidence
coordinates domain decisions
formats results
decides exit codes

quickly becomes a god object/module — one place owning too many unrelated responsibilities.

You have only been introduced to this architecture so far. You are not expected to independently design the entire application architecture yet.


---

3. Product runtime is not every Python file in the repository

Another architectural distinction:

src/upgradepilot/
→ installable product runtime

tests/
→ deterministic regression for product runtime

experiments/
→ non-product research / evaluation / calibration

experiments/tests/
→ regression for experiment machinery

tools/
→ developer-operated live proofs / diagnostics / utilities

So:

Python code exists

does not imply:

product runtime architecture

An experiment can prove that an approach looks promising without becoming a product dependency.

A tool can demonstrate live behavior without defining product semantics.

And product runtime should never depend backward on:

experiments/
tests/
tools/

This is an important engineering concept beyond UpgradePilot:

> Executable code can belong to different trust and lifecycle boundaries.



The source-topology tests now enforce part of this architectural model.


---

4. Why upgradepilot.__init__ became intentionally tiny

The old design exposed many things through the package root.

The new approach prefers:

from upgradepilot.ci.dependency_exercise import evaluate_dependency_ci_exercise

instead of hiding ownership behind something like:

from upgradepilot import evaluate_dependency_ci_exercise

Why?

Because giant root re-exports make this:

upgradepilot.SomeThing

look like a stable public API even when SomeThing is actually an internal implementation contract.

Precise imports tell you:

ci
└── dependency_exercise
    └── evaluate_dependency_ci_exercise

That is architectural information.

The project even has a topology test verifying:

upgradepilot.__all__ == ()

and verifying that obsolete flat paths such as:

upgradepilot.workflow_commands
upgradepilot.ci_dependency_exercise
upgradepilot.dependency_change

are genuinely absent.

This gives us another important principle:

> Architecture can have executable tests.



Architecture is not limited to diagrams and ADRs.


---

5. The main responsibility we have actually been learning deeply

Our first deep anchor is:

CI dependency exercise

Current owner:

src/upgradepilot/ci/dependency_exercise.py

Its product question is approximately:

> Does at least one admitted successful CI path tied to the PR's exact current revision provide sufficient evidence that the changed dependency source was installed and that the changed package was directly exercised?



The module itself explicitly limits its claim: it does not establish complete test coverage, compatibility, safety, or a maintainer decision.

That sentence is probably the single most important thing to remember.


---

6. CI: Continuous Integration

CI = Continuous Integration.

Practically, CI systems such as GitHub Actions automatically run jobs when software changes.

Typical jobs may:

install dependencies
run tests
lint
build
check formatting
perform static analysis

But:

CI was green

does not automatically imply:

the changed dependency was actually installed

and does not imply:

the changed package was actually exercised

and absolutely does not imply:

the upgrade is compatible
safe
correct
ready to merge

UpgradePilot deliberately asks a much narrower evidence question.


---

7. Dependency consumption versus package exercise

These are two different facts.

Suppose the changed package is:

pytest

and the changed dependency source is:

requirements-dev.txt

Consumption evidence might be:

pip install -r requirements-dev.txt

Exercise evidence might be:

pytest

or:

python -m pytest

The intended narrow proposition is approximately:

this CI path consumed the relevant dependency source
AND
this CI path directly exercised the changed package

That is stronger than merely:

CI succeeded

but weaker than:

this dependency upgrade is fully compatible


---

8. Exact-head evidence

One of the most important evidence concepts we've learned is exact revision alignment.

A GitHub commit has a SHA.

SHA = Secure Hash Algorithm.

Git uses hash-like commit identifiers such as:

aa2dc...

to identify a particular repository revision.

When we say exact-head, we mean evidence tied to the PR's exact current head revision.

Conceptually:

PR head commit
      =
workflow run head SHA
      =
workflow job head SHA
      =
workflow definition revision being interpreted

Why?

Imagine:

Monday:
workflow does NOT run pytest

Tuesday:
workflow changed to run pytest

If you took:

Monday's successful CI result
+
Tuesday's workflow YAML

you could falsely conclude that Monday's CI executed pytest.

So UpgradePilot rejects:

definition.revision != run.head_sha

before interpreting the commands.

This is an evidence-integrity property.


---

9. The three CI dependency-exercise states

The public state vocabulary is:

Literal[
    "proven",
    "no_successful_ci",
    "unresolved",
]

The meanings matter.

proven

Means:

> At least one admitted successful exact-head CI path satisfies the current narrow dependency-installation + package-exercise rule.



It does not mean all workflows satisfy it.

It does not mean all tests passed universally.

It does not mean compatibility.


---

no_successful_ci

Means:

> The evaluator did not have the successful CI execution required to reach the evidence question.



Examples:

no exact-head workflows

or:

all available exact-head jobs failed/cancelled

It does not mean:

> CI ran successfully and proved that the dependency was not exercised.




---

unresolved

Means:

> Successful CI exists, but UpgradePilot cannot establish the narrow dependency-exercise proposition using its admitted deterministic rule.



Examples:

workflow definition unavailable
wrong definition revision
requirements installation path unavailable
unsupported workflow structure
install command not established
package invocation not established

This distinction is fundamental:

not proved
≠
proved false

Your learning plan considers Unit 1 complete at current operational depth.


---

10. The evidence objects

The evaluator receives:

DependencyVersionChange

and:

WorkflowDependencyExerciseInput

where:

@dataclass(frozen=True, slots=True)
class WorkflowDependencyExerciseInput:
    run: WorkflowRun
    jobs: tuple[WorkflowJob, ...]
    definition: RepositoryFileEvidence

Think of this as:

one workflow evidence bundle
├── run
├── jobs
└── exact workflow definition

The evaluator produces one:

WorkflowDependencyExerciseResult

per workflow, then one:

DependencyCIExerciseResult

for the aggregate.

That separation is architectural:

interpret ONE workflow
→ WorkflowDependencyExerciseResult

aggregate ALL interpreted workflows
→ DependencyCIExerciseResult


---

11. Literal — a gap we should close now

We had seen:

type DependencyCIExerciseState = Literal[
    "proven",
    "no_successful_ci",
    "unresolved",
]

Literal is from Python typing.

Instead of saying:

state: str

which permits essentially any string:

"banana"
"success"
"PROVEN"
"proved"

we say:

state: DependencyCIExerciseState

whose intended type-level vocabulary is exactly:

"proven"
"no_successful_ci"
"unresolved"

Why is the name Literal appropriate?

Because it refers to specific literal values.

This:

Literal["proven", "unresolved"]

means:

> Only these literal strings belong to this type.



Runtime Python itself does not magically reject every wrong value; this primarily helps:

type checkers
IDEs
human readers
exhaustive state reasoning

Depth now

You should understand Literal operationally.

You do not need advanced Python type-system theory yet.


---

12. @dataclass

We repeatedly encounter:

@dataclass(...)
class Something:
    ...

A dataclass is a Python class intended primarily to hold structured data.

Instead of manually writing:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

you can write:

@dataclass
class Person:
    name: str
    age: int

and Python generates useful boilerplate such as the constructor.

UpgradePilot uses dataclasses heavily because evidence is naturally represented as structured records:

WorkflowRun
WorkflowJob
RepositoryTextFile
WorkflowCommandEvidence
WorkflowDependencyExerciseResult


---

13. Why frozen=True

We see:

@dataclass(frozen=True, slots=True)

frozen=True means the instance is intended to be immutable after creation.

Conceptually:

result.state = "something-else"

should not be normal allowed usage.

That is useful for evidence records.

Why?

Because evidence should behave more like:

a recorded fact/result

than:

a mutable bag that arbitrary code changes later

Immutability reduces accidental state mutation and makes reasoning easier.


---

14. Why slots=True

Ordinary Python class instances usually keep attributes in a dynamic dictionary such as conceptually:

instance.__dict__

slots=True tells dataclasses to use a more constrained attribute layout.

Practical effects include:

less accidental arbitrary attribute creation
often lower memory overhead
clearer fixed record shape

For this project, the conceptual value matters more than micro-performance:

> This object has a defined evidence shape.



You do not need deep Python object-layout internals yet.


---

15. Keyword-only arguments and *

Consider:

def evaluate_dependency_ci_exercise(
    dependency,
    workflow_inputs,
    *,
    direct_requirements_install_path,
):

Everything after:

*

must be supplied by name.

Valid:

evaluate_dependency_ci_exercise(
    dependency,
    workflow_inputs,
    direct_requirements_install_path="requirements-dev.txt",
)

Not intended:

evaluate_dependency_ci_exercise(
    dependency,
    workflow_inputs,
    "requirements-dev.txt",
)

Why?

Because several arguments may have similar primitive types such as str.

Keyword-only arguments make the call communicate meaning:

direct_requirements_install_path=

instead of relying on positional memory.


---

16. Sequence[...]

The outer function accepts:

workflow_inputs: Sequence[WorkflowDependencyExerciseInput]

Sequence comes from:

collections.abc

It means approximately:

> I need ordered sequence-like behavior; I do not care whether the caller specifically gives me a list or tuple.



For example:

[
    workflow_a,
    workflow_b,
]

or:

(
    workflow_a,
    workflow_b,
)

both satisfy the broad idea.

Compare:

list[Thing]

which says:

> specifically a list



with:

Sequence[Thing]

which says:

> any suitable sequence.



This is programming to the required interface, rather than unnecessarily demanding one concrete container implementation.


---

17. Tuple materialization

This was one of the most important Python mechanisms we studied.

Current code:

results = tuple(
    _evaluate_workflow_dependency_exercise(
        dependency,
        workflow_input,
        direct_requirements_install_path=direct_requirements_install_path,
    )
    for workflow_input in workflow_inputs
)

Inside tuple(...) is a generator expression:

expression
for item in collection

Generators are lazy by themselves.

But:

tuple(generator)

immediately consumes the generator.

Therefore when that statement completes:

Workflow A evaluated
Workflow B evaluated
Workflow C evaluated

results = (ResultA, ResultB, ResultC)

All workflow evaluations have already happened.

This becomes important immediately afterward.


---

18. next(..., None) — existence plus witness

Current code:

proven = next(
    (result for result in results if result.state == "proven"),
    None,
)

This asks:

Give me the first result whose state is proven.

If one exists:

return that result object

If none exists:

return None

Compare:

any(...)

which gives:

True / False

with:

next(..., None)

which gives:

actual witness / None

Example:

A → unresolved
B → proven
C → proven

Then:

proven = B

but:

results == (A, B, C)

still contains all three.

This distinction matters:

proof sufficiency
≠
evidence preservation

One witness may be sufficient for the decision while all evidence remains useful diagnostically.


---

19. Why next() does not prevent C from being evaluated

This was an easy place to form the wrong mental model.

Because:

results = tuple(...)

has already evaluated all workflows.

Then:

next(...)

searches through the already-created result objects.

So:

A evaluated
B evaluated
C evaluated
↓
results exists
↓
next searches A, B...
↓
stops at B

It does not mean C was never evaluated.

The short-circuit applies only to the later witness search.


---

20. None as expected absence

Here:

proven = None

does not mean an error.

It means:

No proven workflow was found.

That is a perfectly legitimate product situation.

Using:

next(iterator, None)

also avoids allowing Python's normal:

StopIteration

exception to escape when nothing matches.

So:

None

is serving as an expected absence marker.


---

21. Why if proven is not None

Current code uses:

if proven is not None:

rather than:

if proven:

The former asks explicitly:

> Is this object different from our absence marker?



That is clearer because None has a deliberate semantic role.

It avoids mixing:

absence

with generic Python truthiness.


---

22. Internal invariant versus product uncertainty

Inside the proven branch:

assert direct_requirements_install_path is not None

This is a very important distinction.

An assertion here means approximately:

> If our preceding logic is correct, this condition must already be true.



Why?

Because a workflow cannot become proven through the inner evaluator when:

direct_requirements_install_path is None

The inner evaluator would already have returned:

unresolved

So if we somehow have:

proven workflow
+
direct_requirements_install_path == None

that indicates an internal programming inconsistency.

Compare:

expected missing evidence
→ explicit product state such as unresolved

impossible internal combination
→ assertion / programming defect

This distinction appears throughout good evidence-oriented software.


---

23. state, reason, detail, evidence payload

Results intentionally separate several concepts.

Example:

WorkflowDependencyExerciseResult(
    state="unresolved",
    reason="workflow_definition_revision_mismatch",
    detail="Workflow definition revision did not match the run head SHA.",
    install_command=None,
    execution_command=None,
)

Think:

state
→ broad classification

reason
→ specific stable machine-oriented category

detail
→ human-readable explanation

evidence fields
→ structured supporting facts

Do not treat:

detail string

as the actual evidence model.

This becomes especially important when interfaces change.


---

24. Aggregate semantics are existential

The aggregate question is effectively:

Does there exist at least one workflow that proves the proposition?

Mathematical notation would be:

∃ workflow

where ∃ means:

> there exists.



Therefore:

A → unresolved
B → proven
C → failed

gives:

aggregate → proven

because B is sufficient for this narrow existential proposition.

It does not produce:

all workflows proven

That would be a universal proposition:

∀ workflow

which is a different question.


---

25. Aggregate decision order

The outer evaluator has this effective hierarchy:

No workflow inputs?
│
├── yes
│   → no_successful_ci
│      reason=no_exact_head_workflows
│
└── no
    ↓
evaluate every workflow
    ↓
Any workflow proven?
│
├── yes
│   → aggregate proven
│
└── no
    ↓
Any completed-successful job anywhere?
│
├── no
│   → no_successful_ci
│
└── yes
    → unresolved

The final unresolved means:

successful execution exists
BUT
admitted dependency exercise proof does not

The current implementation reflects exactly this structure.


---

26. any(...) versus next(...)

The code later asks:

has_successful_job = any(
    job.status == "completed"
    and job.conclusion == "success"
    for workflow_input in workflow_inputs
    for job in workflow_input.jobs
)

Why any() here?

Because the next branch only needs:

Does at least one such job exist?

It does not need the actual job object.

So:

Need witness object?
→ next(..., None)

Need only existence?
→ any(...)

That is a useful transferable Python design decision.


---

27. Nested generator expressions

This:

for workflow_input in workflow_inputs
for job in workflow_input.jobs

inside the generator corresponds conceptually to:

for workflow_input in workflow_inputs:
    for job in workflow_input.jobs:
        ...

So it flattens:

all workflows
    ↓
all jobs within every workflow

for the Boolean existence test.


---

28. Per-workflow evaluator — gate ordering

Now move inside:

_evaluate_workflow_dependency_exercise(...)

This owns one workflow bundle.

The gate order is part of the product semantics.

It is approximately:

Gate	Question	Failure result

1	Is there a completed-successful job?	no_successful_ci / no_successful_jobs
2	Is the parent run completed-successfully?	unresolved / workflow_not_successful
3	Is the workflow definition available?	unresolved / workflow_definition_unavailable
4	Does definition revision equal run head SHA?	unresolved / workflow_definition_revision_mismatch
5	Is an explicit direct requirements install path available?	unresolved / direct_requirements_install_path_unavailable
6	Does the bounded command reader establish install + invocation?	unresolved / reader reason
7	Everything above passed	proven


This ordering is implemented in the current restructured source.


---

29. Why child job success is checked separately from parent run success

Suppose:

Job A → completed / success
Job B → completed / failure

workflow run → completed / failure

The first gate:

successful_jobs

is non-empty because Job A succeeded.

So this is not:

no_successful_ci

for that workflow.

But the parent run itself failed.

Therefore the next gate produces:

unresolved / workflow_not_successful

That distinction preserves the actual observed facts rather than flattening everything into generic failure.


---

30. Early returns are semantics

Consider:

if not successful_jobs:
    return ...

Once return executes:

the function ends

Nothing below it runs.

So if no job succeeded:

definition availability
revision alignment
command inspection

are irrelevant to this result.

This gives us a general principle:

> Branch ordering in evidence software can encode the meaning of the result, not merely implementation convenience.




---

31. Repository file availability

The definition is modeled as:

RepositoryTextFile
OR
UnavailableRepositoryFile

This matters because acquisition can fail.

Instead of pretending:

workflow file always exists

the system represents unavailable evidence explicitly.

If CI succeeded but the exact workflow definition cannot be acquired:

we know CI ran
but
we cannot inspect its admitted command evidence

Therefore:

unresolved

rather than:

proven

or:

false


---

32. isinstance(...)

We saw:

if isinstance(definition, UnavailableRepositoryFile):

isinstance(object, Type) asks:

> Is this object an instance of this class/type?



After the unavailable case returns:

assert isinstance(definition, RepositoryTextFile)

means the remaining valid branch must be the available text-file variant.

This also helps static type narrowing.


---

33. Dependency identity is not CI installation evidence

This distinction is extremely important.

Suppose UpgradePilot established:

soupsieve changed 2.6 → 2.8.4

from:

uv.lock

That establishes a dependency-version-change fact.

It does not establish:

CI installed uv.lock

or even:

CI consumed that lockfile

Likewise, dependency evidence coming from:

constraints.txt

does not automatically imply CI installed it.

Therefore the evaluator receives a separate:

direct_requirements_install_path

and refuses to infer it from arbitrary dependency evidence.

Mental model:

DEPENDENCY IDENTITY
What dependency changed?

≠

OPERATIONAL CI CONSUMPTION
What source did CI actually install?

This separation is intentional.


---

34. Boundary between CI evidence and command interpretation

Only after all higher-level gates pass does this happen:

commands = inspect_workflow_commands(
    definition.content,
    source_file=direct_requirements_install_path,
    package=dependency.package,
    normalized_package=dependency.normalized_package,
)

This is good responsibility separation.

dependency_exercise.py owns:

Was this CI evidence admissible?

workflow_commands.py owns:

What can we conservatively establish from the visible workflow commands?

The command reader does not own:

GitHub run success
SHA identity
repository acquisition
dependency identity


---

35. The workflow reader is deliberately not a YAML parser

Current owner:

src/upgradepilot/ci/workflow_commands.py

Its module description explicitly says it understands only a shallow indentation-based workflow shape and visible run: commands.

It does not claim to evaluate:

full YAML semantics
arbitrary shell semantics
reusable workflows
expressions
task runners
transitive scripts

When it cannot establish the fact:

unresolved

is preferred over guessing.

This is a central UpgradePilot philosophy:

unsupported meaning
→ abstain

not:
unsupported meaning
→ infer optimistically


---

36. WorkflowCommandEvidence

The command reader produces:

@dataclass(frozen=True, slots=True)
class WorkflowCommandEvidence:
    status: WorkflowCommandStatus
    reason: str
    detail: str
    job_count: int
    install_command: str | None = None
    execution_command: str | None = None

Its state vocabulary is narrower:

Literal["supported", "unresolved"]

Notice:

command reader → supported

CI evaluator → proven

Those are intentionally different terms.

workflow_commands.py can establish only:

> The visible command grammar supports the command-level proposition.



It cannot independently establish:

> The entire exact-head CI evidence proposition is proven.



So:

supported command evidence
≠
proven CI evidence


---

37. _WorkflowJobDefinition

Internal lightweight record:

@dataclass(frozen=True, slots=True)
class _WorkflowJobDefinition:
    key: str
    commands: tuple[str, ...]

Notice what it does not contain:

runner image
permissions
matrix
services
environment
timeout
strategy
all Actions semantics

Because the reader only needs:

job identity
+
visible run commands

That is an example of a purpose-built intermediate representation.

You do not need to model the entire world if the product responsibility only needs a small bounded subset.


---

38. None versus empty tuple from _extract_job_definitions

This distinction matters.

None

means:

> I could not even identify the supported jobs: mapping.



Whereas:

()

means:

> I found the mapping, but discovered zero readable direct jobs.



Those represent different structural observations.

Higher code then maps:

None
→ workflow_jobs_not_statically_readable

len(jobs) != 1
→ multiple_or_zero_workflow_jobs

So:

absence of readable parent structure
≠
readable parent with zero supported children


---

39. Exactly-one-job rule

Current implementation requires:

len(jobs) == 1

If:

len(jobs) != 1

the reader returns unresolved.

So:

jobs:
  test:
    steps:
      - run: pip install -r requirements-dev.txt
      - run: pytest

  lint:
    steps:
      - run: ruff check .

is currently:

unresolved

even though the test job independently satisfies the narrow command rule.

This led to our LR-002 design observation.

Important terminology:

CASE-SPECIFIC HARDCODING
if repo == something
if package == pytest
if PR == 1234

not observed

versus:

SHAPE-SPECIFIC / NARROW GRAMMAR
exactly one job
direct pip -r
direct package invocation

definitely present

That makes it an intentionally bounded prototype rule, not literal package-specific cheating.


---

40. A more general conservative rule

We identified a possible future generalization:

for each job independently:
    does THIS SAME job contain install + invocation?

if any one job does:
    one same-job witness exists

This preserves safety because it still rejects:

Job A installs
Job B invokes

as insufficient.

So:

conservative

does not necessarily mean:

reject every richer structure

This is a useful engineering design insight.

It remains an open review question, not an approved product change.


---

41. Install and execution witnesses are searched independently

After the one-job gate:

commands = jobs[0].commands

Then:

install_command = next(...)

and:

execution_command = next(...)

are separate searches.

Conceptually:

∃ command that installs admitted source?
AND
∃ command that invokes package?

If either is missing:

if install_command is None or execution_command is None:

then:

unresolved

Why or?

Success requires:

install found AND execution found

The logical complement is:

install missing OR execution missing

Truth table:

Install	Exercise	Result

found	found	supported
found	missing	unresolved
missing	found	unresolved
missing	missing	unresolved



---

42. Partial evidence is preserved

Suppose:

install found
execution missing

The result still includes:

install_command=<actual matching command>
execution_command=None

This is a good evidence-design pattern.

Overall classification:

unresolved

does not mean:

nothing was observed

Structured partial evidence remains available.


---

43. Install matcher

Current helper:

_command_installs_source_file(
    command,
    source_file,
)

asks:

> Does a visible shell segment contain an admitted pip-install form whose requirement path matches the supplied source file?



The flow is:

normalize expected source path
↓
split command into visible shell segments
↓
find supported pip-install syntax
↓
find -r / --requirement path
↓
normalize extracted path
↓
compare exact normalized paths


---

44. _PIP_INSTALL_PATTERN

The regex is:

(?<![A-Za-z0-9_.-])
(?:python(?:3)?\s+-m\s+pip|pip(?:3)?)
\s+install\b

You do not need to become a regex specialist right now, but you should understand each major mechanism.

(?<!...)

This is a negative lookbehind.

It says approximately:

> Immediately before this position, there must not be one of these token characters.



Why?

So the matcher does not accidentally recognize pip embedded inside a larger identifier.


---

(?:...)

This is a non-capturing group.

Grouping is needed for logic:

option A
OR
option B

but we do not need to retrieve the group afterward.


---

python(?:3)?

Means:

python

followed optionally by:

3

So:

python
python3

both match.

? means:

> zero or one occurrence.




---

\s+

Means:

> one or more whitespace characters.




---

|

Means logical regex alternative:

A | B

roughly:

> A or B.




---

pip(?:3)?

Matches:

pip
pip3


---

\b

Means a word boundary.

So matching:

install

does not accidentally treat a larger attached token as the same command word.


---

re.IGNORECASE

Means:

pip
PIP
Pip

can match case-insensitively.

Practically, the recognized entry shapes include things such as:

pip install
pip3 install
python -m pip install
python3 -m pip install


---

45. _REQUIREMENT_PATTERN

Current regex:

(?:^|\s)
(?:-r|--requirement)
(?:=|\s+)
(?P<path>[^\s;&|]+)

Interpret it as:

start of command or whitespace
↓
-r or --requirement
↓
= or whitespace
↓
capture requirement path

So forms such as:

-r requirements-dev.txt
--requirement requirements-dev.txt
--requirement=requirements-dev.txt

can be recognized.


---

46. Named regex group

This part:

(?P<path>...)

creates a named capture group called:

path

Then Python can do:

match.group("path")

instead of something obscure like:

match.group(1)

Named groups improve readability because the captured value has semantic meaning.

We'll encounter the same concept later in:

_JOB_KEY_PATTERN
_RUN_PATTERN

but we have not yet studied their scanning logic in detail.


---

47. Why the requirement-path character class stops where it does

This:

[^\s;&|]+

means:

> one or more characters that are not whitespace, ;, &, or |.



The purpose is to avoid allowing a later shell command to become part of the requirement path.

Example:

pip install -r requirements-dev.txt && pytest

should capture approximately:

requirements-dev.txt

not:

requirements-dev.txt && pytest


---

48. Path normalization

The helper does:

normalized = path.strip().replace("\\", "/")

while normalized.startswith("./"):
    normalized = normalized[2:]

Therefore:

./requirements-dev.txt
requirements-dev.txt

are treated equivalently.

And:

requirements\dev.txt

becomes:

requirements/dev.txt

But the helper deliberately does not resolve:

..
environment variables
symlinks
working-directory changes

Why?

Because those would require deeper filesystem/shell interpretation that the workflow text alone does not prove.

A key correction from our learning:

> The function does not rewrite the whole command.



It extracts the path and normalizes the path identity only.


---

49. Shell segmentation

Current helper splits at:

&&
||
;
newline

For example:

echo hello && pip install -r requirements-dev.txt && python -m pytest

becomes approximately:

echo hello

pip install -r requirements-dev.txt

python -m pytest

The purpose is limited.

It does not implement a shell.

It does not correctly model every aspect of:

quoting
pipelines
substitution
conditions
working directories
functions

It simply avoids treating a whole chained command as one undifferentiated token.


---

50. Package invocation matcher

Current helper:

_command_invokes_package(
    command,
    package,
    normalized_package,
)

asks:

> Does a visible shell segment directly begin with the changed package, possibly behind one explicitly admitted wrapper?



This is not:

> Does the package's name occur anywhere in the command?



That distinction is critical.


---

51. Raw package and normalized package

It considers:

(package, normalized_package)

because package identity may have more than one known spelling.

The full normalization responsibility itself belongs elsewhere in the restructured architecture:

package_identity.py

and we have not learned the full PEP 503 normalization logic yet.

For the command reader, just understand:

known package spelling
+
known normalized spelling
→ possible direct invocation candidates

without guessing arbitrary aliases.


---

52. Set comprehension

The code:

candidates = {
    candidate.lower()
    for candidate in (package, normalized_package)
    if ...
}

is a set comprehension.

Sets deduplicate values.

If:

package = "pytest"
normalized_package = "pytest"

then:

candidates == {"pytest"}

not:

pytest twice

So the comprehension performs:

validation
+
lowercasing
+
deduplication


---

53. re.fullmatch

Candidates are admitted only if:

re.fullmatch(
    r"[A-Za-z0-9][A-Za-z0-9._-]*",
    candidate,
)

fullmatch means:

> The entire candidate must fit this grammar.



Compare conceptually:

search
→ pattern can occur somewhere

match
→ pattern begins at the beginning

fullmatch
→ entire string must conform

This prevents shell syntax or arbitrary weird strings from being injected into the later dynamic command matcher.


---

54. Supported invocation prefixes

Current explicit prefixes are:

""
"python -m "
"python3 -m "
"uv run "
"poetry run "
"pipenv run "
"coverage run -m "

Therefore:

pytest
python -m pytest
python3 -m pytest
uv run pytest
poetry run pytest
pipenv run pytest
coverage run -m pytest

can be admitted.

Important terminology:

python -m pytest
→ Python module execution

uv run pytest
poetry run pytest
pipenv run pytest
→ command/environment wrappers

The reader treats those wrappers as sufficiently transparent for the current rule.

But:

tox

does not count merely because tox might internally run pytest.

That would require interpreting another configuration boundary.


---

55. Leading environment-variable assignments

Shell syntax permits:

PYTHONWARNINGS=error python -m pytest

This means approximately:

> Run python -m pytest with PYTHONWARNINGS=error in its environment.



The actual invoked command is still:

python -m pytest

So the matcher strips supported visible leading assignments.

Conceptual transformation:

PYTHONWARNINGS=error python -m pytest
↓
python -m pytest

Likewise:

A=1 B=2 pytest

can have the assignments removed before invocation matching.

It is still not a complete shell evaluation.


---

56. re.escape(expected)

The code dynamically constructs:

expected = f"{prefix}{candidate}"

for example:

python -m pytest

Then:

re.escape(expected)

makes that dynamic text literal for regex purposes.

This matters because package strings may contain characters such as:

.
-

that could otherwise be interpreted specially.

Mental model:

> Treat this expected invocation as literal text, not regex language.




---

57. Invocation must begin the segment

Current match starts with:

^

which means:

> start of string/segment.



So:

pytest -q

matches.

But:

echo pytest

does not.

That is exactly what we want because:

mentioning the word pytest
≠
invoking pytest


---

58. Positive lookahead for command boundary

Current regex ends with:

(?=\s|$)

This is a positive lookahead.

Its practical meaning here:

> After the expected package invocation, the next position must be whitespace or the end of the string.



Therefore:

pytest
pytest -q
pytest tests/

can match.

But:

pytestfoo
pytest123

do not accidentally count as pytest.


---

59. Invocation examples you already classified correctly

For:

package = pytest

current outcomes are:

Command	Match

pytest -q	True
python -m pytest tests/	True
echo pytest	False
pytestfoo	False
uv run pytest -x	True


That prediction demonstrated that you understood the direct-invocation boundary.


---

60. One major current limitation: install order is not established

This was an important discovery.

Consider:

steps:
  - run: pytest
  - run: pip install -r requirements-dev.txt

Human reasoning says:

pytest occurred BEFORE the changed requirements were installed

So this should not be strong evidence that the changed installed dependency was exercised.

But the current implementation performs two independent searches:

∃ install command
AND
∃ execution command

It does not currently prove:

install position < execution position

Therefore the current reader can return:

supported

and, assuming all surrounding CI gates pass:

workflow → proven

even for the reversed order.

This is not a newly discovered bug requiring a new audit. It is already part of AUDIT-002's proof-boundary analysis.


---

61. The deeper AUDIT-002 lesson

The current CI evidence can be thought of as levels.

LEVEL 1 — STATIC RECOGNITION
The YAML visibly contains admitted install + exercise commands.

LEVEL 2 — EXECUTION-GROUNDED
Those corresponding steps are known to have executed successfully.

LEVEL 3 — VERSION-GROUNDED
Runtime evidence establishes the exact proposed dependency version.

LEVEL 4 — EXERCISED-VERSION-GROUNDED
That observed exact version is then known to have been exercised.

The current implementation is closest to:

Level 1
+
successful job/workflow evidence

It does not yet fully establish Level 2–4.

That explains limitations such as:

pip install ... || true
continue-on-error
conditional/skipped steps
reversed install/exercise order
runtime step correspondence
exact installed version
same interpreter/environment continuity

This is one of the strongest architectural lessons from the whole CI section:

> A claim should be no stronger than the evidence actually establishing it.




---

62. LR-001 — first proven workflow in the human detail

Aggregate code chooses:

proven = next(
    (result for result in results if result.state == "proven"),
    None,
)

Suppose:

A → unresolved
B → proven
C → proven

Aggregate state:

proven

is correct.

workflows=results preserves:

A
B
C

But the human detail names only B, the first proof witness.

This may be:

a diagnostic/presentation limitation

but it is not currently considered:

an aggregation correctness defect

Why?

Because one witness is sufficient for the existential state.

The open question is whether human presentation should communicate:

one witness

or:

all witnesses / witness count

This remains LR-001 rather than a formal defect.


---

63. Current _extract_job_definitions(...) knowledge boundary

Now we reach the exact point where our detailed source study currently stops.

We have learned the first stage of:

_extract_job_definitions(text)

Current beginning:

lines = text.splitlines()

jobs_index: int | None = None
jobs_indent: int | None = None

Then it searches for the first plain:

jobs:


---

64. splitlines()

Suppose:

name: Tests

jobs:
  test:
    steps:
      - run: pytest

splitlines() conceptually produces:

[
    "name: Tests",
    "",
    "jobs:",
    "  test:",
    "    steps:",
    "      - run: pytest",
]

Newline characters are removed.

Leading indentation remains.

That is essential because this narrow reader uses indentation as structural evidence.


---

65. enumerate(...)

The scanner uses:

for index, line in enumerate(lines):

enumerate gives:

index
+
value

Conceptually:

0 → "name: Tests"
1 → ""
2 → "jobs:"
3 → "  test:"

The line position matters because the reader later needs to slice the original text structure.


---

66. .strip()

Inside:

stripped = line.strip()

.strip() removes leading/trailing whitespace for comparison.

So:

"    jobs:   "

becomes:

"jobs:"

But the original line remains available separately.

That allows the function to:

use stripped text for semantic recognition
+
use original text for indentation

A subtle but useful pattern.


---

67. Blank/comment skipping

Current scanner does:

if not stripped or stripped.startswith("#"):
    continue

Therefore:

# CI jobs below


jobs:

still works.

continue means:

> Stop processing this current loop iteration and move to the next one.




---

68. Exact jobs: recognition

It requires:

if stripped == "jobs:":

So this does not count:

workflow_jobs:

and this comment does not count:

# jobs:

The current reader is intentionally looking for one plain mapping key it knows how to reason about.


---

69. jobs_index

When found:

jobs_index = index

records:

> Where in the line sequence did the jobs: mapping begin?



Later scanning starts from:

jobs_index + 1


---

70. jobs_indent

The code calculates:

jobs_indent = len(line) - len(line.lstrip())

Suppose:

"    jobs:"

has four leading spaces.

Then:

length including spaces
-
length without leading spaces
=
4

So:

jobs_indent = 4

This is a simple indentation-measurement technique.


---

71. Why break

Once the first admitted plain jobs: is found:

break

ends that search loop.

So the reader does not attempt to discover and reconcile multiple arbitrary jobs: structures.

Again:

bounded known grammar

rather than:

general YAML understanding


---

72. Missing jobs: returns None

After scanning:

if jobs_index is None or jobs_indent is None:
    return None

So this:

name: CI

workflow_jobs:
  test:
    ...

produces:

None

because no exact admitted:

jobs:

mapping exists.

That is the exact point where our detailed source study currently stops.

We have not yet learned the following lines deeply:

direct child-job scanning
first child establishing job_indent
nested key filtering
sibling job start collection
job-body slicing
_extract_run_commands(...)
inline run values
block run values
_JOB_KEY_PATTERN details
_RUN_PATTERN details

Those are next, not part of your current required learned checkpoint.


---

73. One more architecture principle: shared library does not imply shared responsibility

This came directly from the restructuring.

Previously:

packaging_method.py

contained both:

dependency version semantics
target Python specifier semantics

because both used the third-party Python library:

packaging

The restructuring split that into:

dependency/versioning.py

and:

target/python_specifier.py

Why?

Because:

uses same library

does not imply:

answers same product question

This is a mature architecture principle:

> Group code around responsibility/cohesion, not merely around implementation technology.



We have only introduced this concept; later learning units will make it concrete.


---

74. A plan does not own permanent filenames

One of the newest governance clarifications also matters for your engineering mental model.

A plan owns:

responsibility
sequence
proof obligations
stop conditions

An ADR and active source own:

accepted architecture
actual current module structure

Therefore:

old plan says:
src/upgradepilot/workflow_commands.py

accepted architecture moves responsibility:
src/upgradepilot/ci/workflow_commands.py

The solution is:

update the live plan

not:

recreate obsolete workflow_commands.py

Historical dated records retain old names because they document historical reality.

That is why our old learning notes remain untouched while the live plan uses the new paths.


---

75. What your actual learning depth is right now

This is important because “we discussed it” must not become “mastered.”

Area	Current honest depth

Responsibility-based architecture	Introduced / mapped
CI dependency-exercise product question	Operationally understood
proven / no_successful_ci / unresolved	Operationally understood
Exact-head evidence concept	Operationally understood
Aggregate evaluator mechanics	Operationally understood with guidance / implementation-adjacent
Tuple/generator/next/any	Operationally understood at current use sites
Per-workflow gate order	Operationally understood with guidance
Evidence authority distinctions	Operationally understood
Workflow command-reader architecture	Implementation-adjacent, still in progress
Install matcher	Operationally understood with guidance
Package invocation matcher	Operationally understood with guidance
Command-reader limitations	Good conceptual exposure
_extract_job_definitions first stage	Introduced/operationally understood
_extract_job_definitions child scan onward	Not yet learned
Independent CI ownership	Not demonstrated yet
Writing/modifying central CI test independently	Not demonstrated yet
Independent architecture design ownership	Not demonstrated yet


That matches the learning plan: Unit 1 is closed at operational depth, Unit 2 and Unit 3 still have ownership gates open, Unit 4 remains active, and Units 5 onward have not yet been taught in this package.


---

76. The entire learned flow in one picture

This is the picture I most want you to retain:

Canonical dependency change
│
│  package
│  normalized package
│  explicit direct requirements install path
│
↓
Exact-head workflow inputs
│
├── WorkflowRun
├── WorkflowJob(s)
└── exact RepositoryFileEvidence
        │
        ↓
PER-WORKFLOW EVALUATOR
        │
        ├── successful completed job exists?
        │      no → no_successful_ci
        │
        ├── parent run completed-successfully?
        │      no → unresolved
        │
        ├── workflow definition available?
        │      no → unresolved
        │
        ├── definition revision == run head SHA?
        │      no → unresolved
        │
        ├── explicit requirements install path exists?
        │      no → unresolved
        │
        ↓
BOUNDARY INTO COMMAND READER
        │
        ├── readable jobs mapping?
        │
        ├── exactly one current admitted job?
        │
        ├── extract visible run commands
        │
        ├── ∃ admitted pip install of exact source?
        │
        └── ∃ direct invocation of package?
                │
                ├── missing evidence → unresolved
                │
                └── both found → command supported
                                    ↓
                          workflow result = proven

ALL PER-WORKFLOW RESULTS
        ↓
materialize tuple
        ↓
∃ proven workflow?
│
├── yes
│   → aggregate proven
│
└── no
    ↓
∃ successful completed job anywhere?
│
├── no
│   → no_successful_ci
│
└── yes
    → unresolved

That is the actual conceptual spine of everything we have learned so far.


---

77. What it proves — and what it never proves

Keep this boundary extremely clear.

Current proven means roughly:

At least one successful exact-head workflow path
satisfied the currently admitted static dependency-install
and direct-package-exercise evidence rule.

It does not inherently mean:

the proposed dependency version was definitely the runtime-installed version

the exact corresponding install step itself succeeded

the exercise definitely occurred after installation

all workflow jobs exercised the dependency

all supported Python versions were tested

the package is compatible

the upgrade is safe

the PR should be merged

the maintainer should accept the update

The current module's own docstring makes the compatibility/safety/decision nonclaim explicit.


---

78. What you should be able to answer after studying this review

Use these as your self-check. Do not worry if one or two require rereading; the point is to identify the exact weak spots before continuing.

1. Explain why github/actions.py and ci/dependency_exercise.py belong to different responsibilities even though both participate in CI analysis.


2. Explain proven, no_successful_ci, and unresolved without using vague words such as “pass” and “fail.”


3. Explain why exact workflow-definition revision equality with run.head_sha matters.


4. Explain why dependency identity evidence is not automatically CI consumption evidence.


5. Explain why tuple(generator) means all workflows have already been evaluated before next(...) searches for the first proven witness.


6. Explain when next(..., None) is preferable to any(...).


7. Explain why an expected missing piece of evidence should become unresolved, while an impossible internal state may justify assert.


8. Given a per-workflow scenario, walk the gates in the correct order and say which early return wins.


9. Explain why supported from workflow_commands.py is weaker than proven from dependency_exercise.py.


10. Explain why pip install -r ./requirements-dev.txt can match requirements-dev.txt, but ../requirements-dev.txt is not semantically resolved.


11. Explain why echo pytest is not a direct package invocation while uv run pytest -x currently is.


12. Explain why pytestfoo is prevented from matching pytest.


13. Explain the current exactly-one-job limitation and the safer possible same-job existential generalization.


14. Explain why reversed pytest → pip install ordering can currently still satisfy the static command rule, and why that matters.


15. Reconstruct the beginning of _extract_job_definitions(...): splitlines() → scan → skip blank/comments → exact jobs: → jobs_index → jobs_indent → missing mapping returns None.


16. Explain why src/upgradepilot/, experiments/, and tools/ can all contain executable Python while representing different architectural responsibilities.


17. Explain why using the same third-party library does not necessarily justify putting two responsibilities in the same module.


18. Explain why an old plan mentioning an old filename does not override a newer accepted architecture.



If you can answer those accurately in your own words, then the material before our exact current checkpoint is in reasonably strong shape. The next work after that is not a new topic: it is simply continuing _extract_job_definitions(...) from the direct-child-job scanning logic and finishing the remaining Unit 4 mechanics before we move toward an ownership exercise.
