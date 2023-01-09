#!/usr/bin/python3

def no_c(my_string):
    chars = [x for x in my_string]

    for char in chars:
        if char == "c" or char == "C":
            chars.remove(char)
        new_string = ''.join(chars)
    return new_string
