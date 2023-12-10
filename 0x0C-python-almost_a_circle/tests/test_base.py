#!/usr/bin/python3
"""
This module is  used in the testing of
Class Base
"""


import os
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    This class is used for the testing of the base class
    """

    def test_idAssignment(self):
        """
        Test if the assignment of id is
        given correctly:
            Autogiven if not provided in class call
                *This autoincrements
        """
        b = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b2.id + 1, b3.id)