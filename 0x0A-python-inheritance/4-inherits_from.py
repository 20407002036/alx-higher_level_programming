#!/usr/bin/python3
""" Defines the function
"""


def inherits_from(obj, a_class):
    """
    Definition of the function
    """
    NewClass = type(obj)

    while NewClass is not object:
        if NewClass == a_class:
            return True
        NewClass = NewClass.__base__

    return False
