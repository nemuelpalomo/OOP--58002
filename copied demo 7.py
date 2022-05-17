from tkinter import *
window = Tk()
window.title("The Grid Manager")
window.geometry("600x200+20+10")

txtfld1 = Entry(window,bd=3,justify="center")
txtfld1.grid(row = 0, column = 0, padx=2)
txtfld1.insert(0,"row 0, column 0")

txtfld2 = Entry(window, bd=3, justify="center")
txtfld2.grid(row=0,column=1, padx=2)
txtfld2.insert(0,"row 0, column 1")
txtfld3 = Entry(window, bd=3, justify="center")
txtfld3.grid(row=0,column=2, padx=2)
txtfld3.insert(0,"row 0, column 2")

txtfld4 = Entry(window, bd=3, justify="center")
txtfld4.grid(row=0,column=3, padx=2)
txtfld4.insert(0,"row 0, column 3")

txtfld5 = Entry(window, bd=3, justify="center")
txtfld5.grid(row=1,column=0, padx=2)
txtfld5.insert(0,"row 1, column 0")

txtfld6 = Entry(window, bd=3, justify="center")
txtfld6.grid(row=1,column=1, padx=2)
txtfld6.insert(0,"row 1, column 1")

txtfld7 = Entry(window, bd=3, justify="center")
txtfld7.grid(row=1,column=2, padx=2)
txtfld7.insert(0,"row 1, column 2")

txtfld8 = Entry(window, bd=3, justify="center")
txtfld8.grid(row=1,column=3, padx=2)
txtfld8.insert(0,"row 1, column 3")

txtfld9 = Entry(window, bd=3, justify="center")
txtfld9.grid(row=2,column=0, padx=2)
txtfld9.insert(0,"row 2, column 0")

txtfld10 = Entry(window, bd=3, justify="center")
txtfld10.grid(row=2,column=1, padx=2)
txtfld10.insert(0,"row 2, column 1")

txtfld11 = Entry(window, bd=3, justify="center")
txtfld11.grid(row=2,column=2, padx=2)
txtfld11.insert(0,"row 2, column 2")

txtfld12 = Entry(window, bd=3, justify="center")
txtfld12.grid(row=2,column=3, padx=2)
txtfld12.insert(0,"row 2, column 3")

#

yscroll = Scrollbar(window,orient=VERTICAL)
yscroll.grid(row=7, column=1,padx=(0,100),pady=5,rowspan=4, sticky=NS)

datalist = "Student1", "Student2", "Student3","Student4","Student5", "Student6", "Student7", "Student8","Student9","Student10"
var= StringVar()

lb = Listbox(window,width=14,height=4,listvariable=var,yscrollcommand=yscroll.set)
lb.grid(row = 7,column=0,rowspan=4,padx=(100,0), pady=5)

var.set(tuple(datalist))
yscroll["command"] = lb.yview

window.mainloop()