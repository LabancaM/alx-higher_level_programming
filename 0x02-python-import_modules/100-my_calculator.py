#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    length = len(sys.argv)
    operators = "+-*/"
    if length != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        operator = sys.argv[2]
        if operator not in operators:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        else:
            a = int(sys.argv[1])
            b = int(sys.argv[3])
            operator = sys.argv[2]
            if operator == "+":
                print("{} + {} = {}".format(a, b, add(a, b)))
            elif operator == "-":
                print("{} - {} = {}".format(a, b, sub(a, b)))
            elif operator == "*":
                print("{} * {} = {}".format(a, b, mul(a, b)))
            else:
                print("{} / {} = {}".format(a, b, div(a, b)))
            sys.exit(0)
