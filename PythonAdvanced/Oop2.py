class Person:
    id=None
    _name=None
    __family=None

    def __init__(self,id, name,family):
       self.id=id
       self._name = name
       self.__family=family

    def __str__(self):
       return str(self.id)
    
    def getFamily(self):
        return self.__family
    
    def setFamily(self,newFamily):
        self.__family=newFamily
    
    def _showPersonInfo(self):
        return "\t"+str(self.id)+"\t"+self._name+"\t"+self.__family

class Student(Person):
    __studentId=None
    def __init__(self,studentId,id,name,family):
        super().__init__(id,name,family)
        self.__studentId=studentId
    
    def showStudentInfo(self):
        return str(self.__studentId)+self._showPersonInfo()


person1=Person(25,"saeid","soheili")
student1=Student(9620,26,"reza","hoseini")
print(person1.getFamily())
person1.setFamily("vahid")
print(person1.getFamily())
print(person1)
print(person1._showPersonInfo())
print(student1.showStudentInfo())
    

