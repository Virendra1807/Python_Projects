from tkinter import *

base = Tk()
base.configure(bg="teal")
base.geometry("350x420")
base.title("Labrary Management System")
ft = ("Arial Bold ", 10)

title = Label(base, text=" Issue Book " , font=("Arial bold", 12, "underline"))
title.configure(fg="black", bg="teal", pady=10)
title.place(x=120, y=10)

lb1 = Label(base, text="Enter book No. : ", bg="teal", font=ft)
lb1.place(x=10, y=80)
bnum = Entry(base)
bnum.place(x=110 , y=80)
ch1 = Label(base, text="Check",font=ft, fg="blue", bg="teal")
ch1.place(x=240, y=78)

# lb2 = Label(base, text="Book Title : ", bg="teal", font=ft)
# lb2.place(x=10, y=110)
# btitle = Entry(base)
# btitle.place(x=110 , y=110)

lb3 = Label(base, text="Enrollment No. : ", bg="teal", font=ft)
lb3.place(x=10, y=170)
bauth = Entry(base)
bauth.place(x=110 , y=170)

# lb4 = Label(base, text="Book Publcn : ", bg="teal", font=ft)
# lb4.place(x=10, y=230)
# bpubl = Entry(base)
# bpubl.place(x=110 , y=230)

issueBtn = Button(base, text="Issue Book", fg="black", font=ft)
issueBtn.place(x=120 , y=230 )

home = Button(base, text="Back to Home", fg="red", font=ft)
home.place(x=200 , y=330 )



base.mainloop()