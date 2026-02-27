#!/usr/bin/python3
"""Handles basic operations using calculator_1 functions."""
import sys
from calculator_1 import add, sub, mul, div


def main():
    """Entry point for the calculator script."""
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    op = sys.argv[2]
    b = int(sys.argv[3])

    ops = ['+', '-', chr(42), '/']
    if op not in ops:
        print("Unknown operator. Available operators: +, -, " +
              chr(42) + " and /")
        sys.exit(1)

    if op == '+':
        result = add(a, b)
    elif op == '-':
        result = sub(a, b)
    elif op == chr(42):
        result = mul(a, b)
    else:
        result = div(a, b)

    print("{} {} {} = {}".format(a, op, b, result))


if __name__ == "__main__":
    main()
