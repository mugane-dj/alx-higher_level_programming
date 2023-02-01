#!/usr/bin/python3

"""Unit tests for max integer module"""

import unittest
max_int = __import__('6-max_integer').max_integer

class TestMaxInt(unittest.TestCase):
    """Class containing all test case for max integer module"""

    def test_int_and_floats(self):
        self.assertEqual(max_int([5, 12, 78, 32]), 78)
        self.assertEqual(max_int([1]), 1)
        self.assertEqual(max_int([-24, 58, -72]), 58)
        self.assertEqual(max_int([-0.5, -3.4, -5.2]), -0.5)

    def test_string_chars(self):
        self.assertEqual(max_int(['a', 'b', 'c', 'd']), 'd')
        self.assertEqual(max_int("abcdef"), 'f')

    def test_lists(self):
        self.assertEqual(max_int([[5, 7], [3, 2]]), [5, 7])

    def test_none(self):
        self.assertEqual(max_int([]), None)
        self.assertEqual(max_int(), None)

    def test_errors(self):
        with self.assertRaises(TypeError):
            max_int([True, None])
        with self.assertRaises(TypeError):
            max_int({4, 7, 9, 10})

if __name__ == "__main__":
    unittest.main()
