#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    # Check if the number of arguments is exactly 3 (plus the script name)
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    # Dictionary to map the operator string to the specific imported function
    ops = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div
    }

    operator = sys.argv[2]

    # Check if the provided operator is valid
    if operator not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    # Cast arguments to integers
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    # Perform the calculation using the correct function
    result = ops[operator](a, b)

    # Print the result in the expected format
    print("{} {} {} = {}".format(a, operator, b, result))
