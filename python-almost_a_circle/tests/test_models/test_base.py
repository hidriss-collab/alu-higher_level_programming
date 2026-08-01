#!/usr/bin/python3
"""Unittest for Base class"""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Tests for Base"""

    def test_auto_id(self):
        b = Base()
        self.assertIsInstance(b.id, int)

    def test_auto_id_increment(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_given_id(self):
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_to_json_string_none(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_dict(self):
        self.assertEqual(Base.to_json_string([{'id': 12}]), '[{"id": 12}]')

    def test_to_json_string_returns_string(self):
        self.assertEqual(type(Base.to_json_string([{'id': 12}])), str)

    def test_from_json_string_none(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string_valid(self):
        self.assertEqual(Base.from_json_string('[{ "id": 89 }]'),
                         [{"id": 89}])

    def test_from_json_string_returns_list(self):
        self.assertEqual(type(Base.from_json_string('[{ "id": 89 }]')),
                         list)


if __name__ == '__main__':
    unittest.main()
