#!/usr/bin/python3
"""
Returns a list of available attributes and methods of an object
"""

def lookup(obj):
    return [attr for attr in dir(obj) if not callable(getattr(obj, attr)) or callable(getattr(obj, attr))]
