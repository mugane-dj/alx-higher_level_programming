#!/usr/bin/python3
"""This script fetches a header from a url using requests lib"""
import requests
import sys


if __name__ == "__main__":
    res = requests.get(sys.argv[1])
    print(res.headers['X-Request-Id'])
