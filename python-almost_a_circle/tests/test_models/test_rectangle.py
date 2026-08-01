#!/usr/bin/python3
"""Unittest for Rectangle class"""
import unittest
import io
import os
import sys
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """Tests for Rectangle"""

    def test_two_args(self):
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)

    def test_three_args(self):
        r = Rectangle(1, 2, 3)
        self.assertEqual(r.x, 3)

    def test_four_args(self):
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.y, 4)

    def test_five_args(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.id, 5)

    def test_width_string(self):
        with self.assertRaises(TypeError) as e:
            Rectangle("1", 2)
        self.assertEqual(str(e.exception), "width must be an integer")

    def test_height_string(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(1, "2")
        self.assertEqual(str(e.exception), "height must be an integer")

    def test_x_string(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(1, 2, "3")
        self.assertEqual(str(e.exception), "x must be an integer")

    def test_y_string(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(1, 2, 3, "4")
        self.assertEqual(str(e.exception), "y must be an integer")

    def test_width_negative(self):
        with self.assertRaises(ValueError) as e:
            Rectangle(-1, 2)
        self.assertEqual(str(e.exception), "width must be > 0")

    def test_height_negative(self):
        with self.assertRaises(ValueError) as e:
            Rectangle(1, -2)
        self.assertEqual(str(e.exception), "height must be > 0")

    def test_width_zero(self):
        with self.assertRaises(ValueError) as e:
            Rectangle(0, 2)
        self.assertEqual(str(e.exception), "width must be > 0")

    def test_height_zero(self):
        with self.assertRaises(ValueError) as e:
            Rectangle(1, 0)
        self.assertEqual(str(e.exception), "height must be > 0")

    def test_x_negative(self):
        with self.assertRaises(ValueError) as e:
            Rectangle(1, 2, -3)
        self.assertEqual(str(e.exception), "x must be >= 0")

    def test_y_negative(self):
        with self.assertRaises(ValueError) as e:
            Rectangle(1, 2, 3, -4)
        self.assertEqual(str(e.exception), "y must be >= 0")

    def test_area(self):
        self.assertEqual(Rectangle(3, 2).area(), 6)

    def test_str(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_display_no_x_no_y(self):
        captured = io.StringIO()
        sys.stdout = captured
        Rectangle(2, 2).display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "##\n##\n")

    def test_display_no_y(self):
        captured = io.StringIO()
        sys.stdout = captured
        Rectangle(2, 2, 1).display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), " ##\n ##\n")

    def test_display_x_y(self):
        captured = io.StringIO()
        sys.stdout = captured
        Rectangle(2, 2, 1, 1).display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "\n ##\n ##\n")

    def test_to_dictionary(self):
        r = Rectangle(10, 2, 1, 9, 5)
        expected = {'id': 5, 'width': 10, 'height': 2, 'x': 1, 'y': 9}
        self.assertEqual(r.to_dictionary(), expected)

    def test_update_no_args(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update()
        self.assertEqual(str(r), "[Rectangle] (10) 10/10 - 10/10")

    def test_update_id(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        self.assertEqual(r.id, 89)

    def test_update_id_width(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 1)
        self.assertEqual(r.width, 1)

    def test_update_id_width_height(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 1, 2)
        self.assertEqual(r.height, 2)

    def test_update_id_width_height_x(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 1, 2, 3)
        self.assertEqual(r.x, 3)

    def test_update_all_args(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 1, 2, 3, 4)
        self.assertEqual(str(r), "[Rectangle] (89) 3/4 - 1/2")

    def test_update_kwargs_id(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(**{'id': 89})
        self.assertEqual(r.id, 89)

    def test_update_kwargs_id_width(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(**{'id': 89, 'width': 1})
        self.assertEqual(r.width, 1)

    def test_update_kwargs_id_width_height(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(r.height, 2)

    def test_update_kwargs_id_width_height_x(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(r.x, 3)

    def test_update_kwargs_all(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(str(r), "[Rectangle] (89) 3/4 - 1/2")

    def test_create_id(self):
        r = Rectangle.create(**{'id': 89})
        self.assertEqual(r.id, 89)

    def test_create_id_width(self):
        r = Rectangle.create(**{'id': 89, 'width': 1})
        self.assertEqual(r.width, 1)

    def test_create_id_width_height(self):
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(r.height, 2)

    def test_create_id_width_height_x(self):
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(r.x, 3)

    def test_create_all(self):
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2,
                                'x': 3, 'y': 4})
        self.assertEqual(str(r), "[Rectangle] (89) 3/4 - 1/2")

    def test_save_to_file_none(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_rectangle(self):
        Rectangle.save_to_file([Rectangle(1, 2)])
        with open("Rectangle.json", "r") as f:
            self.assertIn('"width": 1', f.read())

    def test_load_from_file_no_file(self):
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file_exists(self):
        r1 = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([r1])
        output = Rectangle.load_from_file()
        self.assertEqual(str(output[0]), str(r1))


if __name__ == '__main__':
    unittest.main()
