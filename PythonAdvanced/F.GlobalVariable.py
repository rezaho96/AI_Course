# x=10
# def func():
#     x=50
#     print("x is:",x)
    
   
# x+=10
# func()
# print("x:",x)

print("///////////////////////////////////")
x=100
def func1():
    global x
    x=20
    print("x is:",x)
def func2():
    global x
    x=50
    print("x is:",x)
def func3():
    x=30
    print("x is:",x)

func1()
print(x)
func2()
func3()
print(x)