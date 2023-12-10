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

    def test_input_data_Types(self):
        """
        Tests the data types given to as input
        """
        # When input is string
        with self.assertRaises(TypeError):
            n = Rectangle("hello", "world")
        
        # Whne input is float
        with self.assertRaises(TypeError):
            n = Rectangle(5.4, 3.8)

        # x and y as String
        with self.assertRaises(TypeError):
            n = Rectangle(4, 8, "hello", "world")

        # x and y as float
        with self.assertRaises(TypeError):
            n = Rectangle(4, 8, 5.12, 5.9)
        
        # inputs as boolean 
        with self.assertRaises(TypeError):
            n = Rectangle(True, False, True, False)
        
    def test_input_values(self):
        """ Test the input value given
        """
        with self.assertRaises(ValueError):
            n = Rectangle(0, 0)
        with self.assertRaises(ValueError):
            n = Rectangle(1, 1, -5, -2)
