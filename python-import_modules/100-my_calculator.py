#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    # Check if the number of arguments is exactly 3 (plus the script name itself)
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    # Assign arguments to variables
    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    # Dictionary to map operators to their respective functions
    ops = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div
    }

    # Check if the operator is valid
    if operator not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    # Perform the calculation and print the result
    result = ops[operator](a, b)
    print("{} {} {} = {}".format(a, operator, b, result))
