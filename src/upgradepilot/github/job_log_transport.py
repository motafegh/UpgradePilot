"""Bounded GitHub Actions job-log download without cross-origin credential forwarding.

The Actions API returns a short-lived location, not JSON. The selected job identity
belongs to the caller; this module owns only a tightly limited two-hop text transfer.
The signed redirect URI and returned text must never appear in exception messages.
"""

from __future__ import annotations

from urllib.parse import urlsplit

from requests import Session
from requests.exceptions import RequestException, Timeout

from .api import GitHubAcquisitionError, GitHubApiClient, GitHubResponseError

MAX_JOB_LOG_BYTES = 256 * 1024
_CHUNK_BYTES = 8192
_MAX_REDIRECT_CHARS = 8192


def _admitted_actions_log_location(value: str | None) -> bool:
    if not value or len(value) > _MAX_REDIRECT_CHARS:
        return False
    try:
        parsed = urlsplit(value)
        host = parsed.hostname
        port = parsed.port
    except ValueError:
        return False
    return (
        parsed.scheme == "https"
        and port in (None, 443)
        and parsed.username is None
        and parsed.password is None
        and parsed.fragment == ""
        and host is not None
        and (
            host.endswith(".blob.core.windows.net")
            or host == "pipelines.actions.githubusercontent.com"
        )
    )


def download_bounded_job_log(
    session: Session,
    *,
    api_url: str,
    github_headers: dict[str, str],
    timeout: tuple[float, float],
    max_bytes: int = MAX_JOB_LOG_BYTES,
) -> bytes:
    """Read one GitHub job log with a hard decoded-byte cap and no retries.

    Only the GitHub API request receives the optional bearer token. A redirect is
    manually validated and followed with a new header set; no token, netrc auth,
    or original signed URL is retained in the returned result or error messages.
    """

    if not 0 < max_bytes <= MAX_JOB_LOG_BYTES:
        raise ValueError("job-log decoded-byte limit is outside the supported range")

    def fetch(url: str, headers: dict[str, str]):
        try:
            return session.get(
                url, headers=headers, timeout=timeout,
                allow_redirects=False, stream=True,
            )
        except Timeout:
            raise GitHubAcquisitionError(
                "GitHub job-log acquisition timed out.", reason="timeout"
            ) from None
        except RequestException:
            raise GitHubAcquisitionError(
                "GitHub job-log acquisition failed before a usable response.",
                reason="transport_error",
            ) from None

    response = fetch(api_url, github_headers)
    try:
        if response.status_code == 302:
            location = response.headers.get("Location")
            if not _admitted_actions_log_location(location):
                raise GitHubResponseError(
                    "GitHub job-log redirect destination is not admitted."
                )
        else:
            GitHubApiClient._raise_for_status(response, resource="job-log")
            location = None
            if response.status_code != 200:
                raise GitHubResponseError("GitHub job-log response status is unsupported.")
        if location is not None:
            response.close()
            response = fetch(
                location,
                {"User-Agent": github_headers["User-Agent"], "Accept": "text/plain"},
            )
            if response.status_code != 200:
                GitHubApiClient._raise_for_status(response, resource="job-log-content")
                raise GitHubResponseError(
                    "The GitHub job-log storage response did not contain a supported body."
                )

        declared = response.headers.get("Content-Length")
        if declared and declared.isdecimal() and int(declared) > max_bytes:
            raise GitHubAcquisitionError(
                "GitHub job log exceeds the bounded download size.",
                reason="response_too_large",
            )
        result = bytearray()
        try:
            for chunk in response.iter_content(chunk_size=_CHUNK_BYTES):
                if chunk:
                    if len(result) + len(chunk) > max_bytes:
                        raise GitHubAcquisitionError(
                            "GitHub job log exceeds the bounded download size.",
                            reason="response_too_large",
                        )
                    result.extend(chunk)
        except Timeout:
            raise GitHubAcquisitionError(
                "GitHub job-log streaming timed out.", reason="timeout"
            ) from None
        except RequestException:
            raise GitHubAcquisitionError(
                "GitHub job-log transfer failed.", reason="transport_error"
            ) from None

        if not result:
            raise GitHubResponseError("GitHub job log was empty.")
        return bytes(result)
    finally:
        response.close()


__all__ = ["download_bounded_job_log", "MAX_JOB_LOG_BYTES"]
