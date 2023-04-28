#!/usr/bin/python3
"""This script fetches headers from a url using urllib"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = {"email": email}
    data = urllib.parse.urlencode(data)
    req = urllib.request.Request(url, data=data.encode('utf-8'))
    with urllib.request.urlopen(req) as f:
        print(f.read().decode('utf-8'))
