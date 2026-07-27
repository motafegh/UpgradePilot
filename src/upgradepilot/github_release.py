"""Acquire a published GitHub Release and its exact tag reference."""

from __future__ import annotations

from collections.abc import Callable, Mapping
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Literal
from urllib.parse import quote

from requests import Session

from .github_api import (
    DEFAULT_TIMEOUT,
    GitHubAcquisitionError,
    GitHubApiClient,
    GitHubResponseError,
    required_bool,
    required_mapping,
    required_positive_int,
    required_str,
)
from .github_client import validate_repository


type GitHubReleaseProblemState = Literal[
    "source_unavailable",
    "identity_mismatch",
    "malformed_response",
    "acquisition_failed",
]


@dataclass(frozen=True, slots=True)
class GitHubReleaseEvidence:
    """One published release bound to an exact Git tag reference."""

    state: Literal["available"] = field(init=False, default="available")
    repository: str
    requested_tag: str
    release_id: int
    release_url: str
    release_name: str | None
    body: str | None
    prerelease: bool
    published_at: str
    tag_ref: str
    tag_object_type: str
    tag_object_sha: str
    retrieved_at: datetime


@dataclass(frozen=True, slots=True)
class GitHubReleaseProblem:
    """A bounded reason why an exact published GitHub release was not established."""

    state: GitHubReleaseProblemState
    repository: str
    requested_tag: str
    detail: str
    status_code: int | None = None


type GitHubReleaseResult = GitHubReleaseEvidence | GitHubReleaseProblem


class GitHubReleaseClient(GitHubApiClient):
    """Read published release and tag-ref evidence for a public GitHub repository."""

    def __init__(
        self,
        *,
        token: str | None = None,
        session: Session | None = None,
        timeout: tuple[float, float] = DEFAULT_TIMEOUT,
        now: Callable[[], datetime] | None = None,
        max_release_body_chars: int = 200_000,
    ) -> None:
        if max_release_body_chars < 1:
            raise ValueError("max_release_body_chars must be positive.")
        super().__init__(token=token, session=session, timeout=timeout)
        self._now = now or (lambda: datetime.now(timezone.utc))
        self._max_release_body_chars = max_release_body_chars

    def get_release(self, repository: str, tag: str) -> GitHubReleaseResult:
        repository = validate_repository(repository)
        tag = _nonempty_text(tag, "tag")

        release_url = self.api_url(
            f"/repos/{repository}/releases/tags/{quote(tag, safe='')}"
        )
        try:
            release_data = self._get_json_object(
                release_url,
                resource="release-by-tag",
            )
        except GitHubAcquisitionError as exc:
            state: GitHubReleaseProblemState = (
                "source_unavailable"
                if exc.reason == "not_found_or_inaccessible"
                else "acquisition_failed"
            )
            return GitHubReleaseProblem(
                state=state,
                repository=repository,
                requested_tag=tag,
                detail=str(exc),
                status_code=exc.status_code,
            )
        except GitHubResponseError as exc:
            return GitHubReleaseProblem(
                state="malformed_response",
                repository=repository,
                requested_tag=tag,
                detail=str(exc),
            )

        try:
            release = _parse_release(
                release_data,
                tag,
                max_body_chars=self._max_release_body_chars,
            )
        except KeyError as exc:
            return GitHubReleaseProblem(
                state="malformed_response",
                repository=repository,
                requested_tag=tag,
                detail=f"GitHub release response is missing required field: {exc.args[0]}.",
                status_code=200,
            )
        except GitHubResponseError as exc:
            return GitHubReleaseProblem(
                state="malformed_response",
                repository=repository,
                requested_tag=tag,
                detail=str(exc),
                status_code=200,
            )
        except _IdentityMismatch as exc:
            return GitHubReleaseProblem(
                state="identity_mismatch",
                repository=repository,
                requested_tag=tag,
                detail=str(exc),
                status_code=200,
            )

        ref_url = self.api_url(
            f"/repos/{repository}/git/ref/tags/{quote(tag, safe='')}"
        )
        try:
            ref_data = self._get_json_object(ref_url, resource="tag-reference")
        except GitHubAcquisitionError as exc:
            state = (
                "identity_mismatch"
                if exc.reason == "not_found_or_inaccessible"
                else "acquisition_failed"
            )
            return GitHubReleaseProblem(
                state=state,
                repository=repository,
                requested_tag=tag,
                detail=(
                    "The published release exists, but its exact tag reference was not established."
                    if state == "identity_mismatch"
                    else str(exc)
                ),
                status_code=exc.status_code,
            )
        except GitHubResponseError as exc:
            return GitHubReleaseProblem(
                state="malformed_response",
                repository=repository,
                requested_tag=tag,
                detail=str(exc),
            )

        try:
            tag_ref, object_type, object_sha = _parse_tag_ref(ref_data, tag)
        except KeyError as exc:
            return GitHubReleaseProblem(
                state="malformed_response",
                repository=repository,
                requested_tag=tag,
                detail=(
                    "GitHub tag-reference response is missing required field: "
                    f"{exc.args[0]}."
                ),
                status_code=200,
            )
        except GitHubResponseError as exc:
            return GitHubReleaseProblem(
                state="malformed_response",
                repository=repository,
                requested_tag=tag,
                detail=str(exc),
                status_code=200,
            )
        except _IdentityMismatch as exc:
            return GitHubReleaseProblem(
                state="identity_mismatch",
                repository=repository,
                requested_tag=tag,
                detail=str(exc),
                status_code=200,
            )

        return GitHubReleaseEvidence(
            repository=repository,
            requested_tag=tag,
            release_id=release["release_id"],
            release_url=release["release_url"],
            release_name=release["release_name"],
            body=release["body"],
            prerelease=release["prerelease"],
            published_at=release["published_at"],
            tag_ref=tag_ref,
            tag_object_type=object_type,
            tag_object_sha=object_sha,
            retrieved_at=self._now(),
        )


class _IdentityMismatch(ValueError):
    pass


def _parse_release(
    data: Mapping[str, Any],
    tag: str,
    *,
    max_body_chars: int,
) -> dict[str, Any]:
    returned_tag = required_str(data, "tag_name")
    if returned_tag != tag:
        raise _IdentityMismatch(
            f"GitHub returned release tag {returned_tag!r} instead of {tag!r}."
        )
    if required_bool(data, "draft"):
        raise _IdentityMismatch("GitHub returned a draft instead of a published release.")

    release_name = _optional_text(data, "name")
    body = _optional_text(data, "body")
    if body is not None and len(body) > max_body_chars:
        raise GitHubResponseError(
            "GitHub release body exceeded the configured character limit."
        )
    return {
        "release_id": required_positive_int(data, "id"),
        "release_url": required_str(data, "html_url"),
        "release_name": release_name,
        "body": body,
        "prerelease": required_bool(data, "prerelease"),
        "published_at": required_str(data, "published_at"),
    }


def _optional_text(data: Mapping[str, Any], key: str) -> str | None:
    value = data[key]
    if value is not None and not isinstance(value, str):
        raise GitHubResponseError(
            f"GitHub release field {key!r} must be text or null."
        )
    return value


def _parse_tag_ref(data: Mapping[str, Any], tag: str) -> tuple[str, str, str]:
    expected_ref = f"refs/tags/{tag}"
    returned_ref = required_str(data, "ref")
    if returned_ref != expected_ref:
        raise _IdentityMismatch(
            f"GitHub returned tag reference {returned_ref!r} instead of {expected_ref!r}."
        )
    target = required_mapping(data, "object")
    object_type = required_str(target, "type")
    if object_type not in {"commit", "tag"}:
        raise _IdentityMismatch(
            f"GitHub tag reference points to unsupported object type {object_type!r}."
        )
    return returned_ref, object_type, required_str(target, "sha")


def _nonempty_text(value: str, name: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{name} must be a non-empty string.")
    return value.strip()
