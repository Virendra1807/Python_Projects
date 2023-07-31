from datetime import date
# def checking(dishnm):
#     decision = False
#     line_num = -1
#     flag = 1

#     fobj = open("hotelDish.txt","r")
#     menu_list = fobj.readlines()
#     fobj.close()

#     for one_dish in menu_list:
#         line_num += 1
#         one_dish = one_dish.split(",")
#         if one_dish[1] == dishnm:
#             flag = 2
#             decision = True
#             print("Dish is in Menu....✔")
#             break
#     if flag==1:
#         print("No such Dish in this File....❌ ")
#         print("-"*90)
#     return decision, line_num

def get_date():
    obj = date.today()
    d = obj.day
    m = obj.month
    y = obj.year
    today_dt = str(d) + "/" + str(m) + "/" + str(y)
    return today_dt


def checking(dcode):
    decision = False
    line_num = -1
    flag = 1

    fobj = open("hotelDish.txt","r")
    menu_list = fobj.readlines()
    fobj.close()

    for one_dish in menu_list:
        line_num += 1
        one_dish = one_dish.split(",")
        if one_dish[0] == dcode:
            flag = 2
            decision = True
            print("Dish is in Menu....✔")
            break
    if flag==1:
        print("No such Dish in this File....❌ ")
        print("-"*90)
    return decision, line_num

def add_dish():
    dish_code = input("Enter Dish Code : ")
    decision,linenum = checking(dish_code)
    if decision == False:
        dish_name = input("Enter Dish Name : ")
        dish_price = int(input("Enter Dish Price : "))
        fobj=open("hotelDish.txt","a")
        fobj.write(dish_code+","+dish_name+","+str(dish_price)+"\n")
        fobj.close()
        print("Dish Added Successfully....🙌")
    input()


def generate_bill():
    total_amt = 0
    while True:
        print("-"*90)
        print("1-Order more Dishes")
        print("2-Finalize the Bill")
        uch = int(input("Select the Option: "))
        if uch == 1:
            today_dte = get_date()
            dishc = input("Enter the dish code: ")
            decision, line_no = checking(dishc)
            if decision == True:
                qty = int(input("Enter the Quantity: "))

                fobj = open("hotelDish.txt","r")
                dishes = fobj.readlines()
                fobj.close()

                dish = dishes[line_no]
                dish = dish.split(",")
                cost = dish[2]
                dish_amt = qty * int(cost)
                total_amt = total_amt + dish_amt
            elif decision == False:
                print("This dish does not exists.")
        elif uch == 2:
            if total_amt == 0:
                print("-"*90)
                print("Are you not feeling Hungry...🙄")
                break
            else:
                fobj = open("hotelBills.txt","r")
                bill_list = fobj.readlines()
                fobj.close()

                bill_no = len(bill_list) + 101

                bill = str(str(bill_no)+","+str(total_amt)+","+today_dte+"\n")
                fobj = open("hotelBills.txt","a")
                fobj.write(bill)
                fobj.close()
                print("Total amount is: Rs."+str(total_amt))
                break
        input()
                    

def view_menu():
    fobj = open("hotelDish.txt","r")
    menu = fobj.readlines()
    fobj.close()

    print("---------- All Dishes Of Hotel ---------- ")
    print("DishCode \t Dishes \t Price")
    for each_dish in menu:
        each_dish = each_dish.split(",")
        print(each_dish[0],"\t\t",each_dish[1],"\t\t","Rs",each_dish[2],end="")
    print("----------- Thanks For Visit -----------")
    
    input()


def update_price():
    fobj = open("hotelDish.txt","r")
    data = fobj.readlines()
    fobj.close()

    dcode = input("Enter Dish Code to Update : ")
    decision,line_num = checking(dcode)
    if decision == True:
        dish = data[line_num]
        dish = dish.split(",")
        data.pop(line_num)

        dish_name = dish[1]
        dish_price = int(input("Enter New Price : "))

        fobj = open("hotelDish.txt", "w")
        fobj.writelines(data)
        fobj.writelines("")
        fobj.writelines(dcode+","+dish_name+","+str(dish_price))
        fobj.write("\n")
        fobj.close()
        print("Dish Price Updated Successfully\n")

        view_menu()


def view_todays_bills():
    print("--------- Todays Customers Bills ---------")
    today_date = get_date()
    fobj = open("hotelBills.txt","r")
    bills = fobj.readlines()
    fobj.close()
    print("Bill No \t Amount \t Date")
    for each_day in bills:
        each_day = each_day.split(",")
        dtt = today_date+"\n"
        if dtt == each_day[2]:
            print(each_day[0]+"\t\t"+each_day[1],"\t\t",each_day[2],end="")

    # for each_day in bills:
    #     each_day = each_day.split(",")
    #     dtt = today_date+"\n"
    #     if dtt != each_day[2]:
    #         print("-"*90)
    # print("No Bills of Toadays Date...❌")


def view_bills():
    pass


while True:
    print("="*90)
    print("Provide your Choice")
    print("1 - Add new Dish")
    print("2 - Generate Bill")
    print("3 - View Menu")
    print("4 - Update Price")
    print("5 - View Today's Bills")
    print("6 - View Bill")
    print("7 - Exit")
    chh = int(input("Select An Option : "))

    if chh == 1:
        add_dish()
    elif chh == 2:
        generate_bill()
    elif chh == 3:
        view_menu()
    elif chh == 4:
        update_price()
    elif chh == 5:
        view_todays_bills()
    elif chh == 6:
        view_bills()
    elif chh == 7:
        exit(0)
