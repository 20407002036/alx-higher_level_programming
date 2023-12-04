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
            raise TypeError(name +" must be an integer")

        if (value <= 0):
            raise ValueError(name +" must be greater than 0")
