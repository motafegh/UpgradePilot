"""Acquire one GitHub pull-request identity and its complete changed-file evidence.

This provider module owns PR-specific endpoints, response interpretation, pagination,
and completeness checks. Shared HTTP behavior lives in ``github.api`` and pure GitHub
locator syntax lives in ``github.identity``.
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any

from .api import (
    DEFAULT_TIMEOUT,
    GitHubAcquisitionError,
    GitHubApiClient,
    GitHubResponseError,
    required_bool,
    required_int,
    required_mapping,
    required_nonnegative_int,
    required_str,
)
from .identity import UpgradePilotInputError, validate_pull_number, validate_repository

_CHANGED_FILES_PER_PAGE = 100
_MAX_CHANGED_FILES = 3_000


@dataclass(frozen=True, slots=True)
class PullRequestIdentity:
    """Trusted PR identity plus immutable base/head revision boundaries."""

    repository: str
    number: int
    title: str
    state: str
    merged: bool
    author: str
    base_ref: str
    base_sha: str
    head_ref: str
    head_sha: str
    changed_files: int


@dataclass(frozen=True, slots=True)
class ChangedFile:
    """Validated GitHub metadata and optional patch text for one changed file."""

    filename: str
    status: str
    additions: int
    deletions: int
    changes: int
    patch: str | None


class GitHubPullRequestClient(GitHubApiClient):
    """Read PR identity and complete changed-file evidence without repository writes."""

    def get_pull_request(
        self,
        repository: str,
        pull_number: int,
    ) -> PullRequestIdentity:
        repository = validate_repository(repository)
        pull_number = validate_pull_number(pull_number)
        data = self._get_json_object(
            self.api_url(f"/repos/{repository}/pulls/{pull_number}"),
            resource="pull-request",
        )
        return self._parse_pull_request(repository, pull_number, data)

    def get_changed_files(
        self,
        identity: PullRequestIdentity,
    ) -> tuple[ChangedFile, ...]:
        if identity.changed_files > _MAX_CHANGED_FILES:
            raise GitHubResponseError(
                "The pull request exceeds the current complete changed-file "
                f"acquisition limit of {_MAX_CHANGED_FILES} files."
            )
        if identity.changed_files == 0:
            return ()

        url = self.api_url(
            f"/repos/{identity.repository}/pulls/{identity.number}/files"
        )
        records: list[ChangedFile] = []
        page = 1

        while len(records) < identity.changed_files:
            items = self._get_json_array(
                url,
                resource="changed-file",
                params={"per_page": _CHANGED_FILES_PER_PAGE, "page": page},
            )
            if not items:
                break

            for item_index, item in enumerate(items):
                if not isinstance(item, Mapping):
                    raise GitHubResponseError(
                        "GitHub changed-file response item "
                        f"{len(records) + item_index + 1} was not an object."
                    )
                records.append(self._parse_changed_file(item))

            if len(items) < _CHANGED_FILES_PER_PAGE:
                break
            page += 1

        if len(records) != identity.changed_files:
            raise GitHubResponseError(
                "GitHub pull-request metadata and changed-file acquisition disagree: "
                f"expected {identity.changed_files} records but acquired {len(records)}."
            )
        return tuple(records)

    @staticmethod
    def _parse_pull_request(
        repository: str,
        pull_number: int,
        data: Mapping[str, Any],
    ) -> PullRequestIdentity:
        try:
            base = required_mapping(data, "base")
            head = required_mapping(data, "head")
            user = required_mapping(data, "user")
            number = required_int(data, "number")
            if number != pull_number:
                raise GitHubResponseError(
                    "GitHub returned a different pull-request number than requested."
                )
            return PullRequestIdentity(
                repository=repository,
                number=number,
                title=required_str(data, "title"),
                state=required_str(data, "state"),
                merged=required_bool(data, "merged"),
                author=required_str(user, "login"),
                base_ref=required_str(base, "ref"),
                base_sha=required_str(base, "sha"),
                head_ref=required_str(head, "ref"),
                head_sha=required_str(head, "sha"),
                changed_files=required_nonnegative_int(data, "changed_files"),
            )
        except KeyError as exc:
            raise GitHubResponseError(
                f"GitHub response is missing required field: {exc.args[0]}."
            ) from exc

    @staticmethod
    def _parse_changed_file(data: Mapping[str, Any]) -> ChangedFile:
        try:
            patch = data.get("patch")
            if patch is not None and not isinstance(patch, str):
                raise GitHubResponseError(
                    "GitHub field 'patch' must be text or absent."
                )
            return ChangedFile(
                filename=required_str(data, "filename"),
                status=required_str(data, "status"),
                additions=required_nonnegative_int(data, "additions"),
                deletions=required_nonnegative_int(data, "deletions"),
                changes=required_nonnegative_int(data, "changes"),
                patch=patch,
            )
        except KeyError as exc:
            raise GitHubResponseError(
                "GitHub changed-file response is missing required field: "
                f"{exc.args[0]}."
            ) from exc


# Historical internal name retained only through the migration period.
GitHubReadClient = GitHubPullRequestClient
_DEFAULT_TIMEOUT = DEFAULT_TIMEOUT

__all__ = (
    "ChangedFile",
    "GitHubAcquisitionError",
    "GitHubPullRequestClient",
    "GitHubReadClient",
    "GitHubResponseError",
    "PullRequestIdentity",
    "UpgradePilotInputError",
    "validate_pull_number",
    "validate_repository",
)
