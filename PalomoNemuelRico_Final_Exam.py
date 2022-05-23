from tkinter import *
window = Tk()
window.geometry("400x500")
window.title('PalomoNemuelRico_FINAL_EXAM_OOP')

# Applying Objects and Classes for the program

# This is the code for the GUI

class final_exam:
    def __init__(self,window):
        self.title_lbl = Label(window, text="FIND THE LEAST NUMBER AMONG THREE NUMBERS")
        self.title_lbl.place(relx=0.50, y=50, anchor="center")
        self.input1_lbl = Label(window,text="Enter the first number: ")
        self.input1_lbl.place(x=120, y=80)
        self.input1 = Entry(window, bd=1)
        self.input1.place(x=120, y=120)
        self.input2_lbl = Label(window,text="Enter the second number: ")
        self.input2_lbl.place(x=120, y=160)
        self.input2 = Entry(window, bd=1)
        self.input2.place(x=120, y=200)
        self.input3_lbl = Label(window, text="Enter the third number: ")
        self.input3_lbl.place(x=120, y=240)
        self.input3 = Entry(window, bd=1)
        self.input3.place(x=120, y=280)
        self.button = Button(window, text="FIND THE LEAST NUMBER", command=self.least_value)
        self.button.place(x=120, y=320)
        self.output = Label(window, text="---RESULT---")
        self.output.place(x=140, y=380)
        self.output_result = Entry(window, bd=4, width=25)
        self.output_result.place(x=120, y=420)

# Function to find the least value in the said GUI

    def least_value(self):
        try:
            self.output_result.delete(0, 'end')
            L = []
            num1 = int(self.input1.get())
            num2 = int(self.input2.get())
            num3 = int(self.input3.get())
            L.append(num1)
            L.append(num2)
            L.append(num3)
            result = min(L)
            self.output_result.insert(END, result)
        except:
            self.output_result.insert(END, 'Please check your inputs.')

finals = final_exam(window)

window.mainloop()