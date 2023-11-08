#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # searches all the occurences and replaces with the replace
    return ([ele if ele != search else replace for ele in my_list])
