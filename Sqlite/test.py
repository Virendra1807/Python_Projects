# import sqlite3

# conn = sqlite3.connect("kk_db")
# # conn.execute(f"""create table student ( name varchar, post varchar, city varchar)""")

# nm = input("Enter your name : ")
# post = input("Enter your post : ")
# city =  input("Enter your City : ")

# conn.execute(f"""insert into student values ( "{nm}", "{post}", "{city}" ) """)
# conn.commit()
# val = conn.execute(f"""Select * from student""")
# for i in val:
#     print(*i)

# print("Successful")

# conn.close()

# ==================================================================================
from tabulate import tabulate

# col = ['name', 'Accno', 'mobno', 'email']
# data = [("viren", '120' , '9021', "viren@gmail.com")]
# print(tabulate(data, headers=col ))
nm = "ciren"
enr = "235"
mob = "902114"
email = "viren@gmail.com"
col = ["name", "enrollment", "MobileNumber", "Email"]        
print(tabulate([[nm]+[enr]+[mob]+[email]], headers=col))