#!/usr/bin/python3

class Square:
    """
    class square that has attributes:
        size
    
    """
    def __init__(self, size=0):
        """
        to define attributes.
        initialization function for our square clasee
        size is private, self.__size
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        to define Class Methods
        calculates the area of the square
        """
        return self.__size ** 2
