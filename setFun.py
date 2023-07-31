# set1 = {10,"viren",52,20.3,'A',"jonas","friday"}
# print("Initial Set:",set1)
# print(type(a))
# val = 0
# for val in set1:
#     print(val)

# set1.add("Dexter")
# print("Updated Set:",set1)

# set1.pop()
# print("Set After Popping:",set1)

# set1.remove("viren")
# print("Remove Set :",set1)

# set1.discard("jonas")
# print("Discard Set :",set1)

# length = len(set1)
# print("length is :",length)

# set2 = {20,45,12,51,85,65,32,41}

# maxi = max(set2)
# mini = min(set2)
# print("max value in Set :",maxi)
# print("min value in Set :",mini)

# set2.clear()
# print("After Clear function used :",set2)

# print(20 in set2)
# print(20 not in set2)

# set1 = {45,85,2,1,3,2,20,32,85}
# set2 = {20,45,12,51,85,65,32,41}

# diff = set1.difference(set2)
# print(diff)

# symDiff = set1.symmetric_difference(set2)
# print(symDiff)

# common = set1.intersection(set2)
# print(common)

# a = set1.difference(set2)
# print(a)

# set1 = {45,85,2,1,3,2,20,32,85}
# set2 = {"viren",49}
# i = 0
# j = 0
# def checkItems():
#     for i in set1:
#         for j in set2:
#             if i == j:
#                 return True
#     return False         
# a = checkItems()
# print(a)

# s = {"Mahabaleshwar","Pune","Mumbai","Bangluru","Vishakhapatnam","Kochi"}
# def checkLength():
#     max_len = 0
#     i = 0
#     for i in s:
#         if len(i) > max_len:
#             max_len = len(i)
#             max_string = i
#             return max_string
#     return max_string
# a = checkLength()
# print(a)

# max_len = 0
# for i in s:
#     if len(i) > max_len:
#         max_len = len(i)
#         max_string = i

# print(max_string)  

# s = {"Mahabaleshwar","Pune","Mumbai","Bangluru","Vishakhapatnam","Kochi"}
# list = []
# for i in s:
#     a = len(i) 
#     list.append(a)
# print(list)

# s = {"Mahabaleshwar","Pune","Mumbai","Bangluru","Vishakhapatnam","Kochi"}
# dict = {}
# for i in s:
#    dict.update({i : len(i)})
# print(dict)


#=============================================================================================================================

# set1 = {10,20,30,40}
# set2 = {20,40,50}
# set1.difference_update(set2)
# print(set1)

# set1 = {10, 20, 30, 40, 50}
# set1.difference_update({10,20,30})
# print(set1)

# set1 = {10, 20, 30, 40, 50}
# set2 = {60, 70, 80, 90, 10}
# if set1.isdisjoint(set2):
#     print("No common elements")
# else:
#     print("Set has common elements")
#     a = set1.intersection(set2)
#     print("Common Elements:",a)

# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# set1.symmetric_difference_update(set2)
# print(set1)

# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# set1.intersection_update(set2)
# print(set1)

# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# def identical():
#     a = set1.intersection(set2)
#     return a
# k = identical()
# print(k)

# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}


# def common():
#     set1.update(set2)
#     return set1

# common()
# print(set1)

#=============================================================================
#                 Exercise On Dict
# ls = [10,"viren",45.8,98,"jay"]
# tp = (20,"hey",54,32,74)
# ls2  = [32,4,10]

# ls.extend(ls2)
# print(ls)

# def lstp(arg):
#     ls.append(arg)
#     print("New List :",ls)
#     i = 0
#     j = 0
#     for i in ls:
#         print("Type of elements in LIST :",type(i))
#     for j in tp:
#         print("Type of elements in TUPLE :",type(j))         
# lstp(500)


# def lstp(*args):
#     if type(args) == list:
#         return tuple(args)
#     elif type(args) == tuple:
#         ls = list(args)
#         a = ls.sort()
#         return a
#     elif type(args) == str:
#         l = str(args)
#         return l

# a = lstp((10,20,10,30))
# print(a)

# dict =  {0: 10, 1: 20}
# dict.update({2:30})
# print(dict)

# dict1={1:10, 2:20}
# dict2={3:30, 4:40}
# dict3={5:50,6:60}
# res_dict = {}
# for i in (dict1, dict2, dict3): res_dict.update(i)
# print(res_dict)

# dict1 = { "one": 10, "two": 20, "three": 30, "four": 40, "five": 50, "six": 60}
# for i in dict1:
#     print(i,":",dict1[i])

# dict1 = { "one": 10, "two": 20, "three": 30, "four": 40, "five": 50, "six": 60}
# size = len(dict1)
# keys, values = list(dict1.keys()), list(dict1.values())
# i=0
# while(i < size):
#     print(keys[i], ":",values[i])
#     i += 1


# dict = {}

# i=0

# while(i<10):
#     dict = {i:i}
#     li = list(dict.keys())
#     dict.update(li)
#     i += 1

# dict1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
 
# for i in dict1:

# print(dict1)
