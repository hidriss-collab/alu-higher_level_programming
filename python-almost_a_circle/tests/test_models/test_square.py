#!/usr/bin/python3
"""Unittest for Square class"""
import unittest
import os
from models.square import Square
from models.rectangle import Rectangle


class TestSquare(unittest.TestCase):
    """Tests for Square"""

    def tearDown(self):
        """Remove created files after each test"""
        for f in ("Square.json", "Rectangle.json"):
            if os.path.exists(f):
                os.remove(f)

    def test_one_arg(self):
        s = Square(1)
        self.assertEqual(s.size, 1)

    def test_two_args(self):
        s = Square(1, 2)
        self.assertEqual(s.x, 2)

    def test_three_args(self):
        s = Square(1, 2, 3)
        self.assertEqual(s.y, 3)

    def test_four_args(self):
        s = Square(1, 2, 3, 4)
        self.assertEqual(s.id, 4)

    def test_size_string(self):
        with self.assertRaises(TypeError) as e:
            Square("1")
        self.assertEqual(str(e.exception), "width must be an integer")

    def test_x_string(self):
        with self.assertRaises(TypeError) as e:
            Square(1, "2")
        self.assertEqual(str(e.exception), "x must be an integer")

    def test_y_string(self):
        with self.assertRaises(TypeError) as e:
            Square(1, 2, "3")
        self.assertEqual(str(e.exception), "y must be an integer")

    def test_size_negative(self):
        with self.assertRaises(ValueError) as e:
            Square(-1)
        self.assertEqual(str(e.exception), "width must be > 0")

    def test_size_zero(self):
        with self.assertRaises(ValueError) as e:
            Square(0)
        self.assertEqual(str(e.exception), "width must be > 0")

    def test_x_negative(self):
        with self.assertRaises(ValueError) as e:
            Square(1, -2)
        self.assertEqual(str(e.exception), "x must be >= 0")

    def test_y_negative(self):
        with self.assertRaises(ValueError) as e:
            Square(1, 2, -3)
        self.assertEqual(str(e.exception), "y must be >= 0")

    def test_str(self):
        s = Square(5, 0, 0, 1)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 5")

    def test_to_dictionary(self):
        s = Square(10, 2, 1, 5)
        self.assertEqual(s.to_dictionary(),
                         {'id': 5, 'size': 10, 'x': 2, 'y': 1})

    def test_update_no_args(self):
        s = Square(5, 0, 0, 1)
        s.update()
        self.assertEqual(str(s), "[Square] (1) 0/0 - 5")

    def test_update_id(self):
        s = Square(5)
        s.update(89)
        self.assertEqual(s.id, 89)

    def test_update_id_size(self):
        s = Square(5)
        s.update(89, 1)
        self.assertEqual(s.size, 1)

    def test_update_id_size_x(self):
        s = Square(5)
        s.update(89, 1, 2)
        self.assertEqual(s.x, 2)

    def test_update_id_size_x_y(self):
        s = Square(5)
        s.update(89, 1, 2, 3)
        self.assertEqual(str(s), "[Square] (89) 2/3 - 1")

    def test_update_kwargs_id(self):
        s = Square(5)
        s.update(**{'id': 89})
        self.assertEqual(s.id, 89)

    def test_update_kwargs_id_size(self):
        s = Square(5)
        s.update(**{'id': 89, 'size': 1})
        self.assertEqual(s.size, 1)

    def test_update_kwargs_id_size_x(self):
        s = Square(5)
        s.update(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(s.x, 2)

    def test_update_kwargs_all(self):
        s = Square(5)
        s.update(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(str(s), "[Square] (89) 2/3 - 1")

    def test_create_id(self):
        s = Square.create(**{'id': 89})
        self.assertEqual(s.id, 89)

    def test_create_id_size(self):
        s = Square.create(**{'id': 89, 'size': 1})
        self.assertEqual(s.size, 1)

    def test_create_id_size_x(self):
        s = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(s.x, 2)

    def test_create_all(self):
        s = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(str(s), "[Square] (89) 2/3 - 1")

    def test_save_to_file_none(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_square(self):
        Square.save_to_file([Square(1)])
        with open("Square.json", "r") as f:
            self.assertIn('"size": 1', f.read())

    def test_load_from_file_no_file(self):
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        self.assertEqual(Square.load_from_file(), [])

    def test_load_from_file_exists(self):
        s1 = Square(5)
        Square.save_to_file([s1])
        output = Square.load_from_file()
        self.assertEqual(str(output[0]), str(s1))


if __name__ == '__main__':
    unittest.main()
