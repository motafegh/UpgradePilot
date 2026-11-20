"""Correlate exact static workflow jobs and steps with one captured attempt.

GitHub provider modules own the factual static and runtime records. This CI module owns only
the deterministic relationship between those independently acquired records for the bounded
ordinary route or the prepared literal-matrix route. The latter first compares compatible
job origins and then preserves independent step matches and omissions for established jobs.

Correlation answers identity only. Runtime status/conclusion is preserved on the matched
``WorkflowStep`` but is not interpreted here as dependency installation, exercise, or success.
"""

from __future__ import annotations

from collections import Counter
from collections.abc import Sequence
from dataclasses import dataclass, replace
from typing import Literal

from ..github.actions import WorkflowJob, WorkflowRun, WorkflowStep
from ..github.repository import RepositoryTextFile
from ..github.workflow_instance_commands import materialize_workflow_job_instance
from ..github.workflow_definition import (
    JobProblem,
    ReusableWorkflowJobDefinition,
    RunStepDefinition,
    StepProblem,
    StepsJobDefinition,
    UsesStepDefinition,
    WorkflowDefinition,
    WorkflowDefinitionProblem,
    parse_workflow_definition,
)
from ..github.workflow_specialization import (
    PreparedWorkflowJobInstances,
    WorkflowJobInstanceIdentity,
)


type CorrelatableWorkflowStep = RunStepDefinition | UsesStepDefinition
type WorkflowRuntimeCorrelationState = Literal[
    "correlated", "correlated_with_skipped_jobs", "partially_correlated", "unresolved"
]


@dataclass(frozen=True, slots=True)
class WorkflowRuntimeStepCorrelation:
    """One user-declared static step matched to one factual runtime step record."""

    static_step: CorrelatableWorkflowStep
    runtime_step: WorkflowStep
    job_instance: WorkflowJobInstanceIdentity | None = None


@dataclass(frozen=True, slots=True)
class WorkflowRuntimeStepProblem:
    source_index: int
    reason: str


@dataclass(frozen=True, slots=True)
class WorkflowJobAssociationBasis:
    """Affirmative source witnesses and independent omissions for one associated job."""

    explicit_job_name: str | None
    witness_step_numbers: tuple[int, ...]
    step_problems: tuple[WorkflowRuntimeStepProblem, ...]


@dataclass(frozen=True, slots=True)
class UnmatchedWorkflowJobInstance:
    instance: WorkflowJobInstanceIdentity
    reason: str
    candidate_job_ids: tuple[int, ...]


@dataclass(frozen=True, slots=True)
class UnassignedRuntimeJob:
    job: WorkflowJob
    reason: str
    candidate_instances: tuple[WorkflowJobInstanceIdentity, ...]


@dataclass(frozen=True, slots=True)
class ScopedWorkflowRuntimeEvidence:
    run_id: int
    run_attempt: int
    head_sha: str
    unmatched_instances: tuple[UnmatchedWorkflowJobInstance, ...]
    unassigned_jobs: tuple[UnassignedRuntimeJob, ...]
    unresolved_source_jobs: tuple[int, ...]


@dataclass(frozen=True, slots=True)
class WorkflowRuntimeJobCorrelation:
    """One static steps job matched to one runtime job plus its user-step matches."""

    static_job: StepsJobDefinition
    runtime_job: WorkflowJob
    steps: tuple[WorkflowRuntimeStepCorrelation, ...]
    job_instance: WorkflowJobInstanceIdentity | None = None
    association: WorkflowJobAssociationBasis | None = None

    @property
    def skipped_without_steps(self) -> bool:
        job = self.runtime_job
        return job.status == "completed" and job.conclusion == "skipped" and job.steps == ()


@dataclass(frozen=True, slots=True)
class WorkflowRuntimeCorrelationResult:
    """Workflow-scoped correlation result with ambiguity preserved as unresolved."""

    state: WorkflowRuntimeCorrelationState
    reason: str
    detail: str
    jobs: tuple[WorkflowRuntimeJobCorrelation, ...] = ()
    scoped: ScopedWorkflowRuntimeEvidence | None = None

    @property
    def has_job_matches(self) -> bool:
        return self.state in {"correlated", "correlated_with_skipped_jobs", "partially_correlated"}


def correlate_workflow_runtime(
    source: RepositoryTextFile,
    run: WorkflowRun,
    jobs: Sequence[WorkflowJob],
    *,
    prepared: PreparedWorkflowJobInstances | None = None,
) -> WorkflowRuntimeCorrelationResult:
    """Correlate the first admitted ordinary static workflow class to runtime evidence.

    Positive correlation requires an exact static/run revision match, ordinary non-strategy
    steps jobs with unique literal job names, an exact static/runtime job-name bijection, and
    deterministic user-step display identities that appear once and in order within each
    runtime job. Explicit literal step names are used directly; admitted unnamed steps use
    GitHub Runner's provider-defined display-name rule. Runtime-only setup/post/completion
    steps are allowed between those user-declared steps. An explicitly skipped completed
    job with a supplied empty step list retains its job identity without step matches.
    """

    if (
        prepared is not None and isinstance(prepared.definition, WorkflowDefinition)
        and any(isinstance(job, StepsJobDefinition) and job.strategy is not None
                for job in prepared.definition.jobs)
    ):
        return _correlate_prepared_matrix(source, run, jobs, prepared)

    if source.revision != run.head_sha:
        return _unresolved(
            "workflow_revision_mismatch",
            "Static workflow revision does not match the runtime workflow head SHA.",
        )

    if any(job.run_id != run.run_id or job.head_sha != run.head_sha for job in jobs):
        return _unresolved(
            "runtime_job_scope_mismatch",
            "A runtime job belongs to a different run or head revision.",
        )
    if len({job.job_id for job in jobs}) != len(jobs):
        return _unresolved(
            "duplicate_runtime_job_id",
            "Runtime job IDs are not unique in the supplied attempt.",
        )

    definition = prepared.definition if prepared is not None else parse_workflow_definition(source)
    if definition.source != source:
        return _unresolved("workflow_source_mismatch", "Prepared job instances have another source.")
    if isinstance(definition, WorkflowDefinitionProblem):
        return _unresolved(
            "static_workflow_definition_unresolved",
            f"Static workflow definition is unresolved: {definition.reason}: {definition.detail}",
        )

    static_jobs: list[StepsJobDefinition] = []
    static_job_names: list[str] = []
    for job in definition.jobs:
        if isinstance(job, JobProblem):
            return _unresolved(
                "static_job_unresolved",
                f"Static job structure is unresolved: {job.reason}: {job.detail}",
            )
        if isinstance(job, ReusableWorkflowJobDefinition):
            return _unresolved(
                "reusable_workflow_job_unsupported",
                f"Reusable workflow job {job.key!r} is outside the first correlation class.",
            )
        assert isinstance(job, StepsJobDefinition)
        if job.strategy is not None:
            return _unresolved(
                "static_job_strategy_unsupported",
                f"Job {job.key!r} uses strategy/matrix expansion, which is not yet correlated.",
            )
        if job.name is None:
            return _unresolved(
                "static_job_name_missing",
                f"Job {job.key!r} has no explicit display name for bounded correlation.",
            )
        if job.name.contains_expression:
            return _unresolved(
                "static_job_name_dynamic",
                f"Job {job.key!r} has a dynamic display name that cannot be matched literally.",
            )
        job_name = job.name.text
        if not job_name.strip():
            return _unresolved(
                "static_job_name_empty",
                f"Job {job.key!r} has an empty display name.",
            )
        static_jobs.append(job)
        static_job_names.append(job_name)

    duplicate_static_job_name = _first_duplicate(static_job_names)
    if duplicate_static_job_name is not None:
        return _unresolved(
            "duplicate_static_job_name",
            f"Static job display name {duplicate_static_job_name!r} is not unique.",
        )

    runtime_job_names = [job.name for job in jobs]
    duplicate_runtime_job_name = _first_duplicate(runtime_job_names)
    if duplicate_runtime_job_name is not None:
        return _unresolved(
            "duplicate_runtime_job_name",
            f"Runtime job display name {duplicate_runtime_job_name!r} is not unique.",
        )

    if set(static_job_names) != set(runtime_job_names):
        return _unresolved(
            "static_runtime_job_name_set_mismatch",
            "Static and runtime job display-name sets do not form a one-to-one match.",
        )

    runtime_jobs_by_name = {job.name: job for job in jobs}
    ordinary_instances = {
        instance.identity.job_source_index: instance.identity
        for prepared_job in prepared.jobs
        for instance in prepared_job.instances
        if instance.identity.kind == "ordinary"
    } if prepared is not None else {}
    correlations: list[WorkflowRuntimeJobCorrelation] = []
    for static_job, static_job_name in zip(static_jobs, static_job_names, strict=True):
        runtime_job = runtime_jobs_by_name[static_job_name]
        instance = ordinary_instances.get(static_job.source_index)
        if prepared is not None and instance is None:
            return _unresolved(
                "ordinary_job_instance_unavailable",
                "The ordinary job has no retained prepared instance.",
            )
        job = WorkflowRuntimeJobCorrelation(static_job, runtime_job, (), instance)
        if job.skipped_without_steps:
            correlations.append(job)
            continue
        step_result = _correlate_job_steps(static_job, runtime_job)
        if isinstance(step_result, WorkflowRuntimeCorrelationResult):
            return step_result
        if instance is not None:
            step_result = tuple(replace(step, job_instance=instance) for step in step_result)
        correlations.append(
            WorkflowRuntimeJobCorrelation(
                static_job=static_job,
                runtime_job=runtime_job,
                steps=step_result,
                job_instance=instance,
            )
        )

    skipped = tuple(job for job in correlations if job.skipped_without_steps)
    if skipped:
        names = ", ".join(repr(job.runtime_job.name) for job in skipped)
        return WorkflowRuntimeCorrelationResult(
            state="correlated_with_skipped_jobs",
            reason="workflow_jobs_correlated_with_skipped_jobs_without_steps",
            detail=(
                f"The exact attempt reported these jobs skipped with zero steps: {names}. "
                "Their job identities are retained without step matches. Other jobs retain "
                "their exact ordered step matches."
            ),
            jobs=tuple(correlations),
        )

    return WorkflowRuntimeCorrelationResult(
        state="correlated",
        reason="workflow_jobs_and_steps_correlated",
        detail=(
            "Static ordinary jobs and user-declared steps were matched one-to-one to "
            "runtime jobs and ordered runtime step summaries."
        ),
        jobs=tuple(correlations),
    )


@dataclass(frozen=True, slots=True)
class _DeclaredJob:
    instance: WorkflowJobInstanceIdentity
    job: StepsJobDefinition
    name: str | None
    step_names: dict[str, CorrelatableWorkflowStep]
    step_problems: tuple[WorkflowRuntimeStepProblem, ...]


def _literal_job_name(job: StepsJobDefinition) -> str | None:
    name = job.name
    return name.text if name is not None and not name.contains_expression and name.text.strip() else None


def _declared_job(
    instance: WorkflowJobInstanceIdentity,
    job: StepsJobDefinition,
    original: StepsJobDefinition,
) -> _DeclaredJob:
    named_steps = []
    problems = []
    for step in job.steps:
        if isinstance(step, StepProblem):
            problems.append(WorkflowRuntimeStepProblem(step.source_index, "static_step_unresolved"))
            continue
        # Runner defaults are qualified only on the original literal declaration.
        # A generated unnamed run step cannot gain a guessed display witness.
        display_step = step if step.name is not None else original.steps[step.source_index]
        assert isinstance(display_step, (RunStepDefinition, UsesStepDefinition))
        name = _static_step_runtime_display_name(job.key, display_step)
        if isinstance(name, WorkflowRuntimeCorrelationResult):
            problems.append(WorkflowRuntimeStepProblem(step.source_index, name.reason))
        else:
            named_steps.append((name, step))
    counts = Counter(name for name, _ in named_steps)
    step_names = {}
    for name, step in named_steps:
        if counts[name] == 1:
            step_names[name] = step
        else:
            problems.append(WorkflowRuntimeStepProblem(step.source_index, "duplicate_static_step_name"))
    return _DeclaredJob(instance, job, _literal_job_name(job), step_names, tuple(problems))


@dataclass(frozen=True, slots=True)
class _JobComparison:
    matches: tuple[WorkflowRuntimeStepCorrelation, ...] = ()
    problems: tuple[WorkflowRuntimeStepProblem, ...] = ()
    explicit_name: str | None = None
    conflict: bool = False

    @property
    def has_witness(self) -> bool:
        return self.explicit_name is not None or bool(self.matches)


def _compare_job(
    declared: _DeclaredJob,
    job: WorkflowJob,
    by_name: dict[str, list[WorkflowStep]],
    observed_witness_names: set[str],
    distinct_step_names: set[str],
    invalid_step_order: bool,
) -> _JobComparison | None:
    if declared.name is not None and declared.name != job.name:
        return None
    shared = observed_witness_names & declared.step_names.keys()
    if observed_witness_names - declared.step_names.keys():
        if declared.name is not None or shared & distinct_step_names:
            return _JobComparison(conflict=True)
        # An unresolved source step can account for an otherwise foreign name.
        # This origin remains possible but contributes no affirmative witness.
        return _JobComparison() if declared.step_problems else None
    if invalid_step_order:
        return _JobComparison(conflict=declared.name is not None or bool(shared))
    matches = []
    problems = list(declared.step_problems)
    for name, step in declared.step_names.items():
        rows = by_name.get(name)
        if rows and len(rows) == 1:
            matches.append(WorkflowRuntimeStepCorrelation(step, rows[0], declared.instance))
        else:
            reason = (
                "runtime_step_match_ambiguous" if rows
                else "runtime_steps_unavailable" if job.steps is None
                else "runtime_step_match_missing"
            )
            problems.append(WorkflowRuntimeStepProblem(step.source_index, reason))
    numbers = tuple(match.runtime_step.number for match in matches)
    if any(current <= prior for prior, current in zip(numbers, numbers[1:])):
        return _JobComparison(conflict=True)
    return _JobComparison(tuple(matches), tuple(problems), declared.name)


# Bound the cross-product work separately from the provider's individual input limits.
_MAX_ASSOCIATION_COMPARISON_WORK = 500_000


def _correlate_prepared_matrix(
    source: RepositoryTextFile,
    run: WorkflowRun,
    jobs: Sequence[WorkflowJob],
    prepared: PreparedWorkflowJobInstances,
) -> WorkflowRuntimeCorrelationResult:
    """Collect all competing origins before committing any job association."""
    if source.revision != run.head_sha:
        return _unresolved("workflow_revision_mismatch", "The exact source differs from the captured run head.")
    if prepared.definition.source != source:
        return _unresolved("workflow_source_mismatch", "Prepared instances belong to another source.")
    definition = prepared.definition
    assert isinstance(definition, WorkflowDefinition)
    declared = []
    unknown_origins = {}
    for job in prepared.jobs:
        original = definition.jobs[job.source_index]
        if job.state != "complete":
            unknown_origins[job.source_index] = (
                _literal_job_name(original) if isinstance(original, StepsJobDefinition) else None
            )
        for instance in job.instances:
            assert isinstance(original, StepsJobDefinition)
            view = materialize_workflow_job_instance(definition, instance)
            declared.append(_declared_job(instance.identity, view, original))
    if prepared.problem is not None:
        unknown_origins = dict.fromkeys(range(len(definition.jobs)))

    step_name_counts = Counter(name for entry in declared for name in entry.step_names)
    distinct_step_names = {name for name, count in step_name_counts.items() if count == 1}
    counts = Counter(job.job_id for job in jobs)
    row_reasons: dict[int, str] = {}
    candidate_rows: dict[WorkflowJobInstanceIdentity, list[int]] = {
        entry.instance: [] for entry in declared
    }
    row_comparisons: dict[int, list[tuple[_DeclaredJob, _JobComparison]]] = {}
    starters = sum(1 + len(entry.job.steps) for entry in declared) + len(unknown_origins)
    observations = sum(1 + len(job.steps or ()) for job in jobs)
    if starters * observations > _MAX_ASSOCIATION_COMPARISON_WORK:
        return _scoped_result(
            run, (),
            tuple(UnmatchedWorkflowJobInstance(entry.instance, "association_work_limit", ()) for entry in declared),
            tuple(UnassignedRuntimeJob(job, "association_work_limit", ()) for job in jobs),
            tuple(unknown_origins),
        )

    for row, job in enumerate(jobs):
        if job.run_id != run.run_id or job.head_sha != run.head_sha:
            row_reasons[row] = "runtime_job_scope_mismatch"
            continue
        by_name: dict[str, list[WorkflowStep]] = {}
        for step in job.steps or ():
            by_name.setdefault(step.name, []).append(step)
        # Additional runner setup/post rows are allowed. A name admitted for a
        # different source origin is material and cannot be ignored as runner noise.
        seen_witnesses = set(by_name).intersection(step_name_counts)
        # Repeated display rows may be a scoped step problem, but cannot make
        # one source origin look uniquely compatible by eliminating its siblings.
        observed = {name for name in seen_witnesses if len(by_name[name]) == 1}
        numbers = tuple(step.number for step in job.steps or ())
        invalid_order = any(prior >= current for prior, current in zip(numbers, numbers[1:]))
        if job.status == "queued" and job.start_phase == "unknown":
            invalid_order = True  # A queued snapshot conflicts with positive start witnesses.
        if job.status == "completed" and job.conclusion == "skipped" and job.start_phase == "started":
            invalid_order = True  # An explicitly skipped job cannot supply a positive start witness.
        comparisons = []
        for entry in declared:
            pair = _compare_job(entry, job, by_name, observed, distinct_step_names, invalid_order)
            if pair is not None:
                comparisons.append((entry, pair))
        if not observed and any(pair.explicit_name is not None for _, pair in comparisons):
            comparisons = [
                (entry, pair) for entry, pair in comparisons if pair.explicit_name is not None
            ]
        row_comparisons[row] = comparisons
        has_signal = bool(seen_witnesses) or any(
            pair.explicit_name is not None or pair.conflict for _, pair in comparisons
        )
        if has_signal:
            for entry, _ in comparisons:
                candidate_rows[entry.instance].append(row)
        if counts[job.job_id] != 1:
            row_reasons[row] = "duplicate_runtime_job_id"
        elif any(pair.conflict for _, pair in comparisons):
            row_reasons[row] = "conflicting_job_or_step_witnesses"
        elif not has_signal:
            row_reasons[row] = "runtime_job_identity_witness_missing"
        elif any(name is None or name == job.name for name in unknown_origins.values()):
            row_reasons[row] = "static_competing_origin_unresolved"
        elif len(comparisons) != 1 or not comparisons[0][1].has_witness:
            row_reasons[row] = "static_job_match_ambiguous" if comparisons else "static_job_match_missing"

    matches = {}
    unassigned = []
    for row, job in enumerate(jobs):
        reason = row_reasons.get(row)
        comparisons = row_comparisons.get(row, [])
        if reason is None:
            (entry, pair), = comparisons
            # Test the reciprocal relation against all observed contenders, including
            # ambiguous rows. Never remove a winner and infer another by elimination.
            if len(candidate_rows[entry.instance]) == 1:
                matches[entry.instance] = WorkflowRuntimeJobCorrelation(
                    entry.job, job, pair.matches, entry.instance,
                    WorkflowJobAssociationBasis(
                        pair.explicit_name,
                        tuple(step.runtime_step.number for step in pair.matches),
                        pair.problems,
                    ),
                )
                continue
            reason = "runtime_job_match_ambiguous"
        candidates = (
            () if reason == "runtime_job_identity_witness_missing"
            else tuple(entry.instance for entry, _ in comparisons)
        )
        unassigned.append(UnassignedRuntimeJob(job, reason, candidates))
    unmatched = []
    for entry in declared:
        if entry.instance not in matches:
            candidates = candidate_rows[entry.instance]
            unmatched.append(UnmatchedWorkflowJobInstance(
                entry.instance, "runtime_job_match_unresolved" if candidates else "runtime_job_evidence_missing",
                tuple(dict.fromkeys(jobs[row].job_id for row in candidates)),
            ))
    return _scoped_result(
        run, tuple(matches[entry.instance] for entry in declared if entry.instance in matches),
        tuple(unmatched), tuple(unassigned), tuple(unknown_origins),
    )


def _scoped_result(
    run: WorkflowRun,
    matches: tuple[WorkflowRuntimeJobCorrelation, ...],
    unmatched: tuple[UnmatchedWorkflowJobInstance, ...],
    unassigned: tuple[UnassignedRuntimeJob, ...],
    unresolved_sources: tuple[int, ...],
) -> WorkflowRuntimeCorrelationResult:
    partial = unmatched or unassigned or unresolved_sources or any(
        match.association.step_problems and not match.skipped_without_steps for match in matches
    )
    if not matches:
        state, reason = "unresolved", "scoped_job_correspondence_unresolved"
    elif partial:
        state, reason = "partially_correlated", "scoped_job_or_step_correspondence_partial"
    elif any(match.skipped_without_steps for match in matches):
        state, reason = "correlated_with_skipped_jobs", "scoped_jobs_correlated_with_skips"
    else:
        state, reason = "correlated", "scoped_jobs_and_steps_correlated"
    return WorkflowRuntimeCorrelationResult(
        state, reason,
        f"Associated {len(matches)} declared jobs; {len(unmatched)} declared and "
        f"{len(unassigned)} reported jobs remain unassociated. Step evidence is retained per job.",
        matches, ScopedWorkflowRuntimeEvidence(
            run.run_id, run.run_attempt, run.head_sha, unmatched, unassigned, unresolved_sources,
        ),
    )


def find_correlated_runtime_step(
    correlation: WorkflowRuntimeCorrelationResult,
    *,
    job_key: str,
    step_source_index: int,
    instance: WorkflowJobInstanceIdentity | None,
    head_sha: str | None = None,
) -> WorkflowRuntimeStepCorrelation | None:
    jobs = tuple(
        job for job in correlation.jobs
        if job.static_job.key == job_key and job.job_instance == instance
        and (instance is None or job.static_job.source_index == instance.job_source_index)
        and (head_sha is None or job.runtime_job.head_sha == head_sha)
    )
    if len(jobs) != 1:
        return None
    steps = tuple(
        step for step in jobs[0].steps if step.static_step.source_index == step_source_index
    )
    if (
        len(steps) == 1
        and steps[0].job_instance == instance
        and steps[0].runtime_step in (jobs[0].runtime_job.steps or ())
    ):
        return steps[0]
    return None


def _correlate_job_steps(
    static_job: StepsJobDefinition,
    runtime_job: WorkflowJob,
) -> tuple[WorkflowRuntimeStepCorrelation, ...] | WorkflowRuntimeCorrelationResult:
    static_steps: list[CorrelatableWorkflowStep] = []
    static_step_names: list[str] = []
    for step in static_job.steps:
        if isinstance(step, StepProblem):
            return _unresolved(
                "static_step_unresolved",
                (
                    f"Job {static_job.key!r} contains unresolved static step structure: "
                    f"{step.reason}: {step.detail}"
                ),
            )
        assert isinstance(step, (RunStepDefinition, UsesStepDefinition))
        step_name = _static_step_runtime_display_name(static_job.key, step)
        if isinstance(step_name, WorkflowRuntimeCorrelationResult):
            return step_name
        static_steps.append(step)
        static_step_names.append(step_name)

    duplicate_static_step_name = _first_duplicate(static_step_names)
    if duplicate_static_step_name is not None:
        return _unresolved(
            "duplicate_static_step_name",
            (
                f"Job {static_job.key!r} repeats static step display name "
                f"{duplicate_static_step_name!r}."
            ),
        )

    if runtime_job.steps is None:
        return _unresolved(
            "runtime_steps_unavailable",
            f"Runtime job {runtime_job.name!r} did not provide step summaries.",
        )

    runtime_steps = runtime_job.steps
    runtime_numbers = [step.number for step in runtime_steps]
    if len(runtime_numbers) != len(set(runtime_numbers)):
        return _unresolved(
            "duplicate_runtime_step_number",
            f"Runtime job {runtime_job.name!r} contains duplicate step numbers.",
        )
    if any(current <= previous for previous, current in zip(runtime_numbers, runtime_numbers[1:])):
        return _unresolved(
            "runtime_step_numbers_not_ordered",
            f"Runtime job {runtime_job.name!r} step numbers are not strictly increasing.",
        )

    matched_indices: list[int] = []
    correlations: list[WorkflowRuntimeStepCorrelation] = []
    for static_step, static_step_name in zip(static_steps, static_step_names, strict=True):
        matches = [
            (index, runtime_step)
            for index, runtime_step in enumerate(runtime_steps)
            if runtime_step.name == static_step_name
        ]
        if not matches:
            return _unresolved(
                "runtime_step_match_missing",
                (
                    f"Runtime job {runtime_job.name!r} has no step matching static display "
                    f"name {static_step_name!r}."
                ),
            )
        if len(matches) != 1:
            return _unresolved(
                "runtime_step_match_ambiguous",
                (
                    f"Runtime job {runtime_job.name!r} has multiple steps matching static "
                    f"display name {static_step_name!r}."
                ),
            )
        runtime_index, runtime_step = matches[0]
        matched_indices.append(runtime_index)
        correlations.append(
            WorkflowRuntimeStepCorrelation(
                static_step=static_step,
                runtime_step=runtime_step,
            )
        )

    if any(current <= previous for previous, current in zip(matched_indices, matched_indices[1:])):
        return _unresolved(
            "static_runtime_step_order_mismatch",
            (
                f"Runtime job {runtime_job.name!r} does not preserve the declared user-step "
                "name order as an ordered subsequence."
            ),
        )

    return tuple(correlations)


def _static_step_runtime_display_name(
    job_key: str,
    step: CorrelatableWorkflowStep,
) -> str | WorkflowRuntimeCorrelationResult:
    """Return the runtime display identity GitHub Runner assigns to one admitted step."""

    if step.name is not None:
        if step.name.contains_expression:
            return _unresolved(
                "static_step_name_dynamic",
                (
                    f"Job {job_key!r} step {step.source_index} has a dynamic display name "
                    "that cannot be matched literally."
                ),
            )
        if not step.name.text.strip():
            return _unresolved(
                "static_step_name_empty",
                f"Job {job_key!r} step {step.source_index} has an empty display name.",
            )
        return step.name.text

    if isinstance(step, RunStepDefinition):
        if step.command.contains_expression:
            return _unresolved(
                "unnamed_run_step_display_name_dynamic",
                (
                    f"Job {job_key!r} step {step.source_index} omits name and its run "
                    "command contains an expression, so the runner-derived display name "
                    "cannot be predicted literally."
                ),
            )
        payload = _runner_display_payload(step.command.text)
        if not payload:
            return _unresolved(
                "unnamed_run_step_display_name_empty",
                (
                    f"Job {job_key!r} step {step.source_index} omits name and its run "
                    "command has no non-empty first line for runner display-name identity."
                ),
            )
        return f"Run {payload}"

    if step.reference.contains_expression:
        return _unresolved(
            "unnamed_uses_step_display_name_dynamic",
            (
                f"Job {job_key!r} step {step.source_index} omits name and its uses "
                "reference is dynamic, so the runner-derived display name cannot be "
                "predicted literally."
            ),
        )

    reference = step.reference.text
    if reference.startswith("docker://"):
        return _unresolved(
            "unnamed_container_step_display_name_unsupported",
            (
                f"Job {job_key!r} step {step.source_index} uses an unnamed container "
                "action whose runner display identity is outside the first bounded "
                "repository-action correlation class."
            ),
        )

    payload = _runner_display_payload(reference)
    if not payload:
        return _unresolved(
            "unnamed_uses_step_display_name_empty",
            (
                f"Job {job_key!r} step {step.source_index} omits name and its uses "
                "reference cannot produce a non-empty runner display identity."
            ),
        )
    return f"Run {payload}"


def _runner_display_payload(value: str) -> str:
    """Mirror GitHub Runner FormatStepName payload trimming for literal values."""

    result = value.lstrip(" \t\r\n")
    newline_positions = [position for position in (result.find("\r"), result.find("\n")) if position >= 0]
    if newline_positions:
        result = result[: min(newline_positions)]
    return result


def _first_duplicate(values: Sequence[str]) -> str | None:
    seen: set[str] = set()
    for value in values:
        if value in seen:
            return value
        seen.add(value)
    return None


def _unresolved(reason: str, detail: str) -> WorkflowRuntimeCorrelationResult:
    return WorkflowRuntimeCorrelationResult(
        state="unresolved",
        reason=reason,
        detail=detail,
    )


__all__ = (
    "CorrelatableWorkflowStep",
    "WorkflowRuntimeCorrelationResult",
    "WorkflowRuntimeCorrelationState",
    "WorkflowRuntimeJobCorrelation",
    "WorkflowRuntimeStepCorrelation",
    "correlate_workflow_runtime",
)
