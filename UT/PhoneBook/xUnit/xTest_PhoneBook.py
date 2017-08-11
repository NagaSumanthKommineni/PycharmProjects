import unittest

from xUnit.PhoneBook import PhoneBook


class Test_PhoneBooth(unittest.TestCase):

    def setUp(self):
        self.phonebook = PhoneBook()

    def test_lookup_entry_by_name(self):
        self.phonebook.add("mark", 978)
        self.assertEqual(978, self.phonebook.lookup("mark"))

    def test_missing_entry_raises_key_error(self):
        with self.assertRaises(KeyError):
            self.phonebook.lookup("missing")

    def test_look_up_names_and_numbers_in_phonebook(self):
        self.phonebook.add("abc", 123)
        self.assertIn("abc", self.phonebook.names())
        self.assertIn(123, self.phonebook.numbers())

    def test_empty_phonebook_is_consistent(self):
        self.assertTrue(self.phonebook.is_consistent())

    @unittest.skip("Not_Complete")
    def test_to_check_skip_report(self):
        pass

    def test_to_check_error_report(self):
        self.phonebook.add("abc", 123, "def")

    def test_to_check_failure_report(self):
        self.phonebook.add("mark", 9785642310)
        self.assertEqual(978, self.phonebook.lookup("mark"))

