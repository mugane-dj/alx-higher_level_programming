#!/usr/bin/python3

def multiple_returns(sentence):
    chars = [x for x in sentence]

    if chars[0] is None:
        return (len(sentence), None)
    else:
        return (len(sentence), chars[0])
