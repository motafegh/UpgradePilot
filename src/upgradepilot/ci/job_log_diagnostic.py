"""Admit a bounded *textual CI log observation*, not runtime applicability or cause.

The provider owns bytes, digest and exact job identity. This CI owner selects only a
well-defined Python unexpected-keyword exception and a dependency-install summary token.
A missing/ambiguous match does not become positive or negative evidence.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Literal

from ..dependency.change import DependencyVersionChange
from ..github.actions import GitHubActionsClient, WorkflowJobLog
from ..github.api import GitHubAcquisitionError, GitHubResponseError
from ..github.pull_request import PullRequestIdentity


@dataclass(frozen=True, slots=True)
class SelectedCIJob:
    run_id: int
    run_attempt: int
    job_id: int

    def __post_init__(self) -> None:
        if any(type(value) is not int or value <= 0 for value in
               (self.run_id, self.run_attempt, self.job_id)):
            raise ValueError("Selected CI run, attempt and job must be positive integers.")


@dataclass(frozen=True, slots=True)
class CIJobLogDiagnostic:
    """A private job-log witness with one minimal selected error substring.

    A SHA-256 digest does not imply the discarded full log is retained or inspectable.
    No state here proves the traceback's loaded module version or upgrade causality.
    """

    repository: str
    head_sha: str
    run_id: int
    run_attempt: int
    job_id: int
    source_url: str
    state: Literal["observed_keyword_error", "unclassified_log", "unavailable"]
    reason: str
    log_bytes: int | None
    log_sha256: str | None
    error_line: int | None
    error_excerpt: str | None
    rejected_keyword: str | None
    compared_callee: str | None
    install_token: str | None
    install_line: int | None


# A regex of only identifier-like names ensures selected retained material is bounded
# and not arbitrary log text. Literal timestamp/prefix and other lines are discarded.
_ERROR_RE = re.compile(
    r"TypeError: (?P<callee>[A-Za-z_][\w.]*)\(\) got an unexpected "
    r"keyword argument '(?P<keyword>[A-Za-z_][\w]*)'"
)


def _base(
    identity: PullRequestIdentity, selection: SelectedCIJob,
) -> dict[str, object]:
    return dict(
        repository=identity.repository, head_sha=identity.head_sha,
        run_id=selection.run_id, run_attempt=selection.run_attempt,
        job_id=selection.job_id,
        source_url=(f"https://api.github.com/repos/{identity.repository}"
                    f"/actions/jobs/{selection.job_id}/logs"),
    )


def interpret_selected_job_log(
    identity: PullRequestIdentity, dependency: DependencyVersionChange,
    selection: SelectedCIJob, evidence: WorkflowJobLog,
) -> CIJobLogDiagnostic:
    """Extract one trustworthy *text* match; never execute a log or source snippet."""
    if (
        (evidence.repository, evidence.head_sha,
         evidence.run_id, evidence.run_attempt, evidence.job_id)
        != (identity.repository, identity.head_sha,
            selection.run_id, selection.run_attempt, selection.job_id)
    ):
        raise ValueError("CI diagnostic log belongs to another exact PR/run/attempt/job.")
    # The same traceback is often repeated in pytest's short summary. Treat
    # identical normalized errors as one observation, not a conflict.
    matches: dict[tuple[str, str, str], int] = {}
    install_token = None
    install_line = None
    expected_token = f"{dependency.normalized_package}-{dependency.proposed_version}"
    for lineno, line in enumerate(evidence.text.splitlines(), 1):
        if "Successfully installed " in line and expected_token in line.split(
            "Successfully installed ", 1
        )[1].split():
            install_token, install_line = expected_token, lineno
        if len(line) > 4096:
            # A line too long to inspect safely is not silently truncated
            # into a positive classification.
            continue
        found = _ERROR_RE.search(line)
        if found is not None:
            key = (found.group(0), found.group("callee"), found.group("keyword"))
            matches.setdefault(key, lineno)
    detail = None
    if len(matches) == 1:
        (error_text, callee, keyword), first_line = next(iter(matches.items()))
        detail = (error_text, callee, keyword, first_line)
    return CIJobLogDiagnostic(
        **_base(identity, selection),
        state="observed_keyword_error" if detail else "unclassified_log",
        reason=("unique_matching_keyword_exception_text"
                if detail else "no_unique_admitted_keyword_exception_text"),
        log_bytes=evidence.utf8_bytes, log_sha256=evidence.sha256,
        error_line=detail[3] if detail else None,
        error_excerpt=detail[0] if detail else None,
        rejected_keyword=detail[2] if detail else None,
        compared_callee=detail[1] if detail else None,
        install_token=install_token, install_line=install_line,
    )


def acquire_selected_ci_diagnostic(
    identity: PullRequestIdentity, dependency: DependencyVersionChange,
    selection: SelectedCIJob, actions: GitHubActionsClient,
) -> CIJobLogDiagnostic:
    """Acquire one selected historical failure or retain its explicit unavailable state."""
    try:
        run, job = actions.get_selected_failed_workflow_job(
            identity, selection.run_id, selection.run_attempt, selection.job_id
        )
        raw = actions.get_failed_workflow_job_log(
            identity, run, job, max_bytes=65536
        )
        return interpret_selected_job_log(identity, dependency, selection, raw)
    except (GitHubAcquisitionError, GitHubResponseError) as error:
        return CIJobLogDiagnostic(
            **_base(identity, selection), state="unavailable",
            reason=getattr(error, "reason", "source_response_unusable"),
            log_bytes=None, log_sha256=None, error_line=None, error_excerpt=None,
            rejected_keyword=None, compared_callee=None,
            install_token=None, install_line=None,
        )


__all__ = [
    "SelectedCIJob", "CIJobLogDiagnostic", "acquire_selected_ci_diagnostic",
    "interpret_selected_job_log",
]
