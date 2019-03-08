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
root.geometry("400x500")

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

# buttons
num0 = Button(bottomFrame, text='0', bg='pink', height=3, width=2)
num1 = Button(bottomFrame, text='1', bg='pink', height=3, width=2)
num2 = Button(bottomFrame, text='2', bg='pink', height=3, width=2)
num3 = Button(bottomFrame, text='3', bg='pink', height=3, width=2)
num4 = Button(bottomFrame, text='4', bg='pink', height=3, width=2)
num5 = Button(bottomFrame, text='5', bg='pink', height=3, width=2)
num6 = Button(bottomFrame, text='6', bg='pink', height=3, width=2)
num7 = Button(bottomFrame, text='7', bg='pink', height=3, width=2)
num8 = Button(bottomFrame, text='8', bg='pink', height=3, width=2)
num9 = Button(bottomFrame, text='9', bg='pink', height=3, width=2)
dot = Button(bottomFrame, text='.', bg='magenta', height=3, width=2)
equal = Button(bottomFrame, text='=', bg='magenta', height=3, width=2)
add = Button(bottomFrame, text='+', bg='cyan', height=3, width=2)
sub = Button(bottomFrame, text='-', bg='cyan', height=3, width=2)
mul = Button(bottomFrame, text='x', bg='cyan', height=3, width=2)
truediv = Button(bottomFrame, text='/', bg='cyan', height=3, width=2)

num1.grid(row=0, column=0)
num2.grid(row=0, column=1)
num3.grid(row=0, column=2)
num4.grid(row=1, column=0)
num5.grid(row=1, column=1)
num6.grid(row=1, column=2)
num7.grid(row=2, column=0)
num8.grid(row=2, column=1)
num9.grid(row=2, column=2)
num0.grid(row=3, column=0)
dot.grid(row=3, column=1)
equal.grid(row=3, column=2)
add.grid(row=0, column=3)
sub.grid(row=1, column=3)
mul.grid(row=2, column=3)
truediv.grid(row=3, column=3)

if __name__ == '__main__':
    main()

root.mainloop()
