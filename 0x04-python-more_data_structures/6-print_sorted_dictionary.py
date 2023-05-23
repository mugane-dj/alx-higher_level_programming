#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    "Print a sorted dictionary"

    for key in sorted(a_dictionary.keys()):
        print("{}: {}".format(key, a_dictionary[key]))
