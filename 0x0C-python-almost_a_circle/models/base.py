#!/usr/bin/python3
"""
By Solomon 
Class Def
"""


class Base():
    """
    Class Base that is My 1st Class in this project
    This class will be the “base” of all other classes in this project.
    The goal of it is to manage id attribute in all your future classes
    and to avoid duplicating the same code (by extension, same bugs)
    """

    __nb_objects = 0


    def __init__(self, id=None):
       #__nb_objects = 0
       # __nb_objects=__nb_objects+1

        if id is not None:
            self.id = id

        else:
            # __nb_objects = 0
            Base.__nb_objects+=1

            self.id = Base.__nb_objects