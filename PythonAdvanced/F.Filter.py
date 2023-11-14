# def fun1(x):
#     return x//5==0
# list1=[2,5,8,14,65,12,10]
# print(list(filter(fun1,list1)))


# list1=[2,5,8,14,65,12,10]
# print(list(filter(lambda x:x>10,list1)))


# list1=[2,"♣","584",True,"ali","reza",False,False]
# print(list(filter(lambda x: str(x).isnumeric(),list1)))
# print(list(filter(lambda x: str(x).isalpha(),list1)))
# print(list(filter(lambda x: str(x).isdecimal(),list1)))
# print(list(filter(lambda x: str(x).isalnum(),list1)))

list1=[256,568,82,147,65,12,140]
print(list(filter(lambda x:str(x).find("5")!=-1,list1)))