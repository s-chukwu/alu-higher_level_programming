#!/usr/bin/python3
import sys
from calculator_1

if __name__ == "__main__":
    # 1. Check if the number of arguments is exactly 3 (plus the script name = 4)
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    # 2. Extract arguments
    a_str = sys.argv[1]
    operator = sys.argv[2]
    b_str = sys.argv[3]

    # 3. Map operators to the explicitly imported functions
    ops = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div
    }

    # 4. Check if the operator is valid
    if operator not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    # 5. Cast a and b into integers
    a = int(a_str)
    b = int(b_str)

    # 6. Calculate the result
    result = ops[operator](a, b)

    # 7. Print the exact required output format
    print("{} {} {} = {}".format(a, operator, b, result))
