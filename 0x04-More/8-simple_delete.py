#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    # It had to be deleted, based on the keys 
    if key is not "" and key in a_dictionary:
        a_dictionary.pop(key)
    return (a_dictionary.copy())
