#!/usr/bin/python3
"""
This module is used in the testing
"""


import os
import unittest
from models.rectangle import Rectangle

class TestRect(unittest.TestCase):
    """
    This class focuses on the test of the class Rectangle
    """

    def test_input(self):
        """
        This will test
        """
        r = Rectangle("ME", 6)
        self.assertIsInstance()