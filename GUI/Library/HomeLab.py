from tkinter import *
from datetime import date as dt

def get_date():
    obj = dt.today()
    d = obj.day
    m = obj.month
    y = obj.year
    today_dt = str(d) + "/" + str(m) + "/" + str(y)
    return today_dt

homeBase = Tk()




def issue_book():
    
    issueBookBase = Tk()
    issueBookBase.configure(bg="teal")
    issueBookBase.geometry("350x420")
    issueBookBase.title("Library Management System")
    ft = ("Arial Bold ", 10)

    title = Label(issueBookBase, text=" Issue Book " , font=("Arial bold", 12, "underline"))
    title.configure(fg="black", bg="teal", pady=10)
    title.place(x=120, y=10)

    e = Label(issueBookBase, text="Enter Enrl No. : ", bg="teal", font=ft)
    e.place(x=10, y=80)
    enum = Entry(issueBookBase)
    enum.place(x=110 , y=80)
    # ch1 = Label(issueBookBase, text="Check",font=ft, fg="blue", bg="teal")
    # ch1.place(x=240, y=78)

    # lb2 = Label(isuueBookBase, text="Book Title : ", bg="teal", font=ft)
    # lb2.place(x=10, y=110)
    # btitle = Entry(isuueBookBase)
    # btitle.place(x=110 , y=110)

    lb3 = Label(issueBookBase, text="Enrollment No. : ", bg="teal", font=ft)
    lb3.place(x=10, y=170)
    bauth = Entry(issueBookBase)
    bauth.place(x=110 , y=170)

    issueBtn = Button(issueBookBase, text="Issue Book", fg="black", font=ft)
    issueBtn.place(x=120 , y=230 )

    h = Button(issueBookBase, text="Exit", fg="red", font=ft, command=homefun)
    # h.bind("Button-1", home)
    h.place(x=200 , y=330 )

    # homeBase.destroy()
    issueBookBase.mainloop()


def homefun():
    homeBase.configure(bg="teal")
    homeBase.geometry("350x420")
    homeBase.title("Labrary Management System")
    ft = ("Arial", 10)

    title = Label(homeBase, text="~Labrary Management System~" , font=("Arial bold", 10, "underline"))
    title.configure(fg="black", bg="teal", pady=10)
    title.place(x=55, y=10)

    btn3 = Button(homeBase, text="Add Student" , font=ft, fg="black", bg="white")
    # btn1.configure(command=add_stud)
    btn3.place(x=50, y=60)

    btn4 = Button(homeBase, text="Add a Book" , font=ft, fg="black", bg="white")
    # btn1.configure(command=add_book)
    btn4.place(x=165, y=60)

    IssueBtn = Button(homeBase, text="Issue Book" , font=ft, fg="black", bg="White", command = issue_book)
    # IssueBtn.configure()
    IssueBtn.place(x=20, y=110)

    btn2 = Button(homeBase, text="Return Book" , font=ft, fg="black", bg="white")
    # btn1.configure(command=return_book)
    btn2.place(x=100, y=110)


    btn6 = Button(homeBase, text="Book History" , font=ft, fg="black", bg="white", )
    # btn1.configure(command=book_history)
    btn6.place(x=190, y=110)

    btn5 = Button(homeBase, text="Not Returned Book" , font=ft, fg="black", bg="white")
    # btn1.configure(command=show_not_ret_books)
    btn5.place(x=30, y=160)

    btn7 = Button(homeBase, text="Student History" , font=ft, fg="black", bg="white")
    # btn1.configure(command=stud_history)
    btn7.place(x=160, y=160)


    exit = Button(homeBase, text="Exit", font=ft, fg="Red", bg="White")
    exit.place(x=230, y=220)

    
    # issueBookBase.destroy()

    homeBase.mainloop()

homefun()


