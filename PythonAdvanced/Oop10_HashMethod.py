class Person:
    def __init__(self, name, age):
      self.__name = name
      self.__age = age
    # def __eq__(self,obj2):
    #     if  not isinstance(obj2,Person):
    #         return False
    #     return self.__name==obj2.__name and self.__age==obj2.__age
    # def __hash__(self) -> int:
    #    return hash(self.__name)+hash(self.__age)
    def __sum__(self,obj2):
        return self.__age+obj2.__age
    def __str__(self) -> str:
       return  f"Name is :{self.__name}\tAge is :{self.__age}"

person1=Person("ali",12)
person2=Person("hasan",23)
person3=Person("ali",12)
print(hash(person1))
print(hash(person2))
set1={person1,person2,person3}
for obj1 in set1:
    print(obj1)
print(len(set1))