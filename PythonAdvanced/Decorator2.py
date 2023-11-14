# def mainFunc(func,name):
#     def func1():
#         print("$$$$$$$$$$$$$$$$$$$$$$$$")
#         func(name)
#         print("$$$$$$$$$$$$$$$$$$$$$$$$")
#     return func1

# def printName(name):
#     print(name)

# k=mainFunc(printName,"ali")
# k()



# def printStar():
#     print("*******************")

# def mainFunc(func):
#     def func1():
#         for i in range(5):
#             func()
#     return func1
# endFunc=mainFunc(printStar)
# endFunc()




# def mainFunc(func):
#     def func1():
#         for i in range(5):
#             func()
#     return func1
# @mainFunc
# def printStar():
#     print("*******************")

# printStar()


# def mainFunc(func):
#     def func1(*args,**kwargs):
#         print("//////////////////")
#         func(*args,**kwargs)
#         func(*args,**kwargs)
#         print("//////////////////")
#     return func1

# @mainFunc
# def sum(x,y):
#     print(x+y)

# sum(5,4)



# def mainFunc(func):
#     def func1(*args,**kwargs):
#         print("//////////////////")
#         print(func(*args,**kwargs))
#         print("//////////////////")
#     return func1
# @mainFunc
# def sum(x,y):
#     return f"sum is :{x+y} "
# @mainFunc
# def mul(x,y,z):
#     return f"mul is:{x*y*z}" 
# @mainFunc
# def name(name):
#     return "My name is: "+name
# sum(5,4)
# mul(5,4,7)
# name("ali")


def decor1(func):
    def func1():
        x=func()
        return x*10
    return func1
def decor2(func):
    def func1():
        x=func()
        return x+2
    return func1    
def decor3(func):
    def func1():
        x=func()
        return x%5
    return func1
@decor1
@decor3
@decor2
def func():
    return 10
print(func())


