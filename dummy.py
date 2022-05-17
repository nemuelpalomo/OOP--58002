from tkinter import *

calculator = Tk()
calculator.title('Simple Calculator')
calculator.configure(bg='snow')
calculator.geometry('328x320')


# Defining Functions for the Calculator

def add_field(number):
    current = txt.get()
    txt.delete(0, END)
    txt.insert(0, str(current) + str(number))


def clear_field():
    txt.delete(0, END)


def add():
    num = txt.get()
    global firstNum
    global op
    op = "add"
    firstNum = float(num)
    txt.delete(0, END)


def subtract():
    num = txt.get()
    global firstNum
    global op
    op = "subtract"
    firstNum = float(num)
    txt.delete(0, END)


def mutiply():
    num = txt.get()
    global firstNum
    global op
    op = "multiply"
    firstNum = float(num)
    txt.delete(0, END)


def divide():
    num = txt.get()
    global firstNum
    global op
    op = "divide"
    firstNum = float(num)
    txt.delete(0, END)


def equivalent():
    N2 = txt.get()
    txt.delete(0, END)

    if op == "add":
        txt.insert(0, float(firstNum) + float(N2))
    if op == "subtract":
        txt.insert(0, float(firstNum) - float(N2))
    if op == "multiply":
        txt.insert(0, float(firstNum) * float(N2))
    if op == "divide":
        txt.insert(0, float(firstNum) / float(N2))


# Widgets for the text field and for "C" for clear button

txt = Entry(calculator, bd=15, bg="White", font=("bold", '25'), justify="right", width=300)
txt.pack(fill='x')

buttonC = Button(calculator, text='C', fg='black', height=2, width=12, font='bold', command=clear_field)
buttonC.pack(fill='x')

button_frame = Frame()
button_frame.pack(side='top', fill='x')

# Button Operators Widget

Addition = Button(button_frame, text='+', fg='black', height=2, width=8, font='bold', command=add)
Addition.grid(row=4, column=3)
Subtraction = Button(button_frame, text='-', fg='black', height=2, width=8, font='bold', command=subtract)
Subtraction.grid(row=1, column=3)
Multiplication = Button(button_frame, text='*', fg='black', height=2, width=8, font='bold', command=mutiply)
Multiplication.grid(row=2, column=3)
Division = Button(button_frame, text='/', fg='black', height=2, width=8, font='bold', command=divide)
Division.grid(row=3, column=3)
Equals = Button(button_frame, text='=', fg='black', height=2, width=8, font='bold', command=equivalent)
Equals.grid(row=4, column=1)

# Buttons from 0 to 9

button1 = Button(button_frame, text='1', fg='black', height=2, width=8, font='bold', command=lambda: add_field(1))
button1.grid(row=1, column=0)
button2 = Button(button_frame, text='2', fg='black', height=2, width=8, font='bold', command=lambda: add_field(2))
button2.grid(row=1, column=1)
button3 = Button(button_frame, text='3', fg='black', height=2, width=8, font='bold', command=lambda: add_field(3))
button3.grid(row=1, column=2)
button4 = Button(button_frame, text='4', fg='black', height=2, width=8, font='bold', command=lambda: add_field(4))
button4.grid(row=2, column=0)
button5 = Button(button_frame, text='5', fg='black', height=2, width=8, font='bold', command=lambda: add_field(5))
button5.grid(row=2, column=1)
button6 = Button(button_frame, text='6', fg='black', height=2, width=8, font='bold', command=lambda: add_field(6))
button6.grid(row=2, column=2)
button7 = Button(button_frame, text='7', fg='black', height=2, width=8, font='bold', command=lambda: add_field(7))
button7.grid(row=3, column=0)
button8 = Button(button_frame, text='8', fg='black', height=2, width=8, font='bold', command=lambda: add_field(8))
button8.grid(row=3, column=1)
button9 = Button(button_frame, text='9', fg='black', height=2, width=8, font='bold', command=lambda: add_field(9))
button9.grid(row=3, column=2)
button0 = Button(button_frame, text='0', fg='black', height=2, width=8, font='bold', command=lambda: add_field(0))
button0.grid(row=4, column=0)

calculator.mainloop()