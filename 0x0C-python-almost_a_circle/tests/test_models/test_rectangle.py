#!/usr/bin/python3
"""[Test module for the 'Base' class]
"""


import unittest, io
from models.base import Base
from models.rectangle import Rectangle
from contextlib import redirect_stdout

class testRectangle(unittest.TestCase):
        """[Define the test for Rectangle class]
        """

        def test_id(self):
                res = Rectangle(10, 2)
                self.assertEqual(res.id, 1)