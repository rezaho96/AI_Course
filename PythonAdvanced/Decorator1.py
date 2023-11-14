# def func1(name):
#     return "hello "+name

# print(func1("reza"))
# func2=func1
# del(func1) 

# print(func2("ALI"))
#print(func1("saeid"))#???


# def func():

#     print("............................")
#     def func1():
#         print("this is func1")

#     def func2():
#         print("this is func2")
#     func1()
#     func2()

# func()
#func1()#??!!


# def strChange(str):
#     return "^^"+str+"^^"

# def strShift(str):
#     return "  "+str

# def mainFunc(func,name):
#     print(".///.")
#     print(func(name))

# mainFunc(strChange,"saeid")
# mainFunc(strShift,"samad")



def mainFunc(name):
    def func1(str):
        print(name+"--"+str)
    print("......//...........")
    return func1
k=mainFunc("ali")
k("shokohi")

