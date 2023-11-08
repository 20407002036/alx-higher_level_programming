#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    # it's an update of the dictionary, A copy is the one affected
    a_dictionary.update({key: value})
    return (a_dictionary.copy())
