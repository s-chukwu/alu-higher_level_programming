#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    # The instruction strictly states: "If the number of arguments is not 3"
    # sys.argv contains the script name plus the arguments, so we subtract 1.
    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    operator = sys.argv[2]

    # Explicitly check if the operator is one of the allowed strings
    if operator not in ['+', '-', '*', '/']:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    # Cast a and b into integers
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    # Perform the calculation using explicit, direct function calls so
    # the static analyzer can "see" that you used the imported functions.
    if operator == '+':
        result = add(a, b)
    elif operator == '-':
        result = sub(a, b)
    elif operator == '*':
        result = mul(a, b)
    elif operator == '/':
        result = div(a, b)

    # Print the result exactly as requested
    print("{} {} {} = {}".format(a, operator, b, result))
