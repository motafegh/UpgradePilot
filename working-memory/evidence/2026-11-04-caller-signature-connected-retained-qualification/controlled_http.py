"""Authored HTTP universe over retained source bytes for normal product composition.

PR identity/diffs and source bytes come from the selected capture. JSON provider
wrappers, catalog-only inventories, missing-file responses and release/tag/index
responses are controlled observations, not original provider-response replay.
The normal clients, shared ledger and source selection execute without path or
expected-answer selectors. Unknown endpoints fail rather than escape to network.
"""
import base64
from hashlib import sha256
from io import BytesIO
import json
from urllib.parse import parse_qs, unquote, urlsplit

from requests import Response
from requests.adapters import BaseAdapter


class RetainedHTTP(BaseAdapter):
    def __init__(self, case):
        self.case = case
        self.dispatched = []
        self.raw = case.body["acquisition"]["native_inputs"]
        scopes = {s.source_id: s for s in case.catalog.scopes}
        self.files = {(scopes[f.source_id].repository, scopes[f.source_id].revision, f.path): f.content for f in case.catalog.files}
        self.inventories = {}
        self.trees = {}
        for repo, revision, path in self.files:
            self.inventories.setdefault((repo, revision), []).append(path)
        for key, paths in self.inventories.items():
            tree = sha256(json.dumps([*key, sorted(paths)]).encode()).hexdigest()[:40]
            self.trees[key] = tree
        self.packages, self.tags = {}, {}
        acquisition = case.body["acquisition"]
        ordinary = acquisition["ordinary_acquisition"]
        receipts = [*ordinary["changed_package_sources"]["attempts"], *acquisition["internal_module_requests"]]
        for item in receipts:
            if item["state"] != "module_examined":
                continue
            metadata = item["metadata"]
            self.packages[metadata["package"], metadata["version"]] = (
                item["repository"], [r["raw"] for r in metadata["requirements"]],
            )
            self.tags.update({(item["repository"], tag): revision for tag, revision in item["tag_commits"].items()})
        for sample in ordinary["adapter_exploration"]["samples"]:
            metadata = sample["metadata"]
            self.packages[metadata["package"], sample["version"]] = (
                sample["repository"], [r["raw"] for r in metadata["requirements"]],
            )
            self.tags[sample["repository"], sample["version"]] = sample["revision"]

    def payload(self, url):
        parsed = urlsplit(url)
        path = unquote(parsed.path)
        identity = self.raw["identity"]
        if parsed.hostname == "pypi.org":
            bits = path.strip("/").split("/")
            assert bits[0] == "pypi" and bits[-1] == "json", path
            package = bits[1]
            if len(bits) == 3:
                versions = {version: [] for p, version in self.packages if p == package}
                return (200, dict(info=dict(name=package), releases=versions, last_serial=1)) if versions else (404, {})
            assert len(bits) == 4, path
            version = bits[2]
            if (package, version) not in self.packages:
                return 404, {}
            repo, requirements = self.packages[package, version]
            return 200, dict(info=dict(name=package, version=version, requires_dist=requirements,
                project_urls={"Source": "https://github.com/" + repo}), urls=[], last_serial=1)
        assert parsed.hostname == "api.github.com", parsed.hostname
        prefix = f"/repos/{identity['repository']}/pulls/{identity['number']}"
        if path == prefix:
            return 200, dict(number=identity["number"], title=identity["title"], state=identity["state"], merged=identity["merged"],
                user=dict(login=identity["author"]), base=dict(ref=identity["base_ref"], sha=identity["base_sha"]),
                head=dict(ref=identity["head_ref"], sha=identity["head_sha"]), changed_files=identity["changed_files"],
                body=self.raw["description"]["text"])
        if path == prefix + "/files":
            return 200, [dict(f, contents_url=f"https://api.github.com/repos/{identity['repository']}/contents/{f['filename']}?ref={identity['head_sha']}") for f in self.raw["changed_files"]]
        bits = path.strip("/").split("/")
        assert len(bits) >= 4 and bits[0] == "repos", path
        repo = "/".join(bits[1:3])
        suffix = "/".join(bits[3:])
        if suffix.startswith("git/ref/tags/"):
            tag = suffix.removeprefix("git/ref/tags/")
            revision = self.tags.get((repo, tag))
            return (200, dict(ref="refs/tags/" + tag, object=dict(type="commit", sha=revision))) if revision else (404, {})
        if suffix.startswith("git/commits/"):
            revision = suffix.removeprefix("git/commits/")
            tree = self.trees.get((repo, revision))
            return (200, dict(sha=revision, tree=dict(sha=tree))) if tree else (404, {})
        if suffix.startswith("git/trees/"):
            tree = suffix.removeprefix("git/trees/")
            key = next((k for k, v in self.trees.items() if k[0] == repo and v == tree), None)
            return (200, dict(sha=tree, truncated=False,
                tree=[dict(path=p, type="blob", mode="100644") for p in sorted(self.inventories[key])])) if key else (404, {})
        if suffix.startswith("contents/"):
            file_path = suffix.removeprefix("contents/")
            revision = parse_qs(parsed.query)["ref"][0]
            content = self.files.get((repo, revision, file_path))
            return (200, dict(type="file", path=file_path, encoding="base64",
                content=base64.b64encode(content.encode()).decode())) if content is not None else (404, {})
        raise AssertionError("Unadmitted controlled endpoint: " + path)

    def send(self, request, **kwargs):
        assert request.method == "GET"
        status, payload = self.payload(request.url)
        self.dispatched.append(dict(url=request.url, status=status))
        response = Response()
        response.status_code, response.raw = status, BytesIO(json.dumps(payload).encode())
        response.request, response.url = request, request.url
        return response

    def close(self):
        pass
