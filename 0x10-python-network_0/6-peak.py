#!/usr/bin/python3
"""This module contains a divide and conquer algorithm that finds
the peak in a list of unsorted ints"""


def find_peak(list_of_integers):
    """Finds the peak of a list of ints

    list_of_integers: the list to check.
    Returns: peak int.
    """
    size = len(list_of_integers)

    if size == 0:
        return
    elif size == 1:
        return list_of_integers[0]
    elif size == 2:
        return max(list_of_integers)
    else:
        mid = (size - 1) // 2
        if (list_of_integers[mid] > list_of_integers[mid + 1]
                and list_of_integers[mid] > list_of_integers[mid - 1]):
            return list_of_integers[mid]
        elif list_of_integers[mid] < list_of_integers[mid + 1]:
            return find_peak(list_of_integers[mid:])
        else:
            return find_peak(list_of_integers[:mid])
