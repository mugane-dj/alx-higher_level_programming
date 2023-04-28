#!/usr/bin/python3
"""This script fetches the id of a github user"""
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/users/{}".format(username)
    headers = {
        'Authorization': 'Basic ' + password
    }

    res = requests.get(url=url, headers=headers).json()
    print(res.get('id'))
