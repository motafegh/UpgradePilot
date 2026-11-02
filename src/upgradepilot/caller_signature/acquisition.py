"""Invocation policy and shared physical-request ledger for source acquisition.

Construct AcquisitionSession with an explicit policy before the ordinary PR
prefix, then inject that same session into existing GitHub/PyPI clients. Stages
reserve later GitHub work without resetting counts. Every dispatched request,
including the narrowly opted-in PyPI timeout recovery, consumes shared budgets.
Snapshot acquisition_receipt() for the native source-family owner; this module
neither publishes Workspace revisions nor interprets admitted source evidence.

The deadline is cooperative checks plus bounded socket timeouts, not a process
wall-clock sandbox. Analysis uses the separate bounded product worker.
"""
from __future__ import annotations

import time
from contextlib import contextmanager
from dataclasses import asdict, dataclass
from urllib.parse import urlsplit

from requests.exceptions import RequestException, Timeout

from ..github.api import GitHubAcquisitionError
from ..github.auth_session import GitHubPublicSession
from .evidence import MeasuredDuration
from .source_evidence import (
    SourceAcquisitionLimits, SourceAcquisitionStop, SourceRequestEvent,
    SourceRetryDecision, SourceTransportReceipt,
)


@dataclass(frozen=True)
class AcquisitionPolicy:
    """Explicit invocation work policy, independent of provider/account quota.

    Defaults and ceilings preserve the qualified source-acquisition contract. A
    token changes authentication, never these limits. Policy construction alone
    does not authorize provider work or enlarge source/checker capability.
    """

    github_requests: int = 50
    provider_requests: int = 100
    response_bytes: int = 8 * 1024 * 1024
    aggregate_bytes: int = 32 * 1024 * 1024
    elapsed_seconds: float = 180.0
    source_request_reserve: int = 24
    target_file_attempts: int = 16
    adapter_candidate_attempts: int = 2

    def __post_init__(self):
        ceilings = (200, 400, 8 * 1024 * 1024, 64 * 1024 * 1024, 300.0, 199, 200, 12)
        for name, ceiling in zip(self.__dataclass_fields__, ceilings):
            value = getattr(self, name)
            types = (int, float) if name == "elapsed_seconds" else (int,)
            if type(value) not in types or not 0 < value <= ceiling:
                raise ValueError("Invalid acquisition policy: " + name)
        if self.source_request_reserve >= self.github_requests:
            raise ValueError("Source reservation must leave earlier GitHub work available.")
        if self.provider_requests < self.github_requests:
            raise ValueError("All-provider budget cannot be below the GitHub budget.")


PYPI_TIMEOUT_RETRY_POLICY = dict(host="pypi.org", method="GET", max_retries_per_request=1,
    max_retries_per_acquisition=2, eligible_failure="timeout_before_response", shared_limits_unchanged=True)


class AcquisitionSession(GitHubPublicSession):
    """Host-scoped transport; anonymous unless a token is explicitly supplied.

    No declared URL is passed here: provider clients construct their own URLs.
    Rejected redirects are provider failures, never source absence or success.
    """

    request_limit_reason = "acquisition_request_limit"

    def __init__(self, *, token: str | None = None, policy: AcquisitionPolicy,
                 clock=time.monotonic, retry_pypi_timeouts=False):
        if not isinstance(policy, AcquisitionPolicy):
            raise ValueError("An explicit acquisition policy is required.")
        if type(retry_pypi_timeouts) is not bool:
            raise ValueError("Timeout recovery requires an explicit charged policy.")
        super().__init__()
        self.github_requests = 0
        self.request_limit_reached = False
        self._github_token = token
        self.auth_mode = "token-env" if token else "anonymous"
        self.policy = policy
        self._clock = clock
        self._started = clock()
        self._stage = "unscoped"
        self._reserve = 0
        self.provider_requests = 0
        self.body_bytes = 0
        self.receipts = []
        self.stop_reasons = []
        self.retry_pypi_timeouts = retry_pypi_timeouts
        self.retry_decisions = []

    @contextmanager
    def stage(self, name, *, reserve_github=0):
        """Reserve later work without resetting shared counters or changing auth."""
        previous = self._stage, self._reserve
        if type(reserve_github) is not int or reserve_github < 0:
            raise ValueError("Invalid stage reservation.")
        self._stage, self._reserve = name, max(self._reserve, reserve_github)
        try:
            yield
        finally:
            self._stage, self._reserve = previous

    def _refuse(self, reason):
        marker = {"stage": self._stage, "reason": reason}
        if marker not in self.stop_reasons:
            self.stop_reasons.append(marker)
        if reason == "acquisition_request_limit":
            self.request_limit_reached = True
        raise GitHubAcquisitionError("Source acquisition stopped: " + reason, reason=reason)

    def _remaining_time(self):
        remaining = self.policy.elapsed_seconds - (self._clock() - self._started)
        if remaining <= 0:
            self._refuse("acquisition_deadline")
        return remaining

    def finish_acquisition(self):
        """Reject an over-deadline acquisition even if its last read completed."""
        self._remaining_time()

    def acquisition_receipt(self) -> SourceTransportReceipt:
        """Snapshot exact public-safe costs into the existing native source family.

        Snapshots own immutable event copies, so a later request cannot rewrite an
        earlier source-progress checkpoint. No headers, credential values or URL
        query strings enter retained evidence. A received event means a bounded
        body arrived; provider parsing/identity admission remains client-owned.
        """
        limits = asdict(self.policy)
        limits["elapsed_seconds"] = MeasuredDuration.from_seconds(
            float(self.policy.elapsed_seconds), "acquisition_policy_elapsed_limit"
        )
        return SourceTransportReceipt(
            limits=SourceAcquisitionLimits(**limits), auth=self.auth_mode,
            github_requests=self.github_requests, provider_requests=self.provider_requests,
            decoded_body_bytes=self.body_bytes,
            elapsed=MeasuredDuration.from_seconds(max(0.0, self._clock() - self._started), "source_acquisition_elapsed"),
            deadline_kind="cooperative_monotonic_checks_and_bounded_socket_timeouts",
            stops=tuple(SourceAcquisitionStop(**item) for item in self.stop_reasons),
            requests=tuple(SourceRequestEvent(**item) for item in self.receipts),
            retry_policy="pypi-get-timeout-once/1" if self.retry_pypi_timeouts else "none",
            retry_decisions=tuple(SourceRetryDecision(**item) for item in self.retry_decisions),
        )

    def request(self, method, url, **kwargs):
        """Optional narrowly bounded recovery; every physical attempt stays charged.

        Only PyPI GET Timeout before a response is eligible. Status, body,
        integrity, auth, policy and GitHub failures keep their original handling.
        Recovery is disabled unless explicitly selected. No whole-attempt rerun.
        """
        before = self.provider_requests
        try:
            return self._request_once(method, url, **kwargs)
        except Timeout:
            if (not self.retry_pypi_timeouts or method.upper() != "GET" or urlsplit(url).hostname != "pypi.org"
                or self.provider_requests <= before or self.receipts[-1]["status"] is not None
                or len(self.retry_decisions) >= PYPI_TIMEOUT_RETRY_POLICY["max_retries_per_acquisition"]):
                raise
            decision = dict(after_provider_request=self.provider_requests, retry_provider_request=None,
                            reason="timeout_before_response", state="selected")
            self.retry_decisions.append(decision)
            before_retry = self.provider_requests
            try:
                # No catch/retry around this second physical attempt: at most one
                # retry per logical request, subject to the same remaining limits.
                return self._request_once(method, url, **kwargs)
            finally:
                if self.provider_requests > before_retry:
                    decision.update(retry_provider_request=self.provider_requests, state="dispatched")
                else:
                    decision["state"] = "not_dispatched"

    @staticmethod
    def _request_host(method, url):
        parsed = urlsplit(url)
        if (
            method.upper() != "GET"
            or parsed.scheme != "https"
            or parsed.hostname not in {"pypi.org", "api.github.com"}
            or parsed.username
            or parsed.password
            or parsed.port
        ):
            raise RequestException("Source request outside admitted provider scope.")
        return parsed.hostname

    def _request_headers(self, host, headers):
        headers = dict(headers)
        if host == "api.github.com" and self._github_token:
            headers["Authorization"] = "Bearer " + self._github_token
        else:
            headers.pop("Authorization", None)
        return headers

    def _request_once(self, method, url, **kwargs):
        host = self._request_host(method, url)
        github = host == "api.github.com"
        maximum = self.policy.github_requests
        if github:
            if self.github_requests >= maximum:
                self.request_limit_reached = True
                self._refuse("acquisition_request_limit")
            if self.github_requests >= maximum - self._reserve:
                self._refuse("acquisition_stage_request_limit")
        remaining = self._remaining_time()
        if self.provider_requests >= self.policy.provider_requests:
            self._refuse("acquisition_provider_request_limit")
        if self.body_bytes >= self.policy.aggregate_bytes:
            self._refuse("acquisition_aggregate_body_limit")
        timeout = kwargs.get("timeout", (3.05, 15.0))
        timeout = timeout if isinstance(timeout, tuple) else (timeout, timeout)
        kwargs["timeout"] = tuple(min(t or remaining, remaining) for t in timeout)
        kwargs["stream"] = True
        if github:
            self.github_requests += 1
        kwargs["headers"] = self._request_headers(host, kwargs.get("headers", {}))
        kwargs["allow_redirects"] = False
        self.provider_requests += 1
        receipt = dict(stage=self._stage, host=host, path=urlsplit(url).path[:512],
                       github_requests=self.github_requests, provider_requests=self.provider_requests,
                       decoded_body_bytes=0, status=None, state="started", reason=None)
        self.receipts.append(receipt)
        response = None
        try:
            response = super().request(method, url, **kwargs)
            receipt["status"] = response.status_code
            body = bytearray()
            for chunk in response.iter_content(chunk_size=8192):
                self.body_bytes += len(chunk)
                receipt["decoded_body_bytes"] += len(chunk)
                self._remaining_time()
                if receipt["decoded_body_bytes"] > self.policy.response_bytes:
                    self._refuse("acquisition_response_body_limit")
                if self.body_bytes > self.policy.aggregate_bytes:
                    self._refuse("acquisition_aggregate_body_limit")
                body.extend(chunk)
            self._remaining_time()
            # Requests' Response API then serves both json() and iter_content()
            # from these bounded decoded bytes. Providers keep their stricter caps.
            response._content = bytes(body)
            response._content_consumed = True
            receipt["state"] = "received"
            return response
        except Exception as exc:
            receipt["state"] = "failed"
            receipt["reason"] = getattr(exc, "reason", "transport_error")
            raise
        finally:
            if response is not None:
                response.close()

