# B2 Step 7C — LM Studio Proxy Contamination Diagnosis

**Date:** 2026-08-05  
**Scope:** S001 live Step 7C provider preflight failure  
**Result:** Root cause established; LM Studio loopback transport itself remained healthy

## Observed failure

The live S001 Step 7C proof successfully reacquired the real Soup Sieve evidence and built the complete crossed-release source window:

```text
soupsieve 2.6 -> 2.8.4
crossed releases: 2.7, 2.8, 2.8.1, 2.8.2, 2.8.3, 2.8.4
exact commit: 28108ab805818c832d9568142a99844fd95a0d39
changelog: docs/src/markdown/about/changelog.md
window: 1450 / 4096 characters
```

The LM Studio preflight then returned:

```text
GET http://127.0.0.1:12345/v1/models
HTTP 500
```

This initially looked like a local-provider failure.

## Proxy evidence

The WSL shell contained ambient proxy variables pointing to a local Privoxy listener:

```text
HTTP_PROXY=http://127.0.0.1:8080
HTTPS_PROXY=http://127.0.0.1:8080
http_proxy=http://127.0.0.1:8080
https_proxy=http://127.0.0.1:8080
```

`NO_PROXY`/`no_proxy` contained wildcard-like loopback entries including `127.*`, but the normal curl probe still selected the proxy:

```text
Trying 127.0.0.1:8080...
Connected to 127.0.0.1 port 8080
GET http://127.0.0.1:12345/v1/models
HTTP/1.1 500 Internal Privoxy Error
```

The response body identified Privoxy explicitly.

## Direct-loopback control

The same request with explicit proxy bypass:

```bash
curl -i -v --noproxy '*' http://127.0.0.1:12345/v1/models
```

connected directly to:

```text
127.0.0.1:12345
```

and returned:

```text
HTTP/1.1 200 OK
X-Powered-By: Express
Content-Type: application/json
```

The model inventory included the adopted model:

```text
gemma-4-e4b-it-ud
```

Therefore:

```text
LM Studio server unavailable                  false
WSL -> LM Studio localhost transport broken   false
selected model missing                        false
ambient proxy intercepted loopback request    true
```

## Product correction

The Step 7C product adapter now creates a dedicated `requests.Session` with:

```python
session.trust_env = False
```

for LM Studio loopback traffic. The default extractor therefore does not inherit ambient `HTTP_PROXY`, `HTTPS_PROXY`, `ALL_PROXY`, or client-specific `NO_PROXY` behavior.

The live Step 7C tool uses the same proxy-independent session for its provider preflight and inference request.

## Why this is a security boundary

The accepted deployment is intentionally local:

```text
UpgradePilot in WSL
-> loopback HTTP
-> LM Studio on Windows host
```

Silently routing bounded release text or model prompts through an unrelated proxy violates that intended transport boundary even if the proxy is also local. Proxy independence is therefore both a reliability requirement and a privacy/security control.

## Reusable diagnostic rule

When a future local-model probe returns an unexpected HTTP response:

1. inspect response headers/body to identify who actually answered;
2. compare a normal request with `curl --noproxy '*'`;
3. inspect proxy environment variables without exposing credentials;
4. do not change LM Studio bind/CORS/firewall settings until proxy contamination is excluded.

This incident did not justify disabling the user's VPN/proxy globally.
