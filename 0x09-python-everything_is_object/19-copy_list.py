#!/usr/bin/python3
def copy_list(l):
     if not isinstance(l, list):
        return None
    return l[:]
