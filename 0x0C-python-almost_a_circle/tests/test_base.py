#!/usr/bin/python3
""""""

import unittest
import pep8
import inspect
import json

from models.base import Base


class TestBasePepDocs(unittest.TestCase):
    """Tests to check docs and style of Base class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.funcs = inspect.getmembers(Base, inspect.isfunction)


    def test_module_docstring(self):
        """Tests for the module docstring

        Args:
            None

        Returns:
            None
        """
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests for the Base class docstring

        Args:
            None

        Returns:
            None
        """
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_func_docstrings(self):
        """Tests for the docstrings in all functions

         Args:
             None

         Returns:
             None
         """
        for func in self.funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)


class TestBase(unittest.TestCase):
    """Tests to check functionality of Base class"""


    def test_no_id(self):
        """Tests id as None
        Args:
            None

        Returns:
            None
        """
        base = Base()
        self.assertEqual(base.id, 1)

    def test_id_set(self):
        """Tests id as not None
        Args:
            None

        Returns:
            None
        """
        base = Base(100)
        self.assertEqual(base.id, 100)

    def test_no_id_after_set(self):
        """Tests id as None after not None
        Args:
            None

        Returns:
            None
        """
        base2 = Base()
        self.assertEqual(base2.id, 2)



    def test_to_json_string_empty(self):
        """Check for passing empty list/ None
        Args:
            None

        Returns:
            None
        """
        json_s = Base.to_json_string([])
        self.assertTrue(type(json_s) is str)
        self.assertEqual(json_s, "[]")

    def test_to_json_String_None(self):
        """Tests to_json_string Empty
        Args:
            None

        Returns:
            None
        """
        json_s = Base.to_json_string(None)
        self.assertTrue(type(json_s) is str)
        self.assertEqual(json_s, "[]")

    def test_from_json_string_empty(self):
        """Tests from_json_string with an empty string
        Args:
            None

        Returns:
            None
        """
        self.assertEqual([], Base.from_json_string(""))

    def test_from_json_string_None(self):
        """Tests from_json_string with an empty string
        Args:
            None

        Returns:
            None
        """
        self.assertEqual([], Base.from_json_string(None))
