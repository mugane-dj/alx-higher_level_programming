#!/usr/bin/python3
"""This script makes a post request to specified url"""
import requests
import sys


if __name__ == "__main__":
    if sys.argv[1]:
        param = sys.argv[1]
    else:
        param = ""
    url = "http://0.0.0.0:5000/search_user?q={}".format(param)
    res = requests.post(url)
    try:
        output = res.json()
        if output:
            print("{[]} {}".format(output.id, output.name))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
