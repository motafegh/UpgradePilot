"""Bounded file declarations from the PyPI Simple Index JSON endpoint."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from hashlib import sha256
import re
from urllib.parse import quote

from ..package_identity import normalize_package_name
from .api import PyPIJsonApiClient, PyPIRequestError, PyPIResponseError
from .release import MAX_REQUIRES_PYTHON_TEXT, PublishedFileRequiresPython


SIMPLE_INDEX_MEDIA = "application/vnd.pypi.simple.v1+json"
MAX_INDEX_VERSIONS = 20_000
MAX_INDEX_FILES = 50_000


def simple_index_url(package: str) -> str:
    return f"https://pypi.org/simple/{quote(package, safe='')}/"


@dataclass(frozen=True)
class SimpleIndexBasis:
    source_url: str
    sha256: str
    serial: int
    observed_at: datetime
    file_count: int


@dataclass(frozen=True)
class SimpleIndexObservation:
    basis: SimpleIndexBasis
    versions: tuple[str, ...]
    files: tuple[PublishedFileRequiresPython, ...]


@dataclass(frozen=True)
class SimpleIndexProblem:
    reason: str


class PyPISimpleIndexClient(PyPIJsonApiClient):
    def __init__(self, *, session):
        super().__init__(session=session, max_response_bytes=8 * 1024 * 1024, accept=SIMPLE_INDEX_MEDIA)

    def get_index(self, package: str) -> SimpleIndexObservation | SimpleIndexProblem:
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", package):
            raise ValueError("Simple index needs a normalized package name.")
        url = simple_index_url(package)
        body_digests = []
        try:
            response = self._get_response(url, resource="Simple Index")
            if response.status_code != 200:
                status = response.status_code
                response.close()
                return SimpleIndexProblem("index_not_found" if status == 404 else "index_http_failure")
            media = response.headers.get("Content-Type", "").partition(";")[0].strip().lower()
            if media != SIMPLE_INDEX_MEDIA:
                response.close()
                return SimpleIndexProblem("unsupported_index_media")
            data = self._read_json_object(
                response, resource="Simple Index", observe_body=lambda body: body_digests.append(sha256(body).hexdigest()),
            )
        except PyPIRequestError as exc:
            return SimpleIndexProblem(exc.reason)
        except (PyPIResponseError, RecursionError):
            return SimpleIndexProblem("malformed_index_response")
        name, meta = data.get("name"), data.get("meta")
        if type(name) is not str or normalize_package_name(name) != package:
            return SimpleIndexProblem("index_identity_mismatch")
        if type(meta) is not dict or not re.fullmatch(r"1\.[0-9]+", str(meta.get("api-version", ""))):
            return SimpleIndexProblem("unsupported_index_metadata")
        serial = meta.get("_last-serial")
        versions, files = data.get("versions"), data.get("files")
        if (type(serial) is not int or serial < 0 or type(versions) is not list or type(files) is not list
                or len(versions) > MAX_INDEX_VERSIONS or len(files) > MAX_INDEX_FILES):
            return SimpleIndexProblem("invalid_index_scope")
        if any(type(version) is not str or not 0 < len(version) <= 128 for version in versions):
            return SimpleIndexProblem("malformed_index_versions")
        records = []
        seen = set()
        for row in files:
            filename = row.get("filename") if type(row) is dict else None
            if type(filename) is not str or not 0 < len(filename) <= 512 or filename in seen:
                return SimpleIndexProblem("malformed_index_files")
            seen.add(filename)
            hashes = row.get("hashes")
            digest = hashes.get("sha256") if type(hashes) is dict else None
            spec = row.get("requires-python")
            yanked = row.get("yanked")
            records.append(PublishedFileRequiresPython(
                filename, digest.lower() if type(digest) is str and re.fullmatch(r"[0-9a-fA-F]{64}", digest) else "",
                spec if type(spec) is str and 0 < len(spec) <= MAX_REQUIRES_PYTHON_TEXT else None,
                True if type(yanked) is str else yanked if type(yanked) is bool else None,
            ))
        basis = SimpleIndexBasis(url, body_digests[0], serial, datetime.now(timezone.utc), len(records))
        return SimpleIndexObservation(basis, tuple(versions), tuple(records))
