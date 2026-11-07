"""Two public installed-client probes over the existing PyPI-only loopback route."""
import json
import os
from dataclasses import asdict
from pathlib import Path
from urllib.parse import urlsplit

from requests.utils import select_proxy

from upgradepilot.caller_signature.acquisition import AcquisitionPolicy, AcquisitionSession
from upgradepilot.pypi.release import PyPIReleaseIndexClient


PACKAGES = ("fastapi", "pytest")


def configured_loopback_proxy():
    proxy = os.environ.pop("UPGRADEPILOT_DIAGNOSTIC_PROXY")
    url = urlsplit(proxy)
    if (url.scheme != "http" or url.hostname not in {"localhost", "127.0.0.1", "::1"}
            or url.port != 8080 or url.username or url.password or url.path not in {"", "/"}
            or url.query or url.fragment):
        raise ValueError("Expected the existing unauthenticated HTTP loopback proxy.")
    return proxy


def main():
    proxy = configured_loopback_proxy()

    class RouteCheckedSession(AcquisitionSession):
        def send(self, request, **kwargs):
            assert request.url in {f"https://pypi.org/pypi/{name}/json" for name in PACKAGES}
            assert request.method == "GET" and "Authorization" not in request.headers
            assert select_proxy(request.url, kwargs["proxies"]) == proxy
            assert kwargs.get("verify")
            return super().send(request, **kwargs)

    observations = []
    for package in PACKAGES:
        with RouteCheckedSession(policy=AcquisitionPolicy(), token=None) as session:
            session.proxies["https://pypi.org"] = proxy
            with session.stage("pypi_route_diagnostic"):
                index = PyPIReleaseIndexClient(session=session).get_release_index(package)
            observations.append(dict(package=package, state=index.state,
                detail=getattr(index, "detail", None), versions=len(getattr(index, "release_versions", ())),
                transport=asdict(session.acquisition_receipt())))
        Path("observations.json").write_text(json.dumps(observations, indent=2) + "\n")
        print(json.dumps({k:v for k,v in observations[-1].items() if k != "transport"}), flush=True)


if __name__ == "__main__":
    main()
