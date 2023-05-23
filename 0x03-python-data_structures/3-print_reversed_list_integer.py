#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    rev_list = sorted(my_list, reverse=True)
    for x in rev_list:
        print("{:d}".format(x))
