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

class D(B):
     def __init__(self):
        B.__init__(self)
        print("run init of class D")
     def showD(self):
        print("DDDD")
d=D()
d.showA()
d.showB()
d.showD()