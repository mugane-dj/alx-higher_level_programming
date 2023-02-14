#!/usr/bin/python3

"""Test cases for Rectangle class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
import io
import sys


class TestRectangle_Instantiation(unittest.TestCase):
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


class Test_width_attribute(unittest.TestCase):
    """Test the behavior of width attribute"""

    def test_width_none(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 6, 1, 1, 7)

    def test_width_float(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(5.6, 4, 2, 2, 5)

    def test_width_list(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([5, 6], 4, 2, 2, 5)

    def test_width_dict(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({5, 6}, 4, 2, 2, 5)

    def test_width_tuple(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((4, 2), 6, 1, 1, 7)

    def test_width_str(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("width", 10, 2, 3, 17)

    def test_width_negative(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-5, 4, 2, 2, 5)

    def test_width_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 4, 2, 2, 5)


class Test_height_attribute(unittest.TestCase):
    """Test the behavior of height attribute"""

    def test_height_none(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(6, None, 1, 1, 7)

    def test_height_float(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, 4.2, 2, 2, 5)

    def test_height_list(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, [6, 4], 2, 2, 5)

    def test_height_dict(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, {6, 4}, 2, 2, 5)

    def test_height_tuple(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, (2, 6), 1, 1, 7)

    def test_height_str(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, "height", 2, 3, 17)

    def test_height_negative(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(5, -4, 2, 2, 5)

    def test_height_zero(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(4, 0, 2, 2, 5)


class Test_x_attribute(unittest.TestCase):
    """Tests the x attribute"""

    def test_x_none(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 6, None, 1, 7)

    def test_x_float(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 4, 2.1, 2, 5)

    def test_x_list(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 4, [2, 1], 2, 5)

    def test_x_dict(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 6, {4, 2}, 2, 5)

    def test_x_tuple(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 2, (6, 1), 1, 7)

    def test_x_str(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 10, "x", 3, 17)

    def test_x_negative(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(5, 4, -2, 2, 5)


class Test_y_attribute(unittest.TestCase):
    """Tests the y attribute"""

    def test_y_none(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 6, 2, None, 7)

    def test_y_float(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 4, 2, 2.8, 5)

    def test_y_list(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 4, 2, [1, 2], 5)

    def test_y_dict(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 6, 4, {2, 2}, 5)

    def test_y_tuple(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 2, 6, (1, 1), 7)

    def test_y_str(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 10, 3, "y", 17)

    def test_y_negative(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(5, 4, 2, -2, 5)


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


class Test_to_dictionary(unittest.TestCase):
    """Tests the to_dictionary method"""

    def test_to_dictionary_correct(self):
        rect = Rectangle(10, 5, 2, 2, 7)
        expected = {
            "id": 7,
            "width": 10,
            "height": 5,
            "x": 2,
            "y": 2,
        }
        self.assertEqual(expected, rect.to_dictionary())

    def test_to_dictionary_error(self):
        rect = Rectangle(10, 5, 2, 2, 7)
        expected = {
            "id": 10,
            "width": 5,
            "height": 2,
            "x": 2,
            "y": 7
        }
        self.assertNotEqual(expected, rect.to_dictionary())

    def test_to_dictionary_extra_arg(self):
        rect = Rectangle(10, 5, 2, 2, 7)
        with self.assertRaises(TypeError):
            rect.to_dictionary(1)


class Test_update(unittest.TestCase):
    """Tests the update method"""

    def test_update_args(self):
        rect = Rectangle(2, 4, 0, 0, 6)
        rect.update(6, 2, 1, 1, 5)
        self.assertEqual(str(rect), "[Rectangle] (6) 1/5 - 2/1")

    def test_update_no_args(self):
        rect = Rectangle(10, 5, 5, 5, 10)
        rect.update()
        self.assertEqual(str(rect), "[Rectangle] (10) 5/5 - 10/5")

    def test_update_kwargs(self):
        rect = Rectangle(10, 5, 5, 5, 10)
        rect.update(id=5, width=5, height=5, x=1, y=1)
        self.assertEqual(str(rect), "[Rectangle] (5) 1/1 - 5/5")


if __name__ == "__main__":
    unittest.main()
