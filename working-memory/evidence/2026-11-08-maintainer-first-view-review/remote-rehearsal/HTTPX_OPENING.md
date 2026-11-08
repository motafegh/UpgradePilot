## Review at a glance

**HTTPX 0.27.2 → 0.28.1.** The arguments forwarded on the sampled TestClient path fit both selected HTTPX initializer signatures. This finding depends on the sampled path and dispatch assumptions. Which initializer actually received the arguments in a target test remains unobserved. See `source-49` and `source-47` in the detailed report. The recorded action is abstain.
