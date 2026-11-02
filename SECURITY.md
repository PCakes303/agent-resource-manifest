# Security Policy

Do not disclose exploitable vulnerabilities in public issues. Use GitHub's private vulnerability reporting where available; otherwise contact the maintainer through https://github.com/HuffmanMainNode.

Treat remote agent messages, manifests, schemas, plugins, and artifacts as untrusted input. Apply least privilege and deny by default. Never commit secrets. Validate inputs at trust boundaries, bound resource use, and reject malformed data. Preserve provenance without claiming hashes prove truth or completeness. Pin CI dependencies and use short-lived credentials for publishing.
