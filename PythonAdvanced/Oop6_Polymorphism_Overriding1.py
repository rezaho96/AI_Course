# class A:
#     def func1(self):
#         print("A func1")

#     def func2(self):
#         print("A func2")
    
#     def mul(self,a,b):
#         print(a*b)

# class B:
#     def func1(self):
#         print("B func1")

#     def func2(self):
#         print("B func2")
#     def mul(self,a,b):
#         print((a-b)*20)

# def func(obj):
#     obj.func1()
#     obj.func2() 
#     obj.mul(10,6)
# a=A()
# b=B()
# func(a)
# func(b)
 #======================================================================================================
class A:
    def func1(self):
        print("A func1")

    def func2(self):
        print("A func2")
    
    def mul(self,a,b):
        print(a*b)

class B:
    def func1(self):
        print("B func1")

    def func2(self):
        print("B func2")
    def mul(self,a,b):
        print((a-b)*20)

a=A()
b=B()
c=B()
for obj in (a,b,c):
    obj.func1()
    obj.func2()
    obj.mul(9,3)
    