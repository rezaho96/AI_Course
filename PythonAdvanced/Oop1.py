class Person:
    count=0
    def __init__(self, name, age):
      self.name = name
      self.age = age
      Person.count+=1

    def __str__(self):
       return f"{self.name}+\t+{self.age}"

    def __del__(self):
        print(f"{self.name}\t the end...")
# print(Person.count)
# person1=Person("reza",22)
# person2=Person("sajad",32)
# print(Person.count)
# del(person1)

person1=Person("reza",22)
person2=Person("sajad",32)
print(person1.count)
print(person2.count)
print(Person.count)

person1.count=50
print("........................................................")
print(person1.count)
print(person2.count)
print(Person.count)


Person.count=100
print("........................................................")
print(person1.count)
print(person2.count)
print(Person.count)