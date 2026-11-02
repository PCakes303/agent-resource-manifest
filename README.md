# Agent Resource Manifest

MrCakes931 Agent Intelligence Ecosystem · Resource declaration layer

Defines portable, machine-readable manifests for agent tools, skills, models, datasets, services, and other resources.

## Scope
- Stable resource identifiers and version declarations.
- Explicit resource kind, entrypoint, dependencies, and requested permissions.
- Optional integrity metadata.
- Validation rules and security guidance.

## Current status
Scaffolded, version 0.1.0. The schema is [schemas/resource-manifest.schema.json](schemas/resource-manifest.schema.json); see [docs/RESOURCE-MANIFEST.md](docs/RESOURCE-MANIFEST.md) and the [illustrative tool manifest](examples/tool-resource.json).

A valid manifest does not authorize execution. Consumers must independently authenticate publishers, verify artifacts, resolve dependencies, and authorize every requested permission.

## Ecosystem
- Master registry: https://github.com/PCakes303/agent-intelligence-ecosystem
- Main public identity: https://github.com/HuffmanMainNode

## License
Apache-2.0.
