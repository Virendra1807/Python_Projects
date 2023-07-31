def checking(e):
    decision = False
    stud_index = -1
    flag = 1

    fobj = open("Stud_info.txt","r")
    stud_list = fobj.readlines()
    fobj.close()

    for one_stud in stud_list:
        stud_index += 1
        one_stud = one_stud.split(",")
        if one_stud[0] == e:
            flag = 2
            decision = True
            print("Student Found in File")
            break
    if flag==1:
        print("No such Enrollment number in this File ")
        print("-"*50)
    return decision, stud_index
    

def add_new_stud():
    enr = input("Enter Your Enrollment Number : ")
    decision, stud_index = checking(enr)
    if decision == True:
        print("-"*40)
        print("Enrollment Number Already Present ❌")
    else:
        name = input("Enter Student Name : ")
        mob = input("Enter Mobile Number : ")
        email = input("Enter Your Email : ")
        fobj = open("Stud_info.txt", "a")
        fobj.writelines(enr+","+name+","+mob+","+email+"\n")
        fobj.close()
        print("-"*50)
        print("Student Details Added Successfully 👍")
    input()

def update_stud_info():
    enr = input("Enter Enrollment No for Update : ")
    fobj = open("Stud_info.txt","r")
    stud_data = fobj.readlines()
    fobj.close()

    decision, stud_index = checking(enr)

    if decision == True:

        print("what you want to Update")
        print("1 - Update Name")
        print("2 - Update Mob No")
        print("3 - Update Email")
        uch = int(input("Select an Option : "))
        each_stud = stud_data[stud_index]
        each_stud = each_stud.split(",")
        
        if uch == 1:
            nm = input("Enter New Name for Update : ")
            each_stud[1] = nm
            print("Name Updated Successfully")
            print("-"*50)

        elif uch == 2:
            mob = input("Enter New Mobile Number for Update : ")
            each_stud[2] = mob
            print("Mobile number Updated Successfully")
            print("-"*50)

        elif uch == 3:
            em = input("Enter New Email for Update : ")
            each_stud[3] = em
            print("New Email address Updated Successfully")
            print("-"*50)
        stud_data.pop(stud_index)
        enr = each_stud[0]
        nm = each_stud[1]
        mob = each_stud[2]
        em = each_stud[3]
        fobj = open("Stud_info.txt", "w")
        fobj.writelines(stud_data)
        fobj.writelines("")
        fobj.writelines(enr+","+nm+","+mob+","+em)
        fobj.close()

        print("Student Information Updated SuccessFully 🙌")

        # print(stud_data)
        # stud_data.append(each_stud)
        # print(stud_data)

    # fobj = open("Stud_info.txt","w")
    # fobj.writelines(stud_data)
    # fobj.close()

def remove_stud_info():
    enr = input("Enter Enrollment Number : ")
    fobj = open("Stud_info.txt","r")
    stud_data = fobj.readlines()
    fobj.close()

    decision, stud_index = checking(enr)
    if decision == True:
        stud_data.pop(stud_index)
        print("Student Removed Successfully")
        print("-"*50)
    for each_s in stud_data:
        print(each_s,end="")
    print("-"*50)

    fobj = open("Stud_info.txt","w")
    fobj.writelines(stud_data)
    fobj.close()

    
def show_stud_info():
    flag = 1
    enroll = input("Enter Enrollment Number : ")

    fobj = open("Stud_info.txt","r")
    stud_data = fobj.readlines()
    fobj.close()

    for each_stud in stud_data:
        each_stud = each_stud.split(",")
        if each_stud[0]==enroll:
            flag = 2
            print("Student Found")
            print(each_stud)
            print("-"*50)
    if flag == 1:
        print("No such Enrollment Number Found in File")
        print("-"*50)

def show_all_stud():
    fobj = open("Stud_info.txt","r")
    stud_data = fobj.readlines()
    fobj.close()
    print("-"*50)
    print("Enrl","\t","Name","\t","Mob No","\t","Email")
    print("-"*50)
    for each_stud in stud_data:
        each_stud = each_stud.split(",")
        print(each_stud[0],"\t",each_stud[1],"\t",each_stud[2],"\t",each_stud[3],end="")

    input()



while True:
    print("="*50)
    print("Provide your choice")
    print("1 - Add New Student")
    print("2 - Update Student Info")
    print("3 - Remove Student Info")
    print("4 - Show Student Info")
    print("5 - Show All Student")
    print("6 - Exit")

    ch = int(input("Select an Option : "))

    if ch == 1:
        add_new_stud()
    elif ch == 2:
        update_stud_info()
    elif ch == 3:
        remove_stud_info()
    elif ch == 4:
        show_stud_info()
    elif ch == 5:
        show_all_stud()
    elif ch == 6:
        exit(0)