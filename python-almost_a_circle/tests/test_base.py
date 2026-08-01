#!/usr/bin/python3
"""Unittests for the Base class."""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test cases for Base class."""

    def test_auto_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_given_id(self):
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_id_after_given(self):
        b1 = Base()
        b2 = Base(50)
        b3 = Base()
        self.assertEqual(b3.id, b1.id + 1)

    def test_to_json_string_none(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_valid(self):
        result = Base.to_json_string([{"id": 1}])
        self.assertEqual(type(result), str)

    def test_from_json_string_none(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        self.assertEqual(Base.from_json_string(""), [])

    def test_from_json_string_valid(self):
        result = Base.from_json_string('[{"id": 89}]')
        self.assertEqual(result, [{"id": 89}])

    def test_create_rectangle(self):
        r1 = Rectangle(3, 5, 1)
        r2 = Rectangle.create(**r1.to_dictionary())
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)

    def test_create_square(self):
        s1 = Square(3, 1, 2)
        s2 = Square.create(**s1.to_dictionary())
        self.assertEqual(str(s1), str(s2))

    def test_save_to_file_none(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_rectangle(self):
        r = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            self.assertIn("10", f.read())

    def test_load_from_file_not_exist(self):
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        self.assertEqual(Square.load_from_file(), [])

    def test_load_from_file_exist(self):
        r1 = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([r1])
        output = Rectangle.load_from_file()
        self.assertEqual(str(output[0]), str(r1))


if __name__ == '__main__':
    unittest.main()
