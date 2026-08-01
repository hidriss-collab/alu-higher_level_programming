#!/usr/bin/python3
"""Unittests for the Square class."""
import unittest
from models.square import Square
from models.rectangle import Rectangle


class TestSquare(unittest.TestCase):
    """Test cases for Square class."""

    def test_is_rectangle(self):
        self.assertIsInstance(Square(1), Rectangle)

    def test_attributes(self):
        s = Square(5, 2, 3, 62)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 62)

    def test_width_equals_height(self):
        s = Square(4)
        self.assertEqual(s.width, s.height)

    def test_str(self):
        s = Square(5, 0, 0, 1)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 5")

    def test_size_not_int(self):
        with self.assertRaises(TypeError) as e:
            Square("9")
        self.assertEqual(str(e.exception), "width must be an integer")

    def test_size_negative(self):
        with self.assertRaises(ValueError):
            Square(-5)

    def test_size_zero(self):
        with self.assertRaises(ValueError):
            Square(0)

    def test_size_setter(self):
        s = Square(5)
        s.size = 10
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_size_setter_invalid(self):
        s = Square(5)
        with self.assertRaises(TypeError):
            s.size = "9"

    def test_area(self):
        self.assertEqual(Square(5).area(), 25)

    def test_update_args(self):
        s = Square(5, 0, 0, 1)
        s.update(1, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (1) 3/4 - 2")

    def test_update_kwargs(self):
        s = Square(5, 0, 0, 1)
        s.update(size=7, y=1, id=89)
        self.assertEqual(str(s), "[Square] (89) 0/1 - 7")

    def test_to_dictionary(self):
        s = Square(10, 2, 1, 5)
        expected = {'id': 5, 'size': 10, 'x': 2, 'y': 1}
        self.assertEqual(s.to_dictionary(), expected)
        self.assertEqual(type(s.to_dictionary()), dict)


if __name__ == '__main__':
    unittest.main()
