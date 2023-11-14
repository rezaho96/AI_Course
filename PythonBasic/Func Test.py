#خروجی یک تابع مقادیری نیست که یک تابع چاپ می کند بلکه مقادیریست که به محل فراخوانی تابع برمی گردد

# def sumAvg(a,b,c,d=3):
#     s=a+b+c+d
#     avg=s/4
#     print(f"sum:{s},Avg={avg}")
# num1=int(input("enter number:"))
# sumAvg(2,num1,6)


# def sumAvg(a,b,c,d=3):
#     s=a+b+c+d
#     avg=s/4
#     return s,avg
# out=sumAvg(4,8,6,10)
# print(f"sum:{out[0]},Avg={out[1]}")

#......................................................

# def showPersonInfo(name,last_name,id_number,age):
#     print(f"Name is:{name}")
#     print(f"Last Name is:{last_name}")
#     print(f"Number ID is:{id_number}")
#     print(f"Age is:{age}")

# showPersonInfo("reza","hoseini",9621,20)
# print("************")
# showPersonInfo(last_name="hoseini",name="reza",age=20,id_number=9621)

#.......................................................
# import random
# def getRandomList(n):
#     list1=[]
#     for i in range(n):
#         list1.append(random.randint(1,100))
#     return list1

# print(getRandomList(20))

#.........................................................

def func(num,*arg):
    for i in arg:
        print(i)

func(5,4,8,10,"45","ali",87)




