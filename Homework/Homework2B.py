
class Person:
    def __init__(self, name, family):
      self.__name = self.__toPascalCase(name)
      self.__family=self.__toPascalCase(family)

    def __toPascalCase(self,str1):
        liststr=list(str1)
        liststr[0]=chr(ord(liststr[0])-32)
        return ''.join(liststr)
    def _show(self):
        return f"Name: {self.__name}\tFamily: {self.__family}"
    def setName(self,Name):
        self.__name=Name

    def setFamily(self,Family):
         self.__family=Family

class Manager(Person):
    n_manager=0
    def __init__(self, name, family , personalCode, salary ):
      Person.__init__(self,name,family)
      Manager.n_manager+=1

      self.__personalCode=personalCode
      self.__salary=salary
    def show(self):
        print(f"{self._show()}\tPersonalCode: {self.__personalCode}\tSalary: {self.__salary}")
class Employee(Person):
    n_employee=0
    def __init__(self, name, family  , personalCode , rank):
      super().__init__(name,family)
      Employee.n_employee+=1

      self.__personalCode=personalCode
      self.__rank=self.__rankStr(rank)
    def __rankStr(self,rank1):
        match rank1:
            case 1:
                return "A"
            case 2:
                return "B"
            case 3:
                return "C"
            case 4:
                return "D"
            case _: 
                return rank1
    def show(self):
        print(f"{self._show()}\tPersonalCode: {self.__personalCode}\tRank: {self.__rank}")


class Intern(Person):
    
    n_intern=0
    def __init__(self, name, family , period=12):
      super().__init__(name,family)
      Intern.n_intern+=1
      self.__period=period
    def show(self):
        print(f"{self._show()}\tDuration of internship: {self.__period}")
manager1=Manager("ali","hoseini",256,6500)
manager2=Manager("vahid","moradi",232,6800)
employee1=Employee("neda","soltani",321,"A")
employee2=Employee("daryoosh","ezedi",126,1)
employee3= Employee("sadegh","godarzi",210,3)
intern1=Intern("reza","karimi")  
list1=[manager1,manager2,employee1,employee2,employee3,intern1]
manager1.setFamily("saravi")
for item in list1:
    item.show()
print(f'''Number of intern: {Intern.n_intern}\nNumber of employee:{Employee.n_employee}\nNumber of manager: {Manager.n_manager}''')
    
