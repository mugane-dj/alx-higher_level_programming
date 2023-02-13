#!/usr/bin/python5
"""Test cases for Base class"""
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
import os


class Test_Base_Instantiation(unittest.TestCase):
    """Testing the instantiation of the Base class"""

    def test_none_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_no_id_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_unique_id_arg(self):
        b1 = Base(2)
        self.assertEqual(2, b1.id)

    def test_two_unique_args(self):
        with self.assertRaises(TypeError):
            Base(2, 4)

    def test_str_arg(self):
        b1 = Base("Jasper")
        self.assertEqual("Jasper", b1.id)

    def test_float_arg(self):
        b1 = Base(5.5)
        self.assertEqual(5.5, b1.id)

    def test_bool_arg(self):
        b1 = Base(True)
        self.assertEqual(True, b1.id)


class Test_to_json_string(unittest.TestCase):
    """Tests the to_json_string static method of Base class"""
    def test_to_json_string_rectangle_instance(self):
        r1 = Rectangle(6, 4, 2, 3)
        dictionary = r1.to_dictionary()
        json_dict = Base.to_json_string(dictionary)
        self.assertEqual(str, type(json_dict))

    def test_to_json_string_square_instance(self):
        s = Square(10, 4, 6, 2)
        dict_s = s.to_dictionary()
        json_dict = Base.to_json_string(dict_s)
        self.assertEqual(str, type(json_dict))

    def test_to_json_string_non_arg(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_no_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_more_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 4)


class Test_save_to_file(unittest.TestCase):
    """Tests the save_to_file class method"""

    def test_save_to_file_none_arg(self):
        Base.save_to_file(None)

        with open("Base.json", "r", encoding="utf-8") as f:
            read_data = f.read()

        self.assertEqual("[]", read_data)

    def test_save_to_file_empty_list(self):
        Base.save_to_file([])
        with open("Base.json", "r", encoding="utf-8") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_no_arg(self):
        with self.assertRaises(TypeError):
            Base.save_to_file()

    def test_save_to_file_extra_arg(self):
        with self.assertRaises(TypeError):
            Base.save_to_file([], "hello")

    def test_exceptions(self):
        try:
            os.remove("Base.json")
        except IOError:
            pass


class Test_from_json_string(unittest.TestCase):
    """Tests the from_json_string static method"""

    def test_from_json_string_rectangle_instance(self):
        list_input = [{"id": 4, "width": 6, "height": 4}]
        to_json = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(to_json)
        self.assertEqual(list, type(list_output))

    def test_from_json_string_square_instance(self):
        list_input = [{"id": 6, "size": 4}]
        to_json = Square.to_json_string(list_input)
        list_output = Square.from_json_string(to_json)
        self.assertEqual(list, type(list_output))

    def test_from_json_string_none_arg(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_string_empty_list(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_string_no_arg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_more_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], "world")


class Test_create(unittest.TestCase):
    """Tests the create class method"""
    def test_create_rect_instance(self):
        rect_1 = Rectangle(10, 6, 0, 0, 8)
        rect_1_dict = rect_1.to_dictionary()
        rect_2 = Rectangle.create(**rect_1_dict)
        self.assertNotEqual(rect_1, rect_2)

    def test_create_rect_instance_2(self):
        rect_1 = Rectangle(10, 6, 0, 0, 8)
        rect_1_dict = rect_1.to_dictionary()
        rect_2 = Rectangle.create(**rect_1_dict)
        self.assertIsNot(rect_1, rect_2)

    def test_create_dummy_square(self):
        s1 = Square(4, 1, 1, 8)
        s1_dict = s1.to_dictionary()
        s2 = Square.create(**s1_dict)
        self.assertNotEqual(s1, s2)

    def test_create_dummy_square_2(self):
        s1 = Square(4, 1, 1, 8)
        s1_dict = s1.to_dictionary()
        s2 = Square.create(**s1_dict)
        self.assertIsNot(s1, s2)


class Test_load_from_file(unittest.TestCase):
    """Tests the load_from_file class method"""

    def test_load_from_file_rect_instance(self):
        rect_1 = Rectangle(10, 6, 2, 3, 8)
        rect_2 = Rectangle(8, 7, 0, 0, 12)

        Rectangle.save_to_file([rect_1, rect_2])
        self.assertEqual(str(rect_1), str(Rectangle.load_from_file()[0]))

    def test_load_from_file_rect_instance_2(self):
        rect_1 = Rectangle(10, 6, 2, 3, 8)
        rect_2 = Rectangle(8, 7, 0, 0, 12)

        Rectangle.save_to_file([rect_1, rect_2])
        self.assertEqual(str(rect_2), str(Rectangle.load_from_file()[1]))

    def test_load_from_file_square_instance(self):
        s1 = Square(4, 0, 0, 3)
        s2 = Square(6, 2, 2, 4)

        Square.save_to_file([s1, s2])
        self.assertEqual(str(s1), str(Square.load_from_file()[0]))

    def test_load_from_file_square_instance_2(self):
        s1 = Square(4, 0, 0, 3)
        s2 = Square(6, 2, 2, 4)

        Square.save_to_file([s1, s2])
        self.assertEqual(str(s2), str(Square.load_from_file()[1]))

    def test_load_from_file_extra_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], "load")

    def test_exceptions(self):
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
