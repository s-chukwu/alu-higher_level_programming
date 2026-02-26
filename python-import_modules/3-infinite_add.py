#!/usr/bin/python3
import sys

if __name__ == "__main__":
    total = 0
    # Loop through all arguments starting from index 1
    for arg in sys.argv[1:]:
        total += int(arg)

    print("{}".format(total))
