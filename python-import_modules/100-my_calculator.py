#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    # Check if we have exactly 3 arguments (plus the script name = 4)
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    # Map the string operators to the imported functions
    ops = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div
    }

    # Extract the operator string from the arguments
    operator = sys.argv[2]

    # Validate the operator
    if operator not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    # Cast a and b to integers
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    # Calculate the result by calling the function from the dictionary
    result = ops[operator](a, b)

    # Print the result
    print("{} {} {} = {}".format(a, operator, b, result))
