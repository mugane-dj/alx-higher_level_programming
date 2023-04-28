#!/usr/bin/python3
#This script makes a post request to the url passed as argument
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = {"email": email}
    res = requests.post(url, data=date)
    print(res.text)
