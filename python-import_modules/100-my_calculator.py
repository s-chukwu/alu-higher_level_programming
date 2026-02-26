#!/usr/bin/python3
import sys
import calculator_1

if __name__ == "__main__":
    # Check if the number of arguments is exactly 3
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    # Dictionary mapping operators to the functions inside calculator_1
    ops = {
        "+": calculator_1.add,
        "-": calculator_1.sub,
        "*": calculator_1.mul,
        "/": calculator_1.div
    }

    # Check for valid operator
    if operator not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    # Perform calculation and print
    result = ops[operator](a, b)
    print("{} {} {} = {}".format(a, operator, b, result))
