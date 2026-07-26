"""Acquire exact-head GitHub Actions workflow, job, and step evidence.

The module answers one bounded factual question: which pull-request-triggered
GitHub Actions runs and jobs belong to the exact PR head SHA already frozen by
``PullRequestIdentity``?

It does not decide whether the changed dependency was installed, exercised, or
safe. Those are later CI-authority interpretations. Here, every successful
response is still untrusted until its count, shape, event, run identity, and head
SHA have been validated.

The client intentionally validates GitHub's server-side filtering again locally.
A query parameter narrows what the API should return; it is not evidence that each
returned record actually matches the requested proposal revision.
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any

from .github_api import (
    GitHubApiClient,
    GitHubResponseError,
    optional_str,
    required_list,
    required_nonnegative_int,
    required_positive_int,
    required_str,
)
from .github_client import PullRequestIdentity

# Use GitHub's largest supported page size to minimize requests while preserving
# explicit total-count reconciliation as the real completeness proof.
_RESULTS_PER_PAGE = 100
# GitHub bounds filtered workflow-run searches at 1,000 results. UpgradePilot
# also refuses larger evidence sets rather than silently truncating them.
_MAX_WORKFLOW_RUNS = 1_000
# Jobs receive a separate bound because they are a different evidence collection
# with their own pagination and completeness invariant.
_MAX_JOBS_PER_RUN = 1_000


@dataclass(frozen=True, slots=True)
class WorkflowRun:
    """One validated pull-request workflow run bound to an exact head SHA.

    ``run_id`` identifies this concrete execution, while ``workflow_id`` identifies
    the workflow definition across executions. ``run_attempt`` distinguishes reruns
    of the same execution. Freezing the record prevents later evidence stages from
    accidentally changing that identity.
    """

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
    """One bounded step summary reported for a GitHub Actions job.

    These fields describe GitHub's step state and name; they are not the workflow
    command text and therefore cannot by themselves prove dependency exercise.
    """

    number: int
    name: str
    status: str
    conclusion: str | None


@dataclass(frozen=True, slots=True)
class WorkflowJob:
    """One validated job for a specific workflow run and exact PR head SHA.

    ``steps=None`` means GitHub omitted step evidence, whereas ``steps=()`` means
    it supplied an explicit empty list. Preserving that distinction prevents
    unavailable evidence from being mistaken for evidence that no steps existed.
    """

    job_id: int
    run_id: int
    name: str
    head_sha: str
    status: str
    conclusion: str | None
    steps: tuple[WorkflowStep, ...] | None


class GitHubActionsClient(GitHubApiClient):
    """Acquire read-only GitHub Actions evidence for the current B2 slice.

    Inheritance reuses the shared HTTP/JSON trust boundary; this subclass adds
    Actions-specific pagination, identity, and record validation.
    """

    def get_exact_head_workflow_runs(
        self,
        identity: PullRequestIdentity,
    ) -> tuple[WorkflowRun, ...]:
        """Return all ``pull_request`` runs associated with ``identity.head_sha``.

        The GitHub query narrows the response, but local checks still enforce the
        event and SHA. A server-side filter is an acquisition aid, not proof that
        every returned item has the requested identity.

        Records are accumulated in a mutable list during pagination and exposed as
        an immutable tuple only after the declared total has been reconciled.
        """

        url = self.api_url(f"/repos/{identity.repository}/actions/runs")
        records: list[WorkflowRun] = []
        # The total is unknown until GitHub returns page one. ``None`` represents
        # "not observed yet" and is distinct from a valid total of zero.
        expected_total: int | None = None
        # GitHub's REST pagination is one-based.
        page = 1

        # The first iteration is required to discover ``total_count``. Later
        # iterations continue only while the validated collection is incomplete.
        while expected_total is None or len(records) < expected_total:
            data = self._get_json_object(
                url,
                resource="workflow-run",
                params={
                    # Both filters reduce irrelevant traffic; each returned record
                    # is nevertheless checked again by ``_parse_workflow_run``.
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
                # Freeze the first page's declaration as the independent target
                # against which every later page is reconciled.
                expected_total = total_count
            elif total_count != expected_total:
                # A changing total makes the multi-page snapshot internally
                # inconsistent, so the client refuses to construct evidence.
                raise GitHubResponseError(
                    "GitHub workflow-run total changed during pagination: "
                    f"expected {expected_total} but later observed {total_count}."
                )

            for item_index, item in enumerate(items):
                if not isinstance(item, Mapping):
                    # Combine the page-local index with records already acquired to
                    # report a stable one-based position across the full result set.
                    raise GitHubResponseError(
                        "GitHub workflow-run response item "
                        f"{len(records) + item_index + 1} was not an object."
                    )
                records.append(self._parse_workflow_run(identity, item))

            # Over-acquisition is checked separately from final under-acquisition;
            # both contradict GitHub's declared total in different ways.
            if len(records) > expected_total:
                raise GitHubResponseError(
                    "GitHub returned more workflow runs than its total_count declared."
                )
            # A short page is the normal pagination stop signal, but it is not the
            # final completeness proof; the equality check below remains decisive.
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
        """Acquire the latest-attempt jobs for one validated workflow run.

        GitHub can rerun a workflow. ``filter='latest'`` avoids combining jobs from
        older attempts with the current run evidence while the pagination checks
        still guarantee that every job in the selected attempt was acquired.
        """

        # Reject an inconsistent caller-supplied pair before issuing a request.
        # A run from another commit must never be attached to this PR identity.
        if run.head_sha != identity.head_sha:
            raise GitHubResponseError(
                "Cannot acquire jobs for a workflow run bound to a different head SHA."
            )

        url = self.api_url(
            f"/repos/{identity.repository}/actions/runs/{run.run_id}/jobs"
        )
        records: list[WorkflowJob] = []
        # As with workflow runs, ``None`` means the first page has not yet supplied
        # the authoritative total; zero is a valid observed count.
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
                # Both the parent run ID and frozen head SHA are revalidated while
                # converting the raw item into a trusted job record.
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
        """Validate one workflow-run object against the frozen PR identity.

        ``@staticmethod`` is used because parsing depends only on explicit inputs,
        not on authentication, HTTP state, or mutable client attributes.
        """

        try:
            # Read the identity fields first because every remaining field is only
            # meaningful after the record is proven to belong to this PR revision.
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
                # GitHub may return null while a run is queued or in progress, so
                # conclusion is required-but-nullable rather than always text.
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
        """Validate one workflow job and its optional step summaries.

        The parser reconciles the job against both its immediate parent run and
        the wider frozen PR identity before accepting any step summaries.
        """

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

            # ``get`` is intentional: GitHub may omit ``steps`` from an otherwise
            # valid job response. Absence is therefore different from a malformed
            # required field and must remain visible as ``None``.
            raw_steps = data.get("steps")
            if raw_steps is None:
                steps = None
            elif isinstance(raw_steps, list):
                # Build mutably while validating every external item, then freeze
                # the completed collection into a tuple for downstream consumers.
                parsed_steps: list[WorkflowStep] = []
                for step_index, step in enumerate(raw_steps):
                    if not isinstance(step, Mapping):
                        raise GitHubResponseError(
                            "GitHub workflow-job step "
                            f"{step_index + 1} was not an object."
                        )
                    # The class-qualified call makes it explicit that this parser
                    # is a stateless helper, not polymorphic instance behavior.
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
        """Convert one untrusted step summary into an immutable record.

        Step parsing remains separate so the job parser owns collection shape while
        this function owns the field-level contract for one item.
        """

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
