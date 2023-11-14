
class Person :
    def __init__(self , customerCode , name , lastName , phoneNumber , emailAddress):
        self.__customerCode=customerCode
        self.__name=name
        self.__lastName=lastName
        self.__phoneNumber=phoneNumber
        self.__emailAddress=emailAddress
        self._dicPerson={"customerCode":self.__customerCode,"name":self.__name,"lastName":self.__lastName,
        "phoneNumber":self.__phoneNumber,"emailAddress":self.__emailAddress}

    def showInfo(self):
        print(self._dicPerson)

#/////////////////////////
class Address:
    def __init__(self,cityName , plaque , streetName):
        self.__cityName=cityName
        self.__plaque=plaque
        self.__streetName=streetName
        self._dicAddress={"cityName":self.__cityName,"plaque":self.__plaque,"streetName":self.__streetName}

    def showInfo(self):
        print(self._dicAddress)

#/////////////////////////

class Contact(Person,Address):
    def __init__(self, customerCode , name , lastName , phoneNumber , emailAddress ,cityName
     , plaque , streetName):
       Person.__init__(self, customerCode , name , lastName , phoneNumber , emailAddress)
       Address.__init__(self,cityName , plaque , streetName)

       #merge tow dictionary
       self._dicPerson.update(self._dicAddress)
       self.dicContact=self._dicPerson

    def showInfo(self):
        print(self.dicContact)
#/////////////////////////
class PhoneBook:
    def __init__(self):
        self.phoneNumberList=[]

    def add_contact(self,contact):
        self.phoneNumberList.append(contact.dicContact)

    def search_customer(self,lastNameSearch):
        flag=True
        for dict in self.phoneNumberList:
            if dict["lastName"]==lastNameSearch:
                contactSearched=Contact(dict["customerCode"],dict["name"],dict["lastName"],dict["phoneNumber"]
                ,dict["emailAddress"],dict["cityName"],dict["customerCode"],dict["streetName"])
                contactSearched.showInfo()
                flag=False
            
        if flag:
            print("Unknown customer")
    def showInfo(self):
        print(self.phoneNumberList)


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

c1=Contact(124,"ali","saeidi",91865404,"ali@gmail.com","shiraz",22,"shoshtari")
c2=Contact(214,"daryoosh","karimi",9165487,"saryoosh01@gmail.com","hamedan",44,"bahonar")
c3=Contact(564,"davood","ahmadi",9132536,"d.ahmadi@gmail.com","kerman",12,"shakori")
c4=Contact(312,"ahmad","ghafari",9784585,"ahm@email.com","yasoj",11,"jamali")
c5=Contact(125,"mohamad","atashi",9321458,"m.a@gmail.com","shosh",54,"razavi")
c6=Contact(396,"sajad","shokati",6945876,"sajads@gmail.com","mashhad",34,"tahami")
c7=Contact(201,"reza","hoseini",54789621,"hosein96@gmail.com","sabzavar",18,"shokohi")
c8=Contact(784,"hamid","samadi",12543652,"hamid47@gmail.com","tehran",12,"afsareye")
c9=Contact(328,"jamal","jamali",85742587,"jamal@gmail.com","esfehan",56,"zahraei")
c10=Contact(639,"mahvash","kazemi",9782503,"mahvashkkk@gmail.com","oromye",10,"shahreyari")
#............
p1=PhoneBook()
p1.add_contact(c1)
p1.add_contact(c2)
p1.add_contact(c3)
p1.add_contact(c4)
p1.add_contact(c5)
p1.add_contact(c6)
p1.add_contact(c7)
p1.add_contact(c8)
p1.add_contact(c9)
p1.add_contact(c10)
p1.showInfo()
#For example, available
p1.search_customer("jamali")
#For example, not available
print("...................")
p1.search_customer("rahimi")





