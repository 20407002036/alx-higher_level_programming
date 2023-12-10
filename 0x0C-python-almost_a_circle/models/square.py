#!/usr/bin/python3
"""
This module gives the class Square
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class Square that inherita Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)



    def __str__(self):
        """
        Overriding the metho
        it returns [Rectangle] (<id>) <x>/<y> - <width>/<height>
        Eg [Rectabgle] (12) 2/1 - 4/6
        """

        builder = "[Square] ({}) {}/{} - {}".format(self.__class__.__name__,
                                                   self.id,
                                                   self.x,
                                                   self.y,
                                                   self.width)
        
        return builder
    

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        self.width = value
        self.height = value