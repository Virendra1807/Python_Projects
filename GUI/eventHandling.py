from tkinter import *


base = Tk()
base.geometry("500x300")
base.configure(bg="White")
base.title("Event Handling Test")
ft = ("Arial Bold", 12)

def eventMethod1():
    a = v1.get()
    if a==1:
        lb.configure(text="You Selected Male")
    else:
        lb.configure(text="You Selected Female")



def eventMethod2():
    b = txt1.get()
    lb2.configure(text=b)
    
    # base.destroy()

def Reset():
    txt1.delete(0, END)
    lb2.configure(text="")

v1 = IntVar()
v1.set(1)

btn1 = Radiobutton(text="Male", font=ft)
btn1.configure(variable=v1, value=1)
btn1.pack()

btn2 = Radiobutton(text="Female", font=ft)
btn2.configure(variable=v1, value=2)
btn2.pack()

btn3 = Button(text="Submit", font=ft)
btn3.configure(command=eventMethod1)
btn3.pack()

lb = Label(fg="Red", font=ft)
lb.pack()

txt1 = Entry(base, font=ft)
txt1.configure(bg="cyan")
txt1.pack()

btn4 = Button(base, text="TextSubmit")
btn4.configure(command=eventMethod2)
btn4.pack()

btn5 = Button(base, text="Reset")
btn5.configure(command=Reset)
btn5.pack()

lb2 = Label(font=ft)
lb2.pack()



base.mainloop()