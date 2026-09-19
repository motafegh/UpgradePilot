# Current End-to-End Product Flow — Public PR to Evidence Report and Synthesis Boundary

**Learning-artifact date:** 2026-09-19  
**Source/test evidence horizon:** main@ddf4ceb0944376ea7c7e1f5e52a229cb78572adb  
**Roadmap responsibility:** Group 10 — real product composition: public PR to evidence-backed output  
**Artifact role:** current pinned end-to-end learning/reference snapshot after the source-verified product-flow reconstruction  
**Target depth:** **must master / own** the major producer → evidence → composition → consumer boundaries, identity/provenance handoffs, branch activation/stopping, evidence-strength transitions, PublicPullRequestInvestigation role, standalone synthesis boundary, CLI presentation boundary, and important non-claims; provider/parser/library details remain delegated to focused notes

This note answers:

> **What does UpgradePilot actually do today when given one public dependency-update pull request, and where does each stronger claim stop?**

The shortest current model is:

~~~text
CLI input
→ exact public-PR identity
→ coherent changed-file / exact-file evidence
→ one trusted dependency transition + source contexts
→ CI evidence branch
→ package / upstream evidence branches
→ mechanism-specific impact and target applicability
→ PublicPullRequestInvestigation
→ standalone abstention-only synthesis
AND separately
→ current CLI evidence rendering
~~~

The most important presentation fact is:

~~~text
current CLI
→ investigate_public_pull_request(...)
→ render PublicPullRequestInvestigation

current CLI
!= synthesize_maintainer_action(...)
~~~

So today:

~~~text
typed investigation evidence
exists in the normal CLI path

standalone synthesis
exists as a separate product function

maintainer recommendation
is not yet rendered by the CLI
~~~

---

## 1. Why an end-to-end view matters

Many UpgradePilot modules are individually conservative and well-bounded.

But product correctness depends on their composition.

A fact can be correct locally and still fail to support a downstream proposition because:

~~~text
identity was not preserved
a stronger evidence class is missing
one branch stopped
the consumer requires another proposition
the evidence is static rather than runtime
the mechanism applies but action permission is not established
~~~

So the useful ownership question is not:

> Which files exist?

It is:

> **Which proposition does each stage establish, what identity does it preserve, who consumes it, and what stronger claim is still unavailable?**

---

## 2. Current top-level owners

The most important end-to-end owners are:

~~~text
src/upgradepilot/__main__.py
→ package execution adapter

src/upgradepilot/cli.py
→ arguments, environment input, presentation, shell exit policy

src/upgradepilot/investigation.py
→ application orchestration and typed investigation result

src/upgradepilot/dependency/analysis.py
→ PR-wide trusted dependency transition + source contexts

src/upgradepilot/ci/
→ static/runtime dependency coverage evidence

src/upgradepilot/pypi/
→ exact package release evidence

src/upgradepilot/upstream/
→ trusted upstream identity / interval / semantic evidence

src/upgradepilot/impact/
→ mechanism-specific candidate/applicability reasoning

src/upgradepilot/target/
→ exact target declarations / bounded target relevance/context

src/upgradepilot/maintainer_action.py
→ standalone action-relative synthesis
~~~

The main architectural rule is:

> **The application orchestrator coordinates already-owned domain evidence; it should not silently redefine what each domain result means.**

---

## 3. Program entry: __main__.py stays intentionally tiny

When the package is executed as:

~~~text
python -m upgradepilot
~~~

Python runs:

~~~text
src/upgradepilot/__main__.py
~~~

That adapter does only:

~~~text
from .cli import main
raise SystemExit(main())
~~~

This keeps:

~~~text
argument parsing
provider acquisition
domain interpretation
rendering
exit-code policy
~~~

out of the package adapter.

The integer returned by cli.main becomes the operating-system process exit status.

This small boundary prevents a second command-line orchestration path from emerging in __main__.py.

---

## 4. CLI owns input, environment, rendering, and exit policy

Primary owner:

~~~text
src/upgradepilot/cli.py
~~~

Current required arguments:

~~~text
repository
pull_number
~~~

Repository is expected in:

~~~text
owner/repository
~~~

form.

The CLI also currently reads:

~~~text
GITHUB_TOKEN
~~~

from the ambient environment and passes it into the application.

That token behavior is a known trust/configuration concern under AUDIT-008-F9.

This note records the current fact only:

~~~text
ambient GITHUB_TOKEN
→ currently influences public GitHub acquisition
~~~

It does not teach that behavior as ideal or final.

---

## 5. CLI delegates product orchestration

The main successful path is:

~~~text
cli.main(...)
→ investigate_public_pull_request(
     repository,
     pull_number,
     token=os.getenv("GITHUB_TOKEN")
  )
→ _print_investigation(...)
→ return 0
~~~

The CLI does not coordinate GitHub/PyPI/upstream/impact modules itself.

That responsibility belongs to:

~~~text
src/upgradepilot/investigation.py
~~~

This separation allows a future interface to reuse the same typed investigation without copying product sequencing out of the CLI.

---

## 6. CLI exit codes are operational, not safety verdicts

Current CLI maps broad operational failures:

~~~text
0
→ investigation returned and evidence was rendered

2
→ input rejected

3
→ GitHub acquisition failure

4
→ GitHub response could not establish required evidence
~~~

A crucial non-claim is:

~~~text
exit 0
!= dependency update safe
!= merge recommended
~~~

Exit 0 means the current read-only investigation completed far enough to produce its typed evidence output.

The evidence itself may still contain:

~~~text
unsupported
unresolved
conflicted
not evaluated
not established
~~~

states.

---

## 7. The application boundary owns orchestration

Primary owner:

~~~text
src/upgradepilot/investigation.py
~~~

Main entry:

~~~text
investigate_public_pull_request(...)
~~~

Its responsibility is:

~~~text
instantiate/use provider clients
→ acquire exact public-PR evidence
→ call domain owners in dependency order
→ preserve independent branch results
→ return one typed PublicPullRequestInvestigation
~~~

It does not own presentation.

It does not own final action policy.

It does not make target repository mutations.

---

## 8. First trust anchor: PullRequestIdentity

The application first acquires:

~~~text
PullRequestIdentity
~~~

This freezes material PR identity such as:

~~~text
repository
PR number
base ref / base SHA
head ref / head SHA
declared changed-file count
state / merged state
author/title
~~~

Downstream exact-head or exact-base/head evidence is tied back to this identity.

The critical mental model is:

~~~text
repository + PR number
→ locate the pull request

base/head immutable SHAs
→ anchor evidence to the analyzed proposal
~~~

A later mutable view of the same PR must not silently substitute for the frozen revision identity.

---

## 9. Changed-file acquisition is part of snapshot coherence

The PR changed-file path is not treated as a casual list.

Current acquisition logic establishes bounded coherence against the frozen PR identity.

The reconstructed source/test model includes protections around:

~~~text
exact repository/path locator identity
frozen head revision
complete declared changed-file count
post-acquisition PR identity re-check
base/head/count drift detection
multi-page drift handling
~~~

This is not transactional GitHub snapshot isolation.

It is a bounded observable coherence contract strong enough for the admitted public-PR evidence path.

That distinction matters:

~~~text
coherent exact-identity acquisition
!= global transactional snapshot
~~~

---

## 10. Dependency analysis is PR-wide, not first-match

Primary owner:

~~~text
src/upgradepilot/dependency/analysis.py
~~~

It considers the admitted dependency sources across the whole PR.

Current source families include bounded support for:

~~~text
requirements / constraints exact pins
modified uv.lock
modified pyproject.toml optional-extra changes
~~~

Arbitrary unrelated files are ignored.

Recognized-source problems remain explicit.

The coordinator does not simply take the first plausible dependency update.

---

## 11. Different dependency sources use different evidence methods

### Requirements / constraints

For exact requirement changes, the coherent PR patch can establish:

~~~text
old exact pin
→ new exact pin
~~~

and records source provenance such as:

~~~text
extraction_method = changed_file_patch
~~~

### uv.lock

A modified lockfile requires exact immutable files:

~~~text
base uv.lock
head uv.lock
~~~

and structured extraction records:

~~~text
extraction_method = exact_base_head_files
~~~

### pyproject optional extras

A modified pyproject.toml can likewise require exact base/head file comparison for the admitted optional-extra rule.

The general lesson is:

> **Evidence acquisition method follows the source format and proposition, not one universal changed-file strategy.**

---

## 12. PR-wide consensus creates one trusted dependency transition

After source-specific extraction, UpgradePilot compares the admitted results.

The coordinator will not promote:

~~~text
one valid source
+
one recognized unresolved/problem source
~~~

into a trusted dependency transition.

Likewise conflicting package/version transitions remain explicit.

Only when admitted evidence agrees does it create:

~~~text
DependencyVersionChange
~~~

with source-evidence provenance.

So:

~~~text
one plausible change
!= trusted PR-wide dependency transition
~~~

---

## 13. DependencyChangeAnalysis adds source contexts

A successful dependency analysis returns:

~~~text
DependencyChangeAnalysis
~~~

containing:

~~~text
dependency: DependencyVersionChange
source_contexts: tuple[DependencySourceContext, ...]
~~~

These contexts preserve facts such as:

~~~text
exact target repository
exact head revision
source path
source type
package identity
optional-extra/group/lock context where applicable
~~~

But:

~~~text
source context
!= workflow selected it
!= command executed it
!= dependency installed
!= target compatible
~~~

It is a handoff into later environment/CI reasoning.

---

## 14. Dependency failure is an early product stop

If dependency analysis returns:

~~~text
DependencyChangeProblem
~~~

the application does not continue into dependency-specific CI/PyPI/upstream/impact branches.

The CLI then renders states such as:

~~~text
Dependency change: unsupported
CI dependency coverage: not evaluated
Package evidence: not evaluated
Upstream repository: not evaluated
Artifact applicability: not evaluated
Target Python relevance: not evaluated
~~~

This is not a crash.

It is an explicit product result:

~~~text
the admitted front door could not establish one supported dependency transition
~~~

---

## 15. Once the transition is trusted, branches begin

When the dependency result is a trusted DependencyVersionChange, current application orchestration activates several evidence responsibilities.

The broad shape is:

~~~text
trusted dependency transition
├─ CI / workflow branch
├─ proposed + old package release branch
│  └─ artifact-serviceability branch
└─ upstream semantic branch
   └─ Python-support impact branch
~~~

The branches share exact transition identity but remain independently meaningful.

A failure in one branch does not automatically erase evidence already earned by another.

---

## 16. CI branch: exact-head workflow evidence

The application asks the GitHub Actions provider for:

~~~text
exact-head workflow runs
~~~

for the frozen PR head.

For each run it acquires:

~~~text
workflow jobs
exact workflow definition at the analyzed head
~~~

It also acquires exact project-environment source bundles when required for uv/project-environment reasoning.

These become:

~~~text
WorkflowDependencyCoverageInput
~~~

values.

---

## 17. CI branch: one static definition feeds current consumers

The current static CI architecture, taught in Group 8, uses:

~~~text
exact workflow run step
+ effective shell context
→ parser-backed StaticCommandAnalysis
→ shared exact command occurrence identity
~~~

Then the same static analysis supports:

~~~text
direct requirements observation
project-environment selection
direct package invocation
~~~

CI composes those with:

~~~text
repository checkout provenance
dependency source contexts
source membership / uv reachability
static ordering
~~~

to derive changed-dependency consumption/direct-exercise evidence.

---

## 18. CI branch: runtime strengthening stays bounded

The current strengthening ladder is:

~~~text
supported exact static occurrence
+ positive structural/whole-step relation
+ admitted execution profile
+ exact static↔runtime owning-step correlation
+ completed-successful unmasked runtime step
→ bounded Runtime-Correlated Support
~~~

Top-level CI states include:

~~~text
supported_runtime_correlated
supported_not_correlated
no_successful_ci
unresolved
~~~

Even the strongest current positive CI state does not prove:

~~~text
exact installed dependency version
selected wheel/sdist
full compatibility
all affected behavior
maintainer action
~~~

---

## 19. Real S001 pressure illustrates the dependency→CI path

A useful real product-simulation flow is S001 Pydantic / soupsieve.

The preserved shape includes:

~~~text
uv.lock dependency source
→ changed package soupsieve
→ docs environment selection
→ uv sync --all-packages --group docs
→ selected-root reachability witness
   mkdocs-llmstxt
   → beautifulsoup4
   → soupsieve
~~~

This establishes useful static dependency consumption for the docs environment.

The later Cycle-3 architecture also admits the sole ordinary top-level command shape for bounded runtime strengthening when exact runtime correlation exists.

This real case is useful for the front/CI half of the product.

It is not presented as a case that exercises every PyPI/upstream/artifact/synthesis branch.

---

## 20. Proposed package release is the next shared external evidence

The application requests exact PyPI evidence for:

~~~text
dependency.package
dependency.proposed_version
~~~

A successful result is:

~~~text
PackageReleaseEvidence
~~~

carrying exact requested/published identity and distribution/project metadata.

If proposed release evidence cannot be established, downstream branches that require it cannot proceed normally.

Problems remain typed rather than being interpreted as “no impact.”

---

## 21. Old release evidence enables artifact comparison

If the proposed release exists, the application also requests:

~~~text
old package release
~~~

for the exact dependency transition.

Exact old/proposed release evidence feeds:

~~~text
build_artifact_serviceability_impact_candidate(...)
~~~

The artifact branch asks whether published wheel capability changed across the exact transition.

This branch is independent from the upstream semantic support-drop branch.

---

## 22. Artifact branch: candidate before applicability

Current artifact flow:

~~~text
exact old release
+ exact proposed release
→ published wheel-tag inventories
→ removed/added capability sets
→ ArtifactServiceabilityImpactCandidate
~~~

A candidate establishes a package-level artifact mechanism.

It does not establish target applicability.

Current normal application then calls:

~~~text
evaluate_artifact_serviceability_impact(candidate)
~~~

without exact TargetWheelCompatibilityEvidence.

Therefore target-specific artifact applicability normally remains:

~~~text
unresolved
~~~

when the stronger target witness is unavailable.

---

## 23. Partial Target artifact environment is composed separately

When a real artifact candidate exists, current application also tries to derive bounded static target-environment context from supported direct-requirements CI relationships.

It may preserve:

~~~text
workflow path/revision
selected job when safely available
runner label
setup-python version
dependency installation declaration
limitations
~~~

But:

~~~text
TargetArtifactEnvironmentEvidence
!= TargetWheelCompatibilityEvidence
~~~

and current static target evidence intentionally keeps:

~~~text
exact_wheel_compatibility_state = unresolved
~~~

This is the current missing-producer boundary taught in Group 7.

---

## 24. Multi-job Target selection remains a composition limitation

CI can already know the exact consuming job.

But current Target artifact-environment composition does not yet transfer that exact CI job identity into the Target interpreter.

The Target interpreter may therefore see a multi-job workflow and return:

~~~text
ambiguous_target_job_selection
~~~

This is a real current F4 composition limitation.

But fixing it would improve static Target selection only.

It still would not manufacture exact supported wheel tags.

Keep:

~~~text
CI job handoff gap
!= exact target wheel-tag producer gap
~~~

---

## 25. Upstream branch begins from trusted repository identity

From proposed PyPI release evidence, current application resolves a trusted upstream repository.

The upstream resolver does not blindly trust one convenient project URL.

The reconstructed trust model reconciles admitted repository-association evidence with package-file provenance and requires an acceptable matching GitHub identity.

Possible unresolved/problem states remain explicit.

This creates the upstream identity anchor for release/changelog reasoning.

---

## 26. Exact dependency interval controls upstream reasoning

From the trusted dependency transition:

~~~text
old version
→ proposed version
~~~

the application creates the release interval:

~~~text
old-exclusive
proposed-inclusive
~~~

Then it acquires the package release index and selects crossed releases.

This keeps semantic analysis bounded to the exact transition.

The system is not asking:

> What has ever changed in this project?

It asks:

> **What authoritative evidence lies inside the exact dependency interval being proposed?**

---

## 27. Tag and changelog evidence are pinned to immutable upstream identity

Current upstream flow resolves the proposed version tag.

Admitted canonical spellings include:

~~~text
<version>
v<version>
~~~

A successful tag result yields an exact resolved commit.

The changelog path is then discovered against that exact immutable commit, and the changelog is acquired at that same commit.

This supports:

~~~text
exact dependency interval
+ exact upstream repository
+ exact proposed release commit
+ exact tagged source evidence
~~~

rather than mutable latest-branch prose.

---

## 28. Upstream authority precedes semantic extraction

The application assembles:

~~~text
AuthoritativeUpstreamIntervalEvidence
~~~

from the exact interval sources.

Only after that authority exists does it invoke the bounded support-drop evaluator.

The trust shape is:

~~~text
deterministic identity / source authority
→ bounded semantic candidate extraction
→ deterministic grounding / validation
→ GroundedPythonSupportDropClaim
~~~

The local model/extractor can propose semantic candidates.

It does not create source authority.

---

## 29. A grounded support-drop claim still does not prove target impact

If the current semantic path produces:

~~~text
GroundedPythonSupportDropClaim
~~~

the application builds:

~~~text
PythonSupportDropImpactCandidate
~~~

The mechanism is established.

Target exposure/activation remain:

~~~text
to_evaluate
~~~

This begins the Group-9 applicability path.

---

## 30. Python-support path selects one discriminating target investigation

Before exact target Python evidence, applicability is unresolved.

The mechanism-specific selector can choose:

~~~text
acquire_exact_target_python_declaration
~~~

with exact:

~~~text
repository
head revision
path = pyproject.toml
proposition key
~~~

The application rechecks that the selected repository/revision match the frozen PR target.

Then it performs the exact-head read.

---

## 31. Target Python evidence is interpreted and compared

The acquired target file passes through:

~~~text
interpret_target_python_declaration(...)
→ TargetPythonDeclaration / Problem
~~~

Then:

~~~text
evaluate_target_python_relevance(...)
~~~

asks only whether the dropped Python line intersects:

~~~text
[project].requires-python
~~~

for the exact target revision.

Possible results include:

~~~text
declared_python_overlap
outside_declared_python_range
target_declaration_unresolved
comparison_unsupported
~~~

---

## 32. Python-support applicability is reevaluated

The final mechanism-specific evaluation can become:

~~~text
established_applicable
established_not_applicable
unresolved
conflicted
~~~

For example:

~~~text
grounded Python 3.9 support drop
+ exact target requires-python includes stable 3.9.Z
→ bounded Python-support candidate applicable
~~~

Whereas:

~~~text
grounded Python 3.9 support drop
+ exact target requires-python >=3.10
→ bounded Python-support candidate not applicable
~~~

Neither result is a whole-update maintainer verdict.

---

## 33. PublicPullRequestInvestigation is the application evidence envelope

After all currently activated branches, investigation.py returns:

~~~text
PublicPullRequestInvestigation
~~~

It contains heterogeneous typed results including:

~~~text
pull_request
changed_files
dependency_result
workflow_evidence
ci_coverage_result
package_result
old_package_result
artifact candidate/impact/Target results
upstream repository/index/tag/changelog/interval results
support-drop result
target Python evidence/relevance
pre/post Python-support impact
selected Python-support investigation
~~~

This is intentionally richer than one scalar result.

It preserves:

~~~text
what succeeded
what failed
what stayed unresolved
what was never activated
what exact evidence/provenance produced each branch state
~~~

---

## 34. PublicPullRequestInvestigation is not a recommendation

The dataclass docstring calls it:

~~~text
Typed result of the current read-only evidence and reasoning sequence.
~~~

That is its responsibility.

It does not itself answer:

~~~text
merge?
run checks?
investigate?
block?
defer?
~~~

Those are later maintainer-action synthesis questions.

This distinction is fundamental to the current architecture.

---

## 35. Branch stopping does not erase independent evidence

Consider an upstream changelog-discovery problem:

~~~text
exact dependency transition established
CI evidence established
package release established
upstream repository established
tag established
changelog path unavailable
~~~

Then:

~~~text
upstream semantic support-drop branch stops
Python-support target investigation is not activated
Python-support impact is not produced
~~~

But independently earned CI/package/artifact evidence remains in the investigation.

The application does not collapse everything to one generic failure.

This enables later synthesis to explain:

~~~text
what is known
what branch stopped
what remains uncertain
~~~

---

## 36. Current standalone synthesis boundary

Primary owner:

~~~text
src/upgradepilot/maintainer_action.py
~~~

Current action type remains:

~~~text
MaintainerAction = Literal["abstain"]
~~~

So even at this horizon:

~~~text
no merge action
no targeted-check action
no investigate action
no block action
no defer action
~~~

has been admitted into executable synthesis.

The current evaluator explicitly refuses to infer those actions from strong-looking technical evidence.

---

## 37. Current abstention synthesis preserves material uncertainty

At the pinned horizon:

~~~text
main@ddf4ceb...
~~~

the F3 correction exists in source/tests.

synthesize_maintainer_action(...) now preserves selected material branch-stopping uncertainty from the typed investigation, including bounded classes such as:

~~~text
dependency transition problems
non-supported CI coverage states
package/upstream authority/source problems
artifact evidence problems
Target artifact-environment problems
unresolved/conflicted Python impact
unresolved/conflicted artifact impact
~~~

The projection remains synthesis-owned and bounded.

It does not copy the entire investigation into duplicate action-domain structures.

---

## 38. Residual uncertainty is not a new action permission

Suppose changelog discovery fails:

~~~text
ChangelogPathDiscoveryProblem(
  state = no_candidate_path
)
~~~

At this horizon, standalone synthesis can preserve a residual uncertainty message explaining that the upstream semantic branch stopped there.

But the action remains:

~~~text
abstain
~~~

This repair improves honesty of explanation.

It does not create:

~~~text
investigate
defer
block
~~~

permission.

That is why F3 is a synthesis-correctness repair rather than feature/action expansion.

---

## 39. Strong technical evidence still does not manufacture an action

Tests preserve an important case:

~~~text
CI state = supported_runtime_correlated
~~~

Yet:

~~~text
synthesize_maintainer_action(...)
→ action = abstain
~~~

because runtime-correlated dependency support alone does not satisfy any admitted non-abstention permission.

Likewise:

~~~text
Python-support candidate = established_applicable
~~~

does not automatically justify block.

Action-specific positive permission requires its own exact premises.

---

## 40. Current CLI does not call synthesis

This is the most important current presentation boundary.

cli.py imports:

~~~text
PublicPullRequestInvestigation
investigate_public_pull_request
~~~

It does not import/call:

~~~text
synthesize_maintainer_action
~~~

The successful CLI path is:

~~~text
investigate
→ print investigation evidence
→ return 0
~~~

not:

~~~text
investigate
→ synthesize
→ print recommendation
~~~

CLI tests explicitly assert that output does **not** include:

~~~text
Maintainer recommendation
~~~

---

## 41. CLI renders evidence at its owned proof strength

Examples of current rendered evidence include:

~~~text
Dependency change: supported / unsupported
CI dependency coverage: ...
Package evidence: ...
Upstream repository: ...
Artifact serviceability candidate: ...
Target artifact environment: ...
Exact wheel compatibility: unresolved
Artifact applicability: unresolved
Target Python declaration: ...
Target Python relevance: ...
~~~

The CLI is careful not to dump stronger-looking details that could imply more proof than the typed result owns.

For example, artifact rendering can say:

~~~text
Exact target wheel compatibility: not established
~~~

without printing a fabricated target tag set.

---

## 42. Current product topology therefore has two outputs

Conceptually:

~~~text
                 ┌──────────────────────────────┐
                 │ PublicPullRequestInvestigation│
                 └──────────────┬───────────────┘
                                │
                   ┌────────────┴────────────┐
                   │                         │
                   ▼                         ▼
         current CLI renderer      standalone synthesis
         evidence presentation     action = abstain
                   │                         │
                   ▼                         ▼
          human evidence text     MaintainerActionSynthesis
~~~

Today those two branches are not integrated into one public CLI recommendation flow.

That is intentional current incompleteness, not evidence that synthesis does not exist.

---

## 43. What a degraded upstream path looks like end to end

Take a normal-shaped current case:

~~~text
trusted dependency transition
→ CI branch runs
→ proposed/old package evidence runs
→ upstream repository resolves
→ proposed tag resolves
→ changelog discovery returns no_candidate_path
~~~

Then:

~~~text
changelog_path_result
→ typed problem

upstream_interval_result
→ not established

upstream_support_drop_result
→ inactive / not produced

target Python investigation
→ not activated

Python-support impact
→ not produced
~~~

Other independent branches may survive.

At the pinned horizon, standalone synthesis can preserve the branch-stopping changelog problem in:

~~~text
residual_uncertainty
~~~

while still returning:

~~~text
abstain
~~~

The CLI, however, remains the separate evidence renderer.

---

## 44. What a successful Python-support branch looks like end to end

A complete current integration-test-shaped path is:

~~~text
trusted DependencyVersionChange
→ proposed + old PyPI releases
→ trusted upstream repository
→ crossed release index
→ proposed version tag
→ tagged changelog authority
→ grounded Python-support-drop claim
→ PythonSupportDropImpactCandidate
→ pre-investigation applicability unresolved
→ select exact target pyproject read
→ TargetPythonDeclaration
→ target relevance
→ reevaluated applicability
~~~

If target range lies outside the dropped line:

~~~text
→ established_not_applicable
~~~

If it overlaps:

~~~text
→ established_applicable
~~~

Both are preserved inside PublicPullRequestInvestigation.

Neither directly changes the CLI into a recommendation surface.

---

## 45. What the artifact branch looks like end to end

A current artifact candidate path is:

~~~text
trusted DependencyVersionChange
→ exact old/proposed PyPI releases
→ published wheel-tag comparison
→ ArtifactServiceabilityImpactCandidate
→ immediate applicability evaluation without exact target tag witness
→ unresolved applicability
→ separate partial Target artifact-environment interpretation
~~~

This reveals one of the current strongest end-to-end bottlenecks:

~~~text
exact target wheel compatibility contract exists
but
normal exact target tag producer does not
~~~

The application correctly keeps the stronger proposition unresolved.

---

## 46. Evidence strength changes as it flows

One useful way to understand the whole system is as a sequence of increasingly specific propositions.

### Dependency identity ladder

~~~text
changed file
< source-specific dependency evidence
< PR-wide trusted dependency transition
~~~

### CI ladder

~~~text
static command/source relationship
< supported static dependency consumption
< bounded runtime-correlated support
~~~

### Upstream ladder

~~~text
package release exists
< trusted upstream repository/source authority
< bounded semantic candidate
< grounded support-drop claim
~~~

### Impact ladder

~~~text
grounded mechanism
< target-bound impact candidate
< target applicability
~~~

### Action ladder

~~~text
technical applicability
< action-specific evidence sufficiency
< positive maintainer-action permission
~~~

Each "<" means:

> a different or stronger proposition requiring additional evidence.

It is not a numeric confidence scale.

---

## 47. Exact identity is carried across domains

The whole path repeatedly preserves or revalidates identities such as:

~~~text
target repository
PR number
base SHA
head SHA
dependency normalized package
old/proposed versions
workflow path/revision
job key
step source index
command location
upstream repository
upstream release interval
tag/commit SHA
target file revision
~~~

Why so many?

Because a true fact about:

~~~text
another commit
another job
another release interval
another package
another target environment
~~~

is not automatically evidence for the current proposition.

Identity is not metadata decoration.

It is part of the proof.

---

## 48. Typed problems are part of product output semantics

Across providers/domains, the application often preserves typed problem values instead of throwing generic errors.

Examples include:

~~~text
DependencyChangeProblem
PackageReleaseProblem
UpstreamRepositoryProblem
CrossedReleaseIndexSelectionProblem
GitHubTagCommitProblem
ChangelogPathDiscoveryProblem
UpstreamIntervalAuthorityProblem
UpstreamSupportDropClaimProblem
TargetPythonDeclarationProblem
ArtifactServiceabilityEvidenceProblem
TargetArtifactEnvironmentProblem
~~~

These types let the application distinguish:

~~~text
branch produced a negative/refuted result
from
branch could not establish the required evidence
from
branch was never activated
~~~

That distinction matters later for honest synthesis and presentation.

---

## 49. Exceptions and typed evidence problems serve different roles

The CLI catches broad operational exceptions such as:

~~~text
UpgradePilotInputError
GitHubAcquisitionError
GitHubResponseError
~~~

and maps them to process exit codes.

Inside a successfully running investigation, many domain limitations instead become typed result/problem values.

So:

~~~text
process-level operational failure
!= domain-level unresolved evidence
~~~

Do not infer that every evidence problem should become a non-zero shell exit.

---

## 50. Current important normal-path gaps

At this snapshot, key gaps include:

### F4 — CI consuming job → Target composition

The exact CI consuming job is not fully transferred into Target job selection.

### F5 — exact target wheel-tag producer

The strong TargetWheelCompatibilityEvidence contract lacks a normal producer.

### F6 — exact runtime installed version/artifact witness

Current runtime-correlated CI support does not establish exact resolved/installed dependency artifact identity.

This should be added only if a selected downstream proposition requires it.

### F7 — bounded candidate/context discovery coverage

A favorable whole-update action such as merge would require explicit bounded positive closure rather than assuming discovered candidates are complete.

### presentation gap

The CLI does not yet render standalone synthesis.

These are different responsibilities and should not be collapsed into one generic “missing evidence” project.

---

## 51. Current product non-claims

Even after a successful read-only investigation, UpgradePilot does not currently claim that it has proven:

~~~text
universal dependency-file support
universal GitHub Actions semantics
every workflow/job/environment
exact installed dependency version
selected wheel/sdist in runtime CI
exact target wheel compatibility in the normal path
complete affected-behavior coverage
complete impact-candidate discovery
update safety
merge permission
block permission
investigate permission
defer permission
automatic repository mutation
~~~

The system's current value is in **evidence-bounded technical investigation and explicit uncertainty**, not vocabulary-complete action output.

---

## 52. Source/test proof at this horizon

Important current test families include:

~~~text
tests/test_dependency_analysis.py
tests/test_investigation.py
tests/test_cli.py
tests/test_ci_runtime_correlated_dependency_coverage.py
tests/test_artifact_serviceability.py
tests/test_python_support_impact.py
tests/test_maintainer_action.py
~~~

Together they protect different layers:

~~~text
dependency source/consensus
application branch composition
CLI presentation/exit policy
CI static/runtime proof
artifact candidate/applicability
Python-support investigation/applicability
standalone abstention synthesis
~~~

No single test file proves the whole product.

Composition tests are important because unit correctness alone does not prove producer→consumer reachability.

---

## 53. Historical hosted proof and current proof boundary

Cycle-3 hosted proof historically established:

~~~text
fresh installed package
Python 3.12.14
pip check
installed CLI
focused investigation 15/15
Cycle-3 focused 76/76
full deterministic product 604/604
~~~

That proof remains historical evidence for the then-current source/test horizon.

The current Group-10 snapshot includes later synthesis changes at:

~~~text
main@ddf4ceb...
~~~

This artifact-authoring session did not run a fresh full suite.

Therefore:

~~~text
current source/test contract inspection
+ current committed focused tests
!= fresh hosted/live proof of all external providers
~~~

---

## 54. Why one real case is not enough for the whole flow

The current product has several independent evidence mechanisms.

S001 is excellent pressure for:

~~~text
dependency source
uv reachability
CI command/environment selection
runtime-strengthening eligibility
~~~

S008 is excellent pressure for:

~~~text
artifact serviceability
wheel-path transition
source-fallback distinction
~~~

Other cases pressure action semantics.

No one current real public case should be falsely presented as proof that every end-to-end branch is normally reachable.

For complete orchestration learning, use:

~~~text
real cases for mechanism pressure
+
current integration tests for producer→consumer composition
+
source for actual ownership
~~~

That combination is stronger than inventing a synthetic “one case proves all” story.

---

## 55. Current fact, rationale, judgment, and open boundary

### Current implementation fact

UpgradePilot currently provides a read-only public-PR investigation pipeline that:

~~~text
establishes exact dependency identity
collects CI/package/upstream/target evidence
evaluates selected mechanism-specific impacts
preserves typed problems/unresolved states
returns PublicPullRequestInvestigation
~~~

It also has a standalone deterministic maintainer-action evaluator whose only admitted action is:

~~~text
abstain
~~~

At this horizon that evaluator preserves selected material branch-stopping uncertainty.

The CLI still renders investigation evidence only.

### Evidenced rationale

The source/tests/specifications and completed reconstruction consistently preserve:

~~~text
evidence acquisition
!= domain interpretation
!= applicability
!= action permission
!= presentation
~~~

### Engineering judgment

The separation is currently useful because it prevents:

~~~text
green CI
or
one applicable mechanism
or
one missing evidence source
~~~

from becoming an automatic maintainer recommendation.

### Open boundary

The active product journey is still improving the action layer and later presentation.

Therefore this artifact is a pinned end-to-end snapshot, not a claim that maintainer-action synthesis or CLI integration is final.

---

## 56. Depth calibration

### Must own

- CLI vs application orchestration;
- exact PR identity as the evidence anchor;
- PR-wide dependency consensus;
- source context vs workflow/runtime evidence;
- CI static → runtime-correlated evidence ladder;
- exact PyPI/upstream authority flow;
- semantic extraction vs deterministic grounding;
- impact candidate vs target applicability;
- artifact-serviceability missing exact target-tag producer;
- PublicPullRequestInvestigation as evidence envelope, not recommendation;
- standalone synthesis vs CLI evidence renderer;
- exit 0 is not a safety verdict;
- independent branch stopping/preservation;
- typed problem vs negative/refuted result vs inactive branch;
- identity/provenance handoff;
- action permission requires more than technical applicability.

### Understand operationally

- major investigation.py branch order;
- current dependency source families;
- current CI coverage states;
- upstream interval/tag/changelog path;
- Python-support target investigation;
- artifact Target partial-context path;
- current abstention residual-uncertainty projection;
- CLI exit-code classes and rendering role.

### Lookup-level

- exact client constructors;
- every provider method;
- every CLI print line;
- JSON helper internals;
- every dataclass field;
- every test fixture builder;
- full API transport handling.

### Deferred deliberately

- F9 authentication redesign;
- F4 Target job handoff repair;
- F5 exact wheel-tag producer;
- F6 runtime installed-version/artifact producer;
- F7 positive discovery/context closure;
- non-abstention action implementation;
- synthesis-to-CLI integration;
- automatic repository mutation.

---

## 57. Fast relearning route

When returning later:

~~~text
1. Open:
   src/upgradepilot/cli.py
   and identify what CLI owns vs delegates.

2. Open:
   src/upgradepilot/investigation.py
   and read PublicPullRequestInvestigation first.

3. Trace the normal spine:
   PR identity
   → changed files
   → analyze_dependency_change
   → CI
   → PyPI releases
   → artifact branch
   → upstream branch
   → Python-support branch.

4. Open:
   tests/test_investigation.py
   and read one:
   - complete Python-support path,
   - branch-stopping upstream problem,
   - artifact candidate/Target path.

5. Revisit:
   Group 8 for CI internals,
   Group 7 for artifact serviceability,
   Group 9 Note 1 for applicability/investigation.

6. Open:
   src/upgradepilot/maintainer_action.py
   and state:
   action family currently admitted = abstain only.

7. Open:
   tests/test_maintainer_action.py
   and inspect residual-uncertainty examples.

8. Return to:
   src/upgradepilot/cli.py
   and verify synthesis is still not invoked.

9. Read:
   tests/test_cli.py
   and locate:
   Maintainer recommendation not present.

10. State the final boundary:
    evidence report today
    != integrated maintainer recommendation.
~~~

---

## 58. Ownership / transfer questions

Without looking at this note, explain:

1. Why does __main__.py not own investigation orchestration?
2. Why is CLI exit code 0 not evidence that an update is safe?
3. Why does dependency analysis consider all admitted PR dependency sources rather than accept the first valid source?
4. What does DependencyChangeAnalysis.source_contexts establish, and what does it not establish?
5. Why can an upstream changelog problem stop the Python-support branch without erasing CI evidence?
6. Why is supported_runtime_correlated stronger than static consumption but weaker than exact installed-version evidence?
7. Why does a GroundedPythonSupportDropClaim still require exact target evidence?
8. Why can artifact serviceability establish a package-level candidate while target applicability remains unresolved?
9. Why is TargetArtifactEnvironmentEvidence not enough for exact wheel compatibility?
10. What is the role of PublicPullRequestInvestigation?
11. What does synthesize_maintainer_action currently produce?
12. Why does the current CLI not constitute a maintainer-action interface?
13. Why should a typed branch problem often survive in the investigation instead of becoming a process exception?
14. Why is exact identity/provenance part of proof rather than incidental metadata?
15. Which current gap would you investigate if a future selected action specifically required exact runtime installed-version identity?

### Transfer exercise

Suppose a PR produces:

~~~text
trusted dependency transition
CI = supported_runtime_correlated
proposed/old PyPI releases = available
artifact candidate = established
Target artifact environment = available
exact target wheel compatibility = unresolved
upstream changelog discovery = no_candidate_path
~~~

Explain:

~~~text
what the current investigation can honestly preserve,
what standalone synthesis can honestly say,
what the current CLI will render,
and which conclusions remain prohibited.
~~~

Then identify which pieces belong to:

~~~text
CI evidence
artifact applicability
upstream semantic authority
synthesis
presentation
~~~

without collapsing them into one risk verdict.

---

## 59. Evidence anchors

Pinned horizon:

~~~text
main@ddf4ceb0944376ea7c7e1f5e52a229cb78572adb
~~~

Primary end-to-end source:

~~~text
src/upgradepilot/__main__.py
src/upgradepilot/cli.py
src/upgradepilot/investigation.py
src/upgradepilot/dependency/analysis.py
src/upgradepilot/maintainer_action.py
~~~

Major delegated owners:

~~~text
src/upgradepilot/ci/
src/upgradepilot/pypi/
src/upgradepilot/upstream/
src/upgradepilot/impact/
src/upgradepilot/target/
~~~

Primary composition/presentation tests:

~~~text
tests/test_dependency_analysis.py
tests/test_investigation.py
tests/test_cli.py
tests/test_maintainer_action.py
~~~

Supporting focused learning packages:

~~~text
learning/2026-09-19-parser-backed-ci-command-evidence-and-runtime-strengthening/
learning/2026-09-19-artifact-serviceability-and-exact-target-wheel-applicability.md
learning/2026-09-19-impact-applicability-investigation-and-synthesis/01_impact_applicability_and_mechanism_specific_investigation.md
~~~

Completed reconstruction owner:

~~~text
working-memory/2026-09-19_1825_parent-synthesis-evidence-path-reaudit.md
~~~

Execution plan:

~~~text
plans/END_TO_END_PRODUCT_FLOW_LEARNING_AND_EVIDENCE_TO_ACTION_EXECUTION_PLAN.md
~~~

Current-system audit:

~~~text
audits/2026-09-19_AUDIT-008_current-system-evidence-to-action-readiness.md
~~~

Representative real pressure:

~~~text
S001
→ dependency / uv reachability / CI flow

S008
→ artifact serviceability / wheel-path distinction
~~~

This artifact is a pinned learning/reference snapshot. It is not a specification, live-state owner, final synthesis contract, or product-change authorization.

UP-SKILL:upgradepilot-learning-artifact
UP-SKILL:upgradepilot-planning-design
