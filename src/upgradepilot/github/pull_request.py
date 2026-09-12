"""Acquire one GitHub pull-request identity and its complete changed-file evidence.

This provider module owns PR-specific endpoints, response interpretation, pagination,
completeness checks, and snapshot correspondence for mutable PR-files evidence.
Shared HTTP behavior lives in ``github.api`` and pure GitHub locator syntax lives in
``github.identity``.
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any
from urllib.parse import parse_qs, unquote, urlsplit

from .api import (
    DEFAULT_TIMEOUT,
    GITHUB_API_ROOT,
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
        """Acquire changed files only when they remain coherent with ``identity``.

        GitHub's PR-files endpoint is mutable because it is addressed by pull-request
        number rather than immutable commit IDs. Each returned ``contents_url`` must
        therefore identify the frozen PR head and exact returned path, and a final PR
        identity read must show that base/head/count stayed unchanged around acquisition.
        """

        if identity.changed_files > _MAX_CHANGED_FILES:
            raise GitHubResponseError(
                "The pull request exceeds the current complete changed-file "
                f"acquisition limit of {_MAX_CHANGED_FILES} files."
            )

        records: list[ChangedFile] = []
        if identity.changed_files > 0:
            url = self.api_url(
                f"/repos/{identity.repository}/pulls/{identity.number}/files"
            )
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
                    records.append(self._parse_changed_file(identity, item))

                if len(items) < _CHANGED_FILES_PER_PAGE:
                    break
                page += 1

        if len(records) != identity.changed_files:
            raise GitHubResponseError(
                "GitHub pull-request metadata and changed-file acquisition disagree: "
                f"expected {identity.changed_files} records but acquired {len(records)}."
            )

        self._validate_post_acquisition_identity(identity)
        return tuple(records)

    def _validate_post_acquisition_identity(
        self,
        identity: PullRequestIdentity,
    ) -> None:
        """Reject observable PR snapshot drift around changed-file acquisition."""

        current = self.get_pull_request(identity.repository, identity.number)
        if (
            current.base_sha != identity.base_sha
            or current.head_sha != identity.head_sha
            or current.changed_files != identity.changed_files
        ):
            raise GitHubResponseError(
                "GitHub pull-request identity changed while acquiring changed-file "
                "evidence; the frozen base/head/count snapshot cannot be trusted."
            )

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
    def _parse_changed_file(
        identity: PullRequestIdentity,
        data: Mapping[str, Any],
    ) -> ChangedFile:
        try:
            filename = required_str(data, "filename")
            GitHubPullRequestClient._validate_changed_file_head_locator(
                identity,
                filename,
                required_str(data, "contents_url"),
            )
            patch = data.get("patch")
            if patch is not None and not isinstance(patch, str):
                raise GitHubResponseError(
                    "GitHub field 'patch' must be text or absent."
                )
            return ChangedFile(
                filename=filename,
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

    @staticmethod
    def _validate_changed_file_head_locator(
        identity: PullRequestIdentity,
        filename: str,
        contents_url: str,
    ) -> None:
        """Require GitHub's per-file locator to name the frozen head file exactly."""

        try:
            locator = urlsplit(contents_url)
            query = parse_qs(
                locator.query,
                keep_blank_values=True,
                strict_parsing=True,
            )
            decoded_path = unquote(locator.path, errors="strict")
        except (UnicodeDecodeError, ValueError) as exc:
            raise GitHubResponseError(
                "GitHub changed-file contents_url was not a valid supported locator."
            ) from exc

        api_root = urlsplit(GITHUB_API_ROOT)
        expected_path = f"/repos/{identity.repository}/contents/{filename}"
        if (
            locator.scheme != api_root.scheme
            or locator.netloc != api_root.netloc
            or decoded_path != expected_path
            or locator.fragment
            or query != {"ref": [identity.head_sha]}
        ):
            raise GitHubResponseError(
                "GitHub changed-file contents_url does not identify the frozen "
                "pull-request head file."
            )


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
