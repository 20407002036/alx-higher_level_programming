#!/usr/bin/python3
"""
By Solomon Kanairu
Class Def
"""


from models.base import Base


class Rectangle(Base):
    """
    Class Rectangle:
    Attributes:
        __width
        __height
        __x
        __y
    """

    def __init__(self, width, height, x=0,y=0, id=None):
        Base.__init__(id)


    @property
    def width(self):
        return self.__width