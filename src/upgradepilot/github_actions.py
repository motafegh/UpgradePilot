"""Acquire workflow-run, job, and step evidence for the exact PR head commit.

Purpose of this file
--------------------
After ``github_client.py`` creates a trusted ``PullRequestIdentity``, this module
asks GitHub Actions which pull-request workflow runs belong to that exact
``identity.head_sha`` and which jobs belong to each run.

The output is factual execution evidence:

* ``WorkflowRun`` says which workflow execution GitHub recorded;
* ``WorkflowJob`` says which jobs GitHub recorded for that run;
* ``WorkflowStep`` preserves the bounded step summaries included in a job response.

How this file relates to the rest of UpgradePilot
-------------------------------------------------
``GitHubActionsClient`` inherits HTTP, status, and top-level JSON handling from
``GitHubApiClient`` in ``github_api.py``. It receives ``PullRequestIdentity`` from
``github_client.py`` and adds Actions-specific pagination and identity checks.

The records produced here are not enough to prove that the changed dependency was
installed and exercised. Step names are summaries, not the workflow's actual
``run:`` commands. ``github_repository.py`` therefore fetches the workflow file used
by each run, ``workflow_commands.py`` reads the supported commands, and
``ci_authority.py`` combines all three evidence sources.

Typical execution flow
----------------------
1. ``cli.py`` passes a frozen ``PullRequestIdentity`` to
   ``get_exact_head_workflow_runs``.
2. The client requests pull-request runs filtered by ``head_sha`` and validates every
   returned run locally.
3. For each validated run, ``cli.py`` calls ``get_workflow_jobs``.
4. Every job is reconciled with both its parent run ID and the frozen PR head SHA.
5. Complete immutable tuples are returned for later workflow-file acquisition and
   CI-authority interpretation.

This file acquires execution metadata. It does not interpret commands, claim test
coverage, or decide upgrade safety.
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

# GitHub supports 100 results per page for these endpoints. Requesting the maximum
# reduces HTTP calls, but completeness is still established by ``total_count``.
_RESULTS_PER_PAGE = 100

# GitHub bounds filtered workflow-run searches at 1,000 results. UpgradePilot also
# refuses a larger declared set rather than pretending a truncated response is whole.
_MAX_WORKFLOW_RUNS = 1_000

# Jobs form a separate paginated collection, so they receive their own explicit
# complete-acquisition boundary.
_MAX_JOBS_PER_RUN = 1_000


@dataclass(frozen=True, slots=True)
class WorkflowRun:
    """Validated identity and state of one GitHub Actions workflow execution.

    The important identifiers are different:

    * ``workflow_id`` identifies the reusable workflow definition;
    * ``run_id`` identifies one execution of that workflow;
    * ``run_attempt`` distinguishes reruns of that execution.

    ``head_sha`` binds the execution to the exact proposal revision from
    ``PullRequestIdentity``. ``status`` describes lifecycle state such as queued or
    completed, while ``conclusion`` may be ``None`` until GitHub has a final result.

    ``github_repository.py`` later uses both ``run_id`` and ``workflow_id`` to resolve
    the workflow path used by this execution. The frozen dataclass prevents those
    identifiers from changing between acquisition stages.
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
    """One validated step summary reported inside a workflow job.

    A step summary contains its number, display name, status, and conclusion. It does
    not contain the complete workflow command definition. For example, a step named
    ``Test with tox`` does not by itself reveal whether the changed dependency was
    installed or invoked. That proof must come from exact-revision workflow text.
    """

    number: int
    name: str
    status: str
    conclusion: str | None


@dataclass(frozen=True, slots=True)
class WorkflowJob:
    """Validated job belonging to one workflow run and the frozen PR head.

    ``run_id`` links the job to its parent ``WorkflowRun``. ``head_sha`` independently
    reconnects it to the proposal revision, preventing a job from another commit from
    being attached to this evidence chain.

    ``steps`` deliberately has three meaningful states:

    * ``None``: GitHub omitted the steps field or returned JSON null;
    * ``()``: GitHub explicitly supplied an empty step array;
    * a non-empty tuple: validated step summaries were supplied.

    Preserving these states avoids turning unavailable evidence into a false claim
    that the job had no steps.
    """

    job_id: int
    run_id: int
    name: str
    head_sha: str
    status: str
    conclusion: str | None
    steps: tuple[WorkflowStep, ...] | None


class GitHubActionsClient(GitHubApiClient):
    """Read exact-head GitHub Actions evidence using the shared API foundation.

    The inherited class handles GET requests, authentication, timeouts, HTTP errors,
    JSON decoding, and top-level object checks. This subclass understands Actions
    response fields, total-count pagination, run/job identity, and domain records.
    """

    def get_exact_head_workflow_runs(
        self,
        identity: PullRequestIdentity,
    ) -> tuple[WorkflowRun, ...]:
        """Acquire every PR-triggered workflow run for ``identity.head_sha``.

        Goal:
            Produce the complete set of workflow executions GitHub associates with
            the exact proposal revision—not merely with a mutable branch name.

        GitHub receives ``event=pull_request`` and ``head_sha=...`` query filters.
        These filters reduce irrelevant results, but they are not trusted as proof.
        ``_parse_workflow_run`` checks the event and SHA again for every returned item.

        Pagination uses the first page's ``total_count`` as a frozen target. Every
        later page must repeat the same total, and the final number of validated
        records must equal it exactly.
        """

        url = self.api_url(f"/repos/{identity.repository}/actions/runs")
        records: list[WorkflowRun] = []

        # Before page one, no total has been observed. ``None`` represents that state
        # and remains distinct from the valid GitHub result ``total_count == 0``.
        expected_total: int | None = None
        page = 1

        # The first iteration discovers the total. Later iterations continue only
        # while fewer validated records exist than GitHub originally declared.
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
                # ``total_count`` is a count, so zero is valid. ``workflow_runs`` must
                # be a list, but each item remains untrusted until parsed below.
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
                # Freeze page one's declaration. It becomes the reference against
                # which all later pages and the final collection are reconciled.
                expected_total = total_count
            elif total_count != expected_total:
                # A total that changes mid-pagination means the pages no longer form
                # one internally consistent snapshot, so the client abstains.
                raise GitHubResponseError(
                    "GitHub workflow-run total changed during pagination: "
                    f"expected {expected_total} but later observed {total_count}."
                )

            for item_index, item in enumerate(items):
                if not isinstance(item, Mapping):
                    # Convert page-local zero-based position to a global one-based
                    # position for a useful error message.
                    raise GitHubResponseError(
                        "GitHub workflow-run response item "
                        f"{len(records) + item_index + 1} was not an object."
                    )
                records.append(self._parse_workflow_run(identity, item))

            # More records than the declared total is a contradiction immediately;
            # under-acquisition is checked after the loop.
            if len(records) > expected_total:
                raise GitHubResponseError(
                    "GitHub returned more workflow runs than its total_count declared."
                )

            # A short page is a pagination stopping signal, not the final proof. The
            # exact equality check below still decides whether acquisition was whole.
            if len(items) < _RESULTS_PER_PAGE:
                break
            page += 1

        if expected_total is None or len(records) != expected_total:
            raise GitHubResponseError(
                "GitHub workflow-run pagination was incomplete: "
                f"expected {expected_total or 0} runs but acquired {len(records)}."
            )

        # Freeze the complete evidence set before ``cli.py`` begins job acquisition.
        return tuple(records)

    def get_workflow_jobs(
        self,
        identity: PullRequestIdentity,
        run: WorkflowRun,
    ) -> tuple[WorkflowJob, ...]:
        """Acquire every latest-attempt job belonging to one validated run.

        Goal:
            Build a complete job collection whose parent run ID and head SHA are
            consistent with the supplied ``WorkflowRun`` and ``PullRequestIdentity``.

        GitHub workflows can be rerun. ``filter="latest"`` asks for jobs from the
        latest attempt instead of mixing earlier and later attempts in one collection.
        The returned items are still locally validated.
        """

        # Validate the relationship between caller-supplied records before spending a
        # network request. A run from another commit cannot belong to this PR identity.
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

        # This loop mirrors run pagination because jobs are another independently
        # counted collection with the same completeness risks.
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
                # The parser rechecks both the parent run ID and exact PR head SHA.
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
        """Validate one raw run object against the frozen PR identity.

        Goal:
            Convert untrusted run JSON into a record that is proven to be a
            pull-request-triggered execution for ``identity.head_sha``.

        ``@staticmethod`` is appropriate because the parser needs only its explicit
        inputs and shared validators; it does not use the client's session or token.
        """

        try:
            # Validate relationship fields first. Other run metadata matters only if
            # this record actually belongs to the requested PR evidence boundary.
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
                # The key is required, but GitHub may use null before completion.
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
        """Validate one raw job object and its optional step collection.

        Goal:
            Prove that the job belongs to the requested parent run and exact PR head,
            then convert any supplied step summaries into immutable records.
        """

        try:
            run_id = required_positive_int(data, "run_id")
            head_sha = required_str(data, "head_sha")

            # Check both relationships. Matching only the head SHA would not prove the
            # job belongs to this particular workflow execution.
            if run_id != run.run_id:
                raise GitHubResponseError(
                    "Workflow job run ID does not match the requested workflow run."
                )
            if head_sha != identity.head_sha:
                raise GitHubResponseError(
                    "Workflow job head SHA does not match the frozen pull-request head."
                )

            # ``get`` is intentional because steps may be absent or null in an
            # otherwise valid job response. Required fields below use ``data[key]``.
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
                    # The class-qualified call emphasizes that the helper is stateless
                    # and does not depend on the current client instance.
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
        """Validate one raw step summary and build ``WorkflowStep``.

        The job parser owns whether ``steps`` is absent, an array, or malformed. This
        helper owns only the required field contract for one array item. Separating
        those responsibilities keeps collection validation and item validation clear.
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
