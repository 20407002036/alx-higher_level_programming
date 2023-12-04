#!/usr/bin/python3
""" Class MyList definition
"""


class MyList(list):
    """Class MyList
    Has no defined attributtes
    """

    def print_sorted(self):
        newList = sorted(self)
        print(newList)
