class A:
    def show(self):
        print("AAAAAA")



class B:
     def show(self):
        print("BBBBB")

class D(B,A):
     def show(self):
        print("DDDD")
        A.show(self)

d=D()
d.show()
super(D,d).show()
