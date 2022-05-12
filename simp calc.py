from tkinter import *

window = Tk()
window.geometry("328x370+530+130")
window.title("Basic Calculator")
window.configure(bg='floral white')

# Functions for the operations to work in buttons.

def click(number):
    inputspace.insert(END, number)

def button_divide():
    num = textfield.get()
    global firstNumber
    global operator
    operator = "divide"
    firstNumber = float(num)
    textfield.delete(0, END)


def button_multiply():
    num = textfield.get()
    global firstNumber
    global operator
    operator = "multiply"
    firstNumber = float(num)
    textfield.delete(0, END)


def button_subtract():
    num = textfield.get()
    global firstNumber
    global operator
    operator = "subtract"
    firstNumber = float(num)
    textfield.delete(0, END)


def button_add():
    num = textfield.get()
    global firstNumber
    global operator
    operator = "add"
    firstNumber = float(num)
    textfield.delete(0, END)


def button_equals():
    second_num = textfield.get()
    textfield.delete(0, END)

    if operator == "add":
        textfield.insert(0, float(second_num) + float(firstNumber))
    if operator == "multiply":
        textfield.insert(0, float(second_num) * float(firstNumber))
    if operator == "divide":
        textfield.insert(0, float(firstNumber) / float(second_num))
    if operator == "subtract":
        textfield.insert(0, float(firstNumber) - float(second_num))


def button_clear():
    textfield.delete(0, END)
