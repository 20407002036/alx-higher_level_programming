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
        """
        Functon that raises excption
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Function that checks the input values
        """
        if (type(value) != int):
            raise TypeError("{} must be an integer".format(name))

        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))
