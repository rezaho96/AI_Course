#وراثت :وقتی که چند کلاس داشته باشیم که دارای ویژگی ها و توابع یکسان باشند یک کلاس پدر تعریف می شود که inheritance
#شامل این ویژگی ها و توابع باشد و بقیه کلاس ها به عنوان کلاس فرزند تعریف می شوند  
#در اینشیال کلاس فرزند باید اینشیال کلاس پدر فراخوانی شود به واسطه تابع سوپر

class Person:
    def __init__(self,name,family,age):
        self.name=name
        self.family=family
        self.age=age
    
    def showInfo(self):
        print(self)

class Student(Person):
    def __init__(self,idStudent,name,family,age) :
        super().__init__(name,family,age)
        self.idstudent=idStudent
    def __str__(self):
        return str(self.idstudent)+" "+self.name+" "+self.family+" "+str(self.age)

class Teacher(Person):
    def __init__(self,teacherCode,name,family,age) :
        super().__init__(name,family,age)
        self.teacherCode=teacherCode
    def __str__(self):
        return str(self.teacherCode)+" "+self.name+" "+self.family+" "+str(self.age)

class Employee(Person):
    def __init__(self,employeeCode,name,family,age) :
        super().__init__(name,family,age)
        self.employeeCode=employeeCode
    def __str__(self):
        return str(self.iemployeeCode)+" "+self.name+" "+self.family+" "+str(self.age)

#-------------------------------------------------------------------

st1=Student(96,"reza","hoseini",20)
th1=Teacher(85,"hamid","marateb",55)
em1=Employee(23,"saeid","karimi",36)
st1.showInfo()
print(th1)
