#!/usr/bin/python3

# Finds the peak in a list of numbers

def find_peak(list_of_integers):
    """
    Finds the peak in a list.
    in a sorted list, the last item is always the peak element
    """
    list_of_integers.sort()
    if len(list_of_integers) == 0:
        return None
    else:
        return(list_of_integers[-1])
