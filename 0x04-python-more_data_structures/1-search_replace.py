#!/usr/bin/python3

def search_replace(my_list, search, replace):
    "Replaces an element in a list"

    new_list = my_list[:]

    return (list(map(lambda x: replace if x == search else x, new_list)))
