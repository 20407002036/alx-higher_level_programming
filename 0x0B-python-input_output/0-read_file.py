#!/usr/bin/python3
"""
The Last exciting project
"""


def read_file(filename=""):
    """
    Enable for the file access
    """

    with open(filename, encoding="utf-8") as f:
        read_file = f.read()

        print(read_file)

    f.closed
