class A:
    def show(self):
        print("AAAAAA")



class B(A):
     def show(self):
        print("BBBBB")
        return A.show(self)

class D(A):
     def show(self):
        print("DDDD")

class C(B,D):
     def show(self):
        print("CCCCC")

c=C()
d=D()
c.show()
super(C,c).show()
d.show()
