from tkinter import *
import sqlite3
from tkinter import messagebox as ms
from tabulate import tabulate 

ft = ("", 11)
mainBase = Tk()
mainBase.geometry("350x420")
mainBase.title("Home Page")

v1 = IntVar()

def eventmethod1(e):
    print("Book")
    book_Table()

def eventmethod2(e):
    print("Acc")
    acc_Table()

def eventmethod3(e):
    print("Home")
    home()

#========================================================================================
def home():
    base = Frame()
    base.place(x=0,y=0, height=420, width=350 )

    lb = Label(base, text="Select table : ", font=ft )
    lb.place(x=10, y=10)

    bradio = Radiobutton(base, text="Book Table", font=ft, variable=v1, value=1)
    bradio.bind("<Button-1>", eventmethod1)
    bradio.place(x=100, y=10)

    aradio = Radiobutton(base, text="Account Table", font=ft, variable=v1, value=2)
    aradio.bind("<Button-1>", eventmethod2)
    aradio.place(x=210, y=10)

    lb1 = Label(base, text=".................. : ", font=ft)
    lb1.place(x=40, y=50)
    txt1 = Entry(base, font=ft)
    txt1.place(x=140, y=50)

    lb2 = Label(base, text=".................. : ", font=ft)
    lb2.place(x=40, y=90)
    txt2 = Entry(base, font=ft)
    txt2.place(x=140, y=90)

    lb3 = Label(base, text=".................. : ", font=ft)
    lb3.place(x=40, y=130)
    txt3 = Entry(base, font=ft)
    txt3.place(x=140, y=130)

    lb4 = Label(base, text=".................. : ", font=ft)
    lb4.place(x=40, y=170)
    txt4 = Entry(base, font=ft)
    txt4.place(x=140, y=170)

    demo1 = Button(base, text="  Add Record  ",font=ft)
    demo1.place(x=60, y=230)

    demo2 = Button(base, text="Delete Record",font=ft)
    demo2.place(x=180, y=230)

    demo3 = Button(base, text="Update Record",font=ft)
    demo3.place(x=60, y=270)

    demo4 = Button(base, text="Fetch Record",font=ft)
    demo4.place(x=180, y=270)

home()

# ==============================  Book Table  ===============================================
def book_Table():
    v1.set(1)
    f1 = Frame()
    f1.place(x=0, y=0, height=420, width=350)

    def addBookRec():
        conn = sqlite3.connect("Book_Acc_db")
        cursor = conn.cursor()
        
        cursor.execute(f"""CREATE TABLE IF NOT EXISTS books (
                                Bnumber varchar , 
                                Btitle varchar,
                                Bauthor varchar,
                                Bpublication varchar )""")
         
        bnum = txt1.get()
        btitle = txt2.get()
        bauth = txt3.get()
        bpubli = txt4.get()
        try:
            cursor.execute(f"""INSERT INTO books Values("{bnum}", "{btitle}", "{bauth}", "{bpubli}")""")
            conn.commit()

            cursor.execute(f"""SELECT * FROM books WHERE Bnumber={bnum}""")
            data = cursor.fetchone()
            col = ['Book Num', 'Title', 'Author', 'Publication']
            # print(data[0]+"\t\t"+ data[1]+"\t\t"+data[2]+"\t\t"+data[3])
            print(tabulate([data], headers=col, tablefmt="fancy_grid"))
            ms.showinfo("Message Box", "Data Saved Successfully")

        except:
            ms.showwarning("Warning", "Book Number Already Exists")

        cursor.close()
        conn.close()

        txt1.delete(0,END)
        txt2.delete(0,END)
        txt3.delete(0,END)
        txt4.delete(0,END)
        txt1.focus()
        print("SUCEESSFULLY RUN")

    
    def delBookRec():
        
        conn = sqlite3.connect("Book_Acc_db")
        cursor = conn.cursor()

        bnum = txt1.get()
        btitle = txt2.get()
        bauth = txt3.get()
        bpubli = txt4.get()
        cursor.execute(f"""Delete From books Where Bnumber={bnum}""")
        conn.commit()

        print("Record Deleted")
        print(bnum+"\t\t"+ btitle+"\t\t"+bauth+"\t\t"+bpubli)

        cursor.close()
        conn.close()

        ms.showinfo("Message Box", "Data Deleted Successfully")
        txt1.delete(0,END)
        txt2.delete(0,END)
        txt3.delete(0,END)
        txt4.delete(0,END)
        txt1.focus()

    def upBookRec():
        conn = sqlite3.connect("Book_Acc_db")
        cursor = conn.cursor()

        bnum = txt1.get()
        btitle = txt2.get()
        bauth = txt3.get()
        bpubli = txt4.get()

        print(bnum + btitle + bauth + bpubli)

        cursor.execute(f"""Update books Set Btitle="{btitle}", Bauthor="{bauth}", Bpublication="{bpubli}" Where Bnumber="{bnum}";""")
        print("After Updating")
        conn.commit()
        cursor.execute(f"""SELECT * FROM books WHERE Bnumber={bnum}""")
        data = cursor.fetchone()
        col = ['Book No', 'Title', 'Author', 'Publication']
        # print(data[0]+"\t\t"+ data[1]+"\t\t"+data[2]+"\t\t"+data[3])
        print(tabulate([data], headers=col, tablefmt="fancy_grid"))
        
        cursor.close()
        conn.close()

        ms.showinfo("Update Box", "Information Updated Successfully")
        txt1.delete(0, END)
        txt2.delete(0,END)
        txt3.delete(0,END)
        txt4.delete(0,END)
        txt1.focus()

    def fetchRec():
        conn = sqlite3.connect("Book_Acc_db")
        cursor = conn.cursor()
        bnum = txt1.get()

        cursor.execute(f"""Select * from books where Bnumber={bnum}""")
        data = cursor.fetchone()

        ms.showinfo("Fetch Info", f"""Book No.: {data[0]},\n Title : {data[1]}, \n Author : {data[2]},\n Publication : {data[3]}""")

        cursor.close()
        conn.close()

        txt1.delete(0, END)
        txt2.delete(0, END)
        txt3.delete(0, END)
        txt4.delete(0, END)
        txt1.focus()

    lb = Label(f1, text="Select table : ", font=ft )
    lb.place(x=10, y=10)

    bradio = Radiobutton(f1, text="Book Table", font=ft, variable=v1, value=1)
    bradio.bind("<Button-1>", eventmethod1)
    bradio.place(x=100, y=10)

    aradio = Radiobutton(f1, text="Account Table", font=ft, variable=v1, value=2)
    aradio.bind("<Button-1>", eventmethod2)
    aradio.place(x=210, y=10)

    lb1 = Label(f1, text="Book Number : ", font=ft)
    lb1.place(x=40, y=50)
    txt1 = Entry(f1, font=ft)
    txt1.place(x=140, y=50)

    lb2 = Label(f1, text="Book Title : ", font=ft)
    lb2.place(x=40, y=90)
    txt2 = Entry(f1, font=ft)
    txt2.place(x=140, y=90)

    lb3 = Label(f1, text="Book Author : ", font=ft)
    lb3.place(x=40, y=130)
    txt3 = Entry(f1, font=ft)
    txt3.place(x=140, y=130)

    lb4 = Label(f1, text="B Publication : ", font=ft)
    lb4.place(x=40, y=170)
    txt4 = Entry(f1, font=ft)
    txt4.place(x=140, y=170)

    AddBtn = Button(f1, text="  Add Record  ",font=ft, command=addBookRec)
    AddBtn.place(x=60, y=230)

    DelBtn = Button(f1, text="Delete Record",font=ft, command=delBookRec)
    DelBtn.place(x=180, y=230)

    UpBtn = Button(f1, text="Update Record",font=ft, command=upBookRec)
    UpBtn.place(x=60, y=270)

    FetchBtn = Button(f1, text="Fetch Record",font=ft, command=fetchRec)
    FetchBtn.place(x=180, y=270)

    back = Button(f1, text="Home", font=ft)
    back.bind("<Button-1>", eventmethod3)
    back.place(x=4, y=380)



# =====================================================================================
def acc_Table():
    v1.set(2)
    f2 = Frame()
    f2.place(x=0, y=0, height=420, width=350)

    def addAccRec():
        conn = sqlite3.connect("Book_Acc_db")
        cursor = conn.cursor()

        cursor.execute(f"""CREATE TABLE IF NOT EXISTS account (
                                Hname varchar,
                                Accnumber varchar,
                                Mobnumber varchar,
                                Eaddress varchar )""")
        nm = txt1.get()
        acc = txt2.get()
        mob = txt3.get()
        email = txt4.get()
        try:
            cursor.execute(f"""INSERT INTO account VALUES ("{nm}", "{acc}", "{mob}", "{email}")""")
            conn.commit()

            cursor.execute(f"""SELECT * FROM account Where Accnumber={acc}""")
            data = cursor.fetchone()
            col = ['Name', 'AccNo', 'MobNo', 'Email']
            # print(data[0]+"\t\t"+ data[1]+"\t\t"+data[2]+"\t\t"+data[3])
            print(tabulate([data], headers=col, tablefmt="psql"))
            ms.showinfo("Insert Box", "Data Inserted Successfully")
        except:
            ms.showwarning("Warning", " Holder Already Exists")

        cursor.close()
        conn.close()

        txt1.delete(0, END)
        txt2.delete(0, END)
        txt3.delete(0, END)
        txt4.delete(0, END)
        txt1.focus()

    def delAccRec():
        conn = sqlite3.connect("Book_Acc_db")
        cursor = conn.cursor()

        nm = txt1.get()
        acc = txt2.get()
        mob = txt3.get()
        email = txt4.get()

        cursor.execute(f"""Delete from account where Accnumber={acc}""")
        conn.commit()

        cursor.close()
        conn.close()
        ms.showinfo("Delete Box", f"""Info Deleted \n Name:{nm}\n Mob:{mob} \n Email:{email}""")
        txt1.delete(0, END)
        txt2.delete(0, END)
        txt3.delete(0, END)
        txt4.delete(0, END)
        txt1.focus()

    def upAccRec():
        conn = sqlite3.connect("Book_Acc_db")
        cursor = conn.cursor()
        nm = txt1.get()
        acc = txt2.get()
        mob = txt3.get()
        email = txt4.get()

        cursor.execute(f"""Update account SET Hname="{nm}", Mobnumber="{mob}", Eaddress="{email}" Where Accnumber="{acc}";""")
        conn.commit()
        cursor.execute(f"""Select * from account Where Accnumber={acc}""")
        data = cursor.fetchone()
        col = ['Name', 'Acc No', 'Mob No', 'Email']
        print(tabulate([data], headers=col, tablefmt="fancy_grid"))

        cursor.close()
        conn.close()

        ms.showinfo("Update Box", "Information Updated Successfully")
        txt1.delete(0, END)
        txt2.delete(0, END)
        txt3.delete(0, END)
        txt4.delete(0, END)
        txt1.focus()

    def fetchAccRec():
        conn = sqlite3.connect("Book_Acc_db")
        cursor = conn.cursor()
        acc = txt2.get()

        cursor.execute(f"""SELECT * FROM account Where Accnumber={acc}""")
        data = cursor.fetchone()
        col = ['Name', 'AccNo', 'MobNo', 'Email']
        print(tabulate([data], headers=col, tablefmt="fancy_grid"))

        cursor.close()
        conn.close()

        ms.showinfo("Fetch Box", f"""Name : {data[0]} \n MobNo : {data[2]}""")
        txt1.delete(0, END)
        txt2.delete(0, END)
        txt3.delete(0, END)
        txt4.delete(0, END)
        txt1.focus()


    lb = Label(f2, text="Select table : ", font=ft )
    lb.place(x=10, y=10)

    bradio = Radiobutton(f2, text="Book Table", font=ft, variable=v1, value=1)
    bradio.bind("<Button-1>", eventmethod1)
    bradio.place(x=100, y=10)

    aradio = Radiobutton(f2, text="Account Table", font=ft, variable=v1, value=2)
    aradio.bind("<Button-1>", eventmethod2)
    aradio.place(x=210, y=10)

    lb1 = Label(f2, text="Holder Name : ", font=ft)
    lb1.place(x=40, y=50)
    txt1 = Entry(f2, font=ft)
    txt1.place(x=140, y=50)

    lb2 = Label(f2, text="Acc Number  : ", font=ft)
    lb2.place(x=40, y=90)
    txt2 = Entry(f2, font=ft)
    txt2.place(x=140, y=90)

    lb3 = Label(f2, text="Mobile No. : ", font=ft)
    lb3.place(x=40, y=130)
    txt3 = Entry(f2, font=ft)
    txt3.place(x=140, y=130)

    lb4 = Label(f2, text="Email Add  : ", font=ft)
    lb4.place(x=40, y=170)
    txt4 = Entry(f2, font=ft)
    txt4.place(x=140, y=170)

    demo1 = Button(f2, text="  Add Record  ", font=ft, command=addAccRec)
    demo1.place(x=60, y=230)

    demo2 = Button(f2, text="Delete Record",font=ft, command=delAccRec)
    demo2.place(x=180, y=230)

    demo3 = Button(f2, text="Update Record",font=ft, command=upAccRec)
    demo3.place(x=60, y=270)

    demo4 = Button(f2, text="Fetch Record",font=ft, command=fetchAccRec)
    demo4.place(x=180, y=270)

    back = Button(f2, text="Home", font=ft)
    back.bind("<Button-1>", eventmethod3)
    back.place(x=4, y=380)

mainBase.mainloop()