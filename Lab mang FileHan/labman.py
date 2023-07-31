from datetime import date as dt

def checkingStud(e):
    decision = False
    stud_index = -1
    flag = 1

    fobj = open("all_stud.txt","r")
    stud_list = fobj.readlines()
    fobj.close()

    for one_stud in stud_list:
        stud_index += 1
        one_stud = one_stud.split(",")
        if one_stud[0] == e:
            flag = 2
            decision = True
            print("Student Found in File 🙌")
            break
    if flag==1:
        print("No such Enrollment number in this File ❌ ")
        print("-"*50)
    return decision, stud_index

def checking(e):
    decision = False
    stud_index = -1
    flag = 1

    fobj = open("all_issued.txt","r")
    stud_list = fobj.readlines()
    fobj.close()

    for one_stud in stud_list:
        stud_index += 1
        one_stud = one_stud.split(",")
        if one_stud[0] == e:
            flag = 2
            decision = True
            print("Student Found in File 🙌")
            break
    if flag==1:
        print("No such Enrollment number in this File ❌")
        print("-"*50)
    return decision, stud_index


def get_date():
    obj = dt.today()
    d = obj.day
    m = obj.month
    y = obj.year
    today_dt = str(d) + "/" + str(m) + "/" + str(y)
    return today_dt

def issue_book():
    enr = input("Enter Enrollment Number of Borrower : ")
    bnum = input("Enter Book Number to Borrow : ")
    i_date = get_date()
    fobj = open("all_issued.txt", "a")
    fobj.write(enr + "," + bnum + "," + i_date + ",NA,P\n")
    fobj.close()
    print("Book Issued ✔")
    input()

def return_book():
    enr = input("Enter Enrollment Number for Returning Book : ")

    fobj = open("all_issued.txt","r")
    stud_data = fobj.readlines()
    fobj.close()

    decision, stud_index = checking(enr)
    
    if decision == True:
        ret_date = get_date()
        stud = stud_data[stud_index]
        stud = stud.split(",")
        stud_data.pop(stud_index)

        enr = stud[0]
        bnum = stud[1]
        i_date = stud[2]
        r_date = ret_date
        ret = "N"
        fobj = open("all_issued.txt", "w")
        fobj.writelines(stud_data)
        fobj.writelines("")
        fobj.writelines(enr+","+bnum+","+i_date+","+r_date+","+ret)
        fobj.write("\n")
        fobj.close()
        print("Book Returned Successfully")
        print("-"*50)
        print("Issued Date : ",stud[2])
        print("Returned Date : ",r_date)
    print("-"*50)

def show_not_ret_books():
    fobj = open("all_issued.txt","r")
    stud_data = fobj.readlines()
    fobj.close()
    print("-"*50)
    print("Not Return Book List ")
    for each_stud in stud_data:
        each_stud = each_stud.split(",")
        if each_stud[4] == "P\n":
            # print(each_stud[0:len(each_stud)-2])
            print(each_stud[0]+"\t"+each_stud[1]+"\t"+each_stud[2])
        

def add_new_stud():
    enr = input("Enter Your Enrollment Number : ")
    decision, stud_index = checkingStud(enr)
    if decision == True:
        print("-"*40)
        print("Enrollment Number Already Present ❌")
    else:
        name = input("Enter Student Name : ")
        mob = input("Enter Mobile Number : ")
        email = input("Enter Your Email : ")
        fobj = open("all_stud.txt", "a")
        fobj.writelines(enr+","+name+","+mob+","+email+"\n")
        fobj.close()
        print("-"*50)
        print("Student Details Added Successfully 👍")
    input()
    

def add_new_book():
    # - create new file "all_books.txt"
	# - Format of that file's data will be:
	# 	book number, book title, book author, book publication
    bnum = input("Enter Book Number : ")
    btit = input("Enter Book Title : ")
    bauth = input("Enter Book Author : ")
    bpubl = input("Enter Publication Name :")

    fobj = open("all_book.txt","a")
    fobj.write(bnum + "," +btit+ "," +bauth+","+bpubl+"\n")
    fobj.close()
    print("New Book Added Successfully 👍")

def stud_history():
    # - Accept enrollment number of student.
	# - Show a table that contains all the books which is issued to this student.
	# 	book number\t	issue date\t	return date
    enr = input("Enter Enrollment number : ")
    fobj = open("all_issued.txt","r")
    stud_data = fobj.readlines()
    fobj.close()

    print("Enrl No \t Book No \t issued_d \t\t retur_d \t Status" )
    print("-"*90)
    for each_book in stud_data:
        each_book = each_book.split(",")
        if enr == each_book[0]:
            print(each_book[0],"\t\t",each_book[1],"\t\t",each_book[2],"\t\t",each_book[3],"\t",each_book[4])
    print("-"*90)




def book_history():
    # - Accept book number
	# - show a table that contains history of this book (issued history)
	# 	enrollment number\t	issue date\t	return date
	# - Also show total count, how many times that book is total issued.
    bnumber =  input("Enter Book Number : ")
    fobj = open("all_issued.txt","r")
    stud_data = fobj.readlines()
    fobj.close()
    count = 0
    print("Enrl No \t Book No")
    print("-"*50)
    for each_book in stud_data:
        each_book = each_book.split(",")
        if bnumber == each_book[1]:
            count+=1
            print(each_book[0],"\t\t",each_book[1])
    print("-"*50)
    if count == 1:
        print("Book Issued only 1 Time")
    else:
        print("Book Issued Total ",count," times")


def search_book():
    # a) search by Book Title
	# 	- accept book title and print book information
	# 		book number\t	book author\t	book publication

	# b) search by Author Name
	# 	- accept author name and print all the books which are written by that author.
	# 		book number\t	book title\t		book publication

	# c) search by Publication Name
	# 	- accept publication name and print all the books which are published by that publication.
	# 		book number\t	book title\t	book author
    fobj = open("all_book.txt","r")
    bdata = fobj.readlines()
    fobj.close()

    print("1 - Search by book Author")
    print("2 - Search by book Title")
    print("3 - Search by Publication")
    
    chh = int(input("Select an Option : "))
    if chh == 1:
        author = input("Enter Author Name : ")
        for each_book in bdata:
            each_book = each_book.split(",")
            if each_book[2] == author:
                print("Book No \t Book Auth \t Book Publc")
                print("-"*70)
                print(each_book[0]+"\t\t"+each_book[2]+"\t\t"+each_book[3])
        # else:
        #     print("-"*70)
        #     print("Author Book is not There..❌")

    elif chh == 2:
        btitle = input("Enter Book Title : ")
        for each_book in bdata:
            each_book = each_book.split(",")
            if each_book[1] == btitle:
                print("Book No \t Book Title \t Book Publc")
                print("-"*70)
                print(each_book[0]+"\t\t"+each_book[1]+"\t\t"+each_book[3])

    elif chh == 3:
        public = input("Enter Book Publication : ")
        for each_book in bdata:
            each_book = each_book.split(",")
            if each_book[3] == public:
                print("Book No \t Book Title \t Book Auth")
                print("-"*70)
                print(each_book[0]+"\t\t"+each_book[1]+"\t\t"+each_book[2])

    else:
        print("You Entered Wrong Key ...❌")

def search_stud():
    enr = input("Enter Enrollment number : ")
    decision, stud_index = checkingStud(enr)
    fobj = open("all_stud.txt", "r")
    stud_data = fobj.readlines()
    fobj.close()
    if decision == True:
        one_stud = stud_data[stud_index]
        one_stud = one_stud.split(",")
        print("-"*40)
        print("Name is: ",one_stud[1])
        print("Mobile : ",one_stud[2])
        print("Email  : ",one_stud[3])
        print("-"*40)

while True:
    print("="*70)
    print("\nSelect an option")
    print("1 - Issue Book")
    print("2 - Return Book")
    print("3 - Add New Student")
    print("4 - Add New Book")
    print("5 - Show Not Returned Books")
    print("6 - Student History")
    print("7 - Book History")
    print("8 - Search Book")
    print("9 - Search Student")
    print("0 - Exit")
    ch = int(input("Provide your choice : "))

    if ch==1: issue_book()
    elif ch==2: return_book()
    elif ch==3: add_new_stud()
    elif ch==4: add_new_book()
    elif ch==5: show_not_ret_books()
    elif ch==6: stud_history()
    elif ch==7: book_history()
    elif ch==8: search_book()
    elif ch==9: search_stud()
    else: exit(0)
