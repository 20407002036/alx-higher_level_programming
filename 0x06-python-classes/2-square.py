#!/usr/bin/python3

class Square:
    """
    class square that has attributes:
        size, This is private
    some attributes are protected from input.
    """
    def __init__(self, size=0):
        """
        the initialization function for the square class
        checks for input error defining wether or not the input
        is int, or if size < 0
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
