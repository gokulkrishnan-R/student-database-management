from tkinter import*
#import tkinter as ttk

#class students:

    #def forms __init__(self):

root=Tk()

students=Label(root,text="students login form",font=("aerial medium",25)) 
students.pack()

def lab_activity():
    lab1=Label(root,text="student name",font=("italic medium",12))
    lab1=Label(root,text="password",font=("italic medium",15))
    lab1.pack()
    lab1.pack()
lab_activity()

def but_actitvity():
    but=Button(root,text="click here",font=("italic small",12),fg="blue")
    but=Button(root,text="click here",font=("italic small",12),fg="blue")
    but.pack()
but_actitvity()
    
def tex_enter():
    txt=Entry(root,text="welcome to the students registration form")
tex_enter()

def combo():
    #combo=Combobox(root)
    #combo["values"]=(1,2,3,4,5,"text")
    #combo.current(3)
    combo()
def radio():
    radbut=Radiobutton(root,text="login",value=1)
    radbut=Radiobutton(root,text="check",value=2)
    radbut=Radiobutton(root,text="done",value=3)
radio()




root.mainloop()
