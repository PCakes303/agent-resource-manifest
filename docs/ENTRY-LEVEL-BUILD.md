# Entry-level build

Requires Python 3.10+; no third-party packages are required.

```bash
python tools/starter_build.py
python -m unittest discover -s tests -v
```

The starter build loads the example tool resource and validates its ID, kind, version, permissions, dependencies, and optional integrity block. It does not execute the resource.

**Next tiers**
- Developer: author a manifest for a local tool and add positive/negative fixtures.
- Production: verify publisher signatures, resolve dependencies from approved sources, generate SBOMs, and enforce sandboxed execution policy.
