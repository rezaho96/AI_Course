import operator
print(dir(operator))
print(operator.add(6,5))
print(operator.mul(6,5))
print(operator.sub(4,5))
print(operator.mod(20,5))
print(operator.truediv(21,5))
print(operator.floordiv(21,5))

print("******************************")
print(operator.eq(21,5))
print(operator.lt(21,5))
print(operator.le(21,5))
print(operator.gt(21,21))
print(operator.ge(21,5))

print("******************************")
print(operator.not_(21>5))
print(operator.not_(False))

print("******************************")

print(operator.lshift(17,1))
print(operator.rshift(17,1))


print("******************************")

print(operator.contains("ali is good boy","a"))
print(operator.contains(str(2450),"4"))

print("******************************")
list1=[5,6,4,5,1]
operator.delitem(list1,3)
print(list1)
print(operator.countOf(list1,5))

print("******************************")
print(operator.itemgetter(2)(list1))
print("******************************")

list2=[("ali","ahmadi",23),("hesam","hoseini",33),("jalal","hashemi",12)]
print(sorted(list2,key=operator.itemgetter(2)))