#!/usr/bin/python3
"""This script fetches headers from a url using urllib"""
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as f:
            print(f.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.status))
