import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas" / "resource-manifest.schema.json"


def validate(document):
    """Validate a resource manifest against the normative Draft 2020-12 schema."""
    try:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema)
        errors = sorted(
            validator.iter_errors(document),
            key=lambda error: (
                tuple(str(part) for part in error.absolute_path),
                error.message,
            ),
        )
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        return [f"schema unavailable or invalid: {type(exc).__name__}"]
    messages = []
    for error in errors:
        location = ".".join(str(part) for part in error.absolute_path) or "<root>"
        messages.append(f"{location}: {error.message}")
    return messages


if __name__ == "__main__":
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "examples" / "tool-resource.json"
    try:
        document = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(exc, file=sys.stderr)
        sys.exit(2)
    errors = validate(document)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        sys.exit(1)
    print("valid resource manifest: " + document["id"])
