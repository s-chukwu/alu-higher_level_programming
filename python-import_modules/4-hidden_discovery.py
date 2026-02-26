#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    # Get all defined names in the module
    names = dir(hidden_4)

    for name in sorted(names):
        if not name.startswith("__"):
            print("{}".format(name))
