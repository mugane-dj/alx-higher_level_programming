#!/usr/bin/python3
"""This script fetches headers from a url using requests lib"""
import requests


if __name__ == "__main__":
    res = requests.get("https://alx-intranet.hbtn.io/status").text
    print("Body response:")
    print("\t- type: {}".format(type(res)))
    print("\t- content: {}".format(res))
