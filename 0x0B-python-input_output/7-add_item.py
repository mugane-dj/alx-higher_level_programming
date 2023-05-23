#!/usr/bin/python3


"""Defines the load, add, save module"""
import sys
load = __import__('6-load_from_json_file').load_from_json_file
save = __import__('5-save_to_json_file').save_to_json_file

if __name__ == "__main__":
    try:
        args = load("add_item.json")
    except FileNotFoundError:
        args = []

    args.extend(sys.argv[1:])
    save(args, "add_item.json")
