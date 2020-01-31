# students login module using tkinter module

import tkinter

from tkinter import scrolledtext

from tkinter import messagebox

from tkinter.ttk import*

#HEIGHT=700
#WIDTH=800


window=tkinter.Tk()
window.title("students login form")

#defining widgets

def can():
    tkinter

def lab_1():
    tkinter.Label(text="student name:").grid(row=0)
    tkinter.Entry(window).grid(row=0,column=1)
    
lab_1()

def pass_1():
    tkinter.Label(text="password:").grid(row=1)
    tkinter.Entry(window).grid(row=1,column=1)
    
pass_1()

def but_actitvity():
    tkinter.Button(window,text="click here")
    tkinter.Grid()
    grid=column(0),row(0)
    grid=column(1),row(0)

#but_actitvity()

def buttton_actitvity():
    tkinter.Button(window,text="login").grid(row=2,column=1)
    #tkinter.Button(window,command=click)
buttton_actitvity()

def combo():
    combo=Combobox(window)
    combo["values"]=(1,2,3,4,5,"text")
    combo.current(3)
    
combo()



window.mainloop()







