import demjson

class Person:
    def __init__(self, name, age):
      self.name = name
      self.age = age
    
    def __str__(self) -> str:
       return f"name:{self.name},age:{self.age}"
person1=Person("ali",22)
person2=Person("hasan",25)
person3=Person("mahvash",35)
list1=[person1.__dict__,person2.__dict__,person3.__dict__]
jstr=demjson.encode(list1)
print(jstr)
print(type(jstr))


obj1=demjson.decode(jstr)
for i in obj1:
    print(i)