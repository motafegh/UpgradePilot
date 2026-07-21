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

## Public claim boundary

Passing CI, a merged PR, release metadata, SemVer, a model score, or agreement among AI agents does not prove compatibility or safety.

Reports must preserve provenance, uncertainty, missing evidence, limitations, assistance, and what each source cannot establish.

Do not use unsupported claims such as “production-ready,” “enterprise-grade,” “expert,” or “safe” without evidence meeting that exact standard.

## Reporting a vulnerability

Do not publish exploitable details or credentials in a public issue. Contact the repository owner through an agreed private channel. Until a private disclosure channel is configured, preserve a minimal local note and request direction without exposing sensitive details.
