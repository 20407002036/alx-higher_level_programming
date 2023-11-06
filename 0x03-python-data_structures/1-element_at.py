#!/usr/bin/python3
def element_at(my_list, idx):
    #if idx < 0:
    #    return 
    #elif idx > (len(my_list) - 1):
    #   return

    #this could have been done using one statement
    list_len = len(my_list)
    if idx >= list_len or idx < 0:
        return
    else:
        return my_list[idx]
