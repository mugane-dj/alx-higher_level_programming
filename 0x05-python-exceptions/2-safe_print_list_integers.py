#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Prints the first x elements of a list"""

    no_of_elements = 0
    for element in range(x):
        try:
            print("{:d}".format(int(my_list[element])), end="")
            no_of_elements += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (no_of_elements)
