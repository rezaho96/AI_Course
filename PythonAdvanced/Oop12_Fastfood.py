from abc import ABC, abstractmethod
import enum


class Order:
    def __init__(self,delivery,intance=1):
       self.delivery=delivery
       self.itemPack=[]
       self.intance=intance
    def addItem(self,item):
        self.itemPack.append(item)
    def totalPrice(self):
        sumPrice=self.delivery*self.intance
        for item in self.itemPack:
            sumPrice+=item.itemPrice()
        return sumPrice 
#------------------------------------------
class Delivery(enum.Enum):
    bycicle=2000
    motorcycle=10000
    airplane=80000
#------------------------------------------
class Item(ABC):

    @abstractmethod
    def itemPrice(self):
        pass
#----------------------------------------
class Drink(Item):
    def __init__(self,cc , carbonated):
        super().__init__()
        self.carbonated=carbonated
        self.cc=cc

    def itemPrice(self):
        if self.carbonated:
           return self.cc*20+4000
        else:
           return self.cc*20
#-----------------------------------------

class Pizza(Item):
    def __init__(self,size):
        super().__init__()
        self.size=size
        self.unitPrice=10000
        self.contentPack=[]
    def addContent(self,content):
        self.contentPack.append(content)

    def itemPrice(self):
        sum=self.unitPrice
        for content in self.contentPack:
            sum+=content.contentPrice()
        
        return sum*self.size
#-----------------------------------------
class Size(enum.Enum):
    min=1
    medium=2
    large=5
#-----------------------------------------
class Content(ABC):

    @abstractmethod
    def contentPrice(self):
        pass

#-----------------------------------------
class Tomato(Content):
    def __init__(self,wieght):
        super().__init__()
        if wieght>0.2:
            wieght=0.2
        self.wight=wieght
    
    def contentPrice(self):
        return self.wight*8000
#-----------------------------------------
class Chicken(Content):
    def __init__(self,wieght):
        super().__init__()
        if wieght>0.15:
            wieght=0.15
        self.wight=wieght
    
    def contentPrice(self):
        return self.wight*45000
#-----------------------------------------
class Chickenham(Content):
    def __init__(self,wieght):
        super().__init__()
        if wieght>0.15:
            wieght=0.15
        self.wight=wieght
    
    def contentPrice(self):
        return self.wight*120000
#-----------------------------------------
class Redmeat(Content):
    def __init__(self,wieght):
        super().__init__()
        if wieght>0.15:
            wieght=0.15
        self.wight=wieght
    
    def contentPrice(self):
        return self.wight*200000
#-----------------------------------------
class Cheese(Content):
    def __init__(self,wieght):
        super().__init__()
        if wieght>0.1:
            wieght=0.1
        self.wight=wieght
    
    def contentPrice(self):
        return self.wight*180000
#-----------------------------------------
class Mushroom(Content):
    def __init__(self,wieght,canned):
        super().__init__()
        if wieght>0.2:
            wieght=0.2
        self.wight=wieght
        self.canned=canned
    def contentPrice(self):
        if self.canned:
            return self.wight*30000
        else:
            return self.wight*30000*2


p1=Pizza(Size.large.value)
p1.addContent(Mushroom(.3,True))
p1.addContent(Cheese(.1))
p1.addContent(Redmeat(.03))
p1.addContent(Chicken(.01))
p1.addContent(Chickenham(.01))
print(p1.itemPrice())
d1=Drink(10,True)
d2=Drink(30,False)
print(d1.itemPrice())
o1=Order(Delivery.bycicle.value,10)
o1.addItem(p1)
o1.addItem(d1)
o1.addItem(d2)
print(o1.totalPrice())


      