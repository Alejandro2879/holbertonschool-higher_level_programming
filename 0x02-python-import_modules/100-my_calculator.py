#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    import sys


if len(sys.argv) is not 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)

ops = ['+', '-', '*', '/']
first_e = int(sys.argv[1])
second_e = int(sys.argv[3])
operator = sys.argv[2]
result = 0

if operator not in ops:
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)

for i in sys.argv[1:]:
    if operator is '+':
        result = add(first_e, second_e)
    elif operator is '-':
        result = sub(first_e, second_e)
    elif operator is '*':
        result = mul(first_e, second_e)
    elif operator is '/':
        result = div(first_e, second_e)

print("{} {} {} = {}".format(first_e, operator, second_e, result))
