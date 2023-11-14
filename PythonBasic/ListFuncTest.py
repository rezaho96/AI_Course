#sort sorted reverse count  copy  pop

# list1=[20,10,3,5,80,20,9,4,40,15,7]
# list1.sort()
# print(list1)

# list1=[20,10,3,5,80,20,9,4,40,15,7]
# list2=sorted(list1)
# print(list2)
# print(list1)

# list1=[20,10,3,5,80,20,9,4,40,15,7]
# list1.reverse()
# print(list1)

# list1=[20,10,3,5,80,20,9,4,40,15,7]
# print(len(list1))
# print(list1.count(20))

# list1=[20,10,3,5,80,20,9,4,40,15,7]
# list2=list1.copy()
# print(list2)

list1=[20,10,3,5,80,20,9,4,40,15,7]
while len(list1)>0:
    x=list1.pop()
    print(list1)
