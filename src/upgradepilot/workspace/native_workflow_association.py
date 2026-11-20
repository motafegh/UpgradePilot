"""Validate the recorded job/step association boundary using retained material only."""

from collections import Counter

from ..ci.dependency_exercise import WorkflowDependencyCoverageInput
from ..ci.workflow_runtime_correlation import WorkflowRuntimeCorrelationResult
from ..github.workflow_definition import WorkflowDefinition
from ..github.workflow_instance_commands import materialize_workflow_job_instance
from ..github.workflow_specialization import WorkflowJobInstance, WorkflowJobInstanceIdentity
from .native_representation import NativeReconstructionError


def _require(condition: bool, detail: str) -> None:
    if not condition:
        raise NativeReconstructionError("invalid_native_material", detail)


def validate_scoped_workflow_associations(
    correlation: WorkflowRuntimeCorrelationResult,
    supplied: WorkflowDependencyCoverageInput,
    instances: dict[WorkflowJobInstanceIdentity, WorkflowJobInstance],
) -> None:
    """Check membership and recorded witness references without recomputing matching."""
    scope = correlation.scoped
    prepared = supplied.prepared
    assert scope is not None and prepared is not None
    definition = prepared.definition
    _require(isinstance(definition, WorkflowDefinition), "Scoped association lacks its prepared definition.")
    assert isinstance(definition, WorkflowDefinition)
    run = supplied.run
    _require(
        (scope.run_id, scope.run_attempt, scope.head_sha) == (run.run_id, run.run_attempt, run.head_sha),
        "Scoped association has another retained run, attempt or head.",
    )
    expected_unresolved = (
        tuple(range(len(definition.jobs))) if prepared.problem is not None
        else tuple(job.source_index for job in prepared.jobs if job.state != "complete")
    )
    _require(scope.unresolved_source_jobs == expected_unresolved,
             "Scoped association omits or changes unresolved source origins.")
    instance_refs = [match.job_instance for match in correlation.jobs]
    instance_refs.extend(item.instance for item in scope.unmatched_instances)
    _require(
        len(instance_refs) == len(instances) and set(instance_refs) == instances.keys(),
        "Associated and unmatched job instances do not partition their retained inventory.",
    )
    observations = Counter(supplied.jobs)
    partition = Counter(match.runtime_job for match in correlation.jobs)
    partition.update(item.job for item in scope.unassigned_jobs)
    _require(observations == partition, "Associated and unassigned observations differ from retained jobs.")
    job_ids = Counter(job.job_id for job in supplied.jobs)
    candidates = {}
    for item in scope.unassigned_jobs:
        _require(
            bool(item.reason)
            and len(set(item.candidate_instances)) == len(item.candidate_instances)
            and set(item.candidate_instances) <= instances.keys(),
            "Unassigned job references another candidate inventory.",
        )
        for candidate in item.candidate_instances:
            candidates.setdefault(candidate, set()).add(item.job.job_id)
    for item in scope.unmatched_instances:
        _require(
            bool(item.reason) and len(set(item.candidate_job_ids)) == len(item.candidate_job_ids)
            and set(item.candidate_job_ids) <= candidates.get(item.instance, set()),
            "Unmatched instance references an unretained runtime candidate.",
        )

    incomplete_steps = False
    for match in correlation.jobs:
        identity = match.job_instance
        assert identity is not None  # The partition above requires admitted instances.
        instance = instances[identity]
        job = match.runtime_job
        basis = match.association
        _require(
            basis is not None and job_ids[job.job_id] == 1
            and (job.run_id, job.head_sha) == (run.run_id, run.head_sha)
            and not (job.status == "queued" and job.start_phase == "unknown")
            and not (job.status == "completed" and job.conclusion == "skipped"
                     and job.start_phase == "started")
            and match.static_job == materialize_workflow_job_instance(definition, instance),
            "Association does not identify one material job and exact scoped workflow instance.",
        )
        assert basis is not None
        numbers = tuple(step.runtime_step.number for step in match.steps)
        observed = tuple(step.number for step in job.steps or ())
        _require(
            all(a < b for a, b in zip(observed, observed[1:]))
            and all(a < b for a, b in zip(numbers, numbers[1:]))
            and basis.witness_step_numbers == numbers,
            "Association witness numbers differ from its ordered retained step rows.",
        )
        declared_name = match.static_job.name
        if basis.explicit_job_name is not None:
            _require(
                declared_name is not None and not declared_name.contains_expression
                and bool(declared_name.text.strip())
                and basis.explicit_job_name == declared_name.text == job.name,
                "Association has another source-defined job witness.",
            )
        elif declared_name is not None and not declared_name.contains_expression and declared_name.text.strip():
            _require(False, "Association omits its source-defined job witness.")
        _require(bool(numbers) or basis.explicit_job_name is not None,
                 "Association has no affirmative job or step witness.")
        source_indices = [step.static_step.source_index for step in match.steps]
        _require(all(a < b for a, b in zip(source_indices, source_indices[1:])),
                 "Associated steps do not follow declared source order.")
        source_indices.extend(problem.source_index for problem in basis.step_problems)
        _require(
            all(problem.reason for problem in basis.step_problems)
            and sorted(source_indices) == sorted(step.source_index for step in match.static_job.steps),
            "Scoped step matches and problems do not partition their declared job.",
        )
        for step in match.steps:
            _require(
                step.job_instance == identity and step.static_step in match.static_job.steps
                and step.runtime_step in (job.steps or ())
                and sum(other.name == step.runtime_step.name for other in job.steps or ()) == 1,
                "Associated step has another retained job or instance.",
            )
            name = step.static_step.name
            if name is not None:
                _require(not name.contains_expression and name.text == step.runtime_step.name,
                         "Associated step has another source-defined name witness.")
        incomplete_steps |= bool(basis.step_problems) and not match.skipped_without_steps
    partial = bool(scope.unmatched_instances or scope.unassigned_jobs or scope.unresolved_source_jobs
                   or incomplete_steps)
    expected_state = (
        "unresolved" if not correlation.jobs
        else "partially_correlated" if partial
        else "correlated_with_skipped_jobs" if any(match.skipped_without_steps for match in correlation.jobs)
        else "correlated"
    )
    _require(correlation.state == expected_state, "Association aggregate contradicts scoped evidence.")
