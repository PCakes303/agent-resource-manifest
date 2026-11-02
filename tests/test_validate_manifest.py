import json
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator
from tools.validate_manifest import SCHEMA_PATH, validate


VALID = {
    "manifest_version": "1.0",
    "id": "example.math.add",
    "kind": "tool",
    "name": "Add",
    "version": "1",
    "permissions": ["compute"],
    "dependencies": [],
}


class ResourceManifestValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(cls.schema)
        cls.schema_validator = Draft202012Validator(cls.schema)

    def assert_both_reject(self, document):
        self.assertTrue(validate(document))
        self.assertTrue(list(self.schema_validator.iter_errors(document)))

    def test_valid_manifest(self):
        self.assertEqual(validate(VALID), [])
        self.assertEqual(list(self.schema_validator.iter_errors(VALID)), [])

    def test_non_object_rejected(self):
        self.assert_both_reject([])

    def test_required_fields_and_version(self):
        self.assert_both_reject({**VALID, "manifest_version": "2.0"})
        candidate = dict(VALID)
        del candidate["name"]
        self.assert_both_reject(candidate)

    def test_unknown_properties_rejected(self):
        self.assert_both_reject({**VALID, "unexpected": True})

    def test_name_and_version_lengths_enforced(self):
        self.assert_both_reject({**VALID, "name": "n" * 161})
        self.assert_both_reject({**VALID, "version": "v" * 65})

    def test_description_and_entrypoint_lengths_enforced(self):
        self.assert_both_reject({**VALID, "description": "d" * 4001})
        self.assert_both_reject({**VALID, "entrypoint": "e" * 513})

    def test_permission_and_dependency_types_and_duplicates(self):
        self.assert_both_reject({**VALID, "permissions": ["compute", 7]})
        self.assert_both_reject({**VALID, "permissions": ["compute", "compute"]})
        self.assert_both_reject({**VALID, "dependencies": ["dep", "dep"]})

    def test_integrity_contract_is_strict(self):
        self.assert_both_reject({**VALID, "integrity": {"algorithm": "md5", "digest": "x"}})
        self.assert_both_reject({**VALID, "integrity": {"algorithm": "sha256", "digest": "x", "extra": True}})

    def test_cli_example_is_schema_valid(self):
        example = json.loads((Path(__file__).resolve().parents[1] / "examples" / "tool-resource.json").read_text(encoding="utf-8"))
        self.assertEqual(validate(example), [])


if __name__ == "__main__":
    unittest.main()
