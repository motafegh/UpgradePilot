# B2 LM Studio Network Boundary Learning Plan

**Status:** Position-neutral supporting learning plan  
**Owner:** Ali Rajabi  
**Parent experiment:** [`B2_LOCAL_LLM_SEMANTIC_EXTRACTION_REEVALUATION_PLAN.md`](B2_LOCAL_LLM_SEMANTIC_EXTRACTION_REEVALUATION_PLAN.md)  
**Responsibility:** Build operational understanding of how WSL2, Windows, LM Studio, bind addresses, firewall policy, authentication, and browser CORS interact, without contaminating the first semantic-model evaluation or leaving the local inference server unnecessarily exposed.

## 1. Why this plan exists

The current baseline works through:

```text
UpgradePilot in WSL2
→ http://127.0.0.1:12345
→ LM Studio desktop server on Windows
```

That establishes one functioning transport path. It does not make the following topics unnecessary:

```text
WSL2 NAT versus mirrored networking
Windows host/gateway reachability
loopback versus non-loopback bind addresses
Windows Defender Firewall behavior
LM Studio authentication
LAN exposure
browser same-origin policy and CORS
```

UpgradePilot is a learning-by-doing project. A simpler first path should reduce experiment variables, not erase adjacent technical learning.

## 2. Sequencing rule

Do not mix network-boundary changes into the first structured-output and semantic-quality baseline.

Sequence:

```text
1. freeze one localhost model deployment
2. complete transport/schema smoke proof
3. obtain at least one initial semantic evaluation result
4. preserve the localhost result as the control
5. activate this network-boundary learning plan
6. test alternate network paths one variable at a time
7. restore and verify the secure baseline
```

This ordering separates:

```text
model or semantic failure
from
network exposure or browser-policy failure
```

The networking slice may start after an initial scored result; it does not require final product adoption.

## 3. Learning objectives

Ali should be able to explain and demonstrate:

1. what a network interface and IP address represent;
2. why `127.0.0.1` is loopback and who can normally reach it;
3. how WSL2 NAT and mirrored networking differ at a practical level;
4. what the WSL2 default gateway represents;
5. why a server bound to `127.0.0.1` differs from one bound to `0.0.0.0`;
6. how a listening socket, route, and firewall rule are separate controls;
7. why a Python or `curl` client does not require CORS;
8. why a browser page may require CORS even when the TCP connection works;
9. what LM Studio authentication protects and what it does not protect;
10. how to verify exposure and return to the intended secure state.

## 4. Baseline evidence to preserve

Before changing network configuration, record:

```text
LM Studio server port
current bind/listen addresses
current authentication state
current Windows firewall state relevant to the port
WSL2 network mode
localhost /v1/models result
selected model/load configuration
one successful structured-output response
```

The current known control is:

```text
server port: 12345
WSL2 localhost reachability: working
CORS change: not required for the Python baseline
non-loopback exposure: not required for the Python baseline
```

The last two statements are baseline requirements only, not statements that the concepts are unnecessary.

## 5. Controlled investigations

### A. Listener and bind-address inspection

Inspect which addresses own port `12345` using Windows networking tools. Distinguish:

```text
127.0.0.1:12345
[::1]:12345
0.0.0.0:12345
specific LAN address:12345
```

No bind change occurs until the current listener is understood.

### B. WSL2 route and gateway path

Record:

```text
WSL2 default route
Windows host/gateway candidate
localhost behavior
explicit gateway-address behavior
```

Test the gateway path only after the server bind permits it. A failed gateway request while the server is loopback-only is an expected boundary result, not necessarily a routing defect.

### C. Firewall behavior

If a non-loopback listener is temporarily admitted:

- inspect existing inbound rules;
- create the narrowest temporary rule only when needed;
- limit profile, interface, source range, and port where supported;
- record before/after reachability;
- remove or disable the temporary rule after the exercise.

### D. Authentication behavior

When LM Studio authentication is available and relevant:

- compare unauthenticated rejection with authenticated success;
- use a disposable local credential;
- never commit or paste the credential into repository evidence;
- confirm that authentication does not replace bind/firewall restrictions.

### E. Browser CORS behavior

Use a minimal local browser page served from a distinct origin to compare:

```text
curl/Python request succeeds
browser preflight or fetch fails under same-origin policy
CORS-enabled browser request succeeds
```

CORS is a browser-enforced policy. It is not a general server authentication mechanism and does not protect non-browser clients.

### F. LAN exposure observation

Only if explicitly approved for the controlled exercise:

- bind beyond loopback;
- apply a narrow firewall rule;
- test from one known local device or interface;
- verify that unintended interfaces or sources remain blocked;
- restore loopback-only or the intended final bind.

## 6. Safety and restoration rules

- Do not expose the server to the public internet.
- Do not use router port forwarding or UPnP.
- Do not leave `0.0.0.0` plus a broad inbound firewall rule active after testing.
- Do not enable CORS with an unrestricted origin as a substitute for authentication.
- Do not store credentials in the repository, shell history, screenshots, or working records.
- Run one network-variable change at a time.
- Preserve exact failures; do not repeatedly loosen controls until a request succeeds.
- End with a verified restoration check.

## 7. Evidence to record

For each test:

```text
question
starting configuration
single change
client and source environment
target address and port
observed result
listener/firewall/auth/CORS interpretation
security implication
restoration result
```

Commands and screenshots are supporting evidence. The learning result must explain why the outcome occurred.

## 8. Stop line

Stop when Ali can demonstrate and explain:

- the localhost control path;
- one gateway or alternate-address path;
- one bind-address boundary;
- one firewall allow/deny contrast;
- one browser CORS contrast;
- authentication behavior if supported by the installed LM Studio version;
- successful restoration to the approved final exposure state.

Do not extend this plan into VPN design, router configuration, public hosting, TLS termination, reverse proxies, containers, Kubernetes, or cloud deployment without a separately admitted responsibility.
