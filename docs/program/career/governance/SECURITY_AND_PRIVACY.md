# Security and Privacy Rules

This repository is public. It must contain only information appropriate for public disclosure.

## Never commit

- medication names, doses, schedules, or prescriber details;
- medical diagnoses, treatment notes, symptoms, or private health records;
- financial balances, account details, or precise private financial circumstances;
- home address, phone number, government identifiers, or private family information;
- passwords, API keys, tokens, private keys, seed phrases, cookies, or session data;
- private SSH keys or unredacted `known_hosts`/credential material;
- raw logs containing personal identifiers, secrets, or unrelated system information;
- `.env` files;
- confidential job applications or private employer correspondence;
- private evaluator memory or personal operating profiles.

## Allowed operational context

The repository may record only generalized facts necessary for execution, such as:

- the 24-hour standard weekly requirement and recorded capacity-mode adjustments;
- normal afternoon/evening work blocks;
- Green, Yellow, and Red capacity modes;
- project and career priorities;
- completed work and evidence;
- non-sensitive blockers.

## Technical evidence handling

Before committing UpgradePilot-derived evidence or selectively reused AegisLab/Sentinel evidence after authorization:

1. remove credentials and private keys;
2. replace runtime-specific secrets with placeholders;
3. avoid committing large raw packet captures unless explicitly justified and reviewed;
4. inspect logs, repository records, CI evidence, and other source material for usernames, hostnames, IP addresses, paths, fingerprints, tokens, and private data;
5. preserve only the minimum evidence required to reproduce or explain the result;
6. do not treat public availability as automatic permission to republish unnecessary personal or sensitive content.

This rule does not authorize UpgradePilot implementation or evidence acquisition before the required planning artifacts approve it.

## Public writing standard

Public claims must be:

- reproducible;
- bounded;
- evidence-backed;
- explicit about AI assistance;
- explicit about limitations;
- free of unsupported words such as “production-ready,” “enterprise-grade,” or “expert.”

## Private context boundary

Sensitive personal context may be used privately by the evaluator to calibrate workload and interpretation. It must not be copied into this repository. Public progress reports should say only what is operationally necessary, for example:

- “Yellow capacity day due to reduced functioning.”
- “Red capacity day; work paused.”

No medical explanation is required in public logs.