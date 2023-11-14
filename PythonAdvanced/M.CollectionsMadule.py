import collections

print(dir(collections))

print("***************************")

print(collections.Counter("lkdfjslkajfjkfjk"))
print(collections.Counter([4,5,6,4,58,7,8,54,21,4,5,6,5,8,7]))
c=collections.Counter([4,5,6,4,58,7,8,54,21,4,5,6,5,8,7])
print(c.most_common(2))

print("******************************")

# dict1={}
# print(dict1["Red"])

# dic2=collections.defaultdict(object)
# print(dic2["Red"])


print("******************************")

dic1=collections.OrderedDict()
dic1["h"]="hamed"
dic1["n"]="negin"
dic1["m"]="mahdi"
dic1["s"]="samad"

dic2=collections.OrderedDict()
dic2["n"]="negin"
dic2["m"]="mahdi"
dic2["h"]="hamed"
dic2["s"]="samad"

for k,v in dic1.items():
    print(f"{k} : {v}")
print()
for k,v in dic2.items():
    print(f"{k} : {v}")

print(dic1==dic2)


print("*******************************")

d1={3:"three",2:"tow",1:"one"}
d2={"three":3,"tow":2,"one":1}
d3={"ali":55,"hasan":21}
d4=collections.ChainMap(d1,d2,d3,d1)
print(d4)


print("*******************************")

Person=collections.namedtuple("Person","name age avg childern")
person1=Person("ali",22,12.5,["ahmad","hamed"])
print(person1)
print(person1.age)
print(person1.avg)
print(person1.childern)
print(person1.name)
person1.childern.append("mahmood")
print(person1.childern)

for item in Person._make(person1):
    print(item)
    
print(Person._make(person1))
print(person1._asdict())
print(person1._fields)

print("*******************************")

deque1=collections.deque([1,2,3])
print(deque1)
deque1.append(5)
deque1.appendleft(5)
print(deque1)
print(type(deque1))
deque1.pop()
deque1.popleft()
print(deque1)


print("*******************************")

class Mylist(collections.UserList):
    def remove(self):
        raise RuntimeError("Delete not alowed")
list1=Mylist[1,2,3,5]

try:
    list1.remove(2)
    print(list1)
except RuntimeError as error:
    print(error)
    
class Mystring(collections.UserString):
    def remove(self,s):
        self.data=self.data.replace(s, "")
str1=Mystring("sjfdljdg")
str1.remove("f")
print(str1)


