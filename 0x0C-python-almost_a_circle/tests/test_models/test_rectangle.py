#!/usr/bin/python3

"""Test cases for Rectangle class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
import io, sys



class Test_Rectangle_Instantiation(unittest.TestCase):
    """Test the instantiation of Rectangle class"""

    def test_inheritance(self):
        rect = Rectangle(10, 5, 0, 0, 7)
        self.assertIsInstance(rect, Base)

    def test_width_getter(self):
        rect = Rectangle(10, 5, 0, 0, 7)
        self.assertEqual(10, rect.width)

    def test_id_getter(self):
        rect = Rectangle(10, 5, 0, 0, 7)
        self.assertEqual(7, rect.id)

    def test_height_getter(self):
        rect = Rectangle(10, 5, 0, 0, 7)
        self.assertEqual(5, rect.height)

    def test_x_getter(self):
        rect = Rectangle(10, 5, 0, 0, 7)
        self.assertEqual(0, rect.x)

    def test_y_getter(self):
        rect = Rectangle(10, 5, 0, 0, 7)
        self.assertEqual(0, rect.y)

    def test_width_setter(self):
        rect = Rectangle(2, 5, 0, 0, 4)
        rect.width = 10
        self.assertEqual(10, rect.width)

    def test_height_setter(self):
        rect = Rectangle(2, 5, 0, 0, 4)
        rect.height = 10
        self.assertEqual(10, rect.height)

    def test_x_setter(self):
        rect = Rectangle(2, 5, 0, 0, 4)
        rect.x = 2
        self.assertEqual(2, rect.x)

    def test_y_setter(self):
        rect = Rectangle(2, 5, 0, 0, 4)
        rect.y = 4
        self.assertEqual(4, rect.y)

    def test_id_setter(self):
        rect = Rectangle(2, 5, 0, 0, 4)
        rect.id = 7
        self.assertEqual(7, rect.id)


class Test_str_method(unittest.TestCase):
    """Tests the __str__ method"""

    def test_correct_str_output(self):
        rect = Rectangle(10, 5, 0, 0, 7)
        expected = "[Rectangle] (7) 0/0 - 10/5"
        self.assertEqual(expected, rect.__str__())

    def test_str_method_extra_arg(self):
        rect = Rectangle(10, 5, 0, 0, 7)
        with self.assertRaises(TypeError):
            rect.__str__(1)


class Test_area_method(unittest.TestCase):
    """Tests the area method"""
    def test_correct_area_output(self):
        rect = Rectangle(10, 5)
        self.assertEqual(50, rect.area())

    def test_error_area_output(self):
        rect = Rectangle(10, 5)
        with self.assertRaises(TypeError):
            rect.area(1)


class Test_display_method(unittest.TestCase):
    """Tests the display method"""

    @staticmethod
    def get_stdout(rect, method):
        """Get output printed to stdout"""
        output = io.StringIO()
        sys.stdout = output
        if method == "display":
            rect.display()
        sys.stdout = sys.__stdout__
        return output

    def test_correct_display_output(self):
        rect = Rectangle(3, 2)
        output = Test_display_method.get_stdout(rect, "display")
        expected = "###\n###\n"
        self.assertEqual(expected, output.getvalue())

    def test_correct_display_output_2(self):
        rect = Rectangle(5, 3, 1, 1, 13)
        output = Test_display_method.get_stdout(rect, "display")
        expected = "\n #####\n #####\n #####\n"
        self.assertEqual(expected, output.getvalue())

    def test_display_exception(self):
        rect = Rectangle(4, 2, 0, 0, 2)
        with self.assertRaises(TypeError):
            rect.display(1)


if __name__ == "__main__":
    unittest.main()
