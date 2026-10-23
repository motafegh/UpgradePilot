"""Acquire one GitHub pull-request identity and its complete changed-file evidence.

This provider module owns PR-specific endpoints, response interpretation, pagination,
completeness checks, and snapshot correspondence for mutable PR-files evidence.
Shared HTTP behavior lives in ``github.api`` and pure GitHub locator syntax lives in
``github.identity``.
"""

from __future__ import annotations

from collections.abc import Callable, Mapping
from dataclasses import dataclass
from datetime import UTC, datetime
from hashlib import sha256
from typing import Any, Literal
from urllib.parse import parse_qs, unquote, urlsplit

from requests import Session

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
# Bounds retained decoded text, not the HTTP response/JSON parser's memory.
MAX_PR_DESCRIPTION_UTF8_BYTES = 262_144
DESCRIPTION_STATES = (
    "retained", "empty", "missing", "null", "invalid_type", "invalid_text", "over_limit"
)
type PullRequestDescriptionState = Literal[
    "retained", "empty", "missing", "null", "invalid_type", "invalid_text", "over_limit"
]


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


@dataclass(frozen=True, slots=True)
class PullRequestDescriptionObservation:
    """Initial PR body observation, without upstream authority or semantic claims.

    Shared preparation carries this once to native capture; report projection later reads
    that canonical record. Validation also protects offline native reconstruction.
    """

    state: PullRequestDescriptionState
    text: str | None
    source_url: str
    observed_at: datetime
    content_sha256: str | None
    utf8_bytes: int | None

    def __post_init__(self) -> None:
        if self.state not in DESCRIPTION_STATES:
            raise ValueError("Unknown PR description state.")
        if (
            type(self.observed_at) is not datetime
            or self.observed_at.utcoffset() is None
            or self.observed_at.utcoffset().total_seconds() != 0
            or type(self.source_url) is not str
            or not self.source_url
        ):
            raise ValueError("Description requires a source locator and UTC observation time.")
        if self.utf8_bytes is not None and (
            type(self.utf8_bytes) is not int or self.utf8_bytes < 0
        ):
            raise ValueError("Invalid description byte count.")
        if self.state in {"retained", "empty"}:
            if type(self.text) is not str or len(self.text) > MAX_PR_DESCRIPTION_UTF8_BYTES:
                raise ValueError("Retained description exceeds the representation bound.")
            encoded = self.text.encode("utf-8", errors="strict")
            if (
                len(encoded) > MAX_PR_DESCRIPTION_UTF8_BYTES
                or self.utf8_bytes != len(encoded)
                or self.content_sha256 != sha256(encoded).hexdigest()
                or (self.state == "empty") != (self.text == "")
            ):
                raise ValueError("Retained description state/count/hash disagree.")
        elif self.text is not None or self.content_sha256 is not None:
            raise ValueError("Unavailable descriptions cannot retain text or a digest.")
        elif self.state == "over_limit":
            if self.utf8_bytes is not None and self.utf8_bytes <= MAX_PR_DESCRIPTION_UTF8_BYTES:
                raise ValueError("Over-limit count must exceed the retention bound.")
        elif self.utf8_bytes is not None:
            raise ValueError("Description byte count was not measured in this state.")


@dataclass(frozen=True, slots=True)
class PullRequestObservation:
    identity: PullRequestIdentity
    description: PullRequestDescriptionObservation


class GitHubPullRequestClient(GitHubApiClient):
    """Read PR identity and complete changed-file evidence without repository writes."""

    def __init__(
        self, *, token: str | None = None, session: Session | None = None,
        timeout: tuple[float, float] = DEFAULT_TIMEOUT,
        now: Callable[[], datetime] | None = None,
    ) -> None:
        super().__init__(token=token, session=session, timeout=timeout)
        self._now = now or (lambda: datetime.now(UTC))

    def _acquire_pull_request(
        self, repository: str, pull_number: int
    ) -> tuple[PullRequestIdentity, Mapping[str, Any], str]:
        repository = validate_repository(repository)
        pull_number = validate_pull_number(pull_number)
        url = self.api_url(f"/repos/{repository}/pulls/{pull_number}")
        data = self._get_json_object(url, resource="pull-request")
        return self._parse_pull_request(repository, pull_number, data), data, url

    def get_pull_request(
        self,
        repository: str,
        pull_number: int,
    ) -> PullRequestIdentity:
        identity, _, _ = self._acquire_pull_request(repository, pull_number)
        return identity

    def get_pull_request_observation(
        self, repository: str, pull_number: int
    ) -> PullRequestObservation:
        """Acquire identity and bounded body from the same initial response, in one GET."""
        identity, data, url = self._acquire_pull_request(repository, pull_number)
        state: PullRequestDescriptionState
        text = None
        digest = None
        size = None
        body = data.get("body")
        if "body" not in data:
            state = "missing"
        elif body is None:
            state = "null"
        elif not isinstance(body, str):
            state = "invalid_type"
        elif len(body) > MAX_PR_DESCRIPTION_UTF8_BYTES:
            # First sufficient refusal: do not encode an already oversized field.
            state = "over_limit"
        else:
            try:
                encoded = body.encode("utf-8", errors="strict")
            except UnicodeEncodeError:
                state = "invalid_text"
            else:
                size = len(encoded)
                if size > MAX_PR_DESCRIPTION_UTF8_BYTES:
                    state = "over_limit"
                else:
                    state = "empty" if body == "" else "retained"
                    text = body
                    digest = sha256(encoded).hexdigest()
        return PullRequestObservation(
            identity,
            PullRequestDescriptionObservation(state, text, url, self._now(), digest, size),
        )

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

        path_parts = decoded_path.split("/", 5)
        locator_repository = (
            f"{path_parts[2]}/{path_parts[3]}" if len(path_parts) == 6 else ""
        )
        locator_filename = path_parts[5] if len(path_parts) == 6 else ""
        api_root = urlsplit(GITHUB_API_ROOT)
        if (
            locator.scheme != api_root.scheme
            or locator.netloc != api_root.netloc
            or len(path_parts) != 6
            or path_parts[0] != ""
            or path_parts[1] != "repos"
            or locator_repository.casefold() != identity.repository.casefold()
            or path_parts[4] != "contents"
            or locator_filename != filename
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
    "PullRequestObservation",
    "PullRequestDescriptionObservation",
    "UpgradePilotInputError",
    "validate_pull_number",
    "validate_repository",
)
