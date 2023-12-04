#!/usr/bin/python3
"""
Class Def
"""


class BaseGeometry:
    """
    Class BaseGeometry
    Methods:
        Area
        integer_validator
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if (type(value) != int):
            raise TypeError("{} must be an integer".format(name))

        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))