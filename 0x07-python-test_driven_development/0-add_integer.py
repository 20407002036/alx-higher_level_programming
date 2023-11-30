#!/usr/bin/python3
"""
Class Definition
"""


def add_integer(a, b=98):
    """
   >>> add_integer = __import__('0-add_integer').add_integer
>>> add_integer(4, 10)
14

>>> add_integer(3, -10)
-7

>>> add_integer(3, "Hello")
Traceback (most recent call last):
	...
TypeError: b must be an integer

>>> add_integer("Hello", 3)
Traceback (most recent call last):
	...
TypeError: a must be an integer

>>> add_integer(3.2, 3)
6

>>> add_integer(4.9, 4.8)
8

>>> add_integer(-4.9, -4.8)
-8

>>> add_integer("Hello", "World")
Traceback (most recent call last):
	...
TypeError: a must be an integer

    """
    if not isinstance(a, int):
        if isinstance(a, float):
            a = int(a)
        else:
            raise TypeError("a must be an integer")
    if not isinstance(b, int):
        if isinstance(b, float):
            b = int(b)
        else:
            raise TypeError("b must be an integer")
    return a + b
