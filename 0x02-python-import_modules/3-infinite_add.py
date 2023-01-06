#!/usr/bin/python3
import sys

if __name__ == '__main__':
    num_args = len(sys.argv) - 1
    sum = 0

    for i in range(num_args):
        sum += int(sys.argv[i + 1])
    print("{}".format(sum))
