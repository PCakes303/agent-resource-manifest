# Agent Resource Manifest

**MrCakes931 Agent Intelligence Ecosystem · Resource declaration layer**

Defines portable, machine-readable manifests for agent tools, skills, models, datasets, services, and other resources that an agent may discover or request to use.

## Contract goals
- Stable resource identifiers and explicit versions.
- Explicit resource kind, entrypoint, dependencies, and requested permissions.
- Optional integrity metadata with named digest algorithms.
- Deterministic validation and clear security responsibilities for consumers.

## Layout
- schemas/resource-manifest.schema.json — JSON Schema Draft 2020-12 contract.
- examples/tool-resource.json — illustrative tool declaration.
- examples/add.py — inert example implementation.
- docs/RESOURCE-MANIFEST.md — contract and security guidance.
- tools/validate_manifest.py — standard-library reference validator.
- tests/ — automated validator tests.
- .github/workflows/validate.yml — CI validation.

## Validate locally
Requires Python 3.10+; no third-party packages are needed.

    python tools/validate_manifest.py
    python -m unittest discover -s tests -v

## Security model
A manifest describes a resource and its requested permissions; it does not grant permission to execute it. Consumers must authenticate publishers, verify artifacts against a trusted digest source, resolve dependencies against approved registries, enforce resource limits, and authorize every permission independently. A digest alone does not prove publisher identity. Never auto-execute a resource solely because its manifest validates.

## Status
Scaffolded, v0.1.0. The format, example, reference validator, tests, and CI are initial contracts—not a production package manager or execution runtime.

## Entry-level build

Start with the runnable starter build:

    python tools/starter_build.py
    python -m unittest discover -s tests -v

See [Entry-level build guide](docs/ENTRY-LEVEL-BUILD.md) for Starter → Developer → Production progression.

## Ecosystem
Master registry: https://github.com/PCakes303/agent-intelligence-ecosystem

Main public identity: https://github.com/HuffmanMainNode

