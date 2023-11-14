class Person:
    def __init__(self, name, age):
      self.__name = name
      self.__age = age
    

    def __eq__(self,obj2):
        if  not isinstance(obj2,Person):
            return False
        return self.__name==obj2.__name and self.__age==obj2.__age
class Student:
    def __init__(self, name, age):
      self.__name = name
      self.__age = age
    

    def __eq__(self,obj2):
        if  not isinstance(obj2,Student):
            return False
        return self.__name==obj2.__name and self.__age==obj2.__age

person1=Person("ali",12)
person2=Person("hasan",12)
person3=Person("ali",12)
student1=Student("ali",12)
print(person1.__eq__(person3))
print(person1.__eq__(person2))
print(person1.__eq__(student1))
print(person1==student1)