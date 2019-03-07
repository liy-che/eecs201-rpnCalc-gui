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

def calculate(arg):
    stack = []
    for token in arg.split():
        try:
            token = float(token)
            stack.append(token)
        except ValueError:
            try:
                function = operators[token]
                arg2 = stack.pop()
                arg1 = stack.pop()
                result = function(arg1, arg2)
                op = ' ' + token
            except KeyError:
                if token == '!' and len(stack) != 1:
                    numElt = len(stack)
                    newArg = ' '.join(str(e) for e in stack)
                    newArg = newArg + (op * (numElt - 1))
                    result = calculate(newArg)
                    del stack[:]
            finally:   
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
