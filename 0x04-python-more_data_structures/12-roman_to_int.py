#!/usr/bin/python3

def roman_to_int(roman_string):
    "Converts Roman numeral to int"

    if type(roman_string) != str or None:
        return 0

    roman_dict = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
    }

    integer = 0

    s = roman_string

    for i in range(len(s)):
        if i > 0 and roman_dict[s[i]] > roman_dict[s[i-1]]:
            integer += roman_dict[s[i]] - 2 * roman_dict[s[i-1]]
        else:
            integer += roman_dict[s[i]]
    return integer
