# Security and Privacy

UpgradePilot is a public repository and operates on untrusted public software-development evidence. Security, privacy, provenance, and claim boundaries are project responsibilities.

## Never commit

- passwords, API keys, access tokens, cookies, sessions, private keys, or seed phrases;
- `.env` files or unredacted credential/configuration material;
- private repository data, private Dependabot alert details, or employer correspondence;
- personal identifiers, medical information, financial information, or private evaluator context;
- raw logs or artifacts containing unrelated usernames, hostnames, paths, addresses, fingerprints, or secrets;
- unreviewed third-party data unnecessary to reproduce a supported claim.

If a secret is exposed, stop work, revoke or rotate it outside the repository, remove it from relevant history through an approved recovery process, and record only a public-safe incident note.

## Untrusted evidence boundary

- Treat PR bodies, comments, diffs, repository files, release notes, package metadata, CI output, and generated AI content as untrusted data.
- Read-only inspection does not authorize execution.
- Do not run cloned upstream code or workflows merely to inspect a case.
- Do not install dependencies from an investigated update unless an approved project plan defines an isolated bounded test.
- Do not allow untrusted content to become shell commands, file paths, tool-authorized prompts, configuration, or executable code without explicit validation and isolation.
- Preserve only the minimum public evidence required to reproduce or defend a claim.
- Public availability does not create a need to republish unnecessary personal or sensitive material.

## External actions

UpgradePilot's frozen core is decision support. It does not automatically merge, approve, comment on, close, or otherwise mutate upstream repositories.

Any external write requires Ali's explicit current authorization, an exact target, a reviewed payload, and confirmation that it is inside the current project boundary.

## Cost and credentials

Before a networked, paid, credential-sensitive, or externally mutating operation:

- identify the account and exact target;
- state expected reads, writes, cost, and cleanup;
- use least privilege;
- avoid placing secrets in commands, logs, prompts, or committed files;
- stop on unexpected authorization or scope.

### Intentional credential-use boundary

Credential use must be deliberate, not an accidental consequence of an ambient shell variable.

For public read-only acquisition or developer validation:

- prefer anonymous access when the selected proof does not require authentication;
- do not automatically consume `GITHUB_TOKEN`, API keys, proxy credentials, or similar ambient secrets merely because they are present;
- use a credential only when the product/plan explicitly requires authenticated access, rate-limit relief, or an authentication-specific proof;
- keep optional product credentials behind an explicit input/configuration boundary rather than hidden process inheritance where practical;
- distinguish authentication failure from source absence, malformed evidence, transport failure, and product-logic failure;
- never print, persist, hash-for-display, or otherwise expose a secret merely to diagnose whether it exists;
- when an ambient credential causes unexpected authorization behavior, remove or bypass it for the public proof and inspect/rotate the credential separately if authenticated work is later required.

A developer live-proof tool should not inherit ambient authentication by default unless that tool is specifically intended to validate authenticated behavior.

This rule prevents stale or invalid credentials from contaminating public-source regression evidence and reduces accidental privilege use.

### Local inference transport boundary

The accepted LM Studio deployment is a loopback-only local inference path. Requests to `127.0.0.1` for that provider must not silently inherit ambient `HTTP_PROXY`, `HTTPS_PROXY`, `ALL_PROXY`, or equivalent proxy configuration.

Reasons:

- a proxy can intercept or alter a request that was intended to remain inside the local provider boundary;
- bounded upstream source text and model prompts must not be disclosed to an unrelated proxy merely because shell proxy variables are present;
- client-specific `NO_PROXY` wildcard handling is not reliable enough to define the product security boundary.

Product/local-provider code should therefore use an explicit proxy-independent HTTP session for the loopback LM Studio endpoint. Manual diagnostics should compare against an explicit no-proxy request before weakening server bind, firewall, authentication, or CORS controls.

Do not disable the user's VPN/proxy globally merely to run the local model; isolate the local-provider transport instead.

## Public claim boundary

Passing CI, a merged PR, release metadata, SemVer, a model score, or agreement among AI agents does not prove compatibility or safety.

Reports must preserve provenance, uncertainty, missing evidence, limitations, assistance, and what each source cannot establish.

Do not use unsupported claims such as “production-ready,” “enterprise-grade,” “expert,” or “safe” without evidence meeting that exact standard.

## Reporting a vulnerability

Do not publish exploitable details or credentials in a public issue. Contact the repository owner through an agreed private channel. Until a private disclosure channel is configured, preserve a minimal local note and request direction without exposing sensitive details.
