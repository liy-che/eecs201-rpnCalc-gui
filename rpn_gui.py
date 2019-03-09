#! /usr/bin/env python3
import rpn
from tkinter import *

# functions
def getBtn(event, out):
	display.insert(END, out)

def getInput():
	text = display.get(0.0, INSERT)
	try:
		result = rpn.calculate(text)
		display.insert
	except Exception as e:
		display.insert(END, e)

def clearDisplay():
	display.delete(1.0, END)

def deleteChar():
	display.delete("insert-1c")

# frames
root = Tk()
root.title("RPN Calculator")
root.geometry("350x485")

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

# buttons
btnList = []
num0 = Button(bottomFrame, text='0', bg='pink', height=3, width=2)
num0.bind('<ButtonRelease>', lambda event: getBtn(event, '0'))
num1 = Button(bottomFrame, text='1', bg='pink', height=3, width=2)
num1.bind('<ButtonRelease>', lambda event: getBtn(event, '1'))
num2 = Button(bottomFrame, text='2', bg='pink', height=3, width=2)
num2.bind('<ButtonRelease>', lambda event: getBtn(event, '2'))
num3 = Button(bottomFrame, text='3', bg='pink', height=3, width=2)
num3.bind('<ButtonRelease>', lambda event: getBtn(event, '3'))
num4 = Button(bottomFrame, text='4', bg='pink', height=3, width=2)
num4.bind('<ButtonRelease>', lambda event: getBtn(event, '4'))
num5 = Button(bottomFrame, text='5', bg='pink', height=3, width=2)
num5.bind('<ButtonRelease>', lambda event: getBtn(event, '5'))
num6 = Button(bottomFrame, text='6', bg='pink', height=3, width=2)
num6.bind('<ButtonRelease>', lambda event: getBtn(event, '6'))
num7 = Button(bottomFrame, text='7', bg='pink', height=3, width=2)
num7.bind('<ButtonRelease>', lambda event: getBtn(event, '7'))
num8 = Button(bottomFrame, text='8', bg='pink', height=3, width=2)
num8.bind('<ButtonRelease>', lambda event: getBtn(event, '8'))
num9 = Button(bottomFrame, text='9', bg='pink', height=3, width=2)
num9.bind('<ButtonRelease>', lambda event: getBtn(event, '9'))
dot = Button(bottomFrame, text='.', bg='magenta', height=3, width=2)
dot.bind('<ButtonRelease>', lambda event: getBtn(event, '.'))
equal = Button(bottomFrame, text='=', bg='magenta', height=3, width=2, command=getInput)
add = Button(bottomFrame, text='+', bg='cyan', height=3, width=2)
add.bind('<ButtonRelease>', lambda event: getBtn(event, '+'))
sub = Button(bottomFrame, text='-', bg='cyan', height=3, width=2)
sub.bind('<ButtonRelease>', lambda event: getBtn(event, '-'))
mul = Button(bottomFrame, text='*', bg='cyan', height=3, width=2)
mul.bind('<ButtonRelease>', lambda event: getBtn(event, '*'))
truediv = Button(bottomFrame, text='/', bg='cyan', height=3, width=2)
truediv.bind('<ButtonRelease>', lambda event: getBtn(event, '/'))
percent = Button(bottomFrame, text='%', bg='cyan', height=3, width=2)
percent.bind('<ButtonRelease>', lambda event: getBtn(event, '%'))
exp = Button(bottomFrame, text='exp', bg='cyan', height=3, width=2)
exp.bind('<ButtonRelease>', lambda event: getBtn(event, '^'))
fact = Button(bottomFrame, text='x!', bg='cyan', height=3, width=2)
fact.bind('<ButtonRelease>', lambda event: getBtn(event, '!'))
bitAnd = Button(bottomFrame, text='AND', bg='yellow', height=3, width=2)
bitAnd.bind('<ButtonRelease>', lambda event: getBtn(event, '&'))
bitOr = Button(bottomFrame, text='OR', bg='yellow', height=3, width=2)
bitOr.bind('<ButtonRelease>', lambda event: getBtn(event, '|'))
bitNot = Button(bottomFrame, text='NOT', bg='yellow', height=3, width=2)
bitNot.bind('<ButtonRelease>', lambda event: getBtn(event, '~'))
clear = Button(bottomFrame, text='clear', bg='red', height=3, width=8, command=clearDisplay)
delete = Button(bottomFrame, text='delete', bg='red', height=3, width=8, command=deleteChar)
repeat = Button(bottomFrame, text='repeat', bg='magenta', height=3, width=2)
repeat.bind('<ButtonRelease>', lambda event: getBtn(event, '!'))
ans = Button(bottomFrame, text='ANS', bg='magenta', height=3, width=2)
#
space = Button(bottomFrame, text='space', bg='blue', fg='white', height=1, width=36)
space.bind('<ButtonRelease>', lambda event: getBtn(event, ' '))

num1.grid(row=1, column=0)
num2.grid(row=1, column=1)
num3.grid(row=1, column=2)
num4.grid(row=2, column=0)
num5.grid(row=2, column=1)
num6.grid(row=2, column=2)
num7.grid(row=3, column=0)
num8.grid(row=3, column=1)
num9.grid(row=3, column=2)
num0.grid(row=4, column=0)
dot.grid(row=4, column=1)
equal.grid(row=4, column=2)
add.grid(row=1, column=3)
sub.grid(row=2, column=3)
mul.grid(row=3, column=3)
truediv.grid(row=4, column=3)
percent.grid(row=1, column=4)
exp.grid(row=2, column=4)
fact.grid(row=3, column=4)
bitAnd.grid(row=4, column=4)
bitOr.grid(row=4, column=5)
bitNot.grid(row=4, column=6)
clear.grid(row=1, column=5, columnspan=2)
delete.grid(row=2, column=5, columnspan=2)
repeat.grid(row=3, column=5)
ans.grid(row=3, column=6)
space.grid(row=0, columnspan=7)

# display screen
display = Text(topFrame, height=5, width=28)
display.config(font='Helvetica 15', bg='black', fg='white')
display.pack()

# status bar
status_text = 'ANS = ' + str(rpn.last)
status = Label(topFrame, text=status_text, bg='black', height=2)
status.pack(side=BOTTOM, fill=X)

root.mainloop()
