"""GitHub-only Requests session that does not inherit ambient HTTP credentials.

Public PR evidence is anonymous unless the caller deliberately supplies a GitHub
bearer token. Keep Requests' environment-based proxy configuration intact; disabling
``trust_env`` to avoid .netrc would also change transport behavior.
"""

from __future__ import annotations

from requests import PreparedRequest, Response, Session
from requests.auth import AuthBase


class _NoAmbientAuth(AuthBase):
    """Mark authentication as explicitly controlled, preventing .netrc auto-selection."""

    def __call__(self, request: PreparedRequest) -> PreparedRequest:
        return request


class GitHubPublicSession(Session):
    """Use only explicit request credentials on initial and redirected GitHub requests."""

    def __init__(self) -> None:
        super().__init__()
        # Requests otherwise consults .netrc when Session.auth and request.auth are absent.
        self.auth = _NoAmbientAuth()

    def rebuild_auth(self, prepared_request: PreparedRequest, response: Response) -> None:
        """Retain Requests' cross-origin credential stripping without .netrc reloading.

        Requests' default rebuild_auth may reinsert .netrc credentials on redirects,
        even when a no-op session auth suppressed them on the initial request.
        """

        if self.should_strip_auth(response.request.url, prepared_request.url):
            prepared_request.headers.pop("Authorization", None)
