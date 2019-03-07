#! /usr/bin/env python3

import operator
import readline

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
}

last = 0

def calculate(arg):
    stack = []
    global last
    for token in arg.split():
        try:
            token = float(token)
            stack.append(token)
        except ValueError:
            try:
                function = operators[token]
            except KeyError:
                stack.append(last)
            else:
                arg2 = stack.pop()
                arg1 = stack.pop()
                result = function(arg1, arg2)
                stack.append(result)
        print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    last = stack.pop()
    return last

def main():
    while True:
        result = calculate(input("rpn calc> "))
        print("Result: ", result)

if __name__ == '__main__':
    main()
