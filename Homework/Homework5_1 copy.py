class My_Exception_Handling(Exception):
    def __init__(self, massage):
        self.massage=massage
        
    def __str__(self):
        return self.massage
    
#////////////////////////////////
class Player_Selection:
    def __init__(self, personalCode, height, age, weight):
        self.__personalCode=personalCode
        self.__height=height
        self.__age=age
        self.__weight=weight
    
    def weight_validation(self):
        Player_Selection.check_float(self.__weight,self.__height)
        Player_Selection.check_integer(self.__age)
        if 15 <= int(self.__age) <=25 and not 60 <= float(self.__weight) <= 80:
            raise My_Exception_Handling("Weight out of range \nThis person is not allowed to register")
    
        elif 25 < int(self.__age) <=35 and not 50 <= float(self.__weight) <= 75:
            raise My_Exception_Handling("Weight out of range \nThis person is not allowed to register")
    
        elif 35 < int(self.__age) or int(self.__age) <15 :
            raise My_Exception_Handling("Age out of range \nThis person is not allowed to register")
        
    def height_validation(self):
        if 15 <= int(self.__age) <= 35 and not 170 <= float(self.__height) <= 190:
            raise My_Exception_Handling("Height out of range \nThis person is not allowed to register")
        elif 35 < int(self.__age) or int(self.__age) <15 :
            raise My_Exception_Handling("Age out of range \nThis person is not allowed to register")
        
    def register_player(self):
        try:
            self.weight_validation()
            self.height_validation()
            return True
        except My_Exception_Handling as error:
            print(error)
    
    def showInfo(self):
        return f"Personal code is:{self.__personalCode} / Age is:{int(self.__age)} / Weight is:{float(self.__weight)} / Weight is:{float(self.__height)}"
    @staticmethod
    def check_integer(age):
        # a=0
        # for i in age:
        #     if not 48<= ord(i) <= 57:
        #         a+=1
        # if a>0:
        #     raise My_Exception_Handling("Age is not valid")
        try:
            int(age)
        except ValueError:
            raise My_Exception_Handling("Age is not valid")
    @staticmethod
    def check_float(weight,height):
        # w=0
        # for i in weight:
        #     if not 48<= ord(i) <= 57 and not ord(i)==46:
        #         w+=1
        # if w>0:
        #     raise My_Exception_Handling("Weight is not valid")
        # h=0
        # for i in height:
        #     if not 48<= ord(i) <= 57 and not ord(i)==46:
        #         h+=1
        # if h>0:
        #     raise My_Exception_Handling("Height is not valid")
        try:
            float(height)
        except ValueError:
            raise My_Exception_Handling("Height is not valid")
        try:
            float(weight)
        except ValueError:
            raise My_Exception_Handling("Weight is not valid")

#.................................
list1=[]
while (1):
    personalCode=input("Enter personal code :")
    age=input("Enter age :")
    weight=input("Enter weight :")
    height=input("Enter height :")
    player1=Player_Selection(personalCode,height,age,weight)
    
    if player1.register_player() :
       list1.append(player1.showInfo())
    print(list1)
    close_program=input("Enter zero and press enter to end the program:")
    if close_program =="0":
        break
    
    
    
    