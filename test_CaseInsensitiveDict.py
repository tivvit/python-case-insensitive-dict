import unittest
from CaseInsensitiveDict import CaseInsensitiveDict

class TestLowercaseDict(unittest.TestCase):
    def setUp(self):
        self.cid = CaseInsensitiveDict({"A": {"A": {"A": 3}}, "B": 2})

    def test_empty(self):
        self.assertEqual("{}", str(CaseInsensitiveDict({})))

    def test_small(self):
        self.assertEqual("{'a': 1}", str(CaseInsensitiveDict({"a": 1})))

    def test_multiple(self):
        self.assertEqual("{'a': 1, 'b': 2}", str(CaseInsensitiveDict({"A": 1, "B": 2})))

    def test_nested(self):
        self.assertEqual("{'a': {'a': 2}, 'b': 2}", str(CaseInsensitiveDict({"A": {"A": 2}, "B": 2})))

    def test_multi_nested(self):
        self.assertEqual("{'a': {'a': {'a': 3}}, 'b': 2}", str(CaseInsensitiveDict({"A": {"A": {"A": 3}}, "B": 2})))

    def test_get(self):
        self.assertEqual("{'a': {'a': 3}}", str(self.cid["A"]))

    def test_nested_get(self):
        self.assertEqual(3, self.cid["A"]["A"]["A"])

    def test_get_low(self):
        self.assertEqual(2, self.cid["b"])

    def test_has(self):
        self.assertTrue("A" in self.cid)

    def test_has(self):
        self.assertFalse("C" in self.cid)

if __name__ == '__main__':
    unittest.main()