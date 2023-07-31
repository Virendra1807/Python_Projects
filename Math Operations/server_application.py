fobj = open("operations.txt","r")
data = fobj.readlines()
fobj.close()

line_num = -1
itr = 1
while itr < 2:
    itr += 1
    for each_opt in data:
        fobj = open("operations.txt","r")
        data = fobj.readlines()
        fobj.close()
        line_num += 1
        each_opt = each_opt.split(",")
        x = int(each_opt[1])
    
        if each_opt[2] == "+\n":
            y = int(each_opt[0])
            operator = "+"
            ans = x+y

        elif each_opt[2]=="-\n":
            y = int(each_opt[0])
            operator = "-"
            ans = y-x

        elif each_opt[2]=="*\n":
            y = int(each_opt[0])
            operator = "*"
            ans = y*x

        elif each_opt[2]=="/\n":
            y = int(each_opt[0])
            operator = "/"
            ans = y/x
        
        elif each_opt[2]=="**\n":
            y = int(each_opt[0])
            operator = "**"
            ans = y**x
            
        whole_str = str(y)+operator+str(x)+"="+str(ans)

        print(data)
        data.pop(line_num)
        print("-"*20)
        print(data)
            
        fobj = open("operations.txt","w")
        fobj.write(whole_str+"\n")
        fobj.writelines(data)
        fobj.close()

    print("Opearations SuccessFully Done ....")
            