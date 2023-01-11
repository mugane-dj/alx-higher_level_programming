#!/usr/bin/python3

def uniq_add(my_list=[]):
    "Sum of unique numbers in a list"

    sum = 0

    for i, element in enumerate(my_list):
        if element not in my_list[:i]:
            sum += element
    return sum
