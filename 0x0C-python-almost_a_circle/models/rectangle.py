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
        """
        Initialize the class 
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y


    @property
    def width(self):
        """Getter for width"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """ setter for width property """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif(value <= 0):
            raise ValueError("Width must be > 0")
        
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """Setter for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif(value <= 0):
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """"Getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif(value < 0):
            raise ValueError("x must be >= 0")
        
        self.__x = value

    @property
    def y(self):
        """Getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif(value < 0):
            raise ValueError("y must be >= 0")
        
        self.__y = value
    
    def area(self):
        """Method that returns area of Rectangle"""

        return self.height * self.width
    
    def display(self):
        """Method to print in stdout the rectabgle using #"""


        for i in range(self.height):
            for j in range(self.width):
                print("#", end="")
            print()