# def func():
#     x=20
#     yield x
#     yield x+10
#     yield x*2

# g1=func()
# print(next(g1))
# print(next(g1))
# print(next(g1))


# def func():
#     x=20
#     x=yield x
#     x=yield x+10
#     yield x*2

# g1=func()
# print(next(g1))
# print(g1.send(26))
# print(g1.send(66))


# def fun1():
#     while True:
#         x=yield 500
#         yield x*2
# g=fun1()
# print(next(g))
# print(g.send(5))
# print(g.send(10))
# print(g.send(10))


import random
def fun1():
    while True:
        x=yield
        print(x,end="\t")
        
def fun2(fun):
    while True:
        r=random.randint(0,100)
        fun.send(r)
        yield
g1=fun1()
g1.send(None)

g2=fun2(g1)
next(g2)
next(g2)