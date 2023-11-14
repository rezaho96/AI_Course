from mimetypes import init


class Person:
    x=None#انکپسوله نیست-همه فرزندان و نمونه ها به آن دسترسی دارند
    _y=None#فقط کلاس های فرزند به آن دسترسی دارند
    __z=None#فقط خود کلاس به آن دسترسی دارد
    def __init__(self, name, family , id):
      self.__name = self.__toPascalCase(name)
      self.__family=self.__toPascalCase(family)
      self.__id=id

    def __toPascalCase(self,str1):
        liststr=list(str1)
        liststr[0]=chr(ord(liststr[0])-32)
        return ''.join(liststr)

    def _showPersonInfo(self):
        return "Name:" + self.__name +"\tFamily: " + self.__family + "\tId: " + str(self.__id)

    def _fullNameLenght(self):
        return len(self.__name)+len(self.__family)

class Student(Person):
    def __init__(self, name, family , id , studentId):
        super().__init__(name,family,id)
        self.__studentId=studentId

    def showStudentInfo(self):
        print(self._showPersonInfo() +"\tStudentId: " + str(self.__studentId))
        print(f"FullNameLenght: {self._fullNameLenght()}") 

class Teacher(Person):
    def __init__(self, name, family , id , teacherCode):
        super().__init__(name,family,id)
        self.__teacherCode=teacherCode

    def showTeacherInfo(self):
        print(f"TeacherCode: {self.__teacherCode} \nFullNameLenght: {self._fullNameLenght()}")

person1=Person("saeid","sadeghi",98)
student1=Student("reza","hoseini",32,41)
teacher1=Teacher("mehdi","abasi",31,147)


print(person1.x)
student1.showStudentInfo()
teacher1.showTeacherInfo()


        

