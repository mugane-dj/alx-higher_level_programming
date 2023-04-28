#!/usr/bin/python3
"""This script fetches the id of a github user"""
import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"
    auth = HTTPBasicAuth(username, password)
    res = requests.get(url=url, auth=auth).json()
    print(res.get('id'))
