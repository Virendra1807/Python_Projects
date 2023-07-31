from tkinter import *

def red():
    print("I am Red")
    base.configure(bg="red")

def cyan():
    print("I am Cyan")
    base.configure(bg="cyan")

def yellow():
    print("I am Yellow")
    base.configure(bg="Yellow")
    
ft = ("Arial Bold", 12)
base = Tk()
base.geometry("700x500")
base.title("Background Colour Chabge")

btn1 = Button(base, text="Red", command=red, font=ft,)
btn1.pack()

btn2 = Button(base, text="cyan", command=cyan, font=ft,)
btn2.pack()

btn3 = Button(base, text="Yellow", command=yellow, font=ft,)
btn3.pack()

base.mainloop()