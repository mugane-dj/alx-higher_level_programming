#!/usr/bin/python3

"""Defines Test cases for Square class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import io
import sys


class TestSquare_instantiation(unittest.TestCase):
    """Test the instantiation of Square class"""

    def test_inheritance_to_rectangle(self):
        s = Square(10, 0, 0, 5)
        self.assertIsInstance(s, Rectangle)

    def test_inheritance_to_base(self):
        s = Square(4, 1, 1, 3)
        self.assertIsInstance(s, Base)

    def test_size_getter(self):
        s = Square(10, 0, 0, 5)
        self.assertEqual(10, s.size)

    def test_size_setter(self):
        s = Square(10, 0, 0, 5)
        s.size = 12
        self.assertEqual(12, s.size)


class Test_size_attribute(unittest.TestCase):
    """Test the behavior of size attribute"""
    def test_size_none(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None, 0, 0, 7)

    def test_size_float(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(1.5, 2, 2, 4)

    def test_size_list(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([3, 4], 1, 1, 5)

    def test_size_str(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("size", 1, 3, 2)

    def test_size_dict(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({"size": 10}, 2, 2, 6)

    def test_size_tuple(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((1, 2), 4, 6, 8)


class Test_str_method(unittest.TestCase):
    """Test the __str__ method"""

    def test_str_correct_output(self):
        s = Square(10, 0, 0, 5)
        expected = "[Square] (5) 0/0 - 10"
        self.assertEqual(str(s), expected)

    def test_str_extra_arg(self):
        s = Square(10, 0, 0, 5)
        with self.assertRaises(TypeError):
            s.__str__(1)


class Test_to_dictionary(unittest.TestCase):
    """Tests the to_dictionary method"""

    def test_to_dictionary_correct(self):
        s = Square(10, 2, 2, 7)
        expected = {
            "id": 7,
            "size": 10,
            "x": 2,
            "y": 2,
        }
        self.assertEqual(expected, s.to_dictionary())

    def test_to_dictionary_error(self):
        s = Square(10, 2, 2, 7)
        expected = {
            "id": 10,
            "size": 2,
            "x": 2,
            "y": 7
        }
        self.assertNotEqual(expected, s.to_dictionary())

    def test_to_dictionary_extra_arg(self):
        s = Square(10, 5, 2, 7)
        with self.assertRaises(TypeError):
            s.to_dictionary(1)


class Test_update(unittest.TestCase):
    """Tests the update method"""

    def test_update_args(self):
        s = Square(6, 4, 4, 6)
        s.update(10)
        self.assertEqual(str(s), "[Square] (10) 4/4 - 6")

    def test_update_no_args_kwargs(self):
        s = Square(6, 4, 4, 6)
        s.update()
        self.assertEqual(str(s), "[Square] (6) 4/4 - 6")

    def test_update_kwargs(self):
        s = Square(6, 4, 4, 6)
        s.update(id=5, size=5, x=1, y=1)
        self.assertEqual(str(s), "[Square] (5) 1/1 - 5")


if __name__ == "__main__":
    unittest.main()
