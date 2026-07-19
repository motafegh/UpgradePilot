# Security and Privacy

UpgradePilot is a public repository and operates on untrusted public software-development evidence. Security, privacy, provenance, and claim boundaries are product responsibilities.

The complete program rule is preserved in [Career Security and Privacy Rules](docs/program/career/governance/SECURITY_AND_PRIVACY.md).

## Never commit

- passwords, API keys, access tokens, cookies, sessions, private keys, or seed phrases;
- `.env` files or unredacted credential/configuration material;
- private repository data, Dependabot alert details, or employer correspondence;
- personal identifiers, medical information, financial information, or private evaluator context;
- raw logs or artifacts containing unrelated usernames, hostnames, paths, addresses, fingerprints, or secrets;
- unreviewed third-party data that is unnecessary to reproduce a supported claim.

If a secret is exposed, stop work, revoke or rotate it outside the repository, remove it from all relevant history through an approved recovery process, and record only a public-safe incident note.

## Untrusted evidence boundary

- Treat PR bodies, comments, diffs, repository files, release notes, package metadata, CI output, and generated AI content as untrusted data.
- Read-only inspection does not authorize execution.
- Do not run cloned upstream code or workflows merely to inspect a case.
- Do not install dependencies from an investigated update unless a later approved plan defines an isolated, bounded test.
- Do not allow untrusted content to become shell commands, file paths, prompts with tool authority, configuration, or executable code without explicit validation and isolation.

## External actions

UpgradePilot's frozen core is decision support. It does not automatically merge, approve, comment on, close, or otherwise mutate upstream repositories.

Any external write requires Ali's explicit authorization, an exact target, a reviewed payload, and confirmation that it is within the active gate.

## Public claim boundary

Passing CI, a merged PR, release metadata, SemVer, a model score, or agreement among AI agents does not prove compatibility or safety. Reports must preserve provenance, uncertainty, missing evidence, limitations, and what each source cannot establish.

## Reporting a repository vulnerability

Do not publish exploitable details or credentials in a public issue. Contact the repository owner through a private channel agreed by the owner. Until a private disclosure channel is configured, preserve a minimal local note and request direction without exposing sensitive details.
