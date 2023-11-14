class A:
    def __init__(self):
        print("run init of class A")

    def showA(self):
        print("AAAAAA")



class B(A):
     def __init__(self):
        super().__init__()
        print("run init of class B")
     def showB(self):
        print("BBBBB")


b=B()
b.showA()
b.showB()