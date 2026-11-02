import unittest
from tools.validate_manifest import validate
V={"manifest_version":"1.0","id":"example.math.add","kind":"tool","name":"Add","version":"1","permissions":["compute"],"dependencies":[]}
class Tests(unittest.TestCase):
 def test_valid(self): self.assertEqual(validate(V),[])
 def test_kind(self): self.assertTrue(validate({**V,"kind":"bad"}))
 def test_duplicate_permissions(self): self.assertTrue(validate({**V,"permissions":["x","x"]}))
 def test_integrity(self): self.assertTrue(validate({**V,"integrity":{"algorithm":"md5","digest":"x"}}))
 def test_type(self): self.assertTrue(validate([]))
if __name__=="__main__": unittest.main()
