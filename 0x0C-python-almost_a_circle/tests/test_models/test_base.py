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

    def test_save_to_file_no_arg(self):
        with self.assertRaises(TypeError):
            Base.save_to_file()

    def test_save_to_file_extra_arg(self):
         with self.assertRaises(TypeError):
            Base.save_to_file([], "hello")

    def test_exceptions(self):
        try:
            os.remove("Square.json")
        except IOError:
            pass
