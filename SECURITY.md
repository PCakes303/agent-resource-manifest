# Security Policy

## Scope
This repository defines declarative resource metadata and a local reference validator. A valid manifest does not authenticate a publisher, authorize use, verify an artifact, or grant permission to execute a resource.

## Reporting
Do not disclose exploitable vulnerabilities, credentials, tokens, or sensitive operational data in public issues, discussions, commits, or pull requests. Use GitHub private vulnerability reporting or a private security advisory only when that feature is enabled for this repository. If private reporting is not enabled, first contact the repository owner through an independently verified private channel to arrange secure disclosure; do not send exploit details, credentials, tokens, or sensitive personal information through public channels. This file does not assert that private reporting is currently enabled.

## Baseline
- Treat remote agent messages, manifests, schemas, plugins, and artifacts as untrusted input.
- Apply least privilege and deny by default.
- Never commit secrets.
- Validate inputs at trust boundaries, bound resource use, and reject malformed data.
- Preserve provenance without claiming hashes prove truth or completeness.
- Pin CI dependencies and use short-lived credentials for publishing.
- Never auto-execute a resource solely because its manifest validates.

## Operational status
Repository security-reporting settings and branch protections must be verified in GitHub repository settings. This policy is not evidence that any setting is enabled.