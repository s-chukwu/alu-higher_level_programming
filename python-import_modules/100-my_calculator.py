#!/usr/bin/python3
"""Module that handles basic arithmetic operations using calculator_1 functions."""
import sys
from calculator_1 import add, sub, mul, div


def main():
    """Main function to handle calculator operations."""
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    operators = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div
    }

    if operator not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    result = operators[operator](a, b)
    print("{} {} {} = {}".format(a, operator, b, result))


if __name__ == "__main__":
    main()
