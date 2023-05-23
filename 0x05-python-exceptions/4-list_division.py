#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """Divides elements in a list"""

    result = []
    new_element = 0

    for element in range(0, list_length):
        try:
            new_element = my_list_1[element] / my_list_2[element]
        except TypeError:
            print("wrong type")
            new_element = 0
        except ZeroDivisionError:
            print("division by 0")
            new_element = 0
        except IndexError:
            print("out of range")
            new_element = 0
        finally:
            result.append(new_element)
    return result
