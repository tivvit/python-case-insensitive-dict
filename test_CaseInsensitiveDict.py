import unittest
from CaseInsensitiveDict import CaseInsensitiveDict

class TestLowercaseDict(unittest.TestCase):
    def setUp(self):
        self.cid = CaseInsensitiveDict({"A": {"A": {"A": 3}}, "B": 2})

    def test_blank_init(self):
        self.assertEqual("{}", str(CaseInsensitiveDict()))

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

    def test_del(self):
        cid = CaseInsensitiveDict({"a": 1})
        del cid["a"]
        self.assertFalse("a" in cid)

    def test_set(self):
        cid = CaseInsensitiveDict()
        cid["a"] = 1
        self.assertEqual("{'a': 1}", str(cid))

    def test_nested_set(self):
        cid = CaseInsensitiveDict()
        cid["a"] = {"B": 2}
        self.assertEqual("{'a': {'b': 2}}", str(cid))

    def test_iteration(self):
        self.assertEqual(["a", "b"], [k for k in self.cid])

    def test_has_key(self):
        self.assertTrue(self.cid.has_key("A"))

    def test_has_key(self):
        self.assertFalse(self.cid.has_key("C"))

    def test_get_method(self):
        self.assertEqual(2, self.cid.get("b"))

    def test_get_method_default(self):
        self.assertEqual(2, self.cid.get("b", 1))

    def test_get_method_default_used(self):
        self.assertEqual(1, self.cid.get("C", 1))

    def test_items(self):
        self.assertEqual("[('a', {'a': {'a': 3}}), ('b', 2)]", str(self.cid.items()))

    def test_keys(self):
        self.assertEqual(["a", "b"], self.cid.keys())

    def test_vals(self):
        self.assertEqual("[{'a': {'a': 3}}, 2]", str(self.cid.values()))

    def test_compare(self):
        self.assertTrue({"a": 1, "B": 2} == CaseInsensitiveDict({"A": 1, "b": 2}))

    def test_update(self):
        cid = CaseInsensitiveDict({"A": 1, "b": 2})
        cid.update({"A": 2})
        self.assertEquals("{'a': 2, 'b': 2}", str(cid))

    def test_update_nested(self):
        cid = CaseInsensitiveDict({"A": 1, "b": 2})
        cid.update({"A": {"C": 3}})
        self.assertEquals("{'a': {'c': 3}, 'b': 2}", str(cid))

if __name__ == '__main__':
    unittest.main()