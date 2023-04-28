#!/usr/bin/python3
"""This script fetches a url using urllib"""
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as f:
        context = f.read()
        print("Body response:")
        print("\t- type: {}".format(type(context)))
        print("\t- content: {}".format(context))
        print("\t- utf8 content: {}".format(context.decode('utf-8')))
