#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    printed_elements = 0

    try:
        for i in range(x):
            print("{}".format(my_list[i]), end=' ')
            # The print is quite important. have the placo holder in place
            printed_elements += 1

    except IndexError:
        pass  # Handle the IndexError exception (when the index is out of range)

    finally:
        print()  # Print a newline after all elements

    return printed_elements
