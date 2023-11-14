class Person:
    def __init__(self, name, age):
      self.name = name
      self.age = age
    
    def showPersonInfo(self):
        print(f"{self.name}\t{self.age}")
    
    
    @staticmethod
    def sum(x,y):
        return x+y
    
    @classmethod
    def func1(cls,a,b):
        return cls.sum(a,b)//5

person1=Person("ali",26)
person1.showPersonInfo()
print(Person.sum(20,30))
print(Person.func1(10,5))