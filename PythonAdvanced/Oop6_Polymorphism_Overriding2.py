class A:
    def show(self):
        print("AAAAAA")



class B(A):
     def show(self):
        print("BBBBB")
        return A.show(self)

# a=A()
# b=B()
# a.show()
# b.show()
# super(B,b).show()
a=A()
b=B()
b.show()
