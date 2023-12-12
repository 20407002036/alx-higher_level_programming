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

        builder = "[Square] ({}) {}/{} - {}".format(
            self.id,
            self.x,
            self.y,
            self.width
            )

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

    def update(self, *args, **kwargs):
        """
        Has both a Dict and list
        """
        if args is not None and len(args) > 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
        elif kwargs is not None:
            for (key, value) in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """gets the dictionary representation of a square object
        """
        new_d = super().to_dictionary()
        del new_d['height']
        del new_d['width']
        new_d['size'] = self.size
        return new_d

    def to_csv(self):
        """returns a list containing csv representation of rectangle
        """
        return [self.id, self.size, self.x, self.y]

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
