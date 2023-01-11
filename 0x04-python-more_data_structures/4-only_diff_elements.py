#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    "Retrieves unique elements between two sets"
    all_elements = set_1 ^ set_2
    return all_elements
