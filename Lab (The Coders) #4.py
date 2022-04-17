from tkinter import *

#Palomo, Nemuel Rico O.

class ListBox:

    def __init__(self, window):
        self.list = Listbox(window, width=29, height=5)
        self.list.pack(pady=15)
        self.list.place(x=125, y=5)
        self.list.insert(END, "reading")
        self.list.insert(END, "writing")
        self.list.insert(END, "arithmetic")
        self.list.insert(END, "coding")


window = Tk()
mywin = ListBox(window)
window.title('Major Subjects (The Coders)')
window.geometry("430x100+10+10")
window.mainloop()