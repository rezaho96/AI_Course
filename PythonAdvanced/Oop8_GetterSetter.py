class Person:
    def __init__(self, name, age):
      self.__name = name
      self.__age = age

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name=name
    # def getName(self):
    #     return self.__name
    # def setName(self,name):
    #     self.__name=name

person1=Person("abolfazl",23)
print(person1.name)
person1.name="ali"
print(person1.name)