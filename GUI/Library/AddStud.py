from tkinter import *

base = Tk()
base.configure(bg="teal")
base.geometry("350x420")
base.title("Labrary Management System")
ft = ("Arial Bold ", 10)

title = Label(base, text="Add New Student" , font=("Arial bold", 12, "underline"))
title.configure(fg="black", bg="teal", pady=10)
title.place(x=85, y=10)

lb1 = Label(base, text="Enter Enrl No. : ", bg="teal", font=ft)
lb1.place(x=10, y=60)
enr = Entry(base)
enr.place(x=110 , y=60)
ch1 = Label(base, text="Check",font=ft, fg="blue", bg="teal")
ch1.place(x=240, y=58)

lb2 = Label(base, text="Enter Name : ", bg="teal", font=ft)
lb2.place(x=10, y=110)
name = Entry(base)
name.place(x=110 , y=110)

lb3 = Label(base, text="Mobile No : ", bg="teal", font=ft)
lb3.place(x=10, y=170)
Mob = Entry(base)
Mob.place(x=110 , y=170)

lb4 = Label(base, text="Enter Email : ", bg="teal", font=ft)
lb4.place(x=10, y=230)
Email = Entry(base)
Email.place(x=110 , y=230)

submit = Button(base, text="Submit", fg="black", font=ft)
submit.place(x=120 , y=280 )

home = Button(base, text="Back to Home", fg="red", font=ft)
home.place(x=200 , y=330 )



base.mainloop()