from tabulate import tabulate

student_obj = []
student_obj_values = []

name = 0
enrl_No = 0
gender = 0
avg_marks = 0
sclass = 0
paid_fees = 0


class Student:
    def __init__(self):
        self.name = input("Enter Your Name : ")
        self.gender = input("Enter Gender M/F : ")
        self.enrll = input("Enter Enrollment : ")
        self.cclass = input("Enter Your Class : ")
        self.avg_marks = input("Enter Avg-Marks : ")
        self.paid_fees = input("Enter Total Paid Fees : ")

        student_obj.append(self)

    def get_values(self):
        return [self.paid_fees,self.gender,self.enrll,self.cclass,self.avg_marks,self.name]
    def set_fees(self,num):
        self.paid_fees = int(self.paid_fees) + int(num)
        # Accept values for all instances here + other m.f  use setter getter method

def change_values():
    student_obj_values.clear()
    for i in student_obj:
        student_obj_values.append(i.get_values())

def add_new_stud():
    #declare object of class student and use constructor to initiallize instances : 
    # name, enroll, gemder, avg marks, class, paid fees   Add this object to all_studs[]
    s1 = Student()
    change_values()

def delete_student():
    
    en = input("Enter Enrollment Number : ")
    # Accept enrollment no. and searcch that student from all_studs and delete that student 
    for i in student_obj:
        ret = i.get_values()
        if ret[2] == en:
            student_obj.remove(i)
            print("Student Removed")
    change_values()

def update_paid_fees():
    #ask for enrollment no. and additional paid fees, 
    # search for that student in all_studs and add this fees in hia current fees(adddition)
    en = input("Enter Enrollment Number : ")
    for i in student_obj:
        ret = i.get_values()
        if ret[2] == en:
            additional_fees = int(input("Enter Additional Fees paid : "))
            i.set_fees(additional_fees)
            print("Fees Updated Successfully")
    change_values()

def show_stud_info():
    en = input("Enter Enrollment Number : ")
    #Accept enr no.  and print details of that student by searching in all_studs
    for i in student_obj_values:
        if i[2]==en:
            print(tabulate([i],headers=["paid fees",'gender','roll no.','class','average marks','name']))
            break

def show_all_stud_info():
    # display info of all students that add  added in all_studs 
    print(tabulate(student_obj_values,headers=["paid fees",'gender','roll no.','class','average marks','name']))



while True:
    print("="*90+"\nProvide Your Choice")
    print("1 - Add New Student")
    print("2 - Delete Student")
    print("3 - Update Fees")
    print("4 - Show Student info")
    print("5 - Show All Sudents info")
    print("6 - Exit")

    uch = int(input("Select an Option : "))

    if uch == 1:
        add_new_stud()
    elif uch == 2:
        delete_student()
    elif uch == 3:
        update_paid_fees()
    elif uch == 4:
        show_stud_info()
    elif uch == 5:
        show_all_stud_info()
    elif uch == 6:
        exit(0)