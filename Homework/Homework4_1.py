class Student :
    level_of_education="Elementary school"
    def __init__(self,idStudent,name,family,grade):
        self.__idStudent=idStudent
        self.__name=name
        self.__family=family
        self.__grade=grade
    def __eq__(self,obj2):
        if not isinstance(obj2,Student):
            return False
        return self.__idStudent==obj2.__idStudent and self.__name==obj2.__name and self.__family==obj2.__family and self.__grade==obj2.__grade
    def __hash__(self):
        return hash(self.__idStudent)+hash(self.__name)+hash(self.__family)+hash(self.__grade)
    
    @staticmethod
    def showLessonsElementary(grade):
        match grade:
            case 1: return f"first grade : farsi ryazi negaresh oloom" 
            case 2: return f"second grade : farsi ryazi ghoraan hedyeAsmani" 
            case 3: return f"third grade : farsi ryazi negaresh hedyeAsmani" 
            case 4: return f"fourth grade : farsi ryazi negaresh ejtemaei hedyeAsmani oloom " 
            case 5: return f"fifth grade : farsi ryazi negaresh ejtemaei hedyeAsmani oloom " 
            case 6: return f"sixth grade : farsi ryazi negaresh ejtemaei hedyeAsmani oloom karofanavari tafkoropashohesh " 
    @classmethod
    def change_level_of_education(cls , level):
        cls.level_of_education=level
    
    def showInfo(self):
        print(f"idStudent is : {self.__idStudent} \t name is: {self.__name} \t family is : {self.__family} \t grade is : {self.__grade} \t level of education is : {student.level_of_education}")

# ---------------main----------------
student1=Student(332102,"ali","hasani",3)
student2=Student(225896,"reza","vahedi",2)
student3=Student(289631,"saeid","nariman",2)
student4=Student(257885,"mina","mohamadi",2)
student5=Student(489134,"masoud","ahmadi",4)
student6=Student(412054,"dvood","nakisa",4)
student7=Student(589431,"karim","shabani",5)
student8=Student(648721,"kamran","homayi",6)
student9=Student(664852,"mahpari","hoseini",6)
student10=Student(198769,"horeye","shamsayi",1)
set_student={student1,student2,student3,student4,student5,student6,student7,student8,student9,student10}
for student in set_student:
    student.showInfo()
    print()

#__eq__ method
print(student1==student2)

#static method
print(Student.showLessonsElementary(1))

#class method
Student.change_level_of_education("High school")
print(Student.level_of_education)        