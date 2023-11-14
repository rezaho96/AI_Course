from abc import ABC,abstractmethod
class Person(ABC):
    def __init__(self, name, age):
      self._name = name
      self._age = age
    @abstractmethod
    def showInfo(self):
        pass


class Student(Person):
    def __init__(self, name, age ,studentId):
      super().__init__(name, age)
      self.__studentId=studentId
    
    def showInfo(self):
       return f"{self._name}\t\t{self._age}\t\t{self.__studentId}"
class Teacher(Person):
    def __init__(self, name, age ,teacherCode):
      super().__init__(name,age)
      self.__teacherCode=teacherCode
    
    def showInfo(self):
       return f"Name :{self._name}\t\tAge:{self._age}\t\tCode :{self.__teacherCode}"
t1=Teacher("reza",25,66)
s1=Student("jac",20,15)
print(t1.showInfo())
print(s1.showInfo())
