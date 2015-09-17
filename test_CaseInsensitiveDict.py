import unittest
from CaseInsensitiveDict import CaseInsensitiveDict


class TestLowercaseDict(unittest.TestCase):
    def setUp(self):
        self.cid = CaseInsensitiveDict({"A": {"A": {"A": 3}}, "B": 2})

    def test_blank_init(self):
        self.assertEqual({}, dict(CaseInsensitiveDict().items()))

    def test_empty(self):
        self.assertEqual({}, dict(CaseInsensitiveDict({}).items()))

    def test_small(self):
        self.assertEqual({'a': 1}, dict(CaseInsensitiveDict({"a": 1}).items()))

    def test_multiple(self):
        self.assertEqual({'a': 1, 'b': 2}, dict(CaseInsensitiveDict({"A": 1, "B": 2}).items()))

    def test_nested(self):
        self.assertEqual({'a': {'a': 2}, 'b': 2}, dict(CaseInsensitiveDict({"A": {"A": 2}, "B": 2}).items()))

    def test_multi_nested(self):
        self.assertEqual({'a': {'a': {'a': 3}}, 'b': 2}, dict(CaseInsensitiveDict({"A": {"A": {"A": 3}}, "B": 2}).items()))

    def test_get(self):
        self.assertEqual({'a': {'a': 3}}, dict(self.cid["A"].items()))

    def test_nested_get(self):
        self.assertEqual(3, self.cid["A"]["A"]["A"])

    def test_get_low(self):
        self.assertEqual(2, self.cid["b"])

    def test_has_a(self):
        self.assertTrue("A" in self.cid)

    def test_has_c(self):
        self.assertFalse("C" in self.cid)

    def test_del(self):
        cid = CaseInsensitiveDict({"a": 1})
        del cid["a"]
        self.assertFalse("a" in cid)

    def test_set(self):
        cid = CaseInsensitiveDict()
        cid["a"] = 1
        self.assertEqual({'a': 1}, dict(cid.items()))

    def test_nested_set(self):
        cid = CaseInsensitiveDict()
        cid["a"] = {"B": 2}
        self.assertEqual({'a': {'b': 2}}, dict(cid.items()))

    def test_iteration(self):
        self.assertEqual(["a", "b"], sorted([k for k in self.cid]))

    def test_has_key_a(self):
        self.assertTrue(self.cid.has_key("A"))
        self.assertTrue("A" in self.cid)

    def test_has_key_c(self):
        self.assertFalse(self.cid.has_key("C"))
        self.assertFalse("C" in self.cid)

    def test_get_method(self):
        self.assertEqual(2, self.cid.get("b"))

    def test_get_method_default(self):
        self.assertEqual(2, self.cid.get("b", 1))

    def test_get_method_default_used(self):
        self.assertEqual(1, self.cid.get("C", 1))

    def test_items(self):
        self.assertEqual([('a', {'a': {'a': 3}}), ('b', 2)], sorted(self.cid.items(), key=lambda x: x[0]))

    def test_keys(self):
        self.assertEqual(["a", "b"], sorted(self.cid.keys()))

    def test_vals(self):
        # or is used because various versions of python are not consistent in order of dict conversion
        self.assertTrue([{'a': {'a': 3}}, 2] == self.cid.values() or
                        [{'a': {'a': 3}}, 2] == self.cid.values())

    def test_compare(self):
        self.assertTrue({"a": 1, "B": 2} == CaseInsensitiveDict({"A": 1, "b": 2}))

    def test_update(self):
        cid = CaseInsensitiveDict({"A": 1, "b": 2})
        cid.update({"A": 2})
        self.assertEquals({'a': 2, 'b': 2}, dict(cid.items()))

    def test_update_nested(self):
        cid = CaseInsensitiveDict({"A": 1, "b": 2})
        cid.update({"A": {"C": 3}})
        self.assertEquals({'a': {'c': 3}, 'b': 2}, dict(cid.items()))

if __name__ == '__main__':
    unittest.main()