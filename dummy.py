from tkinter import *
window = Tk()
window.title("Calculator")
window.geometry("320x320")
window.config(background='gray')

def SHOW(number):
    current = txt.get()
    txt.delete(0, END)
    txt.insert(0, str(current) + str(number))

def RESET():
    txt.delete(0, END)

def ADDITION():
    N = txt.get()
    global N1
    global Eq
    Eq = "ADDITION"
    N1 = float(N)
    txt.delete(0, END)

def EQUIVALENT():
    N2 = txt.get()
    txt.delete(0, END)

    if Eq == "ADDITION":
        txt.insert(0, N1 + float(N2))
    if Eq == "SUBTRACTION":
        txt.insert(0, N1 - float(N2))
    if Eq == "MULTIPLICATION":
        txt.insert(0, N1 * float(N2))
    if Eq == "DIVISION":
        txt.insert(0, N1 / float(N2))

def SUBTRACT():
    N= txt.get()
    global N1
    global Eq
    Eq = "SUBTRACTION"
    N1 = float(N)
    txt.delete(0, END)

def MULT():
    N = txt.get()
    global N1
    global Eq
    Eq = "MULTIPLICATION"
    N1 = float(N)
    txt.delete(0, END)

def DIVISION():
    N = txt.get()
    global N1
    global Eq
    Eq = "DIVISION"
    N1 = float(N)
    txt.delete(0, END)


txt = Entry(window, bd=15, bg="Gray", font=("bold", '25'), justify="right", width=294)
txt.pack(fill='x')

buttonC = Button(window, text='C', fg='black', height=2, width=294, font='bold', command=RESET)
buttonC.pack(fill='x')

button_frame = Frame()
button_frame.pack(side='top', fill='x')

button7 = Button(button_frame, text='7', fg='black', height=1, width=8, font='bold', command=lambda: SHOW(7))
button8 = Button(button_frame, text='8', fg='black', height=1, width=8, font='bold', command=lambda: SHOW(8))
button9 = Button(button_frame, text='9', fg='black', height=1, width=8, font='bold', command=lambda: SHOW(9))
Div = Button(button_frame, text='/', fg='black', height=1, width=8, font='bold', command=DIVISION)
button4 = Button(button_frame, text='4', fg='black', height=1, width=8, font='bold', command=lambda: SHOW(4))
button5 = Button(button_frame, text='5', fg='black', height=1, width=8, font='bold', command=lambda: SHOW(5))
button6 = Button(button_frame, text='6', fg='black', height=1, width=8, font='bold', command=lambda: SHOW(6))
Mul = Button(button_frame, text='*', fg='black', height=1, width=8, font='bold', command=MULT)
button1 = Button(button_frame, text='1', fg='black', height=1, width=8, font='bold', command=lambda: SHOW(1))
button2 = Button(button_frame, text='2', fg='black', height=1, width=8, font='bold', command=lambda: SHOW(2))
button3 = Button(button_frame, text='3', fg='black', height=1, width=8, font='bold', command=lambda: SHOW(3))
Sub = Button(button_frame, text='-', fg='black', height=1, width=8, font='bold', command=SUBTRACT)

button_frame.columnconfigure(4, weight=1)
button_frame.configure(bg='Gray')
button7.grid(row=3, column=0)
button8.grid(row=3, column=1)
button9.grid(row=3, column=2)
Div.grid(row=3, column=3)
button4.grid(row=4, column=0)
button5.grid(row=4, column=1)
button6.grid(row=4, column=2)
Mul.grid(row=4, column=3)
button1.grid(row=5, column=0)
button2.grid(row=5, column=1)
button3.grid(row=5, column=2)
Sub.grid(row=5, column=3)


button_frame1 = Frame()
button_frame1.pack(fill='x')

button0 = Button(button_frame1, text='0', fg='black', height=2, width=11, font='bold', command=lambda: SHOW('0'))
buttonDot = Button(button_frame1, text='.', fg='black', height=2, width=11, font='bold', command=lambda: SHOW('.'))
Add = Button(button_frame1, text='+', fg='black', height=2, width=11, font='bold', command=ADDITION)

button_frame1.columnconfigure(1, weight=1)
button_frame1.configure(bg='Gray')
button0.grid(row=6, column=0)
buttonDot.grid(row=6, column=1)
Add.grid(row=6, column=2)


buttonEq = Button(window, text='=', fg='black', height=2, width=294, font='bold', command=EQUIVALENT)
buttonEq.pack(side='bottom', fill='x')

window.mainloop()