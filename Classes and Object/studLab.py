from datetime import datetime as dt

all_isuued = []
stud_obj = []

class Student:
    s_enr = None
    s_name = None
    s_mob = None
    s_email = None

    def accept_val(self):
        self.s_enr = input("Enter Enrollment Number : ")
        self.s_name = input("Enter Student Name : ")
        self.s_mob = input("Enter Mobile Number : ")
        self.s_email = input("Enter E-mail Address : ")

    def show_val(self):
        print(self.s_enr)
        print(self.s_name)
        print(self.s_mob)
        print(self.s_email)


class Book:
    b_no = 0
    b_title = None
    b_auth = None

    def accept_val(self):
        self.b_no = input("Enter Book Number : ")
        self.b_title = input("Enter Book Title : ")
        self.b_auth = input("Enter book Author : ")

        stud_obj.append(self)

def get_date():
    obj = dt.today()
    d = obj.day
    m = obj.month
    y = obj.year
    today_dt = str(d) + "/" + str(m) + "/" + str(y)
    return today_dt


class Issue:
    s_obj = Student()
    b_obj = Book()
    i_date = None
    r_date = None
    r_status = "p"

    def __init__(self):
        self.s_obj.accept_val()
        self.b_obj.accept_val()
        self.i_date = get_date()
        self.r_date = None
        self.r_status = "p"


def issue_book():
    i1 = Issue()
    all_isuued.append(i1)
    print("Book issued Successfully")



def return_book():
    pass

stud_obj_values = []
def show_not_ret_books():
    for i in stud_obj:
        stud_obj_values.append(i)
        print(stud_obj_values)
        stud_obj_values.clear()

    
while True:
    print("="*90)
    print("1 - Issue a Book")
    print("2 - Return a Book")
    print("3 - Show Not Return Book")
    print("4 - Exit")
    uch = int(input("Select An Option : "))
    
    if uch == 1: 
        issue_book()
    elif uch == 2:
        return_book()
    elif uch == 3:
        show_not_ret_books()
    else:
        exit(0)
