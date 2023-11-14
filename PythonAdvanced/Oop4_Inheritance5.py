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

class C(B,D):
     def __init__(self):
        B.__init__(self)
        D.__init__(self)
        print("run init of class C")
     def showC(self):
        print("CCCCC")
c=C()
c.showA()
c.showB()
c.showC()
c.showD()