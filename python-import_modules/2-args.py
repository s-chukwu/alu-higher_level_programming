#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]  
    count = len(argv)
    
    label = "argument" if count == 1 else "arguments"
    ending = ":" if count > 0 else "."
    
    print("{} {}{}".format(count, label, ending))
    
    for i, arg in enumerate(argv, start=1):
        print("{}: {}".format(i, arg))
