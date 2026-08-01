#!/usr/bin/python3
"""Unittests for the Rectangle class."""
import unittest
import io
import sys
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle class."""

    def test_is_base(self):
        self.assertIsInstance(Rectangle(1, 1), Base)

    def test_attributes(self):
        r = Rectangle(10, 2, 3, 4, 5)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)
        self.assertEqual(r.id, 5)

    def test_default_x_y(self):
        r = Rectangle(1, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_width_not_int(self):
        with self.assertRaises(TypeError):
            Rectangle("10", 2)

    def test_height_not_int(self):
        with self.assertRaises(TypeError):
            Rectangle(10, "2")

    def test_x_not_int(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 2, {})

    def test_y_not_int(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 3, "4")

    def test_width_zero(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_width_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(-10, 2)

    def test_height_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(10, -2)

    def test_x_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(10, 2, -3)

    def test_y_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 3, -1)

    def test_area(self):
        self.assertEqual(Rectangle(3, 2).area(), 6)
        self.assertEqual(Rectangle(8, 7).area(), 56)

    def test_str(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_display(self):
        captured = io.StringIO()
        sys.stdout = captured
        Rectangle(2, 2).display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "##\n##\n")

    def test_display_x_y(self):
        captured = io.StringIO()
        sys.stdout = captured
        Rectangle(2, 2, 1, 1).display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "\n ##\n ##\n")

    def test_update_args(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_kwargs(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(height=1, width=2, x=3, y=4, id=89)
        self.assertEqual(str(r), "[Rectangle] (89) 3/4 - 2/1")

    def test_update_args_priority(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89, height=1)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.height, 10)

    def test_to_dictionary(self):
        r = Rectangle(10, 2, 1, 9, 5)
        expected = {'id': 5, 'width': 10, 'height': 2, 'x': 1, 'y': 9}
        self.assertEqual(r.to_dictionary(), expected)
        self.assertEqual(type(r.to_dictionary()), dict)


if __name__ == '__main__':
    unittest.main()
