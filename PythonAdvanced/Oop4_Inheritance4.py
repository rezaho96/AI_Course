class A:
    def __init__(self):
        print("run init of class A")

    def showA(self):
        print("AAAAAA")



class B(A):
     def __init__(self):
        A.__init__(self)
        print("run init of class B")
     def showB(self):
        print("BBBBB")

class D(A):
     def __init__(self):
        A.__init__(self)
        print("run init of class D")
     def showD(self):
        print("DDDD")
d=D()
d.showA()
d.showD()
b=B()
b.showA()
b.showB()