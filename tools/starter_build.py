#!/usr/bin/env python3
"""Run the entry-level resource-manifest build."""
import json
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools.validate_manifest import validate
root=Path(__file__).resolve().parents[1]
sample=json.loads((root/"examples/tool-resource.json").read_text(encoding="utf-8"))
errors=validate(sample)
if errors: raise SystemExit("\n".join(errors))
print(json.dumps({"build_tier":"starter","project":"agent-resource-manifest","sample":sample["id"],"result":"passed"},indent=2))
