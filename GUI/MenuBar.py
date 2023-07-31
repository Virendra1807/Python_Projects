from tkinter import *

base = Tk()
base.geometry("500x300")
base.title("Menu Bar")
ft = ("Arial bold", 11)

mb = Menu(base)

def add():
    a = int(txt1.get())
    b = int(txt2.get())
    c = a+b
    txt3.insert(0, c)

def sub():
    a = int(txt1.get())
    b = int(txt2.get())
    c = a-b
    txt3.insert(0, c)  
def div():
    a = int(txt1.get())
    b = int(txt2.get())
    c = a/b
    txt3.insert(0, c)
def mul():
    a = int(txt1.get())
    b = int(txt2.get())
    c = a*b
    txt3.insert(0, c)

def maxNum():
    a = int(txt1.get())
    b = int(txt2.get())
    if a>b:
        c = a
        txt3.insert(0, c)
    else:
        c = b
        txt3.insert(0, c)
def minNum():
    a = int(txt1.get())
    b = int(txt2.get())
    if a<b:
        c = a
        txt3.insert(0, c)
    else:
        c = b
        txt3.insert(0, c)  
def equal():
    a = int(txt1.get())
    b = int(txt2.get())
    if a==b:
        txt3.insert(0, "Yes, Numbers are equal")
    else:
        txt3.insert(0, "Np, Numbers Are Not equal")

def notEqual():
    a = int(txt1.get())
    b = int(txt2.get())
    if a==b:
        txt3.insert(0, "Yes, Numbers are equal")
    else:
        txt3.insert(0, "No, Numbers Are Not equal")


m1 = Menu(mb, tearoff=0)
m1.add_command(label="Addition", command=add)
m1.add_command(label="Substraction", command=sub)
m1.add_separator()
m1.add_command(label="Division", command=div)
m1.add_command(label="Multiplication", command=mul)

m2 = Menu(mb, tearoff=0)
m2.add_command(label="Largest", command=maxNum)
m2.add_command(label="Smallest", command=minNum)
m2.add_separator()
m2.add_command(label="Are Equal ?", command=equal)
m2.add_command(label="Are Unequal ?", command=notEqual)

lb1 = Label(base, text="Enter a Number : ", font=ft)
lb1.place(x=20, y=40)
txt1 = Entry(base, width=30, font=ft)
txt1.place(x=150, y=40)

lb2 = Label(base, text="Enter a Number : ", font=ft)
lb2.place(x=20, y=80)
txt2 = Entry(base, width=30, font=ft)
txt2.place(x=150, y=80)

lb3 = Label(base, text="Result : ", font=ft)
lb3.place(x=85, y=120)
txt3 = Entry(base, font=ft, width=30)
txt3.place(x=150, y=120)

def reset():
    txt1.delete(0, END)
    txt2.delete(0, END)
    txt3.delete(0, END)
    txt1.focus()

btn = Button(base, font=ft, text="Reset", command=reset)
btn.place(x=190, y=180)

mb.add_cascade(label="ArithmeticOperations", menu=m1)
mb.add_cascade(label="RelationalOperations", menu=m2)

base.configure(menu=mb)
base.mainloop()