while True:
    print("-_"*50)
    print("Select An Operation")
    print("1 - Addition")
    print("2 - Subtraction")
    print("3 - Multiplication")
    print("4 - Division")
    print("5 - Power")
    # print("6 - Smallest")
    # print("7 - Largest")
    print("6 - Exit")
    chh = int(input("Select An Option : "))

    if chh == 1:
        opt = "+"
    elif chh == 2:
        opt = "-"
    elif chh == 3:
        opt = "*"
    elif chh == 4:
        opt = "/"
    elif chh == 5:
        opt = "**"
    elif chh == 6:
        exit(0)

    num1 = input("Enter First Number : ")
    num2 = input("Enter Second Number : ")

    fobj = open("operations.txt","a")
    fobj.writelines(num1+","+num2+","+opt+"\n")
    fobj.close()
    print("Unsolved Operation Saved in File Successfully...")


