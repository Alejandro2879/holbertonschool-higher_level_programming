#!/usr/bin/python3
"""[Test module for the 'Base' class]
"""


import unittest, json, pep8, inspect
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):

        def test_base_documentation(self):
                """[Test for modules and function documentation]
                """
                self.assertTrue(len(Base.__doc__) > 0)
                d_meth = inspect.getmembers(Base, predicate=inspect.ismethod)
                for name, method in d_meth:
                        self.assertTrue(len(method.__doc__) > 0)
                d_fun = inspect.getmembers(Base, predicate=inspect.isfunction)
                for name, method in d_fun:
                        self.assertTrue(len(method.__doc__) > 0)

        def test_Base_pep8(self):
                """[Test for pep8 style in Base class]
                """
                style = pep8.StyleGuide(quiet = True)
                res = style.check_files(['models/base.py'])
                self.assertEqual(res.total_errors, 0, "Found code style errors")