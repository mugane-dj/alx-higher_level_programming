#!/usr/bin/python3

def text_indentation(text):
    """
    Prints a text with 2 new lines after specified characters `.`, `?` & `:`
    Args:
    text(str): text to be printed.
    Raises:
        TypeError: if text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in ".?:":
        text = text.replace(char, char + "\n\n")
    all_lines = [lines.strip(' ') for lines in text.split('\n')]
    new_text = "\n".join(all_lines)
    print(new_text, end="")
