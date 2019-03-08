#! /usr/bin/env python3
import helper
import operator
import math
import readline
from tkinter import *

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

last = 0
repeat = 0

def calculate(arg):
    stack = []
    global last, repeat
    for token in arg.split():
        repeat = 0
        try:
            token = float(token)
            stack.append(token)
        except ValueError:
            try:
                function = operators[token]
                if token =='!' and len(stack) != 1:
                        raise KeyError("Repeat")
            except KeyError:
                if token == ':ans':
                    stack.append(last)
                if token == '!' and len(stack) != 1:
                    repeat = 1
                    numElt = len(stack)
                    newArg = ' '.join(str(e) for e in stack)
                    newArg = newArg + (op * (numElt - 1))
            else:
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
                op = ' ' + token
                if repeat != 1:
                    stack.append(result)
            if repeat == 1:
                result = calculate(newArg)
                del stack[:] 
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

#---------------- GUI ----------------#
root = Tk()
root.title("RPN Calculator")
root.geometry("300x400")

# buttons
num0 = Button(root, text='0', bg='pink')
num1 = Button(root, text='1', bg='pink')
num2 = Button(root, text='2', bg='pink')
num3 = Button(root, text='3', bg='pink')
num4 = Button(root, text='4', bg='pink')
num5 = Button(root, text='5', bg='pink')
num6 = Button(root, text='6', bg='pink')
num7 = Button(root, text='7', bg='pink')
num8 = Button(root, text='8', bg='pink')
num9 = Button(root, text='9', bg='pink')

num1.grid(row=5, column=0)
num2.grid(row=5, column=1)
num3.grid(row=5, column=2)
if __name__ == '__main__':
    main()

root.mainloop()
