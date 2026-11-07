# PyPI acquisition route repair

November 7, 2026. [Cycle](../../2026-11-07_pypi-route-repair_cycle.md), [direct-route diagnosis](../2026-11-06-pypi-transport-diagnosis/RESULTS.md), [route evidence](results.json), [successor binding](successor-binding.json).

The installed client admitted both release indices through the existing unauthenticated loopback HTTP proxy. The earlier direct controls timed out during TLS. The working route resolves the observed index acquisition failure at the environment and launch boundary. The precise cause of the direct TLS stall remains open.

| PyPI index | Initial proxy control | Verification through successor launcher |
|---|---|---|
| FastAPI | HTTP 200, available, 360 release versions, 585,345 decoded bytes | HTTP 200, available, 585,345 decoded bytes |
| pytest | HTTP 200, available, 193 release versions, 284,454 decoded bytes | HTTP 200, available, 284,454 decoded bytes |

The launcher builds a separate child environment. It uses the validated local `https_proxy` for PyPI and sets the GitHub API host in `NO_PROXY` and `no_proxy`. The existing acquisition session admits only the PyPI and GitHub HTTPS hosts. A controlled adapter exercised the actual Requests environment merge and product header handling. GitHub selected no proxy and carried the synthetic bearer header. PyPI selected the proxy, carried no authorization header and retained certificate verification. Those two adapter calls were offline. The four actual network calls were anonymous PyPI index GETs. Product limits admitted the response sizes without adjustment.

## Successor invocation

Use `launch_successor.py` with the bound virtual environment interpreter. The default mode checks the recorded route proof, source and installed bindings, and availability of `product-attempt-02` and `task-review-02`. The executable command, case guards, acquisition limits and task criteria come from the previous reviewed manifest. The new binding supplies the split route and separate destinations. A later `--execute-live` activation runs that exact normal product invocation and retains its own evidence.

```bash
.venv/bin/python working-memory/evidence/2026-11-07-pypi-route-repair/launch_successor.py
```

The route repair is qualified for both required indices. The full successor product run and paired HTTPX task remain pending. Keep the earlier partial outcome as the result of its original invocation. Its saved report, source and Workspace evidence verify against their original digests.
