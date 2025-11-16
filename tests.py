import unittest
import os
import tempfile
from fields import Phone, Name
from record import Record
from address_book import AddressBook
from storage import save_data, load_data
from main import handle_add, handle_change, handle_phone, handle_show_all


class TestPhone(unittest.TestCase):

    def test_valid_phone(self):
        p = Phone("0931234567")
        self.assertEqual(p.value, "0931234567")

    def test_phone_not_digits(self):
        with self.assertRaises(ValueError):
            Phone("09312abcde")

    def test_phone_too_short(self):
        with self.assertRaises(ValueError):
            Phone("12345")

    def test_phone_too_long(self):
        with self.assertRaises(ValueError):
            Phone("093123456789")


class TestRecord(unittest.TestCase):

    def test_add_phone(self):
        r = Record(Name("Alex"))
        r.add_phone(Phone("0931234567"))
        self.assertEqual(len(r.phones), 1)

    def test_edit_phone(self):
        r = Record(Name("Alex"))
        r.add_phone(Phone("0931234567"))
        r.edit_phone("0931234567", "0509876543")
        self.assertEqual(r.phones[0].value, "0509876543")

    def test_remove_phone(self):
        r = Record(Name("Alex"))
        r.add_phone(Phone("0931234567"))
        removed = r.remove_phone("0931234567")
        self.assertTrue(removed)
        self.assertEqual(len(r.phones), 0)


class TestAddressBook(unittest.TestCase):

    def test_add_and_get_record(self):
        book = AddressBook()
        r = Record(Name("Alex"))
        r.add_phone(Phone("0931234567"))
        book.add_record(r)
        self.assertEqual(book.get("Alex").name.value, "Alex")

    def test_delete_record(self):
        book = AddressBook()
        r = Record(Name("Alex"))
        book.add_record(r)
        book.delete("Alex")
        self.assertIsNone(book.get("Alex"))


class TestCommands(unittest.TestCase):

    def test_handle_add_success(self):
        book = AddressBook()
        result = handle_add(["Alex", "0931234567"], book)
        self.assertIn("added", result.lower())

    def test_handle_add_invalid_phone(self):
        book = AddressBook()
        result = handle_add(["Alex", "12345"], book)
        self.assertIn("error", result.lower())

    def test_handle_change_success(self):
        book = AddressBook()
        handle_add(["Alex", "0931234567"], book)
        result = handle_change(["Alex", "0509876543"], book)
        self.assertIn("updated", result.lower())

    def test_handle_change_invalid(self):
        book = AddressBook()
        handle_add(["Alex", "0931234567"], book)
        result = handle_change(["Alex", "12345"], book)
        self.assertIn("error", result.lower())

    def test_handle_phone_found(self):
        book = AddressBook()
        handle_add(["Alex", "0931234567"], book)
        result = handle_phone(["Alex"], book)
        self.assertIn("0931234567", result)

    def test_handle_phone_not_found(self):
        book = AddressBook()
        result = handle_phone(["Unknown"], book)
        self.assertIn("not found", result.lower())

    def test_handle_show_all(self):
        book = AddressBook()
        handle_add(["Alex", "0931234567"], book)
        result = handle_show_all(book)
        self.assertIn("0931234567", result)


class TestStorage(unittest.TestCase):

    def test_save_and_load(self):
        with tempfile.TemporaryDirectory() as tmp:
            filename = os.path.join(tmp, "test.pkl")

            book = AddressBook()
            handle_add(["Alex", "0931234567"], book)

            save_data(book, filename)
            loaded = load_data(filename)

            self.assertEqual(
                loaded.get("Alex").phones[0].value,
                "0931234567"
            )


class TestFullFlow(unittest.TestCase):

    def test_full_integration(self):
        """
        Повний сценарій:
        add → change → phone → save → load
        """
        with tempfile.TemporaryDirectory() as tmp:
            filename = os.path.join(tmp, "full.pkl")

            book = AddressBook()

            # ADD
            self.assertIn("added", handle_add(["Alex", "0931234567"], book).lower())

            # CHANGE
            self.assertIn("updated", handle_change(["Alex", "0509876543"], book).lower())

            # PHONE
            result = handle_phone(["Alex"], book)
            self.assertIn("0509876543", result)

            # SAVE
            save_data(book, filename)

            # LOAD
            restored = load_data(filename)
            rec = restored.get("Alex")
            self.assertEqual(rec.phones[0].value, "0509876543")


if __name__ == "__main__":
    tests.main()
