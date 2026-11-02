# Resource manifest contract

A resource manifest describes a resource and its requested permissions; it does not grant permission to execute it.

## Required fields
`manifest_version`, stable `id`, `kind`, human-readable `name`, and `version`.

## Security
- Treat manifests and referenced artifacts as untrusted.
- Resolve dependencies against an allowlisted registry.
- Require explicit authorization for every declared permission.
- Verify integrity against a trusted digest source; a digest alone does not prove publisher identity.
- Never auto-execute a resource solely because its manifest validates.

The normative JSON Schema is [resource-manifest.schema.json](../schemas/resource-manifest.schema.json).
