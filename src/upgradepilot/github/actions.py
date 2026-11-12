"""Acquire GitHub Actions evidence for the exact pull-request head commit.

This provider module owns workflow-run/job/step acquisition, pagination, and identity
reconciliation. Job acquisition is bound to the captured workflow-run attempt so a
later rerun cannot silently replace the jobs paired with that run. The provider produces
factual execution evidence only; workflow command meaning and dependency-exercise
interpretation remain in the CI domain.
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass, field
from hashlib import sha256
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
from .job_log_transport import MAX_JOB_LOG_BYTES, download_bounded_job_log
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


@dataclass(frozen=True, slots=True)
class WorkflowJobLog:
    """Content-bound job log, separate from command execution or causal assessment."""

    repository: str
    head_sha: str
    run_id: int
    run_attempt: int
    job_id: int
    source_url: str
    utf8_bytes: int
    sha256: str
    text: str = field(repr=False)


class GitHubActionsClient(GitHubApiClient):
    """Read exact-head GitHub Actions evidence through a bounded read-only path."""

    def get_failed_workflow_job_log(
        self,
        identity: PullRequestIdentity,
        run: WorkflowRun,
        job: WorkflowJob,
        *,
        max_bytes: int = MAX_JOB_LOG_BYTES,
    ) -> WorkflowJobLog:
        """Retrieve one selected failed job from its already captured exact attempt.

        The caller must select a job returned by get_workflow_jobs(identity, run).
        This method cannot independently prove run-attempt membership from the
        job-log URL: the attempt-specific job-list acquisition owns that evidence.
        """
        if (
            run.event != "pull_request"
            or run.head_sha != identity.head_sha
            or run.run_attempt < 1
            or job.head_sha != identity.head_sha
            or job.run_id != run.run_id
            or job.job_id < 1
            or job.status != "completed"
            or job.conclusion != "failure"
        ):
            raise ValueError(
                "Selected workflow job is not a failed job at the frozen PR head/run."
            )

        url = self.api_url(
            f"/repos/{identity.repository}/actions/jobs/{job.job_id}/logs"
        )
        content = download_bounded_job_log(
            self._session, api_url=url,
            github_headers=self._headers,
            timeout=self._timeout,
            max_bytes=max_bytes,
        )
        try:
            text = content.decode("utf-8")
        except UnicodeDecodeError as exc:
            raise GitHubResponseError(
                "GitHub job log cannot be decoded as valid UTF-8."
            ) from exc
        return WorkflowJobLog(
            repository=identity.repository,
            head_sha=identity.head_sha,
            run_id=run.run_id,
            run_attempt=run.run_attempt,
            job_id=job.job_id,
            source_url=url,
            utf8_bytes=len(content),
            sha256=sha256(content).hexdigest(),
            text=text,
        )

    def get_selected_failed_workflow_job(
        self, identity: PullRequestIdentity,
        run_id: int, run_attempt: int, job_id: int,
    ) -> tuple[WorkflowRun, WorkflowJob]:
        """Bind one explicit user-selected job to a frozen PR run and attempt.

        Exactly two GitHub metadata GETs; refuse any job listing requiring
        pagination rather than accidentally using the newest attempt.
        """
        if any(type(value) is not int or value <= 0
               for value in (run_id, run_attempt, job_id)):
            raise ValueError("Selected CI coordinates must be positive integers.")
        run_data = self._get_json_object(
            self.api_url(
                f"/repos/{identity.repository}/actions/runs/{run_id}"
                f"/attempts/{run_attempt}"
            ),
            resource="selected-workflow-run-attempt",
        )
        run = self._parse_workflow_run(identity, run_data)
        try:
            related_prs = required_list(run_data, "pull_requests")
        except KeyError as exc:
            raise GitHubResponseError(
                "Selected run attempt lacks verifiable pull-request association."
            ) from exc
        def matches_pull_request(value: object) -> bool:
            if not isinstance(value, Mapping) or value.get("number") != identity.number:
                return False
            head, base = value.get("head"), value.get("base")
            return (
                isinstance(head, Mapping) and head.get("sha") == identity.head_sha
                and isinstance(base, Mapping) and base.get("sha") == identity.base_sha
            )
        if not any(matches_pull_request(item) for item in related_prs):
            raise GitHubResponseError(
                "Selected run attempt is not associated with the frozen pull request."
            )
        if (run.run_id, run.run_attempt) != (run_id, run_attempt):
            raise GitHubResponseError("Selected CI run/attempt identity does not match.")
        data = self._get_json_object(
            self.api_url(
                f"/repos/{identity.repository}/actions/runs/{run_id}"
                f"/attempts/{run_attempt}/jobs"
            ), resource="selected-workflow-jobs",
            params={"per_page": _RESULTS_PER_PAGE, "page": 1},
        )
        try:
            total = required_nonnegative_int(data, "total_count")
            items = required_list(data, "jobs")
        except KeyError as exc:
            raise GitHubResponseError("Selected job list has missing required fields.") from exc
        if total > _RESULTS_PER_PAGE or len(items) != total:
            raise GitHubResponseError("Selected job list is incomplete or exceeds one-page budget.")
        jobs = []
        for item in items:
            if not isinstance(item, Mapping):
                raise GitHubResponseError("Selected job item is not an object.")
            jobs.append(self._parse_workflow_job(identity, run, item))
        matches = [job for job in jobs if job.job_id == job_id]
        if len(matches) != 1:
            raise GitHubResponseError("Selected job is absent or ambiguous in the exact attempt.")
        job = matches[0]
        if job.status != "completed" or job.conclusion != "failure":
            raise GitHubResponseError("Selected job has no completed failure observation.")
        return run, job

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

        # The run-level /jobs endpoint can return the latest rerun attempt. Bind the
        # request to the attempt captured on this WorkflowRun so run metadata and jobs
        # remain one coherent observation even if another rerun starts later.
        url = self.api_url(
            f"/repos/{identity.repository}/actions/runs/{run.run_id}"
            f"/attempts/{run.run_attempt}/jobs"
        )
        records: list[WorkflowJob] = []
        expected_total: int | None = None
        page = 1

        while expected_total is None or len(records) < expected_total:
            data = self._get_json_object(
                url,
                resource="workflow-job",
                params={
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
