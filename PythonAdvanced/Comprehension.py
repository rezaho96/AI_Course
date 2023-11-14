# list1=[]
# for i in range(1,10):
#     list1.append(i)
# print(list1)



# list1=[i  for i in range(1,10)]
# print(list1)



# list1=[i**3 for i in range(1,10)]
# print(list1)




# def func1(num1):
#     num1*=20
#     num1+=3
#     return num1
# list1=[func1(i) for i in range(1,10)]
# print(list1)


# list1=[i for i in range(1,20) if i<15]
# print(list1)




# list1=[i if i<10 else i/10  for i in range(1,30)]
# print(list1)



# set1={i for i in range(1,11)}
# print(set1)


# set1={i if i<10  else i//2  for i in range(1,30)}
# list1=[i if i<10  else i//2  for i in range(1,30)]
# print(list1)
# print(set1)



# dic1={x:"*"*x  for x in range(1,20)}
# print(dic1)



# list1=[i for i in range(1,11)]
# list2=["ali","ahamad","saeid","vahid","roya","mahvash"]
# zip1=zip(list1,list2)
# print(f"{type(zip1)}\t{zip1}")

# for key,value in zip1:
#     print(f"{key}:{value}")






# list1=[i for i in range(1,11)]
# list2=["ali","ahamad","saeid","vahid","roya","mahvash"]
# zip1=zip(list2,list1)

# dic1={key:value if value!=5 else key for key,value in zip1}
# print(dic1)



###Nested Comprehension

# list1=[]

# for i in range(0,9):
#     # list2=[]
#     list1.append([])
#     for j in range(1,10):
#         list1[i].append(j*i)
#         print(j*i,end="\t")
#     print()
      
# print(list1)

def printMatrix(matrix):
    for row in matrix:
        for col in row:
            print(col,end="\t")
        print()
matrix1=[[i*j  for j in range(1,11)]  for i in range(1,11)]
print(matrix1)
printMatrix(matrix1)
