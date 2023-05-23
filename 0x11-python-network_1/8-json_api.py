#!/usr/bin/python3
"""This script makes a post request to specified url"""
import requests
import sys


if __name__ == "__main__":
    try:
        param = sys.argv[1]
    except IndexError:
        param = ""
    data = {'q': param}
    url = "http://0.0.0.0:5000/search_user"
    res = requests.post(url, data=data)
    try:
        output = res.json()
        if output:
            print("[{}] {}".format(output.get('id'), output.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
