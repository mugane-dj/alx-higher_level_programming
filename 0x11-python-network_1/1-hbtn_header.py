#!/usr/bin/python3
"""This script fetches headers from a url using urllib"""
import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as f:
        headers = f.getheaders()
        print(headers[-3][1])
