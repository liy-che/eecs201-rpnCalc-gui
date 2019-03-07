#! /usr/bin/env python3
import helper
import operator
import math
import readline

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '%': helper.percent,
    '^': operator.pow,
    '//': operator.floordiv,
    '!': math.factorial,
    '&': operator.and_,
    '|': operator.or_,
    '~': operator.invert,
}

def calculate(arg):
    stack = []
    for token in arg.split():
        try:
            token = float(token)
            stack.append(token)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            if token != '~' and token != '!':
                arg1 = stack.pop()
            if token == '%':
                stack.append(arg1)
            if token == '&' or token == '|' or token == '~' or token == '!':
                arg2 = int(arg2)
                if token != '~' and token != '!':
                    arg1 = int(arg1)
            if token == '~' or token == '!':
                result = function(arg2)
            else:
                result = function(arg1, arg2)
            stack.append(result)
        print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def main():
    while True:
        result = calculate(input("rpn calc> "))
        print("Result: ", result)

if __name__ == '__main__':
    main()
