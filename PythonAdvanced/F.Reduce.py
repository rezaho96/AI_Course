from functools import reduce

def add(x,y):
    return x+y

def mul(x,y):
    return x*y
list1=[2,5,8,14,65,12,10]
print(reduce(add,list1))
print(reduce(mul,list1))
print(reduce(lambda x,y:x+y,list1))
print(reduce(lambda x,y:x*y,list1))
print(reduce(lambda x,y:x-y,list1))