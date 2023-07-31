#print("Helli")
# number = 10
# print("Num  is : ",number)
# print(type(number))
###############################################################
# import random  #...for generating random number

# health = 50 
# difficulty = 1

# patient_health = int(random.randint(25,50) / difficulty)
# print(patient_health)

# health = health + patient_health
# print(health)
###############################################################

# Python Math Module

# import math

# import math
# print(math.pi)

# class test:
#     a = 20
#     def __init__(self):
#         b = 50
#         # print("value of a:", a)
#         print("value of b:", b)
    
#     def sum():
#         b=20
#         print("aaaa",b)
#     sum()

# t1 = test()
#==============================================================
# i = 1
# while i<6:
#     print("HELLO ",end="")
#     i += 1
#+=============================================================
# n = int(input("Enter a number :"))
# sum=0
# i=0
# while i<=n:
#     sum= i+sum
#     i+=1
# print("sum is :",sum)
#=============================================================
# n = int(input("Enter a number :"))
# while 1:
#     if n % 2 == 0 :
#         print("Even number:",n)
#         # break10
#     else:
#        print("ODD number",n)
#     # break
#============================================================
# n = input("Enter string:")
# for i in n:
#     print(i,ord(i))
#======================================================================

# for i in range(1,10,2):
#     print(i,i**2)
#=======================================================================

# fobj = open("test.txt","w")
# fobj.writelines("Hello world...")
# fobj.close()

# fobj = open("test.txt","r")
# a = fobj.readlines()
# fobj.close()
# print(a)

# ================================================================================

# def checking():
#     # decision = False
#     # stud_index = -1
    
#     fobj = open("Stud_info.txt","r")
#     stud = fobj.readlines()
#     fobj.close()
#     # x = stud.split(",")
#     print(stud[0:len(stud)-1])
#     # print(x)
#     input()
# checking()

# import datetime 

# e = datetime.datetime.today()
# print(e.date())


# ls = [[1,2,3],[4,5,6]]
# ls.pop(0)
# print(ls)


# for each_stud in stud_data:
#         stud_ind += 1
#         each_stud = each_stud.split(",")
#         if each_stud[0]==enr:
#             flag=2
#             stud_data.pop(stud_ind)
#             print("Student Removed Successfully")
#             print("-"*50)
#     if flag == 1:
#         print("No such Student Found")
#         print("-"*50) 

# ls = [10,50,45]
# print(sum(ls))

# fobj = open("operations.txt","r")
# data = fobj.readlines()
# fobj.close()

# print(len(data))

# ================================================================================================================

# from tkinter import *

# ft = ("Arial Bold", 12)
# base = Tk()
# base.geometry("500x500")
# base.title("Demonstrating First GUI")

# def eventmethod1():
#     a = v1.get()
#     b = v2.get()
#     c = v3.get()
#     print(a,b,c, sep="\t")

# v1 = IntVar()
# v1.set(2) #<--- prefer to set offvalue as default value of variable
# v2 = IntVar()
# v2.set(2) #<--- prefer to set offvalue as default for variable
# v3 = IntVar()
# v3.set(2) #<--- prefer to set offvalue as default for variable

# ch1 = Checkbutton(base, text="Pizza", font=ft)
# ch1.configure(variable=v1, onvalue=1, offvalue=2)
# ch1.pack()

# ch2 = Checkbutton(base, text="Burger", font=ft)
# ch2.configure(variable=v2, onvalue=1, offvalue=2)
# ch2.pack()

# ch3 = Checkbutton(base, text="Pastry", font=ft)
# ch3.configure(variable=v3, onvalue=1, offvalue=2)
# ch3.pack()

# btn1 = Button(base, text="CHECK", command=eventmethod1)
# btn1.pack()

# base.mainloop()

# ===================================================================================================================

# from tkinter import *

# ft = ("Arial Bold", 12)
# base = Tk()
# base.geometry("500x500")
# base.title("Demonstrating First GUI")

# def abc():
#     base.destroy()

# def xyz():
#     base2 = Tk()
#     base2.geometry("200x200")
#     base2.title("Second Window")
#     lb = Label(base2, text="This is new window", font=ft)
#     lb.pack()
#     btn = Button(base2, text="abc", font=ft)
#     btn.pack()
#     base.destroy()
#     base2.mainloop()

# btn1 = Button(base, text="CLOSE", font=ft, command=abc)
# btn1.pack()

# btn2 = Button(base, text="NEW", font=ft, command=xyz)
# btn2.pack()

# base.mainloop()

# =================================================================================================================
# from tkinter import *

# ft = ("Arial Bold", 12)
# base = Tk()
# base.geometry("500x500")
# base.title("Demonstrating First GUI")

# def eventmethod1(e):
#     print("Right Click")

# def eventmethod2(e):
#     print("Left Click")

# def eventmethod3(e):
#     btn.configure(bg="green", fg="black")

# def eventmethod4(e):
#     btn.configure(bg="silver", fg="black")

# btn = Button(base, text="Click Here", font=ft)
# btn.bind("<Button-3>", eventmethod1)
# btn.bind("<Button-1>", eventmethod2)
# btn.bind("<Enter>", eventmethod3)
# btn.bind("<Leave>", eventmethod4)
# btn.pack()

# base.mainloop()

# ============================================================================================================

# from tkinter import *

# ft = ("Arial Bold", 12)
# base = Tk()
# base.geometry("500x500")
# base.title("Demonstrating First GUI")

# def eventmethod3(e):
#     btn.configure(bg="red", fg="yellow")
#     a = int(txt1.get())
#     b = int(txt2.get())
#     c = a + b
#     txt3.delete(0, END)
#     txt3.insert(0, str(c))

# def eventmethod4(e):
#     txt1.delete(0, END)
#     txt2.delete(0, END)
#     txt3.delete(0, END)
#     txt1.focus()
#     btn.configure(bg="silver", fg="black")

# txt1 = Entry(base, font=ft)
# txt1.pack()

# txt2 = Entry(base, font=ft)
# txt2.pack()

# btn = Button(base, text="ADD", font=ft, bg="silver")
# btn.bind("<Double-Button-1>", eventmethod3)
# btn.bind("<Button-3>", eventmethod4)
# btn.pack()

# txt3 = Entry(base, font=ft)
# txt3.pack()

# base.mainloop()

# ==================================================================================================
# from tkinter import *

# ft = ("Arial Bold", 12)
# base = Tk()
# base.geometry("500x500")
# base.title("Demonstrating First GUI")

# def eventmethod3(e):
#     a = e.widget.cget("text")
#     print("You selected : ", a)


# btn1 = Button(base, text="ADD", font=ft, bg="silver")
# btn1.bind("<Button-1>", eventmethod3)
# btn1.pack()

# btn2 = Button(base, text="SUBTR", font=ft, bg="green")
# btn2.bind("<Button-1>", eventmethod3)
# btn2.pack()

# base.mainloop()

# ==================================================================================================
# from tkinter import *

# def eventmethod3(e):
#     a = e.x
#     b = e.y
#     lb.configure(text=str(a) + "x" + str(b))

# ft = ("Arial Bold", 12)
# base = Tk()
# base.geometry("500x500")
# base.title("Demonstrating First GUI")
# base.bind("<Motion>", eventmethod3)

# lb = Label(base, font=ft)
# lb.pack()

# base.mainloop()
# ===============================================================================/
# btn1 = Button(base, text="submit")
# btn1.bind("<MouseEnter>", eventMethod1)
# btn1.pack()

# txt1 = Entry(base, font=ft)
# txt1.bind("<FocusOut>", eventMethod2)
# txt1.pack()

# txt2 = Entry(base, font=ft)
# txt2.bind("<FocusIn>", eventmethod3)
# txt2.pack()

# ================================================================================================
