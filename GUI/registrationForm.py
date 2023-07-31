from tkinter import *

base = Tk()
base.geometry("500x600")
base.title("Student Registration Form")
# base.configure(background='')

v1 = IntVar()
v1.set(1)

# ft = ("Arial bold", 15)

ttl = Label(text="Login Form", font=("Arial", 15))
ttl.place(x=70, y=10)

lbl= Label(text="Name : ")
lbl.place(x= 40, y=50)

nameIpt = Entry(base, textvariable="Username Here")
nameIpt.place(x=90, y=50)

lbl2= Label(text="Mob No. : ")
lbl2.place(x=40, y=70)

passIpt = Entry(base, textvariable="Enter Password", show="*")
passIpt.place(x=100, y=70)

ch1 = Radiobutton(base, text="Male", variable=v1, value=1)
ch1.place(x=40, y=100)

ch2 = Radiobutton(base, text="Female", variable=v1, value=2)
ch2.place(x=130, y=100)

btn = Button(base,text="Submit", fg="black", bg="White")
btn.place(x=70, y=140)


base.mainloop()