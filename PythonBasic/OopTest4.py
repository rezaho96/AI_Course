#polymorphism
# چند ریختی : وقتی تابعی با یک اسم داشته باشیم که آن را به شکل های مختلف در برنامه استفاده کنیم
class Person:
    def __init__(self,name,family,age):
        self.name=name
        self.family=family
        self.age=age
    
    def show(self):
        print("person....")

class Student(Person):
    def __init__(self,idStudent,name,family,age) :
        Person.__init__(self,name,family,age)
        self.idstudent=idStudent
    
    def show(self):
        print("student....")

#/////////////////////////////////////////////////////////
s1=Student(25,"reza","hoseini",23)
s1.show()


#/////////////////////////////////////
def sum(a,b,c=0):
    return a+b+c
print(sum(2,5,6))
print(sum(5,6))
