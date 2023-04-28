#!/usr/bin/python3
"""This script fetches headers from a url using requests lib"""
import requests
import sys


if __name__ == "__main__":
    res = requests.get(sys.argv[1])
    print(res.headers['X-Request-Id'])
