"""Acquire GitHub Actions evidence for the exact pull-request head commit.

This provider module owns workflow-run/job/step acquisition, pagination, and identity
reconciliation. It produces factual execution evidence only; workflow command meaning
and dependency-exercise interpretation remain in the CI domain.
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any

from .api import (
    GitHubApiClient,
    GitHubResponseError,
    optional_str,
    required_list,
    required_nonnegative_int,
    required_positive_int,
    required_str,
)
from .pull_request import PullRequestIdentity

_RESULTS_PER_PAGE = 100
_MAX_WORKFLOW_RUNS = 1_000
_MAX_JOBS_PER_RUN = 1_000


@dataclass(frozen=True, slots=True)
class WorkflowRun:
    run_id: int
    workflow_id: int
    name: str
    event: str
    head_sha: str
    status: str
    conclusion: str | None
    run_attempt: int


@dataclass(frozen=True, slots=True)
class WorkflowStep:
    number: int
    name: str
    status: str
    conclusion: str | None


@dataclass(frozen=True, slots=True)
class WorkflowJob:
    job_id: int
    run_id: int
    name: str
    head_sha: str
    status: str
    conclusion: str | None
    steps: tuple[WorkflowStep, ...] | None


class GitHubActionsClient(GitHubApiClient):
    """Read exact-head GitHub Actions evidence through a bounded read-only path."""

    def get_exact_head_workflow_runs(
        self,
        identity: PullRequestIdentity,
    ) -> tuple[WorkflowRun, ...]:
        url = self.api_url(f"/repos/{identity.repository}/actions/runs")
        records: list[WorkflowRun] = []
        expected_total: int | None = None
        page = 1

        while expected_total is None or len(records) < expected_total:
            data = self._get_json_object(
                url,
                resource="workflow-run",
                params={
                    "event": "pull_request",
                    "head_sha": identity.head_sha,
                    "per_page": _RESULTS_PER_PAGE,
                    "page": page,
                },
            )
            try:
                total_count = required_nonnegative_int(data, "total_count")
                items = required_list(data, "workflow_runs")
            except KeyError as exc:
                raise GitHubResponseError(
                    "GitHub workflow-run response is missing required field: "
                    f"{exc.args[0]}."
                ) from exc

            if total_count > _MAX_WORKFLOW_RUNS:
                raise GitHubResponseError(
                    "The exact-head workflow-run search exceeds the current "
                    f"acquisition limit of {_MAX_WORKFLOW_RUNS} runs."
                )
            if expected_total is None:
                expected_total = total_count
            elif total_count != expected_total:
                raise GitHubResponseError(
                    "GitHub workflow-run total changed during pagination: "
                    f"expected {expected_total} but later observed {total_count}."
                )

            for item_index, item in enumerate(items):
                if not isinstance(item, Mapping):
                    raise GitHubResponseError(
                        "GitHub workflow-run response item "
                        f"{len(records) + item_index + 1} was not an object."
                    )
                records.append(self._parse_workflow_run(identity, item))

            if len(records) > expected_total:
                raise GitHubResponseError(
                    "GitHub returned more workflow runs than its total_count declared."
                )
            if len(items) < _RESULTS_PER_PAGE:
                break
            page += 1

        if expected_total is None or len(records) != expected_total:
            raise GitHubResponseError(
                "GitHub workflow-run pagination was incomplete: "
                f"expected {expected_total or 0} runs but acquired {len(records)}."
            )
        return tuple(records)

    def get_workflow_jobs(
        self,
        identity: PullRequestIdentity,
        run: WorkflowRun,
    ) -> tuple[WorkflowJob, ...]:
        if run.head_sha != identity.head_sha:
            raise GitHubResponseError(
                "Cannot acquire jobs for a workflow run bound to a different head SHA."
            )

        url = self.api_url(
            f"/repos/{identity.repository}/actions/runs/{run.run_id}/jobs"
        )
        records: list[WorkflowJob] = []
        expected_total: int | None = None
        page = 1

        while expected_total is None or len(records) < expected_total:
            data = self._get_json_object(
                url,
                resource="workflow-job",
                params={
                    "filter": "latest",
                    "per_page": _RESULTS_PER_PAGE,
                    "page": page,
                },
            )
            try:
                total_count = required_nonnegative_int(data, "total_count")
                items = required_list(data, "jobs")
            except KeyError as exc:
                raise GitHubResponseError(
                    "GitHub workflow-job response is missing required field: "
                    f"{exc.args[0]}."
                ) from exc

            if total_count > _MAX_JOBS_PER_RUN:
                raise GitHubResponseError(
                    "The workflow run exceeds the current complete job-acquisition "
                    f"limit of {_MAX_JOBS_PER_RUN} jobs."
                )
            if expected_total is None:
                expected_total = total_count
            elif total_count != expected_total:
                raise GitHubResponseError(
                    "GitHub workflow-job total changed during pagination: "
                    f"expected {expected_total} but later observed {total_count}."
                )

            for item_index, item in enumerate(items):
                if not isinstance(item, Mapping):
                    raise GitHubResponseError(
                        "GitHub workflow-job response item "
                        f"{len(records) + item_index + 1} was not an object."
                    )
                records.append(self._parse_workflow_job(identity, run, item))

            if len(records) > expected_total:
                raise GitHubResponseError(
                    "GitHub returned more workflow jobs than its total_count declared."
                )
            if len(items) < _RESULTS_PER_PAGE:
                break
            page += 1

        if expected_total is None or len(records) != expected_total:
            raise GitHubResponseError(
                "GitHub workflow-job pagination was incomplete: "
                f"expected {expected_total or 0} jobs but acquired {len(records)}."
            )
        return tuple(records)

    @staticmethod
    def _parse_workflow_run(
        identity: PullRequestIdentity,
        data: Mapping[str, Any],
    ) -> WorkflowRun:
        try:
            event = required_str(data, "event")
            head_sha = required_str(data, "head_sha")
            if event != "pull_request":
                raise GitHubResponseError(
                    f"Workflow run event was {event!r}, not 'pull_request'."
                )
            if head_sha != identity.head_sha:
                raise GitHubResponseError(
                    "Workflow run head SHA does not match the frozen pull-request head."
                )
            return WorkflowRun(
                run_id=required_positive_int(data, "id"),
                workflow_id=required_positive_int(data, "workflow_id"),
                name=required_str(data, "name"),
                event=event,
                head_sha=head_sha,
                status=required_str(data, "status"),
                conclusion=optional_str(data, "conclusion"),
                run_attempt=required_positive_int(data, "run_attempt"),
            )
        except KeyError as exc:
            raise GitHubResponseError(
                "GitHub workflow-run item is missing required field: "
                f"{exc.args[0]}."
            ) from exc

    @staticmethod
    def _parse_workflow_job(
        identity: PullRequestIdentity,
        run: WorkflowRun,
        data: Mapping[str, Any],
    ) -> WorkflowJob:
        try:
            run_id = required_positive_int(data, "run_id")
            head_sha = required_str(data, "head_sha")
            if run_id != run.run_id:
                raise GitHubResponseError(
                    "Workflow job run ID does not match the requested workflow run."
                )
            if head_sha != identity.head_sha:
                raise GitHubResponseError(
                    "Workflow job head SHA does not match the frozen pull-request head."
                )

            raw_steps = data.get("steps")
            if raw_steps is None:
                steps = None
            elif isinstance(raw_steps, list):
                parsed_steps: list[WorkflowStep] = []
                for step_index, step in enumerate(raw_steps):
                    if not isinstance(step, Mapping):
                        raise GitHubResponseError(
                            "GitHub workflow-job step "
                            f"{step_index + 1} was not an object."
                        )
                    parsed_steps.append(GitHubActionsClient._parse_workflow_step(step))
                steps = tuple(parsed_steps)
            else:
                raise GitHubResponseError(
                    "GitHub field 'steps' must be an array or absent."
                )

            return WorkflowJob(
                job_id=required_positive_int(data, "id"),
                run_id=run_id,
                name=required_str(data, "name"),
                head_sha=head_sha,
                status=required_str(data, "status"),
                conclusion=optional_str(data, "conclusion"),
                steps=steps,
            )
        except KeyError as exc:
            raise GitHubResponseError(
                "GitHub workflow-job item is missing required field: "
                f"{exc.args[0]}."
            ) from exc

    @staticmethod
    def _parse_workflow_step(data: Mapping[str, Any]) -> WorkflowStep:
        try:
            return WorkflowStep(
                number=required_positive_int(data, "number"),
                name=required_str(data, "name"),
                status=required_str(data, "status"),
                conclusion=optional_str(data, "conclusion"),
            )
        except KeyError as exc:
            raise GitHubResponseError(
                "GitHub workflow-step item is missing required field: "
                f"{exc.args[0]}."
            ) from exc


__all__ = (
    "GitHubActionsClient",
    "WorkflowJob",
    "WorkflowRun",
    "WorkflowStep",
)
