import unittest
from multivalue_dict import multivalue_dict

class TestMultiValueDictionary(unittest.TestCase):

    def test_ADD_success(self):
        mvd = multivalue_dict.MultiValueDictionary()
        mvd.ADD("key1", "member1-1").ADD("key1", "member1-2").ADD("key2", "member2-1")
        result1 = mvd._multivalue_dict.get("key1")
        result2 = mvd._multivalue_dict.get("key2")
        self.assertEqual(result1, {"member1-1", "member1-2"})
        self.assertEqual(result2, {"member2-1"})

    def test_ADD_fail(self):
        mvd = multivalue_dict.MultiValueDictionary()
        mvd._multivalue_dict["key1"] = {"member1-1"}
        result = mvd.ADD("key1", "member1-1")
        self.assertIsNone(result)

    def test_ADDMANY_success_new(self):
        mvd = multivalue_dict.MultiValueDictionary()
        mvd.ADDMANY("key1", "member1-1", "member1-2")
        result = mvd._multivalue_dict.get("key1")
        self.assertEqual(result, {"member1-1", "member1-2"})

    def test_ADDMANY_success_partial(self):
        mvd = multivalue_dict.MultiValueDictionary()
        mvd._multivalue_dict["key1"] = {"member1-1"}
        mvd.ADDMANY("key1", "member1-1", "member1-2")
        result = mvd._multivalue_dict.get("key1")
        self.assertEqual(result, {"member1-1", "member1-2"})

    def test_ADDMANY_fail(self):
        mvd = multivalue_dict.MultiValueDictionary()
        mvd._multivalue_dict["key1"] = {"member1-1", "member1-2"}
        result = mvd.ADDMANY("key1", "member1-1", "member1-2")
        self.assertIsNone(result)

    def test_KEYS_empty(self):
        mvd = multivalue_dict.MultiValueDictionary()
        result = mvd.KEYS()
        self.assertIsNone(result)

    def test_KEYS_not_empty(self):
        mvd = multivalue_dict.MultiValueDictionary()
        mvd._multivalue_dict["key1"] = {"member1-1", "member1-2"}
        mvd._multivalue_dict["key2"] = {"member2-1"}
        result = mvd.KEYS()
        self.assertEqual(result, {"key1", "key2"})

    def test_MEMBERS_success(self):
        mvd = multivalue_dict.MultiValueDictionary()
        mvd._multivalue_dict["key1"] = {"member1-1", "member1-2"}
        mvd._multivalue_dict["key2"] = {"member2-1"}
        result = mvd.MEMBERS("key1")
        self.assertEqual(result, {"member1-1", "member1-2"})

    def test_MEMBERS_fail(self):
        mvd = multivalue_dict.MultiValueDictionary()
        mvd._multivalue_dict["key1"] = {"member1-1", "member1-2"}
        mvd._multivalue_dict["key2"] = {"member2-1"}
        result = mvd.MEMBERS("key3")
        self.assertIsNone(result)

    def test_REMOVE_success(self):
        mvd = multivalue_dict.MultiValueDictionary()
        mvd._multivalue_dict["key1"] = {"member1-1", "member1-2"}
        mvd._multivalue_dict["key2"] = {"member2-1"}
        mvd.REMOVE("key1", "member1-1")
        result = mvd._multivalue_dict.get("key1")
        self.assertEqual(result, {"member1-2"})

    def test_REMOVE_success_last(self):
        mvd = multivalue_dict.MultiValueDictionary()
        mvd._multivalue_dict["key1"] = {"member1-1", "member1-2"}
        mvd._multivalue_dict["key2"] = {"member2-1"}
        mvd.REMOVE("key2", "member2-1")
        result = mvd._multivalue_dict.keys()
        self.assertEqual(result, {"key1"})

    def test_REMOVE_fail_key(self):
        mvd = multivalue_dict.MultiValueDictionary()
        mvd._multivalue_dict["key1"] = {"member1-1", "member1-2"}
        mvd._multivalue_dict["key2"] = {"member2-1"}
        result = mvd.REMOVE("key3", "member3-1")
        self.assertIsNone(result)

    def test_REMOVE_fail_member(self):
        mvd = multivalue_dict.MultiValueDictionary()
        mvd._multivalue_dict["key1"] = {"member1-1", "member1-2"}
        mvd._multivalue_dict["key2"] = {"member2-1"}
        result = mvd.REMOVE("key2", "member2-2")
        self.assertIsNone(result)

    def test_REMOVEALL_success(self):
        mvd = multivalue_dict.MultiValueDictionary()
        mvd._multivalue_dict["key1"] = {"member1-1", "member1-2"}
        mvd._multivalue_dict["key2"] = {"member2-1"}
        mvd.REMOVEALL("key1")
        result = mvd._multivalue_dict.keys()
        self.assertEqual(result, {"key2"})

    def test_REMOVEALL_fail(self):
        mvd = multivalue_dict.MultiValueDictionary()
        mvd._multivalue_dict["key1"] = {"member1-1", "member1-2"}
        mvd._multivalue_dict["key2"] = {"member2-1"}
        result = mvd.REMOVEALL("key3")
        self.assertIsNone(result)

    def test_CLEAR_empty(self):
        mvd = multivalue_dict.MultiValueDictionary()
        mvd.CLEAR()
        result = mvd._multivalue_dict
        self.assertEqual(result, {})

    def test_CLEAR_not_empty(self):
        mvd = multivalue_dict.MultiValueDictionary()
        mvd._multivalue_dict["key1"] = {"member1-1", "member1-2"}
        mvd._multivalue_dict["key2"] = {"member2-1"}
        mvd.CLEAR()
        result = mvd._multivalue_dict
        self.assertEqual(result, {})

    def test_KEYEXISTS_success(self):
        mvd = multivalue_dict.MultiValueDictionary()
        mvd._multivalue_dict["key1"] = {"member1-1", "member1-2"}
        result = mvd.KEYEXISTS("key1")
        self.assertEqual(result, True)

    def test_KEYEXISTS_fail(self):
        mvd = multivalue_dict.MultiValueDictionary()
        mvd._multivalue_dict["key1"] = {"member1-1", "member1-2"}
        result = mvd.KEYEXISTS("key2")
        self.assertEqual(result, False)

    def test_MEMBEREXISTS_success(self):
        mvd = multivalue_dict.MultiValueDictionary()
        mvd._multivalue_dict["key1"] = {"member1-1", "member1-2"}
        result = mvd.MEMBEREXISTS("key1", "member1-2")
        self.assertEqual(result, True)

    def test_MEMBEREXISTS_fail_key(self):
        mvd = multivalue_dict.MultiValueDictionary()
        mvd._multivalue_dict["key1"] = {"member1-1", "member1-2"}
        result = mvd.MEMBEREXISTS("key2", "member2-1")
        self.assertEqual(result, False)

    def test_MEMBEREXISTS_fail_member(self):
        mvd = multivalue_dict.MultiValueDictionary()
        mvd._multivalue_dict["key1"] = {"member1-1", "member1-2"}
        result = mvd.MEMBEREXISTS("key1", "member2-1")
        self.assertEqual(result, False)

    def test_ALLMEMBERS_empty(self):
        mvd = multivalue_dict.MultiValueDictionary()
        result = mvd.ALLMEMBERS()
        self.assertIsNone(result)

    def test_ALLMEMBERS_not_empty(self):
        mvd = multivalue_dict.MultiValueDictionary()
        mvd._multivalue_dict["key1"] = {"member1-1", "member1-2"}
        mvd._multivalue_dict["key2"] = {"member2-1", "member1-2"} #Create a duplicate members, since return should be a list
        result = mvd.ALLMEMBERS()
        self.assertEqual(sorted(result), sorted(["member1-1", "member1-2", "member2-1", "member1-2"])) #Sort lists since order is not guaranteed from creation

    def test_ITEMS_empty(self):
        mvd = multivalue_dict.MultiValueDictionary()
        result = mvd.ITEMS()
        self.assertIsNone(result)

    def test_ITEMS_not_empty(self):
        mvd = multivalue_dict.MultiValueDictionary()
        mvd._multivalue_dict["key1"] = {"member1-1", "member1-2"}
        mvd._multivalue_dict["key2"] = {"member2-1"}
        result = mvd.ITEMS()
        self.assertEqual(result, {("key1", "member1-1"), ("key1", "member1-2"), ("key2", "member2-1")})

if __name__ == "__main__":
    unittest.main()