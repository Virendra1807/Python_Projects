from tkinter import *

base = Tk()
base.geometry("800x400")
base.title('Login Form')
base.configure(background='cyan')

ttl = Label(text="Login Form", font=("Arial", 15)).grid(row=0, column=1)


lbl= Label(text="Username : ").grid(row=1, column=0)
# lbl.place("500x400")

nameIpt = Entry(base, textvariable="Username Here").grid(row=1, column=1)
# nameInput.pack()

lbl2= Label(text="Password : ").grid(row=2, column=0)
passIpt = Entry(base, textvariable="Enter Password", show="*").grid(row=2, column=1)

btn = Button(base,text="Submit", fg="cyan", bg="blue").grid(row=4, column=1)
# btn.place()


base.mainloop()