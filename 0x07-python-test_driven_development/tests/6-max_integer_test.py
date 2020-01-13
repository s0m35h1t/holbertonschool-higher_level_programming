#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class MaxIntegerTest(unittest.TestCase):
    """Represents a Unitest fot max_integer
    Attributes:
        None
    """

    def test_module_docstring(self):
        """Check: module docsting"""
        m = __import__('6-max_integer').__doc__
        self.assertTrue(len(m) > 1)

    def test_function_docstring(self):
        """Check: funstion docstring"""
        f = max_integer.__doc__
        self.assertTrue(len(f) > 1)

    def test_no_args(self):
        """Check: no arguments passed to func"""
        self.assertIsNone(max_integer())

    def test_empty_list(self):
        """Check: empty list []"""
        l = []
        self.assertIsNone(max_integer(l))

    def test_max_at_end(self):
        """Check: all positive with max at end"""
        l = [12, 1, 18, 6, 14, 40]
        self.assertEqual(max_integer(l), 40)

    def test_two_of_max(self):
        """Check: all positive with max at end"""
        l = [12, 1, 40, 6, 14, 40]
        self.assertEqual(max_integer(l), 40)

    def test_none(self):
        """Check: passing none as argument"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_non_int_arg(self):
        """Check: a non-int type in list"""
        l = [1, "string", 3, 4, 5]
        with self.assertRaises(TypeError):
            max_integer(l)

    def test_one_element(self):
        """Check: only one number in the list"""
        l = [10]
        self.assertEqual(max_integer(l), 10)

    def test_max_at_beginning(self):
        """Check: all positive with max at beginning"""
        l = [130, 129, 23, 6, 0, 10]
        self.assertEqual(max_integer(l), 130)

    def test_max_at_middle(self):
        """Check: all positive with max in middle"""
        l = [1, 10, 23, 30, 14, 12]
        self.assertEqual(max_integer(l), 30)

    def test_one_negative(self):
        """Check: list with one negative number"""
        l = [10, -10, 1, 6, 4, 2]
        self.assertEqual(max_integer(l), 10)

    def test_all_10(self):
        """Check: all otems egual to 10"""
        l = [10, 10, 10, 10, 10, 10]
        self.assertEqual(max_integer(l), 10)

    def test_all_negative(self):
        """Check: list with all negative numbers"""
        l = [-1, -2, -3, -4, -5]
        self.assertEqual(max_integer(l), -1)


if __name__ == "__main__":
    unittest.main()
