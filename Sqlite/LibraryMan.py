import sqlite3
from tkinter import *
from datetime import date as dt
from tabulate import tabulate
from tkinter import messagebox as ms
from datetime import date as dt
from tkinter import ttk


base = Tk()
base.geometry("450x520")
base.title("Home Page")
ft = ("", 11)

def get_date():
    obj = dt.today()
    d = obj.day
    m = obj.month
    y = obj.year
    today_dt = str(d) + "/" + str(m) + "/" + str(y)
    return today_dt

def addStudent():
    f2 = Frame()
    f2.place(x=0,y=0,width=450,height=520)

    def addNewStud():
        conn = sqlite3.connect("LabMan_db")
        cursor = conn.cursor()
        cursor.execute(f"""CREATE TABLE IF NOT EXISTS all_students(
                                    stud_name varchar NOT NULL,
                                    enrollment varchar PRIMARY KEY,
                                    mob_number varchar,
                                    stud_email varchar
            )""")
        
        nm = txt1.get()
        enr = txt2.get()
        mob = txt3.get()
        email = txt4.get()
        try:
            cursor.execute(f"""Insert into all_students Values('{nm}','{enr}','{mob}','{email}')""")
            conn.commit()
            cursor.execute(f"""SELECT * FROM all_students WHERE enrollment={enr}""")
            data = cursor.fetchone()
            col = ["name", "enrollment", "MobileNumber", "Email"]
            print(tabulate([data], headers=col, tablefmt="fancy_grid"))
            ms.showinfo("Add New Student", "Student Added Successfully")
        
        except:
            ms.showerror("Warning", "Student Already Exists")
            cursor.execute(f"""SELECT * FROM all_students WHERE enrollment={enr}""")
            data = cursor.fetchone()
            nm1 = data[0]
            enr1 = data[1]
            l = Label(f2, text="Existing Student Details",fg="red", font=("", 13, "underline"))
            l.place(x=30 , y=330)
            l1 = Label(f2, text="Name : "+nm1, font=ft, fg="red")
            l1.place(x=40 , y=360)
            l2 = Label(f2, text="Enrl No.: "+ enr1, font=ft, fg="red")
            l2.place(x=40 , y=380)

        cursor.close()
        conn.close()
        txt1.delete(0, END)
        txt2.delete(0, END)
        txt3.delete(0, END)
        txt4.delete(0, END)
        txt1.focus()


    title = Label(f2, text="Add New Student" , font=("Arial bold", 15, "underline"))
    title.configure(fg="black")
    title.place(x=130, y=10)

    lb1 = Label(f2, text="Enter Name :  ", font=ft)
    lb1.place(x=30, y=60)
    txt1 = Entry(f2)
    txt1.place(x=140 , y=60, width=200)
    txt1.focus()
    
    lb2 = Label(f2, text="Enter Enrl No. :", font=ft)
    lb2.place(x=30, y=110)
    txt2 = Entry(f2)
    txt2.place(x=140 , y=110, width=200)

    lb3 = Label(f2, text="Mobile No : ", font=ft)
    lb3.place(x=30, y=170)
    txt3 = Entry(f2)
    txt3.place(x=140 , y=170, width=200)

    lb4 = Label(f2, text="Enter Email : ", font=ft)
    lb4.place(x=30, y=230)
    txt4 = Entry(f2)
    txt4.place(x=140 , y=230, width=200)

    s = Button(f2, text="Submit", fg="black", font=ft, command= addNewStud)
    s.place(x=140 , y=280)

    h = Button(f2, text="Back to Home", fg="red", font=ft)
    h.configure(command=home)
    h.place(x=300 , y=330)

# =================================================================================
def addBook():
    f3 = Frame()
    f3.place(x=0,y=0,width=450,height=520)
    
    def addNewBook():
        conn = sqlite3.connect("LabMan_db")
        cursor = conn.cursor()
        cursor.execute(f"""CREATE TABLE IF NOT EXISTS all_books(
                                BookTitle Varchar NOT NULL,
                                BookNumber Varchar PRIMARY KEY,
                                BookAuthor varchar,
                                BookPublication Varchar )""")

        title1 = txt1.get()
        bookno1 = txt2.get()
        bookauthor1 = txt3.get()
        bookpubli1 = txt4.get()

        try:
            cursor.execute(f"""Insert into all_books Values('{title1}','{bookno1}','{bookauthor1}','{bookpubli1}')""")
            conn.commit()
            ms.showinfo("Confirmation Box", "Books Added Successfully")

        except:
            ms.showwarning("Warning Msg", "Book Number Already Exists")
            cursor.execute(f"""SELECT * FROM all_books WHERE BookNumber={bookno1}""")
            data = cursor.fetchone()
            nm1 = data[0]
            bId = data[1]
            l = Label(f3, text="Existing Books Details",fg="red", font=("", 13, "underline"))
            l.place(x=30 , y=330)
            l1 = Label(f3, text="Title : "+nm1, font=ft, fg="red")
            l1.place(x=40 , y=360)
            l2 = Label(f3, text="Book Id : "+ bId, font=ft, fg="red")
            l2.place(x=40 , y=380)

        cursor.close()
        conn.close()
        txt1.delete(0, END)
        txt2.delete(0, END)
        txt3.delete(0, END)
        txt4.delete(0, END)
        txt1.focus()


    title = Label(f3, text="   Add New Book " , font=("Arial bold", 15, "underline"))
    title.configure(fg="black")
    title.place(x=130, y=10)

    lb1 = Label(f3, text="Book Title :  ", font=ft)
    lb1.place(x=30, y=60)
    txt1 = Entry(f3)
    txt1.place(x=140 , y=60, width=200)
    txt1.focus()
    
    lb2 = Label(f3, text="Book Number :", font=ft)
    lb2.place(x=30, y=110)
    txt2 = Entry(f3)
    txt2.place(x=140 , y=110, width=200)

    lb3 = Label(f3, text="Book Author : ", font=ft)
    lb3.place(x=30, y=170)
    txt3 = Entry(f3)
    txt3.place(x=140 , y=170, width=200)

    lb4 = Label(f3, text="Book Publction : ", font=ft)
    lb4.place(x=30, y=230)
    txt4 = Entry(f3)
    txt4.place(x=140 , y=230, width=200)

    s = Button(f3, text="Submit", fg="black", font=ft, command=addNewBook)
    s.place(x=140 , y=280)

    h = Button(f3, text="Back to Home", fg="red", font=ft)
    h.configure(command=home)
    h.place(x=300 , y=330)

# =================================================================================
def issueBook():
    f4 = Frame()
    f4.place(x=0, y=0, height=520, width=450)

    def SubIssue():
        conn = sqlite3.connect("LabMan_db") 
        cursor = conn.cursor()


        
        cursor.execute(f"""CREATE TABLE IF NOT EXISTS all_issues(
                                Student_id Varchar unique,
                                Book_id varchar NOT NULL,
                                Book_title VARCHAR NOT NULL,
                                Issue_date varchar,
                                Return_date varchar default pending )""")
        sId = txt1.get()
        bId = txt2.get()
        btitle = txt3.get()
        i_date = get_date()
        try:
            print("In TRY")
            cursor.execute(f"""INSERT INTO all_issues ('Student_id', 'Book_id', 'Book_title', 'Issue_date') Values('{sId}', '{bId}', '{btitle}', '{i_date}')""")
            print("AFTER INSERT")
            conn.commit()
            ms.showinfo("Issue Book", "Book Issued Successfully")

        except:
            ms.showwarning("WARNING", "You have already Borrowed a Book \n Return it and Borrow a New Book ")

        cursor.close()
        conn.close()

        txt1.delete(0, END)
        txt2.delete(0, END)
        txt3.delete(0, END)
        txt1.focus()

    title = Label(f4, text="    Issue a Book " , font=("Arial bold", 15, "underline"))
    title.configure(fg="black")
    title.place(x=130, y=10)

    lb1 = Label(f4, text="Stud Enrl :  ", font=ft)
    lb1.place(x=30, y=60)
    txt1 = Entry(f4)
    txt1.place(x=140 , y=60, width=200)
    txt1.focus()
    
    lb2 = Label(f4, text="Book Number :", font=ft)
    lb2.place(x=30, y=110)
    txt2 = Entry(f4)
    txt2.place(x=140 , y=110, width=200)

    lb3 = Label(f4, text="Book Title : ", font=ft)
    lb3.place(x=30, y=170)
    txt3 = Entry(f4)
    txt3.place(x=140 , y=170, width=200)

    s = Button(f4, text="Issue Book", fg="black", font=ft, command=SubIssue)
    s.place(x=140 , y=230)

    h = Button(f4, text="Back to Home", fg="red", font=ft)
    h.configure(command=home)
    h.place(x=300 , y=330)
# =================================================================================

def returnBook():
    f5 = Frame()
    f5.place(x=0, y=0,height=520, width=450)

    def SubReturnBook():
        conn = sqlite3.connect("LabMan_db")
        cursor = conn.cursor()
        ret_date = get_date()
        sId = txt1.get()

        try:
            cursor.execute(f"""Update all_issues SET Return_date ='{ret_date}' Where Student_id ='{sId}'""")
            conn.commit()
            ms.showinfo("Return Box", "Book Return Successfully \n Now You can Borrow new Book")
        except:
            ms.showerror("Error Box", "Something went wrong during processing")

        cursor.close()
        conn.close()
        txt1.delete(0, END)
        txt2.delete(0, END)
        txt3.delete(0, END)
        txt1.focus()


    title = Label(f5, text="   Return a Book " , font=("Arial bold", 15, "underline"))
    title.configure(fg="black")
    title.place(x=130, y=10)

    lb1 = Label(f5, text="Student Enrl :  ", font=ft)
    lb1.place(x=30, y=60)
    txt1 = Entry(f5)
    txt1.place(x=140 , y=60, width=200)
    txt1.focus()
    
    lb2 = Label(f5, text="Book Number :", font=ft)
    lb2.place(x=30, y=110)
    txt2 = Entry(f5)
    txt2.place(x=140 , y=110, width=200)

    lb3 = Label(f5, text="Book Title : ", font=ft)
    lb3.place(x=30, y=170)
    txt3 = Entry(f5)
    txt3.place(x=140 , y=170, width=200)

    s = Button(f5, text="Return Book", fg="black", font=ft, command=SubReturnBook)
    s.place(x=140 , y=230)

    h = Button(f5, text="Back to Home", fg="red", font=ft)
    h.configure(command=home)
    h.place(x=300 , y=330)
# =================================================================================
def bookHistory():
    f6 = Frame()
    f6.place(x=0, y=0, height=520, width=450)

    def subBookHistory():
        conn = sqlite3.connect("LabMan_db")
        cursor = conn.cursor()
        bId = txt1.get()
        cursor.execute(f"""SELECT * FROM all_issues Where Book_id ='{bId}';""")
        # Rcount = cursor.rowcount
        rows = cursor.fetchall()
        HistoryTableBase = Frame()
        HistoryTableBase.place(x=0, y=0, height=520, width=450)
        
        table = ttk.Treeview(HistoryTableBase, columns=("c1","c2","c3","c4"), show="headings")
        table.column("#1",anchor=CENTER,width=20 )
        table.heading("#1", text="Student Id")
        table.column("#2",anchor=CENTER,width=20)
        table.heading("#2", text="Book Id")
        table.column("#3",anchor=CENTER,width=20)
        table.heading("#3", text="Title")
        table.column("#4",anchor=CENTER,width=20)
        table.heading("#4", text="Issue Date")
        table.place(x=0, y=0, height=520, width=450)
        count = 0
        for i in rows:
            table.insert(parent="",index=0, values=i)
            count += 1
        if count == 0:
            Blank = Label(table,fg="red", text="No data for this Book")
            Blank.place(x=160, y=50)

        h = Button(table, text="Back to Home", fg="red", font=ft)
        h.configure(command=home)
        h.place(x=300 , y=330)
        cursor.close()
        conn.close()

    title = Label(f6, text="  Book History " , font=("Arial bold", 15, "underline"))
    title.configure(fg="black")
    title.place(x=130, y=10)

    lb1 = Label(f6, text="Book Number :  ", font=ft)
    lb1.place(x=30, y=60)
    txt1 = Entry(f6)
    txt1.place(x=140 , y=60, width=200)
    txt1.focus()
    
    lb2 = Label(f6, text="Book Title :", font=ft)
    lb2.place(x=30, y=110)
    txt2 = Entry(f6)
    txt2.place(x=140 , y=110, width=200)

    lb3 = Label(f6, text="Book Publction : ", font=ft)
    lb3.place(x=30, y=170)
    txt3 = Entry(f6)
    txt3.place(x=140 , y=170, width=200)

    s = Button(f6, text="Show Hisroty", fg="black", font=ft, command=subBookHistory)
    s.place(x=140 , y=230)

    h = Button(f6, text="Back to Home", fg="red", font=ft)
    h.configure(command=home)
    h.place(x=300 , y=330)
# =================================================================================
def notRetBook():
        conn = sqlite3.connect("LabMan_db")
        cursor = conn.cursor()
        cursor.execute(f"""SELECT * FROM all_issues Where Return_date = '{"pending"}';""")
        # Rcount = cursor.rowcount
        rows = cursor.fetchall()
        NoRetBookTableBase = Frame()
        NoRetBookTableBase.place(x=0, y=0, height=520, width=450)
        
        table = ttk.Treeview(NoRetBookTableBase, columns=("c1","c2","c3","c4"), show="headings")
        table.column("#1",anchor=CENTER,width=20 )
        table.heading("#1", text="Student Id")
        table.column("#2",anchor=CENTER,width=20)
        table.heading("#2", text="Book Id")
        table.column("#3",anchor=CENTER,width=20)
        table.heading("#3", text="Title")
        table.column("#4",anchor=CENTER,width=20)
        table.heading("#4", text="Issue Date")
        table.place(x=0, y=0, height=520, width=450)
        count = 0
        for i in rows:
            table.insert(parent="",index=0, values=i)
            count += 1
        if count == 0:
            Blank = Label(table,fg="red", text="No data for this Book")
            Blank.place(x=160, y=30)

        h = Button(table, text="Back to Home", fg="red", font=ft)
        h.configure(command=home)
        h.place(x=300 , y=330)
        cursor.close()
        conn.close()
#==================================================================================
def studHistory():
    f7 = Frame()
    f7.place(x=0, y=0,height=520, width=450)

    def showHistory():
        conn = sqlite3.connect("LabMan_db")
        cursor = conn.cursor()
        sId = txt1.get()

        cursor.execute(f"""SELECT * FROM all_issues Where Student_id = '{sId}';""")
        # Rcount = cursor.rowcount
        rows = cursor.fetchall()
        NoRetBookTableBase = Frame()
        NoRetBookTableBase.place(x=0, y=0, height=520, width=450)
        
        table = ttk.Treeview(NoRetBookTableBase, columns=("c1","c2","c3","c4"), show="headings")
        table.column("#1",anchor=CENTER,width=20 )
        table.heading("#1", text="Student Id")
        table.column("#2",anchor=CENTER,width=20)
        table.heading("#2", text="Book Id")
        table.column("#3",anchor=CENTER,width=20)
        table.heading("#3", text="Title")
        table.column("#4",anchor=CENTER,width=20)
        table.heading("#4", text="Issue Date")
        table.place(x=0, y=0, height=520, width=450)
        count = 0
        for i in rows:
            table.insert(parent="",index=0, values=i)
            count += 1
        if count == 0:
            Blank = Label(table,fg="red", text="No data for this Student")
            Blank.place(x=160, y=30)

        h = Button(table, text="Back to Home", fg="red", font=ft)
        h.configure(command=home)
        h.place(x=300 , y=330)

        cursor.close()
        conn.close()

    title = Label(f7, text="  Student History  " , font=("Arial bold", 15, "underline"))
    title.configure(fg="black")
    title.place(x=130, y=10)

    lb2 = Label(f7, text="Enrollment No. :", font=ft)
    lb2.place(x=30, y=110)
    txt1 = Entry(f7)
    txt1.place(x=140 , y=110, width=200)

    lb3 = Label(f7, text="Student Name : ", font=ft)
    lb3.place(x=30, y=170)
    txt2 = Entry(f7)
    txt2.place(x=140 , y=170, width=200)

    s = Button(f7, text="Show History", fg="black", font=ft, command=showHistory)
    s.place(x=140 , y=230)

    h = Button(f7, text="Back to Home", fg="red", font=ft)
    h.configure(command=home)
    h.place(x=300 , y=330)

#==================================================================================
def delStudData():
    f8 = Frame()
    f8.place(x=0, y=0, width=450, height=520)
    def deleteBtn():
        conn = sqlite3.connect("LabMan_db")
        cursor = conn.cursor()
        sId = txt1.get()
        cursor.execute(f"""Delete from all_students Where enrollment = '{sId}'""")
        conn.commit()
        ms.showinfo("DeleteBox", "Student Data Deleted")
        cursor.close()
        conn.close()

    title = Label(f8, text="  Delete Student  " , font=("Arial bold", 15, "underline"))
    title.configure(fg="black")
    title.place(x=130, y=10)

    lb2 = Label(f8, text="Enrollment No. :", font=ft)
    lb2.place(x=30, y=110)
    txt1 = Entry(f8)
    txt1.place(x=140 , y=110, width=200)

    lb3 = Label(f8, text="Student Name : ", font=ft)
    lb3.place(x=30, y=170)
    txt2 = Entry(f8)
    txt2.place(x=140 , y=170, width=200)

    s = Button(f8, text="Delete Data", fg="black", font=ft, command=deleteBtn)
    s.place(x=140 , y=230)

    h = Button(f8, text="Back to Home", fg="red", font=ft)
    h.configure(command=home)
    h.place(x=300 , y=330)
# ================================================================================
def delBookData():
    f9 = Frame()
    f9.place(x=0, y=0, width=450, height=520)
    def deleteBtn():
        conn = sqlite3.connect("LabMan_db")
        cursor = conn.cursor()
        bId = txt1.get()
        cursor.execute(f"""Delete from all_books Where BookNumber = '{bId}'""")
        conn.commit()
        ms.showinfo("DeleteBox", "Book Data Deleted")
        cursor.close()
        conn.close()

    title = Label(f9, text="    Delete Book  " , font=("Arial bold", 15, "underline"))
    title.configure(fg="black")
    title.place(x=130, y=10)

    lb2 = Label(f9, text="Book Number :", font=ft)
    lb2.place(x=30, y=110)
    txt1 = Entry(f9)
    txt1.place(x=140 , y=110, width=200)

    lb3 = Label(f9, text="Book Title  : ", font=ft)
    lb3.place(x=30, y=170)
    txt2 = Entry(f9)
    txt2.place(x=140 , y=170, width=200)

    s = Button(f9, text="Delete Data", fg="black", font=ft, command=deleteBtn)
    s.place(x=140 , y=230)

    h = Button(f9, text="Back to Home", fg="red", font=ft)
    h.configure(command=home)
    h.place(x=300 , y=330)

# =================================================================================
def home():
    f1 = Frame()
    f1.place(x=0,y=0, height=520, width=450)

    title = Label(f1, text="~ Labrary Management System ~" , font=("Arial bold", 15, "underline"))
    title.configure(fg="black")
    title.place(x=70, y=10)

    btn1 = Button(f1, text="Add Student" , font=ft, fg="black", bg="white", command=addStudent)
    btn1.place(x=100, y=100)

    btn2 = Button(f1, text="Add a Book" , font=ft, fg="black", bg="white", command=addBook)
    btn2.place(x=245, y=100)

    btn3 = Button(f1, text="Issue Book" , font=ft, fg="black", bg="White", command=issueBook)
    btn3.place(x=40, y=150)

    btn4 = Button(f1, text="Return Book" , font=ft, fg="black", bg="white", command=returnBook)
    btn4.place(x=165, y=150)

    btn5 = Button(f1, text="Book History" , font=ft, fg="black", bg="white", command=bookHistory)
    btn5.place(x=300, y=150)

    btn6 = Button(f1, text="Not Returned Book" , font=ft, fg="black", bg="white", command=notRetBook)
    btn6.place(x=80, y=200)

    btn7 = Button(f1, text="Student History" , font=ft, fg="black", bg="white", command=studHistory)
    btn7.place(x=235, y=200)

    del1 = Button(f1, text="Delete Student", font=ft, bg="White", command=delStudData)
    del1.place(x=110, y=250)

    del2 = Button(f1, text="Delete Book", font=ft, bg="White", command=delBookData)
    del2.place(x=230, y=250)
    
    def eventExit(event):
        f1.destroy()
        base.destroy()

    exit = Button(f1, text="Exit", font=ft, fg="Red", bg="White")
    exit.bind("<Button-1>", eventExit)
    exit.place(x=360, y=330)

home()
base.mainloop()