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

    def test_update(self):
        r = Rectangle(4, 5, 45)
        r.update(500)
        self.assertEqual(500, r.id)
        r.update(500, 2)
        self.assertEqual(2, r.width)
        r.update(500, 2, 3)
        self.assertEqual(3, r.height)
        r.update(500, 2, 3, 4)
        self.assertEqual(4, r.x)
        r.update(500, 2, 3, 4, 5)
        self.assertEqual(5, r.y)
        r.update(500, 2, 3, 4, 5, 6, 7, 8)
        self.assertEqual(5, r.y)


    def test_kwarg_update(self):
        r = Rectangle(4, 5, 0, 0, 33)
        r.update(45, id=32, width=42)
        self.assertEqual(45, r.id)
        r.update(45, 10, 10, x=5, y=6)
        self.assertEqual(0, r.x)
        self.assertEqual(10, r.width)
        self.assertEqual(45, r.id)
        r.update(width=4)
        self.assertEqual(4, r.width)
        r.update(width=6, id=6, height=45)
        self.assertEqual(6, r.width)
        self.assertEqual(6, r.id)
        self.assertEqual(45, r.height)
        r.update(x=100, y=100)
        self.assertEqual(6, r.id)
        self.assertEqual(100, r.x)
        self.assertEqual(100, r.y)

    def test_dictionary(self):
        """tests rectangle's to_dictionary method
        """
        r = Rectangle(4, 5, 6, 7, 33)
        r_dict = r.to_dictionary()
        self.assertEqual(r_dict['id'], 33)
        self.assertEqual(r_dict['width'], 4)
        self.assertEqual(r_dict['height'], 5)
        self.assertEqual(r_dict['x'], 6)
        self.assertEqual(r_dict['y'], 7)

