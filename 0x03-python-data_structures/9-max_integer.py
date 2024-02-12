#!/usr/bin/python3
def max_integer(my_list=[]):
    # finds the largest integer of a list
    # The function sorts the memebers of the list in ascending order
    # then takes the last value (highest value)
    if len(my_list) == 0:
        return (None)
    my_list.sort()
    return (my_list[-1])
