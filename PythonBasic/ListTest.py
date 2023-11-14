from typing import List


list1=[55,77,99,66,"adskj",8,True,88,66,99,"ali",[55,66,11,"jlkf"]]
# for i in range(len(list1)):
#     print(list1[i])

# list1[2]=10
# print(list1)

# list1.append("ali")
# print(list1)

# list1.clear()
# print(list1)

# list1.extend([8,6])
# print(list1)

list1.remove(66)
print(list1)

# name="Reza"
# name[1]="E"
# print(name)

name="reza"
temp=list(name)
temp[0]="R"
name=''.join(temp)
print(f"{name}")